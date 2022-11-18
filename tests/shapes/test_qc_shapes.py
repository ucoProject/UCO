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

from typing import Optional, Set, Tuple

import pytest
from rdflib import Graph, Literal, Namespace, SH, URIRef

NS_UCO_OWL = Namespace("https://ontology.unifiedcyberontology.org/owl/")


# Documentation for parametrize:
# https://docs.pytest.org/en/6.2.x/parametrize.html
@pytest.mark.parametrize(
    ["filename", "expected_validation_result", "expected_focus_values"],
    [
        (
            "examples_uco_owl/owl_incompatibleWith_shape_PASS_validation.ttl",
            True,
            {
                # example-1 is expected to not trigger a warning.
                (
                    URIRef("http://example.org/example-2-a"),
                    URIRef("http://example.org/example-2-b"),
                ),
                (
                    URIRef("http://example.org/example-3-b"),
                    URIRef("http://example.org/example-3-b"),
                ),
                (
                    URIRef("http://example.org/example-4-b/v1"),
                    None,
                ),
                (
                    URIRef("http://example.org/example-5-a"),
                    URIRef("http://example.org/example-5-b/v1"),
                ),
                (
                    URIRef("http://example.org/example-5-b/v1"),
                    None,
                ),
                # example-6 is expected to not trigger a warning.
                (
                    URIRef("http://example.org/example-7-c"),
                    URIRef("http://example.org/example-7-c"),
                ),
                (
                    URIRef("http://example.org/example-8-c"),
                    URIRef("http://example.org/example-8-c"),
                ),
                (
                    URIRef("http://example.org/example-9-c/v1"),
                    None,
                ),
                (
                    URIRef("http://example.org/example-10-c/v1"),
                    None,
                ),
                (
                    URIRef("http://example.org/example-11-d"),
                    URIRef("http://example.org/example-11-d"),
                ),
                (
                    URIRef("http://example.org/example-12-d"),
                    URIRef("http://example.org/example-12-d"),
                ),
                (
                    URIRef("http://example.org/example-13-d"),
                    URIRef("http://example.org/example-13-d"),
                ),
                (
                    URIRef("http://example.org/example-14-d/v1"),
                    None,
                ),
                (
                    URIRef("http://example.org/example-15-d/v1"),
                    None,
                ),
                (
                    URIRef("http://example.org/example-16-d/v3"),
                    None,
                ),
            },
        ),
        (
            "examples_uco_owl/owl_versionIRI_multiversion_shape_PASS_validation.ttl",
            True,
            {
                (URIRef("http://example.org/example-1"), None),
            },
        ),
        (
            "examples_uco_owl/owl_shacl_paths_PASS_validation.ttl",
            True,
            set(),
        ),
        (
            "examples_uco_qc/owl_Ontology_shape_property_owl_versionIRI_PASS_validation.ttl",
            True,
            set(),
        ),
        (
            "examples_uco_qc/owl_Ontology_shape_property_owl_versionIRI_XFAIL_validation.ttl",
            False,
            {
                (URIRef("https://ontology.unifiedcyberontology.org/example-1"), None),
                (URIRef("https://ontology.unifiedcyberontology.org/example-2"), None),
                (
                    URIRef("https://ontology.unifiedcyberontology.org/example-2"),
                    URIRef("https://ontology.unifiedcyberontology.org/example-2/1/1"),
                ),
            },
        ),
        (
            "examples_uco_qc/owl_Ontology_shape_sparql_imports_XFAIL_validation.ttl",
            False,
            {
                (
                    URIRef("https://ontology.unifiedcyberontology.org/example-1"),
                    URIRef("https://ontology.unifiedcyberontology.org/example-2"),
                ),
                (
                    URIRef("https://ontology.unifiedcyberontology.org/example-2"),
                    URIRef("https://ontology.unifiedcyberontology.org/FOO/example-3"),
                ),
            },
        ),
    ],
)
def test_validation_result(
    filename: str,
    expected_validation_result: bool,
    expected_focus_values: Set[Tuple[URIRef, Optional[URIRef]]],
) -> None:
    graph = Graph()
    graph.parse(filename, format="turtle")

    computed_validation_result: Optional[bool] = None
    for triple in graph.triples((None, SH.conforms, None)):
        assert isinstance(triple[2], Literal)
        computed_validation_result = bool(triple[2])
    assert expected_validation_result == computed_validation_result

    computed_focus_values: Set[Tuple[URIRef, Optional[URIRef]]] = set()
    for result in graph.query(
        """\
SELECT ?nFocusNode ?nValue
WHERE {
  ?nValidationResult sh:focusNode ?nFocusNode .

  OPTIONAL {
    ?nValidationResult sh:value ?nValue .
  }
}
"""
    ):
        assert isinstance(result[0], URIRef)
        assert isinstance(result[1], URIRef) or result[1] is None
        computed_focus_values.add(result)
    assert expected_focus_values == computed_focus_values


def test_bnode_validation_result() -> None:
    graph = Graph()
    graph.parse(
        "examples_uco_owl/owl_ontologyIRI_versionIRI_prerequisite_shape_XFAIL_validation.ttl",
        format="turtle",
    )

    expected_source_shapes: Set[URIRef] = {
        NS_UCO_OWL["ontologyIRI-versionIRI-prerequisite-shape"]
    }
    computed_source_shapes: Set[URIRef] = set()

    computed_validation_result: Optional[bool] = None
    for triple in graph.triples((None, SH.conforms, None)):
        assert isinstance(triple[2], Literal)
        computed_validation_result = bool(triple[2])
    assert computed_validation_result is False

    for triple in graph.triples((None, SH.sourceShape, None)):
        assert isinstance(triple[2], URIRef)
        computed_source_shapes.add(triple[2])
    assert expected_source_shapes == computed_source_shapes
