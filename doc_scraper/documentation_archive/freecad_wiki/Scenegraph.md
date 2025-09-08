---
url: https://wiki.freecad.org/Scenegraph
title: Scenegraph
scraped_at: 2025-09-08 16:42:40
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Description
  * 3 Coding examples

# Scenegraph

  * [Page](/Scenegraph "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Scenegraph&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Scenegraph)
  * [Edit](/index.php?title=Scenegraph&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Scenegraph&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Scenegraph.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Scenegraph&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Scenegraph)
  * [Edit](/index.php?title=Scenegraph&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Scenegraph&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Scenegraph&action=history)

General

  * [What links here](/Special:WhatLinksHere/Scenegraph "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Scenegraph "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Scenegraph&oldid=1207142 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Scenegraph&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Scenegraph&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Scenegraph&action=page&filter=&language=en)This is the approved revision of
this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Scenegraph&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/Scenegraph/id "Scenegraph \(5% translated\)")
  * [Deutsch](/Scenegraph/de "Szenengraph \(100% translated\)")
  * English
  * [Türkçe](/Scenegraph/tr "Scenegraph \(5% translated\)")
  * [español](/Scenegraph/es "Scenegraph \(5% translated\)")
  * [français](/Scenegraph/fr "Graphe de scène \(100% translated\)")
  * [italiano](/Scenegraph/it "Grafo della Scena \(100% translated\)")
  * [polski](/Scenegraph/pl "Scenogram \(100% translated\)")
  * [português](/Scenegraph/pt "Scenegraph \(5% translated\)")
  * [português do Brasil](/Scenegraph/pt-br "Grafo de cena \(10% translated\)")
  * [română](/Scenegraph/ro "Descrierea scenelor 3D \(5% translated\)")
  * [svenska](/Scenegraph/sv "Scenegraph \(5% translated\)")
  * [čeština](/Scenegraph/cs "Scenegraph/cs \(0% translated\)")
  * [русский](/Scenegraph/ru "Граф сцены \(35% translated\)")

![](/images/6/6f/Arrow-left.svg) [Scripted objects](/Scripted_objects
"Scripted objects")

