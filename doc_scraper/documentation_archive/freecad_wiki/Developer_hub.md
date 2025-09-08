---
url: https://wiki.freecad.org/Developer_hub
title: Developer hub
scraped_at: 2025-09-08 16:44:42
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Developer Documentation Toggle Developer Documentation subsection
    * 1.1 Compiling FreeCAD
    * 1.2 Packaging
    * 1.3 Build Support Tools
    * 1.4 Modifying FreeCAD
    * 1.5 Module developer's guide
    * 1.6 Internals
      * 1.6.1 OpenCascade Documentation
      * 1.6.2 File format
      * 1.6.3 Sketcher solver
  * 2 Roadmap
  * 3 Community
  * 4 Credits

# Developer hub

  * [Page](/Developer_hub "View the content page \[ctrl-option-c\]")
  * [Discussion](/Talk:Developer_hub "Discussion about the content page \[ctrl-option-t\]")

English

  * [Read](/Developer_hub)
  * [Edit](/index.php?title=Developer_hub&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Developer_hub&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Developer_hub.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Developer_hub&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Developer_hub)
  * [Edit](/index.php?title=Developer_hub&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Developer_hub&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Developer_hub&action=history)

General

  * [What links here](/Special:WhatLinksHere/Developer_hub "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Developer_hub "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Developer_hub&oldid=1626548 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Developer_hub&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Developer_hub&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Developer+hub&action=page&filter=&language=en)This is the approved revision of
this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Developer+hub&language=&task=view "Start translation for this language")
  * [Deutsch](/Developer_hub/de "Entwicklerzentrum \(100% translated\)")
  * English
  * [español](/Developer_hub/es "Centro de desarrolladores \(73% translated\)")
  * [français](/Developer_hub/fr "Documentation pour développeurs \(100% translated\)")
  * [hrvatski](/Developer_hub/hr "Programersko okruženje \(3% translated\)")
  * [italiano](/Developer_hub/it "Hub degli sviluppatori di FreeCAD \(84% translated\)")
  * [polski](/Developer_hub/pl "Centrum programisty \(100% translated\)")
  * [português](/Developer_hub/pt "Developer hub \(3% translated\)")
  * [português do Brasil](/Developer_hub/pt-br "Documentação para desenvolvedores \(84% translated\)")
  * [română](/Developer_hub/ro "Hub Dezvoltatori \(8% translated\)")
  * [svenska](/Developer_hub/sv "Developer hub \(3% translated\)")
  * [čeština](/Developer_hub/cs "Vývojářské centrum \(3% translated\)")
  * [русский](/Developer_hub/ru "Центр разработчиков \(46% translated\)")
  * [中文（中国大陆）](/Developer_hub/zh-cn "开发者中心 \(100% translated\)")
  * [日本語](/Developer_hub/ja "開発者向けハブ \(3% translated\)")
  * [한국어](/Developer_hub/ko "개발자 허브 \(8% translated\)")

[![](/images/thumb/0/0b/Crystal_Clear_app_tutorials.png/64px-
Crystal_Clear_app_tutorials.png)](/index.php?title=File:Crystal_Clear_app_tutorials.png&filetimestamp=20090202153438&)

* * *

This is the place to come if you want to contribute to the development of the
FreeCAD software. Many of the following pages might be outdated. Check the
official FreeCAD Developers Handbook for more up to date information:
<https://freecad.github.io/DevelopersHandbook/>

