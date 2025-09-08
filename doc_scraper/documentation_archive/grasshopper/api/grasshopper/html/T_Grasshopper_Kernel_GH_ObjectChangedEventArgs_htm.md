---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_ObjectChangedEventArgs.htm
scraped_at: 2025-09-08T16:17:11.483698
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_ObjectChangedEventArgs
Class](../html/T_Grasshopper_Kernel_GH_ObjectChangedEventArgs.htm
"GH_ObjectChangedEventArgs Class")

[GH_ObjectChangedEventArgs Constructor
](../html/Overload_Grasshopper_Kernel_GH_ObjectChangedEventArgs__ctor.htm
"GH_ObjectChangedEventArgs Constructor ")

[GH_ObjectChangedEventArgs
Properties](../html/Properties_T_Grasshopper_Kernel_GH_ObjectChangedEventArgs.htm
"GH_ObjectChangedEventArgs Properties")

[GH_ObjectChangedEventArgs
Fields](../html/Fields_T_Grasshopper_Kernel_GH_ObjectChangedEventArgs.htm
"GH_ObjectChangedEventArgs Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_ObjectChangedEventArgs Class  
  
---  
  
Event arguments passed during ObjectChanged events.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[SystemEventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
Grasshopper.KernelGH_ObjectChangedEventArgs  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_ObjectChangedEventArgs : EventArgs
    
    
    Public Class GH_ObjectChangedEventArgs
    	Inherits EventArgs

The GH_ObjectChangedEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_ObjectChangedEventArgs(IGH_DocumentObject,
GH_ObjectEventType)](M_Grasshopper_Kernel_GH_ObjectChangedEventArgs__ctor.htm)|
Initializes a new instance of the GH_ObjectChangedEventArgs class  
![Public method](../icons/pubmethod.gif)|
[GH_ObjectChangedEventArgs(IGH_DocumentObject,
String)](M_Grasshopper_Kernel_GH_ObjectChangedEventArgs__ctor_2.htm)|
Initializes a new instance of the GH_ObjectChangedEventArgs class  
![Public method](../icons/pubmethod.gif)|
[GH_ObjectChangedEventArgs(IGH_DocumentObject, GH_ObjectEventType,
Object)](M_Grasshopper_Kernel_GH_ObjectChangedEventArgs__ctor_1.htm)|
Initializes a new instance of the GH_ObjectChangedEventArgs class  
![Public method](../icons/pubmethod.gif)|
[GH_ObjectChangedEventArgs(IGH_DocumentObject, String,
Object)](M_Grasshopper_Kernel_GH_ObjectChangedEventArgs__ctor_3.htm)|
Initializes a new instance of the GH_ObjectChangedEventArgs class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[CustomType](P_Grasshopper_Kernel_GH_ObjectChangedEventArgs_CustomType.htm)|
Gets the customised type description of this event. This field is only set
when the Type is GH_ObjectEventType.Custom.  
![Public property](../icons/pubproperty.gif)|
[Sender](P_Grasshopper_Kernel_GH_ObjectChangedEventArgs_Sender.htm)|  Gets the
object which raised this event.  
![Public property](../icons/pubproperty.gif)|
[Tag](P_Grasshopper_Kernel_GH_ObjectChangedEventArgs_Tag.htm)|  Gets the tag
for this event.  
![Public property](../icons/pubproperty.gif)|
[Type](P_Grasshopper_Kernel_GH_ObjectChangedEventArgs_Type.htm)|  Gets the
type of this event.  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Protected field](../icons/protfield.gif)|
[m_custom](F_Grasshopper_Kernel_GH_ObjectChangedEventArgs_m_custom.htm)|  
![Protected field](../icons/protfield.gif)|
[m_sender](F_Grasshopper_Kernel_GH_ObjectChangedEventArgs_m_sender.htm)|  
![Protected field](../icons/protfield.gif)|
[m_tag](F_Grasshopper_Kernel_GH_ObjectChangedEventArgs_m_tag.htm)|  
![Protected field](../icons/protfield.gif)|
[m_type](F_Grasshopper_Kernel_GH_ObjectChangedEventArgs_m_type.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

