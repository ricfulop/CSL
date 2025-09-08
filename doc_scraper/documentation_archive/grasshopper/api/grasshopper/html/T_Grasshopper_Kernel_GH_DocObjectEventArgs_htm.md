---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_DocObjectEventArgs.htm
scraped_at: 2025-09-08T16:16:07.192786
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_DocObjectEventArgs
Class](../html/T_Grasshopper_Kernel_GH_DocObjectEventArgs.htm
"GH_DocObjectEventArgs Class")

[GH_DocObjectEventArgs
Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocObjectEventArgs.htm
"GH_DocObjectEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_DocObjectEventArgs Class  
  
---  
  
These arguments are passed along with ObjectsAdded and ObjectsRemoved events
on GH_Document.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[SystemEventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
Grasshopper.KernelGH_DocObjectEventArgs  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_DocObjectEventArgs : EventArgs
    
    
    Public Class GH_DocObjectEventArgs
    	Inherits EventArgs

The GH_DocObjectEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Attributes](P_Grasshopper_Kernel_GH_DocObjectEventArgs_Attributes.htm)|  Gets
all the attributes that are associated with all objects in the event.  
![Public property](../icons/pubproperty.gif)|
[Document](P_Grasshopper_Kernel_GH_DocObjectEventArgs_Document.htm)|  Gets the
document that raised the event.  
![Public property](../icons/pubproperty.gif)|
[Object](P_Grasshopper_Kernel_GH_DocObjectEventArgs_Object.htm)|  Gets the
object to which this event pertains.  
![Public property](../icons/pubproperty.gif)|
[ObjectCount](P_Grasshopper_Kernel_GH_DocObjectEventArgs_ObjectCount.htm)|
Gets the number of objects in this event.  
![Public property](../icons/pubproperty.gif)|
[Objects](P_Grasshopper_Kernel_GH_DocObjectEventArgs_Objects.htm)|  Gets a
readonly list of the objects to which this event pertains.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

