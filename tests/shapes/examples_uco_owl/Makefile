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

top_srcdir := $(shell cd ../../.. ; pwd)

tests_srcdir := $(top_srcdir)/tests

shapes_srcdir := $(tests_srcdir)/shapes

sample_ttls := $(wildcard *_PASS.ttl *_XFAIL.ttl)

validation_ttls := $(foreach sample_ttl,$(sample_ttls),$(subst .ttl,_validation.ttl,$(sample_ttl)))

all: \
  $(validation_ttls)

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
  %.ttl \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/ontology/owl/owl.ttl
	rm -f __$@ _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && pyshacl \
	    --allow-warnings \
	    --data-file-format turtle \
	    --format turtle \
	    --inference none \
	    --shacl $(top_srcdir)/ontology/owl/owl.ttl \
	    --shacl-file-format turtle \
	    --output __$@ \
	    $< \
	    ; rc=$$? ; test 0 -eq $$rc -o 1 -eq $$rc
	java -jar $(top_srcdir)/lib/rdf-toolkit.jar \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

check: \
  $(validation_ttls)

clean:
	@rm -f \
	  *_validation.ttl
