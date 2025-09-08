---
url: https://wiki.freecad.org/Ubuntu_Snap
title: Ubuntu Snap
scraped_at: 2025-09-08 16:45:37
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Installation Toggle Installation subsection
    * 2.1 Debian/Ubuntu
    * 2.2 Manjaro
  * 3 Notes Toggle Notes subsection
    * 3.1 What FC version am I running
    * 3.2 Changing between different Snaps
  * 4 Advanced
  * 5 Links Toggle Links subsection
    * 5.1 Repositories
    * 5.2 Maintainer(s)
  * 6 Related

# Ubuntu Snap

  * [Page](/Ubuntu_Snap "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Ubuntu_Snap&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Ubuntu_Snap)
  * [Edit](/index.php?title=Ubuntu_Snap&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Ubuntu_Snap&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Ubuntu_Snap.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Ubuntu_Snap&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Ubuntu_Snap)
  * [Edit](/index.php?title=Ubuntu_Snap&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Ubuntu_Snap&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Ubuntu_Snap&action=history)

General

  * [What links here](/Special:WhatLinksHere/Ubuntu_Snap "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Ubuntu_Snap "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Ubuntu_Snap&oldid=1633976 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Ubuntu_Snap&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Ubuntu_Snap&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Ubuntu+Snap&action=page&filter=&language=en)This is the approved revision of
this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Ubuntu+Snap&language=&task=view "Start translation for this language")
  * [Deutsch](/Ubuntu_Snap/de "Ubuntu Snap \(33% translated\)")
  * English
  * [español](/Ubuntu_Snap/es "Ubuntu Snap \(21% translated\)")
  * [français](/Ubuntu_Snap/fr "Ubuntu Snap \(100% translated\)")
  * [italiano](/Ubuntu_Snap/it "Ubuntu Snap \(100% translated\)")
  * [polski](/Ubuntu_Snap/pl "Ubuntu Snap \(100% translated\)")
  * [português do Brasil](/Ubuntu_Snap/pt-br "Zrzut Ubuntu \(3% translated\)")
  * [русский](/Ubuntu_Snap/ru "Ubuntu Snap \(10% translated\)")
  * [日本語](/Ubuntu_Snap/ja "Ubuntu Snap \(5% translated\)")

## Introduction

An Ubuntu Snap package, or just Snap is a distribution format similar to
[AppImage](/AppImage "AppImage") in that it is intended to be a "universal
installable package" to deploy software on Linux systems. Snaps were
introduced by Ubuntu but they are intended to run on all Linux distributions
as long as the Snap daemon, or `snapd`, is available on the target system.

A Snap package has two main characteristics:

  * Programs are sandboxed so they do not interfere with the rest of the operating system.
  * Programs are updated automatically in the background in order to get the newest version of the application.

For other ways of installing the software, see [Installing on
Linux](/Installing_on_Linux "Installing on Linux").

## Installation

The use of Snaps is experimental. The current Snaps are generated and hosted
by volunteers.

On all systems where Snaps are to be installed, the Snap daemon must be
installed first. The package is normally called `snapd`.

### Debian/Ubuntu

For Debian/Ubuntu and similar systems which use the APT manager the daemon is
installed as follows:

    
    
    sudo apt install snapd
    

To install the stable version of the Snap use:

    
    
    sudo snap install freecad
    

To install the development version of the Snap use:

    
    
    sudo snap install --edge freecad
    

### Manjaro

To install the stable version of the Snap use:

    
    
    snap install freecad
    

To install the development version of the Snap use:

    
    
    snap install --edge freecad
    

## Notes

#### What FC version am I running

To figure out which development version is installed type the following in the
Command-line interface:

    
    
    snap info freecad
    

#### Changing between different Snaps

