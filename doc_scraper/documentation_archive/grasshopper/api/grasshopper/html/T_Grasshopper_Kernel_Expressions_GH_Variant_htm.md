---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Expressions_GH_Variant.htm
scraped_at: 2025-09-08T16:19:47.212294
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Expressions](../html/N_Grasshopper_Kernel_Expressions.htm
"Grasshopper.Kernel.Expressions")

[GH_Variant Class](../html/T_Grasshopper_Kernel_Expressions_GH_Variant.htm
"GH_Variant Class")

[GH_Variant Constructor
](../html/Overload_Grasshopper_Kernel_Expressions_GH_Variant__ctor.htm
"GH_Variant Constructor ")

[GH_Variant
Properties](../html/Properties_T_Grasshopper_Kernel_Expressions_GH_Variant.htm
"GH_Variant Properties")

[GH_Variant
Methods](../html/Methods_T_Grasshopper_Kernel_Expressions_GH_Variant.htm
"GH_Variant Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Variant Class  
  
---  
  
Variant data used in Grasshopper Expressions.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Kernel.ExpressionsGH_Variant  

**Namespace:**
[Grasshopper.Kernel.Expressions](N_Grasshopper_Kernel_Expressions.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Variant
    
    
    Public Class GH_Variant

The GH_Variant type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_Variant](M_Grasshopper_Kernel_Expressions_GH_Variant__ctor.htm)|  Create a
new Null variant.  
![Public method](../icons/pubmethod.gif)|
[GH_Variant(Boolean)](M_Grasshopper_Kernel_Expressions_GH_Variant__ctor_6.htm)|
Create a new Bool variant.  
![Public method](../icons/pubmethod.gif)|
[GH_Variant(Complex)](M_Grasshopper_Kernel_Expressions_GH_Variant__ctor_2.htm)|
Create a new Complex variant.  
![Public method](../icons/pubmethod.gif)|
[GH_Variant(Double)](M_Grasshopper_Kernel_Expressions_GH_Variant__ctor_7.htm)|
Create a new Double variant.  
![Public method](../icons/pubmethod.gif)|
[GH_Variant(GH_Variant)](M_Grasshopper_Kernel_Expressions_GH_Variant__ctor_1.htm)|
Duplicate a Variant.  
![Public method](../icons/pubmethod.gif)|
[GH_Variant(Int32)](M_Grasshopper_Kernel_Expressions_GH_Variant__ctor_8.htm)|
Create a new Integer variant.  
![Public method](../icons/pubmethod.gif)|
[GH_Variant(Plane)](M_Grasshopper_Kernel_Expressions_GH_Variant__ctor_3.htm)|
Create a new Plane variant.  
![Public method](../icons/pubmethod.gif)|
[GH_Variant(Point3d)](M_Grasshopper_Kernel_Expressions_GH_Variant__ctor_4.htm)|
Create a new Point variant.  
![Public method](../icons/pubmethod.gif)|
[GH_Variant(String)](M_Grasshopper_Kernel_Expressions_GH_Variant__ctor_9.htm)|
Create a new String variant.  
![Public method](../icons/pubmethod.gif)|
[GH_Variant(Vector3d)](M_Grasshopper_Kernel_Expressions_GH_Variant__ctor_5.htm)|
Create a new Point variant.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[_Bool](P_Grasshopper_Kernel_Expressions_GH_Variant__Bool.htm)|  Gets the
contents of this Variant as a bool.  
![Public property](../icons/pubproperty.gif)|
[_Complex](P_Grasshopper_Kernel_Expressions_GH_Variant__Complex.htm)|  Gets
the contents of this Variant as a complex number.  
![Public property](../icons/pubproperty.gif)|
[_Double](P_Grasshopper_Kernel_Expressions_GH_Variant__Double.htm)|  Gets the
contents of this Variant as a double. If the Variant is of type Integer this
cast will also work.  
![Public property](../icons/pubproperty.gif)|
[_Int](P_Grasshopper_Kernel_Expressions_GH_Variant__Int.htm)|  Gets the
contents of this Variant as an integer.  
![Public property](../icons/pubproperty.gif)|
[_Plane](P_Grasshopper_Kernel_Expressions_GH_Variant__Plane.htm)|  Gets the
contents of this Variant as a Plane.  
![Public property](../icons/pubproperty.gif)|
[_Point](P_Grasshopper_Kernel_Expressions_GH_Variant__Point.htm)|  Gets the
contents of this Variant as a Point.  
![Public property](../icons/pubproperty.gif)|
[_String](P_Grasshopper_Kernel_Expressions_GH_Variant__String.htm)|  Gets the
contents of this Variant as a String. This function will work for all Variant
types.  
![Public property](../icons/pubproperty.gif)|
[_Vector](P_Grasshopper_Kernel_Expressions_GH_Variant__Vector.htm)|  Gets the
contents of this Variant as a Vector.  
![Public property](../icons/pubproperty.gif)|
[IsNumeric](P_Grasshopper_Kernel_Expressions_GH_Variant_IsNumeric.htm)|  Gets
a value indicating whether or not the Variant is a numeric type. Only Doubles
and Integers are considered to be Numeric.  
![Public property](../icons/pubproperty.gif)|
[Type](P_Grasshopper_Kernel_Expressions_GH_Variant_Type.htm)|  Gets the Type
of this Variant.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[DataT](M_Grasshopper_Kernel_Expressions_GH_Variant_Data__1.htm)|  Perform a
straight cast of the data inside this Variant.  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Kernel_Expressions_GH_Variant_Duplicate.htm)|
Duplicate this Variant. If the type of this Variant is [unknown] the contents
are not guaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)|
[Evaluate](M_Grasshopper_Kernel_Expressions_GH_Variant_Evaluate.htm)|  If this
variant represents a string, this function will attempt to evaluate that
string and replace the data inside this variant.  
![Public method](../icons/pubmethod.gif)|
[ToGoo](M_Grasshopper_Kernel_Expressions_GH_Variant_ToGoo.htm)|  Attempt to
convert a Variant to a Grasshopper IGH_Goo type.  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Expressions_GH_Variant_ToString.htm)|
(Overrides
[ObjectToString](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Expressions
Namespace](N_Grasshopper_Kernel_Expressions.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

