---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Base_GH_ColourPickerBase.htm
scraped_at: 2025-09-08T16:13:32.550364
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Base](../html/N_Grasshopper_GUI_Base.htm
"Grasshopper.GUI.Base")

[GH_ColourPickerBase
Class](../html/T_Grasshopper_GUI_Base_GH_ColourPickerBase.htm
"GH_ColourPickerBase Class")

[GH_ColourPickerBase Constructor
](../html/M_Grasshopper_GUI_Base_GH_ColourPickerBase__ctor.htm
"GH_ColourPickerBase Constructor ")

[GH_ColourPickerBase
Properties](../html/Properties_T_Grasshopper_GUI_Base_GH_ColourPickerBase.htm
"GH_ColourPickerBase Properties")

[GH_ColourPickerBase
Methods](../html/Methods_T_Grasshopper_GUI_Base_GH_ColourPickerBase.htm
"GH_ColourPickerBase Methods")

[GH_ColourPickerBase
Events](../html/Events_T_Grasshopper_GUI_Base_GH_ColourPickerBase.htm
"GH_ColourPickerBase Events")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_ColourPickerBase Class  
  
---  
  
Provides Colour picker GUI not tied to a control-handle.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.GUI.BaseGH_ColourPickerBase  

**Namespace:** [Grasshopper.GUI.Base](N_Grasshopper_GUI_Base.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_ColourPickerBase
    
    
    Public Class GH_ColourPickerBase

The GH_ColourPickerBase type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_ColourPickerBase](M_Grasshopper_GUI_Base_GH_ColourPickerBase__ctor.htm)|
Create a new instance of the Colour Picker base control. This constructor
assigns the default Colour space model and involves a call to the Grasshopper
core settings server. You must call SetupColourPicker() prior to rendering
this control on screen.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[AutoSize](P_Grasshopper_GUI_Base_GH_ColourPickerBase_AutoSize.htm)|  Gets or
sets a value indicating whether the width and height of the Bounds are
adjusted to fit the UI.  
![Public property](../icons/pubproperty.gif)|
[BackColour](P_Grasshopper_GUI_Base_GH_ColourPickerBase_BackColour.htm)|  Gets
or sets the background colour of the picker.  
![Public property](../icons/pubproperty.gif)|
[BaseColour](P_Grasshopper_GUI_Base_GH_ColourPickerBase_BaseColour.htm)|  Gets
the original base colour for this picker. Use SetupColourPicker to assign this
colour.  
![Public property](../icons/pubproperty.gif)|
[Bounds](P_Grasshopper_GUI_Base_GH_ColourPickerBase_Bounds.htm)|  Gets or sets
the Bounds for this control.  
![Public property](../icons/pubproperty.gif)|
[ColourSpace](P_Grasshopper_GUI_Base_GH_ColourPickerBase_ColourSpace.htm)|
Gets the Colour space mode used in this picker.  
![Public property](../icons/pubproperty.gif)|
[DesiredHeight](P_Grasshopper_GUI_Base_GH_ColourPickerBase_DesiredHeight.htm)|
Gets the ideal height for this colour picker given it's width and UI settings.  
![Public property](../icons/pubproperty.gif)|
[DrawAlphaSlider](P_Grasshopper_GUI_Base_GH_ColourPickerBase_DrawAlphaSlider.htm)|
Gets or sets whether or not the alpha slider is included in the UI.  
![Public property](../icons/pubproperty.gif)|
[DrawBackground](P_Grasshopper_GUI_Base_GH_ColourPickerBase_DrawBackground.htm)|
Gets or sets whether the background of the picker is drawn.  
![Public property](../icons/pubproperty.gif)|
[DrawChannelSliders](P_Grasshopper_GUI_Base_GH_ColourPickerBase_DrawChannelSliders.htm)|
Gets or sets whether or not the three basic channel sliders are included in
the UI.  
![Public property](../icons/pubproperty.gif)|
[DropperPreviewBox](P_Grasshopper_GUI_Base_GH_ColourPickerBase_DropperPreviewBox.htm)|
Gets the rectangle in which the eye-dropped preview will be drawn.  
![Public property](../icons/pubproperty.gif)|
[Font](P_Grasshopper_GUI_Base_GH_ColourPickerBase_Font.htm)|  Gets or sets the
Font used in this Colour Picker. Do not Dispose the Font returned by this
property.  
![Public property](../icons/pubproperty.gif)|
[IsTextInput](P_Grasshopper_GUI_Base_GH_ColourPickerBase_IsTextInput.htm)|
Gets whether any of the slider is currently displaying a text input box.  
![Public property](../icons/pubproperty.gif)|
[Padding](P_Grasshopper_GUI_Base_GH_ColourPickerBase_Padding.htm)|  Gets or
sets the Padding for this control.  
![Public property](../icons/pubproperty.gif)|
[PickColour](P_Grasshopper_GUI_Base_GH_ColourPickerBase_PickColour.htm)|  Gets
the picked colour.  
![Public property](../icons/pubproperty.gif)|
[SRCSpaceBox](P_Grasshopper_GUI_Base_GH_ColourPickerBase_SRCSpaceBox.htm)|
Gets the rectangle containing the eye-dropper function.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Invalidate](M_Grasshopper_GUI_Base_GH_ColourPickerBase_Invalidate.htm)|
Raise the Invalidated event.  
![Public method](../icons/pubmethod.gif)|
[MouseClick](M_Grasshopper_GUI_Base_GH_ColourPickerBase_MouseClick.htm)|
Respond to mouse-click events.  
![Public method](../icons/pubmethod.gif)|
[MouseDoubleClick](M_Grasshopper_GUI_Base_GH_ColourPickerBase_MouseDoubleClick.htm)|
Respond to mouse-doubleclick events.  
![Public method](../icons/pubmethod.gif)|
[MouseDown](M_Grasshopper_GUI_Base_GH_ColourPickerBase_MouseDown.htm)|
Respond to mouse-down events.  
![Public method](../icons/pubmethod.gif)|
[MouseMove](M_Grasshopper_GUI_Base_GH_ColourPickerBase_MouseMove.htm)|
Respond to mouse-move events.  
![Public method](../icons/pubmethod.gif)|
[MouseUp](M_Grasshopper_GUI_Base_GH_ColourPickerBase_MouseUp.htm)|  Respond to
mouse-up events.  
![Public method](../icons/pubmethod.gif)|
[OnColorChanged](M_Grasshopper_GUI_Base_GH_ColourPickerBase_OnColorChanged.htm)|
Raise the ColorChanged event.  
![Public method](../icons/pubmethod.gif)|
[Render](M_Grasshopper_GUI_Base_GH_ColourPickerBase_Render.htm)|  Render this
slider into a Graphics context.  
![Public method](../icons/pubmethod.gif)|
[RespondToEnter](M_Grasshopper_GUI_Base_GH_ColourPickerBase_RespondToEnter.htm)|  
![Public method](../icons/pubmethod.gif)|
[RespondToEscape](M_Grasshopper_GUI_Base_GH_ColourPickerBase_RespondToEscape.htm)|  
![Public method](../icons/pubmethod.gif)|
[SetUiScaling](M_Grasshopper_GUI_Base_GH_ColourPickerBase_SetUiScaling.htm)|  
![Public method](../icons/pubmethod.gif)| [SetupColourPicker(Color, Point4d,
GH_ColourSpace)](M_Grasshopper_GUI_Base_GH_ColourPickerBase_SetupColourPicker.htm)|
Setup all UI elements.  
![Public method](../icons/pubmethod.gif)| [SetupColourPicker(Color, Color,
GH_ColourSpace)](M_Grasshopper_GUI_Base_GH_ColourPickerBase_SetupColourPicker_1.htm)|
Setup all UI elements.  
Top

![](../icons/SectionExpanded.png)Events

| Name| Description  
---|---|---  
![Public event](../icons/pubevent.gif)|
[ColorChanged](E_Grasshopper_GUI_Base_GH_ColourPickerBase_ColorChanged.htm)|
Raised whenever the color of this picker is changed due to User-Interface
methods.  
![Public event](../icons/pubevent.gif)|
[Invalidated](E_Grasshopper_GUI_Base_GH_ColourPickerBase_Invalidated.htm)|
Raised whenever a redraw is required.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Base Namespace](N_Grasshopper_GUI_Base.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

