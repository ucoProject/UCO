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

all:

.PHONY: \
  check-minimal \
  check-concise

check: \
  check-minimal \
  check-concise

check-concise: \
  $(tests_srcdir)/.venv.done.log
	source $(tests_srcdir)/venv/bin/activate \
	  && python3 context_tester.py \
	    --concise

check-minimal: \
  $(tests_srcdir)/.venv.done.log
	source $(tests_srcdir)/venv/bin/activate \
	  && python3 context_tester.py
