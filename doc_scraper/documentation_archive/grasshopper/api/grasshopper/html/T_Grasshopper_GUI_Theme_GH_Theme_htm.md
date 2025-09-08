---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Theme_GH_Theme.htm
scraped_at: 2025-09-08T16:15:13.981244
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Theme](../html/N_Grasshopper_GUI_Theme.htm
"Grasshopper.GUI.Theme")

[GH_Theme Class](../html/T_Grasshopper_GUI_Theme_GH_Theme.htm "GH_Theme
Class")

[GH_Theme Constructor
](../html/Overload_Grasshopper_GUI_Theme_GH_Theme__ctor.htm "GH_Theme
Constructor ")

[GH_Theme Properties](../html/Properties_T_Grasshopper_GUI_Theme_GH_Theme.htm
"GH_Theme Properties")

[GH_Theme Methods](../html/Methods_T_Grasshopper_GUI_Theme_GH_Theme.htm
"GH_Theme Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Theme Class  
  
---  
  
![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.GUI.ThemeGH_Theme  

**Namespace:** [Grasshopper.GUI.Theme](N_Grasshopper_GUI_Theme.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Theme : GH_ISerializable
    
    
    Public Class GH_Theme
    	Implements GH_ISerializable

The GH_Theme type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_Theme](M_Grasshopper_GUI_Theme_GH_Theme__ctor.htm)|  Create a new default
theme.  
![Public method](../icons/pubmethod.gif)|
[GH_Theme(GH_Theme)](M_Grasshopper_GUI_Theme_GH_Theme__ctor_1.htm)|  Make a
duplicate of another theme.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[BackGround](P_Grasshopper_GUI_Theme_GH_Theme_BackGround.htm)|  Gets the theme
background settings.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[DefaultTheme](P_Grasshopper_GUI_Theme_GH_Theme_DefaultTheme.htm)|  
![Public property](../icons/pubproperty.gif)|
[Objects](P_Grasshopper_GUI_Theme_GH_Theme_Objects.htm)|  Gets the theme
objects and ZUI settings.  
![Public property](../icons/pubproperty.gif)|
[Page](P_Grasshopper_GUI_Theme_GH_Theme_Page.htm)|  Gets the theme page and
grid settings.  
![Public property](../icons/pubproperty.gif)|
[Palettes](P_Grasshopper_GUI_Theme_GH_Theme_Palettes.htm)|  Gets the theme
palette settings.  
![Public property](../icons/pubproperty.gif)|
[Wires](P_Grasshopper_GUI_Theme_GH_Theme_Wires.htm)|  Gets the theme wire
settings.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[LoadTheme](M_Grasshopper_GUI_Theme_GH_Theme_LoadTheme.htm)|  Instantiate all
palette and gui defaults. This function reads the colour values out of
grasshopper_gui.xml settings database if it exists.  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_GUI_Theme_GH_Theme_Read.htm)|  
![Public method](../icons/pubmethod.gif)|
[SaveTheme](M_Grasshopper_GUI_Theme_GH_Theme_SaveTheme.htm)|  Store all
palette and gui defaults. This function writes the colour values out to
grasshopper_gui.xml settings database.  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_GUI_Theme_GH_Theme_Write.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Theme Namespace](N_Grasshopper_GUI_Theme.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

