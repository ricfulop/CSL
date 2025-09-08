---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Base_GH_DigitScrollerBase.htm
scraped_at: 2025-09-08T16:13:39.587084
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Base](../html/N_Grasshopper_GUI_Base.htm
"Grasshopper.GUI.Base")

[GH_DigitScrollerBase
Class](../html/T_Grasshopper_GUI_Base_GH_DigitScrollerBase.htm
"GH_DigitScrollerBase Class")

[GH_DigitScrollerBase Constructor
](../html/M_Grasshopper_GUI_Base_GH_DigitScrollerBase__ctor.htm
"GH_DigitScrollerBase Constructor ")

[GH_DigitScrollerBase
Properties](../html/Properties_T_Grasshopper_GUI_Base_GH_DigitScrollerBase.htm
"GH_DigitScrollerBase Properties")

[GH_DigitScrollerBase
Methods](../html/Methods_T_Grasshopper_GUI_Base_GH_DigitScrollerBase.htm
"GH_DigitScrollerBase Methods")

[GH_DigitScrollerBase
Events](../html/Events_T_Grasshopper_GUI_Base_GH_DigitScrollerBase.htm
"GH_DigitScrollerBase Events")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_DigitScrollerBase Class  
  
---  
  
Provides Numeric digit scrolling GUI not tied to a control-handle.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.GUI.BaseGH_TextBoxInputBase](T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm)  
Grasshopper.GUI.BaseGH_DigitScrollerBase  

