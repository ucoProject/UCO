#!python
#
# NOTICE
# This software was produced for the U.S. Government under contract FA8702-22-C-0001,
# and is subject to the Rights in Data-General Clause 52.227-14, Alt. IV (DEC 2007)
# ©2022 The MITRE Corporation. All Rights Reserved.
# Released under PRS 18-4297.
#

"""
Purpose statement

1) json-ld context to support compaction of all IRI base paths through defined
   prefixes
2) json-ld context to support compaction of all property type assertions
3) json-ld context to support assertion of properties with potential
   cardinalities >1 as set arrrays
4) json-ld context to support compaction of json-ld specific key strings @id,
   @type, @value and @graph to simple json key strings id, type, value, and
   graph such that the body of content can be viewed as simple json and the
   context can be utilized to expand it into fully codified json-ld

"""

__version__ = "0.0.1"

import argparse
import logging
import os
import typing
import pathlib
import sys
import re

import rdflib

_logger = logging.getLogger(os.path.basename(__file__))


class ObjectPropertyInfo:
    """Class to hold ObjectProperty info which will be used to build
    context"""

    def __init__(self) -> None:
        self.ns_prefix: typing.Optional[str] = None
        self.root_class_name: typing.Optional[str] = None
        self.shacl_count_lte_1: typing.Optional[bool] = None
        self.shacl_property_bnode = None

    def __get_json(self, hdr: str) -> str:
        json_str = hdr
        json_str += '\t"@type":"@id"'
        if self.shacl_count_lte_1 is not True:
            json_str += ',\n\t"@container":"@set"\n'
        else:
            json_str += "\n"

        json_str += "},\n"
        return json_str

    def get_minimal_json(self) -> str:
        hdr_str = f'"{self.ns_prefix}:{self.root_class_name}":{{\n'
        json_str = self.__get_json(hdr=hdr_str)
        return json_str

    def get_concise_json(self) -> str:
        hdr_str = f'"{self.root_class_name}":{{\n'
        json_str = self.__get_json(hdr=hdr_str)
        return json_str


class DatatypePropertyInfo:
    """Class to hold DatatypeProperty info which will be used to build
    context"""

    def __init__(self) -> None:
        self.ns_prefix: typing.Optional[str] = None
        self.root_property_name: typing.Optional[str] = None
        self.prefixed_datatype_name: typing.Optional[str] = None
        self.shacl_count_lte_1: typing.Optional[bool] = None
        self.shacl_property_bnode = None

    def __get_json(self, hdr: str) -> str:
        json_str = hdr
        json_str += f'\t"@id":"{self.ns_prefix}:{self.root_property_name}"'
        if self.prefixed_datatype_name is not None:
            json_str += ",\n"
            json_str += f'\t"@type":"{self.prefixed_datatype_name}"'
        if self.shacl_count_lte_1 is not True:
            json_str += ',\n\t"@container":"@set"\n'
        else:
            json_str += "\n"
        json_str += "},\n"
        return json_str

    def get_minimal_json(self) -> str:
        hdr_str = f'"{self.ns_prefix}:{self.root_property_name}":{{\n'
        json_str = self.__get_json(hdr=hdr_str)
        return json_str

    def get_concise_json(self) -> str:
        hdr_str = f'"{self.root_property_name}":{{\n'
        json_str = self.__get_json(hdr=hdr_str)
        return json_str


class UCO_Class:
    def __init__(self) -> None:
        self.ns_prefix: typing.Optional[str] = None
        self.root_class_name: typing.Optional[str] = None
        self.prefixed_datatype_name: typing.Optional[str] = None
        self.shacl_count_lte_1: typing.Optional[bool] = None
        self.shacl_property_bnode = None

    def __get_json(self, hdr: str) -> str:
        json_str = hdr
        json_str += f'\t"@id":"{self.ns_prefix}:{self.root_class_name}"'
        json_str += "\n"
        json_str += "},\n"
        return json_str

    def get_minimal_json(self) -> str:
        hdr_str = f'"{self.ns_prefix}:{self.root_class_name}":{{\n'
        json_str = self.__get_json(hdr=hdr_str)
        return json_str

    def get_concise_json(self) -> str:
        hdr_str = f'"{self.root_class_name}":{{\n'
        json_str = self.__get_json(hdr=hdr_str)
        return json_str


