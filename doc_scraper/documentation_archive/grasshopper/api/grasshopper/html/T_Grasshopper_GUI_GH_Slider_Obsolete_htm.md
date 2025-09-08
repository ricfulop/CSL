---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_GH_Slider_Obsolete.htm
scraped_at: 2025-09-08T16:13:07.431333
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH_Slider_Obsolete Class](../html/T_Grasshopper_GUI_GH_Slider_Obsolete.htm
"GH_Slider_Obsolete Class")

[GH_Slider_Obsolete Constructor
](../html/M_Grasshopper_GUI_GH_Slider_Obsolete__ctor.htm "GH_Slider_Obsolete
Constructor ")

[GH_Slider_Obsolete
Properties](../html/Properties_T_Grasshopper_GUI_GH_Slider_Obsolete.htm
"GH_Slider_Obsolete Properties")

[GH_Slider_Obsolete
Methods](../html/Methods_T_Grasshopper_GUI_GH_Slider_Obsolete.htm
"GH_Slider_Obsolete Methods")

[GH_Slider_Obsolete
Events](../html/Events_T_Grasshopper_GUI_GH_Slider_Obsolete.htm
"GH_Slider_Obsolete Events")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Slider_Obsolete Class  
  
---  
  
General purpose numeric slider.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[SystemMarshalByRefObject](https://docs.microsoft.com/dotnet/api/system.marshalbyrefobject)  
[System.ComponentModelComponent](https://docs.microsoft.com/dotnet/api/system.componentmodel.component)  
[System.Windows.FormsControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.control)  
[System.Windows.FormsScrollableControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol)  
[System.Windows.FormsContainerControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.containercontrol)  
[System.Windows.FormsUserControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.usercontrol)  
Grasshopper.GUIGH_Slider_Obsolete  

**Namespace:** [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Slider_Obsolete : UserControl
    
    
    Public Class GH_Slider_Obsolete
    	Inherits UserControl

The GH_Slider_Obsolete type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_Slider_Obsolete](M_Grasshopper_GUI_GH_Slider_Obsolete__ctor.htm)|
Initializes a new instance of the GH_Slider_Obsolete class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[DisplayFormat](P_Grasshopper_GUI_GH_Slider_Obsolete_DisplayFormat.htm)|  Gets
or sets the display format fo the slider. This is the formatting that is
applied prior to drawing. The default is {0} which results in a 1:1 display.
Use this to append units or symbols.  
![Public property](../icons/pubproperty.gif)|
[DrawRail](P_Grasshopper_GUI_GH_Slider_Obsolete_DrawRail.htm)|  Gets or sets a
flag that control whether or not grip rails are drawn.  
![Public property](../icons/pubproperty.gif)|
[GripBackColor](P_Grasshopper_GUI_GH_Slider_Obsolete_GripBackColor.htm)|
Background colour of slider grip.  
![Public property](../icons/pubproperty.gif)|
[GripForeColor](P_Grasshopper_GUI_GH_Slider_Obsolete_GripForeColor.htm)|
Foreground colour of slider grip.  
![Public property](../icons/pubproperty.gif)|
[IsIntermediate](P_Grasshopper_GUI_GH_Slider_Obsolete_IsIntermediate.htm)|
Gets the intermediate flag. If True, the user is currently dragging the
slider.  
![Public property](../icons/pubproperty.gif)|
[Max](P_Grasshopper_GUI_GH_Slider_Obsolete_Max.htm)|  Gets or sets the maximum
allowed value.  
![Public property](../icons/pubproperty.gif)|
[Min](P_Grasshopper_GUI_GH_Slider_Obsolete_Min.htm)|  Gets or sets the minimum
allowed value.  
![Public property](../icons/pubproperty.gif)|
[NumericFormat](P_Grasshopper_GUI_GH_Slider_Obsolete_NumericFormat.htm)|  Gets
or sets the numeric format for the slider. This is the formatting that is
applied to the number. The default is #0.00 which results in a two digit
rounding scheme.  
![Public property](../icons/pubproperty.gif)|
[TextInputMode](P_Grasshopper_GUI_GH_Slider_Obsolete_TextInputMode.htm)|  Gets
or sets the Text input mode for this slider.  
![Public property](../icons/pubproperty.gif)|
[TickFrequency](P_Grasshopper_GUI_GH_Slider_Obsolete_TickFrequency.htm)|  Gets
or sets the tick frequency of the slider.  
![Public property](../icons/pubproperty.gif)|
[Value](P_Grasshopper_GUI_GH_Slider_Obsolete_Value.htm)|  Gets or sets the
current value.  
![Public property](../icons/pubproperty.gif)|
[ValueF](P_Grasshopper_GUI_GH_Slider_Obsolete_ValueF.htm)|  Gets or sets the
current value in single-floating-point precision.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[Dispose](M_Grasshopper_GUI_GH_Slider_Obsolete_Dispose.htm)| Releases the
unmanaged resources used by the GH_Slider_Obsolete and optionally releases the
managed resources (Overrides
[ContainerControlDispose(Boolean)](https://docs.microsoft.com/dotnet/api/system.windows.forms.containercontrol.dispose#system-
windows-forms-containercontrol-dispose\(system-boolean\)).)  
![Protected method](../icons/protmethod.gif)|
[OnPaint](M_Grasshopper_GUI_GH_Slider_Obsolete_OnPaint.htm)|  (Overrides
[ControlOnPaint(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.control.onpaint#system-
windows-forms-control-onpaint\(system-windows-forms-painteventargs\)).)  
![Protected method](../icons/protmethod.gif)|
[OnPaintBackground](M_Grasshopper_GUI_GH_Slider_Obsolete_OnPaintBackground.htm)|
(Overrides
[ScrollableControlOnPaintBackground(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol.onpaintbackground#system-
windows-forms-scrollablecontrol-onpaintbackground\(system-windows-forms-
painteventargs\)).)  
![Public method](../icons/pubmethod.gif)|
[OnValueChanged](M_Grasshopper_GUI_GH_Slider_Obsolete_OnValueChanged.htm)|
Raise the ValueChanged event  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[SendMessage](M_Grasshopper_GUI_GH_Slider_Obsolete_SendMessage.htm)|  
Top

![](../icons/SectionExpanded.png)Events

| Name| Description  
---|---|---  
![Public event](../icons/pubevent.gif)|
[ValueChanged](E_Grasshopper_GUI_GH_Slider_Obsolete_ValueChanged.htm)|  Raised
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

