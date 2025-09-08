---
url: https://wiki.freecad.org/Part_scripting
title: Part scripting
scraped_at: 2025-09-08 16:41:37
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction Toggle Introduction subsection
    * 1.1 See also
  * 2 Test script
  * 3 Examples Toggle Examples subsection
    * 3.1 Line
    * 3.2 Circle
    * 3.3 Arc

# Part scripting

  * [Page](/Part_scripting "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Part_scripting&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Part_scripting)
  * [Edit](/index.php?title=Part_scripting&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Part_scripting&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Part_scripting.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Part_scripting&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Part_scripting)
  * [Edit](/index.php?title=Part_scripting&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Part_scripting&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Part_scripting&action=history)

General

  * [What links here](/Special:WhatLinksHere/Part_scripting "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Part_scripting "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Part_scripting&oldid=1605965 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Part_scripting&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Part_scripting&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Part+scripting&action=page&filter=&language=en)This is the approved revision
of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Part+scripting&language=&task=view "Start translation for this language")
  * [Deutsch](/Part_scripting/de "Part Skripten \(100% translated\)")
  * English
  * [español](/Part_scripting/es "Pieza Guiónes \(18% translated\)")
  * [français](/Part_scripting/fr "Part Écrire un script \(100% translated\)")
  * [italiano](/Part_scripting/it "Script di Part \(100% translated\)")
  * [polski](/Part_scripting/pl "Skrypty w środowisku Część \(100% translated\)")
  * [português do Brasil](/Part_scripting/pt-br "Script\(roteiro\) da peça \(3% translated\)")
  * [русский](/Part_scripting/ru "Скрипты верстака Деталь \(100% translated\)")

