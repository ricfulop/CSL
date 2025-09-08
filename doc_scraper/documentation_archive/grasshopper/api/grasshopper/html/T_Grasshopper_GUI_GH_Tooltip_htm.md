---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_GH_Tooltip.htm
scraped_at: 2025-09-08T16:13:11.443532
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH_Tooltip Class](../html/T_Grasshopper_GUI_GH_Tooltip.htm "GH_Tooltip
Class")

[GH_Tooltip Properties](../html/Properties_T_Grasshopper_GUI_GH_Tooltip.htm
"GH_Tooltip Properties")

[GH_Tooltip Methods](../html/Methods_T_Grasshopper_GUI_GH_Tooltip.htm
"GH_Tooltip Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Tooltip Class  
  
---  
  
Implements a custom Tooltip class with advanced functionality. All methods and
fields are Shared. There can never be more than one GH_Tooltip.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.GUIGH_Tooltip  

**Namespace:** [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class GH_Tooltip
    
    
    Public NotInheritable Class GH_Tooltip

The GH_Tooltip type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)| [Tag](P_Grasshopper_GUI_GH_Tooltip_Tag.htm)|
Gets or sets the tag object for the tooltip  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[TooltipForm](P_Grasshopper_GUI_GH_Tooltip_TooltipForm.htm)|  Gets the
internal instance of GH_TooltipForm.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Adjust](M_Grasshopper_GUI_GH_Tooltip_Adjust.htm)|  Repositions the tooltip to
match with new cursor positions.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[AssignTooltipFields](M_Grasshopper_GUI_GH_Tooltip_AssignTooltipFields.htm)|
Set all fields of the Tooltip. You'll still need to call Show() to display the
tooltip.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Clear](M_Grasshopper_GUI_GH_Tooltip_Clear.htm)|  Hides the tooltip and clears
all references and caches.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[IsOwner](M_Grasshopper_GUI_GH_Tooltip_IsOwner.htm)|  Returns true if the test
control matches the internal Owner control. Use this method to make sure you
actually own this tooltip prior to clearing it.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[IsTag](M_Grasshopper_GUI_GH_Tooltip_IsTag.htm)|  Returns True if the test
object matches the internal Tag object  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Layout](M_Grasshopper_GUI_GH_Tooltip_Layout.htm)|  Layout the tooltip fields.
Layout happens automatically if you use the AssigTooltipField method, if
however you poke values directly in the tooltip form you must place a call to
Layout() before showing the tooltip.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Show](M_Grasshopper_GUI_GH_Tooltip_Show.htm)|  Display the tooltip on screen.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[TooltipDetailedInformation](M_Grasshopper_GUI_GH_Tooltip_TooltipDetailedInformation.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