class ContextBuilder:
    def __init__(self) -> None:
        self.ttl_file_list: typing.Optional[typing.List[pathlib.Path]] = None
        self.prefix_dict = None
        self.top_srcdir: typing.Optional[pathlib.Path] = None
        self.iri_dict: typing.Optional[typing.Dict[str, str]] = None
        # TODO ERROR MITIGATION: These two dicts should be keyed by IRI (str() cast) rather than IRI fragment.
        self.datatype_properties_dict: typing.Dict[
            str, typing.List[DatatypePropertyInfo]
        ] = dict()
        self.object_properties_dict: typing.Dict[
            str, typing.List[ObjectPropertyInfo]
        ] = dict()
        self.classes_dict: typing.Dict[str, typing.List[ObjectPropertyInfo]] = dict()
        # The string that will hold the processed context
        self.context_str = ""

    def init_context_str(self) -> None:
        self.context_str = '{\n\t"@context":{\n' ""

    def close_context_str(self) -> None:
        self.context_str = self.context_str.strip()
        if self.context_str[-1] == ",":
            self.context_str = self.context_str[:-1]
        self.context_str += "\n\t}\n}"

    def get_ttl_files(
        self, subdirs: typing.List[str] = []
    ) -> typing.List[pathlib.Path]:
        """
        Finds all turtle (.ttl) files in directory structure
        @subdirs - Optional list used to restrict search to particular
        directories.
        """
        # TODO - It seems some of the purpose of get_ttl_files() may be mooted by using tests/uco_monolithic.ttl, a temporary build artifact.

        if self.ttl_file_list is not None:
            return self.ttl_file_list

        # Shamelessly stolen from populate_node_kind.py
        # 0. Self-orient.
        self.top_srcdir = pathlib.Path(os.path.dirname(__file__)) / ".."
        top_srcdir = self.top_srcdir
        # Sanity check.
        assert (
            top_srcdir / ".git"
        ).exists(), "Hard-coded top_srcdir discovery is no longer correct."

        # 1. Load all ontology files into dictionary of graphs.

        # The extra filtering step loop to keep from picking up CI files.
        # Path.glob returns dot files, unlike shell's glob.
        # The uco.ttl file is also skipped because the Python output removes
        # supplementary prefix statements.
        file_list = []
        _logger.debug(top_srcdir)

        if len(subdirs) < 1:
            for x in (top_srcdir).rglob("*.ttl"):
                if ".check-" in str(x):
                    continue
                if "uco.ttl" in str(x):
                    continue
                # _logger.debug(x)
                file_list.append(x)
            self.ttl_file_list = file_list
        else:
            for dir in subdirs:
                for x in (top_srcdir / dir).rglob("*.ttl"):
                    if ".check-" in str(x):
                        continue
                    if "uco.ttl" in str(x):
                        continue
                    # _logger.debug(x)
                    file_list.append(x)
            self.ttl_file_list = file_list

        return self.ttl_file_list

    def get_iris(self) -> typing.List[str]:
        """
        Returns sorted list of IRIs as prefix:value strings
        """
        assert self.iri_dict is not None
        k_list = list(self.iri_dict.keys())
        # print(k_list)
        k_list.sort()
        irs_list = []
        for k in k_list:
            # print(f"\"{k}\":{self.iri_dict[k]}")
            # prepend "uco-" to specific IRIs
            v = self.iri_dict[k]
            # _logger.debug(v.split('/'))
            if ("uco" in v.split("/")) and (
                "ontology.unifiedcyberontology.org" in v.split("/")
            ):
                irs_list.append(f'"uco-{k}":"{v}"')
            else:
                irs_list.append(f'"{k}":"{v}"')
        return irs_list

    def add_prefixes_to_cntxt(self) -> None:
        """Adds detected prefixes to the context string"""
        for i in self.get_iris():
            self.context_str += f"{i},\n"

    def __add_to_iri_dict(self, in_prefix: str) -> None:
        """INTERNAL function: Adds unique key value pairs to dict
        that will be used to generate context. Dies if inconsistent
        key value pair is found.
        @in_prefix - an input prefix triple
        """
        if self.iri_dict is None:
            self.iri_dict = {}

        iri_dict = self.iri_dict
        t_split = in_prefix.split()
        # Taking the ':' off the end of the key
        k = t_split[1][:-1]
        v = t_split[2]
        # Taking the angle brackets off the IRIs
        v = v.strip()[1:-1]
        if k in iri_dict.keys():
            # _logger.debug(f"'{k}' already exists")
            if iri_dict[k] != v:
                _logger.error(f"Mismatched values:\t{iri_dict[k]}!={v}")
                sys.exit()
        else:
            iri_dict[k] = v

    def __process_DatatypePropertiesHelper(self, in_file: str) -> None:
        """
        Does the actual work using rdflib
        @in_file - ttl file to get object properties from
        """
        graph = rdflib.Graph()
        graph.parse(in_file, format="turtle")
        "Make sure to do an itter that looks for rdflib.OWL.class"
        # If we cannot find rdf range, skip
        # If rdf range is a blank node, skip

        # Troubleshooting loop
        for triple in graph.triples(
            # (None, rdflib.RDF.type, rdflib.OWL.DatatypeProperty)
            (None, rdflib.RDF.type, None)
        ):
            _logger.debug(f"Any: {triple}")

        # Troubleshooting loop
        for triple in graph.triples((None, None, rdflib.OWL.DatatypeProperty)):
            _logger.debug(f"Any Owl DatatypeProperty: {triple}")

        for triple in graph.triples(
            (None, rdflib.RDF.type, rdflib.OWL.DatatypeProperty)
        ):
            dtp_obj = DatatypePropertyInfo()
            _logger.debug(triple)
            _logger.debug(triple[0].split("/"))
            s_triple = triple[0].split("/")
            # (rdflib calls this "fragment" rather than root)
            # TODO LIKELY ERROR: This assumes fragments are unique within UCO, which is not true in UCO 0.9.0.
            root = s_triple[-1]
            ns_prefix = f"{s_triple[-3]}-{s_triple[-2]}"
            # print(ns_prefix, root)
            dtp_obj.ns_prefix = ns_prefix
            dtp_obj.root_property_name = root
            for triple2 in graph.triples((triple[0], rdflib.RDFS.range, None)):
                # Testing for Blank Nodes
                if isinstance(triple2[-1], rdflib.term.BNode):
                    _logger.debug(f"\tBlank: {triple2}\n")
                    continue
                _logger.debug(f"\ttriple2: f{triple2}\n")
                rdf_rang_str = str(triple2[-1].n3(graph.namespace_manager))
                dtp_obj.prefixed_datatype_name = rdf_rang_str

            for sh_triple in graph.triples((None, rdflib.SH.path, triple[0])):
                _logger.debug(f"\t\t**sh_triple:{sh_triple}")
                dtp_obj.shacl_property_bnode = sh_triple[0]
                for sh_triple2 in graph.triples(
                    (dtp_obj.shacl_property_bnode, rdflib.SH.maxCount, None)
                ):
                    _logger.debug(f"\t\t***sh_triple:{sh_triple2}")
                    _logger.debug(f"\t\t***sh_triple:{sh_triple2[2]}")
                    if int(sh_triple2[2]) <= 1:
                        if dtp_obj.shacl_count_lte_1 is not None:
                            _logger.debug(
                                f"\t\t\t**MaxCount Double Definition? {triple[0].n3(graph.namespace_manager)}"
                            )
                        dtp_obj.shacl_count_lte_1 = True
                    else:
                        _logger.debug(f"\t\t\t***Large max_count: {sh_triple2[2]}")

            if root in self.datatype_properties_dict.keys():
                _logger.debug(f"None Unique Entry Found:\t {ns_prefix}:{root}")
                self.datatype_properties_dict[root].append(dtp_obj)
            else:
                self.datatype_properties_dict[root] = [dtp_obj]
        return

    def process_DatatypeProperties(self) -> None:
        assert self.ttl_file_list is not None
        for ttl_file in self.ttl_file_list:
            _logger.debug(f"Datatype Processing for {str(ttl_file)}")
            self.__process_DatatypePropertiesHelper(in_file=str(ttl_file))

    def __process_ObjectPropertiesHelper(self, in_file: str) -> None:
        """
        Does the actual work using rdflib
        @in_file - ttl file to get object properties from
        """
        graph = rdflib.Graph()
        graph.parse(in_file, format="turtle")
        # If we cannot find rdf range, skip
        # If rdf range is a blank node, skip
        for triple in graph.triples((None, rdflib.RDF.type, rdflib.OWL.ObjectProperty)):
            op_obj = ObjectPropertyInfo()
            _logger.debug((triple))
            # print(triple[0].split('/'))
            s_triple = triple[0].split("/")
            root = s_triple[-1]
            ns_prefix = f"{s_triple[-3]}-{s_triple[-2]}"
            # print(ns_prefix, root)
            op_obj.ns_prefix = ns_prefix
            op_obj.root_class_name = root

            for sh_triple in graph.triples((None, rdflib.SH.path, triple[0])):
                _logger.debug(f"\t**obj_sh_triple:{sh_triple}")
                op_obj.shacl_property_bnode = sh_triple[0]
                for sh_triple2 in graph.triples(
                    (op_obj.shacl_property_bnode, rdflib.SH.maxCount, None)
                ):
                    _logger.debug(f"\t\t***sh_triple:{sh_triple2}")
                    _logger.debug(f"\t\t***sh_triple:{sh_triple2[2]}")
                    if int(sh_triple2[2]) <= 1:
                        if op_obj.shacl_count_lte_1 is not None:
                            _logger.debug(
                                f"\t\t\t**MaxCount Double Definition? {triple[0].n3(graph.namespace_manager)}"
                            )
                        op_obj.shacl_count_lte_1 = True
                    else:
                        _logger.debug(f"\t\t\t***Large max_count: {sh_triple2[2]}")

            if root in self.object_properties_dict.keys():
                _logger.debug(f"None Unique Entry Found:\t {ns_prefix}:{root}")
                self.object_properties_dict[root].append(op_obj)
            else:
                self.object_properties_dict[root] = [op_obj]
        return

    def __process_ClassesHelper(self, in_file: str) -> None:
        graph = rdflib.Graph()
        graph.parse(in_file, format="turtle")
        # Make sure to do an iter that looks for rdflib.OWL.class"
        # If we cannot find rdf range, skip
        # If rdf range is a blank node, skip
        for triple in graph.triples((None, rdflib.RDF.type, rdflib.OWL.Class)):
            # Skip Blank Nodes
            if isinstance(triple[0], rdflib.term.BNode):
                _logger.debug(f"\tBlank: {triple}\n")
                continue
            c_obj = UCO_Class()
            # print(triple)
            _logger.debug((triple))
            # print(triple[0].split("/"))
            s_triple = triple[0].split("/")
            root = s_triple[-1]
            ns_prefix = f"{s_triple[-3]}-{s_triple[-2]}"
            # print(ns_prefix, root)
            # print(root)
            c_obj.ns_prefix = ns_prefix
            c_obj.root_class_name = root

            # for sh_triple in graph.triples((None, rdflib.SH.path, triple[0])):
            #    _logger.debug(f"\t**obj_sh_triple:{sh_triple}")
            #    op_obj.shacl_property_bnode = sh_triple[0]
            #    for sh_triple2 in graph.triples(
            #        (op_obj.shacl_property_bnode, rdflib.SH.maxCount, None)
            #    ):
            #        _logger.debug(f"\t\t***sh_triple:{sh_triple2}")
            #        _logger.debug(f"\t\t***sh_triple:{sh_triple2[2]}")
            #        if int(sh_triple2[2]) <= 1:
            #            if op_obj.shacl_count_lte_1 is not None:
            #                _logger.debug(
            #                    f"\t\t\t**MaxCount Double Definition? {triple[0].n3(graph.namespace_manager)}"
            #                )
            #            op_obj.shacl_count_lte_1 = True
            #        else:
            #            _logger.debug(f"\t\t\t***Large max_count: {sh_triple2[2]}")

            if root in self.classes_dict.keys():
                _logger.debug(f"None Unique Entry Found:\t {ns_prefix}:{root}")
                print(f"None Unique Entry Found:\t {ns_prefix}:{root}")
                self.classes_dict[root].append(c_obj)
            else:
                self.classes_dict[root] = [c_obj]
        return

    def process_ObjectProperties(self) -> None:
        assert self.ttl_file_list is not None
        for ttl_file in self.ttl_file_list:
            _logger.debug(f"ObjectProperty Processing for {str(ttl_file)}")
            self.__process_ObjectPropertiesHelper(in_file=str(ttl_file))

    def process_Classes(self) -> None:
        assert self.ttl_file_list is not None
        for ttl_file in self.ttl_file_list:
            _logger.debug(f"Class Processing for {str(ttl_file)}")
            self.__process_ClassesHelper(in_file=str(ttl_file))

    def process_prefixes(self) -> None:
        """
        Finds all prefix lines in list of ttl files. Adds them to an
        an internal dict
        """
        ttl_file_list = self.get_ttl_files()
        if len(ttl_file_list) < 1:
            _logger.error("No ttls files to process")
            sys.exit()

        for ttl_file in ttl_file_list:
            with open(ttl_file, "r") as file:
                for line in file:
                    if re.search("^@prefix", line):
                        _logger.debug(f"Prefix: {ttl_file}\t{line.strip()}")
                        self.__add_to_iri_dict(in_prefix=line.strip())

    def add_minimal_datatype_props_to_cntxt(self) -> None:
        """Adds Datatype Properties to context string"""
        dtp_str_sect = ""
        dt_list = list(self.datatype_properties_dict.keys())
        dt_list.sort()
        # last_dtp_obj = self.datatype_properties_dict[dt_list[-1]][-1]
        for key in dt_list:
            for dtp_obj in self.datatype_properties_dict[key]:
                dtp_str_sect += dtp_obj.get_minimal_json()
        self.context_str += dtp_str_sect

    def add_concise_datatype_props_to_cntxt(self) -> None:
        """Adds Datatype Properties to context string"""
        dtp_str_sect = ""
        dtp_list = list(self.datatype_properties_dict.keys())
        dtp_list.sort()
        for key in dtp_list:
            if len(self.datatype_properties_dict[key]) > 1:
                for dtp_obj in self.datatype_properties_dict[key]:
                    dtp_str_sect += dtp_obj.get_minimal_json()
            else:
                for dtp_obj in self.datatype_properties_dict[key]:
                    dtp_str_sect += dtp_obj.get_concise_json()
        self.context_str += dtp_str_sect

    def add_minimal_object_props_to_cntxt(self) -> None:
        """Adds Object Properties to context string"""
        op_str_sect = ""
        op_list = list(self.object_properties_dict.keys())
        op_list.sort()
        for key in op_list:
            for op_obj in self.object_properties_dict[key]:
                op_str_sect += op_obj.get_minimal_json()
        self.context_str += op_str_sect

    def add_concise_object_props_to_cntxt(self) -> None:
        """Adds Object Properties to context string"""
        op_str_sect = ""
        op_list = list(self.object_properties_dict.keys())
        op_list.sort()
        for key in op_list:
            if len(self.object_properties_dict[key]) > 1:
                for op_obj in self.object_properties_dict[key]:
                    # print(op_obj.ns_prefix, op_obj.root_class_name)
                    op_str_sect += op_obj.get_minimal_json()
            else:
                for op_obj in self.object_properties_dict[key]:
                    op_str_sect += op_obj.get_concise_json()
        self.context_str += op_str_sect

    def add_key_strings_to_cntxt(self) -> None:
        """Adds id, type, and graph key strings to context string"""
        ks_str = ""
        ks_str += '\t"id":"@id",\n'
        ks_str += '\t"type":"@type",\n'
        ks_str += '\t"value":"@value",\n'
        ks_str += '\t"graph":"@graph",\n'

        self.context_str += ks_str

    def add_concise_classes_to_cntxt(self) -> None:
        """Adds classes to context string"""
        c_sect_str = ""
        c_list = list(self.classes_dict.keys())
        c_list.sort()

        for key in c_list:
            if len(self.classes_dict[key]) > 1:
                # print(f"M:{self.classes_dict[key]}")
                for c_obj in self.classes_dict[key]:
                    c_sect_str += c_obj.get_minimal_json()
            else:
                # print(f"S:{self.classes_dict[key]}")
                for c_obj in self.classes_dict[key]:
                    c_sect_str += c_obj.get_concise_json()
        self.context_str += c_sect_str


