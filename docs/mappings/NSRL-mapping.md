---
title: NSRL CASE UCO mapping
---

# NSRL CASE UCO mapping


## NSRLMFG mapping

|NSRL|CASE/UCO Class|CASE/UCO Property|CASE/UCO Example|
|---|---|---|---|
|MfgCode|uco-core.UcoObject; NA (Gap)|uco-core.UcoObject.id (for universal identification); NA (Gap)(for NSRL local ID)||
|MfgName|uco-core.Identity|uco-core.Identity.name||

## NSRLOS mapping

|NSRL|CASE/UCO Class|CASE/UCO Property|CASE/UCO Example|
|---|---|---|---|
|OpSystemCode|uco-core.UcoObject; NA (Gap)|uco-core.UcoObject.id (for universal identification); NA (Gap)(for NSRL local ID)||
|OpSystemName|uco-observable.CyberItem(Trace)|uco-observable.CyberItem(Trace).name||
|OpSystemVersion|uco-observable.OperatingSystem|uco-observable.OperatingSystem.version||
|MfgCode|uco-observable.OperatingSystem|uco-observable.OperatingSystem.manufacturer||

## NSRLPROD mapping

|NSRL|CASE/UCO Class|CASE/UCO Property|CASE/UCO Example|
|---|---|---|---|
|ProductCode|uco-core.UcoObject; NA (Gap)|uco-core.UcoObject.id (for universal identification); NA (Gap)(for NSRL local ID)||
|ProductName|uco-observable.CyberItem(Trace)|uco-observable.CyberItem(Trace).name|||
|ProductVersion|uco-observable.Software|uco-observable.Software.version||
|OpSystemCode|uco-observable.Application|uco-observable.Application.operatingSystem||
|MfgCode|uco-observable.Software|uco-observable.Software.manufacturer||
|Language|uco-observable.Software|uco-observable.Software.language||
|ApplicationType|NA (Gap)|||

## NSRLFile mapping

|NSRL|CASE/UCO Class|CASE/UCO Property|CASE/UCO Example|
|---|---|---|---|
|SHA-1|uco-observable.ContentData|uco-observable.ContentData.Hash.hashMethod="SHA1" AND uco-observable.ContentData.Hash.hashValue||
|MD5|uco-observable.ContentData|uco-observable.ContentData.Hash.hashMethod="MD5" AND uco-observable.ContentData.Hash.hashValue||
|CRC32|uco-observable.ContentData|uco-observable.ContentData.Hash.hashMethod="CRC32" AND uco-observable.ContentData.Hash.hashValue||
|FileName|uco-observable.File|uco-observable.File.fileName||
|FileSize|uco-observable.File OR uco-observable.ContentData|uco-observable.File.sizeInBytes (file system asserted) OR uco-observable.ContentData.sizeInBytes (actual)||
|ProductCode|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="ComponentOf" AND uco-core.Relationship.source=id of file object AND uco-core.Relationship.target=id of product object||
|OpSystemCode|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="RelevantTo"(???) AND uco-core.Relationship.source=id of operating system object AND uco-core.Relationship.target=id of operating system object|||
|SpecialCode|NA (Gap)|||
