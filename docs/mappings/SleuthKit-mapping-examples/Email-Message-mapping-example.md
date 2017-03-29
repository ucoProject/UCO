# Email Message Mapping Example

## SleuthKit

TSK_EMAIL_MSG (for an e-mail message that was found)
* TSK_EMAIL_TO
* TSK_EMAIL_CC
* TSK_EMAIL_BCC
* TSK_EMAIL_FROM
* TSK_SUBJECT
* TSK_EMAIL_CONTENT_* (message body. Use specific attribute for HTML, PlainText, or RTF. Use multiple content attributes if the message has both plain text and HTML)
* TSK_PATH (Folder that inbox is stored in -- "INBOX", etc. This attribute is REQUIRED to make the artifact show up in Autopsy's tree view.)
* TSK_USERNAME (Username of account that e-mail is associated with)
* TSK_DOMAIN (Domain of account that e-mail is associated with)
* TSK_DATETIME_RCVD
* TSK_DATETIME_SENT
* TSK_MSG_ID
* TSK_MSG_REPLY_ID


## CASE/UCO v0.1.0
```json
{ //Email message
  "@id": "email-59e9cf76-08c3-4f0b-a319-2a3b55b54f03",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "EmailMessage",
      "to": ["EmailAccount-bb704188-de16-4743-92fc-b4cba6f9f464"],
      "cc": ["EmailAccount-6c0e2c89-05c2-4713-8a2e-51126725c783"],
      "bcc": ["EmailAccount-a41737ad-558c-44a4-8031-40c623b3f07b"],
      "from": "EmailAccount-bcc67257-331c-4151-8818-1196eb91e7e0",
      "subject": "Example email message",
      "bodyRaw": "(message body)",
      "sender": "EmailAccount-bcc67257-331c-4151-8818-1196eb91e7e0",
      "receivedTime": "2017-03-28T13:44:23.40Z",
      "sentTime": "2017-03-28T13:44:22.19Z",
      "messageID": "CAKBqNfyKo+ZXtkz6DUAHw6FjmsDjWDB-pvHkJy6kwO82jTbkNA@mail.gmail.com"
    }
  ]
},
{ //Sender Email account
  "@id": "EmailAccount-bcc67257-331c-4151-8818-1196eb91e7e0",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "EmailAccount",
      "emailAddress": "foobar@gmail.com"
    },
    {
      "@type": "DigitalAccount",
      "accountlogin": "(Username of account that e-mail is associated with)"
    }
  ]
},
{//Relationship tying domain to email account
  "@id": "relationship-51f4a684-c7c4-4d8d-9d5f-9f72b07565a5",
  "@type": "Relationship",
  "source": "EmailAccount-bcc67257-331c-4151-8818-1196eb91e7e0",
  "target": "domain-5ec73396-fb52-4bd5-9a66-e6dddfc96d76",
  "kindOfRelationship": "has-domain",
  "isDirectional": true
},
{ //Domain Name
  "@id": "domain-5ec73396-fb52-4bd5-9a66-e6dddfc96d76",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "DomainName",
      "value": "gmail.com"
    }
  ]
},
{ //Intended target Email account
  "@id": "EmailAccount-bb704188-de16-4743-92fc-b4cba6f9f464",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "EmailAccount",
      "emailAddress": "foo@yahoo.com"
    }
  ]
},
{ //Carbon Copy Email account
  "@id": "EmailAccount-6c0e2c89-05c2-4713-8a2e-51126725c783",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "EmailAccount",
      "emailAddress": "bar@yahoo.com"
    }
  ]
},
{ //Blind Carbon Copy Email account
  "@id": "EmailAccount-a41737ad-558c-44a4-8031-40c623b3f07b",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "EmailAccount",
      "emailAddress": "zed@yahoo.com"
    }
  ]
}
```
