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

import typing

import pytest
import rdflib

NS_UCO_CORE = rdflib.Namespace("https://ontology.unifiedcyberontology.org/uco/core/")
NS_UCO_OBSERVABLE = rdflib.Namespace("https://ontology.unifiedcyberontology.org/uco/observable/")

NSDICT = {
    "core": NS_UCO_CORE,
    "observable": NS_UCO_OBSERVABLE,
    "skos": rdflib.SKOS
}

@pytest.fixture
def mime_pass_graph() -> rdflib.Graph:
    graph = rdflib.Graph()
    graph.parse("mime_PASS.json", format="json-ld")
    return graph


def test_mime_file_names(mime_pass_graph: rdflib.Graph) -> None:
    expected: typing.Set[str] = {
        "1.gz",
        "2.gz",
        "3.tar",
        "4.tar.gz",
        "5.dat",
        "6.dat",
    }
    computed: typing.Set[str] = set()

    query = rdflib.plugins.sparql.prepareQuery("""\
SELECT ?lFileName
WHERE {
  ?nFile core:hasFacet/observable:fileName ?lFileName .
}
""", initNs=NSDICT)
    for result in mime_pass_graph.query(query):
        computed.add(str(result[0]))
    assert expected == computed


def test_mime_gzip_files(mime_pass_graph: rdflib.Graph) -> None:
    expected: typing.Set[str] = {
        "1.gz",
        "2.gz",
        "4.tar.gz",
    }
    computed: typing.Set[str] = set()

    query = rdflib.plugins.sparql.prepareQuery("""\
SELECT ?lFileName
WHERE {
  ?nFile core:hasFacet/observable:fileName ?lFileName .
  ?nFile core:hasFacet/observable:mimeType ?nMimeType .

  ?nMimeType skos:exactMatch*/skos:broader*/skos:notation "application/gzip" .
}
""", initNs=NSDICT)
    for result in mime_pass_graph.query(query):
        computed.add(str(result[0]))
    assert expected == computed



def test_mime_tar_files(mime_pass_graph: rdflib.Graph) -> None:
    expected: typing.Set[str] = {
        "3.tar",
        "4.tar.gz",
    }
    computed: typing.Set[str] = set()

    query = rdflib.plugins.sparql.prepareQuery("""\
SELECT ?lFileName
WHERE {
  ?nFile core:hasFacet/observable:fileName ?lFileName .
  ?nFile core:hasFacet/observable:mimeType ?nMimeType .

  ?nMimeType skos:exactMatch*/skos:broader*/skos:notation "application/tar" .
}
""", initNs=NSDICT)
    for result in mime_pass_graph.query(query):
        computed.add(str(result[0]))
    assert expected == computed
