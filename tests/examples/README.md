# SHACL tests on example data

This directory contains example instance data files that are meant to trigger SHACL validation passing and failing in expected manners.

Two instance data files are currently in the directory:
* `location_PASS.json` - a file adapted from the [CASE Examples repository](https://github.com/casework/CASE-Examples/).
* `location_XFAIL.json` - The file `location_PASS.jsonld`, with some data modified to trigger shape validation errors.

SHACL validation results are stored in corresponding files named `..._validation.ttl`, to present the current state of validation conditions.
