---
url: https://wiki.freecad.org/Selection_methods
title: Selection methods
scraped_at: 2025-09-08 16:45:41
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Overview
  * 2 3D view Toggle 3D view subsection
    * 2.1 Simple selection
    * 2.2 Repeated clicks
    * 2.3 Selection commands
  * 3 Selection view Toggle Selection view subsection
    * 3.1 Object export
  * 4 Tree view
  * 5 Scripting

# Selection methods

  * [Page](/Selection_methods "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Selection_methods&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Selection_methods)
  * [Edit](/index.php?title=Selection_methods&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Selection_methods&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Selection_methods.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Selection_methods&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Selection_methods)
  * [Edit](/index.php?title=Selection_methods&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Selection_methods&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Selection_methods&action=history)

General

  * [What links here](/Special:WhatLinksHere/Selection_methods "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Selection_methods "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Selection_methods&oldid=1597894 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Selection_methods&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Selection_methods&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Selection+methods&action=page&filter=&language=en)This is the approved
revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Selection+methods&language=&task=view "Start translation for this language")
  * [Deutsch](/Selection_methods/de "Auswahlmethoden \(100% translated\)")
  * English
  * [español](/Selection_methods/es "Métodos de selección \(17% translated\)")
  * [français](/Selection_methods/fr "Méthodes de sélection \(100% translated\)")
  * [hrvatski](/Selection_methods/hr "Metoda odabira \(23% translated\)")
  * [italiano](/Selection_methods/it "Metodi di selezione \(100% translated\)")
  * [polski](/Selection_methods/pl "Metody wyboru \(100% translated\)")
  * [português do Brasil](/Selection_methods/pt-br "Métodos de seleção \(80% translated\)")
  * [русский](/Selection_methods/ru "Методы выделения \(66% translated\)")
  * [日本語](/Selection_methods/ja "オブジェクトの選択方法 \(11% translated\)")
  * [한국어](/Selection_methods/ko "대상물 선택 방법 \(11% translated\)")

