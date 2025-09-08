---
url: https://wiki.freecad.org/Robot_Workbench
title: Robot Workbench
scraped_at: 2025-09-08 16:44:24
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Tools Toggle Tools subsection
    * 2.1 Robots
    * 2.2 Trajectories
      * 2.2.1 Non parametric trajectories
      * 2.2.2 Parametric trajectories
  * 3 Scripting
  * 4 Tutorials

# Robot Workbench

  * [Page](/Robot_Workbench "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Robot_Workbench&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Robot_Workbench)
  * [Edit](/index.php?title=Robot_Workbench&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Robot_Workbench&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Robot_Workbench.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Robot_Workbench&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Robot_Workbench)
  * [Edit](/index.php?title=Robot_Workbench&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Robot_Workbench&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Robot_Workbench&action=history)

General

  * [What links here](/Special:WhatLinksHere/Robot_Workbench "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Robot_Workbench "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Robot_Workbench&oldid=1604505 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Robot_Workbench&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Robot_Workbench&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Robot+Workbench&action=page&filter=&language=en)This is the approved revision
of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Robot+Workbench&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/Robot_Workbench/id "Robot Workbench \(5% translated\)")
  * [Deutsch](/Robot_Workbench/de "Arbeitsbereich Robot \(100% translated\)")
  * English
  * [Türkçe](/Robot_Workbench/tr "Robot Tezgahı \(42% translated\)")
  * [español](/Robot_Workbench/es "Ambiente de trabajo Robot \(95% translated\)")
  * [français](/Robot_Workbench/fr "Atelier Robot \(100% translated\)")
  * [hrvatski](/Robot_Workbench/hr "Robot Radni stol \(5% translated\)")
  * [italiano](/Robot_Workbench/it " Ambiente Robot \(100% translated\)")
  * [magyar](/Robot_Workbench/hu "Robot Workbench \(5% translated\)")
  * [polski](/Robot_Workbench/pl "Środowisko pracy Robot \(100% translated\)")
  * [português](/Robot_Workbench/pt "Robot Workbench \(53% translated\)")
  * [português do Brasil](/Robot_Workbench/pt-br "Bancada de trabalho Robot \(95% translated\)")
  * [română](/Robot_Workbench/ro "Atelierul Robotică \(42% translated\)")
  * [suomi](/Robot_Workbench/fi "Robot Workbench \(5% translated\)")
  * [svenska](/Robot_Workbench/sv "Allmänt bruk \(11% translated\)")
  * [čeština](/Robot_Workbench/cs "Robot Workbench \(11% translated\)")
  * [български](/Robot_Workbench/bg "Robot Workbench \(5% translated\)")
  * [русский](/Robot_Workbench/ru "Верстак Robot \(95% translated\)")
  * [українська](/Robot_Workbench/uk "Robot Workbench \(5% translated\)")
  * [中文](/Robot_Workbench/zh "Robot Workbench/zh \(0% translated\)")
  * [中文（中国大陆）](/Robot_Workbench/zh-cn "机器人工作台 \(21% translated\)")
  * [中文（繁體）](/Robot_Workbench/zh-hant "Robot Workbench \(5% translated\)")
  * [中文（臺灣）](/Robot_Workbench/zh-tw "機器人工作台 \(5% translated\)")
  * [日本語](/Robot_Workbench/ja "Robot Workbench/ロボットワークベンチ \(26% translated\)")
  * [한국어](/Robot_Workbench/ko "로봇 작업대 \(16% translated\)")

![](/images/6/6f/Arrow-left.svg)
![](/images/8/83/Workbench_Reverse_Engineering.svg) [Reverse Engineering
Workbench](/Reverse_Engineering_Workbench "Reverse Engineering Workbench")

