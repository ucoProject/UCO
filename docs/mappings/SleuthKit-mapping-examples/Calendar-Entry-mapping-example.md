# Calendar Entry Mapping Example

## SleuthKit

TSK_CALENDAR_ENTRY (a Calendar entry from a phone, PIM or a Calendar application.)
* TSK_CALENDAR_ENTRY_TYPE (entry type: meeting, task, etc.)
* TSK_DESCRIPTION (calendar entry description)
* TSk_DATETIME_START (starting date/time)
* TSK_DATETIME_END (ending date/time)


## CASE/UCO v0.1.0
```json
{ //Calendar entry
  "@id": "CalendarEntry-b3d18c4c-6395-4488-8cd6-5ccd2d1f9ab6",
  "@type": "Trace",
  "description": "(calendar entry description)",
  "propertyBundle": [
    {
      "@type": "CalendarEntry",
      "eventType": "Meeting",
      "startTime": "2017-03-28T11:00:00Z",
      "endTime": "2017-03-28T12:00:00Z"
    }
  ]
}
```
