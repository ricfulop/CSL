---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Canvas_IGH_CanvasValidator.htm
scraped_at: 2025-09-08T16:14:52.899190
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm
"Grasshopper.GUI.Canvas")

[IGH_CanvasValidator
Interface](../html/T_Grasshopper_GUI_Canvas_IGH_CanvasValidator.htm
"IGH_CanvasValidator Interface")

[IGH_CanvasValidator
Methods](../html/Methods_T_Grasshopper_GUI_Canvas_IGH_CanvasValidator.htm
"IGH_CanvasValidator Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_CanvasValidator Interface  
  
---  
  
'Interface used for limiting a collection of typical actions on the canvas. Do
not implement this interface directly if you can help it, instead inherit from
GH_CanvasValidator.

**Namespace:** [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_CanvasValidator
    
    
    Public Interface IGH_CanvasValidator

The IGH_CanvasValidator type exposes the following members.

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AddedToCanvas](M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_AddedToCanvas.htm)|
This method will be called by the Canvas when this validator is added to it.  
![Public method](../icons/pubmethod.gif)|
[AppliesToDocument](M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_AppliesToDocument.htm)|
Test whether this validator applies to a specific document.  
![Public method](../icons/pubmethod.gif)|
[CanAcceptObject](M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_CanAcceptObject.htm)|
Validates whether a specific component can be accepted by the canvas at all.  
![Public method](../icons/pubmethod.gif)|
[CanCreateObject](M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_CanCreateObject.htm)|
Validates whether a specific component may be inserted at a specific point.  
![Public method](../icons/pubmethod.gif)|
[CanCreateWire](M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_CanCreateWire.htm)|
Validates whether a wire-operation can commence.  
![Public method](../icons/pubmethod.gif)|
[CanDeleteObject](M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_CanDeleteObject.htm)|
Validates whether a specific object can be deleted.  
![Public method](../icons/pubmethod.gif)|
[CanDeleteWire](M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_CanDeleteWire.htm)|
Validates whether a wire can be deleted.  
![Public method](../icons/pubmethod.gif)|
[CanDragObject](M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_CanDragObject.htm)|
Validates whether some components can be dragged.  
![Public method](../icons/pubmethod.gif)|
[CanNavigateCanvas](M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_CanNavigateCanvas.htm)|
Validates whether the canvas can be navigated (panning, zooming etc)  
![Public method](../icons/pubmethod.gif)|
[CanShowCanvasMenu](M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_CanShowCanvasMenu.htm)|
Validates whether the canvas menus (both the radial and the old-fashioned one)
are allowed to pop up at a specific point.  
![Public method](../icons/pubmethod.gif)|
[CanShowComponentSearchBox](M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_CanShowComponentSearchBox.htm)|
Validates whether the double-click-component-search-window is allowed to pop
up at a specific point.  
![Public method](../icons/pubmethod.gif)|
[CanShowObjectMenu](M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_CanShowObjectMenu.htm)|
Validates whether the object menu can be shown.  
![Public method](../icons/pubmethod.gif)|
[RemovedFromCanvas](M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_RemovedFromCanvas.htm)|
This method will be called by the Canvas when this validator is removed from
it.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

