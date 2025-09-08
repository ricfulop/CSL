---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_GH_RadialDimension.htm
scraped_at: 2025-09-08T16:21:25.601621
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[GH_RadialDimension
Class](../html/T_Grasshopper_Kernel_Types_GH_RadialDimension.htm
"GH_RadialDimension Class")

[GH_RadialDimension Constructor
](../html/Overload_Grasshopper_Kernel_Types_GH_RadialDimension__ctor.htm
"GH_RadialDimension Constructor ")

[GH_RadialDimension
Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_RadialDimension.htm
"GH_RadialDimension Properties")

[GH_RadialDimension
Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_RadialDimension.htm
"GH_RadialDimension Methods")

[GH_RadialDimension
Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_RadialDimension.htm
"GH_RadialDimension Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_RadialDimension Class  
  
---  
  
Represents an implementation of a Rhino radial dimension.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.Kernel.TypesGH_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)AnnotationBase  
[Grasshopper.Kernel.TypesGH_GeometricGoo](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm)AnnotationBase  
[Grasshopper.Kernel.TypesGH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm)  
[Grasshopper.Kernel.TypesGH_Dimension](T_Grasshopper_Kernel_Types_GH_Dimension.htm)  
Grasshopper.Kernel.TypesGH_RadialDimension  

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_RadialDimension : GH_Dimension
    
    
    Public Class GH_RadialDimension
    	Inherits GH_Dimension

