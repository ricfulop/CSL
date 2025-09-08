---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Canvas_IGH_ResponsiveObject.htm
scraped_at: 2025-09-08T16:14:53.887841
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm
"Grasshopper.GUI.Canvas")

[IGH_ResponsiveObject
Interface](../html/T_Grasshopper_GUI_Canvas_IGH_ResponsiveObject.htm
"IGH_ResponsiveObject Interface")

[IGH_ResponsiveObject
Methods](../html/Methods_T_Grasshopper_GUI_Canvas_IGH_ResponsiveObject.htm
"IGH_ResponsiveObject Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_ResponsiveObject Interface  
  
---  
  
If you wish to participate in Canvas UI events, you must implement this
interface.

**Namespace:** [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_ResponsiveObject
    
    
    Public Interface IGH_ResponsiveObject

The IGH_ResponsiveObject type exposes the following members.

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[RespondToKeyDown](M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToKeyDown.htm)|  
![Public method](../icons/pubmethod.gif)|
[RespondToKeyUp](M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToKeyUp.htm)|  
![Public method](../icons/pubmethod.gif)|
[RespondToMouseDoubleClick](M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToMouseDoubleClick.htm)|
This function will be called whenever the left button is double-clicked over
the canvas. If you are active, you will be the only object who gets called.  
![Public method](../icons/pubmethod.gif)|
[RespondToMouseDown](M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToMouseDown.htm)|
This function will be called whenever a mouse button is pressed over the
canvas. If you are active, you will be the only object who gets called. If you
are inactive, you might get called if nobody on top of you decides to become
active.  
![Public method](../icons/pubmethod.gif)|
[RespondToMouseMove](M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToMouseMove.htm)|
This function will be called when the mouse moves across the canvas. If you
are active, you will be the only object who gets called. If you are inactive,
you might get called if nobody on top of you decides to become active.  
![Public method](../icons/pubmethod.gif)|
[RespondToMouseUp](M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToMouseUp.htm)|
This function will be called whenever a mouse button is released over the
canvas. If you are active, you will be the only object who gets called. If you
are inactive, you will not be called at all for MouseUp events.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

