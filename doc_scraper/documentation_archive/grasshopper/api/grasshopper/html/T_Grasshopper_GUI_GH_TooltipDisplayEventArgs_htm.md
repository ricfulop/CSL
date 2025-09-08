---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_GH_TooltipDisplayEventArgs.htm
scraped_at: 2025-09-08T16:13:14.450422
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH_TooltipDisplayEventArgs
Class](../html/T_Grasshopper_GUI_GH_TooltipDisplayEventArgs.htm
"GH_TooltipDisplayEventArgs Class")

[GH_TooltipDisplayEventArgs
Properties](../html/Properties_T_Grasshopper_GUI_GH_TooltipDisplayEventArgs.htm
"GH_TooltipDisplayEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_TooltipDisplayEventArgs Class  
  
---  
  
Event arguments used in the Tooltip Component.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[SystemEventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
Grasshopper.GUIGH_TooltipDisplayEventArgs  

**Namespace:** [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class GH_TooltipDisplayEventArgs : EventArgs
    
    
    Public NotInheritable Class GH_TooltipDisplayEventArgs
    	Inherits EventArgs

The GH_TooltipDisplayEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Control](P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Control.htm)|  Gets the
control for whom the tooltip is about to be displayed.  
![Public property](../icons/pubproperty.gif)|
[Description](P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Description.htm)|
Gets or sets the description of the tooltip. This field is optional.  
![Public property](../icons/pubproperty.gif)|
[Diagram](P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Diagram.htm)|  Gets or
sets the image that is displayed in the details section of the tooltip. This
field is optional, but when it is defined, the Description property is
ignored.  
![Public property](../icons/pubproperty.gif)|
[Icon](P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Icon.htm)|  Gets or sets
the icon that is displayed in the upper left hand corner of the tooltip. This
field is optional.  
![Public property](../icons/pubproperty.gif)|
[Point](P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Point.htm)|  Gets the
point in control coordinates for the tooltip locus.  
![Public property](../icons/pubproperty.gif)|
[Region](P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Region.htm)|  Gets or
sets the active region (in control coordinates) for this tooltip. Once a
tooltip is shown inside the region, the tooltip will 'stick' to the mouse for
as long as the mouse remains within this region. By default the region is set
to Rectangle.Empty, which indicates that region tracking is not used for this
tooltip.  
![Public property](../icons/pubproperty.gif)|
[Text](P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Text.htm)|  Gets or sets
the text of the tooltip. If you do not set the Text property, you must set the
Title property or the tooltip will not be shown.  
![Public property](../icons/pubproperty.gif)|
[Title](P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Title.htm)|  Gets or sets
the title of the tooltip. If you do not set the Title property, you must set
the Text property or the tooltip will not be shown.  
![Public property](../icons/pubproperty.gif)|
[Valid](P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Valid.htm)|  Gets whether
there is currently enough data to display a tooltip.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

