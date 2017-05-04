---
title: Bulk Extractor CASE UCO mapping
---

# Bulk Extractor CASE UCO mapping


## Output file mappings

|BulkExtractor|CASE/UCO Class|CASE/UCO Property|Mapping Examples|CASE/UCO Example|
|---|---|---|---|---|
|ccn.txt|one or more uco-observable.CyberItem(Trace) (with Account property bundle); NA (Gap)&#x1F534;||||
|ccn_track2.txt|NA (Gap)&#x1F534;||||
|domain.txt|one or more uco-observable.CyberItem(Trace) (with DomainName property bundle) each with a separate “contained-within” uco-core.Relationship between domain name Trace and image Trace with DataRange property bundle specifying offset and and ExtractedStrings property bundle specifying the string extraction context for the domain name.||[Domain.txt mapping](BulkExtractor-mapping-examples/Domain.txt-mapping-example.md)||
|email.txt|one or more uco-observable.CyberItem(Trace) (with EmailAddress property bundle) each with a separate “contained-within” uco-core.Relationship between email address Trace and image Trace with DataRange property bundle specifying offset and and ExtractedStrings property bundle specifying the string extraction context for the email address.||[Email.txt mapping](BulkExtractor-mapping-examples/Email.txt-mapping-example.md)||
|ether.txt|one or more uco-observable.CyberItem(Trace) (with MACAddress property bundle)||||
|exif.txt|one or more uco-observable.CyberItem(Trace) (with Exif property bundle)||||
|find.txt|_Need more information_||||
|ip.txt|one or more uco-observable.CyberItem(Trace) (with IPv4Address and/or IPv6Address property bundle)||||
|telephone.txt|one or more uco-observable.CyberItem(Trace) (with PhoneAccount and/or PhoneCall property bundle)||||
|url.txt|one or more uco-observable.CyberItem(Trace) (with URL property bundle)||||
|url_searches.txt|one or more uco-observable.CyberItem(Trace) (with ExtractedStrings property bundle)||||
|wordlist.txt|one or more uco-observable.CyberItem(Trace) (with ExtractedStrings property bundle)||||
|wordlist_*.txt|one or more uco-observable.CyberItem(Trace) (with ExtractedStrings property bundle)||||
|zip.txt|one or more uco-observable.CyberItem(Trace) (with File,ContentData, ArchiveFile, etc  property bundles); uco-core.Relationship (with kindOfRelationship="contained-within" and/or with PathRelation property bundle)||||

## Identified Gaps

- Magnetic strip card Track2 specific information([#28](https://github.com/ucoProject/uco/issues/28))
