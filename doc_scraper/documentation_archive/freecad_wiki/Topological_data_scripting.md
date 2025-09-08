---
url: https://wiki.freecad.org/Topological_data_scripting
title: Topological data scripting
scraped_at: 2025-09-08 16:41:32
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction Toggle Introduction subsection
    * 1.1 See also
  * 2 Class diagram Toggle Class diagram subsection
    * 2.1 Geometry
    * 2.2 Topology
  * 3 Example: Create simple topology Toggle Example: Create simple topology subsection
    * 3.1 Create geometry
    * 3.2 Arc
    * 3.3 Line
    * 3.4 Put it all together
    * 3.5 Make a prism
    * 3.6 Show it all
  * 4 Create basic shapes Toggle Create basic shapes subsection
    * 4.1 Import modules
    * 4.2 Create a vector
    * 4.3 Create an edge
    * 4.4 Put the shape on screen
    * 4.5 Create a wire
    * 4.6 Create a face
    * 4.7 Create a circle
    * 4.8 Create an arc along points
    * 4.9 Create a polygon
    * 4.10 Create a Bézier curve
    * 4.11 Create a plane
    * 4.12 Create an ellipse
    * 4.13 Create a torus
    * 4.14 Create a box or cuboid
    * 4.15 Create a sphere
    * 4.16 Create a cylinder
    * 4.17 Create a cone
  * 5 Modify shapes
  * 6 Transform operations Toggle Transform operations subsection
    * 6.1 Translate a shape
    * 6.2 Rotate a shape
    * 6.3 Matrix transformations
    * 6.4 Scale a shape
  * 7 Boolean operations Toggle Boolean operations subsection
    * 7.1 Subtraction
    * 7.2 Intersection
    * 7.3 Union
    * 7.4 Section
    * 7.5 Extrusion
  * 8 Explore shapes Toggle Explore shapes subsection
    * 8.1 Edge analysis
    * 8.2 Use a selection
  * 9 Example: The OCC bottle Toggle Example: The OCC bottle subsection
    * 9.1 The script
    * 9.2 Detailed explanation
  * 10 Example: Pierced box
  * 11 Loading and saving

# Topological data scripting

  * [Page](/Topological_data_scripting "View the content page \[ctrl-option-c\]")
  * [Discussion](/Talk:Topological_data_scripting "Discussion about the content page \[ctrl-option-t\]")

English

  * [Read](/Topological_data_scripting)
  * [Edit](/index.php?title=Topological_data_scripting&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Topological_data_scripting&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Topological_data_scripting.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Topological_data_scripting&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Topological_data_scripting)
  * [Edit](/index.php?title=Topological_data_scripting&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Topological_data_scripting&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Topological_data_scripting&action=history)

General

  * [What links here](/Special:WhatLinksHere/Topological_data_scripting "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Topological_data_scripting "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Topological_data_scripting&oldid=1605107 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Topological_data_scripting&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Topological_data_scripting&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Topological+data+scripting&action=page&filter=&language=en)This is the
approved revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Topological+data+scripting&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/Topological_data_scripting/id "Topological data scripting/id \(0% translated\)")
  * [Deutsch](/Topological_data_scripting/de "Topologische Daten skripten \(100% translated\)")
  * English
  * [Türkçe](/Topological_data_scripting/tr "Topological data scripting \(1% translated\)")
  * [español](/Topological_data_scripting/es "Guionización datos topológicos \(32% translated\)")
  * [français](/Topological_data_scripting/fr "Script de données topologiques \(100% translated\)")
  * [italiano](/Topological_data_scripting/it "Script di dati topologici \(100% translated\)")
  * [polski](/Topological_data_scripting/pl "Skrypty danych topologicznych \(100% translated\)")
  * [português](/Topological_data_scripting/pt "Topological data scripting \(1% translated\)")
  * [português do Brasil](/Topological_data_scripting/pt-br "Escrituração de dados topológicos \(1% translated\)")
  * [română](/Topological_data_scripting/ro "Programare script pentru piese \(7% translated\)")
  * [svenska](/Topological_data_scripting/sv "Topological data scripting \(3% translated\)")
  * [čeština](/Topological_data_scripting/cs "Topological data scripting/cs \(0% translated\)")
  * [русский](/Topological_data_scripting/ru "Программирование топологических данных \(45% translated\)")
  * [中文](/Topological_data_scripting/zh "Topological data scripting/zh \(0% translated\)")
  * [中文（中国大陆）](/Topological_data_scripting/zh-cn "拓扑数据脚本 \(10% translated\)")
  * [日本語](/Topological_data_scripting/ja "位相データーのスクリプティング \(2% translated\)")

