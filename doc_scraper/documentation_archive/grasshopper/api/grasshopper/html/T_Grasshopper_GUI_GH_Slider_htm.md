---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_GH_Slider.htm
scraped_at: 2025-09-08T16:13:05.419041
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH_Slider Class](../html/T_Grasshopper_GUI_GH_Slider.htm "GH_Slider Class")

[GH_Slider Constructor ](../html/M_Grasshopper_GUI_GH_Slider__ctor.htm
"GH_Slider Constructor ")

[GH_Slider Properties](../html/Properties_T_Grasshopper_GUI_GH_Slider.htm
"GH_Slider Properties")

[GH_Slider Methods](../html/Methods_T_Grasshopper_GUI_GH_Slider.htm "GH_Slider
Methods")

[GH_Slider Events](../html/Events_T_Grasshopper_GUI_GH_Slider.htm "GH_Slider
Events")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Slider Class  
  
---  
  
Provides a standard Grasshopper slider as a winforms control.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[SystemMarshalByRefObject](https://docs.microsoft.com/dotnet/api/system.marshalbyrefobject)  
[System.ComponentModelComponent](https://docs.microsoft.com/dotnet/api/system.componentmodel.component)  
[System.Windows.FormsControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.control)  
[System.Windows.FormsScrollableControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol)  
[System.Windows.FormsContainerControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.containercontrol)  
[System.Windows.FormsUserControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.usercontrol)  
GH_TextInputBaseControl  
Grasshopper.GUIGH_Slider  

**Namespace:** [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Slider : GH_TextInputBaseControl
    
    
    Public Class GH_Slider
    	Inherits GH_TextInputBaseControl

The GH_Slider type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_Slider](M_Grasshopper_GUI_GH_Slider__ctor.htm)| Initializes a new instance
of the GH_Slider class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[ControlEdgeColour](P_Grasshopper_GUI_GH_Slider_ControlEdgeColour.htm)|  Gets
or sets the EdgeColor for this slider control.  
![Public property](../icons/pubproperty.gif)|
[ControlShadowColour](P_Grasshopper_GUI_GH_Slider_ControlShadowColour.htm)|
Gets or sets the Shadow colour for this control.  
![Public property](../icons/pubproperty.gif)|
[DecimalPlaces](P_Grasshopper_GUI_GH_Slider_DecimalPlaces.htm)|  Gets or sets
the number of decimal places allowed for Floating Point Sliders.  
![Public property](../icons/pubproperty.gif)|
[DrawControlBorder](P_Grasshopper_GUI_GH_Slider_DrawControlBorder.htm)|  Gets
or sets whether the border of the slider should be drawn.  
![Public property](../icons/pubproperty.gif)|
[DrawControlShadows](P_Grasshopper_GUI_GH_Slider_DrawControlShadows.htm)|
Gets or sets whether the drop shadows of the slider should be drawn.  
![Public property](../icons/pubproperty.gif)|
[FormatMask](P_Grasshopper_GUI_GH_Slider_FormatMask.htm)|  Gets or sets the
string format mask to use for the display. Should contain at least one "{0}"
element.  
![Public property](../icons/pubproperty.gif)|
[GripBottomColour](P_Grasshopper_GUI_GH_Slider_GripBottomColour.htm)|  Gets or
sets the fill colour for the bottom edge of the slider grip.  
![Public property](../icons/pubproperty.gif)|
[GripDisplay](P_Grasshopper_GUI_GH_Slider_GripDisplay.htm)|  Gets or sets how
the slider grip (or thumb) is drawn.  
![Public property](../icons/pubproperty.gif)|
[GripEdgeColour](P_Grasshopper_GUI_GH_Slider_GripEdgeColour.htm)|  Gets or
sets the edge colour for the slider grip.  
![Public property](../icons/pubproperty.gif)|
[GripTopColour](P_Grasshopper_GUI_GH_Slider_GripTopColour.htm)|  Gets or sets
the fill colour for the top edge of the slider grip.  
![Public property](../icons/pubproperty.gif)|
[Maximum](P_Grasshopper_GUI_GH_Slider_Maximum.htm)|  Gets or sets the upper
numeric limit for the slider range.  
![Public property](../icons/pubproperty.gif)|
[Minimum](P_Grasshopper_GUI_GH_Slider_Minimum.htm)|  Gets or sets the lower
numeric limit for the slider range.  
![Public property](../icons/pubproperty.gif)|
[RailBrightColour](P_Grasshopper_GUI_GH_Slider_RailBrightColour.htm)|  Gets or
sets the edge colour for the bright parts of the rail.  
![Public property](../icons/pubproperty.gif)|
[RailDarkColour](P_Grasshopper_GUI_GH_Slider_RailDarkColour.htm)|  Gets or
sets the edge colour for the dark parts of the rail.  
![Public property](../icons/pubproperty.gif)|
[RailDisplay](P_Grasshopper_GUI_GH_Slider_RailDisplay.htm)|  Gets or sets how
the slider rail (or track) is drawn.  
![Public property](../icons/pubproperty.gif)|
[RailEmptyColour](P_Grasshopper_GUI_GH_Slider_RailEmptyColour.htm)|  Gets or
sets the fill colour for the empty portion of the rail.  
![Public property](../icons/pubproperty.gif)|
[RailFullColour](P_Grasshopper_GUI_GH_Slider_RailFullColour.htm)|  Gets or
sets the fill colour for the full portion of the rail.  
![Public property](../icons/pubproperty.gif)|
[ShadowSize](P_Grasshopper_GUI_GH_Slider_ShadowSize.htm)|  Gets or sets the
size of the border shadow along all edges of the box.  
![Public property](../icons/pubproperty.gif)|
[TextColour](P_Grasshopper_GUI_GH_Slider_TextColour.htm)|  Gets or sets the
fill colour for the slider text.  
![Public property](../icons/pubproperty.gif)|
[TickCount](P_Grasshopper_GUI_GH_Slider_TickCount.htm)|  Gets or sets the
number of ticks.  
![Public property](../icons/pubproperty.gif)|
[TickDisplay](P_Grasshopper_GUI_GH_Slider_TickDisplay.htm)|  Gets or sets how
the slider ticks are drawn.  
![Public property](../icons/pubproperty.gif)|
[TickFrequency](P_Grasshopper_GUI_GH_Slider_TickFrequency.htm)|  Gets or sets
the frequency of large ticks vs small ticks.  
![Public property](../icons/pubproperty.gif)|
[Type](P_Grasshopper_GUI_GH_Slider_Type.htm)|  Gets or sets the numeric type
of this slider.  
![Public property](../icons/pubproperty.gif)|
[Value](P_Grasshopper_GUI_GH_Slider_Value.htm)|  Gets or sets the numeric
value for the slider range.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[Input_Assign](M_Grasshopper_GUI_GH_Slider_Input_Assign.htm)|  (Overrides
GH_TextInputBaseControl.Input_Assign(String).)  
![Protected method](../icons/protmethod.gif)|
[Input_Parse](M_Grasshopper_GUI_GH_Slider_Input_Parse.htm)|  (Overrides
GH_TextInputBaseControl.Input_Parse(String).)  
![Protected method](../icons/protmethod.gif)|
[Input_Supply](M_Grasshopper_GUI_GH_Slider_Input_Supply.htm)|  (Overrides
GH_TextInputBaseControl.Input_Supply.)  
![Protected method](../icons/protmethod.gif)|
[OnPaint](M_Grasshopper_GUI_GH_Slider_OnPaint.htm)|  (Overrides
[ControlOnPaint(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.control.onpaint#system-
windows-forms-control-onpaint\(system-windows-forms-painteventargs\)).)  
![Protected method](../icons/protmethod.gif)|
[OnPaintBackground](M_Grasshopper_GUI_GH_Slider_OnPaintBackground.htm)|
(Overrides
[ScrollableControlOnPaintBackground(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol.onpaintbackground#system-
windows-forms-scrollablecontrol-onpaintbackground\(system-windows-forms-
painteventargs\)).)  
Top

![](../icons/SectionExpanded.png)Events

| Name| Description  
---|---|---  
![Public event](../icons/pubevent.gif)|
[ValueChanged](E_Grasshopper_GUI_GH_Slider_ValueChanged.htm)|  Raised whenever
the value of the slider is changed via GUI interaction.  
Top

![](../icons/SectionExpanded.png)Extension Methods

| Name| Description  
---|---|---  
![Public Extension Method](../icons/pubextension.gif)|
[ToEto](M_Grasshopper_EtoExtensions_ToEto_7.htm)|  (Defined by
[EtoExtensions](T_Grasshopper_EtoExtensions.htm).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

