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
Tests in this file confirm that the JSON-LD files with "PASS" in the
name to pass SHACL validation, and JSON-LD files with "XFAIL" in the
name not only to fail SHACL validation, but also to report a set of
properties used in their JSON-LD that triggered SHACL validation errors.

This test was written to be called with the pytest framework, expecting
the only functions to be called to be named "test_*".
"""

import logging
import typing

import pytest
import rdflib.plugins.sparql

NS_SH = rdflib.SH
NS_UCO_ACTION = rdflib.Namespace("https://unifiedcyberontology.org/ontology/uco/action#")
NS_UCO_CORE = rdflib.Namespace("https://unifiedcyberontology.org/ontology/uco/core#")
NS_UCO_LOCATION = rdflib.Namespace("https://unifiedcyberontology.org/ontology/uco/location#")

NSDICT = {"sh": NS_SH}

def load_validation_graph(
  filename : str,
  expected_conformance : bool
) -> rdflib.Graph:
    g = rdflib.Graph()
    g.parse(filename, format="turtle")
    g.namespace_manager.bind("sh", NS_SH)

    query = rdflib.plugins.sparql.prepareQuery("""\
SELECT ?lConforms
WHERE {
  ?nReport
    a sh:ValidationReport ;
    sh:conforms ?lConforms ;
    .
}
""", initNs=NSDICT)

    computed_conformance = None
    for result in g.query(query):
        (l_conforms,) = result
        computed_conformance = bool(l_conforms)
    assert expected_conformance == computed_conformance
    return g

def confirm_validation_errors(
  filename : str,
  *,
  expected_error_iris : typing.Optional[typing.Set[str]] = None,
  expected_focus_nodes : typing.Optional[typing.Set[str]] = None
):
    g = load_validation_graph(filename, False)

    computed_error_iris = set()
    computed_focus_nodes = set()

    query = rdflib.plugins.sparql.prepareQuery("""\
SELECT DISTINCT ?nFocusNode ?nResultPath
WHERE {
  ?nReport
    a sh:ValidationReport ;
    sh:result ?nValidationResult ;
    .

  ?nValidationResult
    a sh:ValidationResult ;
    sh:focusNode ?nFocusNode ;
    sh:resultPath ?nResultPath ;
    .
}
""", initNs=NSDICT)

    for result in g.query(query):
        (n_focus_node, n_result_path) = result
        computed_focus_nodes.add(str(n_focus_node))
        computed_error_iris.add(str(n_result_path))

    if not expected_error_iris is None:
        try:
            assert expected_error_iris == computed_error_iris
        except:
            logging.error("Please review %s and its associated .json file to identify the ground truth validation error mismatch pertaining to data properties noted in this function.", filename)
            raise

    if not expected_focus_nodes is None:
        try:
            assert expected_focus_nodes == computed_focus_nodes
        except:
            logging.error("Please review %s and its associated .json file to identify the ground truth validation error mismatch pertaining to focus nodes noted in this function.", filename)
            raise

def test_action_inheritance_PASS_validation():
    """
    Confirm the PASS instance data passes validation.
    """
    g = load_validation_graph("action_inheritance_PASS_validation.ttl", True)
    assert isinstance(g, rdflib.Graph)

def test_action_inheritance_XFAIL_validation():
    """
    Confirm the XFAIL instance data fails validation based on an expected set of properties not conforming to shape constraints.
    """
    confirm_validation_errors(
      "action_inheritance_XFAIL_validation.ttl",
      expected_error_iris={
        str(NS_UCO_ACTION.action),
        str(NS_UCO_ACTION.actionStatus)
      }
    )

def test_action_result_PASS_validation():
    """
    Confirm the PASS instance data passes validation.
    """
    g = load_validation_graph("action_result_PASS_validation.ttl", True)
    assert isinstance(g, rdflib.Graph)

def test_location_PASS_validation():
    """
    Confirm the PASS instance data passes validation.
    """
    g = load_validation_graph("location_PASS_validation.ttl", True)
    assert isinstance(g, rdflib.Graph)

def test_location_XFAIL_validation():
    """
    Confirm the XFAIL instance data fails validation based on an expected set of properties not conforming to shape constraints.
    """
    confirm_validation_errors(
      "location_XFAIL_validation.ttl",
      expected_error_iris={
        str(NS_UCO_CORE.hasFacet),
        str(NS_UCO_LOCATION.postalCode)
      }
    )

@pytest.mark.xfail(strict=True)
def test_location_XFAIL_validation_XPASS_wrong_concept_name():
    """
    Report the XFAIL instance data XPASSes one of the induced errors - the non-existent concept core:descriptionButWrongName is not reported as an error.
    Should a SHACL mechanism later be identified to detect this error, this test can be retired, adding NS_UCO_CORE.descriptionButWrongName to the expected IRI set in test_location_XFAIL_validation().
    """
    confirm_validation_errors(
      "location_XFAIL_validation.ttl",
      expected_error_iris={
        str(NS_UCO_CORE.descriptionButWrongName)
      }
    )

def test_relationship_PASS_validation():
    """
    Confirm the PASS instance data passes validation.
    """
    g = load_validation_graph("relationship_PASS_validation.ttl", True)
    assert isinstance(g, rdflib.Graph)

def test_relationship_XFAIL_validation():
    """
    Confirm the PASS instance data passes validation.
    """
    confirm_validation_errors(
      "relationship_XFAIL_validation.ttl",
      expected_focus_nodes={
        "http://example.org/kb/relationship1",
        "http://example.org/kb/relationship2",
        "http://example.org/kb/relationship3"
      }
    )

def test_relationship_PASS_via_rdf_toolkit_validation_after_translation():
    g = load_validation_graph("relationship_PASS_via_rdf_toolkit_validation_after_translation.ttl", True)
    assert isinstance(g, rdflib.Graph)

def relationship_PASS_via_rdflib_validation_after_translation():
    g = load_validation_graph("relationship_PASS_via_rdflib_validation_after_translation.ttl", True)
    assert isinstance(g, rdflib.Graph)
