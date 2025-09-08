---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_GH_Plane.htm
scraped_at: 2025-09-08T16:21:14.565592
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[GH_Plane Class](../html/T_Grasshopper_Kernel_Types_GH_Plane.htm "GH_Plane
Class")

[GH_Plane Constructor
](../html/Overload_Grasshopper_Kernel_Types_GH_Plane__ctor.htm "GH_Plane
Constructor ")

[GH_Plane
Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Plane.htm
"GH_Plane Properties")

[GH_Plane Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Plane.htm
"GH_Plane Methods")

[GH_Plane Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_Plane.htm
"GH_Plane Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Plane Class  
  
---  
  
Represents a 3D plane. GH_Plane re-implements the OpenNURBS OnPlane class.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.Kernel.TypesGH_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)Plane  
[Grasshopper.Kernel.TypesGH_GeometricGoo](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm)Plane  
Grasshopper.Kernel.TypesGH_Plane  

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Plane : GH_GeometricGoo<Plane>, 
    	IGH_BakeAwareData, IGH_PreviewData
    
    
    Public Class GH_Plane
    	Inherits GH_GeometricGoo(Of Plane)
    	Implements IGH_BakeAwareData, IGH_PreviewData

The GH_Plane type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_Plane](M_Grasshopper_Kernel_Types_GH_Plane__ctor.htm)|  Default
constructor. Creates a world XY plane.  
![Public method](../icons/pubmethod.gif)|
[GH_Plane(GH_Plane)](M_Grasshopper_Kernel_Types_GH_Plane__ctor_1.htm)|  Create
a duplicate of another plane.  
![Public method](../icons/pubmethod.gif)|
[GH_Plane(Guid)](M_Grasshopper_Kernel_Types_GH_Plane__ctor_3.htm)| Initializes
a new instance of the GH_Plane class  
![Public method](../icons/pubmethod.gif)|
[GH_Plane(Plane)](M_Grasshopper_Kernel_Types_GH_Plane__ctor_2.htm)|  Create a
duplicate of another plane.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Boundingbox](P_Grasshopper_Kernel_Types_GH_Plane_Boundingbox.htm)|
(Overrides
[GH_GeometricGooTBoundingbox](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Boundingbox.htm).)  
![Public property](../icons/pubproperty.gif)|
[ClippingBox](P_Grasshopper_Kernel_Types_GH_Plane_ClippingBox.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_Plane_IsGeometryLoaded.htm)|
Gets the load state of this plane. The plane is considered to be loaded when
it is valid.  (Overrides
[GH_GeometricGooTIsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsGeometryLoaded.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsReferencedGeometry](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsReferencedGeometry.htm)|
Gets a value indicating whether or not this geometry is referenced. Not all
IGH_GeometricGoo implementations support referenced geometry.  (Inherited from
[GH_GeometricGooT](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Kernel_Types_GH_Plane_IsValid.htm)|  Gets the validity
of the plane. If the plane is invalid, attempts are made to fix the data. If
the plane remains invalid, False is returned.  (Overrides
[GH_GeometricGooTIsValid](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsValid.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Plane_IsValidWhyNot.htm)|  Gets
a string describing the state of "invalidness". If the instance _is_ valid,
then this property should return Nothing or String.Empty.  (Overrides
[GH_GooTIsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm).)  
![Public property](../icons/pubproperty.gif)|
[ReferenceID](P_Grasshopper_Kernel_Types_GH_Plane_ReferenceID.htm)|
(Overrides
[GH_GeometricGooTReferenceID](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ReferenceID.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeDescription](P_Grasshopper_Kernel_Types_GH_Plane_TypeDescription.htm)|
(Overrides
[GH_GooTTypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_Types_GH_Plane_TypeName.htm)|  (Overrides
[GH_GooTTypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).)  
![Public property](../icons/pubproperty.gif)|
[Value](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Value.htm)|  Gets or sets
the value of this type. Note that if the type has a ReferenceID this value
might get destroyed in the future.  (Inherited from
[GH_GeometricGooT](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[BakeGeometry](M_Grasshopper_Kernel_Types_GH_Plane_BakeGeometry.htm)|  
![Public method](../icons/pubmethod.gif)|
[CastFrom](M_Grasshopper_Kernel_Types_GH_Plane_CastFrom.htm)|  Remote to Local
caster function. This stuff is complex, don't concern yourself with casting
logic.  (Overrides
[GH_GeometricGooTCastFrom(Object)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastFrom.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToQ(Q)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo__1.htm)|
Attempt a cast to type T.  (Inherited from
[GH_GeometricGooT](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToQ(Q)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm)|  Attempt a
cast to type Q.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Kernel_Types_GH_Plane_CastTo__1.htm)|  Local to
Remote caster function. This stuff is complex, don't concern yourself with
casting logic.  (Overrides
[GH_GeometricGooTCastToQ(Q)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo__1.htm).)  
![Public method](../icons/pubmethod.gif)|
[ClearCaches](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ClearCaches.htm)|
Clears all caches. Typically if the geometry is referenced, this will erase
the local copy. If your T is a value-type, you must override this function and
specifically unset the local value.  (Inherited from
[GH_GeometricGooT](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).)  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[DrawPlane(DisplayPipeline,
Plane)](M_Grasshopper_Kernel_Types_GH_Plane_DrawPlane.htm)|  Draw a plane with
default colours and default size.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[DrawPlane(DisplayPipeline, Plane, Double,
Int32)](M_Grasshopper_Kernel_Types_GH_Plane_DrawPlane_1.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[DrawPlane(DisplayPipeline, Plane, Double, Int32, Color, Color,
Color)](M_Grasshopper_Kernel_Types_GH_Plane_DrawPlane_2.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[DrawPlane(DisplayPipeline, Plane, Double, Int32, Color, Color, Color,
Color)](M_Grasshopper_Kernel_Types_GH_Plane_DrawPlane_3.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[DrawPlaneIcon](M_Grasshopper_Kernel_Types_GH_Plane_DrawPlaneIcon.htm)|  
![Public method](../icons/pubmethod.gif)|
[DrawViewportMeshes](M_Grasshopper_Kernel_Types_GH_Plane_DrawViewportMeshes.htm)|  
![Public method](../icons/pubmethod.gif)|
[DrawViewportWires](M_Grasshopper_Kernel_Types_GH_Plane_DrawViewportWires.htm)|  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Kernel_Types_GH_Plane_Duplicate.htm)|  (Overrides
[GH_GeometricGooTDuplicate](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Duplicate.htm).)  
![Public method](../icons/pubmethod.gif)|
[DuplicateGeometry](M_Grasshopper_Kernel_Types_GH_Plane_DuplicateGeometry.htm)|
Create a duplicate of this plane.  (Overrides
[GH_GeometricGooTDuplicateGeometry](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_DuplicateGeometry.htm).)  
![Public method](../icons/pubmethod.gif)|
[DuplicatePlane](M_Grasshopper_Kernel_Types_GH_Plane_DuplicatePlane.htm)|
Create a duplicate of this plane.  
![Public method](../icons/pubmethod.gif)|
[EmitProxy](M_Grasshopper_Kernel_Types_GH_Plane_EmitProxy.htm)|  Returns a
proxy that represents this plane. Do not call this function unless you're
(Overrides
[GH_GeometricGooTEmitProxy](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_EmitProxy.htm).)  
![Public method](../icons/pubmethod.gif)|
[GetBoundingBox](M_Grasshopper_Kernel_Types_GH_Plane_GetBoundingBox.htm)|
(Overrides
[GH_GeometricGooTGetBoundingBox(Transform)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_GetBoundingBox.htm).)  
![Public method](../icons/pubmethod.gif)|
[LoadGeometry](M_Grasshopper_Kernel_Types_GH_Plane_LoadGeometry.htm)|  If the
geometry is referenced and not yet loaded, attempts to load the geometry.
(Overrides
[GH_GeometricGooTLoadGeometry](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry.htm).)  
![Public method](../icons/pubmethod.gif)|
[LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_Plane_LoadGeometry_1.htm)|
(Overrides
[GH_GeometricGooTLoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[Morph](M_Grasshopper_Kernel_Types_GH_Plane_Morph.htm)|  (Overrides
[GH_GeometricGooTMorph(SpaceMorph)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Morph.htm).)  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_Types_GH_Plane_Read.htm)|  (Overrides
[GH_GooTRead(GH_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).)  
![Public method](../icons/pubmethod.gif)|
[ScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm)|
This function will be called when the local IGH_Goo instance disappears into a
user Script. This would be an excellent place to cast your IGH_Goo type to a
simple data type.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Types_GH_Plane_ToString.htm)|  Format the
plane using default grasshopper formatting logic.  (Overrides
[GH_GooTToString](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).)  
![Public method](../icons/pubmethod.gif)|
[Transform](M_Grasshopper_Kernel_Types_GH_Plane_Transform.htm)|  (Overrides
[GH_GeometricGooTTransform(Transform)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Transform.htm).)  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_Types_GH_Plane_Write.htm)|  (Overrides
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

