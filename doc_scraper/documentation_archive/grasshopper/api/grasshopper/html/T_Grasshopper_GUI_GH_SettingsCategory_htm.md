---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_GH_SettingsCategory.htm
scraped_at: 2025-09-08T16:13:04.404372
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH_SettingsCategory Class](../html/T_Grasshopper_GUI_GH_SettingsCategory.htm
"GH_SettingsCategory Class")

[GH_SettingsCategory Constructor
](../html/Overload_Grasshopper_GUI_GH_SettingsCategory__ctor.htm
"GH_SettingsCategory Constructor ")

[GH_SettingsCategory
Properties](../html/Properties_T_Grasshopper_GUI_GH_SettingsCategory.htm
"GH_SettingsCategory Properties")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_SettingsCategory Class  
  
---  
  
Base implementation of IGH_SettingsCategory. Derive from this class and
provide an empty constructor to play ball.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.GUIGH_SettingsCategory  

**Namespace:** [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public abstract class GH_SettingsCategory : IGH_SettingCategory
    
    
    Public MustInherit Class GH_SettingsCategory
    	Implements IGH_SettingCategory

The GH_SettingsCategory type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)| [GH_SettingsCategory(String,
Bitmap)](M_Grasshopper_GUI_GH_SettingsCategory__ctor.htm)|  Create a new top-
level category.  
![Protected method](../icons/protmethod.gif)| [GH_SettingsCategory(String,
String, Bitmap)](M_Grasshopper_GUI_GH_SettingsCategory__ctor_1.htm)|  Create a
new nested category.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Description](P_Grasshopper_GUI_GH_SettingsCategory_Description.htm)|  
![Public property](../icons/pubproperty.gif)|
[Icon](P_Grasshopper_GUI_GH_SettingsCategory_Icon.htm)|  
![Public property](../icons/pubproperty.gif)|
[Name](P_Grasshopper_GUI_GH_SettingsCategory_Name.htm)|  
![Public property](../icons/pubproperty.gif)|
[Parent](P_Grasshopper_GUI_GH_SettingsCategory_Parent.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

