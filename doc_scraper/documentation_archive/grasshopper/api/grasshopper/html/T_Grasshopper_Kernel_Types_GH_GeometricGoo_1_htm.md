---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm
scraped_at: 2025-09-08T16:20:39.404402
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[GH_GeometricGoo(T)
Class](../html/T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm
"GH_GeometricGoo\(T\) Class")

[GH_GeometricGoo(T) Constructor
](../html/Overload_Grasshopper_Kernel_Types_GH_GeometricGoo_1__ctor.htm
"GH_GeometricGoo\(T\) Constructor ")

[GH_GeometricGoo(T)
Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm
"GH_GeometricGoo\(T\) Properties")

[GH_GeometricGoo(T)
Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm
"GH_GeometricGoo\(T\) Methods")

[GH_GeometricGoo(T)
Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm
"GH_GeometricGoo\(T\) Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_GeometricGooT Class  
  
---  
  
Abstract base implementation of IGH_GeometricGoo. If you implement
IGH_GeometricGoo, use this for a booster.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.Kernel.TypesGH_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)T  
Grasshopper.Kernel.TypesGH_GeometricGooT  
More...

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public abstract class GH_GeometricGoo<T> : GH_Goo<T>, 
    	IGH_GeometricGoo
    
    
    
    Public MustInherit Class GH_GeometricGoo(Of T)
    	Inherits GH_Goo(Of T)
    	Implements IGH_GeometricGoo

#### Type Parameters

T

    

