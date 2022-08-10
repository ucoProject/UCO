#!/usr/bin/env python3

# This software was developed at the National Institute of Standards
# and Technology by employees of the Federal Government in the course
# of their official duties. Pursuant to title 17 Section 105 of the
# United States Code this software is not subject to copyright
# protection and is in the public domain. NIST assumes no
# responsibility whatsoever for its use by other parties, and makes
# no guarantees, expressed or implied, about its quality,
# reliability, or any other characteristic.
#
# We would appreciate acknowledgement if the software is used.

"""
This script executes a SPARQL SELECT query, returning a table representation.  The design of the workflow is based on this example built on SPARQLWrapper:
https://lawlesst.github.io/notebook/sparql-dataframe.html

Note that this assumes a limited syntax style in the outer SELECT clause of the query - only named variables, no aggregations, and a single space character separating all variable names.  E.g.:

SELECT ?x ?y ?z
WHERE
{ ... }

The word "DISTINCT" will also be cut from the query, if present.

Should a more complex query be necessary, an outer, wrapping SELECT query would let this script continue to function.
"""

__version__ = "0.4.2"

import argparse
import binascii
import logging
import os
import sys

import pandas as pd  # type: ignore
import rdflib.plugins.sparql  # type: ignore

import uco_utils.ontology
from uco_utils.ontology.version_info import (
    CURRENT_UCO_VERSION,
    built_version_choices_list,
)

NS_XSD = rdflib.XSD

_logger = logging.getLogger(os.path.basename(__file__))


def main() -> None:
    parser = argparse.ArgumentParser()

    # Configure debug logging before running parse_args, because there could be an error raised before the construction of the argument parser.
    logging.basicConfig(
        level=logging.DEBUG
        if ("--debug" in sys.argv or "-d" in sys.argv)
        else logging.INFO
    )

    parser.add_argument("-d", "--debug", action="store_true")
    parser.add_argument(
        "--built-version",
        choices=tuple(built_version_choices_list),
        default="uco-" + CURRENT_UCO_VERSION,
        help="Ontology version to use to supplement query, such as for subclass querying.  Does not require networking to use.  Default is most recent UCO release.",
    )
    parser.add_argument(
        "--disallow-empty-results",
        action="store_true",
        help="Raise error if no results are returned for query.",
    )
    parser.add_argument(
        "out_table",
        help="Expected extensions are .html for HTML tables or .md for Markdown tables.",
    )
    parser.add_argument(
        "in_sparql",
        help="File containing a SPARQL SELECT query.  Note that prefixes not mapped with a PREFIX statement will be mapped according to their first occurrence among input graphs.",
    )
    parser.add_argument("in_graph", nargs="+")
    args = parser.parse_args()

    graph = rdflib.Graph()
    for in_graph_filename in args.in_graph:
        graph.parse(in_graph_filename)

    # Inherit prefixes defined in input context dictionary.
    nsdict = {k: v for (k, v) in graph.namespace_manager.namespaces()}

    select_query_text = None
    with open(args.in_sparql, "r") as in_fh:
        select_query_text = in_fh.read().strip()
    _logger.debug("select_query_text = %r." % select_query_text)

    if "subClassOf" in select_query_text:
        uco_utils.ontology.load_subclass_hierarchy(
            graph, built_version=args.built_version
        )

    # Build columns list from SELECT line.
    select_query_text_lines = select_query_text.split("\n")
    select_line = [
        line for line in select_query_text_lines if line.startswith("SELECT ")
    ][0]
    variables = select_line.replace(" DISTINCT", "").replace("SELECT ", "").split(" ")

    tally = 0
    records = []
    select_query_object = rdflib.plugins.sparql.prepareQuery(
        select_query_text, initNs=nsdict
    )
    for (row_no, row) in enumerate(graph.query(select_query_object)):
        tally = row_no + 1
        record = []
        for (column_no, column) in enumerate(row):
            if column is None:
                column_value = ""
            elif (
                isinstance(column, rdflib.term.Literal)
                and column.datatype == NS_XSD.hexBinary
            ):
                # Use hexlify to convert xsd:hexBinary to ASCII.
                # The render to ASCII is in support of this script rendering results for website viewing.
                # .decode() is because hexlify returns bytes.
                column_value = binascii.hexlify(column.toPython()).decode()
            else:
                column_value = column.toPython()
            if row_no == 0:
                _logger.debug("row[0]column[%d] = %r." % (column_no, column_value))
            record.append(column_value)
        records.append(record)
    if tally == 0:
        if args.disallow_empty_results:
            raise ValueError("Failed to return any results.")

    df = pd.DataFrame(records, columns=variables)

    table_text = None
    if args.out_table.endswith(".html"):
        # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_html.html
        # Add CSS classes for UCO website Bootstrap support.
        table_text = df.to_html(classes=("table", "table-bordered", "table-condensed"))
    elif args.out_table.endswith(".md"):
        # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_markdown.html
        # https://pypi.org/project/tabulate/
        # Assume Github-flavored Markdown.
        table_text = df.to_markdown(tablefmt="github")
    if table_text is None:
        raise NotImplementedError(
            "Unsupported output extension for output filename %r.", args.out_table
        )

    with open(args.out_table, "w") as out_fh:
        out_fh.write(table_text)


if __name__ == "__main__":
    main()
