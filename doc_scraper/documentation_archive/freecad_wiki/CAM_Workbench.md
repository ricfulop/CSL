---
url: https://wiki.freecad.org/CAM_Workbench
title: CAM Workbench
scraped_at: 2025-09-08 16:44:01
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 General concepts
  * 3 Limitations
  * 4 Units
  * 5 Heights and depths
  * 6 Commands Toggle Commands subsection
    * 6.1 Project Commands
    * 6.2 Tool Commands
    * 6.3 Basic Operations
    * 6.4 3D Operations
    * 6.5 Path Dressup
    * 6.6 Supplemental Commands
    * 6.7 Path Modification
    * 6.8 Specialty Operations
    * 6.9 Miscellaneous
  * 7 ToolBit architecture
  * 8 Other
  * 9 Preferences
  * 10 Scripting
  * 11 Tutorials
  * 12 Videos
  * 13 Roadmap

# CAM Workbench

  * [Page](/CAM_Workbench "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:CAM_Workbench&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/CAM_Workbench)
  * [Edit](/index.php?title=CAM_Workbench&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=CAM_Workbench&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/CAM_Workbench.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=CAM_Workbench&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/CAM_Workbench)
  * [Edit](/index.php?title=CAM_Workbench&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=CAM_Workbench&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=CAM_Workbench&action=history)

General

  * [What links here](/Special:WhatLinksHere/CAM_Workbench "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/CAM_Workbench "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=CAM_Workbench&oldid=1623600 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=CAM_Workbench&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=CAM_Workbench&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
CAM+Workbench&action=page&filter=&language=en)This is the approved revision of
this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-CAM+Workbench&language=&task=view "Start translation for this language")
  * [Deutsch](/CAM_Workbench/de "Arbeitsbereich CAM \(88% translated\)")
  * English
  * [Türkçe](/CAM_Workbench/tr "CNC G-Kod Tezgahı \(1% translated\)")
  * [español](/CAM_Workbench/es "Ambiente de trabajo Trayectoria \(7% translated\)")
  * [français](/CAM_Workbench/fr "Atelier CAM \(100% translated\)")
  * [hrvatski](/CAM_Workbench/hr "CAM Workbench/hr \(1% translated\)")
  * [italiano](/CAM_Workbench/it "Ambiente CAM \(100% translated\)")
  * [polski](/CAM_Workbench/pl "Środowisko pracy CAM \(100% translated\)")
  * [português](/CAM_Workbench/pt "Bancada de trabalho Path \(1% translated\)")
  * [português do Brasil](/CAM_Workbench/pt-br "Bancada de trabalho Path \(7% translated\)")
  * [română](/CAM_Workbench/ro "Path Workbench/Atelierul Traiectorii \(4% translated\)")
  * [suomi](/CAM_Workbench/fi "Path Workbench \(1% translated\)")
  * [svenska](/CAM_Workbench/sv "CAM Workbench/sv \(0% translated\)")
  * [čeština](/CAM_Workbench/cs "CAM Workbench/cs \(0% translated\)")
  * [русский](/CAM_Workbench/ru "Верстак Path \(42% translated\)")
  * [中文](/CAM_Workbench/zh "刀路工作台 \(4% translated\)")
  * [中文（中国大陆）](/CAM_Workbench/zh-cn "路径工作台 \(4% translated\)")
  * [中文（臺灣）](/CAM_Workbench/zh-tw "CAM Workbench/zh-tw \(0% translated\)")
  * [日本語](/CAM_Workbench/ja "CAMワークベンチ \(5% translated\)")
  * [한국어](/CAM_Workbench/ko "CAM 작업대 \(7% translated\)")

![](/images/6/6f/Arrow-left.svg) ![](/images/0/05/Workbench_BIM.svg) [BIM
Workbench](/BIM_Workbench "BIM Workbench")

