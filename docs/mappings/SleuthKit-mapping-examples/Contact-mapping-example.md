# Contact Mapping Example

## SleuthKit

TSK_CONTACT (a Address-book/Email/Messaging application contact )
* TSK_NAME_PERSON (contact's name)
* TSK_PHONE_NUMBER (contact's main/default phone number)
* TSK_PHONE_NUMBER_HOME (contact's home phone number)
* TSK_PHONE_NUMBER_OFFICE (contact's office phone number)
* TSK_PHONE_NUMBER_MOBILE (contact's mobile phone number)
* TSK_EMAIL (contact's main/default email address)
* TSK_EMAIL_HOME (contact's home email address)
* TSK_EMAIL_OFFICE (contact's office email address)


## CASE/UCO v0.1.0
```json
{ //Contact
  "@id": "contact-fbfeff04-806d-407f-adf9-7b0258773d57",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "Contact",
      "contactname": "(contact's name)",
      "emailAddress": [
        "EmailAccount-685fceb3-5354-4b49-9ae0-b3b3c8ba81aa", "EmailAccount-1180e0aa-4ded-4349-945d-621ec7045ba2", "EmailAccount-5c87b531-6d17-4721-93ab-f6df83ee2c50"
      ],
      "phoneNumbers": [
        "2125553944", "home-2125552131", "office-2125559932", "mobile-2125555670"
      ]
    }
  ]
},
{ //Main Email account
  "@id": "EmailAccount-685fceb3-5354-4b49-9ae0-b3b3c8ba81aa",
  "@type": "Trace",
  "name": "Main Email",
  "propertyBundle": [
    {
      "@type": "EmailAccount",
      "emailAddress": "bar@gmail.com"
    }
  ]
},
{ //Home Email account
  "@id": "EmailAccount-1180e0aa-4ded-4349-945d-621ec7045ba2",
  "@type": "Trace",
  "name": "Home Email",
  "propertyBundle": [
    {
      "@type": "EmailAccount",
      "emailAddress": "foo@yahoo.com"
    }
  ]
},
{ //Office Email account
  "@id": "EmailAccount-5c87b531-6d17-4721-93ab-f6df83ee2c50",
  "@type": "Trace",
  "name": "Office Email",
  "propertyBundle": [
    {
      "@type": "EmailAccount",
      "emailAddress": "foobar@acme.com"
    }
  ]
},
```

There are known issues with the structure of Contact within CASE/UCO v0.1.0.

These issues are identified and a solution proposed in the following UCO issue entry: [#25](https://github.com/ucoProject/uco/issues/25)

The above CASE/UCO content represents the recommended approach for v0.1.0 to at least partially mitigate the known issues.
