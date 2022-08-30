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
  qc_monolithic.ttl
	$(MAKE) \
	  --directory examples_uco_owl
	$(MAKE) \
	  --directory examples_uco_qc

.PHONY: \
  check-%.ttl

.PRECIOUS: \
  .check-%.ttl

.check-%.ttl: \
  %.ttl \
  $(top_srcdir)/.lib.done.log
	java -jar $(top_srcdir)/lib/rdf-toolkit.jar \
	  --inline-blank-nodes \
	  --source $< \
	  --source-format turtle \
	  --target $@_ \
	  --target-format turtle
	mv $@_ $@

check: \
  check-uco-closure-qc.ttl \
  check-uco-qc.ttl \
  qc_monolithic.ttl
	$(MAKE) \
	  --directory examples_uco_owl \
	  check
	$(MAKE) \
	  --directory examples_uco_qc \
	  check
	source $(tests_srcdir)/venv/bin/activate \
	  && pytest \
	    --log-level=DEBUG \
	    --verbose \
	    --verbose

# Reminder: diff exits non-0 on finding any differences.
# Reminder: The $^ automatic Make variable is the name of all recipe prerequisites.
check-%.ttl: \
  %.ttl \
  .check-%.ttl
	diff $^ \
	  || (echo "ERROR:tests/shapes/Makefile:The local $< does not match the normalized version. If the above reported changes look fine, run 'cp .check-$< $<' while in the sub-folder tests/shapes/ to get a file ready to commit to Git." >&2 ; exit 1)

clean:
	@$(MAKE) \
	  --directory examples_uco_qc \
	  clean
	@$(MAKE) \
	  --directory examples_uco_owl \
	  clean
	@rm -f \
	  .check-*.ttl* \
	  qc_monolithic.ttl

qc_monolithic.ttl: \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/.lib.done.log \
  uco-closure-qc.ttl \
  uco-qc.ttl
	rm -f __$@ _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && rdfpipe \
	    --output-format turtle \
	    uco-closure-qc.ttl \
	    uco-qc.ttl \
	    > __$@
	java -jar $(top_srcdir)/lib/rdf-toolkit.jar \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

