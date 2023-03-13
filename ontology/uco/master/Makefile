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

all: \
  catalog-v001.xml

# TODO - Move virtual environment creation up to root directory and re-order top_srcdir's descent.
catalog-v001.xml: \
  $(top_srcdir)/src/create-catalog-v001.xml.py \
  $(top_srcdir)/tests/.venv.done.log
	rm -f _$@
	source $(top_srcdir)/tests/venv/bin/activate \
	  && python3 $(top_srcdir)/src/create-catalog-v001.xml.py \
	    _$@ \
	    domain_directories.tsv \
	    "$(top_srcdir)" \
	    uco.ttl
	mv _$@ $@

check: \
  catalog-v001.xml

clean:
	@rm -f \
	  catalog-v001.xml
