# OS Account Mapping Example

## SleuthKit

TSK_OS_ACCOUNT (an operating system user account)
* TSK_USER_NAME (the login name associated with the account)
* TSK_USER_ID (an identifier associated with the account, e.g., a SID)


## CASE/UCO v0.1.0
```json
{ //OS Account
  "@id": "account-4fe57390-0b6e-4ac8-b813-bbfe3a8ab14d",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "Account",
      "accountType": "OS User",
      "accountIdentifier": "(an identifier associated with the account)"
    },
    {
      "@type": "DigitalAccount",
      "accountLogin": "(the login name associated with the account)"
    }
  ]
}
```
