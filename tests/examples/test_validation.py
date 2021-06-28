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

import pytest
import rdflib.plugins.sparql

query_text = """\
SELECT ?lConforms
WHERE {
  ?nReport
    a sh:ValidationReport ;
    sh:conforms ?lConforms ;
    .
}
"""

nsdict = {"sh": "http://www.w3.org/ns/shacl#"}

def load_validation_graph(filename):
    g = rdflib.Graph()
    g.parse(filename, format="turtle")
    g.namespace_manager.bind("sh", "http://www.w3.org/ns/shacl#")
    return g

def test_location_PASS_validation():
    g = load_validation_graph("location_PASS_validation.ttl")
    query = rdflib.plugins.sparql.prepareQuery(query_text, initNs=nsdict)
    conforms = None
    for result in g.query(query):
        (l_conforms,) = result
        conforms = bool(l_conforms)
    assert conforms

def test_location_XFAIL_validation():
    g = load_validation_graph("location_XFAIL_validation.ttl")
    query = rdflib.plugins.sparql.prepareQuery(query_text, initNs=nsdict)
    conforms = None
    for result in g.query(query):
        (l_conforms,) = result
        conforms = bool(l_conforms)
    assert conforms == False
