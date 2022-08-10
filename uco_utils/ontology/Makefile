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

uco_srcdir := $(top_srcdir)/dependencies/UCO

uco_srcdir := $(uco_srcdir)/dependencies/UCO

RDF_TOOLKIT_JAR := $(uco_srcdir)/lib/rdf-toolkit.jar

uco_version := $(shell python3 version_info.py)

all: \
  uco-$(uco_version)-subclasses.ttl

.PRECIOUS: \
  uco-$(uco_version).ttl

uco-$(uco_version).ttl: \
  $(top_srcdir)/.git_submodule_init.done.log \
  $(RDF_TOOLKIT_JAR)
	$(MAKE) \
	  --directory $(uco_srcdir)/tests \
	    uco_monolithic.ttl
	#TODO This cleanup step should be removed after the 0.3.0 release of UCO-Utility-SHACL-Inheritance-Reviewer.
	test ! -d $(uco_srcdir)/dependencies/UCO-Utility-SHACL-Inheritance-Reviewer/build \
	  || rm -rf \
	    $(uco_srcdir)/dependencies/UCO-Utility-SHACL-Inheritance-Reviewer/build
	#TODO This normalization step will not be needed after resolution of ONT-445.
	java -jar $(RDF_TOOLKIT_JAR) \
	  --inline-blank-nodes \
	  --source $(uco_srcdir)/tests/uco_monolithic.ttl \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	mv _$@ $@

uco-$(uco_version)-subclasses.ttl: \
  uco-$(uco_version).ttl \
  src/subclasses_ttl.py
	# The UCO ontology test venv is made by the earlier build step
	# of uco_monolithic.ttl.  However, unless a new ontology
	# release is being made, that step will have been skipped.
	# This recursive Make call guarantees the virtual environment is
	# set up.
	$(MAKE) \
	  --directory $(uco_srcdir)/tests \
	    .venv.done.log
	#TODO This cleanup step should be removed after the 0.3.0 release of UCO-Utility-SHACL-Inheritance-Reviewer.
	test ! -d $(uco_srcdir)/dependencies/UCO-Utility-SHACL-Inheritance-Reviewer/build \
	  || rm -rf \
	    $(uco_srcdir)/dependencies/UCO-Utility-SHACL-Inheritance-Reviewer/build
	source $(uco_srcdir)/tests/venv/bin/activate \
	  && python3 src/subclasses_ttl.py \
	  __$@ \
	 $<
	java -jar $(RDF_TOOLKIT_JAR) \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

clean:
	@rm -f \
	  uco-$(uco_version)*.ttl
