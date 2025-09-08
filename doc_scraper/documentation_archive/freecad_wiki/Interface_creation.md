---
url: https://wiki.freecad.org/Interface_creation
title: Interface creation
scraped_at: 2025-09-08 16:46:41
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Description Toggle Description subsection
    * 2.1 Interface in a .ui file
    * 2.2 Interface completely in Python code

# Interface creation

  * [Page](/Interface_creation "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Interface_creation&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Interface_creation)
  * [Edit](/index.php?title=Interface_creation&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Interface_creation&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Interface_creation.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Interface_creation&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Interface_creation)
  * [Edit](/index.php?title=Interface_creation&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Interface_creation&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Interface_creation&action=history)

General

  * [What links here](/Special:WhatLinksHere/Interface_creation "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Interface_creation "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Interface_creation&oldid=1068428 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Interface_creation&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Interface_creation&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Interface+creation&action=page&filter=&language=en)This is the approved
revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Interface+creation&language=&task=view "Start translation for this language")
  * [Deutsch](/Interface_creation/de "Schnittstellen erstellen \(100% translated\)")
  * English
  * [français](/Interface_creation/fr "Création d'interface \(100% translated\)")
  * [italiano](/Interface_creation/it "Creare l'interfaccia \(100% translated\)")
  * [polski](/Interface_creation/pl "Tworzenie interfejsu \(100% translated\)")
  * [português do Brasil](/Interface_creation/pt-br "Criação de diálogo \(7% translated\)")
  * [русский](/Interface_creation/ru "Разработка графического интерфейса \(64% translated\)")

![](/images/6/6f/Arrow-left.svg) [PySide](/PySide "PySide")

[Dialog creation](/Dialog_creation "Dialog creation") ![](/images/a/af/Arrow-
right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

## Introduction

Power users have the possibility of creating interfaces to help them produce
complex tools for their custom [addons](/Addon "Addon"), such as
[macros](/Macros "Macros") or full [workbenches](/Workbenches "Workbenches").

Interfaces are created using [PySide](/PySide "PySide"), which is a library
for using Qt with [Python](/Python "Python").

[![](/images/8/83/FreeCAD_creating_interfaces.svg)](/index.php?title=File:FreeCAD_creating_interfaces.svg&filetimestamp=20200514224916&)

Two general methods to create interfaces, by including the interface in the
Python file, or by using `.ui` files.

## Description

There are typically two ways of creating interfaces with PySide.

### Interface in a .ui file

In this method the interface is defined in a `.ui` file (an XML document that
defines the structure of the interface), which is then imported into
[Python](/Python "Python") code that uses it. This is the recommended
approach.

  * It allows the programmer to work with the graphical interface separately from the logic that will use it.
  * It allows anybody to look at the interface alone, that is, the `.ui` file, without having to run Python code.
  * The `.ui` file may be designed by anybody without programming knowledge.
  * The `.ui` interface can be used in a standalone window (modal), or in an embedded window (non-modal); therefore, this method is ideal to create custom [task panels](/Task_panel "Task panel").
  * Since the `.ui` file just describes the "appearance" of the interface, it does not need to be tied to a particular programming language; it may be used both in [Python](/Python "Python") and C++ code.

### Interface completely in Python code

In this method the entire interface is defined by several Python calls.

  * This is an older way of working with interfaces.
  * This method produces very verbose code because many details of the interface need to be specified by hand.
  * It is not simple to separate the interface from the logic that uses that code, meaning that a user would need to run the [Python](/Python "Python") file in the correct context in order to see how the interface would look.
  * This method has the advantage that several interfaces may be contained within a single document, at the expense of making the file very large.
  * This method is recommended only for small interfaces that don't define more than a few widgets, for example in [macros](/Macros "Macros").

For examples on this method see [Interface creation completely in
Python](/Dialog_creation "Dialog creation").

  

![](/images/6/6f/Arrow-left.svg) [PySide](/PySide "PySide")

[Dialog creation](/Dialog_creation "Dialog creation") ![](/images/a/af/Arrow-
right.svg)

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
  * **Graphical interface:** Interface creation, [Interface creation completely in Python](/Dialog_creation "Dialog creation") ([1](/Dialog_creation_with_various_widgets "Dialog creation with various widgets"), [2](/Dialog_creation_reading_and_writing_files "Dialog creation reading and writing files"), [3](/Dialog_creation_setting_colors "Dialog creation setting colors"), [4](/Dialog_creation_image_and_animated_GIF "Dialog creation image and animated GIF"), [5](/PySide_usage_snippets "PySide usage snippets")), [PySide](/PySide "PySide"), PySide examples [beginner](/PySide_Beginner_Examples "PySide Beginner Examples"), [intermediate](/PySide_Intermediate_Examples "PySide Intermediate Examples"), [advanced](/PySide_Advanced_Examples "PySide Advanced Examples")
  * **Macros:** [Macros](/Macros "Macros"), [How to install macros](/How_to_install_macros "How to install macros")
  * **Embedding:** [Embedding FreeCAD](/Embedding_FreeCAD "Embedding FreeCAD"), [Embedding FreeCADGui](/Embedding_FreeCADGui "Embedding FreeCADGui")

* * *

  * **Other:** [Expressions](/Expressions "Expressions"), [Code snippets](/Code_snippets "Code snippets"), [Line drawing function](/Line_drawing_function "Line drawing function"), [FreeCAD vector math library](/FreeCAD_vector_math_library "FreeCAD vector math library") (deprecated)

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

