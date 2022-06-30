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

turtle_directories := $(shell find * -type d -maxdepth 0 | sort)

all_directories := $(foreach turtle_directory,$(turtle_directories),all-$(turtle_directory))

check_directories := $(foreach turtle_directory,$(turtle_directories),check-$(turtle_directory))

clean_directories := $(foreach turtle_directory,$(turtle_directories),clean-$(turtle_directory))

all: \
  $(all_directories)

all-%: \
  % \
  $(top_srcdir)/.lib.done.log
	$(MAKE) \
	  --directory $< \
	  --file $(top_srcdir)/src/review.mk

check: \
  $(check_directories)

check-%: \
  % \
  $(top_srcdir)/.lib.done.log
	$(MAKE) \
	  --directory $< \
	  --file $(top_srcdir)/src/review.mk \
	  check

clean: \
  $(clean_directories)

clean-%: \
  %
	@$(MAKE) \
	  --directory $< \
	  --file $(top_srcdir)/src/review.mk \
	  clean
