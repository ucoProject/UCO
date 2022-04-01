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
NS_UCO_ACTION = rdflib.Namespace("https://ontology.unifiedcyberontology.org/uco/action/")
NS_UCO_CORE = rdflib.Namespace("https://ontology.unifiedcyberontology.org/uco/core/")
NS_UCO_LOCATION = rdflib.Namespace("https://ontology.unifiedcyberontology.org/uco/location/")

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

def confirm_validation_results(
  filename : str,
  expected_conformance: bool,
  *,
  expected_focus_node_severities : typing.Optional[typing.Tuple[typing.Set[str], str]] = None,
  expected_result_paths : typing.Optional[typing.Set[str]] = None
):
    g = load_validation_graph(filename, expected_conformance)

    computed_focus_node_severities = set()
    computed_result_paths = set()

    query = rdflib.plugins.sparql.prepareQuery("""\
SELECT DISTINCT ?nFocusNode ?nResultPath ?nSeverity
WHERE {
  ?nReport
    a sh:ValidationReport ;
    sh:result ?nValidationResult ;
    .

  ?nValidationResult
    a sh:ValidationResult ;
    sh:focusNode ?nFocusNode ;
    sh:resultPath ?nResultPath ;
    sh:resultSeverity ?nSeverity ;
    .
}
""", initNs=NSDICT)

    for result in g.query(query):
        (n_focus_node, n_result_path, n_severity) = result
        computed_focus_node_severities.add((str(n_focus_node), str(n_severity)))
        computed_result_paths.add(str(n_result_path))

    if not expected_focus_node_severities is None:
        try:
            assert expected_focus_node_severities == computed_focus_node_severities
        except:
            logging.error("Please review %s and its associated .json file to identify the ground truth validation error mismatch pertaining to focus nodes noted in this function.", filename)
            raise

    if not expected_result_paths is None:
        try:
            assert expected_result_paths == computed_result_paths
        except:
            logging.error("Please review %s and its associated .json file to identify the ground truth validation error mismatch pertaining to data properties noted in this function.", filename)
            raise

def test_action_inheritance_PASS_validation():
    """
    Confirm the PASS instance data passes validation.
    """
    confirm_validation_results(
      "action_inheritance_PASS_validation.ttl",
      True,
      expected_focus_node_severities={
        ("http://example.org/kb/action1", str(NS_SH.Info)),
      }
    )

def test_action_inheritance_XFAIL_validation():
    """
    Confirm the XFAIL instance data fails validation based on an expected set of properties not conforming to shape constraints.
    """
    confirm_validation_results(
      "action_inheritance_XFAIL_validation.ttl",
      False,
      expected_result_paths={
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

def test_hash_PASS() -> None:
    g = load_validation_graph("hash_PASS_validation.ttl", True)
    assert isinstance(g, rdflib.Graph)

def test_hash_XFAIL() -> None:
    confirm_validation_results(
      "hash_XFAIL_validation.ttl",
      False,
      expected_focus_node_severities={
        ("http://example.org/kb/hash-2", str(NS_SH.Info)),
        ("http://example.org/kb/hash-3", str(NS_SH.Violation)),
        ("http://example.org/kb/hash-4", str(NS_SH.Info)),
        ("http://example.org/kb/hash-5", str(NS_SH.Info)),
        ("http://example.org/kb/hash-5", str(NS_SH.Violation))
      }
    )

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
    confirm_validation_results(
      "location_XFAIL_validation.ttl",
      False,
      expected_result_paths={
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
    confirm_validation_results(
      "location_XFAIL_validation.ttl",
      False,
      expected_result_paths={
        str(NS_UCO_CORE.descriptionButWrongName)
      }
    )

def test_relationship_PASS_partial() -> None:
    """
    This test should be replaced with test_relationship_XFAIL_full when the semi-open vocabulary design current as of UCO 0.8.0 is re-done.
    """
    confirm_validation_results(
      "relationship_PASS_validation.ttl",
      True,
      expected_focus_node_severities=set()
    )

@pytest.mark.xfail(reason="Test expected to fail under semi-open vocabulary design current as of UCO 0.8.0.", strict=True)
def test_relationship_PASS_full() -> None:
    confirm_validation_results(
      "relationship_PASS_validation.ttl",
      True,
      expected_focus_node_severities={
        ("http://example.org/kb/relationship-1-1-1", str(NS_SH.Info)),
        ("http://example.org/kb/relationship-1-2-1", str(NS_SH.Info)),
        ("http://example.org/kb/relationship-1-3-1", str(NS_SH.Info)),
        ("http://example.org/kb/relationship-2-1-1", str(NS_SH.Info)),
        ("http://example.org/kb/relationship-2-2-1", str(NS_SH.Info)),
        ("http://example.org/kb/relationship-2-3-1", str(NS_SH.Info)),
      }
    )

def test_relationship_XFAIL_partial() -> None:
    """
    This test should be replaced with test_relationship_XFAIL_full when the semi-open vocabulary design current as of UCO 0.8.0 is re-done.
    """
    confirm_validation_results(
      "relationship_XFAIL_validation.ttl",
      False,
      expected_focus_node_severities={
        ("http://example.org/kb/relationship-1-1-2", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-1-1-3", str(NS_SH.Violation)),
        ('http://example.org/kb/relationship-1-2-2', str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-1-2-3", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-1-3-2", str(NS_SH.Violation)),
        ('http://example.org/kb/relationship-1-3-3', str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-2-1-2", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-2-1-3", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-2-2-2", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-2-2-3", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-2-3-2", str(NS_SH.Violation)),
        ('http://example.org/kb/relationship-2-3-3', str(NS_SH.Violation)),
      }
    )

@pytest.mark.xfail(reason="Test expected to fail under semi-open vocabulary design current as of UCO 0.8.0.", strict=True)
def test_relationship_XFAIL_full() -> None:
    confirm_validation_results(
      "relationship_XFAIL_validation.ttl",
      False,
      expected_focus_node_severities={
        ("http://example.org/kb/relationship-1-1-2", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-1-1-3", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-1-2-3", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-1-3-2", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-2-1-2", str(NS_SH.Info)),
        ("http://example.org/kb/relationship-2-1-2", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-2-1-3", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-2-2-2", str(NS_SH.Info)),
        ("http://example.org/kb/relationship-2-2-2", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-2-2-3", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-2-3-2", str(NS_SH.Info)),
        ("http://example.org/kb/relationship-2-3-2", str(NS_SH.Violation)),
      }
    )
