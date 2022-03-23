> *“An ontology defines the basic terms and relations comprising the vocabulary of a topic area, as well as the rules for combining terms and relations to define extensions to the vocabulary. ” (Neches R, Fikes R, Finin T, Gruber T, Patil R, Senator T, Swartout WR (1991) “Enabling Technology for Knowledge Sharing” AI Magazine. Winter 1991. 36-56.)*

> *“An ontology is a formal, explicit specification of a shared conceptualization. ” (Studer, Benjamins, Fensel. Knowledge Engineering: Principles and Methods. Data and Knowledge Engineering. 25 (1998) 161-197)*

# Unified Cyber Ontology (UCO)

Unified Cyber Ontology (UCO) is a community-developed ontology/model, which is intended to serve as a consistent foundation for standardized information representation across the cyber security domain/ecosystem.

Specific information representations focused on individual cyber security subdomains (cyber investigation, computer/network defense, threat intelligence, malware analysis, vulnerability research, offensive/hack-back operations, etc.) can be be based on UCO and defined as appropriate subsets of UCO constructs.

Through this approach not only are domain-focused representations defined consistently but they also can take advantage of shared APIs and information can flow in an automated fashion across subdomain boundaries.

The purpose of this repository is to provide a foundation for broader community involvement in defining what to represent and how.

### Current Release
The current release of UCO is 0.8.0.

UCO 0.8.0 is primarily focused on an initial implementation of Shapes Constraint Language (SHACL) review of semi-open vocabulary usage, restructuring of all UCO ontology IRIs and file structures to enable delivery of ontology resources from a new subdomain, flattening action:ActionReferencesFacet properties directly onto action:Action, normalizing decimal number properties to xsd:decimal, improvements to unit and CI testing, numerous modifications and improvements to the Observable namespace, and correcting several minor issues and bugs.

More detail of improvements is documented in the [UCO 0.8.0 release notes](https://unifiedcyberontology.org/releases/0.8.0/).
