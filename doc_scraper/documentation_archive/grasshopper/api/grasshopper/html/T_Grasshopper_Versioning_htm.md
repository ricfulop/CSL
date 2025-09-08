---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Versioning.htm
scraped_at: 2025-09-08T16:11:51.105594
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper](../html/N_Grasshopper.htm "Grasshopper")

[Versioning Class](../html/T_Grasshopper_Versioning.htm "Versioning Class")

[Versioning Properties](../html/Properties_T_Grasshopper_Versioning.htm
"Versioning Properties")

[Versioning Methods](../html/Methods_T_Grasshopper_Versioning.htm "Versioning
Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# Versioning Class  
  
---  
  
Static class that provides information regarding the Grasshopper versioning.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
GrasshopperVersioning  

**Namespace:** [Grasshopper](N_Grasshopper.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class Versioning
    
    
    Public NotInheritable Class Versioning

The Versioning type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[BuildDate](P_Grasshopper_Versioning_BuildDate.htm)|  Gets the build date
string. This is the visible release iteration tag. Typically the BuildDate is
just the date (MMMM-dd, yyyy), but it may carry a prefix or suffix for special
builds.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)| [Version](P_Grasshopper_Versioning_Version.htm)|
Gets the version of the current build of Grasshopper.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[VersionString](P_Grasshopper_Versioning_VersionString.htm)|  Gets the version
of the current build of Grasshopper.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[SyncVersionHistoryData](M_Grasshopper_Versioning_SyncVersionHistoryData.htm)|
Attempts to download the version history information. The downloaded data (if
the download works) will eventually be stored at:
Grasshopper.Folders.VersionHistoryFile  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[VersionHistoryData](M_Grasshopper_Versioning_VersionHistoryData.htm)|  Gets
the currently most up-to-date version history data.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper Namespace](N_Grasshopper.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

