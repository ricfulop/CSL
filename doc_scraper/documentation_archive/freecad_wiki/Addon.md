---
url: https://wiki.freecad.org/Addon
title: Addon
scraped_at: 2025-09-08 16:46:00
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Different types
  * 3 Installation
  * 4 Information for developers

# Addon

  * [Page](/Addon "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Addon&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Addon)
  * [Edit](/index.php?title=Addon&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Addon&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Addon.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Addon&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Addon)
  * [Edit](/index.php?title=Addon&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Addon&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Addon&action=history)

General

  * [What links here](/Special:WhatLinksHere/Addon "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Addon "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Addon&oldid=1597778 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Addon&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Addon&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Addon&action=page&filter=&language=en)This is the approved revision of this
page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Addon&language=&task=view "Start translation for this language")
  * [Deutsch](/Addon/de "Addon \(100% translated\)")
  * English
  * [español](/Addon/es "Complemento \(91% translated\)")
  * [français](/Addon/fr "Extension \(100% translated\)")
  * [italiano](/Addon/it "Addon \(100% translated\)")
  * [polski](/Addon/pl "Dodatki \(100% translated\)")
  * [português do Brasil](/Addon/pt-br "Extensões \(18% translated\)")
  * [русский](/Addon/ru "Дополнения \(100% translated\)")
  * [日本語](/Addon/ja "アドオン \(91% translated\)")

## Introduction

In FreeCAD and in this documentation, an addon is any component that is not
part of the base installation, but that can be added to the system by certain
methods.

## Different types

There are three types of addons:

  * [Macros](/Macros "Macros"): short snippet of [Python](/Python "Python") code that provides a new tool or functionality in a single file ending with `.FCMacro`.
  * [Workbenches](/External_workbenches "External workbenches"): collections of Python files that provide related [Gui Commands](/Gui_Command "Gui Command") (tools) centered around a particular topic, for example, tools to design cabinets, or tools to work with architecture, or tools to design boats, etc. These workbenches usually define new toolbars where [commands](/Gui_Command "Gui Command") are placed as buttons.
  * [Preference Packs](/Preference_Packs "Preference Packs"): distributable collections of user preferences. [introduced in 0.20](/Release_notes_0.20 "Release notes 0.20")

## Installation

The recommended way to install addons is with the
[![](/images/e/ee/Std_AddonMgr.svg)](/index.php?title=File:Std_AddonMgr.svg&filetimestamp=20240704212012&)
[Addon Manager](/Std_AddonMgr "Std AddonMgr").

But for macros and workbenches manual installation is also possible:

  * [How to install macros](/How_to_install_macros "How to install macros")
  * [Installing more workbenches](/Installing_more_workbenches "Installing more workbenches")

## Information for developers

If you have developed a macro or workbench, and want to see it included in the
Addon manager, read how to do so on the repository pages: ([FreeCAD-
addons](https://github.com/FreeCAD/FreeCAD-addons/) and [FreeCAD-
macros](https://github.com/FreeCAD/FreeCAD-macros/)). If you add your macro to
the [Macros recipes](/Macros_recipes "Macros recipes") page, there is nothing
else to do, it will automatically be picked up by the Addon manager.

See also:

  * [Distribution of a Python workbench](/Workbench_creation#Distribution "Workbench creation")
  * [Distribution of a C++ workbench](/Workbench_creation#Distribution_2 "Workbench creation")

  

Expand[![](/images/thumb/9/94/User_hub.png/24px-
User_hub.png)](/index.php?title=File:User_hub.png&filetimestamp=20190221145008&)
[User documentation](/User_hub "User hub")

  * **[Getting started](/Getting_started "Getting started")**
  * **Installation:** [Download](/Download "Download"), [Windows](/Installing_on_Windows "Installing on Windows"), [Linux](/Installing_on_Linux "Installing on Linux"), [Mac](/Installing_on_Mac "Installing on Mac"), [Additional components](/Installing_additional_components "Installing additional components"), [Docker](/Compile_on_Docker "Compile on Docker"), [AppImage](/AppImage "AppImage"), [Ubuntu Snap](/Ubuntu_Snap "Ubuntu Snap")
  * **Basics:** [About FreeCAD](/About_FreeCAD "About FreeCAD"), [Interface](/Interface "Interface"), [Mouse navigation](/Mouse_navigation "Mouse navigation"), [Selection methods](/Selection_methods "Selection methods"), [Object name](/Object_name "Object name"), [Preferences](/Preferences_Editor "Preferences Editor"), [Workbenches](/Workbenches "Workbenches"), [Document structure](/Document_structure "Document structure"), [Properties](/Property "Property"), [Help FreeCAD](/Help_FreeCAD "Help FreeCAD"), [Donate](/Donate "Donate")

* * *

  * **Help:** [Tutorials](/Tutorials "Tutorials"), [Video tutorials](/Video_tutorials "Video tutorials")
  * **[Workbenches](/Workbenches "Workbenches"):** [Std Base](/Std_Base "Std Base"), [Assembly](/Assembly_Workbench "Assembly Workbench"), [BIM](/BIM_Workbench "BIM Workbench"), [CAM](/CAM_Workbench "CAM Workbench"), [Draft](/Draft_Workbench "Draft Workbench"), [FEM](/FEM_Workbench "FEM Workbench"), [Inspection](/Inspection_Workbench "Inspection Workbench"), [Material](/Material_Workbench "Material Workbench"), [Mesh](/Mesh_Workbench "Mesh Workbench"), [OpenSCAD](/OpenSCAD_Workbench "OpenSCAD Workbench"), [Part](/Part_Workbench "Part Workbench"), [PartDesign](/PartDesign_Workbench "PartDesign Workbench"), [Points](/Points_Workbench "Points Workbench"), [Reverse Engineering](/Reverse_Engineering_Workbench "Reverse Engineering Workbench"), [Robot](/Robot_Workbench "Robot Workbench"), [Sketcher](/Sketcher_Workbench "Sketcher Workbench"), [Spreadsheet](/Spreadsheet_Workbench "Spreadsheet Workbench"), [Surface](/Surface_Workbench "Surface Workbench"), [TechDraw](/TechDraw_Workbench "TechDraw Workbench"), [Test Framework](/Testing "Testing")

* * *

  * **Addons:** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

