---
url: https://developer.rhino3d.com/api/grasshopper/html/N_Grasshopper_GUI_Base.htm#!
scraped_at: 2025-09-08T16:13:30.511263
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Base](../html/N_Grasshopper_GUI_Base.htm
"Grasshopper.GUI.Base")

[GH_ColourCube Class](../html/T_Grasshopper_GUI_Base_GH_ColourCube.htm
"GH_ColourCube Class")

[GH_ColourPickerBase
Class](../html/T_Grasshopper_GUI_Base_GH_ColourPickerBase.htm
"GH_ColourPickerBase Class")

[GH_ColourPickerBase.ColorChangedEventHandler
Delegate](../html/T_Grasshopper_GUI_Base_GH_ColourPickerBase_ColorChangedEventHandler.htm
"GH_ColourPickerBase.ColorChangedEventHandler Delegate")

[GH_ColourPickerBase.InvalidatedEventHandler
Delegate](../html/T_Grasshopper_GUI_Base_GH_ColourPickerBase_InvalidatedEventHandler.htm
"GH_ColourPickerBase.InvalidatedEventHandler Delegate")

[GH_ColourPickerEventArgs
Class](../html/T_Grasshopper_GUI_Base_GH_ColourPickerEventArgs.htm
"GH_ColourPickerEventArgs Class")

[GH_ColourSpace Enumeration](../html/T_Grasshopper_GUI_Base_GH_ColourSpace.htm
"GH_ColourSpace Enumeration")

[GH_DigitAlign Enumeration](../html/T_Grasshopper_GUI_Base_GH_DigitAlign.htm
"GH_DigitAlign Enumeration")

[GH_DigitNumber Class](../html/T_Grasshopper_GUI_Base_GH_DigitNumber.htm
"GH_DigitNumber Class")

[GH_DigitScrollerBase
Class](../html/T_Grasshopper_GUI_Base_GH_DigitScrollerBase.htm
"GH_DigitScrollerBase Class")

[GH_DigitScrollerBase.GH_MouseAction
Enumeration](../html/T_Grasshopper_GUI_Base_GH_DigitScrollerBase_GH_MouseAction.htm
"GH_DigitScrollerBase.GH_MouseAction Enumeration")

[GH_DigitScrollerBase.InvalidatedEventHandler
Delegate](../html/T_Grasshopper_GUI_Base_GH_DigitScrollerBase_InvalidatedEventHandler.htm
"GH_DigitScrollerBase.InvalidatedEventHandler Delegate")

[GH_DigitScrollerBase.ValueChangedEventHandler
Delegate](../html/T_Grasshopper_GUI_Base_GH_DigitScrollerBase_ValueChangedEventHandler.htm
"GH_DigitScrollerBase.ValueChangedEventHandler Delegate")

[GH_DigitScrollerEventArgs
Class](../html/T_Grasshopper_GUI_Base_GH_DigitScrollerEventArgs.htm
"GH_DigitScrollerEventArgs Class")

[GH_ScrollBarVerticalBase
Class](../html/T_Grasshopper_GUI_Base_GH_ScrollBarVerticalBase.htm
"GH_ScrollBarVerticalBase Class")

[GH_SliderAccuracy
Enumeration](../html/T_Grasshopper_GUI_Base_GH_SliderAccuracy.htm
"GH_SliderAccuracy Enumeration")

[GH_SliderBase Class](../html/T_Grasshopper_GUI_Base_GH_SliderBase.htm
"GH_SliderBase Class")

[GH_SliderBase.DrawSliderChannel
Delegate](../html/T_Grasshopper_GUI_Base_GH_SliderBase_DrawSliderChannel.htm
"GH_SliderBase.DrawSliderChannel Delegate")

[GH_SliderBase.TextInputHandler
Delegate](../html/T_Grasshopper_GUI_Base_GH_SliderBase_TextInputHandler.htm
"GH_SliderBase.TextInputHandler Delegate")

