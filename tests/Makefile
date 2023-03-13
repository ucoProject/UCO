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

top_srcdir := $(shell cd .. ; pwd)

PYTHON3 ?= $(shell which python3.9 2>/dev/null || which python3.8 2>/dev/null || which python3.7 2>/dev/null || which python3.6 2>/dev/null || which python3)

uco_turtle_files := $(shell /bin/ls $(top_srcdir)/ontology/*/*.ttl $(top_srcdir)/ontology/*/*/*.ttl)

imported_ontology_files := \
  $(top_srcdir)/dependencies/collections-ontology/collections.owl \
  $(top_srcdir)/dependencies/error/docs/current/error.owl

all:

.PHONY: \
  check-dependencies

# Ensure the UCO-internal shapes pass their own tests.
.shapes.done.log: \
  $(top_srcdir)/ontology/owl/owl.ttl \
  .venv.done.log \
  shapes/uco-closure-qc.ttl \
  shapes/uco-qc.ttl
	$(MAKE) \
	  --directory shapes \
	  check
	touch $@

# The two CASE-Utility... files are to trigger rebuilds based on command-line interface changes or version increments.
.venv.done.log: \
  $(top_srcdir)/.git_submodule_init.done.log \
  $(top_srcdir)/dependencies/CASE-Utility-SHACL-Inheritance-Reviewer/case_shacl_inheritance_reviewer/__init__.py \
  $(top_srcdir)/dependencies/CASE-Utility-SHACL-Inheritance-Reviewer/setup.cfg \
  requirements.txt
	rm -rf venv
	$(PYTHON3) -m venv \
	  venv
	source venv/bin/activate \
	  && pip install \
	    --upgrade \
	    pip \
	    setuptools \
	    wheel
	source venv/bin/activate \
	  && pip install \
	    $(top_srcdir)/dependencies/CASE-Utility-SHACL-Inheritance-Reviewer
	source venv/bin/activate \
	  && pip install \
	    --requirement requirements.txt
	touch $@

check: \
  check-dependencies \
  inheritance_review.ttl \
  uco_monolithic.ttl
	source venv/bin/activate \
	  && pytest \
	    --ignore examples \
	    --ignore shapes \
	    --log-level=DEBUG
	$(MAKE) \
	  --directory examples \
	  check

check-dependencies: \
  .venv.done.log
	$(MAKE) \
	  --directory dependencies \
	  check

clean:
	@$(MAKE) \
	  --directory examples \
	  clean
	@$(MAKE) \
	  --directory dependencies \
	  clean
	@rm -f \
	  .*.done.log \
	  uco_monolithic.ttl
	@rm -rf \
	  venv

inheritance_review.ttl: \
  $(uco_turtle_files) \
  .venv.done.log
	rm -f _$@
	source venv/bin/activate \
	  && case_shacl_inheritance_reviewer \
	    --strict \
	    _$@ \
	    $(uco_turtle_files) \
	    || (cat _$@ && exit 1)
	mv _$@ $@

uco_monolithic.ttl: \
  $(imported_ontology_files) \
  $(top_srcdir)/.lib.done.log \
  $(uco_turtle_files) \
  .shapes.done.log \
  thing.ttl
	source venv/bin/activate \
          && rdfpipe \
	    --input-format ttl \
	    --output-format ttl \
	    $(uco_turtle_files) \
	    > __$@
	# Review UCO closure for versioning consistency.
	source venv/bin/activate \
          && rdfpipe \
	  __$@ \
	  $(imported_ontology_files) \
	  > ___$@
	source venv/bin/activate \
	  && pyshacl \
	    --data-file-format turtle \
	    --format turtle \
	    --inference none \
	    --shacl shapes/uco-closure-qc.ttl \
	    --shacl-file-format turtle \
	    ___$@
	# Review UCO closure with SHACL-SHACL.
	source venv/bin/activate \
	  && pyshacl \
	    --data-file-format turtle \
	    --format turtle \
	    --inference none \
	    --metashacl \
	    --shacl ___$@ \
	    --shacl-file-format turtle \
	    thing.ttl
	# Closure tests have passed; remove closure file.
	rm ___$@
	# Review UCO for practice conformance.
	source venv/bin/activate \
	  && pyshacl \
	    --data-file-format turtle \
	    --format turtle \
	    --inference none \
	    --shacl shapes/uco-qc.ttl \
	    --shacl-file-format turtle \
	    __$@
	# Review UCO for OWL 2 DL conformance.
	source venv/bin/activate \
	  && pyshacl \
	    --data-file-format turtle \
	    --format turtle \
	    --inference none \
	    --ont-file-format turtle \
	    --shacl $(top_srcdir)/ontology/owl/owl.ttl \
	    --shacl-file-format turtle \
	    __$@
	java -jar $(top_srcdir)/lib/rdf-toolkit.jar \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@