![](/images/9/91/Workbench_Sketcher.svg) [Sketcher
Workbench](/Sketcher_Workbench "Sketcher Workbench") ![](/images/a/af/Arrow-
right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

The Robot Workbench is unmaintained. If you have experience with the topic and
are interested in maintaining it, please state your intention in the
developer's section of the [FreeCAD forum](https://forum.freecad.org).

The reason this workbench is still in the master source code is because this
workbench is programmed in C++. If this workbench could be programmed in
Python, then it could be made an [external workbench](/External_workbenches
"External workbenches") and it could be moved to a separate repository.

## Introduction

[![](/images/e/e3/Workbench_Robot.svg)](/index.php?title=File:Workbench_Robot.svg&filetimestamp=20200404173908&)Robot
workbench icon

The
[![](/images/e/e3/Workbench_Robot.svg)](/index.php?title=File:Workbench_Robot.svg&filetimestamp=20200404173908&)
Robot Workbench is a tool to simulate a standard [6-axis industrial
robot](/Robot_6-Axis "Robot 6-Axis"), like [Kuka](http://kuka.com/).

You can do the following tasks:

  * Set up a simulation environment with a robot and work pieces.
  * Create and fill up movement trajectories.
  * Decompose features of a CAD part to a trajectory.
  * Simulate the robot movement and reaching distance.
  * Export the trajectory to a robot program file.

To get started try the [Robot tutorial](/Robot_tutorial "Robot tutorial"), and
see the programming interface in the
[RobotExample.py](https://github.com/FreeCAD/FreeCAD_sf_master/blob/master/src/Mod/Robot/RobotExample.py)
example file.

[![](/images/thumb/c/cb/Robot_Workbench_example.jpg/500px-
Robot_Workbench_example.jpg)](/index.php?title=File:Robot_Workbench_example.jpg&filetimestamp=20181206194102&)

## Tools

Here the principal commands you can use to create a robot set-up.

### Robots

The tools to create and manage the 6-Axis robots

  * [![](/images/0/0a/Robot_CreateRobot.svg)](/index.php?title=File:Robot_CreateRobot.svg&filetimestamp=20170322205803&) [Create a robot](/Robot_CreateRobot "Robot CreateRobot"): Insert a new robot into the scene
  * [![](/images/8/80/Robot_Simulate.svg)](/index.php?title=File:Robot_Simulate.svg&filetimestamp=20170322210231&) [Simulate a trajectory](/Robot_Simulate "Robot Simulate"): Opens the simulation dialog and lets you simulate
  * [![](/images/f/f2/Robot_Export.svg)](/index.php?title=File:Robot_Export.svg&filetimestamp=20170322205926&) [Export a trajectory](/Robot_Export "Robot Export"): Export a robot program file
  * [![](/images/4/4a/Robot_SetHomePos.svg)](/index.php?title=File:Robot_SetHomePos.svg&filetimestamp=20170322210202&) [Set home position](/Robot_SetHomePos "Robot SetHomePos"): Set the home position of a robot
  * [![](/images/9/96/Robot_RestoreHomePos.svg)](/index.php?title=File:Robot_RestoreHomePos.svg&filetimestamp=20170322210040&) [Restore home position](/Robot_RestoreHomePos "Robot RestoreHomePos"): move the robot to its home position

### Trajectories

Tools to create and manipulate trajectories. There are two kinds, the
parametric and non parametric ones.

#### Non parametric trajectories

  * [![](/images/a/a2/Robot_CreateTrajectory.svg)](/index.php?title=File:Robot_CreateTrajectory.svg&filetimestamp=20170322205833&) [Create a trajectory](/Robot_CreateTrajectory "Robot CreateTrajectory"): Inserts a new empty trajectory-object into the scene
  * [![](/images/6/65/Robot_SetDefaultOrientation.svg)](/index.php?title=File:Robot_SetDefaultOrientation.svg&filetimestamp=20170322210103&) [Set the default orientation](/Robot_SetDefaultOrientation "Robot SetDefaultOrientation"): Set the orientation way-points gets created by default
  * [![](/images/d/d8/Robot_SetDefaultValues.svg)](/index.php?title=File:Robot_SetDefaultValues.svg&filetimestamp=20170322210136&) [Set the default speed parameter](/Robot_SetDefaultValues "Robot SetDefaultValues"): Set the default values for way-point creation
  * [![](/images/b/b8/Robot_InsertWaypoint.svg)](/index.php?title=File:Robot_InsertWaypoint.svg&filetimestamp=20170322205955&) [Insert a waypoint](/Robot_InsertWaypoint "Robot InsertWaypoint"): Insert a way-point from the current robot position into a trajectory
  * [![](/images/6/6f/Robot_InsertWaypointPre.svg)](/index.php?title=File:Robot_InsertWaypointPre.svg&filetimestamp=20170322210016&) [Insert a waypoint preselected](/Robot_InsertWaypointPre "Robot InsertWaypointPre"): Insert a way-point from the current mouse position into a trajectory

#### Parametric trajectories

  * [![](/images/4/43/Robot_Edge2Trac.svg)](/index.php?title=File:Robot_Edge2Trac.svg&filetimestamp=20170322205900&) [Create a trajectory out of edges](/Robot_Edge2Trac "Robot Edge2Trac"): Insert a new object which decompose edges to a trajectory
  * [![](/images/8/84/Robot_TrajectoryDressUp.svg)](/index.php?title=File:Robot_TrajectoryDressUp.svg&filetimestamp=20170322210320&) [Dress-up a trajectory](/Robot_TrajectoryDressUp "Robot TrajectoryDressUp"): Lets you override one or more properties of a trajectory
  * [![](/images/2/24/Robot_TrajectoryCompound.svg)](/index.php?title=File:Robot_TrajectoryCompound.svg&filetimestamp=20170322210255&) [Trajectory compound](/Robot_TrajectoryCompound "Robot TrajectoryCompound"): Create a compound out of some single trajectories

## Scripting

See the [Robot API example](/Robot_API_example "Robot API example") for a
description of the functions used to model the robot displacements.

## Tutorials

  * [Robot 6-Axis](/Robot_6-Axis "Robot 6-Axis")
  * [VRML Preparation for Robot Simulation](/VRML_Preparation_for_Robot_Simulation "VRML Preparation for Robot Simulation")

  

![](/images/6/6f/Arrow-left.svg)
![](/images/8/83/Workbench_Reverse_Engineering.svg) [Reverse Engineering
Workbench](/Reverse_Engineering_Workbench "Reverse Engineering Workbench")

![](/images/9/91/Workbench_Sketcher.svg) [Sketcher
Workbench](/Sketcher_Workbench "Sketcher Workbench") ![](/images/a/af/Arrow-
right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

Expand[![](/images/e/e3/Workbench_Robot.svg)](/index.php?title=File:Workbench_Robot.svg&filetimestamp=20200404173908&)
Robot

  * **Robots:** [Create a robot](/Robot_CreateRobot "Robot CreateRobot"), [Simulate](/Robot_Simulate "Robot Simulate"), [Export](/Robot_Export "Robot Export"), [Set home position](/Robot_SetHomePos "Robot SetHomePos"), [Restore home position](/Robot_RestoreHomePos "Robot RestoreHomePos")

  * **Trajectories, non parametric:** [Create a trajectory](/Robot_CreateTrajectory "Robot CreateTrajectory"), [Set default orientation](/Robot_SetDefaultOrientation "Robot SetDefaultOrientation"), [Set default values](/Robot_SetDefaultValues "Robot SetDefaultValues"), [Insert waypoint](/Robot_InsertWaypoint "Robot InsertWaypoint"), [Insert waypoint (mouse)](/Robot_InsertWaypointPre "Robot InsertWaypointPre")

  * **Trajectories, parametric:** [Create a trajectory from edges](/Robot_Edge2Trac "Robot Edge2Trac"), [Dress-up trajectory](/Robot_TrajectoryDressUp "Robot TrajectoryDressUp"), [Trajectory compound](/Robot_TrajectoryCompound "Robot TrajectoryCompound")

Expand[![](/images/thumb/9/94/User_hub.png/24px-
User_hub.png)](/index.php?title=File:User_hub.png&filetimestamp=20190221145008&)
[User documentation](/User_hub "User hub")

  * **[Getting started](/Getting_started "Getting started")**
  * **Installation:** [Download](/Download "Download"), [Windows](/Installing_on_Windows "Installing on Windows"), [Linux](/Installing_on_Linux "Installing on Linux"), [Mac](/Installing_on_Mac "Installing on Mac"), [Additional components](/Installing_additional_components "Installing additional components"), [Docker](/Compile_on_Docker "Compile on Docker"), [AppImage](/AppImage "AppImage"), [Ubuntu Snap](/Ubuntu_Snap "Ubuntu Snap")
  * **Basics:** [About FreeCAD](/About_FreeCAD "About FreeCAD"), [Interface](/Interface "Interface"), [Mouse navigation](/Mouse_navigation "Mouse navigation"), [Selection methods](/Selection_methods "Selection methods"), [Object name](/Object_name "Object name"), [Preferences](/Preferences_Editor "Preferences Editor"), [Workbenches](/Workbenches "Workbenches"), [Document structure](/Document_structure "Document structure"), [Properties](/Property "Property"), [Help FreeCAD](/Help_FreeCAD "Help FreeCAD"), [Donate](/Donate "Donate")

* * *

  * **Help:** [Tutorials](/Tutorials "Tutorials"), [Video tutorials](/Video_tutorials "Video tutorials")
  * **[Workbenches](/Workbenches "Workbenches"):** [Std Base](/Std_Base "Std Base"), [Assembly](/Assembly_Workbench "Assembly Workbench"), [BIM](/BIM_Workbench "BIM Workbench"), [CAM](/CAM_Workbench "CAM Workbench"), [Draft](/Draft_Workbench "Draft Workbench"), [FEM](/FEM_Workbench "FEM Workbench"), [Inspection](/Inspection_Workbench "Inspection Workbench"), [Material](/Material_Workbench "Material Workbench"), [Mesh](/Mesh_Workbench "Mesh Workbench"), [OpenSCAD](/OpenSCAD_Workbench "OpenSCAD Workbench"), [Part](/Part_Workbench "Part Workbench"), [PartDesign](/PartDesign_Workbench "PartDesign Workbench"), [Points](/Points_Workbench "Points Workbench"), [Reverse Engineering](/Reverse_Engineering_Workbench "Reverse Engineering Workbench"), Robot, [Sketcher](/Sketcher_Workbench "Sketcher Workbench"), [Spreadsheet](/Spreadsheet_Workbench "Spreadsheet Workbench"), [Surface](/Surface_Workbench "Surface Workbench"), [TechDraw](/TechDraw_Workbench "TechDraw Workbench"), [Test Framework](/Testing "Testing")

* * *

  * **[Addons](/Addon "Addon"):** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

