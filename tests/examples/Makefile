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

SHELL := /bin/bash

top_srcdir := $(shell cd ../.. ; pwd)

tests_srcdir := $(top_srcdir)/tests

all: \
  action_inheritance_PASS_validation.ttl \
  action_inheritance_XFAIL_validation.ttl \
  action_result_PASS_validation.ttl \
  location_PASS_validation.ttl \
  location_XFAIL_validation.ttl \
  relationship_PASS_validation.ttl \
  relationship_PASS_via_rdflib_validation_after_translation.ttl \
  relationship_PASS_via_rdf_toolkit_validation_after_translation.ttl \
  relationship_XFAIL_validation.ttl

.PHONY: \
  check-context

.PRECIOUS: \
  %_validation.ttl \
  relationship_PASS_via_rdflib.ttl \
  relationship_PASS_via_rdf_toolkit.ttl

# NOTE - this recipe makes an allowance for a certain failure type
# reported by pyshacl.  Pyshacl will exit status 1 in the case where
# "DataGraph is Non-Conformant".  This XFAIL test is intenced to
# generate a non-conformance result, and feed that result forward to
# pytest.  Hence, the Make recipe allows for an exit status of 0 or 1.
# (0 would cause an expected failure later in pytest.)
# Note that should another issue cause an exit status of 1, pytest will
# fail because the result validation-graph file would not have expected
# characteristics.
%_validation.ttl: \
  %.json \
  $(tests_srcdir)/.venv.done.log \
  $(tests_srcdir)/uco_monolithic.ttl
	source $(tests_srcdir)/venv/bin/activate \
	  && pyshacl \
	    --data-file-format json-ld \
	    --format turtle \
	    --inference none \
	    --ont-file-format turtle \
	    --ont-graph $(tests_srcdir)/uco_monolithic.ttl \
	    --shacl $(tests_srcdir)/uco_monolithic.ttl \
	    --shacl-file-format turtle \
	    --output __$@ \
	    $< \
	    ; rc=$$? ; test 0 -eq $$rc -o 1 -eq $$rc
	java -jar $(top_srcdir)/lib/rdf-toolkit.jar \
	  --infer-base-iri \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

%_validation_after_translation.ttl: \
  %.ttl \
  $(tests_srcdir)/.venv.done.log \
  $(tests_srcdir)/uco_monolithic.ttl
	source $(tests_srcdir)/venv/bin/activate \
	  && pyshacl \
	    --data-file-format turtle \
	    --format turtle \
	    --inference none \
	    --ont-file-format turtle \
	    --ont-graph $(tests_srcdir)/uco_monolithic.ttl \
	    --shacl $(tests_srcdir)/uco_monolithic.ttl \
	    --shacl-file-format turtle \
	    --output __$@ \
	    $< \
	    ; rc=$$? ; test 0 -eq $$rc -o 1 -eq $$rc
	java -jar $(top_srcdir)/lib/rdf-toolkit.jar \
	  --infer-base-iri \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

check: \
  action_inheritance_PASS_validation.ttl \
  action_inheritance_XFAIL_validation.ttl \
  action_result_PASS_validation.ttl \
  check-context \
  location_PASS_validation.ttl \
  location_XFAIL_validation.ttl \
  relationship_PASS_validation.ttl \
  relationship_PASS_via_rdflib_validation_after_translation.ttl \
  relationship_PASS_via_rdf_toolkit_validation_after_translation.ttl \
  relationship_XFAIL_validation.ttl
	source $(tests_srcdir)/venv/bin/activate \
	  && pytest \
	    --log-level=DEBUG

# These Turtle renders of the JSON file are for confirming data characteristics are preserved when consumed by multiple RDF applications.
check-context: \
  relationship_PASS_via_rdflib.ttl \
  relationship_PASS_via_rdf_toolkit.ttl
	diff $^

clean:
	@rm -f \
	  *_validation*.ttl

relationship_PASS_via_rdf_toolkit.ttl: \
  relationship_PASS.json
	java -jar $(top_srcdir)/lib/rdf-toolkit.jar \
	  --infer-base-iri \
	  --inline-blank-nodes \
	  --source $< \
	  --source-format json-ld \
	  --target _$@ \
	  --target-format turtle
	mv _$@ $@

relationship_PASS_via_rdflib.ttl: \
  relationship_PASS.json \
  $(tests_srcdir)/.venv.done.log \
  $(tests_srcdir)/src/glom_graph.py
	source $(tests_srcdir)/venv/bin/activate \
	  && python3 $(tests_srcdir)/src/glom_graph.py \
	    __$@ \
	    $<
	java -jar $(top_srcdir)/lib/rdf-toolkit.jar \
	  --infer-base-iri \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@
