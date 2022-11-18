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

import pathlib
import logging
import typing

import pytest
import rdflib.plugins.sparql

NS_CO = rdflib.Namespace("http://purl.org/co/")
NS_SH = rdflib.SH
NS_UCO_ACTION = rdflib.Namespace("https://ontology.unifiedcyberontology.org/uco/action/")
NS_UCO_CO = rdflib.Namespace("https://ontology.unifiedcyberontology.org/co/")
NS_UCO_CORE = rdflib.Namespace("https://ontology.unifiedcyberontology.org/uco/core/")
NS_UCO_LOCATION = rdflib.Namespace("https://ontology.unifiedcyberontology.org/uco/location/")
NS_UCO_TYPES = rdflib.Namespace("https://ontology.unifiedcyberontology.org/uco/types/")

NSDICT = {"sh": NS_SH}

@pytest.fixture(scope="session")
def monolithic_ontology_graph() -> rdflib.Graph:
    graph = rdflib.Graph()
    monolithic_ttl_path = pathlib.Path(__file__).parent.parent / "uco_monolithic.ttl"
    graph.parse(str(monolithic_ttl_path), format="turtle")
    return graph

def load_validation_graph(
  filename : str,
  expected_conformance : bool
) -> rdflib.Graph:
    g = rdflib.Graph()
    g.parse(filename, format="turtle")
    g.namespace_manager.bind("sh", NS_SH)

    query = rdflib.plugins.sparql.processor.prepareQuery("""\
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
  expected_focus_node_severities : typing.Optional[typing.Set[typing.Tuple[str, str]]] = None,
  expected_result_paths : typing.Optional[typing.Set[str]] = None,
  expected_source_shapes: typing.Optional[typing.Set[str]] = None
) -> None:
    """
    The expected-sets are sets where names are known.

    Blank nodes are omitted, and should be tested with a different set.
    """
    g = load_validation_graph(filename, expected_conformance)

    computed_focus_node_severities = set()
    computed_result_paths = set()
    computed_source_shapes = set()

    query = rdflib.plugins.sparql.processor.prepareQuery("""\
SELECT DISTINCT ?nFocusNode ?nResultPath ?nSeverity ?nSourceShape
WHERE {
  ?nReport
    a sh:ValidationReport ;
    sh:result ?nValidationResult ;
    .

  ?nValidationResult
    a sh:ValidationResult ;
    sh:focusNode ?nFocusNode ;
    sh:resultSeverity ?nSeverity ;
    sh:sourceShape ?nSourceShape ;
    .

  # sh:not violations do not have a sh:resultPath.
  OPTIONAL {
  ?nValidationResult
    sh:resultPath ?nResultPath ;
    .
  }
}
""", initNs=NSDICT)

    for result in g.query(query):
        (n_focus_node, n_result_path, n_severity, n_source_shape) = result

        computed_focus_node_severities.add((str(n_focus_node), str(n_severity)))

        if isinstance(n_result_path, rdflib.URIRef):
            computed_result_paths.add(str(n_result_path))

        if isinstance(n_source_shape, rdflib.URIRef):
            computed_source_shapes.add(str(n_source_shape))

    if not expected_focus_node_severities is None:
        try:
            assert expected_focus_node_severities == computed_focus_node_severities
        except:
            logging.error("Please review %s and its associated .json file to identify the ground truth validation error mismatch pertaining to named focus nodes noted in this function.", filename)
            raise

    if not expected_result_paths is None:
        try:
            assert expected_result_paths == computed_result_paths
        except:
            logging.error("Please review %s and its associated .json file to identify the ground truth validation error mismatch pertaining to data properties noted in this function.", filename)
            raise

    if not expected_source_shapes is None:
        try:
            assert expected_source_shapes == computed_source_shapes
        except:
            logging.error("Please review %s and its associated .json file to identify the ground truth validation error mismatch pertaining to named source shapes noted in this function.", filename)
            raise

def test_action_inheritance_PASS_validation() -> None:
    """
    Confirm the PASS instance data passes validation.
    """
    confirm_validation_results(
      "action_inheritance_PASS_validation.ttl",
      True,
      expected_focus_node_severities={
        ("http://example.org/kb/action-7acb25ab-0a51-4495-9133-baa69c3be54e", str(NS_SH.Info)),
      }
    )

def test_action_inheritance_XFAIL_validation() -> None:
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

def test_action_result_PASS_validation() -> None:
    """
    Confirm the PASS instance data passes validation.
    """
    g = load_validation_graph("action_result_PASS_validation.ttl", True)
    assert isinstance(g, rdflib.Graph)

def test_configuration_setting_PASS_validation() -> None:
    g = load_validation_graph("configuration_setting_PASS_validation.ttl", True)
    assert isinstance(g, rdflib.Graph)

def test_configuration_setting_XFAIL_validation() -> None:
    confirm_validation_results(
      "configuration_setting_XFAIL_validation.ttl",
      False,
      expected_focus_node_severities={
        ("http://example.org/kb/configuration-entry-5f0fc3ea-e763-4b6d-997a-be0d1ceffc8c", str(NS_SH.Violation)),
        ("http://example.org/kb/configured-object-7156bff0-b805-4190-83ee-230fae31e33a", str(NS_SH.Violation)),
      }
)

def test_database_records_PASS() -> None:
    confirm_validation_results(
      "database_records_PASS_validation.ttl",
      True
    )

def test_database_records_XFAIL() -> None:
    confirm_validation_results(
      "database_records_XFAIL_validation.ttl",
      False,
      expected_focus_node_severities={
        ("http://example.org/kb/table-field-facet-46aafb6e-0be4-4412-a938-16c4b5ae5314", str(NS_SH.Violation)),
        ("http://example.org/kb/table-field-facet-37182dba-4dbd-4b97-b49e-8038b7fbfd29", str(NS_SH.Violation)),
      }
    )

def test_has_facet_inverse_functional_PASS() -> None:
    confirm_validation_results(
      "has_facet_inverse_functional_PASS_validation.ttl",
      True
    )

def test_has_facet_inverse_functional_XFAIL() -> None:
    confirm_validation_results(
      "has_facet_inverse_functional_XFAIL_validation.ttl",
      False,
      expected_focus_node_severities={
        ("http://example.org/kb/facet-b94b9cce-f11a-49f2-b5d4-9efff5e8ab2d", str(NS_SH.Violation))
      }
    )

def test_hash_PASS() -> None:
    g = load_validation_graph("hash_PASS_validation.ttl", True)
    assert isinstance(g, rdflib.Graph)

def test_hash_XFAIL() -> None:
    confirm_validation_results(
      "hash_XFAIL_validation.ttl",
      False,
      expected_focus_node_severities={
        ("http://example.org/kb/hash-04dcd1dc-6920-4977-a898-e242870249a4", str(NS_SH.Info)),
        ("http://example.org/kb/hash-af4b0c85-b042-4e2d-a213-210b3d7f115c", str(NS_SH.Violation)),
        ("http://example.org/kb/hash-e97431ea-6fb8-46d9-9c23-94be4b7cc977", str(NS_SH.Info)),
        ("http://example.org/kb/hash-f46c714f-559a-4325-bf8a-4ef60c92c771", str(NS_SH.Info)),
        ("http://example.org/kb/hash-f46c714f-559a-4325-bf8a-4ef60c92c771", str(NS_SH.Violation))
      }
    )

def test_co_PASS_validation() -> None:
    confirm_validation_results("co_PASS_validation.ttl", True)

def test_co_XFAIL_validation() -> None:
    # The "index" entry's spelling is due to Namespace objects being
    # strings, therefore having the .index() function defined.
    confirm_validation_results(
      "co_XFAIL_validation.ttl",
      False,
      expected_result_paths={
        str(NS_CO.firstItem),
        str(NS_CO["index"]),
        str(NS_CO.item),
        str(NS_CO.itemContent),
        str(NS_CO.lastItem),
        str(NS_CO.nextItem),
        str(NS_CO.previousItem),
        str(NS_CO.size),
      },
      expected_source_shapes={
        str(NS_UCO_CO["firstItem-subjects-shape"]),
        str(NS_UCO_CO["firstItem-subjects-previousItem-shape"]),
        str(NS_UCO_CO["item-subjects-shape"]),
        str(NS_UCO_CO["itemContent-subjects-shape"]),
        str(NS_UCO_CO["lastItem-subjects-shape"]),
        str(NS_UCO_CO["nextItem-subjects-shape"]),
        str(NS_UCO_CO["previousItem-subjects-shape"]),
        str(NS_UCO_CO["size-subjects-shape"]),
      }
    )

def test_location_PASS_validation() -> None:
    """
    Confirm the PASS instance data passes validation.
    """
    g = load_validation_graph("location_PASS_validation.ttl", True)
    assert isinstance(g, rdflib.Graph)

def test_location_XFAIL_validation() -> None:
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
def test_location_XFAIL_validation_XPASS_wrong_concept_name() -> None:
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

def test_message_thread(monolithic_ontology_graph: rdflib.Graph) -> None:
    r"""
    Confirm the answer to this question:
    What are all of the messages that followed the first in the thread kb:message-thread-86bef664...?

    message-thread-86bef664... forked, and has these reply paths:

     1     2     3
    * --- * --- *
     \     \
      \     \ 4
       \     *
     5  \ 6
    * --- *

     7
    *

    (Message 7 is outside the thread.)
    """

    expected: typing.Set[str] = {
        "http://example.org/kb/message-2-2e770ebe-cc83-46cd-b340-9c2ba081c002",
        "http://example.org/kb/message-3-3ec6dff5-edcc-4b64-ad51-aa8a262dcef1",
        "http://example.org/kb/message-4-51392250-533d-4a04-89d7-6db6340d09c3",
        "http://example.org/kb/message-6-7e4f6696-13cb-443b-bccf-ac1bd1c90300",
    }
    computed: typing.Set[str] = set()

    data_graph = rdflib.Graph()
    data_filepath = pathlib.Path(__file__).parent / "message_thread_PASS.json"
    data_graph.parse(str(data_filepath), format="json-ld")

    analysis_graph = data_graph + monolithic_ontology_graph

    query_str = """\
PREFIX co: <http://purl.org/co/>
PREFIX kb: <http://example.org/kb/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX types: <https://ontology.unifiedcyberontology.org/uco/types/>

SELECT ?nLaterMessage
WHERE {
  ?nFirstMessageItem
    co:itemContent kb:message-1-01a38f9a-d91b-4f7a-b446-308829b0b6c3 ;
    (types:threadNextItem|types:threadSuccessor)+ / co:itemContent ?nLaterMessage ;
    .
}
"""

    for result in analysis_graph.query(query_str):
        computed.add(str(result[0]))

    assert expected == computed

def test_message_thread_PASS_validation() -> None:
    confirm_validation_results("message_thread_PASS_validation.ttl", True)

def test_message_thread_XFAIL_validation() -> None:
    confirm_validation_results("message_thread_XFAIL_validation.ttl", False)

def test_owl_axiom_PASS() -> None:
    confirm_validation_results(
      "owl_axiom_PASS_validation.ttl",
      True,
      expected_focus_node_severities=set()
    )

def test_owl_axiom_XFAIL() -> None:
    confirm_validation_results(
      "owl_axiom_XFAIL_validation.ttl",
      False,
      expected_focus_node_severities={
        ("http://example.org/kb/axiom-1", str(NS_SH.Violation)),
      }
    )

def test_owl_properties_PASS() -> None:
    confirm_validation_results(
      "owl_properties_PASS_validation.ttl",
      True,
      expected_focus_node_severities=set()
    )

def test_owl_properties_XFAIL() -> None:
    confirm_validation_results(
      "owl_properties_XFAIL_validation.ttl",
      False,
      expected_focus_node_severities={
        ("http://example.org/kb/cross-property-ad", str(NS_SH.Violation)),
        ("http://example.org/kb/cross-property-ao", str(NS_SH.Violation)),
        ("http://example.org/kb/cross-property-do", str(NS_SH.Violation)),
      }
    )

def test_rdf_list_PASS() -> None:
    confirm_validation_results(
      "rdf_list_PASS_validation.ttl",
      True,
      expected_focus_node_severities=set()
    )

def test_rdf_list_XFAIL() -> None:
    confirm_validation_results(
      "rdf_list_XFAIL_validation.ttl",
      False
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
        ("http://example.org/kb/relationship-1-1-1-7273698b-34ef-4d04-8cbf-99bdcad7a336", str(NS_SH.Info)),
        ("http://example.org/kb/relationship-1-2-1-87a18d97-1bd2-4b02-9438-96ddbcba9372", str(NS_SH.Info)),
        ("http://example.org/kb/relationship-1-3-1-9b94518f-4415-4869-ae49-af66e99d0250", str(NS_SH.Info)),
        ("http://example.org/kb/relationship-2-1-1-a6ba4ba1-00b2-436e-b64a-4475355560cd", str(NS_SH.Info)),
        ("http://example.org/kb/relationship-2-2-1-a8e6100b-4e1c-4ec8-a6a4-a4db8ecb8233", str(NS_SH.Info)),
        ("http://example.org/kb/relationship-2-3-1-b8d01d00-5a32-4c8f-8a30-11a69b8c5420", str(NS_SH.Info)),
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
        ("http://example.org/kb/relationship-1-1-2-2e668923-bfb7-4f54-afb6-66074ab5b9b0", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-1-1-3-35598cb0-1770-49af-a417-51e91774df89", str(NS_SH.Violation)),
        ('http://example.org/kb/relationship-1-2-2-3ee0cc25-5923-40df-ba8f-0cce5f18f724', str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-1-2-3-46da302e-cff3-4634-bcf8-6f52649e2496", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-1-3-2-746aeee5-c857-4afb-8dba-85d5d60be279", str(NS_SH.Violation)),
        ('http://example.org/kb/relationship-1-3-3-779c2646-dd1d-4fac-9e22-5a14bd78c6ea', str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-2-1-2-800dd373-2916-4104-a2bb-2715cbc80804", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-2-1-3-803a8e5c-f09a-403d-9c8d-91b08a3c0bbd", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-2-2-2-851c5f1a-1f1e-4315-b7b8-6d7f4a602e98", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-2-2-3-90046c36-98f7-4f69-8566-2541eaad1dce", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-2-3-2-c1e3518a-b808-49ee-9d68-73aaa6ec2ea7", str(NS_SH.Violation)),
        ('http://example.org/kb/relationship-2-3-3-cee42e22-3f76-465f-b737-62f2786eadfc', str(NS_SH.Violation)),
      }
    )

@pytest.mark.xfail(reason="Test expected to fail under semi-open vocabulary design current as of UCO 0.8.0.", strict=True)
def test_relationship_XFAIL_full() -> None:
    confirm_validation_results(
      "relationship_XFAIL_validation.ttl",
      False,
      expected_focus_node_severities={
        ("http://example.org/kb/relationship-1-1-2-2e668923-bfb7-4f54-afb6-66074ab5b9b0", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-1-1-3-35598cb0-1770-49af-a417-51e91774df89", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-1-2-3-46da302e-cff3-4634-bcf8-6f52649e2496", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-1-3-2-746aeee5-c857-4afb-8dba-85d5d60be279", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-2-1-2-800dd373-2916-4104-a2bb-2715cbc80804", str(NS_SH.Info)),
        ("http://example.org/kb/relationship-2-1-2-800dd373-2916-4104-a2bb-2715cbc80804", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-2-1-3-803a8e5c-f09a-403d-9c8d-91b08a3c0bbd", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-2-2-2-851c5f1a-1f1e-4315-b7b8-6d7f4a602e98", str(NS_SH.Info)),
        ("http://example.org/kb/relationship-2-2-2-851c5f1a-1f1e-4315-b7b8-6d7f4a602e98", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-2-2-3-90046c36-98f7-4f69-8566-2541eaad1dce", str(NS_SH.Violation)),
        ("http://example.org/kb/relationship-2-3-2-c1e3518a-b808-49ee-9d68-73aaa6ec2ea7", str(NS_SH.Info)),
        ("http://example.org/kb/relationship-2-3-2-c1e3518a-b808-49ee-9d68-73aaa6ec2ea7", str(NS_SH.Violation)),
      }
    )

def test_thread_PASS_validation() -> None:
    confirm_validation_results("thread_PASS_validation.ttl", True)

def test_thread_XFAIL_validation() -> None:
    confirm_validation_results(
      "thread_XFAIL_validation.ttl",
      False,
      expected_result_paths={
        str(NS_CO.item),
        str(NS_CO.itemContent),
        str(NS_UCO_TYPES.threadOriginItem),
      }
    )

def uco_thing_XFAIL_validation() -> None:
    confirm_validation_results(
      "uco_thing_XFAIL_validation.ttl",
      False,
    )
