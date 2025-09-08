---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_ModelUnitSystem_Value.htm
scraped_at: 2025-09-08T16:22:43.917282
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros](../html/N_Grasshopper_Rhinoceros.htm
"Grasshopper.Rhinoceros")

[ModelUnitSystem.Value
Structure](../html/T_Grasshopper_Rhinoceros_ModelUnitSystem_Value.htm
"ModelUnitSystem.Value Structure")

[Value Constructor
](../html/Overload_Grasshopper_Rhinoceros_ModelUnitSystem_Value__ctor.htm
"Value Constructor ")

[Value
Properties](../html/Properties_T_Grasshopper_Rhinoceros_ModelUnitSystem_Value.htm
"Value Properties")

[Value
Methods](../html/Methods_T_Grasshopper_Rhinoceros_ModelUnitSystem_Value.htm
"Value Methods")

[Value
Operators](../html/Operators_T_Grasshopper_Rhinoceros_ModelUnitSystem_Value.htm
"Value Operators")

[Value
Fields](../html/Fields_T_Grasshopper_Rhinoceros_ModelUnitSystem_Value.htm
"Value Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelUnitSystemValue Structure  
  
---  
  
**Namespace:** [Grasshopper.Rhinoceros](N_Grasshopper_Rhinoceros.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public struct Value : GH_ISerializable, IEquatable<ModelUnitSystemValue>, 
    	IComparable<ModelUnitSystemValue>, IComparable
    
    
    Public Structure Value
    	Implements GH_ISerializable, IEquatable(Of ModelUnitSystemValue), 
    	IComparable(Of ModelUnitSystemValue), IComparable

The ModelUnitSystemValue type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)| [ModelUnitSystemValue(ActiveSpace,
String)](M_Grasshopper_Rhinoceros_ModelUnitSystem_Value__ctor_1.htm)|
Initializes a new instance of the ModelUnitSystemValue class  
![Public method](../icons/pubmethod.gif)| [ModelUnitSystemValue(UnitSystem,
String)](M_Grasshopper_Rhinoceros_ModelUnitSystem_Value__ctor_2.htm)|
Initializes a new instance of the ModelUnitSystemValue class  
![Public method](../icons/pubmethod.gif)| [ModelUnitSystemValue(UnitSystem,
String, Double)](M_Grasshopper_Rhinoceros_ModelUnitSystem_Value__ctor_3.htm)|
Initializes a new instance of the ModelUnitSystemValue class  
![Public method](../icons/pubmethod.gif)|
[ModelUnitSystemValue(ModelUnitSystemValue, String,
NullableDouble)](M_Grasshopper_Rhinoceros_ModelUnitSystem_Value__ctor.htm)|
Initializes a new instance of the ModelUnitSystemValue class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[ActiveSpace](P_Grasshopper_Rhinoceros_ModelUnitSystem_Value_ActiveSpace.htm)|  
![Public property](../icons/pubproperty.gif)|
[BaseSystem](P_Grasshopper_Rhinoceros_ModelUnitSystem_Value_BaseSystem.htm)|  
![Public property](../icons/pubproperty.gif)|
[Factor](P_Grasshopper_Rhinoceros_ModelUnitSystem_Value_Factor.htm)|  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[Feet](P_Grasshopper_Rhinoceros_ModelUnitSystem_Value_Feet.htm)|  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[Inches](P_Grasshopper_Rhinoceros_ModelUnitSystem_Value_Inches.htm)|  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[Meters](P_Grasshopper_Rhinoceros_ModelUnitSystem_Value_Meters.htm)|  
![Public property](../icons/pubproperty.gif)|
[MetersPerUnit](P_Grasshopper_Rhinoceros_ModelUnitSystem_Value_MetersPerUnit.htm)|  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[Millimeters](P_Grasshopper_Rhinoceros_ModelUnitSystem_Value_Millimeters.htm)|  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[ModelUnits](P_Grasshopper_Rhinoceros_ModelUnitSystem_Value_ModelUnits.htm)|  
![Public property](../icons/pubproperty.gif)|
[Name](P_Grasshopper_Rhinoceros_ModelUnitSystem_Value_Name.htm)|  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[None](P_Grasshopper_Rhinoceros_ModelUnitSystem_Value_None.htm)|  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[PageUnits](P_Grasshopper_Rhinoceros_ModelUnitSystem_Value_PageUnits.htm)|  
![Public property](../icons/pubproperty.gif)|
[Symbol](P_Grasshopper_Rhinoceros_ModelUnitSystem_Value_Symbol.htm)|  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[Unset](P_Grasshopper_Rhinoceros_ModelUnitSystem_Value_Unset.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AdjustDocumentUnitSystem](M_Grasshopper_Rhinoceros_ModelUnitSystem_Value_AdjustDocumentUnitSystem.htm)|  
![Public method](../icons/pubmethod.gif)|
[CompareTo(Object)](M_Grasshopper_Rhinoceros_ModelUnitSystem_Value_CompareTo_1.htm)|  
![Public method](../icons/pubmethod.gif)|
[CompareTo(ModelUnitSystemValue)](M_Grasshopper_Rhinoceros_ModelUnitSystem_Value_CompareTo.htm)|  
![Public method](../icons/pubmethod.gif)|
[Equals(Object)](M_Grasshopper_Rhinoceros_ModelUnitSystem_Value_Equals_1.htm)|
(Overrides
[ValueTypeEquals(Object)](https://docs.microsoft.com/dotnet/api/system.valuetype.equals#system-
valuetype-equals\(system-object\)).)  
![Public method](../icons/pubmethod.gif)|
[Equals(ModelUnitSystemValue)](M_Grasshopper_Rhinoceros_ModelUnitSystem_Value_Equals.htm)|  
![Public method](../icons/pubmethod.gif)|
[GetHashCode](M_Grasshopper_Rhinoceros_ModelUnitSystem_Value_GetHashCode.htm)|
(Overrides
[ValueTypeGetHashCode](https://docs.microsoft.com/dotnet/api/system.valuetype.gethashcode#system-
valuetype-gethashcode).)  
![Public method](../icons/pubmethod.gif)|
[ToNonCustomUnitSystem](M_Grasshopper_Rhinoceros_ModelUnitSystem_Value_ToNonCustomUnitSystem.htm)|  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Rhinoceros_ModelUnitSystem_Value_ToString.htm)|
(Overrides
[ValueTypeToString](https://docs.microsoft.com/dotnet/api/system.valuetype.tostring#system-
valuetype-tostring).)  
![Public method](../icons/pubmethod.gif)|
[ToUnitSystem](M_Grasshopper_Rhinoceros_ModelUnitSystem_Value_ToUnitSystem.htm)|  
Top

![](../icons/SectionExpanded.png)Operators

| Name| Description  
---|---|---  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)|
[Equality](M_Grasshopper_Rhinoceros_ModelUnitSystem_Value_op_Equality.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)|
[Inequality](M_Grasshopper_Rhinoceros_ModelUnitSystem_Value_op_Inequality.htm)|  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Public field](../icons/pubfield.gif)|
[_MetersPerUnit](F_Grasshopper_Rhinoceros_ModelUnitSystem_Value__MetersPerUnit.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros Namespace](N_Grasshopper_Rhinoceros.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

