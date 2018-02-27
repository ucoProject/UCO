---
title: Cellebrite CASE UCO mapping
---

# Cellebrite CASE UCO mapping


## Concept mappings

|Cellebrite|CASE/UCO|
|---|---|
|Report|uco-core.Bundle OR uco-core.Grouping OR uco-investigation.Investigation|
|Extraction|uco-action.Action|
|Device|uco-observable.CyberItem(Trace).Device|
|Files|uco-observable.CyberItem(Trace).File; uco-observable.CyberItem(Trace).ContentData|
|Contacts|uco-observable.CyberItem(Trace).Contact|
|Events|uco-action.Action|
|Web Bookmarks|uco-observable.CyberItem(Trace).BrowserBookmark|

### Category mappings

|Cellebrite|CASE/UCO Class|
|---|---|
|Report Summary|uco-investigation.Investigation|
|Source Extraction|uco-action.Action|
|Device Information|uco-observable.CyberItem(Trace).Device|
|Image Details|uco-observable.CyberItem(Trace).File; uco-observable.CyberItem(Trace).Image; uco-observable.CyberItem(Trace).ContentData|
|Plugins|uco-core.Tool|
|Contents|uco-observable.CyberItem(Trace)|
|Data Files|uco-observable.CyberItem(Trace).File; uco-observable.CyberItem(Trace).ContentData|
|Activity Analytics|_More information needed_|
|Analytics Phones|_More information needed_|
|Contacts|uco-observable.CyberItem(Trace).Contact|
|Databases|uco-observable.CyberItem(Trace).File; uco-observable.CyberItem(Trace).ContentData|
|Powering Events|uco-action.Action|
|Text files|uco-observable.CyberItem(Trace).File; uco-observable.CyberItem(Trace).ContentData|
|Web Bookmarks|uco-observable.CyberItem(Trace).BrowserBookmark|
|Timeline|uco-action.Action; uco-core.Relationship|

### Property mappings

|Cellebrite|CASE/UCO Class|CASE/UCO Property|Mapping Examples|CASE/UCO Example|
|---|---|---|---|---|
|**Report Summary**|uco-investigation.Investigation||[Report Summary and Source Extraction mapping](Cellebrite-mapping-examples/Report-Summary-and-Source-Extraction-mapping-example.md)||
|  -Report type|uco-investigation.Investigation|uco-investigation.Investigation.investigationForm OR uco-investigation.Investigation.focus||
|  -Case number|uco-investigation.Investigation|uco-investigation.Investigation.id||
|  -Case name|uco-investigation.Investigation|uco-investigation.Investigation.name||
|  -Device|uco-observable.Device|uco-observable.Device.manufacturer; uco-observable.Device.model||
|  -UFED Physical Analyzer version|uco-core.Tool|uco-core.Tool.version||
|  -Unit Identifier|_More information needed_|||
|  -Time zone settings (UTC)|NA (all CASE/UCO timestamps include timezone)|||
|  -Examiner name|uco-action.ActionReferences|uco-action.ActionReferences.performer||
|  -Notes|uco-core.Annotation; uco-core.Assertion|uco-core.Annotation.statement; uco-core.Assertion.statement||

