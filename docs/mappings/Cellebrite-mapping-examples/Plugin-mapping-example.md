# Plugin Mapping Example

## Cellebrite

|Name|Description|Author|Version|
|---|---|---|---|
|MBRGeneric|Parses a Master Boot Record to generate a memory range for each partition listed in the MBR table|Cellebrite|2.0|
|AndroidMD|Parse the metadata for Android dumps|Cellebrite|2.0|
|GUIDPartitionTable|Parses the GUID partition Table (GPT) to extract FS Partitions|Cellebrite|2.0|
|Android Disk Encryption Remover|Enable decoding of a variety of encrypted Android phones using a given password|Cellebrite|2.0|
|ExtX ID|Identifies ExtX partitions|Cellebrite|2.0|
|ExtXNative|Decodes Ext 2, 3 and 4 File Systems|Cellebrite|2.0|
|Yaffs2|Parses Yaffs2 dump (considers all Yaffs2ExtendedTags properties)|Cellebrite|2.0|
|UBIFS|Decodes UbiFS|Cellebrite|2.0|
|SmartFAT|Decodes FAT 12, 16 and 32 (File Allocation Table file system)|Cellebrite|2.0|
|AndroidFSG|Decodes the FSG partition in Android devices|Cellebrite|2.0|
|F2FS|Decodes F2FS filesystem|Cellebrite|2.0|
|Android Databases|Decodes user-data and 3rd party application databases for Android devices|Cellebrite|2.0|
|AndroidUnlockPattern|Decodes Android Unlock pattern|Cellebrite|2.0|
|AndroidUnlockPassword|Decrypts the numeric lock password for Android devices|Cellebrite|2.0|
|ProcdataAnalyzer|Analyze files in procdata|Cellebrite|2.0|
|Pre Project||||
|Garbage Cleaner||||
|ContactsCrossReference|Cross references the phone numbers in a device's contacts with the numbers in SMS messages and Calls. Will fill in the Name field of calls and SMS if there's a match.|Cellebrite|2.0|
|Analytics|Generates the Analytics section information|Cellebrite|2.0|
|Project Processor Finisher||||
|Post Project||||

## CASE/UCO v0.1.0
```json
{//UFED tool
  "@id": "tool-d8be53cd-5c02-47cf-bfe7-dba834662ca3",
  "@type": "Tool",
  "name": "UFED Physical Analyzer",
  "creator": "Cellebrite",
  "version": "4.5.1.14"
},
{//UFED Plugin
  "@id": "tool-d???",
  "@type": "Tool",
  "name": "MBRGeneric",
  "description": "Parses a Master Boot Record to generate a memory range for each partition listed in the MBR table",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-d???",
  "@type": "Tool",
  "name": "AndroidMD",
  "description": "Parse the metadata for Android dump",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-d???",
  "@type": "Tool",
  "name": "GUIDPartitionTable",
  "description": "Parses the GUID partition Table (GPT) to extract FS Partitions",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-d???",
  "@type": "Tool",
  "name": "Android Disk Encryption Remover",
  "description": "Enable decoding of a variety of encrypted Android phones using a given password",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-d???",
  "@type": "Tool",
  "name": "ExtX ID",
  "description": "Identifies ExtX partitions",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-d???",
  "@type": "Tool",
  "name": "ExtXNative",
  "description": "Decodes Ext 2, 3 and 4 File Systems",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-d???",
  "@type": "Tool",
  "name": "Yaffs2",
  "description": "Parses Yaffs2 dump (considers all Yaffs2ExtendedTags properties)",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-d???",
  "@type": "Tool",
  "name": "UBIFS",
  "description": "Decodes UbiFS",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-d???",
  "@type": "Tool",
  "name": "SmartFAT",
  "description": "ecodes FAT 12, 16 and 32 (File Allocation Table file system)",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-d???",
  "@type": "Tool",
  "name": "AndroidFSG",
  "description": "Decodes the FSG partition in Android devices",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-d???",
  "@type": "Tool",
  "name": "F2FS",
  "description": "Decodes F2FS filesystem",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-d???",
  "@type": "Tool",
  "name": "Android Databases",
  "description": "Decodes user-data and 3rd party application databases for Android devices",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-d???",
  "@type": "Tool",
  "name": "AndroidUnlockPattern",
  "description": "Decodes Android Unlock pattern",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-d???",
  "@type": "Tool",
  "name": "AndroidUnlockPassword",
  "description": "Decrypts the numeric lock password for Android devices",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-d???",
  "@type": "Tool",
  "name": "ProcdataAnalyzer",
  "description": "Analyze files in procdata",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-d???",
  "@type": "Tool",
  "name": "Pre Project"
},
{//Plugin
  "@id": "tool-d???",
  "@type": "Tool",
  "name": "Garbage Cleaner"
},
{//Plugin
  "@id": "tool-d???",
  "@type": "Tool",
  "name": "ContactsCrossReference",
  "description": "Cross references the phone numbers in a device's contacts with the numbers in SMS messages and Calls. Will fill in the Name field of calls and SMS if there's a match.",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-d???",
  "@type": "Tool",
  "name": "Analytics",
  "description": "Generates the Analytics section information",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-d???",
  "@type": "Tool",
  "name": "Project Processor Finisher"
},
{//Plugin
  "@id": "tool-d???",
  "@type": "Tool",
  "name": "Post Project"
}
```
