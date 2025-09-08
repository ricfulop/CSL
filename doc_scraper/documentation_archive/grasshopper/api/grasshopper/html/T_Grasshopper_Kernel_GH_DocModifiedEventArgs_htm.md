---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_DocModifiedEventArgs.htm
scraped_at: 2025-09-08T16:16:06.194274
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_DocModifiedEventArgs
Class](../html/T_Grasshopper_Kernel_GH_DocModifiedEventArgs.htm
"GH_DocModifiedEventArgs Class")

[GH_DocModifiedEventArgs
Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocModifiedEventArgs.htm
"GH_DocModifiedEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_DocModifiedEventArgs Class  
  
---  
  
These arguments are passed along with ModifiedChanged events on GH_Document.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[SystemEventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
Grasshopper.KernelGH_DocModifiedEventArgs  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_DocModifiedEventArgs : EventArgs
    
    
    Public Class GH_DocModifiedEventArgs
    	Inherits EventArgs

The GH_DocModifiedEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Document](P_Grasshopper_Kernel_GH_DocModifiedEventArgs_Document.htm)|  Gets
the document that raised the event.  
![Public property](../icons/pubproperty.gif)|
[Modified](P_Grasshopper_Kernel_GH_DocModifiedEventArgs_Modified.htm)|  Gets
the value of the document Modified flag at the time the event was raised, it
_may_ have been changed in between by other event handlers.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

