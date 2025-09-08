---
url: https://wiki.freecad.org/Installing_on_Mac
title: Installing on Mac
scraped_at: 2025-09-08 16:45:30
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Simple installation
  * 2 Uninstallation

# Installing on Mac

  * [Page](/Installing_on_Mac "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Installing_on_Mac&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Installing_on_Mac)
  * [Edit](/index.php?title=Installing_on_Mac&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Installing_on_Mac&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Installing_on_Mac.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Installing_on_Mac&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Installing_on_Mac)
  * [Edit](/index.php?title=Installing_on_Mac&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Installing_on_Mac&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Installing_on_Mac&action=history)

General

  * [What links here](/Special:WhatLinksHere/Installing_on_Mac "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Installing_on_Mac "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Installing_on_Mac&oldid=1626403 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Installing_on_Mac&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Installing_on_Mac&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Installing+on+Mac&action=page&filter=&language=en)This is the approved
revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Installing+on+Mac&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/Installing_on_Mac/id "Install on Mac \(0% translated\)")
  * [Deutsch](/Installing_on_Mac/de "Installieren auf Mac \(100% translated\)")
  * English
  * [Türkçe](/Installing_on_Mac/tr "Mac için Kurulum \(28% translated\)")
  * [español](/Installing_on_Mac/es "Instalación en Mac \(56% translated\)")
  * [français](/Installing_on_Mac/fr "Installation sous Mac \(100% translated\)")
  * [hrvatski](/Installing_on_Mac/hr "Instalacija na Mac-u \(0% translated\)")
  * [italiano](/Installing_on_Mac/it "Installare in Mac \(100% translated\)")
  * [polski](/Installing_on_Mac/pl "Instalacja w systemie Mac OS \(100% translated\)")
  * [português](/Installing_on_Mac/pt "Install on Mac \(28% translated\)")
  * [português do Brasil](/Installing_on_Mac/pt-br "Instalando no Mac \(56% translated\)")
  * [română](/Installing_on_Mac/ro "Install on Mac \(28% translated\)")
  * [svenska](/Installing_on_Mac/sv "Install on Mac \(28% translated\)")
  * [čeština](/Installing_on_Mac/cs "Instalace na Mac \(28% translated\)")
  * [български](/Installing_on_Mac/bg "Инсталация на Mac \(28% translated\)")
  * [русский](/Installing_on_Mac/ru "Установка на Mac \(56% translated\)")
  * [українська](/Installing_on_Mac/uk "Install on Mac \(0% translated\)")
  * [中文](/Installing_on_Mac/zh "Install on Mac \(0% translated\)")
  * [中文（中国大陆）](/Installing_on_Mac/zh-cn "在 Mac 上安装 \(28% translated\)")
  * [中文（臺灣）](/Installing_on_Mac/zh-tw "在Mac上安裝 \(0% translated\)")
  * [日本語](/Installing_on_Mac/ja "Macへのインストール \(44% translated\)")
  * [한국어](/Installing_on_Mac/ko "Mac 시스템에 설치 \(22% translated\)")

![](/images/6/6f/Arrow-left.svg) [Installing on Linux](/Installing_on_Linux
"Installing on Linux")

