# Web Download Mapping Example

## SleuthKit

TSK_WEB_DOWNLOAD
* TSK_URL (Location file was downloaded from)
* TSK_DATETIME_ACCESSED (time file was downloaded)
* TSK_PATH (location saved to)
* TSK_PATH_ID (ID of TSK_PATH attribute file)


## CASE/UCO v0.1.0
```json
{ //Download file action
  "@id": "action-4b823cc5-fa95-481f-a266-bdb02ef7d041",
  "@type": "Action",
  "name": "Download File",
  "endTime": "2017-03-28T17:59:43.25Z",
  "propertyBundle": [
    {
      "@type": "ActionReferences",
      "object": [
        "url-5ac08375-040f-4f49-a798-7c7aeb7bbe72"
      ],
      "result": [
        "file-1a729e78-c64d-4762-86dd-07d7af420451"
      ]
    }
  ]
},
{ //URL
  "@id": "url-5ac08375-040f-4f49-a798-7c7aeb7bbe72",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "URL",
      "fullValue": "https://ucoproject.github.io/uco/mappings/SleuthKit-mapping-examples/Web-Download-mapping-example.md",
    }
  ]
},
{
  "@id": "file-1a729e78-c64d-4762-86dd-07d7af420451",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "File",
      "filePath": "/some/files/Web-Download-mapping-example.md",
    }
  ]
},
```
