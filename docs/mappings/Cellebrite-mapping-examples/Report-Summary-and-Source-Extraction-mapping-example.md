# Report Summary & Source Extraction Mapping Example

## Cellebrite

|Name|Value|
|---|---|
|Device	SGH-i747|Galaxy S III|
|Connection Type|Cable No. 100|
|Extraction start date/time|3/21/2016 11:26:42 AM|
|Extraction end date/time|3/21/2016 11:28:58 AM|
|Extraction Type|Logical [ Android ADB ]|
|Extraction ID|01E84816-83CC-4C3E-AF3E-4A11C22668CA|
|Internal Version|4.2.12.323|
|Report type|Phone|
|Selected Manufacturer|Samsung GSM|
|Selected Device Name|SGH-i747 Galaxy S III|
|UFED Version|4.5.1.323|
|Unit Identifier|1024526148|
|UFED Physical Analyzer version|4.5.1.14|
|Time zone settings (UTC)|Original UTC value|
|Case number|1234|
|Case name|White Shadow|
|Examiner name|John White|
|Notes|Test report in XLSX and XLS formats.|


## CASE/UCO v0.1.0
```json
{ //Investigation-Extraction
  "@id": "investigation-39d09044-ad6e-4771-a0a5-80619727cdc0",
  "@type": "Investigation",
  "name": "White Shadow",
  "focus": "ForensicExtraction:Phone",
},
{ //Phone extraction
  "@id": "action-05f6b570-9055-41b7-9c50-c551b6a84d87",
  "@type": "Action",
  "name": "Logical Extraction [ Android ADB ]",
  "startTime": "2016-03-21T11:26:42Z",
  "endTime": "2016-03-21T11:28:58Z",
  "propertyBundle": [
    {
      "@type": "ActionReferences",
      "performer": "role-c4fb816f-ef90-4562-88ac-bbbf4257c7f7",
      "instrument": "tool-d8be53cd-5c02-47cf-bfe7-dba834662ca3",
      "object": [
        "device-153f4eb8-b6ec-4cf2-93e3-7ef6b919751f"
      ],
      "result": [
        "file-???",
        "file-???",
        "file-???",
        "contact-???",
        "BrowserBookmark-???",
        "action-???",
        "action-???"
      ]
    }
  ]
},
{//Device
  "@id": "device-153f4eb8-b6ec-4cf2-93e3-7ef6b919751f",
  "@type": "Trace",
  "name": "SGH-i747 Galaxy S III",
  "propertyBundle": [
    {
      "@type": "Device",
      "manufacturer": "Samsung GSM",
      "model": "SGH-i747 Galaxy S III",
    }
  ]
},
{//UFED tool
  "@id": "tool-d8be53cd-5c02-47cf-bfe7-dba834662ca3",
  "@type": "Tool",
  "name": "UFED Physical Analyzer",
  "creator": "Cellebrite",
  "version": "4.5.1.14"
},
{//Examiner role
  "@id": "role-c4fb816f-ef90-4562-88ac-bbbf4257c7f7",
  "@type": "Role",
  "name": "Examiner1",
},
{//relationship tying John White to role of Examiner1
  "@id": "relationship-3bd6a277-8276-4b22-b564-a962009a748f",
  "@type": "Relationship",
  "source": "role-c4fb816f-ef90-4562-88ac-bbbf4257c7f7",
  "target": ["identity-a5b2df87-bc86-491d-837c-0dc18e4b6f15"],
  "kindOfRelationship": "has-identity",
  "isDirectional": true
},
{//Identity
  "@id": "identity-a5b2df87-bc86-491d-837c-0dc18e4b6f15",
  "@type": "Identity",
  "propertyBundle": [
    {
      "@type": "SimpleName",
      "givenName": "John",
      "familyName": "White"
    }
  ]
}
```
