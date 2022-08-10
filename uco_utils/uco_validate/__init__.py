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
This script provides a wrapper to the pySHACL command line tool,
available here:
https://github.com/RDFLib/pySHACL

Portions of the pySHACL command line interface are preserved and passed
through to the underlying pySHACL validation functionality.

Other portions of the pySHACL command line interface are adapted to
UCO, specifically to support CASE and UCO as ontologies that store
subclass hierarchy and node shapes together (rather than as separate
ontology and shape graphs).  More specifically to UCO, if no particular
ontology or shapes graph is requested, the most recent version of UCO
will be used.  (That most recent version is shipped with this package as
a monolithic file; see uco_utils.ontology if interested in further
details.)
"""

__version__ = "0.1.2"

import argparse
import importlib.resources
import logging
import os
import sys
import typing

import pyshacl  # type: ignore
import rdflib.util  # type: ignore

import uco_utils.ontology
from uco_utils.ontology.version_info import (
    CURRENT_UCO_VERSION,
    built_version_choices_list,
)

_logger = logging.getLogger(os.path.basename(__file__))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="UCO wrapper to pySHACL command line tool."
    )

    # Configure debug logging before running parse_args, because there
    # could be an error raised before the construction of the argument
    # parser.
    logging.basicConfig(
        level=logging.DEBUG
        if ("--debug" in sys.argv or "-d" in sys.argv)
        else logging.INFO
    )

    # Add arguments specific to uco_validate.
    parser.add_argument(
        "-d", "--debug", action="store_true", help="Output additional runtime messages."
    )
    parser.add_argument(
        "--built-version",
        choices=tuple(built_version_choices_list),
        default="uco-" + CURRENT_UCO_VERSION,
        help="Monolithic aggregation of UCO ontology files at certain versions.  Does not require networking to use.  Default is most recent UCO release.",
    )
    parser.add_argument(
        "--ontology-graph",
        action="append",
        help="Combined ontology (i.e. subclass hierarchy) and shapes (SHACL) file, in any format accepted by rdflib recognized by file extension (e.g. .ttl).  Will supplement ontology selected by --built-version.  Can be given multiple times.",
    )

    # Inherit arguments from pyshacl.
    parser.add_argument(
        "--abort",
        action="store_true",
        help="(As with pyshacl CLI) Abort on first invalid data.",
    )
    parser.add_argument(
        "-w",
        "--allow-warnings",
        action="store_true",
        help="(As with pyshacl CLI) Shapes marked with severity of Warning or Info will not cause result to be invalid.",
    )
    parser.add_argument(
        "-f",
        "--format",
        choices=("human", "turtle", "xml", "json-ld", "nt", "n3"),
        default="human",
        help="(ALMOST as with pyshacl CLI) Choose an output format. Default is \"human\".  Difference: 'table' not provided.",
    )
    parser.add_argument(
        "-im",
        "--imports",
        action="store_true",
        help="(As with pyshacl CLI) Allow import of sub-graphs defined in statements with owl:imports.",
    )
    parser.add_argument(
        "-i",
        "--inference",
        choices=("none", "rdfs", "owlrl", "both"),
        default="none",
        help='(As with pyshacl CLI) Choose a type of inferencing to run against the Data Graph before validating. Default is "none".',
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        nargs="?",
        type=argparse.FileType("x"),
        help='(ALMOST as with pyshacl CLI) Send output to a file.  If absent, output will be written to stdout.  Difference: If specified, file is expected not to exist.  Clarification: Does NOT influence --format flag\'s default value of "human".  (I.e., any machine-readable serialization format must be specified with --format.)',
        default=sys.stdout,
    )

    parser.add_argument("in_graph", nargs="+")

    args = parser.parse_args()

    data_graph = rdflib.Graph()
    for in_graph in args.in_graph:
        _logger.debug("in_graph = %r.", in_graph)
        data_graph.parse(in_graph)

    ontology_graph = rdflib.Graph()
    if args.built_version != "none":
        ttl_filename = args.built_version + ".ttl"
        _logger.debug("ttl_filename = %r.", ttl_filename)
        ttl_data = importlib.resources.read_text(uco_utils.ontology, ttl_filename)
        ontology_graph.parse(data=ttl_data, format="turtle")
    if args.ontology_graph:
        for arg_ontology_graph in args.ontology_graph:
            _logger.debug("arg_ontology_graph = %r.", arg_ontology_graph)
            ontology_graph.parse(arg_ontology_graph)

    # Determine output format.
    # pySHACL's determination of output formatting is handled solely
    # through the -f flag.  Other UCO CLI tools handle format
    # determination by output file extension.  uco_validate will defer
    # to pySHACL behavior, as other UCO tools don't (at the time of
    # this writing) have the value "human" as an output format.
    validator_kwargs: typing.Dict[str, str] = dict()
    if args.format != "human":
        validator_kwargs["serialize_report_graph"] = args.format

    validate_result: typing.Tuple[
        bool, typing.Union[Exception, bytes, str, rdflib.Graph], str
    ]
    validate_result = pyshacl.validate(
        data_graph,
        shacl_graph=ontology_graph,
        ont_graph=ontology_graph,
        inference=args.inference,
        abort_on_first=args.abort,
        allow_warnings=True if args.allow_warnings else False,
        debug=True if args.debug else False,
        do_owl_imports=True if args.imports else False,
        **validator_kwargs
    )

    # Relieve RAM of the data graph after validation has run.
    del data_graph

    conforms = validate_result[0]
    validation_graph = validate_result[1]
    validation_text = validate_result[2]

    # NOTE: The output logistics code is adapted from pySHACL's file
    # pyshacl/cli.py.  This section should be monitored for code drift.
    if args.format == "human":
        args.output.write(validation_text)
    else:
        if isinstance(validation_graph, rdflib.Graph):
            raise NotImplementedError(
                "rdflib.Graph expected not to be created from --format value %r."
                % args.format
            )
        elif isinstance(validation_graph, bytes):
            args.output.write(validation_graph.decode("utf-8"))
        elif isinstance(validation_graph, str):
            args.output.write(validation_graph)
        else:
            raise NotImplementedError(
                "Unexpected result type returned from validate: %r."
                % type(validation_graph)
            )

    sys.exit(0 if conforms else 1)


if __name__ == "__main__":
    main()
