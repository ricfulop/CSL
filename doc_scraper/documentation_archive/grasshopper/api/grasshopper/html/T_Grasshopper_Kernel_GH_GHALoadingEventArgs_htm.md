---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_GHALoadingEventArgs.htm
scraped_at: 2025-09-08T16:16:55.404981
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_GHALoadingEventArgs
Class](../html/T_Grasshopper_Kernel_GH_GHALoadingEventArgs.htm
"GH_GHALoadingEventArgs Class")

[GH_GHALoadingEventArgs
Properties](../html/Properties_T_Grasshopper_Kernel_GH_GHALoadingEventArgs.htm
"GH_GHALoadingEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_GHALoadingEventArgs Class  
  
---  
  
Event arguments used in the GH_GHALoaded event on GH_ComponentServer.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[SystemEventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
Grasshopper.KernelGH_GHALoadingEventArgs  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_GHALoadingEventArgs : EventArgs
    
    
    Public Class GH_GHALoadingEventArgs
    	Inherits EventArgs

The GH_GHALoadingEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Assembly](P_Grasshopper_Kernel_GH_GHALoadingEventArgs_Assembly.htm)|  Gets
the assembly that was loaded from the GHA file.  
![Public property](../icons/pubproperty.gif)|
[FileName](P_Grasshopper_Kernel_GH_GHALoadingEventArgs_FileName.htm)|  Gets
the location of the gha file.  
![Public property](../icons/pubproperty.gif)|
[Icon](P_Grasshopper_Kernel_GH_GHALoadingEventArgs_Icon.htm)|  Gets the
official icon of the GHA file.  
![Public property](../icons/pubproperty.gif)|
[Id](P_Grasshopper_Kernel_GH_GHALoadingEventArgs_Id.htm)|  Gets the Id of the
GHA file.  
![Public property](../icons/pubproperty.gif)|
[LoadingMechanism](P_Grasshopper_Kernel_GH_GHALoadingEventArgs_LoadingMechanism.htm)|
Gets the mechanism that was used to load the file.  
![Public property](../icons/pubproperty.gif)|
[Name](P_Grasshopper_Kernel_GH_GHALoadingEventArgs_Name.htm)|  Gets the
official name of the GHA file.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

