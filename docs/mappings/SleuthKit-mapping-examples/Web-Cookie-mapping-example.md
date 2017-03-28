# Web Cookie Mapping Example

## SleuthKit

TSK_WEB_COOKIE
* TSK_URL
* TSK_DATETIME (last accessed)
* TSK_NAME
* **_TSK_VALUE_**
* TSK_PROG_NAME (browser this came from)
* TSK_DOMAIN (domain name of URL)


## CASE/UCO v0.1.0
```json
{ //Cookie
  "@id": "Cookie-3fc60abc-9fa6-46b2-9e89-29db6aa5b3c4",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "BrowserCookie",
      "accessedTime": "2014-01-24T13:44:22.19Z",
      "cookieName": "OmNomNom",
      "application": "software-bf98d09d-5131-42ab-9df3-d5a1af81afb3",
      "domain": "domain-4001e0d8-86cc-4d13-a961-2a230841217e"
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
