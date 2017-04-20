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
{//Plugin
  "@id": "tool-f9d860d2-bdfb-4739-a8a8-0b5b58cefabd",
  "@type": "Tool",
  "name": "MBRGeneric",
  "description": "Parses a Master Boot Record to generate a memory range for each partition listed in the MBR table",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-17635748-0dff-4488-ba0a-6c12b7387e52",
  "@type": "Tool",
  "name": "AndroidMD",
  "description": "Parse the metadata for Android dump",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-96c5c340-5c83-472c-8251-1bc5374a8078",
  "@type": "Tool",
  "name": "GUIDPartitionTable",
  "description": "Parses the GUID partition Table (GPT) to extract FS Partitions",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-6dfbf395-f7b7-43a2-8724-dd87db659e76",
  "@type": "Tool",
  "name": "Android Disk Encryption Remover",
  "description": "Enable decoding of a variety of encrypted Android phones using a given password",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-80ec0271-42bc-42b0-9b9a-f326cb919368",
  "@type": "Tool",
  "name": "ExtX ID",
  "description": "Identifies ExtX partitions",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-31a9db11-bb0f-4eae-bc01-6ad68ada926c",
  "@type": "Tool",
  "name": "ExtXNative",
  "description": "Decodes Ext 2, 3 and 4 File Systems",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-b4cb71d5-b692-49c5-a1ba-3dd5c9c72682",
  "@type": "Tool",
  "name": "Yaffs2",
  "description": "Parses Yaffs2 dump (considers all Yaffs2ExtendedTags properties)",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-1bc32419-05b6-4c11-9599-ff04df685794",
  "@type": "Tool",
  "name": "UBIFS",
  "description": "Decodes UbiFS",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-607978b7-dd98-414c-8cc8-ee62af6ba205",
  "@type": "Tool",
  "name": "SmartFAT",
  "description": "ecodes FAT 12, 16 and 32 (File Allocation Table file system)",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-af93ec9d-258c-4784-a1c2-9241346bdba6",
  "@type": "Tool",
  "name": "AndroidFSG",
  "description": "Decodes the FSG partition in Android devices",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-032970e4-af0a-49de-a937-c3b3903f082a",
  "@type": "Tool",
  "name": "F2FS",
  "description": "Decodes F2FS filesystem",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-dcf9e4a7-abda-4629-b11f-a1517b75e530",
  "@type": "Tool",
  "name": "Android Databases",
  "description": "Decodes user-data and 3rd party application databases for Android devices",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-dd12a49c-07e0-4f7a-8938-8b6f49791668",
  "@type": "Tool",
  "name": "AndroidUnlockPattern",
  "description": "Decodes Android Unlock pattern",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-f4a5f0db-b40c-4c29-bb76-cfc829725371",
  "@type": "Tool",
  "name": "AndroidUnlockPassword",
  "description": "Decrypts the numeric lock password for Android devices",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-da0e0cbd-9f74-405d-9f66-5e5c396e214c",
  "@type": "Tool",
  "name": "ProcdataAnalyzer",
  "description": "Analyze files in procdata",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-7b0de5bc-893c-4301-b21e-ec4ee0892e79",
  "@type": "Tool",
  "name": "Pre Project"
},
{//Plugin
  "@id": "tool-b98638ae-d97c-44c7-a48b-873790531572",
  "@type": "Tool",
  "name": "Garbage Cleaner"
},
{//Plugin
  "@id": "tool-1cc9bc64-4318-4998-a2f1-cc25457c87ac",
  "@type": "Tool",
  "name": "ContactsCrossReference",
  "description": "Cross references the phone numbers in a device's contacts with the numbers in SMS messages and Calls. Will fill in the Name field of calls and SMS if there's a match.",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-a6743d20-1bbe-4efd-9fb8-08617b21639b",
  "@type": "Tool",
  "name": "Analytics",
  "description": "Generates the Analytics section information",
  "creator": "Cellebrite",
  "version": "2.0"
},
{//Plugin
  "@id": "tool-5a716829-273d-4df5-91aa-f2793deb5f05",
  "@type": "Tool",
  "name": "Project Processor Finisher"
},
{//Plugin
  "@id": "tool-1a61140b-2901-4e23-a0d9-7973bd1c8373",
  "@type": "Tool",
  "name": "Post Project"
}
```
