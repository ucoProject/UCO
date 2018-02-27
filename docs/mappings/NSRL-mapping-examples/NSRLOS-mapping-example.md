# NSRLOS.txt mapping example

## NSRLOS

```CSV
"OpSystemCode","OpSystemName","OpSystemVersion","MfgCode"
"356","NetWare 4.x","4.x","675"
"358","TBD","none","1006"
"359","Windows 7","7","609"
```

## CASE/UCO v0.1.0 JSON-LD
```json
{
  "@id": "https://www.nsrl.nist.gov/RDS/OS/71b516bb-1a15-45d1-a4fb-31e107f73010",
  "@type": "Trace",
  "name": "NetWare 4.x",
  "propertyBundle": [
    {
      "@type": "OperatingSystem",
      "version": "4.x",
      "manufacturer": "Novell Inc."
    },
    {
      "@type": "ExternalId",
      "externalIDValue": "356",
      "externalIDContext": "NSRL-rds_2.54-OpSystemCode"
    }
  ]
},
{
  "@id": "https://www.nsrl.nist.gov/RDS/OS/7064cf1a-fb4a-4a3a-8101-6c0874b24bd8",
  "@type": "Trace",
  "name": "TBD",
  "propertyBundle": [
    {
      "@type": "OperatingSystem",
      "version": "none",
      "manufacturer": "Unknown"
    },
    {
      "@type": "ExternalId",
      "externalIDValue": "358",
      "externalIDContext": "NSRL-rds_2.54-OpSystemCode"
    }
  ]
},
{
  "@id": "https://www.nsrl.nist.gov/RDS/OS/7de08557-8fb1-458a-b4b3-f34ae425c804",
  "@type": "Trace",
  "name": "Windows 7",
  "propertyBundle": [
    {
      "@type": "OperatingSystem",
      "version": "7",
      "manufacturer": "Microsoft"
    },
    {
      "@type": "ExternalId",
      "externalIDValue": "359",
      "externalIDContext": "NSRL-rds_2.54-OpSystemCode"
    }
  ]
}
```
