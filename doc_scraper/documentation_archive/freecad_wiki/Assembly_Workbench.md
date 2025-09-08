---
url: https://wiki.freecad.org/Assembly_Workbench
title: Assembly Workbench
scraped_at: 2025-09-08 16:43:53
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Tools Toggle Tools subsection
    * 2.1 Assembly
    * 2.2 Joints
  * 3 Preferences
  * 4 Example crank and slider Toggle Example crank and slider subsection
    * 4.1 Crank and slider assembly
    * 4.2 Prepare parts
    * 4.3 Add an assembly
    * 4.4 Move the parts into the assembly
    * 4.5 Ground a part
    * 4.6 Alternative: Insert Link
    * 4.7 Apply joints
      * 4.7.1 Note
    * 4.8 Drive the crank
  * 5 Example universal joint Toggle Example universal joint subsection
    * 5.1 Universal joint assembly
    * 5.2 Prepare parts
    * 5.3 Change angle of axles
    * 5.4 Add an assembly
    * 5.5 Move the axles into the assembly
    * 5.6 Ground the axles
    * 5.7 Move the solids into the assembly
    * 5.8 Apply joints
    * 5.9 Drive the universal joint
  * 6 Example vise Toggle Example vise subsection
    * 6.1 Assembly of a vise
    * 6.2 Prepare parts
    * 6.3 Add an assembly
    * 6.4 Move the parts into the assembly container
    * 6.5 Ground a part
    * 6.6 Apply joints
    * 6.7 Drive the vise
  * 7 Example shock absorber Toggle Example shock absorber subsection
    * 7.1 Assembly of a shock absorber
    * 7.2 Prepare parts
    * 7.3 Add an assembly
    * 7.4 Move the parts into the assembly container
    * 7.5 Ground the two axles
    * 7.6 Apply joints
    * 7.7 Drive the shock absorber

# Assembly Workbench

  * [Page](/Assembly_Workbench "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Assembly_Workbench&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Assembly_Workbench)
  * [Edit](/index.php?title=Assembly_Workbench&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Assembly_Workbench&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Assembly_Workbench.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Assembly_Workbench&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Assembly_Workbench)
  * [Edit](/index.php?title=Assembly_Workbench&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Assembly_Workbench&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Assembly_Workbench&action=history)

General

  * [What links here](/Special:WhatLinksHere/Assembly_Workbench "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Assembly_Workbench "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Assembly_Workbench&oldid=1628569 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Assembly_Workbench&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Assembly_Workbench&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Assembly+Workbench&action=page&filter=&language=en)This is the approved
revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Assembly+Workbench&language=&task=view "Start translation for this language")
  * [Deutsch](/Assembly_Workbench/de "Arbeitsbereich Assembly \(100% translated\)")
  * English
  * [français](/Assembly_Workbench/fr "Atelier Assembly \(89% translated\)")
  * [italiano](/Assembly_Workbench/it "Assembly Workbench \(100% translated\)")
  * [polski](/Assembly_Workbench/pl "Środowisko pracy Złożenie \(100% translated\)")
  * [português do Brasil](/Assembly_Workbench/pt-br "Bancadas de trabalho Assembly \(2% translated\)")
  * [русский](/Assembly_Workbench/ru "Верстак Сборка \(Assembly\) \(1% translated\)")
  * [日本語](/Assembly_Workbench/ja "アセンブリーワークベンチ \(4% translated\)")
  * [한국어](/Assembly_Workbench/ko "조립 작업대 \(32% translated\)")

![](/images/6/6f/Arrow-left.svg) ![](/images/0/06/Freecad.svg) [Std
Base](/Std_Base "Std Base")

