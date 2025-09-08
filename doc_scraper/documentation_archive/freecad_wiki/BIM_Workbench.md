---
url: https://wiki.freecad.org/BIM_Workbench
title: BIM Workbench
scraped_at: 2025-09-08 16:43:57
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Getting started
  * 3 Tools Toggle Tools subsection
    * 3.1 2D drafting
    * 3.2 3D/BIM
    * 3.3 Annotation
    * 3.4 Snapping
    * 3.5 Modify
    * 3.6 Manage
    * 3.7 Utils
    * 3.8 Status bar
    * 3.9 Tree view context menu
    * 3.10 3D view context menu
    * 3.11 Obsolete tools
  * 4 Preferences
  * 5 Working with IFC
  * 6 File formats
  * 7 API
  * 8 Tutorials and learning
  * 9 Example files

# BIM Workbench

  * [Page](/BIM_Workbench "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:BIM_Workbench&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/BIM_Workbench)
  * [Edit](/index.php?title=BIM_Workbench&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=BIM_Workbench&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/BIM_Workbench.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=BIM_Workbench&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/BIM_Workbench)
  * [Edit](/index.php?title=BIM_Workbench&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=BIM_Workbench&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=BIM_Workbench&action=history)

General

  * [What links here](/Special:WhatLinksHere/BIM_Workbench "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/BIM_Workbench "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=BIM_Workbench&oldid=1639001 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=BIM_Workbench&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=BIM_Workbench&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
BIM+Workbench&action=page&filter=&language=en)This is the approved revision of
this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-BIM+Workbench&language=&task=view "Start translation for this language")
  * [Deutsch](/BIM_Workbench/de "Arbeitsbereich BIM \(89% translated\)")
  * English
  * [español](/BIM_Workbench/es "Ambiente de trabajo BIM \(5% translated\)")
  * [français](/BIM_Workbench/fr "Atelier BIM \(99% translated\)")
  * [hrvatski](/BIM_Workbench/hr "BIM radni stol \(1% translated\)")
  * [italiano](/BIM_Workbench/it "Ambiente BIM \(69% translated\)")
  * [polski](/BIM_Workbench/pl "Środowisko pracy BIM \(100% translated\)")
  * [português do Brasil](/BIM_Workbench/pt-br "Bancada de trabalho BIM \(18% translated\)")
  * [русский](/BIM_Workbench/ru "Верстак BIM \(5% translated\)")
  * [日本語](/BIM_Workbench/ja "BIMワークベンチ \(2% translated\)")
  * [한국어](/BIM_Workbench/ko "BIM 작업대 \(1% translated\)")

![](/images/6/6f/Arrow-left.svg) ![](/images/c/cd/Workbench_Assembly.svg)
[Assembly Workbench](/Assembly_Workbench "Assembly Workbench")

