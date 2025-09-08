---
url: https://wiki.freecad.org/Installing_on_Windows
title: Installing on Windows
scraped_at: 2025-09-08 16:45:27
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Standard Installation
  * 2 Installation for all users of the Windows system
  * 3 Silent Installation
  * 4 Chocolatey
  * 5 Uninstallation

# Installing on Windows

  * [Page](/Installing_on_Windows "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Installing_on_Windows&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Installing_on_Windows)
  * [Edit](/index.php?title=Installing_on_Windows&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Installing_on_Windows&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Installing_on_Windows.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Installing_on_Windows&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Installing_on_Windows)
  * [Edit](/index.php?title=Installing_on_Windows&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Installing_on_Windows&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Installing_on_Windows&action=history)

General

  * [What links here](/Special:WhatLinksHere/Installing_on_Windows "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Installing_on_Windows "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Installing_on_Windows&oldid=1626404 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Installing_on_Windows&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Installing_on_Windows&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Installing+on+Windows&action=page&filter=&language=en)This is the approved
revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Installing+on+Windows&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/Installing_on_Windows/id "Install on Windows \(0% translated\)")
  * [Deutsch](/Installing_on_Windows/de "Installieren auf Windows \(100% translated\)")
  * English
  * [Türkçe](/Installing_on_Windows/tr "Windows'ta kurulum \(4% translated\)")
  * [español](/Installing_on_Windows/es "Instalación en Windows \(32% translated\)")
  * [français](/Installing_on_Windows/fr "Installation sous Windows \(100% translated\)")
  * [hrvatski](/Installing_on_Windows/hr "Instaliraj u Windowse \(0% translated\)")
  * [italiano](/Installing_on_Windows/it "Installare in Windows \(100% translated\)")
  * [polski](/Installing_on_Windows/pl "Instalacja w systemie Windows \(100% translated\)")
  * [português](/Installing_on_Windows/pt "Instalar em Windows \(4% translated\)")
  * [português do Brasil](/Installing_on_Windows/pt-br "Instalando no Windows \(28% translated\)")
  * [română](/Installing_on_Windows/ro "Instalarea sub Windows \(12% translated\)")
  * [svenska](/Installing_on_Windows/sv "Install on Windows \(4% translated\)")
  * [čeština](/Installing_on_Windows/cs "Instalace na Windows \(4% translated\)")
  * [български](/Installing_on_Windows/bg "Инсталация на Windows \(4% translated\)")
  * [русский](/Installing_on_Windows/ru "Установка в Windows \(52% translated\)")
  * [українська](/Installing_on_Windows/uk "Installing on Windows/uk \(0% translated\)")
  * [中文](/Installing_on_Windows/zh "在Windows环境中安装 \(0% translated\)")
  * [中文（中国大陆）](/Installing_on_Windows/zh-cn "在 Windows 上安装 \(8% translated\)")
  * [日本語](/Installing_on_Windows/ja "Windowsへのインストール \(16% translated\)")
  * [한국어](/Installing_on_Windows/ko "윈도우에 설치하기 \(20% translated\)")

![](/images/6/6f/Arrow-left.svg) [Feature list](/Feature_list "Feature list")

[Installing on Linux](/Installing_on_Linux "Installing on Linux")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

## Standard Installation

The easiest way to install the latest stable version of FreeCAD is to use the
installer, see the [Download](/Download "Download") page.

