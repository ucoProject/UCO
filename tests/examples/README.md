# SHACL tests on example data

This directory contains example instance data files that are meant to trigger SHACL validation passing and failing in expected manners.

Two instance data files are currently in the directory:
* `location_PASS.json` - a file adapted from the [CASE Examples repository](https://github.com/casework/CASE-Examples/).
* `location_XFAIL.json` - The file `location_PASS.jsonld`, with some data modified to trigger shape validation errors.

SHACL validation results are stored in corresponding files named `..._validation.ttl`, to present the current state of validation conditions.


## Design of the Dictionary tests

The `Dictionary` objects in the `dictionary_*.json` files cover these combinations of asserted type (proper dictionary, improper dictionary, or the generic parent class), whether a dictionary entry key is repeated in the data, and whether the `repeatsKey` property is asserted.  (P/X denotes whether the instance is a PASS or XFAIL test case.)

| uuid       | P/X | Dictionary type      | Key repeats | repeatsKey asserted |
| ---        | --- | ---                  | ---         | ---                 |
| `3bb38b3e` |  P  | `Dictionary`         |          no |                  no |
| `e6dc9c2e` |  X  | `Dictionary`         |          no |                 yes |
| `e9adf6c1` |  P  | `Dictionary`         |         yes |                  no |
| `34ac0c49` |  X  | `Dictionary`         |         yes |                 yes |
| `cbc1c80d` |  P  | `ImproperDictionary` |          no |                  no |
| `7fa3ea45` |  P  | `ImproperDictionary` |          no |                 yes |
| `14e28425` |  P  | `ImproperDictionary` |         yes |                  no |
| `a8e5e8e1` |  P  | `ImproperDictionary` |         yes |                 yes |
| `eaded28e` |  P  | `ProperDictionary`   |          no |                  no |
| `8114819f` |  X  | `ProperDictionary`   |          no |                 yes |
| `b2baf8af` |  X  | `ProperDictionary`   |         yes |                  no |
| `f5ae2e6a` |  X  | `ProperDictionary`   |         yes |                 yes |

Other miscellaneous tests are added without full combinatoric review:

* `kb:ProperDictionary-f5ae2e6a-9b10-46f3-8441-30aada36aa1b` also demonstrates an XFAIL case where a key-value *pair* is repeated.
* `kb:ImproperDictionary-7fa3ea45-6426-4ad3-bb5f-7559e07adeb4` also demonstrates a PASS case where `repeatsKey`'s value is not in the supplied dictionary.
* `kb:Dictionary-5bc55661-4808-48e6-9e02-80a153eee5d3` demonstrates an XFAIL case where the disjoint `Dictionary` subtypes are both asserted.


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
