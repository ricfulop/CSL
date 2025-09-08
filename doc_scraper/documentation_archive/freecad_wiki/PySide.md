---
url: https://wiki.freecad.org/PySide
title: PySide
scraped_at: 2025-09-08 16:41:48
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 PySide in FreeCAD with Qt5
  * 3 Examples of PySide use
  * 4 Documentation

# PySide

  * [Page](/PySide "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:PySide&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/PySide)
  * [Edit](/index.php?title=PySide&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=PySide&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/PySide.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=PySide&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/PySide)
  * [Edit](/index.php?title=PySide&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=PySide&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=PySide&action=history)

General

  * [What links here](/Special:WhatLinksHere/PySide "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/PySide "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=PySide&oldid=1392731 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=PySide&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=PySide&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
PySide&action=page&filter=&language=en)This is the approved revision of this
page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-PySide&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/PySide/id "PySide \(5% translated\)")
  * [Deutsch](/PySide/de "PySide \(100% translated\)")
  * English
  * [Türkçe](/PySide/tr "PySide \(5% translated\)")
  * [español](/PySide/es "PySide \(5% translated\)")
  * [français](/PySide/fr "PySide \(100% translated\)")
  * [italiano](/PySide/it "PySide \(100% translated\)")
  * [polski](/PySide/pl "PySide \(5% translated\)")
  * [português](/PySide/pt "PySide \(5% translated\)")
  * [português do Brasil](/PySide/pt-br "PySide \(9% translated\)")
  * [română](/PySide/ro "PySide \(5% translated\)")
  * [svenska](/PySide/sv "PySide \(5% translated\)")
  * [čeština](/PySide/cs "PySide \(5% translated\)")
  * [русский](/PySide/ru "PySide \(59% translated\)")
  * [日本語](/PySide/ja "PySide/ja \(41% translated\)")

![](/images/6/6f/Arrow-left.svg) [Pivy](/Pivy "Pivy")

[Interface creation](/Interface_creation "Interface creation")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

## Introduction

The PySide library gives access to the cross-platform graphical user interface
(GUI) toolkit Qt from [Python](/Python "Python"). Qt is a collection of C++
libraries, but with the help of PySide, the same components can be used from
[Python](/Python "Python"). Every graphical interface that can be created in
C++, can also be created and modified in Python. An advantage of using Python
is that Qt interfaces can be developed and tested live, as we don't need to
compile the source files.

When you install FreeCAD, you should get both Qt and PySide as part of the
package. If you are [compiling](/Compiling "Compiling") yourself then you must
verify that these two libraries are installed in order for FreeCAD to run
correctly. Of course, PySide will only work if Qt is present.

