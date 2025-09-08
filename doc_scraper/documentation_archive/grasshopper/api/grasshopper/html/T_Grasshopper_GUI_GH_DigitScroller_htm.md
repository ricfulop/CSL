---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_GH_DigitScroller.htm
scraped_at: 2025-09-08T16:12:24.259696
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH_DigitScroller Class](../html/T_Grasshopper_GUI_GH_DigitScroller.htm
"GH_DigitScroller Class")

[GH_DigitScroller Constructor
](../html/M_Grasshopper_GUI_GH_DigitScroller__ctor.htm "GH_DigitScroller
Constructor ")

[GH_DigitScroller
Properties](../html/Properties_T_Grasshopper_GUI_GH_DigitScroller.htm
"GH_DigitScroller Properties")

[GH_DigitScroller
Methods](../html/Methods_T_Grasshopper_GUI_GH_DigitScroller.htm
"GH_DigitScroller Methods")

[GH_DigitScroller
Events](../html/Events_T_Grasshopper_GUI_GH_DigitScroller.htm
"GH_DigitScroller Events")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_DigitScroller Class  
  
---  
  
Provides the standard Grasshopper Digit scroller as a winforms Control.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[SystemMarshalByRefObject](https://docs.microsoft.com/dotnet/api/system.marshalbyrefobject)  
[System.ComponentModelComponent](https://docs.microsoft.com/dotnet/api/system.componentmodel.component)  
[System.Windows.FormsControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.control)  
[System.Windows.FormsScrollableControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol)  
[System.Windows.FormsContainerControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.containercontrol)  
[System.Windows.FormsUserControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.usercontrol)  
GH_TextInputBaseControl  
Grasshopper.GUIGH_DigitScroller  

**Namespace:** [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_DigitScroller : GH_TextInputBaseControl
    
    
    Public Class GH_DigitScroller
    	Inherits GH_TextInputBaseControl

The GH_DigitScroller type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_DigitScroller](M_Grasshopper_GUI_GH_DigitScroller__ctor.htm)| Initializes
a new instance of the GH_DigitScroller class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[AllowRadixDrag](P_Grasshopper_GUI_GH_DigitScroller_AllowRadixDrag.htm)|  Gets
or sets whether the radix symbol can be dragged.  
![Public property](../icons/pubproperty.gif)|
[AllowTextInput](P_Grasshopper_GUI_GH_DigitScroller_AllowTextInput.htm)|  Gets
or sets whether the control accepts text input override.  
![Public property](../icons/pubproperty.gif)|
[Amplify](P_Grasshopper_GUI_GH_DigitScroller_Amplify.htm)|  Gets or sets
whether vertical mouse movement ought to be amplified.  
![Public property](../icons/pubproperty.gif)|
[DecimalPlaces](P_Grasshopper_GUI_GH_DigitScroller_DecimalPlaces.htm)|  Gets
or sets the number of decimal places.  
![Public property](../icons/pubproperty.gif)|
[DigitAlign](P_Grasshopper_GUI_GH_DigitScroller_DigitAlign.htm)|  Gets or sets
the digit align mode  
![Public property](../icons/pubproperty.gif)|
[Digits](P_Grasshopper_GUI_GH_DigitScroller_Digits.htm)|  Gets or sets the
number of digits displayed in the scroller.  
![Public property](../icons/pubproperty.gif)|
[DigitScroller](P_Grasshopper_GUI_GH_DigitScroller_DigitScroller.htm)|  Gets
the internal scroller object.  
![Public property](../icons/pubproperty.gif)|
[Epsilon](P_Grasshopper_GUI_GH_DigitScroller_Epsilon.htm)|  Gets the smallest
possible change with the current settings.  
![Public property](../icons/pubproperty.gif)|
[MaximumValue](P_Grasshopper_GUI_GH_DigitScroller_MaximumValue.htm)|  Gets or
sets the upper bound of the scroll value.  
![Public property](../icons/pubproperty.gif)|
[MinimumValue](P_Grasshopper_GUI_GH_DigitScroller_MinimumValue.htm)|  Gets or
sets the lower bound of the scroll value.  
![Public property](../icons/pubproperty.gif)|
[Prefix](P_Grasshopper_GUI_GH_DigitScroller_Prefix.htm)|  Gets or sets the
prefix text  
![Public property](../icons/pubproperty.gif)|
[Radix](P_Grasshopper_GUI_GH_DigitScroller_Radix.htm)|  Gets or sets the radix
point index.  
![Public property](../icons/pubproperty.gif)|
[Suffix](P_Grasshopper_GUI_GH_DigitScroller_Suffix.htm)|  Gets or sets the
prefix text  
![Public property](../icons/pubproperty.gif)|
[Value](P_Grasshopper_GUI_GH_DigitScroller_Value.htm)|  Gets or sets the value
of this scroller.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[Input_Assign](M_Grasshopper_GUI_GH_DigitScroller_Input_Assign.htm)|
(Overrides GH_TextInputBaseControl.Input_Assign(String).)  
![Protected method](../icons/protmethod.gif)|
[Input_Parse](M_Grasshopper_GUI_GH_DigitScroller_Input_Parse.htm)|  (Overrides
GH_TextInputBaseControl.Input_Parse(String).)  
![Protected method](../icons/protmethod.gif)|
[Input_Supply](M_Grasshopper_GUI_GH_DigitScroller_Input_Supply.htm)|
(Overrides GH_TextInputBaseControl.Input_Supply.)  
![Protected method](../icons/protmethod.gif)|
[OnPaint](M_Grasshopper_GUI_GH_DigitScroller_OnPaint.htm)|  (Overrides
[ControlOnPaint(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.control.onpaint#system-
windows-forms-control-onpaint\(system-windows-forms-painteventargs\)).)  
![Protected method](../icons/protmethod.gif)|
[OnPaintBackground](M_Grasshopper_GUI_GH_DigitScroller_OnPaintBackground.htm)|
(Overrides
[ScrollableControlOnPaintBackground(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol.onpaintbackground#system-
windows-forms-scrollablecontrol-onpaintbackground\(system-windows-forms-
painteventargs\)).)  
Top

![](../icons/SectionExpanded.png)Events

| Name| Description  
---|---|---  
![Public event](../icons/pubevent.gif)|
[ValueChanged](E_Grasshopper_GUI_GH_DigitScroller_ValueChanged.htm)|  
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

