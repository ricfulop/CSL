---
url: https://wiki.freecad.org/Compile_on_Docker
title: Compile on Docker
scraped_at: 2025-09-08 16:45:34
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Overview Toggle Overview subsection
    * 1.1 Benefits
  * 2 Docker Repository
  * 3 Prerequisites
  * 4 Installation Toggle Installation subsection
    * 4.1 Download the source
    * 4.2 Create build directory
    * 4.3 Pull Docker image
    * 4.4 Allow access to your window manager
      * 4.4.1 Mac OS users
    * 4.5 Launch the docker image
    * 4.6 Build FreeCAD
    * 4.7 Run FreeCAD
  * 5 Discussion
  * 6 Related

# Compile on Docker

  * [Page](/Compile_on_Docker "View the content page \[ctrl-option-c\]")
  * [Discussion](/Talk:Compile_on_Docker "Discussion about the content page \[ctrl-option-t\]")

English

  * [Read](/Compile_on_Docker)
  * [Edit](/index.php?title=Compile_on_Docker&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Compile_on_Docker&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Compile_on_Docker.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Compile_on_Docker&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Compile_on_Docker)
  * [Edit](/index.php?title=Compile_on_Docker&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Compile_on_Docker&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Compile_on_Docker&action=history)

General

  * [What links here](/Special:WhatLinksHere/Compile_on_Docker "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Compile_on_Docker "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Compile_on_Docker&oldid=1636723 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Compile_on_Docker&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Compile_on_Docker&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Compile+on+Docker&action=page&filter=&language=en)This is the approved
revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Compile+on+Docker&language=&task=view "Start translation for this language")
  * [Deutsch](/Compile_on_Docker/de "Kompilieren auf Docker \(100% translated\)")
  * English
  * [español](/Compile_on_Docker/es "Compilar en Docker \(38% translated\)")
  * [français](/Compile_on_Docker/fr "Compiler sous Docker \(100% translated\)")
  * [italiano](/Compile_on_Docker/it "Compilazione con Docker \(100% translated\)")
  * [polski](/Compile_on_Docker/pl "Kompilacja w środowisku Docker \(100% translated\)")
  * [português do Brasil](/Compile_on_Docker/pt-br "Compilar no Docker \(11% translated\)")
  * [русский](/Compile_on_Docker/ru "Компиляция в Docker \(11% translated\)")
  * [日本語](/Compile_on_Docker/ja "Dockerでのコンパイル \(3% translated\)")

This documentation is not finished. Please help and contribute documentation.

[GuiCommand model](/GuiCommand_model "GuiCommand model") explains how commands
should be documented. Browse
[Category:UnfinishedDocu](/Category:UnfinishedDocu "Category:UnfinishedDocu")
to see more incomplete pages like this one. See [Category:Command
Reference](/Category:Command_Reference "Category:Command Reference") for all
commands.

See [WikiPages](/WikiPages "WikiPages") to learn about editing the wiki pages,
and go to [Help FreeCAD](/Help_FreeCAD "Help FreeCAD") to learn about other
ways in which you can contribute.