|Cellebrite|CASE/UCO Class|CASE/UCO Property|Mapping Examples|CASE/UCO Example|
|---|---|---|---|---|
|**Source Extraction**|uco-action.Action||[Report Summary and Source Extraction mapping](Cellebrite-mapping-examples/Report-Summary-and-Source-Extraction-mapping-example.md)||
|  -Extraction start date/time|uco-action.Action|uco-action.Action.startTime|||
|  -Extraction end date/time|uco-action.Action|uco-action.Action.endTime|||
|  -UFED Version|uco-core.Tool|uco-core.Tool.version|||
|  -Internal Version|_More information needed_||||
|  -Selected Manufacturer|uco-observable.Device|uco-observable.Device.manufacturer||[device.json](https://github.com/casework/case/blob/master/examples/device.json)|
|  -Selected Device Name|uco-observable.Device|uco-observable.Device.model||[device.json](https://github.com/casework/case/blob/master/examples/device.json)|
|  -Connection Type|_More information needed_||||
|  -Extraction Type|uco-action.Action|uco-action.Action.name|||
|  -Extraction ID|uco-action.Action|uco-action.Action.id|||

|Cellebrite|CASE/UCO Class|CASE/UCO Property|Mapping Examples|CASE/UCO Example|
|---|---|---|---|---|
|**Plugins**|uco-core.Tool||[Plugin mapping](Cellebrite-mapping-examples/Plugin-mapping-example.md)||
|  -Name|uco-core.Tool|uco-core.Tool.name||
|  -Description|uco-core.Tool|uco-core.Tool.description||
|  -Author|uco-core.Tool|uco-core.Tool.creator||
|  -Version|uco-core.Tool|uco-core.Tool.version||

|Cellebrite|CASE/UCO Class|CASE/UCO Property|Mapping Examples|CASE/UCO Example|
|---|---|---|---|---|
|**Image**|uco-observable.File|||
|  -Name|uco-observable.File.fileName|||
|  -Path|uco-observable.File|uco-observable.File.filePath||
|  -Size(bytes)|uco-observable.File OR uco-observable.ContentData|uco-observable.File.sizeInBytes (file system asserted) OR uco-observable.ContentData.sizeInBytes (actual)||
|  -MD5|uco-observable.ContentData|uco-observable.ContentData.Hash.hashMethod="MD5" AND uco-observable.ContentData.Hash.hashValue||

|Cellebrite|CASE/UCO Class|CASE/UCO Property|Mapping Examples|CASE/UCO Example|
|---|---|---|---|---|
|**Device Information**|uco-observable.Device|||
|  -Android Id|NA (GAP)&#x1F534;|||
|  -Bluetooth device name|uco-observable.Device|uco-observable.Device.model||[device.json](https://github.com/casework/case/blob/master/examples/device.json)|
|  -Bluetooth MAC Address|uco-observable.MACAddress|uco-observable.MACAddress.value||
|  -Client Used for Extraction|_More information needed_|||
|  -DeviceInfoDetectedManufacturer|uco-observable.Device|uco-observable.Device.manufacturer||[device.json](https://github.com/casework/case/blob/master/examples/device.json)|
|  -DeviceInfoDetectedModel|uco-observable.Device|uco-observable.Device.model||
|  -DeviceInfoPhoneDateTime|_More information needed_|||
|  -DeviceInfoRevision|_More information needed_|||
|  -Factory Number|uco-observable.Device|uco-observable.Device.serialNumber||
|  -Generic|_More information needed_|||
|  -ICCID|NA (GAP)&#x1F534;|||
|  -IMEI|NA (GAP)&#x1F534;|||
|  -IMSI|NA (GAP)&#x1F534;|||
|  -Mock Locations Allowed|_More information needed_|||
|  -MSISDN|NA (GAP)&#x1F534;|||
|  -MSISDN Type|NA (GAP)&#x1F534;|||
|  -Phone Activation Time|NA (GAP)&#x1F534;|||

|Cellebrite|CASE/UCO Class|CASE/UCO Property|Mapping Examples|CASE/UCO Example|
|---|---|---|---|---|
|**Activity Analytics**|_More information needed_|||
|  -_More information needed_|_More information needed_|||

|Cellebrite|CASE/UCO Class|CASE/UCO Property|Mapping Examples|CASE/UCO Example|
|---|---|---|---|---|
|**Analytics Phones**|_More information needed_|||
|  -_More information needed_|_More information needed_|||

|Cellebrite|CASE/UCO Class|CASE/UCO Property|Mapping Examples|CASE/UCO Example|
|---|---|---|---|---|
|**Contact**|uco-observable.Contact|||
|  -Group|_More information needed_|||
|  -Contact Type|uco-observable.Contact|uco-observable.Contact.contactType||
|  -Created-Date|_More information needed_|||
|  -Created-Time|_More information needed_|||
|  -Modified-Date|_More information needed_|||
|  -Modified-Time|_More information needed_|||
|  -Entries|_More information needed_|||
|  -Notes|_More information needed_|||
|  -Organizations|uco-core.Identity|||
|  -Addresses|uco-core.Location|||
|  -Last time contacted-Date|_More information needed_|||
|  -Last time contacted-Time|_More information needed_|||
|  -Times contacted|_More information needed_|||
|  -Source|_More information needed_|||
|  -Deleted|_More information needed_|||
|  -Bookmark Note|_More information needed_|||

|Cellebrite|CASE/UCO Class|CASE/UCO Property|Mapping Examples|CASE/UCO Example|
|---|---|---|---|---|
|**Database**|uco-observable.File|||
|  -File System|uco-observable.File|uco-observable.File.fileSystemType||
|  -Name|uco-observable.File|uco-observable.File.fileName||
|  -Row count|NA (GAP)&#x1F534;|||
|  --Size(bytes)|uco-observable.File OR uco-observable.ContentData|uco-observable.File.sizeInBytes (file system asserted) OR uco-observable.ContentData.sizeInBytes (actual)||
|  -Path|uco-observable.File|uco-observable.File.filePath||
|  -Meta Data|_More information needed_|||
|    --Path|uco-observable.File|uco-observable.File.filePath||
|    --File size|uco-observable.File OR uco-observable.ContentData|uco-observable.File.sizeInBytes (file system asserted) OR uco-observable.ContentData.sizeInBytes (actual)||
|    --Chunks|_More information needed_|||
|    --Date & Time||||
|      ---Creation time|uco-observable.File|uco-observable.File.createdTime||
|      ---Modify time|uco-observable.File|uco-observable.File.modifiedTime||
|      ---Last access time|uco-observable.File|uco-observable.File.accessedTime||
|    --Offsets|uco-observable.DataRange|||
|      ---Data offset|uco-observable.DataRange|uco-observable.DataRange.rangeOffset||
|  -Tags|_More information needed_|||
|  -MD5|uco-observable.ContentData|uco-observable.ContentData.Hash.hashMethod="MD5" AND uco-observable.ContentData.Hash.hashValue||
|  -SHA256|uco-observable.ContentData|uco-observable.ContentData.Hash.hashMethod="SHA256" AND uco-observable.ContentData.Hash.hashValue||
|  -Modified-Date|uco-observable.File|uco-observable.File.modifiedTime||
|  -Modified-Time|uco-observable.File|uco-observable.File.modifiedTime||
|  -Created-Date|uco-observable.File|uco-observable.File.createdTime||
|  -Created-Time|uco-observable.File|uco-observable.File.createdTime||
|  -Access-Date|uco-observable.File|uco-observable.File.accessedTime||
|  -Access-Time|uco-observable.File|uco-observable.File.accessedTime||
|  -Deleted|_More information needed_|||
|  -Bookmark Note|_More information needed_|||
|  -Additional file info|_More information needed_|||

|Cellebrite|CASE/UCO Class|CASE/UCO Property|Mapping Examples|CASE/UCO Example|
|---|---|---|---|---|
|**Powering Events**|uco-action.Action|||
|  -Element|uco-action.ActionReferences|uco-action.ActionReferences.object||
|  -Timestamp|uco-action.Action|uco-action.Action.startTime||
|  -Event|uco-action.Action|uco-action.Action.name||
|  -Deleted|_More information needed_|||
|  -Bookmark Note|_More information needed_|||

|Cellebrite|CASE/UCO Class|CASE/UCO Property|Mapping Examples|CASE/UCO Example|
|---|---|---|---|---|
|**Text file**|uco-observable.File|||
|  -File System|uco-observable.File|uco-observable.File.fileSystemType||
|  -Name|uco-observable.File|uco-observable.File.fileName||
|  --Size(bytes)|uco-observable.File OR uco-observable.ContentData|uco-observable.File.sizeInBytes (file system asserted) OR uco-observable.ContentData.sizeInBytes (actual)||
|  -Path|uco-observable.File|uco-observable.File.filePath||
|  -Meta Data|_More information needed_|||
|    --Path|uco-observable.File|uco-observable.File.filePath||
|    --File size|uco-observable.File OR uco-observable.ContentData|uco-observable.File.sizeInBytes (file system asserted) OR uco-observable.ContentData.sizeInBytes (actual)||
|    --Chunks|_More information needed_|||
|    --Date & Time||||
|      ---Creation time|uco-observable.File|uco-observable.File.createdTime||
|      ---Modify time|uco-observable.File|uco-observable.File.modifiedTime||
|      ---Last access time|uco-observable.File|uco-observable.File.accessedTime||
|    --Offsets|uco-observable.DataRange|||
|      ---Data offset|uco-observable.DataRange|uco-observable.DataRange.rangeOffset||
|  -Tags|_More information needed_|||
|  -MD5|uco-observable.ContentData|uco-observable.ContentData.Hash.hashMethod="MD5" AND uco-observable.ContentData.Hash.hashValue||
|  -SHA256|uco-observable.ContentData|uco-observable.ContentData.Hash.hashMethod="SHA256" AND uco-observable.ContentData.Hash.hashValue||
|  -Modified-Date|uco-observable.File|uco-observable.File.modifiedTime||
|  -Modified-Time|uco-observable.File|uco-observable.File.modifiedTime||
|  -Created-Date|uco-observable.File|uco-observable.File.createdTime||
|  -Created-Time|uco-observable.File|uco-observable.File.createdTime||
|  -Access-Date|uco-observable.File|uco-observable.File.accessedTime||
|  -Access-Time|uco-observable.File|uco-observable.File.accessedTime||
|  -Deleted|_More information needed_|||
|  -Bookmark Note|_More information needed_|||
|  -Additional file info|_More information needed_|||

|Cellebrite|CASE/UCO Class|CASE/UCO Property|Mapping Examples|CASE/UCO Example|
|---|---|---|---|---|
|**Data file**|uco-observable.File|||
|  -File System|uco-observable.File|uco-observable.File.fileSystemType||
|  -Name|uco-observable.File|uco-observable.File.fileName||
|  --Size(bytes)|uco-observable.File OR uco-observable.ContentData|uco-observable.File.sizeInBytes (file system asserted) OR uco-observable.ContentData.sizeInBytes (actual)||
|  -Path|uco-observable.File|uco-observable.File.filePath||
|  -Meta Data|_More information needed_|||
|    --Path|uco-observable.File|uco-observable.File.filePath||
|    --File size|uco-observable.File OR uco-observable.ContentData|uco-observable.File.sizeInBytes (file system asserted) OR uco-observable.ContentData.sizeInBytes (actual)||
|    --Chunks|_More information needed_|||
|    --Date & Time||||
|      ---Creation time|uco-observable.File|uco-observable.File.createdTime||
|      ---Modify time|uco-observable.File|uco-observable.File.modifiedTime||
|      ---Last access time|uco-observable.File|uco-observable.File.accessedTime||
|    --Offsets|uco-observable.DataRange|||
|      ---Data offset|uco-observable.DataRange|uco-observable.DataRange.rangeOffset||
|  -Tags|_More information needed_|||
|  -MD5|uco-observable.ContentData|uco-observable.ContentData.Hash.hashMethod="MD5" AND uco-observable.ContentData.Hash.hashValue||
|  -SHA256|uco-observable.ContentData|uco-observable.ContentData.Hash.hashMethod="SHA256" AND uco-observable.ContentData.Hash.hashValue||
|  -Modified-Date|uco-observable.File|uco-observable.File.modifiedTime||
|  -Modified-Time|uco-observable.File|uco-observable.File.modifiedTime||
|  -Created-Date|uco-observable.File|uco-observable.File.createdTime||
|  -Created-Time|uco-observable.File|uco-observable.File.createdTime||
|  -Access-Date|uco-observable.File|uco-observable.File.accessedTime||
|  -Access-Time|uco-observable.File|uco-observable.File.accessedTime||
|  -Deleted|_More information needed_|||
|  -Bookmark Note|_More information needed_|||
|  -Additional file info|_More information needed_|||

|Cellebrite|CASE/UCO Class|CASE/UCO Property|Mapping Examples|CASE/UCO Example|
|---|---|---|---|---|
|**Web Bookmarks**|uco-observable.BrowserBookmark|||
|  -Title|uco-observable.CyberItem(Trace)|uco-observable.CyberItem(Trace).name||
|  -URL|uco-observable.BrowserBookmark|uco-observable.BrowserBookmark.urlTargeted||
|  -Last Visited-Date|_More information needed_|||
|  -Last Visited-Time|_More information needed_|||
|  -Visits|uco-observable.BrowserBookmark|uco-observable.BrowserBookmark.visitCount||
|  -Position|_More information needed_|||
|  -Map Address|_More information needed_|||
|  -Source|_More information needed_|||
|  -Date|_More information needed_|||
|  -Time|_More information needed_|||
|  -Deleted|_More information needed_|||
|  -Bookmark Note|_More information needed_|||

|Cellebrite|CASE/UCO Class|CASE/UCO Property|Mapping Examples|CASE/UCO Example|
|---|---|---|---|---|
|**Timeline**|uco-action.Action|||
|  -Type|uco-action.Action|uco-action.Action.name||
|  -Direction|_More information needed_|||
|  -Attachments|uco-core.Relationship; uco-observable.CyberItem(Trace)|||
|  -Locations|uco-core.Location|||
|  -Date|uco-action.Action|uco-action.Action.startTime||
|  -Time|uco-action.Action|uco-action.Action.startTime||
|  -Party|_More information needed_|||
|  -Description|uco-action.Action|uco-action.Action||
|  -Location Info|uco-core.Location|||
|  -Deleted|_More information needed_|||
|  -Bookmark Note|_More information needed_|||

## Identified Gaps

- Mobile account properties (e.g. IMSI, MSISDN) ([#33](https://github.com/ucoProject/uco/issues/33))
- SIM Card properties (e.g. ICCID) ([#34](https://github.com/ucoProject/uco/issues/34))
- Mobile device specific properties (e.g. IMEI) ([#35](https://github.com/ucoProject/uco/issues/35))
- Android mobile device specific properties (e.g. AndroidID) ([#36](https://github.com/ucoProject/uco/issues/36))
- Database row count ([#37](https://github.com/ucoProject/uco/issues/37))
