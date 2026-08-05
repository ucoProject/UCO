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
   @type, @value and @graph to simple json key strings id, type, value, and graph such that the body of content can be viewed as simple json and the context can be utilized to expand it into fully codified json-ld

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

_logger = logging.getLogger(os.path.basename(__file__))

"""
 27 def main():                                                                                                                                                     
 28     g = rdflib.Graph()                                                                                                                                          
 29     for in_graph in args.in_graph:                                                                                                                              
 30         g.parse(in_graph, format="turtle")                                                                                                                      
 31     g.serialize(args.out_graph, format="turtle") 
"""

class context_builder:
    def __init__(self):
        self.ttl_file_list=None
        self.prefix_dict=None
        self.top_srcdir=None
        self.iri_dict=None
        self.datatype_properties_dict={}

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
        Returns sorted list of IRIs 
        """
        k_list=list(self.iri_dict.keys())
        #print(k_list)
        k_list.sort()
        irs_list=[]
        for k in k_list:
            #print(f"\"{k}\":{self.iri_dict[k]}")
            irs_list.append(f"\"{k}\":{self.iri_dict[k]}")
        return irs_list

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
        #limit = 4
        #count = 0
        for triple in graph.triples((None,rdflib.RDF.type,rdflib.OWL.DatatypeProperty)):
            print(triple)
            print(triple[0].split('/'))
            s_triple=triple[0].split('/')
            root=s_triple[-1]
            ns_prefix=f"{s_triple[-3]}-{s_triple[-2]}"
            print(ns_prefix, root)

            if root in self.datatype_properties_dict.keys():
                print(f"None Unique Entry Found:\t {ns_prefix}:{root}")
                self.datatype_properties_dict[root].append(ns_prefix)
            else:
                self.datatype_properties_dict[root]=[ns_prefix]

        return
            #count += 1
            #if count >= limit:
            #    return
    
    def process_DatatypeProperties(self):
        for ttl_file in self.ttl_file_list:
            self.__process_DatatypePropertiesHelper(in_file=ttl_file)

    def get_prefixes(self):
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



def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('--debug', action="store_true")
    #argument_parser.add_argument('-i', '--in_graph', help="Input graph to be simplified")
    args = argument_parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    _logger.debug("Debug Mode enabled")
    
    cb = context_builder()
    for i in (cb.get_ttl_files(subdirs=['ontology'])):
        _logger.debug(f" Input ttl: {i}")
    
    cb.get_prefixes()
    #for i in cb.get_iris():
    #    print(i)
    
    cb.process_DatatypeProperties()

"""
If we cannot find rdf range, skip
if rdf range is a blank node, skip
"""
    dt_list = list(cb.datatype_properties_dict.keys())
    dt_list.sort()
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

    #from pprint import pprint
    #pprint(cb.datatype_properties_dict)
    graph = rdflib.Graph()
    graph.parse("../tests/uco_monolithic.ttl", format="turtle")
    graph.serialize("_uco_monolithic.json-ld", format="json-ld")
    graph.serialize("_uco_monolithic.json-ld", format="json-ld")
    sys.exit()
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
