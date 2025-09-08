---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value.htm
scraped_at: 2025-09-08T16:23:57.235728
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros.Drafting](../html/N_Grasshopper_Rhinoceros_Drafting.htm
"Grasshopper.Rhinoceros.Drafting")

[ObjectDraftingColor.Value
Structure](../html/T_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value.htm
"ObjectDraftingColor.Value Structure")

[Value Constructor
](../html/Overload_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value__ctor.htm
"Value Constructor ")

[Value
Properties](../html/Properties_T_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value.htm
"Value Properties")

[Value
Methods](../html/Methods_T_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value.htm
"Value Methods")

[Value Type
Conversions](../html/Operators_T_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value.htm
"Value Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ObjectDraftingColorValue Structure  
  
---  
  
**Namespace:**
[Grasshopper.Rhinoceros.Drafting](N_Grasshopper_Rhinoceros_Drafting.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public struct Value : GH_ISerializable, IEquatable<ObjectDraftingColorValue>, 
    	IComparable<ObjectDraftingColorValue>, IComparable
    
    
    Public Structure Value
    	Implements GH_ISerializable, IEquatable(Of ObjectDraftingColorValue), 
    	IComparable(Of ObjectDraftingColorValue), IComparable

The ObjectDraftingColorValue type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ObjectDraftingColorValue(ModelColor)](M_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value__ctor.htm)|
Initializes a new instance of the ObjectDraftingColorValue class  
![Public method](../icons/pubmethod.gif)|
[ObjectDraftingColorValue(ObjectPlotColorSource)](M_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value__ctor_1.htm)|
Initializes a new instance of the ObjectDraftingColorValue class  
![Public method](../icons/pubmethod.gif)|
[ObjectDraftingColorValue(ObjectPlotColorSource,
ModelColor)](M_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value__ctor_2.htm)|
Initializes a new instance of the ObjectDraftingColorValue class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[ByDisplay](P_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value_ByDisplay.htm)|  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[ByLayer](P_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value_ByLayer.htm)|  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[ByParent](P_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value_ByParent.htm)|  
![Public property](../icons/pubproperty.gif)|
[Color](P_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value_Color.htm)|  
![Public property](../icons/pubproperty.gif)|
[Source](P_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value_Source.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CompareTo(Object)](M_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value_CompareTo_1.htm)|  
![Public method](../icons/pubmethod.gif)|
[CompareTo(ObjectDraftingColorValue)](M_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value_CompareTo.htm)|  
![Public method](../icons/pubmethod.gif)|
[Deconstruct](M_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value_Deconstruct.htm)|  
![Public method](../icons/pubmethod.gif)|
[Equals(Object)](M_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value_Equals_1.htm)|
(Overrides
[ValueTypeEquals(Object)](https://docs.microsoft.com/dotnet/api/system.valuetype.equals#system-
valuetype-equals\(system-object\)).)  
![Public method](../icons/pubmethod.gif)|
[Equals(ObjectDraftingColorValue)](M_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value_Equals.htm)|  
![Public method](../icons/pubmethod.gif)|
[GetHashCode](M_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value_GetHashCode.htm)|
(Overrides
[ValueTypeGetHashCode](https://docs.microsoft.com/dotnet/api/system.valuetype.gethashcode#system-
valuetype-gethashcode).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value_ToString.htm)|
(Overrides
[ValueTypeToString](https://docs.microsoft.com/dotnet/api/system.valuetype.tostring#system-
valuetype-tostring).)  
Top

![](../icons/SectionExpanded.png)Operators

| Name| Description  
---|---|---  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(ModelColor to
ObjectDraftingColorValue)](M_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value_op_Implicit_2.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(ObjectPlotColorSource to
ObjectDraftingColorValue)](M_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value_op_Implicit_3.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(ObjectDraftingColorValue to
ModelColor)](M_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value_op_Implicit_1.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(ObjectDraftingColorValue to
ObjectPlotColorSource)](M_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor_Value_op_Implicit.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Drafting
Namespace](N_Grasshopper_Rhinoceros_Drafting.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

