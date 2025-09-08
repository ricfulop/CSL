---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_ModelUnitSystem.htm
scraped_at: 2025-09-08T16:22:42.906161
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros](../html/N_Grasshopper_Rhinoceros.htm
"Grasshopper.Rhinoceros")

[ModelUnitSystem Class](../html/T_Grasshopper_Rhinoceros_ModelUnitSystem.htm
"ModelUnitSystem Class")

[ModelUnitSystem Constructor
](../html/Overload_Grasshopper_Rhinoceros_ModelUnitSystem__ctor.htm
"ModelUnitSystem Constructor ")

[ModelUnitSystem
Properties](../html/Properties_T_Grasshopper_Rhinoceros_ModelUnitSystem.htm
"ModelUnitSystem Properties")

[ModelUnitSystem
Methods](../html/Methods_T_Grasshopper_Rhinoceros_ModelUnitSystem.htm
"ModelUnitSystem Methods")

[ModelUnitSystem Type
Conversions](../html/Operators_T_Grasshopper_Rhinoceros_ModelUnitSystem.htm
"ModelUnitSystem Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelUnitSystem Class  
  
---  
  
Represents a Rhino Unit System. Wraps the functionality of the UnitSystem
type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.RhinocerosModelValue](T_Grasshopper_Rhinoceros_ModelValue.htm)  
Grasshopper.RhinocerosModelUnitSystem  

**Namespace:** [Grasshopper.Rhinoceros](N_Grasshopper_Rhinoceros.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class ModelUnitSystem : ModelValue
    
    
    Public NotInheritable Class ModelUnitSystem
    	Inherits ModelValue

The ModelUnitSystem type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ModelUnitSystem](M_Grasshopper_Rhinoceros_ModelUnitSystem__ctor.htm)|
Initializes a new instance of the ModelUnitSystem class  
![Public method](../icons/pubmethod.gif)|
[ModelUnitSystem(ModelUnitSystemValue)](M_Grasshopper_Rhinoceros_ModelUnitSystem__ctor_1.htm)|
Initializes a new instance of the ModelUnitSystem class  
![Public method](../icons/pubmethod.gif)| [ModelUnitSystem(ActiveSpace,
RhinoDoc)](M_Grasshopper_Rhinoceros_ModelUnitSystem__ctor_2.htm)| Initializes
a new instance of the ModelUnitSystem class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[ActiveSpace](P_Grasshopper_Rhinoceros_ModelUnitSystem_ActiveSpace.htm)|  
![Public property](../icons/pubproperty.gif)|
[BaseSystem](P_Grasshopper_Rhinoceros_ModelUnitSystem_BaseSystem.htm)|  
![Public property](../icons/pubproperty.gif)|
[Factor](P_Grasshopper_Rhinoceros_ModelUnitSystem_Factor.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Rhinoceros_ModelUnitSystem_IsValid.htm)|  (Overrides
ModelValue.IsValid.)  
![Public property](../icons/pubproperty.gif)|
[MetersPerUnit](P_Grasshopper_Rhinoceros_ModelUnitSystem_MetersPerUnit.htm)|  
![Public property](../icons/pubproperty.gif)|
[Name](P_Grasshopper_Rhinoceros_ModelUnitSystem_Name.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AdjustDocumentUnitSystem](M_Grasshopper_Rhinoceros_ModelUnitSystem_AdjustDocumentUnitSystem.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Cast](M_Grasshopper_Rhinoceros_ModelUnitSystem_Cast.htm)|  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Rhinoceros_ModelUnitSystem_CastTo__1.htm)|
(Overrides
[ModelValueCastToT(T)](M_Grasshopper_Rhinoceros_ModelValue_CastTo__1.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Rhinoceros_ModelValue_CastTo__1.htm)|  (Inherited
from [ModelValue](T_Grasshopper_Rhinoceros_ModelValue.htm).)  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Copy](M_Grasshopper_Rhinoceros_ModelUnitSystem_Copy.htm)|  
![Public method](../icons/pubmethod.gif)|
[Equals(ModelValue)](M_Grasshopper_Rhinoceros_ModelValue_Equals.htm)|
(Inherited from [ModelValue](T_Grasshopper_Rhinoceros_ModelValue.htm).)  
![Public method](../icons/pubmethod.gif)|
[Equals(Object)](M_Grasshopper_Rhinoceros_ModelUnitSystem_Equals.htm)|
(Overrides
[ModelValueEquals(Object)](M_Grasshopper_Rhinoceros_ModelValue_Equals_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[GetHashCode](M_Grasshopper_Rhinoceros_ModelUnitSystem_GetHashCode.htm)|
(Overrides
[ModelValueGetHashCode](M_Grasshopper_Rhinoceros_ModelValue_GetHashCode.htm).)  
![Public method](../icons/pubmethod.gif)|
[TooltipString](M_Grasshopper_Rhinoceros_ModelUnitSystem_TooltipString.htm)|
(Overrides
[ModelValueTooltipString](M_Grasshopper_Rhinoceros_ModelValue_TooltipString.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Rhinoceros_ModelValue_ToString.htm)|  (Inherited from
[ModelValue](T_Grasshopper_Rhinoceros_ModelValue.htm).)  
Top

![](../icons/SectionExpanded.png)Operators

| Name| Description  
---|---|---  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(ModelUnitSystem to
ModelUnitSystemValue)](M_Grasshopper_Rhinoceros_ModelUnitSystem_op_Implicit.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(ModelUnitSystemValue to
ModelUnitSystem)](M_Grasshopper_Rhinoceros_ModelUnitSystem_op_Implicit_1.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros Namespace](N_Grasshopper_Rhinoceros.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

