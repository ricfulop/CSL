---
url: https://wiki.freecad.org/PythonOCC
title: PythonOCC
scraped_at: 2025-09-08 16:46:14
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Description
  * 2 Usage
  * 3 Installation
  * 4 Compilation
  * 5 More information

# PythonOCC

  * [Page](/PythonOCC "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:PythonOCC&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/PythonOCC)
  * [Edit](/index.php?title=PythonOCC&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=PythonOCC&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/PythonOCC.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=PythonOCC&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/PythonOCC)
  * [Edit](/index.php?title=PythonOCC&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=PythonOCC&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=PythonOCC&action=history)

General

  * [What links here](/Special:WhatLinksHere/PythonOCC "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/PythonOCC "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=PythonOCC&oldid=1601587 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=PythonOCC&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=PythonOCC&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
PythonOCC&action=page&filter=&language=en)This is the approved revision of
this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-PythonOCC&language=&task=view "Start translation for this language")
  * [Deutsch](/PythonOCC/de "PythonOCC \(100% translated\)")
  * English
  * [Türkçe](/PythonOCC/tr "PythonOCC/tr \(6% translated\)")
  * [español](/PythonOCC/es "PythonOCC \(62% translated\)")
  * [français](/PythonOCC/fr "PythonOCC \(100% translated\)")
  * [italiano](/PythonOCC/it "PythonOCC \(6% translated\)")
  * [polski](/PythonOCC/pl "Środowisko PythonOCC \(100% translated\)")
  * [română](/PythonOCC/ro "PythonOCC/ro \(6% translated\)")
  * [svenska](/PythonOCC/sv "PythonOCC \(6% translated\)")
  * [čeština](/PythonOCC/cs "PythonOCC \(6% translated\)")
  * [русский](/PythonOCC/ru "PythonOCC/ru \(0% translated\)")

## Description

PythonOCC is a project that aims at providing the entire range of [OpenCASCADE
Technology](/OpenCASCADE "OpenCASCADE") (OCCT) functions through the
[Python](/Python "Python") module `OCC`. This is a different approach from
FreeCAD's, where only certain components of OCCT are exposed through the [Part
Workbench](/Part_Workbench "Part Workbench").

PythonOCC, on the other hand, provides access to all OCCT classes and
functions so it is complex but also very powerful. Therefore, when you are
limited by FreeCAD's OCCT functionality, using `OCC` is a good alternative.

## Usage

The [Part Workbench](/Part_Workbench "Part Workbench") has the methods
`Part.__toPythonOCC__()` and `Part.__fromPythonOCC__()` to exchange
`TopoDS_Shape` ([Part TopoShape](/Part_TopoShape "Part TopoShape")) entities
to and from PythonOCC. These methods allow us to use the full power of OCCT in
Python and then put the resulting shapes back into FreeCAD objects.

PythonOCC is internally used by the [IFC](/Arch_IFC "Arch IFC") viewer
included with the [IfcOpenShell](/IfcOpenShell "IfcOpenShell") libraries.
IfcOpenShell is used to read and write [IFC](/Arch_IFC "Arch IFC") documents
with FreeCAD. PythonOCC is only needed to launch IfcOpenShell's integrated
viewer, otherwise it is not necessary.

## Installation

PythonOCC must be compiled from source. For this you need to get the
corresponding development files for [OpenCASCADE Technology](/OpenCASCADE
"OpenCASCADE") (OCCT) and SWIG. The older version of PythonOCC was intended to
wrap around OCE 0.18, the community edition of OCCT 6.9.x, which is now
unmaintained. The newest version of PythonOCC is now intended to work with the
recent, official OCCT 7.4 version.

Together with OCCT 7.4, PythonOCC requires fairly recent dependencies like
Python 3.7, CMake 3.12, and SWIG 3.0.11. Python 2 is no longer supported.

It is also possible to install pre-compiled PythonOCC libraries using
[Conda](/Conda "Conda"). For more information and compilation instructions,
see the main project's repository, [tpaviot/pythonocc-
core](https://github.com/tpaviot/pythonocc-core).

## Compilation

You can also self compile pythonOCC (see
[instructions](https://github.com/tpaviot/pythonocc-
core/blob/master/INSTALL.md)). Below is the procedure for Debian/Ubuntu using
distro-provided opencascade packages:

    
    
    git clone git://github.com/tpaviot/pythonocc-core.git pythonocc
    cd pythonocc
    mkdir build
    cd build
    cmake -DOCE_INCLUDE_PATH=/usr/include/opencascade -DOCE_LIB_PATH=/usr/lib/x86_64-linux-gnu ..
    make
    

## More information

  * Project page: [pythonocc.org](http://www.pythonocc.org/)
  * Newer version compatible with OCCT 7.4, [tpaviot/pythonocc-core](https://github.com/tpaviot/pythonocc-core).
  * Older version compatible with OCE 0.18, the community edition of OCCT 6.9.x, [tpaviot/pythonocc](https://github.com/tpaviot/pythonocc).
  * [IfcPlusPlus compiled on Gentoo - questions and alternatives?](https://forum.freecad.org/viewtopic.php?f=39&t=33254)

Expand[![](/images/thumb/8/8f/Power_user_hub.png/24px-
Power_user_hub.png)](/index.php?title=File:Power_user_hub.png&filetimestamp=20200511213015&)
[Power user documentation](/Power_users_hub "Power users hub")

  * **FreeCAD scripting:** [Python](/Python "Python"), [Introduction to Python](/Introduction_to_Python "Introduction to Python"), [Python scripting tutorial](/Python_scripting_tutorial "Python scripting tutorial"), [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics")

* * *

  * **Modules:** [Builtin modules](/Builtin_modules "Builtin modules"), [Units](/Units "Units"), [Quantity](/Quantity "Quantity")
  * **Workbenches:** [Workbench creation](/Workbench_creation "Workbench creation"), [Gui Commands](/Gui_Command "Gui Command"), [Commands](/Command "Command"), [Installing more workbenches](/Installing_more_workbenches "Installing more workbenches")
  * **Meshes and Parts:** [Mesh Scripting](/Mesh_Scripting "Mesh Scripting"), [Topological data scripting](/Topological_data_scripting "Topological data scripting"), [Mesh to Part](/Mesh_to_Part "Mesh to Part"), PythonOCC

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

