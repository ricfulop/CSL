---
url: https://developer.rhino3d.com/api/grasshopper/html/N_GH_IO.htm#!
scraped_at: 2025-09-08T16:10:32.763075
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[GH_IO](../html/N_GH_IO.htm "GH_IO")

[GH_ISerializable Interface](../html/T_GH_IO_GH_ISerializable.htm
"GH_ISerializable Interface")

[VersionNumber Structure](../html/T_GH_IO_VersionNumber.htm "VersionNumber
Structure")

[VersionNumber.Branch Enumeration](../html/T_GH_IO_VersionNumber_Branch.htm
"VersionNumber.Branch Enumeration")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_IO Namespace  
  
---  
  
Base namespace of the GH_IO.dll library. This library contains the classes and
functions needed to read and write Grasshopper files. This library does not
depend on Grasshopper.dll or Rhino_DotNET.dll, so it can be used by unrelated
projects.

![](../icons/SectionExpanded.png)Structures

| Structure| Description  
---|---|---  
![Public structure](../icons/pubstructure.gif)|
[VersionNumber](T_GH_IO_VersionNumber.htm)|  Represents a product version
number that encodes major, minor, time and build branch information. as
major.minor.yyddd.hhmmb where: yy = year of build - 2000 ddd = year day of
build (1-366) hh = hour of build mm = minute of build b = branch of build  
  
![](../icons/SectionExpanded.png)Interfaces

| Interface| Description  
---|---|---  
![Public interface](../icons/pubinterface.gif)|
[GH_ISerializable](T_GH_IO_GH_ISerializable.htm)|  Every object which needs to
(de)serialize itself using GH_IO methodology must implement this interface.  
  
![](../icons/SectionExpanded.png)Enumerations

| Enumeration| Description  
---|---|---  
![Public enumeration](../icons/pubenumeration.gif)|
[VersionNumberBranch](T_GH_IO_VersionNumber_Branch.htm)|  Build branch, set by
the build process.  
  
Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

