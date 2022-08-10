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
This module creates a graph object that provides a basic UCO characterization of a single file.  The gathered metadata is among the more "durable" file characteristics, i.e. characteristics that would remain consistent when transferring a file between locations.
"""

__version__ = "0.3.2"

import argparse
import datetime
import hashlib
import logging
import os
import typing
import warnings

import rdflib  # type: ignore

import uco_utils
from uco_utils.namespace import (
    NS_RDF,
    NS_UCO_CORE,
    NS_UCO_OBSERVABLE,
    NS_UCO_TYPES,
    NS_UCO_VOCABULARY,
    NS_XSD,
)

DEFAULT_PREFIX = "http://example.org/kb/"

# Shortcut syntax for defining an immutable named tuple is noted here:
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
# via the "See also" box here: https://docs.python.org/3/library/collections.html#collections.namedtuple
class HashDict(typing.NamedTuple):
    filesize: int
    md5: str
    sha1: str
    sha256: str
    sha512: str


def create_file_node(
    graph: rdflib.Graph,
    filepath: str,
    node_iri: typing.Optional[str] = None,
    node_prefix: str = DEFAULT_PREFIX,
    disable_hashes: bool = False,
    disable_mtime: bool = False,
) -> rdflib.URIRef:
    r"""
    This function characterizes the file at filepath.

    :param graph: The rdflib Graph that will house the new triples characterizing the file.
    :type graph: rdflib.Graph

    :param filepath: The path to the file to characterize.  Can be relative or absolute.
    :type filepath: str

    :param node_iri: The desired full IRI for the node.  If absent, will make an IRI of the pattern ``ns_base + 'file-' + uuid4``
    :type node_iri: str

    :param node_prefix: The base prefix to use if node_iri is not supplied.
    :type node_prefix: str

    :param disable_hashes: Skip computing hashes.
    :type disable_hashes: bool

    :param disable_mtime: Skip recording mtime.
    :type disable_mtime: bool

    :returns: The File Observable Object's node.
    :rtype: rdflib.URIRef
    """
    if node_iri is None:
        node_slug = "file-" + uco_utils.local_uuid.local_uuid()
        node_iri = rdflib.Namespace(node_prefix)[node_slug]
    n_file = rdflib.URIRef(node_iri)
    graph.add((n_file, NS_RDF.type, NS_UCO_OBSERVABLE.File))

    basename = os.path.basename(filepath)
    literal_basename = rdflib.Literal(basename)

    file_stat = os.stat(filepath)
    n_file_facet = rdflib.BNode()
    graph.add(
        (
            n_file_facet,
            NS_RDF.type,
            NS_UCO_OBSERVABLE.FileFacet,
        )
    )
    graph.add((n_file_facet, NS_UCO_OBSERVABLE.fileName, literal_basename))
    graph.add(
        (
            n_file_facet,
            NS_UCO_OBSERVABLE.sizeInBytes,
            rdflib.Literal(int(file_stat.st_size)),
        )
    )
    graph.add((n_file, NS_UCO_CORE.hasFacet, n_file_facet))

    if not disable_mtime:
        mtime_datetime = datetime.datetime.fromtimestamp(
            file_stat.st_mtime, tz=datetime.timezone.utc
        )
        str_mtime = mtime_datetime.isoformat()
        literal_mtime = rdflib.Literal(str_mtime, datatype=NS_XSD.dateTime)
        graph.add((n_file_facet, NS_UCO_OBSERVABLE.modifiedTime, literal_mtime))

    if not disable_hashes:
        n_contentdata_facet = rdflib.BNode()
        graph.add((n_file, NS_UCO_CORE.hasFacet, n_contentdata_facet))
        graph.add(
            (n_contentdata_facet, NS_RDF.type, NS_UCO_OBSERVABLE.ContentDataFacet)
        )

        # Compute hashes until they are re-computed and match once.  (This is a lesson learned from working with a NAS that had a subtly faulty network cable.)

        successful_hashdict: typing.Optional[HashDict] = None
        last_hashdict: typing.Optional[HashDict] = None
        for attempt_no in [0, 1, 2, 3]:
            # Hash file's contents.
            # This hashing logic was partially copied from DFXML's walk_to_dfxml.py.
            md5obj = hashlib.md5()
            sha1obj = hashlib.sha1()
            sha256obj = hashlib.sha256()
            sha512obj = hashlib.sha512()
            stashed_error = None
            byte_tally = 0
            with open(filepath, "rb") as in_fh:
                chunk_size = 2**22
                while True:
                    buf = b""
                    try:
                        buf = in_fh.read(chunk_size)
                        byte_tally += len(buf)
                    except Exception as e:
                        stashed_error = e
                        buf = b""
                    if buf == b"":
                        break
                    md5obj.update(buf)
                    sha1obj.update(buf)
                    sha256obj.update(buf)
                    sha512obj.update(buf)
            if stashed_error is not None:
                raise stashed_error
            current_hashdict = HashDict(
                byte_tally,
                md5obj.hexdigest(),
                sha1obj.hexdigest(),
                sha256obj.hexdigest(),
                sha512obj.hexdigest(),
            )
            if last_hashdict == current_hashdict:
                successful_hashdict = current_hashdict
                break
            else:
                last_hashdict = current_hashdict
        del last_hashdict
        del current_hashdict
        if successful_hashdict is None:
            raise ValueError("Failed to confirm hashes of file %r." % filepath)
        if successful_hashdict.filesize != file_stat.st_size:
            # TODO - Discuss with AC whether this should be something stronger, like an assertion error.
            warnings.warn(
                "Inode file size and hashed file sizes disagree: %d vs. %d."
                % (file_stat.st_size, successful_hashdict.filesize)
            )
        # TODO - Discuss whether this property should be recorded even if hashes are not attempted.
        graph.add(
            (
                n_contentdata_facet,
                NS_UCO_OBSERVABLE.sizeInBytes,
                rdflib.Literal(successful_hashdict.filesize),
            )
        )

        # Add confirmed hashes into graph.
        for key in successful_hashdict._fields:
            if key not in ("md5", "sha1", "sha256", "sha512"):
                continue
            n_hash = rdflib.BNode()
            graph.add((n_contentdata_facet, NS_UCO_OBSERVABLE.hash, n_hash))
            graph.add((n_hash, NS_RDF.type, NS_UCO_TYPES.Hash))
            graph.add(
                (
                    n_hash,
                    NS_UCO_TYPES.hashMethod,
                    rdflib.Literal(
                        key.upper(), datatype=NS_UCO_VOCABULARY.HashNameVocab
                    ),
                )
            )
            hash_value = getattr(successful_hashdict, key)
            graph.add(
                (
                    n_hash,
                    NS_UCO_TYPES.hashValue,
                    rdflib.Literal(hash_value.upper(), datatype=NS_XSD.hexBinary),
                )
            )

    return n_file


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-prefix", default=DEFAULT_PREFIX)
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("--disable-hashes", action="store_true")
    parser.add_argument("--disable-mtime", action="store_true")
    parser.add_argument(
        "--output-format", help="Override extension-based format guesser."
    )
    parser.add_argument("out_graph")
    parser.add_argument("in_file")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    uco_utils.local_uuid.configure()

    NS_BASE = rdflib.Namespace(args.base_prefix)

    graph = rdflib.Graph()
    graph.namespace_manager.bind("kb", NS_BASE)
    graph.namespace_manager.bind("uco-core", NS_UCO_CORE)
    graph.namespace_manager.bind("uco-observable", NS_UCO_OBSERVABLE)
    graph.namespace_manager.bind("uco-types", NS_UCO_TYPES)
    graph.namespace_manager.bind("uco-vocabulary", NS_UCO_VOCABULARY)
    graph.namespace_manager.bind("xsd", NS_XSD)

    output_format = None
    if args.output_format is None:
        output_format = rdflib.util.guess_format(args.out_graph)
    else:
        output_format = args.output_format

    serialize_kwargs: typing.Dict[str, typing.Any] = {"format": output_format}
    if output_format == "json-ld":
        context_dictionary = {k: v for (k, v) in graph.namespace_manager.namespaces()}
        serialize_kwargs["context"] = context_dictionary

    node_iri = NS_BASE["file-" + uco_utils.local_uuid.local_uuid()]
    create_file_node(
        graph,
        args.in_file,
        node_iri=node_iri,
        node_prefix=args.base_prefix,
        disable_hashes=args.disable_hashes,
        disable_mtime=args.disable_mtime,
    )

    graph.serialize(args.out_graph, **serialize_kwargs)


if __name__ == "__main__":
    main()
