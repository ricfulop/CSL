---
url: https://wiki.freecad.org/Interface
title: Interface
scraped_at: 2025-09-08 16:45:39
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Components of the interface Toggle Components of the interface subsection
    * 2.1 Menus
    * 2.2 Toolbars
    * 2.3 Panels
    * 2.4 Other
    * 2.5 Customization
  * 3 Dock panel overlay Toggle Dock panel overlay subsection
    * 3.1 Overlay Modes
    * 3.2 Commands

# Interface

  * [Page](/Interface "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Interface&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Interface)
  * [Edit](/index.php?title=Interface&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Interface&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Interface.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Interface&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Interface)
  * [Edit](/index.php?title=Interface&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Interface&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Interface&action=history)

General

  * [What links here](/Special:WhatLinksHere/Interface "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Interface "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Interface&oldid=1619936 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Interface&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Interface&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Interface&action=page&filter=&language=en)This is the approved revision of
this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Interface&language=&task=view "Start translation for this language")
  * [Deutsch](/Interface/de "Oberfläche \(59% translated\)")
  * English
  * [español](/Interface/es "Interfaz \(59% translated\)")
  * [français](/Interface/fr "Interface \(100% translated\)")
  * [hrvatski](/Interface/hr "Interface/hr \(3% translated\)")
  * [italiano](/Interface/it "Interfaccia \(59% translated\)")
  * [polski](/Interface/pl "Interfejs użytkownika \(100% translated\)")
  * [português do Brasil](/Interface/pt-br "Interface \(5% translated\)")
  * [русский](/Interface/ru "Интерфейс \(24% translated\)")
  * [日本語](/Interface/ja "ユーザー・インタフェース \(5% translated\)")
  * [한국어](/Interface/ko "인터페이스 \(59% translated\)")

## Introduction

The FreeCAD interface is based on Qt, a well known graphical user interface
(GUI) toolkit, particularly used in Linux, but also available in Windows and
MacOS.

[![](/images/d/d8/FreeCAD_interface_base_divisions.svg)](/index.php?title=File:FreeCAD_interface_base_divisions.svg&filetimestamp=20200314201207&)

Standard interface in v0.19.

The main window of the application can be roughly divided into 11 sections:

  1. The [main view area](/Main_view_area "Main view area"), which can contain different tabbed windows
  2. The [3D view](/3D_view "3D view"), normally embedded in the [main view area](/Main_view_area "Main view area")
  3. The upper part of the [combo view](/Combo_view "Combo view"), which includes the [tree view](/Tree_view "Tree view") and [task panel](/Task_panel "Task panel")
  4. The lower part of the [combo view](/Combo_view "Combo view"), which includes the [property editor](/Property_editor "Property editor")
  5. The [selection view](/Selection_view "Selection view")
  6. The [report view](/Report_view "Report view")
  7. The [Python console](/Python_console "Python console")
  8. The [status bar](/Status_bar "Status bar")
  9. The toolbar area, see the following information on the toolbars
  10. The [Workbench selector](/Std_Workbench "Std Workbench"), which itself is a toolbar
  11. The [standard menu](/Standard_Menu "Standard Menu")

## Components of the interface

Like many pieces of software, FreeCAD includes a standard menu bar, and then a
series of toolbars and panels where the user tools are found.

### Menus

