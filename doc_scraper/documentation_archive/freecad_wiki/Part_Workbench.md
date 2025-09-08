---
url: https://wiki.freecad.org/Part_Workbench
title: Part Workbench
scraped_at: 2025-09-08 16:44:16
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Tools Toggle Tools subsection
    * 2.1 Solids toolbar
    * 2.2 Part tools toolbar
    * 2.3 Boolean toolbar
    * 2.4 Other tools
  * 3 Obsolete tools Toggle Obsolete tools subsection
    * 3.1 Measure
  * 4 Preferences
  * 5 Scripting
  * 6 Tutorials

# Part Workbench

  * [Page](/Part_Workbench "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Part_Workbench&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Part_Workbench)
  * [Edit](/index.php?title=Part_Workbench&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Part_Workbench&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Part_Workbench.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Part_Workbench&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Part_Workbench)
  * [Edit](/index.php?title=Part_Workbench&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Part_Workbench&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Part_Workbench&action=history)

General

  * [What links here](/Special:WhatLinksHere/Part_Workbench "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Part_Workbench "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Part_Workbench&oldid=1629771 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Part_Workbench&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Part_Workbench&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Part+Workbench&action=page&filter=&language=en)This is the approved revision
of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Part+Workbench&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/Part_Workbench/id "Part Workbench \(1% translated\)")
  * [Deutsch](/Part_Workbench/de "Arbeitsbereich Part \(100% translated\)")
  * English
  * [Türkçe](/Part_Workbench/tr "Parça Tezgahı \(1% translated\)")
  * [español](/Part_Workbench/es "Modulo Pieza \(39% translated\)")
  * [français](/Part_Workbench/fr "Atelier Part \(100% translated\)")
  * [hrvatski](/Part_Workbench/hr "Dio Moduli \(3% translated\)")
  * [italiano](/Part_Workbench/it "Ambiente Part \(100% translated\)")
  * [polski](/Part_Workbench/pl "Środowisko pracy Część \(100% translated\)")
  * [português](/Part_Workbench/pt "Part Workbench \(1% translated\)")
  * [português do Brasil](/Part_Workbench/pt-br "Bancada de trabalho Part \(67% translated\)")
  * [română](/Part_Workbench/ro "Atelierul Piese \(38% translated\)")
  * [suomi](/Part_Workbench/fi "Part Workbench \(1% translated\)")
  * [svenska](/Part_Workbench/sv "Part Workbench \(17% translated\)")
  * [čeština](/Part_Workbench/cs "Modul Díl \(1% translated\)")
  * [русский](/Part_Workbench/ru "Верстак Деталь \(97% translated\)")
  * [українська](/Part_Workbench/uk "Part Workbench \(1% translated\)")
  * [中文](/Part_Workbench/zh "Part Workbench/zh \(0% translated\)")
  * [中文（中国大陆）](/Part_Workbench/zh-cn "零件模块 \(25% translated\)")
  * [中文（臺灣）](/Part_Workbench/zh-tw "物件坊 \(1% translated\)")
  * [日本語](/Part_Workbench/ja "パートワークベンチ \(7% translated\)")
  * [한국어](/Part_Workbench/ko "부품 작업대 \(11% translated\)")

![](/images/6/6f/Arrow-left.svg) ![](/images/4/4e/Workbench_OpenSCAD.svg)
[OpenSCAD Workbench](/OpenSCAD_Workbench "OpenSCAD Workbench")

![](/images/3/39/Workbench_PartDesign.svg) [PartDesign
Workbench](/PartDesign_Workbench "PartDesign Workbench")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

[![](/images/0/04/Workbench_Part.svg)](/index.php?title=File:Workbench_Part.svg&filetimestamp=20240712190040&)Part
workbench icon

## Introduction

