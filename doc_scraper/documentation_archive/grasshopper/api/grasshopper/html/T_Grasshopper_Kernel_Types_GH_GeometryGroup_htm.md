---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_GH_GeometryGroup.htm
scraped_at: 2025-09-08T16:20:41.399459
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[GH_GeometryGroup
Class](../html/T_Grasshopper_Kernel_Types_GH_GeometryGroup.htm
"GH_GeometryGroup Class")

[GH_GeometryGroup Constructor
](../html/M_Grasshopper_Kernel_Types_GH_GeometryGroup__ctor.htm
"GH_GeometryGroup Constructor ")

[GH_GeometryGroup
Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_GeometryGroup.htm
"GH_GeometryGroup Properties")

[GH_GeometryGroup
Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_GeometryGroup.htm
"GH_GeometryGroup Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_GeometryGroup Class  
  
---  
  
![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Kernel.TypesGH_GeometryGroup  

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_GeometryGroup : IGH_GeometricGoo, 
    	IGH_BakeAwareData, IGH_RenderAwareData, IGH_PreviewData
    
    
    Public Class GH_GeometryGroup
    	Implements IGH_GeometricGoo, IGH_BakeAwareData, IGH_RenderAwareData, IGH_PreviewData

The GH_GeometryGroup type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_GeometryGroup](M_Grasshopper_Kernel_Types_GH_GeometryGroup__ctor.htm)|
Initializes a new instance of the GH_GeometryGroup class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Boundingbox](P_Grasshopper_Kernel_Types_GH_GeometryGroup_Boundingbox.htm)|  
![Public property](../icons/pubproperty.gif)|
[ClippingBox](P_Grasshopper_Kernel_Types_GH_GeometryGroup_ClippingBox.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_GeometryGroup_IsGeometryLoaded.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsReferencedGeometry](P_Grasshopper_Kernel_Types_GH_GeometryGroup_IsReferencedGeometry.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Kernel_Types_GH_GeometryGroup_IsValid.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_GeometryGroup_IsValidWhyNot.htm)|  
![Public property](../icons/pubproperty.gif)|
[Name](P_Grasshopper_Kernel_Types_GH_GeometryGroup_Name.htm)|  
![Public property](../icons/pubproperty.gif)|
[Objects](P_Grasshopper_Kernel_Types_GH_GeometryGroup_Objects.htm)|  
![Public property](../icons/pubproperty.gif)|
[ReferenceID](P_Grasshopper_Kernel_Types_GH_GeometryGroup_ReferenceID.htm)|  
![Public property](../icons/pubproperty.gif)|
[TypeDescription](P_Grasshopper_Kernel_Types_GH_GeometryGroup_TypeDescription.htm)|  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_Types_GH_GeometryGroup_TypeName.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AppendRenderGeometry](M_Grasshopper_Kernel_Types_GH_GeometryGroup_AppendRenderGeometry.htm)|  
![Public method](../icons/pubmethod.gif)|
[BakeGeometry](M_Grasshopper_Kernel_Types_GH_GeometryGroup_BakeGeometry.htm)|  
![Public method](../icons/pubmethod.gif)|
[CastFrom](M_Grasshopper_Kernel_Types_GH_GeometryGroup_CastFrom.htm)|  
![Public method](../icons/pubmethod.gif)|
[CastToT](M_Grasshopper_Kernel_Types_GH_GeometryGroup_CastTo__1.htm)|  
![Public method](../icons/pubmethod.gif)|
[ClearCaches](M_Grasshopper_Kernel_Types_GH_GeometryGroup_ClearCaches.htm)|  
![Public method](../icons/pubmethod.gif)|
[DrawViewportMeshes](M_Grasshopper_Kernel_Types_GH_GeometryGroup_DrawViewportMeshes.htm)|  
![Public method](../icons/pubmethod.gif)|
[DrawViewportWires](M_Grasshopper_Kernel_Types_GH_GeometryGroup_DrawViewportWires.htm)|  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Kernel_Types_GH_GeometryGroup_Duplicate.htm)|  
![Public method](../icons/pubmethod.gif)|
[DuplicateGeometry](M_Grasshopper_Kernel_Types_GH_GeometryGroup_DuplicateGeometry.htm)|  
![Public method](../icons/pubmethod.gif)|
[EmitProxy](M_Grasshopper_Kernel_Types_GH_GeometryGroup_EmitProxy.htm)|  
![Public method](../icons/pubmethod.gif)|
[GetBoundingBox](M_Grasshopper_Kernel_Types_GH_GeometryGroup_GetBoundingBox.htm)|  
![Public method](../icons/pubmethod.gif)|
[LoadGeometry](M_Grasshopper_Kernel_Types_GH_GeometryGroup_LoadGeometry.htm)|  
![Public method](../icons/pubmethod.gif)|
[LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_GeometryGroup_LoadGeometry_1.htm)|  
![Public method](../icons/pubmethod.gif)|
[Morph](M_Grasshopper_Kernel_Types_GH_GeometryGroup_Morph.htm)|  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_Types_GH_GeometryGroup_Read.htm)|  
![Public method](../icons/pubmethod.gif)|
[ScriptVariable](M_Grasshopper_Kernel_Types_GH_GeometryGroup_ScriptVariable.htm)|  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Types_GH_GeometryGroup_ToString.htm)|
(Overrides
[ObjectToString](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring).)  
![Public method](../icons/pubmethod.gif)|
[Transform](M_Grasshopper_Kernel_Types_GH_GeometryGroup_Transform.htm)|  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_Types_GH_GeometryGroup_Write.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