These pages are in the early stage of development. If you can't find the
information you are looking for, or have found useful information somewhere we
have not linked to, then please leave a comment on the
[forum](https://forum.freecad.org/index.php?sid=5f84150e79db8842e277b042077097ff)
and someone will look into it.

## Developer Documentation

The developer documentation comprises the following sections:

### Compiling FreeCAD

  * [GitHub repo](https://github.com/FreeCAD/FreeCAD): If you are new to git, read [Source code management](/Source_code_management "Source code management")
  * [Compile on Docker](/Compile_on_Docker "Compile on Docker")
  * [Compiling on Windows](/Compile_on_Windows "Compile on Windows")
  * [Compiling on Linux](/Compile_on_Linux "Compile on Linux")
  * [Compiling on MacOS](/Compile_on_MacOS "Compile on MacOS")
  * [License details](/License "License"): About the FreeCAD licences and allowed uses of the source code and application.
  * [Logo and other assets](/Logo "Logo"): How the FreeCAD logo and other assets of FreeCAD should be used.
  * [Third Party Libraries](/Third_Party_Libraries "Third Party Libraries")
  * [Third Party Tools](/Third_Party_Tools "Third Party Tools")
  * [Start up and Configuration](/Start_up_and_Configuration "Start up and Configuration")
  * [Source documentation](/Start_up_and_Configuration "Start up and Configuration")
  * Use the [bug tracker](/Tracker "Tracker") when you have a problem or think you may have found a bug

### Packaging

[Packaging](/Packaging "Packaging") consists in taking the compiled binaries
and Python source files of FreeCAD, and distributing them for use in a
particular system.

  * [Linux packaging](/Linux_packaging "Linux packaging")
    * [Debian development](/Debian_development "Debian development")
    * [Debian Unstable](/Debian_Unstable "Debian Unstable")
    * [Git buildpackage](/Git_buildpackage "Git buildpackage")
  * [Windows packaging](/Windows_packaging "Windows packaging")
  * [MacOS packaging](/MacOS_packaging "MacOS packaging")

### Build Support Tools

  * The [FreeCAD Build Tool](/FreeCAD_Build_Tool "FreeCAD Build Tool")
    * [Adding an application module](/Workbench_creation "Workbench creation") to FreeCAD
  * [Debugging](/Debugging "Debugging") FreeCAD
  * [Testing](/Testing "Testing") FreeCAD
  * [Compiling (Speeding up)](/Compiling_\(Speeding_up\) "Compiling \(Speeding up\)") FreeCAD
  * [Continuous Integration](/Continuous_Integration "Continuous Integration")

### Modifying FreeCAD

  * Understanding [The FreeCAD source code](/The_FreeCAD_source_code "The FreeCAD source code")
  * [Submitting patches](/Tracker#Submitting_patches "Tracker")
  * Add [Features](/Gui_Command "Gui Command") to FreeCAD or a Workbench
  * [Branding](/Branding "Branding") or _how to give FreeCAD a unique look_
  * [Artwork](/Artwork "Artwork") we made for FreeCAD, that you can freely reuse.
  * [Artwork guidelines](/Artwork_Guidelines "Artwork Guidelines") standards for icons
  * [Translating FreeCAD](/Localisation "Localisation")
  * [Extra Python modules](/Extra_python_modules "Extra python modules"), or _how to extend python functionality within FreeCAD_
  * [Google Summer of Code](/Google_Summer_of_Code "Google Summer of Code") get involved via Google's student support program.
  * [Fine-tuning](/Fine-tuning "Fine-tuning") shows different options and parameter switches that can overcome problems.
  * [Wrapping a C++ class in Python](/Wrapping_a_Cplusplus_class_in_Python "Wrapping a Cplusplus class in Python") shows how to create the Python wrapper for a C++ class.
  * [Checklist for adding a Feature to a C++ workbench](/NewFeatureCheckList_C%2B%2B "NewFeatureCheckList C++") provides an aid for contributors.

  * [Translating an external workbench](/Translating_an_external_workbench "Translating an external workbench")

### Module developer's guide

[FreeCAD Mod Dev Guide](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide):
This is an ebook under writing on GitHub, please fork and send pull request to
contribute.

Chapters:

  * Overview and Software Architecture
  * Source code structure
  * Base and App module
  * Gui module
  * Python wrapping
  * Modular design
  * FEM module source analysis (mixed C++ and Python)
  * Development of CFD Module (pure Python)
  * Module testing and debugging
  * Contribute code with git

Latest PDF preview can be downloaded from
[PDFfolder](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide/tree/master/pdf)
of this GitHub repository.

### Internals

#### OpenCascade Documentation

OpenCascade is a software development platform for 3D surface and solid
modeling, CAD data exchange, and visualization, mostly in the form of C++
libraries.

  * [Roman Lygin's tutorials](http://opencascade.wikidot.com/romansarticles)
  * [Full Online Documentation](https://dev.opencascade.org/cdoc/overview/html/index.html)
  * [Reference Manual](https://dev.opencascade.org/doc/refman/html/index.html)
  * [The openCascade wiki](http://opencascade.wikidot.com) (currently containing ?? Chinese spam)

#### File format

[File Format FCStd](/File_Format_FCStd "File Format FCStd"). The files created
with FreeCAD are `.zip` files that include the
[BREP](https://en.wikipedia.org/wiki/Boundary_representation) geometry, as
well as XML data that describes the document.

#### Sketcher solver

  * [Sketcher Solver Architecture Booklet](https://forum.freecad.org/viewtopic.php?f=10&t=36355) (forum thread), [source](https://github.com/abdullahtahiriyo/FreeCADBooks/tree/master/FreeCAD_Solver_Architecture) in GitHub.
  * [PlaneGCS solver](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/) in the FreeCAD source code; important files are [GCS.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/GCS.cpp) and [SubSystem.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/SubSystem.cpp).
  * [Recent Several Sketcher improvements](https://forum.freecad.org/viewtopic.php?f=9&t=29192).

The Sketcher solver isn't perfect, as there are some issues with numerical
precision when using large values, see [Adventure of fixing sketcher solver
for large sketches](https://forum.freecad.org/viewtopic.php?f=10&t=40502).

The development of a new solver architecture could improve the way the solver
is used both in the [Sketcher Workbench](/Sketcher_Workbench "Sketcher
Workbench"), and for assembly of 3D bodies. See [Reimplementing constraint
solver](https://forum.freecad.org/viewtopic.php?f=20&t=40525).

## Roadmap

FreeCAD, though usable in certain areas, is at the beginning of a long way
into the CAD mainstream. There is still a lot to do to reach a state where we
can compete with commercial software.

[FreeCAD 1.0 Development Cycle](/FreeCAD_1.0_Development_Cycle "FreeCAD 1.0
Development Cycle")

## Community

  * [IRC channel](ircs://irc.libera.chat:6697/freecad) ,synchronized with [gitter channel](https://gitter.im/FreeCAD/FreeCAD)
  * [Development forum](https://forum.freecad.org/viewforum.php?f=6)

  * [Development roadmap](/Development_roadmap "Development roadmap")

## Credits

[Contributors](/Contributors "Contributors")

  

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

  * **[Addons](/Addon "Addon"):** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), Developer hub