The GH_GeometricGooT type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[GH_GeometricGooT](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1__ctor.htm)|
Blank constructor, m_value will be set to default (null for reference types,
zeroes for value types)  
![Protected method](../icons/protmethod.gif)|
[GH_GeometricGooT(T)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1__ctor_1.htm)|
Data constructor, m_value will be set to internal_data.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Boundingbox](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Boundingbox.htm)|
Gets the boundingbox for this geometry.  
![Public property](../icons/pubproperty.gif)|
[IsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsGeometryLoaded.htm)|
Gets a value indicating whether or not this geometry is currently loaded
(assuming it is referenced). Not all IGH_GeometricGoo implementations support
referenced geometry. The default is to always return True.  
![Public property](../icons/pubproperty.gif)|
[IsReferencedGeometry](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsReferencedGeometry.htm)|
Gets a value indicating whether or not this geometry is referenced. Not all
IGH_GeometricGoo implementations support referenced geometry.  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsValid.htm)|  Gets a
value indicating whether or not the current value is valid.  (Overrides
[GH_GooTIsValid](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValid.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm)|  Gets
a string describing the state of "invalidness". If the instance _is_ valid,
then this property should return Nothing or String.Empty.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[ReferenceID](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ReferenceID.htm)|
Gets or sets the Guid of the object that is referenced. Not all
IGH_GeometricGoo implementations support referenced geometry. The default
implementation is to always return Guid.Empty.  
![Public property](../icons/pubproperty.gif)|
[TypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm)|
Gets a description of the type of the implementation.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm)|  Gets the name
of the type of the implementation.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[Value](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Value.htm)|  Gets or sets
the value of this type. Note that if the type has a ReferenceID this value
might get destroyed in the future.  (Overrides
[GH_GooTValue](P_Grasshopper_Kernel_Types_GH_Goo_1_Value.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CastFrom](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastFrom.htm)|
Attempt a cast from generic object.  (Overrides
[GH_GooTCastFrom(Object)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastFrom.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToQ(Q)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo__1.htm)|
Attempt a cast to type T.  (Overrides
[GH_GooTCastToQ(Q)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToQ(Q)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm)|  Attempt a
cast to type Q.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[ClearCaches](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ClearCaches.htm)|
Clears all caches. Typically if the geometry is referenced, this will erase
the local copy. If your T is a value-type, you must override this function and
specifically unset the local value.  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Duplicate.htm)|  Make
a complete duplicate of this instance. No shallow copies.  (Overrides
[GH_GooTDuplicate](M_Grasshopper_Kernel_Types_GH_Goo_1_Duplicate.htm).)  
![Public method](../icons/pubmethod.gif)|
[DuplicateGeometry](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_DuplicateGeometry.htm)|
Make a complete duplicate of this geometry. No shallow copies.  
![Public method](../icons/pubmethod.gif)|
[EmitProxy](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_EmitProxy.htm)|
Create a new proxy for this instance. Return Null if this class does not
support proxies.  (Overrides
[GH_GooTEmitProxy](M_Grasshopper_Kernel_Types_GH_Goo_1_EmitProxy.htm).)  
![Public method](../icons/pubmethod.gif)|
[GetBoundingBox](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_GetBoundingBox.htm)|
Compute an aligned boundingbox.  
![Public method](../icons/pubmethod.gif)|
[LoadGeometry](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry.htm)|
If the geometry is referenced and currently unloaded, forces loading of the
geometry. Not all IGH_GeometricGoo implementations support referenced
geometry.  
![Public method](../icons/pubmethod.gif)|
[LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry_1.htm)|
If the geometry is referenced and currently unloaded, forces loading of the
geometry. Not all IGH_GeometricGoo implementations support referenced
geometry. The default is to always return True.  
![Public method](../icons/pubmethod.gif)|
[Morph](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Morph.htm)|  Morph the
object or a deformable representation of the object.  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm)|  Default behaviour is to
return True.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[ScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm)|
This function will be called when the local IGH_Goo instance disappears into a
user Script. This would be an excellent place to cast your IGH_Goo type to a
simple data type.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm)|  Creates a
string description of the current instance value.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[Transform](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Transform.htm)|
Transforms the object or a deformable representation of the object.  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm)|  Default behaviour is
to return True.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
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

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.Kernel.TypesGH_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)T  
Grasshopper.Kernel.TypesGH_GeometricGooT  
[Grasshopper.Kernel.TypesGH_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm)  
[Grasshopper.Kernel.TypesGH_Arc](T_Grasshopper_Kernel_Types_GH_Arc.htm)  
[Grasshopper.Kernel.TypesGH_Box](T_Grasshopper_Kernel_Types_GH_Box.htm)  
[Grasshopper.Kernel.TypesGH_Brep](T_Grasshopper_Kernel_Types_GH_Brep.htm)  
[Grasshopper.Kernel.TypesGH_Circle](T_Grasshopper_Kernel_Types_GH_Circle.htm)  
[Grasshopper.Kernel.TypesGH_Curve](T_Grasshopper_Kernel_Types_GH_Curve.htm)  
[Grasshopper.Kernel.TypesGH_DetailView](T_Grasshopper_Kernel_Types_GH_DetailView.htm)  
[Grasshopper.Kernel.TypesGH_Extrusion](T_Grasshopper_Kernel_Types_GH_Extrusion.htm)  
[Grasshopper.Kernel.TypesGH_Hatch](T_Grasshopper_Kernel_Types_GH_Hatch.htm)  
[Grasshopper.Kernel.TypesGH_InstanceReference](T_Grasshopper_Kernel_Types_GH_InstanceReference.htm)  
[Grasshopper.Kernel.TypesGH_Light](T_Grasshopper_Kernel_Types_GH_Light.htm)  
[Grasshopper.Kernel.TypesGH_Line](T_Grasshopper_Kernel_Types_GH_Line.htm)  
[Grasshopper.Kernel.TypesGH_Mesh](T_Grasshopper_Kernel_Types_GH_Mesh.htm)  
[Grasshopper.Kernel.TypesGH_Plane](T_Grasshopper_Kernel_Types_GH_Plane.htm)  
[Grasshopper.Kernel.TypesGH_PointCloud](T_Grasshopper_Kernel_Types_GH_PointCloud.htm)  
[Grasshopper.Kernel.TypesGH_Rectangle](T_Grasshopper_Kernel_Types_GH_Rectangle.htm)  
[Grasshopper.Kernel.TypesGH_SubD](T_Grasshopper_Kernel_Types_GH_SubD.htm)  
[Grasshopper.Kernel.TypesGH_Surface](T_Grasshopper_Kernel_Types_GH_Surface.htm)  
[Grasshopper.Kernel.TypesGH_TextDot](T_Grasshopper_Kernel_Types_GH_TextDot.htm)  

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

