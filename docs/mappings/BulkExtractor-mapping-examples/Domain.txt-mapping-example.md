# BulkExtractor Domain.txt mapping example

## Domain.txt

```csv
152496	openoffice.org	lns:ooo="http://openoffice.org/2004/office" of
338347207	m57.biz	Pat McGoo" <pat@m57.biz>\x0D\x0ADate:\x0D\x0AWed, 2
338347270	m57.biz	\x0D\x0ATo:\x0D\x0A<charlie@m57.biz>, <jo@m57.biz>\x0D
338360657	mail.com	:\x0D\x0Arubinfritz31@mail.com\x0D\x0ADate:\x0D\x0AWed, 02
```


## CASE/UCO v0.1.0 JSON-LD
```json
{
  "@id": "https://www.example.org/deae35f7-0f6d-45e8-9e5f-1ef5afc6742f",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "DomainName",
      "value": "openoffice.org"
    }
  ]
},
{
  "@id": "https://www.example.org/7eec41fe-479d-484e-81ed-cf0052527e88",
  "@type": "Relationship",
  "source": "https://www.example.org/deae35f7-0f6d-45e8-9e5f-1ef5afc6742f",
  "target": "https://www.example.org/ffd38812-76ed-4136-93ce-66f686bf3e74", //the image scanned
  "kindOfRelationship": "contained-within",
  "isDirectional": true,
  "propertyBundle": [
    {
      "@type": "DataRange",
      "rangeOffset": 152496
    }
    {
      "@type": "ExtractedStrings",
      "strings": "lns:ooo=\"http://openoffice.org/2004/office\" of",
    },
  ]
},
{
  "@id": "https://www.example.org/c3def531-9f28-4579-ae6a-62d38d5cb219",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "DomainName",
      "value": "m57.biz"
    }
  ]
},
{
  "@id": "https://www.example.org/0d022aa0-9a1d-4341-bae8-d481aedef456",
  "@type": "Relationship",
  "source": "https://www.example.org/c3def531-9f28-4579-ae6a-62d38d5cb219",
  "target": "https://www.example.org/ffd38812-76ed-4136-93ce-66f686bf3e74",
  "kindOfRelationship": "contained-within",
  "isDirectional": true,
  "propertyBundle": [
    {
      "@type": "DataRange",
      "rangeOffset": 338347207
    }
    {
      "@type": "ExtractedStrings",
      "strings": "Pat McGoo\" <pat@m57.biz>\x0D\x0ADate:\x0D\x0AWed, 2",
    },
  ]
},
{
  "@id": "https://www.example.org/f77338eb-9b16-41d6-891b-605f23207741",
  "@type": "Relationship",
  "source": "https://www.example.org/c3def531-9f28-4579-ae6a-62d38d5cb219",
  "target": "https://www.example.org/ffd38812-76ed-4136-93ce-66f686bf3e74",
  "kindOfRelationship": "contained-within",
  "isDirectional": true,
  "propertyBundle": [
    {
      "@type": "DataRange",
      "rangeOffset": 338347270
    }
    {
      "@type": "ExtractedStrings",
      "strings": "\x0D\x0ATo:\x0D\x0A<charlie@m57.biz>, <jo@m57.biz>\x0D",
    },
  ]
},
{
  "@id": "https://www.example.org/ec0bf619-2afd-489f-a442-166587372ea0",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "DomainName",
      "value": "mail.com"
    }
  ]
},
{
  "@id": "https://www.example.org/93937d18-0a73-44b0-8e8b-c6a67e853aca",
  "@type": "Relationship",
  "source": "https://www.example.org/ec0bf619-2afd-489f-a442-166587372ea0",
  "target": "https://www.example.org/ffd38812-76ed-4136-93ce-66f686bf3e74",
  "kindOfRelationship": "contained-within",
  "isDirectional": true,
  "propertyBundle": [
    {
      "@type": "DataRange",
      "rangeOffset": 338360657
    }
    {
      "@type": "ExtractedStrings",
      "strings": ":\x0D\x0Arubinfritz31@mail.com\x0D\x0ADate:\x0D\x0AWed, 02",
    },
  ]
}
```
