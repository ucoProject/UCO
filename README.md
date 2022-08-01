> *“An ontology defines the basic terms and relations comprising the vocabulary of a topic area, as well as the rules for combining terms and relations to define extensions to the vocabulary. ” (Neches R, Fikes R, Finin T, Gruber T, Patil R, Senator T, Swartout WR (1991) “Enabling Technology for Knowledge Sharing” AI Magazine. Winter 1991. 36-56.)*

> *“An ontology is a formal, explicit specification of a shared conceptualization. ” (Studer, Benjamins, Fensel. Knowledge Engineering: Principles and Methods. Data and Knowledge Engineering. 25 (1998) 161-197)*

# Unified Cyber Ontology (UCO)

Unified Cyber Ontology (UCO) is a community-developed ontology/model, which is intended to serve as a consistent foundation for standardized information representation across the cyber security domain/ecosystem.

Specific information representations focused on individual cyber security subdomains (cyber investigation, computer/network defense, threat intelligence, malware analysis, vulnerability research, offensive/hack-back operations, etc.) can be be based on UCO and defined as appropriate subsets of UCO constructs.

Through this approach not only are domain-focused representations defined consistently but they also can take advantage of shared APIs and information can flow in an automated fashion across subdomain boundaries.

The purpose of this repository is to provide a foundation for broader community involvement in defining what to represent and how.

### Current Release
The current release of UCO is 0.9.0.

UCO 0.9.0 primarily focused on workflow technology transitions, and was necessitated by a Java dependency upgrade.  The workflow used to normalize Turtle files in UCO and in downstream repositories now minimally requires Java 11, which impacts several public repositories---especially within the [CASE](https://caseontology.org/) community---that present Turtle files as part of their review process.  The workflow to interface with the UCO and CASE ontologies has transitioned to Github Issues, which has caused some files related to programming Github interfaces to become versioned with the ontology.  SHACL documentation will now use `sh:description` when documenting SHACL shapes.  OWL-level ontological commitments are being restored since the transition to SHACL, starting with clarifying that `core:UcoObject` and `core:Facet` are disjoint classes, and that `core:hasFacet` is an OWL inverse-functional property.  In SHACL validation updates, 0.9.0 refines some properties in email stub graph objects, polyglot designations with multiple MIME types, and a correction with names of accounts.

More detail of improvements is documented in the [UCO 0.9.0 release notes](https://unifiedcyberontology.org/releases/0.9.0/).
