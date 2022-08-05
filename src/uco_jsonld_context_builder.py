#
# Release Statement?
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
from multiprocessing import context
import os
import typing
import pathlib
import sys
import re
import rdflib
from rdflib.namespace import Namespace, NamespaceManager

_logger = logging.getLogger(os.path.basename(__file__))

class ObjectPropertyInfo:
    """Class to hold ObjectProperty info which will be used to build context"""
    def __init__(self):
        self.ns_prefix = None
        self.root_class_name = None
        self.shacl_count_lte_1 = False

class DatatypePropertyInfo:
    """Class to hold DatatypeProperty info which will be used to build context"""
    def __init__(self):
        self.ns_prefix = None
        self.root_property_name = None
        self.prefixed_datatype_name = None
        self.shacl_count_lte_1 = False
    

class ContextBuilder:
    def __init__(self):
        self.ttl_file_list=None
        self.prefix_dict=None
        self.top_srcdir=None
        self.iri_dict=None
        #A dict of DataTypePropertyInfo Objects
        self.datatype_properties_dict={}
        #A dict of ObjectPropertyInfo Objects
        self.object_properties_dict={}
        #The string that will hold the processed context
        self.context_str = ""

    def init_context_str(self) -> None:
        self.context_str="{\n\t\"@context\":{\n"""

    def close_context_str(self) -> None:
        self.context_str=self.context_str.strip()
        if self.context_str[-1] == ',':
            self.context_str=self.context_str[:-1]
        self.context_str+="\n\t}\n}"

    def get_ttl_files(self, subdirs=[]) -> list:
        """
        Finds all turtle (.ttl) files in directory structure
        @subdirs - Optional list used to restrict search to particular directories.
        """
        if self.ttl_file_list is not None:
            return self.ttl_file_list

        #Shamelessly stolen from populate_node_kind.py
        # 0. Self-orient.
        self.top_srcdir = pathlib.Path(os.path.dirname(__file__)) / ".."
        top_srcdir=self.top_srcdir
        # Sanity check.
        assert (top_srcdir / ".git").exists(), "Hard-coded top_srcdir discovery is no longer correct."

        # 1. Load all ontology files into dictionary of graphs.

        # The extra filtering step loop to keep from picking up CI files.  Path.glob returns dot files, unlike shell's glob.
        # The uco.ttl file is also skipped because the Python output removes supplementary prefix statements.
        ontology_filepaths : typing.List[pathlib.Path] = []

        file_list=[]
        _logger.debug(top_srcdir)

        if len(subdirs) < 1:
            for x in (top_srcdir).rglob("*.ttl"):
                if ".check-" in str(x):
                    continue
                if "uco.ttl" in str(x):
                    continue
                #_logger.debug(x)
                file_list.append(x)
            self.ttl_file_list=file_list
        else:
            for dir in subdirs:
                for x in (top_srcdir / dir).rglob("*.ttl"):
                    if ".check-" in str(x):
                        continue
                    if "uco.ttl" in str(x):
                        continue
                    #_logger.debug(x)
                    file_list.append(x)
                self.ttl_file_list=file_list

        return self.ttl_file_list

    def get_iris(self)->list:
        """
        Returns sorted list of IRIs as prefix:value strings
        """
        k_list=list(self.iri_dict.keys())
        #print(k_list)
        k_list.sort()
        irs_list=[]
        for k in k_list:
            #print(f"\"{k}\":{self.iri_dict[k]}")
            irs_list.append(f"\"{k}\":\"{self.iri_dict[k]}\"")
        return irs_list

    def add_prefixes_to_cntxt(self) -> None:
        """Adds detected prefixes to the context string"""
        for i in self.get_iris():
            self.context_str+=f"{i},\n"

    def __add_to_iri_dict(self, in_prefix):
        """INTERNAL function: Adds unique key value pairs to dict
        that will be used to generate context. Dies if inconsistent
        key value pair is found.
        @in_prefix - an input prefix triple
        """
        if self.iri_dict is None:
            self.iri_dict={}

        iri_dict = self.iri_dict
        t_split=in_prefix.split()
        #Taking the ':' off the end of the key
        k=t_split[1][:-1]
        v=t_split[2]
        if k in iri_dict.keys():
            #_logger.debug(f"'{k}' already exists")
            if iri_dict[k]!=v:
                _logger.error(f"Mismatched values:\t{iri_dict[k]}!={v}")
                sys.exit()
        else:
            iri_dict[k]=v

    def __process_DatatypePropertiesHelper(self, in_file=None):
        """
        Does the actual work using rdflib
        @in_file - ttl file to get object properties from
        """
        graph = rdflib.Graph()
        graph.parse(in_file, format="turtle")
        "Make sure to do an itter that looks for rdflib.OWL.class"
        #If we cannot find rdf range, skip
        #If rdf range is a blank node, skip
        for triple in graph.triples((None,rdflib.RDF.type,rdflib.OWL.DatatypeProperty)):
            dtp_obj = DatatypePropertyInfo()
            #print(triple)
            #print(triple[0].split('/'))
            s_triple=triple[0].split('/')
            root=s_triple[-1]
            ns_prefix=f"{s_triple[-3]}-{s_triple[-2]}"
            #print(ns_prefix, root)
            dtp_obj.ns_prefix=ns_prefix
            dtp_obj.root_property_name=root
            for triple2 in graph.triples((triple[0],rdflib.RDFS.range, None)):
                #Testing for Blank Nodes
                if isinstance(triple2[-1],rdflib.term.BNode):
                    continue
                rdf_rang_str = str(triple2[-1].n3(graph.namespace_manager))
                dtp_obj.prefixed_datatype_name=rdf_rang_str
                #if str(rdf_rang_str) not in test_list:
                #    test_list.append(rdf_rang_str)
            

            if root in self.datatype_properties_dict.keys():
                _logger.debug(f"None Unique Entry Found:\t {ns_prefix}:{root}")
                self.datatype_properties_dict[root].append(dtp_obj)
            else:
                self.datatype_properties_dict[root]=[dtp_obj]
        return
    
    def process_DatatypeProperties(self):
        for ttl_file in self.ttl_file_list:
            self.__process_DatatypePropertiesHelper(in_file=ttl_file)

    def __process_ObjectPropertiesHelper(self, in_file=None):
        """
        Does the actual work using rdflib
        @in_file - ttl file to get object properties from
        """
        graph = rdflib.Graph()
        graph.parse(in_file, format="turtle")
        #Make sure to do an iter that looks for rdflib.OWL.class"
        #If we cannot find rdf range, skip
        #If rdf range is a blank node, skip
        for triple in graph.triples((None,rdflib.RDF.type,rdflib.OWL.ObjectProperty)):
            op_obj = ObjectPropertyInfo()
            #print(triple)
            #print(triple[0].split('/'))
            s_triple=triple[0].split('/')
            root=s_triple[-1]
            ns_prefix=f"{s_triple[-3]}-{s_triple[-2]}"
            #print(ns_prefix, root)
            op_obj.ns_prefix=ns_prefix
            op_obj.root_class_name=root
            
            #for triple2 in graph.triples((triple[0],rdflib.RDFS.range, None)):
            #    #Testing for Blank Nodes
            #    if isinstance(triple2[-1],rdflib.term.BNode):
            #        continue
            #    rdf_rang_str = str(triple2[-1].n3(graph.namespace_manager))
            #    print(f"\t{rdf_rang_str}")
            #    op_obj.prefixed_datatype_name=rdf_rang_str
            #    #if str(rdf_rang_str) not in test_list:
            #    #    test_list.append(rdf_rang_str)
            

            if root in self.object_properties_dict.keys():
                _logger.debug(f"None Unique Entry Found:\t {ns_prefix}:{root}")
                self.object_properties_dict[root].append(op_obj)
            else:
                self.object_properties_dict[root]=[op_obj]
        return
    
    def process_ObjectProperties(self):
        for ttl_file in self.ttl_file_list:
            self.__process_ObjectPropertiesHelper(in_file=ttl_file)

    def process_prefixes(self):
        """
        Finds all prefix lines in list of ttl files. Adds them to an
        an internal dict
        """
        ttl_file_list = self.get_ttl_files()
        if len(ttl_file_list) < 1:
            _logger.error("No ttls files to process")
            sys.exit()
        
        for ttl_file in ttl_file_list:
            with open(ttl_file,'r') as file:
                for line in file:
                    if re.search("^\@prefix",line):
                        #_logger.debug(line.strip())
                        self.__add_to_iri_dict(in_prefix=line.strip())

    def print_minimal_datatype_properties(self)->str:
        """Prints DataType Properties in a format suitable for the contect"""
        dtp_str_sect=""
        dt_list = list(self.datatype_properties_dict.keys())
        dt_list.sort()
        last_dtp_obj = self.datatype_properties_dict[dt_list[-1]][-1]
        for key in dt_list:
            #if len(cb.datatype_properties_dict[key]) > 1:
            for dtp_obj in self.datatype_properties_dict[key]:
                con_str=f"\"{dtp_obj.ns_prefix}:{dtp_obj.root_property_name}\":{{\n"
                con_str+=f"\t\"@id\":\"{dtp_obj.ns_prefix}:{dtp_obj.root_property_name}\""
                if (dtp_obj.prefixed_datatype_name is not None):
                    con_str+=",\n"
                    con_str+=f"\t\"@type\":\"{dtp_obj.prefixed_datatype_name}\"\n"
                else:
                    con_str+="\n"
                if dtp_obj != last_dtp_obj:
                    con_str+="},\n"
                else:
                    con_str+="}\n"
                #print(dtp_obj.root_property_name)
                #print(con_str)
                dtp_str_sect+=con_str
        #print(dtp_str_sect)
        return(dtp_str_sect)

    def add_minimal_datatype_props_to_cntxt(self) -> None:
        """Adds Datatype Properties to context string"""
        dtp_str_sect=""
        dt_list = list(self.datatype_properties_dict.keys())
        dt_list.sort()
        #last_dtp_obj = self.datatype_properties_dict[dt_list[-1]][-1]
        for key in dt_list:
            for dtp_obj in self.datatype_properties_dict[key]:
                con_str=f"\"{dtp_obj.ns_prefix}:{dtp_obj.root_property_name}\":{{\n"
                con_str+=f"\t\"@id\":\"{dtp_obj.ns_prefix}:{dtp_obj.root_property_name}\""
                if (dtp_obj.prefixed_datatype_name is not None):
                    con_str+=",\n"
                    con_str+=f"\t\"@type\":\"{dtp_obj.prefixed_datatype_name}\"\n"
                else:
                    con_str+="\n"
                con_str+="},\n"
                
                dtp_str_sect+=con_str

        self.context_str+=dtp_str_sect

    def add_minimal_object_props_to_cntxt(self) -> None:
        """Adds Object Properties to context string"""
        op_str_sect=""
        op_list = list(self.object_properties_dict.keys())
        op_list.sort()
        for key in op_list:
            for op_obj in self.object_properties_dict[key]:
                con_str=f"\"{op_obj.ns_prefix}:{op_obj.root_class_name}\":{{\n"
                con_str+="\t\"@type\":\"@id\"\n"
                con_str+="},\n"
                
                op_str_sect+=con_str
        self.context_str+=op_str_sect

    def add_key_strings_to_cntxt(self) -> None:
        """Adds id, type, and graph key strings to context string"""
        ks_str=""
        ks_str+="\t\"uco-core:id\":\"@id\",\n"
        ks_str+="\t\"uco-core:type\":\"@type\",\n"
        ks_str+="\t\"value\":\"@value\",\n"
        ks_str+="\t\"graph\":\"@graph\",\n"

        self.context_str+=ks_str
        



