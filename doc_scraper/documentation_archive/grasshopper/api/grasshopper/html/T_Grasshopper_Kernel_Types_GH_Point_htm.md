---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_GH_Point.htm
scraped_at: 2025-09-08T16:21:16.564128
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[GH_Point Class](../html/T_Grasshopper_Kernel_Types_GH_Point.htm "GH_Point
Class")

[GH_Point Constructor
](../html/Overload_Grasshopper_Kernel_Types_GH_Point__ctor.htm "GH_Point
Constructor ")

[GH_Point
Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Point.htm
"GH_Point Properties")

[GH_Point Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Point.htm
"GH_Point Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Point Class  
  
---  
  
![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Kernel.TypesGH_Point  

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Point : IGH_GeometricGoo, IGH_BakeAwareData, 
    	IGH_PreviewData
    
    
    Public Class GH_Point
    	Implements IGH_GeometricGoo, IGH_BakeAwareData, IGH_PreviewData

The GH_Point type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_Point](M_Grasshopper_Kernel_Types_GH_Point__ctor.htm)| Initializes a new
instance of the GH_Point class  
![Public method](../icons/pubmethod.gif)|
[GH_Point(GH_Point)](M_Grasshopper_Kernel_Types_GH_Point__ctor_1.htm)|
Initializes a new instance of the GH_Point class  
![Public method](../icons/pubmethod.gif)|
[GH_Point(Guid)](M_Grasshopper_Kernel_Types_GH_Point__ctor_3.htm)| Initializes
a new instance of the GH_Point class  
![Public method](../icons/pubmethod.gif)|
[GH_Point(Point3d)](M_Grasshopper_Kernel_Types_GH_Point__ctor_2.htm)|
Initializes a new instance of the GH_Point class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Boundingbox](P_Grasshopper_Kernel_Types_GH_Point_Boundingbox.htm)|  
![Public property](../icons/pubproperty.gif)|
[ClippingBox](P_Grasshopper_Kernel_Types_GH_Point_ClippingBox.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_Point_IsGeometryLoaded.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsReferencedGeometry](P_Grasshopper_Kernel_Types_GH_Point_IsReferencedGeometry.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Kernel_Types_GH_Point_IsValid.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Point_IsValidWhyNot.htm)|  Gets
a string describing the state of "invalidness". If the instance _is_ valid,
then this property should return Nothing or String.Empty.  
![Public property](../icons/pubproperty.gif)|
[ReferenceData](P_Grasshopper_Kernel_Types_GH_Point_ReferenceData.htm)|  Gets
or sets the reference data of this point geometry.  
![Public property](../icons/pubproperty.gif)|
[ReferenceID](P_Grasshopper_Kernel_Types_GH_Point_ReferenceID.htm)|  
![Public property](../icons/pubproperty.gif)|
[TypeDescription](P_Grasshopper_Kernel_Types_GH_Point_TypeDescription.htm)|  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_Types_GH_Point_TypeName.htm)|  
![Public property](../icons/pubproperty.gif)|
[Value](P_Grasshopper_Kernel_Types_GH_Point_Value.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[BakeGeometry](M_Grasshopper_Kernel_Types_GH_Point_BakeGeometry.htm)|  
![Public method](../icons/pubmethod.gif)|
[CastFrom](M_Grasshopper_Kernel_Types_GH_Point_CastFrom.htm)|  
![Public method](../icons/pubmethod.gif)|
[CastToT](M_Grasshopper_Kernel_Types_GH_Point_CastTo__1.htm)|  
![Public method](../icons/pubmethod.gif)|
[ClearCaches](M_Grasshopper_Kernel_Types_GH_Point_ClearCaches.htm)|  
![Public method](../icons/pubmethod.gif)|
[CreateFromCoordinate](M_Grasshopper_Kernel_Types_GH_Point_CreateFromCoordinate.htm)|
Create a new point geometry instance based on a fixed coordinate  
![Public method](../icons/pubmethod.gif)|
[CreateFromCurveDistance](M_Grasshopper_Kernel_Types_GH_Point_CreateFromCurveDistance.htm)|
Create new point geometry instance based on a curve distance parameter  
![Public method](../icons/pubmethod.gif)|
[CreateFromCurveRatio](M_Grasshopper_Kernel_Types_GH_Point_CreateFromCurveRatio.htm)|
Create new point geometry instance based on a curve parameter ratio  
![Public method](../icons/pubmethod.gif)|
[CreateFromEdgeDistance](M_Grasshopper_Kernel_Types_GH_Point_CreateFromEdgeDistance.htm)|
Create new point geometry instance based on a curve distance parameter  
![Public method](../icons/pubmethod.gif)|
[CreateFromEdgeRatio](M_Grasshopper_Kernel_Types_GH_Point_CreateFromEdgeRatio.htm)|
Create new point geometry instance based on an edge parameter ratio  
![Public method](../icons/pubmethod.gif)|
[CreateFromPointObject](M_Grasshopper_Kernel_Types_GH_Point_CreateFromPointObject.htm)|
Create a new point geometry instance based on point object ID. Technically
this now also accepts Dot object IDs.  
![Public method](../icons/pubmethod.gif)|
[CreateFromSurfaceParam](M_Grasshopper_Kernel_Types_GH_Point_CreateFromSurfaceParam.htm)|
Create new point geometry instance based on a curve distance parameter  
![Public method](../icons/pubmethod.gif)|
[DrawViewportMeshes](M_Grasshopper_Kernel_Types_GH_Point_DrawViewportMeshes.htm)|  
![Public method](../icons/pubmethod.gif)|
[DrawViewportWires](M_Grasshopper_Kernel_Types_GH_Point_DrawViewportWires.htm)|  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Kernel_Types_GH_Point_Duplicate.htm)|  
![Public method](../icons/pubmethod.gif)|
[DuplicateGeometry](M_Grasshopper_Kernel_Types_GH_Point_DuplicateGeometry.htm)|  
![Public method](../icons/pubmethod.gif)|
[DuplicatePoint](M_Grasshopper_Kernel_Types_GH_Point_DuplicatePoint.htm)|  
![Public method](../icons/pubmethod.gif)|
[EmitProxy](M_Grasshopper_Kernel_Types_GH_Point_EmitProxy.htm)|  
![Public method](../icons/pubmethod.gif)|
[EnsureReferenceData](M_Grasshopper_Kernel_Types_GH_Point_EnsureReferenceData.htm)|
Creates new Reference data if it doesn't already exists  
![Public method](../icons/pubmethod.gif)|
[GetBoundingBox](M_Grasshopper_Kernel_Types_GH_Point_GetBoundingBox.htm)|  
![Public method](../icons/pubmethod.gif)|
[LoadGeometry](M_Grasshopper_Kernel_Types_GH_Point_LoadGeometry.htm)|  
![Public method](../icons/pubmethod.gif)|
[LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_Point_LoadGeometry_1.htm)|  
![Public method](../icons/pubmethod.gif)|
[Morph](M_Grasshopper_Kernel_Types_GH_Point_Morph.htm)|  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_Types_GH_Point_Read.htm)|  
![Public method](../icons/pubmethod.gif)|
[ReferenceCurve](M_Grasshopper_Kernel_Types_GH_Point_ReferenceCurve.htm)|  
![Public method](../icons/pubmethod.gif)|
[ReferenceCurve(RhinoObject)](M_Grasshopper_Kernel_Types_GH_Point_ReferenceCurve_1.htm)|  
![Public method](../icons/pubmethod.gif)|
[ReferenceIndex](M_Grasshopper_Kernel_Types_GH_Point_ReferenceIndex.htm)|
Retrieve the index of the point reference data.  
![Public method](../icons/pubmethod.gif)|
[ReferenceIndex(Int32)](M_Grasshopper_Kernel_Types_GH_Point_ReferenceIndex_1.htm)|
Sets the index of the point reference data.  
![Public method](../icons/pubmethod.gif)|
[ReferenceParam(Int32)](M_Grasshopper_Kernel_Types_GH_Point_ReferenceParam.htm)|
Retrieve the indexed param of the point reference data.  
![Public method](../icons/pubmethod.gif)| [ReferenceParam(Int32,
Double)](M_Grasshopper_Kernel_Types_GH_Point_ReferenceParam_1.htm)|  Sets the
index of the point reference data.  
![Public method](../icons/pubmethod.gif)|
[ReferencesCurve](M_Grasshopper_Kernel_Types_GH_Point_ReferencesCurve.htm)|
Returns true if this point is based on a curve reference  
![Public method](../icons/pubmethod.gif)|
[ReferencesEdge](M_Grasshopper_Kernel_Types_GH_Point_ReferencesEdge.htm)|
Returns True if this point is based on an edge reference  
![Public method](../icons/pubmethod.gif)|
[ReferenceSurface](M_Grasshopper_Kernel_Types_GH_Point_ReferenceSurface.htm)|  
![Public method](../icons/pubmethod.gif)|
[ReferenceType](M_Grasshopper_Kernel_Types_GH_Point_ReferenceType.htm)|
Retrieve the reference type of this point object.  
![Public method](../icons/pubmethod.gif)|
[ReferenceType(GH_PointRefType)](M_Grasshopper_Kernel_Types_GH_Point_ReferenceType_1.htm)|
Sets the type of the point reference data.  
![Public method](../icons/pubmethod.gif)|
[ScriptVariable](M_Grasshopper_Kernel_Types_GH_Point_ScriptVariable.htm)|  
![Public method](../icons/pubmethod.gif)|
[SetReferenceParams](M_Grasshopper_Kernel_Types_GH_Point_SetReferenceParams.htm)|
Sets both param values of the point reference  
![Public method](../icons/pubmethod.gif)|
[ShowReferenceDialog](M_Grasshopper_Kernel_Types_GH_Point_ShowReferenceDialog.htm)|  
![Public method](../icons/pubmethod.gif)|
[ShowReferenceDialog(IWin32Window)](M_Grasshopper_Kernel_Types_GH_Point_ShowReferenceDialog_1.htm)|  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Types_GH_Point_ToString.htm)|  (Overrides
[ObjectToString](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring).)  
![Public method](../icons/pubmethod.gif)|
[Transform](M_Grasshopper_Kernel_Types_GH_Point_Transform.htm)|  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_Types_GH_Point_Write.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

