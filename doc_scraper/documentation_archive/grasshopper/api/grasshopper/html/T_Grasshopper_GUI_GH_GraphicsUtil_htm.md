---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_GH_GraphicsUtil.htm
scraped_at: 2025-09-08T16:12:43.353235
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH_GraphicsUtil Class](../html/T_Grasshopper_GUI_GH_GraphicsUtil.htm
"GH_GraphicsUtil Class")

[GH_GraphicsUtil
Properties](../html/Properties_T_Grasshopper_GUI_GH_GraphicsUtil.htm
"GH_GraphicsUtil Properties")

[GH_GraphicsUtil
Methods](../html/Methods_T_Grasshopper_GUI_GH_GraphicsUtil.htm
"GH_GraphicsUtil Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_GraphicsUtil Class  
  
---  
  
Utility class with static (Shared) functions that help with colour, shape and
text rendering.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.GUIGH_GraphicsUtil  

**Namespace:** [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class GH_GraphicsUtil
    
    
    Public NotInheritable Class GH_GraphicsUtil

The GH_GraphicsUtil type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[UiScale](P_Grasshopper_GUI_GH_GraphicsUtil_UiScale.htm)|  Gets the screen-
scaling factor for the entire system. Use the UiAdjust methods in the
Grasshopper top level namespace (Global_Proc module) to modify integer and
single values.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[AppendArc(Point3d, Point3d, Vector3d,
GraphicsPath)](M_Grasshopper_GUI_GH_GraphicsUtil_AppendArc.htm)|  Append an
arc segment to a GraphicsPath. If the arc cannot be solved, a linear segment
is appended instead.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[AppendArc(PointF, PointF, SizeF,
GraphicsPath)](M_Grasshopper_GUI_GH_GraphicsUtil_AppendArc_1.htm)|  Append an
arc segment to a GraphicsPath. If the arc cannot be solved, a linear segment
is appended instead.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[BlendColour(Color,
Color)](M_Grasshopper_GUI_GH_GraphicsUtil_BlendColour.htm)|  Overlays two
colours. The Alpha component of the top colour controls the blend.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[BlendColour(Color, Color,
Double)](M_Grasshopper_GUI_GH_GraphicsUtil_BlendColour_1.htm)|  Overlays two
colours.  
![Public method](../icons/pubmethod.gif)![Static
member](../icons/static.gif)![Code example](../icons/CodeExample.png)|
[BlendInteger](M_Grasshopper_GUI_GH_GraphicsUtil_BlendInteger.htm)|
Calculates a linear blend between two extremes. Although the inputs are
unlimited integers, the output is an integer in the byte range (0-255).  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[BoxClosestArcPoint](M_Grasshopper_GUI_GH_GraphicsUtil_BoxClosestArcPoint.htm)|
Find the closest point on or in a box given a test point. Arc extension is
implied.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[BoxClosestPoint(Point,
Rectangle)](M_Grasshopper_GUI_GH_GraphicsUtil_BoxClosestPoint.htm)|  Find the
closest point on or in a box given a test point.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[BoxClosestPoint(PointF,
RectangleF)](M_Grasshopper_GUI_GH_GraphicsUtil_BoxClosestPoint_1.htm)|  Find
the closest point on or in a box given a test point.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[BoxFurthestPoint(Point,
Rectangle)](M_Grasshopper_GUI_GH_GraphicsUtil_BoxFurthestPoint.htm)|  Find the
furthest point on or in a box given a test point.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[BoxFurthestPoint(PointF,
RectangleF)](M_Grasshopper_GUI_GH_GraphicsUtil_BoxFurthestPoint_1.htm)|  Find
the furthest point on or in a box given a test point.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[BoxViewCone](M_Grasshopper_GUI_GH_GraphicsUtil_BoxViewCone.htm)|  Computes
the graphicspath that represents the viewcone for a point and a rectangle. If
the rectangle contains the point, null is returned.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ColourARGB(Double, Double,
Double)](M_Grasshopper_GUI_GH_GraphicsUtil_ColourARGB.htm)|  Create a colour
from floating ARGB channels (0.0~1.0). Channels are clipped to valid ranges.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ColourARGB(Int32, Int32,
Int32)](M_Grasshopper_GUI_GH_GraphicsUtil_ColourARGB_1.htm)|  Create a colour
from integer RGB channels. Channels are clipped to valid ranges.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ColourARGB(Int32, Int32, Int32,
Int32)](M_Grasshopper_GUI_GH_GraphicsUtil_ColourARGB_2.htm)|  Create a colour
from integer ARGB channels. Channels are clipped to valid ranges.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateColourIcon](M_Grasshopper_GUI_GH_GraphicsUtil_CreateColourIcon.htm)|
Create a colour swatch icon.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[DentHorizontal(Graphics,
Rectangle)](M_Grasshopper_GUI_GH_GraphicsUtil_DentHorizontal.htm)|  Draws a
horizontal dent. A horizontal dent had dark lines along the top and bottom
edges.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[DentHorizontal(Graphics, Rectangle, Int32,
Int32)](M_Grasshopper_GUI_GH_GraphicsUtil_DentHorizontal_1.htm)|  Draws a
horizontal dent. A horizontal dent had dark lines along the top and bottom
edges.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[DentVertical(Graphics,
Rectangle)](M_Grasshopper_GUI_GH_GraphicsUtil_DentVertical.htm)|  Draws a
vertical dent. A vertical dent had dark lines along the left and right edges.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[DentVertical(Graphics, Rectangle, Int32,
Int32)](M_Grasshopper_GUI_GH_GraphicsUtil_DentVertical_1.htm)|  Draws a
vertical dent. A vertical dent had dark lines along the left and right edges.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Distance](M_Grasshopper_GUI_GH_GraphicsUtil_Distance.htm)|  Compute the
distance between two points.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[DistanceS](M_Grasshopper_GUI_GH_GraphicsUtil_DistanceS.htm)|  Compute the
squared distance between two points.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[EtchFadingHorizontal](M_Grasshopper_GUI_GH_GraphicsUtil_EtchFadingHorizontal.htm)|
Draw an etched line with fading on the extremes.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[EtchFadingVertical](M_Grasshopper_GUI_GH_GraphicsUtil_EtchFadingVertical.htm)|
Draw an etched line with fading on the extremes.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[EtchHorizontal(Graphics, Single, Single, Single,
Int32)](M_Grasshopper_GUI_GH_GraphicsUtil_EtchHorizontal_1.htm)|  Draws an
etched line segment.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[EtchHorizontal(Graphics, Int32, Int32, Int32, Int32,
Int32)](M_Grasshopper_GUI_GH_GraphicsUtil_EtchHorizontal.htm)|  Draws an
etched line segment.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[EtchVertical(Graphics, Int32, Int32, Int32,
Int32)](M_Grasshopper_GUI_GH_GraphicsUtil_EtchVertical.htm)|  Draws an etched
line segment.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[EtchVertical(Graphics, Single, Single, Single,
Int32)](M_Grasshopper_GUI_GH_GraphicsUtil_EtchVertical_1.htm)|  Draws an
etched line segment.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FadeColour](M_Grasshopper_GUI_GH_GraphicsUtil_FadeColour.htm)|  Fade a colour
to transparency by linearly blending a parameter between extremes.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ForegroundColour](M_Grasshopper_GUI_GH_GraphicsUtil_ForegroundColour.htm)|
Calculates a suitable foreground color. If the background is lighter than 50%,
the foreground will be darker, otherwise the foreground will be lighter.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Grid(Graphics, RectangleF,
Int32)](M_Grasshopper_GUI_GH_GraphicsUtil_Grid.htm)|  Draw a default grid.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Grid(Graphics, RectangleF, Int32,
Int32)](M_Grasshopper_GUI_GH_GraphicsUtil_Grid_1.htm)|  Draw a default grid.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Grid(Graphics, RectangleF, Int32, Int32, Color,
Color)](M_Grasshopper_GUI_GH_GraphicsUtil_Grid_2.htm)|  Draw a grid.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[HighlightBrush](M_Grasshopper_GUI_GH_GraphicsUtil_HighlightBrush.htm)|  Gets
a new brush object that can be used to draw the content of hover and focus
rectangles. Caller is responsible for disposing the brush.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[HighlightPen](M_Grasshopper_GUI_GH_GraphicsUtil_HighlightPen.htm)|  Gets a
new pen object that can be used to draw the edges of hover and focus
rectangles. Caller is responsible for disposing the pen.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[InvertColour](M_Grasshopper_GUI_GH_GraphicsUtil_InvertColour.htm)|  Computes
the inverted colour. Alpha remains the same.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[IsPointInEllipse](M_Grasshopper_GUI_GH_GraphicsUtil_IsPointInEllipse.htm)|
Test whether a point is inside or outside an ellipse.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[LimitInteger](M_Grasshopper_GUI_GH_GraphicsUtil_LimitInteger.htm)|  Limits
the given integer to the 0~255 range.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[LimitIntegers](M_Grasshopper_GUI_GH_GraphicsUtil_LimitIntegers.htm)|  Limits
RGB channels to the 0~255 range,  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[OffsetColour(Color,
Int32)](M_Grasshopper_GUI_GH_GraphicsUtil_OffsetColour.htm)|  Add a fixed
value to all the channels in a colour.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[OffsetColour(Color, Int32, Int32,
Int32)](M_Grasshopper_GUI_GH_GraphicsUtil_OffsetColour_1.htm)|  Add a fixed
value to all the channels in a colour.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderBalloonTag(Graphics, String, PointF,
RectangleF)](M_Grasshopper_GUI_GH_GraphicsUtil_RenderBalloonTag_3.htm)|  Draw
a default balloon tag in a container.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderBalloonTag(Graphics, String, Font, PointF,
RectangleF)](M_Grasshopper_GUI_GH_GraphicsUtil_RenderBalloonTag_2.htm)|  Draw
a default balloon tag in a container with a Font override.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderBalloonTag(Graphics, String, Font, Color, Color, PointF,
Boolean)](M_Grasshopper_GUI_GH_GraphicsUtil_RenderBalloonTag.htm)|  Draw a
balloon tag in a container.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderBalloonTag(Graphics, String, Font, Color, Color, PointF,
RectangleF)](M_Grasshopper_GUI_GH_GraphicsUtil_RenderBalloonTag_1.htm)|  Draw
a balloon tag in a container.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderCenteredIcon(Graphics, RectangleF,
Image)](M_Grasshopper_GUI_GH_GraphicsUtil_RenderCenteredIcon.htm)|
**Obsolete.** Draw an icon centered in a frame. This code is not zoom-aware,
but it will perform consistent rounding (to avoid pixel-jitter when moving the
frame across the screen). Icon will not be clipped to the frame.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderCenteredIcon(Graphics, RectangleF, Image,
Double)](M_Grasshopper_GUI_GH_GraphicsUtil_RenderCenteredIcon_1.htm)|  Draw an
icon centered in a frame. This code is not zoom-aware, but it will perform
consistent rounding (to avoid pixel-jitter when moving the frame across the
screen). Icon will not be clipped to the frame.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderCenteredIcon(Graphics, RectangleF, Image,
Single)](M_Grasshopper_GUI_GH_GraphicsUtil_RenderCenteredIcon_2.htm)|
**Obsolete.** Draw an icon centered in a frame. This code is not zoom-aware,
but it will perform consistent rounding (to avoid pixel-jitter when moving the
frame across the screen). Icon will not be clipped to the frame.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderCenteredText](M_Grasshopper_GUI_GH_GraphicsUtil_RenderCenteredText.htm)|
Render a bit of text centered on a point.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderColourIcon(Graphics, Rectangle,
Color)](M_Grasshopper_GUI_GH_GraphicsUtil_RenderColourIcon.htm)|
**Obsolete.** Render a colour icon into a graphics context. A colour icon
contains a black outer and white inner edge.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderColourIcon(Graphics, Rectangle, Color,
Single)](M_Grasshopper_GUI_GH_GraphicsUtil_RenderColourIcon_1.htm)|  Render a
colour icon into a graphics context. A colour icon contains a black outer and
white inner edge.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderFadedImage(Graphics, Image, Rectangle,
Double)](M_Grasshopper_GUI_GH_GraphicsUtil_RenderFadedImage.htm)|  Render an
icon into a rectangle with a specific fading factor.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderFadedImage(Graphics, Image, Rectangle,
Int32)](M_Grasshopper_GUI_GH_GraphicsUtil_RenderFadedImage_1.htm)|  Render an
icon into a rectangle with a specific fading factor.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderHighlightBox(Graphics, Rectangle,
Int32)](M_Grasshopper_GUI_GH_GraphicsUtil_RenderHighlightBox.htm)|  Render a
typical blueish highlight rectangle  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderHighlightBox(Graphics, Rectangle, Int32, Boolean,
Boolean)](M_Grasshopper_GUI_GH_GraphicsUtil_RenderHighlightBox_1.htm)|  Render
a typical blueish highlight rectangle  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderHighlightBox(Graphics, Rectangle, Int32, Color,
Color)](M_Grasshopper_GUI_GH_GraphicsUtil_RenderHighlightBox_2.htm)|  Render a
typical blueish highlight rectangle  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderIcon](M_Grasshopper_GUI_GH_GraphicsUtil_RenderIcon.htm)|  Render an
icon into a frame. The icon is positioned in the center and will be drawn at
its own size multiplied by the system UiScale, provided it doesn't exceed the
frame.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderObjectOverlay(Graphics, IGH_DocumentObject,
RectangleF)](M_Grasshopper_GUI_GH_GraphicsUtil_RenderObjectOverlay.htm)|
Render all overlay icons for a specific object. Overlays aren't drawn when the
zoom is less than 80%  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderObjectOverlay(Graphics, IGH_ObjectProxy,
RectangleF)](M_Grasshopper_GUI_GH_GraphicsUtil_RenderObjectOverlay_1.htm)|
Render all overlay icons for a specific object. Overlays aren't drawn when the
zoom is less than 80%  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderRoundBar](M_Grasshopper_GUI_GH_GraphicsUtil_RenderRoundBar.htm)|
Render a cylinder shaped object with round caps.  
![Public method](../icons/pubmethod.gif)![Static
member](../icons/static.gif)![Code example](../icons/CodeExample.png)|
[RenderTag](M_Grasshopper_GUI_GH_GraphicsUtil_RenderTag.htm)|  Render a text
tag into a Graphics surface.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderUnscaledIcon(Graphics, Image, Int32,
Int32)](M_Grasshopper_GUI_GH_GraphicsUtil_RenderUnscaledIcon.htm)|
**Obsolete.** Draws an image file at 1:1 scale centered on the given
coordinates.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderUnscaledIcon(Graphics, Image, Int32, Int32,
Double)](M_Grasshopper_GUI_GH_GraphicsUtil_RenderUnscaledIcon_1.htm)|
**Obsolete.** Draws an image file at 1:1 scale centered on the given
coordinates.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderVerticalString](M_Grasshopper_GUI_GH_GraphicsUtil_RenderVerticalString.htm)|
Render vertical text (rotated 90 degrees counter-clockwise) within a
rectangle.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderWarningIcon](M_Grasshopper_GUI_GH_GraphicsUtil_RenderWarningIcon.htm)|
Render a typical warning icon into a graphics context. A warning icon is an
upright yellow triangle.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ScaleColour](M_Grasshopper_GUI_GH_GraphicsUtil_ScaleColour.htm)|  Multiply
the channels of a colour construct with a fixed factor.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ShadowHorizontal(Graphics, Int32, Int32, Int32, Int32, Boolean,
Color)](M_Grasshopper_GUI_GH_GraphicsUtil_ShadowHorizontal.htm)|  Draws a
horizontal shadow edge.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ShadowHorizontal(Graphics, Int32, Int32, Int32, Int32, Boolean,
Int32)](M_Grasshopper_GUI_GH_GraphicsUtil_ShadowHorizontal_1.htm)|  Draws a
horizontal shadow edge.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ShadowHorizontal(Graphics, Single, Single, Single, Single, Boolean,
Int32)](M_Grasshopper_GUI_GH_GraphicsUtil_ShadowHorizontal_2.htm)|  Draws a
horizontal shadow edge.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ShadowRectangle(Graphics, Rectangle, Int32,
Color)](M_Grasshopper_GUI_GH_GraphicsUtil_ShadowRectangle.htm)|  Draws shadow
edges on the interior of a rectangle.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ShadowRectangle(Graphics, Rectangle, Int32,
Int32)](M_Grasshopper_GUI_GH_GraphicsUtil_ShadowRectangle_1.htm)|  Draws
shadow edges on the interior of a rectangle.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ShadowVertical(Graphics, Int32, Int32, Int32, Int32, Boolean,
Color)](M_Grasshopper_GUI_GH_GraphicsUtil_ShadowVertical.htm)|  Draws a
vertical shadow edge.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ShadowVertical(Graphics, Int32, Int32, Int32, Int32, Boolean,
Int32)](M_Grasshopper_GUI_GH_GraphicsUtil_ShadowVertical_1.htm)|  Draws a
vertical shadow edge.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ShadowVertical(Graphics, Single, Single, Single, Single, Boolean,
Int32)](M_Grasshopper_GUI_GH_GraphicsUtil_ShadowVertical_2.htm)|  Draws a
vertical shadow edge.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[SolveArc(Point3d, Point3d, Vector3d, RectangleF, Single,
Single)](M_Grasshopper_GUI_GH_GraphicsUtil_SolveArc.htm)|  Create a GDI
circular arc definition from start-point, end-point and tangent direction.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[SolveArc(PointF, PointF, SizeF, RectangleF, Single,
Single)](M_Grasshopper_GUI_GH_GraphicsUtil_SolveArc_2.htm)|  Create a GDI
circular arc definition from start-point, end-point and tangent direction.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[SolveArc(Double, Double, Double, Double, Double, Double, RectangleF, Single,
Single)](M_Grasshopper_GUI_GH_GraphicsUtil_SolveArc_1.htm)|  Create a GDI
circular arc definition from start-point, end-point and tangent direction.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[TransparencyMatrix(Double)](M_Grasshopper_GUI_GH_GraphicsUtil_TransparencyMatrix.htm)|
Create an image transparency matrix for a specific blending factor.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[TransparencyMatrix(Int32)](M_Grasshopper_GUI_GH_GraphicsUtil_TransparencyMatrix_1.htm)|
Create an image transparency matrix for a specific blending factor.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

