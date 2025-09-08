---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_ModelColor.htm
scraped_at: 2025-09-08T16:22:30.853831
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros](../html/N_Grasshopper_Rhinoceros.htm
"Grasshopper.Rhinoceros")

[ModelColor Structure](../html/T_Grasshopper_Rhinoceros_ModelColor.htm
"ModelColor Structure")

[ModelColor Methods](../html/Methods_T_Grasshopper_Rhinoceros_ModelColor.htm
"ModelColor Methods")

[ModelColor Operators and Type
Conversions](../html/Operators_T_Grasshopper_Rhinoceros_ModelColor.htm
"ModelColor Operators and Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelColor Structure  
  
---  
  
Represents a color stored on a model.

**Namespace:** [Grasshopper.Rhinoceros](N_Grasshopper_Rhinoceros.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public struct ModelColor : IGH_Goo, 
    	IFormattable, IEquatable<ModelColor>, IComparable, IComparable<ModelColor>
    
    
    Public Structure ModelColor
    	Implements IGH_Goo, IFormattable, IEquatable(Of ModelColor), 
    	IComparable, IComparable(Of ModelColor)

The ModelColor type exposes the following members.

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CompareTo](M_Grasshopper_Rhinoceros_ModelColor_CompareTo.htm)|  
![Public method](../icons/pubmethod.gif)|
[Equals(ModelColor)](M_Grasshopper_Rhinoceros_ModelColor_Equals.htm)|  
![Public method](../icons/pubmethod.gif)|
[Equals(Object)](M_Grasshopper_Rhinoceros_ModelColor_Equals_1.htm)|
(Overrides
[ValueTypeEquals(Object)](https://docs.microsoft.com/dotnet/api/system.valuetype.equals#system-
valuetype-equals\(system-object\)).)  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FromArgb(Int32)](M_Grasshopper_Rhinoceros_ModelColor_FromArgb_2.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FromArgb(Byte, Byte,
Byte)](M_Grasshopper_Rhinoceros_ModelColor_FromArgb.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FromArgb(Byte, Byte, Byte,
Byte)](M_Grasshopper_Rhinoceros_ModelColor_FromArgb_1.htm)|  
![Public method](../icons/pubmethod.gif)|
[GetHashCode](M_Grasshopper_Rhinoceros_ModelColor_GetHashCode.htm)|
(Overrides
[ValueTypeGetHashCode](https://docs.microsoft.com/dotnet/api/system.valuetype.gethashcode#system-
valuetype-gethashcode).)  
![Public method](../icons/pubmethod.gif)|
[ToArgb](M_Grasshopper_Rhinoceros_ModelColor_ToArgb.htm)|  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Rhinoceros_ModelColor_ToString.htm)|  (Overrides
[ValueTypeToString](https://docs.microsoft.com/dotnet/api/system.valuetype.tostring#system-
valuetype-tostring).)  
Top

![](../icons/SectionExpanded.png)Operators

| Name| Description  
---|---|---  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [Equality(Color,
ModelColor)](M_Grasshopper_Rhinoceros_ModelColor_op_Equality_2.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [Equality(ModelColor,
ModelColor)](M_Grasshopper_Rhinoceros_ModelColor_op_Equality.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [Equality(ModelColor,
Color)](M_Grasshopper_Rhinoceros_ModelColor_op_Equality_1.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(ModelColor to
ColorRGBA)](M_Grasshopper_Rhinoceros_ModelColor_op_Explicit.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(Color to
ModelColor)](M_Grasshopper_Rhinoceros_ModelColor_op_Implicit_2.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(ColorRGBA to
ModelColor)](M_Grasshopper_Rhinoceros_ModelColor_op_Implicit_1.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(ModelColor to
Color)](M_Grasshopper_Rhinoceros_ModelColor_op_Implicit.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [Inequality(Color,
ModelColor)](M_Grasshopper_Rhinoceros_ModelColor_op_Inequality_2.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [Inequality(ModelColor,
ModelColor)](M_Grasshopper_Rhinoceros_ModelColor_op_Inequality.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [Inequality(ModelColor,
Color)](M_Grasshopper_Rhinoceros_ModelColor_op_Inequality_1.htm)|  
Top

![](../icons/SectionExpanded.png)Remarks

This is an opaque representation of a color with conversion methods to and
from other color types.

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros Namespace](N_Grasshopper_Rhinoceros.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

