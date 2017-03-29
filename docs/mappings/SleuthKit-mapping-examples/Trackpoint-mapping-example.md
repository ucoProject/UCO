# Trackpoint Mapping Example

## SleuthKit

TSK_TRACKPOINT
* TSK_GEO_LATITUDE
* TSK_GEO_LONGITUDE
* TSK_GEO_* (other geo-related attributes as needed and available)
* TSK_DATETIME


## CASE/UCO v0.1.0
```json
{ //GeoLocationEntry
  "@id": "GeoLocationEntry-78562dbf-ea07-4b7f-ae34-7110b21f441e",
  "@type": "Trace",
  "propertyBundle": [
    {
      "@type": "GeoLocationEntry",
      "createdTime": "2014-01-24T13:44:22.19Z",
      "location": "location-7e3df4f5-798a-46ce-869d-9d306a17fbd4"
    }
  ]
},
{ //Location
  "@id": "location-7e3df4f5-798a-46ce-869d-9d306a17fbd4",
  "@type": "Location",
  "propertyBundle": [
    {
      "@type": "LatLongCoordinates",
      "latitude": "38.889496",
      "longitude": "-77.035296"
    }
  ]
}
```