![](/images/6/6f/Arrow-left.svg) [FreeCAD Scripting
Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics")

[Topological data scripting](/Topological_data_scripting "Topological data
scripting") ![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

## Introduction

The main data structure used in the Part module is the
[BRep](http://en.wikipedia.org/wiki/Boundary_representation) data type from
[OpenCASCADE](/OpenCASCADE "OpenCASCADE"). Almost all contents and object
types of the Part module are available in [Python](/Python "Python")
scripting. This includes geometric primitives, such as Lines, Circles and
Arcs, and the whole range of TopoShapes, like Vertexes, Edges, Wires, Faces,
Solids and Compounds. For each of those objects, several creation methods
exist, and for some of them, especially the TopoShapes, advanced operations
like boolean union/difference/intersection are also available. Explore the
contents of the Part module, as described in the [FreeCAD Scripting
Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics") page, to know
more.

The most basic object that can be created is a [Part Feature](/Part_Feature
"Part Feature"), which has a simple Data**Placement** property, and basic
properties to define its color and appearance.

Another simple object used in 2D geometrical objects is the [Part
Part2DObject](/Part_Part2DObject "Part Part2DObject"), which is the base of
the [Sketcher SketchObject](/Sketcher_SketchObject "Sketcher SketchObject")
and most [Draft elements](/Draft_Workbench "Draft Workbench").

### See also

  * [Topological data scripting](/Topological_data_scripting "Topological data scripting")
  * [OpenCASCADE](/OpenCASCADE "OpenCASCADE")

## Test script

Test the creation of [Part Primitives](/Part_Primitives "Part Primitives")
with a script.

    
    
    import parttests.part_test_objects as pto
    pto.create_test_file("example_file")
    

This script is located in the installation directory of the program, and can
be examined to see how the basic primitives are built.

    
    
    $INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
    

## Examples

### Line

To create a line element switch to the [Python console](/Python_console
"Python console") and enter:

    
    
    import FreeCAD as App
    import Part
    
    doc = App.newDocument()
    
    line = Part.LineSegment()
    line.StartPoint = (0.0, 0.0, 0.0)
    line.EndPoint = (1.0, 1.0, 1.0)
    obj = doc.addObject("Part::Feature", "Line")
    obj.Shape= line.toShape()
    
    doc.recompute()
    

Let's go through the above Python example step by step:

    
    
    import FreeCAD as App
    import Part
    doc = App.newDocument()
    

This loads the FreeCAD and Part modules and creates a new document.

    
    
    line = Part.LineSegment()
    line.StartPoint = (0.0, 0.0, 0.0)
    line.EndPoint = (1.0, 1.0, 1.0)
    

Line is actually a line segment, hence the start and endpoint.

    
    
    obj = doc.addObject("Part::Feature", "Line")
    obj.Shape= line.toShape()
    

This adds a Part object type to the document and assigns the shape
representation of the line segment to the `Shape` property of the added
object. It is important to understand here that we use a geometric primitive
(the `Part.LineSegment`) to create a TopoShape out of it (with the `toShape()`
method). Only shapes can be added to the document. In FreeCAD geometric
primitives are used as "building structures" for shapes.

    
    
    doc.recompute()
    

Updates the document. This also prepares the visual representation of the new
Part object.

Note that a line segment can also be created by specifying its start and
endpoint directly in the constructor, for example `Part.LineSegment(point1,
point2)`, or we can create a default line and set its properties afterwards,
as we did here.

A Line can also be created using:

    
    
    import FreeCAD as App
    import Part
    
    def my_create_line(pt1, pt2, obj_name):
        obj = App.ActiveDocument.addObject("Part::Line", obj_name)
        obj.X1 = pt1[0]
        obj.Y1 = pt1[1]
        obj.Z1 = pt1[2]
    
        obj.X2 = pt2[0]
        obj.Y2 = pt2[1]
        obj.Z2 = pt2[2]
    
        App.ActiveDocument.recompute()
        return obj
    
    line = my_create_line((0, 0, 0), (0, 10, 0), "LineName")
    

### Circle

A circle can be created in a similar way:

    
    
    import FreeCAD as App
    import Part
    
    doc = App.activeDocument()
    
    circle = Part.Circle() 
    circle.Radius = 10.0  
    obj = doc.addObject("Part::Feature", "Circle")
    obj.Shape = circle.toShape()
    
    doc.recompute()
    

Or using:

    
    
    import FreeCAD as App
    import Part
    
    def my_create_circle(rad, obj_name):
        obj = App.ActiveDocument.addObject("Part::Circle", obj_name)
        obj.Radius = rad
    
        App.ActiveDocument.recompute()
        return obj
    
    circle = my_create_circle(5.0, "CircleName")
    

Alternatively we can create a circle by defining its center, axis and radius:

    
    
    import FreeCAD as App
    import Part
    
    doc = App.activeDocument()
    
    center = App.Vector(1, 2, 3)
    axis = App.Vector(1, 1, 1)
    radius = 10
    circle = Part.Circle(center, axis, radius)
    obj = doc.addObject("Part::Feature", "Circle")
    obj.Shape = circle.toShape()
    
    doc.recompute()
    

Or by defining three points on its circumference:

    
    
    import FreeCAD as App
    import Part
    
    doc = App.activeDocument()
    
    p1 = App.Vector(10, 0, 0)
    p2 = App.Vector(0, 10, 0)
    p3 = App.Vector(0, 0, 10)
    circle = Part.Circle(p1, p2, p3)
    obj = doc.addObject("Part::Feature", "Circle")
    obj.Shape = circle.toShape()
    
    doc.recompute()
    

Note again, we used the circle (geometric primitive) to construct a shape. We
can of course still access our construction geometry afterwards, by doing:

    
    
    shape = obj.Shape
    edge = shape.Edges[0]
    curve = edge.Curve
    

Here we take the `Shape` of our object `obj` and then its list of `Edges`. In
this case there will be only one edge because we made the shape out of a
single circle. So we take only the first item in the `Edges` list, and then
take its curve. Every edge has a `Curve`, which is the geometric primitive it
is based on.

### Arc

An arc can be created like this:

    
    
    import FreeCAD as App
    import Part
    
    doc = App.activeDocument()
    
    p1 = App.Vector(10, 0, 0)
    p2 = App.Vector(0, 10, 0)
    p3 = App.Vector(-10, 0, 0)
    arc = Part.Arc(p1, p2, p3)
    obj = doc.addObject("Part::Feature", "Arc")
    obj.Shape = arc.toShape()
    
    doc.recompute()
    

This draws a half circle. The center is at (0, 0, 0). The radius is 10. P1 is
the start point on +X axis. P2 is the middle point on +Y axis and P3 is the
end point on -X axis.

We can also create an arc from a circle:

    
    
    import FreeCAD as App
    import Part
    
    doc = App.activeDocument()
    
    p1 = App.Vector(10, 0, 0)
    p2 = App.Vector(0, 10, 0)
    p3 = App.Vector(-10, 0, 0)
    circle = Part.Circle(p1, p2, p3)
    arc = Part.ArcOfCircle(circle, 0.0, 0.7854)
    obj = doc.addObject("Part::Feature", "Arc")
    obj.Shape = arc.toShape()
    
    doc.recompute()
    

It needs a circle, and a start angle and end angle in radians.

  

![](/images/6/6f/Arrow-left.svg) [FreeCAD Scripting
Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics")

[Topological data scripting](/Topological_data_scripting "Topological data
scripting") ![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

Expand[![](/images/thumb/8/8f/Power_user_hub.png/24px-
Power_user_hub.png)](/index.php?title=File:Power_user_hub.png&filetimestamp=20200511213015&)
[Power user documentation](/Power_users_hub "Power users hub")

  * **FreeCAD scripting:** [Python](/Python "Python"), [Introduction to Python](/Introduction_to_Python "Introduction to Python"), [Python scripting tutorial](/Python_scripting_tutorial "Python scripting tutorial"), [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics")

* * *

  * **Modules:** [Builtin modules](/Builtin_modules "Builtin modules"), [Units](/Units "Units"), [Quantity](/Quantity "Quantity")
  * **Workbenches:** [Workbench creation](/Workbench_creation "Workbench creation"), [Gui Commands](/Gui_Command "Gui Command"), [Commands](/Command "Command"), [Installing more workbenches](/Installing_more_workbenches "Installing more workbenches")
  * **Meshes and Parts:** [Mesh Scripting](/Mesh_Scripting "Mesh Scripting"), [Topological data scripting](/Topological_data_scripting "Topological data scripting"), [Mesh to Part](/Mesh_to_Part "Mesh to Part"), [PythonOCC](/PythonOCC "PythonOCC")

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

Expand[![](/images/0/04/Workbench_Part.svg)](/index.php?title=File:Workbench_Part.svg&filetimestamp=20240712190040&)
[Part](/Part_Workbench "Part Workbench")

  * **Primitives:** [Box](/Part_Box "Part Box"), [Cylinder](/Part_Cylinder "Part Cylinder"), [Sphere](/Part_Sphere "Part Sphere"), [Cone](/Part_Cone "Part Cone"), [Torus](/Part_Torus "Part Torus"), [Tube](/Part_Tube "Part Tube"), [Create primitives](/Part_Primitives "Part Primitives"), [Shape builder](/Part_Builder "Part Builder")

* * *

  * **Creation and modification:** [Create sketch](/Sketcher_NewSketch "Sketcher NewSketch"), [Extrude](/Part_Extrude "Part Extrude"), [Revolve](/Part_Revolve "Part Revolve"), [Mirror](/Part_Mirror "Part Mirror"), [Scale](/Part_Scale "Part Scale"), [Fillet](/Part_Fillet "Part Fillet"), [Chamfer](/Part_Chamfer "Part Chamfer"), [Make face from wires](/Part_MakeFace "Part MakeFace"), [Ruled Surface](/Part_RuledSurface "Part RuledSurface"), [Loft](/Part_Loft "Part Loft"), [Sweep](/Part_Sweep "Part Sweep"), [Section](/Part_Section "Part Section"), [Cross sections](/Part_CrossSections "Part CrossSections"), [3D Offset](/Part_Offset "Part Offset"), [2D Offset](/Part_Offset2D "Part Offset2D"), [Thickness](/Part_Thickness "Part Thickness"), [Projection on surface](/Part_ProjectionOnSurface "Part ProjectionOnSurface"), [Color per face](/Part_ColorPerFace "Part ColorPerFace")

* * *

  * **Boolean:** [Make compound](/Part_Compound "Part Compound"), [Explode compound](/Part_ExplodeCompound "Part ExplodeCompound"), [Compound Filter](/Part_CompoundFilter "Part CompoundFilter"), [Boolean](/Part_Boolean "Part Boolean"), [Cut](/Part_Cut "Part Cut"), [Union](/Part_Fuse "Part Fuse"), [Intersection](/Part_Common "Part Common"), [Connect objects](/Part_JoinConnect "Part JoinConnect"), [Embed object](/Part_JoinEmbed "Part JoinEmbed"), [Cutout for object](/Part_JoinCutout "Part JoinCutout"), [Boolean fragments](/Part_BooleanFragments "Part BooleanFragments"), [Slice apart](/Part_SliceApart "Part SliceApart"), [Slice to compound](/Part_Slice "Part Slice"), [Boolean XOR](/Part_XOR "Part XOR"), [Check geometry](/Part_CheckGeometry "Part CheckGeometry"), [Defeaturing](/Part_Defeaturing "Part Defeaturing")

* * *

  * **Other tools:** [Import CAD file](/Part_Import "Part Import"), [Export CAD file](/Part_Export "Part Export"), [Box selection](/Part_BoxSelection "Part BoxSelection"), [Create shape from mesh](/Part_ShapeFromMesh "Part ShapeFromMesh"), [Create points object from geometry](/Part_PointsFromMesh "Part PointsFromMesh"), [Convert to solid](/Part_MakeSolid "Part MakeSolid"), [Reverse shapes](/Part_ReverseShape "Part ReverseShape"), [Create simple copy](/Part_SimpleCopy "Part SimpleCopy"), [Create transformed copy](/Part_TransformedCopy "Part TransformedCopy"), [Create shape element copy](/Part_ElementCopy "Part ElementCopy"), [Refine shape](/Part_RefineShape "Part RefineShape"), [Attachment](/Part_EditAttachment "Part EditAttachment")

* * *

  * **Preferences:** [Preferences](/PartDesign_Preferences "PartDesign Preferences"), [Fine tuning](/Fine-tuning "Fine-tuning")

