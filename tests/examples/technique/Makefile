#!/usr/bin/make -f

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

SHELL := /bin/bash

top_srcdir := $(shell cd ../../.. ; pwd)

all: \
  check

check: \
  technique_ontology_XFAIL_validation.ttl \
  technique_data_PASS_validation.ttl \
  technique_data_XFAIL_validation.ttl

clean:
	@rm -f \
	  _* \
	  generated-*

generated-shapes.ttl: \
  $(top_srcdir)/.venv.done.log \
  $(top_srcdir)/tests/uco_monolithic.ttl \
  $(top_srcdir)/tests/thing.ttl \
  technique_shapes_PASS.ttl
	source $(top_srcdir)/venv/bin/activate \
	  && rdfpipe \
	    --output-format turtle \
	    $(top_srcdir)/tests/uco_monolithic.ttl \
	    technique_shapes_PASS.ttl \
	    > _$@
	source $(top_srcdir)/venv/bin/activate \
	  && pyshacl \
	    --format turtle \
	    --metashacl \
	    --shacl _$@ \
	    $(top_srcdir)/tests/thing.ttl
	mv _$@ $@

generated-tbox.ttl: \
  $(top_srcdir)/.venv.done.log \
  $(top_srcdir)/tests/uco_monolithic.ttl \
  generated-shapes.ttl \
  technique_ontology_PASS.ttl
	source $(top_srcdir)/venv/bin/activate \
	  && rdfpipe \
	    --output-format turtle \
	    $(top_srcdir)/tests/uco_monolithic.ttl \
	    technique_ontology_PASS.ttl \
	    > _$@
	source $(top_srcdir)/venv/bin/activate \
	  && pyshacl \
	    --format turtle \
	    --shacl generated-shapes.ttl \
	    _$@
	mv _$@ $@

technique_data_PASS_validation.ttl: \
  generated-tbox.ttl \
  technique_data_PASS.json
	source $(top_srcdir)/venv/bin/activate \
	  && pyshacl \
	    --format turtle \
	    --ont-graph generated-tbox.ttl \
	    --output __$@ \
	    --shacl generated-shapes.ttl \
	    technique_data_PASS.json
	java -jar $(top_srcdir)/lib/rdf-toolkit.jar \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

technique_data_XFAIL_validation.ttl: \
  generated-tbox.ttl \
  technique_data_XFAIL.json
	source $(top_srcdir)/venv/bin/activate \
	  && pyshacl \
	    --format turtle \
	    --ont-graph generated-tbox.ttl \
	    --output __$@ \
	    --shacl generated-shapes.ttl \
	    technique_data_XFAIL.json \
	    ; test 1 -eq $$?
	java -jar $(top_srcdir)/lib/rdf-toolkit.jar \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

technique_ontology_XFAIL_validation.ttl: \
  $(top_srcdir)/.venv.done.log \
  $(top_srcdir)/tests/uco_monolithic.ttl \
  generated-shapes.ttl \
  technique_ontology_XFAIL.ttl
	source $(top_srcdir)/venv/bin/activate \
	  && rdfpipe \
	    --output-format turtle \
	    $(top_srcdir)/tests/uco_monolithic.ttl \
	    technique_ontology_XFAIL.ttl \
	    > _$@
	source $(top_srcdir)/venv/bin/activate \
	  && pyshacl \
	    --format turtle \
	    --output __$@ \
	    --shacl generated-shapes.ttl \
	    _$@ \
	    ; test 1 -eq $$?
	rm _$@
	java -jar $(top_srcdir)/lib/rdf-toolkit.jar \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@
