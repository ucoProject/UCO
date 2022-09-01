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

all: \
  all-co \
  all-owl \
  all-uco

.PHONY: \
  all-co \
  all-owl \
  all-uco \
  check-co \
  check-owl \
  check-uco \
  clean-co \
  clean-owl \
  clean-uco

all-co:
	$(MAKE) \
	  --directory co

all-owl:
	$(MAKE) \
	  --directory owl

all-uco:
	$(MAKE) \
	  --directory uco

check: \
  check-co \
  check-owl \
  check-uco

check-co:
	$(MAKE) \
	  --directory co \
	  check

check-owl:
	$(MAKE) \
	  --directory owl \
	  check

check-uco:
	$(MAKE) \
	  --directory uco \
	  check

clean: \
  clean-co \
  clean-owl \
  clean-uco

clean-co:
	@$(MAKE) \
	  --directory co \
	  clean

clean-owl:
	@$(MAKE) \
	  --directory owl \
	  clean

clean-uco:
	@$(MAKE) \
	  --directory uco \
	  clean
