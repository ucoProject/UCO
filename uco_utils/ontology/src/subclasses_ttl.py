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
This script creates an excerpt of an ontology graph that consists solely of all rdfs:subClassOf statements.
"""

__version__ = "0.1.0"

import argparse

import rdflib


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("out_ttl")
    parser.add_argument("in_ttl", nargs="+")
    args = parser.parse_args()

    in_graph = rdflib.Graph()
    out_graph = rdflib.Graph()

    in_ttl: str
    for in_ttl in args.in_ttl:
        in_graph.parse(in_ttl)

    for triple in in_graph.triples((None, rdflib.RDFS.subClassOf, None)):
        out_graph.add(triple)

    out_graph.serialize(args.out_ttl)


if __name__ == "__main__":
    main()
