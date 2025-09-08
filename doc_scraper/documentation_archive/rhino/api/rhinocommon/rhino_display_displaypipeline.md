---
url: https://developer.rhino3d.com/api/rhinocommon/rhino.display.displaypipeline
scraped_at: 2025-09-08T16:03:18.835495
title: Untitled
---

[_home_](/api/rhinocommon/)

/

[Rhino.Display](/api/rhinocommon/rhino.display)

/

DisplayPipeline

# DisplayPipeline class

The display pipeline calls events during specific phases of drawing During the
drawing of a single frame the events are called in the following order. [Begin
Drawing of a Frame]

  * CalculateBoundingBox
  * CalculateClippingPanes
  * SetupFrustum
  * SetupLighting
  * InitializeFrameBuffer
  * DrawBackground
  * If this is a layout and detail objects exist the channels are called in the same order for each detail object (drawn as a nested viewport)
  * PreDrawObjects
  * For Each Visible Non Highlighted Object
    * SetupObjectDisplayAttributes
    * PreDrawObject
    * DrawObject
    * PostDrawObject
  * PostDrawObjects - depth writing/testing on
  * DrawForeGround - depth writing/testing off
  * For Each Visible Highlighted Object
    * SetupObjectDisplayAttributes
    * PreDrawObject
    * DrawObject
    * PostDrawObject
  * PostProcessFrameBuffer (If a delegate exists that requires this)
  * DrawOverlay (if Rhino is in a feedback mode)

[End of Drawing of a Frame] NOTE: There may be multiple DrawObject calls for a
single object. An example of when this could happen would be with a shaded
sphere. The shaded mesh is first drawn and these channels would be processed;
then at a later time the isocurves for the sphere would be drawn.

  
_Derived Classes:_

_Namespace:[Rhino.Display](/api/rhinocommon/rhino.display)_  
_DisplayPipeline:[references](/api/rhinocommon/references/rhino.display.displaypipeline)_

 _keyboard_arrow_down_

Properties (28)

