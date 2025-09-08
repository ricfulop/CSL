---
url: https://wiki.freecad.org/Workbenches
title: Workbenches
scraped_at: 2025-09-08 16:43:50
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Built-in workbenches Toggle Built-in workbenches subsection
    * 1.1 Current
    * 1.2 Obsolete
  * 2 External workbenches

# Workbenches

  * [Page](/Workbenches "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Workbenches&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Workbenches)
  * [Edit](/index.php?title=Workbenches&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Workbenches&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Workbenches.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Workbenches&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Workbenches)
  * [Edit](/index.php?title=Workbenches&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Workbenches&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Workbenches&action=history)

General

  * [What links here](/Special:WhatLinksHere/Workbenches "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Workbenches "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Workbenches&oldid=1540514 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Workbenches&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Workbenches&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Workbenches&action=page&filter=&language=en)This is the approved revision of
this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Workbenches&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/Workbenches/id "Workbenches \(2% translated\)")
  * [Deutsch](/Workbenches/de "Arbeitsbereiche \(100% translated\)")
  * English
  * [Türkçe](/Workbenches/tr "Tezgahlar \(12% translated\)")
  * [español](/Workbenches/es "Bancos de Trabajo \(44% translated\)")
  * [français](/Workbenches/fr "Ateliers \(100% translated\)")
  * [hrvatski](/Workbenches/hr "Radne površine \(12% translated\)")
  * [italiano](/Workbenches/it "Ambienti di Lavoro \(100% translated\)")
  * [magyar](/Workbenches/hu "Workbenches \(2% translated\)")
  * [polski](/Workbenches/pl "Środowiska pracy \(100% translated\)")
  * [português](/Workbenches/pt "Workbenches \(37% translated\)")
  * [português do Brasil](/Workbenches/pt-br "Bancadas de trabalho \(98% translated\)")
  * [română](/Workbenches/ro "Ateliere \(12% translated\)")
  * [suomi](/Workbenches/fi "Workbenches \(2% translated\)")
  * [svenska](/Workbenches/sv "Workbenches \(5% translated\)")
  * [čeština](/Workbenches/cs "Pracovní plochy \(5% translated\)")
  * [български](/Workbenches/bg "Workbenches \(2% translated\)")
  * [русский](/Workbenches/ru "Верстаки \(100% translated\)")
  * [українська](/Workbenches/uk "Workbenches \(2% translated\)")
  * [中文](/Workbenches/zh "工作台 \(17% translated\)")
  * [中文（中国大陆）](/Workbenches/zh-cn "工作台 \(15% translated\)")
  * [中文（繁體）](/Workbenches/zh-hant "Workbenches \(2% translated\)")
  * [中文（臺灣）](/Workbenches/zh-tw "工作台 \(2% translated\)")
  * [日本語](/Workbenches/ja "ワークベンチ \(85% translated\)")
  * [한국어](/Workbenches/ko "작업대\(Workbench\) \(78% translated\)")