![](/images/6/6f/Arrow-left.svg) [Compile on macOS](/Compile_on_MacOS "Compile
on MacOS")

[FreeCAD Docker CLI mode](/FreeCAD_Docker_CLI_mode "FreeCAD Docker CLI mode")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

## Overview

Among the options for building and installing FreeCAD, there is the option of
using Docker. This method is primarily useful for FreeCAD developers, using
Linux or Mac OS computers.

### Benefits

All of FreeCAD's dependencies are already installed, compatible with each
other, and configured appropriately, allowing you to get started developing
very quickly.

  * The dependencies are contained within the docker container, preventing any unwanted packages contaminating your workstation, and preventing any clashing versions.
  * The source code and build directories are outside the docker container. This allows you to use your preferred editors, versioning systems, dev tools etc, without having to set them up in the docker container. You can just use them as normal, right from your workstation. (Also, it means you don't have to rebuild the docker container each time you want to build FreeCAD.)
  * For those using obscure *nix distros and [instructions are not available](/Compile_on_Linux#Getting_the_dependencies "Compile on Linux") for fetching dependencies, all you need to install on your workstation is docker, which is quite commonly available across many distributions.
  * It provides a static, immutable development environment. I personally find this useful when developing to reduce the number of potential variables that could be causing an issue. You know you've not altered something esoteric in the environment between builds. For developers collaborating, and both using the same docker container, you can be sure you're both working from the same environment, which reduces communication errors caused by differences in environment.

## Docker Repository

  * Original: <https://gitlab.com/daviddaish/freecad_docker_env>
  * Official: <https://GitHub.com/FreeCAD/Docker>

## Prerequisites

  * 10GB of free storage
  * Docker

## Installation

### Download the source

The best way to get FreeCAD's source code is to clone the [Git
repository](https://github.com/FreeCAD/FreeCAD). For this you need the `git`
program which can be easily installed in most Linux and Mac OS distributions,
and it can also be obtained from the [official website](http://git-scm.com/).

This will place a copy of the latest version of the FreeCAD source code in a
new directory called `freecad_source`.

    
    
    git clone --recurse-submodules https://github.com/FreeCAD/FreeCAD.git ~/my_code/freecad_source
    

For more information on using Git, and contributing code to the project, see
[Source code management](/Source_code_management "Source code management").

### Create build directory

Create a directory to hold your compiled FreeCAD source.

    
    
    mkdir ~/my_code/freecad_build
    

### Pull Docker image

Pull the Docker image. (Official image coming soon.)

    
    
    docker pull registry.gitlab.com/daviddaish/freecad_docker_env:latest
    

### Allow access to your window manager

In order for FreeCAD to launch it's GUI from within the Docker container, you
need to give Docker access permissions to your window manager. In most Linux
distributions, this is the X window system. You can use the below command to
allow blanket access to X, until you reboot or logoff your computer.

    
    
    xhost +
    

If you're connected to any untrusted systems, such as via `ssh`, this will
make you vulnerable to malicious code. Either close any `ssh` connections, or
look into more secure xhost permissions, which is outside the scope of this
tutorial.

#### Mac OS users

For those using Mac OS, the X window system may not be installed. The XQuartz
project is a long running open source project that will allow you to add it to
your computer. [You can find it here](https://www.xquartz.org/).

### Launch the docker image

Assign environment variables so the Docker container will mount FreeCAD's
source code, and build directory. In addition, you can mount an extra
directory to contain any files you'd like to use for testing purposes. In the
below snippet, we've left it as your home directory as a simple default.

    
    
    fc_source=~/my_code/freecad_source
    fc_build=~/my_code/freecad_build
    other_files=~/
    

Launch the Docker image.

    
    
    docker run -it --rm \
    -v $fc_source:/mnt/source \
    -v $fc_build:/mnt/build \
    -v $other_files:/mnt/files \
    -e "DISPLAY" -e "QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:ro \
    registry.gitlab.com/daviddaish/freecad_docker_env:latest
    

### Build FreeCAD

You can build FreeCAD using the installed build script, or using your
preferred method.

    
    
    /root/build_script.sh
    

### Run FreeCAD

Once FreeCAD has been built, it can be run as normal.

    
    
    /mnt/build/bin/FreeCAD
    

You can find the attached directories in the `/mnt` directory.

## Discussion

  * [Docker env build container](https://forum.freecad.org/viewtopic.php?f=4&t=42954)
  * [VSCode setup with Docker (1)](https://forum.freecad.org/viewtopic.php?f=10&t=48266)
  * [VSCode setup with Docker (2)](https://forum.freecad.org/viewtopic.php?p=427812#p427812)

## Related

  * [AppImage](/AppImage "AppImage")

  

![](/images/6/6f/Arrow-left.svg) [Compile on macOS](/Compile_on_MacOS "Compile
on MacOS")

[FreeCAD Docker CLI mode](/FreeCAD_Docker_CLI_mode "FreeCAD Docker CLI mode")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

Expand[![](/images/thumb/9/94/User_hub.png/24px-
User_hub.png)](/index.php?title=File:User_hub.png&filetimestamp=20190221145008&)
[User documentation](/User_hub "User hub")

  * **[Getting started](/Getting_started "Getting started")**
  * **Installation:** [Download](/Download "Download"), [Windows](/Installing_on_Windows "Installing on Windows"), [Linux](/Installing_on_Linux "Installing on Linux"), [Mac](/Installing_on_Mac "Installing on Mac"), [Additional components](/Installing_additional_components "Installing additional components"), Docker, [AppImage](/AppImage "AppImage"), [Ubuntu Snap](/Ubuntu_Snap "Ubuntu Snap")
  * **Basics:** [About FreeCAD](/About_FreeCAD "About FreeCAD"), [Interface](/Interface "Interface"), [Mouse navigation](/Mouse_navigation "Mouse navigation"), [Selection methods](/Selection_methods "Selection methods"), [Object name](/Object_name "Object name"), [Preferences](/Preferences_Editor "Preferences Editor"), [Workbenches](/Workbenches "Workbenches"), [Document structure](/Document_structure "Document structure"), [Properties](/Property "Property"), [Help FreeCAD](/Help_FreeCAD "Help FreeCAD"), [Donate](/Donate "Donate")

* * *

  * **Help:** [Tutorials](/Tutorials "Tutorials"), [Video tutorials](/Video_tutorials "Video tutorials")
  * **[Workbenches](/Workbenches "Workbenches"):** [Std Base](/Std_Base "Std Base"), [Assembly](/Assembly_Workbench "Assembly Workbench"), [BIM](/BIM_Workbench "BIM Workbench"), [CAM](/CAM_Workbench "CAM Workbench"), [Draft](/Draft_Workbench "Draft Workbench"), [FEM](/FEM_Workbench "FEM Workbench"), [Inspection](/Inspection_Workbench "Inspection Workbench"), [Material](/Material_Workbench "Material Workbench"), [Mesh](/Mesh_Workbench "Mesh Workbench"), [OpenSCAD](/OpenSCAD_Workbench "OpenSCAD Workbench"), [Part](/Part_Workbench "Part Workbench"), [PartDesign](/PartDesign_Workbench "PartDesign Workbench"), [Points](/Points_Workbench "Points Workbench"), [Reverse Engineering](/Reverse_Engineering_Workbench "Reverse Engineering Workbench"), [Robot](/Robot_Workbench "Robot Workbench"), [Sketcher](/Sketcher_Workbench "Sketcher Workbench"), [Spreadsheet](/Spreadsheet_Workbench "Spreadsheet Workbench"), [Surface](/Surface_Workbench "Surface Workbench"), [TechDraw](/TechDraw_Workbench "TechDraw Workbench"), [Test Framework](/Testing "Testing")

* * *

  * **[Addons](/Addon "Addon"):** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

