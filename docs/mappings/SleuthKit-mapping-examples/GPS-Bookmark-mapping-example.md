# GPS Bookmark Mapping Example

## SleuthKit

TSK_GPS_BOOKMARK (a GPS location bookmark)
* TSK_GPS_LATITUDE (latitude for the location)
* TSK_GPS_LONGITUDE (longitude for the location)
* TSK_GPS_ALTITUDE (altitude for the location)
* TSK_NAME (location name)
* TSK_LOCATION (descriptive address of the location - e.g. a street address)
* TSK_DATETIME (date/time when the bookmark was created)


## CASE/UCO v0.1.0
```json
{ //GPS bookmark
  "@id": "GeoLocationEntry-78562dbf-ea07-4b7f-ae34-7110b21f441e",
  "@type": "Trace",
  "name": "GPS Bookmark",
  "propertyBundle": [
    {
      "@type": "GeoLocationEntry",
      "createdTime": "2014-01-24T13:44:22.19Z",
      "location": "location-9106e34c-60b3-4c19-afec-567195d7d898"
    }
  ]
},
{ //Location
  "@id": "location-9106e34c-60b3-4c19-afec-567195d7d898",
  "@type": "Location",
  "name": "Washington Monument",
  "propertyBundle": [
    {
      "@type": "LatLongCoordinates",
      "latitude": "38.889496",
      "longitude": "-77.035296",
      "altitude": "17.38Z"
    },
    {
      "@type": "SimpleAddress",
      "locality": "Washington",
      "country": "USA",
      "region": "District of Columbia",
      "postalCode": "20024",
      "street": "2 15th St NW"
    }
  ]
}
```
