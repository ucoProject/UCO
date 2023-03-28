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

PYTHON3 ?= $(shell which python3)

all: \
  .lib.done.log \
  .venv.done.log
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

# The two CASE-Utility... files are to trigger rebuilds based on command-line interface changes or version increments.
.venv.done.log: \
  dependencies/CASE-Utility-SHACL-Inheritance-Reviewer/case_shacl_inheritance_reviewer/__init__.py \
  dependencies/CASE-Utility-SHACL-Inheritance-Reviewer/setup.cfg \
  requirements.txt
	rm -rf venv
	$(PYTHON3) -m venv \
	  venv
	source venv/bin/activate \
	  && pip install \
	    --upgrade \
	    pip \
	    setuptools \
	    wheel
	source venv/bin/activate \
	  && pip install \
	    dependencies/CASE-Utility-SHACL-Inheritance-Reviewer
	source venv/bin/activate \
	  && pip install \
	    --requirement requirements.txt
	touch $@

check: \
  .lib.done.log \
  .venv.done.log
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
	  .lib.done.log \
	  .venv.done.log
	@rm -rf \
	  venv

clean-ontology:
	@$(MAKE) \
	  --directory ontology \
	  clean

clean-tests:
	@$(MAKE) \
	  --directory tests \
	  clean

# Maintain timestamp order.
dependencies/CASE-Utility-SHACL-Inheritance-Reviewer/case_shacl_inheritance_reviewer/__init__.py: \
  .git_submodule_init.done.log
	touch -c $@
	test -r $@

# Maintain timestamp order.
dependencies/CASE-Utility-SHACL-Inheritance-Reviewer/setup.cfg: \
  .git_submodule_init.done.log
	touch -c $@
	test -r $@
