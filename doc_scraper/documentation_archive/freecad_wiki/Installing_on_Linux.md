---
url: https://wiki.freecad.org/Installing_on_Linux
title: Installing on Linux
scraped_at: 2025-09-08 16:45:28
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Overview
  * 2 Ubuntu and Ubuntu-based systems Toggle Ubuntu and Ubuntu-based systems subsection
    * 2.1 Official version
    * 2.2 Stable PPA version
      * 2.2.1 GUI
      * 2.2.2 CLI
      * 2.2.3 Checking Installation
    * 2.3 Development PPA (Daily)
  * 3 Debian and other Debian-based systems
  * 4 OpenSUSE Toggle OpenSUSE subsection
    * 4.1 Stable
    * 4.2 Development
  * 5 Gentoo
  * 6 Fedora
  * 7 Arch
  * 8 Other Toggle Other subsection
    * 8.1 Installing on other Linux/Unix systems
  * 9 Next Step

# Installing on Linux

  * [Page](/Installing_on_Linux "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Installing_on_Linux&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Installing_on_Linux)
  * [Edit](/index.php?title=Installing_on_Linux&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Installing_on_Linux&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Installing_on_Linux.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Installing_on_Linux&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Installing_on_Linux)
  * [Edit](/index.php?title=Installing_on_Linux&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Installing_on_Linux&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Installing_on_Linux&action=history)

General

  * [What links here](/Special:WhatLinksHere/Installing_on_Linux "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Installing_on_Linux "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Installing_on_Linux&oldid=1610599 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Installing_on_Linux&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Installing_on_Linux&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Installing+on+Linux&action=page&filter=&language=en)This is the approved
revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Installing+on+Linux&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/Installing_on_Linux/id "Install on Linux/id \(0% translated\)")
  * [Deutsch](/Installing_on_Linux/de "Installation unter Linux \(100% translated\)")
  * English
  * [Türkçe](/Installing_on_Linux/tr "Linux'te kurulum \(0% translated\)")
  * [español](/Installing_on_Linux/es "Instalación en Linux \(94% translated\)")
  * [français](/Installing_on_Linux/fr "Installation sous Linux \(100% translated\)")
  * [hrvatski](/Installing_on_Linux/hr "Install on Linux/hr \(0% translated\)")
  * [italiano](/Installing_on_Linux/it "Installare in Linux \(100% translated\)")
  * [polski](/Installing_on_Linux/pl "Instalacja w systemie Linux \(100% translated\)")
  * [português](/Installing_on_Linux/pt "Install on Linux/pt \(0% translated\)")
  * [português do Brasil](/Installing_on_Linux/pt-br "Instalando no Linux \(85% translated\)")
  * [română](/Installing_on_Linux/ro "Install on Linux/ro \(0% translated\)")
  * [svenska](/Installing_on_Linux/sv "Install on Linux/sv \(0% translated\)")
  * [čeština](/Installing_on_Linux/cs "Instalace na Linux \(0% translated\)")
  * [български](/Installing_on_Linux/bg "Инсталация на Linux \(0% translated\)")
  * [русский](/Installing_on_Linux/ru "Установка в Linux \(94% translated\)")
  * [українська](/Installing_on_Linux/uk "Install on Linux/uk \(0% translated\)")
  * [中文](/Installing_on_Linux/zh "Install on Linux/zh \(0% translated\)")
  * [中文（中国大陆）](/Installing_on_Linux/zh-cn "Install on Linux/zh-cn \(0% translated\)")
  * [日本語](/Installing_on_Linux/ja "Install on Linux/ja \(4% translated\)")
  * [한국어](/Installing_on_Linux/ko "리눅스에 설치하기 \(5% translated\)")

![](/images/6/6f/Arrow-left.svg) [Installing on
Windows](/Installing_on_Windows "Installing on Windows")

[Installing on Mac](/Installing_on_Mac "Installing on Mac")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

## Overview

The installation of FreeCAD on most well-known Linux systems is endorsed by
the community, and FreeCAD is available via the package manager on those
systems. The FreeCAD team also provides some:

  * "Official" packages when new releases are made available via [Snap packages](/Ubuntu_Snap "Ubuntu Snap"), [AppImages](/AppImage "AppImage"), [Flatpaks](/Flatpak "Flatpak") and the PPA
  * Experimental or 'bleeding edge' builds available via PPA daily repository, [AppImages](/AppImage "AppImage"), [Ubuntu Snaps](/Ubuntu_Snap "Ubuntu Snap").

