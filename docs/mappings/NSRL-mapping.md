---
title: NSRL CASE UCO mapping
---

# NSRL CASE UCO mapping


## NSRLMFG mapping

|NSRL|CASE/UCO Class|CASE/UCO Property|CASE/UCO Example|
|---|---|---|---|
|MfgCode|uco-core.UcoObject; NA (Gap)|uco-core.UcoObject.id (for universal identification); NA (Gap)(for NSRL local ID)||
|MfgName|uco-core.Identity|uco-core.Identity.name||

## NSRLOS mapping

|NSRL|CASE/UCO Class|CASE/UCO Property|CASE/UCO Example|
|---|---|---|---|
|OpSystemCode|uco-core.UcoObject; NA (Gap)|uco-core.UcoObject.id (for universal identification); NA (Gap)(for NSRL local ID)||
|OpSystemName|uco-observable.CyberItem(Trace)|uco-observable.CyberItem(Trace).name||
|OpSystemVersion|uco-observable.OperatingSystem|uco-observable.OperatingSystem.version||
|MfgCode|uco-observable.OperatingSystem|uco-observable.OperatingSystem.manufacturer||

## NSRLPROD mapping

|NSRL|CASE/UCO Class|CASE/UCO Property|CASE/UCO Example|
|---|---|---|---|
|ProductCode|uco-core.UcoObject; NA (Gap)|uco-core.UcoObject.id (for universal identification); NA (Gap)(for NSRL local ID)||
|ProductName|uco-observable.CyberItem(Trace)|uco-observable.CyberItem(Trace).name|||
|ProductVersion|uco-observable.Software|uco-observable.Software.version||
|OpSystemCode|uco-observable.Application|uco-observable.Application.operatingSystem||
|MfgCode|uco-observable.Software|uco-observable.Software.manufacturer||
|Language|uco-observable.Software|uco-observable.Software.language||
|ApplicationType|NA (Gap)|||
