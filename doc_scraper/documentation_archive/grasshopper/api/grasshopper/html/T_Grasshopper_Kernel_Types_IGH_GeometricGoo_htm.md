---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_IGH_GeometricGoo.htm
scraped_at: 2025-09-08T16:21:44.677350
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[IGH_GeometricGoo
Interface](../html/T_Grasshopper_Kernel_Types_IGH_GeometricGoo.htm
"IGH_GeometricGoo Interface")

[IGH_GeometricGoo
Properties](../html/Properties_T_Grasshopper_Kernel_Types_IGH_GeometricGoo.htm
"IGH_GeometricGoo Properties")

[IGH_GeometricGoo
Methods](../html/Methods_T_Grasshopper_Kernel_Types_IGH_GeometricGoo.htm
"IGH_GeometricGoo Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_GeometricGoo Interface  
  
---  
  
Base interface for all Data inside Grasshoper that could pass for Geometry

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_GeometricGoo : IGH_Goo
    
    
    Public Interface IGH_GeometricGoo
    	Inherits IGH_Goo

The IGH_GeometricGoo type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Boundingbox](P_Grasshopper_Kernel_Types_IGH_GeometricGoo_Boundingbox.htm)|
Gets the (cached) boundingbox for this geometry. Not all geometry types cache
boundingbox results.  
![Public property](../icons/pubproperty.gif)|
[IsGeometryLoaded](P_Grasshopper_Kernel_Types_IGH_GeometricGoo_IsGeometryLoaded.htm)|
Gets a value indicating whether or not this geometry is currently loaded
(assuming it is referenced). Not all IGH_GeometricGoo implementations support
referenced geometry.  
![Public property](../icons/pubproperty.gif)|
[IsReferencedGeometry](P_Grasshopper_Kernel_Types_IGH_GeometricGoo_IsReferencedGeometry.htm)|
Gets a value indicating whether or not this geometry is referenced. Not all
IGH_GeometricGoo implementations support referenced geometry.  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Kernel_Types_IGH_Goo_IsValid.htm)|  Gets a value
indicating whether or not the current value is valid.  (Inherited from
[IGH_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Kernel_Types_IGH_Goo_IsValidWhyNot.htm)|  Gets a
string describing the state of "invalidness". If the instance _is_ valid, then
this property should return Nothing or String.Empty.  (Inherited from
[IGH_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).)  
![Public property](../icons/pubproperty.gif)|
[ReferenceID](P_Grasshopper_Kernel_Types_IGH_GeometricGoo_ReferenceID.htm)|
Gets or sets the Guid of the object that is referenced. Not all
IGH_GeometricGoo implementations support referenced geometry.  
![Public property](../icons/pubproperty.gif)|
[TypeDescription](P_Grasshopper_Kernel_Types_IGH_Goo_TypeDescription.htm)|
Gets a description of the type of the implementation.  (Inherited from
[IGH_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_Types_IGH_Goo_TypeName.htm)|  Gets the name of
the type of the implementation.  (Inherited from
[IGH_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CastFrom](M_Grasshopper_Kernel_Types_IGH_Goo_CastFrom.htm)|  Attempt a cast
from generic object  (Inherited from
[IGH_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT](M_Grasshopper_Kernel_Types_IGH_Goo_CastTo__1.htm)|  Attempt a cast
to type T  (Inherited from [IGH_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).)  
![Public method](../icons/pubmethod.gif)|
[ClearCaches](M_Grasshopper_Kernel_Types_IGH_GeometricGoo_ClearCaches.htm)|
Clears all caches. Typically if the geometry is referenced, this will erase
the local copy.  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Kernel_Types_IGH_Goo_Duplicate.htm)|  Make a
complete duplicate of this instance. No shallow copies.  (Inherited from
[IGH_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).)  
![Public method](../icons/pubmethod.gif)|
[DuplicateGeometry](M_Grasshopper_Kernel_Types_IGH_GeometricGoo_DuplicateGeometry.htm)|
Make a complete duplicate of this geometry. No shallow copies.  
![Public method](../icons/pubmethod.gif)|
[EmitProxy](M_Grasshopper_Kernel_Types_IGH_Goo_EmitProxy.htm)|  Create a new
proxy for this instance. Return Null if this class does not support proxies.
(Inherited from [IGH_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).)  
![Public method](../icons/pubmethod.gif)|
[GetBoundingBox](M_Grasshopper_Kernel_Types_IGH_GeometricGoo_GetBoundingBox.htm)|
Compute an aligned boundingbox.  
![Public method](../icons/pubmethod.gif)|
[LoadGeometry](M_Grasshopper_Kernel_Types_IGH_GeometricGoo_LoadGeometry.htm)|
If the geometry is referenced and currently unloaded, forces loading of the
geometry. Not all IGH_GeometricGoo implementations support referenced
geometry.  
![Public method](../icons/pubmethod.gif)|
[LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_IGH_GeometricGoo_LoadGeometry_1.htm)|
If the geometry is referenced and currently unloaded, forces loading of the
geometry. Not all IGH_GeometricGoo implementations support referenced
geometry.  
![Public method](../icons/pubmethod.gif)|
[Morph](M_Grasshopper_Kernel_Types_IGH_GeometricGoo_Morph.htm)|  Morph the
object or a deformable representation of the object.  
![Public method](../icons/pubmethod.gif)|
[ScriptVariable](M_Grasshopper_Kernel_Types_IGH_Goo_ScriptVariable.htm)|  This
function will be called when the local IGH_Goo instance disapears into a user
Script. This would be an excellent place to cast your IGH_Goo type to a simple
data type.  (Inherited from
[IGH_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Types_IGH_Goo_ToString.htm)|  Creates a string
description of the current instance value  (Inherited from
[IGH_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).)  
![Public method](../icons/pubmethod.gif)|
[Transform](M_Grasshopper_Kernel_Types_IGH_GeometricGoo_Transform.htm)|
Transforms the object or a deformable representation of the object.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

