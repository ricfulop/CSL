---
url: https://developer.rhino3d.com/api/grasshopper/html/T_GH_IO_Serialization_GH_Message.htm
scraped_at: 2025-09-08T16:10:47.840243
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[GH_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH_Message Class](../html/T_GH_IO_Serialization_GH_Message.htm "GH_Message
Class")

[GH_Message Constructor
](../html/Overload_GH_IO_Serialization_GH_Message__ctor.htm "GH_Message
Constructor ")

[GH_Message
Properties](../html/Properties_T_GH_IO_Serialization_GH_Message.htm
"GH_Message Properties")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Message Class  
  
---  
  
Represents an archive log message. Messages are collected during read/write
operations.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
GH_IO.SerializationGH_Message  

**Namespace:** [GH_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:** GH_IO (in GH_IO.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Message
    
    
    Public Class GH_Message

The GH_Message type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_Message](M_GH_IO_Serialization_GH_Message__ctor.htm)|  Fake constructor to
avoid new instances being created by a PropertyGrid.  
![Public method](../icons/pubmethod.gif)|
[GH_Message(String)](M_GH_IO_Serialization_GH_Message__ctor_1.htm)|  Create a
new message of type GH_Message_Type.info  
![Public method](../icons/pubmethod.gif)| [GH_Message(String,
GH_Message_Type)](M_GH_IO_Serialization_GH_Message__ctor_2.htm)|  Create a new
message.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Message](P_GH_IO_Serialization_GH_Message_Message.htm)|  Gets the text
content of this message.  
![Public property](../icons/pubproperty.gif)|
[Type](P_GH_IO_Serialization_GH_Message_Type.htm)|  Gets the type of this
message.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