[GH_SliderBase.ValueChangedEventHandler
Delegate](../html/T_Grasshopper_GUI_Base_GH_SliderBase_ValueChangedEventHandler.htm
"GH_SliderBase.ValueChangedEventHandler Delegate")

[GH_SliderEventArgs
Class](../html/T_Grasshopper_GUI_Base_GH_SliderEventArgs.htm
"GH_SliderEventArgs Class")

[GH_SliderGripDisplay
Enumeration](../html/T_Grasshopper_GUI_Base_GH_SliderGripDisplay.htm
"GH_SliderGripDisplay Enumeration")

[GH_SliderRailDisplay
Enumeration](../html/T_Grasshopper_GUI_Base_GH_SliderRailDisplay.htm
"GH_SliderRailDisplay Enumeration")

[GH_SliderTickDisplay
Enumeration](../html/T_Grasshopper_GUI_Base_GH_SliderTickDisplay.htm
"GH_SliderTickDisplay Enumeration")

[GH_TextBoxInputBase
Class](../html/T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm
"GH_TextBoxInputBase Class")

[SliderSnapRange Structure](../html/T_Grasshopper_GUI_Base_SliderSnapRange.htm
"SliderSnapRange Structure")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# Grasshopper.GUI.Base Namespace  
  
---  
  
This namespace contains general purpose UI elements that have been divorced
from winforms Control handles. This allows them to be rendered on screen as
part of a larger constellation of UI elements. There are dedicated winforms
control implementations of all the elements in this namespace in the
Grasshopper.GUI namespace.

![](../icons/SectionExpanded.png)Classes

| Class| Description  
---|---|---  
![Public class](../icons/pubclass.gif)|
[GH_ColourCube](T_Grasshopper_GUI_Base_GH_ColourCube.htm)|  Maintains a
collection of graphical shapes and coordinates that specify important features
of the Colour Space Cube graphics.  
![Public class](../icons/pubclass.gif)|
[GH_ColourPickerBase](T_Grasshopper_GUI_Base_GH_ColourPickerBase.htm)|
Provides Colour picker GUI not tied to a control-handle.  
![Public class](../icons/pubclass.gif)|
[GH_ColourPickerEventArgs](T_Grasshopper_GUI_Base_GH_ColourPickerEventArgs.htm)|
Arguments passed via GH_SliderBase.ValueChanged events.  
![Public class](../icons/pubclass.gif)|
[GH_DigitNumber](T_Grasshopper_GUI_Base_GH_DigitNumber.htm)|  Maintains and
provides functionality for evaluating and modifying numbers as used in the
GH_DigitScrollerBase control.  
![Public class](../icons/pubclass.gif)|
[GH_DigitScrollerBase](T_Grasshopper_GUI_Base_GH_DigitScrollerBase.htm)|
Provides Numeric digit scrolling GUI not tied to a control-handle.  
![Public class](../icons/pubclass.gif)|
[GH_DigitScrollerEventArgs](T_Grasshopper_GUI_Base_GH_DigitScrollerEventArgs.htm)|
Arguments passed via GH_digitScrollerBase.ValueChanged events.  
![Public class](../icons/pubclass.gif)|
[GH_ScrollBarVerticalBase](T_Grasshopper_GUI_Base_GH_ScrollBarVerticalBase.htm)|
Provides basic vertical scroll bar logic.  
![Public class](../icons/pubclass.gif)|
[GH_SliderBase](T_Grasshopper_GUI_Base_GH_SliderBase.htm)|  Provides Numeric
slider GUI not tied to a control-handle.  
![Public class](../icons/pubclass.gif)|
[GH_SliderEventArgs](T_Grasshopper_GUI_Base_GH_SliderEventArgs.htm)|
Arguments passed via GH_SliderBase.ValueChanged events.  
![Public class](../icons/pubclass.gif)|
[GH_TextBoxInputBase](T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm)|  
  
