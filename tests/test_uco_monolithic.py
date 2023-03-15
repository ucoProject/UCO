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

import logging
import os
from typing import Generator, List, Optional, Set, Tuple, Union

import pytest
import rdflib.plugins.sparql.processor
from rdflib import BNode, Graph, Literal, Namespace, OWL, RDF, RDFS, SH, URIRef
from rdflib.term import Node

IdentifiedNode = Union[BNode, URIRef]

NS_UCO_CORE = Namespace("https://ontology.unifiedcyberontology.org/uco/core/")


@pytest.fixture(scope="module")
def graph() -> Generator[Graph, None, None]:
    graph = Graph()
    graph.parse(os.path.join(os.path.dirname(__file__), "uco_monolithic.ttl"))
    assert len(graph) > 0, "Failed to load uco_monolithic.ttl."
    yield graph


def test_rdf_design_vocabularies_defined(graph: Graph) -> None:
    """
    This test performs a typo review of RDF-, RDFS-, and OWL-namespaced concepts.

    The mechanism used is rdflib's ClosedNamespace.  The imported
    objects RDF, RDFS, and OWL are instances of this Python class.
    """

    expected: Set[URIRef] = set()  # This set is intentionally empty.
    computed: Set[URIRef] = set()

    concepts_used: Set[URIRef] = set()
    for triple in graph.triples((None, None, None)):
        for triple_member in triple:
            if not isinstance(triple_member, URIRef):
                continue
            concepts_used.add(triple_member)

    OWL_str = str(OWL)
    RDF_str = str(RDF)
    RDFS_str = str(RDFS)
    SH_str = str(SH)

    def _concept_in_design_vocabulary(concept: URIRef) -> Optional[bool]:
        """
        Return True -> Concept is defined in some design vocabulary.
        Return False -> Concept is not defined in design vocabulary.
        Return None -> N/A.
        """
        design_vocabulary: Namespace
        if concept.startswith(OWL_str):
            concept_fragment = concept.replace(OWL_str, "")
            design_vocabulary = OWL
        elif concept.startswith(RDF_str):
            concept_fragment = concept.replace(RDF_str, "")
            design_vocabulary = RDF
        elif concept.startswith(RDFS_str):
            concept_fragment = concept.replace(RDFS_str, "")
            design_vocabulary = RDFS
        elif concept.startswith(SH_str):
            concept_fragment = concept.replace(SH_str, "")
            design_vocabulary = SH
        else:
            return None

        try:
            _ = design_vocabulary[concept_fragment]
        except AttributeError:
            return False

    assert (
        _concept_in_design_vocabulary(
            URIRef(
                "http://www.w3.org/2002/07/owl#NonExistentConcept-f287fb8b-433b-45a2-82b8-9b53bfa35c64"
            )
        )
        is False
    ), "ClosedNamespace functionality used in this test did not detect a known-erroneous value.  This test needs revising."

    for concept_used in concepts_used:
        if _concept_in_design_vocabulary(concept_used) is False:
            computed.add(concept_used)

    assert expected == computed


