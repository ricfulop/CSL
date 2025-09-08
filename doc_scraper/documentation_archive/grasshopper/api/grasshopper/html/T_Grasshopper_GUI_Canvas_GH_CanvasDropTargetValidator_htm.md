---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Canvas_GH_CanvasDropTargetValidator.htm
scraped_at: 2025-09-08T16:14:27.801452
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm
"Grasshopper.GUI.Canvas")

[GH_CanvasDropTargetValidator
Class](../html/T_Grasshopper_GUI_Canvas_GH_CanvasDropTargetValidator.htm
"GH_CanvasDropTargetValidator Class")

[GH_CanvasDropTargetValidator Constructor
](../html/M_Grasshopper_GUI_Canvas_GH_CanvasDropTargetValidator__ctor.htm
"GH_CanvasDropTargetValidator Constructor ")

[GH_CanvasDropTargetValidator
Properties](../html/Properties_T_Grasshopper_GUI_Canvas_GH_CanvasDropTargetValidator.htm
"GH_CanvasDropTargetValidator Properties")

[GH_CanvasDropTargetValidator
Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_CanvasDropTargetValidator.htm
"GH_CanvasDropTargetValidator Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_CanvasDropTargetValidator Class  
  
---  
  
Utility validator for restricting component creation.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.GUI.CanvasGH_CanvasValidator](T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm)  
Grasshopper.GUI.CanvasGH_CanvasDropTargetValidator  

**Namespace:** [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_CanvasDropTargetValidator : GH_CanvasValidator
    
    
    Public Class GH_CanvasDropTargetValidator
    	Inherits GH_CanvasValidator

The GH_CanvasDropTargetValidator type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_CanvasDropTargetValidator](M_Grasshopper_GUI_Canvas_GH_CanvasDropTargetValidator__ctor.htm)|
Initializes a new instance of the GH_CanvasDropTargetValidator class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Protected property](../icons/protproperty.gif)|
[Canvas](P_Grasshopper_GUI_Canvas_GH_CanvasValidator_Canvas.htm)|  Gets the
canvas this validator is associated with.  (Inherited from
[GH_CanvasValidator](T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm).)  
![Protected property](../icons/protproperty.gif)|
[Document](P_Grasshopper_GUI_Canvas_GH_CanvasValidator_Document.htm)|  Gets
the document (if it exists) that is currently loaded in the canvas.
(Inherited from
[GH_CanvasValidator](T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm).)  
![Public property](../icons/pubproperty.gif)|
[DropDelegate](P_Grasshopper_GUI_Canvas_GH_CanvasDropTargetValidator_DropDelegate.htm)|
Gets or sets the delegate to be invoked when a component is dropped inside the
dropregion.  
![Public property](../icons/pubproperty.gif)|
[DropID](P_Grasshopper_GUI_Canvas_GH_CanvasDropTargetValidator_DropID.htm)|
Gets or sets the ID for the allowed component.  
![Public property](../icons/pubproperty.gif)|
[DropRegion](P_Grasshopper_GUI_Canvas_GH_CanvasDropTargetValidator_DropRegion.htm)|
Gets or sets the dropregion for this validator. Regions are cloned so you can
dispose of the original immedately after assignment.  
![Public property](../icons/pubproperty.gif)|
[DropText](P_Grasshopper_GUI_Canvas_GH_CanvasDropTargetValidator_DropText.htm)|
Gets or sets the text to display.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AddedToCanvas](M_Grasshopper_GUI_Canvas_GH_CanvasDropTargetValidator_AddedToCanvas.htm)|
(Overrides
[GH_CanvasValidatorAddedToCanvas(GH_Canvas)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_AddedToCanvas.htm).)  
![Public method](../icons/pubmethod.gif)|
[AppliesToDocument](M_Grasshopper_GUI_Canvas_GH_CanvasDropTargetValidator_AppliesToDocument.htm)|
(Overrides
[GH_CanvasValidatorAppliesToDocument(Guid)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_AppliesToDocument.htm).)  
![Public method](../icons/pubmethod.gif)|
[CanAcceptObject](M_Grasshopper_GUI_Canvas_GH_CanvasDropTargetValidator_CanAcceptObject.htm)|
(Overrides
[GH_CanvasValidatorCanAcceptObject(Guid)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanAcceptObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[CanCreateObject](M_Grasshopper_GUI_Canvas_GH_CanvasDropTargetValidator_CanCreateObject.htm)|
(Overrides [GH_CanvasValidatorCanCreateObject(Guid,
PointF)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanCreateObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[CanCreateWire](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanCreateWire.htm)|
(Inherited from
[GH_CanvasValidator](T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm).)  
![Public method](../icons/pubmethod.gif)|
[CanDeleteObject](M_Grasshopper_GUI_Canvas_GH_CanvasDropTargetValidator_CanDeleteObject.htm)|
(Overrides
[GH_CanvasValidatorCanDeleteObject(IGH_DocumentObject)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanDeleteObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[CanDeleteWire](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanDeleteWire.htm)|
(Inherited from
[GH_CanvasValidator](T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm).)  
![Public method](../icons/pubmethod.gif)|
[CanDragObject](M_Grasshopper_GUI_Canvas_GH_CanvasDropTargetValidator_CanDragObject.htm)|
(Overrides [GH_CanvasValidatorCanDragObject(IGH_DocumentObject,
PointF)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanDragObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[CanNavigateCanvas](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanNavigateCanvas.htm)|
(Inherited from
[GH_CanvasValidator](T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm).)  
![Public method](../icons/pubmethod.gif)|
[CanShowCanvasMenu](M_Grasshopper_GUI_Canvas_GH_CanvasDropTargetValidator_CanShowCanvasMenu.htm)|
(Overrides
[GH_CanvasValidatorCanShowCanvasMenu(PointF)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanShowCanvasMenu.htm).)  
![Public method](../icons/pubmethod.gif)|
[CanShowComponentSearchBox](M_Grasshopper_GUI_Canvas_GH_CanvasDropTargetValidator_CanShowComponentSearchBox.htm)|
(Overrides
[GH_CanvasValidatorCanShowComponentSearchBox(PointF)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanShowComponentSearchBox.htm).)  
![Public method](../icons/pubmethod.gif)|
[CanShowObjectMenu](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanShowObjectMenu.htm)|
(Inherited from
[GH_CanvasValidator](T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm).)  
![Public method](../icons/pubmethod.gif)|
[RemovedFromCanvas](M_Grasshopper_GUI_Canvas_GH_CanvasDropTargetValidator_RemovedFromCanvas.htm)|
(Overrides
[GH_CanvasValidatorRemovedFromCanvas(GH_Canvas)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_RemovedFromCanvas.htm).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

