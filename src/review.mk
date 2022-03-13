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

# This Makefile is assumed to execute in a repository directory ontology/*.

top_srcdir := $(shell cd ../.. ; pwd)

ttl_basenames := $(shell find *.ttl -type f | sort)

# These are reference files, named with a leading dot.
check_reference_basenames := $(foreach ttl_basename,$(ttl_basenames),.check-$(ttl_basename))

# These are recipe targets, not intended to be created files.
check_targets := $(foreach ttl_basename,$(ttl_basenames),check-$(ttl_basename))

all: \
  $(check_reference_basenames)

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
  $(check_targets)

# Reminder: diff exits non-0 on finding any differences.
# Reminder: The $^ automatic Make variable is the name of all recipe prerequisites.
check-%.ttl: \
  %.ttl \
  .check-%.ttl
	diff $^	\
	  || (echo "ERROR:src/review.mk:The local $< does not match the normalized version. If the above reported changes look fine, run 'cp .check-$< $<' while in the sub-folder ontology/$$(basename $< .ttl)/ to get a file ready to commit to Git." >&2 ; exit 1)

clean:
	@rm -f $(check_reference_basenames)
