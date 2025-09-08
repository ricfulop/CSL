---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Base_GH_ColourPickerEventArgs.htm
scraped_at: 2025-09-08T16:13:35.553303
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Base](../html/N_Grasshopper_GUI_Base.htm
"Grasshopper.GUI.Base")

[GH_ColourPickerEventArgs
Class](../html/T_Grasshopper_GUI_Base_GH_ColourPickerEventArgs.htm
"GH_ColourPickerEventArgs Class")

[GH_ColourPickerEventArgs
Properties](../html/Properties_T_Grasshopper_GUI_Base_GH_ColourPickerEventArgs.htm
"GH_ColourPickerEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_ColourPickerEventArgs Class  
  
---  
  
Arguments passed via GH_SliderBase.ValueChanged events.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[SystemEventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
Grasshopper.GUI.BaseGH_ColourPickerEventArgs  

**Namespace:** [Grasshopper.GUI.Base](N_Grasshopper_GUI_Base.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_ColourPickerEventArgs : EventArgs
    
    
    Public Class GH_ColourPickerEventArgs
    	Inherits EventArgs

The GH_ColourPickerEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Colour](P_Grasshopper_GUI_Base_GH_ColourPickerEventArgs_Colour.htm)|  Gets
the new value of the colour picker. This value is cached, so even if the
picker subsequently updates, this property remains constant.  
![Public property](../icons/pubproperty.gif)|
[ColourPicker](P_Grasshopper_GUI_Base_GH_ColourPickerEventArgs_ColourPicker.htm)|
Gets the instance of the picker that raised the event.  
![Public property](../icons/pubproperty.gif)|
[Intermediate](P_Grasshopper_GUI_Base_GH_ColourPickerEventArgs_Intermediate.htm)|
Gets a value indicating whether the change was an intermediate one.  
![Public property](../icons/pubproperty.gif)|
[Original](P_Grasshopper_GUI_Base_GH_ColourPickerEventArgs_Original.htm)|
Gets the original value of the colour picker. This value is cached, so even if
the picker subsequently updates, this property remains constant.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Base Namespace](N_Grasshopper_GUI_Base.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

