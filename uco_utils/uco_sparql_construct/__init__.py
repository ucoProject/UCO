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
This script executes a SPARQL CONSTRUCT query, returning a graph of the generated triples.
"""

__version__ = "0.2.2"

import argparse
import logging
import os
import sys
import typing

import rdflib.plugins.sparql  # type: ignore

import uco_utils.ontology
from uco_utils.ontology.version_info import (
    CURRENT_UCO_VERSION,
    built_version_choices_list,
)

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
        "--output-format", help="Override extension-based format guesser."
    )
    parser.add_argument("out_graph")
    parser.add_argument(
        "in_sparql",
        help="File containing a SPARQL CONSTRUCT query.  Note that prefixes not mapped with a PREFIX statement will be mapped according to their first occurrence among input graphs.",
    )
    parser.add_argument("in_graph", nargs="+")
    args = parser.parse_args()

    in_graph = rdflib.Graph()
    for in_graph_filename in args.in_graph:
        in_graph.parse(in_graph_filename)
        _logger.debug("len(in_graph) = %d.", len(in_graph))

    out_graph = rdflib.Graph()

    # Inherit prefixes defined in input context dictionary.
    nsdict = {k: v for (k, v) in in_graph.namespace_manager.namespaces()}
    for prefix in sorted(nsdict.keys()):
        out_graph.bind(prefix, nsdict[prefix])

    _logger.debug("Running query in %r." % args.in_sparql)
    construct_query_text = None
    with open(args.in_sparql, "r") as in_fh:
        construct_query_text = in_fh.read().strip()
    assert construct_query_text is not None

    if "subClassOf" in construct_query_text:
        uco_utils.ontology.load_subclass_hierarchy(
            in_graph, built_version=args.built_version
        )

    construct_query_object = rdflib.plugins.sparql.prepareQuery(
        construct_query_text, initNs=nsdict
    )

    # https://rdfextras.readthedocs.io/en/latest/working_with.html
    construct_query_result = in_graph.query(construct_query_object)
    _logger.debug("type(construct_query_result) = %r." % type(construct_query_result))
    _logger.debug("len(construct_query_result) = %d." % len(construct_query_result))
    for (row_no, row) in enumerate(construct_query_result):
        if row_no == 0:
            _logger.debug("row[0] = %r." % (row,))
        out_graph.add(row)

    output_format = None
    if args.output_format is None:
        output_format = rdflib.util.guess_format(args.out_graph)
    else:
        output_format = args.output_format

    serialize_kwargs: typing.Dict[str, typing.Any] = {"format": output_format}
    if output_format == "json-ld":
        context_dictionary = {
            k: v for (k, v) in out_graph.namespace_manager.namespaces()
        }
        serialize_kwargs["context"] = context_dictionary

    out_graph.serialize(args.out_graph, **serialize_kwargs)


if __name__ == "__main__":
    main()
