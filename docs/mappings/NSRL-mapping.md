---
title: NSRL CASE UCO mapping
---

# NSRL CASE UCO mapping


## NSRLMFG mapping

|NSRL|CASE/UCO Class|CASE/UCO Property|Mapping Examples|CASE/UCO Example|
|---|---|---|---|---|
|MfgCode|uco-core.UcoObject; NA (GAP)&#x1F534;|uco-core.UcoObject.id (for universal identification); NA (GAP)&#x1F534; (for NSRL local ID) (likely capture in ExternalID property bundle [#38](https://github.com/ucoProject/uco/issues/38))|[NSRLMfg mapping](NSRL-mapping-examples/NSRLMFG-mapping-example.md)||
|MfgName|uco-core.Identity|uco-core.Identity.name|[NSRLMfg mapping](NSRL-mapping-examples/NSRLMFG-mapping-example.md)||

## NSRLOS mapping

|NSRL|CASE/UCO Class|CASE/UCO Property|Mapping Examples|CASE/UCO Example|
|---|---|---|---|---|
|OpSystemCode|uco-core.UcoObject; NA (GAP)&#x1F534;|uco-core.UcoObject.id (for universal identification); NA (GAP)&#x1F534; (for NSRL local ID) (likely capture in ExternalID property bundle [#38](https://github.com/ucoProject/uco/issues/38))|[NSRLOS mapping](NSRL-mapping-examples/NSRLOS-mapping-example.md)||
|OpSystemName|uco-observable.CyberItem(Trace)|uco-observable.CyberItem(Trace).name|[NSRLOS mapping](NSRL-mapping-examples/NSRLOS-mapping-example.md)||
|OpSystemVersion|uco-observable.OperatingSystem|uco-observable.OperatingSystem.version|[NSRLOS mapping](NSRL-mapping-examples/NSRLOS-mapping-example.md)||
|MfgCode|uco-observable.OperatingSystem|uco-observable.OperatingSystem.manufacturer|[NSRLOS mapping](NSRL-mapping-examples/NSRLOS-mapping-example.md)||

## NSRLPROD mapping

|NSRL|CASE/UCO Class|CASE/UCO Property|Mapping Examples|CASE/UCO Example|
|---|---|---|---|---|
|ProductCode|uco-core.UcoObject; NA (GAP)&#x1F534;|uco-core.UcoObject.id (for universal identification); NA (GAP)&#x1F534; (for NSRL local ID) (likely capture in ExternalID property bundle [#38](https://github.com/ucoProject/uco/issues/38))|[NSRLProd mapping](NSRL-mapping-examples/NSRLProd-mapping-example.md)||
|ProductName|uco-observable.CyberItem(Trace)|uco-observable.CyberItem(Trace).name|[NSRLProd mapping](NSRL-mapping-examples/NSRLProd-mapping-example.md)||
|ProductVersion|uco-observable.Software|uco-observable.Software.version|[NSRLProd mapping](NSRL-mapping-examples/NSRLProd-mapping-example.md)||
|OpSystemCode|uco-observable.Application|uco-observable.Application.operatingSystem|[NSRLProd mapping](NSRL-mapping-examples/NSRLProd-mapping-example.md)||
|MfgCode|uco-observable.Software|uco-observable.Software.manufacturer|[NSRLProd mapping](NSRL-mapping-examples/NSRLProd-mapping-example.md)||
|Language|NA (GAP)&#x1F534;|||
|ApplicationType|NA (GAP)&#x1F534;|||

## NSRLFile mapping

|NSRL|CASE/UCO Class|CASE/UCO Property|Mapping Examples|CASE/UCO Example|
|---|---|---|---|---|
|SHA-1|uco-observable.ContentData|uco-observable.ContentData.Hash.hashMethod="SHA1" AND uco-observable.ContentData.Hash.hashValue|[NSRLFile mapping](NSRL-mapping-examples/NSRLFILE-mapping-example.md)||
|MD5|uco-observable.ContentData|uco-observable.ContentData.Hash.hashMethod="MD5" AND uco-observable.ContentData.Hash.hashValue|[NSRLFile mapping](NSRL-mapping-examples/NSRLFILE-mapping-example.md)||
|CRC32|uco-observable.ContentData|uco-observable.ContentData.Hash.hashMethod="CRC32" AND uco-observable.ContentData.Hash.hashValue|[NSRLFile mapping](NSRL-mapping-examples/NSRLFILE-mapping-example.md)||
|FileName|uco-observable.File|uco-observable.File.fileName|[NSRLFile mapping](NSRL-mapping-examples/NSRLFILE-mapping-example.md)||
|FileSize|uco-observable.File OR uco-observable.ContentData|uco-observable.File.sizeInBytes (file system asserted) OR uco-observable.ContentData.sizeInBytes (actual)|[NSRLFile mapping](NSRL-mapping-examples/NSRLFILE-mapping-example.md)||
|ProductCode|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within" AND uco-core.Relationship.source=id of file object AND uco-core.Relationship.target=id of product object|[NSRLFile mapping](NSRL-mapping-examples/NSRLFILE-mapping-example.md)||
|OpSystemCode|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="RelevantTo" AND uco-core.Relationship.source=id of operating system object AND uco-core.Relationship.target=id of operating system object|[NSRLFile mapping](NSRL-mapping-examples/NSRLFILE-mapping-example.md)||
|SpecialCode|NA (GAP)&#x1F534;||| Is this field actually used?
