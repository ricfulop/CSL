---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_ModelTags.htm
scraped_at: 2025-09-08T16:22:41.908327
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros](../html/N_Grasshopper_Rhinoceros.htm
"Grasshopper.Rhinoceros")

[ModelTags Structure](../html/T_Grasshopper_Rhinoceros_ModelTags.htm
"ModelTags Structure")

[ModelTags Constructor ](../html/M_Grasshopper_Rhinoceros_ModelTags__ctor.htm
"ModelTags Constructor ")

[ModelTags
Properties](../html/Properties_T_Grasshopper_Rhinoceros_ModelTags.htm
"ModelTags Properties")

[ModelTags Methods](../html/Methods_T_Grasshopper_Rhinoceros_ModelTags.htm
"ModelTags Methods")

[ModelTags Operators and Type
Conversions](../html/Operators_T_Grasshopper_Rhinoceros_ModelTags.htm
"ModelTags Operators and Type Conversions")

[ModelTags Fields](../html/Fields_T_Grasshopper_Rhinoceros_ModelTags.htm
"ModelTags Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelTags Structure  
  
---  
  
Represents an immutable set of strings.

**Namespace:** [Grasshopper.Rhinoceros](N_Grasshopper_Rhinoceros.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public struct ModelTags : GH_ISerializable, IReadOnlyCollection<string>, 
    	IEquatable<ModelTags>, IStructuralEquatable, IComparable, IComparable<ModelTags>
    
    
    Public Structure ModelTags
    	Implements GH_ISerializable, IReadOnlyCollection(Of String), 
    	IEquatable(Of ModelTags), IStructuralEquatable, IComparable, IComparable(Of ModelTags)

The ModelTags type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ModelTags](M_Grasshopper_Rhinoceros_ModelTags__ctor.htm)| Initializes a new
instance of the ModelTags class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Count](P_Grasshopper_Rhinoceros_ModelTags_Count.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsDefault](P_Grasshopper_Rhinoceros_ModelTags_IsDefault.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsDefaultOrEmpty](P_Grasshopper_Rhinoceros_ModelTags_IsDefaultOrEmpty.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsEmpty](P_Grasshopper_Rhinoceros_ModelTags_IsEmpty.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AddRange](M_Grasshopper_Rhinoceros_ModelTags_AddRange.htm)|  
![Public method](../icons/pubmethod.gif)|
[CompareTo(ModelTags)](M_Grasshopper_Rhinoceros_ModelTags_CompareTo.htm)|  
![Public method](../icons/pubmethod.gif)|
[CompareTo(Object)](M_Grasshopper_Rhinoceros_ModelTags_CompareTo_1.htm)|  
![Public method](../icons/pubmethod.gif)|
[Contains](M_Grasshopper_Rhinoceros_ModelTags_Contains.htm)|  
![Public method](../icons/pubmethod.gif)|
[Equals(ModelTags)](M_Grasshopper_Rhinoceros_ModelTags_Equals.htm)|  
![Public method](../icons/pubmethod.gif)|
[Equals(Object)](M_Grasshopper_Rhinoceros_ModelTags_Equals_1.htm)|  (Overrides
[ValueTypeEquals(Object)](https://docs.microsoft.com/dotnet/api/system.valuetype.equals#system-
valuetype-equals\(system-object\)).)  
![Public method](../icons/pubmethod.gif)|
[GetEnumerator](M_Grasshopper_Rhinoceros_ModelTags_GetEnumerator.htm)|  
![Public method](../icons/pubmethod.gif)|
[GetHashCode](M_Grasshopper_Rhinoceros_ModelTags_GetHashCode.htm)|  (Overrides
[ValueTypeGetHashCode](https://docs.microsoft.com/dotnet/api/system.valuetype.gethashcode#system-
valuetype-gethashcode).)  
![Public method](../icons/pubmethod.gif)|
[RemoveRange](M_Grasshopper_Rhinoceros_ModelTags_RemoveRange.htm)|  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Rhinoceros_ModelTags_ToString.htm)|  (Overrides
[ValueTypeToString](https://docs.microsoft.com/dotnet/api/system.valuetype.tostring#system-
valuetype-tostring).)  
Top

![](../icons/SectionExpanded.png)Operators

| Name| Description  
---|---|---  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)|
[Addition](M_Grasshopper_Rhinoceros_ModelTags_op_Addition.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)|
[Equality](M_Grasshopper_Rhinoceros_ModelTags_op_Equality.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(ModelTags to
String)](M_Grasshopper_Rhinoceros_ModelTags_op_Implicit.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(String to
ModelTags)](M_Grasshopper_Rhinoceros_ModelTags_op_Implicit_1.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)|
[Inequality](M_Grasshopper_Rhinoceros_ModelTags_op_Inequality.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)|
[Subtraction](M_Grasshopper_Rhinoceros_ModelTags_op_Subtraction.htm)|  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[Empty](F_Grasshopper_Rhinoceros_ModelTags_Empty.htm)|  
Top

![](../icons/SectionExpanded.png)Remarks

Comparison is not case sensitive.

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros Namespace](N_Grasshopper_Rhinoceros.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

