#!/usr/bin/env python3

# Portions of this file contributed by NIST are governed by the
# following statement:
#
# This software was developed at the National Institute of Standards
# and Technology by employees of the Federal Government in the course
# of their official duties. Pursuant to Title 17 Section 105 of the
# United States Code, this software is not subject to copyright
# protection within the United States. NIST assumes no responsibility
# whatsoever for its use by other parties, and makes no guarantees,
# expressed or implied, about its quality, reliability, or any other
# characteristic.
#
# We would appreciate acknowledgement if the software is used.

"""
This program constructs a catalog-v001.xml file, initially implemented
to satisfy local-file needs of the Protégé ontology editor.  The
resulting catalog file lets a user of the XML file interact with their
ontology, even spread across multiple files, without requesting network
resources.  This is beneficial, for instance, in tracking local edits to
resources otherwise stored online.  It is also beneficial when networked
resources are not available, such as due to service interruptions or
link rot.

One catalog-v001.xml file will generally support only its housing
directory in a source code hierarchy.  The catalog file is built to make
relative path references to every OWL-imported IRI in the transitive
import closure of all of the ontology graph files in the directory.
Once the catalog file is generated, a user should be able to open a
sibling graph file in the same directory and have Protégé load without
making network requests for ontology graphs.
"""

__version__ = "0.1.0"

import argparse
import csv
import logging
import os
import xml.etree.ElementTree as ETree
from pathlib import Path
from typing import Dict, List, Set, Tuple
from xml.dom import minidom

from rdflib import OWL, RDF, Graph, URIRef

NS_OWL = OWL
NS_RDF = RDF


