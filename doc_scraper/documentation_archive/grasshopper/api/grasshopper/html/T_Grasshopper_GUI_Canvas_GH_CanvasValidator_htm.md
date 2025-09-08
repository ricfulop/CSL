---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm
scraped_at: 2025-09-08T16:14:30.840120
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm
"Grasshopper.GUI.Canvas")

[GH_CanvasValidator
Class](../html/T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm
"GH_CanvasValidator Class")

[GH_CanvasValidator Constructor
](../html/M_Grasshopper_GUI_Canvas_GH_CanvasValidator__ctor.htm
"GH_CanvasValidator Constructor ")

[GH_CanvasValidator
Properties](../html/Properties_T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm
"GH_CanvasValidator Properties")

[GH_CanvasValidator
Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm
"GH_CanvasValidator Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_CanvasValidator Class  
  
---  
  
Abstract implementation of IGH_CanvasValidator. Inherit from this class rather
than implementing IGH_CanvasValidator from scratch.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.GUI.CanvasGH_CanvasValidator  
[Grasshopper.GUI.CanvasGH_CanvasDropTargetValidator](T_Grasshopper_GUI_Canvas_GH_CanvasDropTargetValidator.htm)  
[Grasshopper.GUI.CanvasGH_CanvasWireValidator](T_Grasshopper_GUI_Canvas_GH_CanvasWireValidator.htm)  

**Namespace:** [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public abstract class GH_CanvasValidator : IGH_CanvasValidator
    
    
    Public MustInherit Class GH_CanvasValidator
    	Implements IGH_CanvasValidator

The GH_CanvasValidator type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[GH_CanvasValidator](M_Grasshopper_GUI_Canvas_GH_CanvasValidator__ctor.htm)|
Initializes a new instance of the GH_CanvasValidator class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Protected property](../icons/protproperty.gif)|
[Canvas](P_Grasshopper_GUI_Canvas_GH_CanvasValidator_Canvas.htm)|  Gets the
canvas this validator is associated with.  
![Protected property](../icons/protproperty.gif)|
[Document](P_Grasshopper_GUI_Canvas_GH_CanvasValidator_Document.htm)|  Gets
the document (if it exists) that is currently loaded in the canvas.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AddedToCanvas](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_AddedToCanvas.htm)|
Override this method if you want to be informed when this validator gets
assigned to a canvas. But *always* call the base class method.  
![Public method](../icons/pubmethod.gif)|
[AppliesToDocument](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_AppliesToDocument.htm)|  
![Public method](../icons/pubmethod.gif)|
[CanAcceptObject](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanAcceptObject.htm)|  
![Public method](../icons/pubmethod.gif)|
[CanCreateObject](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanCreateObject.htm)|  
![Public method](../icons/pubmethod.gif)|
[CanCreateWire](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanCreateWire.htm)|  
![Public method](../icons/pubmethod.gif)|
[CanDeleteObject](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanDeleteObject.htm)|  
![Public method](../icons/pubmethod.gif)|
[CanDeleteWire](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanDeleteWire.htm)|  
![Public method](../icons/pubmethod.gif)|
[CanDragObject](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanDragObject.htm)|  
![Public method](../icons/pubmethod.gif)|
[CanNavigateCanvas](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanNavigateCanvas.htm)|  
![Public method](../icons/pubmethod.gif)|
[CanShowCanvasMenu](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanShowCanvasMenu.htm)|  
![Public method](../icons/pubmethod.gif)|
[CanShowComponentSearchBox](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanShowComponentSearchBox.htm)|  
![Public method](../icons/pubmethod.gif)|
[CanShowObjectMenu](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanShowObjectMenu.htm)|  
![Public method](../icons/pubmethod.gif)|
[RemovedFromCanvas](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_RemovedFromCanvas.htm)|
Override this method if you want to be informed when this validator gets
removed from a canvas. But *always* call the base class method.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

