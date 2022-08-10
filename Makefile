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

uco_version := $(shell $(PYTHON3) uco_utils/ontology/version_info.py)
ifeq ($(uco_version),)
$(error Unable to determine UCO version)
endif

all: \
  .ontology.done.log \
  .venv-pre-commit/var/.pre-commit-built.log

.PHONY: \
  download

.git_submodule_init.done.log: \
  .gitmodules
	# Log current submodule pointers.
	cd dependencies \
	  && git diff . \
	    | cat
	test -r dependencies/UCO/ontology/master/uco.ttl \
	  || (git submodule init dependencies/UCO && git submodule update dependencies/UCO)
	test -r dependencies/UCO/ontology/master/uco.ttl
	$(MAKE) \
	  --directory dependencies/UCO \
	  .git_submodule_init.done.log \
	  .lib.done.log
	touch $@

.ontology.done.log: \
  dependencies/UCO/ontology/master/uco.ttl
	# Do not rebuild the current ontology file if it is already present.  It is expected not to change once built.
	# touch -c: Do not create the file if it does not exist.  This will convince the recursive make nothing needs to be done if the file is present.
	touch -c uco_utils/ontology/uco-$(uco_version).ttl
	touch -c uco_utils/ontology/uco-$(uco_version)-subclasses.ttl
	$(MAKE) \
	  --directory uco_utils/ontology
	# Confirm the current monolithic file is in place.
	test -r uco_utils/ontology/uco-$(uco_version).ttl
	test -r uco_utils/ontology/uco-$(uco_version)-subclasses.ttl
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
  .ontology.done.log \
  .venv-pre-commit/var/.pre-commit-built.log
	$(MAKE) \
	  PYTHON3=$(PYTHON3) \
	  --directory tests \
	  check

clean:
	@$(MAKE) \
	  --directory tests \
	  clean
	@rm -f \
	  .*.done.log
	@# 'clean' in the ontology directory should only happen when testing and building new ontology versions.  Hence, it is not called from the top-level Makefile.
	@test ! -r dependencies/UCO/README.md \
	  || $(MAKE) \
	    --directory dependencies/UCO \
	    clean
	@# Restore UCO validation output files that do not affect UCO build process.
	@test ! -r dependencies/UCO/README.md \
	  || ( \
	    cd dependencies/UCO \
	      && git checkout \
	        -- \
	        tests/examples \
	        || true \
	  )

# This recipe guarantees timestamp update order, and is otherwise intended to be a no-op.
dependencies/UCO/ontology/master/uco.ttl: \
  .git_submodule_init.done.log
	test -r $@
	touch $@

distclean: \
  clean
	@rm -rf \
	  build \
	  *.egg-info \
	  dist

download: \
  .git_submodule_init.done.log
	$(MAKE) \
	  --directory tests \
	  download
