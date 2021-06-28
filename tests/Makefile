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

uco_turtle_files := $(shell /bin/ls $(top_srcdir)/uco-*/*.ttl)

all:

.venv.done.log: \
  requirements.txt
	rm -rf venv
	$(PYTHON3) -m virtualenv \
	  --python=$(PYTHON3) \
	  venv
	source venv/bin/activate \
	  && pip install \
	    --upgrade \
	    pip \
	    setuptools
	source venv/bin/activate \
	  && pip install \
	    --requirement requirements.txt
	touch $@

check: \
  uco_monolithic.ttl
	$(MAKE) \
	  --directory examples \
	  check

clean:
	@$(MAKE) \
	  --directory examples \
	  clean
	@rm -f \
	  .venv.done.log \
	  uco_monolithic.ttl
	@rm -rf \
	  venv

uco_monolithic.ttl: \
  $(top_srcdir)/.lib.done.log \
  $(uco_turtle_files) \
  .venv.done.log \
  src/glom_graph.py
	source venv/bin/activate \
	  && python3 src/glom_graph.py \
	    __$@ \
	    $(uco_turtle_files)
	java -jar $(top_srcdir)/lib/rdf-toolkit.jar \
	  --infer-base-iri \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@
