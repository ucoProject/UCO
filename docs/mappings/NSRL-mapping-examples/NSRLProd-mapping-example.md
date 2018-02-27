# NSRLProd.txt mapping example

## NSRLProd

```CSV
"ProductCode","ProductName","ProductVersion","OpSystemCode","MfgCode","Language","ApplicationType"
42850,"Gold Key","1.0.0","663","8681","Unknown","Business"
42851,"Gold Inspector","1.5","663","8682","Unknown","Business"
42852,"Gold Forum 2015","1.13","663","8683","Unknown","Business"
```

## CASE/UCO v0.1.0 JSON-LD
```json
{
  "@id": "https://www.nsrl.nist.gov/RDS/Product/67e9ff22-8605-4caf-8507-e3ddb5f64d17",
  "@type": "Trace",
  "name": "Gold Key",
  "propertyBundle": [
    {
      "@type": "Software",
      "version": "1.0.0",
      "manufacturer": "Acacia Studios"
    },
    {
      "@type": "Application",
      "operatingSystem": ["https://www.nsrl.nist.gov/RDS/OS/ab2e2e82-afbc-4d2e-9294-91dbe7feb153"]
    },
    {
      "@type": "ExternalId",
      "externalIDValue": "42850",
      "externalIDContext": "NSRL-rds_2.54-ProductCode"
    }
  ]
},
{
  "@id": "https://www.nsrl.nist.gov/RDS/Product/7e8aadb6-556e-4b4a-bc2c-2498ce577654",
  "@type": "Trace",
  "name": "Gold Inspector",
  "propertyBundle": [
    {
      "@type": "Software",
      "version": "1.5",
      "manufacturer": "DREAMHATCH (Thailand) Co., Ltd."
    },
    {
      "@type": "Application",
      "operatingSystem": ["https://www.nsrl.nist.gov/RDS/OS/ab2e2e82-afbc-4d2e-9294-91dbe7feb153"]
    },
    {
      "@type": "ExternalId",
      "externalIDValue": "42851",
      "externalIDContext": "NSRL-rds_2.54-ProductCode"
    }
  ]
},
{
  "@id": "https://www.nsrl.nist.gov/RDS/Product/5ff1b8e4-4569-4cda-86da-8b5a352f74ea",
  "@type": "Trace",
  "name": "Gold Forum 2015",
  "propertyBundle": [
    {
      "@type": "Software",
      "version": "1.13",
      "manufacturer": "CrowdCompass, Inc."
    },
    {
      "@type": "Application",
      "operatingSystem": ["https://www.nsrl.nist.gov/RDS/OS/ab2e2e82-afbc-4d2e-9294-91dbe7feb153"]
    },
    {
      "@type": "ExternalId",
      "externalIDValue": "42852",
      "externalIDContext": "NSRL-rds_2.54-ProductCode"
    }
  ]
}
```