![](/images/6/6f/Arrow-left.svg) [Mouse navigation](/Mouse_navigation "Mouse
navigation")

[Navigation Cube](/Navigation_Cube "Navigation Cube") ![](/images/a/af/Arrow-
right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

## Overview

Selection methods in FreeCAD allow picking objects in the [FreeCAD
Interface](/Interface "Interface"): such as [3D view](/3D_view "3D view"),
[tree view](/Tree_view "Tree view"), [selection view](/Selection_view
"Selection view"), and other dialogs. Some selection methods are workbench
specific and are documented in the particular workbench documentation.

## 3D view

In the [3D view](/3D_view "3D view") there are various ways of selecting
objects.

### Simple selection

Simple selection with the mouse (by default left-click) and pre-selection
(hover) are described in the [mouse navigation](/Mouse_navigation "Mouse
navigation") page.

### Repeated clicks

The first click selects a sub-element (vertex, edge or face) of the object
under the mouse. A second click selects the whole object.

The third click extends the selection to its container object ([PartDesign
Body](/PartDesign_Body "PartDesign Body"), [Std Part](/Std_Part "Std Part"),
and others). Further clicks expand the selection up the container chain.

### Selection commands

  * To select all objects: [Std SelectAll](/Std_SelectAll "Std SelectAll").
  * To box select multiple main objects: [Std BoxSelection](/Std_BoxSelection "Std BoxSelection").
  * To box select multiple faces: [Std BoxElementSelection](/Std_BoxElementSelection "Std BoxElementSelection") or [Part BoxSelection](/Part_BoxSelection "Part BoxSelection").

## Selection view

The [selection view](/Selection_view "Selection view") shows the names of the
objects being selected, including their full name within an object, for
example, `Unnamed#Body.Box001.Face17`.

It also allows to perform some actions like [Std
ViewFitSelection](/Std_ViewFitSelection "Std ViewFitSelection"), and sending
the object to the [Python console](/Python_console "Python console").

### Object export

_This should be in the[selection view](/Selection_view "Selection view")
page._

Select any complex object, for example, a [PartDesign Body](/PartDesign_Body
"PartDesign Body") or [Std Part](/Std_Part "Std Part"), then in the [selection
view](/Selection_view "Selection view") select again the object, and then
press Ctrl \+ C in the keyboard to open the **Object selection** dialog. This
allows copying the selected object together with all or only some of that
object's dependency objects. For example, for a [Std Part](/Std_Part "Std
Part") the possible objects to select include the [Std Part](/Std_Part "Std
Part") itself, but also its Origin, its three base axes (XYZ), and its three
base planes (XY, YZ, XZ).

After pressing OK, the selected objects are copied into memory, and then can
be pasted in the document to duplicate these objects only.

[![](/images/5/55/ObjectSelection.png)](/index.php?title=File:ObjectSelection.png&filetimestamp=20200204032022&)

Object selection dialog that is launched from the [selection
view](/Selection_view "Selection view").

## Tree view

In the [tree view](/Tree_view "Tree view") items can be selected, or
deselected, one at a time, by holding the Ctrl key and clicking with the
mouse.

A range of items can be selected by clicking on the first item, holding Shift,
and clicking on the last item.

Selecting a single item will also show its properties in the [property
editor](/Property_editor "Property editor").

Double clicking will open any associated [task panel](/Task_panel "Task
panel") containing actions. Make sure to close this task panel before
executing another command or switching to any other workbench.

More methods are available by opening the context menu (right-click),
depending on the object selected or the active workbench; see the information
in [tree view](/Tree_view "Tree view").

## Scripting

Selecting objects is inherently a graphical task and therefore it is only
available when the graphical user interface is loaded.

These methods can be used in [macros](/Macros "Macros") or from the [Python
console](/Python_console "Python console"):

    
    
    import FreeCADGui as Gui
    
    Gui.Selection.addSelection
    Gui.Selection.addSelectionGate
    Gui.Selection.Filter
    

The `addSelectionGate` method prevents the user from selecting objects not
specified in the selection string. A
[![](/images/3/3c/Button_invalid.svg)](/index.php?title=File:Button_invalid.svg&filetimestamp=20240704191248&)
symbol appears when the pointer is over an item not in the specified group.

    
    
    Gui.Selection.addSelectionGate("SELECT Part::Feature SUBELEMENT Edge")
    
    #### or
    Gui.Selection.addSelectionGate("SELECT Part::Feature SUBELEMENT Face")
    
    #### or
    Gui.Selection.addSelectionGate("SELECT Part::Feature SUBELEMENT Vertex")
    

To remove `SelectionGate()`:

    
    
    Gui.Selection.removeSelectionGate()
    

See the [Source documentation](/Source_documentation "Source documentation")
and [Std PythonHelp](/Std_PythonHelp "Std PythonHelp") for more help on using
these tools.

  

![](/images/6/6f/Arrow-left.svg) [Mouse navigation](/Mouse_navigation "Mouse
navigation")

[Navigation Cube](/Navigation_Cube "Navigation Cube") ![](/images/a/af/Arrow-
right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

Expand[![](/images/thumb/9/94/User_hub.png/24px-
User_hub.png)](/index.php?title=File:User_hub.png&filetimestamp=20190221145008&)
[User documentation](/User_hub "User hub")

  * **[Getting started](/Getting_started "Getting started")**
  * **Installation:** [Download](/Download "Download"), [Windows](/Installing_on_Windows "Installing on Windows"), [Linux](/Installing_on_Linux "Installing on Linux"), [Mac](/Installing_on_Mac "Installing on Mac"), [Additional components](/Installing_additional_components "Installing additional components"), [Docker](/Compile_on_Docker "Compile on Docker"), [AppImage](/AppImage "AppImage"), [Ubuntu Snap](/Ubuntu_Snap "Ubuntu Snap")
  * **Basics:** [About FreeCAD](/About_FreeCAD "About FreeCAD"), [Interface](/Interface "Interface"), [Mouse navigation](/Mouse_navigation "Mouse navigation"), Selection methods, [Object name](/Object_name "Object name"), [Preferences](/Preferences_Editor "Preferences Editor"), [Workbenches](/Workbenches "Workbenches"), [Document structure](/Document_structure "Document structure"), [Properties](/Property "Property"), [Help FreeCAD](/Help_FreeCAD "Help FreeCAD"), [Donate](/Donate "Donate")

* * *

  * **Help:** [Tutorials](/Tutorials "Tutorials"), [Video tutorials](/Video_tutorials "Video tutorials")
  * **[Workbenches](/Workbenches "Workbenches"):** [Std Base](/Std_Base "Std Base"), [Assembly](/Assembly_Workbench "Assembly Workbench"), [BIM](/BIM_Workbench "BIM Workbench"), [CAM](/CAM_Workbench "CAM Workbench"), [Draft](/Draft_Workbench "Draft Workbench"), [FEM](/FEM_Workbench "FEM Workbench"), [Inspection](/Inspection_Workbench "Inspection Workbench"), [Material](/Material_Workbench "Material Workbench"), [Mesh](/Mesh_Workbench "Mesh Workbench"), [OpenSCAD](/OpenSCAD_Workbench "OpenSCAD Workbench"), [Part](/Part_Workbench "Part Workbench"), [PartDesign](/PartDesign_Workbench "PartDesign Workbench"), [Points](/Points_Workbench "Points Workbench"), [Reverse Engineering](/Reverse_Engineering_Workbench "Reverse Engineering Workbench"), [Robot](/Robot_Workbench "Robot Workbench"), [Sketcher](/Sketcher_Workbench "Sketcher Workbench"), [Spreadsheet](/Spreadsheet_Workbench "Spreadsheet Workbench"), [Surface](/Surface_Workbench "Surface Workbench"), [TechDraw](/TechDraw_Workbench "TechDraw Workbench"), [Test Framework](/Testing "Testing")

* * *

  * **[Addons](/Addon "Addon"):** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

