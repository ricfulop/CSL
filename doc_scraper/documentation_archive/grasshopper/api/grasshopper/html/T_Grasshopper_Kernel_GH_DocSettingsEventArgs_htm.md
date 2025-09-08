---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_DocSettingsEventArgs.htm
scraped_at: 2025-09-08T16:16:08.202687
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_DocSettingsEventArgs
Class](../html/T_Grasshopper_Kernel_GH_DocSettingsEventArgs.htm
"GH_DocSettingsEventArgs Class")

[GH_DocSettingsEventArgs
Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocSettingsEventArgs.htm
"GH_DocSettingsEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_DocSettingsEventArgs Class  
  
---  
  
These arguments are passed along with SettingsChanged events on GH_Document.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[SystemEventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
Grasshopper.KernelGH_DocSettingsEventArgs  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_DocSettingsEventArgs : EventArgs
    
    
    Public Class GH_DocSettingsEventArgs
    	Inherits EventArgs

The GH_DocSettingsEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Document](P_Grasshopper_Kernel_GH_DocSettingsEventArgs_Document.htm)|  Gets
the document that raised the event.  
![Public property](../icons/pubproperty.gif)|
[Kind](P_Grasshopper_Kernel_GH_DocSettingsEventArgs_Kind.htm)|  Gets the type
of setting that was changed.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

