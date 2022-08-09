#!python

import json
import rdflib
import sys
import subprocess
import os

# Test graph file in JSON format
test_file = "action_result_NO_CONTEXT.json"
# File to which context will be written
output_file = "_temp_cntxt.json"
# Serialization of graph without using context
no_cntxt_out = "_test_out_no_cntxt.json-ld"
# Serialization of graph using context
cntxt_out = "_test_out_cntxt.json-ld"

# Execute Context builder
cmd = "python ../../src/uco_jsonld_context_builder.py --output " + output_file
print(cmd)
subprocess.run(cmd.split())

with open(output_file, 'r') as file:
	tmp_c = json.load(file)

graph = rdflib.Graph()
graph.parse(test_file, format="json-ld")
graph.serialize(no_cntxt_out, format="json-ld")
graph2 = rdflib.Graph()
graph2.parse(test_file, format="json-ld", context_data=tmp_c)
graph.serialize(cntxt_out, context_data=tmp_c, format="json-ld", auto_compact=True)

# Clean up
# os.remove(output_file)
# os.remove(no_cntxt_out)
# os.remove(cntxt_out)
sys.exit()
