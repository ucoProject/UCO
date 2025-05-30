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

top_srcdir := $(shell cd ../.. ; pwd)

all:

check: \
  uco-owl-co.done.log \
  uco-owl-error.done.log

clean:
	@rm -f \
	  *.done.log

uco-owl-co.done.log: \
  $(top_srcdir)/dependencies/collections-ontology/collections.owl \
  $(top_srcdir)/.venv.done.log \
  $(top_srcdir)/ontology/owl/owl.ttl
	# Review for OWL 2 DL conformance.
	source $(top_srcdir)/venv/bin/activate \
	  && pyshacl \
	    --data-file-format xml \
	    --format turtle \
	    --inference none \
	    --ont-file-format turtle \
	    --shacl $(top_srcdir)/ontology/owl/owl.ttl \
	    --shacl-file-format turtle \
	    $<
	touch $@

uco-owl-error.done.log: \
  $(top_srcdir)/dependencies/error/docs/current/error.ttl \
  $(top_srcdir)/.venv.done.log \
  $(top_srcdir)/ontology/owl/owl.ttl
	# Review for OWL 2 DL conformance.
	source $(top_srcdir)/venv/bin/activate \
	  && pyshacl \
	    --data-file-format turtle \
	    --format turtle \
	    --inference none \
	    --ont-file-format turtle \
	    --shacl $(top_srcdir)/ontology/owl/owl.ttl \
	    --shacl-file-format turtle \
	    $<
	touch $@