If you would like to download a development version, which may be unstable,
see the [weekly builds](https://github.com/FreeCAD/FreeCAD/releases).

After downloading the installer, double-click it to start the installation
process.

Below is more information about some technical options. But most users don't
need more than the installer. Head to [Getting started](/Getting_started
"Getting started") once installation is complete.

## Installation for all users of the Windows system

By default FreeCAD will be installed for the user that executes the installer.
If this user only has user permissions, the default installation path is:

    C:\Users\<username>\AppData\Local\Programs\FreeCAD X.YY

If the installer is executed by an admin user, or you execute it as admin, you
can choose if FreeCAD should be installed for all users of the system or just
for you. The default is for all users.

If installed for all users, the default installation path is:

    C:\Program Files\FreeCAD X.YY

## Silent Installation

To install FreeCAD silently, you can execute the installer from the command
line:

    
    
    FreeCAD-~.exe /S
    

Default settings will be used for all options. A custom installation path can
be specified in this manner:

    
    
    FreeCAD-~.exe /S /D=A path to FreeCAD with spaces
    

By default, even with silent installations, there will be a short popup when
the installer is checked for corruption. This so-called cyclic redundancy
check only takes a few seconds at most. To disable this corruption check:

    
    
    FreeCAD-~.exe /S /NCRC
    

Note that this `/NCRC` flag is **not recommended** since the corruption check
assures that the installer was e.g. completely downloaded.

## Chocolatey

It is highly recommended that you use a package manager such as Chocolatey to
keep your software updated. You can install Chocolatey following [these
instructions](https://chocolatey.org/install) and then open a PowerShell
terminal as admin and run:

    
    
    choco install freecad
    

Every once in a while you can update your software with:

    
    
    choco upgrade freecad
    

This will get the latest version available from the Chocolatey repository. If
there are any issues with the Chocolatey package, you can contact maintainers
on [this page](https://chocolatey.org/packages/freecad).

## Uninstallation

To uninstall FreeCAD it is preferable to use the Windows tools for
uninstalling software. Alternatively you can execute the uninstaller directly.
This is the file:

    Uninstall-FreeCAD.exe

You can find it in the folder where FreeCAD is installed.

The uninstaller can also be executed silently using the command line:

    
    
    Uninstall-FreeCAD.exe /S
    

Note that (silent) uninstallation will fail if there is a running instance of
FreeCAD, even if that instance is not the version being uninstalled.

  

![](/images/6/6f/Arrow-left.svg) [Feature list](/Feature_list "Feature list")

[Installing on Linux](/Installing_on_Linux "Installing on Linux")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

Expand[![](/images/thumb/9/94/User_hub.png/24px-
User_hub.png)](/index.php?title=File:User_hub.png&filetimestamp=20190221145008&)
[User documentation](/User_hub "User hub")

  * **[Getting started](/Getting_started "Getting started")**
  * **Installation:** [Download](/Download "Download"), Windows, [Linux](/Installing_on_Linux "Installing on Linux"), [Mac](/Installing_on_Mac "Installing on Mac"), [Additional components](/Installing_additional_components "Installing additional components"), [Docker](/Compile_on_Docker "Compile on Docker"), [AppImage](/AppImage "AppImage"), [Ubuntu Snap](/Ubuntu_Snap "Ubuntu Snap")
  * **Basics:** [About FreeCAD](/About_FreeCAD "About FreeCAD"), [Interface](/Interface "Interface"), [Mouse navigation](/Mouse_navigation "Mouse navigation"), [Selection methods](/Selection_methods "Selection methods"), [Object name](/Object_name "Object name"), [Preferences](/Preferences_Editor "Preferences Editor"), [Workbenches](/Workbenches "Workbenches"), [Document structure](/Document_structure "Document structure"), [Properties](/Property "Property"), [Help FreeCAD](/Help_FreeCAD "Help FreeCAD"), [Donate](/Donate "Donate")

* * *

  * **Help:** [Tutorials](/Tutorials "Tutorials"), [Video tutorials](/Video_tutorials "Video tutorials")
  * **[Workbenches](/Workbenches "Workbenches"):** [Std Base](/Std_Base "Std Base"), [Assembly](/Assembly_Workbench "Assembly Workbench"), [BIM](/BIM_Workbench "BIM Workbench"), [CAM](/CAM_Workbench "CAM Workbench"), [Draft](/Draft_Workbench "Draft Workbench"), [FEM](/FEM_Workbench "FEM Workbench"), [Inspection](/Inspection_Workbench "Inspection Workbench"), [Material](/Material_Workbench "Material Workbench"), [Mesh](/Mesh_Workbench "Mesh Workbench"), [OpenSCAD](/OpenSCAD_Workbench "OpenSCAD Workbench"), [Part](/Part_Workbench "Part Workbench"), [PartDesign](/PartDesign_Workbench "PartDesign Workbench"), [Points](/Points_Workbench "Points Workbench"), [Reverse Engineering](/Reverse_Engineering_Workbench "Reverse Engineering Workbench"), [Robot](/Robot_Workbench "Robot Workbench"), [Sketcher](/Sketcher_Workbench "Sketcher Workbench"), [Spreadsheet](/Spreadsheet_Workbench "Spreadsheet Workbench"), [Surface](/Surface_Workbench "Surface Workbench"), [TechDraw](/TechDraw_Workbench "TechDraw Workbench"), [Test Framework](/Testing "Testing")

* * *

  * **[Addons](/Addon "Addon"):** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