def main() -> None:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--debug", action="store_true")
    argument_parser.add_argument(
        "--concise",
        action="store_true",
        help='Creates a "concise" context. This is more compact than the \
        default behavior which creates a "minimal" context',
    )
    argument_parser.add_argument(
        "-o",
        "--output",
        help="Output file for context.\
         Will print to stdout by default.",
    )
    args = argument_parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    _logger.debug("\t***Debug Mode enabled***")

    out_f = None
    if args.output is not None:
        out_f = open(args.output, "w")

    cb = ContextBuilder()
    for i in cb.get_ttl_files(subdirs=["ontology"]):
        _logger.debug(f" Input ttl: {i}")

    cb.process_prefixes()
    cb.process_DatatypeProperties()
    cb.process_ObjectProperties()
    cb.init_context_str()
    cb.add_prefixes_to_cntxt()
    if args.concise:
        # Note there is classes are not in minimal context
        cb.process_Classes()
        cb.add_concise_classes_to_cntxt()
        cb.add_concise_object_props_to_cntxt()
        cb.add_concise_datatype_props_to_cntxt()
    else:
        cb.add_minimal_object_props_to_cntxt()
        cb.add_minimal_datatype_props_to_cntxt()
    cb.add_key_strings_to_cntxt()
    cb.close_context_str()

    if out_f is not None:
        out_f.write(cb.context_str)
        out_f.flush()
        out_f.close()
    else:
        print(cb.context_str)

    return


if __name__ == "__main__":
    main()
