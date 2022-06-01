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

PYTHON3 ?= python3

all: \
  .venv-pre-commit/var/.pre-commit-built.log

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

# This virtual environment is meant to be built once and then persist, even through 'make clean'.
# If a recipe is written to remove this flag file, it should first run `pre-commit uninstall`.
.venv-pre-commit/var/.pre-commit-built.log:
	rm -rf .venv-pre-commit
	test -r .pre-commit-config.yaml \
	  || (echo "ERROR:Makefile:pre-commit is expected to install for this repository, but .pre-commit-config.yaml does not seem to exist." >&2 ; exit 1)
	$(PYTHON3) -m venv \
	  .venv-pre-commit
	source .venv-pre-commit/bin/activate \
	  && pip install \
	    --upgrade \
	    pip \
	    setuptools \
	    wheel
	source .venv-pre-commit/bin/activate \
	  && pip install \
	    pre-commit
	source .venv-pre-commit/bin/activate \
	  && pre-commit install
	mkdir -p \
	  .venv-pre-commit/var
	touch $@

check: \
  .git_submodule_init.done.log \
  .venv-pre-commit/var/.pre-commit-built.log
	$(MAKE) \
	  PYTHON3=$(PYTHON3) \
	  --directory tests \
	  check

clean: \
  clean-tests
	@rm -f \
	  .git_submodule_init.done.log \
	  .lib.done.log

clean-tests:
	@$(MAKE) \
	  --directory tests \
	  clean