![](/images/6/6f/Arrow-left.svg) [Property editor](/Property_editor "Property
editor")

![](/images/0/06/Freecad.svg) [Std Base](/Std_Base "Std Base")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

FreeCAD, like many modern design applications such as
[Revit](https://en.wikipedia.org/wiki/Autodesk_Revit) or
[CATIA](https://en.wikipedia.org/wiki/CATIA), is based on the concept of
[Workbench](https://en.wikipedia.org/wiki/Workbench). A workbench can be
considered as a set of tools specially grouped for a certain task. In a
traditional furniture workshop, you would have a work table for the person who
works with wood, another one for the one who works with metal pieces, and
maybe a third one for the guy who mounts all the pieces together.

In FreeCAD, the same concept applies. Tools are grouped into workbenches
according to the tasks they are related to.

When you switch from one workbench to another, the tools available on the
interface change. Toolbars, command bars and possibly other parts of the
interface switch to the new workbench, but the contents of your scene doesn't
change. You could, for example, start drawing 2D shapes with the Draft
Workbench, then work further on them with the Part Workbench.

Note that sometimes a Workbench is referred to as a _Module_. However,
Workbenches and Modules are different entities. A Module is any extension of
FreeCAD, while a Workbench is a special type of Module with a GUI
configuration (toolbars and menus).

## Built-in workbenches

### Current

The following workbenches are bundled with every FreeCAD installation:

  * [![](/images/0/06/Freecad.svg)](/index.php?title=File:Freecad.svg&filetimestamp=20240704193018&) [Std Base](/Std_Base "Std Base"). This is not really a workbench, but rather a category of 'standard' commands and tools that can be used in all workbenches.

  * [![](/images/c/cd/Workbench_Assembly.svg)](/index.php?title=File:Workbench_Assembly.svg&filetimestamp=20240325203121&) The [Assembly Workbench](/Assembly_Workbench "Assembly Workbench") for building and solving mechanical assemblies. [introduced in 1.0](/Release_notes_1.0 "Release notes 1.0")

  * [![](/images/0/05/Workbench_BIM.svg)](/index.php?title=File:Workbench_BIM.svg&filetimestamp=20240524155736&) The [BIM Workbench](/BIM_Workbench "BIM Workbench") for working with architectural elements and creating [BIM](https://en.wikipedia.org/wiki/Building_information_modeling) models. It combines the Arch Workbench and the formerly external BIM Workbench available in 0.21 and below.

  * [![](/images/9/95/Workbench_CAM.svg)](/index.php?title=File:Workbench_CAM.svg&filetimestamp=20240316105021&) The [CAM Workbench](/CAM_Workbench "CAM Workbench") is used to produce G-Code instructions. This workbench was called "Path Workbench" in 0.21 and below.

  * [![](/images/9/91/Workbench_Draft.svg)](/index.php?title=File:Workbench_Draft.svg&filetimestamp=20200404172706&) The [Draft Workbench](/Draft_Workbench "Draft Workbench") contains 2D tools and basic 2D and 3D CAD operations.

  * [![](/images/8/87/Workbench_FEM.svg)](/index.php?title=File:Workbench_FEM.svg&filetimestamp=20240405093343&) The [FEM Workbench](/FEM_Workbench "FEM Workbench") provides Finite Element Analysis (FEA) workflow.

  * [![](/images/f/f8/Workbench_Inspection.svg)](/index.php?title=File:Workbench_Inspection.svg&filetimestamp=20200404172947&) The [Inspection Workbench](/Inspection_Workbench "Inspection Workbench") is made to give you specific tools for examination of shapes. Still in the early stages of development.

  * [![](/images/e/e2/Workbench_Material.svg)](/index.php?title=File:Workbench_Material.svg&filetimestamp=20240623140009&) The [Material Workbench](/Material_Workbench "Material Workbench") handles the FreeCAD material system. [introduced in 1.0](/Release_notes_1.0 "Release notes 1.0")

  * [![](/images/8/84/Workbench_Mesh.svg)](/index.php?title=File:Workbench_Mesh.svg&filetimestamp=20200404173024&) The [Mesh Workbench](/Mesh_Workbench "Mesh Workbench") for working with triangulated meshes.

  * [![](/images/4/4e/Workbench_OpenSCAD.svg)](/index.php?title=File:Workbench_OpenSCAD.svg&filetimestamp=20200404173116&) The [OpenSCAD Workbench](/OpenSCAD_Workbench "OpenSCAD Workbench") for interoperability with OpenSCAD and repairing [constructive solid geometry](/Constructive_solid_geometry "Constructive solid geometry") (CSG) model history.

  * [![](/images/0/04/Workbench_Part.svg)](/index.php?title=File:Workbench_Part.svg&filetimestamp=20240712190040&) The [Part Workbench](/Part_Workbench "Part Workbench") for working with geometric primitives and boolean operations.

  * [![](/images/3/39/Workbench_PartDesign.svg)](/index.php?title=File:Workbench_PartDesign.svg&filetimestamp=20240405092932&) The [Part Design Workbench](/PartDesign_Workbench "PartDesign Workbench") for building Part shapes from sketches.

  * [![](/images/6/6c/Workbench_Points.svg)](/index.php?title=File:Workbench_Points.svg&filetimestamp=20200404174800&) The [Points Workbench](/Points_Workbench "Points Workbench") for working with point clouds.

  * [![](/images/8/83/Workbench_Reverse_Engineering.svg)](/index.php?title=File:Workbench_Reverse_Engineering.svg&filetimestamp=20200404173756&) The [Reverse Engineering Workbench](/Reverse_Engineering_Workbench "Reverse Engineering Workbench") is intended to provide specific tools to convert shapes/solids/meshes into parametric FreeCAD-compatible features.

  * [![](/images/e/e3/Workbench_Robot.svg)](/index.php?title=File:Workbench_Robot.svg&filetimestamp=20200404173908&) The [Robot Workbench](/Robot_Workbench "Robot Workbench") for studying robot movements. Currently unmaintained.

  * [![](/images/9/91/Workbench_Sketcher.svg)](/index.php?title=File:Workbench_Sketcher.svg&filetimestamp=20231231194727&) The [Sketcher Workbench](/Sketcher_Workbench "Sketcher Workbench") for working with geometry-constrained sketches.

  * [![](/images/b/be/Workbench_Spreadsheet.svg)](/index.php?title=File:Workbench_Spreadsheet.svg&filetimestamp=20240527155805&) The [Spreadsheet Workbench](/Spreadsheet_Workbench "Spreadsheet Workbench") for creating and manipulating spreadsheet data.

  * [![](/images/b/bf/Workbench_Surface.svg)](/index.php?title=File:Workbench_Surface.svg&filetimestamp=20210130230011&) The [Surface Workbench](/Surface_Workbench "Surface Workbench") provides tools to create and modify surfaces. It is similar to the [Part Builder](/Part_Builder "Part Builder") Face from edges option.

  * [![](/images/b/b6/Workbench_TechDraw.svg)](/index.php?title=File:Workbench_TechDraw.svg&filetimestamp=20240713144548&) The [TechDraw Workbench](/TechDraw_Workbench "TechDraw Workbench") for producing technical drawings from 3D models. It is the successor of the [Drawing Workbench](/Drawing_Workbench "Drawing Workbench").

  * [![](/images/b/bf/Workbench_Test.svg)](/index.php?title=File:Workbench_Test.svg&filetimestamp=20200404174253&) The [Test Framework Workbench](/Testing "Testing") is for debugging FreeCAD.

### Obsolete

The following workbenches are no longer included after version 0.21:

  * [![](/images/e/eb/Workbench_Start.svg)](/index.php?title=File:Workbench_Start.svg&filetimestamp=20200404174126&) The [Start Workbench](/Start_Workbench "Start Workbench") allows you to quickly jump to one of the most common workbenches. This workbench has been replaced by the Start page that can be accessed via the [Help menu](/Std_Help_Menu "Std Help Menu").

  * [![](/images/3/3e/Workbench_Web.svg)](/index.php?title=File:Workbench_Web.svg&filetimestamp=20200404174327&) The [Web Workbench](/Web_Workbench "Web Workbench") provides you with a browser window instead of the [3D view](/3D_view "3D view") within FreeCAD.

The following workbenches are no longer included after version 0.20:

  * [![](/images/0/0a/Workbench_Drawing.svg)](/index.php?title=File:Workbench_Drawing.svg&filetimestamp=20200404172745&) The [Drawing Workbench](/Drawing_Workbench "Drawing Workbench") was used for producing technical drawings. The [TechDraw Workbench](/TechDraw_Workbench "TechDraw Workbench") is its more advanced replacement.

  * [![](/images/d/de/Workbench_Image.svg)](/index.php?title=File:Workbench_Image.svg&filetimestamp=20200404172907&) The [Image Workbench](/Image_Workbench "Image Workbench") was used for working with bitmap images. Its functionality has been integrated in [Std Base](/Std_Base "Std Base"). See [Std Import](/Std_Import "Std Import") and [Std ViewLoadImage](/Std_ViewLoadImage "Std ViewLoadImage").

  * [![](/images/a/aa/Workbench_Raytracing.svg)](/index.php?title=File:Workbench_Raytracing.svg&filetimestamp=20200404173709&) The [Raytracing Workbench](/Raytracing_Workbench "Raytracing Workbench") was used for ray-tracing (rendering). The external [Render Workbench](https://github.com/FreeCAD/FreeCAD-render) should be used instead.

## External workbenches

FreeCAD workbenches are easy to program in [Python](/Python "Python"), there
are therefore many people developing additional workbenches outside of the
FreeCAD main development area.

The [external workbenches](/External_workbenches "External workbenches") page
lists all that are known to this community. Most are easily installable from
within FreeCAD, using the [Addon Manager](/Std_AddonMgr "Std AddonMgr"), found
under menu **Tools
→[![](/images/e/ee/Std_AddonMgr.svg)](/index.php?title=File:Std_AddonMgr.svg&filetimestamp=20240704212012&)
Addon manager**.

  

![](/images/6/6f/Arrow-left.svg) [Property editor](/Property_editor "Property
editor")

![](/images/0/06/Freecad.svg) [Std Base](/Std_Base "Std Base")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

Expand[![](/images/thumb/9/94/User_hub.png/24px-
User_hub.png)](/index.php?title=File:User_hub.png&filetimestamp=20190221145008&)
[User documentation](/User_hub "User hub")

  * **[Getting started](/Getting_started "Getting started")**
  * **Installation:** [Download](/Download "Download"), [Windows](/Installing_on_Windows "Installing on Windows"), [Linux](/Installing_on_Linux "Installing on Linux"), [Mac](/Installing_on_Mac "Installing on Mac"), [Additional components](/Installing_additional_components "Installing additional components"), [Docker](/Compile_on_Docker "Compile on Docker"), [AppImage](/AppImage "AppImage"), [Ubuntu Snap](/Ubuntu_Snap "Ubuntu Snap")
  * **Basics:** [About FreeCAD](/About_FreeCAD "About FreeCAD"), [Interface](/Interface "Interface"), [Mouse navigation](/Mouse_navigation "Mouse navigation"), [Selection methods](/Selection_methods "Selection methods"), [Object name](/Object_name "Object name"), [Preferences](/Preferences_Editor "Preferences Editor"), Workbenches, [Document structure](/Document_structure "Document structure"), [Properties](/Property "Property"), [Help FreeCAD](/Help_FreeCAD "Help FreeCAD"), [Donate](/Donate "Donate")

* * *

  * **Help:** [Tutorials](/Tutorials "Tutorials"), [Video tutorials](/Video_tutorials "Video tutorials")
  * **Workbenches:** [Std Base](/Std_Base "Std Base"), [Assembly](/Assembly_Workbench "Assembly Workbench"), [BIM](/BIM_Workbench "BIM Workbench"), [CAM](/CAM_Workbench "CAM Workbench"), [Draft](/Draft_Workbench "Draft Workbench"), [FEM](/FEM_Workbench "FEM Workbench"), [Inspection](/Inspection_Workbench "Inspection Workbench"), [Material](/Material_Workbench "Material Workbench"), [Mesh](/Mesh_Workbench "Mesh Workbench"), [OpenSCAD](/OpenSCAD_Workbench "OpenSCAD Workbench"), [Part](/Part_Workbench "Part Workbench"), [PartDesign](/PartDesign_Workbench "PartDesign Workbench"), [Points](/Points_Workbench "Points Workbench"), [Reverse Engineering](/Reverse_Engineering_Workbench "Reverse Engineering Workbench"), [Robot](/Robot_Workbench "Robot Workbench"), [Sketcher](/Sketcher_Workbench "Sketcher Workbench"), [Spreadsheet](/Spreadsheet_Workbench "Spreadsheet Workbench"), [Surface](/Surface_Workbench "Surface Workbench"), [TechDraw](/TechDraw_Workbench "TechDraw Workbench"), [Test Framework](/Testing "Testing")

* * *

  * **[Addons](/Addon "Addon"):** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

