---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Canvas_GH_Viewport.htm
scraped_at: 2025-09-08T16:14:48.892906
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm
"Grasshopper.GUI.Canvas")

[GH_Viewport Class](../html/T_Grasshopper_GUI_Canvas_GH_Viewport.htm
"GH_Viewport Class")

[GH_Viewport Constructor
](../html/Overload_Grasshopper_GUI_Canvas_GH_Viewport__ctor.htm "GH_Viewport
Constructor ")

[GH_Viewport
Properties](../html/Properties_T_Grasshopper_GUI_Canvas_GH_Viewport.htm
"GH_Viewport Properties")

[GH_Viewport Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_Viewport.htm
"GH_Viewport Methods")

[GH_Viewport Fields](../html/Fields_T_Grasshopper_GUI_Canvas_GH_Viewport.htm
"GH_Viewport Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Viewport Class  
  
---  
  
Provides functionality for panning and zooming in a GH_Canvas environment.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.GUI.CanvasGH_Viewport  

**Namespace:** [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class GH_Viewport
    
    
    Public NotInheritable Class GH_Viewport

The GH_Viewport type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_Viewport](M_Grasshopper_GUI_Canvas_GH_Viewport__ctor.htm)| Initializes a
new instance of the GH_Viewport class  
![Public method](../icons/pubmethod.gif)|
[GH_Viewport(GH_Viewport)](M_Grasshopper_GUI_Canvas_GH_Viewport__ctor_1.htm)|
Initializes a new instance of the GH_Viewport class  
![Public method](../icons/pubmethod.gif)|
[GH_Viewport(Point)](M_Grasshopper_GUI_Canvas_GH_Viewport__ctor_2.htm)|
Initializes a new instance of the GH_Viewport class  
![Public method](../icons/pubmethod.gif)| [GH_Viewport(Point,
Single)](M_Grasshopper_GUI_Canvas_GH_Viewport__ctor_3.htm)| Initializes a new
instance of the GH_Viewport class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[ControlMidPoint](P_Grasshopper_GUI_Canvas_GH_Viewport_ControlMidPoint.htm)|
Gets the point in the exact center of the viewport in control coordinates.  
![Public property](../icons/pubproperty.gif)|
[Diagonal](P_Grasshopper_GUI_Canvas_GH_Viewport_Diagonal.htm)|  Gets the
length of the diagonal of the viewport in canvas coordinates.  
![Public property](../icons/pubproperty.gif)|
[Height](P_Grasshopper_GUI_Canvas_GH_Viewport_Height.htm)|  Gets or sets the
height of the viewport. Typically this is tied to the dimensions of the
canvas. Height is not allowed to go below 5 pixels.  
![Public property](../icons/pubproperty.gif)|
[MidPoint](P_Grasshopper_GUI_Canvas_GH_Viewport_MidPoint.htm)|  Gets or sets
the canvas coordinate that is directly underneath the center of the viewport.  
![Public property](../icons/pubproperty.gif)|
[ScreenPort](P_Grasshopper_GUI_Canvas_GH_Viewport_ScreenPort.htm)|  Gets the
dimensions of the viewport in control coordinates.  
![Public property](../icons/pubproperty.gif)|
[Size](P_Grasshopper_GUI_Canvas_GH_Viewport_Size.htm)|  Gets or sets the size
of the viewport. The size is typically tied to the dimensions of the Canvas.  
![Public property](../icons/pubproperty.gif)|
[Target](P_Grasshopper_GUI_Canvas_GH_Viewport_Target.htm)|  Gets or sets the
location of the target pixel. The target represents where the canvas origin is
drawn.  
![Public property](../icons/pubproperty.gif)|
[TargetRatio](P_Grasshopper_GUI_Canvas_GH_Viewport_TargetRatio.htm)|  Gets or
sets the target ratio with respect to the viewport dimensions. This is a
useful tool to prevent weird view changes during a canvas resize.  
![Public property](../icons/pubproperty.gif)|
[Tx](P_Grasshopper_GUI_Canvas_GH_Viewport_Tx.htm)|  Gets or sets the
x-component of the target pixel. The target represents where the canvas origin
is drawn.  
![Public property](../icons/pubproperty.gif)|
[Ty](P_Grasshopper_GUI_Canvas_GH_Viewport_Ty.htm)|  Gets or sets the
y-component of the target pixel. The target represents where the canvas origin
is drawn.  
![Public property](../icons/pubproperty.gif)|
[VisibleRegion](P_Grasshopper_GUI_Canvas_GH_Viewport_VisibleRegion.htm)|  Gets
the rectangle in canvas coordinates that is visible in the control.  
![Public property](../icons/pubproperty.gif)|
[Width](P_Grasshopper_GUI_Canvas_GH_Viewport_Width.htm)|  Gets or sets the
width of the viewport. Typically this is tied to the dimensions of the canvas.
Width is not allowed to go below 5 pixels.  
![Public property](../icons/pubproperty.gif)|
[Zoom](P_Grasshopper_GUI_Canvas_GH_Viewport_Zoom.htm)|  Gets or sets the Zoom
factor of the viewport. Please assign only sensible values.  
![Public property](../icons/pubproperty.gif)|
[ZoomBoolean](P_Grasshopper_GUI_Canvas_GH_Viewport_Zoom_1.htm)|  Sets the zoom
of the viewport with a view anchor.  
![Public property](../icons/pubproperty.gif)|
[ZoomInverse](P_Grasshopper_GUI_Canvas_GH_Viewport_ZoomInverse.htm)|  Gets the
inverse of the zoom.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ApplyProjection](M_Grasshopper_GUI_Canvas_GH_Viewport_ApplyProjection.htm)|
Apply the current display transformation to a Graphics object.  
![Public method](../icons/pubmethod.gif)|
[ComputeProjection](M_Grasshopper_GUI_Canvas_GH_Viewport_ComputeProjection.htm)|
Forces a recomputation of all cached data.  
![Public method](../icons/pubmethod.gif)|
[DollyZoom](M_Grasshopper_GUI_Canvas_GH_Viewport_DollyZoom.htm)|  Advanced
interface function for mouse 'dolly' zooming.  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_GUI_Canvas_GH_Viewport_Duplicate.htm)|  
![Public method](../icons/pubmethod.gif)|
[Focus(IGH_Attributes)](M_Grasshopper_GUI_Canvas_GH_Viewport_Focus.htm)|  Look
at a specific object.  
![Public method](../icons/pubmethod.gif)|
[Focus(ListIGH_Attributes)](M_Grasshopper_GUI_Canvas_GH_Viewport_Focus_1.htm)|
Look at a set of specific objects.  
![Public method](../icons/pubmethod.gif)|
[Focus(Point)](M_Grasshopper_GUI_Canvas_GH_Viewport_Focus_2.htm)|  Look at a
specific point.  
![Public method](../icons/pubmethod.gif)|
[Focus(PointF)](M_Grasshopper_GUI_Canvas_GH_Viewport_Focus_3.htm)|  Look at a
specific point.  
![Public method](../icons/pubmethod.gif)| [IsVisible(PointF,
Single)](M_Grasshopper_GUI_Canvas_GH_Viewport_IsVisible.htm)|  Test visibility
of a point.  
![Public method](../icons/pubmethod.gif)| [IsVisible(RectangleF,
Single)](M_Grasshopper_GUI_Canvas_GH_Viewport_IsVisible_1.htm)|  Test
visibility of a rectangle.  
![Public method](../icons/pubmethod.gif)|
[LimitUnit](M_Grasshopper_GUI_Canvas_GH_Viewport_LimitUnit.htm)|  Utility
function for calculating pixel dimensions in a zoom-aware environment. The
desired value is put through the zoom projection and if the resulting size (as
displayed on the screen) exceeds the visual limits it is clipped. This
function can be used for example to make sure that a certain penwidth never
exceeds visual limits (i.e. it doesn't get too thin or too thick on the
screen).  
![Public method](../icons/pubmethod.gif)|
[Project](M_Grasshopper_GUI_Canvas_GH_Viewport_Project.htm)|  Transform a
point from canvas into control coordinate space.  
![Public method](../icons/pubmethod.gif)|
[ProjectPoint](M_Grasshopper_GUI_Canvas_GH_Viewport_ProjectPoint.htm)|
Project a point from canvas coordinates into control coordinates.  
![Public method](../icons/pubmethod.gif)|
[ProjectRectangle](M_Grasshopper_GUI_Canvas_GH_Viewport_ProjectRectangle.htm)|
Project a rectangle from canvas coordinates into control coordinates.  
![Public method](../icons/pubmethod.gif)|
[ProjectX](M_Grasshopper_GUI_Canvas_GH_Viewport_ProjectX.htm)|  Project a
value along constant X from canvas coordinates into control coordinates.  
![Public method](../icons/pubmethod.gif)|
[ProjectY](M_Grasshopper_GUI_Canvas_GH_Viewport_ProjectY.htm)|  Project a
value along constant Y from canvas coordinates into control coordinates.  
![Public method](../icons/pubmethod.gif)|
[Set](M_Grasshopper_GUI_Canvas_GH_Viewport_Set.htm)|  
![Public method](../icons/pubmethod.gif)|
[SolveUnit](M_Grasshopper_GUI_Canvas_GH_Viewport_SolveUnit.htm)|  Utility
function for calculating graphics dimensions in a zoom-aware environment. This
function can be used for example to compute the linewidth of a pen which
always needs to appear as 3 pixels thick on the screen regardless of zoom
values.  
![Public method](../icons/pubmethod.gif)|
[Unproject](M_Grasshopper_GUI_Canvas_GH_Viewport_Unproject.htm)|  Transform a
point from control into canvas coordinate space.  
![Public method](../icons/pubmethod.gif)|
[UnprojectPoint](M_Grasshopper_GUI_Canvas_GH_Viewport_UnprojectPoint.htm)|
Project a point from control coordinates into canvas coordinates.  
![Public method](../icons/pubmethod.gif)|
[UnprojectRectangle](M_Grasshopper_GUI_Canvas_GH_Viewport_UnprojectRectangle.htm)|
Project a rectangle from control coordinates into canvas coordinates.  
![Public method](../icons/pubmethod.gif)|
[UnprojectX](M_Grasshopper_GUI_Canvas_GH_Viewport_UnprojectX.htm)|  Project a
value along constant X from control coordinates into canvas coordinates.  
![Public method](../icons/pubmethod.gif)|
[UnprojectY](M_Grasshopper_GUI_Canvas_GH_Viewport_UnprojectY.htm)|  Project a
value along constant Y from control coordinates into canvas coordinates.  
![Public method](../icons/pubmethod.gif)|
[XFormMatrix](M_Grasshopper_GUI_Canvas_GH_Viewport_XFormMatrix.htm)|  Gets the
display transformation cached by this viewport.  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[ZoomDefault](F_Grasshopper_GUI_Canvas_GH_Viewport_ZoomDefault.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[ZoomDefaultLower](F_Grasshopper_GUI_Canvas_GH_Viewport_ZoomDefaultLower.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[ZoomDefaultUpper](F_Grasshopper_GUI_Canvas_GH_Viewport_ZoomDefaultUpper.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[ZoomMaximum](F_Grasshopper_GUI_Canvas_GH_Viewport_ZoomMaximum.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[ZoomMinimum](F_Grasshopper_GUI_Canvas_GH_Viewport_ZoomMinimum.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

