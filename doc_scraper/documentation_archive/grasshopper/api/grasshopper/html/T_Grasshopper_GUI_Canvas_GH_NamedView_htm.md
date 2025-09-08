---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Canvas_GH_NamedView.htm
scraped_at: 2025-09-08T16:14:38.847248
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm
"Grasshopper.GUI.Canvas")

[GH_NamedView Class](../html/T_Grasshopper_GUI_Canvas_GH_NamedView.htm
"GH_NamedView Class")

[GH_NamedView Constructor
](../html/Overload_Grasshopper_GUI_Canvas_GH_NamedView__ctor.htm "GH_NamedView
Constructor ")

[GH_NamedView
Properties](../html/Properties_T_Grasshopper_GUI_Canvas_GH_NamedView.htm
"GH_NamedView Properties")

[GH_NamedView
Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_NamedView.htm
"GH_NamedView Methods")

[GH_NamedView Events](../html/Events_T_Grasshopper_GUI_Canvas_GH_NamedView.htm
"GH_NamedView Events")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_NamedView Class  
  
---  
  
Named views are used both to store named views but also to allow smooth
programmatic canvas navigation.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.GUI.CanvasGH_NamedView  

**Namespace:** [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_NamedView : GH_ISerializable
    
    
    Public Class GH_NamedView
    	Implements GH_ISerializable

The GH_NamedView type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_NamedView](M_Grasshopper_GUI_Canvas_GH_NamedView__ctor.htm)|  Create a
default named view.  
![Public method](../icons/pubmethod.gif)| [GH_NamedView(Rectangle,
RectangleF)](M_Grasshopper_GUI_Canvas_GH_NamedView__ctor_3.htm)|  Create a new
view useful for box-fit transitions.  
![Public method](../icons/pubmethod.gif)| [GH_NamedView(GH_Viewport, Point,
PointF)](M_Grasshopper_GUI_Canvas_GH_NamedView__ctor_1.htm)|  Create a new
view useful for point match transitions.  
![Public method](../icons/pubmethod.gif)| [GH_NamedView(GH_Viewport,
Rectangle, PointF)](M_Grasshopper_GUI_Canvas_GH_NamedView__ctor_2.htm)|
Create a new view useful for point inclusion transitions.  
![Public method](../icons/pubmethod.gif)| [GH_NamedView(String, PointF,
Single, GH_NamedViewType)](M_Grasshopper_GUI_Canvas_GH_NamedView__ctor_4.htm)|
Create a new named view.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Name](P_Grasshopper_GUI_Canvas_GH_NamedView_Name.htm)|  Gets or sets the name
of the view.  
![Public property](../icons/pubproperty.gif)|
[Point](P_Grasshopper_GUI_Canvas_GH_NamedView_Point.htm)|  Gets or sets the
anchor point of the named view.  
![Public property](../icons/pubproperty.gif)|
[Type](P_Grasshopper_GUI_Canvas_GH_NamedView_Type.htm)|  Gets or sets a value
indicating whether the anchor point represents the target or the center.  
![Public property](../icons/pubproperty.gif)|
[Zoom](P_Grasshopper_GUI_Canvas_GH_NamedView_Zoom.htm)|  Gets or sets the zoom
factor of the named view.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[LoadFromViewport](M_Grasshopper_GUI_Canvas_GH_NamedView_LoadFromViewport.htm)|
Create a named view from a viewport.  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_GUI_Canvas_GH_NamedView_Read.htm)|  
![Public method](../icons/pubmethod.gif)|
[SetToViewport(GH_Canvas)](M_Grasshopper_GUI_Canvas_GH_NamedView_SetToViewport.htm)|
Set the named view to the canvas viewport and redraw the canvas.  
![Public method](../icons/pubmethod.gif)|
[SetToViewport(GH_Viewport)](M_Grasshopper_GUI_Canvas_GH_NamedView_SetToViewport_2.htm)|
Set the named view to a viewport.  
![Public method](../icons/pubmethod.gif)| [SetToViewport(GH_Canvas,
Int32)](M_Grasshopper_GUI_Canvas_GH_NamedView_SetToViewport_1.htm)|  Animates
a view transition.  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_GUI_Canvas_GH_NamedView_Write.htm)|  
Top

![](../icons/SectionExpanded.png)Events

| Name| Description  
---|---|---  
![Public event](../icons/pubevent.gif)|
[SmoothFrame](E_Grasshopper_GUI_Canvas_GH_NamedView_SmoothFrame.htm)|  This
event is raised during smooth animations.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

