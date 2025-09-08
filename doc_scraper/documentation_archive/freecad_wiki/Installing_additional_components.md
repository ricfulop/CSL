---
url: https://wiki.freecad.org/Installing_additional_components
title: Installing additional components
scraped_at: 2025-09-08 16:45:31
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Help files
  * 3 External workbenches
  * 4 Third party software Toggle Third party software subsection
    * 4.1 Support
      * 4.1.1 GitPython
      * 4.1.2 GraphViz
      * 4.1.3 OpenCAMLib
      * 4.1.4 OpenSCAD
    * 4.2 File formats
      * 4.2.1 CADExchanger
      * 4.2.2 DXF Importer
      * 4.2.3 DWG converters
      * 4.2.4 IfcOpenShell
      * 4.2.5 IfcJson
      * 4.2.6 Pycollada
    * 4.3 Rendering
      * 4.3.1 LuxCoreRender
      * 4.3.2 LuxRender
      * 4.3.3 POV-Ray
    * 4.4 Finite element
      * 4.4.1 CalculiX
      * 4.4.2 Gmsh
      * 4.4.3 Elmer
      * 4.4.4 FEniCS
      * 4.4.5 Z88
      * 4.4.6 OpenFOAM
  * 5 Related pages

# Installing additional components

  * [Page](/Installing_additional_components "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Installing_additional_components&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Installing_additional_components)
  * [Edit](/index.php?title=Installing_additional_components&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Installing_additional_components&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Installing_additional_components.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Installing_additional_components&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Installing_additional_components)
  * [Edit](/index.php?title=Installing_additional_components&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Installing_additional_components&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Installing_additional_components&action=history)

General

  * [What links here](/Special:WhatLinksHere/Installing_additional_components "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Installing_additional_components "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Installing_additional_components&oldid=1583353 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Installing_additional_components&action=info "More information about this page")

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Installing_additional_components&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Installing+additional+components&action=page&filter=&language=en)This is the
approved revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Installing+additional+components&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/Installing_additional_components/id "Installing \(2% translated\)")
  * [Deutsch](/Installing_additional_components/de "Installieren zusätzlicher Komponenten \(100% translated\)")
  * English
  * [español](/Installing_additional_components/es "Instalación de componentes adicionales \(81% translated\)")
  * [français](/Installing_additional_components/fr "Installer des logiciels supplémentaires \(100% translated\)")
  * [hrvatski](/Installing_additional_components/hr "Instalacija \(2% translated\)")
  * [italiano](/Installing_additional_components/it "Installare componenti aggiuntivi \(100% translated\)")
  * [polski](/Installing_additional_components/pl "Instalacja dodatkowych komponentów \(100% translated\)")
  * [português](/Installing_additional_components/pt "Installing \(2% translated\)")
  * [português do Brasil](/Installing_additional_components/pt-br "Instalação de componentes adicionais \(76% translated\)")
  * [română](/Installing_additional_components/ro "Instalare \(2% translated\)")
  * [svenska](/Installing_additional_components/sv "Installing \(2% translated\)")
  * [čeština](/Installing_additional_components/cs "Instalace \(2% translated\)")
  * [български](/Installing_additional_components/bg "Инсталация \(2% translated\)")
  * [русский](/Installing_additional_components/ru "Установка дополнительных компонентов \(84% translated\)")
  * [中文（中国大陆）](/Installing_additional_components/zh-cn "安装 \(2% translated\)")
  * [日本語](/Installing_additional_components/ja "付加機能のインストール \(7% translated\)")
  * [한국어](/Installing_additional_components/ko "추가 기능 설치하기 \(47% translated\)")

![](/images/6/6f/Arrow-left.svg) [Installing on Mac](/Installing_on_Mac
"Installing on Mac")