![](../icons/SectionExpanded.png)Structures

| Structure| Description  
---|---|---  
![Public structure](../icons/pubstructure.gif)|
[SliderSnapRange](T_Grasshopper_GUI_Base_SliderSnapRange.htm)|  Represents a
snap range on a slider.  
  
![](../icons/SectionExpanded.png)Delegates

| Delegate| Description  
---|---|---  
![Public delegate](../icons/pubdelegate.gif)|
[GH_ColourPickerBaseColorChangedEventHandler](T_Grasshopper_GUI_Base_GH_ColourPickerBase_ColorChangedEventHandler.htm)|  
![Public delegate](../icons/pubdelegate.gif)|
[GH_ColourPickerBaseInvalidatedEventHandler](T_Grasshopper_GUI_Base_GH_ColourPickerBase_InvalidatedEventHandler.htm)|  
![Public delegate](../icons/pubdelegate.gif)|
[GH_DigitScrollerBaseInvalidatedEventHandler](T_Grasshopper_GUI_Base_GH_DigitScrollerBase_InvalidatedEventHandler.htm)|  
![Public delegate](../icons/pubdelegate.gif)|
[GH_DigitScrollerBaseValueChangedEventHandler](T_Grasshopper_GUI_Base_GH_DigitScrollerBase_ValueChangedEventHandler.htm)|  
![Public delegate](../icons/pubdelegate.gif)|
[GH_SliderBaseDrawSliderChannel](T_Grasshopper_GUI_Base_GH_SliderBase_DrawSliderChannel.htm)|
This delegate is used to intervene in the slider drawing process.  
![Public delegate](../icons/pubdelegate.gif)|
[GH_SliderBaseTextInputHandler](T_Grasshopper_GUI_Base_GH_SliderBase_TextInputHandler.htm)|
Delegate used during Text Input handling.  
![Public delegate](../icons/pubdelegate.gif)|
[GH_SliderBaseValueChangedEventHandler](T_Grasshopper_GUI_Base_GH_SliderBase_ValueChangedEventHandler.htm)|  
  
![](../icons/SectionExpanded.png)Enumerations

| Enumeration| Description  
---|---|---  
![Public enumeration](../icons/pubenumeration.gif)|
[GH_ColourSpace](T_Grasshopper_GUI_Base_GH_ColourSpace.htm)|  Enumerates the
different colour spaces supported by the GH_ColourPickerBase class.  
![Public enumeration](../icons/pubenumeration.gif)|
[GH_DigitAlign](T_Grasshopper_GUI_Base_GH_DigitAlign.htm)|  Enumerates the
possible alignments for digits inside the GH_DigitScroller control.  
![Public enumeration](../icons/pubenumeration.gif)|
[GH_DigitScrollerBaseGH_MouseAction](T_Grasshopper_GUI_Base_GH_DigitScrollerBase_GH_MouseAction.htm)|
Enumerates the possible actions due to mouse-down mouse-move events.  
![Public enumeration](../icons/pubenumeration.gif)|
[GH_SliderAccuracy](T_Grasshopper_GUI_Base_GH_SliderAccuracy.htm)|  Enumerates
the possible numeric slider accuracies.  
![Public enumeration](../icons/pubenumeration.gif)|
[GH_SliderGripDisplay](T_Grasshopper_GUI_Base_GH_SliderGripDisplay.htm)|
Enumerates the possible slider grip displays.  
![Public enumeration](../icons/pubenumeration.gif)|
[GH_SliderRailDisplay](T_Grasshopper_GUI_Base_GH_SliderRailDisplay.htm)|
Enumerates the possible slider rail displays.  
![Public enumeration](../icons/pubenumeration.gif)|
[GH_SliderTickDisplay](T_Grasshopper_GUI_Base_GH_SliderTickDisplay.htm)|
Enumerates the possible slider tick displays.  
  
Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

