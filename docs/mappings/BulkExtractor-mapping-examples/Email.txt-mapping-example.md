# BulkExtractor Email.txt mapping example

## Email.txt

```csv
338347203	pat@m57.biz	:\x0D\x0A"Pat McGoo" <pat@m57.biz>\x0D\x0ADate:\x0D\x0AWed, 2
338347262	charlie@m57.biz	39 -0800\x0D\x0ATo:\x0D\x0A<charlie@m57.biz>, <jo@m57.biz>\x0D
338360644	rubinfritz31@mail.com	onight?\x0D\x0AFrom:\x0D\x0Arubinfritz31@mail.com\x0D\x0ADate:\x0D\x0AWed, 02
338360712	charlie@m57.biz	:53 -0500\x0D\x0ATo:\x0D\x0Acharlie@m57.biz\x0D\x0A\x0D\x0ACharlie,\x0D\x0A\x0D\x0A
```


## CASE/UCO v0.1.0 JSON-LD
```json
{
  "@id": "https://www.example.org/f9d45926-7132-4eae-99da-d6b6e57a6c9b",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "EmailAddress",
      "value": "pat@m57.biz"
    }
  ]
},
{
  "@id": "https://www.example.org/7b84984d-90aa-48e5-a97c-d5cb40ed6248",
  "@type": "Relationship",
  "source": "https://www.example.org/f9d45926-7132-4eae-99da-d6b6e57a6c9b",
  "target": "https://www.example.org/ffd38812-76ed-4136-93ce-66f686bf3e74", //the image scanned
  "kindOfRelationship": "contained-within",
  "isDirectional": true,
  "propertyBundle": [
    {
      "@type": "DataRange",
      "rangeOffset": 338347203
    }
    {
      "@type": "ExtractedStrings",
      "strings": ":\x0D\x0A\"Pat McGoo\" <pat@m57.biz>\x0D\x0ADate:\x0D\x0AWed, 2",
    },
  ]
},
{
  "@id": "https://www.example.org/71678495-065a-483c-a1ef-572ba6fcb157",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "EmailAddress",
      "value": "charlie@m57.biz"
    }
  ]
},
{
  "@id": "https://www.example.org/f6d43112-c9ee-49ff-982e-65ad7ea4934a",
  "@type": "Relationship",
  "source": "https://www.example.org/71678495-065a-483c-a1ef-572ba6fcb157",
  "target": "https://www.example.org/ffd38812-76ed-4136-93ce-66f686bf3e74",
  "kindOfRelationship": "contained-within",
  "isDirectional": true,
  "propertyBundle": [
    {
      "@type": "DataRange",
      "rangeOffset": 338347262
    }
    {
      "@type": "ExtractedStrings",
      "strings": "39 -0800\x0D\x0ATo:\x0D\x0A<charlie@m57.biz>, <jo@m57.biz>\x0D",
    },
  ]
},
{
  "@id": "https://www.example.org/6c0c7ca4-173d-4f46-9396-c599c0e626a8",
  "@type": "Relationship",
  "source": "https://www.example.org/71678495-065a-483c-a1ef-572ba6fcb157",
  "target": "https://www.example.org/ffd38812-76ed-4136-93ce-66f686bf3e74",
  "kindOfRelationship": "contained-within",
  "isDirectional": true,
  "propertyBundle": [
    {
      "@type": "DataRange",
      "rangeOffset": 338360712
    }
    {
      "@type": "ExtractedStrings",
      "strings": ":53 -0500\x0D\x0ATo:\x0D\x0Acharlie@m57.biz\x0D\x0A\x0D\x0ACharlie,\x0D\x0A\x0D\x0A",
    },
  ]
},
{
  "@id": "https://www.example.org/63302b1b-c45a-4b53-9432-6d881453eef4",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "EmailAddress",
      "value": "rubinfritz31@mail.com"
    }
  ]
},
{
  "@id": "https://www.example.org/bd0334e1-612c-49ed-a279-3cd759fab0c5",
  "@type": "Relationship",
  "source": "https://www.example.org/63302b1b-c45a-4b53-9432-6d881453eef4",
  "target": "https://www.example.org/ffd38812-76ed-4136-93ce-66f686bf3e74",
  "kindOfRelationship": "contained-within",
  "isDirectional": true,
  "propertyBundle": [
    {
      "@type": "DataRange",
      "rangeOffset": 338360644
    }
    {
      "@type": "ExtractedStrings",
      "strings": ":53 -0500\x0D\x0ATo:\x0D\x0Acharlie@m57.biz\x0D\x0A\x0D\x0ACharlie,\x0D\x0A\x0D\x0A",
    },
  ]
}
```
