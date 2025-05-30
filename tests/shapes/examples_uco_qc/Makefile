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

shapes_srcdir := $(top_srcdir)/tests/shapes

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
  $(top_srcdir)/.venv.done.log \
  $(shapes_srcdir)/qc_monolithic.ttl
	rm -f __$@ _$@
	source $(top_srcdir)/venv/bin/activate \
	  && pyshacl \
	    --allow-warnings \
	    --data-file-format turtle \
	    --format turtle \
	    --inference none \
	    --shacl $(shapes_srcdir)/qc_monolithic.ttl \
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
