#!python
#
# NOTICE
# This software was produced for the U.S. Government under contract
# FA8702-22-C-0001, and is subject to the Rights in Data-General
# Clause 52.227-14, Alt. IV (DEC 2007) 
# 
# ©2022 The MITRE Corporation. All Rights Reserved.
# Released under PRS 18-4297.
#


import argparse
import json
import rdflib
import subprocess
import os


def main() -> None:

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--skip-clean",  action="store_true",
        help="Keeps intermediate test files instead of \
        automatic deletion")	
    arg_parser.add_argument("--input",  default="action_result_NO_CONTEXT_minimal.json",
        help="input file for testing")	
    arg_parser.add_argument('--concise', action="store_true",
        help="Perform testing on \"concise\" context instead of \"minimal\"")
    args = arg_parser.parse_args()    

    # Test graph file in JSON format
    # test_file = "action_result_NO_CONTEXT_minimal.json"
    test_file = args.input
    # File to which context will be written
    output_file = "_temp_cntxt.json"
    # Serialization of graph without using context
    # no_cntxt_out = "_test_out_no_cntxt.json-ld"
    no_cntxt_out = f"_out_no_cntxt_{test_file}"
    # Serialization of graph using context
    # cntxt_out = "_test_out_cntxt.json-ld"    
    cntxt_out = f"_out_ctxt_{test_file}"
    # Execute Context builder
    if args.concise:
        cmd = "python ../../src/uco_jsonld_context_builder.py\
            --concise --output " + output_file
    else:
        cmd = "python ../../src/uco_jsonld_context_builder.py\
            --output " + output_file
 
    print(cmd)
    subprocess.run(cmd.split())    
    with open(output_file, 'r') as file:
        tmp_c = json.load(file)    
    graph = rdflib.Graph()
    graph.parse(test_file, format="json-ld")
    graph.serialize(no_cntxt_out, format="json-ld")
    graph2 = rdflib.Graph()
    graph2.parse(test_file, format="json-ld", context_data=tmp_c)
    graph.serialize(cntxt_out, context_data=tmp_c, 
        format="json-ld", auto_compact=True)

    # Clean up
    if not args.skip_clean:
        os.remove(output_file)
        os.remove(no_cntxt_out)
        os.remove(cntxt_out)
    return


if __name__ == '__main__':
    main()