![](/images/9/91/Workbench_Draft.svg) [Draft Workbench](/Draft_Workbench
"Draft Workbench") ![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

[![](/images/9/95/Workbench_CAM.svg)](/index.php?title=File:Workbench_CAM.svg&filetimestamp=20240316105021&)CAM
workbench icon

## Introduction

The
[![](/images/9/95/Workbench_CAM.svg)](/index.php?title=File:Workbench_CAM.svg&filetimestamp=20240316105021&)
CAM Workbench is used to produce machine instructions for [CNC
machines](https://en.wikipedia.org/wiki/CNC_router) from a FreeCAD 3D model.
These produce real-world 3D objects on CNC machines such as mills, lathes,
lasercutters, or similar. Typically, instructions are a
[G-code](https://en.wikipedia.org/wiki/G-code) dialect. A [general CNC lathe
tool path sequence simulation example](https://www.ange-
softs.com/SIMULCNCHTML/index.html) is presented here.

[![](/images/thumb/8/8d/Pathwb.png/600px-
Pathwb.png)](/index.php?title=File:Pathwb.png&filetimestamp=20180111213035&)

The FreeCAD CAM Workbench workflow creates these machine instructions as
follows:

  * A 3D model is the base object, typically created using one or more of the [![](/images/3/39/Workbench_PartDesign.svg)](/index.php?title=File:Workbench_PartDesign.svg&filetimestamp=20240405092932&) [Part Design](/PartDesign_Workbench "PartDesign Workbench"), [![](/images/0/04/Workbench_Part.svg)](/index.php?title=File:Workbench_Part.svg&filetimestamp=20240712190040&) [Part](/Part_Workbench "Part Workbench") or [![](/images/9/91/Workbench_Draft.svg)](/index.php?title=File:Workbench_Draft.svg&filetimestamp=20200404172706&) [Draft](/Draft_Workbench "Draft Workbench") Workbenches.
  * A [CAM Job](/CAM_Job "CAM Job") is created in the CAM Workbench. This contains all the information required to generate the necessary G-code to process the Job on a CNC mill: there is Stock material, the mill has a certain [set of tools](/CAM_ToolBitLibraryOpen "CAM ToolBitLibraryOpen") and it follows certain commands controlling speed and movements (usually G-code).
  * [CAM Tools](/CAM_Tools "CAM Tools") are selected as required by the Job Operations.
  * Milling paths are created using e.g. [Contour](/CAM_Profile "CAM Profile") and [Pocket](/CAM_Pocket_3D "CAM Pocket 3D") Operations. These CAM objects use internal FreeCAD G-code dialect, independent of the CNC machine.
  * Export the job with a G-code, matching to your machine. This step is called _post processing_ ; there are different post processors available.

## General concepts

The CAM Workbench generates G-code defining the paths required to mill the
Project represented by the 3D model on the target mill in [the CAM Job
Operations FreeCAD G-code
dialect](/CAM_scripting#The_FreeCAD_Internal_GCode_Format "CAM scripting"),
which is later translated to the appropriate dialect for the target CNC
controller by selecting the appropriate postprocessor.

The G-code is generated from directives and Operations contained in a CAM Job.
The Job Workflow lists these in the order they will be executed. The list is
populated by adding CAM Operations, Path Dressups, Supplemental Commands, and
Path Modifications from the CAM Menu, or GUI buttons.

The CAM Workbench provides a Tool Manager (Library, Tool-Table), and G-code
Inspection, and Simulation tools. It links the Postprocessor, and allows
importing and exporting Job Templates.

The CAM Workbench has external dependencies including:

  1. The FreeCAD 3D model units are defined in the **Edit → Preference → General → Default unit system**. The Postprocessor configuration defines the final G-code units.
  2. The Macro file path, and Geometric tolerances, are defined in the **Edit → Preferences → CAM → Job Preferences** tab.
  3. Colors are defined in the **Edit → Preferences → CAM → GUI** tab.
  4. Holding tag parameters are defined in the **Edit → Preferences → CAM → Dressups** tab.
  5. That the Base 3D model quality supports the CAM workbench requirements, passes Check Geometry.

## Limitations

Some current limitations of which you should be aware are:

  * Most of the CAM Tools are not true 3D tools but only 2.5D capable. This means that they take a fixed 2D shape and can cut it down to a given depth. However, there are two tools which produce true 3D paths: [![](/images/7/7b/CAM_3DPocket.svg)](/index.php?title=File:CAM_3DPocket.svg&filetimestamp=20240316110553&) [3D Pocket](/CAM_Pocket_3D "CAM Pocket 3D") and [![](/images/d/dc/CAM_Surface.svg)](/index.php?title=File:CAM_Surface.svg&filetimestamp=20240316161123&) [3D Surface](/CAM_Surface "CAM Surface") (which is still an [experimental feature](/CAM_experimental "CAM experimental") as of November 2020).
  * Most of CAM workbench is designed for a simple, standard 3-axis (xyz) CNC mill/router, but lathe tools are under development in 0.19_pre.
  * Most operations in CAM workbench will return paths based on a standard endmill tool/bit only, regardless of the tool/bit type assigned in a given tool controller with the exception of the [![](/images/4/44/CAM_Engrave.svg)](/index.php?title=File:CAM_Engrave.svg&filetimestamp=20240316111030&) [Engrave](/CAM_Engrave "CAM Engrave") and [![](/images/d/dc/CAM_Surface.svg)](/index.php?title=File:CAM_Surface.svg&filetimestamp=20240316161123&) [3D Surface](/CAM_Surface "CAM Surface") operations.
  * The operations within the CAM workbench are not aware of clamping mechanisms in use to secure the model to your machine. Consequently, please review and simulate the paths you generate prior to sending the code to your machine. If necessary, model your clamping mechanisms in FreeCAD in order to better inspect the paths generated. Look for possible collisions with clamps or other obstacles along the paths.

## Units

Unit handling in CAM can be confusing. There are several points to understand:

  1. FreeCAD base units for length and time are 'mm' and 's' respectively. Velocity is thus 'mm/s'. This is what FreeCAD stores internally regardless of anything else
  2. The default unit schema uses the default units. If you're using the default schema and you enter a feed rate without a unit string, it will get entered as 'mm/s'
  3. Most CNC machines expect feed rate in the form of either 'mm/min' or 'in/min'. Most post-processors will automatically convert the unit when generating gcode.

Schemas:

  1. Changing schema in preferences changes default unit string for the input fields. If you're a CAM user and prefer to design in metric, it's highly recommended that you use the "Metric Small Parts & CNC" schema. If you design in US units, either the Imperial Decimal and Building US will work.
  2. Changing your preferred unit schema will have no effect on output but will help avoid input errors.

Output:

  1. Generating the correct unit in output is the responsibility of the post-processor and is done only at that time.
  2. Machine output unit is completely unrelated to your selected unit schema.
  3. Post-processors produce either metric (G21) output, Imperial (G20) output or are configurable.
  4. Configurable post-processors default to metric (G21).
  5. If you want your configurable post-processor to output imperial G-code (G20), set the correct argument in your job output configuration (ie --inches for linuxcnc). This can be stored in a job template and set as your default template to make it automatic for all future jobs.

CAM Inspection:

  1. If you use the CAM Inspect tool to look at G-code, you will see it in 'mm/s' because it is not being post-processed.

## Heights and depths

Many of the commands have various heights and depths:

[![](/images/thumb/e/e4/Path-DepthsAndHeights.gif/500px-Path-
DepthsAndHeights.gif)](/index.php?title=File:Path-
DepthsAndHeights.gif&filetimestamp=20200118224712&)

Visual reference for Depth properties (settings)

## Commands

Some commands are experimental and not available by default. To enable them
see [CAM experimental](/CAM_experimental "CAM experimental").

### Project Commands

  * [![](/images/a/ad/CAM_Job.svg)](/index.php?title=File:CAM_Job.svg&filetimestamp=20240316111219&) [Job](/CAM_Job "CAM Job"): Creates a new CNC job.

  * [![](/images/7/70/CAM_Post.svg)](/index.php?title=File:CAM_Post.svg&filetimestamp=20240316111427&) [Post Process](/CAM_Post "CAM Post"): Exports a project to G-code.

  * [![](/images/7/7d/CAM_Sanity.svg)](/index.php?title=File:CAM_Sanity.svg&filetimestamp=20240316111518&) [Check the CAM job for common errors](/CAM_Sanity "CAM Sanity"): Checks the selected job for missing values.

  * [![](/images/5/55/CAM_ExportTemplate.svg)](/index.php?title=File:CAM_ExportTemplate.svg&filetimestamp=20240316111041&) [Export Template](/CAM_ExportTemplate "CAM ExportTemplate"): Export the current job as a template.

### Tool Commands

  * [![](/images/0/0f/CAM_Inspect.svg)](/index.php?title=File:CAM_Inspect.svg&filetimestamp=20240316111207&) [Inspect CAM Commands](/CAM_Inspect "CAM Inspect"): Shows the G-code for checking.

  * [![](/images/8/85/CAM_Simulator.svg)](/index.php?title=File:CAM_Simulator.svg&filetimestamp=20240316111612&) [CAM Simulator](/CAM_Simulator "CAM Simulator"): Shows the milling operation like it's done on the machine.

  * [![](/images/3/39/CAM_SimulatorGL.svg)](/index.php?title=File:CAM_SimulatorGL.svg&filetimestamp=20240524152657&) [CAM SimulatorGL](/CAM_SimulatorGL "CAM SimulatorGL"): Enables the new, improved CAM simulator. [introduced in 1.0](/Release_notes_1.0 "Release notes 1.0")

  * [![](/images/6/6d/CAM_SelectLoop.svg)](/index.php?title=File:CAM_SelectLoop.svg&filetimestamp=20240316111527&) [Finish Selecting Loop](/CAM_SelectLoop "CAM SelectLoop"): Completes a loop from two selected edges.

  * [![](/images/0/02/CAM_OpActiveToggle.svg)](/index.php?title=File:CAM_OpActiveToggle.svg&filetimestamp=20240316160831&) [Toggle the Active State of the Operation](/CAM_OpActiveToggle "CAM OpActiveToggle"): Activates or de-activates a path operation.

  * [![](/images/c/cd/CAM_ToolBitLibraryOpen.svg)](/index.php?title=File:CAM_ToolBitLibraryOpen.svg&filetimestamp=20240316160858&) [ToolBit Library editor](/CAM_ToolBitLibraryOpen "CAM ToolBitLibraryOpen"): Opens an editor to manage ToolBit libraries.

  * [![](/images/1/1d/CAM_ToolBitDock.svg)](/index.php?title=File:CAM_ToolBitDock.svg&filetimestamp=20240316160921&) [ToolBit Dock](/CAM_ToolBitDock "CAM ToolBitDock"): Toggles the ToolBit Dock.

### Basic Operations

  * [![](/images/3/3d/CAM_Profile.svg)](/index.php?title=File:CAM_Profile.svg&filetimestamp=20240316111447&) [Profile](/CAM_Profile "CAM Profile"): Creates a profile operation of the entire model, or from one or more selected faces or edges.

  * [![](/images/9/98/CAM_Pocket_Shape.svg)](/index.php?title=File:CAM_Pocket_Shape.svg&filetimestamp=20240316160940&) [Pocket Shape](/CAM_Pocket_Shape "CAM Pocket Shape"): Creates a pocketing operation from one or more selected pocket(s).

  * [![](/images/b/b6/CAM_Drilling.svg)](/index.php?title=File:CAM_Drilling.svg&filetimestamp=20240316111020&) [Drilling](/CAM_Drilling "CAM Drilling"): Performs a drilling cycle.

  * [![](/images/3/36/CAM_MillFace.svg)](/index.php?title=File:CAM_MillFace.svg&filetimestamp=20240316161005&) [Face](/CAM_MillFace "CAM MillFace"): Creates a surfacing path.

  * [![](/images/2/21/CAM_Helix.svg)](/index.php?title=File:CAM_Helix.svg&filetimestamp=20240316111146&) [Helix](/CAM_Helix "CAM Helix"): Creates a helical path.

  * [![](/images/f/f7/CAM_Adaptive.svg)](/index.php?title=File:CAM_Adaptive.svg&filetimestamp=20240316110626&) [Adaptive](/CAM_Adaptive "CAM Adaptive"): Creates an adaptive clearing and profiling operation.

  * [![](/images/3/3a/CAM_Slot.svg)](/index.php?title=File:CAM_Slot.svg&filetimestamp=20240316111622&) [Slot](/CAM_Slot "CAM Slot"): Creates a slotting operation from selected features or custom points. [_Experimental_](/CAM_experimental "CAM experimental").

  * [![](/images/4/44/CAM_Engrave.svg)](/index.php?title=File:CAM_Engrave.svg&filetimestamp=20240316111030&) [Engrave](/CAM_Engrave "CAM Engrave"): Creates an engraving path.

  * [![](/images/f/f5/CAM_Deburr.svg)](/index.php?title=File:CAM_Deburr.svg&filetimestamp=20240316110947&) [Deburr](/CAM_Deburr "CAM Deburr"): Creates a deburr path.

  * [![](/images/a/a5/CAM_Vcarve.svg)](/index.php?title=File:CAM_Vcarve.svg&filetimestamp=20240316111837&) [Vcarve](/CAM_Vcarve "CAM Vcarve"): Creates an engraving path using a V tool shape.

### 3D Operations

  * [![](/images/5/58/CAM_Pocket_3D.svg)](/index.php?title=File:CAM_Pocket_3D.svg&filetimestamp=20240316161050&) [3D Pocket](/CAM_Pocket_3D "CAM Pocket 3D"): Creates a path for a 3D pocket.

  * [![](/images/d/dc/CAM_Surface.svg)](/index.php?title=File:CAM_Surface.svg&filetimestamp=20240316161123&) [3D Surface](/CAM_Surface "CAM Surface"): Creates a path for a 3D surface. [_Experimental_](/CAM_experimental "CAM experimental").

  * [![](/images/b/b6/CAM_Waterline.svg)](/index.php?title=File:CAM_Waterline.svg&filetimestamp=20240316111846&) [Waterline](/CAM_Waterline "CAM Waterline"): Creates a waterline path for a 3D surface. [_Experimental_](/CAM_experimental "CAM experimental").

### Path Dressup

  * [![](/images/b/b1/CAM_DressupAxisMap.svg)](/index.php?title=File:CAM_DressupAxisMap.svg&filetimestamp=20240316160524&) [Axis Map](/CAM_DressupAxisMap "CAM DressupAxisMap"): Remaps one axis to another.

  * [![](/images/5/5f/CAM_DressupPathBoundary.svg)](/index.php?title=File:CAM_DressupPathBoundary.svg&filetimestamp=20240316160550&) [Boundary](/CAM_DressupPathBoundary "CAM DressupPathBoundary"): Adds a boundary dressup modification to a selected path.

  * [![](/images/d/df/CAM_DressupDogbone.svg)](/index.php?title=File:CAM_DressupDogbone.svg&filetimestamp=20240316160601&) [Dogbone](/CAM_DressupDogbone "CAM DressupDogbone"): Adds a dogbone dressup modification to a selected path.

  * [![](/images/9/91/CAM_DressupDragKnife.svg)](/index.php?title=File:CAM_DressupDragKnife.svg&filetimestamp=20240316160610&) [DragKnife](/CAM_DressupDragKnife "CAM DressupDragKnife"): Adds a dragknife dressup modification to a selected path.

  * [![](/images/f/f9/CAM_DressupLeadInOut.svg)](/index.php?title=File:CAM_DressupLeadInOut.svg&filetimestamp=20240316160626&) [LeadInOut](/CAM_DressupLeadInOut "CAM DressupLeadInOut"): Adds a lead-in and/or lead-out point to a selected path.

  * [![](/images/f/f2/CAM_DressupRampEntry.svg)](/index.php?title=File:CAM_DressupRampEntry.svg&filetimestamp=20240316160639&) [RampEntry](/CAM_DressupRampEntry "CAM DressupRampEntry"): Adds ramp entry dressup modification to a selected path.

  * [![](/images/b/b4/CAM_DressupTag.svg)](/index.php?title=File:CAM_DressupTag.svg&filetimestamp=20240316160650&) [Tag](/CAM_DressupTag "CAM DressupTag"): Adds a holding tag dressup modification to a selected path.

  * [![](/images/e/e7/CAM_DressupZCorrect.svg)](/index.php?title=File:CAM_DressupZCorrect.svg&filetimestamp=20240316160700&) [Z Depth Correction](/CAM_DressupZCorrect "CAM DressupZCorrect"): Corrects the Z depth using Probe Map.

### Supplemental Commands

  * [![](/images/a/a7/CAM_Fixture.svg)](/index.php?title=File:CAM_Fixture.svg&filetimestamp=20240316160750&) [Fixture](/CAM_Fixture "CAM Fixture"): Changes the fixture position.

  * [![](/images/f/f3/CAM_Comment.svg)](/index.php?title=File:CAM_Comment.svg&filetimestamp=20240316110851&) [Comment](/CAM_Comment "CAM Comment"): Inserts a comment in the G-code of a path.

  * [![](/images/2/25/CAM_Stop.svg)](/index.php?title=File:CAM_Stop.svg&filetimestamp=20240316111642&) [Stop](/CAM_Stop "CAM Stop"): Inserts a full stop of the machine.

  * [![](/images/2/27/CAM_Custom.svg)](/index.php?title=File:CAM_Custom.svg&filetimestamp=20240316110925&) [Custom](/CAM_Custom "CAM Custom"): Inserts custom G-code.

  * [![](/images/3/3a/CAM_Probe.svg)](/index.php?title=File:CAM_Probe.svg&filetimestamp=20240316111437&) [Probe](/CAM_Probe "CAM Probe"): Creates a Probing Grid from a job stock.

  * [![](/images/3/31/CAM_Shape.svg)](/index.php?title=File:CAM_Shape.svg&filetimestamp=20240316111546&) [From Shape](/CAM_Shape "CAM Shape"): Creates a path object from a selected Part object. [_Experimental_](/CAM_experimental "CAM experimental").

### Path Modification

  * [![](/images/4/4d/CAM_Copy.svg)](/index.php?title=File:CAM_Copy.svg&filetimestamp=20240316110912&) [Copy the operation in the job](/CAM_Copy "CAM Copy"): Creates a parametric Copy of a selected path object.

  * [![](/images/6/66/CAM_Array.svg)](/index.php?title=File:CAM_Array.svg&filetimestamp=20240316110714&) [Array](/CAM_Array "CAM Array"): Creates an array by duplicating a selected path.

  * [![](/images/f/f5/CAM_SimpleCopy.svg)](/index.php?title=File:CAM_SimpleCopy.svg&filetimestamp=20240316111559&) [Simple Copy](/CAM_SimpleCopy "CAM SimpleCopy"): Creates a non-parametric copy of a selected path object.

### Specialty Operations

  * [![](/images/7/74/CAM_ThreadMilling.svg)](/index.php?title=File:CAM_ThreadMilling.svg&filetimestamp=20240316111701&) [Thread Milling](/CAM_ThreadMilling "CAM ThreadMilling"): Creates a CAM Thread Milling operation from features of a base object. [_Experimental_](/CAM_experimental "CAM experimental").

### Miscellaneous

  * [![](/images/b/bb/CAM_Area.svg)](/index.php?title=File:CAM_Area.svg&filetimestamp=20240316110637&) [Area](/CAM_Area "CAM Area"): Creates a feature area from selected objects. [_Experimental_](/CAM_experimental "CAM experimental").

  * [![](/images/d/dd/CAM_Area_Workplane.svg)](/index.php?title=File:CAM_Area_Workplane.svg&filetimestamp=20240316110701&) [Area workplane](/CAM_Area_Workplane "CAM Area Workplane"): Creates a feature area workplane. [_Experimental_](/CAM_experimental "CAM experimental").

## ToolBit architecture

Manage tools, bits, and the Tool Library. Based on the ToolBit architecture.

  * [CAM Tools](/CAM_Tools "CAM Tools")
  * [CAM ToolShape](/CAM_ToolShape "CAM ToolShape")
  * [CAM ToolBit](/CAM_ToolBit "CAM ToolBit")
  * [CAM ToolBit Library](/CAM_ToolBit_Library "CAM ToolBit Library")
  * [CAM ToolController](/CAM_ToolController "CAM ToolController")

## Other

  * [CAM FAQ](/CAM_FAQ "CAM FAQ"): The CAM Workbench shares many concepts with other CAM software packages but has its own peculiarities. If something seems wrong this is a good place to start.
  * [CAM SetupSheet](/CAM_SetupSheet "CAM SetupSheet"): You can use a SetupSheet to customize how various property values for operations are calculated.
  * [CAM Postprocessor Customization](/CAM_Postprocessor_Customization "CAM Postprocessor Customization"): If you have a special machine which cannot use one of the available post-processors you may need to write your own post-processor.
  * [CAM fourth axis](/CAM_fourth_axis "CAM fourth axis"): Experimental four axis milling.

## Preferences

  * [![](/images/5/5c/Preferences-cam.svg)](/index.php?title=File:Preferences-cam.svg&filetimestamp=20240316111954&) [Preferences...](/CAM_Preferences "CAM Preferences"): Preferences available for the CAM Workbench.

## Scripting

See [CAM scripting](/CAM_scripting "CAM scripting").

## Tutorials

  * [CAM Walkthrough for the Impatient](/CAM_Walkthrough_for_the_Impatient "CAM Walkthrough for the Impatient"): a quick tutorial to get familiar with CAM.

## Videos

  * [FreeCAD Path: Custom paths with Python - Part 1 - 5](https://www.youtube.com/playlist?list=PLEuOia-QxyFKgzAeTyH62GKqWKVURiWJL): A playlist with a series of 5 videos in English by sliptonic. This series shows how to work with the CAM Workbench.
  * [FreeCAD CAM Path Workbench](https://www.youtube.com/playlist?list=PLUrr_kHPp4vhGdLlj6IemtF-OPUlRvSTC): A playlist with a series of 7 videos in English by CAD CAM Lessons.
  * [FreeCAD CAM CNC](https://www.youtube.com/playlist?list=PLUrr_kHPp4vh2n6DcIlegK4dEKIFjmISJ): A playlist with a series of 8 videos in English by CAD CAM Lessons.
  * Also see the [Computer-Aided Manufacturing (CAM) section](/Video_tutorials#Computer-Aided_Manufacturing_\(CAM\) "Video tutorials") of the [Video tutorials](/Video_tutorials "Video tutorials") wiki page.

## Roadmap

  * [CAM Development Roadmap](/CAM_Development_Roadmap "CAM Development Roadmap"): Read this if you are a developer and want to contribute to CAM.

  

![](/images/6/6f/Arrow-left.svg) ![](/images/0/05/Workbench_BIM.svg) [BIM
Workbench](/BIM_Workbench "BIM Workbench")

![](/images/9/91/Workbench_Draft.svg) [Draft Workbench](/Draft_Workbench
"Draft Workbench") ![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

Expand[![](/images/9/95/Workbench_CAM.svg)](/index.php?title=File:Workbench_CAM.svg&filetimestamp=20240316105021&)
CAM

  * **Project Commands:** [Job](/CAM_Job "CAM Job"), [Post Process](/CAM_Post "CAM Post"), [Check the CAM job for common errors](/CAM_Sanity "CAM Sanity"), [Export Template](/CAM_ExportTemplate "CAM ExportTemplate")

* * *

  * **Tool Commands:** [Inspect CAM Commands](/CAM_Inspect "CAM Inspect"), [CAM Simulator](/CAM_Simulator "CAM Simulator"), [Finish Selecting Loop](/CAM_SelectLoop "CAM SelectLoop"), [Toggle the Active State of the Operation](/CAM_OpActiveToggle "CAM OpActiveToggle"), [ToolBit Library editor](/CAM_ToolBitLibraryOpen "CAM ToolBitLibraryOpen"), [ToolBit Dock](/CAM_ToolBitDock "CAM ToolBitDock")

* * *

  * **Basic Operations:** [Profile](/CAM_Profile "CAM Profile"), [Pocket Shape](/CAM_Pocket_Shape "CAM Pocket Shape"), [Drilling](/CAM_Drilling "CAM Drilling"), [Face](/CAM_MillFace "CAM MillFace"), [Helix](/CAM_Helix "CAM Helix"), [Adaptive](/CAM_Adaptive "CAM Adaptive"), [Slot](/CAM_Slot "CAM Slot"), [Engrave](/CAM_Engrave "CAM Engrave"), [Deburr](/CAM_Deburr "CAM Deburr"), [Vcarve](/CAM_Vcarve "CAM Vcarve")

* * *

  * **3D Operations:** [3D Pocket](/CAM_Pocket_3D "CAM Pocket 3D"), [3D Surface](/CAM_Surface "CAM Surface"), [Waterline](/CAM_Waterline "CAM Waterline")

* * *

  * **CAM Dressup:** [Axis Map](/CAM_DressupAxisMap "CAM DressupAxisMap"), [Boundary](/CAM_DressupPathBoundary "CAM DressupPathBoundary"), [Dogbone](/CAM_DressupDogbone "CAM DressupDogbone"), [DragKnife](/CAM_DressupDragKnife "CAM DressupDragKnife"), [LeadInOut](/CAM_DressupLeadInOut "CAM DressupLeadInOut"), [RampEntry](/CAM_DressupRampEntry "CAM DressupRampEntry"), [Tag](/CAM_DressupTag "CAM DressupTag"), [Z Depth Correction](/CAM_DressupZCorrect "CAM DressupZCorrect")

* * *

  * **Supplemental Commands:** [Fixture](/CAM_Fixture "CAM Fixture"), [Comment](/CAM_Comment "CAM Comment"), [Stop](/CAM_Stop "CAM Stop"), [Custom](/CAM_Custom "CAM Custom"), [Probe](/CAM_Probe "CAM Probe"), [From Shape](/CAM_Shape "CAM Shape")

* * *

  * **CAM Modification:** [Copy the operation in the job](/CAM_Copy "CAM Copy"), [Array](/CAM_Array "CAM Array"), [Simple Copy](/CAM_SimpleCopy "CAM SimpleCopy")

* * *

  * **Specialty Operations:** [Thread Milling](/CAM_ThreadMilling "CAM ThreadMilling")

* * *

  * **Miscellaneous:** [Area](/CAM_Area "CAM Area"), [Area workplane](/CAM_Area_Workplane "CAM Area Workplane")

* * *

  * **ToolBit architecture:** [Tools](/CAM_Tools "CAM Tools"), [ToolShape](/CAM_ToolShape "CAM ToolShape"), [ToolBit](/CAM_ToolBit "CAM ToolBit"), [ToolBit Library](/CAM_ToolBit_Library "CAM ToolBit Library"), [ToolController](/CAM_ToolController "CAM ToolController")

* * *

  * **Additional:** [Preferences](/CAM_Preferences "CAM Preferences"), [Scripting](/CAM_scripting "CAM scripting")

Expand[![](/images/thumb/9/94/User_hub.png/24px-
User_hub.png)](/index.php?title=File:User_hub.png&filetimestamp=20190221145008&)
[User documentation](/User_hub "User hub")

  * **[Getting started](/Getting_started "Getting started")**
  * **Installation:** [Download](/Download "Download"), [Windows](/Installing_on_Windows "Installing on Windows"), [Linux](/Installing_on_Linux "Installing on Linux"), [Mac](/Installing_on_Mac "Installing on Mac"), [Additional components](/Installing_additional_components "Installing additional components"), [Docker](/Compile_on_Docker "Compile on Docker"), [AppImage](/AppImage "AppImage"), [Ubuntu Snap](/Ubuntu_Snap "Ubuntu Snap")
  * **Basics:** [About FreeCAD](/About_FreeCAD "About FreeCAD"), [Interface](/Interface "Interface"), [Mouse navigation](/Mouse_navigation "Mouse navigation"), [Selection methods](/Selection_methods "Selection methods"), [Object name](/Object_name "Object name"), [Preferences](/Preferences_Editor "Preferences Editor"), [Workbenches](/Workbenches "Workbenches"), [Document structure](/Document_structure "Document structure"), [Properties](/Property "Property"), [Help FreeCAD](/Help_FreeCAD "Help FreeCAD"), [Donate](/Donate "Donate")

* * *

  * **Help:** [Tutorials](/Tutorials "Tutorials"), [Video tutorials](/Video_tutorials "Video tutorials")
  * **[Workbenches](/Workbenches "Workbenches"):** [Std Base](/Std_Base "Std Base"), [Assembly](/Assembly_Workbench "Assembly Workbench"), [BIM](/BIM_Workbench "BIM Workbench"), CAM, [Draft](/Draft_Workbench "Draft Workbench"), [FEM](/FEM_Workbench "FEM Workbench"), [Inspection](/Inspection_Workbench "Inspection Workbench"), [Material](/Material_Workbench "Material Workbench"), [Mesh](/Mesh_Workbench "Mesh Workbench"), [OpenSCAD](/OpenSCAD_Workbench "OpenSCAD Workbench"), [Part](/Part_Workbench "Part Workbench"), [PartDesign](/PartDesign_Workbench "PartDesign Workbench"), [Points](/Points_Workbench "Points Workbench"), [Reverse Engineering](/Reverse_Engineering_Workbench "Reverse Engineering Workbench"), [Robot](/Robot_Workbench "Robot Workbench"), [Sketcher](/Sketcher_Workbench "Sketcher Workbench"), [Spreadsheet](/Spreadsheet_Workbench "Spreadsheet Workbench"), [Surface](/Surface_Workbench "Surface Workbench"), [TechDraw](/TechDraw_Workbench "TechDraw Workbench"), [Test Framework](/Testing "Testing")

* * *

  * **[Addons](/Addon "Addon"):** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

