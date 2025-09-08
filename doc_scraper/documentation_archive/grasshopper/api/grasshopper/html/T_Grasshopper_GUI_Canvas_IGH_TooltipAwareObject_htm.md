---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject.htm
scraped_at: 2025-09-08T16:14:54.890893
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm
"Grasshopper.GUI.Canvas")

[IGH_TooltipAwareObject
Interface](../html/T_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject.htm
"IGH_TooltipAwareObject Interface")

[IGH_TooltipAwareObject
Properties](../html/Properties_T_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject.htm
"IGH_TooltipAwareObject Properties")

[IGH_TooltipAwareObject
Methods](../html/Methods_T_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject.htm
"IGH_TooltipAwareObject Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_TooltipAwareObject Interface  
  
---  
  
Implement this interface if you want your object to participate in Grasshopper
Canvas tooltips.

**Namespace:** [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_TooltipAwareObject
    
    
    Public Interface IGH_TooltipAwareObject

The IGH_TooltipAwareObject type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[TooltipEnabled](P_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject_TooltipEnabled.htm)|
Gets the tooltip enabled value. If False, no further tooltip functions will be
called.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[IsTooltipRegion](M_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject_IsTooltipRegion.htm)|
Determine whether the specified pixel should result in a tooltip when the
cursor hovers over it.  
![Public method](../icons/pubmethod.gif)|
[SetupTooltip](M_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject_SetupTooltip.htm)|
This function is called when a tooltip it about to be displayed.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

