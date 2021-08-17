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

import os

import rdflib.plugins.sparql

def test_max_1_sh_datatype_per_property_shape():
    """
    This enforces the maximum sh:datatype count of 1, as specified here:

    "A shape has at most one value for sh:datatype."
    https://www.w3.org/TR/shacl/#DatatypeConstraintComponent

    This is encoded in the SHACL ontology with the statement 'sh:DatatypeConstraintComponent-datatype sh:maxCount 1 .'
    """
    expected = set()  # This set is intentionally empty.
    computed = set()

    graph = rdflib.Graph()
    graph.parse(os.path.join(os.path.dirname(__file__), "uco_monolithic.ttl"))
    assert len(graph) > 0, "Failed to load uco_monolithic.ttl."

    nsdict = {
      "sh": rdflib.SH
    }

    query_object = rdflib.plugins.sparql.prepareQuery("""\
SELECT ?nClass ?nPath ?lConstraintDatatypeTally
WHERE {
  {
    SELECT ?nClass ?nPath (COUNT(DISTINCT ?nConstraintDatatype) AS ?lConstraintDatatypeTally)
    WHERE {
      ?nClass
        sh:property ?nPropertyShape ;
        .

      ?nPropertyShape
        sh:datatype ?nConstraintDatatype ;
        sh:path ?nPath ;
        .
    } GROUP BY ?nClass ?nPath
  }

  FILTER (?lConstraintDatatypeTally > 1)
}
""", initNs=nsdict)
    for result in graph.query(query_object):
        computed.add(result)
    assert expected == computed