Starting from the tail end of the v0.20 release cycle, the FreeCAD snap
maintainers added the ability to test experimental FreeCAD builds. Snaps allow
for this by easily toggling between different snaps (terminology is '[channels
or tracks](https://snapcraft.io/docs/channels)'). For example:

Testing the Topological Naming ('toponaming') branch (created at the start of
the v0.21/v1.0 release cycle):

    
    
    snap refresh freecad --channel=latest/edge/toponaming
    

Using the `refresh` command will switch and update the snap channel you're
switching to:

    
    
    snap refresh freecad --channel=latest/edge/toponaming
    

Toggling back to the nightly 'edge' channel:

    
    
    snap refresh freecad --channel=latest/edge
    

## Advanced

The following commands are geared towards users that are familiar with `git`
and have a locally cloned repository of the upstream FreeCAD repository.

    
    
    git clone https://github.com/FreeCAD/FreeCAD
    cd FreeCAD/
    

To find out the latest upstream revision number (also known as 'HEAD'):

    
    
    git pull upstream master  # first make sure we have the most up-to-date commits
    git rev-list --count HEAD # 'HEAD' refers to the current commit you are viewing (tip of the master branch)
    

To translate the current snap development version in to a revision number
(make sure you're within your cloned FreeCAD repository as mentioned above):

    
    
    snap info freecad |\
    grep -e '^\s\+latest/edge' |\
    awk -F ' ' '{ print $2 }' |\
    xargs -I{} git rev-list --count {}
    

**Note:** the above bash script 1 liner assumes user has 'edge' (nightly)
installed

The difference between HEAD and the snap edge revision numbers indicates the
amount of revisions trailing behind upstream the snap development (edge) is.

Taking it a step further, if you want a short summary of the commits between
the current snap edge and HEAD:

    
    
    snap info freecad |\
    grep -e '^\s\+latest/edge' |\
    awk -F ' ' '{ print $2 }' |\
    xargs -I{} git log --oneline --ancestry-path {}..HEAD
    

**Note:** The output will indicate what commits **are not** in the current
'edge' (but will be on the next nightly update).

## Links

More information about the current efforts to deal with Snaps:

  * [0.19 Snap Preview needs "testers"](https://forum.freecad.org/viewtopic.php?f=4&t=46044), older Snap by _vejmarie_. (deprecated)
  * [Discussion: State of the snap (Snap Packaging)](https://forum.freecad.org/viewtopic.php?f=42&t=46853), newer version of the Snap by _ppd_. (deprecated)

### Repositories

  * <https://github.com/FreeCAD/FreeCAD-snap>
  * <https://snapcraft.io/freecad>

### Maintainer(s)

  * ppd ([forum](https://forum.freecad.org/memberlist.php?mode=viewprofile&u=24042), [github](https://github.com/ppd))
  * luzpaz ([forum](https://forum.freecad.org/memberlist.php?mode=viewprofile&u=12229), [github](https://github.com/luzpaz))

## Related

  * [AppImage](/AppImage "AppImage") \- another self-contained 'binary' like format to run FreeCAD
  * [Flatpak](/Flatpak "Flatpak") packages

Expand[![](/images/thumb/9/94/User_hub.png/24px-
User_hub.png)](/index.php?title=File:User_hub.png&filetimestamp=20190221145008&)
[User documentation](/User_hub "User hub")

  * **[Getting started](/Getting_started "Getting started")**
  * **Installation:** [Download](/Download "Download"), [Windows](/Installing_on_Windows "Installing on Windows"), [Linux](/Installing_on_Linux "Installing on Linux"), [Mac](/Installing_on_Mac "Installing on Mac"), [Additional components](/Installing_additional_components "Installing additional components"), [Docker](/Compile_on_Docker "Compile on Docker"), [AppImage](/AppImage "AppImage"), Ubuntu Snap
  * **Basics:** [About FreeCAD](/About_FreeCAD "About FreeCAD"), [Interface](/Interface "Interface"), [Mouse navigation](/Mouse_navigation "Mouse navigation"), [Selection methods](/Selection_methods "Selection methods"), [Object name](/Object_name "Object name"), [Preferences](/Preferences_Editor "Preferences Editor"), [Workbenches](/Workbenches "Workbenches"), [Document structure](/Document_structure "Document structure"), [Properties](/Property "Property"), [Help FreeCAD](/Help_FreeCAD "Help FreeCAD"), [Donate](/Donate "Donate")

* * *

  * **Help:** [Tutorials](/Tutorials "Tutorials"), [Video tutorials](/Video_tutorials "Video tutorials")
  * **[Workbenches](/Workbenches "Workbenches"):** [Std Base](/Std_Base "Std Base"), [Assembly](/Assembly_Workbench "Assembly Workbench"), [BIM](/BIM_Workbench "BIM Workbench"), [CAM](/CAM_Workbench "CAM Workbench"), [Draft](/Draft_Workbench "Draft Workbench"), [FEM](/FEM_Workbench "FEM Workbench"), [Inspection](/Inspection_Workbench "Inspection Workbench"), [Material](/Material_Workbench "Material Workbench"), [Mesh](/Mesh_Workbench "Mesh Workbench"), [OpenSCAD](/OpenSCAD_Workbench "OpenSCAD Workbench"), [Part](/Part_Workbench "Part Workbench"), [PartDesign](/PartDesign_Workbench "PartDesign Workbench"), [Points](/Points_Workbench "Points Workbench"), [Reverse Engineering](/Reverse_Engineering_Workbench "Reverse Engineering Workbench"), [Robot](/Robot_Workbench "Robot Workbench"), [Sketcher](/Sketcher_Workbench "Sketcher Workbench"), [Spreadsheet](/Spreadsheet_Workbench "Spreadsheet Workbench"), [Surface](/Surface_Workbench "Surface Workbench"), [TechDraw](/TechDraw_Workbench "TechDraw Workbench"), [Test Framework](/Testing "Testing")

* * *

  * **[Addons](/Addon "Addon"):** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

