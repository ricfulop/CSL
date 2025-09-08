---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Canvas_GH_ResizeBorder.htm
scraped_at: 2025-09-08T16:14:46.885110
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm
"Grasshopper.GUI.Canvas")

[GH_ResizeBorder Class](../html/T_Grasshopper_GUI_Canvas_GH_ResizeBorder.htm
"GH_ResizeBorder Class")

[GH_ResizeBorder Constructor
](../html/Overload_Grasshopper_GUI_Canvas_GH_ResizeBorder__ctor.htm
"GH_ResizeBorder Constructor ")

[GH_ResizeBorder
Properties](../html/Properties_T_Grasshopper_GUI_Canvas_GH_ResizeBorder.htm
"GH_ResizeBorder Properties")

[GH_ResizeBorder
Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_ResizeBorder.htm
"GH_ResizeBorder Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_ResizeBorder Class  
  
---  
  
![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.GUI.CanvasGH_Border](T_Grasshopper_GUI_Canvas_GH_Border.htm)  
Grasshopper.GUI.CanvasGH_ResizeBorder  

**Namespace:** [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_ResizeBorder : GH_Border
    
    
    Public Class GH_ResizeBorder
    	Inherits GH_Border

The GH_ResizeBorder type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_ResizeBorder(GH_Border)](M_Grasshopper_GUI_Canvas_GH_ResizeBorder__ctor.htm)|
Create a new instance of the GH_ResizeBorder class.  
![Public method](../icons/pubmethod.gif)| [GH_ResizeBorder(RectangleF,
GH_BorderTopology)](M_Grasshopper_GUI_Canvas_GH_ResizeBorder__ctor_1.htm)|
Create a new instance of the GH_ResizeBorder class.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Anchor](P_Grasshopper_GUI_Canvas_GH_ResizeBorder_Anchor.htm)|  Gets or sets
the anchor point for sizing operations. This point is determined automatically
when you call Setup(), however you can alter it afterwards if you want.  
![Public property](../icons/pubproperty.gif)|
[Region](P_Grasshopper_GUI_Canvas_GH_Border_Region.htm)|  Gets the shape of
the border.  (Inherited from
[GH_Border](T_Grasshopper_GUI_Canvas_GH_Border.htm).)  
![Public property](../icons/pubproperty.gif)|
[Size_Cursor](P_Grasshopper_GUI_Canvas_GH_Border_Size_Cursor.htm)|  Gets the
cursor associated with this border.  (Inherited from
[GH_Border](T_Grasshopper_GUI_Canvas_GH_Border.htm).)  
![Public property](../icons/pubproperty.gif)|
[Topology](P_Grasshopper_GUI_Canvas_GH_Border_Topology.htm)|  Gets the type of
border.  (Inherited from [GH_Border](T_Grasshopper_GUI_Canvas_GH_Border.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Contains](M_Grasshopper_GUI_Canvas_GH_Border_Contains.htm)|  Test a point for
border inclusion.  (Inherited from
[GH_Border](T_Grasshopper_GUI_Canvas_GH_Border.htm).)  
![Public method](../icons/pubmethod.gif)| [Setup(IGH_Attributes,
PointF)](M_Grasshopper_GUI_Canvas_GH_ResizeBorder_Setup.htm)|  Set up a new
sizing operation.  
![Public method](../icons/pubmethod.gif)| [Setup(IGH_Attributes, PointF,
SizeF)](M_Grasshopper_GUI_Canvas_GH_ResizeBorder_Setup_1.htm)|  Set up a new
sizing operation.  
![Public method](../icons/pubmethod.gif)| [Setup(RectangleF, PointF,
PointF)](M_Grasshopper_GUI_Canvas_GH_ResizeBorder_Setup_3.htm)|  Set up a new
sizing operation.  
![Public method](../icons/pubmethod.gif)| [Setup(IGH_Attributes, PointF,
SizeF, SizeF)](M_Grasshopper_GUI_Canvas_GH_ResizeBorder_Setup_2.htm)|  Set up
a new sizing operation.  
![Public method](../icons/pubmethod.gif)| [Setup(RectangleF, PointF, PointF,
SizeF)](M_Grasshopper_GUI_Canvas_GH_ResizeBorder_Setup_4.htm)|  Set up a new
sizing operation.  
![Public method](../icons/pubmethod.gif)| [Setup(RectangleF, PointF, PointF,
SizeF, SizeF)](M_Grasshopper_GUI_Canvas_GH_ResizeBorder_Setup_5.htm)|  Set up
a new sizing operation.  
![Public method](../icons/pubmethod.gif)|
[Solve](M_Grasshopper_GUI_Canvas_GH_ResizeBorder_Solve.htm)|  Solve a resizing
step.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

