---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_GH_Brep.htm
scraped_at: 2025-09-08T16:20:21.347413
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[GH_Brep Class](../html/T_Grasshopper_Kernel_Types_GH_Brep.htm "GH_Brep
Class")

[GH_Brep Constructor
](../html/Overload_Grasshopper_Kernel_Types_GH_Brep__ctor.htm "GH_Brep
Constructor ")

[GH_Brep Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Brep.htm
"GH_Brep Properties")

[GH_Brep Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Brep.htm
"GH_Brep Methods")

[GH_Brep Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_Brep.htm
"GH_Brep Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Brep Class  
  
---  
  
Represents a 3D polysurface. GH_Brep wraps the functionality of the OpenNURBS
OnBrep class.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.Kernel.TypesGH_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)Brep  
[Grasshopper.Kernel.TypesGH_GeometricGoo](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm)Brep  
Grasshopper.Kernel.TypesGH_Brep  

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Brep : GH_GeometricGoo<Brep>, 
    	IGH_BakeAwareData, IGH_PreviewData, IGH_PreviewMeshData, IGH_RenderAwareData
    
    
    Public Class GH_Brep
    	Inherits GH_GeometricGoo(Of Brep)
    	Implements IGH_BakeAwareData, IGH_PreviewData, IGH_PreviewMeshData, IGH_RenderAwareData

The GH_Brep type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_Brep](M_Grasshopper_Kernel_Types_GH_Brep__ctor.htm)| Initializes a new
instance of the GH_Brep class  
![Public method](../icons/pubmethod.gif)|
[GH_Brep(Brep)](M_Grasshopper_Kernel_Types_GH_Brep__ctor_2.htm)| Initializes a
new instance of the GH_Brep class  
![Public method](../icons/pubmethod.gif)|
[GH_Brep(GH_Brep)](M_Grasshopper_Kernel_Types_GH_Brep__ctor_1.htm)|
Initializes a new instance of the GH_Brep class  
![Public method](../icons/pubmethod.gif)|
[GH_Brep(Guid)](M_Grasshopper_Kernel_Types_GH_Brep__ctor_3.htm)| Initializes a
new instance of the GH_Brep class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Boundingbox](P_Grasshopper_Kernel_Types_GH_Brep_Boundingbox.htm)|  (Overrides
[GH_GeometricGooTBoundingbox](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Boundingbox.htm).)  
![Public property](../icons/pubproperty.gif)|
[ClippingBox](P_Grasshopper_Kernel_Types_GH_Brep_ClippingBox.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_Brep_IsGeometryLoaded.htm)|
(Overrides
[GH_GeometricGooTIsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsGeometryLoaded.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsReferencedGeometry](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsReferencedGeometry.htm)|
Gets a value indicating whether or not this geometry is referenced. Not all
IGH_GeometricGoo implementations support referenced geometry.  (Inherited from
[GH_GeometricGooT](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Kernel_Types_GH_Brep_IsValid.htm)|  (Overrides
[GH_GeometricGooTIsValid](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsValid.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Brep_IsValidWhyNot.htm)|  Gets a
string describing the state of "invalidness". If the instance _is_ valid, then
this property should return Nothing or String.Empty.  (Overrides
[GH_GooTIsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm).)  
![Public property](../icons/pubproperty.gif)|
[ReferenceID](P_Grasshopper_Kernel_Types_GH_Brep_ReferenceID.htm)|  (Overrides
[GH_GeometricGooTReferenceID](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ReferenceID.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeDescription](P_Grasshopper_Kernel_Types_GH_Brep_TypeDescription.htm)|
(Overrides
[GH_GooTTypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_Types_GH_Brep_TypeName.htm)|  (Overrides
[GH_GooTTypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).)  
![Public property](../icons/pubproperty.gif)|
[Value](P_Grasshopper_Kernel_Types_GH_Brep_Value.htm)|  (Overrides
[GH_GeometricGooTValue](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Value.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AppendRenderGeometry](M_Grasshopper_Kernel_Types_GH_Brep_AppendRenderGeometry.htm)|  
![Public method](../icons/pubmethod.gif)|
[BakeGeometry](M_Grasshopper_Kernel_Types_GH_Brep_BakeGeometry.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[BrepTightBoundingBox](M_Grasshopper_Kernel_Types_GH_Brep_BrepTightBoundingBox.htm)|
Compute the boundingbox of a Brep object without meshing.  
![Public method](../icons/pubmethod.gif)|
[CastFrom](M_Grasshopper_Kernel_Types_GH_Brep_CastFrom.htm)|  (Overrides
[GH_GeometricGooTCastFrom(Object)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastFrom.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Kernel_Types_GH_Brep_CastTo__1.htm)|  (Overrides
[GH_GeometricGooTCastToQ(Q)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo__1.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToQ(Q)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo__1.htm)|
Attempt a cast to type T.  (Inherited from
[GH_GeometricGooT](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToQ(Q)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm)|  Attempt a
cast to type Q.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[ClearCaches](M_Grasshopper_Kernel_Types_GH_Brep_ClearCaches.htm)|  (Overrides
[GH_GeometricGooTClearCaches](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ClearCaches.htm).)  
![Public method](../icons/pubmethod.gif)|
[DestroyPreviewMeshes](M_Grasshopper_Kernel_Types_GH_Brep_DestroyPreviewMeshes.htm)|  
![Public method](../icons/pubmethod.gif)|
[DrawViewportMeshes](M_Grasshopper_Kernel_Types_GH_Brep_DrawViewportMeshes.htm)|  
![Public method](../icons/pubmethod.gif)|
[DrawViewportWires](M_Grasshopper_Kernel_Types_GH_Brep_DrawViewportWires.htm)|  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Kernel_Types_GH_Brep_Duplicate.htm)|  (Overrides
[GH_GeometricGooTDuplicate](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Duplicate.htm).)  
![Public method](../icons/pubmethod.gif)|
[DuplicateBrep](M_Grasshopper_Kernel_Types_GH_Brep_DuplicateBrep.htm)|  
![Public method](../icons/pubmethod.gif)|
[DuplicateGeometry](M_Grasshopper_Kernel_Types_GH_Brep_DuplicateGeometry.htm)|
(Overrides
[GH_GeometricGooTDuplicateGeometry](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_DuplicateGeometry.htm).)  
![Public method](../icons/pubmethod.gif)|
[EmitProxy](M_Grasshopper_Kernel_Types_GH_Brep_EmitProxy.htm)|  (Overrides
[GH_GeometricGooTEmitProxy](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_EmitProxy.htm).)  
![Public method](../icons/pubmethod.gif)|
[GetBoundingBox](M_Grasshopper_Kernel_Types_GH_Brep_GetBoundingBox.htm)|
(Overrides
[GH_GeometricGooTGetBoundingBox(Transform)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_GetBoundingBox.htm).)  
![Public method](../icons/pubmethod.gif)|
[GetPreviewMeshes](M_Grasshopper_Kernel_Types_GH_Brep_GetPreviewMeshes.htm)|  
![Public method](../icons/pubmethod.gif)|
[LoadGeometry](M_Grasshopper_Kernel_Types_GH_Brep_LoadGeometry.htm)|  If the
geometry is referenced and not yet loaded, attempts to load the geometry.
(Overrides
[GH_GeometricGooTLoadGeometry](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry.htm).)  
![Public method](../icons/pubmethod.gif)|
[LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_Brep_LoadGeometry_1.htm)|
(Overrides
[GH_GeometricGooTLoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[Morph](M_Grasshopper_Kernel_Types_GH_Brep_Morph.htm)|  (Overrides
[GH_GeometricGooTMorph(SpaceMorph)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Morph.htm).)  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_Types_GH_Brep_Read.htm)|  (Overrides
[GH_GooTRead(GH_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).)  
![Public method](../icons/pubmethod.gif)|
[ScriptVariable](M_Grasshopper_Kernel_Types_GH_Brep_ScriptVariable.htm)|
(Overrides
[GH_GooTScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Types_GH_Brep_ToString.htm)|  (Overrides
[GH_GooTToString](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).)  
![Public method](../icons/pubmethod.gif)|
[Transform](M_Grasshopper_Kernel_Types_GH_Brep_Transform.htm)|  (Overrides
[GH_GeometricGooTTransform(Transform)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Transform.htm).)  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_Types_GH_Brep_Write.htm)|  (Overrides
[GH_GooTWrite(GH_IWriter)](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm).)  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Protected field](../icons/protfield.gif)|
[m_value](F_Grasshopper_Kernel_Types_GH_Goo_1_m_value.htm)|  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