![](/images/9/95/Workbench_CAM.svg) [CAM Workbench](/CAM_Workbench "CAM
Workbench") ![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

In v1.0 the BIM, Native-IFC and [Arch](/Arch_Workbench "Arch Workbench")
Workbenches have been merged into the integrated BIM Workbench.  
This page has been updated for that version.

[![](/images/0/05/Workbench_BIM.svg)](/index.php?title=File:Workbench_BIM.svg&filetimestamp=20240524155736&)BIM
Workbench icon

## Introduction

The
[![](/images/0/05/Workbench_BIM.svg)](/index.php?title=File:Workbench_BIM.svg&filetimestamp=20240524155736&)
BIM Workbench provides a modern [Building Information
Modelling](https://en.wikipedia.org/wiki/Building_information_modeling)
workflow in FreeCAD, with fully parametric objects such as walls, beams,
roofs, windows, stairs, pipes, and furniture. It supports [Industry Foundation
Classes](/Arch_IFC "Arch IFC") (IFC) files, and the production of 2D plans in
combination with the
[![](/images/b/b6/Workbench_TechDraw.svg)](/index.php?title=File:Workbench_TechDraw.svg&filetimestamp=20240713144548&)
[TechDraw Workbench](/TechDraw_Workbench "TechDraw Workbench").

The BIM Workbench imports tools from the
[![](/images/9/91/Workbench_Draft.svg)](/index.php?title=File:Workbench_Draft.svg&filetimestamp=20200404172706&)
[Draft Workbench](/Draft_Workbench "Draft Workbench"), as it uses its 2D
objects to build 3D parametric objects. But it can also use solid shapes
created with other workbenches like
[![](/images/0/04/Workbench_Part.svg)](/index.php?title=File:Workbench_Part.svg&filetimestamp=20240712190040&)
[Part](/Part_Workbench "Part Workbench") and
[![](/images/3/39/Workbench_PartDesign.svg)](/index.php?title=File:Workbench_PartDesign.svg&filetimestamp=20240405092932&)
[PartDesign](/PartDesign_Workbench "PartDesign Workbench").

See [FreeCAD BIM migration
guide](https://yorik.uncreated.net/?blog/2020-010-freecad-bim-guide) for a
quick overview if you are already a user of another BIM application.

The developers of Draft and BIM also collaborate with the greater [OSArch
community](https://osarch.org), with the ultimate goal of improving building
design by using entirely free software.

[![](/images/thumb/5/5e/BIM_workbench_presentation.png/800px-
BIM_workbench_presentation.png)](/index.php?title=File:BIM_workbench_presentation.png&filetimestamp=20180823195331&)

## Getting started

[![](/images/thumb/2/23/BIM_welcome_screen.png/800px-
BIM_welcome_screen.png)](/index.php?title=File:BIM_welcome_screen.png&filetimestamp=20181119180753&)

When starting the BIM workbench for the first time, a welcome dialog is shown,
giving a quick overview of how the workbench works, and allowing the user to
start an [in-game tutorial](/BIM_ingame_tutorial "BIM ingame tutorial"). The
welcome dialog is also available from the **help** menu. When the welcome
screen is closed by clicking OK, the [BIM setup dialog](/BIM_Setup "BIM
Setup") will be shown, that allows the user to quickly set some of the most
common BIM-related preferences of FreeCAD without the need to browse through
the full [FreeCAD preferences pages](/Preferences_Editor "Preferences
Editor").

The [BIM project setup](/BIM_Setup "BIM Setup") tool allows you to quickly
setup a BIM project by entering some basic information about your project. You
can then, for example, use the different 2D drafting tools to sketch
guidelines and baselines, then use the different 3D modeling tools to
automatically build 3D BIM objects from them. A line, for example, can become
a wall simply by selecting it and pressing the [Wall](/Arch_Wall "Arch Wall")
button.

Common building elements such as [walls](/Arch_Wall "Arch Wall") or
[columns](/BIM_Column "BIM Column") are easily created by pressing the
appropriate toolbar button and clicking points in the 3D view. They can be
moved, rotated and edited once created. Most BIM elements are created on the
current [working plane](/Draft_SelectPlane "Draft SelectPlane"), so a typical
workflow involves placing the working plane first, then creating a BIM
element. More complex elements can be created by drawing 2D elements first,
then using one of the BIM tools to convert them into the desired element.

Elements of building projects can be organized using [sites](/Arch_Site "Arch
Site"), [buildings](/Arch_Building "Arch Building") and
[levels](/Arch_BuildingPart "Arch BuildingPart"), to reproduce what is
commonly done in other BIM applications. In FreeCAD, however, such structures
are not mandatory, and you are free to organize your model elements as you see
fit, for example using [groups](/Std_Group "Std Group").

2D drawings can be generated from a model to represent plan, section or
elevation views. To generate such a drawing,[section
planes](/Arch_SectionPlane "Arch SectionPlane") are placed in the model, to
indicate where it should be cut or viewed from. Once the section planes are in
place, two methods are possible:

  1. Create projected views in the document using [shape views](/Draft_Shape2DView "Draft Shape2DView"), then add all the necessary annotations such as texts and dimensions, then put all this on a page. This is the recommended way, as it offers more flexibility.
  2. Create a view on a page directly from the section plane. Then all the needed 2D annotations must either be added to the section plane, or done directly on the page. This is less flexible.

Finally, quantities schedules can be created using the
[schedule](/Arch_Schedule "Arch Schedule") tool.

If you are used to another BIM application, check our [BIM application
compatibility table](/BIM_application_compatibility_table "BIM application
compatibility table") to get your bearings when starting with FreeCAD.

[![](/images/thumb/7/7f/BIM_tutorial_screenshot.png/800px-
BIM_tutorial_screenshot.png)](/index.php?title=File:BIM_tutorial_screenshot.png&filetimestamp=20181120153101&)

The [in-game tutorial](/BIM_ingame_tutorial "BIM ingame tutorial") is an easy
way to quickly get on track with the BIM workbench.

## Tools

The BIM workbench gathers tools from several other FreeCAD workbenches, mainly
[Draft](/Draft_Workbench "Draft Workbench") and [Part](/Part_Workbench "Part
Workbench"), roughly reorganized in logical categories.

Additionally, if such [addons](/External_workbenches "External workbenches")
are installed, tools from [Reinforcement](/Reinforcement_Workbench
"Reinforcement Workbench") (extra reinforcing bar tools),
[Fasteners](/Fasteners_Workbench "Fasteners Workbench") (bolts and screws),
[Flamingo/Dodo](/Flamingo_Workbench "Flamingo Workbench") (metal structure and
piping tools) and [Parts Library](/Parts_Library_Workbench "Parts Library
Workbench") are automatically included in the BIM workbench.

The BIM workbench also adds a series of items in the **status bar** of
FreeCAD, and a couple of **context menu items** , accessible by right-clicking
in the 3D view or in the tree view.

### 2D drafting

2D objects are commonly used as drafting aids, or to draw base lines and
profiles to build BIM objects on. They can also be used to draw symbols and
annotations in your model. Apart from sketches, that use their own coordinate
system, 2D objects will be drawn on the current [working
plane](/Draft_SelectPlane "Draft SelectPlane").

  * [![](/images/8/8a/BIM_Sketch.svg)](/index.php?title=File:BIM_Sketch.svg&filetimestamp=20240608153905&) [Sketch](/BIM_Sketch "BIM Sketch"): Creates‎ a new sketch and enters sketch edit mode. Sketches are advanced 2D objects with constraints support.

  * [![](/images/2/23/Draft_Line.svg)](/index.php?title=File:Draft_Line.svg&filetimestamp=20210319101803&) [Line](/Draft_Line "Draft Line"): Creates a straight line.

  * [![](/images/1/10/Draft_Wire.svg)](/index.php?title=File:Draft_Wire.svg&filetimestamp=20210319103011&) [Polyline](/Draft_Wire "Draft Wire"): Creates a polyline (also called wire), a sequence of several connected line segments.

  * [![](/images/b/b1/Draft_Circle.svg)](/index.php?title=File:Draft_Circle.svg&filetimestamp=20210319101000&) [Circle](/Draft_Circle "Draft Circle"): Creates a circle from a center and a radius.

  * [![](/images/e/ee/Draft_Arc.svg)](/index.php?title=File:Draft_Arc.svg&filetimestamp=20210319100639&) [Arc](/Draft_Arc "Draft Arc"): Creates a circular arc from a center, a radius, a start angle and an aperture angle.

  * [![](/images/4/49/Draft_Arc_3Points.svg)](/index.php?title=File:Draft_Arc_3Points.svg&filetimestamp=20210319100656&) [Arc by 3 points](/Draft_Arc_3Points "Draft Arc 3Points"): Creates a circular arc from three points that define its circumference.

  * [![](/images/6/67/Draft_Fillet.svg)](/index.php?title=File:Draft_Fillet.svg&filetimestamp=20210319101610&) [Fillet](/Draft_Fillet "Draft Fillet"): Creates a fillet, a rounded corner, or a chamfer, a straight edge, between two [Draft Lines](/Draft_Line "Draft Line").

  * [![](/images/1/10/Draft_Ellipse.svg)](/index.php?title=File:Draft_Ellipse.svg&filetimestamp=20240513220403&) [Ellipse](/Draft_Ellipse "Draft Ellipse"): Creates an ellipse from two points defining a rectangle in which the ellipse will fit.

  * [![](/images/9/91/Draft_Polygon.svg)](/index.php?title=File:Draft_Polygon.svg&filetimestamp=20210319102534&) [Polygon](/Draft_Polygon "Draft Polygon"): Creates a regular polygon from a center and a radius.

  * [![](/images/d/da/Draft_Rectangle.svg)](/index.php?title=File:Draft_Rectangle.svg&filetimestamp=20210319102545&) [Rectangle](/Draft_Rectangle "Draft Rectangle"): Creates a rectangle from two points.

  * [![](/images/b/b4/Draft_BSpline.svg)](/index.php?title=File:Draft_BSpline.svg&filetimestamp=20210319100925&) [B-spline](/Draft_BSpline "Draft BSpline"): Creates a B-spline curve from several points.

  * [![](/images/b/b9/Draft_BezCurve.svg)](/index.php?title=File:Draft_BezCurve.svg&filetimestamp=20210319100832&) [Bézier curve](/Draft_BezCurve "Draft BezCurve"): Creates a Bézier curve from several points.

  * [![](/images/5/59/Draft_CubicBezCurve.svg)](/index.php?title=File:Draft_CubicBezCurve.svg&filetimestamp=20240513220259&) [Cubic Bézier curve](/Draft_CubicBezCurve "Draft CubicBezCurve"): Creates a Bézier curve of the third degree.

  * [![](/images/1/1e/Draft_Point.svg)](/index.php?title=File:Draft_Point.svg&filetimestamp=20210319102426&) [Point](/Draft_Point "Draft Point"): Creates a simple point.

### 3D/BIM

3D and BIM objects are the real-world elements that will compose your BIM
project.

  * [![](/images/b/ba/BIM_Project.svg)](/index.php?title=File:BIM_Project.svg&filetimestamp=20240608171931&) [Project](/BIM_Project "BIM Project"): Creates an IFC project including selected objects.

  * [![](/images/8/8c/Arch_Site.svg)](/index.php?title=File:Arch_Site.svg&filetimestamp=20250123011723&) [Site](/Arch_Site "Arch Site"): Creates a site including selected objects.

  * [![](/images/6/60/Arch_Building.svg)](/index.php?title=File:Arch_Building.svg&filetimestamp=20250123011508&) [Building](/Arch_Building "Arch Building"): Creates a building including selected objects.

  * [![](/images/9/9b/Arch_Floor.svg)](/index.php?title=File:Arch_Floor.svg&filetimestamp=20250123011543&) [Level](/Arch_Floor "Arch Floor"): Creates a floor including selected objects.

  * [![](/images/b/b6/Arch_Space.svg)](/index.php?title=File:Arch_Space.svg&filetimestamp=20250123011726&) [Space](/Arch_Space "Arch Space"): Creates a space object.

  * [![](/images/9/97/Arch_Wall.svg)](/index.php?title=File:Arch_Wall.svg&filetimestamp=20250123011753&) [Wall](/Arch_Wall "Arch Wall"): Creates a wall from scratch or using a selected object as a base.

  * [![](/images/d/d2/Arch_CurtainWall.svg)](/index.php?title=File:Arch_CurtainWall.svg&filetimestamp=20250123011526&) [Curtain Wall](/Arch_CurtainWall "Arch CurtainWall"): Creates a curtain wall from scratch or using a selected object as a base.

  * [![](/images/7/70/BIM_Column.svg)](/index.php?title=File:BIM_Column.svg&filetimestamp=20240608121140&) [Column](/BIM_Column "BIM Column"): Creates a vertical [structural](/Arch_Structure "Arch Structure") element at a given point, optionally using a selected object as a profile.

  * [![](/images/8/8b/BIM_Beam.svg)](/index.php?title=File:BIM_Beam.svg&filetimestamp=20240608121047&) [Beam](/BIM_Beam "BIM Beam"): Creates a horizontal [structural](/Arch_Structure "Arch Structure") element between two points, optionally using a selected object as a profile.

  * [![](/images/d/d7/BIM_Slab.svg)](/index.php?title=File:BIM_Slab.svg&filetimestamp=20240608121911&) [Slab](/BIM_Slab "BIM Slab"): Creates a flat [structural](/Arch_Structure "Arch Structure") element by extruding a selected flat object.

  * [![](/images/6/60/BIM_Door.svg)](/index.php?title=File:BIM_Door.svg&filetimestamp=20240608121344&) [Door](/BIM_Door "BIM Door"): Creates a [Window](/Arch_Window "Arch Window") object using door presets.

  * [![](/images/c/cd/Arch_Window.svg)](/index.php?title=File:Arch_Window.svg&filetimestamp=20250123011811&) [Window](/Arch_Window "Arch Window"): Creates a window from scratch or using a selected object as a base.

  * [![](/images/e/eb/Arch_Pipe.svg)](/index.php?title=File:Arch_Pipe.svg&filetimestamp=20250123011617&) [Pipe](/Arch_Pipe "Arch Pipe"): Creates a pipe.

  * [![](/images/8/8c/Arch_PipeConnector.svg)](/index.php?title=File:Arch_PipeConnector.svg&filetimestamp=20250123011619&) [Connector](/Arch_PipeConnector "Arch PipeConnector"): Creates a corner or T-connection between 2 or 3 selected pipes.

  * [![](/images/a/a1/Arch_Stairs.svg)](/index.php?title=File:Arch_Stairs.svg&filetimestamp=20250123011732&) [Stairs](/Arch_Stairs "Arch Stairs"): Creates a stairs object.

  * [![](/images/d/df/Arch_Roof.svg)](/index.php?title=File:Arch_Roof.svg&filetimestamp=20250123011703&) [Roof](/Arch_Roof "Arch Roof"): Creates a sloped roof from a selected wire.

  * [![](/images/1/18/Arch_Panel.svg)](/index.php?title=File:Arch_Panel.svg&filetimestamp=20250123011608&) [Panel](/Arch_Panel "Arch Panel"): Creates a panel object from a selected 2D object.

  * [![](/images/4/4f/Arch_Frame.svg)](/index.php?title=File:Arch_Frame.svg&filetimestamp=20250123011546&) [Frame](/Arch_Frame "Arch Frame"): Creates a frame object from a selected layout.

  * [![](/images/f/ff/Arch_Fence.svg)](/index.php?title=File:Arch_Fence.svg&filetimestamp=20250123011538&) [Fence](/Arch_Fence "Arch Fence"): Creates a fence object from a selected post and path.

  * [![](/images/c/ca/Arch_Truss.svg)](/index.php?title=File:Arch_Truss.svg&filetimestamp=20250123011749&) [Truss](/Arch_Truss "Arch Truss"): Creates a truss from a selected line or from scratch.

  * [![](/images/d/d0/Arch_Equipment.svg)](/index.php?title=File:Arch_Equipment.svg&filetimestamp=20250123011536&) [Equipment](/Arch_Equipment "Arch Equipment"): Creates an equipment or furniture object.

  * Reinforcement tools:

    These tools, except the first, are only available if the [Reinforcement Workbench](/Reinforcement_Workbench "Reinforcement Workbench") has been installed.

    

  * [![](/images/4/49/Arch_Rebar.svg)](/index.php?title=File:Arch_Rebar.svg&filetimestamp=20250123011624&) [Custom Rebar](/Arch_Rebar "Arch Rebar"): Creates a custom reinforcement bar in a selected structural element using a sketch.

    

  * [![](/images/a/a9/Reinforcement_StraightRebar.svg)](/index.php?title=File:Reinforcement_StraightRebar.svg&filetimestamp=20240309122526&) [Straight Rebar](/Reinforcement_StraightRebar "Reinforcement StraightRebar"): Creates a straight reinforcement bar in a selected structural element.

    

  * [![](/images/c/c2/Reinforcement_UShapeRebar.svg)](/index.php?title=File:Reinforcement_UShapeRebar.svg&filetimestamp=20240309122537&) [U-Shape Rebar](/Reinforcement_UShapeRebar "Reinforcement UShapeRebar"): Creates a U-shape reinforcement bar in a selected structural element.

    

  * [![](/images/0/04/Reinforcement_LShapeRebar.svg)](/index.php?title=File:Reinforcement_LShapeRebar.svg&filetimestamp=20240309122446&) [L-Shape Rebar](/Reinforcement_LShapeRebar "Reinforcement LShapeRebar"): Creates an L-shape reinforcement bar in a selected structural element.

    

  * [![](/images/6/6a/Reinforcement_StirrupRebar.svg)](/index.php?title=File:Reinforcement_StirrupRebar.svg&filetimestamp=20240309122514&) [Stirrup](/Reinforcement_StirrupRebar "Reinforcement StirrupRebar"): Creates a stirrup reinforcement bar in a selected structural element.

    

  * [![](/images/6/69/Reinforcement_BentShapeRebar.svg)](/index.php?title=File:Reinforcement_BentShapeRebar.svg&filetimestamp=20240309122325&) [Bent-Shape Rebar](/Reinforcement_BentShapeRebar "Reinforcement BentShapeRebar"): Creates a bent-shape reinforcement bar in a selected structural element.

    

  * [![](/images/3/39/Reinforcement_HelicalRebar.svg)](/index.php?title=File:Reinforcement_HelicalRebar.svg&filetimestamp=20240309122434&) [Helical Rebar](/Reinforcement_HelicalRebar "Reinforcement HelicalRebar"): Creates a helical reinforcement bar in a selected structural element.

    

  * [![](/images/3/34/Reinforcement_ColumnRebars.svg)](/index.php?title=File:Reinforcement_ColumnRebars.svg&filetimestamp=20240309122350&) [Column Reinforcement](/Reinforcement_ColumnRebars "Reinforcement ColumnRebars"): Creates reinforcement bars in a selected column.

    

  * [![](/images/f/f0/Reinforcement_BeamRebars.svg)](/index.php?title=File:Reinforcement_BeamRebars.svg&filetimestamp=20240309122313&) [Beam Reinforcement](/Reinforcement_BeamRebars "Reinforcement BeamRebars"): Creates reinforcement bars in a selected beam.

    

  * [![](/images/6/60/Reinforcement_SlabRebars.svg)](/index.php?title=File:Reinforcement_SlabRebars.svg&filetimestamp=20240309122501&) [Slab Reinforcement](/Reinforcement_SlabRebars "Reinforcement SlabRebars"): Creates reinforcement bars in a selected slab.

    

  * [![](/images/7/7e/Reinforcement_FootingRebars.svg)](/index.php?title=File:Reinforcement_FootingRebars.svg&filetimestamp=20240309122420&) [Footing Reinforcement](/Reinforcement_FootingRebars "Reinforcement FootingRebars"): Creates reinforcement bars in a selected footing.

  * Generic 3D tools:

    These tools build generic 3D objects that can be turned or used into BIM components.

    

  * [![](/images/4/4c/Arch_Profile.svg)](/index.php?title=File:Arch_Profile.svg&filetimestamp=20250123011621&) [Profile](/Arch_Profile "Arch Profile"): Creates a parametric 2D profile.

    

  * [![](/images/5/5c/BIM_Box.svg)](/index.php?title=File:BIM_Box.svg&filetimestamp=20240608121057&) [Box](/BIM_Box "BIM Box"): Creates a box by specifying its dimensions graphically.

    

  * [![](/images/2/2a/Part_Builder.svg)](/index.php?title=File:Part_Builder.svg&filetimestamp=20240611075248&) [Shape builder...](/Part_Builder "Part Builder"): Creates more complex shapes from various geometric primitives.

    

  * [![](/images/5/5a/Draft_Facebinder.svg)](/index.php?title=File:Draft_Facebinder.svg&filetimestamp=20210319101547&) [Facebinder](/Draft_Facebinder "Draft Facebinder"): creates a surface object from selected faces.

    

  * [![](/images/0/05/BIM_Library.svg)](/index.php?title=File:BIM_Library.svg&filetimestamp=20240608121636&) [Objects library](/BIM_Library "BIM Library"): Inserts an equipment or furniture object. Requires the [Parts Library](/Parts_Library "Parts Library") addon.

    

  * [![](/images/1/19/Arch_Component.svg)](/index.php?title=File:Arch_Component.svg&filetimestamp=20250123011523&) [Component](/Arch_Component "Arch Component"): Creates a non-parametric Arch component.

    

  * [![](/images/3/3c/Arch_Reference.svg)](/index.php?title=File:Arch_Reference.svg&filetimestamp=20250123011657&) [External reference](/Arch_Reference "Arch Reference"): Links objects from another FreeCAD file into the current document.

### Annotation

Annotations are visual help objects that can be placed inside your model. They
can be used to export your model directly to a 2D format like [DXF](/Draft_DXF
"Draft DXF"), or reused when creating 2D views of your model with the
[TechDraw Workbench](/TechDraw_Workbench "TechDraw Workbench").

  * [![](/images/3/37/BIM_Text.svg)](/index.php?title=File:BIM_Text.svg&filetimestamp=20240608172604&) [Text](/BIM_Text "BIM Text"): Creates a 2D text in a document or on a TechDraw page.

  * [![](/images/5/55/Draft_ShapeString.svg)](/index.php?title=File:Draft_ShapeString.svg&filetimestamp=20210319102707&) [Shape from text](/Draft_ShapeString "Draft ShapeString"): Creates a compound shape that represents a text string.

  * [![](/images/5/54/BIM_DimensionAligned.svg)](/index.php?title=File:BIM_DimensionAligned.svg&filetimestamp=20240608121307&) [Aligned dimension](/BIM_DimensionAligned "BIM DimensionAligned"): Creates a dimension aligned with two points or a selected edge.

  * [![](/images/0/09/BIM_DimensionHorizontal.svg)](/index.php?title=File:BIM_DimensionHorizontal.svg&filetimestamp=20240608121319&) [Horizontal dimension](/BIM_DimensionHorizontal "BIM DimensionHorizontal"): Creates an horizontal dimension between two points or from a selected edge.

  * [![](/images/2/20/BIM_DimensionVertical.svg)](/index.php?title=File:BIM_DimensionVertical.svg&filetimestamp=20240608121331&) [Vertical dimension](/BIM_DimensionVertical "BIM DimensionVertical"): Creates a vertical dimension between two points or from a selected edge.

  * [![](/images/b/b7/BIM_Leader.svg)](/index.php?title=File:BIM_Leader.svg&filetimestamp=20240608121615&) [Leader](/BIM_Leader "BIM Leader"): Creates a 2-segment polyline with an arrow at its end, to be used as a leader line in conjunction with a [Text](/BIM_Text "BIM Text").

  * [![](/images/1/12/Draft_Label.svg)](/index.php?title=File:Draft_Label.svg&filetimestamp=20240513220515&) [Label](/Draft_Label "Draft Label"): Creates a multi-line text with a 2-segment leader line and an arrow.

  * [![](/images/6/62/Draft_Hatch.svg)](/index.php?title=File:Draft_Hatch.svg&filetimestamp=20210929161025&) [Hatch](/Draft_Hatch "Draft Hatch"): Creates hatches on the planar faces of a selected object.

  * [![](/images/7/7b/Arch_Axis.svg)](/index.php?title=File:Arch_Axis.svg&filetimestamp=20250123011457&) [Axis](/Arch_Axis "Arch Axis"): Adds a 1-direction array of axes.

  * [![](/images/3/33/Arch_AxisSystem.svg)](/index.php?title=File:Arch_AxisSystem.svg&filetimestamp=20250123011459&) [Axis System](/Arch_AxisSystem "Arch AxisSystem"): Adds an axis system composed of several axes.

  * [![](/images/a/af/Arch_Grid.svg)](/index.php?title=File:Arch_Grid.svg&filetimestamp=20250123011551&) [Grid](/Arch_Grid "Arch Grid"): Adds a grid-like object.

  * [![](/images/8/89/Arch_SectionPlane.svg)](/index.php?title=File:Arch_SectionPlane.svg&filetimestamp=20250123011710&) [Section Plane](/Arch_SectionPlane "Arch SectionPlane"): Adds a section plane object.

  * [![](/images/5/55/BIM_DrawingView.svg)](/index.php?title=File:BIM_DrawingView.svg&filetimestamp=20250717112924&)[![](/images/3/34/Toolbar_flyout_arrow_blue_background.svg)](/index.php?title=File:Toolbar_flyout_arrow_blue_background.svg&filetimestamp=20221006081506&) Create 2D views:

    

  * [![](/images/5/55/BIM_DrawingView.svg)](/index.php?title=File:BIM_DrawingView.svg&filetimestamp=20250717112924&) [2D Drawing](/BIM_DrawingView "BIM DrawingView"): Creates a container to hold 2D projections.

    

  * [![](/images/5/55/BIM_Shape2DView.svg)](/index.php?title=File:BIM_Shape2DView.svg&filetimestamp=20240608172459&) [Section view](/BIM_Shape2DView "BIM Shape2DView"): Creates a 2D projected view from a selected object such as a [Section plane](/Arch_SectionPlane "Arch SectionPlane") or a [Level](/Arch_BuildingPart "Arch BuildingPart").

    

  * [![](/images/f/f1/BIM_Shape2DCut.svg)](/index.php?title=File:BIM_Shape2DCut.svg&filetimestamp=20250717103842&) [Section cut](/BIM_Shape2DCut "BIM Shape2DCut"): Creates a 2D cut view from a selected object such as a [Section plane](/Arch_SectionPlane "Arch SectionPlane") or a [Level](/Arch_BuildingPart "Arch BuildingPart").

  * [![](/images/f/f6/BIM_TDPage.svg)](/index.php?title=File:BIM_TDPage.svg&filetimestamp=20240705091236&) [Page](/BIM_TDPage "BIM TDPage"): Creates a [TechDraw page](/TechDraw_PageTemplate "TechDraw PageTemplate") from a template SVG file.

  * [![](/images/4/42/BIM_TDView.svg)](/index.php?title=File:BIM_TDView.svg&filetimestamp=20250717143752&) [Insert view](/BIM_TDView "BIM TDView"): Creates a view of the selected object(s) such as a [Section plane](/Arch_SectionPlane "Arch SectionPlane") or a Group containing the different elements of a 2D view.

### Snapping

This menu contains the [Draft Snap](/Draft_Snap "Draft Snap") tools as well as
the following tools:

  * [![](/images/9/91/BIM_SetWPTop.svg)](/index.php?title=File:BIM_SetWPTop.svg&filetimestamp=20240612172153&) [Working Plane Top](/BIM_SetWPTop "BIM SetWPTop"): Places the working plane on the global XY plane (ground).

  * [![](/images/4/4b/BIM_SetWPFront.svg)](/index.php?title=File:BIM_SetWPFront.svg&filetimestamp=20240612172130&) [Working Plane Front](/BIM_SetWPFront "BIM SetWPFront"): Places the working plane on the global XZ plane (front).

  * [![](/images/6/62/BIM_SetWPSide.svg)](/index.php?title=File:BIM_SetWPSide.svg&filetimestamp=20240612172142&) [Working Plane Side](/BIM_SetWPSide "BIM SetWPSide"): Places the working plane on the global YZ plane (side).

### Modify

  * [![](/images/3/3c/Draft_Move.svg)](/index.php?title=File:Draft_Move.svg&filetimestamp=20210319101921&) [Move](/Draft_Move "Draft Move"): Moves or copies selected objects from one point to another.

  * [![](/images/2/27/BIM_Copy.svg)](/index.php?title=File:BIM_Copy.svg&filetimestamp=20240608121150&) [Copy](/BIM_Copy "BIM Copy"): Copies selected objects from one point to another.

  * [![](/images/f/f0/Draft_Rotate.svg)](/index.php?title=File:Draft_Rotate.svg&filetimestamp=20210319102554&) [Rotate](/Draft_Rotate "Draft Rotate"): Rotates or copies selected objects around a center point by a given angle.

  * [![](/images/5/56/BIM_Clone.svg)](/index.php?title=File:BIM_Clone.svg&filetimestamp=20240608121130&) [Clone](/BIM_Clone "BIM Clone"): Clones selected objects.

  * [![](/images/9/9e/BIM_SimpleCopy.svg)](/index.php?title=File:BIM_SimpleCopy.svg&filetimestamp=20240608200936&) [Create simple copy](/BIM_SimpleCopy "BIM SimpleCopy"): Creates a non-parametric copy of a selected object. This is the same tool as [Part SimpleCopy](/Part_SimpleCopy "Part SimpleCopy").

  * [![](/images/4/48/BIM_Compound.svg)](/index.php?title=File:BIM_Compound.svg&filetimestamp=20240608200834&) [Make compound](/BIM_Compound "BIM Compound"): Creates a compound from selected objects. This is the same tool as [Part Compound](/Part_Compound "Part Compound").

  * [![](/images/6/6c/Draft_Offset.svg)](/index.php?title=File:Draft_Offset.svg&filetimestamp=20210319102057&) [Offset](/Draft_Offset "Draft Offset"): Offsets each segment of a selected object over a given distance, or creates an offset copy of the selected object.

  * [![](/images/5/5c/BIM_Offset2D.svg)](/index.php?title=File:BIM_Offset2D.svg&filetimestamp=20240608200922&) [2D Offset...](/BIM_Offset2D "BIM Offset2D"): Constructs a parallel wire at a given distance from the original, or enlarges/shrinks a planar face (parametric version). This is the same tool as [Part Offset2D](/Part_Offset2D "Part Offset2D").

  * [![](/images/e/e9/Draft_Trimex.svg)](/index.php?title=File:Draft_Trimex.svg&filetimestamp=20210319102910&) [Trimex](/Draft_Trimex "Draft Trimex"): Trims or extends a selected object.

  * [![](/images/e/ef/Draft_Join.svg)](/index.php?title=File:Draft_Join.svg&filetimestamp=20210319101730&) [Join](/Draft_Join "Draft Join"): Joins [Draft Lines](/Draft_Line "Draft Line") and [Draft Wires](/Draft_Wire "Draft Wire") into a single wire.

  * [![](/images/a/a0/Draft_Split.svg)](/index.php?title=File:Draft_Split.svg&filetimestamp=20210319102812&) [Split](/Draft_Split "Draft Split"): Splits a [Draft Line](/Draft_Line "Draft Line") or [Draft Wire](/Draft_Wire "Draft Wire") at a specified point or edge.

  * [![](/images/1/1e/Draft_Scale.svg)](/index.php?title=File:Draft_Scale.svg&filetimestamp=20210319102628&) [Scale](/Draft_Scale "Draft Scale"): Scales or copies selected objects around a base point.

  * [![](/images/3/3e/Draft_Stretch.svg)](/index.php?title=File:Draft_Stretch.svg&filetimestamp=20210319102822&) [Stretch](/Draft_Stretch "Draft Stretch"): Stretches objects by moving selected points.

  * [![](/images/b/b2/Draft_Draft2Sketch.svg)](/index.php?title=File:Draft_Draft2Sketch.svg&filetimestamp=20210319101429&) [Draft to sketch](/Draft_Draft2Sketch "Draft Draft2Sketch"): Converts Draft objects to [Sketcher Sketches](/Sketcher_NewSketch "Sketcher NewSketch") and vice versa.

  * [![](/images/b/ba/Draft_Upgrade.svg)](/index.php?title=File:Draft_Upgrade.svg&filetimestamp=20210319102935&) [Upgrade](/Draft_Upgrade "Draft Upgrade"): Upgrades selected objects.

  * [![](/images/8/84/Draft_Downgrade.svg)](/index.php?title=File:Draft_Downgrade.svg&filetimestamp=20210319101401&) [Downgrade](/Draft_Downgrade "Draft Downgrade"): Downgrades selected objects.

  * [![](/images/b/b7/Arch_Add.svg)](/index.php?title=File:Arch_Add.svg&filetimestamp=20250123011455&) [Add component](/Arch_Add "Arch Add"): Adds objects to a component.

  * [![](/images/b/b9/Arch_Remove.svg)](/index.php?title=File:Arch_Remove.svg&filetimestamp=20250123011658&) [Remove component](/Arch_Remove "Arch Remove"): Subtracts or removes objects from a component.

  * [![](/images/3/34/Draft_OrthoArray.svg)](/index.php?title=File:Draft_OrthoArray.svg&filetimestamp=20200313192550&) [Array](/Draft_OrthoArray "Draft OrthoArray"): Creates an orthogonal array from a selected object. It can optionally create a [Link](/App_Link "App Link") array.

  * [![](/images/0/07/Draft_PathArray.svg)](/index.php?title=File:Draft_PathArray.svg&filetimestamp=20210319102244&) [Path array](/Draft_PathArray "Draft PathArray"): Creates an array from a selected object by placing copies along a path.

  * [![](/images/c/c1/Draft_PolarArray.svg)](/index.php?title=File:Draft_PolarArray.svg&filetimestamp=20210319102507&) [Polar array](/Draft_PolarArray "Draft PolarArray"): Creates an array from a selected object by placing copies along a circumference. It can optionally create a [Link](/App_Link "App Link") array.

  * [![](/images/d/d4/Draft_PointArray.svg)](/index.php?title=File:Draft_PointArray.svg&filetimestamp=20210319102438&) [Point array](/Draft_PointArray "Draft PointArray"): Creates an array from a selected object by placing copies at the points from a point compound.

  * [![](/images/0/09/Arch_CutPlane.svg)](/index.php?title=File:Arch_CutPlane.svg&filetimestamp=20250123011532&) [Cut with plane](/Arch_CutPlane "Arch CutPlane"): Cuts an object according to a plane.

  * [![](/images/4/4b/Draft_Mirror.svg)](/index.php?title=File:Draft_Mirror.svg&filetimestamp=20210319101909&) [Mirror](/Draft_Mirror "Draft Mirror"): Creates mirrored copies from selected objects.

  * [![](/images/1/11/BIM_Extrude.svg)](/index.php?title=File:BIM_Extrude.svg&filetimestamp=20240608200857&) [Extrude...](/BIM_Extrude "BIM Extrude"): Extrudes planar faces of an object. This is the same tool as [Part Extrude](/Part_Extrude "Part Extrude").

  * [![](/images/0/08/BIM_Cut.svg)](/index.php?title=File:BIM_Cut.svg&filetimestamp=20240608200847&) [Difference](/BIM_Cut "BIM Cut"): Subtracts one object from another. This is the same tool as [Part Cut](/Part_Cut "Part Cut").

  * [![](/images/1/19/BIM_Fuse.svg)](/index.php?title=File:BIM_Fuse.svg&filetimestamp=20240608200910&) [Union](/BIM_Fuse "BIM Fuse"): Fuses two objects. This is the same tool as [Part Fuse](/Part_Fuse "Part Fuse").

  * [![](/images/c/ce/BIM_Common.svg)](/index.php?title=File:BIM_Common.svg&filetimestamp=20240608200724&) [Intersection](/BIM_Common "BIM Common"): Extracts the common part of two objects. This is the same tool as [Part Common](/Part_Common "Part Common").

### Manage

  * [![](/images/8/8e/BIM_Setup.svg)](/index.php?title=File:BIM_Setup.svg&filetimestamp=20240611075223&) [BIM Setup...](/BIM_Setup "BIM Setup"): Configures some of the FreeCAD preferences most commonly used for BIM.

  * [![](/images/5/51/BIM_Views.svg)](/index.php?title=File:BIM_Views.svg&filetimestamp=20250904184914&) [Views manager](/BIM_Views "BIM Views"): Manage the different views and levels of your project.

  * [![](/images/d/d6/BIM_ProjectManager.svg)](/index.php?title=File:BIM_ProjectManager.svg&filetimestamp=20240608171910&) [Manage project...](/BIM_ProjectManager "BIM ProjectManager"): Allows to create some basic objects such as a [site](/Arch_Site "Arch Site"), a [building](/Arch_Building "Arch Building") and [axes](/Arch_Axis "Arch Axis") by filling basic project information.

  * [![](/images/2/2c/BIM_Windows.svg)](/index.php?title=File:BIM_Windows.svg&filetimestamp=20240608122142&) [Manage doors and windows...](/BIM_Windows "BIM Windows"): Manage the doors and windows of your project.

  * [![](/images/3/3b/BIM_IfcElements.svg)](/index.php?title=File:BIM_IfcElements.svg&filetimestamp=20240608121525&) [Manage IFC elements...](/BIM_IfcElements "BIM IfcElements"): Manage how the different elements of your project will be exported to IFC.

  * [![](/images/f/f5/BIM_IfcQuantities.svg)](/index.php?title=File:BIM_IfcQuantities.svg&filetimestamp=20240608121549&) [Manage IFC quantities...](/BIM_IfcQuantities "BIM IfcQuantities"): Manage how the quantities of your objects are explicitely exported to IFC

  * [![](/images/e/eb/BIM_IfcProperties.svg)](/index.php?title=File:BIM_IfcProperties.svg&filetimestamp=20240608121538&) [Manage IFC properties...](/BIM_IfcProperties "BIM IfcProperties"): Manage the IFC properties attached to each of your objects.

  * [![](/images/7/76/BIM_Classification.svg)](/index.php?title=File:BIM_Classification.svg&filetimestamp=20240608121117&) [Manage classification...](/BIM_Classification "BIM Classification"): Manage how objects and materials of your project relate to classifications systems such as [Uniclass](https://en.wikipedia.org/wiki/Uniclass).

  * [![](/images/8/85/BIM_Layers.svg)](/index.php?title=File:BIM_Layers.svg&filetimestamp=20240608121601&) [Manage layers...](/BIM_Layers "BIM Layers"): Manage the layers of your document.

  * [![](/images/1/19/BIM_Material.svg)](/index.php?title=File:BIM_Material.svg&filetimestamp=20240608121647&) [Material](/BIM_Material "BIM Material"): Manages [materials](/Arch_SetMaterial "Arch SetMaterial") or [multimaterials](/Arch_MultiMaterial "Arch MultiMaterial") of selected objects

  * [![](/images/9/90/Arch_Schedule.svg)](/index.php?title=File:Arch_Schedule.svg&filetimestamp=20250123011709&) [Schedule](/Arch_Schedule "Arch Schedule"): Creates different types of schedules.

  * [![](/images/7/7b/BIM_Preflight.svg)](/index.php?title=File:BIM_Preflight.svg&filetimestamp=20240608121802&) [Preflight checks...](/BIM_Preflight "BIM Preflight"): Perform different checks on your model before exporting to IFC.

  * [![](/images/6/63/Draft_AnnotationStyleEditor.svg)](/index.php?title=File:Draft_AnnotationStyleEditor.svg&filetimestamp=20200513071606&) [Annotation styles...](/Draft_AnnotationStyleEditor "Draft AnnotationStyleEditor"): Allows you to define styles that affect the visual properties of annotation-like objects.

### Utils

  * [![](/images/2/23/BIM_TogglePanels.svg)](/index.php?title=File:BIM_TogglePanels.svg&filetimestamp=20250904184913&) [Toggle bottom panels](/BIM_TogglePanels "BIM TogglePanels"): Shows or hides output windows (the Report view and the Python console).

  * [![](/images/3/3b/BIM_Trash.svg)](/index.php?title=File:BIM_Trash.svg&filetimestamp=20240704082322&) [Move to Trash](/BIM_Trash "BIM Trash"): Moves selected objects to a Trash group, which gets created if necessary

  * [![](/images/7/71/BIM_WPView.svg)](/index.php?title=File:BIM_WPView.svg&filetimestamp=20240608122153&) [Working Plane View](/BIM_WPView "BIM WPView"): Sets the camera to face the current working plane

  * [![](/images/5/5f/Draft_SelectGroup.svg)](/index.php?title=File:Draft_SelectGroup.svg&filetimestamp=20210319102641&) [Select group](/Draft_SelectGroup "Draft SelectGroup"): Selects the contents of [Std Groups](/Std_Group "Std Group") or group-like [Arch](/Arch_Workbench "Arch Workbench") objects.

  * [![](/images/4/48/Draft_Slope.svg)](/index.php?title=File:Draft_Slope.svg&filetimestamp=20210319102728&) [Set slope](/Draft_Slope "Draft Slope"): Slopes selected [Draft Lines](/Draft_Line "Draft Line") or [Draft Wires](/Draft_Wire "Draft Wire") by increasing, or decreasing, the Z coordinate of all points after the first one.

  * [![](/images/f/f1/Draft_WorkingPlaneProxy.svg)](/index.php?title=File:Draft_WorkingPlaneProxy.svg&filetimestamp=20210615195315&) [Create working plane proxy](/Draft_WorkingPlaneProxy "Draft WorkingPlaneProxy"): Creates a working plane proxy to save the current [Draft working plane](/Draft_SelectPlane "Draft SelectPlane").

  * [![](/images/e/e4/Draft_AddConstruction.svg)](/index.php?title=File:Draft_AddConstruction.svg&filetimestamp=20210319100501&) [Add to construction group](/Draft_AddConstruction "Draft AddConstruction"): Moves objects to the [Draft construction group](/Draft_ToggleConstructionMode "Draft ToggleConstructionMode").

  * [![](/images/e/eb/Arch_SplitMesh.svg)](/index.php?title=File:Arch_SplitMesh.svg&filetimestamp=20250123011731&) [Split Mesh](/Arch_SplitMesh "Arch SplitMesh"): Splits a selected mesh into separate components.

  * [![](/images/f/f0/Arch_MeshToShape.svg)](/index.php?title=File:Arch_MeshToShape.svg&filetimestamp=20250123011601&) [Mesh to Shape](/Arch_MeshToShape "Arch MeshToShape"): Converts a mesh into a shape, unifying coplanar faces.

  * [![](/images/f/fc/Arch_SelectNonSolidMeshes.svg)](/index.php?title=File:Arch_SelectNonSolidMeshes.svg&filetimestamp=20250123011719&) [Select non-manifold meshes](/Arch_SelectNonSolidMeshes "Arch SelectNonSolidMeshes"): Selects all non-manifold meshes from the current selection or from the document.

  * [![](/images/8/82/Arch_RemoveShape.svg)](/index.php?title=File:Arch_RemoveShape.svg&filetimestamp=20250123011700&) [Remove Shape from Arch](/Arch_RemoveShape "Arch RemoveShape"): Turns cubic shape-based Arch object fully parametric.

  * [![](/images/5/51/Arch_CloseHoles.svg)](/index.php?title=File:Arch_CloseHoles.svg&filetimestamp=20250123011518&) [Close holes](/Arch_CloseHoles "Arch CloseHoles"): Closes holes in a selected shape-based object.

  * [![](/images/3/3a/Arch_MergeWalls.svg)](/index.php?title=File:Arch_MergeWalls.svg&filetimestamp=20250123011559&) [Merge Walls](/Arch_MergeWalls "Arch MergeWalls"): Merges walls.

  * [![](/images/c/c8/Arch_Check.svg)](/index.php?title=File:Arch_Check.svg&filetimestamp=20250123011515&) [Check](/Arch_Check "Arch Check"): Check if the selected objects are solids and don't contain defects.

  * [![](/images/f/f7/Arch_ToggleIfcBrepFlag.svg)](/index.php?title=File:Arch_ToggleIfcBrepFlag.svg&filetimestamp=20250123011748&) [Toggle IFC B-rep flag](/Arch_ToggleIfcBrepFlag "Arch ToggleIfcBrepFlag"): Forces a selected object to be exported as an [IfcFacetedBrep](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm).

  * [![](/images/1/1b/Arch_ToggleSubs.svg)](/index.php?title=File:Arch_ToggleSubs.svg&filetimestamp=20250123011748&) [Toggle subcomponents](/Arch_ToggleSubs "Arch ToggleSubs"): Shows or hides the subcomponents of an Arch object.

  * [![](/images/a/a9/Arch_Survey.svg)](/index.php?title=File:Arch_Survey.svg&filetimestamp=20250123011744&) [Survey](/Arch_Survey "Arch Survey"): Enters or leaves surveying mode.

  * [![](/images/3/36/BIM_Diff.svg)](/index.php?title=File:BIM_Diff.svg&filetimestamp=20240608121249&) [IFC Diff](/BIM_Diff "BIM Diff"): Shows a visual diff between two IFC files

  * [![](/images/7/7a/BIM_IfcExplorer.svg)](/index.php?title=File:BIM_IfcExplorer.svg&filetimestamp=20240608205422&) [IFC explorer](/BIM_IfcExplorer "BIM IfcExplorer"): Opens a tool to explore the structure of an IFC file prior to importing

  * [![](/images/7/76/Arch_IfcSpreadsheet.svg)](/index.php?title=File:Arch_IfcSpreadsheet.svg&filetimestamp=20250123011555&) [Create IFC spreadsheet...](/Arch_IfcSpreadsheet "Arch IfcSpreadsheet"): This tool creates a spreadsheet to store IFC properties of an object.

  * [![](/images/5/50/BIM_ImagePlane.svg)](/index.php?title=File:BIM_ImagePlane.svg&filetimestamp=20240608205438&) [Image plane](/index.php?title=BIM_ImagePlane&action=edit&redlink=1 "BIM ImagePlane \(page does not exist\)"): Inserts an image plane in the document.

  * [![](/images/6/6f/BIM_Unclone.svg)](/index.php?title=File:BIM_Unclone.svg&filetimestamp=20240608122110&) [Unclone](/index.php?title=BIM_Unclone&action=edit&redlink=1 "BIM Unclone \(page does not exist\)"): Makes a cloned object independent from its original object

  * [![](/images/4/4b/BIM_Rewire.svg)](/index.php?title=File:BIM_Rewire.svg&filetimestamp=20240608121900&) [Rewire](/index.php?title=BIM_Rewire&action=edit&redlink=1 "BIM Rewire \(page does not exist\)"):

  * [![](/images/9/92/BIM_Glue.svg)](/index.php?title=File:BIM_Glue.svg&filetimestamp=20240704082115&) [Glue](/index.php?title=BIM_Glue&action=edit&redlink=1 "BIM Glue \(page does not exist\)"):

  * [![](/images/5/53/BIM_Reextrude.svg)](/index.php?title=File:BIM_Reextrude.svg&filetimestamp=20240608121828&) [Reextrude](/index.php?title=BIM_Reextrude&action=edit&redlink=1 "BIM Reextrude \(page does not exist\)"): Recreates an extrusion from a shape that has lost its parametric extrusion by selecting a base face

  * Panel tools:

    

  * [![](/images/1/18/Arch_Panel.svg)](/index.php?title=File:Arch_Panel.svg&filetimestamp=20250123011608&) [Panel](/Arch_Panel "Arch Panel"): Creates a panel object from a selected 2D object.

    

  * [![](/images/e/ef/Arch_Panel_Cut.svg)](/index.php?title=File:Arch_Panel_Cut.svg&filetimestamp=20250123011611&) [Panel Cut](/Arch_Panel_Cut "Arch Panel Cut"): Creates a 2D cut view from a panel.

    

  * [![](/images/3/32/Arch_Panel_Sheet.svg)](/index.php?title=File:Arch_Panel_Sheet.svg&filetimestamp=20250123011613&) [Panel Sheet](/Arch_Panel_Sheet "Arch Panel Sheet"): Creates a 2D cut sheet including panel cuts or other 2D objects.

    

  * [![](/images/5/56/Arch_Nest.svg)](/index.php?title=File:Arch_Nest.svg&filetimestamp=20250123011605&) [Nest](/Arch_Nest "Arch Nest"): Allows to nest several flat objects inside a container shape.

  * Structure tools:

    

  * [![](/images/b/bc/Arch_Structure.svg)](/index.php?title=File:Arch_Structure.svg&filetimestamp=20250123011738&) [Structure](/Arch_Structure "Arch Structure"): Creates a structural element from scratch or using a selected object as a base.

    

  * [![](/images/4/44/Arch_StructuralSystem.svg)](/index.php?title=File:Arch_StructuralSystem.svg&filetimestamp=20250123011736&) [Structural System](/index.php?title=Arch_StructuralSystem&action=edit&redlink=1 "Arch StructuralSystem \(page does not exist\)"):

    

  * [![](/images/8/82/Arch_StructuresFromSelection.svg)](/index.php?title=File:Arch_StructuresFromSelection.svg&filetimestamp=20250123011742&) [Multiple Structures](/index.php?title=Arch_StructuresFromSelection&action=edit&redlink=1 "Arch StructuresFromSelection \(page does not exist\)"):

  * [![](/images/4/4f/IFC_Diff.svg)](/index.php?title=File:IFC_Diff.svg&filetimestamp=20240608211623&) [IFC Diff...](/index.php?title=IFC_Diff&action=edit&redlink=1 "IFC Diff \(page does not exist\)"):

  * [![](/images/d/d2/IFC_Expand.svg)](/index.php?title=File:IFC_Expand.svg&filetimestamp=20240608211637&) [IFC Expand](/index.php?title=IFC_Expand&action=edit&redlink=1 "IFC Expand \(page does not exist\)"):

  * [![](/images/a/a8/IFC_MakeProject.svg)](/index.php?title=File:IFC_MakeProject.svg&filetimestamp=20240608211647&) [Make IFC project](/index.php?title=IFC_MakeProject&action=edit&redlink=1 "IFC MakeProject \(page does not exist\)"):

  * [![](/images/3/3a/IFC_UpdateIOS.svg)](/index.php?title=File:IFC_UpdateIOS.svg&filetimestamp=20240608211703&) [IfcOpenShell update](/index.php?title=IFC_UpdateIOS&action=edit&redlink=1 "IFC UpdateIOS \(page does not exist\)"):

  * Nudge:

    

  * [Nudge Switch](/index.php?title=BIM_Nudge_Switch&action=edit&redlink=1 "BIM Nudge Switch \(page does not exist\)"):

    

  * [Nudge Up](/index.php?title=BIM_Nudge_Up&action=edit&redlink=1 "BIM Nudge Up \(page does not exist\)"):

    

  * [Nudge Down](/index.php?title=BIM_Nudge_Down&action=edit&redlink=1 "BIM Nudge Down \(page does not exist\)"):

    

  * [Nudge Left](/index.php?title=BIM_Nudge_Left&action=edit&redlink=1 "BIM Nudge Left \(page does not exist\)"):

    

  * [Nudge Right](/index.php?title=BIM_Nudge_Right&action=edit&redlink=1 "BIM Nudge Right \(page does not exist\)"):

    

  * [Nudge Rotate Left](/index.php?title=BIM_Nudge_RotateLeft&action=edit&redlink=1 "BIM Nudge RotateLeft \(page does not exist\)"):

    

  * [Nudge Rotate Right](/index.php?title=BIM_Nudge_RotateRight&action=edit&redlink=1 "BIM Nudge RotateRight \(page does not exist\)"):

    

  * [Nudge Extend](/index.php?title=BIM_Nudge_Extend&action=edit&redlink=1 "BIM Nudge Extend \(page does not exist\)"):

    

  * [Nudge Shrink](/index.php?title=BIM_Nudge_Shrink&action=edit&redlink=1 "BIM Nudge Shrink \(page does not exist\)"):

### Status bar

The status bar contains a few buttons that allow to easily change different
states:

  * [![](/images/2/23/BIM_TogglePanels.svg)](/index.php?title=File:BIM_TogglePanels.svg&filetimestamp=20250904184913&) [Toggle panels](/BIM_TogglePanels "BIM TogglePanels"): Shows or hides the [Report view](/Report_view "Report view") and the [Python console](/Python_console "Python console").

  * [![](/images/5/51/BIM_Views.svg)](/index.php?title=File:BIM_Views.svg&filetimestamp=20250904184914&) Toggle Views: Shows or hides the [BIM Views](/BIM_Views "BIM Views") panel.

  * [![](/images/2/2a/BIM_ToggleBackground.svg)](/index.php?title=File:BIM_ToggleBackground.svg&filetimestamp=20240704095212&) Cycle background: Cycles between vertical gradient, radial gradient and simple color background modes. This can be used to toggle between a dark background for modelling and a white background for 2D drawing.

  * [![](/images/2/2f/IFC.svg)](/index.php?title=File:IFC.svg&filetimestamp=20240608122339&) Lock IFC: Switches between [locked and unlocked IFC mode](/Native_IFC#Locked_and_unlocked_modes "Native IFC").

### Tree view context menu

TBD

### 3D view context menu

TBD

### Obsolete tools

  * [![](/images/1/1d/Arch_3Views.svg)](/index.php?title=File:Arch_3Views.svg&filetimestamp=20250123011452&) [Arch 3Views](/Arch_3Views "Arch 3Views"): Creates top, front and side views from a [mesh](/Mesh_Workbench "Mesh Workbench"). Not available in 1.0 and above.

  * [![](/images/e/ea/Arch_BuildingPart.svg)](/index.php?title=File:Arch_BuildingPart.svg&filetimestamp=20250123011510&) [Arch BuildingPart](/Arch_BuildingPart "Arch BuildingPart"): Creates a building part including selected objects. Not available in 1.0 and above. Use [Arch Floor](/Arch_Floor "Arch Floor") instead.

  * [![](/images/6/67/Arch_CloneComponent.svg)](/index.php?title=File:Arch_CloneComponent.svg&filetimestamp=20201202213038&) [Arch CloneComponent](/Arch_CloneComponent "Arch CloneComponent"): Produces Arch Components that are clones of selected Arch objects. Not available in 1.0 and above. Use [Draft Clone](/Draft_Clone "Draft Clone") instead.

  * [![](/images/3/3d/Arch_CutLine.svg)](/index.php?title=File:Arch_CutLine.svg&filetimestamp=20200215011420&) [Arch CutLine](/Arch_CutLine "Arch CutLine"): Cuts an object according to a line. Not available in 1.0 and above. Use [Arch CutPlane](/Arch_CutPlane "Arch CutPlane") instead.

  * [![](/images/e/e4/Arch_MultiMaterial.svg)](/index.php?title=File:Arch_MultiMaterial.svg&filetimestamp=20200210212214&) [Arch MultiMaterial](/Arch_MultiMaterial "Arch MultiMaterial"): Creates a multi-material and attributes it to selected objects, if any. Not available in 1.0 and above. Use [BIM Material](/BIM_Material "BIM Material") instead.

  * [![](/images/8/8b/Arch_Project.svg)](/index.php?title=File:Arch_Project.svg&filetimestamp=20250123011621&) [Arch Project](/Arch_Project "Arch Project"): Creates a project including selected objects. Not available in 1.0 and above. Use [BIM Project](/BIM_Project "BIM Project") instead.

  * [![](/images/2/21/Arch_SetMaterial.svg)](/index.php?title=File:Arch_SetMaterial.svg&filetimestamp=20200210212431&) [Arch SetMaterial](/Arch_SetMaterial "Arch SetMaterial"): Creates a material and attributes it to selected objects, if any. Not available in 1.0 and above. Use [BIM Material](/BIM_Material "BIM Material") instead.

## Preferences

  * [![](/images/f/f3/Preferences-bim.svg)](/index.php?title=File:Preferences-bim.svg&filetimestamp=20240608122714&) [Preferences](/BIM_Preferences "BIM Preferences"): General preferences for the BIM Workbench.
  * [Fine tuning](/Fine-tuning#BIM_Workbench "Fine-tuning"): Extra parameters to fine-tune BIM behavior.

## Working with IFC

The BIM workbench works natively with [Industry Foundation
Classes](https://en.wikipedia.org/wiki/Industry_Foundation_Classes) (IFC)
files. Native means there is no more translation between the IFC contents and
FreeCAD: The IFC contents are directly rendered in FreeCAD, and any change
affects the IFC contents directly. Read more on [Native IFC](/Native_IFC
"Native IFC").

If you don't plan to work with others, and have no need for IFC, you can still
use the BIM workbench tools and simply ignore anything related to IFC. You can
still export your model to IFC anytime.

The old [Arch IFC](/Arch_IFC "Arch IFC") importer is disabled by default in
FreeCAD, but still available from Python.

There is also a specific [Native IFC Tutorial](/Native_IFC_Tutorial "Native
IFC Tutorial") that explains the concepts further.

## File formats

  * [IFC](/Arch_IFC "Arch IFC"): industry foundation classes
  * [DAE](/Arch_DAE "Arch DAE"): Collada mesh format
  * [OBJ](/Arch_OBJ "Arch OBJ"): OBJ mesh format (export only)
  * [JSON](/Arch_JSON "Arch JSON"): JavaScript Object Notation format (export only)
  * [3DS](/Arch_3DS "Arch 3DS"): 3DS format (import only)
  * [SHP](/Arch_SHP "Arch SHP"): GIS Shapefiles (import only)

## API

The Arch module can be used in [Python](/Python "Python") scripts and
[macros](/Macros "Macros") using the [Arch Python API](/Arch_API "Arch API")
functions.

## Tutorials and learning

  * [Migrating to FreeCAD from Revit](/Migrating_to_FreeCAD_from_Revit "Migrating to FreeCAD from Revit")
  * [Arch & BIM tutorials on this wiki](/Tutorials#Architecture_and_BIM "Tutorials")
  * ["BIM with FreeCAD" video series by Yorik](https://www.youtube.com/playlist?list=PLmKdGVtV5Vnt2cj4IZIv9FM39QHaE1ZaU)
  * ["FreeCAD tutorials" video series by Regis](https://www.youtube.com/playlist?list=PLDd21g-eSHwkkxVOfVmR8ObpPN5QbL7ye)
  * ["Quinta Monroy" video series by Regis](https://www.youtube.com/playlist?list=PLDd21g-eSHwnAYyutuKhrPY51skaBhrVU)
  * ["HRCompacta" youtube channel](https://www.youtube.com/@HRCompacta) (most content is in portuguese)
  * ["FreeCADBIM" youtube channel](https://www.youtube.com/@FreeCadBIM) (most content is in portuguese)
  * ["FCB Lounge" youtube channel](https://www.youtube.com/@FCBlounge) dedicated to BIM and Draft content

## Example files

  * FreeCAD features a BIM example file on the Start page.
  * More example BIM files are available at <https://github.com/yorikvanhavre/FreeCAD-BIM-examples>. From within FreeCAD, use menu **Help → BIM Examples**.
  * OSArch Wiki (OpenSource Architecture) provides FreeCAD BIM examples created by multiple authors: <https://wiki.osarch.org/index.php?title=FreeCAD/Architecture_3D_models_created_in_FreeCAD>.

  

![](/images/6/6f/Arrow-left.svg) ![](/images/c/cd/Workbench_Assembly.svg)
[Assembly Workbench](/Assembly_Workbench "Assembly Workbench")

![](/images/9/95/Workbench_CAM.svg) [CAM Workbench](/CAM_Workbench "CAM
Workbench") ![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

Expand[![](/images/0/05/Workbench_BIM.svg)](/index.php?title=File:Workbench_BIM.svg&filetimestamp=20240524155736&)
BIM

  * **2D drafting:** [Sketch](/BIM_Sketch "BIM Sketch"), [Line](/Draft_Line "Draft Line"), [Polyline](/Draft_Wire "Draft Wire"), [Circle](/Draft_Circle "Draft Circle"), [Arc](/Draft_Arc "Draft Arc"), [Arc by 3 points](/Draft_Arc_3Points "Draft Arc 3Points"), [Fillet](/Draft_Fillet "Draft Fillet"), [Ellipse](/Draft_Ellipse "Draft Ellipse"), [Polygon](/Draft_Polygon "Draft Polygon"), [Rectangle](/Draft_Rectangle "Draft Rectangle"), [B-spline](/Draft_BSpline "Draft BSpline"), [Bézier curve](/Draft_BezCurve "Draft BezCurve"), [Cubic Bézier curve](/Draft_CubicBezCurve "Draft CubicBezCurve"), [Point](/Draft_Point "Draft Point")

* * *

  * **3D/BIM:** [Project](/BIM_Project "BIM Project"), [Site](/Arch_Site "Arch Site"), [Building](/Arch_Building "Arch Building"), [Level](/Arch_Floor "Arch Floor"), [Space](/Arch_Space "Arch Space"), [Wall](/Arch_Wall "Arch Wall"), [Curtain Wall](/Arch_CurtainWall "Arch CurtainWall"), [Column](/BIM_Column "BIM Column"), [Beam](/BIM_Beam "BIM Beam"), [Slab](/BIM_Slab "BIM Slab"), [Door](/BIM_Door "BIM Door"), [Window](/Arch_Window "Arch Window"), [Pipe](/Arch_Pipe "Arch Pipe"), [Pipe Connector](/Arch_PipeConnector "Arch PipeConnector"), [Stairs](/Arch_Stairs "Arch Stairs"), [Roof](/Arch_Roof "Arch Roof"), [Panel](/Arch_Panel "Arch Panel"), [Frame](/Arch_Frame "Arch Frame"), [Fence](/Arch_Fence "Arch Fence"), [Truss](/Arch_Truss "Arch Truss"), [Equipment](/Arch_Equipment "Arch Equipment")
    * **Reinforcement tools:** [Custom Rebar](/Arch_Rebar "Arch Rebar"), [Straight Rebar](/Reinforcement_StraightRebar "Reinforcement StraightRebar"), [U-Shape Rebar](/Reinforcement_UShapeRebar "Reinforcement UShapeRebar"), [L-Shape Rebar](/Reinforcement_LShapeRebar "Reinforcement LShapeRebar"), [Stirrup](/Reinforcement_StirrupRebar "Reinforcement StirrupRebar"), [Bent-Shape Rebar](/Reinforcement_BentShapeRebar "Reinforcement BentShapeRebar"), [Helical Rebar](/Reinforcement_HelicalRebar "Reinforcement HelicalRebar"), [Column Reinforcement](/Reinforcement_ColumnRebars "Reinforcement ColumnRebars"), [Beam Reinforcement](/Reinforcement_BeamRebars "Reinforcement BeamRebars"), [Slab Reinforcement](/Reinforcement_SlabRebars "Reinforcement SlabRebars"), [Footing Reinforcement](/Reinforcement_FootingRebars "Reinforcement FootingRebars")
    * **Generic 3D tools:** [Profile](/Arch_Profile "Arch Profile"), [Box](/BIM_Box "BIM Box"), [Shape builder...](/Part_Builder "Part Builder"), [Facebinder](/Draft_Facebinder "Draft Facebinder"), [Objects library](/BIM_Library "BIM Library"), [Component](/Arch_Component "Arch Component"), [External reference](/Arch_Reference "Arch Reference")

* * *

  * **Annotation:** [Text](/BIM_Text "BIM Text"), [Shape from text](/Draft_ShapeString "Draft ShapeString"), [Aligned dimension](/BIM_DimensionAligned "BIM DimensionAligned"), [Horizontal dimension](/BIM_DimensionHorizontal "BIM DimensionHorizontal"), [Vertical dimension](/BIM_DimensionVertical "BIM DimensionVertical"), [Leader](/BIM_Leader "BIM Leader"), [Label](/Draft_Label "Draft Label"), [Axis](/Arch_Axis "Arch Axis"), [Axes System](/Arch_AxisSystem "Arch AxisSystem"), [Grid](/Arch_Grid "Arch Grid"), [Section Plane](/Arch_SectionPlane "Arch SectionPlane"), [Hatch](/Draft_Hatch "Draft Hatch"), [Page](/BIM_TDPage "BIM TDPage"), [View](/BIM_TDView "BIM TDView"), [Shape-based view](/BIM_Shape2DView "BIM Shape2DView")

* * *

  * **[Snapping](/Draft_Snap "Draft Snap"):** [Snap lock](/Draft_Snap_Lock "Draft Snap Lock"), [Snap endpoint](/Draft_Snap_Endpoint "Draft Snap Endpoint"), [Snap midpoint](/Draft_Snap_Midpoint "Draft Snap Midpoint"), [Snap center](/Draft_Snap_Center "Draft Snap Center"), [Snap angle](/Draft_Snap_Angle "Draft Snap Angle"), [Snap intersection](/Draft_Snap_Intersection "Draft Snap Intersection"), [Snap perpendicular](/Draft_Snap_Perpendicular "Draft Snap Perpendicular"), [Snap extension](/Draft_Snap_Extension "Draft Snap Extension"), [Snap parallel](/Draft_Snap_Parallel "Draft Snap Parallel"), [Snap special](/Draft_Snap_Special "Draft Snap Special"), [Snap near](/Draft_Snap_Near "Draft Snap Near"), [Snap ortho](/Draft_Snap_Ortho "Draft Snap Ortho"), [Snap grid](/Draft_Snap_Grid "Draft Snap Grid"), [Snap working plane](/Draft_Snap_WorkingPlane "Draft Snap WorkingPlane"), [Snap dimensions](/Draft_Snap_Dimensions "Draft Snap Dimensions"), [Toggle grid](/Draft_ToggleGrid "Draft ToggleGrid"), [Working Plane Top](/BIM_SetWPTop "BIM SetWPTop"), [Working Plane Front](/BIM_SetWPFront "BIM SetWPFront"), [Working Plane Side](/BIM_SetWPSide "BIM SetWPSide")

* * *

  * **Modify:** [Move](/Draft_Move "Draft Move"), [Copy](/BIM_Copy "BIM Copy"), [Rotate](/Draft_Rotate "Draft Rotate"), [Clone](/BIM_Clone "BIM Clone"), [Create simple copy](/BIM_SimpleCopy "BIM SimpleCopy"), [Make compound](/BIM_Compound "BIM Compound"), [Offset](/Draft_Offset "Draft Offset"), [2D Offset...](/BIM_Offset2D "BIM Offset2D"), [Trimex](/Draft_Trimex "Draft Trimex"), [Join](/Draft_Join "Draft Join"), [Split](/Draft_Split "Draft Split"), [Scale](/Draft_Scale "Draft Scale"), [Stretch](/Draft_Stretch "Draft Stretch"), [Draft to sketch](/Draft_Draft2Sketch "Draft Draft2Sketch"), [Upgrade](/Draft_Upgrade "Draft Upgrade"), [Downgrade](/Draft_Downgrade "Draft Downgrade"), [Add component](/Arch_Add "Arch Add"), [Remove component](/Arch_Remove "Arch Remove"), [Array](/Draft_OrthoArray "Draft OrthoArray"), [Path array](/Draft_PathArray "Draft PathArray"), [Polar array](/Draft_PolarArray "Draft PolarArray"), [Point array](/Draft_PointArray "Draft PointArray"), [Cut with plane](/Arch_CutPlane "Arch CutPlane"), [Mirror](/Draft_Mirror "Draft Mirror"), [Extrude...](/BIM_Extrude "BIM Extrude"), [Difference](/BIM_Cut "BIM Cut"), [Union](/BIM_Fuse "BIM Fuse"), [Intersection](/BIM_Common "BIM Common")

* * *

  * **Manage:** [BIM Setup...](/BIM_Setup "BIM Setup"), [Views manager](/BIM_Views "BIM Views"), [Manage project...](/BIM_ProjectManager "BIM ProjectManager"), [Manage doors and windows...](/BIM_Windows "BIM Windows"), [Manage IFC elements...](/BIM_IfcElements "BIM IfcElements"), [Manage IFC quantities...](/BIM_IfcQuantities "BIM IfcQuantities"), [Manage IFC properties...](/BIM_IfcProperties "BIM IfcProperties"), [Manage classification...](/BIM_Classification "BIM Classification"), [Manage layers...](/BIM_Layers "BIM Layers"), [Material](/BIM_Material "BIM Material"), [Schedule](/Arch_Schedule "Arch Schedule"), [Preflight checks...](/BIM_Preflight "BIM Preflight"), [Annotation styles...](/Draft_AnnotationStyleEditor "Draft AnnotationStyleEditor")

* * *

  * **Utils:** [Toggle bottom panels](/BIM_TogglePanels "BIM TogglePanels"), [Move to Trash](/BIM_Trash "BIM Trash"), [Working Plane View](/BIM_WPView "BIM WPView"), [Select group](/Draft_SelectGroup "Draft SelectGroup"), [Set slope](/Draft_Slope "Draft Slope"), [Create working plane proxy](/Draft_WorkingPlaneProxy "Draft WorkingPlaneProxy"), [Add to construction group](/Draft_AddConstruction "Draft AddConstruction"), [Split Mesh](/Arch_SplitMesh "Arch SplitMesh"), [Mesh to Shape](/Arch_MeshToShape "Arch MeshToShape"), [Select non-manifold meshes](/Arch_SelectNonSolidMeshes "Arch SelectNonSolidMeshes"), [Remove Shape from Arch](/Arch_RemoveShape "Arch RemoveShape"), [Close Holes](/Arch_CloseHoles "Arch CloseHoles"), [Merge Walls](/Arch_MergeWalls "Arch MergeWalls"), [Check](/Arch_Check "Arch Check"), [Toggle IFC Brep flag](/Arch_ToggleIfcBrepFlag "Arch ToggleIfcBrepFlag"), [Toggle subcomponents](/Arch_ToggleSubs "Arch ToggleSubs"), [Survey](/Arch_Survey "Arch Survey"), [IFC Diff](/BIM_Diff "BIM Diff"), [IFC explorer](/BIM_IfcExplorer "BIM IfcExplorer"), [Create IFC spreadsheet...](/Arch_IfcSpreadsheet "Arch IfcSpreadsheet"), [Image plane](/index.php?title=BIM_ImagePlane&action=edit&redlink=1 "BIM ImagePlane \(page does not exist\)"), [Unclone](/index.php?title=BIM_Unclone&action=edit&redlink=1 "BIM Unclone \(page does not exist\)"), [Rewire](/index.php?title=BIM_Rewire&action=edit&redlink=1 "BIM Rewire \(page does not exist\)"), [Glue](/index.php?title=BIM_Glue&action=edit&redlink=1 "BIM Glue \(page does not exist\)"), [Reextrude](/index.php?title=BIM_Reextrude&action=edit&redlink=1 "BIM Reextrude \(page does not exist\)")
    * **Panel tools:** [Panel](/Arch_Panel "Arch Panel"), [Panel Cut](/Arch_Panel_Cut "Arch Panel Cut"), [Panel Sheet](/Arch_Panel_Sheet "Arch Panel Sheet"), [Nest](/Arch_Nest "Arch Nest")
    * **Structure tools:** [Structure](/Arch_Structure "Arch Structure"), [Structural System](/index.php?title=Arch_StructuralSystem&action=edit&redlink=1 "Arch StructuralSystem \(page does not exist\)"), [Multiple Structures](/index.php?title=Arch_StructuresFromSelection&action=edit&redlink=1 "Arch StructuresFromSelection \(page does not exist\)")
    * **IFC tools:** [IFC Diff...](/index.php?title=IFC_Diff&action=edit&redlink=1 "IFC Diff \(page does not exist\)"), [IFC Expand](/index.php?title=IFC_Expand&action=edit&redlink=1 "IFC Expand \(page does not exist\)"), [Make IFC project](/index.php?title=IFC_MakeProject&action=edit&redlink=1 "IFC MakeProject \(page does not exist\)"), [IfcOpenShell update](/index.php?title=IFC_UpdateIOS&action=edit&redlink=1 "IFC UpdateIOS \(page does not exist\)")
    * **Nudge:** [Nudge Switch](/index.php?title=BIM_Nudge_Switch&action=edit&redlink=1 "BIM Nudge Switch \(page does not exist\)"), [Nudge Up](/index.php?title=BIM_Nudge_Up&action=edit&redlink=1 "BIM Nudge Up \(page does not exist\)"), [Nudge Down](/index.php?title=BIM_Nudge_Down&action=edit&redlink=1 "BIM Nudge Down \(page does not exist\)"), [Nudge Left](/index.php?title=BIM_Nudge_Left&action=edit&redlink=1 "BIM Nudge Left \(page does not exist\)"), [Nudge Right](/index.php?title=BIM_Nudge_Right&action=edit&redlink=1 "BIM Nudge Right \(page does not exist\)"), [Nudge Rotate Left](/index.php?title=BIM_Nudge_RotateLeft&action=edit&redlink=1 "BIM Nudge RotateLeft \(page does not exist\)"), [Nudge Rotate Right](/index.php?title=BIM_Nudge_RotateRight&action=edit&redlink=1 "BIM Nudge RotateRight \(page does not exist\)"), [Nudge Extend](/index.php?title=BIM_Nudge_Extend&action=edit&redlink=1 "BIM Nudge Extend \(page does not exist\)"), [Nudge Shrink](/index.php?title=BIM_Nudge_Shrink&action=edit&redlink=1 "BIM Nudge Shrink \(page does not exist\)")

* * *

  * **Additional:** [Preferences](/BIM_Preferences "BIM Preferences"), [Fine tuning](/Fine-tuning "Fine-tuning"), [Import Export Preferences](/Import_Export_Preferences "Import Export Preferences"), [IFC](/Arch_IFC "Arch IFC"), [DAE](/Arch_DAE "Arch DAE"), [OBJ](/Arch_OBJ "Arch OBJ"), [JSON](/Arch_JSON "Arch JSON"), [3DS](/Arch_3DS "Arch 3DS"), [SHP](/Arch_SHP "Arch SHP")

Expand[![](/images/thumb/9/94/User_hub.png/24px-
User_hub.png)](/index.php?title=File:User_hub.png&filetimestamp=20190221145008&)
[User documentation](/User_hub "User hub")

  * **[Getting started](/Getting_started "Getting started")**
  * **Installation:** [Download](/Download "Download"), [Windows](/Installing_on_Windows "Installing on Windows"), [Linux](/Installing_on_Linux "Installing on Linux"), [Mac](/Installing_on_Mac "Installing on Mac"), [Additional components](/Installing_additional_components "Installing additional components"), [Docker](/Compile_on_Docker "Compile on Docker"), [AppImage](/AppImage "AppImage"), [Ubuntu Snap](/Ubuntu_Snap "Ubuntu Snap")
  * **Basics:** [About FreeCAD](/About_FreeCAD "About FreeCAD"), [Interface](/Interface "Interface"), [Mouse navigation](/Mouse_navigation "Mouse navigation"), [Selection methods](/Selection_methods "Selection methods"), [Object name](/Object_name "Object name"), [Preferences](/Preferences_Editor "Preferences Editor"), [Workbenches](/Workbenches "Workbenches"), [Document structure](/Document_structure "Document structure"), [Properties](/Property "Property"), [Help FreeCAD](/Help_FreeCAD "Help FreeCAD"), [Donate](/Donate "Donate")

* * *

  * **Help:** [Tutorials](/Tutorials "Tutorials"), [Video tutorials](/Video_tutorials "Video tutorials")
  * **[Workbenches](/Workbenches "Workbenches"):** [Std Base](/Std_Base "Std Base"), [Assembly](/Assembly_Workbench "Assembly Workbench"), BIM, [CAM](/CAM_Workbench "CAM Workbench"), [Draft](/Draft_Workbench "Draft Workbench"), [FEM](/FEM_Workbench "FEM Workbench"), [Inspection](/Inspection_Workbench "Inspection Workbench"), [Material](/Material_Workbench "Material Workbench"), [Mesh](/Mesh_Workbench "Mesh Workbench"), [OpenSCAD](/OpenSCAD_Workbench "OpenSCAD Workbench"), [Part](/Part_Workbench "Part Workbench"), [PartDesign](/PartDesign_Workbench "PartDesign Workbench"), [Points](/Points_Workbench "Points Workbench"), [Reverse Engineering](/Reverse_Engineering_Workbench "Reverse Engineering Workbench"), [Robot](/Robot_Workbench "Robot Workbench"), [Sketcher](/Sketcher_Workbench "Sketcher Workbench"), [Spreadsheet](/Spreadsheet_Workbench "Spreadsheet Workbench"), [Surface](/Surface_Workbench "Surface Workbench"), [TechDraw](/TechDraw_Workbench "TechDraw Workbench"), [Test Framework](/Testing "Testing")

* * *

  * **[Addons](/Addon "Addon"):** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

