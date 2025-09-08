---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Base_GH_DigitNumber.htm
scraped_at: 2025-09-08T16:13:38.559114
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Base](../html/N_Grasshopper_GUI_Base.htm
"Grasshopper.GUI.Base")

[GH_DigitNumber Class](../html/T_Grasshopper_GUI_Base_GH_DigitNumber.htm
"GH_DigitNumber Class")

[GH_DigitNumber Constructor
](../html/Overload_Grasshopper_GUI_Base_GH_DigitNumber__ctor.htm
"GH_DigitNumber Constructor ")

[GH_DigitNumber
Properties](../html/Properties_T_Grasshopper_GUI_Base_GH_DigitNumber.htm
"GH_DigitNumber Properties")

[GH_DigitNumber
Methods](../html/Methods_T_Grasshopper_GUI_Base_GH_DigitNumber.htm
"GH_DigitNumber Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_DigitNumber Class  
  
---  
  
Maintains and provides functionality for evaluating and modifying numbers as
used in the GH_DigitScrollerBase control.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.GUI.BaseGH_DigitNumber  

**Namespace:** [Grasshopper.GUI.Base](N_Grasshopper_GUI_Base.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_DigitNumber
    
    
    Public Class GH_DigitNumber

The GH_DigitNumber type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_DigitNumber(GH_DigitNumber)](M_Grasshopper_GUI_Base_GH_DigitNumber__ctor.htm)|
Create an exact duplicate of another GH_DigitNumber instance.  
![Public method](../icons/pubmethod.gif)|
[GH_DigitNumber(Int32)](M_Grasshopper_GUI_Base_GH_DigitNumber__ctor_1.htm)|
Create a new GH_DigitNumber instance with the specified number of decimal
places.  
![Public method](../icons/pubmethod.gif)| [GH_DigitNumber(Int32,
Int32)](M_Grasshopper_GUI_Base_GH_DigitNumber__ctor_2.htm)|  Create a new
GH_DigitNumber instance with the specified number of decimal places and a
given radix position.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[DigitCount](P_Grasshopper_GUI_Base_GH_DigitNumber_DigitCount.htm)|  Gets or
sets the amount of digits in this number.  
![Public property](../icons/pubproperty.gif)|
[Epsilon](P_Grasshopper_GUI_Base_GH_DigitNumber_Epsilon.htm)|  Gets the
smallest possible change.  
![Public property](../icons/pubproperty.gif)|
[IsPrimaryDigitSignificant](P_Grasshopper_GUI_Base_GH_DigitNumber_IsPrimaryDigitSignificant.htm)|
Gets whether the primary digit at the given index is significant.  
![Public property](../icons/pubproperty.gif)|
[IsSecondaryDigitSignificant](P_Grasshopper_GUI_Base_GH_DigitNumber_IsSecondaryDigitSignificant.htm)|
Gets whether the secondary digit at the given index is significant.  
![Public property](../icons/pubproperty.gif)|
[Maximum](P_Grasshopper_GUI_Base_GH_DigitNumber_Maximum.htm)|  Gets the
maximum value allowed in this number.  
![Public property](../icons/pubproperty.gif)|
[Minimum](P_Grasshopper_GUI_Base_GH_DigitNumber_Minimum.htm)|  Gets the
minimum value allowed in this number.  
![Public property](../icons/pubproperty.gif)|
[Offset](P_Grasshopper_GUI_Base_GH_DigitNumber_Offset.htm)|  Gets the offset
between the primary and secondary digits.  
![Public property](../icons/pubproperty.gif)|
[PrimaryDigits](P_Grasshopper_GUI_Base_GH_DigitNumber_PrimaryDigits.htm)|
Gets the internal list of primary digits. Do not modify this list.  
![Public property](../icons/pubproperty.gif)|
[PrimaryPositive](P_Grasshopper_GUI_Base_GH_DigitNumber_PrimaryPositive.htm)|
Gets or sets a value indicating whether the number is positive.  
![Public property](../icons/pubproperty.gif)|
[Radix](P_Grasshopper_GUI_Base_GH_DigitNumber_Radix.htm)|  Gets or sets the
radix point index. A negative radix index disables the radix point, zero is
not a valid index.  
![Public property](../icons/pubproperty.gif)|
[RadixIndex](P_Grasshopper_GUI_Base_GH_DigitNumber_RadixIndex.htm)|  Gets the
mapped radix.  
![Public property](../icons/pubproperty.gif)|
[SecondaryDigits](P_Grasshopper_GUI_Base_GH_DigitNumber_SecondaryDigits.htm)|
Gets the internal list of secondary digits. Do not modify this list.  
![Public property](../icons/pubproperty.gif)|
[SecondaryPositive](P_Grasshopper_GUI_Base_GH_DigitNumber_SecondaryPositive.htm)|
Gets a value indicating whether the secondary number is positive.  
![Public property](../icons/pubproperty.gif)|
[Value](P_Grasshopper_GUI_Base_GH_DigitNumber_Value.htm)|  Gets or sets the
value of this number.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AssignOffset](M_Grasshopper_GUI_Base_GH_DigitNumber_AssignOffset.htm)|
Assign an offset to a given digit and recursively adjust all leftwards offsets
if needed.  
![Public method](../icons/pubmethod.gif)|
[LimitValue](M_Grasshopper_GUI_Base_GH_DigitNumber_LimitValue.htm)|  Limits
the value to the minimum and maximum domain.  
![Public method](../icons/pubmethod.gif)|
[Reset](M_Grasshopper_GUI_Base_GH_DigitNumber_Reset.htm)|  Reset all parts to
zero.  
![Public method](../icons/pubmethod.gif)|
[Round](M_Grasshopper_GUI_Base_GH_DigitNumber_Round.htm)|  Round the number by
cancelling the offset in the proper direction.  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_GUI_Base_GH_DigitNumber_ToString.htm)|  (Overrides
[ObjectToString](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Base Namespace](N_Grasshopper_GUI_Base.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

