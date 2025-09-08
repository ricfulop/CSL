---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Canvas_GH_CanvasWireValidator.htm
scraped_at: 2025-09-08T16:14:33.820753
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm
"Grasshopper.GUI.Canvas")

[GH_CanvasWireValidator
Class](../html/T_Grasshopper_GUI_Canvas_GH_CanvasWireValidator.htm
"GH_CanvasWireValidator Class")

[GH_CanvasWireValidator Constructor
](../html/M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator__ctor.htm
"GH_CanvasWireValidator Constructor ")

[GH_CanvasWireValidator
Properties](../html/Properties_T_Grasshopper_GUI_Canvas_GH_CanvasWireValidator.htm
"GH_CanvasWireValidator Properties")

[GH_CanvasWireValidator
Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_CanvasWireValidator.htm
"GH_CanvasWireValidator Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_CanvasWireValidator Class  
  
---  
  
Utility validator for restricting wire creation.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.GUI.CanvasGH_CanvasValidator](T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm)  
Grasshopper.GUI.CanvasGH_CanvasWireValidator  

**Namespace:** [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_CanvasWireValidator : GH_CanvasValidator
    
    
    Public Class GH_CanvasWireValidator
    	Inherits GH_CanvasValidator

The GH_CanvasWireValidator type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_CanvasWireValidator](M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator__ctor.htm)|
Initializes a new instance of the GH_CanvasWireValidator class  
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
[WireDelegate](P_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_WireDelegate.htm)|
Gets or sets the delegate to be invoked when a wire is created.  
![Public property](../icons/pubproperty.gif)|
[WireMotionText](P_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_WireMotionText.htm)|
Gets or sets the text to draw at the wire interior.  
![Public property](../icons/pubproperty.gif)|
[WireSource](P_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_WireSource.htm)|
Gets or sets the wire source filter.  
![Public property](../icons/pubproperty.gif)|
[WireSourceText](P_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_WireSourceText.htm)|
Gets or sets the text to draw at the wire source location.  
![Public property](../icons/pubproperty.gif)|
[WireTarget](P_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_WireTarget.htm)|
Gets or sets the wire target filter.  
![Public property](../icons/pubproperty.gif)|
[WireTargetText](P_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_WireTargetText.htm)|
Gets or sets the text to draw at the wire target location.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AddedToCanvas](M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_AddedToCanvas.htm)|
(Overrides
[GH_CanvasValidatorAddedToCanvas(GH_Canvas)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_AddedToCanvas.htm).)  
![Public method](../icons/pubmethod.gif)|
[AppliesToDocument](M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_AppliesToDocument.htm)|
(Overrides
[GH_CanvasValidatorAppliesToDocument(Guid)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_AppliesToDocument.htm).)  
![Public method](../icons/pubmethod.gif)|
[CanAcceptObject](M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_CanAcceptObject.htm)|
(Overrides
[GH_CanvasValidatorCanAcceptObject(Guid)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanAcceptObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[CanCreateObject](M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_CanCreateObject.htm)|
(Overrides [GH_CanvasValidatorCanCreateObject(Guid,
PointF)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanCreateObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[CanCreateWire](M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_CanCreateWire.htm)|
(Overrides [GH_CanvasValidatorCanCreateWire(IGH_Param,
IGH_Param)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanCreateWire.htm).)  
![Public method](../icons/pubmethod.gif)|
[CanDeleteObject](M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_CanDeleteObject.htm)|
(Overrides
[GH_CanvasValidatorCanDeleteObject(IGH_DocumentObject)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanDeleteObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[CanDeleteWire](M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_CanDeleteWire.htm)|
(Overrides [GH_CanvasValidatorCanDeleteWire(IGH_Param,
IGH_Param)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanDeleteWire.htm).)  
![Public method](../icons/pubmethod.gif)|
[CanDragObject](M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_CanDragObject.htm)|
(Overrides [GH_CanvasValidatorCanDragObject(IGH_DocumentObject,
PointF)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanDragObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[CanNavigateCanvas](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanNavigateCanvas.htm)|
(Inherited from
[GH_CanvasValidator](T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm).)  
![Public method](../icons/pubmethod.gif)|
[CanShowCanvasMenu](M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_CanShowCanvasMenu.htm)|
(Overrides
[GH_CanvasValidatorCanShowCanvasMenu(PointF)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanShowCanvasMenu.htm).)  
![Public method](../icons/pubmethod.gif)|
[CanShowComponentSearchBox](M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_CanShowComponentSearchBox.htm)|
(Overrides
[GH_CanvasValidatorCanShowComponentSearchBox(PointF)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanShowComponentSearchBox.htm).)  
![Public method](../icons/pubmethod.gif)|
[CanShowObjectMenu](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanShowObjectMenu.htm)|
(Inherited from
[GH_CanvasValidator](T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm).)  
![Public method](../icons/pubmethod.gif)|
[RemovedFromCanvas](M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_RemovedFromCanvas.htm)|
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

