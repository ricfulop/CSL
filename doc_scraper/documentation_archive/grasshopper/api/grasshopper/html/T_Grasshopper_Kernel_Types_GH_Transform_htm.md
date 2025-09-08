---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_GH_Transform.htm
scraped_at: 2025-09-08T16:21:39.673964
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[GH_Transform Class](../html/T_Grasshopper_Kernel_Types_GH_Transform.htm
"GH_Transform Class")

[GH_Transform Constructor
](../html/Overload_Grasshopper_Kernel_Types_GH_Transform__ctor.htm
"GH_Transform Constructor ")

[GH_Transform
Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Transform.htm
"GH_Transform Properties")

[GH_Transform
Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Transform.htm
"GH_Transform Methods")

[GH_Transform
Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_Transform.htm
"GH_Transform Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Transform Class  
  
---  
  
Represents a collection of transformations.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.Kernel.TypesGH_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)Transform  
Grasshopper.Kernel.TypesGH_Transform  

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Transform : GH_Goo<Transform>
    
    
    Public Class GH_Transform
    	Inherits GH_Goo(Of Transform)

The GH_Transform type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_Transform](M_Grasshopper_Kernel_Types_GH_Transform__ctor.htm)| Initializes
a new instance of the GH_Transform class  
![Public method](../icons/pubmethod.gif)|
[GH_Transform(GH_Transform)](M_Grasshopper_Kernel_Types_GH_Transform__ctor_1.htm)|
Initializes a new instance of the GH_Transform class  
![Public method](../icons/pubmethod.gif)|
[GH_Transform(ITransform)](M_Grasshopper_Kernel_Types_GH_Transform__ctor_2.htm)|
Initializes a new instance of the GH_Transform class  
![Public method](../icons/pubmethod.gif)|
[GH_Transform(Transform)](M_Grasshopper_Kernel_Types_GH_Transform__ctor_3.htm)|
Initializes a new instance of the GH_Transform class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[CompoundTransforms](P_Grasshopper_Kernel_Types_GH_Transform_CompoundTransforms.htm)|
Gets the internal set of transforms. If you modify the compound
transformations, you _must_ call ClearCaches().  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Kernel_Types_GH_Transform_IsValid.htm)|  (Overrides
[GH_GooTIsValid](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValid.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Transform_IsValidWhyNot.htm)|
Gets a string describing the state of "invalidness". If the instance _is_
valid, then this property should return Nothing or String.Empty.  (Overrides
[GH_GooTIsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeDescription](P_Grasshopper_Kernel_Types_GH_Transform_TypeDescription.htm)|
(Overrides
[GH_GooTTypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_Types_GH_Transform_TypeName.htm)|  (Overrides
[GH_GooTTypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).)  
![Public property](../icons/pubproperty.gif)|
[Value](P_Grasshopper_Kernel_Types_GH_Transform_Value.htm)|  (Overrides
[GH_GooTValue](P_Grasshopper_Kernel_Types_GH_Goo_1_Value.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CastFrom](M_Grasshopper_Kernel_Types_GH_Transform_CastFrom.htm)|  (Overrides
[GH_GooTCastFrom(Object)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastFrom.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToQ(Q)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm)|  Attempt a
cast to type Q.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToQ(Q)](M_Grasshopper_Kernel_Types_GH_Transform_CastTo__1.htm)|
(Overrides
[GH_GooTCastToQ(Q)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm).)  
![Public method](../icons/pubmethod.gif)|
[ClearCaches](M_Grasshopper_Kernel_Types_GH_Transform_ClearCaches.htm)|  Erase
the compound transformation caches.  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Kernel_Types_GH_Transform_Duplicate.htm)|
(Overrides
[GH_GooTDuplicate](M_Grasshopper_Kernel_Types_GH_Goo_1_Duplicate.htm).)  
![Public method](../icons/pubmethod.gif)|
[EmitProxy](M_Grasshopper_Kernel_Types_GH_Transform_EmitProxy.htm)|  Returns a
proxy that represents this transform. Do not call this function unless you're
(Overrides
[GH_GooTEmitProxy](M_Grasshopper_Kernel_Types_GH_Goo_1_EmitProxy.htm).)  
![Public method](../icons/pubmethod.gif)|
[GetInverse](M_Grasshopper_Kernel_Types_GH_Transform_GetInverse.htm)|  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_Types_GH_Transform_Read.htm)|  (Overrides
[GH_GooTRead(GH_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).)  
![Public method](../icons/pubmethod.gif)|
[ScriptVariable](M_Grasshopper_Kernel_Types_GH_Transform_ScriptVariable.htm)|
(Overrides
[GH_GooTScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Types_GH_Transform_ToString.htm)|  (Overrides
[GH_GooTToString](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).)  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_Types_GH_Transform_Write.htm)|  (Overrides
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

