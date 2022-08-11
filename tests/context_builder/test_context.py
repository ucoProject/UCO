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
from typing import Any, Dict

from rdflib import Graph


def _test_graph_context_query(input_graph_file: str, input_context_file: str) -> None:
    expected = 8
    computed = 0

    context_object: Dict[str, Any]
    with open(input_context_file, "r") as context_fh:
        context_object = json.load(context_fh)

    graph = Graph()
    graph.parse(input_graph_file, context=context_object)
    for result in graph.query("""\
PREFIX uco-action: <https://ontology.unifiedcyberontology.org/uco/action/>
SELECT ?nResult
WHERE {
  ?nAction uco-action:result ?nResult .
}
"""):
        computed += 1

    assert expected == computed


def test_context_concise() -> None:
    _test_graph_context_query("action_result_NO_CONTEXT.json", "context-concise.json")


def test_context_minimal() -> None:
    _test_graph_context_query("action_result_NO_CONTEXT.json", "context-minimal.json")