[Installing additional components](/Installing_additional_components
"Installing additional components") ![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

FreeCAD can be installed on macOS from a .dmg package which you can drag and
drop into your Applications folder, see the [Download](/Download "Download")
page.

If you would like to download a development version, which may be unstable,
see the [weekly builds](https://github.com/FreeCAD/FreeCAD/releases).

You can also use a package manager such as HomeBrew to keep your software
updated. Instructions to install HomeBrew can be seen
[here](https://brew.sh/). When HomeBrew installed you can simply install
FreeCAD through your bash terminal with

    
    
    brew install --cask freecad
    

and to use the latest version available on HomeBrew you may run

    
    
    brew install freecad
    

If there are any issues with the HomeBrew Cask or Formula you may report them
to [here](https://github.com/FreeCAD/homebrew-freecad).

This page describes the usage and features of the FreeCAD installer. It also
includes uninstallation instructions. Head to [Getting
started](/Getting_started "Getting started") once installation is complete.

## Simple installation

The FreeCAD installer is provided as a app package (.app) enclosed in a disk
image file.

You can download the latest installer from the [Download](/Download
"Download") page. After downloading the file, just mount the disk image, then
drag it to the Application folder or a folder of your choice.

[![](/images/4/44/Mac_installer_1.png)](/index.php?title=File:Mac_installer_1.png&filetimestamp=20170401072219&)

That's it.Just click on the app to launch FreeCAD. If you have this message
"FreeCAD can't be open as it is from unidentified developer." Open the folder
(Application) and right click on the app then click open and accept to open
the application.

## Uninstallation

There currently isn't an uninstaller for FreeCAD installed with dmg package.
To completely remove FreeCAD and all installed components, drag the following
files and folders to the Trash:

  * In the Applications directory: 
    * /Applications/FreeCAD.app
  * In the Users Home Library directory 
    * $HOME/Library/Application Support/FreeCAD
    * $HOME/Library/Preferences/FreeCAD
    * $HOME/Library/Preferences/com.freecad.FreeCAD.plist
    * $HOME/Library/Preferences/freecad.plist
    * $HOME/Library/Caches/FreeCAD

If you installed FreeCAD with homebrew, then use the `brew uninstall freecad`
command to uninstall /Applications/FreeCAD.app. The related files and
directories in the user home Library will still need to be removed manually.

  

![](/images/6/6f/Arrow-left.svg) [Installing on Linux](/Installing_on_Linux
"Installing on Linux")

[Installing additional components](/Installing_additional_components
"Installing additional components") ![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

Expand[![](/images/thumb/9/94/User_hub.png/24px-
User_hub.png)](/index.php?title=File:User_hub.png&filetimestamp=20190221145008&)
[User documentation](/User_hub "User hub")

  * **[Getting started](/Getting_started "Getting started")**
  * **Installation:** [Download](/Download "Download"), [Windows](/Installing_on_Windows "Installing on Windows"), [Linux](/Installing_on_Linux "Installing on Linux"), Mac, [Additional components](/Installing_additional_components "Installing additional components"), [Docker](/Compile_on_Docker "Compile on Docker"), [AppImage](/AppImage "AppImage"), [Ubuntu Snap](/Ubuntu_Snap "Ubuntu Snap")
  * **Basics:** [About FreeCAD](/About_FreeCAD "About FreeCAD"), [Interface](/Interface "Interface"), [Mouse navigation](/Mouse_navigation "Mouse navigation"), [Selection methods](/Selection_methods "Selection methods"), [Object name](/Object_name "Object name"), [Preferences](/Preferences_Editor "Preferences Editor"), [Workbenches](/Workbenches "Workbenches"), [Document structure](/Document_structure "Document structure"), [Properties](/Property "Property"), [Help FreeCAD](/Help_FreeCAD "Help FreeCAD"), [Donate](/Donate "Donate")

* * *

  * **Help:** [Tutorials](/Tutorials "Tutorials"), [Video tutorials](/Video_tutorials "Video tutorials")
  * **[Workbenches](/Workbenches "Workbenches"):** [Std Base](/Std_Base "Std Base"), [Assembly](/Assembly_Workbench "Assembly Workbench"), [BIM](/BIM_Workbench "BIM Workbench"), [CAM](/CAM_Workbench "CAM Workbench"), [Draft](/Draft_Workbench "Draft Workbench"), [FEM](/FEM_Workbench "FEM Workbench"), [Inspection](/Inspection_Workbench "Inspection Workbench"), [Material](/Material_Workbench "Material Workbench"), [Mesh](/Mesh_Workbench "Mesh Workbench"), [OpenSCAD](/OpenSCAD_Workbench "OpenSCAD Workbench"), [Part](/Part_Workbench "Part Workbench"), [PartDesign](/PartDesign_Workbench "PartDesign Workbench"), [Points](/Points_Workbench "Points Workbench"), [Reverse Engineering](/Reverse_Engineering_Workbench "Reverse Engineering Workbench"), [Robot](/Robot_Workbench "Robot Workbench"), [Sketcher](/Sketcher_Workbench "Sketcher Workbench"), [Spreadsheet](/Spreadsheet_Workbench "Spreadsheet Workbench"), [Surface](/Surface_Workbench "Surface Workbench"), [TechDraw](/TechDraw_Workbench "TechDraw Workbench"), [Test Framework](/Testing "Testing")

* * *

  * **[Addons](/Addon "Addon"):** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

