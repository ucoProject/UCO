# Web Bookmark Mapping Example

## SleuthKit
TSK_WEB_BOOKMARK
* TSK_URL (URL of bookmark)
* TSK_DATETIME_CREATED (when bookmark was created)
* TSK_PROG_NAME (browser this came from)
* **_TSK_TITLE (Title of webpage)_**
* TSK_DOMAIN (domain name of URL)



## CASE/UCO v0.1.0
```json
{ //Bookmark
  "@id": "bookmark-3fc60abc-9fa6-46b2-9e89-29db6aa5b3c4",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "BrowserBookmark",
      "urlTargeted": "url-91c01ab8-37e6-43a4-9889-0044f7dcd73f",
      "createdTime": "2010-01-15T17:59:43.25Z",
      "application": "software-bf98d09d-5131-42ab-9df3-d5a1af81afb3",
    }
  ]
},
{ //URL
  "@id": "url-91c01ab8-37e6-43a4-9889-0044f7dcd73f",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "URL",
      "fullValue": "http://wiki.sleuthkit.org/index.php?title=Artifact_Examples",
      "host": "domain-4001e0d8-86cc-4d13-a961-2a230841217e"
    }
  ]
},
{ //Domain Name
  "@id": "domain-4001e0d8-86cc-4d13-a961-2a230841217e",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "DomainName",
      "value": "wiki.sleuthkit.org"
    }
  ]
},
{ //Software application (broswer)
  "@id": "software-bf98d09d-5131-42ab-9df3-d5a1af81afb3",
  "@type": "Trace",
  "name": "Chrome",
  "propertyBundle": [
    {
      "@type": "Software",
      "manufacturer": "Google",
      "version": "57.0.2987.110"
    }
  ]
}
```