The [standard menus](/Standard_Menu "Standard Menu") are:
[**File**](/Std_File_Menu "Std File Menu") , [**Edit**](/Std_Edit_Menu "Std
Edit Menu") , [**View**](/Std_View_Menu "Std View Menu") ,
[**Tools**](/Std_Tools_Menu "Std Tools Menu") , [**Macro**](/Std_Macro_Menu
"Std Macro Menu") , [**Windows**](/Std_Windows_Menu "Std Windows Menu") ,
[**Help**](/Std_Help_Menu "Std Help Menu").

### Toolbars

The standard toolbars that appear in the interface are:

  * File toolbar: tools to work with files, open documents, copy, paste, undo and redo actions.
  * [Workbench toolbar](/Std_Workbench "Std Workbench"): it contains a single widget to select the active [workbench](/Workbenches "Workbenches").
  * Macro toolbar: tools to record, edit, and execute [macros](/Macros "Macros").
  * View toolbar: tools to control how objects appear in the [3D view](/3D_view "3D view").
  * Structure toolbar: tools to organize objects in the document, and create links to additional documents.

These can be turned on and off by right clicking on an empty space on one of
the toolbars and choosing the desired element, or from the menu, **View →
Toolbars**.

### Panels

The main panels that allow working with objects are:

  * [3D view](/3D_view "3D view"): the area where 2D and 3D geometry is drawn.
  * [Combo view](/Combo_view "Combo view"): the panel that contains the [tree view](/Tree_view "Tree view"), the [task panel](/Task_panel "Task panel"), and the [property editor](/Property_editor "Property editor").
  * [Tree view](/Tree_view "Tree view"): the element that shows all objects in the document and their parametric history.
  * [Task panel](/Task_panel "Task panel"): the panel that shows different actions and options depending on the drawing tool selected.
  * [Property editor](/Property_editor "Property editor"): the place where object properties are modified.
  * [Selection view](/Selection_view "Selection view"): the panel that shows elements that are currently selected.
  * [Report view](/Report_view "Report view"): the text box that shows different messages from the application and its tools.
  * [Python console](/Python_console "Python console"): the editor that allows running [Python](/Python "Python") code interactively to see results in the [3D view](/3D_view "3D view").
  * [Status bar](/Status_bar "Status bar"): the bar that shows certain messages from the application, and that has the [mouse navigation](/Mouse_navigation "Mouse navigation") selector.
  * [DAG view](/DAG_view "DAG view"): an alternative to the [tree view](/Tree_view "Tree view"), which shows the relationships between different objects through a graph.

With the exception of the 3D view, all can be turned on and off by right
clicking on an empty space on one of the top toolbars and choosing the desired
element, or from the menu, **View → Panels**.

To activate and deactivate the status bar use the menu, **View → Status bar**.

### Other

Other useful interfaces and windows include:

  * [Scene inspector](/Std_SceneInspector "Std SceneInspector"): a panel that shows the Coin3D nodes that make up the [scenegraph](/Scenegraph "Scenegraph"). For power users and developers, it may be useful to troubleshoot operations that manipulate the scene directly, and the objects created in the [3D view](/3D_view "3D view").
  * [Dependency graph](/Std_DependencyGraph "Std DependencyGraph"): a window showing the dependency graph of all the objects in the document, created with the auxiliary program [Graphviz](https://graphviz.org/). It is helpful to recognize problems in the creation of objects, such as circular dependencies, which may not be entirely evident from the [tree view](/Tree_view "Tree view") or the [DAG view](/DAG_view "DAG view").

### Customization

Toolbars can have more or fewer buttons, and custom toolbars can be created
with a mix of different tools, and to store developed macros.

These options are in the menu, **Tools → Customize**. See [interface
customization](/Interface_Customization "Interface Customization").

## Dock panel overlay

[introduced in 1.0](/Release_notes_1.0 "Release notes 1.0")

[![Dock panel overlay enabled, showing transparent and auto-hidden
panels](/images/thumb/8/81/Dock_Panel_Overlay.png/300px-
Dock_Panel_Overlay.png)](/index.php?title=File:Dock_Panel_Overlay.png&filetimestamp=20250726040057&)Dock
panel overlay enabled, showing transparent and auto-hidden panels

The dock panel overlay system is a feature to maximize the space available for
the [3D view](/3D_view "3D view"). It transforms standard docked panels, like
the [Combo View](/Combo_view "Combo view"), into floating, transparent widgets
that sit on top of the 3D view. This allows the 3D view to expand and use the
space the panels previously occupied. The overlay panels become fully opaque
and interactive when the mouse hovers over them, and transparent again when
the mouse moves away, even enabling clicking through them to interact with the
model.

The main switch for this feature is the **[Toggle overlay for
all](/Std_DockOverlayAll "Std DockOverlayAll")** command. Additional commands
are available for more granular control.

### Overlay Modes

Each panel in the overlay system can be set to a different mode, allowing for
a customized workflow. These settings are available by clicking the overlay
mode button
([![](/images/3/38/Overlay_Mode.svg)](/index.php?title=File:Overlay_Mode.svg&filetimestamp=20250726043037&))
in the title bar of an overlay panel.

  * **None** : This is the default mode. The panel remains visible but transparent when not in use, and becomes opaque on mouse-over. It provides a good balance between access to tools and 3D view space.

  * **Auto hide** : This mode completely hides the panel by sliding it off-screen. The panel will only reappear when you move your mouse to the edge of the window where it is hiding. This mode provides the maximum screen space and is suitable for panels that are used infrequently.

  * **Show on edit** : A context-aware mode that automatically shows the panel when an object's edit mode is entered (e.g., editing a sketch). When the edit is finished, the panel automatically hides again. This mode well suited for the [Task panel](/Task_panel "Task panel"), for instance.

  * **Hide on edit** : The opposite of "Show on edit". This mode automatically hides the panel when an object's edit mode is entered. This is useful for clearing away secondary panels (like the [Report view](/Report_view "Report view")) to reduce clutter while focusing on a specific task.

  * **Auto task** : A smart version of "Show on edit", designed for the [Task panel](/Task_panel "Task panel"). It shows the panel only when a command opens an active task, and hides it the moment the task is completed, providing a more automated workflow.

### Commands

The following commands control the dock panel overlay feature:

  * **[Toggle overlay for all](/Std_DockOverlayAll "Std DockOverlayAll")** : The master switch for the overlay feature. Toggles overlay mode on or off for all panels.
  * **[Toggle transparent for all](/Std_DockOverlayTransparentAll "Std DockOverlayTransparentAll")** : Toggles the special "transparent active" mode, where panels remain transparent even when you mouse over them.
  * **[Toggle overlay](/Std_DockOverlayToggle "Std DockOverlayToggle")** : Toggles overlay mode for the single panel currently under the mouse cursor.
  * **[Toggle transparent mode](/Std_DockOverlayToggleTransparent "Std DockOverlayToggleTransparent")** : Toggles the "transparent active" mode for the single panel currently under the mouse cursor.
  * **[Toggle left](/Std_DockOverlayToggleLeft "Std DockOverlayToggleLeft")** , **[Toggle right](/Std_DockOverlayToggleRight "Std DockOverlayToggleRight")** , **[Toggle top](/Std_DockOverlayToggleTop "Std DockOverlayToggleTop")** , **[Toggle bottom](/Std_DockOverlayToggleBottom "Std DockOverlayToggleBottom")** : Show or hide the entire group of overlay panels on a specific side of the screen.

  

Expand[![](/images/0/06/Freecad.svg)](/index.php?title=File:Freecad.svg&filetimestamp=20240704193018&)
Interface

  * [Preferences Editor](/Preferences_Editor "Preferences Editor"), [Interface Customization](/Interface_Customization "Interface Customization")
  * Main window: [Standard menu](/Standard_Menu "Standard Menu"), [Main view area](/Main_view_area "Main view area"), [3D view](/3D_view "3D view"), [Combo view](/Combo_view "Combo view") ([Tree view](/Tree_view "Tree view"), [Task panel](/Task_panel "Task panel"), [Property editor](/Property_editor "Property editor")), [Selection view](/Selection_view "Selection view"), [Report view](/Report_view "Report view"), [Python console](/Python_console "Python console"), [Status bar](/Status_bar "Status bar"), [DAG view](/DAG_view "DAG view"), [Workbench Selector](/Std_Workbench "Std Workbench")
  * Auxiliary windows: [Scene inspector](/Std_SceneInspector "Std SceneInspector"), [Dependency graph](/Std_DependencyGraph "Std DependencyGraph")

Expand[![](/images/thumb/9/94/User_hub.png/24px-
User_hub.png)](/index.php?title=File:User_hub.png&filetimestamp=20190221145008&)
[User documentation](/User_hub "User hub")

  * **[Getting started](/Getting_started "Getting started")**
  * **Installation:** [Download](/Download "Download"), [Windows](/Installing_on_Windows "Installing on Windows"), [Linux](/Installing_on_Linux "Installing on Linux"), [Mac](/Installing_on_Mac "Installing on Mac"), [Additional components](/Installing_additional_components "Installing additional components"), [Docker](/Compile_on_Docker "Compile on Docker"), [AppImage](/AppImage "AppImage"), [Ubuntu Snap](/Ubuntu_Snap "Ubuntu Snap")
  * **Basics:** [About FreeCAD](/About_FreeCAD "About FreeCAD"), Interface, [Mouse navigation](/Mouse_navigation "Mouse navigation"), [Selection methods](/Selection_methods "Selection methods"), [Object name](/Object_name "Object name"), [Preferences](/Preferences_Editor "Preferences Editor"), [Workbenches](/Workbenches "Workbenches"), [Document structure](/Document_structure "Document structure"), [Properties](/Property "Property"), [Help FreeCAD](/Help_FreeCAD "Help FreeCAD"), [Donate](/Donate "Donate")

* * *

  * **Help:** [Tutorials](/Tutorials "Tutorials"), [Video tutorials](/Video_tutorials "Video tutorials")
  * **[Workbenches](/Workbenches "Workbenches"):** [Std Base](/Std_Base "Std Base"), [Assembly](/Assembly_Workbench "Assembly Workbench"), [BIM](/BIM_Workbench "BIM Workbench"), [CAM](/CAM_Workbench "CAM Workbench"), [Draft](/Draft_Workbench "Draft Workbench"), [FEM](/FEM_Workbench "FEM Workbench"), [Inspection](/Inspection_Workbench "Inspection Workbench"), [Material](/Material_Workbench "Material Workbench"), [Mesh](/Mesh_Workbench "Mesh Workbench"), [OpenSCAD](/OpenSCAD_Workbench "OpenSCAD Workbench"), [Part](/Part_Workbench "Part Workbench"), [PartDesign](/PartDesign_Workbench "PartDesign Workbench"), [Points](/Points_Workbench "Points Workbench"), [Reverse Engineering](/Reverse_Engineering_Workbench "Reverse Engineering Workbench"), [Robot](/Robot_Workbench "Robot Workbench"), [Sketcher](/Sketcher_Workbench "Sketcher Workbench"), [Spreadsheet](/Spreadsheet_Workbench "Spreadsheet Workbench"), [Surface](/Surface_Workbench "Surface Workbench"), [TechDraw](/TechDraw_Workbench "TechDraw Workbench"), [Test Framework](/Testing "Testing")

* * *

  * **[Addons](/Addon "Addon"):** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