# XML prolog, as generated by Protégé.
XML_VERSION_INFO = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true")
    parser.add_argument(
        "--catalog-xml",
        help="A generated catalog-v001.xml file for some dependent or imported ontology.  This should be supplied for ontologies not covered by the dependency_files_tsv argument, nor meant to be crawled upon using domain_directories_tsv.  (For instance, this could be used to import relative file references for ontologies tracked as Git submodules.)",
        action="append",
    )
    # "x" mode - exclusive creation.
    # https://docs.python.org/3/library/functions.html#open
    parser.add_argument("out_xml", type=argparse.FileType("x"))
    parser.add_argument(
        "domain_directories_tsv",
        help="A two-column file, with column 1 being a string prefix in-common to ontology prefix IRIs, and column 2 being a file system directory relative to top_srcdir that is the root directory housing that ontology's files.  Directories specified in this file will be recursively walked to discover ontology graph files.  This file may be empty, but it must exist.",
        type=argparse.FileType("r"),
    )
    parser.add_argument(
        "dependency_files_tsv",
        help="A two-column file, with column 1 being an ontology reference IRI (ontology IRI or version IRI), and column 2 being a local, version-controlled file relative to top_srcdir that houses the corresponding ontology data.  This file may be empty, but it must exist.",
        type=argparse.FileType("r"),
    )
    parser.add_argument("top_srcdir", help="The root directory of the Git repository for this ontology.  In the two TSV arguments, the variable top_srcdir is substituted with this value.")
    parser.add_argument(
        "in_ttl",
        help="Input graph files.  Due to the target use case of Protégé Catalog files, these are required to be in the same directory.",
        nargs="+",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    top_srcdir_abspath = Path(args.top_srcdir).resolve()
    if not top_srcdir_abspath.exists():
        raise FileNotFoundError(args.top_srcdir)
    if not top_srcdir_abspath.is_dir():
        raise NotADirectoryError(args.top_srcdir)
    logging.debug("top_srcdir_abspath = %r.", top_srcdir_abspath)

    focus_graph = Graph()

    focus_graph_srcdir_abspaths: Set[Path] = set()
    for in_ttl in args.in_ttl:
        focus_graph_abspath = Path(in_ttl).resolve()
        focus_graph.parse(str(focus_graph_abspath))
        focus_graph_srcdir_abspaths.add(focus_graph_abspath.parent)
    if len(focus_graph_srcdir_abspaths) > 1:
        for focus_graph_srcdir_abspath_no, focus_graph_srcdir_abspath in enumerate(
            sorted(focus_graph_srcdir_abspaths)
        ):
            logging.error(
                "%d: %s",
                1 + focus_graph_srcdir_abspath_no,
                str(focus_graph_srcdir_abspath),
            )
        raise ValueError(
            "Input graphs are required to be in the same directory.  Found them in %d directories."
            % len(focus_graph_srcdir_abspaths)
        )
    focus_graph_srcdir_abspath = sorted(focus_graph_srcdir_abspaths)[0]

    top_srcdir_relpath = Path(
        os.path.relpath(top_srcdir_abspath, focus_graph_srcdir_abspath)
    )
    logging.debug("top_srcdir_relpath = %r.", top_srcdir_relpath)

    # Determine focus ontology IRIs.
    n_focus_ontologies: Set[URIRef] = set()
    for triple in focus_graph.triples((None, NS_RDF.type, NS_OWL.Ontology)):
        if isinstance(triple[0], URIRef):
            n_focus_ontologies.add(triple[0])
    if len(n_focus_ontologies) < 1:
        raise ValueError("Found no focus ontology IRI.")

    # Free focus-graph memory.
    del focus_graph

    # Read TSV to get domain prefixes' housing directories.
    ontology_string_prefix_to_domain_directory: Dict[str, Path] = dict()
    reader = csv.reader(args.domain_directories_tsv, delimiter="\t")
    for row in reader:
        ontology_string_prefix = row[0]
        domain_directory_str = row[1].replace("${top_srcdir}", str(top_srcdir_abspath))
        domain_directory = Path(domain_directory_str)
        if not domain_directory.exists():
            raise FileNotFoundError(domain_directory_str)
        if not domain_directory.is_dir():
            raise NotADirectoryError(domain_directory_str)
        ontology_string_prefix_to_domain_directory[
            ontology_string_prefix
        ] = domain_directory
    logging.debug(
        "ontology_string_prefix_to_domain_directory = %r.",
        ontology_string_prefix_to_domain_directory,
    )

    # Walk domain directories to associate ontology reference IRIs with backing files, and to build imports graph.
    #
    # Definition, possibly specialized to just this script:
    # An "ontology reference IRI" is either an ontology IRI or a versionIRI of an ontology.
    imports_graph = Graph()
    n_ontology_reference_to_backing_file: Dict[URIRef, Path] = dict()

    def _load_graph(graph_file_path: Path) -> None:
        tmp_graph = Graph()
        logging.debug("graph_file_path = %r.", graph_file_path)
        tmp_graph.parse(str(graph_file_path))
        for triple in tmp_graph.triples((None, NS_RDF.type, NS_OWL.Ontology)):
            assert isinstance(triple[0], URIRef)
            n_ontology_reference_to_backing_file[triple[0]] = graph_file_path
            imports_graph.add(triple)
        for triple in tmp_graph.triples((None, NS_OWL.imports, None)):
            imports_graph.add(triple)
        for triple in tmp_graph.triples((None, NS_OWL.versionIRI, None)):
            assert isinstance(triple[2], URIRef)
            n_ontology_reference_to_backing_file[triple[2]] = graph_file_path
            imports_graph.add(triple)

    # Do deep walk for domain directories.
    for domain_directory in ontology_string_prefix_to_domain_directory.values():
        for dirpath, dirnames, filenames in os.walk(str(domain_directory)):
            for filename in filenames:
                # Skip build files (syntax normalization checks).
                if filename.startswith("."):
                    continue
                # Restrict to Turtle files.
                if not filename.endswith(".ttl"):
                    continue
                dirpath_path = Path(dirpath)
                graph_filepath = dirpath_path / filename
                _load_graph(graph_filepath)
    # Do direct imports from dependency file map.
    reader = csv.reader(args.dependency_files_tsv, delimiter="\t")
    for row in reader:
        logging.debug("row = %r.", row)
        n_ontology_reference = URIRef(row[0])
        graph_file_name = row[1].replace("${top_srcdir}", str(top_srcdir_abspath))
        graph_file_path = Path(graph_file_name)
        if not graph_file_path.exists():
            raise FileNotFoundError(graph_file_path)
        if graph_file_path.is_dir():
            raise IsADirectoryError(graph_file_path)
        n_ontology_reference_to_backing_file[n_ontology_reference] = graph_file_path
        _load_graph(graph_file_path)
    # Inherit prior catalog files.
    catalog_paths: Set[Path] = set()
    if args.catalog_xml:
        for catalog_file_name in args.catalog_xml:
            catalog_path = Path(catalog_file_name).resolve()
            logging.debug("catalog_path = %r.", catalog_path)
            if not catalog_path.exists():
                raise FileNotFoundError(catalog_file_name)
            if catalog_path.name != "catalog-v001.xml":
                logging.error("catalog_file_name = %r.", catalog_file_name)
                raise FileNotFoundError(
                    'Expecting catalog file to be named "catalog-v001.xml".'
                )
            catalog_paths.add(catalog_path)
    for catalog_path in sorted(catalog_paths):
        logging.debug("catalog_path = %r.", catalog_path)
        catalogued_directory_path = catalog_path.parent
        # Load graph files accompanying this catalog-v001.xml.
        for file_path in catalogued_directory_path.iterdir():
            file_basename = file_path.name
            # Skip build files (syntax normalization checks).
            if file_basename.startswith("."):
                continue
            # Restrict to Turtle files.
            if not file_basename.endswith(".ttl"):
                continue
            _load_graph(catalog_path)
        # Use catalog-v001.xml to find further graph files.
        tree = ETree.parse(catalog_path)
        for child in tree.getroot():
            logging.debug("child.attrib = %r.", child.attrib)
            logging.debug("child.tag = %r.", child.tag)
            if child.tag != "{urn:oasis:names:tc:entity:xmlns:xml:catalog}uri":
                continue
            if child.attrib["uri"].startswith("http:"):
                continue
            if child.attrib["uri"].startswith("https:"):
                continue
            if child.attrib["uri"].startswith("urn:"):
                continue
            n_ontology_reference = URIRef(child.attrib["name"])
            backing_ontology_path = catalogued_directory_path / child.attrib["uri"]
            logging.debug("backing_ontology_path = %r.", backing_ontology_path)
            if not backing_ontology_path.exists():
                logging.info(
                    "catalogued_directory_path = %r.", catalogued_directory_path
                )
                logging.info('child.attrib["uri"] = %r.', child.attrib["uri"])
                raise FileNotFoundError("Unable to find referenced ontology file.")
            if not backing_ontology_path.is_file():
                logging.info(
                    "catalogued_directory_path = %r.", catalogued_directory_path
                )
                logging.info('child.attrib["uri"] = %r.', child.attrib["uri"])
                raise ValueError("Referenced ontology file path is not regular file.")
            n_ontology_reference_to_backing_file[
                n_ontology_reference
            ] = backing_ontology_path.resolve()
            _load_graph(backing_ontology_path)

    logging.debug("len(imports_graph) = %d.", len(imports_graph))
    if args.debug:
        logging.debug("n_ontology_reference_to_backing_file:")
        for n_ontology_reference in sorted(n_ontology_reference_to_backing_file.keys()):
            logging.debug(
                "%r -> %r.",
                n_ontology_reference,
                n_ontology_reference_to_backing_file[n_ontology_reference],
            )

    n_imported_iri_to_relative_backing_path: Dict[URIRef, Path] = dict()

    def _map_n_ontology_reference(n_ontology_reference: URIRef) -> None:
        logging.debug("n_ontology_reference = %r.", n_ontology_reference)
        ontology_reference_backing_file_abspath = n_ontology_reference_to_backing_file[
            n_ontology_reference
        ]
        ontology_reference_backing_file_relpath = Path(
            os.path.relpath(
                ontology_reference_backing_file_abspath, focus_graph_srcdir_abspath
            )
        )
        n_imported_iri_to_relative_backing_path[
            n_ontology_reference
        ] = ontology_reference_backing_file_relpath
        n_imported_iris: Set[URIRef] = set()
        for result in imports_graph.query(
            """\
SELECT ?nImportIRI
WHERE {
  {
    ?nOntologyReference
      owl:imports+ ?nImportIRI ;
      .
  }
  UNION
  {
    ?nOntology
      owl:imports+ ?nImportIRI ;
      owl:versionIRI ?nOntologyReference ;
      .
  }
}
""",
            initBindings={"nOntologyReference": n_ontology_reference},
        ):
            assert isinstance(result[0], URIRef)
            n_imported_iri = result[0]
            n_imported_iris.add(n_imported_iri)
        # Handle base case - cut mapped nodes.
        logging.debug("n_imported_iris = %r.", n_imported_iris)
        n_imported_unvisited_iris = n_imported_iris - {
            x for x in n_imported_iri_to_relative_backing_path.keys()
        }
        logging.debug("n_imported_unvisited_iris = %r.", n_imported_unvisited_iris)
        # Recurse, because owl:imports could have a versionIRI as its object.
        for n_imported_unvisited_iri in n_imported_unvisited_iris:
            _map_n_ontology_reference(n_imported_unvisited_iri)

    for n_focus_ontology in n_focus_ontologies:
        _map_n_ontology_reference(n_focus_ontology)

    if args.debug:
        logging.debug("n_imported_iri_to_relative_backing_path:")
        for n_imported_iri in sorted(n_imported_iri_to_relative_backing_path.keys()):
            logging.debug(
                "* %r -> %r.",
                n_imported_iri,
                n_imported_iri_to_relative_backing_path[n_imported_iri],
            )

    # Create catalog XML tree.
    xml_root = ETree.Element("catalog")

    # Mimic attributes for the root node from exemplar generated by Protégé.
    xml_root.attrib = {
        "prefer": "public",
        "xmlns": "urn:oasis:names:tc:entity:xmlns:xml:catalog",
    }
    # Sort catalog entries by relative file path, again mimicing Protégé behavior.
    catalog_entries: List[Tuple[str, str]] = sorted(
        [
            (
                str(n_imported_iri_to_relative_backing_path[n_ontology_reference]),
                str(n_ontology_reference),
            )
            for n_ontology_reference in n_imported_iri_to_relative_backing_path.keys()
        ]
    )
    for catalog_entry in catalog_entries:
        e_child = ETree.SubElement(xml_root, "uri")
        e_child.attrib = {
            "id": "User Entered Import Resolution",
            "uri": catalog_entry[0],
            "name": catalog_entry[1],
        }
    xml_tree_string = minidom.parseString(
        ETree.tostring(xml_root, encoding="utf-8", method="xml").decode("utf-8")
    ).toprettyxml(indent="    ")
    args.out_xml.write(f"{XML_VERSION_INFO}\n")
    args.out_xml.write(f"{xml_tree_string[23:]}")

    return


if __name__ == "__main__":
    main()
