---
url: https://wiki.freecad.org/Mesh_Scripting
title: Mesh Scripting
scraped_at: 2025-09-08 16:41:34
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Creation
  * 3 Modeling
  * 4 Notes

# Mesh Scripting

  * [Page](/Mesh_Scripting "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Mesh_Scripting&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Mesh_Scripting)
  * [Edit](/index.php?title=Mesh_Scripting&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Mesh_Scripting&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Mesh_Scripting.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Mesh_Scripting&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Mesh_Scripting)
  * [Edit](/index.php?title=Mesh_Scripting&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Mesh_Scripting&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Mesh_Scripting&action=history)

General

  * [What links here](/Special:WhatLinksHere/Mesh_Scripting "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Mesh_Scripting "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Mesh_Scripting&oldid=1019231 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Mesh_Scripting&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Mesh_Scripting&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Mesh+Scripting&action=page&filter=&language=en)This is the approved revision
of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Mesh+Scripting&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/Mesh_Scripting/id "Mesh Scripting \(6% translated\)")
  * [Deutsch](/Mesh_Scripting/de "Netz Skripten \(100% translated\)")
  * English
  * [Türkçe](/Mesh_Scripting/tr "Mesh Scripting \(6% translated\)")
  * [español](/Mesh_Scripting/es "Guionización Malla \(100% translated\)")
  * [français](/Mesh_Scripting/fr "Mesh Scripts \(100% translated\)")
  * [italiano](/Mesh_Scripting/it "Script in ambiente Mesh \(100% translated\)")
  * [polski](/Mesh_Scripting/pl "Skrytpy w środowisku Siatek \(100% translated\)")
  * [română](/Mesh_Scripting/ro "Script-Programare de Plase \(12% translated\)")
  * [svenska](/Mesh_Scripting/sv "Mesh Scripting \(12% translated\)")
  * [čeština](/Mesh_Scripting/cs "Mesh Scripting \(6% translated\)")
  * [русский](/Mesh_Scripting/ru "Программирование полигональных сеток \(100% translated\)")
  * [中文（中国大陆）](/Mesh_Scripting/zh-cn "网格脚本 \(12% translated\)")

## Introduction

To get access to the `Mesh` module you have to import it first:

    
    
    import Mesh
    

## Creation

To create an empty mesh object just use the standard constructor:

    
    
    mesh = Mesh.Mesh()
    

You can also create an object from a file:

    
    
    mesh = Mesh.Mesh("D:/temp/Something.stl")
    

Or create it out of a set of triangles described by their corner points:

    
    
    triangles = [
    # triangle 1
    [-0.5000, -0.5000, 0.0000], [0.5000, 0.5000, 0.0000], [-0.5000, 0.5000, 0.0000],
    #triangle 2
    [-0.5000, -0.5000, 0.0000], [0.5000, -0.5000, 0.0000], [0.5000, 0.5000, 0.0000],
    ]
    meshObject = Mesh.Mesh(triangles)
    Mesh.show(meshObject)
    

The Mesh-Kernel takes care of creating a topologically correct data structure
by sorting coincident points and edges.

Top

## Modeling

To create regular geometries you can use one of the `create*()` methods. A
torus, for instance, can be created as follows:

    
    
    m = Mesh.createTorus(8.0, 2.0, 50)
    Mesh.show(m)
    

The first two parameters define the radii of the torus and the third parameter
is a sub-sampling factor for how many triangles are created. The higher this
value the smoother the mesh.

The `Mesh` module also provides three Boolean methods: `union()`,
`intersection()` and `difference()`:

    
    
    m1, m2              # are the input mesh objects
    m3 = Mesh.Mesh(m1)  # create a copy of m1
    m3.unite(m2)        # union of m1 and m2, the result is stored in m3
    m4 = Mesh.Mesh(m1)
    m4.intersect(m2)    # intersection of m1 and m2
    m5 = Mesh.Mesh(m1)
    m5.difference(m2)   # the difference of m1 and m2
    m6 = Mesh.Mesh(m2)
    m6.difference(m1)   # the difference of m2 and m1, usually the result is different to m5
    

Here is an example that creates a pipe using the `difference()` method:

    
    
    import FreeCAD, Mesh
    cylA = Mesh.createCylinder(2.0, 10.0, True, 1.0, 36)
    cylB = Mesh.createCylinder(1.0, 12.0, True, 1.0, 36)
    cylB.Placement.Base = (FreeCAD.Vector(-1, 0, 0)) # move cylB to avoid co-planar faces
    pipe = cylA
    pipe = pipe.difference(cylB)
    pipe.flipNormals() # somehow required
    doc = FreeCAD.ActiveDocument
    obj = d.addObject("Mesh::Feature", "Pipe")
    obj.Mesh = pipe
    doc.recompute()
    

Top

## Notes

