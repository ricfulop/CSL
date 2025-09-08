---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_RelevantObjectData.htm
scraped_at: 2025-09-08T16:17:44.629480
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_RelevantObjectData
Class](../html/T_Grasshopper_Kernel_GH_RelevantObjectData.htm
"GH_RelevantObjectData Class")

[GH_RelevantObjectData Constructor
](../html/M_Grasshopper_Kernel_GH_RelevantObjectData__ctor.htm
"GH_RelevantObjectData Constructor ")

[GH_RelevantObjectData
Properties](../html/Properties_T_Grasshopper_Kernel_GH_RelevantObjectData.htm
"GH_RelevantObjectData Properties")

[GH_RelevantObjectData
Methods](../html/Methods_T_Grasshopper_Kernel_GH_RelevantObjectData.htm
"GH_RelevantObjectData Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_RelevantObjectData Class  
  
---  
  
Contains information about relevant objects at a specific canvas location.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_RelevantObjectData  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_RelevantObjectData
    
    
    Public Class GH_RelevantObjectData

The GH_RelevantObjectData type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_RelevantObjectData](M_Grasshopper_Kernel_GH_RelevantObjectData__ctor.htm)|
Construct a new instance.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Attributes](P_Grasshopper_Kernel_GH_RelevantObjectData_Attributes.htm)|  Gets
the attributes that belong to the object.  
![Public property](../icons/pubproperty.gif)|
[Group](P_Grasshopper_Kernel_GH_RelevantObjectData_Group.htm)|  Gets the cast
of the DocObject to GH_Group.  
![Public property](../icons/pubproperty.gif)|
[IsTopLevelObject](P_Grasshopper_Kernel_GH_RelevantObjectData_IsTopLevelObject.htm)|
Gets a value indicating whether or not the Object is a top-level object.  
![Public property](../icons/pubproperty.gif)|
[Object](P_Grasshopper_Kernel_GH_RelevantObjectData_Object.htm)|  Gets the raw
object cached in this data instance.  
![Public property](../icons/pubproperty.gif)|
[ObjectType](P_Grasshopper_Kernel_GH_RelevantObjectData_ObjectType.htm)|  Gets
the type of object indicated by this data.  
![Public property](../icons/pubproperty.gif)|
[Parameter](P_Grasshopper_Kernel_GH_RelevantObjectData_Parameter.htm)|  Gets
the cast of the DocObject to IGH_Param. If the DocObject is not of type
IGH_Param, the attributes of the object will be perused to find a nested
IGH_Param at the point.  
![Public property](../icons/pubproperty.gif)|
[Point](P_Grasshopper_Kernel_GH_RelevantObjectData_Point.htm)|  Gets the point
for which this GH_RelevantObjectData has been made.  
![Public property](../icons/pubproperty.gif)|
[TopLevelObject](P_Grasshopper_Kernel_GH_RelevantObjectData_TopLevelObject.htm)|
Gets the top-level object.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CreateBalloonData](M_Grasshopper_Kernel_GH_RelevantObjectData_CreateBalloonData.htm)|  
![Public method](../icons/pubmethod.gif)|
[CreateGripData](M_Grasshopper_Kernel_GH_RelevantObjectData_CreateGripData.htm)|  
![Public method](../icons/pubmethod.gif)|
[CreateGroupData](M_Grasshopper_Kernel_GH_RelevantObjectData_CreateGroupData.htm)|  
![Public method](../icons/pubmethod.gif)|
[CreateObjectData](M_Grasshopper_Kernel_GH_RelevantObjectData_CreateObjectData.htm)|  
![Public method](../icons/pubmethod.gif)|
[CreateWireData](M_Grasshopper_Kernel_GH_RelevantObjectData_CreateWireData.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

