---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Base_GH_SliderBase.htm
scraped_at: 2025-09-08T16:13:46.682944
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Base](../html/N_Grasshopper_GUI_Base.htm
"Grasshopper.GUI.Base")

[GH_SliderBase Class](../html/T_Grasshopper_GUI_Base_GH_SliderBase.htm
"GH_SliderBase Class")

[GH_SliderBase Constructor
](../html/M_Grasshopper_GUI_Base_GH_SliderBase__ctor.htm "GH_SliderBase
Constructor ")

[GH_SliderBase
Properties](../html/Properties_T_Grasshopper_GUI_Base_GH_SliderBase.htm
"GH_SliderBase Properties")

[GH_SliderBase
Methods](../html/Methods_T_Grasshopper_GUI_Base_GH_SliderBase.htm
"GH_SliderBase Methods")

[GH_SliderBase Events](../html/Events_T_Grasshopper_GUI_Base_GH_SliderBase.htm
"GH_SliderBase Events")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_SliderBase Class  
  
---  
  
Provides Numeric slider GUI not tied to a control-handle.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.GUI.BaseGH_TextBoxInputBase](T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm)  
Grasshopper.GUI.BaseGH_SliderBase  

**Namespace:** [Grasshopper.GUI.Base](N_Grasshopper_GUI_Base.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_SliderBase : GH_TextBoxInputBase
    
    
    Public Class GH_SliderBase
    	Inherits GH_TextBoxInputBase

The GH_SliderBase type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_SliderBase](M_Grasshopper_GUI_Base_GH_SliderBase__ctor.htm)| Initializes a
new instance of the GH_SliderBase class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Bounds](P_Grasshopper_GUI_Base_GH_SliderBase_Bounds.htm)|  Gets or sets the
bounds of the slider.  (Overrides GH_TextBoxInputBase.Bounds.)  
![Public property](../icons/pubproperty.gif)|
[ControlBackColour](P_Grasshopper_GUI_Base_GH_SliderBase_ControlBackColour.htm)|
Gets or sets the BackColour for this slider control.  
![Public property](../icons/pubproperty.gif)|
[ControlEdgeColour](P_Grasshopper_GUI_Base_GH_SliderBase_ControlEdgeColour.htm)|
Gets or sets the EdgeColor for this slider control.  
![Public property](../icons/pubproperty.gif)|
[ControlShadowColour](P_Grasshopper_GUI_Base_GH_SliderBase_ControlShadowColour.htm)|
Gets or sets the Shadow colour for this control.  
![Public property](../icons/pubproperty.gif)|
[DecimalPlaces](P_Grasshopper_GUI_Base_GH_SliderBase_DecimalPlaces.htm)|  Gets
or sets the number of decimal places allowed for floating point type sliders.
Valid values between zero and 12.  
![Public property](../icons/pubproperty.gif)|
[DrawControlBackground](P_Grasshopper_GUI_Base_GH_SliderBase_DrawControlBackground.htm)|
Gets or sets whether the background of the slider should be drawn.  
![Public property](../icons/pubproperty.gif)|
[DrawControlBorder](P_Grasshopper_GUI_Base_GH_SliderBase_DrawControlBorder.htm)|
Gets or sets whether the border of the slider should be drawn.  
![Public property](../icons/pubproperty.gif)|
[DrawControlShadows](P_Grasshopper_GUI_Base_GH_SliderBase_DrawControlShadows.htm)|
Gets or sets whether the drop shadows of the slider should be drawn.  
![Public property](../icons/pubproperty.gif)|
[Epsilon](P_Grasshopper_GUI_Base_GH_SliderBase_Epsilon.htm)|  Gets the
smallest value change supported by the current slider properties.  
![Public property](../icons/pubproperty.gif)|
[Font](P_Grasshopper_GUI_Base_GH_SliderBase_Font.htm)|  Gets or sets the font
for this slider.  (Overrides
[GH_TextBoxInputBaseFont](P_Grasshopper_GUI_Base_GH_TextBoxInputBase_Font.htm).)  
![Public property](../icons/pubproperty.gif)|
[FormatMask](P_Grasshopper_GUI_Base_GH_SliderBase_FormatMask.htm)|  Gets or
sets the string format mask to use for the display. Should contain at least
one "{0}" element.  
![Public property](../icons/pubproperty.gif)|
[Grip](P_Grasshopper_GUI_Base_GH_SliderBase_Grip.htm)|  Gets the box of the
current grip. If the slider value/limits are not set up correctly then this
rectangle may well be outside of the bounds. If the limits are coincident,
this will fail (divide by zero).  
![Public property](../icons/pubproperty.gif)|
[GripBottomColour](P_Grasshopper_GUI_Base_GH_SliderBase_GripBottomColour.htm)|
Gets or sets the fill colour for the bottom edge of the slider grip.  
![Public property](../icons/pubproperty.gif)|
[GripDisplay](P_Grasshopper_GUI_Base_GH_SliderBase_GripDisplay.htm)|  Gets or
sets how the slider grip (or thumb) is drawn.  
![Public property](../icons/pubproperty.gif)|
[GripEdgeColour](P_Grasshopper_GUI_Base_GH_SliderBase_GripEdgeColour.htm)|
Gets or sets the edge colour for the slider grip.  
![Public property](../icons/pubproperty.gif)|
[GripText](P_Grasshopper_GUI_Base_GH_SliderBase_GripText.htm)|  Gets the text
that will be drawn on the slider.  
![Public property](../icons/pubproperty.gif)|
[GripTopColour](P_Grasshopper_GUI_Base_GH_SliderBase_GripTopColour.htm)|  Gets
or sets the fill colour for the top edge of the slider grip.  
![Public property](../icons/pubproperty.gif)|
[GripWidth](P_Grasshopper_GUI_Base_GH_SliderBase_GripWidth.htm)|  Gets an
estimate of the maximum number of pixels taken up by the grip. This property
depends on many different factors, though should remain constant when other
properties are not changed. If the Font hasn't been specified, the default
Windows.Forms.Control font is used.  
![Public property](../icons/pubproperty.gif)|
[IsTextInput](P_Grasshopper_GUI_Base_GH_TextBoxInputBase_IsTextInput.htm)|
Gets whether the text input box is currently on screen.  (Inherited from
[GH_TextBoxInputBase](T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm).)  
![Public property](../icons/pubproperty.gif)|
[Maximum](P_Grasshopper_GUI_Base_GH_SliderBase_Maximum.htm)|  Gets or sets the
upper limit of the slider.  
![Public property](../icons/pubproperty.gif)|
[Minimum](P_Grasshopper_GUI_Base_GH_SliderBase_Minimum.htm)|  Gets or sets the
lower limit of the slider.  
![Public property](../icons/pubproperty.gif)|
[NormalizedValue](P_Grasshopper_GUI_Base_GH_SliderBase_NormalizedValue.htm)|
Gets or sets the normalized value within the slider domain.  
![Public property](../icons/pubproperty.gif)|
[Padding](P_Grasshopper_GUI_Base_GH_SliderBase_Padding.htm)|  Gets or sets the
padding around the slider border.  
![Public property](../icons/pubproperty.gif)|
[Rail](P_Grasshopper_GUI_Base_GH_SliderBase_Rail.htm)|  Gets the shape of the
rail. The height of the rectangle will be zero, but the y-position will be
rounded to integer precision.  
![Public property](../icons/pubproperty.gif)|
[RailBrightColour](P_Grasshopper_GUI_Base_GH_SliderBase_RailBrightColour.htm)|
Gets or sets the bright colour used to draw rails and ticks.  
![Public property](../icons/pubproperty.gif)|
[RailDarkColour](P_Grasshopper_GUI_Base_GH_SliderBase_RailDarkColour.htm)|
Gets or sets the dark colour used to draw rails and ticks.  
![Public property](../icons/pubproperty.gif)|
[RailDisplay](P_Grasshopper_GUI_Base_GH_SliderBase_RailDisplay.htm)|  Gets or
sets how the slider rail (or track) is drawn.  
![Public property](../icons/pubproperty.gif)|
[RailEmptyColour](P_Grasshopper_GUI_Base_GH_SliderBase_RailEmptyColour.htm)|
Gets or sets the fill colour for the empty portion of the rail.  
![Public property](../icons/pubproperty.gif)|
[RailFullColour](P_Grasshopper_GUI_Base_GH_SliderBase_RailFullColour.htm)|
Gets or sets the fill colour for the full portion of the rail.  
![Public property](../icons/pubproperty.gif)|
[RaiseEvents](P_Grasshopper_GUI_Base_GH_SliderBase_RaiseEvents.htm)|  Gets or
sets a value indicating whether this slider raises the ValueChanged event.  
![Public property](../icons/pubproperty.gif)|
[ShadowSize](P_Grasshopper_GUI_Base_GH_SliderBase_ShadowSize.htm)|  Gets or
sets the size of the border shadow along all edges of the box.  
![Public property](../icons/pubproperty.gif)|
[SnapDistance](P_Grasshopper_GUI_Base_GH_SliderBase_SnapDistance.htm)|  Gets
or sets the snap distance in absolute values.  
![Public property](../icons/pubproperty.gif)|
[TextColour](P_Grasshopper_GUI_Base_GH_SliderBase_TextColour.htm)|  Gets or
sets the fill colour for the slider text.  
![Public property](../icons/pubproperty.gif)|
[TextInputHandlerDelegate](P_Grasshopper_GUI_Base_GH_SliderBase_TextInputHandlerDelegate.htm)|
Gets or sets the custom handler for text input. If you do not set a custom
handler the default behaviour will be used.  
![Public property](../icons/pubproperty.gif)|
[TickCount](P_Grasshopper_GUI_Base_GH_SliderBase_TickCount.htm)|  Gets or sets
the number of ticks displayed.  
![Public property](../icons/pubproperty.gif)|
[TickDisplay](P_Grasshopper_GUI_Base_GH_SliderBase_TickDisplay.htm)|  Gets or
sets how the slider ticks are drawn.  
![Public property](../icons/pubproperty.gif)|
[TickFrequency](P_Grasshopper_GUI_Base_GH_SliderBase_TickFrequency.htm)|  Gets
or sets the frequency of large ticks vs small ticks.  
![Public property](../icons/pubproperty.gif)|
[Ticks](P_Grasshopper_GUI_Base_GH_SliderBase_Ticks.htm)|  Gets a list of all
the tick offset x positions.  
![Public property](../icons/pubproperty.gif)|
[Type](P_Grasshopper_GUI_Base_GH_SliderBase_Type.htm)|  Gets or sets the
accuracy type of the slider.  
![Public property](../icons/pubproperty.gif)|
[Value](P_Grasshopper_GUI_Base_GH_SliderBase_Value.htm)|  Gets or sets the
value of the slider.  
![Public property](../icons/pubproperty.gif)|
[ValueF](P_Grasshopper_GUI_Base_GH_SliderBase_ValueF.htm)|  Gets or sets the
value of the slider in single precision.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[FixDomain](M_Grasshopper_GUI_Base_GH_SliderBase_FixDomain.htm)|  Fix the
limits of the slider. Limits will be rounded according to slider type and
accuracy. Also, a minimum range for all types is ensured.  
![Public method](../icons/pubmethod.gif)|
[FixValue](M_Grasshopper_GUI_Base_GH_SliderBase_FixValue.htm)|  Fix the value
of the slider. The value will be rounded according to slider type and
accuracy. Also, the value will be clipped to the limits. Before you call this
function, ensure the limits are set up correctly.  
![Protected method](../icons/protmethod.gif)|
[HandleTextInputAccepted](M_Grasshopper_GUI_Base_GH_SliderBase_HandleTextInputAccepted.htm)|
(Overrides
[GH_TextBoxInputBaseHandleTextInputAccepted(String)](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_HandleTextInputAccepted.htm).)  
![Public method](../icons/pubmethod.gif)|
[HideTextInputBox](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_HideTextInputBox.htm)|
Hides the text-input override form (if it is displayed).  (Inherited from
[GH_TextBoxInputBase](T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm).)  
![Public method](../icons/pubmethod.gif)|
[KeyDown](M_Grasshopper_GUI_Base_GH_SliderBase_KeyDown.htm)|  Respond to a
KeyDown event.  
![Public method](../icons/pubmethod.gif)|
[MouseDown](M_Grasshopper_GUI_Base_GH_SliderBase_MouseDown.htm)|  Respond to
mouse-down events.  
![Public method](../icons/pubmethod.gif)|
[MouseMove](M_Grasshopper_GUI_Base_GH_SliderBase_MouseMove.htm)|  Respond to
mouse-move events.  
![Public method](../icons/pubmethod.gif)|
[MouseUp](M_Grasshopper_GUI_Base_GH_SliderBase_MouseUp.htm)|  Respond to
mouse-up events.  
![Public method](../icons/pubmethod.gif)|
[OnValueChanged](M_Grasshopper_GUI_Base_GH_SliderBase_OnValueChanged.htm)|
Raise the ValueChanged event.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ProcessNumber](M_Grasshopper_GUI_Base_GH_SliderBase_ProcessNumber.htm)|
Process a number using the given slider characteristics.  
![Public method](../icons/pubmethod.gif)|
[Render](M_Grasshopper_GUI_Base_GH_SliderBase_Render.htm)|  Render this slider
into a Graphics context.  
![Public method](../icons/pubmethod.gif)|
[RespondToEnter](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_RespondToEnter.htm)|
(Inherited from
[GH_TextBoxInputBase](T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm).)  
![Public method](../icons/pubmethod.gif)|
[RespondToEscape](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_RespondToEscape.htm)|
(Inherited from
[GH_TextBoxInputBase](T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm).)  
![Public method](../icons/pubmethod.gif)|
[SetSnapRanges](M_Grasshopper_GUI_Base_GH_SliderBase_SetSnapRanges.htm)|
Assign a collection of snap ranges to this slider.  
![Public method](../icons/pubmethod.gif)|
[ShowTextInputBox(Control)](M_Grasshopper_GUI_Base_GH_SliderBase_ShowTextInputBox.htm)|  
![Public method](../icons/pubmethod.gif)| [ShowTextInputBox(Control,
Boolean)](M_Grasshopper_GUI_Base_GH_SliderBase_ShowTextInputBox_1.htm)|  
![Public method](../icons/pubmethod.gif)| [ShowTextInputBox(Control, Boolean,
Matrix)](M_Grasshopper_GUI_Base_GH_SliderBase_ShowTextInputBox_2.htm)|  
![Public method](../icons/pubmethod.gif)| [ShowTextInputBox(Control, String,
Boolean)](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_ShowTextInputBox.htm)|
Display a floating text-box on top of the owner control.  (Inherited from
[GH_TextBoxInputBase](T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm).)  
![Public method](../icons/pubmethod.gif)| [ShowTextInputBox(Control, Boolean,
Matrix, String)](M_Grasshopper_GUI_Base_GH_SliderBase_ShowTextInputBox_3.htm)|  
![Public method](../icons/pubmethod.gif)| [ShowTextInputBox(Control, String,
Boolean,
Boolean)](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_ShowTextInputBox_1.htm)|
Display a floating text-box on top of the owner control.  (Inherited from
[GH_TextBoxInputBase](T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm).)  
![Public method](../icons/pubmethod.gif)| [ShowTextInputBox(Control, String,
Boolean, Boolean,
Matrix)](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_ShowTextInputBox_2.htm)|
Display a floating text-box on top of the owner control.  (Inherited from
[GH_TextBoxInputBase](T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm).)  
Top

![](../icons/SectionExpanded.png)Events

| Name| Description  
---|---|---  
![Public event](../icons/pubevent.gif)|
[ValueChanged](E_Grasshopper_GUI_Base_GH_SliderBase_ValueChanged.htm)|  Raised
whenever the value of this slider is changed due to User-Interface methods.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Base Namespace](N_Grasshopper_GUI_Base.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