![](/images/6/6f/Arrow-left.svg) [Part scripting](/Part_scripting "Part
scripting")

[Scripted objects](/Scripted_objects "Scripted objects")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

## Introduction

Here we will explain to you how to control the [Part](/Part_Workbench "Part
Workbench") module directly from the FreeCAD Python interpreter, or from any
external script. Be sure to browse the [Scripting](/Scripting "Scripting")
section and the [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD
Scripting Basics") pages if you need more information about how Python
scripting works in FreeCAD. If you are new to Python, it is a good idea to
first read the [Introduction to Python](/Introduction_to_Python "Introduction
to Python").

### See also

  * [Part scripting](/Part_scripting "Part scripting")
  * [OpenCASCADE](/OpenCASCADE "OpenCASCADE")

## Class diagram

This is a [Unified Modeling Language
(UML)](http://en.wikipedia.org/wiki/Unified_Modeling_Language) overview of the
most important classes of the Part module: [![Python classes of the Part
module](/images/1/13/Part_Classes.jpg)](/index.php?title=File:Part_Classes.jpg&filetimestamp=20180827135429&
"Python classes of the Part module")

Top

### Geometry

The geometric objects are the building blocks of all topological objects:

  * **Geom** Base class of the geometric objects.
  * **Line** A straight line in 3D, defined by starting point and end point.
  * **Circle** Circle or circle segment defined by a center point and start and end point.
  * Etc.

Top

### Topology

The following topological data types are available:

  * **Compound** A group of any type of topological objects.
  * **Compsolid** A composite solid is a set of solids connected by their faces. It expands the notions of WIRE and SHELL to solids.
  * **Solid** A part of space limited by shells. It is three dimensional.
  * **Shell** A set of faces connected by their edges. A shell can be open or closed.
  * **Face** In 2D it is part of a plane; in 3D it is part of a surface. Its geometry is constrained (trimmed) by contours. It is two dimensional.
  * **Wire** A set of edges connected by their vertices. It can be an open or closed contour depending on whether the edges are linked or not.
  * **Edge** A topological element corresponding to a restrained curve. An edge is generally limited by vertices. It has one dimension.
  * **Vertex** A topological element corresponding to a point. It has zero dimension.
  * **Shape** A generic term covering all of the above.

Top

## Example: Create simple topology

[![Wire](/images/7/77/Wire.png)](/index.php?title=File:Wire.png&filetimestamp=20140228220508&
"Wire")

We will now create a topology by constructing it out of simpler geometry. As a
case study we will use a part as seen in the picture which consists of four
vertices, two arcs and two lines.

Top

### Create geometry

First we create the distinct geometric parts of this wire. Making sure that
parts that have to be connected later share the same vertices.

So we create the points first:

    
    
    import FreeCAD as App
    import Part
    V1 = App.Vector(0, 10, 0)
    V2 = App.Vector(30, 10, 0)
    V3 = App.Vector(30, -10, 0)
    V4 = App.Vector(0, -10, 0)
    

Top

### Arc

[![Circle](/images/e/ec/Circel.png)](/index.php?title=File:Circel.png&filetimestamp=20090202153356&
"Circle")

  
For each arc we need a helper point:

    
    
    VC1 = App.Vector(-10, 0, 0)
    C1 = Part.Arc(V1, VC1, V4)
    VC2 = App.Vector(40, 0, 0)
    C2 = Part.Arc(V2, VC2, V3)
    

Top

### Line

[![Line](/images/5/5b/Line.png)](/index.php?title=File:Line.png&filetimestamp=20090202160336&
"Line")

  
The line segments can be created from two points:

    
    
    L1 = Part.LineSegment(V1, V2)
    L2 = Part.LineSegment(V3, V4)
    

Top

### Put it all together

The last step is to put the geometric base elements together and bake a
topological shape:

    
    
    S1 = Part.Shape([C1, L1, C2, L2])
    

Top

### Make a prism

Now extrude the wire in a direction and make an actual 3D shape:

    
    
    W = Part.Wire(S1.Edges)
    P = W.extrude(App.Vector(0, 0, 10))
    

Top

### Show it all

    
    
    Part.show(P)
    

Top

## Create basic shapes

You can easily create basic topological objects with the `make...()` methods
from the Part module:

    
    
    b = Part.makeBox(100, 100, 100)
    Part.show(b)
    

Some available `make...()` methods:

  * `makeBox(l, w, h, [p, d])` Makes a box located in p and pointing into the direction d with the dimensions (l,w,h).
  * `makeCircle(radius)` Makes a circle with a given radius.
  * `makeCone(radius1, radius2, height)` Makes a cone with the given radii and height.
  * `makeCylinder(radius, height)` Makes a cylinder with a given radius and height.
  * `makeLine((x1, y1, z1), (x2, y2, z2))` Makes a line from two points.
  * `makePlane(length, width)` Makes a plane with length and width.
  * `makePolygon(list)` Makes a polygon from a list of points.
  * `makeSphere(radius)` Makes a sphere with a given radius.
  * `makeTorus(radius1, radius2)` Makes a torus with the given radii.

See the [Part API](/Part_API "Part API") page or this [autogenerated Python
Part API documentation](https://freecad-python-
stubs.readthedocs.io/en/latest/autoapi/Part/) for a complete list of available
methods of the Part module.

Top

### Import modules

First we need to import the FreeCAD and Part modules so we can use their
contents in Python:

    
    
    import FreeCAD as App
    import Part
    

Top

### Create a vector

[Vectors](http://en.wikipedia.org/wiki/Euclidean_vector) are one of the most
important pieces of information when building shapes. They usually contain
three numbers (but not necessarily always): the X, Y and Z cartesian
coordinates. You create a vector like this:

    
    
    myVector = App.Vector(3, 2, 0)
    

We just created a vector at coordinates X = 3, Y = 2, Z = 0. In the Part
module, vectors are used everywhere. Part shapes also use another kind of
point representation called Vertex which is simply a container for a vector.
You access the vector of a vertex like this:

    
    
    myVertex = myShape.Vertexes[0]
    print(myVertex.Point)
    > Vector (3, 2, 0)
    

Top

### Create an edge

An edge is nothing but a line with two vertices:

    
    
    edge = Part.makeLine((0, 0, 0), (10, 0, 0))
    edge.Vertexes
    > [<Vertex object at 01877430>, <Vertex object at 014888E0>]
    

Note: You can also create an edge by passing two vectors:

    
    
    vec1 = App.Vector(0, 0, 0)
    vec2 = App.Vector(10, 0, 0)
    line = Part.LineSegment(vec1, vec2)
    edge = line.toShape()
    

You can find the length and center of an edge like this:

    
    
    edge.Length
    > 10.0
    edge.CenterOfMass
    > Vector (5, 0, 0)
    

Top

### Put the shape on screen

So far we created an edge object, but it doesn't appear anywhere on the
screen. This is because the FreeCAD 3D scene only displays what you tell it to
display. To do that, we use this simple method:

    
    
    Part.show(edge)
    

The show function creates an object in our FreeCAD document and assigns our
"edge" shape to it. Use this whenever it is time to display your creation on
screen.

Top

### Create a wire

A wire is a multi-edge line and can be created from a list of edges or even a
list of wires:

    
    
    edge1 = Part.makeLine((0, 0, 0), (10, 0, 0))
    edge2 = Part.makeLine((10, 0, 0), (10, 10, 0))
    wire1 = Part.Wire([edge1, edge2]) 
    edge3 = Part.makeLine((10, 10, 0), (0, 10, 0))
    edge4 = Part.makeLine((0, 10, 0), (0, 0, 0))
    wire2 = Part.Wire([edge3, edge4])
    wire3 = Part.Wire([wire1, wire2])
    wire3.Edges
    > [<Edge object at 016695F8>, <Edge object at 0197AED8>, <Edge object at 01828B20>, <Edge object at 0190A788>]
    Part.show(wire3)
    

`Part.show(wire3)` will display the 4 edges that compose our wire. Other
useful information can be easily retrieved:

    
    
    wire3.Length
    > 40.0
    wire3.CenterOfMass
    > Vector (5, 5, 0)
    wire3.isClosed()
    > True
    wire2.isClosed()
    > False
    

Top

### Create a face

Only faces created from closed wires will be valid. In this example, wire3 is
a closed wire but wire2 is not (see above):

    
    
    face = Part.Face(wire3)
    face.Area
    > 99.99999999999999
    face.CenterOfMass
    > Vector (5, 5, 0)
    face.Length
    > 40.0
    face.isValid()
    > True
    sface = Part.Face(wire2)
    sface.isValid()
    > False
    

Only faces will have an area, wires and edges do not.

Top

### Create a circle

A circle can be created like this:

    
    
    circle = Part.makeCircle(10)
    circle.Curve
    > Circle (Radius : 10, Position : (0, 0, 0), Direction : (0, 0, 1))
    

If you want to create it at a certain position and with a certain direction:

    
    
    ccircle = Part.makeCircle(10, App.Vector(10, 0, 0), App.Vector(1, 0, 0))
    ccircle.Curve
    > Circle (Radius : 10, Position : (10, 0, 0), Direction : (1, 0, 0))
    

ccircle will be created at distance 10 from the X origin and will be facing
outwards along the X axis. Note: `makeCircle()` only accepts `App.Vector()`
for the position and normal parameters, not tuples. You can also create part
of the circle by giving a start and an end angle:

    
    
    from math import pi
    arc1 = Part.makeCircle(10, App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0, 180)
    arc2 = Part.makeCircle(10, App.Vector(0, 0, 0), App.Vector(0, 0, 1), 180, 360)
    

Angles should be provided in degrees. If you have radians simply convert them
using the formula: `degrees = radians * 180/pi` or by using Python's `math`
module:

    
    
    import math
    degrees = math.degrees(radians)
    

Top

### Create an arc along points

Unfortunately there is no `makeArc()` function, but we have the `Part.Arc()`
function to create an arc through three points. It creates an arc object
joining the start point to the end point through the middle point. The arc
object's `toShape()` function must be called to get an edge object, the same
as when using `Part.LineSegment` instead of `Part.makeLine`.

    
    
    arc = Part.Arc(App.Vector(0, 0, 0), App.Vector(0, 5, 0), App.Vector(5, 5, 0))
    arc
    > <Arc object>
    arc_edge = arc.toShape()
    Part.show(arc_edge)
    

`Arc()` only accepts `App.Vector()` for points and not tuples. You can also
obtain an arc by using a portion of a circle:

    
    
    from math import pi
    circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 10)
    arc = Part.Arc(circle,0,pi)
    

Arcs are valid edges like lines, so they can be used in wires also.

Top

### Create a polygon

A polygon is simply a wire with multiple straight edges. The `makePolygon()`
function takes a list of points and creates a wire through those points:

    
    
    lshape_wire = Part.makePolygon([App.Vector(0, 5, 0), App.Vector(0, 0, 0), App.Vector(5, 0, 0)])
    

Top

### Create a Bézier curve

Bézier curves are used to model smooth curves using a series of poles (points)
and optional weights. The function below makes a `Part.BezierCurve()` from a
series of `FreeCAD.Vector()` points. Note: when "getting" and "setting" a
single pole or weight, indices start at 1, not 0.

    
    
    def makeBCurveEdge(Points):
       geomCurve = Part.BezierCurve()
       geomCurve.setPoles(Points)
       edge = Part.Edge(geomCurve)
       return(edge)
    

Top

### Create a plane

A Plane is a flat rectangular surface. The method used to create one is
`makePlane(length, width, [start_pnt, dir_normal])`. By default start_pnt =
Vector(0, 0, 0) and dir_normal = Vector(0, 0, 1). Using dir_normal = Vector(0,
0, 1) will create the plane facing in the positive Z axis direction, while
dir_normal = Vector(1, 0, 0) will create the plane facing in the positive X
axis direction:

    
    
    plane = Part.makePlane(2, 2)
    plane
    > <Face object at 028AF990>
    plane = Part.makePlane(2, 2, App.Vector(3, 0, 0), App.Vector(0, 1, 0))
    plane.BoundBox
    > BoundBox (3, 0, 0, 5, 0, 2)
    

`BoundBox` is a cuboid enclosing the plane with a diagonal starting at (3, 0,
0) and ending at (5, 0, 2). Here the `BoundBox` thickness along the Y axis is
zero, since our shape is totally flat.

Note: `makePlane()` only accepts `App.Vector()` for start_pnt and dir_normal
and not tuples.

Top

### Create an ellipse

There are several ways to create an ellipse:

    
    
    Part.Ellipse()
    

Creates an ellipse with major radius 2 and minor radius 1 with the center at
(0, 0, 0).

    
    
    Part.Ellipse(Ellipse)
    

Creates a copy of the given ellipse.

    
    
    Part.Ellipse(S1, S2, Center)
    

Creates an ellipse centered on the point Center, where the plane of the
ellipse is defined by Center, S1 and S2, its major axis is defined by Center
and S1, its major radius is the distance between Center and S1, and its minor
radius is the distance between S2 and the major axis.

    
    
    Part.Ellipse(Center, MajorRadius, MinorRadius)
    

Creates an ellipse with major and minor radii MajorRadius and MinorRadius,
located in the plane defined by Center and the normal (0, 0, 1)

    
    
    eli = Part.Ellipse(App.Vector(10, 0, 0), App.Vector(0, 5, 0), App.Vector(0, 0, 0))
    Part.show(eli.toShape())
    

In the above code we have passed S1, S2 and center. Similar to `Arc`,
`Ellipse` creates an ellipse object not an edge, so we need to convert it into
an edge using `toShape()` for display.

Note: `Ellipse()` only accepts `App.Vector()` for points and not tuples.

    
    
    eli = Part.Ellipse(App.Vector(0, 0, 0), 10, 5)
    Part.show(eli.toShape())
    

For the above Ellipse constructor we have passed center, MajorRadius and
MinorRadius.

Top

### Create a torus

Using `makeTorus(radius1, radius2, [pnt, dir, angle1, angle2, angle])`. By
default pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1), angle1 = 0, angle2 = 360
and angle = 360. Consider a torus as small circle sweeping along a big circle.
Radius1 is the radius of the big circle, radius2 is the radius of the small
circle, pnt is the center of the torus and dir is the normal direction. angle1
and angle2 are angles in degrees for the small circle; the last angle
parameter is to make a section of the torus:

    
    
    torus = Part.makeTorus(10, 2)
    

The above code will create a torus with diameter 20 (radius 10) and thickness
4 (small circle radius 2)

    
    
    tor=Part.makeTorus(10, 5, App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0, 180)
    

The above code will create a slice of the torus.

    
    
    tor=Part.makeTorus(10, 5, App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0, 360, 180)
    

The above code will create a semi torus; only the last parameter is changed.
i.e the remaining angles are defaults. Giving the angle 180 will create the
torus from 0 to 180, that is, a half torus.

Top

### Create a box or cuboid

Using `makeBox(length, width, height, [pnt, dir])`. By default pnt = Vector(0,
0, 0) and dir = Vector(0, 0, 1).

    
    
    box = Part.makeBox(10, 10, 10)
    len(box.Vertexes)
    > 8
    

Top

### Create a sphere

Using `makeSphere(radius, [pnt, dir, angle1, angle2, angle3])`. By default pnt
= Vector(0, 0, 0), dir = Vector(0, 0, 1), angle1 = -90, angle2 = 90 and angle3
= 360. Angle1 and angle2 are the vertical minimum and maximum of the sphere,
angle3 is the sphere diameter.

    
    
    sphere = Part.makeSphere(10)
    hemisphere = Part.makeSphere(10, App.Vector(0, 0, 0), App.Vector(0, 0, 1), -90, 90, 180)
    

Top

### Create a cylinder

Using `makeCylinder(radius, height, [pnt, dir, angle])`. By default pnt =
Vector(0, 0, 0), dir = Vector(0, 0, 1) and angle = 360.

    
    
    cylinder = Part.makeCylinder(5, 20)
    partCylinder = Part.makeCylinder(5, 20, App.Vector(20, 0, 0), App.Vector(0, 0, 1), 180)
    

Top

### Create a cone

Using `makeCone(radius1, radius2, height, [pnt, dir, angle])`. By default pnt
= Vector(0, 0, 0), dir = Vector(0, 0, 1) and angle = 360.

    
    
    cone = Part.makeCone(10, 0, 20)
    semicone = Part.makeCone(10, 0, 20, App.Vector(20, 0, 0), App.Vector(0, 0, 1), 180)
    

Top

## Modify shapes

There are several ways to modify shapes. Some are simple transformation
operations such as moving or rotating shapes, others are more complex, such as
unioning and subtracting one shape from another.

Top

## Transform operations

### Translate a shape

Translating is the act of moving a shape from one place to another. Any shape
(edge, face, cube, etc...) can be translated the same way:

    
    
    myShape = Part.makeBox(2, 2, 2)
    myShape.translate(App.Vector(2, 0, 0))
    

This will move our shape "myShape" 2 units in the X direction.

Top

### Rotate a shape

To rotate a shape, you need to specify the rotation center, the axis, and the
rotation angle:

    
    
    myShape.rotate(App.Vector(0, 0, 0),App.Vector(0, 0, 1), 180)
    

The above code will rotate the shape 180 degrees around the Z Axis.

Top

### Matrix transformations

A matrix is a very convenient way to store transformations in the 3D world. In
a single matrix, you can set translation, rotation and scaling values to be
applied to an object. For example:

    
    
    myMat = App.Matrix()
    myMat.move(App.Vector(2, 0, 0))
    myMat.rotateZ(math.pi/2)
    

Note: FreeCAD matrixes work in radians. Also, almost all matrix operations
that take a vector can also take three numbers, so these two lines do the same
thing:

    
    
    myMat.move(2, 0, 0)
    myMat.move(App.Vector(2, 0, 0))
    

Once our matrix is set, we can apply it to our shape. FreeCAD provides two
methods for doing that: `transformShape()` and `transformGeometry()`. The
difference is that with the first one, you are sure that no deformations will
occur (see Scaling a shape below). We can apply our transformation like this:

    
    
    myShape.transformShape(myMat)
    

or

    
    
    myShape.transformGeometry(myMat)
    

Top

### Scale a shape

Scaling a shape is a more dangerous operation because, unlike translation or
rotation, scaling non-uniformly (with different values for X, Y and Z) can
modify the structure of the shape. For example, scaling a circle with a higher
value horizontally than vertically will transform it into an ellipse, which
behaves mathematically very differently. For scaling, we cannot use the
`transformShape()`, we must use `transformGeometry()`:

    
    
    myMat = App.Matrix()
    myMat.scale(2, 1, 1)
    myShape=myShape.transformGeometry(myMat)
    

Top

## Boolean operations

### Subtraction

Subtracting a shape from another one is called "cut" in FreeCAD and is done
like this:

    
    
    cylinder = Part.makeCylinder(3, 10, App.Vector(0, 0, 0), App.Vector(1, 0, 0))
    sphere = Part.makeSphere(5, App.Vector(5, 0, 0))
    diff = cylinder.cut(sphere)
    

Top

### Intersection

The same way, the intersection between two shapes is called "common" and is
done this way:

    
    
    cylinder1 = Part.makeCylinder(3, 10, App.Vector(0, 0, 0), App.Vector(1, 0, 0))
    cylinder2 = Part.makeCylinder(3, 10, App.Vector(5, 0, -5), App.Vector(0, 0, 1))
    common = cylinder1.common(cylinder2)
    

Top

### Union

Union is called "fuse" and works the same way:

    
    
    cylinder1 = Part.makeCylinder(3, 10, App.Vector(0, 0, 0), App.Vector(1, 0, 0))
    cylinder2 = Part.makeCylinder(3, 10, App.Vector(5, 0, -5), App.Vector(0, 0, 1))
    fuse = cylinder1.fuse(cylinder2)
    

Top

### Section

A "section" is the intersection between a solid shape and a plane shape. It
will return an intersection curve, a compound curve composed of edges.

    
    
    cylinder1 = Part.makeCylinder(3, 10, App.Vector(0, 0, 0), App.Vector(1, 0, 0))
    cylinder2 = Part.makeCylinder(3, 10, App.Vector(5, 0, -5), App.Vector(0, 0, 1))
    section = cylinder1.section(cylinder2)
    section.Wires
    > []
    section.Edges
    > [<Edge object at 0D87CFE8>, <Edge object at 019564F8>, <Edge object at 0D998458>, 
     <Edge  object at 0D86DE18>, <Edge object at 0D9B8E80>, <Edge object at 012A3640>, 
     <Edge object at 0D8F4BB0>]
    

Top

### Extrusion

Extrusion is the act of "pushing" a flat shape in a certain direction,
resulting in a solid body. Think of a circle becoming a tube by "pushing it
out":

    
    
    circle = Part.makeCircle(10)
    tube = circle.extrude(App.Vector(0, 0, 2))
    

If your circle is hollow, you will obtain a hollow tube. If your circle is
actually a disc with a filled face, you will obtain a solid cylinder:

    
    
    wire = Part.Wire(circle)
    disc = Part.Face(wire)
    cylinder = disc.extrude(App.Vector(0, 0, 2))
    

Top

## Explore shapes

You can easily explore the topological data structure:

    
    
    import Part
    b = Part.makeBox(100, 100, 100)
    b.Wires
    w = b.Wires[0]
    w
    w.Wires
    w.Vertexes
    Part.show(w)
    w.Edges
    e = w.Edges[0]
    e.Vertexes
    v = e.Vertexes[0]
    v.Point
    

By typing the lines above in the Python interpreter, you will gain a good
understanding of the structure of Part objects. Here, our `makeBox()` command
created a solid shape. This solid, like all Part solids, contains faces. Faces
always contain wires, which are lists of edges that border the face. Each face
has at least one closed wire (it can have more if the face has a hole). In the
wire, we can look at each edge separately, and inside each edge, we can see
the vertices. Straight edges have only two vertices, obviously.

Top

### Edge analysis

In case of an edge, which is an arbitrary curve, it's most likely you want to
do a discretization. In FreeCAD the edges are parametrized by their lengths.
That means you can walk an edge/curve by its length:

    
    
    import Part
    box = Part.makeBox(100, 100, 100)
    anEdge = box.Edges[0]
    print(anEdge.Length)
    

Now you can access a lot of properties of the edge by using the length as a
position. That means if the edge is 100mm long the start position is 0 and the
end position 100.

    
    
    anEdge.tangentAt(0.0)          # tangent direction at the beginning
    anEdge.valueAt(0.0)            # Point at the beginning
    anEdge.valueAt(100.0)          # Point at the end of the edge
    anEdge.derivative1At(50.0)     # first derivative of the curve in the middle
    anEdge.derivative2At(50.0)     # second derivative of the curve in the middle
    anEdge.derivative3At(50.0)     # third derivative of the curve in the middle
    anEdge.centerOfCurvatureAt(50) # center of the curvature for that position
    anEdge.curvatureAt(50.0)       # the curvature
    anEdge.normalAt(50)            # normal vector at that position (if defined)
    

Top

### Use a selection

Here we see now how we can use a selection the user did in the viewer. First
of all we create a box and show it in the viewer.

    
    
    import Part
    Part.show(Part.makeBox(100, 100, 100))
    Gui.SendMsgToActiveView("ViewFit")
    

Now select some faces or edges. With this script you can iterate over all
selected objects and their sub elements:

    
    
    for o in Gui.Selection.getSelectionEx():
        print(o.ObjectName)
        for s in o.SubElementNames:
            print("name: ", s)
            for s in o.SubObjects:
                print("object: ", s)
    

Select some edges and this script will calculate the length:

    
    
    length = 0.0
    for o in Gui.Selection.getSelectionEx():
        for s in o.SubObjects:
            length += s.Length
    
    print("Length of the selected edges: ", length)
    

Top

## Example: The OCC bottle

A typical example found on the [OpenCasCade Technology
website](https://www.opencascade.com/doc/occt-6.9.0/overview/html/occt__tutorial.html)
is how to build a bottle. This is a good exercise for FreeCAD too. In fact, if
you follow our example below and the OCC page simultaneously, you will see how
well OCC structures are implemented in FreeCAD. The script is included in the
FreeCAD installation (inside the Mod/Part folder) and can be called from the
Python interpreter by typing:

    
    
    import Part
    import MakeBottle
    bottle = MakeBottle.makeBottle()
    Part.show(bottle)
    

Top

### The script

For the purpose of this tutorial we will consider a reduced version of the
script. In this version the bottle will not be hollowed out, and the neck of
the bottle will not be threaded.

    
    
    import FreeCAD as App
    import Part, math
    
    def makeBottleTut(myWidth = 50.0, myHeight = 70.0, myThickness = 30.0):
        aPnt1=App.Vector(-myWidth / 2., 0, 0)
        aPnt2=App.Vector(-myWidth / 2., -myThickness / 4., 0)
        aPnt3=App.Vector(0, -myThickness / 2., 0)
        aPnt4=App.Vector(myWidth / 2., -myThickness / 4., 0)
        aPnt5=App.Vector(myWidth / 2., 0, 0)
    
        aArcOfCircle = Part.Arc(aPnt2, aPnt3, aPnt4)
        aSegment1=Part.LineSegment(aPnt1, aPnt2)
        aSegment2=Part.LineSegment(aPnt4, aPnt5)
    
        aEdge1=aSegment1.toShape()
        aEdge2=aArcOfCircle.toShape()
        aEdge3=aSegment2.toShape()
        aWire=Part.Wire([aEdge1, aEdge2, aEdge3])
    
        aTrsf=App.Matrix()
        aTrsf.rotateZ(math.pi) # rotate around the z-axis
    
        aMirroredWire=aWire.copy()
        aMirroredWire.transformShape(aTrsf)
        myWireProfile=Part.Wire([aWire, aMirroredWire])
    
        myFaceProfile=Part.Face(myWireProfile)
        aPrismVec=App.Vector(0, 0, myHeight)
        myBody=myFaceProfile.extrude(aPrismVec)
    
        myBody=myBody.makeFillet(myThickness / 12.0, myBody.Edges)
    
        neckLocation=App.Vector(0, 0, myHeight)
        neckNormal=App.Vector(0, 0, 1)
    
        myNeckRadius = myThickness / 4.
        myNeckHeight = myHeight / 10.
        myNeck = Part.makeCylinder(myNeckRadius, myNeckHeight, neckLocation, neckNormal)
        myBody = myBody.fuse(myNeck)
    
        return myBody
    
    el = makeBottleTut()
    Part.show(el)
    

Top

### Detailed explanation

    
    
    import FreeCAD as App
    import Part, math
    

We will, of course, need the `FreeCAD` and `Part` modules.

    
    
    def makeBottleTut(myWidth = 50.0, myHeight = 70.0, myThickness = 30.0):
        aPnt1=App.Vector(-myWidth / 2., 0, 0)
        aPnt2=App.Vector(-myWidth / 2., -myThickness / 4., 0)
        aPnt3=App.Vector(0, -myThickness / 2., 0)
        aPnt4=App.Vector(myWidth / 2., -myThickness / 4., 0)
        aPnt5=App.Vector(myWidth / 2., 0, 0)
    

Here we define our `makeBottleTut` function. This function can be called
without arguments, like we did above, in which case default values for width,
height, and thickness will be used. Then, we define a couple of points that
will be used for building our base profile.

    
    
    ...
        aArcOfCircle = Part.Arc(aPnt2, aPnt3, aPnt4)
        aSegment1=Part.LineSegment(aPnt1, aPnt2)
        aSegment2=Part.LineSegment(aPnt4, aPnt5)
    

Here we define the geometry: an arc, made of three points, and two line
segments, made of two points.

    
    
    ...
        aEdge1=aSegment1.toShape()
        aEdge2=aArcOfCircle.toShape()
        aEdge3=aSegment2.toShape()
        aWire=Part.Wire([aEdge1, aEdge2, aEdge3])
    

Remember the difference between geometry and shapes? Here we build shapes out
of our construction geometry. Three edges (edges can be straight or curved),
then a wire made of those three edges.

    
    
    ...
        aTrsf=App.Matrix()
        aTrsf.rotateZ(math.pi) # rotate around the z-axis
    
        aMirroredWire=aWire.copy()
        aMirroredWire.transformShape(aTrsf)
        myWireProfile=Part.Wire([aWire, aMirroredWire])
    

So far we have built only a half profile. Instead of building the whole
profile the same way, we can just mirror what we did and glue both halves
together. We first create a matrix. A matrix is a very common way to apply
transformations to objects in the 3D world, since it can contain in one
structure all basic transformations that 3D objects can undergo (move, rotate
and scale). After we create the matrix we mirror it, then we create a copy of
our wire and apply the transformation matrix to it. We now have two wires, and
we can make a third wire out of them, since wires are actually lists of edges.

    
    
    ...
        myFaceProfile=Part.Face(myWireProfile)
        aPrismVec=App.Vector(0, 0, myHeight)
        myBody=myFaceProfile.extrude(aPrismVec)
    
        myBody=myBody.makeFillet(myThickness / 12.0, myBody.Edges)
    

Now that we have a closed wire, it can be turned into a face. Once we have a
face, we can extrude it. In doing so, we make a solid. Then we apply a nice
little fillet to our object because we care about good design, don't we?

    
    
    ...
        neckLocation=App.Vector(0, 0, myHeight)
        neckNormal=App.Vector(0, 0, 1)
    
        myNeckRadius = myThickness / 4.
        myNeckHeight = myHeight / 10.
        myNeck = Part.makeCylinder(myNeckRadius, myNeckHeight, neckLocation, neckNormal)
    

At this point, the body of our bottle is made, but we still need to create a
neck. So we make a new solid, with a cylinder.

    
    
    ...
        myBody = myBody.fuse(myNeck)
    

The fuse operation is very powerful. It will take care of gluing what needs to
be glued and remove parts that need to be removed.

    
    
    ...
        return myBody
    

Then, we return our Part solid as the result of our function.

    
    
    el = makeBottleTut()
    Part.show(el)
    

Finally, we call the function to actually create the part, then make it
visible.

Top

## Example: Pierced box

Here is a complete example of building a pierced box.

The construction is done one side at a time. When the cube is finished, it is
hollowed out by cutting a cylinder through it.

    
    
    import FreeCAD as App
    import Part, math
    
    size = 10
    poly = Part.makePolygon([(0, 0, 0), (size, 0, 0), (size, 0, size), (0, 0, size), (0, 0, 0)])
    
    face1 = Part.Face(poly)
    face2 = Part.Face(poly)
    face3 = Part.Face(poly)
    face4 = Part.Face(poly)
    face5 = Part.Face(poly)
    face6 = Part.Face(poly)
         
    myMat = App.Matrix()
    
    myMat.rotateZ(math.pi / 2)
    face2.transformShape(myMat)
    face2.translate(App.Vector(size, 0, 0))
    
    myMat.rotateZ(math.pi / 2)
    face3.transformShape(myMat)
    face3.translate(App.Vector(size, size, 0))
    
    myMat.rotateZ(math.pi / 2)
    face4.transformShape(myMat)
    face4.translate(App.Vector(0, size, 0))
    
    myMat = App.Matrix()
    
    myMat.rotateX(-math.pi / 2)
    face5.transformShape(myMat)
    
    face6.transformShape(myMat)               
    face6.translate(App.Vector(0, 0, size))
    
    myShell = Part.makeShell([face1, face2, face3, face4, face5, face6])   
    mySolid = Part.makeSolid(myShell)
    
    myCyl = Part.makeCylinder(2, 20)
    myCyl.translate(App.Vector(size / 2, size / 2, 0))
    
    cut_part = mySolid.cut(myCyl)
    
    Part.show(cut_part)
    

Top

## Loading and saving

There are several ways to save your work. You can of course save your FreeCAD
document, but you can also save [Part](/Part_Workbench "Part Workbench")
objects directly to common CAD formats, such as BREP, IGS, STEP and STL.

Saving a shape to a file is easy. There are `exportBrep()`, `exportIges()`,
`exportStep()` and `exportStl()` methods available for all shape objects. So,
doing:

    
    
    import Part
    s = Part.makeBox(10, 10, 10)
    s.exportStep("test.stp")
    

will save our box into a STEP file. To load a BREP, IGES or STEP file:

    
    
    import Part
    s = Part.Shape()
    s.read("test.stp")
    

To convert a STEP file to an IGS file:

    
    
    import Part
     s = Part.Shape()
     s.read("file.stp")       # incoming file igs, stp, stl, brep
     s.exportIges("file.igs") # outbound file igs
    

Top

![](/images/6/6f/Arrow-left.svg) [Part scripting](/Part_scripting "Part
scripting")

[Scripted objects](/Scripted_objects "Scripted objects")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

Expand[![](/images/thumb/8/8f/Power_user_hub.png/24px-
Power_user_hub.png)](/index.php?title=File:Power_user_hub.png&filetimestamp=20200511213015&)
[Power user documentation](/Power_users_hub "Power users hub")

  * **FreeCAD scripting:** [Python](/Python "Python"), [Introduction to Python](/Introduction_to_Python "Introduction to Python"), [Python scripting tutorial](/Python_scripting_tutorial "Python scripting tutorial"), [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics")

* * *

  * **Modules:** [Builtin modules](/Builtin_modules "Builtin modules"), [Units](/Units "Units"), [Quantity](/Quantity "Quantity")
  * **Workbenches:** [Workbench creation](/Workbench_creation "Workbench creation"), [Gui Commands](/Gui_Command "Gui Command"), [Commands](/Command "Command"), [Installing more workbenches](/Installing_more_workbenches "Installing more workbenches")
  * **Meshes and Parts:** [Mesh Scripting](/Mesh_Scripting "Mesh Scripting"), Topological data scripting, [Mesh to Part](/Mesh_to_Part "Mesh to Part"), [PythonOCC](/PythonOCC "PythonOCC")

* * *

  * **Parametric objects:** [Scripted objects](/Scripted_objects "Scripted objects"), [Viewproviders](/Viewprovider "Viewprovider") ([Custom icon in tree view](/Custom_icon_in_tree_view "Custom icon in tree view"))
  * **Scenegraph:** [Coin (Inventor) scenegraph](/Scenegraph "Scenegraph"), [Pivy](/Pivy "Pivy")
  * **Graphical interface:** [Interface creation](/Interface_creation "Interface creation"), [Interface creation completely in Python](/Dialog_creation "Dialog creation") ([1](/Dialog_creation_with_various_widgets "Dialog creation with various widgets"), [2](/Dialog_creation_reading_and_writing_files "Dialog creation reading and writing files"), [3](/Dialog_creation_setting_colors "Dialog creation setting colors"), [4](/Dialog_creation_image_and_animated_GIF "Dialog creation image and animated GIF"), [5](/PySide_usage_snippets "PySide usage snippets")), [PySide](/PySide "PySide"), PySide examples [beginner](/PySide_Beginner_Examples "PySide Beginner Examples"), [intermediate](/PySide_Intermediate_Examples "PySide Intermediate Examples"), [advanced](/PySide_Advanced_Examples "PySide Advanced Examples")
  * **Macros:** [Macros](/Macros "Macros"), [How to install macros](/How_to_install_macros "How to install macros")
  * **Embedding:** [Embedding FreeCAD](/Embedding_FreeCAD "Embedding FreeCAD"), [Embedding FreeCADGui](/Embedding_FreeCADGui "Embedding FreeCADGui")

* * *

  * **Other:** [Expressions](/Expressions "Expressions"), [Code snippets](/Code_snippets "Code snippets"), [Line drawing function](/Line_drawing_function "Line drawing function"), [FreeCAD vector math library](/FreeCAD_vector_math_library "FreeCAD vector math library") (deprecated)

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

