# SHACL tests on example data

This directory contains example instance data files that are meant to trigger SHACL validation passing and failing in expected manners.

Two instance data files are currently in the directory:
* `location_PASS.json` - a file adapted from the [CASE Examples repository](https://github.com/casework/CASE-Examples/).
* `location_XFAIL.json` - The file `location_PASS.jsonld`, with some data modified to trigger shape validation errors.

SHACL validation results are stored in corresponding files named `..._validation.ttl`, to present the current state of validation conditions.


## Design of the Relationship tests

The `Relationship` objects in the `relationship_*.json` files include a numbering scheme in their identifiers, (object class)-(lexical value)-(datatype).  These track the following matrix of test cases:

1. Individual's class:
  - 1: `core:Relationship`
  - 2: `observable:ObservableRelationship`
2. Literal's lexical value:
  - 1: Custom
  - 2: In `vocabulary:ActionRelationshipTypeVocab`
  - 3: In `vocabulary:ObservableObjectRelationshipVocab`
3. Literal's datatype:
  - 1: `xsd:string`
  - 2: `vocabulary:ActionRelationshipTypeVocab`
  - 3: `vocabulary:ObservableObjectRelationshipVocab`
