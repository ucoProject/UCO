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

import json
import logging
from typing import Any, Dict, Set

from rdflib import Graph, RDF, RDFS
from rdflib.term import Node


def _test_action_graph_context_query(input_graph_file: str, input_context_file: str) -> None:
    expected = 8
    computed = 0

    context_object: Dict[str, Any]
    with open(input_context_file, "r") as context_fh:
        context_object = json.load(context_fh)

    graph = Graph()
    graph.parse(input_graph_file, context=context_object)

    # The graph should at least include 8 statements of the form
    # 'x uco-action:result y .'  Actual length includes the rdfs:comment
    # and type declarations, but is otherwise unimportant.
    assert 8 < len(graph), "Graph failed to parse into triples."

    # The rdf:types must be supported by the context parse.
    count_of_types = 0
    for triple in graph.triples((None, RDF.type, None)):
        count_of_types += 1
    assert 0 < count_of_types, "Graph failed to parse non-UCO concept from RDF."

    # The rdfs:comment must be supported by the context parse.
    count_of_comments = 0
    for triple in graph.triples((None, RDFS.comment, None)):
        count_of_comments += 1
    assert 0 < count_of_comments, "Graph failed to parse non-UCO concept from RDFS."

    for result in graph.query("""\
PREFIX uco-action: <https://ontology.unifiedcyberontology.org/uco/action/>
SELECT ?nResult
WHERE {
  ?nAction uco-action:result ?nResult .
}
"""):
        computed += 1
    for triple in sorted(graph.triples((None, None, None))):
        logging.debug(triple)
    try:
        assert expected == computed
    except AssertionError:
        # Provide a debug dump of the graph before forwarding assertion error.
        for triple in sorted(graph.triples((None, None, None))):
            logging.debug(triple)
        raise


def test_action_context_concise() -> None:
    _test_action_graph_context_query("action_result_NO_CONTEXT_concise.json", "context-concise.json")


def test_action_context_minimal() -> None:
    _test_action_graph_context_query("action_result_NO_CONTEXT_minimal.json", "context-minimal.json")


def _test_graph_context_independent_match(input_dependent_graph_file: str, input_context_file: str, input_independent_graph_file: str) -> None:
    """
    Run an exact-parse-match test, confirming that the triples found in a file that does not depend on a context dictionary matches a JSON-LD file that does depend on a context dictionary.

    :param input_dependent_graph_file: File that depends on externally-supplied context dictionary to function.
    :param input_context_file: Context dictionary file.
    :param input_independent_graph_file: File that does not depend on externally-supplied context dictionary to function.
    """

    expected: Set[Tuple[Node, Node, Nonde]] = set()
    computed: Set[Tuple[Node, Node, Nonde]] = set()

    expected_graph = Graph()
    computed_graph = Graph()

    expected_graph.parse(input_independent_graph_file)

    context_object: Dict[str, Any]
    with open(input_context_file, "r") as context_fh:
        context_object = json.load(context_fh)

    computed_graph.parse(input_dependent_graph_file, context=context_object)

    for expected_triple in expected_graph:
        expected.add(expected_triple)

    for computed_triple in computed_graph:
        computed.add(computed_triple)

    assert expected == computed


def test_hash_context_concise() -> None:
    _test_graph_context_independent_match("hash_NO_CONTEXT_concise.json", "context-concise.json", "hash_expanded.json")


def test_hash_context_minimal() -> None:
    _test_graph_context_independent_match("hash_NO_CONTEXT_minimal.json", "context-minimal.json", "hash_expanded.json")


def test_thread_context_concise() -> None:
    _test_graph_context_independent_match("thread_NO_CONTEXT_concise.json", "context-concise.json", "../examples/thread_PASS.json")


def test_thread_context_minimal() -> None:
    _test_graph_context_independent_match("thread_NO_CONTEXT_minimal.json", "context-minimal.json", "../examples/thread_PASS.json")


#def test_context_concise2() -> None:
#    _test_graph_context_query("action_result_concise_NO_CONTEXT.json", "context-concise.json")


# def test_device_context_concise() -> None:
#   _test_graph_context_query("device_NO_CONTEXT.json", "context-concise.json")
 
# def test_device_context_minimal() -> None:
#    _test_graph_context_query("device_NO_CONTEXT.json", "context-minimal.json")
