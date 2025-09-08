---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Base_SliderSnapRange.htm
scraped_at: 2025-09-08T16:13:55.648726
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Base](../html/N_Grasshopper_GUI_Base.htm
"Grasshopper.GUI.Base")

[SliderSnapRange Structure](../html/T_Grasshopper_GUI_Base_SliderSnapRange.htm
"SliderSnapRange Structure")

[SliderSnapRange Constructor
](../html/Overload_Grasshopper_GUI_Base_SliderSnapRange__ctor.htm
"SliderSnapRange Constructor ")

[SliderSnapRange
Properties](../html/Properties_T_Grasshopper_GUI_Base_SliderSnapRange.htm
"SliderSnapRange Properties")

[SliderSnapRange
Methods](../html/Methods_T_Grasshopper_GUI_Base_SliderSnapRange.htm
"SliderSnapRange Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# SliderSnapRange Structure  
  
---  
  
Represents a snap range on a slider.

**Namespace:** [Grasshopper.GUI.Base](N_Grasshopper_GUI_Base.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public struct SliderSnapRange : IComparable<SliderSnapRange>
    
    
    Public Structure SliderSnapRange
    	Implements IComparable(Of SliderSnapRange)

The SliderSnapRange type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[SliderSnapRange(Decimal)](M_Grasshopper_GUI_Base_SliderSnapRange__ctor.htm)|
Initializes a new instance of the SliderSnapRange class  
![Public method](../icons/pubmethod.gif)| [SliderSnapRange(Decimal,
Decimal)](M_Grasshopper_GUI_Base_SliderSnapRange__ctor_1.htm)| Initializes a
new instance of the SliderSnapRange class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[IsSingleton](P_Grasshopper_GUI_Base_SliderSnapRange_IsSingleton.htm)|  
![Public property](../icons/pubproperty.gif)|
[Max](P_Grasshopper_GUI_Base_SliderSnapRange_Max.htm)|  
![Public property](../icons/pubproperty.gif)|
[Min](P_Grasshopper_GUI_Base_SliderSnapRange_Min.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CanMerge](M_Grasshopper_GUI_Base_SliderSnapRange_CanMerge.htm)|  
![Public method](../icons/pubmethod.gif)|
[CompareTo](M_Grasshopper_GUI_Base_SliderSnapRange_CompareTo.htm)|  
![Public method](../icons/pubmethod.gif)|
[DistanceTo](M_Grasshopper_GUI_Base_SliderSnapRange_DistanceTo.htm)|  Compute
the distance from a value to this snap range.  
![Public method](../icons/pubmethod.gif)|
[Merge](M_Grasshopper_GUI_Base_SliderSnapRange_Merge.htm)|  
![Public method](../icons/pubmethod.gif)|
[SnapValue](M_Grasshopper_GUI_Base_SliderSnapRange_SnapValue.htm)|  Gets the
snapped value of another value.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Base Namespace](N_Grasshopper_GUI_Base.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

