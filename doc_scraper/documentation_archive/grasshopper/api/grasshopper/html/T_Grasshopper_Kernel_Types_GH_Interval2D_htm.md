---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_GH_Interval2D.htm
scraped_at: 2025-09-08T16:20:52.441351
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[GH_Interval2D Class](../html/T_Grasshopper_Kernel_Types_GH_Interval2D.htm
"GH_Interval2D Class")

[GH_Interval2D Constructor
](../html/Overload_Grasshopper_Kernel_Types_GH_Interval2D__ctor.htm
"GH_Interval2D Constructor ")

[GH_Interval2D
Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Interval2D.htm
"GH_Interval2D Properties")

[GH_Interval2D
Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Interval2D.htm
"GH_Interval2D Methods")

[GH_Interval2D
Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_Interval2D.htm
"GH_Interval2D Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Interval2D Class  
  
---  
  
Represents a two-dimensional numeric domain.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.Kernel.TypesGH_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)[UVInterval](T_Grasshopper_Kernel_Types_UVInterval.htm)  
Grasshopper.Kernel.TypesGH_Interval2D  

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Interval2D : GH_Goo<UVInterval>
    
    
    Public Class GH_Interval2D
    	Inherits GH_Goo(Of UVInterval)

The GH_Interval2D type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_Interval2D](M_Grasshopper_Kernel_Types_GH_Interval2D__ctor.htm)|  Default
constructor. Creates two empty intervals.  
![Public method](../icons/pubmethod.gif)|
[GH_Interval2D(GH_Interval2D)](M_Grasshopper_Kernel_Types_GH_Interval2D__ctor_1.htm)|
Create a duplicate of another two-dimensional interval  
![Public method](../icons/pubmethod.gif)|
[GH_Interval2D(UVInterval)](M_Grasshopper_Kernel_Types_GH_Interval2D__ctor_2.htm)|
Duplicates a one-dimensional interval in both directions.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Kernel_Types_GH_Interval2D_IsValid.htm)|  Gets the
validity of this instance. Valid intervals contain no #NaN extremes
(Overrides [GH_GooTIsValid](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValid.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Interval2D_IsValidWhyNot.htm)|
Gets a string describing the state of "invalidness". If the instance _is_
valid, then this property should return Nothing or String.Empty.  (Overrides
[GH_GooTIsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeDescription](P_Grasshopper_Kernel_Types_GH_Interval2D_TypeDescription.htm)|
(Overrides
[GH_GooTTypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_Types_GH_Interval2D_TypeName.htm)|  (Overrides
[GH_GooTTypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).)  
![Public property](../icons/pubproperty.gif)|
[Value](P_Grasshopper_Kernel_Types_GH_Goo_1_Value.htm)|  Gets or sets the
internal data.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CastFrom](M_Grasshopper_Kernel_Types_GH_Interval2D_CastFrom.htm)|  Remote to
Local caster function. This stuff is complex, don't concern yourself with
casting logic.  (Overrides
[GH_GooTCastFrom(Object)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastFrom.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToQ(Q)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm)|  Attempt a
cast to type Q.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Kernel_Types_GH_Interval2D_CastTo__1.htm)|  Local
to Remote caster function. this stuff is complex, don't concern yourself with
casting logic.  (Overrides
[GH_GooTCastToQ(Q)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm).)  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Kernel_Types_GH_Interval2D_Duplicate.htm)|  Create a
duplicate of this interval.  (Overrides
[GH_GooTDuplicate](M_Grasshopper_Kernel_Types_GH_Goo_1_Duplicate.htm).)  
![Public method](../icons/pubmethod.gif)|
[DuplicateInterval](M_Grasshopper_Kernel_Types_GH_Interval2D_DuplicateInterval.htm)|
Create a duplicate of this interval.  
![Public method](../icons/pubmethod.gif)|
[EmitProxy](M_Grasshopper_Kernel_Types_GH_Interval2D_EmitProxy.htm)|  Returns
a proxy that represents this interval. Do not call this function unless you're
(Overrides
[GH_GooTEmitProxy](M_Grasshopper_Kernel_Types_GH_Goo_1_EmitProxy.htm).)  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_Types_GH_Interval2D_Read.htm)|  (Overrides
[GH_GooTRead(GH_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).)  
![Public method](../icons/pubmethod.gif)|
[ScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm)|
This function will be called when the local IGH_Goo instance disappears into a
user Script. This would be an excellent place to cast your IGH_Goo type to a
simple data type.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Types_GH_Interval2D_ToString.htm)|  Format the
interval using default grasshopper formatting logic.  (Overrides
[GH_GooTToString](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).)  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_Types_GH_Interval2D_Write.htm)|  (Overrides
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

