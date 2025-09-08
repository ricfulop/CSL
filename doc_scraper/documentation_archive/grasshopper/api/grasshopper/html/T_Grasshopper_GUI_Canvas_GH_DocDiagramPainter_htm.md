---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Canvas_GH_DocDiagramPainter.htm
scraped_at: 2025-09-08T16:14:36.845106
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm
"Grasshopper.GUI.Canvas")

[GH_DocDiagramPainter
Class](../html/T_Grasshopper_GUI_Canvas_GH_DocDiagramPainter.htm
"GH_DocDiagramPainter Class")

[GH_DocDiagramPainter Constructor
](../html/M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter__ctor.htm
"GH_DocDiagramPainter Constructor ")

[GH_DocDiagramPainter
Properties](../html/Properties_T_Grasshopper_GUI_Canvas_GH_DocDiagramPainter.htm
"GH_DocDiagramPainter Properties")

[GH_DocDiagramPainter
Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_DocDiagramPainter.htm
"GH_DocDiagramPainter Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_DocDiagramPainter Class  
  
---  
  
This class paints diagrammatic images of a collection of objects.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.GUI.CanvasGH_DocDiagramPainter  

**Namespace:** [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_DocDiagramPainter
    
    
    Public Class GH_DocDiagramPainter

The GH_DocDiagramPainter type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_DocDiagramPainter](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter__ctor.htm)|
Initializes a new instance of the GH_DocDiagramPainter class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[BoundingBox](P_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_BoundingBox.htm)|
Gets the 2D domain of the diagram in canvas coordinates.  
![Public property](../icons/pubproperty.gif)|
[DrawingBox](P_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_DrawingBox.htm)|
Gets the 2D domain of the diagram in image coordinates.  
![Public property](../icons/pubproperty.gif)|
[IgnoreSelectedStates](P_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_IgnoreSelectedStates.htm)|
Gets or sets the Ignore Selected State flag. When set to True, selected
objects are not drawn in a different colour.  
![Public property](../icons/pubproperty.gif)|
[Image](P_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_Image.htm)|  Gets the
diagram image (only available after a call to PaintDiagram().  
![Public property](../icons/pubproperty.gif)|
[Size](P_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_Size.htm)|  Gets the
width and height (in pixels) of this diagram image.  
![Public property](../icons/pubproperty.gif)|
[Zoom](P_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_Zoom.htm)|  Gets the zoom
factor for this diagram.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[MapPoint(Point)](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_MapPoint.htm)|  
![Public method](../icons/pubmethod.gif)|
[MapPoint(PointF)](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_MapPoint_1.htm)|  
![Public method](../icons/pubmethod.gif)|
[MapRectangle](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_MapRectangle.htm)|  
![Public method](../icons/pubmethod.gif)|
[MapX(Int32)](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_MapX.htm)|  
![Public method](../icons/pubmethod.gif)|
[MapX(Single)](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_MapX_1.htm)|  
![Public method](../icons/pubmethod.gif)|
[MapY(Int32)](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_MapY.htm)|  
![Public method](../icons/pubmethod.gif)|
[MapY(Single)](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_MapY_1.htm)|  
![Public method](../icons/pubmethod.gif)|
[PaintDiagram(IEnumerableIGH_DocumentObject, Int32,
Int32)](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_PaintDiagram.htm)|
Paint a diagram of a document.  
![Public method](../icons/pubmethod.gif)|
[PaintDiagram(IEnumerableIGH_DocumentObject, Int32, Int32,
Int32)](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_PaintDiagram_1.htm)|
Paint a diagram of a document.  
![Public method](../icons/pubmethod.gif)|
[UnmapPoint](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_UnmapPoint.htm)|  
![Public method](../icons/pubmethod.gif)|
[UnmapRectangle](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_UnmapRectangle.htm)|  
![Public method](../icons/pubmethod.gif)|
[UnmapX](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_UnmapX.htm)|  
![Public method](../icons/pubmethod.gif)|
[UnmapY](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_UnmapY.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

