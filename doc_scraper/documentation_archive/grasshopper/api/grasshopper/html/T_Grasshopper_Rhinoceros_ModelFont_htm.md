---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_ModelFont.htm
scraped_at: 2025-09-08T16:22:39.889655
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros](../html/N_Grasshopper_Rhinoceros.htm
"Grasshopper.Rhinoceros")

[ModelFont Class](../html/T_Grasshopper_Rhinoceros_ModelFont.htm "ModelFont
Class")

[ModelFont Constructor
](../html/Overload_Grasshopper_Rhinoceros_ModelFont__ctor.htm "ModelFont
Constructor ")

[ModelFont
Properties](../html/Properties_T_Grasshopper_Rhinoceros_ModelFont.htm
"ModelFont Properties")

[ModelFont Methods](../html/Methods_T_Grasshopper_Rhinoceros_ModelFont.htm
"ModelFont Methods")

[ModelFont Type
Conversions](../html/Operators_T_Grasshopper_Rhinoceros_ModelFont.htm
"ModelFont Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelFont Class  
  
---  
  
Represents a typography font. Wraps the functionality of the Font type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.Kernel.TypesGH_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)Font  
Grasshopper.RhinocerosModelFont  

**Namespace:** [Grasshopper.Rhinoceros](N_Grasshopper_Rhinoceros.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class ModelFont : GH_Goo<Font>, 
    	IEquatable<ModelFont>
    
    
    Public NotInheritable Class ModelFont
    	Inherits GH_Goo(Of Font)
    	Implements IEquatable(Of ModelFont)

The ModelFont type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ModelFont](M_Grasshopper_Rhinoceros_ModelFont__ctor.htm)| Initializes a new
instance of the ModelFont class  
![Public method](../icons/pubmethod.gif)|
[ModelFont(Font)](M_Grasshopper_Rhinoceros_ModelFont__ctor_1.htm)| Initializes
a new instance of the ModelFont class  
![Public method](../icons/pubmethod.gif)|
[ModelFont(String)](M_Grasshopper_Rhinoceros_ModelFont__ctor_2.htm)|
Initializes a new instance of the ModelFont class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[FamilyName](P_Grasshopper_Rhinoceros_ModelFont_FamilyName.htm)|  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[InstalledFamilies](P_Grasshopper_Rhinoceros_ModelFont_InstalledFamilies.htm)|  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[InstalledFonts](P_Grasshopper_Rhinoceros_ModelFont_InstalledFonts.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsInstalled](P_Grasshopper_Rhinoceros_ModelFont_IsInstalled.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Rhinoceros_ModelFont_IsValid.htm)|  (Overrides
[GH_GooTIsValid](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValid.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm)|  Gets
a string describing the state of "invalidness". If the instance _is_ valid,
then this property should return Nothing or String.Empty.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeDescription](P_Grasshopper_Rhinoceros_ModelFont_TypeDescription.htm)|
(Overrides
[GH_GooTTypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Rhinoceros_ModelFont_TypeName.htm)|  (Overrides
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
[CastFrom](M_Grasshopper_Rhinoceros_ModelFont_CastFrom.htm)|  (Overrides
[GH_GooTCastFrom(Object)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastFrom.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToQ](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm)|  Attempt a cast
to type Q.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Rhinoceros_ModelFont_Duplicate.htm)|  (Overrides
[GH_GooTDuplicate](M_Grasshopper_Kernel_Types_GH_Goo_1_Duplicate.htm).)  
![Public method](../icons/pubmethod.gif)|
[EmitProxy](M_Grasshopper_Kernel_Types_GH_Goo_1_EmitProxy.htm)|  Create a new
proxy for this instance. Return Null if this class does not support proxies.
(Inherited from [GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[Equals(ModelFont)](M_Grasshopper_Rhinoceros_ModelFont_Equals.htm)|  
![Public method](../icons/pubmethod.gif)|
[Equals(Object)](M_Grasshopper_Rhinoceros_ModelFont_Equals_1.htm)|  (Overrides
[ObjectEquals(Object)](https://docs.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)).)  
![Public method](../icons/pubmethod.gif)|
[GetHashCode](M_Grasshopper_Rhinoceros_ModelFont_GetHashCode.htm)|  (Overrides
[ObjectGetHashCode](https://docs.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode).)  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[IsFamilyNameInstalled](M_Grasshopper_Rhinoceros_ModelFont_IsFamilyNameInstalled.htm)|  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Rhinoceros_ModelFont_Read.htm)|  (Overrides
[GH_GooTRead(GH_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).)  
![Public method](../icons/pubmethod.gif)|
[ScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm)|
This function will be called when the local IGH_Goo instance disappears into a
user Script. This would be an excellent place to cast your IGH_Goo type to a
simple data type.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Rhinoceros_ModelFont_ToString.htm)|  (Overrides
[GH_GooTToString](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).)  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Rhinoceros_ModelFont_Write.htm)|  (Overrides
[GH_GooTWrite(GH_IWriter)](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm).)  
Top

![](../icons/SectionExpanded.png)Operators

| Name| Description  
---|---|---  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(Font to
ModelFont)](M_Grasshopper_Rhinoceros_ModelFont_op_Implicit.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(String to
ModelFont)](M_Grasshopper_Rhinoceros_ModelFont_op_Implicit_1.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros Namespace](N_Grasshopper_Rhinoceros.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