The GH_RadialDimension type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_RadialDimension](M_Grasshopper_Kernel_Types_GH_RadialDimension__ctor.htm)|
Default constructor, creates an invalid radial dimension.  
![Public method](../icons/pubmethod.gif)|
[GH_RadialDimension(GH_RadialDimension)](M_Grasshopper_Kernel_Types_GH_RadialDimension__ctor_1.htm)|
Create a duplicate of another GH_RadialDimension. This constructor also copies
reference data.  
![Public method](../icons/pubmethod.gif)|
[GH_RadialDimension(Guid)](M_Grasshopper_Kernel_Types_GH_RadialDimension__ctor_4.htm)|
Create a new referenced radial dimension that references a Rhino dimension
with the specified ID.  
![Public method](../icons/pubmethod.gif)|
[GH_RadialDimension(RadialDimension)](M_Grasshopper_Kernel_Types_GH_RadialDimension__ctor_2.htm)|
Create a duplicate of an existing radial dimension.  
![Public method](../icons/pubmethod.gif)| [GH_RadialDimension(RadialDimension,
ModelAnnotationStyle)](M_Grasshopper_Kernel_Types_GH_RadialDimension__ctor_3.htm)|
Create a duplicate of an existing radial dimension.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Boundingbox](P_Grasshopper_Kernel_Types_GH_AnnotationBase_Boundingbox.htm)|
(Inherited from
[GH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).)  
![Public property](../icons/pubproperty.gif)|
[ClippingBox](P_Grasshopper_Kernel_Types_GH_AnnotationBase_ClippingBox.htm)|
(Inherited from
[GH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_AnnotationBase_IsGeometryLoaded.htm)|
Gets the load state of this annotation object. The annotation is considered to
be loaded when the local annotation instance is not null.  (Inherited from
[GH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsReferencedGeometry](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsReferencedGeometry.htm)|
Gets a value indicating whether or not this geometry is referenced. Not all
IGH_GeometricGoo implementations support referenced geometry.  (Inherited from
[GH_GeometricGooT](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Kernel_Types_GH_AnnotationBase_IsValid.htm)|  Gets the
validity of this dimension. If the dimension is referenced but cannot be
loaded, then the dimension is not valid.  (Inherited from
[GH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_AnnotationBase_IsValidWhyNot.htm)|
Gets a string describing the state of "invalidness". If the instance _is_
valid, then this property should return Nothing or String.Empty.  (Inherited
from [GH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).)  
![Public property](../icons/pubproperty.gif)|
[ReferenceID](P_Grasshopper_Kernel_Types_GH_AnnotationBase_ReferenceID.htm)|
(Inherited from
[GH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).)  
![Public property](../icons/pubproperty.gif)|
[Style](P_Grasshopper_Kernel_Types_GH_AnnotationBase_Style.htm)|  (Inherited
from [GH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeDescription](P_Grasshopper_Kernel_Types_GH_RadialDimension_TypeDescription.htm)|
(Overrides
[GH_AnnotationBaseTypeDescription](P_Grasshopper_Kernel_Types_GH_AnnotationBase_TypeDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_Types_GH_RadialDimension_TypeName.htm)|
(Overrides
[GH_AnnotationBaseTypeName](P_Grasshopper_Kernel_Types_GH_AnnotationBase_TypeName.htm).)  
![Public property](../icons/pubproperty.gif)|
[Value](P_Grasshopper_Kernel_Types_GH_RadialDimension_Value.htm)|  
![Protected property](../icons/protproperty.gif)|
[ValueType](P_Grasshopper_Kernel_Types_GH_RadialDimension_ValueType.htm)|
(Overrides
[GH_DimensionValueType](P_Grasshopper_Kernel_Types_GH_Dimension_ValueType.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[BakeGeometry](M_Grasshopper_Kernel_Types_GH_AnnotationBase_BakeGeometry.htm)|
(Inherited from
[GH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastFrom](M_Grasshopper_Kernel_Types_GH_RadialDimension_CastFrom.htm)|
Remote to Local caster function. This stuff is complex, don't concern yourself
with casting logic.  (Overrides
[GH_GeometricGooTCastFrom(Object)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastFrom.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Kernel_Types_GH_AnnotationBase_CastTo__1.htm)|
Local to Remote caster function. This stuff is complex, don't concern yourself
with casting logic.  (Inherited from
[GH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Kernel_Types_GH_Dimension_CastTo__1.htm)|  Local to
Remote caster function. This stuff is complex, don't concern yourself with
casting logic.  (Inherited from
[GH_Dimension](T_Grasshopper_Kernel_Types_GH_Dimension.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToQ(Q)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo__1.htm)|
Attempt a cast to type T.  (Inherited from
[GH_GeometricGooT](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToQ(Q)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm)|  Attempt a
cast to type Q.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Kernel_Types_GH_RadialDimension_CastTo__1.htm)|
Local to Remote caster function. This stuff is complex, don't concern yourself
with casting logic.  (Overrides
[GH_DimensionCastToT(T)](M_Grasshopper_Kernel_Types_GH_Dimension_CastTo__1.htm).)  
![Public method](../icons/pubmethod.gif)|
[ClearCaches](M_Grasshopper_Kernel_Types_GH_AnnotationBase_ClearCaches.htm)|
Clears all volatile caches for this instance. The boundingbox is cleared, and
if the annotation is referenced, the local instance of the annotation is
erased.  (Inherited from
[GH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).)  
![Public method](../icons/pubmethod.gif)|
[DrawViewportMeshes](M_Grasshopper_Kernel_Types_GH_AnnotationBase_DrawViewportMeshes.htm)|
(Inherited from
[GH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).)  
![Public method](../icons/pubmethod.gif)|
[DrawViewportWires](M_Grasshopper_Kernel_Types_GH_AnnotationBase_DrawViewportWires.htm)|
(Inherited from
[GH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).)  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Kernel_Types_GH_AnnotationBase_Duplicate.htm)|
(Inherited from
[GH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).)  
![Public method](../icons/pubmethod.gif)|
[DuplicateAnnotation](M_Grasshopper_Kernel_Types_GH_RadialDimension_DuplicateAnnotation.htm)|
Create a duplicate of this annotation.  (Overrides
[GH_AnnotationBaseDuplicateAnnotation](M_Grasshopper_Kernel_Types_GH_AnnotationBase_DuplicateAnnotation.htm).)  
![Public method](../icons/pubmethod.gif)|
[DuplicateGeometry](M_Grasshopper_Kernel_Types_GH_AnnotationBase_DuplicateGeometry.htm)|
Create a duplicate of this annotation.  (Inherited from
[GH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).)  
![Public method](../icons/pubmethod.gif)|
[DuplicateRadialDimension](M_Grasshopper_Kernel_Types_GH_RadialDimension_DuplicateRadialDimension.htm)|
Create a duplicate of this radial dimension.  
![Public method](../icons/pubmethod.gif)|
[EmitProxy](M_Grasshopper_Kernel_Types_GH_Dimension_EmitProxy.htm)|
(Inherited from [GH_Dimension](T_Grasshopper_Kernel_Types_GH_Dimension.htm).)  
![Public method](../icons/pubmethod.gif)|
[GetBoundingBox](M_Grasshopper_Kernel_Types_GH_AnnotationBase_GetBoundingBox.htm)|
(Inherited from
[GH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).)  
![Public method](../icons/pubmethod.gif)|
[GetOverrides](M_Grasshopper_Kernel_Types_GH_AnnotationBase_GetOverrides.htm)|
(Inherited from
[GH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).)  
![Public method](../icons/pubmethod.gif)|
[LoadGeometry](M_Grasshopper_Kernel_Types_GH_AnnotationBase_LoadGeometry.htm)|
If the geometry is referenced and not yet loaded, attempts to load the
geometry.  (Inherited from
[GH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).)  
![Public method](../icons/pubmethod.gif)|
[LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_AnnotationBase_LoadGeometry_1.htm)|
If the annotation is referenced and not yet loaded, attempts to load the
leader.  (Inherited from
[GH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).)  
![Public method](../icons/pubmethod.gif)|
[Morph](M_Grasshopper_Kernel_Types_GH_AnnotationBase_Morph.htm)|  (Inherited
from [GH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).)  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_Types_GH_AnnotationBase_Read.htm)|  (Inherited
from [GH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).)  
![Public method](../icons/pubmethod.gif)|
[ScriptVariable](M_Grasshopper_Kernel_Types_GH_AnnotationBase_ScriptVariable.htm)|
(Inherited from
[GH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).)  
![Public method](../icons/pubmethod.gif)|
[SetOverrides](M_Grasshopper_Kernel_Types_GH_AnnotationBase_SetOverrides.htm)|
(Inherited from
[GH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Types_GH_RadialDimension_ToString.htm)|
Format the dimension using default grasshopper formatting logic.  (Overrides
[GH_AnnotationBaseToString](M_Grasshopper_Kernel_Types_GH_AnnotationBase_ToString.htm).)  
![Public method](../icons/pubmethod.gif)|
[Transform](M_Grasshopper_Kernel_Types_GH_AnnotationBase_Transform.htm)|
(Inherited from
[GH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).)  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_Types_GH_AnnotationBase_Write.htm)|  (Inherited
from [GH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).)  
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

