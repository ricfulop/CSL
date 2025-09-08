---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_GH_FontList.htm
scraped_at: 2025-09-08T16:12:36.302048
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH_FontList Class](../html/T_Grasshopper_GUI_GH_FontList.htm "GH_FontList
Class")

[GH_FontList Constructor ](../html/M_Grasshopper_GUI_GH_FontList__ctor.htm
"GH_FontList Constructor ")

[GH_FontList Properties](../html/Properties_T_Grasshopper_GUI_GH_FontList.htm
"GH_FontList Properties")

[GH_FontList Methods](../html/Methods_T_Grasshopper_GUI_GH_FontList.htm
"GH_FontList Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_FontList Class  
  
---  
  
Represents the installed Font collection. This control allows both navigation
and selection of Font Families.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[SystemMarshalByRefObject](https://docs.microsoft.com/dotnet/api/system.marshalbyrefobject)  
[System.ComponentModelComponent](https://docs.microsoft.com/dotnet/api/system.componentmodel.component)  
[System.Windows.FormsControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.control)  
[System.Windows.FormsScrollableControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol)  
[System.Windows.FormsPanel](https://docs.microsoft.com/dotnet/api/system.windows.forms.panel)  
[Grasshopper.GUIGH_DoubleBufferedPanel](T_Grasshopper_GUI_GH_DoubleBufferedPanel.htm)  
Grasshopper.GUIGH_FontList  

**Namespace:** [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_FontList : GH_DoubleBufferedPanel
    
    
    Public Class GH_FontList
    	Inherits GH_DoubleBufferedPanel

The GH_FontList type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_FontList](M_Grasshopper_GUI_GH_FontList__ctor.htm)| Initializes a new
instance of the GH_FontList class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[DisplayText](P_Grasshopper_GUI_GH_FontList_DisplayText.htm)|  Gets or sets
the placeholder string.  
![Public property](../icons/pubproperty.gif)|
[Filter](P_Grasshopper_GUI_GH_FontList_Filter.htm)|  Gets or sets the filter
string. You must call RecreateFontList() before the new font list is created.  
![Public property](../icons/pubproperty.gif)|
[FontFamily](P_Grasshopper_GUI_GH_FontList_FontFamily.htm)|  Gets or sets the
selected font family.  
![Public property](../icons/pubproperty.gif)|
[FontSize](P_Grasshopper_GUI_GH_FontList_FontSize.htm)|  Gets or sets the font
size.  
![Public property](../icons/pubproperty.gif)|
[FontStyle](P_Grasshopper_GUI_GH_FontList_FontStyle.htm)|  Gets or sets the
font style for all families.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CreateFont](M_Grasshopper_GUI_GH_FontList_CreateFont.htm)|  Create a font
that best approximates the current settings.  
![Protected method](../icons/protmethod.gif)|
[OnPaint](M_Grasshopper_GUI_GH_FontList_OnPaint.htm)|  (Overrides
[ControlOnPaint(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.control.onpaint#system-
windows-forms-control-onpaint\(system-windows-forms-painteventargs\)).)  
![Protected method](../icons/protmethod.gif)|
[OnPaintBackground](M_Grasshopper_GUI_GH_FontList_OnPaintBackground.htm)|
(Overrides
[ScrollableControlOnPaintBackground(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol.onpaintbackground#system-
windows-forms-scrollablecontrol-onpaintbackground\(system-windows-forms-
painteventargs\)).)  
![Public method](../icons/pubmethod.gif)|
[RecreateFontList](M_Grasshopper_GUI_GH_FontList_RecreateFontList.htm)|  
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