![](/images/0/05/Workbench_BIM.svg) [BIM Workbench](/BIM_Workbench "BIM
Workbench") ![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

[![](/images/c/cd/Workbench_Assembly.svg)](/index.php?title=File:Workbench_Assembly.svg&filetimestamp=20240325203121&)Assembly
workbench icon

## Introduction

[introduced in 1.0](/Release_notes_1.0 "Release notes 1.0")

The
[![](/images/c/cd/Workbench_Assembly.svg)](/index.php?title=File:Workbench_Assembly.svg&filetimestamp=20240325203121&)
Assembly Workbench is FreeCAD's new built-in assembly workbench. It uses the
open-source [Ondsel solver](https://github.com/Ondsel-
Development/OndselSolver).

[![](/images/thumb/9/96/Assembly_Workbench_Example.png/400px-
Assembly_Workbench_Example.png)](/index.php?title=File:Assembly_Workbench_Example.png&filetimestamp=20240904205026&)

## Tools

### Assembly

  * [![](/images/5/50/Assembly_CreateAssembly.svg)](/index.php?title=File:Assembly_CreateAssembly.svg&filetimestamp=20240325210059&) [New Assembly](/Assembly_CreateAssembly "Assembly CreateAssembly"): creates a root assembly in the current document, or a sub-assembly in a pre-existing active assembly.

  * [![](/images/0/06/Assembly_InsertLink.svg)](/index.php?title=File:Assembly_InsertLink.svg&filetimestamp=20240325202742&)[![](/images/3/34/Toolbar_flyout_arrow_blue_background.svg)](/index.php?title=File:Toolbar_flyout_arrow_blue_background.svg&filetimestamp=20221006081506&) Insert Component:

    

  * [![](/images/0/06/Assembly_InsertLink.svg)](/index.php?title=File:Assembly_InsertLink.svg&filetimestamp=20240325202742&) [Component](/Assembly_InsertLink "Assembly InsertLink"): inserts a component into the active assembly.

    

  * [![](/images/1/1d/Assembly_InsertNewPart.svg)](/index.php?title=File:Assembly_InsertNewPart.svg&filetimestamp=20241208200731&) [New Part](/Assembly_InsertNewPart "Assembly InsertNewPart"): inserts a new Part.

  * [![](/images/4/4a/Assembly_SolveAssembly.svg)](/index.php?title=File:Assembly_SolveAssembly.svg&filetimestamp=20240522173434&) [Solve Assembly](/Assembly_SolveAssembly "Assembly SolveAssembly"): solves the currently active assembly.

  * [![](/images/e/e8/Assembly_CreateView.svg)](/index.php?title=File:Assembly_CreateView.svg&filetimestamp=20240509211759&) [Exploded View](/Assembly_CreateView "Assembly CreateView"): creates an exploded views container in the active assembly that contains one or more exploded views.

  * [![](/images/2/22/Assembly_CreateSimulation.svg)](/index.php?title=File:Assembly_CreateSimulation.svg&filetimestamp=20241203203040&) [Simulation](/Assembly_CreateSimulation "Assembly CreateSimulation"): creates a simulation of the current assembly. [introduced in 1.1](/Release_notes_1.1 "Release notes 1.1")

  * [![](/images/c/c8/Assembly_CreateBom.svg)](/index.php?title=File:Assembly_CreateBom.svg&filetimestamp=20240618223458&) [Bill of Materials](/Assembly_CreateBom "Assembly CreateBom"): creates a bill of materials (BOM) from a selected assembly or from the document.

  * [![](/images/f/f3/Assembly_ExportASMT.svg)](/index.php?title=File:Assembly_ExportASMT.svg&filetimestamp=20240522173404&) Export ASMT File: exports data of the currently active assembly as an ASMT file for debugging purposes.

    This tool aims at developers and will not be included in future releases. (see [forum thread](https://forum.freecad.org/viewtopic.php?p=812936#p812925))

### Joints

  * [![](/images/e/ec/Assembly_ToggleGrounded.svg)](/index.php?title=File:Assembly_ToggleGrounded.svg&filetimestamp=20240325202841&) [Toggle Grounded](/Assembly_ToggleGrounded "Assembly ToggleGrounded"): fixes the position and orientation of a shape in relation to the coordinate system of the assembly it belongs to.

  * [![](/images/c/cd/Assembly_CreateJointFixed.svg)](/index.php?title=File:Assembly_CreateJointFixed.svg&filetimestamp=20240325202632&) [Fixed Joint](/Assembly_CreateJointFixed "Assembly CreateJointFixed"): creates a joint locking two assembly parts together, preventing any movement or rotation but can be also used to define other types of joints.

  * [![](/images/4/47/Assembly_CreateJointRevolute.svg)](/index.php?title=File:Assembly_CreateJointRevolute.svg&filetimestamp=20240325202653&) [Revolute Joint](/Assembly_CreateJointRevolute "Assembly CreateJointRevolute"): creates a hinged joint, allowing rotation around a single axis between two selected parts.

  * [![](/images/2/29/Assembly_CreateJointCylindrical.svg)](/index.php?title=File:Assembly_CreateJointCylindrical.svg&filetimestamp=20240325202607&) [Cylindrical Joint](/Assembly_CreateJointCylindrical "Assembly CreateJointCylindrical"): creates a cylindrical joint between two selected parts, allowing rotation around a single axis and a movement along the same axis.

  * [![](/images/4/40/Assembly_CreateJointSlider.svg)](/index.php?title=File:Assembly_CreateJointSlider.svg&filetimestamp=20240325202709&) [Slider Joint](/Assembly_CreateJointSlider "Assembly CreateJointSlider"): creates a slider (prismatic) joint between two selected parts, allowing a linear movement along a single axis while restricting rotation.

  * [![](/images/4/4d/Assembly_CreateJointBall.svg)](/index.php?title=File:Assembly_CreateJointBall.svg&filetimestamp=20240325202552&) [Ball Joint](/Assembly_CreateJointBall "Assembly CreateJointBall"): creates a spherical joint between two selected parts at a single point, allowing free rotation around the point while keeping both parts connected at this point.

  * [![](/images/f/fb/Assembly_CreateJointDistance.svg)](/index.php?title=File:Assembly_CreateJointDistance.svg&filetimestamp=20240325202620&) [Distance Joint](/Assembly_CreateJointDistance "Assembly CreateJointDistance"): creates a distance joint between two selected parts, fixing the distance between both parts.

  * [![](/images/0/0f/Assembly_CreateJointParallel.svg)](/index.php?title=File:Assembly_CreateJointParallel.svg&filetimestamp=20240528153313&) [Parallel Joint](/Assembly_CreateJointParallel "Assembly CreateJointParallel"): creates a parallel joint between two selected parts, setting the Z axes of selected coordinate systems parallel.

  * [![](/images/8/80/Assembly_CreateJointPerpendicular.svg)](/index.php?title=File:Assembly_CreateJointPerpendicular.svg&filetimestamp=20240528153414&) [Perpendicular Joint](/Assembly_CreateJointPerpendicular "Assembly CreateJointPerpendicular"): creates a perpendicular joint between two selected parts, setting the Z axes of selected coordinate systems perpendicular.

  * [![](/images/b/be/Assembly_CreateJointAngle.svg)](/index.php?title=File:Assembly_CreateJointAngle.svg&filetimestamp=20240528153443&) [Angle Joint](/Assembly_CreateJointAngle "Assembly CreateJointAngle"): creates an angle joint between two selected parts, fixing the angle between the Z axes of selected coordinate systems.

  * [![](/images/8/84/Assembly_CreateJointRackPinion.svg)](/index.php?title=File:Assembly_CreateJointRackPinion.svg&filetimestamp=20240509205609&) [Rack and Pinion Joint](/Assembly_CreateJointRackPinion "Assembly CreateJointRackPinion"): creates a rack and pinion joint that couples the translation of a part of a slider joint and the rotation of a part of a revolute joint.

  * [![](/images/c/cc/Assembly_CreateJointScrew.svg)](/index.php?title=File:Assembly_CreateJointScrew.svg&filetimestamp=20240509205753&) [Screw Joint](/Assembly_CreateJointScrew "Assembly CreateJointScrew"): creates a screw (helical) joint that couples the translation of a part of a slider joint and the rotation of a part of a revolute joint.

  * [![](/images/b/b2/Assembly_CreateJointGears.svg)](/index.php?title=File:Assembly_CreateJointGears.svg&filetimestamp=20240509210706&)[![](/images/3/34/Toolbar_flyout_arrow_blue_background.svg)](/index.php?title=File:Toolbar_flyout_arrow_blue_background.svg&filetimestamp=20221006081506&) Gear/Belt Joint:

    

  * [![](/images/b/b2/Assembly_CreateJointGears.svg)](/index.php?title=File:Assembly_CreateJointGears.svg&filetimestamp=20240509210706&) [Gears Joint](/Assembly_CreateJointGears "Assembly CreateJointGears"): creates a gears joint that couples the rotation of two parts of two different revolute joints.

    

  * [![](/images/7/71/Assembly_CreateJointBelt.svg)](/index.php?title=File:Assembly_CreateJointBelt.svg&filetimestamp=20240509211259&) [Belt Joint](/Assembly_CreateJointBelt "Assembly CreateJointBelt"): creates a belt joint that couples the rotation of two parts of two different revolute joints.

## Preferences

  * [![](/images/0/01/Preferences-assembly.svg)](/index.php?title=File:Preferences-assembly.svg&filetimestamp=20240325202921&) [Preferences](/Assembly_Preferences "Assembly Preferences"): preferences for the Assembly workbench.

## Example crank and slider

Expand

[![](/images/thumb/0/05/Assembly3_KinematicExample-01.png/80px-
Assembly3_KinematicExample-01.png)](/index.php?title=File:Assembly3_KinematicExample-01.png&filetimestamp=20220426134647&)
This example is temporary and may be removed once proper
descriptions/tutorials are available.

### Crank and slider assembly

The assembly to be created consists of four parts: a Base, a Slider Rod, a
Crank, and a Connecting Rod. They are connected with four joints.

[![](/images/thumb/0/05/Assembly3_KinematicExample-01.png/300px-
Assembly3_KinematicExample-01.png)](/index.php?title=File:Assembly3_KinematicExample-01.png&filetimestamp=20220426134647&)

Assembled parts: Base (amber), Slider Rod (light blue), Crank (red),
Connecting Rod (green)

### Prepare parts

In this example all parts and the assembly are created in one document.

The cylindrical geometries of the objects are either parallel or
perpendicular, the rest of the shapes is not relevant for this example unless
there are clashes. With this in mind you can model your own objects or create
them with the Python code below. The code will create a new document with the
four objects (simpler than in the images). Just copy-paste the following lines
in the [Python console](/Python_console "Python console"):

    
    
    import FreeCAD as App
    import FreeCADGui as Gui
    import Part
    
    doc = App.newDocument()
    
    box1 = Part.makeBox(140, 40, 7, App.Vector(0, -20, 0))
    cyl1 = Part.makeCylinder(4, 8, App.Vector(120, 0, 7))
    box2 = Part.makeBox(20, 12, 10, App.Vector(5, -6, 7))
    cyl2 = Part.makeCylinder(6, 20, App.Vector(25, 0, 17), App.Vector(-1, 0, 0))
    cyl3 = Part.makeCylinder(4, 20, App.Vector(25, 0, 17), App.Vector(-1, 0, 0))
    shape = box1.fuse([cyl1, box2, cyl2]).removeSplitter().cut(cyl3)
    base = doc.addObject("Part::Feature", "Base")
    base.Shape = shape
    
    box1 = Part.makeBox(4, 12, 12, App.Vector(-12, -6, 0))
    box2 = Part.makeBox(14, 12, 4, App.Vector(-8, -6, 0))
    cyl1 = Part.makeCylinder(4, 8, App.Vector(0, 0, 4))
    cyl2 = Part.makeCylinder(4, 88, App.Vector(-12, 0, 6),App.Vector(-1, 0, 0))
    shape = box1.fuse([box2, cyl1, cyl2]).removeSplitter()
    slider_rod = doc.addObject("Part::Feature", "SliderRod")
    slider_rod.Shape = shape
    slider_rod.Placement.Base = App.Vector(100, -40, 0)
    
    cyl1 = Part.makeCylinder(7.5, 4)
    box1 = Part.makeBox(15, 30, 4, App.Vector(-7.5, 0, 0))
    cyl2 = Part.makeCylinder(7.5, 4, App.Vector(0, 30, 0))
    cyl3 = Part.makeCylinder(4, 6, App.Vector(0, 30, 4))
    cyl4 = Part.makeCylinder(4, 4)
    shape = cyl1.fuse([box1, cyl2]).removeSplitter().fuse(cyl3).cut(cyl4)
    crank = doc.addObject("Part::Feature", "Crank")
    crank.Shape = shape
    crank.Placement.Base = App.Vector(125, -70, 0)
    
    cyl1 = Part.makeCylinder(6, 4)
    box1 = Part.makeBox(50, 12, 4, App.Vector(0, -6, 0))
    cyl2 = Part.makeCylinder(6, 4, App.Vector(50, 0, 0))
    cyl3 = Part.makeCylinder(4, 4)
    cyl4 = Part.makeCylinder(4, 4, App.Vector(50, 0, 0))
    shape = cyl1.fuse([box1, cyl2]).removeSplitter().cut(cyl3.fuse(cyl4))
    connecting_rod = doc.addObject("Part::Feature", "ConnectingRod")
    connecting_rod.Shape = shape
    connecting_rod.Placement.Base = App.Vector(25, -70, 0)
    
    mat = base.ViewObject.ShapeAppearance[0]
    mat.DiffuseColor = (0.80, 0.60, 0.15, 0.0)
    base.ViewObject.ShapeAppearance = (mat,)
    
    mat = slider_rod.ViewObject.ShapeAppearance[0]
    mat.DiffuseColor = (0.55, 0.70, 0.70, 0.0)
    slider_rod.ViewObject.ShapeAppearance = (mat,)
    
    mat = crank.ViewObject.ShapeAppearance[0]
    mat.DiffuseColor = (0.70, 0.30, 0.20, 0.0)
    crank.ViewObject.ShapeAppearance = (mat,)
    
    mat = connecting_rod.ViewObject.ShapeAppearance[0]
    mat.DiffuseColor = (0.55, 0.70, 0.0, 0.0)
    connecting_rod.ViewObject.ShapeAppearance = (mat,)
    
    doc.recompute()
    view = Gui.ActiveDocument.ActiveView
    view.viewIsometric()
    view.fitAll()
    

### Add an assembly

With the
[![](/images/5/50/Assembly_CreateAssembly.svg)](/index.php?title=File:Assembly_CreateAssembly.svg&filetimestamp=20240325210059&)
[Create Assembly](/Assembly_CreateAssembly "Assembly CreateAssembly") tool add
an assembly to the document.

[![](/images/thumb/b/b6/Assembly_KinematicExample-01.png/200px-
Assembly_KinematicExample-01.png)](/index.php?title=File:Assembly_KinematicExample-01.png&filetimestamp=20241029150914&)

Tree view of Parts and Assembly

### Move the parts into the assembly

In the [Tree view](/Tree_view "Tree view") drag and drop the parts on the
Assembly object. They can now be handled by the Assembly's solver.

[![](/images/thumb/e/e3/Assembly_KinematicExample-02.png/200px-
Assembly_KinematicExample-02.png)](/index.php?title=File:Assembly_KinematicExample-02.png&filetimestamp=20241029150939&)

The Parts are in the Assembly container now

### Ground a part

To keep the assembly at the desired position, the base part should be locked,
or grounded as it is called here. Select the Base in the [Tree
view](/Tree_view "Tree view") or in the [3D view](/3D_view "3D view") and use
the
[![](/images/e/ec/Assembly_ToggleGrounded.svg)](/index.php?title=File:Assembly_ToggleGrounded.svg&filetimestamp=20240325202841&)
[Toggle grounded](/Assembly_ToggleGrounded "Assembly ToggleGrounded") tool.
This fixes the position of the Base in relation to the local coordinate system
(LCS) of the Assembly container. A GroundedJoint object is added to the Joints
container.

[![](/images/thumb/e/e1/Assembly_KinematicExample-03.png/200px-
Assembly_KinematicExample-03.png)](/index.php?title=File:Assembly_KinematicExample-03.png&filetimestamp=20241029150955&)
![](/images/5/52/Button_right.svg)
[![](/images/thumb/8/8a/Assembly_KinematicExample-04.png/240px-
Assembly_KinematicExample-04.png)](/index.php?title=File:Assembly_KinematicExample-04.png&filetimestamp=20241029151010&)

Expand the Joints container to find the GroundedJoint object

### Alternative: Insert Link

Instead of the two steps mentioned above it is also possible to use the
[![](/images/0/06/Assembly_InsertLink.svg)](/index.php?title=File:Assembly_InsertLink.svg&filetimestamp=20240325202742&)
[Insert Link](/Assembly_InsertLink "Assembly InsertLink") tool to place
objects inside an assembly. The first object automatically becomes the
grounded part. So you need to start with the Base object. The tool creates
links and the original objects remain outside the assembly. To avoid confusion
it is advisable to make them invisible.

### Apply joints

A joint connects exactly two elements of different parts. They can optionally
be selected before the desired joint tool is invoked (any number of selected
elements other than two results in an empty selection). The elements define
the position and orientation of a LCS represented by a filled circle on the
local XY plane and three lines along the local X (red), Y (green), and Z
(blue) axes.

  * A Revolute joint between Base and Crank

[![](/images/thumb/0/08/Assembly_KinematicExample-05.png/200px-
Assembly_KinematicExample-05.png)](/index.php?title=File:Assembly_KinematicExample-05.png&filetimestamp=20240430120912&)
![](/images/5/52/Button_right.svg)
[![](/images/thumb/3/3a/Assembly_KinematicExample-06.png/200px-
Assembly_KinematicExample-06.png)](/index.php?title=File:Assembly_KinematicExample-06.png&filetimestamp=20240430120937&)

Selected elements +
[![](/images/4/47/Assembly_CreateJointRevolute.svg)](/index.php?title=File:Assembly_CreateJointRevolute.svg&filetimestamp=20240325202653&)
[Create Revolute Joint](/Assembly_CreateJointRevolute "Assembly
CreateJointRevolute") → rearranged Crank

Move the **Crank** using the left mouse button. Only a rotation around the
pivot should be possible.

  * A Slider joint between Base and Slider Rod

[![](/images/thumb/2/20/Assembly_KinematicExample-07.png/200px-
Assembly_KinematicExample-07.png)](/index.php?title=File:Assembly_KinematicExample-07.png&filetimestamp=20240430121049&)
![](/images/5/52/Button_right.svg)
[![](/images/thumb/d/da/Assembly_KinematicExample-08.png/200px-
Assembly_KinematicExample-08.png)](/index.php?title=File:Assembly_KinematicExample-08.png&filetimestamp=20240430121110&)

Selected elements +
[![](/images/4/40/Assembly_CreateJointSlider.svg)](/index.php?title=File:Assembly_CreateJointSlider.svg&filetimestamp=20240325202709&)
[Create Slider Joint](/Assembly_CreateJointSlider "Assembly
CreateJointSlider") → rearranged Slider Rod

Move the **SliderRod** using the left mouse button. Only a displacement along
its centerline should be possible.

  * A Revolute joint between Crank and Connecting Rod

[![](/images/thumb/3/34/Assembly_KinematicExample-09.png/200px-
Assembly_KinematicExample-09.png)](/index.php?title=File:Assembly_KinematicExample-09.png&filetimestamp=20240430121344&)
![](/images/5/52/Button_right.svg)
[![](/images/thumb/c/c0/Assembly_KinematicExample-10.png/200px-
Assembly_KinematicExample-10.png)](/index.php?title=File:Assembly_KinematicExample-10.png&filetimestamp=20240430121414&)

Selected elements +
[![](/images/4/47/Assembly_CreateJointRevolute.svg)](/index.php?title=File:Assembly_CreateJointRevolute.svg&filetimestamp=20240325202653&)
[Create Revolute Joint](/Assembly_CreateJointRevolute "Assembly
CreateJointRevolute") → rearranged Connecting Rod

Move the **ConnectingRod** using the left mouse button. Only a rotation around
the pivot should be possible.

[![](/images/thumb/9/90/Assembly_KinematicExample-11.png/200px-
Assembly_KinematicExample-11.png)](/index.php?title=File:Assembly_KinematicExample-11.png&filetimestamp=20240430122216&)
![](/images/5/52/Button_right.svg)
[![](/images/thumb/6/61/Assembly_KinematicExample-12.png/200px-
Assembly_KinematicExample-12.png)](/index.php?title=File:Assembly_KinematicExample-12.png&filetimestamp=20240430122256&)

If there are several joints in a line we have to help the solver find a
sensible solution.  
If required, click and drag the parts into an easier to compute position.

  * A Cylindrical joint between Connecting Rod and Slider Rod

[![](/images/thumb/3/30/Assembly_KinematicExample-13.png/200px-
Assembly_KinematicExample-13.png)](/index.php?title=File:Assembly_KinematicExample-13.png&filetimestamp=20240430122516&)
![](/images/5/52/Button_right.svg)
[![](/images/thumb/e/e8/Assembly_KinematicExample-14.png/200px-
Assembly_KinematicExample-14.png)](/index.php?title=File:Assembly_KinematicExample-14.png&filetimestamp=20240430122536&)

Selected elements +
[![](/images/2/29/Assembly_CreateJointCylindrical.svg)](/index.php?title=File:Assembly_CreateJointCylindrical.svg&filetimestamp=20240325202607&)
[Create Cylindrical Joint](/Assembly_CreateJointCylindrical "Assembly
CreateJointCylindrical") → finished Assembly

In the finished assembly use the mouse pointer to drag the parts according to
the used joints.

#### Note

The pin of the Slider Rod is redundantly orientated. Its centerline is
parallel to the pin of the Base through the kinematic chain from Base via
Crank and Connecting Rod, i.e. its local Z axis cannot rotate around any X or
Y axis. The Slider joint also prevents the rotation of its Z axis around two
local axes and so results in two redundantly constrained degrees of freedom. A
Cylindrical joint instead of the Slider joint would only lock one rotation
resulting in only a single redundantly constrained degree of freedom.

### Drive the crank

To control the layout of the assembly by the angle between the Base and the
Crank we have to change the Revolute joint between them to a Fixed joint. To
do so double-click the Revolute object in the Tree view. In the dialog change
Revolute to Fixed and change the Rotation value as desired (the movement
should follow the mouse wheel action).

Note that a joint type change will change the joint's Label, but not its Name.
In this case the Label is changed to "Fixed".

To animate the assembly we can change the Rotation (Offset1.Angle) of the
Fixed joint with Python code. Just copy-paste the following lines in the
Python console:

    
    
    import math
    import FreeCAD as App
    import FreeCADGui as Gui
    
    actuator = App.ActiveDocument.getObjectsByLabel("Fixed")[0]
    
    for angle in range(0, 361, 10):
        # A full rotation of the Crank in steps of 10°
        actuator.Offset1.Rotation.Angle = math.radians(angle)
        App.ActiveDocument.recompute()
        Gui.updateGui()
    

The end of the range must be greater than 360 to also include this angle as a
valid result.

## Example universal joint

Expand

[![](/images/thumb/2/2f/Assembly_UniversalJointExample-01.png/80px-
Assembly_UniversalJointExample-01.png)](/index.php?title=File:Assembly_UniversalJointExample-01.png&filetimestamp=20241130122446&)
This example is temporary and may be removed once proper
descriptions/tutorials are available.

### Universal joint assembly

[![](/images/thumb/2/2f/Assembly_UniversalJointExample-01.png/300px-
Assembly_UniversalJointExample-01.png)](/index.php?title=File:Assembly_UniversalJointExample-01.png&filetimestamp=20241130122446&)

In this example a [universal
joint](https://en.wikipedia.org/wiki/Universal_joint) is created.

The assembly consists of three solid parts: two identical Forks and a Cross.
Two additional non solid elements, Axle1 and Axle2, representing the angled
axles, are also needed. The axles and the solid parts are connected with
several joints.

### Prepare parts

In this example all parts and the assembly are created in one document.

The Python code below will create a new document with four objects (only 1
Fork). Just copy-paste the following lines in the [Python
console](/Python_console "Python console"):

    
    
    import math
    import FreeCAD as App
    import FreeCADGui as Gui
    import Part
    
    doc = App.newDocument()
    
    axle1 = doc.addObject("Part::Line", "Axle1")
    axle1.X2 = -80
    axle1.Y2 = 0
    axle1.Z2 = 0
    
    axle2 = doc.addObject("Part::Line", "Axle2")
    axle2.X2 = 80
    axle2.Y2 = 0
    axle2.Z2 = 0
    axle2.Placement.Rotation.Angle = math.radians(20)
    
    sph1 = Part.makeSphere(50, App.Vector(0, 0, 0), App.Vector(-1, 0, 0), 0, 90, 360)
    box1 = Part.makeBox(50, 40, 80, App.Vector(-50, -20, -40))
    cyl1 = Part.makeCylinder(20, 80, App.Vector(0, 0, -40))
    cyl2 = Part.makeCylinder(20, 80, App.Vector(0, 0, 0), App.Vector(-1, 0, 0))
    cyl3 = Part.makeCylinder(30, 60, App.Vector(0, -30, 0), App.Vector(0, 1, 0))
    box2 = Part.makeBox(30, 60, 60, App.Vector(0, -30, -30))
    cyl4 = Part.makeCylinder(15, 80, App.Vector(0, 0, -40))
    cyl5 = Part.makeCylinder(15, 80, App.Vector(0, 0, 0), App.Vector(-1, 0, 0))
    shape = sph1.common(box1).fuse([cyl1, cyl2]).cut(cyl3.fuse([box2, cyl4, cyl5]))
    fork = doc.addObject("Part::Feature", "Fork")
    fork.Shape = shape.removeSplitter()
    fork.Placement.Base = App.Vector(0, 100, 0)
    
    cyl1 = Part.makeCylinder(15, 80, App.Vector(0, 0, -40))
    cyl2 = Part.makeCylinder(15, 80, App.Vector(0, -40, 0), App.Vector(0, 1, 0))
    shape = cyl1.fuse([cyl2])
    cross = doc.addObject("Part::Feature", "Cross")
    cross.Shape = shape.removeSplitter()
    cross.Placement.Base = App.Vector(70, 100, 0)
    
    mat = fork.ViewObject.ShapeAppearance[0]
    mat.DiffuseColor = (0.80, 0.60, 0.15, 0.0)
    fork.ViewObject.ShapeAppearance = (mat,)
    
    mat = cross.ViewObject.ShapeAppearance[0]
    mat.DiffuseColor = (0.55, 0.70, 0.70, 0.0)
    cross.ViewObject.ShapeAppearance = (mat,)
    
    doc.recompute()
    view = Gui.ActiveDocument.ActiveView
    view.viewIsometric()
    view.fitAll()
    

### Change angle of axles

The angle between the axles is set to 20 degrees. If you want to change this
value select Axle2 and change the Placement.Angle property. This property must
be changed before moving Axle2 into the assembly.

Warning: parts may collide if the angle is too large.

### Add an assembly

With the
[![](/images/5/50/Assembly_CreateAssembly.svg)](/index.php?title=File:Assembly_CreateAssembly.svg&filetimestamp=20240325210059&)
[Create Assembly](/Assembly_CreateAssembly "Assembly CreateAssembly") tool add
an assembly to the document.

### Move the axles into the assembly

In the [Tree view](/Tree_view "Tree view") drag and drop the axles on the
Assembly object.

### Ground the axles

Select the two axles in the Tree view and use the
[![](/images/e/ec/Assembly_ToggleGrounded.svg)](/index.php?title=File:Assembly_ToggleGrounded.svg&filetimestamp=20240325202841&)
[Toggle grounded](/Assembly_ToggleGrounded "Assembly ToggleGrounded") tool.

### Move the solids into the assembly

For the other objects we will use the
[![](/images/0/06/Assembly_InsertLink.svg)](/index.php?title=File:Assembly_InsertLink.svg&filetimestamp=20240325202742&)
[Insert Component](/Assembly_InsertLink "Assembly InsertLink") tool:

  1. Invoke the tool.
  2. In the dialog that opens click the Cross object once, and the Fork object twice.
  3. Press the OK button.
  4. Make the objects outside the assembly invisible.
  5. If the objects inside the assembly overlap too much you can drag them to a new position.

### Apply joints

  * A Revolute joint between Axle1 and Fork001

[![](/images/thumb/e/e7/Assembly_UniversalJointExample-02.png/200px-
Assembly_UniversalJointExample-02.png)](/index.php?title=File:Assembly_UniversalJointExample-02.png&filetimestamp=20241130122447&)
![](/images/5/52/Button_right.svg)
[![](/images/thumb/d/d8/Assembly_UniversalJointExample-03.png/200px-
Assembly_UniversalJointExample-03.png)](/index.php?title=File:Assembly_UniversalJointExample-03.png&filetimestamp=20241130122448&)

Selected elements +
[![](/images/4/47/Assembly_CreateJointRevolute.svg)](/index.php?title=File:Assembly_CreateJointRevolute.svg&filetimestamp=20240325202653&)
[Create Revolute Joint](/Assembly_CreateJointRevolute "Assembly
CreateJointRevolute") \+ Offset of +40mm or -40mm → rearranged Fork001

If you invoke the tool first and then select the elements, you can click near
the correct endpoint of Axle1 to avoid having to enter an offset.

  * A Cylindrical joint between Fork001 and Cross001

[![](/images/thumb/7/71/Assembly_UniversalJointExample-04.png/200px-
Assembly_UniversalJointExample-04.png)](/index.php?title=File:Assembly_UniversalJointExample-04.png&filetimestamp=20241130122450&)
![](/images/5/52/Button_right.svg)
[![](/images/thumb/1/12/Assembly_UniversalJointExample-05.png/200px-
Assembly_UniversalJointExample-05.png)](/index.php?title=File:Assembly_UniversalJointExample-05.png&filetimestamp=20241130122451&)

Selected elements +
[![](/images/2/29/Assembly_CreateJointCylindrical.svg)](/index.php?title=File:Assembly_CreateJointCylindrical.svg&filetimestamp=20240325202607&)
[Create Cylindrical Joint](/Assembly_CreateJointCylindrical "Assembly
CreateJointCylindrical") → rearranged Cross001

  * A Cylindrical joint between Axle2 and Fork002

[![](/images/thumb/9/9a/Assembly_UniversalJointExample-06.png/200px-
Assembly_UniversalJointExample-06.png)](/index.php?title=File:Assembly_UniversalJointExample-06.png&filetimestamp=20241130122452&)
![](/images/5/52/Button_right.svg)
[![](/images/thumb/8/82/Assembly_UniversalJointExample-07.png/200px-
Assembly_UniversalJointExample-07.png)](/index.php?title=File:Assembly_UniversalJointExample-07.png&filetimestamp=20241130122453&)

Selected elements +
[![](/images/2/29/Assembly_CreateJointCylindrical.svg)](/index.php?title=File:Assembly_CreateJointCylindrical.svg&filetimestamp=20240325202607&)
[Create Cylindrical Joint](/Assembly_CreateJointCylindrical "Assembly
CreateJointCylindrical") → rearranged Fork002

If required reverse the direction of the joint using the
[![](/images/c/cc/Button_sort.svg)](/index.php?title=File:Button_sort.svg&filetimestamp=20240704190908&)
button in the task panel.

  * A Cylindrical joint between Cross001 and Fork002

[![](/images/thumb/f/f5/Assembly_UniversalJointExample-08.png/200px-
Assembly_UniversalJointExample-08.png)](/index.php?title=File:Assembly_UniversalJointExample-08.png&filetimestamp=20241130122455&)
![](/images/5/52/Button_right.svg)
[![](/images/thumb/7/70/Assembly_UniversalJointExample-09.png/200px-
Assembly_UniversalJointExample-09.png)](/index.php?title=File:Assembly_UniversalJointExample-09.png&filetimestamp=20241130122456&)

Selected elements +
[![](/images/2/29/Assembly_CreateJointCylindrical.svg)](/index.php?title=File:Assembly_CreateJointCylindrical.svg&filetimestamp=20240325202607&)
[Create Cylindrical Joint](/Assembly_CreateJointCylindrical "Assembly
CreateJointCylindrical") → rearranged Cross001 and Fork002

### Drive the universal joint

The universal joint can be driven by moving Fork001 with the left mouse.

If you want to check the situation at distinct rotation angles do the
following:

  1. Change the Cylindrical joint between Axle1 and Fork001 to a Fixed joint.
  2. Select the Offset1.Angle property of the Fixed joint and roll the mouse wheel.
  3. The universal joint may be positioned to any angle.

## Example vise

Expand

[![](/images/thumb/3/30/Assembly_ViseExample-01.png/80px-
Assembly_ViseExample-01.png)](/index.php?title=File:Assembly_ViseExample-01.png&filetimestamp=20241130122457&)
This example is temporary and may be removed once proper
descriptions/tutorials are available.

### Assembly of a vise

[![](/images/thumb/3/30/Assembly_ViseExample-01.png/300px-
Assembly_ViseExample-01.png)](/index.php?title=File:Assembly_ViseExample-01.png&filetimestamp=20241130122457&)

In this example a [vise](https://en.wikipedia.org/wiki/Vise) is created.

The assembly consists of three solid parts: a fixed and a movable jaw and a
screw with a lever. One additional non solid element, a crank, is also needed.
The crank and the solid parts are connected with several joints.

A Screw Joint couples the translation of a part with a Slider Joint to the
rotation of a part with a Revolute Joint. The screw part shall make both a
translation and a rotation movement hence it must be a part with a Cylindrical
Joint. In this assembly, the screw part will be coupled to the movable jaw
with a Distance Joint, to the non solid crank with a Parallel Joint, and to
the fixed jaw with a Cylindrical Joint.

### Prepare parts

In this example all parts and the assembly are created in one document.

The Python code below will create a new document with four objects. Just copy-
paste the following lines in the [Python console](/Python_console "Python
console"):

    
    
    import math
    import FreeCAD as App
    import FreeCADGui as Gui
    import Part
    
    doc = App.newDocument()
    
    box1 = Part.makeBox(95, 40, 75, App.Vector(0, -20, -22))
    cyl1 = Part.makeCylinder(35, 80, App.Vector(0, -40, 53), App.Vector(0, 1, 0), 90)
    box2 = Part.makeBox(20, 80, 30, App.Vector(-20, -40, 58))
    cyl2 = Part.makeCylinder(15, 80, App.Vector(-15, -40, 58), App.Vector(0, 1, 0), 90)
    box3 = Part.makeBox(5, 80, 15, App.Vector(-20, -40, 58))
    box4 = Part.makeBox(35, 24, 24, App.Vector(0, -12, -12))
    box5 = Part.makeBox(60, 34, 69, App.Vector(35, -17, -19))
    cyl3 = Part.makeCylinder(20, 55, App.Vector(-20, -40, 53), App.Vector(1, 0, 0))
    cyl4 = Part.makeCylinder(20, 55, App.Vector(-20, 40, 53), App.Vector(1, 0, 0))
    cyl5 = Part.makeCylinder(5, 35, App.Vector(0, 0, 38), App.Vector(1, 0, 0))
    box6 = Part.makeBox(7, 88, 15, App.Vector(-22, -44, 75))
    box7 = Part.makeBox(95, 90, 10, App.Vector(0, -45, -32))
    shape = box1.fuse([cyl1, box2, box6, box7]).cut(cyl2.fuse([box3, cyl3, cyl4, cyl5, box4, box5]))
    fixedJaw = doc.addObject("Part::Feature", "FixedJaw")
    fixedJaw.Shape = shape.removeSplitter()
    fixedJaw.Placement.Rotation.Axis = App.Vector(0, 0, 1)
    fixedJaw.Placement.Rotation.Angle = math.radians(180)
    
    box1 = Part.makeBox(35, 40, 75, App.Vector(0, -20, -22))
    cyl1 = Part.makeCylinder(35, 80, App.Vector(0, -40, 53), App.Vector(0, 1, 0), 90)
    box2 = Part.makeBox(20, 80, 30, App.Vector(-20, -40, 58))
    cyl2 = Part.makeCylinder(15, 80, App.Vector(-15, -40, 58), App.Vector(0, 1, 0), 90)
    box3 = Part.makeBox(160, 24, 24, App.Vector(-160, -12, -12))
    box4 = Part.makeBox(5, 80, 15, App.Vector(-20, -40, 58))
    box5 = Part.makeBox(160, 18, 18, App.Vector(-160, -9, -9))
    cyl3 = Part.makeCylinder(20, 55, App.Vector(-20, -40, 53), App.Vector(1, 0, 0))
    cyl4 = Part.makeCylinder(20, 55, App.Vector(-20, 40, 53), App.Vector(1, 0, 0))
    cyl5 = Part.makeCylinder(5, 35, App.Vector(0, 0, 38), App.Vector(1, 0, 0))
    box6 = Part.makeBox(7, 88, 15, App.Vector(-22, -44, 75))
    shape = box1.fuse([cyl1, box2, box3, box6]).cut(cyl2.fuse([box4, cyl3, cyl4, box5, cyl5]))
    movableJaw = doc.addObject("Part::Feature", "MovableJaw")
    movableJaw.Shape = shape.removeSplitter()
    movableJaw.Placement.Base = App.Vector(150, 100, 0)
    
    cyl1 = Part.makeCylinder(5, 190, App.Vector(0, 0, 0), App.Vector(1, 0, 0))
    cyl2 = Part.makeCylinder(10, 20, App.Vector(190, 0, 0), App.Vector(1, 0, 0))
    cyl3 = Part.makeCylinder(4, 100, App.Vector(200, 0, -50), App.Vector(0, 0, 1))
    shape = cyl1.fuse([cyl2, cyl3])
    leverScrew = doc.addObject("Part::Feature", "LeverScrew")
    leverScrew.Shape = shape.removeSplitter()
    leverScrew.Placement.Base = App.Vector(150, -100, 0)
    
    wire1 = Part.makePolygon([App.Vector(0, 0, 100), App.Vector(0, 0, 0), App.Vector(100, 0, 0)])
    crank = doc.addObject("Part::Feature", "Crank")
    crank.Shape = wire1
    crank.Placement.Base = App.Vector(0, -100, 0)
    
    mat = fixedJaw.ViewObject.ShapeAppearance[0]
    mat.DiffuseColor = (0.80, 0.60, 0.15, 0.0)
    fixedJaw.ViewObject.ShapeAppearance = (mat,)
    
    mat = movableJaw.ViewObject.ShapeAppearance[0]
    mat.DiffuseColor = (0.55, 0.70, 0.70, 0.0)
    movableJaw.ViewObject.ShapeAppearance = (mat,)
    
    mat = leverScrew.ViewObject.ShapeAppearance[0]
    mat.DiffuseColor = (0.70, 0.30, 0.20, 0.0)
    leverScrew.ViewObject.ShapeAppearance = (mat,)
    
    doc.recompute()
    view = Gui.ActiveDocument.ActiveView
    view.viewIsometric()
    view.fitAll()
    

### Add an assembly

With the
[![](/images/5/50/Assembly_CreateAssembly.svg)](/index.php?title=File:Assembly_CreateAssembly.svg&filetimestamp=20240325210059&)
[Create Assembly](/Assembly_CreateAssembly "Assembly CreateAssembly") tool add
an assembly to the document.

### Move the parts into the assembly container

In the [Tree view](/Tree_view "Tree view") drag and drop the parts on the
Assembly object. They can now be handled by the Assembly's solver.

### Ground a part

To keep the assembly at the desired position, the FixedJaw part should be
locked, or grounded as it is called here. Select the FixedJaw in the [Tree
view](/Tree_view "Tree view") or in the [3D view](/3D_view "3D view") and use
the
[![](/images/e/ec/Assembly_ToggleGrounded.svg)](/index.php?title=File:Assembly_ToggleGrounded.svg&filetimestamp=20240325202841&)
[Toggle grounded](/Assembly_ToggleGrounded "Assembly ToggleGrounded") tool. A
GroundedJoint object is added to the Joints container.

### Apply joints

  * A Revolute joint between FixedJaw and Crank

[![](/images/thumb/3/3d/Assembly_ViseExample-02.png/200px-
Assembly_ViseExample-02.png)](/index.php?title=File:Assembly_ViseExample-02.png&filetimestamp=20241130122458&)
![](/images/5/52/Button_right.svg)
[![](/images/thumb/3/37/Assembly_ViseExample-03.png/200px-
Assembly_ViseExample-03.png)](/index.php?title=File:Assembly_ViseExample-03.png&filetimestamp=20241130122459&)

Selected elements +
[![](/images/4/47/Assembly_CreateJointRevolute.svg)](/index.php?title=File:Assembly_CreateJointRevolute.svg&filetimestamp=20240325202653&)
[Create Revolute Joint](/Assembly_CreateJointRevolute "Assembly
CreateJointRevolute") → rearranged Crank

  * A Slider joint between FixedJaw and MovableJaw

[![](/images/thumb/7/7c/Assembly_ViseExample-04.png/200px-
Assembly_ViseExample-04.png)](/index.php?title=File:Assembly_ViseExample-04.png&filetimestamp=20241130122500&)
![](/images/5/52/Button_right.svg)
[![](/images/thumb/3/32/Assembly_ViseExample-05.png/200px-
Assembly_ViseExample-05.png)](/index.php?title=File:Assembly_ViseExample-05.png&filetimestamp=20241130122502&)

Selected elements +
[![](/images/4/40/Assembly_CreateJointSlider.svg)](/index.php?title=File:Assembly_CreateJointSlider.svg&filetimestamp=20240325202709&)
[Create Slider Joint](/Assembly_CreateJointSlider "Assembly
CreateJointSlider") → rearranged MovableJaw

Set the Min length to -77 mm and the Max length to -7 mm. This limits the
opening of the vise to 70 mm.

The next three joints are necessary to force the LeverScrew to: translate like
the MovableJaw, rotate like the Crank, and rotate around the main axis.

  * A Distance joint between LeverScrew and MovableJaw

[![](/images/thumb/c/c2/Assembly_ViseExample-06.png/200px-
Assembly_ViseExample-06.png)](/index.php?title=File:Assembly_ViseExample-06.png&filetimestamp=20241130122503&)
![](/images/5/52/Button_right.svg)
[![](/images/thumb/8/8c/Assembly_ViseExample-07.png/200px-
Assembly_ViseExample-07.png)](/index.php?title=File:Assembly_ViseExample-07.png&filetimestamp=20241130122504&)

Selected elements +
[![](/images/f/fb/Assembly_CreateJointDistance.svg)](/index.php?title=File:Assembly_CreateJointDistance.svg&filetimestamp=20240325202620&)
[Create Distance Joint](/Assembly_CreateJointDistance "Assembly
CreateJointDistance") → rearranged LeverScrew

Select two faces. Set the distance value to 20 mm.

  * A Parallel joint between LeverScrew and Crank

[![](/images/thumb/0/0f/Assembly_ViseExample-08.png/200px-
Assembly_ViseExample-08.png)](/index.php?title=File:Assembly_ViseExample-08.png&filetimestamp=20241130122506&)
![](/images/5/52/Button_right.svg)
[![](/images/thumb/4/4e/Assembly_ViseExample-09.png/200px-
Assembly_ViseExample-09.png)](/index.php?title=File:Assembly_ViseExample-09.png&filetimestamp=20241130122508&)

Selected elements +
[![](/images/0/0f/Assembly_CreateJointParallel.svg)](/index.php?title=File:Assembly_CreateJointParallel.svg&filetimestamp=20240528153313&)
[Create Parallel Joint](/Assembly_CreateJointParallel "Assembly
CreateJointParallel") → rearranged LeverScrew

  * A Cylindrical joint between LeverScrew and FixedJaw

[![](/images/thumb/9/96/Assembly_ViseExample-10.png/200px-
Assembly_ViseExample-10.png)](/index.php?title=File:Assembly_ViseExample-10.png&filetimestamp=20241130122509&)
![](/images/5/52/Button_right.svg)
[![](/images/thumb/0/00/Assembly_ViseExample-11.png/200px-
Assembly_ViseExample-11.png)](/index.php?title=File:Assembly_ViseExample-11.png&filetimestamp=20241130122511&)

Selected elements +
[![](/images/2/29/Assembly_CreateJointCylindrical.svg)](/index.php?title=File:Assembly_CreateJointCylindrical.svg&filetimestamp=20240325202607&)
[Create Cylindrical Joint](/Assembly_CreateJointCylindrical "Assembly
CreateJointCylindrical") → rearranged LeverScrew

  * A Screw joint between MovableJaw and Crank

[![](/images/thumb/d/d0/Assembly_ViseExample-12.png/200px-
Assembly_ViseExample-12.png)](/index.php?title=File:Assembly_ViseExample-12.png&filetimestamp=20241130122512&)
![](/images/5/52/Button_right.svg)
[![](/images/thumb/f/fb/Assembly_ViseExample-13.png/200px-
Assembly_ViseExample-13.png)](/index.php?title=File:Assembly_ViseExample-13.png&filetimestamp=20241130122514&)

Selected elements (LeverScrew invisible) +
[![](/images/c/cc/Assembly_CreateJointScrew.svg)](/index.php?title=File:Assembly_CreateJointScrew.svg&filetimestamp=20240509205753&)
[Create Screw Joint](/Assembly_CreateJointScrew "Assembly CreateJointScrew") →
complete vise mechanism (LeverScrew visible)

If necessary make the LeverScrew invisible during selection.

Set the Pitch radius to 5 mm

### Drive the vise

The vise can be driven by moving Crank or MovableJaw with the left mouse.

## Example shock absorber

Expand

[![](/images/thumb/0/05/Assembly_ShockAbsorberExample-01.png/80px-
Assembly_ShockAbsorberExample-01.png)](/index.php?title=File:Assembly_ShockAbsorberExample-01.png&filetimestamp=20241130122424&)
This example is temporary and may be removed once proper
descriptions/tutorials are available.

### Assembly of a shock absorber

[![](/images/a/aa/Assembly_ShockAbsorberExample.gif)](/index.php?title=File:Assembly_ShockAbsorberExample.gif&filetimestamp=20241130122445&)

In this example a [shock
absorber](https://en.wikipedia.org/wiki/Shock_absorber) is created.

The assembly consists of three solid parts: a piston, a cylinder and a spring.
Three additional non solid elements, two axles and a rod are also needed. All
parts are connected with several joints.

The hinge of the piston rotates around Axle2, while the hinge of the cylinder
moves on an arc of circle centered on Axle1. The non solid Rod is used for
this movement. The length of the Rod is the radius of the arc.

### Prepare parts

The Python code below will create a new document with 6 objects. Create a new
[macro](/Macros "Macros") and copy-paste the code below in the Python editor
(not in the Python console). Then [run the macro](/Std_DlgMacroExecuteDirect
"Std DlgMacroExecuteDirect").

The code below cannot be run from the Python console because the spring must
be a [Part::FeaturePython](/App_FeaturePython "App FeaturePython") object
defined by of a class with the callback functions `execute()` and
`onChanged()`. Only then can its height be changed via a property.

    
    
    import math
    import FreeCAD as App
    import FreeCADGui as Gui
    import Part
    
    doc = App.newDocument()
    
    class Spring():
        def __init__(self, spring):
            spring.addProperty("App::PropertyLength", "Height", "Spring", "Height of the helix").Height = 200.0
            spring.Proxy = self
            spring.ViewObject.Proxy = 0
            
        def execute(self, spring):
            helix = Part.makeHelix(spring.Height/8.5, spring.Height, 35)
            startPnt = helix.Edges[0].Curve.value(0)
            section = Part.Wire([Part.Circle(startPnt, App.Vector(0, 1, 0), 5).toShape()])
            hel1 = helix.makePipeShell([section], True, True)
            box1 = Part.makeBox(80, 80, 10, App.Vector(-40, -40, -10))
            box2 = Part.makeBox(80, 80, 10, App.Vector(-40, -40, spring.Height))
            shape = hel1.cut(box1).cut(box2)
            spring.Shape = shape
            
        def onChanged(self, spring, prop):
            if prop == "Height":
                self.execute(spring) 
                
    spring = doc.addObject("Part::FeaturePython", "Spring")
    Spring(spring)
    spring.Placement.Base = App.Vector(0, 100, 0)
    
    axle1 = doc.addObject("Part::Line", "Axle1")
    axle1.X2 = 0
    axle1.Y2 = 80
    axle1.Z2 = 0
    
    axle2 = doc.addObject("Part::Line", "Axle2")
    axle2.X2 = 0
    axle2.Y2 = 80
    axle2.Z2 = 0
    axle2.Placement.Base = App.Vector(120, 0, -250)
    
    rod = doc.addObject("Part::Line", "Rod")
    rod.X2 = 100
    rod.Y2 = 0
    rod.Z2 = 0
    rod.Placement.Base = App.Vector(0, -50, 0)
    
    cyl1 = Part.makeCylinder(40, 10,App.Vector(0, 0, -5))
    tor1 = Part.makeTorus(40, 5)
    cyl2 = Part.makeCylinder(45, 5)
    box1 = Part.makeBox(30, 10, 30,App.Vector(-15, -5, -35))
    cyl3 = Part.makeCylinder(15, 10, App.Vector(0, -5, -35), App.Vector(0, 1, 0))
    cyl4 = Part.makeCylinder(40, 5)
    cyl5 = Part.makeCylinder(5, 10,App.Vector(0, -5, -35), App.Vector(0, 1, 0))
    cyl6 = Part.makeCylinder(5, 130)
    cyl7 = Part.makeCylinder(20, 5,App.Vector(0, 0, 130))
    shape = cyl1.fuse([tor1,cyl2, box1, cyl3]).cut(cyl4.fuse([cyl5])).fuse([cyl6, cyl7])
    piston = doc.addObject("Part::Feature", "Piston")
    piston.Shape = shape.removeSplitter()
    piston.Placement.Base = App.Vector(200, 100, -200)
    
    cyl1 = Part.makeCylinder(40, 10,App.Vector(0, 0, -5))
    tor1 = Part.makeTorus(40, 5)
    cyl2 = Part.makeCylinder(45, 5)
    box1 = Part.makeBox(30, 10, 30,App.Vector(-15, -5, -35))
    cyl3 = Part.makeCylinder(15, 10,App.Vector(0, -5, -35), App.Vector(0, 1, 0))
    cyl4 = Part.makeCylinder(40, 5)
    cyl5 = Part.makeCylinder(5, 10,App.Vector(0, -5, -35), App.Vector(0, 1, 0))
    cyl6 = Part.makeCylinder(25, 130)
    tor2 = Part.makeTorus(20, 5,App.Vector(0, 0, 130))
    cyl7 = Part.makeCylinder(20, 135)
    cyl8 = Part.makeCylinder(20, 130)
    cyl9 = Part.makeCylinder(5, 135)
    shape = cyl1.fuse([tor1, cyl2, box1, cyl3]).cut(cyl4.fuse([cyl5])).fuse([cyl6, tor2, cyl7]).cut(cyl8.fuse([cyl9]))
    cylinder = doc.addObject("Part::Feature", "Cylinder")
    cylinder.Shape = shape.removeSplitter()
    cylinder.Placement.Rotation.Axis = App.Vector(0, 1, 0)
    cylinder.Placement.Rotation.Angle = math.pi
    cylinder.Placement.Base = App.Vector(100, 100, 0)
    
    mat = piston.ViewObject.ShapeAppearance[0]
    mat.DiffuseColor = (0.80, 0.60, 0.15, 0.0)
    piston.ViewObject.ShapeAppearance = (mat,)
    
    mat = cylinder.ViewObject.ShapeAppearance[0]
    mat.DiffuseColor = (0.55, 0.70, 0.70, 0.0)
    cylinder.ViewObject.ShapeAppearance = (mat,)
    
    doc.recompute()
    view = Gui.ActiveDocument.ActiveView
    view.viewIsometric()
    view.fitAll()
    

### Add an assembly

With the
[![](/images/5/50/Assembly_CreateAssembly.svg)](/index.php?title=File:Assembly_CreateAssembly.svg&filetimestamp=20240325210059&)
[Create Assembly](/Assembly_CreateAssembly "Assembly CreateAssembly") tool add
an assembly to the document.

### Move the parts into the assembly container

In the [Tree view](/Tree_view "Tree view") drag and drop the parts on the
Assembly object. They can now be handled by the Assembly's solver.

### Ground the two axles

To keep the assembly at the desired position, the two axles should be locked,
or grounded as it is called here. Select the two axles in the [Tree
view](/Tree_view "Tree view") or in the [3D view](/3D_view "3D view") and use
the
[![](/images/e/ec/Assembly_ToggleGrounded.svg)](/index.php?title=File:Assembly_ToggleGrounded.svg&filetimestamp=20240325202841&)
[Toggle grounded](/Assembly_ToggleGrounded "Assembly ToggleGrounded") tool.
Two GroundedJoint objects are added to the Joints container.

### Apply joints

  * A Revolute joint between Axle2 and Piston

[![](/images/thumb/1/1e/Assembly_ShockAbsorberExample-02.png/200px-
Assembly_ShockAbsorberExample-02.png)](/index.php?title=File:Assembly_ShockAbsorberExample-02.png&filetimestamp=20241130122425&)
![](/images/5/52/Button_right.svg)
[![](/images/thumb/e/e6/Assembly_ShockAbsorberExample-03.png/200px-
Assembly_ShockAbsorberExample-03.png)](/index.php?title=File:Assembly_ShockAbsorberExample-03.png&filetimestamp=20241130122426&)

[![](/images/4/47/Assembly_CreateJointRevolute.svg)](/index.php?title=File:Assembly_CreateJointRevolute.svg&filetimestamp=20240325202653&)
[Create Revolute Joint](/Assembly_CreateJointRevolute "Assembly
CreateJointRevolute") \+ Selected elements → rearranged Piston

  * A Slider joint between Piston and Cylinder

[![](/images/thumb/7/72/Assembly_ShockAbsorberExample-04.png/200px-
Assembly_ShockAbsorberExample-04.png)](/index.php?title=File:Assembly_ShockAbsorberExample-04.png&filetimestamp=20241130122427&)
![](/images/5/52/Button_right.svg)
[![](/images/thumb/e/e0/Assembly_ShockAbsorberExample-05.png/200px-
Assembly_ShockAbsorberExample-05.png)](/index.php?title=File:Assembly_ShockAbsorberExample-05.png&filetimestamp=20241130122428&)

[![](/images/4/40/Assembly_CreateJointSlider.svg)](/index.php?title=File:Assembly_CreateJointSlider.svg&filetimestamp=20240325202709&)
[Create Slider Joint](/Assembly_CreateJointSlider "Assembly
CreateJointSlider") \+ Selected elements → rearranged and moved Cylinder

Please pay attention to the location of the coordinate system before selecting
a face. It should be in the center of each face.

Drag the Cylinder to create some distinct between it and the Piston. The
supporting faces for the Spring should be visible.

  * A Distance joint between Piston and Cylinder

[![](/images/thumb/d/d9/Assembly_ShockAbsorberExample-06A.png/200px-
Assembly_ShockAbsorberExample-06A.png)](/index.php?title=File:Assembly_ShockAbsorberExample-06A.png&filetimestamp=20241130122429&)
![](/images/8/8e/List-add.svg)
[![](/images/thumb/0/00/Assembly_ShockAbsorberExample-06B.png/200px-
Assembly_ShockAbsorberExample-06B.png)](/index.php?title=File:Assembly_ShockAbsorberExample-06B.png&filetimestamp=20241130122430&)
![](/images/5/52/Button_right.svg)
[![](/images/thumb/c/c2/Assembly_ShockAbsorberExample-07.png/200px-
Assembly_ShockAbsorberExample-07.png)](/index.php?title=File:Assembly_ShockAbsorberExample-07.png&filetimestamp=20241130122432&)

[![](/images/f/fb/Assembly_CreateJointDistance.svg)](/index.php?title=File:Assembly_CreateJointDistance.svg&filetimestamp=20240325202620&)
[Create Distance Joint](/Assembly_CreateJointDistance "Assembly
CreateJointDistance") \+ Selected faces → rearranged Cylinder Distance set to
200 mm

Set the distance value to 200 mm.

The next two joints are necessary to force the hinge of the Cylinder to move
on an arc of circle.

  * A Cylindrical joint between Axle1 and Rod

[![](/images/thumb/6/6f/Assembly_ShockAbsorberExample-08.png/200px-
Assembly_ShockAbsorberExample-08.png)](/index.php?title=File:Assembly_ShockAbsorberExample-08.png&filetimestamp=20241130122433&)
![](/images/5/52/Button_right.svg)
[![](/images/thumb/9/96/Assembly_ShockAbsorberExample-09.png/200px-
Assembly_ShockAbsorberExample-09.png)](/index.php?title=File:Assembly_ShockAbsorberExample-09.png&filetimestamp=20241130122434&)

[![](/images/2/29/Assembly_CreateJointCylindrical.svg)](/index.php?title=File:Assembly_CreateJointCylindrical.svg&filetimestamp=20240325202607&)
[Create Cylindrical Joint](/Assembly_CreateJointCylindrical "Assembly
CreateJointCylindrical") \+ Selected elements → rearranged Rod

Make sure the Z axis of the coordinate system (blue) is perpendicular to the
Rod by selecting an endpoint.

  * A Revolute joint between Rod and Cylinder

[![](/images/thumb/2/26/Assembly_ShockAbsorberExample-10.png/200px-
Assembly_ShockAbsorberExample-10.png)](/index.php?title=File:Assembly_ShockAbsorberExample-10.png&filetimestamp=20241130122435&)
![](/images/5/52/Button_right.svg)
[![](/images/thumb/7/7e/Assembly_ShockAbsorberExample-11.png/200px-
Assembly_ShockAbsorberExample-11.png)](/index.php?title=File:Assembly_ShockAbsorberExample-11.png&filetimestamp=20241130122436&)

[![](/images/4/47/Assembly_CreateJointRevolute.svg)](/index.php?title=File:Assembly_CreateJointRevolute.svg&filetimestamp=20240325202653&)
[Create Revolute Joint](/Assembly_CreateJointRevolute "Assembly
CreateJointRevolute") \+ Selected elements → rearranged Cylinder

Again make sure the Z axis of the coordinate system (blue) is perpendicular to
the Rod.

You may encounter problems with this joint. If that is the case try the
following:

  1. Delete the joint.
  2. Switch to the [front view](/Std_ViewFront "Std ViewFront").
  3. Rotate the assembly (by dragging the Piston) and rotate the Rod so that center of the hinge hole of the Cylinder lies on the Rod.
  4. Create the joint again.

The next two joints are necessary to fix the Spring to the support face.

  * A Parallel joint between Spring and Piston

[![](/images/thumb/0/0a/Assembly_ShockAbsorberExample-12A.png/200px-
Assembly_ShockAbsorberExample-12A.png)](/index.php?title=File:Assembly_ShockAbsorberExample-12A.png&filetimestamp=20241130122437&)
![](/images/8/8e/List-add.svg)
[![](/images/thumb/0/05/Assembly_ShockAbsorberExample-12B.png/200px-
Assembly_ShockAbsorberExample-12B.png)](/index.php?title=File:Assembly_ShockAbsorberExample-12B.png&filetimestamp=20241130122439&)
![](/images/5/52/Button_right.svg)
[![](/images/thumb/3/37/Assembly_ShockAbsorberExample-13.png/200px-
Assembly_ShockAbsorberExample-13.png)](/index.php?title=File:Assembly_ShockAbsorberExample-13.png&filetimestamp=20241130122440&)

[![](/images/0/0f/Assembly_CreateJointParallel.svg)](/index.php?title=File:Assembly_CreateJointParallel.svg&filetimestamp=20240528153313&)
[Create Parallel Joint](/Assembly_CreateJointParallel "Assembly
CreateJointParallel") \+ Selected faces → rearranged Spring

Select the center of the support face on the Piston and the center of the
bottom face of the spring. Keep the distance value 0.

  * A Fixed joint between Spring and Piston

[![](/images/thumb/4/4f/Assembly_ShockAbsorberExample-14A.png/200px-
Assembly_ShockAbsorberExample-14A.png)](/index.php?title=File:Assembly_ShockAbsorberExample-14A.png&filetimestamp=20241130122442&)
![](/images/8/8e/List-add.svg)
[![](/images/thumb/b/b8/Assembly_ShockAbsorberExample-14B.png/200px-
Assembly_ShockAbsorberExample-14B.png)](/index.php?title=File:Assembly_ShockAbsorberExample-14B.png&filetimestamp=20241130122443&)
![](/images/5/52/Button_right.svg)
[![](/images/thumb/2/28/Assembly_ShockAbsorberExample-15.png/200px-
Assembly_ShockAbsorberExample-15.png)](/index.php?title=File:Assembly_ShockAbsorberExample-15.png&filetimestamp=20241130122444&)

[![](/images/c/cd/Assembly_CreateJointFixed.svg)](/index.php?title=File:Assembly_CreateJointFixed.svg&filetimestamp=20240325202632&)
[Create Fixed Joint](/Assembly_CreateJointFixed "Assembly CreateJointFixed")
\+ Selected elements → rearranged Spring

Select the bottom vertex of the cylinder's seam in the Piston and the corner
vertex in the Spring.

  * Connect the distance property of the **Distance** joint to the Spring's **Height** property using an [expression](/Expressions "Expressions"):

  1. Select the Spring in the [Tree view](/Tree_view "Tree view").
  2. Select the blue icon [![](/images/f/fc/Bound-expression.svg)](/index.php?title=File:Bound-expression.svg&filetimestamp=20250226211651&) in the Height property field.
  3. Enter in the expression editor: `<<Distance>>.Distance`

### Drive the shock absorber

To do so double-click the Distance object in the Tree view and change its
Distance property. Recompute the document. The spring changes its length.

  

![](/images/6/6f/Arrow-left.svg) ![](/images/0/06/Freecad.svg) [Std
Base](/Std_Base "Std Base")

![](/images/0/05/Workbench_BIM.svg) [BIM Workbench](/BIM_Workbench "BIM
Workbench") ![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

Expand[![](/images/c/cd/Workbench_Assembly.svg)](/index.php?title=File:Workbench_Assembly.svg&filetimestamp=20240325203121&)
Assembly

  * **Assembly:** [Create Assembly](/Assembly_CreateAssembly "Assembly CreateAssembly"), [Insert Component](/Assembly_InsertLink "Assembly InsertLink"), [Insert New Part](/Assembly_InsertNewPart "Assembly InsertNewPart"), [Solve Assembly](/Assembly_SolveAssembly "Assembly SolveAssembly"), [Create Exploded View](/Assembly_CreateView "Assembly CreateView"), [Create Simulation](/Assembly_CreateSimulation "Assembly CreateSimulation"), [Create Bill of Materials](/Assembly_CreateBom "Assembly CreateBom")

* * *

  * **Joints:** [Toggle Grounded](/Assembly_ToggleGrounded "Assembly ToggleGrounded"), [Create Fixed Joint](/Assembly_CreateJointFixed "Assembly CreateJointFixed"), [Create Revolute Joint](/Assembly_CreateJointRevolute "Assembly CreateJointRevolute"), [Create Cylindrical Joint](/Assembly_CreateJointCylindrical "Assembly CreateJointCylindrical"), [Create Slider Joint](/Assembly_CreateJointSlider "Assembly CreateJointSlider"), [Create Ball Joint](/Assembly_CreateJointBall "Assembly CreateJointBall"), [Create Distance Joint](/Assembly_CreateJointDistance "Assembly CreateJointDistance"), [Create Parallel Joint](/Assembly_CreateJointParallel "Assembly CreateJointParallel"), [Create Perpendicular Joint](/Assembly_CreateJointPerpendicular "Assembly CreateJointPerpendicular"), [Create Angle Joint](/Assembly_CreateJointAngle "Assembly CreateJointAngle"), [Create Rack and Pinion Joint](/Assembly_CreateJointRackPinion "Assembly CreateJointRackPinion"), [Create Screw Joint](/Assembly_CreateJointScrew "Assembly CreateJointScrew"), [Create Gears Joint](/Assembly_CreateJointGears "Assembly CreateJointGears"), [Create Belt Joint](/Assembly_CreateJointBelt "Assembly CreateJointBelt")

* * *

  * **Preferences:** [Preferences](/Assembly_Preferences "Assembly Preferences")

Expand[![](/images/thumb/9/94/User_hub.png/24px-
User_hub.png)](/index.php?title=File:User_hub.png&filetimestamp=20190221145008&)
[User documentation](/User_hub "User hub")

  * **[Getting started](/Getting_started "Getting started")**
  * **Installation:** [Download](/Download "Download"), [Windows](/Installing_on_Windows "Installing on Windows"), [Linux](/Installing_on_Linux "Installing on Linux"), [Mac](/Installing_on_Mac "Installing on Mac"), [Additional components](/Installing_additional_components "Installing additional components"), [Docker](/Compile_on_Docker "Compile on Docker"), [AppImage](/AppImage "AppImage"), [Ubuntu Snap](/Ubuntu_Snap "Ubuntu Snap")
  * **Basics:** [About FreeCAD](/About_FreeCAD "About FreeCAD"), [Interface](/Interface "Interface"), [Mouse navigation](/Mouse_navigation "Mouse navigation"), [Selection methods](/Selection_methods "Selection methods"), [Object name](/Object_name "Object name"), [Preferences](/Preferences_Editor "Preferences Editor"), [Workbenches](/Workbenches "Workbenches"), [Document structure](/Document_structure "Document structure"), [Properties](/Property "Property"), [Help FreeCAD](/Help_FreeCAD "Help FreeCAD"), [Donate](/Donate "Donate")

* * *

  * **Help:** [Tutorials](/Tutorials "Tutorials"), [Video tutorials](/Video_tutorials "Video tutorials")
  * **[Workbenches](/Workbenches "Workbenches"):** [Std Base](/Std_Base "Std Base"), Assembly, [BIM](/BIM_Workbench "BIM Workbench"), [CAM](/CAM_Workbench "CAM Workbench"), [Draft](/Draft_Workbench "Draft Workbench"), [FEM](/FEM_Workbench "FEM Workbench"), [Inspection](/Inspection_Workbench "Inspection Workbench"), [Material](/Material_Workbench "Material Workbench"), [Mesh](/Mesh_Workbench "Mesh Workbench"), [OpenSCAD](/OpenSCAD_Workbench "OpenSCAD Workbench"), [Part](/Part_Workbench "Part Workbench"), [PartDesign](/PartDesign_Workbench "PartDesign Workbench"), [Points](/Points_Workbench "Points Workbench"), [Reverse Engineering](/Reverse_Engineering_Workbench "Reverse Engineering Workbench"), [Robot](/Robot_Workbench "Robot Workbench"), [Sketcher](/Sketcher_Workbench "Sketcher Workbench"), [Spreadsheet](/Spreadsheet_Workbench "Spreadsheet Workbench"), [Surface](/Surface_Workbench "Surface Workbench"), [TechDraw](/TechDraw_Workbench "TechDraw Workbench"), [Test Framework](/Testing "Testing")

* * *

  * **[Addons](/Addon "Addon"):** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