In the past, FreeCAD used PyQt, another Qt binding for Python, but in 2013
([commit 1dc122dc9a](https://github.com/FreeCAD/FreeCAD/commit/1dc122dc9a))
the project migrated to PySide because it has a more permissible
[License](/License "License").

For more information see:

  * [Wikipedia:PySide](https://en.wikipedia.org/wiki/PySide)
  * [Differences Between PySide and PyQt](https://wiki.qt.io/Differences_Between_PySide_and_PyQt)

[![](/images/8/85/PySideScreenSnapshot1.jpg)](/index.php?title=File:PySideScreenSnapshot1.jpg&filetimestamp=20150206153902&)
[![](/images/8/8f/PySideScreenSnapshot2.jpg)](/index.php?title=File:PySideScreenSnapshot2.jpg&filetimestamp=20150207063525&)

Examples created with PySide. Left: a simple dialog. Right: a more complex
dialog with graphs.

## PySide in FreeCAD with Qt5

FreeCAD was developed to be used with Python 2 and Qt4. As these two libraries
became obsolete, FreeCAD transitioned to Python 3 and Qt5. In most cases this
transition was done without needing to break backwards compatibility.

Normally, the `PySide` module provides support for Qt4, while `PySide2`
provides support for Qt5. However, in FreeCAD there is no need to use
`PySide2` directly, as a special `PySide` module is included to handle Qt5.

This `PySide` module is located in the `Ext/` directory of an installation of
FreeCAD compiled for Qt5.

    
    
    /usr/share/freecad/Ext/PySide
    

This module just imports the necessary classes from `PySide2`, and places them
in the `PySide` namespace. This means that in most cases the same code can be
used with both Qt4 and Qt5, as long as we use the single `PySide` module.

    
    
    PySide2.QtCore -> PySide.QtCore
    PySide2.QtGui -> PySide.QtGui
    PySide2.QtSvg -> PySide.QtSvg
    PySide2.QtUiTools -> PySide.QtUiTools
    

The only unusual aspect is that the `PySide2.QtWidgets` classes are placed in
the `PySide.QtGui` namespace.

    
    
    PySide2.QtWidgets.QCheckBox -> PySide.QtGui.QCheckBox
    

Top

## Examples of PySide use

  * [PySide Beginner Examples](/PySide_Beginner_Examples "PySide Beginner Examples"), hello world, announcements, enter text, enter number.
  * [PySide Intermediate Examples](/PySide_Intermediate_Examples "PySide Intermediate Examples"), window sizing, hiding widgets, popup menus, mouse position, mouse events.
  * [PySide Advanced Examples](/PySide_Advanced_Examples "PySide Advanced Examples"), many widgets.

The examples of PySide are divided into 3 parts, differentiated by level of
exposure to PySide, Python and the FreeCAD internals. The first page has an
overview on PySide; the second and third pages are mostly code examples at
different levels.

It is expected that these examples are useful to get started, and afterwards
the user can consult other resources online, or the official documentation.

Top

## Documentation

There are some differences in handling of widgets in Qt4 (PySide) and Qt5
(PySide2). The programmer should be aware of these incompatibilities, and
should consult the official documentation if something doesn't seem to work as
expected on a given platform. Nevertheless, Qt4 is considered obsolete, so
most development should target Qt5 and Python 3.

The PySide documentation refers to the Python-style classes; however, since Qt
is originally a C++ library, the same information should be available in the
corresponding C++ reference.

  * [Qt Modules](https://doc.qt.io/qtforpython/modules.html) available from PySide2 (Qt5).
  * [All Qt classes by module](https://doc.qt.io/qt-5/modules-cpp.html) in Qt5 for C++.
  * [Qt Modules](https://deptinfo-ensip.univ-poitiers.fr/ENS/pyside-docs/index.html) available from PySide (Qt4).

Top

![](/images/6/6f/Arrow-left.svg) [Pivy](/Pivy "Pivy")

[Interface creation](/Interface_creation "Interface creation")
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
  * **Meshes and Parts:** [Mesh Scripting](/Mesh_Scripting "Mesh Scripting"), [Topological data scripting](/Topological_data_scripting "Topological data scripting"), [Mesh to Part](/Mesh_to_Part "Mesh to Part"), [PythonOCC](/PythonOCC "PythonOCC")

* * *

  * **Parametric objects:** [Scripted objects](/Scripted_objects "Scripted objects"), [Viewproviders](/Viewprovider "Viewprovider") ([Custom icon in tree view](/Custom_icon_in_tree_view "Custom icon in tree view"))
  * **Scenegraph:** [Coin (Inventor) scenegraph](/Scenegraph "Scenegraph"), [Pivy](/Pivy "Pivy")
  * **Graphical interface:** [Interface creation](/Interface_creation "Interface creation"), [Interface creation completely in Python](/Dialog_creation "Dialog creation") ([1](/Dialog_creation_with_various_widgets "Dialog creation with various widgets"), [2](/Dialog_creation_reading_and_writing_files "Dialog creation reading and writing files"), [3](/Dialog_creation_setting_colors "Dialog creation setting colors"), [4](/Dialog_creation_image_and_animated_GIF "Dialog creation image and animated GIF"), [5](/PySide_usage_snippets "PySide usage snippets")), PySide, PySide examples [beginner](/PySide_Beginner_Examples "PySide Beginner Examples"), [intermediate](/PySide_Intermediate_Examples "PySide Intermediate Examples"), [advanced](/PySide_Advanced_Examples "PySide Advanced Examples")
  * **Macros:** [Macros](/Macros "Macros"), [How to install macros](/How_to_install_macros "How to install macros")
  * **Embedding:** [Embedding FreeCAD](/Embedding_FreeCAD "Embedding FreeCAD"), [Embedding FreeCADGui](/Embedding_FreeCADGui "Embedding FreeCADGui")

* * *

  * **Other:** [Expressions](/Expressions "Expressions"), [Code snippets](/Code_snippets "Code snippets"), [Line drawing function](/Line_drawing_function "Line drawing function"), [FreeCAD vector math library](/FreeCAD_vector_math_library "FreeCAD vector math library") (deprecated)

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

