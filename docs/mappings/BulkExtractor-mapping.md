---
title: Bulk Extractor CASE UCO mapping
---

# Bulk Extractor CASE UCO mapping


## Output file mappings

|BulkExtractor|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
||||
|ccn.txt|uco-core.Bundle containing one or more uco-observable.CyberItem(Trace) (with Account property bundle); NA (Gap)||
|ccn_track2.txt|NA (Gap)&#x1F534;||
|domain.txt|uco-core.Bundle containing one or more uco-observable.CyberItem(Trace) (with DomainName property bundle)||
|email.txt|uco-core.Bundle containing one or more uco-observable.CyberItem(Trace) (with EmailAccount property bundle)||
|ether.txt|uco-core.Bundle containing one or more uco-observable.CyberItem(Trace) (with MACAddress property bundle)||
|exif.txt|uco-core.Bundle containing one or more uco-observable.CyberItem(Trace) (with Exif property bundle)||
|find.txt|_Need more information_||
|ip.txt|uco-core.Bundle containing one or more uco-observable.CyberItem(Trace) (with IPv4Address and/or IPv6Address property bundle)||
|telephone.txt|uco-core.Bundle containing one or more uco-observable.CyberItem(Trace) (with PhoneAccount and/or PhoneCall property bundle)||
|url.txt|uco-core.Bundle containing one or more uco-observable.CyberItem(Trace) (with URL property bundle)||
|url_searches.txt|uco-core.Bundle containing one or more uco-observable.CyberItem(Trace) (with ExtractedStrings property bundle)||
|wordlist.txt|uco-core.Bundle containing one or more uco-observable.CyberItem(Trace) (with ExtractedStrings property bundle)||
|wordlist_*.txt|uco-core.Bundle containing one or more uco-observable.CyberItem(Trace) (with ExtractedStrings property bundle)||
|zip.txt|uco-core.Bundle containing one or more uco-observable.CyberItem(Trace) (with File,ContentData, ArchiveFile, etc  property bundles); uco-core.Relationship (with kindOfRelationship="contained-within" and/or with PathRelation property bundle)||

## Identified Gaps

- Magnetic strip card Track2 specific information([#28](https://github.com/ucoProject/uco/issues/28))
