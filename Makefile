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

all: \
  .lib.done.log
	$(MAKE) \
	  --directory ontology

# This recipe guarantees that 'git submodule init' and 'git submodule update' have run at least once.
# The recipe avoids running 'git submodule update' more than once, in case a user is testing with the submodule at a different commit than what UCO tracks.
.git_submodule_init.done.log: \
  .gitmodules
	# CASE-Utility-SHACL-Inheritance-Reviewer
	test -r dependencies/CASE-Utility-SHACL-Inheritance-Reviewer/README.md \
	  || git submodule update --init dependencies/CASE-Utility-SHACL-Inheritance-Reviewer
	@test -r dependencies/CASE-Utility-SHACL-Inheritance-Reviewer/README.md \
	  || (echo "ERROR:Makefile:CASE-Utility-SHACL-Inheritance-Reviewer submodule README.md file not found, even though that submodule is initialized." >&2 ; exit 2)
	# collections-ontology
	test -r dependencies/collections-ontology/README.md \
	  || git submodule update \
	    --init \
	    dependencies/collections-ontology
	# error ontology
	test -r dependencies/error/README.md \
	  || git submodule update \
	    --init \
	    dependencies/error
	touch $@

.lib.done.log:
	$(MAKE) \
	  --directory lib
	touch $@

check: \
  .git_submodule_init.done.log \
  .lib.done.log
	$(MAKE) \
	  --directory ontology \
	  check
	$(MAKE) \
	  --directory tests \
	  check

clean: \
  clean-tests \
  clean-ontology
	@rm -f \
	  .git_submodule_init.done.log \
	  .lib.done.log

clean-ontology:
	@$(MAKE) \
	  --directory ontology \
	  clean

clean-tests:
	@$(MAKE) \
	  --directory tests \
	  clean
