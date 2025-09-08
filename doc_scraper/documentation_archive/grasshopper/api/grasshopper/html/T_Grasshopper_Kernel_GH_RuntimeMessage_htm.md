---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_RuntimeMessage.htm
scraped_at: 2025-09-08T16:17:47.690660
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_RuntimeMessage Class](../html/T_Grasshopper_Kernel_GH_RuntimeMessage.htm
"GH_RuntimeMessage Class")

[GH_RuntimeMessage Constructor
](../html/M_Grasshopper_Kernel_GH_RuntimeMessage__ctor.htm "GH_RuntimeMessage
Constructor ")

[GH_RuntimeMessage
Properties](../html/Properties_T_Grasshopper_Kernel_GH_RuntimeMessage.htm
"GH_RuntimeMessage Properties")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_RuntimeMessage Class  
  
---  
  
Contains all fields that together define a RuntimeMessage. Runtime Messages
are created and recorded by document objects during Grasshopper solutions.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_RuntimeMessage  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_RuntimeMessage
    
    
    Public Class GH_RuntimeMessage

The GH_RuntimeMessage type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_RuntimeMessage](M_Grasshopper_Kernel_GH_RuntimeMessage__ctor.htm)|
Initializes a new instance of the GH_RuntimeMessage class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Event](P_Grasshopper_Kernel_GH_RuntimeMessage_Event.htm)|  Gets the time at
which the message was recorded.  
![Public property](../icons/pubproperty.gif)|
[HasSource](P_Grasshopper_Kernel_GH_RuntimeMessage_HasSource.htm)|  Gets a
value indicating whether or not this message has a source.  
![Public property](../icons/pubproperty.gif)|
[Message](P_Grasshopper_Kernel_GH_RuntimeMessage_Message.htm)|  Gets the
contents of the message.  
![Public property](../icons/pubproperty.gif)|
[Source](P_Grasshopper_Kernel_GH_RuntimeMessage_Source.htm)|  Gets a string
describing the source object that created the message.  
![Public property](../icons/pubproperty.gif)|
[Type](P_Grasshopper_Kernel_GH_RuntimeMessage_Type.htm)|  Gets the type
qualifier of the message.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

