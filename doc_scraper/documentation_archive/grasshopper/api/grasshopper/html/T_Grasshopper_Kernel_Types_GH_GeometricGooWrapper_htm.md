---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_GH_GeometricGooWrapper.htm
scraped_at: 2025-09-08T16:20:40.393509
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[GH_GeometricGooWrapper
Class](../html/T_Grasshopper_Kernel_Types_GH_GeometricGooWrapper.htm
"GH_GeometricGooWrapper Class")

[GH_GeometricGooWrapper Constructor
](../html/Overload_Grasshopper_Kernel_Types_GH_GeometricGooWrapper__ctor.htm
"GH_GeometricGooWrapper Constructor ")

[GH_GeometricGooWrapper
Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_GeometricGooWrapper.htm
"GH_GeometricGooWrapper Properties")

[GH_GeometricGooWrapper
Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_GeometricGooWrapper.htm
"GH_GeometricGooWrapper Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_GeometricGooWrapper Class  
  
---  
  
Utility class for maintaining all kinds of IGH_GeometricGoo types.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Kernel.TypesGH_GeometricGooWrapper  

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class GH_GeometricGooWrapper : IGH_GeometricGoo
    
    
    Public NotInheritable Class GH_GeometricGooWrapper
    	Implements IGH_GeometricGoo

The GH_GeometricGooWrapper type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_GeometricGooWrapper](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper__ctor.htm)|
Initializes a new instance of the GH_GeometricGooWrapper class  
![Public method](../icons/pubmethod.gif)|
[GH_GeometricGooWrapper(IGH_GeometricGoo)](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper__ctor_1.htm)|
Initializes a new instance of the GH_GeometricGooWrapper class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Boundingbox](P_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_Boundingbox.htm)|  
![Public property](../icons/pubproperty.gif)|
[InternalGoo](P_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_InternalGoo.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_IsGeometryLoaded.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsReferencedGeometry](P_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_IsReferencedGeometry.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_IsValid.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_IsValidWhyNot.htm)|  
![Public property](../icons/pubproperty.gif)|
[ReferenceID](P_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_ReferenceID.htm)|  
![Public property](../icons/pubproperty.gif)|
[TypeDescription](P_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_TypeDescription.htm)|  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_TypeName.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CastFrom](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_CastFrom.htm)|  
![Public method](../icons/pubmethod.gif)|
[CastToT](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_CastTo__1.htm)|  
![Public method](../icons/pubmethod.gif)|
[ClearCaches](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_ClearCaches.htm)|  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_Duplicate.htm)|  
![Public method](../icons/pubmethod.gif)|
[DuplicateGeometry](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_DuplicateGeometry.htm)|  
![Public method](../icons/pubmethod.gif)|
[EmitProxy](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_EmitProxy.htm)|  
![Public method](../icons/pubmethod.gif)|
[GetBoundingBox](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_GetBoundingBox.htm)|  
![Public method](../icons/pubmethod.gif)|
[LoadGeometry](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_LoadGeometry.htm)|  
![Public method](../icons/pubmethod.gif)|
[LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_LoadGeometry_1.htm)|  
![Public method](../icons/pubmethod.gif)|
[Morph](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_Morph.htm)|  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_Read.htm)|  
![Public method](../icons/pubmethod.gif)|
[ScriptVariable](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_ScriptVariable.htm)|
This function will be called when the local IGH_Goo instance disapears into a
user Script. This would be an excellent place to cast your IGH_Goo type to a
simple data type.  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_ToString.htm)|
(Overrides
[ObjectToString](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring).)  
![Public method](../icons/pubmethod.gif)|
[Transform](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_Transform.htm)|  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_Write.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