Expand

## Ubuntu and Ubuntu-based systems

Many Linux distributions are based on Ubuntu and share its repositories.
Besides official variants (Kubuntu, Lubuntu and Xubuntu), there are non
official derivatives like Linux Mint, Voyager and others. The installation
options below (Expand) should be compatible with these systems.

### Official version

FreeCAD is available from the Ubuntu Universe repository, and can be installed
via the **Software Center** or from the terminal:

    
    
    sudo apt install freecad
    

_Note:_ the Ubuntu Universe package may be outdated as the packaging may lag
behind the latest stable source code. In this case, it is suggested to install
the package from the `-stable` PPA below. In addition, installing the `-daily`
package can be done to test the development branch.

### Stable PPA version

**Warning:** The FreeCAD PPA is currently unmaintained and [looking for
volunteers](https://forum.freecad.org/viewtopic.php?f=42&t=69055&start=20).
Please use an alternative (snap, appimage) until the issue is fixed!

Personal Package Archive (PPA) for the stable FreeCAD release is maintained by
the FreeCAD community on Launchpad. The Launchpad repository is called
[FreeCAD Stable Releases](https://launchpad.net/~freecad-
maintainers/+archive/freecad-stable) .

#### GUI

Install the stable PPA via the Graphical User Interface (GUI):

    1\. Navigate to **Ubuntu Software → Software & Updates → Software Sources → Other Software**
    2\. Click on Add, then copy and paste the following line 

    
    
    
    ppa:freecad-maintainers/freecad-stable
    

    3\. Add the source, close the dialog, and reload your software sources, if asked.

Now you can find and install the last stable FreeCAD version from the **Ubuntu
Software Center**.

#### CLI

Install the stable PPA via the Command Line Interface (CLI):

    1\. Add the PPA to your software sources: 

    
    
    
    sudo add-apt-repository ppa:freecad-maintainers/freecad-stable
    

    2\. Retrieve the updated package lists: 

    
    
    
    sudo apt update
    

    3\. Then install FreeCAD along with its offline documentation: 

    
    
    
    sudo apt install freecad freecad-doc
    

_Note:_ due to packaging problems, in certain versions of Ubuntu the `freecad-
doc` package has collided with the installation of FreeCAD or one of its
dependencies; if this is the case, remove the `freecad-doc` package, and only
install the `freecad` package. If the `freecad-doc` package doesn't exist,
then ignore it.

#### Checking Installation

    4\. Once you have the stable PPA added to your sources using one of the above methods, the `freecad` package will install this PPA version over the one provided by the Ubuntu Universe repository. You can see the available versions with the following `apt-cache` command:
    
    
    
    apt-cache policy freecad
    

    The output should look similar to the following (of course the version info will vary):
    
    
    freecad:
      Installed: (none)
      Candidate: 2:0.18.4+dfsg1~201911060029~ubuntu18.04.1
      Version table:
         2:0.18.4+dfsg1~201911060029~ubuntu18.04.1 500
            500 http://ppa.launchpad.net/freecad-maintainers/freecad-stable/ubuntu bionic/main amd64 Packages
         0.16.6712+dfsg1-1ubuntu2 500
            500 http://archive.ubuntu.com/ubuntu bionic/universe amd64 Packages
    ubuntu@ubuntu:~$ apt-cache policy freecad-doc
    

    5\. Invoke the stable (PPA) version of FreeCAD from the GUI or CLI. The latter method is as follows:
    
    
    
    ./freecad
    

### Development PPA (Daily)

As FreeCAD is in constant development, you may wish to install the _daily_
package to keep with the latest improvements and bug fixes. The repository is
also hosted on Launchpad and is called [freecad-
daily](https://launchpad.net/~freecad-maintainers/+archive/freecad-daily).

This version is compiled daily from the official master repository. Please
beware that although it will contain new features and bug fixes, it may also
have newer bugs, and be unstable.

Add the daily PPA to your software sources, update the package lists, and
install the daily package:

    
    
    sudo add-apt-repository ppa:freecad-maintainers/freecad-daily
    sudo apt update
    sudo apt install freecad-daily
    

Every day you can update to the latest daily:

    
    
    sudo apt update
    sudo apt install freecad-daily
    

_Note:_ in some cases new code or dependencies added to FreeCAD will cause
packaging errors; if this happens, a daily package may not be generated until
the maintainers manually fix the problems. If you wish to continue testing the
latest code, you should get the source code and compile FreeCAD directly; for
instructions see [compiling](/Compiling "Compiling").

Run the daily (PPA) version of FreeCAD:

    
    
    
    freecad-daily
    

_Note:_ it is possible to install both the `-stable` and `-daily` packages in
the same system. This is useful if you wish to work with a stable version, and
still be able to test the latest features in development. Notice that the
executable for the daily version is `freecad-daily`, but for the stable
version it is just `freecad`.

## Debian and other Debian-based systems

Since Debian Lenny, FreeCAD is available directly from the Debian software
repositories and can be installed via synaptic or simply with:

    
    
    sudo apt install freecad
    

Expand

## OpenSUSE

FreeCAD is typically installed with YAST (abbr. Yet another Setup Tool) the
Linux operating system setup and configuration tool, or in any
terminal/console (root rights required) with:

    
    
    
    zypper install FreeCAD
    

_Note:_ This procedure only covers the installation of officially released
**stable** FreeCAD program versions, depending on the installed links to the
program package repositories of your OS version. The openSUSE package _may be
outdated_ as the packaging may lag behind the latest stable source code. In
this case, it is suggested to install the package manually from the below
indicated (Expand) source repositories.

A vast release program for FreeCAD package builds are offered. Please visit
for a survey:

**[Survey of repositories on
openSUSE](https://software.opensuse.org/search?utf8=%E2%9C%93&baseproject=ALL&q=FreeCAD)**

Generally for selecting the correct openSUSE distribution needed it is
necessary to click on the particular View button.

### Stable

The stable package version: [Stable repositories on
openSUSE](https://software.opensuse.org/package/FreeCAD). The correct openSUSE
distribution version must be selected in the lower part of the web page.

Note: openSUSE has several options to choose from when downloading FreeCAD. To
view these options, visit [Survey of stable repositories on
openSUSE](https://software.opensuse.org/search?utf8=%E2%9C%93&baseproject=ALL&q=FreeCAD).

### Development

Latest development releases AKA _unstable_ : [Unstable repositories listings
on
openSUSE](https://software.opensuse.org/download.html?project=science%3Aunstable&package=FreeCAD)

It is recommended to grab the binary packages directly. Then select the
correct distribution for your installed openSUSE OS.

## Gentoo

FreeCAD can be built/installed simply by issuing:

    
    
    emerge freecad
    

Expand

## Fedora

FreeCAD has been included in the official Fedora packages since Fedora 20
until 38. It can be installed from the command line with:

    
    
    sudo dnf install freecad
    

On older Fedora releases, that was:

    
    
    sudo yum install freecad
    

FreeCAD was removed in fedora 39 due to a [Python version
issue](https://pagure.io/fesco/issue/3080). Nightly builds are available
through a COPR repository at
<https://copr.fedorainfracloud.org/coprs/g/freecad/nightly/> for fedora 40 and
onwards.

The gui packages managers can also be used. Search for "freecad". The official
release package version tends to be well behind the FreeCAD releases.
[Package: freecad](http://rpms.remirepo.net/rpmphp/zoom.php?rpm=freecad) shows
the versions included in the Fedora repositories over time and versions.

More current versions can be obtained by downloading one of the
[.AppImage](https://github.com/FreeCAD/FreeCAD/releases/)releases from the
github repository. These work fine on Fedora.

If you want to keep up with the absolute latest daily builds, FreeCAD is also
available on
[copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/). To install
the build from there, in a terminal session, enter:

    
    
    sudo dnf copr enable @freecad/nightly
    sudo dnf install freecad
    

That leaves the copr repository active, so

    
    
    sudo dnf upgrade
    

or equivalent, will update to the latest FreeCAD build, along with updates
from any of the other active repos. If you want something a bit more stable,
you can disable @freecad/nightly again after the initial install. The copr
repository only keeps builds from the past 2 weeks. This is not a solution if
you want to pick a specific older version.

Instructions are also available on [compile FreeCAD
yourself](/Compile_on_Linux "Compile on Linux"), including a script
specifically for Fedora. With a minor change, to checkout the specific commit
from git, any version since about FreeCAD 0.15 can be built on any
distribution since Fedora 21.

## Arch

Installing FreeCAD on Arch Linux and derivatives (ex. Manjaro):

    
    
    pacman -S freecad
    

## Other

If you find out that your system features FreeCAD but is not documented in
this page, please tell us on the
[forum](https://forum.freecad.org/viewforum.php?f=21)!

Many alternative, non-official FreeCAD packages are available on the net, for
example for systems like slackware or fedora. A search on the net can quickly
give you some results.

### Installing on other Linux/Unix systems

Many common Linux distros now include a precompiled FreeCAD as part of the
standard packages. This is often out of date, but is a place to start. Check
the standard package managers for your system. One of the following (partial)
list of commands could install the official version of FreeCAD for your distro
from the terminal. These probably need administrator privileges.

    
    
    apt install freecad
    dnf install freecad
    emerge freecad
    slackpkg install freecad
    yum install freecad
    zypper install freecad
    pacman -Sy freecad
    

The package name is case sensitive, so try `FreeCAD` as well as `freecad`. If
that does not work for you, either because your package manager does not have
a precompiled FreeCAD version available, or because the available version is
too old for your needs, you can try installing the [Flatpak](/Flatpak
"Flatpak") or [Snap](/Ubuntu_Snap "Ubuntu Snap") packages (these work on most
x86_64 Linux distributions) or try downloading one of the
[.AppImage](https://github.com/FreeCAD/FreeCAD/releases/) releases from the
github repository. These also tend to work on most x86_64 Linux distributions,
without any special installation. Just make sure the downloaded file is marked
as executable, then run it.

If that still is not good enough, and you cannot locate another source of a
precompiled package for your situation, you will need to [compile FreeCAD
yourself](/Compile_on_Linux "Compile on Linux").

## Next Step

Head to [Getting started](/Getting_started "Getting started") once
installation is complete.

  

![](/images/6/6f/Arrow-left.svg) [Installing on
Windows](/Installing_on_Windows "Installing on Windows")

[Installing on Mac](/Installing_on_Mac "Installing on Mac")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

Expand[![](/images/thumb/9/94/User_hub.png/24px-
User_hub.png)](/index.php?title=File:User_hub.png&filetimestamp=20190221145008&)
[User documentation](/User_hub "User hub")

  * **[Getting started](/Getting_started "Getting started")**
  * **Installation:** [Download](/Download "Download"), [Windows](/Installing_on_Windows "Installing on Windows"), Linux, [Mac](/Installing_on_Mac "Installing on Mac"), [Additional components](/Installing_additional_components "Installing additional components"), [Docker](/Compile_on_Docker "Compile on Docker"), [AppImage](/AppImage "AppImage"), [Ubuntu Snap](/Ubuntu_Snap "Ubuntu Snap")
  * **Basics:** [About FreeCAD](/About_FreeCAD "About FreeCAD"), [Interface](/Interface "Interface"), [Mouse navigation](/Mouse_navigation "Mouse navigation"), [Selection methods](/Selection_methods "Selection methods"), [Object name](/Object_name "Object name"), [Preferences](/Preferences_Editor "Preferences Editor"), [Workbenches](/Workbenches "Workbenches"), [Document structure](/Document_structure "Document structure"), [Properties](/Property "Property"), [Help FreeCAD](/Help_FreeCAD "Help FreeCAD"), [Donate](/Donate "Donate")

* * *

  * **Help:** [Tutorials](/Tutorials "Tutorials"), [Video tutorials](/Video_tutorials "Video tutorials")
  * **[Workbenches](/Workbenches "Workbenches"):** [Std Base](/Std_Base "Std Base"), [Assembly](/Assembly_Workbench "Assembly Workbench"), [BIM](/BIM_Workbench "BIM Workbench"), [CAM](/CAM_Workbench "CAM Workbench"), [Draft](/Draft_Workbench "Draft Workbench"), [FEM](/FEM_Workbench "FEM Workbench"), [Inspection](/Inspection_Workbench "Inspection Workbench"), [Material](/Material_Workbench "Material Workbench"), [Mesh](/Mesh_Workbench "Mesh Workbench"), [OpenSCAD](/OpenSCAD_Workbench "OpenSCAD Workbench"), [Part](/Part_Workbench "Part Workbench"), [PartDesign](/PartDesign_Workbench "PartDesign Workbench"), [Points](/Points_Workbench "Points Workbench"), [Reverse Engineering](/Reverse_Engineering_Workbench "Reverse Engineering Workbench"), [Robot](/Robot_Workbench "Robot Workbench"), [Sketcher](/Sketcher_Workbench "Sketcher Workbench"), [Spreadsheet](/Spreadsheet_Workbench "Spreadsheet Workbench"), [Surface](/Surface_Workbench "Surface Workbench"), [TechDraw](/TechDraw_Workbench "TechDraw Workbench"), [Test Framework](/Testing "Testing")

* * *

  * **[Addons](/Addon "Addon"):** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