**Namespace:** [Grasshopper.GUI.Base](N_Grasshopper_GUI_Base.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_DigitScrollerBase : GH_TextBoxInputBase
    
    
    Public Class GH_DigitScrollerBase
    	Inherits GH_TextBoxInputBase

The GH_DigitScrollerBase type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_DigitScrollerBase](M_Grasshopper_GUI_Base_GH_DigitScrollerBase__ctor.htm)|
Initializes a new instance of the GH_DigitScrollerBase class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[AllowRadixDrag](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_AllowRadixDrag.htm)|
Gets or sets a value indicating whether the radix is allowed to be dragged
around.  
![Public property](../icons/pubproperty.gif)|
[AllowTextInput](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_AllowTextInput.htm)|
Gets or sets whether text input is allowed by double click.  
![Public property](../icons/pubproperty.gif)|
[AmplifyMotion](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_AmplifyMotion.htm)|
Gets or sets a value indicating whether vertical mouse drags should be
amplified as the mouse moves further and further.  
![Public property](../icons/pubproperty.gif)|
[BackgroundGradient](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_BackgroundGradient.htm)|
Gets or sets the background Gradient. If the gradient is not null, it
overrides the background colours.  
![Public property](../icons/pubproperty.gif)|
[BottomColour](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_BottomColour.htm)|
Gets or sets the colour used along the bottom edge of the control.  
![Public property](../icons/pubproperty.gif)|
[Bounds](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_Bounds.htm)|  Gets or
sets the Bounds for this scroller.  (Overrides GH_TextBoxInputBase.Bounds.)  
![Public property](../icons/pubproperty.gif)|
[DecimalPlaces](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_DecimalPlaces.htm)|
Gets or sets the number of decimal places available in this scroller. Unlike
Radix, this property maintains the decimal position of the value represented
by this scroller.  
![Public property](../icons/pubproperty.gif)|
[DigitAlign](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_DigitAlign.htm)|
Gets or sets the digit align mode.  
![Public property](../icons/pubproperty.gif)|
[Digits](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_Digits.htm)|  Gets or
sets the number of digits available in this scroller.  
![Public property](../icons/pubproperty.gif)|
[DrawBackground](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_DrawBackground.htm)|
Gets or sets whether the background is drawn in this control.  
![Public property](../icons/pubproperty.gif)|
[DrawBorder](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_DrawBorder.htm)|
Gets or sets whether the border is drawn in this control.  
![Public property](../icons/pubproperty.gif)|
[DrawShadows](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_DrawShadows.htm)|
Gets or sets whether shadows are drawn in this control.  
![Public property](../icons/pubproperty.gif)|
[EdgeColour](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_EdgeColour.htm)|
Gets or sets the edge colour of the control.  
![Public property](../icons/pubproperty.gif)|
[Epsilon](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_Epsilon.htm)|  Gets the
smallest possible change in the value.  
![Public property](../icons/pubproperty.gif)|
[Font](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_Font.htm)|  Gets or sets
the Font for this scroller.  (Overrides
[GH_TextBoxInputBaseFont](P_Grasshopper_GUI_Base_GH_TextBoxInputBase_Font.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsTextInput](P_Grasshopper_GUI_Base_GH_TextBoxInputBase_IsTextInput.htm)|
Gets whether the text input box is currently on screen.  (Inherited from
[GH_TextBoxInputBase](T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm).)  
![Public property](../icons/pubproperty.gif)|
[MaximumValue](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_MaximumValue.htm)|
Gets or sets the upper bound of the scroll value.  
![Public property](../icons/pubproperty.gif)|
[MinimumValue](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_MinimumValue.htm)|
Gets or sets the lower bound of the scroll value.  
![Public property](../icons/pubproperty.gif)|
[Prefix](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_Prefix.htm)|  Gets or
sets the prefix text to be displayed on the scroller.  
![Public property](../icons/pubproperty.gif)|
[PrefixBox](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_PrefixBox.htm)|  Gets
the box containing the prefix string. If there is no prefix the PrefixBox will
be Rectangle.Empty  
![Public property](../icons/pubproperty.gif)|
[Radix](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_Radix.htm)|  Gets or sets
the radix index of this scroller.  
![Public property](../icons/pubproperty.gif)|
[RadixBox](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_RadixBox.htm)|  Gets
the Radix box for this control, if there is no radix box, Rectangle.Empty will
be returned.  
![Public property](../icons/pubproperty.gif)|
[RailColour](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_RailColour.htm)|
Gets or sets the colour used for the rail line.  
![Public property](../icons/pubproperty.gif)|
[RaiseEvents](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_RaiseEvents.htm)|
Gets or sets whether this scroller raises the ValueChanged event.  
![Public property](../icons/pubproperty.gif)|
[ScrollBoxes](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_ScrollBoxes.htm)|
Gets all scroll boxes (from left to right) for this control, not including the
radix box.  
![Public property](../icons/pubproperty.gif)|
[ShadowColour](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_ShadowColour.htm)|
Gets or sets the colour used for the shadows.  
![Public property](../icons/pubproperty.gif)|
[ShadowSize](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_ShadowSize.htm)|
Gets or sets the size of the drop shadow along all four edges.  
![Public property](../icons/pubproperty.gif)|
[SignBox](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_SignBox.htm)|  Gets the
Sign box for this control.  
![Public property](../icons/pubproperty.gif)|
[Suffix](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_Suffix.htm)|  Gets or
sets the suffix text to be displayed on the scroller.  
![Public property](../icons/pubproperty.gif)|
[SuffixBox](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_SuffixBox.htm)|  Gets
the box containing the suffix string. If there is no suffix the PrefixBox will
have zero width  
![Public property](../icons/pubproperty.gif)|
[TextColour](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_TextColour.htm)|
Gets or sets the colour used for the text inside the scrolls.  
![Public property](../icons/pubproperty.gif)|
[TopColour](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_TopColour.htm)|  Gets
or sets the colour used along the top edge of the control.  
![Public property](../icons/pubproperty.gif)|
[Value](P_Grasshopper_GUI_Base_GH_DigitScrollerBase_Value.htm)|  Gets or sets
the value displayed in this scroller.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[HandleTextInputAccepted](M_Grasshopper_GUI_Base_GH_DigitScrollerBase_HandleTextInputAccepted.htm)|
(Overrides
[GH_TextBoxInputBaseHandleTextInputAccepted(String)](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_HandleTextInputAccepted.htm).)  
![Public method](../icons/pubmethod.gif)|
[HideTextInputBox](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_HideTextInputBox.htm)|
Hides the text-input override form (if it is displayed).  (Inherited from
[GH_TextBoxInputBase](T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm).)  
![Public method](../icons/pubmethod.gif)|
[MouseDown](M_Grasshopper_GUI_Base_GH_DigitScrollerBase_MouseDown.htm)|
Respond to mouse-down events.  
![Public method](../icons/pubmethod.gif)|
[MouseMove](M_Grasshopper_GUI_Base_GH_DigitScrollerBase_MouseMove.htm)|
Respond to mouse-move events.  
![Public method](../icons/pubmethod.gif)|
[MouseUp](M_Grasshopper_GUI_Base_GH_DigitScrollerBase_MouseUp.htm)|  Respond
to mouse-up events.  
![Public method](../icons/pubmethod.gif)|
[OnInvalidated](M_Grasshopper_GUI_Base_GH_DigitScrollerBase_OnInvalidated.htm)|
Raise the Invalidated event.  
![Public method](../icons/pubmethod.gif)|
[OnValueChanged](M_Grasshopper_GUI_Base_GH_DigitScrollerBase_OnValueChanged.htm)|
Raise the ValueChanged event.  
![Public method](../icons/pubmethod.gif)|
[Render](M_Grasshopper_GUI_Base_GH_DigitScrollerBase_Render.htm)|  Render all
UI elements.  
![Public method](../icons/pubmethod.gif)|
[RespondToEnter](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_RespondToEnter.htm)|
(Inherited from
[GH_TextBoxInputBase](T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm).)  
![Public method](../icons/pubmethod.gif)|
[RespondToEscape](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_RespondToEscape.htm)|
(Inherited from
[GH_TextBoxInputBase](T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm).)  
![Public method](../icons/pubmethod.gif)|
[SetupScroller](M_Grasshopper_GUI_Base_GH_DigitScrollerBase_SetupScroller.htm)|
Set the minimum, maximum and value fields simultaneously.  
![Public method](../icons/pubmethod.gif)|
[ShowTextInputBox(Control)](M_Grasshopper_GUI_Base_GH_DigitScrollerBase_ShowTextInputBox.htm)|  
![Public method](../icons/pubmethod.gif)| [ShowTextInputBox(Control,
Boolean)](M_Grasshopper_GUI_Base_GH_DigitScrollerBase_ShowTextInputBox_1.htm)|  
![Public method](../icons/pubmethod.gif)| [ShowTextInputBox(Control, Boolean,
Matrix)](M_Grasshopper_GUI_Base_GH_DigitScrollerBase_ShowTextInputBox_2.htm)|  
![Public method](../icons/pubmethod.gif)| [ShowTextInputBox(Control, String,
Boolean)](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_ShowTextInputBox.htm)|
Display a floating text-box on top of the owner control.  (Inherited from
[GH_TextBoxInputBase](T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm).)  
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
[Invalidated](E_Grasshopper_GUI_Base_GH_DigitScrollerBase_Invalidated.htm)|
Raised whenever the display of this scroller is changed, but not the value.  
![Public event](../icons/pubevent.gif)|
[ValueChanged](E_Grasshopper_GUI_Base_GH_DigitScrollerBase_ValueChanged.htm)|
Raised whenever the value of this scroller is changed due to User-Interface
methods.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Base Namespace](N_Grasshopper_GUI_Base.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

