# CallLog Mapping Example

## SleuthKit

TSK_CALLLOG (a phone call log extracted from a phone or soft-phone application)
* TSK_NAME_PERSON (other party's name)
* TSK_PHONE_NUMBER (other party's phone number)
* TSK_DATETIME (date/time of call)
* TSK_DIRECTION (direction of call: incoming, outgoing)


## CASE/UCO v0.1.0
```json
{ //Phone call
  "@id": "PhoneCall-64a02003-af72-470e-9401-d7fbb86a63a1",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "PhoneCall",
      "callType": "Outgoing",
      "to": "PhoneAccount-14db2f1e-5f6c-48d6-8215-2eafd9acdef8",
      "startTime": "2017-03-28T17:59:43.25Z",
      "endTime": "2017-03-28T18:04:55.31Z"
    }
  ]
},
{//Phone account
  "@id": "PhoneAccount-14db2f1e-5f6c-48d6-8215-2eafd9acdef8",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "PhoneAccount",
      "phoneNumber": "2125552131"
    }
  ]
},
{ //Contact
  "@id": "contact-05fb187f-742d-4358-80bd-e2f1b363b864",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "Contact",
      "contactname": "(other party's name)",
      "phoneNumbers": [
        "2125552131"
      ]
    }
  ]
},
```
There is a known issue with the structure of Contact within CASE/UCO v0.1.0 where Contact.phoneNumbers should contain references to phone account objects rather than simple strings.

This issue is identified and a solution proposed in the following UCO issue entry: [#25](https://github.com/ucoProject/uco/issues/25)

The above CASE/UCO content represents the recommended approach for v0.1.0 to at least partially mitigate the known issue.
