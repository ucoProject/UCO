#!/usr/bin/make -f

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
The purpose of this program is to build definition statements in a SHACL ontology, such that sh:PropertyShapes record the rdfs:range defined on the property definition.

The program's current intent is as a single-purpose utility.  Usage:
1. Be in a Python environment that has rdflib installed.  (This could be done by enabling the virtual environment under ../tests/venv.)
2. Run this program.  It will **overwrite** all ontology files matching the pattern ../uco-*/*.ttl.
3. Re-run 'make check' from the root directory, to re-normalize ontology files.

The outline of this program is:
1. Load all ontology files into dictionary of graphs, keyed by relpath from top_srcdir.
2. Store all property-defining rdf:type and rdfs:range triples from all loaded ontologies into a "properties" graph.
3. For each ontology (by relpath):
   3.1 CONSTRUCT triples for each PropertyShape, based on property being ObjectProperty or DatatypeProperty.
       3.1.1 DatatypeProperty -> sh:nodeKind = sh:Literal
       3.1.2 DatatypeProperty -> sh:datatype = (rdfs:range of property, if an IRI[1])
       3.1.3 ObjectProperty -> sh:nodeKind = sh:BlankNodeOrIRI
       3.1.4 ObjectProperty -> sh:class = (rdfs:range of property, if an IRI[1])
       [1] If a property's rdfs:range is a blank node, currently this script does NOT generate a sh:datatype or sh:class constraint, due to needing to address ontology design issues.
"""

__version__ = "0.1.0"

import argparse
import logging
import os
import pathlib
import typing

import rdflib.plugins.sparql

_logger = logging.getLogger(os.path.basename(__file__))

NS_OWL = rdflib.OWL
NS_RDF = rdflib.RDF
NS_RDFS = rdflib.RDFS
NS_SH = rdflib.SH

def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--debug", action="store_true")
    argument_parser.add_argument("--dry-run", action="store_true", help="Count updates, but do not overwrite ontology files.")
    args = argument_parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    # 0. Self-orient.
    top_srcdir = pathlib.Path(os.path.dirname(__file__)) / ".."

    # Sanity check.
    assert (top_srcdir / ".git").exists(), "Hard-coded top_srcdir discovery is no longer correct."

    # 1. Load all ontology files into dictionary of graphs.

    # The extra filtering step loop to keep from picking up CI files.  Path.glob returns dot files, unlike shell's glob.
    # The uco.ttl file is also skipped because the Python output removes supplementary prefix statements.
    ontology_filepaths : typing.List[pathlib.Path] = []
    for x in top_srcdir.glob("uco-*/*.ttl"):
        if ".check-" in str(x):
            continue
        if "uco.ttl" in str(x):
            continue
        ontology_filepaths.append(x)
    assert len(ontology_filepaths) > 0, "Hard-coded relative paths to ontology files is no longer correct."

    filepath_to_graph : typing.Dict[pathlib.Path, rdflib.Graph] = dict()

    for ontology_filepath in sorted(ontology_filepaths):
        _logger.debug("Loading %s...", ontology_filepath)
        filepath_to_graph[ontology_filepath] = rdflib.Graph()
        ontology_filepath_str = str(ontology_filepath)
        filepath_to_graph[ontology_filepath].parse(ontology_filepath_str, format=rdflib.util.guess_format(ontology_filepath_str))
        _logger.debug("Loaded.")

    # Build global nsdict.
    nsdict = dict()
    for ontology_filepath in sorted(filepath_to_graph.keys()):
        tmp_nsdict = {k:v for (k,v) in filepath_to_graph[ontology_filepath].namespace_manager.namespaces()}
        for key in tmp_nsdict:
            if key in nsdict:
                try:
                    assert nsdict[key] == tmp_nsdict[key]
                except:
                    _logger.error("ontology_filepath = %s.", ontology_filepath)
                    _logger.error("key = %r.", key)
                    _logger.error("nsdict[key] = %r.", nsdict[key])
                    _logger.error("tmp_nsdict[key] = %r.", tmp_nsdict[key])
                    raise
            nsdict[key] = tmp_nsdict[key]

    # 2. Store all property-defining rdf:type and rdfs:range triples from all loaded ontologies into a "properties" graph.

    properties_graph = rdflib.Graph()
    _logger.debug("Building properties graph...")
    for ontology_filepath in sorted(filepath_to_graph.keys()):
        for n_type_value in [NS_OWL.DatatypeProperty, NS_OWL.ObjectProperty]:
            for triple_0 in filepath_to_graph[ontology_filepath].triples((
              None,
              NS_RDF.type,
              n_type_value
            )):
                properties_graph.add(triple_0)
                for triple_1 in filepath_to_graph[ontology_filepath].triples((
                  triple_0[0],
                  NS_RDFS.range,
                  None
                )):
                    properties_graph.add(triple_1)
    _logger.debug("Built.")

    #3. For each ontology (by relpath):
    #   3.1 CONSTRUCT triples for each PropertyShape, based on property being ObjectProperty or DatatypeProperty.

    #       3.1.0.1 DatatypeProperty, rdfs:range a bnode -> Warn.
    select_datatype_range_bnode_query = rdflib.plugins.sparql.prepareQuery("""\
SELECT ?nNodeShape ?nPath
WHERE {
  ?nNodeShape
    a sh:NodeShape ;
    sh:property ?nPropertyShape ;
    .

  ?nPropertyShape
    sh:path ?nPath ;
    .

  ?nPath
    a owl:DatatypeProperty ;
    rdfs:range ?nRange ;
    .

  FILTER isBlank(?nRange)
}
""", initNs=nsdict)

    #       3.1.0.2 ObjectProperty, rdfs:range a bnode -> Warn.
    select_object_range_bnode_query = rdflib.plugins.sparql.prepareQuery("""\
SELECT ?nNodeShape ?nPath
WHERE {
  ?nNodeShape
    a sh:NodeShape ;
    sh:property ?nPropertyShape ;
    .

  ?nPropertyShape
    sh:path ?nPath ;
    .

  ?nPath
    a owl:ObjectProperty ;
    rdfs:range ?nRange ;
    .

  FILTER isBlank(?nRange)
}
""", initNs=nsdict)

    #       3.1.1 DatatypeProperty -> sh:nodeKind = sh:Literal
    #       3.1.2 DatatypeProperty -> sh:datatype = (rdfs:range of property)
    construct_datatype_property_query = rdflib.plugins.sparql.prepareQuery("""\
CONSTRUCT {
  ?nPropertyShape
    sh:datatype ?nRange ;
    sh:nodeKind sh:Literal ;
    .
}
WHERE {
  ?nNodeShape
    a sh:NodeShape ;
    sh:property ?nPropertyShape ;
    .

  ?nPropertyShape
    sh:path ?nPath ;
    .

  ?nPath
    a owl:DatatypeProperty ;
    .

  OPTIONAL {
    ?nPath
      rdfs:range ?nRange ;
      .

    FILTER isIRI(?nRange)
  }
}
""", initNs=nsdict)

    #       3.1.3 ObjectProperty -> sh:nodeKind = sh:BlankNodeOrIRI
    #       3.1.4 ObjectProperty -> sh:class = (rdfs:range of property) (NOT performed currently)
    construct_object_property_query = rdflib.plugins.sparql.prepareQuery("""\
CONSTRUCT {
  ?nPropertyShape
    sh:class ?nRange ;
    sh:nodeKind sh:BlankNodeOrIRI ;
    .
}
WHERE {
  ?nNodeShape
    a sh:NodeShape ;
    sh:property ?nPropertyShape ;
    .

  ?nPropertyShape
    sh:path ?nPath ;
    .

  ?nPath
    a owl:ObjectProperty ;
    .

  OPTIONAL {
    ?nPath
      rdfs:range ?nRange ;
      .
      FILTER isIRI(?nRange)
  }
}
""", initNs=nsdict)

    for ontology_filepath in sorted(filepath_to_graph.keys()):
        _logger.debug("Augmenting %s...", ontology_filepath)

        _logger.debug("len(base_graph) = %d.", len(filepath_to_graph[ontology_filepath]))

        base_and_properties_graph = properties_graph + filepath_to_graph[ontology_filepath]
        _logger.debug("len(base_and_properties_graph) = %d.", len(base_and_properties_graph))

        constructed_graph = rdflib.Graph()

        _logger.debug("Finding datatype properties with blank nodes as ranges ...")
        num_found = 0
        for result in base_and_properties_graph.query(select_datatype_range_bnode_query):
            (n_node_shape, n_path) = result
            _logger.warning("n_node_shape = %s.", n_node_shape)
            _logger.warning("n_path = %s.", n_path)
            num_found += 1
        if num_found == 0:
            _logger.debug("None found.")
        else:
            _logger.warning("%d datatype properties with blank nodes as ranges found, and will not receive sh:datatype constraints.", num_found)

        _logger.debug("Finding object properties with blank nodes as ranges ...")
        num_found = 0
        for result in base_and_properties_graph.query(select_object_range_bnode_query):
            (n_node_shape, n_path) = result
            _logger.error("n_node_shape = %s.", n_node_shape)
            _logger.error("n_path = %s.", n_path)
            num_found += 1
        if num_found == 0:
            _logger.debug("None found.")
        else:
            _logger.error("%d object properties with blank nodes as ranges found, and will not receive sh:class constraints.", num_found)

        for result in base_and_properties_graph.query(construct_datatype_property_query):
            constructed_graph.add(result)
        _logger.debug("len(constructed_graph (+d)) = %d.", len(constructed_graph))

        for result in base_and_properties_graph.query(construct_object_property_query):
            constructed_graph.add(result)
        _logger.debug("len(constructed_graph (+o)) = %d.", len(constructed_graph))

        filepath_to_graph[ontology_filepath] += constructed_graph
        _logger.debug("len(base_graph) = %d.", len(filepath_to_graph[ontology_filepath]))

        if not args.dry_run:
            filepath_to_graph[ontology_filepath].serialize(str(ontology_filepath), format="turtle")

        _logger.debug("Augmented.")

if __name__ == "__main__":
    main()
