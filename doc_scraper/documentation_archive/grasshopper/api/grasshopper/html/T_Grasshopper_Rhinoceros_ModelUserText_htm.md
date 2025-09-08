---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_ModelUserText.htm
scraped_at: 2025-09-08T16:22:44.936336
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros](../html/N_Grasshopper_Rhinoceros.htm
"Grasshopper.Rhinoceros")

[ModelUserText Structure](../html/T_Grasshopper_Rhinoceros_ModelUserText.htm
"ModelUserText Structure")

[ModelUserText Constructor
](../html/M_Grasshopper_Rhinoceros_ModelUserText__ctor.htm "ModelUserText
Constructor ")

[ModelUserText
Properties](../html/Properties_T_Grasshopper_Rhinoceros_ModelUserText.htm
"ModelUserText Properties")

[ModelUserText
Methods](../html/Methods_T_Grasshopper_Rhinoceros_ModelUserText.htm
"ModelUserText Methods")

[ModelUserText
Operators](../html/Operators_T_Grasshopper_Rhinoceros_ModelUserText.htm
"ModelUserText Operators")

[ModelUserText
Fields](../html/Fields_T_Grasshopper_Rhinoceros_ModelUserText.htm
"ModelUserText Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelUserText Structure  
  
---  
  
Represents an immutable collection of string/string pairs.

**Namespace:** [Grasshopper.Rhinoceros](N_Grasshopper_Rhinoceros.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public struct ModelUserText : GH_ISerializable, 
    	IReadOnlyList<KeyValuePair<string, string>>, IReadOnlyDictionary<string, string>, 
    	IEquatable<ModelUserText>, IStructuralEquatable
    
    
    Public Structure ModelUserText
    	Implements GH_ISerializable, IReadOnlyList(Of KeyValuePair(Of String, String)), 
    	IReadOnlyDictionary(Of String, String), IEquatable(Of ModelUserText), 
    	IStructuralEquatable

The ModelUserText type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ModelUserText](M_Grasshopper_Rhinoceros_ModelUserText__ctor.htm)| Initializes
a new instance of the ModelUserText class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Count](P_Grasshopper_Rhinoceros_ModelUserText_Count.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsDefault](P_Grasshopper_Rhinoceros_ModelUserText_IsDefault.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsDefaultOrEmpty](P_Grasshopper_Rhinoceros_ModelUserText_IsDefaultOrEmpty.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsEmpty](P_Grasshopper_Rhinoceros_ModelUserText_IsEmpty.htm)|  
![Public property](../icons/pubproperty.gif)|
[ItemInt32](P_Grasshopper_Rhinoceros_ModelUserText_Item.htm)|  
![Public property](../icons/pubproperty.gif)|
[ItemString](P_Grasshopper_Rhinoceros_ModelUserText_Item_1.htm)|  
![Public property](../icons/pubproperty.gif)|
[Keys](P_Grasshopper_Rhinoceros_ModelUserText_Keys.htm)|  
![Public property](../icons/pubproperty.gif)|
[Values](P_Grasshopper_Rhinoceros_ModelUserText_Values.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ContainsKey](M_Grasshopper_Rhinoceros_ModelUserText_ContainsKey.htm)|  
![Public method](../icons/pubmethod.gif)|
[EnsureRange(IEnumerableKeyValuePairString,
String)](M_Grasshopper_Rhinoceros_ModelUserText_EnsureRange.htm)|  
![Public method](../icons/pubmethod.gif)|
[EnsureRange(IEnumerableString)](M_Grasshopper_Rhinoceros_ModelUserText_EnsureRange_1.htm)|  
![Public method](../icons/pubmethod.gif)|
[Equals(ModelUserText)](M_Grasshopper_Rhinoceros_ModelUserText_Equals.htm)|  
![Public method](../icons/pubmethod.gif)|
[Equals(Object)](M_Grasshopper_Rhinoceros_ModelUserText_Equals_1.htm)|
(Overrides
[ValueTypeEquals(Object)](https://docs.microsoft.com/dotnet/api/system.valuetype.equals#system-
valuetype-equals\(system-object\)).)  
![Public method](../icons/pubmethod.gif)|
[GetEnumerator](M_Grasshopper_Rhinoceros_ModelUserText_GetEnumerator.htm)|  
![Public method](../icons/pubmethod.gif)|
[GetHashCode](M_Grasshopper_Rhinoceros_ModelUserText_GetHashCode.htm)|
(Overrides
[ValueTypeGetHashCode](https://docs.microsoft.com/dotnet/api/system.valuetype.gethashcode#system-
valuetype-gethashcode).)  
![Public method](../icons/pubmethod.gif)|
[MergeRange(IEnumerableKeyValuePairString,
String)](M_Grasshopper_Rhinoceros_ModelUserText_MergeRange.htm)|  
![Public method](../icons/pubmethod.gif)|
[MergeRange(IEnumerableString)](M_Grasshopper_Rhinoceros_ModelUserText_MergeRange_1.htm)|  
![Public method](../icons/pubmethod.gif)|
[RemoveRange(IEnumerableKeyValuePairString,
String)](M_Grasshopper_Rhinoceros_ModelUserText_RemoveRange.htm)|  
![Public method](../icons/pubmethod.gif)|
[RemoveRange(IEnumerableString)](M_Grasshopper_Rhinoceros_ModelUserText_RemoveRange_1.htm)|  
![Public method](../icons/pubmethod.gif)|
[TryGetValue](M_Grasshopper_Rhinoceros_ModelUserText_TryGetValue.htm)|  
![Public method](../icons/pubmethod.gif)|
[UpdateRange(IEnumerableKeyValuePairString,
String)](M_Grasshopper_Rhinoceros_ModelUserText_UpdateRange.htm)|  
![Public method](../icons/pubmethod.gif)|
[UpdateRange(IEnumerableString)](M_Grasshopper_Rhinoceros_ModelUserText_UpdateRange_1.htm)|  
Top

![](../icons/SectionExpanded.png)Operators

| Name| Description  
---|---|---  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [Addition(ModelUserText,
IEnumerableKeyValuePairString,
String)](M_Grasshopper_Rhinoceros_ModelUserText_op_Addition.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [Addition(ModelUserText,
IEnumerableString)](M_Grasshopper_Rhinoceros_ModelUserText_op_Addition_1.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [BitwiseAnd(ModelUserText,
IEnumerableKeyValuePairString,
String)](M_Grasshopper_Rhinoceros_ModelUserText_op_BitwiseAnd.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [BitwiseAnd(ModelUserText,
IEnumerableString)](M_Grasshopper_Rhinoceros_ModelUserText_op_BitwiseAnd_1.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [BitwiseOr(ModelUserText,
IEnumerableKeyValuePairString,
String)](M_Grasshopper_Rhinoceros_ModelUserText_op_BitwiseOr.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [BitwiseOr(ModelUserText,
IEnumerableString)](M_Grasshopper_Rhinoceros_ModelUserText_op_BitwiseOr_1.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)|
[Equality](M_Grasshopper_Rhinoceros_ModelUserText_op_Equality.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)|
[Inequality](M_Grasshopper_Rhinoceros_ModelUserText_op_Inequality.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [Subtraction(ModelUserText,
IEnumerableKeyValuePairString,
String)](M_Grasshopper_Rhinoceros_ModelUserText_op_Subtraction.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [Subtraction(ModelUserText,
IEnumerableString)](M_Grasshopper_Rhinoceros_ModelUserText_op_Subtraction_1.htm)|  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[Empty](F_Grasshopper_Rhinoceros_ModelUserText_Empty.htm)|  
Top

![](../icons/SectionExpanded.png)Remarks

Key comparison is not case sensitive.

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros Namespace](N_Grasshopper_Rhinoceros.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

