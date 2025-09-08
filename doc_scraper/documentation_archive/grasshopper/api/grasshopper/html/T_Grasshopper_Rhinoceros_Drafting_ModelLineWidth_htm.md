---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_Drafting_ModelLineWidth.htm
scraped_at: 2025-09-08T16:23:53.214059
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros.Drafting](../html/N_Grasshopper_Rhinoceros_Drafting.htm
"Grasshopper.Rhinoceros.Drafting")

[ModelLineWidth
Class](../html/T_Grasshopper_Rhinoceros_Drafting_ModelLineWidth.htm
"ModelLineWidth Class")

[ModelLineWidth Constructor
](../html/Overload_Grasshopper_Rhinoceros_Drafting_ModelLineWidth__ctor.htm
"ModelLineWidth Constructor ")

[ModelLineWidth
Properties](../html/Properties_T_Grasshopper_Rhinoceros_Drafting_ModelLineWidth.htm
"ModelLineWidth Properties")

[ModelLineWidth
Methods](../html/Methods_T_Grasshopper_Rhinoceros_Drafting_ModelLineWidth.htm
"ModelLineWidth Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelLineWidth Class  
  
---  
  
Represents a Rhino model linetype.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.Kernel.TypesGH_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)[Double](https://docs.microsoft.com/dotnet/api/system.double)  
[Grasshopper.Kernel.TypesGH_Number](T_Grasshopper_Kernel_Types_GH_Number.htm)  
Grasshopper.Rhinoceros.DraftingModelLineWidth  

**Namespace:**
[Grasshopper.Rhinoceros.Drafting](N_Grasshopper_Rhinoceros_Drafting.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class ModelLineWidth : GH_Number, 
    	IEquatable<ModelLineWidth>
    
    
    Public NotInheritable Class ModelLineWidth
    	Inherits GH_Number
    	Implements IEquatable(Of ModelLineWidth)

The ModelLineWidth type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ModelLineWidth](M_Grasshopper_Rhinoceros_Drafting_ModelLineWidth__ctor.htm)|
Initializes a new instance of the ModelLineWidth class  
![Public method](../icons/pubmethod.gif)|
[ModelLineWidth(Double)](M_Grasshopper_Rhinoceros_Drafting_ModelLineWidth__ctor_1.htm)|
Initializes a new instance of the ModelLineWidth class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Kernel_Types_GH_Number_IsValid.htm)|  Gets the
validity of this instance. If the number is NaN, then it is considered invalid
(Inherited from [GH_Number](T_Grasshopper_Kernel_Types_GH_Number.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Number_IsValidWhyNot.htm)|  Gets
a string describing the state of "invalidness". If the instance _is_ valid,
then this property should return Nothing or String.Empty.  (Inherited from
[GH_Number](T_Grasshopper_Kernel_Types_GH_Number.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeDescription](P_Grasshopper_Rhinoceros_Drafting_ModelLineWidth_TypeDescription.htm)|
(Overrides
[GH_NumberTypeDescription](P_Grasshopper_Kernel_Types_GH_Number_TypeDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Rhinoceros_Drafting_ModelLineWidth_TypeName.htm)|
(Overrides
[GH_NumberTypeName](P_Grasshopper_Kernel_Types_GH_Number_TypeName.htm).)  
![Public property](../icons/pubproperty.gif)|
[Value](P_Grasshopper_Kernel_Types_GH_Goo_1_Value.htm)|  Gets or sets the
internal data.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CastFrom](M_Grasshopper_Rhinoceros_Drafting_ModelLineWidth_CastFrom.htm)|
(Overrides
[GH_NumberCastFrom(Object)](M_Grasshopper_Kernel_Types_GH_Number_CastFrom.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToQ(Q)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm)|  Attempt a
cast to type Q.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Kernel_Types_GH_Number_CastTo__1.htm)|  (Inherited
from [GH_Number](T_Grasshopper_Kernel_Types_GH_Number.htm).)  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Rhinoceros_Drafting_ModelLineWidth_Duplicate.htm)|
(Overrides
[GH_NumberDuplicate](M_Grasshopper_Kernel_Types_GH_Number_Duplicate.htm).)  
![Public method](../icons/pubmethod.gif)|
[DuplicateNumber](M_Grasshopper_Kernel_Types_GH_Number_DuplicateNumber.htm)|
(Inherited from [GH_Number](T_Grasshopper_Kernel_Types_GH_Number.htm).)  
![Public method](../icons/pubmethod.gif)|
[EmitProxy](M_Grasshopper_Kernel_Types_GH_Number_EmitProxy.htm)|  (Inherited
from [GH_Number](T_Grasshopper_Kernel_Types_GH_Number.htm).)  
![Public method](../icons/pubmethod.gif)|
[Equals(ModelLineWidth)](M_Grasshopper_Rhinoceros_Drafting_ModelLineWidth_Equals.htm)|  
![Public method](../icons/pubmethod.gif)|
[Equals(Object)](M_Grasshopper_Rhinoceros_Drafting_ModelLineWidth_Equals_1.htm)|
(Overrides
[ObjectEquals(Object)](https://docs.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)).)  
![Public method](../icons/pubmethod.gif)|
[GetHashCode](M_Grasshopper_Rhinoceros_Drafting_ModelLineWidth_GetHashCode.htm)|
(Overrides
[ObjectGetHashCode](https://docs.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode).)  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_Types_GH_Number_Read.htm)|  (Inherited from
[GH_Number](T_Grasshopper_Kernel_Types_GH_Number.htm).)  
![Public method](../icons/pubmethod.gif)|
[ScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm)|
This function will be called when the local IGH_Goo instance disappears into a
user Script. This would be an excellent place to cast your IGH_Goo type to a
simple data type.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Rhinoceros_Drafting_ModelLineWidth_ToString.htm)|
(Overrides
[GH_NumberToString](M_Grasshopper_Kernel_Types_GH_Number_ToString.htm).)  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_Types_GH_Number_Write.htm)|  (Inherited from
[GH_Number](T_Grasshopper_Kernel_Types_GH_Number.htm).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Drafting
Namespace](N_Grasshopper_Rhinoceros_Drafting.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