def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('--debug', action="store_true")
    #argument_parser.add_argument('-i', '--in_graph', help="Input graph to be simplified")
    args = argument_parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    _logger.debug("Debug Mode enabled")
    
    cb = ContextBuilder()
    for i in (cb.get_ttl_files(subdirs=['ontology'])):
        _logger.debug(f" Input ttl: {i}")
    
    cb.process_prefixes()
    cb.process_DatatypeProperties()
    cb.process_ObjectProperties()
    cb.init_context_str()
    cb.add_prefixes_to_cntxt()
    cb.add_minimal_object_props_to_cntxt()
    cb.add_minimal_datatype_props_to_cntxt()
    cb.add_key_strings_to_cntxt()
    cb.close_context_str()
    print(cb.context_str)


    return
    #cb.print_minimal_datatype_properties()

    dt_list = list(cb.datatype_properties_dict.keys())
    dt_list.sort()
    last_dtp_obj = cb.datatype_properties_dict[dt_list[-1]][-1]
    for key in dt_list:
        #if len(cb.datatype_properties_dict[key]) > 1:
        for dtp_obj in cb.datatype_properties_dict[key]:
            con_str=f"\"{dtp_obj.ns_prefix}:{dtp_obj.root_property_name}\":{{\n"
            con_str+=f"\t\"@id\":\"{dtp_obj.ns_prefix}:{dtp_obj.root_property_name}\""
            if (dtp_obj.prefixed_datatype_name is not None):
                con_str+=",\n"
                con_str+=f"\t\"@type\":\"{dtp_obj.prefixed_datatype_name}\"\n"
            else:
                con_str+="\n"
            if dtp_obj != last_dtp_obj:
                con_str+="},\n"
            else:
                con_str+="}\n"
            print(dtp_obj.root_property_name)
            print(con_str)
        #else:
        #    dtp_obj = cb.datatype_properties_dict[key][0]
        #    con_str=f"\"{dtp_obj.ns_prefix}:{dtp_obj.root_property_name}\":{{\n"
        #    con_str+=f"\t\"@id\":\"{dtp_obj.ns_prefix}:{dtp_obj.root_property_name}\"\n"
        #    con_str+=f"\t\"@type\":\"{dtp_obj.prefixed_datatype_name}\"\n"
        #    con_str+="}"


    """Come back to this for concise output""
    for key in dt_list:
        #Non-unique roots
        if len(cb.datatype_properties_dict[key]) > 1:
            print(f"{key}:{cb.datatype_properties_dict[key]}")
            for ns in cb.datatype_properties_dict[key]:
                con_str=f"\"{ns}:{key}\":{{"
                con_str+="\n\t\"@id\":\"%s:%s\"," % (ns,key)
                con_str+="\n\t\"@type\":\"@id\""
                con_str+="\n\t},"
                print(con_str)
        #Unique roots
        else:
            pass   
    """
    return
    #from pprint import pprint
    #pprint(cb.datatype_properties_dict)
    #context keyword in graph parse and graph serialize
    #black formater FLAKE8 for isort
    #check the case-uilities python

    graph = rdflib.Graph()
    graph.parse("../tests/uco_monolithic.ttl", format="turtle")
    "Make sure to do an itter that looks for rdflib.OWL.class"
    limit = 4
    count = 0
    for triple in graph.triples((None,rdflib.RDF.type,rdflib.OWL.DatatypeProperty)):
        print(triple[0].fragment)
        print(triple[0].n3(graph.namespace_manager))
        print(triple)
        count += 1
        if count >= limit:
            sys.exit()
    
    #print(f"{args.in_graph}")
    #g = rdflib.Graph()
    #g.parse(args.in_graph, format="turtle")
    #g.serialize("temp.json-ld", format="json-ld")


if __name__ == "__main__":
    main()
