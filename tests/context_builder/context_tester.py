#!python

import json
import rdflib
import sys
import subprocess

test_file = "action_result_NO_CONTEXT.json"
output_file = "temp_cntxt.json"
# Execute Context builder
cmd = "python ../../src/uco_jsonld_context_builder.py --output " + output_file
print(cmd)
subprocess.run(cmd.split())
with open(output_file, 'r') as file:
	tmp_c = json.load(file)
# print(tmp_c)
graph = rdflib.Graph()
graph.parse(test_file, format="json-ld")
graph.serialize("test_out_no_cntxt.json-ld", format="json-ld")
graph2 = rdflib.Graph()
graph2.parse(test_file, format="json-ld", context_data=tmp_c)
graph.serialize("test_out_cntxt.json-ld", context_data=tmp_c, format="json-ld", auto_compact=True)
# graph2.parse("../tests/uco_monolithic.ttl", format="turtle", context_data=tmp_c)
# graph2.parse("../tests/uco_monolithic.ttl", format="turtle")
# graph.serialize("__uco_monolithic.json-ld", context_data=tmp_c, format="json-ld", auto_compact=False)
# graph2.serialize("__uco_monolithic.json-ld", context_data=tmp_c, format="json-ld", auto_compact=True)
#graph2.serialize("__uco_monolithic.json-ld", context_data=tmp_c, format="json-ld", auto_compact=True)
# graph2.serialize("__uco_monolithic.json-ld", format="json-ld", auto_compact=True)
sys.exit()
