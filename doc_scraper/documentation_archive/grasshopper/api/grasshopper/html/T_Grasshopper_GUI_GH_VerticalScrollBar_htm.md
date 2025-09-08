---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_GH_VerticalScrollBar.htm
scraped_at: 2025-09-08T16:13:17.474364
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH_VerticalScrollBar
Class](../html/T_Grasshopper_GUI_GH_VerticalScrollBar.htm
"GH_VerticalScrollBar Class")

[GH_VerticalScrollBar Constructor
](../html/M_Grasshopper_GUI_GH_VerticalScrollBar__ctor.htm
"GH_VerticalScrollBar Constructor ")

[GH_VerticalScrollBar
Properties](../html/Properties_T_Grasshopper_GUI_GH_VerticalScrollBar.htm
"GH_VerticalScrollBar Properties")

[GH_VerticalScrollBar
Methods](../html/Methods_T_Grasshopper_GUI_GH_VerticalScrollBar.htm
"GH_VerticalScrollBar Methods")

[GH_VerticalScrollBar
Events](../html/Events_T_Grasshopper_GUI_GH_VerticalScrollBar.htm
"GH_VerticalScrollBar Events")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_VerticalScrollBar Class  
  
---  
  
Scroll bar control with floating point accuracy.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[SystemMarshalByRefObject](https://docs.microsoft.com/dotnet/api/system.marshalbyrefobject)  
[System.ComponentModelComponent](https://docs.microsoft.com/dotnet/api/system.componentmodel.component)  
[System.Windows.FormsControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.control)  
[System.Windows.FormsScrollableControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol)  
[System.Windows.FormsPanel](https://docs.microsoft.com/dotnet/api/system.windows.forms.panel)  
[Grasshopper.GUIGH_DoubleBufferedPanel](T_Grasshopper_GUI_GH_DoubleBufferedPanel.htm)  
Grasshopper.GUIGH_VerticalScrollBar  

**Namespace:** [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_VerticalScrollBar : GH_DoubleBufferedPanel
    
    
    Public Class GH_VerticalScrollBar
    	Inherits GH_DoubleBufferedPanel

The GH_VerticalScrollBar type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_VerticalScrollBar](M_Grasshopper_GUI_GH_VerticalScrollBar__ctor.htm)|
Initializes a new instance of the GH_VerticalScrollBar class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Grip](P_Grasshopper_GUI_GH_VerticalScrollBar_Grip.htm)|  Gets the actual
dimensions of the scroll bar grip.  
![Public property](../icons/pubproperty.gif)|
[GripRegion](P_Grasshopper_GUI_GH_VerticalScrollBar_GripRegion.htm)|  Gets the
grip region for this scroll bar. The Grip Region is the area in which the grip
can be found. It is essentially the Client area minus the padding.  
![Public property](../icons/pubproperty.gif)|
[ImpliedVerticalOffset](P_Grasshopper_GUI_GH_VerticalScrollBar_ImpliedVerticalOffset.htm)|
Gets or sets the offset of the target region as implied by the scroll ratio.
If you set this value, the ratio is reverse engineered.  
![Public property](../icons/pubproperty.gif)|
[ScreenHeight](P_Grasshopper_GUI_GH_VerticalScrollBar_ScreenHeight.htm)|  Gets
or sets the height of the screen area (the visible area)  
![Public property](../icons/pubproperty.gif)|
[TargetHeight](P_Grasshopper_GUI_GH_VerticalScrollBar_TargetHeight.htm)|  Gets
or sets the height of the target area (the area being scrolled)  
![Public property](../icons/pubproperty.gif)|
[TargetRatio](P_Grasshopper_GUI_GH_VerticalScrollBar_TargetRatio.htm)|  Gets
or sets the scroll ration. If the scroll ratio is changed, the
OnScrollRatioChanged event will be raised.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[OnPaint](M_Grasshopper_GUI_GH_VerticalScrollBar_OnPaint.htm)|  (Overrides
[ControlOnPaint(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.control.onpaint#system-
windows-forms-control-onpaint\(system-windows-forms-painteventargs\)).)  
![Protected method](../icons/protmethod.gif)|
[OnPaintBackground](M_Grasshopper_GUI_GH_VerticalScrollBar_OnPaintBackground.htm)|
(Overrides
[ScrollableControlOnPaintBackground(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol.onpaintbackground#system-
windows-forms-scrollablecontrol-onpaintbackground\(system-windows-forms-
painteventargs\)).)  
Top

![](../icons/SectionExpanded.png)Events

| Name| Description  
---|---|---  
![Public event](../icons/pubevent.gif)|
[ScrollRatioChanged](E_Grasshopper_GUI_GH_VerticalScrollBar_ScrollRatioChanged.htm)|  
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

