---
url: https://wiki.freecad.org/Installing_more_workbenches
title: Installing more workbenches
scraped_at: 2025-09-08 16:46:11
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 General description
  * 3 Installing system-wide
  * 4 Installing for a single user
  * 5 Additional information

# Installing more workbenches

  * [Page](/Installing_more_workbenches "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Installing_more_workbenches&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Installing_more_workbenches)
  * [Edit](/index.php?title=Installing_more_workbenches&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Installing_more_workbenches&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Installing_more_workbenches.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Installing_more_workbenches&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Installing_more_workbenches)
  * [Edit](/index.php?title=Installing_more_workbenches&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Installing_more_workbenches&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Installing_more_workbenches&action=history)

General

  * [What links here](/Special:WhatLinksHere/Installing_more_workbenches "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Installing_more_workbenches "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Installing_more_workbenches&oldid=1616651 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Installing_more_workbenches&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Installing_more_workbenches&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Installing+more+workbenches&action=page&filter=&language=en)This is the
approved revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Installing+more+workbenches&language=&task=view "Start translation for this language")
  * [Deutsch](/Installing_more_workbenches/de "Weitere Arbeitsbereiche installieren \(100% translated\)")
  * English
  * [Türkçe](/Installing_more_workbenches/tr "Installing more workbenches/tr \(6% translated\)")
  * [español](/Installing_more_workbenches/es "Instalación de más ambientes de trabajo \(88% translated\)")
  * [français](/Installing_more_workbenches/fr "Installer des ateliers supplémentaires \(100% translated\)")
  * [italiano](/Installing_more_workbenches/it "Installare ulteriori ambienti di lavoro \(100% translated\)")
  * [polski](/Installing_more_workbenches/pl "Instalacja zewnętrznych środowisk pracy \(100% translated\)")
  * [română](/Installing_more_workbenches/ro "Installing more workbenches/ro \(6% translated\)")
  * [svenska](/Installing_more_workbenches/sv "Installing more workbenches \(6% translated\)")
  * [русский](/Installing_more_workbenches/ru "Установка дополнительных верстаков \(47% translated\)")
  * [日本語](/Installing_more_workbenches/ja "ワークベンチのインストール方法 \(12% translated\)")

## Introduction

Since v0.17 it is easy to add [external workbenches](/External_workbenches
"External workbenches") by using the [Addon Manager](/Std_AddonMgr "Std
AddonMgr"). A regular user doesn't need to do more than use this tool.

Keep reading for more information regarding installation of workbenches.

## General description

Workbenches are nothing more than collections of files that are placed in a
folder. This folder is usually compressed into a zip archive. On installation,
this folder is simply uncompressed and copied to

    
    
    $ROOT_DIR/Mod/
    

where `$ROOT_DIR` is a top level directory searched by FreeCAD on startup.
This is essentially what the [Addon Manager](/Std_AddonMgr "Std AddonMgr")
does.

The `Mod/` directories are scanned every time FreeCAD is started, and the
available workbenches are automatically added.

## Installing system-wide

Workbenches installed in this way will be available to all users. Depending on
your system, you might need administrator privileges to access the
installation directory.

Copy the workbench folder into `$INSTALL_DIR/Mod/`, where `$INSTALL_DIR` is
the FreeCAD installation directory.

  * On Linux it is usually `/usr/share/freecad/Mod/`
    * For snap versions (for instance on Ubuntu) it is `$HOME/snap/freecad/common/Mod/`
  * On Windows it is usually `C:\Program Files\FreeCAD\Mod\`
  * On macOS it is usually `/Applications/FreeCAD/Mod/`

## Installing for a single user

Workbenches installed in this way will be available only to one user, but will
not require any administrator privileges.

Copy the workbench folder into `$USER_DIR/Mod/`, where `$USER_DIR` is the
FreeCAD directory for a particular `username` (you can find the latter by
typing `App.getUserAppDataDir()` in the [Python console](/Python_console
"Python console")).

  * On Linux it is usually `/home/username/.local/share/FreeCAD/Mod/`
  * On Windows it is `%APPDATA%\FreeCAD\Mod\`, which is usually `C:\Users\username\Appdata\Roaming\FreeCAD\Mod\`
  * On macOS it is usually `/Users/username/Library/Application Support/FreeCAD/Mod/`.

## Additional information

Additional information on how to create a custom workbench can be found in the
[Power users hub](/Power_users_hub "Power users hub") and the [Developer
hub](/Developer_hub "Developer hub").

See also a detailed description in the page [how to install additional
workbenches](/How_to_install_additional_workbenches "How to install additional
workbenches").

  

Expand[![](/images/thumb/8/8f/Power_user_hub.png/24px-
Power_user_hub.png)](/index.php?title=File:Power_user_hub.png&filetimestamp=20200511213015&)
[Power user documentation](/Power_users_hub "Power users hub")

  * **FreeCAD scripting:** [Python](/Python "Python"), [Introduction to Python](/Introduction_to_Python "Introduction to Python"), [Python scripting tutorial](/Python_scripting_tutorial "Python scripting tutorial"), [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics")

* * *

  * **Modules:** [Builtin modules](/Builtin_modules "Builtin modules"), [Units](/Units "Units"), [Quantity](/Quantity "Quantity")
  * **Workbenches:** [Workbench creation](/Workbench_creation "Workbench creation"), [Gui Commands](/Gui_Command "Gui Command"), [Commands](/Command "Command"), Installing more workbenches
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

