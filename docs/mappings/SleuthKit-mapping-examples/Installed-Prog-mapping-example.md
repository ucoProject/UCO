# Installed-Prog Mapping Example

## SleuthKit

TSK_INSTALLED_PROG
* PROG_NAME (name of program installed)
* TSK_DATETIME (time that program was installed)


## CASE/UCO v0.1.0
```json
{ //Program installation action
  "@id": "action-30ef8107-5678-4015-9fc3-c860b73c3dc2",
  "@type": "Action",
  "name": "Program Installed",
  "endTime": "2017-03-28T17:59:43.25Z",
  "propertyBundle": [
    {
      "@type": "ActionReferences",
      "object": [
        "software-bf98d09d-5131-42ab-9df3-d5a1af81afb3"
      ]
    }
  ]
},
{ //Software program
  "@id": "software-bf98d09d-5131-42ab-9df3-d5a1af81afb3",
  "@type": "Trace",
  "name": "Chrome",
  "propertyBundle": [
    {
      "@type": "Software",
      "manufacturer": "Google",
      "version": "57.0.2987.110"
    }
  ]
}
```
