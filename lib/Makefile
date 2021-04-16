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
  rdf-toolkit.jar

# Downloading rdf-toolkit was previously done following the directions
# at:
#   https://github.com/edmcouncil/rdf-toolkit
# However, on the file becoming temporarily unavailable, CASE has placed
# a verified copy at a custom location, as a fallback for an alternative
# retrieval from an EDM Council member's repository.
# The checksum of the original file from EDM Council's build server is
# confirmed before moving file into position.  (This practice will
# probably require frequent updates, unless a signed checksum for the
# jar can be retrieved somehow.)
# In case there are concerns on potentially multiple writes to the same
# file, the documentation for wget's "--output-document file" flag notes
# that "... file will be truncated immediately, and all downloaded
# content will be written there."
rdf-toolkit.jar:
	test -r rdf-toolkit.jar.sha512
	# Try retrieval from Github, then from files.caseontology.org.
	wget \
	  --output-document $@_ \
	  https://github.com/trypuz/openfibo/blob/1f9ab415e8ebd131eadcc9b0fc46241adeeb0384/etc/serialization/rdf-toolkit.jar?raw=true \
	  || wget \
	    --output-document $@_ \
	    http://files.caseontology.org/rdf-toolkit.jar
	test \
	  "x$$(openssl dgst -sha512 $@_ | awk '{print($$NF)}')" \
	  == \
	  "x$$(head -n1 rdf-toolkit.jar.sha512)"
	mv $@_ $@
