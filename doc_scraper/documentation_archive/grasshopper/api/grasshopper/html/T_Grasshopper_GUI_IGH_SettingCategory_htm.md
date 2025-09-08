---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_IGH_SettingCategory.htm
scraped_at: 2025-09-08T16:13:27.506719
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[IGH_SettingCategory
Interface](../html/T_Grasshopper_GUI_IGH_SettingCategory.htm
"IGH_SettingCategory Interface")

[IGH_SettingCategory
Properties](../html/Properties_T_Grasshopper_GUI_IGH_SettingCategory.htm
"IGH_SettingCategory Properties")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_SettingCategory Interface  
  
---  
  
Represents a single category in the Settings UI. Implement this interface or
derive from GH_SettingsCategory to add a new Category to the Grasshopper
Settings interface.

**Namespace:** [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_SettingCategory
    
    
    Public Interface IGH_SettingCategory

The IGH_SettingCategory type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Description](P_Grasshopper_GUI_IGH_SettingCategory_Description.htm)|
Category description.  
![Public property](../icons/pubproperty.gif)|
[Icon](P_Grasshopper_GUI_IGH_SettingCategory_Icon.htm)|  Category icon. Image
should be 48x48 pixels.  
![Public property](../icons/pubproperty.gif)|
[Name](P_Grasshopper_GUI_IGH_SettingCategory_Name.htm)|  Category name (not
case sensitive). Use dots to separate subcategories.  
![Public property](../icons/pubproperty.gif)|
[Parent](P_Grasshopper_GUI_IGH_SettingCategory_Parent.htm)|  Gets the name of
the parent category. If the category is supposed to be top-level, this
property will return null or a String.Empty.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

