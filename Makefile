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

turtle_directories := $(shell find uco-* -type d -maxdepth 0 | sort)

all_directories := $(foreach turtle_directory,$(turtle_directories),all-$(turtle_directory))

check_directories := $(foreach turtle_directory,$(turtle_directories),check-$(turtle_directory))

clean_directories := $(foreach turtle_directory,$(turtle_directories),clean-$(turtle_directory))

all: \
  $(all_directories)

all-%: \
  % \
  .lib.done.log
	$(MAKE) \
	  --directory $< \
	  --file $$PWD/src/review.mk

# This recipe guarantees that 'git submodule init' and 'git submodule update' have run at least once.
# The recipe avoids running 'git submodule update' more than once, in case a user is testing with the submodule at a different commit than what UCO tracks.
.git_submodule_init.done.log: \
  .gitmodules
	# CASE-Utility-SHACL-Inheritance-Reviewer
	test -r dependencies/CASE-Utility-SHACL-Inheritance-Reviewer/README.md \
	  || (git submodule init dependencies/CASE-Utility-SHACL-Inheritance-Reviewer && git submodule update dependencies/CASE-Utility-SHACL-Inheritance-Reviewer)
	@test -r dependencies/CASE-Utility-SHACL-Inheritance-Reviewer/README.md \
	  || (echo "ERROR:Makefile:CASE-Utility-SHACL-Inheritance-Reviewer submodule README.md file not found, even though that submodule is initialized." >&2 ; exit 2)
	touch $@

.lib.done.log:
	$(MAKE) \
	  --directory lib
	touch $@

check: \
  $(check_directories) \
  .git_submodule_init.done.log
	$(MAKE) \
	  --directory tests \
	  check

check-%: \
  % \
  .lib.done.log
	$(MAKE) \
	  --directory $< \
	  --file $$PWD/src/review.mk \
	  check

clean: \
  $(clean_directories) \
  clean-tests
	@rm -f \
	  .git_submodule_init.done.log \
	  .lib.done.log

clean-%: \
  %
	@$(MAKE) \
	  --directory $< \
	  --file $$PWD/src/review.mk \
	  clean

clean-tests:
	@$(MAKE) \
	  --directory tests \
	  clean
