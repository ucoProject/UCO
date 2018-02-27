# NSRLMfg.txt mapping example

## NSRLMfg

```CSV
"MfgCode","MfgName"
"1004","Ulead Systems"
"1005","University"
"1006","Unknown"
"1007","Unreal Visions"
```

## CASE/UCO v0.1.0 JSON-LD
```json
{
  "@id": "https://www.nsrl.nist.gov/RDS/MFG/9ba0f695-2106-40ec-9294-5be201ead36a",
  "@type": "Identity",
  "name": "Ulead Systems",
  "propertyBundle": [
    {
      "@type": "ExternalId",
      "externalIDValue": "1004",
      "externalIDContext": "NSRL-rds_2.54-MfgCode"
    }
  ]
},
{
  "@id": "https://www.nsrl.nist.gov/RDS/MFG/f47b414b-0828-407a-adc3-44a5e0e2b409",
  "@type": "Identity",
  "name": "University",
  "propertyBundle": [
    {
      "@type": "ExternalId",
      "externalIDValue": "1005",
      "externalIDContext": "NSRL-rds_2.54-MfgCode"
    }
  ]
},
{
  "@id": "https://www.nsrl.nist.gov/RDS/MFG/cb788685-bdce-4718-93a3-d03a01e46689",
  "@type": "Identity",
  "name": "Unknown",
  "propertyBundle": [
    {
      "@type": "ExternalId",
      "externalIDValue": "1006",
      "externalIDContext": "NSRL-rds_2.54-MfgCode"
    }
  ]
},
{
  "@id": "https://www.nsrl.nist.gov/RDS/MFG/8559b6f8-9459-47e0-b483-c45a8b6ca7b4",
  "@type": "Identity",
  "name": "Unreal Visions",
  "propertyBundle": [
    {
      "@type": "ExternalId",
      "externalIDValue": "1007",
      "externalIDContext": "NSRL-rds_2.54-MfgCode"
    }
  ]
}
```