[Getting started](/Getting_started "Getting started") ![](/images/a/af/Arrow-
right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

# Introduction

After installing FreeCAD for your operating system
([Windows](/Installing_on_Windows "Installing on Windows"),
[Linux](/Installing_on_Linux "Installing on Linux") or
[Mac](/Installing_on_Mac "Installing on Mac")), you may want to consider
installing one or more of the following additional components.

# Help files

See [Installing Helpfile](/Installing_Helpfile "Installing Helpfile").

# External workbenches

Apart from the default [workbenches](/Workbenches "Workbenches") bundled with
FreeCAD, there is a large collection of useful [external
workbenches](/External_workbenches "External workbenches") made by community
members.

# Third party software

FreeCAD supports several third party software packages out of the box. In many
cases all you need to do is install the software, and when FreeCAD is
restarted it will automatically find and be able to use it. This section aims
to provide a list of such software packages, together with some information
about where they are used in FreeCAD and where they can be downloaded.

## Support

### GitPython

[GitPython](https://github.com/gitpython-developers/GitPython) is a library to
interact with Git repositories. The [Addon Manager](/Std_AddonMgr "Std
AddonMgr") can use this library. GitPython is included in the FreeCAD
installers for Windows and Mac.

### GraphViz

[GraphViz](https://www.graphviz.org) is an open source graph visualization
software. It is used by the [Std DependencyGraph](/Std_DependencyGraph "Std
DependencyGraph") tool.

### OpenCAMLib

[OpenCAMLib](https://www.anderswallin.net/CAM) is an open source library of
computer aided manufacturing (CAM) algorithms. It is used in the [CAM
Workbench](/CAM_Workbench "CAM Workbench"). See the [OpenCamLib](/OpenCamLib
"OpenCamLib") page for installation instructions.

### OpenSCAD

[OpenSCAD](https://www.openscad.org) is a solid 3D modeller. The [OpenSCAD
Workbench](/OpenSCAD_Workbench "OpenSCAD Workbench") depends on this software
and the [Mesh Workbench](/Mesh_Workbench "Mesh Workbench") uses it for its
Boolean tools. It is also required for the import of SCAD files with the [Std
Import](/Std_Import "Std Import") tool.

## File formats

All software in this section will be used by the [Std Import](/Std_Import "Std
Import") or [Std Export](/Std_Export "Std Export") tools.

### CADExchanger

[CADExchanger](https://cadexchanger.com) is a commercial application for
exchanging various CAD file formats. There is an [external
workbench](https://github.com/yorikvanhavre/CADExchanger) to use this
application in FreeCAD.

### DXF Importer

FreeCAD has a native importer and exporter for DXF files, programmed in C++.
Currently they do not implement all features of the DXF format. For those
features the legacy Python importer and exporter are still available. These
require the [Draft-dxf-importer](https://github.com/yorikvanhavre/Draft-dxf-
importer) Python library. See the [FreeCAD and DXF
Import](/FreeCAD_and_DXF_Import "FreeCAD and DXF Import") page for more
information.

### DWG converters

FreeCAD cannot directly read and write DWG files. To convert DXF files to DWG
files, and vice-versa, FreeCAD relies on external converters. There is built-
in support for the following DWG converters:

  * [LibreDWG](https://www.gnu.org/software/libredwg) (open-source, lacks support for some DWG entities).
  * [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter) (free, but not open-source).
  * [QCAD pro](https://qcad.org/en/qcad-command-line-tools#dwg2dwg) (commercial). [introduced in 0.20](/Release_notes_0.20 "Release notes 0.20")

See [Import Export Preferences](/Import_Export_Preferences#DWG "Import Export
Preferences") and [FreeCAD and DWG Import](/FreeCAD_and_DWG_Import "FreeCAD
and DWG Import") for more information.

### IfcOpenShell

[IfcOpenShell](https://ifcopenshell.org) is a library for working with the
Industry Foundation Classes (IFC) file format used in architectural design.
The library is also used by the [Arch IfcExplorer](/Arch_IfcExplorer "Arch
IfcExplorer") (0.18 and below) and [BIM IfcExplorer](/BIM_IfcExplorer "BIM
IfcExplorer") tools. IfcOpenShell is included in the FreeCAD installers for
Windows and Mac.

### IfcJson

[IfcJson](https://github.com/buildingSMART/ifcJSON) is a library required for
exporting to the IFCJSON file format. IFCJSON is a new IFC format that is not
yet supported by many applications.

### Pycollada

[Pycollada](https://github.com/pycollada/pycollada/releases), also known as
python-collada, is a Python library to read and write Collada (DAE) files.
Pycollada is included in the FreeCAD installers for Windows and Mac.

## Rendering

### LuxCoreRender

[LuxCoreRender](https://www.luxcorerender.org) is a render engine, reboot of
the [LuxRender](/LuxRender "LuxRender") project. Officially it is not
supported by the [Raytracing Workbench](/Raytracing_Workbench "Raytracing
Workbench"), but it might be worth to give it a try. It is officially
supported by the new [Render Workbench](https://github.com/FreeCAD/FreeCAD-
render), intended as a future replacement of the Raytracing Workbench. See the
[LuxCoreRender](/LuxCoreRender "LuxCoreRender") page for more information and
installation instructions.

### LuxRender

[LuxRender](https://luxcorerender.org/history/) is one of the two render
engines supported by the [Raytracing Workbench](/Raytracing_Workbench
"Raytracing Workbench"). In 2013 the project has been rebooted becoming
[LuxCoreRender](/LuxCoreRender "LuxCoreRender"), with a major code rewriting
and compatibility breaking changes. Officially the Raytracing Workbench only
supports the abandoned [LuxRender](/LuxRender "LuxRender") (latest version is
1.6, 2017-12-28), while the new [Render
Workbench](https://github.com/FreeCAD/FreeCAD-render) (intended as a future
replacement of the Raytracing Workbench) supports instead LuxCoreRender and
has dropped the support for LuxRender. Anyway, even if officially not
supported, [LuxCoreRender](/LuxCoreRender "LuxCoreRender") may work with the
Raytracing Workbench, it might be worth to give it a try. See the
[LuxRender](/LuxRender "LuxRender") page for more information and installation
instructions, and the [LuxCoreRender](/LuxCoreRender "LuxCoreRender") if you
want to try a more modern software.

### POV-Ray

[POV-Ray](https://www.povray.org) is a well-known ray-tracer which can render
photo-realistic images. It is one of two render engines currently supported by
the [Raytracing Workbench](/Raytracing_Workbench "Raytracing Workbench"). See
the [POV-Ray](/POV-Ray "POV-Ray") page for more information and installation
instructions.

## Finite element

### CalculiX

[CalculiX](https://calculix.de) is a suite of two finite element packages:
CalculiX CrunchiX, a FEM solver, and CalculiX GraphiX, a GUI frontend. Only
the solver is supported by FreeCAD. It is used by the [FEM
SolverCalculixCcxtools](/FEM_SolverCalculixCcxtools "FEM
SolverCalculixCcxtools") tool.

### Gmsh

[Gmsh](https://gmsh.info) is an automatic finite element mesh generator. it is
used by the [FEM MeshGmshFromShape](/FEM_MeshGmshFromShape "FEM
MeshGmshFromShape") and [Mesh FromPartShape](/Mesh_FromPartShape "Mesh
FromPartShape") tools.

### Elmer

[Elmer](https://www.csc.fi/web/elmer) is a multi-physics simulation software,
which was open sourced in 2005. In FreeCAD its Grid and Solver modules are
used by the [FEM SolverElmer](/FEM_SolverElmer "FEM SolverElmer") tool.

### FEniCS

[FEniCS](https://fenicsproject.org) is a computing platform to solve partial
differential equations (PDEs), which are widely used when solving FEM
problems. It is used by the [FEM workbench](/FEM_Workbench "FEM Workbench")

### Z88

[Z88](https://en.z88.de) is another FEM program, containing a mesher, a solver
and converters. It is used by the [FEM SolverZ88](/FEM_SolverZ88 "FEM
SolverZ88") tool. FreeCAD requires the open source Z88OS package.

### OpenFOAM

[OpenFOAM](https://openfoam.org) is a large collection of libraries for
computational fluid dynamics (CFD) simulations. OpenFOAM is used by the
[Cfd](/Cfd_Workbench "Cfd Workbench") and
[CfdOF](https://github.com/jaheyns/CfdOF) [external
workbenches](/External_workbenches "External workbenches").

# Related pages

  * [Import Export](/Import_Export "Import Export")
  * [Import Export Preferences](/Import_Export_Preferences "Import Export Preferences")
  * [Third Party Libraries](/Third_Party_Libraries "Third Party Libraries")

  

![](/images/6/6f/Arrow-left.svg) [Installing on Mac](/Installing_on_Mac
"Installing on Mac")

[Getting started](/Getting_started "Getting started") ![](/images/a/af/Arrow-
right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

