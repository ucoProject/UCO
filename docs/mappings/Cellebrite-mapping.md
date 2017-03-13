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

|Cellebrite|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|Report Summary|uco-investigation.Investigation||
|Source Extraction|uco-action.Action||
|Device Information|uco-observable.CyberItem(Trace).Device||
|Image Details|uco-observable.CyberItem(Trace).File; uco-observable.CyberItem(Trace).Image; uco-observable.CyberItem(Trace).ContentData||
|Plugins|uco-core.Tool||
|Contents|uco-observable.CyberItem(Trace)||
|Data Files|uco-observable.CyberItem(Trace).File; uco-observable.CyberItem(Trace).ContentData||
|Activity Analytics|_More information needed_||
|Analytics Phones|_More information needed_||
|Contacts|uco-observable.CyberItem(Trace).Contact||
|Databases|uco-observable.CyberItem(Trace).File; uco-observable.CyberItem(Trace).ContentData||
|Powering Events|uco-action.Action||
|Text files|uco-observable.CyberItem(Trace).File; uco-observable.CyberItem(Trace).ContentData||
|Web Bookmarks|uco-observable.CyberItem(Trace).BrowserBookmark||
|Timeline|uco-action.Action; uco-core.Relationship||

### Property mappings

|Cellebrite|CASE/UCO Class|CASE/UCO Property|CASE/UCO Example|
|---|---|---|---|
|**Report Summary**|uco-investigation.Investigation|||
|  -Report type|uco-investigation.Investigation|uco-investigation.Investigation.investigationForm OR uco-investigation.Investigation.focus||
|  -Case number|uco-investigation.Investigation|uco-investigation.Investigation.id||
|  -Case name|uco-investigation.Investigation|uco-investigation.Investigation.name||
|  -Device|uco-observable.Device|uco-observable.Device.manufacturer; uco-observable.Device.model||
|  -UFED Physical Analyzer version|uco-core.Tool|uco-core.Tool.version||
|  -Unit Identifier|_More information needed_|||
|  -Time zone settings (UTC)|NA (GAP)|||
|  -Examiner name|uco-action.ActionReferences|uco-action.ActionReferences.performer||
|  -Notes|uco-core.Annotation; uco-core.Assertion|uco-core.Annotation.statement; uco-core.Assertion.statement||
|**Source Extraction**|uco-action.Action|||
|  -Extraction start date/time|uco-action.Action|uco-action.Action.startTime||
|  -Extraction end date/time|uco-action.Action|uco-action.Action.endTime||
|  -UFED Version|uco-core.Tool|uco-core.Tool.version||
|  -Internal Version|_More information needed_|||
|  -Selected Manufacturer|uco-observable.Device|uco-observable.Device.manufacturer||
|  -Selected Device Name|uco-observable.Device|uco-observable.Device.model||
|  -Connection Type|_More information needed_|||
|  -Extraction Type|uco-action.Action|uco-action.Action.name||
|  -Extraction ID|uco-action.Action|uco-action.Action.id||
|**Plugins**|uco-core.Tool|||
|  -Name|uco-core.Tool|uco-core.Tool.name||
|  -Description|uco-core.Tool|uco-core.Tool.description||
|  -Author|uco-core.Tool|uco-core.Tool.creator||
|  -Version|uco-core.Tool|uco-core.Tool.version||
|**Image**|uco-observable.File|||
|  -Name|uco-observable.name|||
|  -Path|uco-observable.File|uco-observable.File.filePath||
|  -Size(bytes)|uco-observable.File OR uco-observable.ContentData|uco-observable.File.sizeInBytes (file system asserted) OR uco-observable.ContentData.sizeInBytes (actual)||
|  -MD5|uco-observable.ContentData|uco-observable.ContentData.Hash.hashMethod="MD5" AND uco-observable.ContentData.Hash.hashValue||
|**Device Information**|uco-observable.Device|||
|  -Android Id|NA (GAP)|||
|  -Bluetooth device name|uco-observable.Device|uco-observable.Device.model||
|  -Bluetooth MAC Address|uco-observable.MACAddress|uco-observable.MACAddress.value||
|  -Client Used for Extraction|_More information needed_|||
|  -DeviceInfoDetectedManufacturer|uco-observable.Device|uco-observable.Device.manufacturer||
|  -DeviceInfoDetectedModel|uco-observable.Device|uco-observable.Device.model||
|  -DeviceInfoPhoneDateTime|_More information needed_|||
|  -DeviceInfoRevision|_More information needed_|||
|  -Factory Number|uco-observable.Device|uco-observable.Device.serialNumber||
|  -Generic|NA (GAP)|||
|  -ICCID|NA (GAP)|||
|  -IMEI|NA (GAP)|||
|  -IMSI|NA (GAP)|||
|  -Mock Locations Allowed|_More information needed_|||
|  -MSISDN|NA (GAP)|||
|  -MSISDN Type|NA (GAP)|||
|  -Phone Activation Time|NA (GAP)|||
|**Activity Analytics**|_More information needed_|||
|  -_More information needed_|_More information needed_|||
|**Analytics Phones**|_More information needed_|||
|  -_More information needed_|_More information needed_|||
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
|**Database**|uco-observable.File|||
|  -File System|uco-observable.File|uco-observable.File.fileSystemType||
|  -Name|uco-observable.CyberItem(Trace)|uco-observable.CyberItem(Trace).name||
|  -Row count|NA (GAP)|||
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
|**Powering Events**|uco-action.Action|||
|  -Element|uco-action.ActionReferences|uco-action.ActionReferences.object||
|  -Timestamp|uco-action.Action|uco-action.Action.startTime||
|  -Event|uco-action.Action|uco-action.Action.name||
|  -Deleted|_More information needed_|||
|  -Bookmark Note|_More information needed_|||
|**Text file**|uco-observable.File|||
|  -File System|uco-observable.File|uco-observable.File.fileSystemType||
|  -Name|uco-observable.CyberItem(Trace)|uco-observable.CyberItem(Trace).name||
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
|**Data file**|uco-observable.File|||
|  -File System|uco-observable.File|uco-observable.File.fileSystemType||
|  -Name|uco-observable.CyberItem(Trace)|uco-observable.CyberItem(Trace).name||
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
