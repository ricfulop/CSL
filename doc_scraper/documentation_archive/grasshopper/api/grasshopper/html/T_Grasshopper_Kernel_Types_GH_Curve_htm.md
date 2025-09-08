---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_GH_Curve.htm
scraped_at: 2025-09-08T16:20:29.404728
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[GH_Curve Class](../html/T_Grasshopper_Kernel_Types_GH_Curve.htm "GH_Curve
Class")

[GH_Curve Constructor
](../html/Overload_Grasshopper_Kernel_Types_GH_Curve__ctor.htm "GH_Curve
Constructor ")

[GH_Curve
Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Curve.htm
"GH_Curve Properties")

[GH_Curve Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Curve.htm
"GH_Curve Methods")

[GH_Curve Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_Curve.htm
"GH_Curve Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Curve Class  
  
---  
  
Represents a 3D spline curve.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.Kernel.TypesGH_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)Curve  
[Grasshopper.Kernel.TypesGH_GeometricGoo](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm)Curve  
Grasshopper.Kernel.TypesGH_Curve  

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Curve : GH_GeometricGoo<Curve>, 
    	IGH_BakeAwareData, IGH_PreviewData
    
    
    Public Class GH_Curve
    	Inherits GH_GeometricGoo(Of Curve)
    	Implements IGH_BakeAwareData, IGH_PreviewData

The GH_Curve type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_Curve](M_Grasshopper_Kernel_Types_GH_Curve__ctor.htm)|  Default
constructor, creates an invalid curve.  
![Public method](../icons/pubmethod.gif)|
[GH_Curve(Curve)](M_Grasshopper_Kernel_Types_GH_Curve__ctor_2.htm)|  Create a
duplicate of an existing curve.  
![Public method](../icons/pubmethod.gif)|
[GH_Curve(GH_Curve)](M_Grasshopper_Kernel_Types_GH_Curve__ctor_1.htm)|  Create
a duplicate of another GH_Curve. This constructor also copies reference data.  
![Public method](../icons/pubmethod.gif)|
[GH_Curve(Guid)](M_Grasshopper_Kernel_Types_GH_Curve__ctor_3.htm)|  Create a
new referenced curve that references a Rhino curve object with the specified
ID.  
![Public method](../icons/pubmethod.gif)| [GH_Curve(Guid,
Int32)](M_Grasshopper_Kernel_Types_GH_Curve__ctor_4.htm)|  Create a new
references edge curve that references an edge index in a Rhino Brep object.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Boundingbox](P_Grasshopper_Kernel_Types_GH_Curve_Boundingbox.htm)|
(Overrides
[GH_GeometricGooTBoundingbox](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Boundingbox.htm).)  
![Public property](../icons/pubproperty.gif)|
[ClippingBox](P_Grasshopper_Kernel_Types_GH_Curve_ClippingBox.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_Curve_IsGeometryLoaded.htm)|
Gets the load state of this curve object. The curve is considered to be loaded
when the local OnCurve instance is not null.  (Overrides
[GH_GeometricGooTIsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsGeometryLoaded.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsReferencedGeometry](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsReferencedGeometry.htm)|
Gets a value indicating whether or not this geometry is referenced. Not all
IGH_GeometricGoo implementations support referenced geometry.  (Inherited from
[GH_GeometricGooT](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Kernel_Types_GH_Curve_IsValid.htm)|  Gets the validity
of this curve. If the curve is referenced but cannot be loaded, the curve is
not valid.  (Overrides
[GH_GeometricGooTIsValid](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsValid.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Curve_IsValidWhyNot.htm)|  Gets
a string describing the state of "invalidness". If the instance _is_ valid,
then this property should return Nothing or String.Empty.  (Overrides
[GH_GooTIsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm).)  
![Public property](../icons/pubproperty.gif)|
[ReferenceEdge](P_Grasshopper_Kernel_Types_GH_Curve_ReferenceEdge.htm)|  Gets
or sets the edge index for a referenced curve. If the index >= 0 then an edge
reference is implied.  
![Public property](../icons/pubproperty.gif)|
[ReferenceID](P_Grasshopper_Kernel_Types_GH_Curve_ReferenceID.htm)|
(Overrides
[GH_GeometricGooTReferenceID](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ReferenceID.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeDescription](P_Grasshopper_Kernel_Types_GH_Curve_TypeDescription.htm)|
(Overrides
[GH_GooTTypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_Types_GH_Curve_TypeName.htm)|  (Overrides
[GH_GooTTypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).)  
![Public property](../icons/pubproperty.gif)|
[Value](P_Grasshopper_Kernel_Types_GH_Curve_Value.htm)|  (Overrides
[GH_GeometricGooTValue](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Value.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[BakeGeometry](M_Grasshopper_Kernel_Types_GH_Curve_BakeGeometry.htm)|  
![Public method](../icons/pubmethod.gif)|
[CastFrom](M_Grasshopper_Kernel_Types_GH_Curve_CastFrom.htm)|  Remote to Local
caster function. This stuff is complex, don't concern yourself with casting
logic.  (Overrides
[GH_GeometricGooTCastFrom(Object)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastFrom.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Kernel_Types_GH_Curve_CastTo__1.htm)|  Local to
Remote caster function. This stuff is complex, don't concern yourself with
casting logic.  (Overrides
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
[ClearCaches](M_Grasshopper_Kernel_Types_GH_Curve_ClearCaches.htm)|  Clears
all volatile caches for this instance. The boundingbox is cleared, and if the
curve is referenced, the local instance of the curve is erased.  (Overrides
[GH_GeometricGooTClearCaches](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ClearCaches.htm).)  
![Public method](../icons/pubmethod.gif)|
[DrawViewportMeshes](M_Grasshopper_Kernel_Types_GH_Curve_DrawViewportMeshes.htm)|  
![Public method](../icons/pubmethod.gif)|
[DrawViewportWires](M_Grasshopper_Kernel_Types_GH_Curve_DrawViewportWires.htm)|  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Kernel_Types_GH_Curve_Duplicate.htm)|  (Overrides
[GH_GeometricGooTDuplicate](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Duplicate.htm).)  
![Public method](../icons/pubmethod.gif)|
[DuplicateCurve](M_Grasshopper_Kernel_Types_GH_Curve_DuplicateCurve.htm)|
Create a duplicate of this curve.  
![Public method](../icons/pubmethod.gif)|
[DuplicateGeometry](M_Grasshopper_Kernel_Types_GH_Curve_DuplicateGeometry.htm)|
Create a duplicate of this curve.  (Overrides
[GH_GeometricGooTDuplicateGeometry](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_DuplicateGeometry.htm).)  
![Public method](../icons/pubmethod.gif)|
[EmitProxy](M_Grasshopper_Kernel_Types_GH_Curve_EmitProxy.htm)|  Returns a
proxy that represents this curve. Do not call this function unless you're
(Overrides
[GH_GeometricGooTEmitProxy](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_EmitProxy.htm).)  
![Public method](../icons/pubmethod.gif)|
[GetBoundingBox](M_Grasshopper_Kernel_Types_GH_Curve_GetBoundingBox.htm)|
(Overrides
[GH_GeometricGooTGetBoundingBox(Transform)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_GetBoundingBox.htm).)  
![Public method](../icons/pubmethod.gif)|
[LoadGeometry](M_Grasshopper_Kernel_Types_GH_Curve_LoadGeometry.htm)|  If the
geometry is referenced and not yet loaded, attempts to load the geometry.
(Overrides
[GH_GeometricGooTLoadGeometry](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry.htm).)  
![Public method](../icons/pubmethod.gif)|
[LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_Curve_LoadGeometry_1.htm)|
If the curve is referenced and not yet loaded, attempts to load the curve.
(Overrides
[GH_GeometricGooTLoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[MakeDeformable](M_Grasshopper_Kernel_Types_GH_Curve_MakeDeformable.htm)|
Converts the local geometry into deformable nurbs curve geometry. This method
will not destroy Reference data.  
![Public method](../icons/pubmethod.gif)|
[Morph](M_Grasshopper_Kernel_Types_GH_Curve_Morph.htm)|  (Overrides
[GH_GeometricGooTMorph(SpaceMorph)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Morph.htm).)  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_Types_GH_Curve_Read.htm)|  (Overrides
[GH_GooTRead(GH_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).)  
![Public method](../icons/pubmethod.gif)|
[ScriptVariable](M_Grasshopper_Kernel_Types_GH_Curve_ScriptVariable.htm)|
(Overrides
[GH_GooTScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Types_GH_Curve_ToString.htm)|  Format the
curve using default grasshopper formatting logic.  (Overrides
[GH_GooTToString](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).)  
![Public method](../icons/pubmethod.gif)|
[Transform](M_Grasshopper_Kernel_Types_GH_Curve_Transform.htm)|  (Overrides
[GH_GeometricGooTTransform(Transform)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Transform.htm).)  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_Types_GH_Curve_Write.htm)|  (Overrides
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