[**ActiveObject**
](/api/rhinocommon/rhino.display.displaypipeline/activeobject#)

* * *

[**ActiveObjectNestingLevel**
](/api/rhinocommon/rhino.display.displaypipeline/activeobjectnestinglevel#)

* * *

[**ActiveObjectNestingStack**
](/api/rhinocommon/rhino.display.displaypipeline/activeobjectnestingstack#)

* * *

[**ActiveTopLevelObject**
](/api/rhinocommon/rhino.display.displaypipeline/activetoplevelobject#)

* * *

[**DefaultCurveThickness** Gets the curve thickness as defined by the current
display mode. Note: this only applies to curve objects, Brep and Mesh wires
may have different
settings.](/api/rhinocommon/rhino.display.displaypipeline/defaultcurvethickness#)

* * *

[**DepthMode** ](/api/rhinocommon/rhino.display.displaypipeline/depthmode#)

* * *

[**DisplayPipelineAttributes**
](/api/rhinocommon/rhino.display.displaypipeline/displaypipelineattributes#)

* * *

[**DpiScale** Scale factor used for high resolution displays. When a monitor
that this pipeline is drawing to is at a DPI of 96, this value is one. On high
DPI monitors, this value will commonly be greater than
one.](/api/rhinocommon/rhino.display.displaypipeline/dpiscale#)

* * *

[**DrawingGrips** Gets a value that indicates whether the pipeline is
currently in a grip drawing
operation.](/api/rhinocommon/rhino.display.displaypipeline/drawinggrips#)

* * *

[**DrawingSurfaces** Gets a value that indicates whether the pipeline is
currently in a surface drawing operation. Surface drawing means draw the
shaded triangles of a mesh representing the surface (mesh, extrusion, or
brep). This is useful when inside of a draw event or display conduit to check
and see if the geometry is about to be drawn as a shaded set of triangles
representing the geometry. See DrawingWires to check and see if the wireframe
representation of the geometry is going to be
drawn.](/api/rhinocommon/rhino.display.displaypipeline/drawingsurfaces#)

* * *

[**DrawingWires** Gets a value that indicates whether the pipeline is
currently in a curve drawing operation. This is useful when inside of a draw
event or display conduit to check and see if the geometry is about to be drawn
is going to be drawing the wire representation of the geometry (mesh,
extrusion, or brep). See DrawingSurfaces to check and see if the shaded mesh
representation of the geometry is going to be
drawn.](/api/rhinocommon/rhino.display.displaypipeline/drawingwires#)

* * *

[**FrameBuffer** Gets the contents of the frame buffer that this pipeline is
drawing to.](/api/rhinocommon/rhino.display.displaypipeline/framebuffer#)

* * *

[**FrameSize** Gets the size of the frame buffer that this pipeline is drawing
to.](/api/rhinocommon/rhino.display.displaypipeline/framesize#)

* * *

[**IsDynamicDisplay** Gets a value that indicates whether the viewport is in
Dynamic Display state. Dynamic display is the state a viewport is in when it
is rapidly redrawing because of an operation like panning or rotating. The
pipeline will drop some level of detail while inside a dynamic display state
to keep the frame rate as high as
possible.](/api/rhinocommon/rhino.display.displaypipeline/isdynamicdisplay#)

* * *

[**IsInViewCapture** Gets a value that indicates whether this pipeline is
currently drawing for ViewCaptureToFile or
ViewCaptureToClipboard](/api/rhinocommon/rhino.display.displaypipeline/isinviewcapture#)

* * *

[**IsOpen** Is True of the pipeline is open, False
otherwise.](/api/rhinocommon/rhino.display.displaypipeline/isopen#)

* * *

[**IsOpenGL** Gets a value indicating whether or not this pipeline is drawing
into an OpenGL
context.](/api/rhinocommon/rhino.display.displaypipeline/isopengl#)

* * *

[**IsPrinting** Gets a value that indicates whether this pipeline is currently
drawing for printing
purposes.](/api/rhinocommon/rhino.display.displaypipeline/isprinting#)

* * *

[**IsStereoMode** Gets a value that indicates whether this pipeline is
currently using an engine that is performing stereo style drawing. Stereo
drawing is for providing an "enhanced 3-D" effect through stereo viewing
devices.](/api/rhinocommon/rhino.display.displaypipeline/isstereomode#)

* * *

[**ModelTransform** Gets or sets the current model transformation that is
applied to vertices when
drawing.](/api/rhinocommon/rhino.display.displaypipeline/modeltransform#)

* * *

[**ModelTransformIsIdentity** Gets a value that indicates whether the Model
Transform is an Identity
transformation.](/api/rhinocommon/rhino.display.displaypipeline/modeltransformisidentity#)

* * *

[**NestLevel** Gets the current nested viewport drawing level. This is used to
know if you are currently inside the drawing of a nested viewport (detail
object in Rhino).  
Nest level = 0 Drawing is occurring in a standard Rhino viewport or on the
page viewport.  
Nest level = 1 Drawing is occurring inside a detail view
object.](/api/rhinocommon/rhino.display.displaypipeline/nestlevel#)

* * *

[**RenderPass** Gets the current pass that the pipeline is in for drawing a
frame. Typically drawing a frame requires a single pass through the
DrawFrameBuffer function, but some special display effects can be achieved
through drawing with multiple
passes.](/api/rhinocommon/rhino.display.displaypipeline/renderpass#)

* * *

[**ShadingRequired** Gets or sets the "ShadingRequired" flag. This flag gets
set inside the pipeline when a request is made to draw a shaded mesh but the
current render engine doesn't support shaded mesh drawing...at this point the
redraw mechanism will make sure everything will work the next time
around.](/api/rhinocommon/rhino.display.displaypipeline/shadingrequired#)

* * *

[**StereoProjection** Gets the current stereo projection if stereo mode is on.  
0 = left  
1 = right If stereo mode is not enables, this property always returns
0.](/api/rhinocommon/rhino.display.displaypipeline/stereoprojection#)

* * *

[**SupportsShading** Gets whether or not this pipeline supports shaded
meshes.](/api/rhinocommon/rhino.display.displaypipeline/supportsshading#)

* * *

[**Viewport** ](/api/rhinocommon/rhino.display.displaypipeline/viewport#)

* * *

[**ZBiasMode** ](/api/rhinocommon/rhino.display.displaypipeline/zbiasmode#)

* * *

_keyboard_arrow_down_

Methods (185)

[**AddClippingPlane**(Point3d point, Vector3d normal) Add a clipping plane to
be used during the drawing of this
frame](/api/rhinocommon/rhino.display.displaypipeline/addclippingplane#\(point3d,vector3d\))

* * *

[**AvailableOpenGLVersion**(Boolean coreProfile) If Rhino is using OpenGL for
display, this function will return major.minor version of OpenGL available for
this instance of
Rhino](/api/rhinocommon/rhino.display.displaypipeline/availableopenglversion#\(out\))

* * *

[**ClearFrameBuffer**(Color color) Fill the frame buffer with a single color.
This function also clears the depth buffer for engines that support depth
buffered
drawing.](/api/rhinocommon/rhino.display.displaypipeline/clearframebuffer#\(color\))

* * *

[**Clone**(RhinoViewport viewport) Clones the pipeline. Creates an identical
copy of "this" pipeline. Copies all conduits from "this" pipeline to the new
pipeline.](/api/rhinocommon/rhino.display.displaypipeline/clone#\(rhinoviewport\))

* * *

[**Close**() Closes the
pipeline.](/api/rhinocommon/rhino.display.displaypipeline/close#\(\))

* * *

[**CullControlPolygon**() Returns a value indicating if only points on the
side of the surface that face the camera are
displayed.](/api/rhinocommon/rhino.display.displaypipeline/cullcontrolpolygon#\(\))

* * *

[**Draw2dLine**(Point from,Point to,Color color,Single thickness)
](/api/rhinocommon/rhino.display.displaypipeline/draw2dline#\(point,point,color,single\))

* * *

[**Draw2dLine**(PointF from,PointF to,Color color,Single thickness)
](/api/rhinocommon/rhino.display.displaypipeline/draw2dline#\(pointf,pointf,color,single\))

* * *

[**Draw2dRectangle**(Rectangle rectangle,Color strokeColor,Int32
thickness,Color fillColor)
](/api/rhinocommon/rhino.display.displaypipeline/draw2drectangle#\(rectangle,color,int32,color\))

* * *

[**Draw2dText**(String text,Color color, Point2d screenCoordinate,Boolean
middleJustified,Int32 height,String fontface) Draws 2D text on the
viewport.](/api/rhinocommon/rhino.display.displaypipeline/draw2dtext#\(string,color,point2d,boolean,int32,string\))

* * *

[**Draw2dText**(String text,Color color, Point2d screenCoordinate,Boolean
middleJustified,Int32 height) Draws 2D text on the
viewport.](/api/rhinocommon/rhino.display.displaypipeline/draw2dtext#\(string,color,point2d,boolean,int32\))

* * *

[**Draw2dText**(String text,Color color, Point2d screenCoordinate,Boolean
middleJustified) Draws 2D text on the
viewport.](/api/rhinocommon/rhino.display.displaypipeline/draw2dtext#\(string,color,point2d,boolean\))

* * *

[**Draw2dText**(String text,Color color, Point3d worldCoordinate,Boolean
middleJustified,Int32 height,String fontface) Draws 2D text on the
viewport.](/api/rhinocommon/rhino.display.displaypipeline/draw2dtext#\(string,color,point3d,boolean,int32,string\))

* * *

[**Draw2dText**(String text,Color color, Point3d worldCoordinate,Boolean
middleJustified,Int32 height) Draws 2D text on the
viewport.](/api/rhinocommon/rhino.display.displaypipeline/draw2dtext#\(string,color,point3d,boolean,int32\))

* * *

[**Draw2dText**(String text,Color color, Point3d worldCoordinate,Boolean
middleJustified) Draws 2D text on the
viewport.](/api/rhinocommon/rhino.display.displaypipeline/draw2dtext#\(string,color,point3d,boolean\))

* * *

[**Draw3dText**(String text,Color color, Plane textPlane,Double height,String
fontface,Boolean bold,Boolean italic,TextHorizontalAlignment
horizontalAlignment,TextVerticalAlignment verticalAlignment)
](/api/rhinocommon/rhino.display.displaypipeline/draw3dtext#\(string,color,plane,double,string,boolean,boolean,texthorizontalalignment,textverticalalignment\))

* * *

[**Draw3dText**(String text,Color color, Plane textPlane,Double height,String
fontface,Boolean bold,Boolean italic)
](/api/rhinocommon/rhino.display.displaypipeline/draw3dtext#\(string,color,plane,double,string,boolean,boolean\))

* * *

[**Draw3dText**(String text,Color color, Plane textPlane,Double height,String
fontface)
](/api/rhinocommon/rhino.display.displaypipeline/draw3dtext#\(string,color,plane,double,string\))

* * *

[**Draw3dText**(Text3d text,Color color, Plane textPlane) Draws 3d text with a
different plane than what is defined in the Text3d
class.](/api/rhinocommon/rhino.display.displaypipeline/draw3dtext#\(text3d,color,plane\))

* * *

[**Draw3dText**(Text3d text,Color color, Point3d textPlaneOrigin) Draws 3d
text using the Text3d plane with an adjusted
origin.](/api/rhinocommon/rhino.display.displaypipeline/draw3dtext#\(text3d,color,point3d\))

* * *

[**Draw3dText**(Text3d text,Color color)
](/api/rhinocommon/rhino.display.displaypipeline/draw3dtext#\(text3d,color\))

* * *

[**DrawActivePoint**(Point3d point) Draws a point in style used during
"GetPoint"
operations](/api/rhinocommon/rhino.display.displaypipeline/drawactivepoint#\(point3d\))

* * *

[**DrawAnnotation**(AnnotationBase annotation,Color color)
](/api/rhinocommon/rhino.display.displaypipeline/drawannotation#\(annotationbase,color\))

* * *

[**DrawAnnotationArrowhead**(Arrowhead arrowhead, Transform xform,Color color)
](/api/rhinocommon/rhino.display.displaypipeline/drawannotationarrowhead#\(arrowhead,transform,color\))

* * *

[**DrawArc**(Arc arc,Color color,Int32 thickness) Draw a single arc
object.](/api/rhinocommon/rhino.display.displaypipeline/drawarc#\(arc,color,int32\))

* * *

[**DrawArc**(Arc arc,Color color) Draw a single arc
object.](/api/rhinocommon/rhino.display.displaypipeline/drawarc#\(arc,color\))

* * *

[**DrawArrow**(Line line,Color color,Double screenSize,Double relativeSize)
Draws a single arrow object. An arrow consists of a Shaft and an Arrow head at
the end of the
shaft.](/api/rhinocommon/rhino.display.displaypipeline/drawarrow#\(line,color,double,double\))

* * *

[**DrawArrow**(Line line,Color color) Draws a single arrow object. An arrow
consists of a Shaft and an Arrow head at the end of the
shaft.](/api/rhinocommon/rhino.display.displaypipeline/drawarrow#\(line,color\))

* * *

[**DrawArrowHead**(Point3d tip, Vector3d direction,Color color,Double
screenSize,Double worldSize) Draws a single arrow
head.](/api/rhinocommon/rhino.display.displaypipeline/drawarrowhead#\(point3d,vector3d,color,double,double\))

* * *

[**DrawArrows**(IEnumerable<Line> lines,Color color) Draws a collection of
arrow objects. An arrow consists of a Shaft and an Arrow head at the end of
the
shaft.](/api/rhinocommon/rhino.display.displaypipeline/drawarrows#\(ienumerable<line>,color\))

* * *

[**DrawArrows**(Line[] lines,Color color) Draws a collection of arrow objects.
An arrow consists of a Shaft and an Arrow head at the end of the
shaft.](/api/rhinocommon/rhino.display.displaypipeline/drawarrows#\(line\[\],color\))

* * *

[**DrawBitmap**(DisplayBitmap bitmap,Int32 left,Int32 top) Draws a bitmap in
screen
coordinates](/api/rhinocommon/rhino.display.displaypipeline/drawbitmap#\(displaybitmap,int32,int32\))

* * *

[**DrawBox**(BoundingBox box,Color color,Int32 thickness) Draws the edges of a
BoundingBox.](/api/rhinocommon/rhino.display.displaypipeline/drawbox#\(boundingbox,color,int32\))

* * *

[**DrawBox**(BoundingBox box,Color color) Draws the edges of a
BoundingBox.](/api/rhinocommon/rhino.display.displaypipeline/drawbox#\(boundingbox,color\))

* * *

[**DrawBox**(Box box,Color color,Int32 thickness) Draws the edges of a Box
object.](/api/rhinocommon/rhino.display.displaypipeline/drawbox#\(box,color,int32\))

* * *

[**DrawBox**(Box box,Color color) Draws the edges of a Box
object.](/api/rhinocommon/rhino.display.displaypipeline/drawbox#\(box,color\))

* * *

[**DrawBoxCorners**(BoundingBox box,Color color,Double size,Int32 thickness)
Draws corner widgets of a world aligned bounding
box.](/api/rhinocommon/rhino.display.displaypipeline/drawboxcorners#\(boundingbox,color,double,int32\))

* * *

[**DrawBoxCorners**(BoundingBox box,Color color,Double size) Draws corner
widgets of a world aligned bounding
box.](/api/rhinocommon/rhino.display.displaypipeline/drawboxcorners#\(boundingbox,color,double\))

* * *

[**DrawBoxCorners**(BoundingBox box,Color color) Draws corner widgets of a
world aligned bounding box. Widget size will be 5% of the Box
diagonal.](/api/rhinocommon/rhino.display.displaypipeline/drawboxcorners#\(boundingbox,color\))

* * *

[**DrawBrepShaded**(Brep brep, DisplayMaterial material) Draws a shaded mesh
representation of a
brep.](/api/rhinocommon/rhino.display.displaypipeline/drawbrepshaded#\(brep,displaymaterial\))

* * *

[**DrawBrepWires**(Brep brep,Color color,Int32 wireDensity) Draws all the
wireframe curves of a brep
object.](/api/rhinocommon/rhino.display.displaypipeline/drawbrepwires#\(brep,color,int32\))

* * *

[**DrawBrepWires**(Brep brep,Color color) Draws all the wireframe curves of a
brep
object.](/api/rhinocommon/rhino.display.displaypipeline/drawbrepwires#\(brep,color\))

* * *

[**DrawCircle**(Circle circle,Color color,Int32 thickness) Draw a single
circle
object.](/api/rhinocommon/rhino.display.displaypipeline/drawcircle#\(circle,color,int32\))

* * *

[**DrawCircle**(Circle circle,Color color) Draw a single circle
object.](/api/rhinocommon/rhino.display.displaypipeline/drawcircle#\(circle,color\))

* * *

[**DrawCone**(Cone cone,Color color,Int32 thickness) Draw a wireframe
cone.](/api/rhinocommon/rhino.display.displaypipeline/drawcone#\(cone,color,int32\))

* * *

[**DrawCone**(Cone cone,Color color) Draw a wireframe
cone.](/api/rhinocommon/rhino.display.displaypipeline/drawcone#\(cone,color\))

* * *

[**DrawConstructionPlane**(ConstructionPlane constructionPlane) Draws a
construction
plane.](/api/rhinocommon/rhino.display.displaypipeline/drawconstructionplane#\(constructionplane\))

* * *

[**DrawCurvatureGraph**(Curve curve,Color color,Int32 hairScale,Int32
hairDensity,Int32 sampleDensity) Draw a typical Rhino Curvature
Graph.](/api/rhinocommon/rhino.display.displaypipeline/drawcurvaturegraph#\(curve,color,int32,int32,int32\))

* * *

[**DrawCurvatureGraph**(Curve curve,Color color,Int32 hairScale) Draw a
typical Rhino Curvature
Graph.](/api/rhinocommon/rhino.display.displaypipeline/drawcurvaturegraph#\(curve,color,int32\))

* * *

[**DrawCurvatureGraph**(Curve curve,Color color) Draw a typical Rhino
Curvature
Graph.](/api/rhinocommon/rhino.display.displaypipeline/drawcurvaturegraph#\(curve,color\))

* * *

[**DrawCurve**(Curve curve, DisplayPen pen)
](/api/rhinocommon/rhino.display.displaypipeline/drawcurve#\(curve,displaypen\))

* * *

[**DrawCurve**(Curve curve,Color color,Int32 thickness) Draw a single Curve
object.](/api/rhinocommon/rhino.display.displaypipeline/drawcurve#\(curve,color,int32\))

* * *

[**DrawCurve**(Curve curve,Color color) Draw a single Curve
object.](/api/rhinocommon/rhino.display.displaypipeline/drawcurve#\(curve,color\))

* * *

[**DrawCylinder**(Cylinder cylinder,Color color,Int32 thickness) Draw a
wireframe
cylinder.](/api/rhinocommon/rhino.display.displaypipeline/drawcylinder#\(cylinder,color,int32\))

* * *

[**DrawCylinder**(Cylinder cylinder,Color color) Draw a wireframe
cylinder.](/api/rhinocommon/rhino.display.displaypipeline/drawcylinder#\(cylinder,color\))

* * *

[**DrawDirectionArrow**(Point3d location, Vector3d direction,Color color)
](/api/rhinocommon/rhino.display.displaypipeline/drawdirectionarrow#\(point3d,vector3d,color\))

* * *

[**DrawDot**(Point3d worldPosition,String text,Color dotColor,Color textColor)
Draw a text dot in world
coordinates.](/api/rhinocommon/rhino.display.displaypipeline/drawdot#\(point3d,string,color,color\))

* * *

[**DrawDot**(Point3d worldPosition,String text) Draws a text dot in world
coordinates.](/api/rhinocommon/rhino.display.displaypipeline/drawdot#\(point3d,string\))

* * *

[**DrawDot**(Single screenX,Single screenY,String text,Color dotColor,Color
textColor) Draws a text dot in screen
coordinates.](/api/rhinocommon/rhino.display.displaypipeline/drawdot#\(single,single,string,color,color\))

* * *

[**DrawDot**(Single screenX,Single screenY,String text) Draws a text dot in
screen
coordinates.](/api/rhinocommon/rhino.display.displaypipeline/drawdot#\(single,single,string\))

* * *

[**DrawDot**(TextDot dot,Color fillColor,Color textColor,Color borderColor)
Draw a text dot as defined by the text dot
class](/api/rhinocommon/rhino.display.displaypipeline/drawdot#\(textdot,color,color,color\))

* * *

[**DrawDottedLine**(Line line,Color color) Draws a single dotted
line.](/api/rhinocommon/rhino.display.displaypipeline/drawdottedline#\(line,color\))

* * *

[**DrawDottedLine**(Point3d from, Point3d to,Color color) Draws a single
dotted
line.](/api/rhinocommon/rhino.display.displaypipeline/drawdottedline#\(point3d,point3d,color\))

* * *

[**DrawDottedPolyline**(IEnumerable<Point3d> points,Color color,Boolean close)
Draws a set of connected lines (polyline) in a dotted pattern
(0x00001111).](/api/rhinocommon/rhino.display.displaypipeline/drawdottedpolyline#\(ienumerable<point3d>,color,boolean\))

* * *

[**DraweInferencePoint**(Point3d P, Color color) Draw inference point used in
gesture based
snapping](/api/rhinocommon/rhino.display.displaypipeline/draweinferencepoint#\(point3d,color\))

* * *

[**DrawExtrusionWires**(Extrusion extrusion,Color color,Int32 wireDensity)
Draws all the wireframe curves of an extrusion
object.](/api/rhinocommon/rhino.display.displaypipeline/drawextrusionwires#\(extrusion,color,int32\))

* * *

[**DrawExtrusionWires**(Extrusion extrusion,Color color) Draws all the
wireframe curves of an extrusion
object.](/api/rhinocommon/rhino.display.displaypipeline/drawextrusionwires#\(extrusion,color\))

* * *

[**DrawGradientHatch**(Hatch hatch, IEnumerable<ColorStop> stops, Point3d
point1, Point3d point2,Boolean linearGradient,Single repeat, DisplayPen
boundary,Color backgroundFillColor)
](/api/rhinocommon/rhino.display.displaypipeline/drawgradienthatch#\(hatch,ienumerable<colorstop>,point3d,point3d,boolean,single,displaypen,color\))

* * *

[**DrawGradientHatch**(Hatch hatch, IEnumerable<ColorStop> stops, Point3d
point1, Point3d point2,Boolean linearGradient,Single repeat,Single
boundaryThickness,Color boundaryColor)
](/api/rhinocommon/rhino.display.displaypipeline/drawgradienthatch#\(hatch,ienumerable<colorstop>,point3d,point3d,boolean,single,single,color\))

* * *

[**DrawGradientHatch**(Hatch hatch,Color color1,Color color2, Point3d point1,
Point3d point2,Boolean linearGradient,Single boundaryThickness,Color
boundaryColor) Draw a two point gradient filled
hatch](/api/rhinocommon/rhino.display.displaypipeline/drawgradienthatch#\(hatch,color,color,point3d,point3d,boolean,single,color\))

* * *

[**DrawGradientLines**(IEnumerable<Line> lines,Single strokeWidth,
IEnumerable<ColorStop> stops, Point3d point1, Point3d point2,Boolean
linearGradient,Single repeat)
](/api/rhinocommon/rhino.display.displaypipeline/drawgradientlines#\(ienumerable<line>,single,ienumerable<colorstop>,point3d,point3d,boolean,single\))

* * *

[**DrawGradientMesh**(Mesh mesh, IEnumerable<ColorStop> stops, Point3d point1,
Point3d point2,Boolean linearGradient,Single repeat)
](/api/rhinocommon/rhino.display.displaypipeline/drawgradientmesh#\(mesh,ienumerable<colorstop>,point3d,point3d,boolean,single\))

* * *

[**DrawHatch**(Hatch hatch,Color hatchColor, DisplayPen boundary,Color
backgroundFillColor)
](/api/rhinocommon/rhino.display.displaypipeline/drawhatch#\(hatch,color,displaypen,color\))

* * *

[**DrawHatch**(Hatch hatch,Color hatchColor,Color boundaryColor)
](/api/rhinocommon/rhino.display.displaypipeline/drawhatch#\(hatch,color,color\))

* * *

[**DrawInferenceLine**(Point3d P, Point3d O, Color color, InferenceLineType
type) Draw an inference line used in gesture based
snapping](/api/rhinocommon/rhino.display.displaypipeline/drawinferenceline#\(point3d,point3d,color,inferencelinetype\))

* * *

[**DrawInstanceDefinition**(InstanceDefinition instanceDefinition, Transform
xform) Draws an <b>DocObjects.InstanceDefinition</b>
.](/api/rhinocommon/rhino.display.displaypipeline/drawinstancedefinition#\(instancedefinition,transform\))

* * *

[**DrawInstanceDefinition**(InstanceDefinition instanceDefinition) Draws an
<b>DocObjects.InstanceDefinition</b>
.](/api/rhinocommon/rhino.display.displaypipeline/drawinstancedefinition#\(instancedefinition\))

* * *

[**DrawLight**(Light light,Color wireframeColor) Draws a
light.](/api/rhinocommon/rhino.display.displaypipeline/drawlight#\(light,color\))

* * *

[**DrawLine**(Line line, DisplayPen pen)
](/api/rhinocommon/rhino.display.displaypipeline/drawline#\(line,displaypen\))

* * *

[**DrawLine**(Line line,Color color,Int32 thickness) Draws a single line
object.](/api/rhinocommon/rhino.display.displaypipeline/drawline#\(line,color,int32\))

* * *

[**DrawLine**(Line line,Color color) Draws a single line
object.](/api/rhinocommon/rhino.display.displaypipeline/drawline#\(line,color\))

* * *

[**DrawLine**(Point3d from, Point3d to,Color color,Int32 thickness) Draws a
single line
object.](/api/rhinocommon/rhino.display.displaypipeline/drawline#\(point3d,point3d,color,int32\))

* * *

[**DrawLine**(Point3d from, Point3d to,Color color) Draws a single line
object.](/api/rhinocommon/rhino.display.displaypipeline/drawline#\(point3d,point3d,color\))

* * *

[**DrawLineArrow**(Line line,Color color,Int32 thickness,Double size) Draws an
arrow made up of three line
segments.](/api/rhinocommon/rhino.display.displaypipeline/drawlinearrow#\(line,color,int32,double\))

* * *

[**DrawLineNoClip**(Point3d from, Point3d to,Color color,Int32 thickness)
Draws a single line object .This version of line drawing will draw the
segments of the line that extend beyond the near and far planes of the view
frustum with depths on those
planes](/api/rhinocommon/rhino.display.displaypipeline/drawlinenoclip#\(point3d,point3d,color,int32\))

* * *

[**DrawLines**(IEnumerable<Line> lines,Color color,Int32 thickness) Draws a
set of lines with a given color and thickness. If you want the fastest
possible set of lines to be drawn, pass a Line[] for
lines.](/api/rhinocommon/rhino.display.displaypipeline/drawlines#\(ienumerable<line>,color,int32\))

* * *

[**DrawLines**(IEnumerable<Line> lines,Color color) Draws a set of lines with
a given color and thickness. If you want the fastest possible set of lines to
be drawn, pass a Line[] for
lines.](/api/rhinocommon/rhino.display.displaypipeline/drawlines#\(ienumerable<line>,color\))

* * *

[**DrawLines**(Line[] lines, DisplayPen pen)
](/api/rhinocommon/rhino.display.displaypipeline/drawlines#\(line\[\],displaypen\))

* * *

[**DrawLinesNoClip**(IEnumerable<Line> lines,Color color,Int32 thickness)
Draws a multiple lines. This version of line drawing will draw the segments of
the line that extend beyond the near and far planes of the view frustum with
depths on those
planes](/api/rhinocommon/rhino.display.displaypipeline/drawlinesnoclip#\(ienumerable<line>,color,int32\))

* * *

[**DrawMarker**(Point3d tip, Vector3d direction,Color color,Int32
thickness,Double size,Double rotation) Draws an arrow marker as a view-aligned
widget.](/api/rhinocommon/rhino.display.displaypipeline/drawmarker#\(point3d,vector3d,color,int32,double,double\))

* * *

[**DrawMarker**(Point3d tip, Vector3d direction,Color color,Int32
thickness,Double size) Draws an arrow marker as a view-aligned
widget.](/api/rhinocommon/rhino.display.displaypipeline/drawmarker#\(point3d,vector3d,color,int32,double\))

* * *

[**DrawMarker**(Point3d tip, Vector3d direction,Color color,Int32 thickness)
Draws an arrow marker as a view-aligned
widget.](/api/rhinocommon/rhino.display.displaypipeline/drawmarker#\(point3d,vector3d,color,int32\))

* * *

[**DrawMarker**(Point3d tip, Vector3d direction,Color color) Draws an arrow
marker as a view-aligned
widget.](/api/rhinocommon/rhino.display.displaypipeline/drawmarker#\(point3d,vector3d,color\))

* * *

[**DrawMeshFalseColors**(Mesh mesh) Draws the mesh faces as False color
patches. The mesh must have Vertex Colors defined for this to
work.](/api/rhinocommon/rhino.display.displaypipeline/drawmeshfalsecolors#\(mesh\))

* * *

[**DrawMeshShaded**(Mesh mesh, DisplayMaterial material, IEnumerable<int>
faceIndices) Draws the shaded faces of a given
mesh.](/api/rhinocommon/rhino.display.displaypipeline/drawmeshshaded#\(mesh,displaymaterial,ienumerable<int>\))

* * *

[**DrawMeshShaded**(Mesh mesh, DisplayMaterial material,Int32[] faceIndices)
Draws the shaded faces of a given
mesh.](/api/rhinocommon/rhino.display.displaypipeline/drawmeshshaded#\(mesh,displaymaterial,int32\[\]\))

* * *

[**DrawMeshShaded**(Mesh mesh, DisplayMaterial material) Draws the shaded
faces of a given
mesh.](/api/rhinocommon/rhino.display.displaypipeline/drawmeshshaded#\(mesh,displaymaterial\))

* * *

[**DrawMeshVertices**(Mesh mesh,Color color) Draws all the vertices in a given
mesh.](/api/rhinocommon/rhino.display.displaypipeline/drawmeshvertices#\(mesh,color\))

* * *

[**DrawMeshWires**(Mesh mesh,Color color,Int32 thickness) Draws all the wires
in a given
mesh.](/api/rhinocommon/rhino.display.displaypipeline/drawmeshwires#\(mesh,color,int32\))

* * *

[**DrawMeshWires**(Mesh mesh,Color color) Draws all the wires in a given
mesh.](/api/rhinocommon/rhino.display.displaypipeline/drawmeshwires#\(mesh,color\))

* * *

[**DrawObject**(RhinoObject rhinoObject, Transform xform) Draws a
<b>DocObjects.RhinoObject</b> with an applied
transformation.](/api/rhinocommon/rhino.display.displaypipeline/drawobject#\(rhinoobject,transform\))

* * *

[**DrawObject**(RhinoObject rhinoObject) Draws a <b>DocObjects.RhinoObject</b>
.](/api/rhinocommon/rhino.display.displaypipeline/drawobject#\(rhinoobject\))

* * *

[**DrawParticles**(ParticleSystem particles, DisplayBitmap bitmap)
](/api/rhinocommon/rhino.display.displaypipeline/drawparticles#\(particlesystem,displaybitmap\))

* * *

[**DrawParticles**(ParticleSystem particles, DisplayBitmap[] bitmaps)
](/api/rhinocommon/rhino.display.displaypipeline/drawparticles#\(particlesystem,displaybitmap\[\]\))

* * *

[**DrawParticles**(ParticleSystem particles)
](/api/rhinocommon/rhino.display.displaypipeline/drawparticles#\(particlesystem\))

* * *

[**DrawPatternedLine**(Line line,Color color,Int32 pattern,Int32 thickness)
Draws a single line with specified
pattern.](/api/rhinocommon/rhino.display.displaypipeline/drawpatternedline#\(line,color,int32,int32\))

* * *

[**DrawPatternedLine**(Point3d from, Point3d to,Color color,Int32
pattern,Int32 thickness) Draws a single line with specified
pattern.](/api/rhinocommon/rhino.display.displaypipeline/drawpatternedline#\(point3d,point3d,color,int32,int32\))

* * *

[**DrawPatternedPolyline**(IEnumerable<Point3d> points,Color color,Int32
pattern,Int32 thickness,Boolean close) Draws a set of connected lines
(polyline) with specified
pattern.](/api/rhinocommon/rhino.display.displaypipeline/drawpatternedpolyline#\(ienumerable<point3d>,color,int32,int32,boolean\))

* * *

[**DrawPoint**(Point3d point, PointStyle style,Color strokeColor,Color
fillColor,Single radius,Single strokeWidth,Single secondarySize,Single
rotationRadians,Boolean diameterIsInPixels,Boolean autoScaleForDpi)
](/api/rhinocommon/rhino.display.displaypipeline/drawpoint#\(point3d,pointstyle,color,color,single,single,single,single,boolean,boolean\))

* * *

[**DrawPoint**(Point3d point, PointStyle style,Int32 radius,Color color) Draws
a point with a given radius, style and
color.](/api/rhinocommon/rhino.display.displaypipeline/drawpoint#\(point3d,pointstyle,int32,color\))

* * *

[**DrawPoint**(Point3d point, PointStyle style,Single radius,Color color)
Draws a point with a given radius, style and
color.](/api/rhinocommon/rhino.display.displaypipeline/drawpoint#\(point3d,pointstyle,single,color\))

* * *

[**DrawPoint**(Point3d point,Color color) Draws a point with a given radius,
style and
color.](/api/rhinocommon/rhino.display.displaypipeline/drawpoint#\(point3d,color\))

* * *

[**DrawPoint**(Point3d point) Draws a point using the current display
attribute size, style and
color](/api/rhinocommon/rhino.display.displaypipeline/drawpoint#\(point3d\))

* * *

[**DrawPointCloud**(PointCloud cloud,Int32 size,Color color) Draws a point
cloud.](/api/rhinocommon/rhino.display.displaypipeline/drawpointcloud#\(pointcloud,int32,color\))

* * *

[**DrawPointCloud**(PointCloud cloud,Int32 size) Draws a point
cloud.](/api/rhinocommon/rhino.display.displaypipeline/drawpointcloud#\(pointcloud,int32\))

* * *

[**DrawPointCloud**(PointCloud cloud,Single size,Color color) Draws a point
cloud.](/api/rhinocommon/rhino.display.displaypipeline/drawpointcloud#\(pointcloud,single,color\))

* * *

[**DrawPointCloud**(PointCloud cloud,Single size) Draws a point
cloud.](/api/rhinocommon/rhino.display.displaypipeline/drawpointcloud#\(pointcloud,single\))

* * *

[**DrawPoints**(DisplayPointSet points, DisplayPointAttributes
fallbackAttributes, DisplayPointAttributes overrideAttributes)
](/api/rhinocommon/rhino.display.displaypipeline/drawpoints#\(displaypointset,displaypointattributes,displaypointattributes\))

* * *

[**DrawPoints**(DisplayPointSet points)
](/api/rhinocommon/rhino.display.displaypipeline/drawpoints#\(displaypointset\))

* * *

[**DrawPoints**(IEnumerable<Point3d> points, PointStyle style,Color
strokeColor,Color fillColor,Single radius,Single strokeWidth,Single
secondarySize,Single rotationRadians,Boolean diameterIsInPixels,Boolean
autoScaleForDpi)
](/api/rhinocommon/rhino.display.displaypipeline/drawpoints#\(ienumerable<point3d>,pointstyle,color,color,single,single,single,single,boolean,boolean\))

* * *

[**DrawPoints**(IEnumerable<Point3d> points, PointStyle style,Int32
radius,Color color) Draw a set of points with a given radius, style and
color.](/api/rhinocommon/rhino.display.displaypipeline/drawpoints#\(ienumerable<point3d>,pointstyle,int32,color\))

* * *

[**DrawPoints**(IEnumerable<Point3d> points, PointStyle style,Single
radius,Color color) Draw a set of points with a given radius, style and
color.](/api/rhinocommon/rhino.display.displaypipeline/drawpoints#\(ienumerable<point3d>,pointstyle,single,color\))

* * *

[**DrawPolygon**(IEnumerable<Point3d> points,Color color,Boolean filled) Draws
a filled, convex polygon from a collection of
points.](/api/rhinocommon/rhino.display.displaypipeline/drawpolygon#\(ienumerable<point3d>,color,boolean\))

* * *

[**DrawPolyline**(IEnumerable<Point3d> polyline,Color color,Int32 thickness)
Draws a single Polyline
object.](/api/rhinocommon/rhino.display.displaypipeline/drawpolyline#\(ienumerable<point3d>,color,int32\))

* * *

[**DrawPolyline**(IEnumerable<Point3d> polyline,Color color) Draws a single
Polyline
object.](/api/rhinocommon/rhino.display.displaypipeline/drawpolyline#\(ienumerable<point3d>,color\))

* * *

[**DrawRoundedRectangle**(PointF center,Single pixelWidth,Single
pixelHeight,Single cornerRadius,Color strokeColor,Single strokeWidth,Color
fillColor)
](/api/rhinocommon/rhino.display.displaypipeline/drawroundedrectangle#\(pointf,single,single,single,color,single,color\))

* * *

[**DrawSphere**(Sphere sphere,Color color,Int32 thickness) Draw a wireframe
sphere.](/api/rhinocommon/rhino.display.displaypipeline/drawsphere#\(sphere,color,int32\))

* * *

[**DrawSphere**(Sphere sphere,Color color) Draw a wireframe
sphere.](/api/rhinocommon/rhino.display.displaypipeline/drawsphere#\(sphere,color\))

* * *

[**DrawSprite**(DisplayBitmap bitmap, Point2d screenLocation,Single size,Color
blendColor)
](/api/rhinocommon/rhino.display.displaypipeline/drawsprite#\(displaybitmap,point2d,single,color\))

* * *

[**DrawSprite**(DisplayBitmap bitmap, Point2d screenLocation,Single size)
](/api/rhinocommon/rhino.display.displaypipeline/drawsprite#\(displaybitmap,point2d,single\))

* * *

[**DrawSprite**(DisplayBitmap bitmap, Point2d screenLocation,Single
width,Single height) Draw screen oriented image centered at 2d screen
location](/api/rhinocommon/rhino.display.displaypipeline/drawsprite#\(displaybitmap,point2d,single,single\))

* * *

[**DrawSprite**(DisplayBitmap bitmap, Point3d worldLocation,Single
size,Boolean sizeInWorldSpace)
](/api/rhinocommon/rhino.display.displaypipeline/drawsprite#\(displaybitmap,point3d,single,boolean\))

* * *

[**DrawSprite**(DisplayBitmap bitmap, Point3d worldLocation,Single size,Color
blendColor,Boolean sizeInWorldSpace)
](/api/rhinocommon/rhino.display.displaypipeline/drawsprite#\(displaybitmap,point3d,single,color,boolean\))

* * *

[**DrawSprites**(DisplayBitmap bitmap, DisplayBitmapDrawList items,Single
size,Boolean sizeInWorldSpace)
](/api/rhinocommon/rhino.display.displaypipeline/drawsprites#\(displaybitmap,displaybitmapdrawlist,single,boolean\))

* * *

[**DrawSprites**(DisplayBitmap bitmap, DisplayBitmapDrawList items,Single
size, Vector3d translation,Boolean sizeInWorldSpace)
](/api/rhinocommon/rhino.display.displaypipeline/drawsprites#\(displaybitmap,displaybitmapdrawlist,single,vector3d,boolean\))

* * *

[**DrawStereoFrameBuffer**(ViewportInfo viewportLeft,ViewportInfo
viewportRight,UInt32 handleLeft,UInt32 handleRight) Draws the viewport as seen
from the left and the right eye viewports and returns the result as OpenGL
texture
handles.](/api/rhinocommon/rhino.display.displaypipeline/drawstereoframebuffer#\(viewportinfo,viewportinfo,out,out\))

* * *

[**DrawSubDShaded**(SubD subd, DisplayMaterial material) Draw a shaded mesh
representation of a
SubD](/api/rhinocommon/rhino.display.displaypipeline/drawsubdshaded#\(subd,displaymaterial\))

* * *

[**DrawSubDWires**(SubD subd, DisplayPen boundaryPen, DisplayPen
smoothInteriorPen, DisplayPen creasePen, DisplayPen nonmanifoldPen) Draws all
the wireframe curves os a SubD object using different
pens](/api/rhinocommon/rhino.display.displaypipeline/drawsubdwires#\(subd,displaypen,displaypen,displaypen,displaypen\))

* * *

[**DrawSubDWires**(SubD subd,Color color,Single thickness) Draws all the
wireframe curves of a SubD
object](/api/rhinocommon/rhino.display.displaypipeline/drawsubdwires#\(subd,color,single\))

* * *

[**DrawSurface**(Surface surface,Color wireColor,Int32 wireDensity) Draw
wireframe display for a single
surface.](/api/rhinocommon/rhino.display.displaypipeline/drawsurface#\(surface,color,int32\))

* * *

[**DrawText**(TextEntity text,Color color,Double scale)
](/api/rhinocommon/rhino.display.displaypipeline/drawtext#\(textentity,color,double\))

* * *

[**DrawText**(TextEntity text,Color color, Transform xform)
](/api/rhinocommon/rhino.display.displaypipeline/drawtext#\(textentity,color,transform\))

* * *

[**DrawText**(TextEntity text,Color color)
](/api/rhinocommon/rhino.display.displaypipeline/drawtext#\(textentity,color\))

* * *

[**DrawToBitmap**(RhinoViewport viewport,Int32 width,Int32 height) Draw a
given viewport to an off-screen
bitmap.](/api/rhinocommon/rhino.display.displaypipeline/drawtobitmap#\(rhinoviewport,int32,int32\))

* * *

[**DrawTorus**(Torus torus,Color color,Int32 thickness) Draw a wireframe
torus.](/api/rhinocommon/rhino.display.displaypipeline/drawtorus#\(torus,color,int32\))

* * *

[**DrawTorus**(Torus torus,Color color) Draw a wireframe
torus.](/api/rhinocommon/rhino.display.displaypipeline/drawtorus#\(torus,color\))

* * *

[**DrawZebraPreview**(Brep brep,Color color) Draws a shaded Brep with Zebra
stripe
preview.](/api/rhinocommon/rhino.display.displaypipeline/drawzebrapreview#\(brep,color\))

* * *

[**DrawZebraPreview**(Mesh mesh,Color color) Draws a shaded Mesh with Zebra
stripe
preview.](/api/rhinocommon/rhino.display.displaypipeline/drawzebrapreview#\(mesh,color\))

* * *

[**EnableClippingPlanes**(Boolean enable) Enable or disable the Clipping Plane
logic of the
engine.](/api/rhinocommon/rhino.display.displaypipeline/enableclippingplanes#\(boolean\))

* * *

[**EnableColorWriting**(Boolean enable) Enable or disable the ColorWriting
behavior of the
engine.](/api/rhinocommon/rhino.display.displaypipeline/enablecolorwriting#\(boolean\))

* * *

[**EnableDepthTesting**(Boolean enable) Enable or disable the DepthTesting
behavior of the engine. When DepthTesting is disabled, objects in front will
no longer occlude objects behind
them.](/api/rhinocommon/rhino.display.displaypipeline/enabledepthtesting#\(boolean\))

* * *

[**EnableDepthWriting**(Boolean enable) Enable or disable the DepthWriting
behavior of the engine. When DepthWriting is disabled, drawn geometry does not
affect the
Z-Buffer.](/api/rhinocommon/rhino.display.displaypipeline/enabledepthwriting#\(boolean\))

* * *

[**EnableLighting**(Boolean enable) Enable or disable the Lighting logic of
the
engine.](/api/rhinocommon/rhino.display.displaypipeline/enablelighting#\(boolean\))

* * *

[**Flush**() Force the pipeline to immediately flush any cached geometry to
the display](/api/rhinocommon/rhino.display.displaypipeline/flush#\(\))

* * *

[**GetDrawListSerialNumbers**(UInt32 modelSerialNumber,UInt32
pageSerialNumber) Gets the current model and page view draw list serial
numbers, which can be used to determine if a model or page view needs to be
redrawn.](/api/rhinocommon/rhino.display.displaypipeline/getdrawlistserialnumbers#\(out,out\))

* * *

[**GetLights**() Get lights that this pipeline is current
using](/api/rhinocommon/rhino.display.displaypipeline/getlights#\(\))

* * *

[**GetOpenGLCameraToClip**() Get an array of 16 floats that represents the
"camera" to "clip" coordinate transformation in OpenGL's right handed
coordinate
system](/api/rhinocommon/rhino.display.displaypipeline/getopenglcameratoclip#\(\))

* * *

[**GetOpenGLWorldToCamera**(Boolean includeModelTransform) Get an array of 16
floats that represents the "world" to "camera" coordinate transformation in
OpenGL's right handed coordinate
system](/api/rhinocommon/rhino.display.displaypipeline/getopenglworldtocamera#\(boolean\))

* * *

[**GetOpenGLWorldToClip**(Boolean includeModelTransform) Get an array of 16
floats that represents the "world" to "clip" coordinate transformation in
OpenGL's right handed coordinate
system](/api/rhinocommon/rhino.display.displaypipeline/getopenglworldtoclip#\(boolean\))

* * *

[**InterruptDrawing**() Tests to see if the pipeline should stop drawing more
geometry and just show what it has so far. If a drawing operation is taking a
long time, this function will return True and tell Rhino it should just finish
up and show the frame buffer. This is used in dynamic drawing
operations.](/api/rhinocommon/rhino.display.displaypipeline/interruptdrawing#\(\))

* * *

[**IsActive**(RhinoObject rhinoObject) Determines if an object can be visible
in this viewport based on it's object type and display attributes. This test
does not check for visibility based on location of the object. NOTE: Use
CRhinoDisplayPipeline::IsVisible() to perform "visibility" tests based on
location (is some part of the object in the view frustum). Use
CRhinoDisplayPipeline::IsActive() to perform "visibility" tests based on
object
type.](/api/rhinocommon/rhino.display.displaypipeline/isactive#\(rhinoobject\))

* * *

[**IsInTiledDraw**(Size fullSize,Rectangle currentTile) Returns True if the
currently drawn frame is part of a tiled capture. Tiled captures are performed
when creating large raster
outputs.](/api/rhinocommon/rhino.display.displaypipeline/isintileddraw#\(out,out\))

* * *

[**IsVisible**(BoundingBox bbox) Test a given box for visibility inside the
view frustum under the current viewport and model transformation
settings.](/api/rhinocommon/rhino.display.displaypipeline/isvisible#\(boundingbox\))

* * *

[**IsVisible**(RhinoObject rhinoObject) Test a given object for visibility
inside the view frustum under the current viewport and model transformation
settings. This function calls a virtual IsVisibleFinal function that sub-
classed pipelines can add extra tests to. In the base class, this test only
tests visibility based on the objects world coordinates location and does not
pay attention to the object's attributes. NOTE: Use
CRhinoDisplayPipeline::IsVisible() to perform "visibility" tests based on
location (is some part of the object in the view frustum). Use
CRhinoDisplayPipeline::IsActive() to perform "visibility" tests based on
object
type.](/api/rhinocommon/rhino.display.displaypipeline/isvisible#\(rhinoobject\))

* * *

[**IsVisible**(Point3d worldCoordinate) Test a given 3d world coordinate point
for visibility inside the view frustum under the current viewport and model
transformation
settings.](/api/rhinocommon/rhino.display.displaypipeline/isvisible#\(point3d\))

* * *

[**MakeDefaultOpenGLContextCurrent**() Make a "default" OpenGL context
current](/api/rhinocommon/rhino.display.displaypipeline/makedefaultopenglcontextcurrent#\(\))

* * *

[**Measure2dText**(String text, Point2d definitionPoint,Boolean
middleJustified,Double rotationRadians,Int32 height,String fontFace)
Determines screen rectangle that would be drawn to using the Draw2dText(..)
function with the same
parameters.](/api/rhinocommon/rhino.display.displaypipeline/measure2dtext#\(string,point2d,boolean,double,int32,string\))

* * *

[**Open**() Opens the
pipeline.](/api/rhinocommon/rhino.display.displaypipeline/open#\(\))

* * *

[**PopClipTesting**() __ Pop a ClipTesting flag off the engine's
stack.](/api/rhinocommon/rhino.display.displaypipeline/popcliptesting#\(\))

* * *

[**PopCullFaceMode**() Pop a FaceCull flag off the engine's
stack.](/api/rhinocommon/rhino.display.displaypipeline/popcullfacemode#\(\))

* * *

[**PopDepthTesting**() Pop a DepthTesting flag off the engine's
stack.](/api/rhinocommon/rhino.display.displaypipeline/popdepthtesting#\(\))

* * *

[**PopDepthWriting**() Pop a DepthWriting flag off the engine's
stack.](/api/rhinocommon/rhino.display.displaypipeline/popdepthwriting#\(\))

* * *

[**PopModelTransform**() Pop a model transformation off the engine's model
transform
stack.](/api/rhinocommon/rhino.display.displaypipeline/popmodeltransform#\(\))

* * *

[**PopProjection**() Pop a view projection off this pipelines projection
stack](/api/rhinocommon/rhino.display.displaypipeline/popprojection#\(\))

* * *

[**Push2dProjection**() Push the current view projection and set the viewport
up to be a simple 2D top projection where the camera frustum matches the same
size as the screen port. This allows geometry draw functions to act like they
are working with typical 2d graphics APIs on a
window](/api/rhinocommon/rhino.display.displaypipeline/push2dprojection#\(\))

* * *

[**PushClipTesting**(Boolean enable) __ Push a ClipTesting flag on the
engine's
stack.](/api/rhinocommon/rhino.display.displaypipeline/pushcliptesting#\(boolean\))

* * *

[**PushCullFaceMode**(CullFaceMode mode) Push a FaceCull flag on the engine's
stack.](/api/rhinocommon/rhino.display.displaypipeline/pushcullfacemode#\(cullfacemode\))

* * *

[**PushDepthTesting**(Boolean enable) Push a DepthTesting flag on the engine's
stack.](/api/rhinocommon/rhino.display.displaypipeline/pushdepthtesting#\(boolean\))

* * *

[**PushDepthWriting**(Boolean enable) Push a DepthWriting flag on the engine's
stack.](/api/rhinocommon/rhino.display.displaypipeline/pushdepthwriting#\(boolean\))

* * *

[**PushModelTransform**(Transform xform) Push a model transformation on the
engine's model transform
stack.](/api/rhinocommon/rhino.display.displaypipeline/pushmodeltransform#\(transform\))

* * *

[**RemoveClippingPlane**(Int32 index) Remove a clipping plane from the
pipeline for this
frame](/api/rhinocommon/rhino.display.displaypipeline/removeclippingplane#\(int32\))

* * *

[**SetupDisplayMaterial**(RhinoDoc doc, RhinoObject rhinoObject,
ObjectAttributes attributes, Transform instanceTransform) Sets up a display
material.](/api/rhinocommon/rhino.display.displaypipeline/setupdisplaymaterial#\(rhinodoc,rhinoobject,objectattributes,transform\))

* * *

[**SetupDisplayMaterial**(RhinoDoc doc, RhinoObject rhinoObject,
ObjectAttributes attributes) Sets up a display
material.](/api/rhinocommon/rhino.display.displaypipeline/setupdisplaymaterial#\(rhinodoc,rhinoobject,objectattributes\))

* * *

[**SetupDisplayMaterial**(RhinoDoc doc, RhinoObject rhinoObject) Sets up a
display
material.](/api/rhinocommon/rhino.display.displaypipeline/setupdisplaymaterial#\(rhinodoc,rhinoobject\))

* * *

[**SetupDisplayMaterial**(Color color)
](/api/rhinocommon/rhino.display.displaypipeline/setupdisplaymaterial#\(color\))

* * *

_keyboard_arrow_down_

Events (13)

[**CalculateBoundingBox**
](/api/rhinocommon/rhino.display.displaypipeline/calculateboundingbox#)

* * *

[**CalculateBoundingBoxZoomExtents** Calculate a bounding to include in the
Zoom Extents
command.](/api/rhinocommon/rhino.display.displaypipeline/calculateboundingboxzoomextents#)

* * *

[**DisplayModeChanged**
](/api/rhinocommon/rhino.display.displaypipeline/displaymodechanged#)

* * *

[**DrawForeground** Called after all non-highlighted objects have been drawn
and PostDrawObjects has been called. Depth writing and testing are turned OFF.
If you want to draw with depth writing/testing, see
PostDrawObjects.](/api/rhinocommon/rhino.display.displaypipeline/drawforeground#)

* * *

[**DrawOverlay** If Rhino is in a feedback mode, the draw overlay call allows
for temporary geometry to be drawn on top of everything in the scene. This is
similar to the dynamic draw routine that occurs with custom get
point.](/api/rhinocommon/rhino.display.displaypipeline/drawoverlay#)

* * *

[**InitFrameBuffer**
](/api/rhinocommon/rhino.display.displaypipeline/initframebuffer#)

* * *

[**ObjectCulling**
](/api/rhinocommon/rhino.display.displaypipeline/objectculling#)

* * *

[**PostDrawObject** Called right after an individual object has been drawn.
NOTE: Do not use this event unless you absolutely need to. It is called for
every object in the document and can slow display down if a large number of
objects exist in the
document](/api/rhinocommon/rhino.display.displaypipeline/postdrawobject#)

* * *

[**PostDrawObjects** Called after all non-highlighted objects have been drawn.
Depth writing and testing are still turned on. If you want to draw without
depth writing/testing, see
DrawForeground.](/api/rhinocommon/rhino.display.displaypipeline/postdrawobjects#)

* * *

[**PreDrawObject** Called right before an individual object is being drawn.
NOTE: Do not use this event unless you absolutely need to. It is called for
every object in the document and can slow display down if a large number of
objects exist in the
document](/api/rhinocommon/rhino.display.displaypipeline/predrawobject#)

* * *

[**PreDrawObjects** Called before objects are been drawn. Depth writing and
testing are
on.](/api/rhinocommon/rhino.display.displaypipeline/predrawobjects#)

* * *

[**PreDrawTransparentObjects** Called before transparent objects have been
drawn. Depth writing and testing are
on.](/api/rhinocommon/rhino.display.displaypipeline/predrawtransparentobjects#)

* * *

[**ViewportProjectionChanged** Called when the projection changes for a
viewport being
drawn.](/api/rhinocommon/rhino.display.displaypipeline/viewportprojectionchanged#)

* * *

