---
url: https://wiki.freecad.org/Mesh_to_Part
title: Mesh to Part
scraped_at: 2025-09-08 16:46:17
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Convert Part objects to meshes
  * 2 Convert meshes to Part objects

# Mesh to Part

  * [Page](/Mesh_to_Part "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Mesh_to_Part&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Mesh_to_Part)
  * [Edit](/index.php?title=Mesh_to_Part&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Mesh_to_Part&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Mesh_to_Part.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Mesh_to_Part&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Mesh_to_Part)
  * [Edit](/index.php?title=Mesh_to_Part&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Mesh_to_Part&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Mesh_to_Part&action=history)

General

  * [What links here](/Special:WhatLinksHere/Mesh_to_Part "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Mesh_to_Part "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Mesh_to_Part&oldid=974325 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Mesh_to_Part&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Mesh_to_Part&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Mesh+to+Part&action=page&filter=&language=en)This is the approved revision of
this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Mesh+to+Part&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/Mesh_to_Part/id "Mesh to Part \(11% translated\)")
  * [Deutsch](/Mesh_to_Part/de "Polygonnetz zu Teil \(100% translated\)")
  * English
  * [Türkçe](/Mesh_to_Part/tr "Mesh to Part \(11% translated\)")
  * [español](/Mesh_to_Part/es "Mesh to Part \(11% translated\)")
  * [français](/Mesh_to_Part/fr "Conversion objet Mesh en Part \(100% translated\)")
  * [italiano](/Mesh_to_Part/it "Da Mesh a Parte e viceversa \(100% translated\)")
  * [polski](/Mesh_to_Part/pl "Konwersja Siatki na Część \(100% translated\)")
  * [română](/Mesh_to_Part/ro "Piese construite din Plase poligonale \(11% translated\)")
  * [svenska](/Mesh_to_Part/sv "Mesh to Part \(11% translated\)")
  * [čeština](/Mesh_to_Part/cs "Mesh to Part \(11% translated\)")
  * [русский](/Mesh_to_Part/ru "Mesh to Part \(89% translated\)")
  * [日本語](/Mesh_to_Part/ja "Mesh to Part/ja \(0% translated\)")

## Convert Part objects to meshes

Converting higher-level objects such as [Part](/Part_Workbench "Part
Workbench") shapes to simpler objects such as [meshes](/Mesh_Workbench "Mesh
Workbench") is a pretty straightforward operation where all faces of a Part
object get triangulated. The result of that triangulation (tessellation) is
then used to construct a mesh:

    
    
    import Mesh
    
    obj = FreeCADGui.Selection.getSelection()[0] # a Part object must be preselected
    shp = obj.Shape
    faces = []
    
    triangles = shp.tessellate(1) # the number represents the precision of the tessellation
    for tri in triangles[1]:
        face = []
        for i in tri:
            face.append(triangles[0][i])
        faces.append(face)
    
    m = Mesh.Mesh(faces)
    Mesh.show(m)
    

Alternative example:

    
    
    import Mesh
    import MeshPart
    
    obj = FreeCADGui.Selection.getSelection()[0] # a Part object must be preselected
    shp = obj.Shape
    
    mesh = FreeCAD.ActiveDocument.addObject("Mesh::Feature", "Mesh")
    mesh.Mesh = MeshPart.meshFromShape(
            Shape=shp,
            LinearDeflection=0.01,
            AngularDeflection=0.025,
            Relative=False)
    

## Convert meshes to Part objects

Converting meshes to Part objects is a common operation. Very often you will
receive 3D data in a mesh format. Meshes are quite practical for representing
free-form geometry and big visual scenes, as they are very lightweight. But in
FreeCAD we generally prefer higher-level objects, solids, that can carry much
more information and allow for curved faces.

Converting meshes to those higher-level objects (handled by the [Part
Workbench](/Part_Workbench "Part Workbench") in FreeCAD) is not an easy
operation. Meshes can contain thousands of triangles (for example when
generated by a 3D scanner), and solids made of the same number of faces would
be extremely difficult to manipulate. So you generally want to optimize the
object when converting.

FreeCAD currently offers two methods to convert meshes to Part objects. The
first method is a simple, direct conversion without any optimization:

    
    
    import Mesh
    import Part
    
    mesh = Mesh.createTorus()
    shape = Part.Shape()
    shape.makeShapeFromMesh(mesh.Topology, 0.05) # the second arg is the tolerance for sewing
    solid = Part.makeSolid(shape)
    Part.show(solid)
    

The second method offers the possibility to consider mesh facets co-planar
when the angle between them is under a certain value, reducing the number of
faces in the final result:

    
    
    import Mesh
    import Part
    import MeshPart
    
    obj = FreeCADGui.Selection.getSelection()[0] # a Mesh object must be preselected
    mesh = obj.Mesh
    segments = mesh.getPlanarSegments(0.00001) # use rather strict tolerance here
    faces = []
    
    for i in segments:
        if len(i) > 0:
            # a segment can have inner holes
            wires = MeshPart.wireFromSegment(mesh, i)
            # we assume that the exterior boundary is that one with the biggest bounding box
            if len(wires) > 0:
                ext = None
                max_length=0
                for i in wires:
                    if i.BoundBox.DiagonalLength > max_length:
                        max_length = i.BoundBox.DiagonalLength
                        ext = i
    
                wires.remove(ext)
                # all interior wires mark a hole and must reverse their orientation, otherwise Part.Face fails
                for i in wires:
                    i.reverse()
    
                # make sure that the exterior wires comes as first in the list
                wires.insert(0, ext)
                faces.append(Part.Face(wires))
    
    solid = Part.Solid(Part.Shell(faces))
    Part.show(solid)
    

  

Expand[![](/images/thumb/8/8f/Power_user_hub.png/24px-
Power_user_hub.png)](/index.php?title=File:Power_user_hub.png&filetimestamp=20200511213015&)
[Power user documentation](/Power_users_hub "Power users hub")

  * **FreeCAD scripting:** [Python](/Python "Python"), [Introduction to Python](/Introduction_to_Python "Introduction to Python"), [Python scripting tutorial](/Python_scripting_tutorial "Python scripting tutorial"), [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics")

* * *

  * **Modules:** [Builtin modules](/Builtin_modules "Builtin modules"), [Units](/Units "Units"), [Quantity](/Quantity "Quantity")
  * **Workbenches:** [Workbench creation](/Workbench_creation "Workbench creation"), [Gui Commands](/Gui_Command "Gui Command"), [Commands](/Command "Command"), [Installing more workbenches](/Installing_more_workbenches "Installing more workbenches")
  * **Meshes and Parts:** [Mesh Scripting](/Mesh_Scripting "Mesh Scripting"), [Topological data scripting](/Topological_data_scripting "Topological data scripting"), Mesh to Part, [PythonOCC](/PythonOCC "PythonOCC")

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
  * **Additional:** [Import Export Preferences](/Import_Export_Preferences "Import Export Preferences"), [OpenSCAD Workbench](/OpenSCAD_Workbench "OpenSCAD Workbench"), [Mesh Scripting](/Mesh_Scripting "Mesh Scripting")