The
[![](/images/0/04/Workbench_Part.svg)](/index.php?title=File:Workbench_Part.svg&filetimestamp=20240712190040&)
**Part Workbench** provides a traditional [constructive solid
geometry](/Constructive_solid_geometry "Constructive solid geometry") (CSG)
workflow. In this workflow each object is an independent solid. The Part
Workbench can create them from parametrically defined
[sketches](/Sketcher_Workbench "Sketcher Workbench") using tools like
[Extrude](/Part_Extrude "Part Extrude"), [Revolve](/Part_Revolve "Part
Revolve"), [Loft](/Part_Loft "Part Loft"), etc. In addition, basic primitive
solids like [Cube](/Part_Box "Part Box"), [Cylinder](/Part_Cylinder "Part
Cylinder"), etc. can be created as well. These objects can be combined,
through [Boolean operations](/Part_Boolean "Part Boolean"), to create more
complex solids.

The Part Workbench can also create objects that are not solids, such as faces,
shells, and objects with only edges or vertices. It also provides a variety of
general purpose tools for geometry manipulation, geometry validation, and
making copies.

The
[![](/images/3/39/Workbench_PartDesign.svg)](/index.php?title=File:Workbench_PartDesign.svg&filetimestamp=20240405092932&)
[PartDesign Workbench](/PartDesign_Workbench "PartDesign Workbench") uses an
alternative workflow for creating solids. For a detailed discussion of the
Part Workbench versus the Part Design Workbench see [Part and Part
Design](/Part_and_PartDesign "Part and PartDesign").

[![](/images/6/62/Part_Workbench_Example.jpg)](/index.php?title=File:Part_Workbench_Example.jpg&filetimestamp=20241019173735&)

## Tools

### Solids toolbar

  * [![](/images/3/34/Part_Box.svg)](/index.php?title=File:Part_Box.svg&filetimestamp=20240710103459&) [Box](/Part_Box "Part Box"): Creates a box.

  * [![](/images/e/e8/Part_Cylinder.svg)](/index.php?title=File:Part_Cylinder.svg&filetimestamp=20240712190137&) [Cylinder](/Part_Cylinder "Part Cylinder"): Creates a cylinder.

  * [![](/images/d/de/Part_Sphere.svg)](/index.php?title=File:Part_Sphere.svg&filetimestamp=20240712190158&) [Sphere](/Part_Sphere "Part Sphere"): Creates a sphere.

  * [![](/images/3/35/Part_Cone.svg)](/index.php?title=File:Part_Cone.svg&filetimestamp=20240712190216&) [Cone](/Part_Cone "Part Cone"): Creates a cone.

  * [![](/images/8/8f/Part_Torus.svg)](/index.php?title=File:Part_Torus.svg&filetimestamp=20240712190237&) [Torus](/Part_Torus "Part Torus"): Creates a torus.

  * [![](/images/2/2c/Part_Tube.svg)](/index.php?title=File:Part_Tube.svg&filetimestamp=20240712190302&) [Tube](/Part_Tube "Part Tube"): Creates a tube.

  * [![](/images/4/4d/Part_Primitives.svg)](/index.php?title=File:Part_Primitives.svg&filetimestamp=20240522201556&) [Create primitives...](/Part_Primitives "Part Primitives"): A tool to create one of the following primitives:

    

  * [![](/images/6/64/Part_Plane.svg)](/index.php?title=File:Part_Plane.svg&filetimestamp=20240712191004&) [Plane](/Part_Plane "Part Plane"): Creates a plane.

    

  * [![](/images/3/34/Part_Box.svg)](/index.php?title=File:Part_Box.svg&filetimestamp=20240710103459&) [Box](/Part_Box "Part Box"): Creates a box. This object can also be created with the [Box](/Part_Box "Part Box") tool.

    

  * [![](/images/e/e8/Part_Cylinder.svg)](/index.php?title=File:Part_Cylinder.svg&filetimestamp=20240712190137&) [Cylinder](/Part_Cylinder "Part Cylinder"): Creates a cylinder. This object can also be created with the [Cylinder](/Part_Cylinder "Part Cylinder") tool.

    

  * [![](/images/3/35/Part_Cone.svg)](/index.php?title=File:Part_Cone.svg&filetimestamp=20240712190216&) [Cone](/Part_Cone "Part Cone"): Creates a cone. This object can also be created with the [Cone](/Part_Cone "Part Cone") tool.

    

  * [![](/images/d/de/Part_Sphere.svg)](/index.php?title=File:Part_Sphere.svg&filetimestamp=20240712190158&) [Sphere](/Part_Sphere "Part Sphere"): Creates a sphere. This object can also be created with the [Sphere](/Part_Sphere "Part Sphere") tool.

    

  * [![](/images/c/ce/Part_Ellipsoid.svg)](/index.php?title=File:Part_Ellipsoid.svg&filetimestamp=20240712191105&) [Ellipsoid](/Part_Ellipsoid "Part Ellipsoid"): Creates a ellipsoid.

    

  * [![](/images/8/8f/Part_Torus.svg)](/index.php?title=File:Part_Torus.svg&filetimestamp=20240712190237&) [Torus](/Part_Torus "Part Torus"): Creates a torus. This object can also be created with the [Torus](/Part_Torus "Part Torus") tool.

    

  * [![](/images/e/e5/Part_Prism.svg)](/index.php?title=File:Part_Prism.svg&filetimestamp=20240712191206&) [Prism](/Part_Prism "Part Prism"): Creates a prism.

    

  * [![](/images/f/f4/Part_Wedge.svg)](/index.php?title=File:Part_Wedge.svg&filetimestamp=20240712191249&) [Wedge](/Part_Wedge "Part Wedge"): Creates a wedge.

    

  * [![](/images/7/70/Part_Helix.svg)](/index.php?title=File:Part_Helix.svg&filetimestamp=20240712191334&) [Helix](/Part_Helix "Part Helix"): Creates a helix.

    

  * [![](/images/2/25/Part_Spiral.svg)](/index.php?title=File:Part_Spiral.svg&filetimestamp=20240712191421&) [Spiral](/Part_Spiral "Part Spiral"): Creates a spiral.

    

  * [![](/images/4/4e/Part_Circle.svg)](/index.php?title=File:Part_Circle.svg&filetimestamp=20240712191503&) [Circle](/Part_Circle "Part Circle"): Creates a circular arc.

    

  * [![](/images/a/ac/Part_Ellipse.svg)](/index.php?title=File:Part_Ellipse.svg&filetimestamp=20240712191545&) [Ellipse](/Part_Ellipse "Part Ellipse"): Creates an elliptical arc.

    

  * [![](/images/a/aa/Part_Point.svg)](/index.php?title=File:Part_Point.svg&filetimestamp=20240712191648&) [Point](/Part_Point "Part Point"): Creates a point.

    

  * [![](/images/3/36/Part_Line.svg)](/index.php?title=File:Part_Line.svg&filetimestamp=20240712191717&) [Line](/Part_Line "Part Line"): Creates a line.

    

  * [![](/images/b/be/Part_RegularPolygon.svg)](/index.php?title=File:Part_RegularPolygon.svg&filetimestamp=20240712191755&) [Regular polygon](/Part_RegularPolygon "Part RegularPolygon"): Creates a regular polygon.

  * [![](/images/2/2a/Part_Builder.svg)](/index.php?title=File:Part_Builder.svg&filetimestamp=20240611075248&) [Shape builder...](/Part_Builder "Part Builder"): Creates shapes from various primitives.

### Part tools toolbar

  * [![](/images/f/f1/Sketcher_NewSketch.svg)](/index.php?title=File:Sketcher_NewSketch.svg&filetimestamp=20231231201726&) [Create sketch](/Sketcher_NewSketch "Sketcher NewSketch"): Creates a new sketch and opens the [Sketcher Dialog](/Sketcher_Dialog "Sketcher Dialog") to edit it.

  * [![](/images/3/38/Part_Extrude.svg)](/index.php?title=File:Part_Extrude.svg&filetimestamp=20240705092108&) [Extrude](/Part_Extrude "Part Extrude"): Extrudes planar faces.

  * [![](/images/5/57/Part_Revolve.svg)](/index.php?title=File:Part_Revolve.svg&filetimestamp=20240712184727&) [Revolve](/Part_Revolve "Part Revolve"): Creates a solid by revolving an object (not a solid) around an axis.

  * [![](/images/8/85/Part_Mirror.svg)](/index.php?title=File:Part_Mirror.svg&filetimestamp=20240712184557&) [Mirror](/Part_Mirror "Part Mirror"): Mirrors the selected object across a mirror plane.

  * [![](/images/e/ed/Part_Scale.svg)](/index.php?title=File:Part_Scale.svg&filetimestamp=20240712184753&) [Scale](/Part_Scale "Part Scale"): Scales one or more shapes. [introduced in 1.0](/Release_notes_1.0 "Release notes 1.0")

  * [![](/images/3/30/Part_Fillet.svg)](/index.php?title=File:Part_Fillet.svg&filetimestamp=20240712184502&) [Fillet](/Part_Fillet "Part Fillet"): Fillets (rounds) edges of an object.

  * [![](/images/8/8c/Part_Chamfer.svg)](/index.php?title=File:Part_Chamfer.svg&filetimestamp=20240712184401&) [Chamfer](/Part_Chamfer "Part Chamfer"): Chamfers edges of an object.

  * [![](/images/a/a7/Part_MakeFace.svg)](/index.php?title=File:Part_MakeFace.svg&filetimestamp=20240710120955&) [Make face from wires](/Part_MakeFace "Part MakeFace"): Makes a face from a set of wires (contours).

  * [![](/images/1/15/Part_RuledSurface.svg)](/index.php?title=File:Part_RuledSurface.svg&filetimestamp=20240712184739&) [Ruled Surface](/Part_RuledSurface "Part RuledSurface"): Creates a ruled surface.

  * [![](/images/6/6b/Part_Loft.svg)](/index.php?title=File:Part_Loft.svg&filetimestamp=20240712184517&) [Loft](/Part_Loft "Part Loft"): Lofts from one profile to another.

  * [![](/images/2/2a/Part_Sweep.svg)](/index.php?title=File:Part_Sweep.svg&filetimestamp=20240712184832&) [Sweep](/Part_Sweep "Part Sweep"): Sweeps one or more profiles along a path.

  * [![](/images/f/f7/Part_Section.svg)](/index.php?title=File:Part_Section.svg&filetimestamp=20240712183658&) [Section](/Part_Section "Part Section"): Creates a section by intersecting an object with a section plane.

  * [![](/images/d/df/Part_CrossSections.svg)](/index.php?title=File:Part_CrossSections.svg&filetimestamp=20240712183356&) [Cross sections...](/Part_CrossSections "Part CrossSections"): Creates one or more cross-sections through an object.

  * [![](/images/9/9a/Part_Offset.svg)](/index.php?title=File:Part_Offset.svg&filetimestamp=20240712184610&)[![](/images/3/34/Toolbar_flyout_arrow_blue_background.svg)](/index.php?title=File:Toolbar_flyout_arrow_blue_background.svg&filetimestamp=20221006081506&) Offset:

    

  * [![](/images/9/9a/Part_Offset.svg)](/index.php?title=File:Part_Offset.svg&filetimestamp=20240712184610&) [3D Offset](/Part_Offset "Part Offset"): Constructs a parallel shape at a certain distance from an original.

    

  * [![](/images/7/7b/Part_Offset2D.svg)](/index.php?title=File:Part_Offset2D.svg&filetimestamp=20240705091942&) [2D Offset](/Part_Offset2D "Part Offset2D"): Constructs a parallel wire at certain distance from an original, or enlarges/shrinks a planar face.

  * [![](/images/d/d2/Part_Thickness.svg)](/index.php?title=File:Part_Thickness.svg&filetimestamp=20240712184843&) [Thickness](/Part_Thickness "Part Thickness"): Hollows out a solid.

  * [![](/images/4/4a/Part_ProjectionOnSurface.svg)](/index.php?title=File:Part_ProjectionOnSurface.svg&filetimestamp=20240712184645&) [Projection on surface](/Part_ProjectionOnSurface "Part ProjectionOnSurface"): Projects a logo, text or any face, wire or edge onto a surface.

  * [![](/images/c/cf/Part_ColorPerFace.svg)](/index.php?title=File:Part_ColorPerFace.svg&filetimestamp=20240413174244&) [Color per face](/Part_ColorPerFace "Part ColorPerFace"): Assigns colors to individual faces of objects.

### Boolean toolbar

  * [![](/images/0/0f/Part_Compound.svg)](/index.php?title=File:Part_Compound.svg&filetimestamp=20190304152450&)[![](/images/3/34/Toolbar_flyout_arrow_blue_background.svg)](/index.php?title=File:Toolbar_flyout_arrow_blue_background.svg&filetimestamp=20221006081506&) Compound:

    

  * [![](/images/0/0f/Part_Compound.svg)](/index.php?title=File:Part_Compound.svg&filetimestamp=20190304152450&) [Make compound](/Part_Compound "Part Compound"): Creates a compound from the selected objects.

    

  * [![](/images/2/23/Part_ExplodeCompound.svg)](/index.php?title=File:Part_ExplodeCompound.svg&filetimestamp=20190304152129&) [Explode compound](/Part_ExplodeCompound "Part ExplodeCompound"): Splits up compounds.

    

  * [![](/images/0/00/Part_CompoundFilter.svg)](/index.php?title=File:Part_CompoundFilter.svg&filetimestamp=20240712183337&) [Compound Filter](/Part_CompoundFilter "Part CompoundFilter"): Extracts the individual pieces from compounds.

  * [![](/images/e/ef/Part_Boolean.svg)](/index.php?title=File:Part_Boolean.svg&filetimestamp=20240712192304&) [Boolean](/Part_Boolean "Part Boolean"): Performs boolean operations on two objects.

  * [![](/images/f/fb/Part_Cut.svg)](/index.php?title=File:Part_Cut.svg&filetimestamp=20240705092150&) [Cut](/Part_Cut "Part Cut"): Cuts one object from another.

  * [![](/images/e/e4/Part_Fuse.svg)](/index.php?title=File:Part_Fuse.svg&filetimestamp=20240705092218&) [Union](/Part_Fuse "Part Fuse"): Fuses two or more objects.

  * [![](/images/1/15/Part_Common.svg)](/index.php?title=File:Part_Common.svg&filetimestamp=20240705092244&) [Intersection](/Part_Common "Part Common"): Extracts the common part of two objects.

  * [![](/images/a/ac/Part_JoinConnect.svg)](/index.php?title=File:Part_JoinConnect.svg&filetimestamp=20240712183548&)[![](/images/3/34/Toolbar_flyout_arrow_blue_background.svg)](/index.php?title=File:Toolbar_flyout_arrow_blue_background.svg&filetimestamp=20221006081506&) Join:

    

  * [![](/images/a/ac/Part_JoinConnect.svg)](/index.php?title=File:Part_JoinConnect.svg&filetimestamp=20240712183548&) [Connect objects](/Part_JoinConnect "Part JoinConnect"): Connects interiors of walled objects.

    

  * [![](/images/4/45/Part_JoinEmbed.svg)](/index.php?title=File:Part_JoinEmbed.svg&filetimestamp=20240712183639&) [Embed object](/Part_JoinEmbed "Part JoinEmbed"): Embeds a walled object into another walled object.

    

  * [![](/images/c/c0/Part_JoinCutout.svg)](/index.php?title=File:Part_JoinCutout.svg&filetimestamp=20240712183610&) [Cutout for object](/Part_JoinCutout "Part JoinCutout"): Creates a cutout in a wall of an object for another walled object.

  * [![](/images/5/5e/Part_BooleanFragments.svg)](/index.php?title=File:Part_BooleanFragments.svg&filetimestamp=20240712183152&)[![](/images/3/34/Toolbar_flyout_arrow_blue_background.svg)](/index.php?title=File:Toolbar_flyout_arrow_blue_background.svg&filetimestamp=20221006081506&) Split:

    

  * [![](/images/5/5e/Part_BooleanFragments.svg)](/index.php?title=File:Part_BooleanFragments.svg&filetimestamp=20240712183152&) [Boolean fragments](/Part_BooleanFragments "Part BooleanFragments"): Creates all pieces obtained from Boolean operations.

    

  * [![](/images/5/56/Part_SliceApart.svg)](/index.php?title=File:Part_SliceApart.svg&filetimestamp=20240712183721&) [Slice apart](/Part_SliceApart "Part SliceApart"): Slices and splits an object by intersecting it with other objects.

    

  * [![](/images/2/2b/Part_Slice.svg)](/index.php?title=File:Part_Slice.svg&filetimestamp=20240712183709&) [Slice to compound](/Part_Slice "Part Slice"): Slices an object by intersecting it with other objects.

    

  * [![](/images/7/73/Part_XOR.svg)](/index.php?title=File:Part_XOR.svg&filetimestamp=20240712183733&) [Boolean XOR](/Part_XOR "Part XOR"): Removes space shared by an even number of objects.

  * [![](/images/6/64/Part_CheckGeometry.svg)](/index.php?title=File:Part_CheckGeometry.svg&filetimestamp=20240712183246&) [Check geometry](/Part_CheckGeometry "Part CheckGeometry"): Checks the geometry of selected objects for errors.

  * [![](/images/b/be/Part_Defeaturing.svg)](/index.php?title=File:Part_Defeaturing.svg&filetimestamp=20240712183424&) [Defeaturing](/Part_Defeaturing "Part Defeaturing"): Removes features from an object.

### Other tools

  * [![](/images/e/e9/Part_BoxSelection.svg)](/index.php?title=File:Part_BoxSelection.svg&filetimestamp=20240712184956&) [Box selection](/Part_BoxSelection "Part BoxSelection"): Selects faces from a rectangular area.

  * [![](/images/7/70/Part_ShapeFromMesh.svg)](/index.php?title=File:Part_ShapeFromMesh.svg&filetimestamp=20240712192625&) [Create shape from mesh](/Part_ShapeFromMesh "Part ShapeFromMesh"): Creates shapes from mesh objects.

  * [![](/images/9/99/Part_PointsFromMesh.svg)](/index.php?title=File:Part_PointsFromMesh.svg&filetimestamp=20240712184634&) [Create points object from geometry](/Part_PointsFromMesh "Part PointsFromMesh"): Creates points objects from geometric objects.

  * [![](/images/1/1f/Part_MakeSolid.svg)](/index.php?title=File:Part_MakeSolid.svg&filetimestamp=20240712184539&) [Convert to solid](/Part_MakeSolid "Part MakeSolid"): Creates solids from shape objects.

  * [![](/images/0/07/Part_ReverseShape.svg)](/index.php?title=File:Part_ReverseShape.svg&filetimestamp=20231116135301&) [Reverse shapes](/Part_ReverseShape "Part ReverseShape"): Creates parametric copies with reversed face normals from selected objects.

  * Create a copy:

    

  * [![](/images/f/ff/Part_SimpleCopy.svg)](/index.php?title=File:Part_SimpleCopy.svg&filetimestamp=20240712192934&) [Create simple copy](/Part_SimpleCopy "Part SimpleCopy"): Creates non-parametric copies of objects.

    

  * [![](/images/a/a7/Part_TransformedCopy.svg)](/index.php?title=File:Part_TransformedCopy.svg&filetimestamp=20240712193014&) [Create transformed copy](/Part_TransformedCopy "Part TransformedCopy"): Creates non-parametric copies of objects. It is intended for objects nested in containers.

    

  * [![](/images/1/1c/Part_ElementCopy.svg)](/index.php?title=File:Part_ElementCopy.svg&filetimestamp=20240712193042&) [Create shape element copy](/Part_ElementCopy "Part ElementCopy"): Creates non-parametric copies of subelements: vertices, edges and faces.

    

  * [![](/images/e/e0/Part_RefineShape.svg)](/index.php?title=File:Part_RefineShape.svg&filetimestamp=20240712193113&) [Refine shape](/Part_RefineShape "Part RefineShape"): Creates parametric copies with a refined shape from selected objects. It removes unnecessary edges from planar and cylindrical faces.

  * [![](/images/f/f6/Part_SectionCut.svg)](/index.php?title=File:Part_SectionCut.svg&filetimestamp=20240712185111&) [Persistent section cut](/Part_SectionCut "Part SectionCut"): Creates persistent cuts of objects and assemblies.

  * [![](/images/8/84/Part_EditAttachment.svg)](/index.php?title=File:Part_EditAttachment.svg&filetimestamp=20240712192200&) [Attachment...](/Part_EditAttachment "Part EditAttachment"): Attaches an object to one or more other objects.

## Obsolete tools

  * [![](/images/6/6f/Part_Import.svg)](/index.php?title=File:Part_Import.svg&filetimestamp=20240712185058&) [Import CAD file...](/Part_Import "Part Import"): Imports from *.IGES, *.STEP, or *.BREP files. Not available in 1.1 and above.

  * [![](/images/a/a6/Part_Export.svg)](/index.php?title=File:Part_Export.svg&filetimestamp=20240712185021&) [Export CAD file...](/Part_Export "Part Export"): Exports to *.IGES, *.STEP, or *.BREP files. Not available in 1.1 and above.

### Measure

The
[![](/images/4/4e/Std_Measure.svg)](/index.php?title=File:Std_Measure.svg&filetimestamp=20240704211636&)
[Std Measure](/Std_Measure "Std Measure") tool replaces the tools listed
below. [introduced in 1.0](/Release_notes_1.0 "Release notes 1.0")

  * [![](/images/c/c7/Part_Measure_Linear.svg)](/index.php?title=File:Part_Measure_Linear.svg&filetimestamp=20170323081126&) [Measure Linear](/Part_Measure_Linear "Part Measure Linear"): Creates a linear measurement. Not available in 1.0 and above.

  * [![](/images/f/ff/Part_Measure_Angular.svg)](/index.php?title=File:Part_Measure_Angular.svg&filetimestamp=20170323081045&) [Measure Angular](/Part_Measure_Angular "Part Measure Angular"): Creates an angular measurement. Not available in 1.0 and above.

  * [![](/images/4/4a/Part_Measure_Refresh.svg)](/index.php?title=File:Part_Measure_Refresh.svg&filetimestamp=20190927060028&) [Measure Refresh](/Part_Measure_Refresh "Part Measure Refresh"): Updates all measurements. Not available in 1.0 and above.

  * [![](/images/a/a6/Part_Measure_Clear_All.svg)](/index.php?title=File:Part_Measure_Clear_All.svg&filetimestamp=20240704194706&) [Clear All](/Part_Measure_Clear_All "Part Measure Clear All") and [View Measure Clear All](/View_Measure_Clear_All "View Measure Clear All"): Clears all measurements. Not available in 1.0 and above.

  * [![](/images/b/b9/Part_Measure_Toggle_All.svg)](/index.php?title=File:Part_Measure_Toggle_All.svg&filetimestamp=20240704194746&) [Toggle All](/Part_Measure_Toggle_All "Part Measure Toggle All") and [View Measure Toggle All](/View_Measure_Toggle_All "View Measure Toggle All"): Shows or hides all measurements. Not available in 1.0 and above.

  * [![](/images/5/50/Part_Measure_Toggle_3D.svg)](/index.php?title=File:Part_Measure_Toggle_3D.svg&filetimestamp=20220914150549&) [Toggle 3D](/Part_Measure_Toggle_3D "Part Measure Toggle 3D"): Shows or hides 3D measurements. Not available in 1.0 and above.

  * [![](/images/b/be/Part_Measure_Toggle_Delta.svg)](/index.php?title=File:Part_Measure_Toggle_Delta.svg&filetimestamp=20170323081328&) [Toggle Delta](/Part_Measure_Toggle_Delta "Part Measure Toggle Delta"): Shows or hides delta measurements. Not available in 1.0 and above.

## Preferences

  * [![](/images/c/c9/Preferences-part_design.svg)](/index.php?title=File:Preferences-part_design.svg&filetimestamp=20240712185139&) [Preferences](/PartDesign_Preferences "PartDesign Preferences"): Preferences for the Part Workbench.
  * [![](/images/2/29/Preferences-import-export.svg)](/index.php?title=File:Preferences-import-export.svg&filetimestamp=20240704194838&) [Import Export Preferences](/Import_Export_Preferences "Import Export Preferences"): Preferences for importing from and exporting to different file formats.
  * [Fine-tuning](/Fine-tuning#Part_Workbench "Fine-tuning"): Some extra parameters to fine-tune Part behavior.

## Scripting

See [Part scripting](/Part_scripting "Part scripting").

## Tutorials

  * [Import from STL or OBJ](/Import_from_STL_or_OBJ "Import from STL or OBJ"): How to import STL/OBJ files in FreeCAD
  * [Export to STL or OBJ](/Export_to_STL_or_OBJ "Export to STL or OBJ"): How to export STL/OBJ files from FreeCAD
  * [Whiffle Ball tutorial](/Whiffle_Ball_tutorial "Whiffle Ball tutorial"): How to use the Part Workbench

  

![](/images/6/6f/Arrow-left.svg) ![](/images/4/4e/Workbench_OpenSCAD.svg)
[OpenSCAD Workbench](/OpenSCAD_Workbench "OpenSCAD Workbench")

![](/images/3/39/Workbench_PartDesign.svg) [PartDesign
Workbench](/PartDesign_Workbench "PartDesign Workbench")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

Expand[![](/images/0/04/Workbench_Part.svg)](/index.php?title=File:Workbench_Part.svg&filetimestamp=20240712190040&)
Part

  * **Primitives:** [Box](/Part_Box "Part Box"), [Cylinder](/Part_Cylinder "Part Cylinder"), [Sphere](/Part_Sphere "Part Sphere"), [Cone](/Part_Cone "Part Cone"), [Torus](/Part_Torus "Part Torus"), [Tube](/Part_Tube "Part Tube"), [Create primitives](/Part_Primitives "Part Primitives"), [Shape builder](/Part_Builder "Part Builder")

* * *

  * **Creation and modification:** [Create sketch](/Sketcher_NewSketch "Sketcher NewSketch"), [Extrude](/Part_Extrude "Part Extrude"), [Revolve](/Part_Revolve "Part Revolve"), [Mirror](/Part_Mirror "Part Mirror"), [Scale](/Part_Scale "Part Scale"), [Fillet](/Part_Fillet "Part Fillet"), [Chamfer](/Part_Chamfer "Part Chamfer"), [Make face from wires](/Part_MakeFace "Part MakeFace"), [Ruled Surface](/Part_RuledSurface "Part RuledSurface"), [Loft](/Part_Loft "Part Loft"), [Sweep](/Part_Sweep "Part Sweep"), [Section](/Part_Section "Part Section"), [Cross sections](/Part_CrossSections "Part CrossSections"), [3D Offset](/Part_Offset "Part Offset"), [2D Offset](/Part_Offset2D "Part Offset2D"), [Thickness](/Part_Thickness "Part Thickness"), [Projection on surface](/Part_ProjectionOnSurface "Part ProjectionOnSurface"), [Color per face](/Part_ColorPerFace "Part ColorPerFace")

* * *

  * **Boolean:** [Make compound](/Part_Compound "Part Compound"), [Explode compound](/Part_ExplodeCompound "Part ExplodeCompound"), [Compound Filter](/Part_CompoundFilter "Part CompoundFilter"), [Boolean](/Part_Boolean "Part Boolean"), [Cut](/Part_Cut "Part Cut"), [Union](/Part_Fuse "Part Fuse"), [Intersection](/Part_Common "Part Common"), [Connect objects](/Part_JoinConnect "Part JoinConnect"), [Embed object](/Part_JoinEmbed "Part JoinEmbed"), [Cutout for object](/Part_JoinCutout "Part JoinCutout"), [Boolean fragments](/Part_BooleanFragments "Part BooleanFragments"), [Slice apart](/Part_SliceApart "Part SliceApart"), [Slice to compound](/Part_Slice "Part Slice"), [Boolean XOR](/Part_XOR "Part XOR"), [Check geometry](/Part_CheckGeometry "Part CheckGeometry"), [Defeaturing](/Part_Defeaturing "Part Defeaturing")

* * *

  * **Other tools:** [Import CAD file](/Part_Import "Part Import"), [Export CAD file](/Part_Export "Part Export"), [Box selection](/Part_BoxSelection "Part BoxSelection"), [Create shape from mesh](/Part_ShapeFromMesh "Part ShapeFromMesh"), [Create points object from geometry](/Part_PointsFromMesh "Part PointsFromMesh"), [Convert to solid](/Part_MakeSolid "Part MakeSolid"), [Reverse shapes](/Part_ReverseShape "Part ReverseShape"), [Create simple copy](/Part_SimpleCopy "Part SimpleCopy"), [Create transformed copy](/Part_TransformedCopy "Part TransformedCopy"), [Create shape element copy](/Part_ElementCopy "Part ElementCopy"), [Refine shape](/Part_RefineShape "Part RefineShape"), [Attachment](/Part_EditAttachment "Part EditAttachment")

* * *

  * **Preferences:** [Preferences](/PartDesign_Preferences "PartDesign Preferences"), [Fine tuning](/Fine-tuning "Fine-tuning")

Expand[![](/images/thumb/9/94/User_hub.png/24px-
User_hub.png)](/index.php?title=File:User_hub.png&filetimestamp=20190221145008&)
[User documentation](/User_hub "User hub")

  * **[Getting started](/Getting_started "Getting started")**
  * **Installation:** [Download](/Download "Download"), [Windows](/Installing_on_Windows "Installing on Windows"), [Linux](/Installing_on_Linux "Installing on Linux"), [Mac](/Installing_on_Mac "Installing on Mac"), [Additional components](/Installing_additional_components "Installing additional components"), [Docker](/Compile_on_Docker "Compile on Docker"), [AppImage](/AppImage "AppImage"), [Ubuntu Snap](/Ubuntu_Snap "Ubuntu Snap")
  * **Basics:** [About FreeCAD](/About_FreeCAD "About FreeCAD"), [Interface](/Interface "Interface"), [Mouse navigation](/Mouse_navigation "Mouse navigation"), [Selection methods](/Selection_methods "Selection methods"), [Object name](/Object_name "Object name"), [Preferences](/Preferences_Editor "Preferences Editor"), [Workbenches](/Workbenches "Workbenches"), [Document structure](/Document_structure "Document structure"), [Properties](/Property "Property"), [Help FreeCAD](/Help_FreeCAD "Help FreeCAD"), [Donate](/Donate "Donate")

* * *

  * **Help:** [Tutorials](/Tutorials "Tutorials"), [Video tutorials](/Video_tutorials "Video tutorials")
  * **[Workbenches](/Workbenches "Workbenches"):** [Std Base](/Std_Base "Std Base"), [Assembly](/Assembly_Workbench "Assembly Workbench"), [BIM](/BIM_Workbench "BIM Workbench"), [CAM](/CAM_Workbench "CAM Workbench"), [Draft](/Draft_Workbench "Draft Workbench"), [FEM](/FEM_Workbench "FEM Workbench"), [Inspection](/Inspection_Workbench "Inspection Workbench"), [Material](/Material_Workbench "Material Workbench"), [Mesh](/Mesh_Workbench "Mesh Workbench"), [OpenSCAD](/OpenSCAD_Workbench "OpenSCAD Workbench"), Part, [PartDesign](/PartDesign_Workbench "PartDesign Workbench"), [Points](/Points_Workbench "Points Workbench"), [Reverse Engineering](/Reverse_Engineering_Workbench "Reverse Engineering Workbench"), [Robot](/Robot_Workbench "Robot Workbench"), [Sketcher](/Sketcher_Workbench "Sketcher Workbench"), [Spreadsheet](/Spreadsheet_Workbench "Spreadsheet Workbench"), [Surface](/Surface_Workbench "Surface Workbench"), [TechDraw](/TechDraw_Workbench "TechDraw Workbench"), [Test Framework](/Testing "Testing")

* * *

  * **[Addons](/Addon "Addon"):** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

