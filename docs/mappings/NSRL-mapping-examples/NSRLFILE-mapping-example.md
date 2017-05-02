# NSRLFile.txt mapping example

## NSRLFile

```csv
"SHA-1","MD5","CRC32","FileName","FileSize","ProductCode","OpSystemCode","SpecialCode"
"0000002D9D62AEBE1E0E9DB6C4C4C7C16A163D2C","1D6EBB5A789ABD108FF578263E1F40F3","FFFFFFFF","_sfx_0024._p",4109,21000,"358",""
"00000142988AFA836117B1B572FAE4713F200567","9B3702B0E788C6D62996392FE3C9786A","05E566DF","J0180794.JPG",32768,10146,"358",""
"00000142988AFA836117B1B572FAE4713F200567","9B3702B0E788C6D62996392FE3C9786A","05E566DF","J0180794.JPG",32768,10156,"358",""
```


## CASE/UCO v0.1.0 JSON-LD
```json
{
  "@id": "https://www.nsrl.nist.gov/RDS/File/82f0e3c2-aa8b-4ddb-bdd3-2ac5d392379f",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "ContentData",
      "sizeInBytes": 4109,
      "hash": [
        {
          "@type": "Hash",
          "hashMethod": "SHA-1",
          "hashValue": "0000002D9D62AEBE1E0E9DB6C4C4C7C16A163D2C"
        },
        {
          "@type": "Hash",
          "hashMethod": "MD5",
          "hashValue": "1D6EBB5A789ABD108FF578263E1F40F3"
        },
        {
          "@type": "Hash",
          "hashMethod": "CRC32",
          "hashValue": "FFFFFFFF"
        },
      ]
    },
    {
      "@type": "File",
      "fileName": "_sfx_0024._p",
      "sizeInBytes": 4109
    },
  ]
},
{
  "@id": "https://www.nsrl.nist.gov/RDS/Relationship/3cd3aa77-b98b-46a8-9c8e-7be76f3abb63",
  "@type": "Relationship",
  "source": "https://www.nsrl.nist.gov/RDS/File/82f0e3c2-aa8b-4ddb-bdd3-2ac5d392379f",
  "target": "https://www.nsrl.nist.gov/RDS/Product/15f9434c-6937-437a-aa95-abababb6cf84",
  "kindOfRelationship": "contained-within",
  "isDirectional": true
},
{
  "@id": "https://www.nsrl.nist.gov/RDS/Relationship/285119e0-07d2-4809-b006-e71d6f5199c7",
  "@type": "Relationship",
  "source": "https://www.nsrl.nist.gov/RDS/File/82f0e3c2-aa8b-4ddb-bdd3-2ac5d392379f",
  "target": "https://www.nsrl.nist.gov/RDS/OS/0449ef20-93c2-4067-aa7a-a0520bf289ea",
  "kindOfRelationship": "relevant-to",
  "isDirectional": true
},
{
  "@id": "https://www.nsrl.nist.gov/RDS/File/82a5bef9-0a8d-4725-a30a-84c5a5887707",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "ContentData",
      "sizeInBytes": 32768,
      "hash": [
        {
          "@type": "Hash",
          "hashMethod": "SHA-1",
          "hashValue": "00000142988AFA836117B1B572FAE4713F200567"
        },
        {
          "@type": "Hash",
          "hashMethod": "MD5",
          "hashValue": "9B3702B0E788C6D62996392FE3C9786A"
        },
        {
          "@type": "Hash",
          "hashMethod": "CRC32",
          "hashValue": "05E566DF"
        },
      ]
    },
    {
      "@type": "File",
      "fileName": "J0180794.JPG",
      "sizeInBytes": 32768
    },
  ]
},
{
  "@id": "https://www.nsrl.nist.gov/RDS/Relationship/ac2e0c77-5940-4ee6-a23e-25ceac0cff59",
  "@type": "Relationship",
  "source": "https://www.nsrl.nist.gov/RDS/File/82a5bef9-0a8d-4725-a30a-84c5a5887707",
  "target": "https://www.nsrl.nist.gov/RDS/Product/ca0755a9-3ec8-4b33-8ef3-2db1fce79222",
  "kindOfRelationship": "contained-within",
  "isDirectional": true
},
{
  "@id": "https://www.nsrl.nist.gov/RDS/Relationship/76a878f3-26fe-4593-a898-f75221f9bf56",
  "@type": "Relationship",
  "source": "https://www.nsrl.nist.gov/RDS/File/82a5bef9-0a8d-4725-a30a-84c5a5887707",
  "target": "https://www.nsrl.nist.gov/RDS/OS/fbd29056-6462-4890-bfd2-99fb1a6e1037",
  "kindOfRelationship": "relevant-to",
  "isDirectional": true
},
{
  "@id": "https://www.nsrl.nist.gov/RDS/Relationship/72c6dc03-29e7-4182-b499-be19688b2a41",
  "@type": "Relationship",
  "source": "https://www.nsrl.nist.gov/RDS/File/82a5bef9-0a8d-4725-a30a-84c5a5887707",
  "target": "https://www.nsrl.nist.gov/RDS/OS/b4c5bad2-7be9-42e7-a71e-9f7d2df58456",
  "kindOfRelationship": "contained-within",
  "isDirectional": true
}
```
