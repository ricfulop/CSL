---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_GH_ColourPicker.htm
scraped_at: 2025-09-08T16:12:18.203414
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH_ColourPicker Class](../html/T_Grasshopper_GUI_GH_ColourPicker.htm
"GH_ColourPicker Class")

[GH_ColourPicker Constructor
](../html/M_Grasshopper_GUI_GH_ColourPicker__ctor.htm "GH_ColourPicker
Constructor ")

[GH_ColourPicker
Properties](../html/Properties_T_Grasshopper_GUI_GH_ColourPicker.htm
"GH_ColourPicker Properties")

[GH_ColourPicker
Methods](../html/Methods_T_Grasshopper_GUI_GH_ColourPicker.htm
"GH_ColourPicker Methods")

[GH_ColourPicker Events](../html/Events_T_Grasshopper_GUI_GH_ColourPicker.htm
"GH_ColourPicker Events")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_ColourPicker Class  
  
---  
  
Provides the standard Grasshopper Colour picker as a winforms Control.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[SystemMarshalByRefObject](https://docs.microsoft.com/dotnet/api/system.marshalbyrefobject)  
[System.ComponentModelComponent](https://docs.microsoft.com/dotnet/api/system.componentmodel.component)  
[System.Windows.FormsControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.control)  
[System.Windows.FormsScrollableControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol)  
[System.Windows.FormsContainerControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.containercontrol)  
[System.Windows.FormsUserControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.usercontrol)  
Grasshopper.GUIGH_ColourPicker  

**Namespace:** [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_ColourPicker : UserControl
    
    
    Public Class GH_ColourPicker
    	Inherits UserControl

The GH_ColourPicker type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_ColourPicker](M_Grasshopper_GUI_GH_ColourPicker__ctor.htm)| Initializes a
new instance of the GH_ColourPicker class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[AllowNumericInput](P_Grasshopper_GUI_GH_ColourPicker_AllowNumericInput.htm)|
Gets or sets whether this colour picker pops up a textbox on channel slider
double clicks.  
![Public property](../icons/pubproperty.gif)|
[Colour](P_Grasshopper_GUI_GH_ColourPicker_Colour.htm)|  Gets or sets the
colour currently specified in the picker.  
![Public property](../icons/pubproperty.gif)|
[DesiredHeight](P_Grasshopper_GUI_GH_ColourPicker_DesiredHeight.htm)|  Gets
the ideal height for this control given the current width and UI settings.  
![Public property](../icons/pubproperty.gif)|
[ShowAlphaSlider](P_Grasshopper_GUI_GH_ColourPicker_ShowAlphaSlider.htm)|
Gets or sets whether the alpha channel slider is included.  
![Public property](../icons/pubproperty.gif)|
[ShowChannelSliders](P_Grasshopper_GUI_GH_ColourPicker_ShowChannelSliders.htm)|
Gets or sets whether the channel sliders are included.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[Dispose](M_Grasshopper_GUI_GH_ColourPicker_Dispose.htm)| Releases the
unmanaged resources used by the GH_ColourPicker and optionally releases the
managed resources (Overrides
[ContainerControlDispose(Boolean)](https://docs.microsoft.com/dotnet/api/system.windows.forms.containercontrol.dispose#system-
windows-forms-containercontrol-dispose\(system-boolean\)).)  
![Protected method](../icons/protmethod.gif)|
[OnPaint](M_Grasshopper_GUI_GH_ColourPicker_OnPaint.htm)|  (Overrides
[ControlOnPaint(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.control.onpaint#system-
windows-forms-control-onpaint\(system-windows-forms-painteventargs\)).)  
![Protected method](../icons/protmethod.gif)|
[OnPaintBackground](M_Grasshopper_GUI_GH_ColourPicker_OnPaintBackground.htm)|
(Overrides
[ScrollableControlOnPaintBackground(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol.onpaintbackground#system-
windows-forms-scrollablecontrol-onpaintbackground\(system-windows-forms-
painteventargs\)).)  
Top

![](../icons/SectionExpanded.png)Events

| Name| Description  
---|---|---  
![Public event](../icons/pubevent.gif)|
[ColourChanged](E_Grasshopper_GUI_GH_ColourPicker_ColourChanged.htm)|  Raised
whenever the value of the slider is changed via GUI interaction.  
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

