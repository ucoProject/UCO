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

# This Makefile is adapted from /src/review.mk.  It is expected to be
# short-lived, because at the time of this writing, there is a separate
# proposal revising the CI process to no longer use Make for Turtle
# normalization.
# TODO https://github.com/ucoProject/UCO/issues/373

SHELL := /bin/bash

top_srcdir := $(shell cd ../.. ; pwd)

ttl_basenames := $(shell find *.ttl -type f | sort)

# These are reference files, named with a leading dot.
check_reference_basenames := $(foreach ttl_basename,$(ttl_basenames),.check-$(ttl_basename))

# These are recipe targets, not intended to be created files.
check_targets := $(foreach ttl_basename,$(ttl_basenames),check-$(ttl_basename))

all: \
  $(check_reference_basenames) \
  catalog-v001.xml

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

catalog-v001.xml: \
  $(top_srcdir)/.venv.done.log \
  $(top_srcdir)/etc/domain_directories.tsv \
  $(top_srcdir)/etc/dependency_files.tsv \
  $(top_srcdir)/src/create-catalog-v001.xml.py \
  $(ttl_basenames)
	rm -f _$@
	source $(top_srcdir)/venv/bin/activate \
	  && python3 $(top_srcdir)/src/create-catalog-v001.xml.py \
	    _$@ \
	    $(top_srcdir)/etc/domain_directories.tsv \
	    $(top_srcdir)/etc/dependency_files.tsv \
	    "$(top_srcdir)" \
	    $(ttl_basenames)
	mv _$@ $@

check: \
  $(check_targets) \
  catalog-v001.xml

# Reminder: diff exits non-0 on finding any differences.
# Reminder: The $^ automatic Make variable is the name of all recipe prerequisites.
check-%.ttl: \
  %.ttl \
  .check-%.ttl
	diff $^	\
	  || (echo "ERROR:ontology/co/Makefile:The local $< does not match the normalized version. If the above reported changes look fine, run 'cp .check-$< $<' while in the sub-folder ontology/co/ to get a file ready to commit to Git." >&2 ; exit 1)

clean:
	@rm -f \
	  $(check_reference_basenames) \
	  catalog-v001.xml
