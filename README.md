> *“An ontology defines the basic terms and relations comprising the vocabulary of a topic area, as well as the rules for combining terms and relations to define extensions to the vocabulary. ” (Neches R, Fikes R, Finin T, Gruber T, Patil R, Senator T, Swartout WR (1991) “Enabling Technology for Knowledge Sharing” AI Magazine. Winter 1991. 36-56.)*

> *“An ontology is a formal, explicit specification of a shared conceptualization. ” (Studer, Benjamins, Fensel. Knowledge Engineering: Principles and Methods. Data and Knowledge Engineering. 25 (1998) 161-197)*

# Unified Cyber Ontology (UCO)

Unified Cyber Ontology (UCO) is a community-developed ontology/model, which is intended to serve as a consistent foundation for standardized information representation across the cyber security domain/ecosystem.

Specific information representations focused on individual cyber security subdomains (cyber investigation, computer/network defense, threat intelligence, malware analysis, vulnerability research, offensive/hack-back operations, etc.) can be be based on UCO and defined as appropriate subsets of UCO constructs.

Through this approach not only are domain-focused representations defined consistently but they also can take advantage of shared APIs and information can flow in an automated fashion across subdomain boundaries.

The purpose of this repository is to provide a foundation for broader community involvement in defining what to represent and how.

### Current Release
The current release of UCO is 0.8.0.

UCO Version 0.8.0 provides an initial implementation of Shapes Constraint Language (SHACL) review of semi-open vocabulary usage.  If a suggested term from a UCO controlled vocabulary is not used on a field that permits vocabulary terms or strings, a "Info"-level validation result is reported in the SHACL validation report.

However, this data-review feature encountered an issue with the `core:Relationship` object's `core:kindOfRelationship` property.  In UCO 0.8.0, `core:kindOfRelationship` is now enforced as being only a string with no datatype annotations - that is, in JSON-LD that means to express a contained-within relationship, a plain `"Contained_Within"` string value should be used, instead of the datatype-annotating JSON dictionary `{"@type": "vocabulary:ObservableObjectRelationshipVocab", "@value": "Contained_Within"}`.

UCO 0.8.0 also has revised its ontology IRI structure to enable delivery of ontology resources from a new subdomain, `ontology.unifiedcyberontology.org`.  This aligns UCO with an IRI restructuring proposal previously adopted by the Cyber-investigation Analysis Standard Expression (CASE) community.  Users of UCO 0.7.0 and earlier should be aware that their UCO IRI prefixes should be adjusted.  For instance, the prefix of the Action namespace `https://unifiedcyberontology.org/ontology/uco/action#` is now `https://ontology.unifiedcyberontology.org/uco/action/`.

Other improvements are documented in the [UCO 0.8.0 release notes](https://unifiedcyberontology.org/releases/0.8.0/).
