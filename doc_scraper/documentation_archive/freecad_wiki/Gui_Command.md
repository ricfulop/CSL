---
url: https://wiki.freecad.org/Gui_Command
title: Gui Command
scraped_at: 2025-09-08 16:41:51
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Naming
  * 2 Help page
  * 3 Icons Toggle Icons subsection
    * 3.1 Icons color coding chart

# Gui Command

  * [Page](/Gui_Command "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Gui_Command&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Gui_Command)
  * [Edit](/index.php?title=Gui_Command&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Gui_Command&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Gui_Command.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Gui_Command&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Gui_Command)
  * [Edit](/index.php?title=Gui_Command&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Gui_Command&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Gui_Command&action=history)

General

  * [What links here](/Special:WhatLinksHere/Gui_Command "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Gui_Command "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Gui_Command&oldid=1597823 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Gui_Command&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Gui_Command&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Gui+Command&action=page&filter=&language=en)This is the approved revision of
this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Gui+Command&language=&task=view "Start translation for this language")
  * [Deutsch](/Gui_Command/de "Gui Befehl \(100% translated\)")
  * English
  * [Türkçe](/Gui_Command/tr "Gui Command/tr \(6% translated\)")
  * [español](/Gui_Command/es "Gui Command \(6% translated\)")
  * [français](/Gui_Command/fr "Gui Command \(100% translated\)")
  * [italiano](/Gui_Command/it "Comandi dell'interfaccia grafica \(100% translated\)")
  * [polski](/Gui_Command/pl "Narzędzia w GUI \(100% translated\)")
  * [português](/Gui_Command/pt "Gui Command \(6% translated\)")
  * [português do Brasil](/Gui_Command/pt-br "Comandos de interface gráfica \(6% translated\)")
  * [română](/Gui_Command/ro "Gui Command \(19% translated\)")
  * [svenska](/Gui_Command/sv "Gui Command \(6% translated\)")
  * [čeština](/Gui_Command/cs "Gui Command \(6% translated\)")
  * [русский](/Gui_Command/ru "Gui Command \(25% translated\)")
  * [日本語](/Gui_Command/ja "GUIコマンド \(6% translated\)")

The GuiCommand is one of the most important functions of FreeCAD in the main
interaction point of the user. Every time the user selects a menu item or
presses a toolbar button it activates a GuiCommand. Some of the attributes of
a GuiCommand are:

  * Defines a name
  * Contains an icon
  * Defines the scope for an undo/redo
  * Has a help page
  * Opens and controls dialogs
  * Macro recording
  * and others.

## Naming

The GuiCommand is named in a standard way: _ModuleName_CommandName_ e.g.,
"[Base_Open](/index.php?title=Base_Open&action=edit&redlink=1 "Base Open
\(page does not exist\)")" this is the Open Gui Command in the Base system.
The GuiCommand in a certain module is named with the module name in front
e.g., "[Part_Cylinder](/Part_Cylinder "Part Cylinder")".

## Help page

Every GuiCommand has to have a help page. The help page is hosted on the
FreeCAD documentation wiki. The article has the same name as the GuiCommand,
e.g. [Draft ShapeString](/Draft_ShapeString "Draft ShapeString").

To create your own help pages you can use the template [GuiCommand
model](/GuiCommand_model "GuiCommand model").

Example:

  * [Draft ShapeString](/Draft_ShapeString "Draft ShapeString")
  * [Draft Line](/Draft_Line "Draft Line")

And as long as the documentation is not finished insert an
[UnfinishedDocu](/Template:UnfinishedDocu "Template:UnfinishedDocu") template
at the top of the help page.

## Icons

[![](/images/thumb/8/8a/Tango-Palette.png/400px-Tango-
Palette.png)](/index.php?title=File:Tango-
Palette.png&filetimestamp=20090202160503&)

Every GuiCommand has to have an icon. We use the [Tango icon
set](http://tango-project.org/Tango_Desktop_Project/) and its guidelines. On
the right side you see the tango color palette.

All icons should be created in [SVG](/SVG "SVG") format with a vector image
application, such as [Inkscape](http://inkscape.org). This makes it easier to
apply changes and derive additional icons in the same application space.

### Icons color coding chart

[![](/images/thumb/9/9b/Colorchart.png/200px-
Colorchart.png)](/index.php?title=File:Colorchart.png&filetimestamp=20100812154803&)

We try as much as possible to respect this chart, so the color of the icons
has a direct meaning.

  

Expand[![](/images/thumb/8/8f/Power_user_hub.png/24px-
Power_user_hub.png)](/index.php?title=File:Power_user_hub.png&filetimestamp=20200511213015&)
[Power user documentation](/Power_users_hub "Power users hub")

  * **FreeCAD scripting:** [Python](/Python "Python"), [Introduction to Python](/Introduction_to_Python "Introduction to Python"), [Python scripting tutorial](/Python_scripting_tutorial "Python scripting tutorial"), [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics")

* * *

  * **Modules:** [Builtin modules](/Builtin_modules "Builtin modules"), [Units](/Units "Units"), [Quantity](/Quantity "Quantity")
  * **Workbenches:** [Workbench creation](/Workbench_creation "Workbench creation"), Gui Commands, [Commands](/Command "Command"), [Installing more workbenches](/Installing_more_workbenches "Installing more workbenches")
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