def test_max_1_sh_datatype_per_property_shape(graph: Graph) -> None:
    """
    This enforces the maximum sh:datatype count of 1, as specified here:

    "A shape has at most one value for sh:datatype."
    https://www.w3.org/TR/shacl/#DatatypeConstraintComponent

    This is encoded in the SHACL ontology with the statement 'sh:DatatypeConstraintComponent-datatype sh:maxCount 1 .'
    """
    expected: Set[Tuple[URIRef, URIRef, Literal]] = set()  # This set is intentionally empty.
    computed: Set[Tuple[URIRef, URIRef, Literal]] = set()

    nsdict = {
      "sh": rdflib.SH
    }

    query_object = rdflib.plugins.sparql.processor.prepareQuery("""\
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


def rdf_list_to_member_list(graph: Graph, n_list: IdentifiedNode) -> List[Node]:
    """
    Recursive convert RDF list to Python Node list, from tail-back.
    """
    default_retval: List[Node] = []
    if n_list == RDF.nil:
        return default_retval

    n_first: Optional[Node] = None
    n_rest: Optional[IdentifiedNode] = None

    for triple0 in graph.triples((n_list, RDF.first, None)):
        n_first = triple0[2]
    if n_first is None:
        return default_retval

    for triple1 in graph.triples((n_list, RDF.rest, None)):
        assert isinstance(triple1[2], (BNode, URIRef))
        n_rest = triple1[2]
    assert n_rest is not None

    rest_of_list = rdf_list_to_member_list(graph, n_rest)
    rest_of_list.insert(0, n_first)
    return rest_of_list


def test_semi_open_vocabulary_owl_shacl_alignment(graph: Graph) -> None:
    """
    This test enforces that when a DatatypeProperty following the "Semi-open vocabulary" design of UCO 0.8.0 is used, that its SHACL shape's enumerant list matches the rdfs:Datatype's enumerant list.
    """
    # A member of these sets is a class's IRI, its semi-open vocabulary's IRI, the list in the SHACL shape, and the list in the Datatype.
    # (The type of the lists is a Tuple because a Set in Python cannot contain a List.)
    # The expected set intentionally has length 0.
    expected: Set[Tuple[URIRef, URIRef, Tuple[Node, ...], Tuple[Node, ...]]] = set()
    computed: Set[Tuple[URIRef, URIRef, Tuple[Node, ...], Tuple[Node, ...]]] = set()

    query = """
SELECT ?nClass ?nDatatype ?nShaclList ?nRdfsList
WHERE {
  ?nClass
    sh:property / sh:or / rdf:rest* / rdf:first ?nMemberCheckShape ;
    .
  ?nMemberCheckShape
    sh:datatype ?nDatatype ;
    sh:in ?nShaclList ;
    .
  ?nDatatype
    a rdfs:Datatype ;
    owl:equivalentClass ?nLexicalSpace ;
    .

  ?nLexicalSpace
    owl:oneOf ?nRdfsList ;
    .
}
"""
    result_tally = 0
    test_cases: Set[Tuple[URIRef, URIRef, IdentifiedNode, IdentifiedNode]] = set()
    for (result_no, result) in enumerate(graph.query(query)):
        result_tally = result_no + 1
        assert isinstance(result[0], URIRef)
        assert isinstance(result[1], URIRef)
        if isinstance(result[2], URIRef) and isinstance(result[3], URIRef):
            assert result[2] == result[3]
        else:
            assert isinstance(result[2], (BNode, URIRef))
            assert isinstance(result[3], (BNode, URIRef))
        test_cases.add(result)
    assert result_tally > 0, "Pattern for semi-open vocabularies is no longer aligned with test."

    for test_case in test_cases:
        n_shacl_list = test_case[2]
        n_rdfs_list = test_case[3]

        if n_shacl_list is n_rdfs_list:
            # No point in doing any comparison work.
            continue

        shacl_list = rdf_list_to_member_list(graph, n_shacl_list)
        rdfs_list = rdf_list_to_member_list(graph, n_rdfs_list)
        if rdfs_list == shacl_list:
            logging.debug("Match")
        else:
            logging.debug(n_shacl_list)
            logging.debug(n_rdfs_list)
            shacl_tuple = tuple(shacl_list)
            rdfs_tuple = tuple(rdfs_list)
            computed.add((test_case[0], test_case[1], shacl_tuple, rdfs_tuple))

    assert expected == computed


def test_only_one_uco_class_is_owl_thing_direct_subclass(graph: Graph) -> None:
    """
    UCO expects all classes defined in UCO namespaces (i.e. excluding the "import review" ontologies) are subclasses of core:UcoThing.  Within OWL, absence of an rdfs:subClassOf statement implies being a subclass of owl:Thing.  Review UCO for any accidental omission of rdfs:subClassOf.
    """
    expected: Set[URIRef] = {NS_UCO_CORE.UcoThing}
    computed: Set[URIRef] = set()

    # Create temporary graph where subClassOf statements for non-UCO classes are removed.
    # This narrows the subclass hierarchy review to UCO-namespaced concepts only.
    tmp_graph = Graph()
    drop_graph = Graph()
    tmp_graph += graph
    for triple in graph.triples((None, RDFS.subClassOf, None)):
        assert isinstance(triple[1], URIRef)
        if not isinstance(triple[0], URIRef):
            continue
        if not isinstance(triple[2], URIRef):
            continue
        if not str(triple[2]).startswith("https://ontology.unifiedcyberontology.org/uco/"):
            drop_graph.add(triple)
    tmp_graph -= drop_graph

    for result in tmp_graph.query("""\
SELECT ?nClass
WHERE {
    {
        ?nClass rdfs:subClassOf owl:Thing .
    }
    UNION
    {
        ?nClass a owl:Class .
        FILTER NOT EXISTS {
            ?nClass rdfs:subClassOf ?nOtherClass .
        }
    }
    FILTER isIRI(?nClass)
}
"""):
        n_class: URIRef = result[0]
        if not str(n_class).startswith("https://ontology.unifiedcyberontology.org/uco/"):
            continue
        computed.add(n_class)
    assert expected == computed
