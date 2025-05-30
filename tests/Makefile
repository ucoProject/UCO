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

top_srcdir := $(shell cd .. ; pwd)

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
  $(top_srcdir)/.venv.done.log \
  shapes/uco-closure-qc.ttl \
  shapes/uco-qc.ttl
	$(MAKE) \
	  --directory shapes \
	  check
	touch $@

check: \
  check-dependencies \
  inheritance_review.ttl \
  uco_monolithic.ttl
	source $(top_srcdir)/venv/bin/activate \
	  && pytest \
	    --ignore examples \
	    --ignore shapes \
	    --log-level=DEBUG
	$(MAKE) \
	  --directory examples \
	  check

check-dependencies: \
  $(top_srcdir)/.venv.done.log
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

inheritance_review.ttl: \
  $(uco_turtle_files) \
  $(top_srcdir)/.venv.done.log
	rm -f _$@
	source $(top_srcdir)/venv/bin/activate \
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
	source $(top_srcdir)/venv/bin/activate \
          && rdfpipe \
	    --input-format ttl \
	    --output-format ttl \
	    $(uco_turtle_files) \
	    > __$@
	# Review UCO closure for versioning consistency.
	source $(top_srcdir)/venv/bin/activate \
          && rdfpipe \
	  __$@ \
	  $(imported_ontology_files) \
	  > ___$@
	source $(top_srcdir)/venv/bin/activate \
	  && pyshacl \
	    --data-file-format turtle \
	    --format turtle \
	    --inference none \
	    --shacl shapes/uco-closure-qc.ttl \
	    --shacl-file-format turtle \
	    ___$@
	# Review UCO closure with SHACL-SHACL.
	source $(top_srcdir)/venv/bin/activate \
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
	source $(top_srcdir)/venv/bin/activate \
	  && pyshacl \
	    --data-file-format turtle \
	    --format turtle \
	    --inference none \
	    --shacl shapes/uco-qc.ttl \
	    --shacl-file-format turtle \
	    __$@
	# Review UCO for OWL 2 DL conformance.
	source $(top_srcdir)/venv/bin/activate \
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