[Pivy](/Pivy "Pivy") ![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

## Introduction

The geometry that appears in the [3D views](/3D_view "3D view") of FreeCAD is
rendered by the [Coin3D](https://en.wikipedia.org/wiki/Coin3D) library. Coin3D
is an implementation of the [Open
Inventor](https://en.wikipedia.org/wiki/Open_Inventor) standard. The
[OpenCASCADE](https://en.wikipedia.org/wiki/Open_Cascade_Technology) software
also provides the same functionality, but it was decided at the very early
stages of FreeCAD not to use the built-in OpenCASCADE viewer, but rather
switch to the more performant Coin3D software. A good way to learn about that
library is the book [Open Inventor Mentor](http://www-
evasion.imag.fr/Membres/Francois.Faure/doc/inventorMentor/sgi_html/).

## Description

[Open Inventor](https://en.wikipedia.org/wiki/Open_Inventor) is a 3D scene
description language. The scene described in Open Inventor is then rendered in
OpenGL on your screen. Coin3D takes care of doing this, so programmers do not
need to deal with complex OpenGL calls, and may just provide valid Open
Inventor code. The big advantage is that Open Inventor is a very well-known
and well documented standard.

One of the big jobs FreeCAD does for you is translating OpenCASCADE geometry
information into Open Inventor language.

Open Inventor describes a 3D scene in the form of a [scene
graph](https://en.wikipedia.org/wiki/Scene_graph), like the one below:

[![](/images/b/b7/Scenegraph.gif)](/index.php?title=File:Scenegraph.gif&filetimestamp=20200530144446&)

Image taken from [Inventor
mentor](https://web.archive.org/web/20190807185912/http://www-
evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/)

An Open Inventor scenegraph describes everything that is part of a 3D scene,
such as geometry, colors, materials, lights, etc, and organizes all that data
in a convenient and clear structure. Everything can be grouped into sub-
structures, allowing you to organize your scene contents pretty much the way
you like. Here is an example of an Open Inventor file:

    
    
    #Inventor V2.0 ascii
     
    Separator { 
        RotationXYZ {	
           axis Z
           angle 0
        }
        Transform {
           translation 0 0 0.5
        }
        Separator {	
           Material {
              diffuseColor 0.05 0.05 0.05
           }
           Transform {
              rotation 1 0 0 1.5708
              scaleFactor 0.2 0.5 0.2
           }
           Cylinder {
           }
        }
    }
    

As you can see, the structure is very simple. You use separators to organize
your data into blocks, a bit like you would organize your files into folders.
Each statement affects what comes next, for example the first two items of our
root separator are a rotation and a translation, both will affect the next
item, which is a separator. In that separator a material is defined and
another transformation. Our cylinder will therefore be affected by both
transformations, the one applied directly to it and the one that was applied
to its parent separator.

We also have many other types of elements to organize our scene, such as
groups, switches or annotations. We can define very complex materials for our
objects, with colors, textures, shading modes and transparency. We can also
define lights, cameras, and even movement. It is even possible to embed pieces
of scripting in Open Inventor files to define more complex behaviors.

If you are interested in learning more about Open Inventor head directly to
its most famous reference: the [Inventor mentor](http://www-
evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/).

In FreeCAD, normally, we don't need to interact directly with the Open
Inventor scenegraph. Every object in a FreeCAD document, being a mesh, a part
shape or anything else, gets automatically converted to Open Inventor code and
inserted in the main scenegraph that you see in a [3D view](/3D_view "3D
view"). That scenegraph gets updated continuously when you modify, add or
remove objects. In fact every object (in App space) has a view provider (a
corresponding object in Gui space) responsible for issuing Open Inventor code.

But there are many advantages to being able to access the scenegraph directly.
For example, we can temporarily change the appearance of an object, or we can
add objects to the scene that have no real existence in the FreeCAD document,
such as construction geometry, helpers, graphical hints or tools such as
manipulators or on-screen information.

FreeCAD itself features several tools to see or modify Open Inventor code. For
example, the following Python code will show the Open Inventor representation
of a selected object:

    
    
    obj = FreeCAD.ActiveDocument.ActiveObject
    viewprovider = obj.ViewObject
    print viewprovider.toString()
    

But we also have a Python module that allows complete access to anything
managed by Coin3D, such as our FreeCAD scenegraph. So, read on to [Pivy](/Pivy
"Pivy").

## Coding examples

See [Coin3d snippets](/Coin3d_snippets "Coin3d snippets") courtesy of
MariwanJ's research for the [Design456 Workbench](/Design456_Workbench
"Design456 Workbench"). The code repository can be found at
<https://github.com/MariwanJ/COIN3D_Snippet>.

Top

![](/images/6/6f/Arrow-left.svg) [Scripted objects](/Scripted_objects
"Scripted objects")

[Pivy](/Pivy "Pivy") ![](/images/a/af/Arrow-right.svg)

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
  * **Scenegraph:** Coin (Inventor) scenegraph, [Pivy](/Pivy "Pivy")
  * **Graphical interface:** [Interface creation](/Interface_creation "Interface creation"), [Interface creation completely in Python](/Dialog_creation "Dialog creation") ([1](/Dialog_creation_with_various_widgets "Dialog creation with various widgets"), [2](/Dialog_creation_reading_and_writing_files "Dialog creation reading and writing files"), [3](/Dialog_creation_setting_colors "Dialog creation setting colors"), [4](/Dialog_creation_image_and_animated_GIF "Dialog creation image and animated GIF"), [5](/PySide_usage_snippets "PySide usage snippets")), [PySide](/PySide "PySide"), PySide examples [beginner](/PySide_Beginner_Examples "PySide Beginner Examples"), [intermediate](/PySide_Intermediate_Examples "PySide Intermediate Examples"), [advanced](/PySide_Advanced_Examples "PySide Advanced Examples")
  * **Macros:** [Macros](/Macros "Macros"), [How to install macros](/How_to_install_macros "How to install macros")
  * **Embedding:** [Embedding FreeCAD](/Embedding_FreeCAD "Embedding FreeCAD"), [Embedding FreeCADGui](/Embedding_FreeCADGui "Embedding FreeCADGui")

* * *

  * **Other:** [Expressions](/Expressions "Expressions"), [Code snippets](/Code_snippets "Code snippets"), [Line drawing function](/Line_drawing_function "Line drawing function"), [FreeCAD vector math library](/FreeCAD_vector_math_library "FreeCAD vector math library") (deprecated)

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