An extensive, though hard to use, source of mesh related scripting are the
unit test scripts of the `Mesh` module. In these unit tests literally all
methods are called and all properties/attributes are tweaked. So if you are
bold enough, take a look at the [Unit Test
module](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Mesh/App/MeshTestsApp.py).

See also: [Mesh API](/Mesh_API "Mesh API").

Top

Expand[![](/images/thumb/8/8f/Power_user_hub.png/24px-
Power_user_hub.png)](/index.php?title=File:Power_user_hub.png&filetimestamp=20200511213015&)
[Power user documentation](/Power_users_hub "Power users hub")

  * **FreeCAD scripting:** [Python](/Python "Python"), [Introduction to Python](/Introduction_to_Python "Introduction to Python"), [Python scripting tutorial](/Python_scripting_tutorial "Python scripting tutorial"), [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics")

* * *

  * **Modules:** [Builtin modules](/Builtin_modules "Builtin modules"), [Units](/Units "Units"), [Quantity](/Quantity "Quantity")
  * **Workbenches:** [Workbench creation](/Workbench_creation "Workbench creation"), [Gui Commands](/Gui_Command "Gui Command"), [Commands](/Command "Command"), [Installing more workbenches](/Installing_more_workbenches "Installing more workbenches")
  * **Meshes and Parts:** Mesh Scripting, [Topological data scripting](/Topological_data_scripting "Topological data scripting"), [Mesh to Part](/Mesh_to_Part "Mesh to Part"), [PythonOCC](/PythonOCC "PythonOCC")

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

Expand[![](/images/8/84/Workbench_Mesh.svg)](/index.php?title=File:Workbench_Mesh.svg&filetimestamp=20200404173024&)
[Mesh](/Mesh_Workbench "Mesh Workbench")

  * **Miscellaneous:** [Import Mesh](/Mesh_Import "Mesh Import"), [Export Mesh](/Mesh_Export "Mesh Export"), [Mesh From Shape](/Mesh_FromPartShape "Mesh FromPartShape"), [Regular solid](/Mesh_BuildRegularSolid "Mesh BuildRegularSolid"), [Unwrap Mesh](/MeshPart_CreateFlatMesh "MeshPart CreateFlatMesh"), [Unwrap Face](/MeshPart_CreateFlatFace "MeshPart CreateFlatFace")
  * **Modifying:** [Harmonize Normals](/Mesh_HarmonizeNormals "Mesh HarmonizeNormals"), [Flip Normals](/Mesh_FlipNormals "Mesh FlipNormals"), [Fill Holes](/Mesh_FillupHoles "Mesh FillupHoles"), [Close Holes](/Mesh_FillInteractiveHole "Mesh FillInteractiveHole"), [Add Triangle](/Mesh_AddFacet "Mesh AddFacet"), [Remove Components](/Mesh_RemoveComponents "Mesh RemoveComponents"), [Remove Components Manually](/Mesh_RemoveCompByHand "Mesh RemoveCompByHand"), [Smooth](/Mesh_Smoothing "Mesh Smoothing"), [Refinement](/Mesh_RemeshGmsh "Mesh RemeshGmsh"), [Decimate](/Mesh_Decimating "Mesh Decimating"), [Scale](/Mesh_Scale "Mesh Scale")

* * *

  * **Boolean:** [Union](/Mesh_Union "Mesh Union"), [Intersection](/Mesh_Intersection "Mesh Intersection"), [Difference](/Mesh_Difference "Mesh Difference")
  * **Cutting:** [Cut](/Mesh_PolyCut "Mesh PolyCut"), [Trim](/Mesh_PolyTrim "Mesh PolyTrim"), [Trim With Plane](/Mesh_TrimByPlane "Mesh TrimByPlane"), [Section From Plane](/Mesh_SectionByPlane "Mesh SectionByPlane"), [Cross-Sections](/Mesh_CrossSections "Mesh CrossSections")
  * **Components and segmentation:** [Merge](/Mesh_Merge "Mesh Merge"), [Split by Components](/Mesh_SplitComponents "Mesh SplitComponents"), [Segmentation](/Mesh_Segmentation "Mesh Segmentation"), [Segmentation From Best-Fit Surfaces](/Mesh_SegmentationBestFit "Mesh SegmentationBestFit")

* * *

  * **Analyze:** [Evaluate and Repair](/Mesh_Evaluation "Mesh Evaluation"), [Face Info](/Mesh_EvaluateFacet "Mesh EvaluateFacet"), [Curvature Plot](/Mesh_VertexCurvature "Mesh VertexCurvature"), [Curvature Info](/Mesh_CurvatureInfo "Mesh CurvatureInfo"), [Evaluate Solid](/Mesh_EvaluateSolid "Mesh EvaluateSolid"), [Bounding Box Info](/Mesh_BoundingBox "Mesh BoundingBox")
  * **Additional:** [Import Export Preferences](/Import_Export_Preferences "Import Export Preferences"), [OpenSCAD Workbench](/OpenSCAD_Workbench "OpenSCAD Workbench"), Mesh Scripting

