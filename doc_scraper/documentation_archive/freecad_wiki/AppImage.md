---
url: https://wiki.freecad.org/AppImage
title: AppImage
scraped_at: 2025-09-08 16:45:35
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 What is an AppImage?
  * 2 FreeCAD AppImages Toggle FreeCAD AppImages subsection
    * 2.1 Obligatory Word of Caution
  * 3 Automatic updating Toggle Automatic updating subsection
    * 3.1 Experimental in-app updating
    * 3.2 GUI method 1 (official)
    * 3.3 GUI method 2 (unofficial)
    * 3.4 CLI method 1 (official)
    * 3.5 CLI method 2 (unofficial)
  * 4 Experimental Toggle Experimental subsection
    * 4.1 Fixing AppImage zsync
    * 4.2 Downloading via Bittorrent
  * 5 Developer Section Toggle Developer Section subsection
    * 5.1 Unpacking AppImages
      * 5.1.1 Modifying AppImages
      * 5.1.2 Repackaging AppImages
    * 5.2 Personalized AppImages
    * 5.3 Related

# AppImage

  * [Page](/AppImage "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:AppImage&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/AppImage)
  * [Edit](/index.php?title=AppImage&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=AppImage&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/AppImage.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=AppImage&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/AppImage)
  * [Edit](/index.php?title=AppImage&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=AppImage&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=AppImage&action=history)

General

  * [What links here](/Special:WhatLinksHere/AppImage "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/AppImage "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=AppImage&oldid=1624288 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=AppImage&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=AppImage&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
AppImage&action=page&filter=&language=en)This is the approved revision of this
page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-AppImage&language=&task=view "Start translation for this language")
  * [Deutsch](/AppImage/de "AnwendungsAbbild \(100% translated\)")
  * English
  * [español](/AppImage/es "Imágenes de las aplicaciones \(28% translated\)")
  * [français](/AppImage/fr "AppImage \(100% translated\)")
  * [italiano](/AppImage/it "AppImage \(100% translated\)")
  * [polski](/AppImage/pl "AppImage \(100% translated\)")
  * [português do Brasil](/AppImage/pt-br "AppImage \(2% translated\)")
  * [русский](/AppImage/ru "AppImage \(98% translated\)")
  * [日本語](/AppImage/ja "AppImage \(2% translated\)")

## What is an AppImage?

[![](/images/a/ab/AppImage-logo.png)](https://appimage.org) _Package once and
run everywhere. Reach users on all major Linux desktop distributions._

AppImage is a "universal binary package" intended to distribute an application
to any Linux distribution. Read more about it on the [Appimage
homepage](https://appimage.org) and
[Wikipedia](https://en.wikipedia.org/wiki/AppImage).

To run it, first make it executable, and then type the relative or full path.

    
    
    chmod +x FreeCAD_xxx-x86_64.AppImage
    ./FreeCAD_xxx-x86_64.AppImage
    

For other types of installation see [Download](/Download "Download").

## FreeCAD AppImages

Available FreeCAD AppImages  Stable  | Development   
---|---  
[![](/images/a/ab/AppImage-logo.png)](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/1.0.2) [v1.0.2](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/1.0.2) | [![](/images/a/ab/AppImage-logo.png)](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds) [Weekly build](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds)  
  
**Important Notes:**

  * Development happens daily and rapidly.
  * Many users on the forum utilize the development version.
  * It can be run on the same system in parallel with another version of FreeCAD.
  * Users use the dev version to take advantage of the latest features and bug fixes (since FreeCAD has a long release cycle). They also use it to help test and find bugs to spur development and improvement of FreeCAD.

#### Obligatory Word of Caution

For the most part the development version is stable but of course it's
important to add the obligatory statement to use it at your own risk. Though
most people that utilize backups and 'save often' do quite well.

## Automatic updating

AppImage has a smart and economical way of updating. It calculates the
difference between the new AppImage and the old one, and will only download
the changes between their versions. In theory the user ends up downloading
around 15% each time instead of an entirely new AppImage.

Automatic updating is done via several optional methods. Currently there are 4
methods, 2 through the graphical interface (GUI), and 2 through the command-
line/terminal interface (CLI).

### Experimental in-app updating

Thanks to the efforts of several key devs, there is an [ongoing
effort](https://forum.freecad.org/viewtopic.php?f=8&t=44324) to integrate a
feature that allows **self-updating the AppImage within FreeCAD** itself.
Starting from FC 0.19.21514 there now exists an AppImage section found via
**Edit → Preferences → AppImage**. Please test this capability and report your
experience to the [forum
discussion](https://forum.freecad.org/viewtopic.php?f=8&t=44324).

### GUI method 1 (official)

This is the official AppImageUpdate GUI application.

  1. Download [AppImageUpdate-x86_64.AppImage](https://github.com/AppImage/AppImageUpdate/releases/download/continuous/AppImageUpdate-x86_64.AppImage).
  2. Make it executable by right clicking on the file, going in to properties and "Run as an executable".
  3. Double click on the AppImage icon, a dialog box will appear and you'll be prompted to specify what AppImage you want to update.
  4. Specify the path to your existing AppImage.
  5. Once the AppImage is updated, press the button Run updated AppImage.

### GUI method 2 (unofficial)

This is a sleeker 3rd-party unofficial version of AppImageUpdate named:
**AppImageUpdater**. It is still in development (at the time of this wiki
edit) but nevertheless, quite nice to use.

  1. Download [AppImageUpdater-*-x86_64.AppImage](https://github.com/antony-jr/AppImageUpdater/releases/tag/continuous)
  2. Make it executable: 
         
         chmod +x AppImageUpdater*-x86_64.AppImage
         

  3. Run it: 
         
         source AppImageUpdater*-x86_64.AppImage
         

  4. Find your current FreeCAD AppImage and drag-drop it on to the AppImageUpdater

Result: Follow the AppImageUpdater prompts

### CLI method 1 (official)

Run the following instructions in your terminal

    
    
    wget https://github.com/AppImage/AppImageUpdate/releases/download/continuous/appimageupdatetool-x86_64.AppImage
    chmod +x ./appimageupdatetool-x86_64.AppImage
    ./appimageupdatetool.AppImage path/to/old/FreeCAD.AppImage
    chmod +x path/to/updated/FreeCAD.AppImage
    ./path/to/updated/FreeCAD.AppImage
    

Notes:

  * The file names will be unique because of the version info is embedded in them. The above instructions are simplified for convenience.
  * Run `./appimageupdatetool-x86_64.AppImage --help` to learn about functionality like `--remove-old`, `--overwrite` and `--self-update`.
  * There is also an i386 version; see the [AppImageUpdate release](https://github.com/AppImage/AppImageUpdate/releases) page.

Todo: share a script that can be added as an alias or
[cron](https://en.wikipedia.org/wiki/Cron) job.

### CLI method 2 (unofficial)

Similarly to the Graphical methods having an official and unofficial
approaches to downloading AppImages, the same applies to the command line.
This is a sleeker 3rd-party command line option to download AppImages.

  1. Download [appimageupdater-*-x86_64.AppImage](https://github.com/antony-jr/AppImageUpdater/releases/tag/continuous-cli)
  2. Make it executable: 
         
         chmod +x appimageupdater*-x86_64.AppImage
         

  3. Run it: 
         
         source appimageupdater*-x86_64.AppImage /path/to/old/FreeCAD-AppImage.AppImage
         

**Result** : Updates specified AppImage file if update exists

  

# Experimental

## Fixing AppImage zsync

It may happen that an AppImage won't update because it's target file changed
in some way. Instead of downloading a whole new AppImage, it's possible to
rewrite the zsync file that is used by the AppImage to download the delta.
More info can be found at <https://github.com/antony-jr/appimage-update-info-
writer>.

This section needs more details.

## Downloading via Bittorrent

An experimental feature that the FreeCAD packaging team is exploring (thanks
to the work of Antony-jr) is being able to download an appimage delta of
FreeCAD via bittorrent. The repository issue is at
<https://github.com/FreeCAD/FreeCAD-Bundle/issues/49>

# Developer Section

_Note:_ the following sections are intended for developers

## Unpacking AppImages

A very convenient aspect of FreeCAD is that a majority of it is built in
[Python](/Python "Python"), which doesn't need to be manually compiled like
C++. Essentially, a Python file can be modified, and upon restarting FreeCAD
those changes will be integrated into the application. A developer can quickly
work on the latest FreeCAD release using this technique and an AppImage.
Moreover, using an AppImage doesn't modify your system's environment in any
way, that is, nothing is installed and no environmental variables are
modified.

### Modifying AppImages

An AppImage embeds a file system in it with everything that is required to run
the application. In order to modify it, the file system needs to be extracted.

    
    
    ./FreeCAD_xxx.AppImage --appimage-extract
    cd squashfs-root/
    

Now open the required Python source files in your preferred code editor,
modify them, and save them. Then run the application.

    
    
    ./AppRun
    

### Repackaging AppImages

If you've modified the code, and now want to re-package the AppImage with your
latest changes, use the
[appimagetool-x86_64](https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage)
tool on the extracted file system.

    
    
    cd ..
    wget "https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage"
    chmod +x appimagetool-x86_64.AppImage
    ./appimagetool-x86_64.AppImage squashfs-root
    

## Personalized AppImages

Thanks to the work of _realthunder_ , author of [App Link](/App_Link "App
Link") and [Assembly3 Workbench](/Assembly3_Workbench "Assembly3 Workbench"),
it is possible to build custom AppImages using a set of scripts.

This makes it very convenient to release images for a specific branch of the
source code for others to test. Although AppImages only work on Linux,
realthunder's scripts make it possible to generate AppImages also on Windows
and MacOS.

The repository for these scripts is at
[realthunder/FreeCADMakeImage](https://github.com/realthunder/FreeCADMakeImage).
Please read the
[Readme.md](https://github.com/realthunder/FreeCADMakeImage/blob/master/Readme.md)
for more details.

## Related

  * [Snap](/Ubuntu_Snap "Ubuntu Snap") packages.
  * [Flatpak](/Flatpak "Flatpak") packages.

Expand[![](/images/thumb/9/94/User_hub.png/24px-
User_hub.png)](/index.php?title=File:User_hub.png&filetimestamp=20190221145008&)
[User documentation](/User_hub "User hub")

  * **[Getting started](/Getting_started "Getting started")**
  * **Installation:** [Download](/Download "Download"), [Windows](/Installing_on_Windows "Installing on Windows"), [Linux](/Installing_on_Linux "Installing on Linux"), [Mac](/Installing_on_Mac "Installing on Mac"), [Additional components](/Installing_additional_components "Installing additional components"), [Docker](/Compile_on_Docker "Compile on Docker"), AppImage, [Ubuntu Snap](/Ubuntu_Snap "Ubuntu Snap")
  * **Basics:** [About FreeCAD](/About_FreeCAD "About FreeCAD"), [Interface](/Interface "Interface"), [Mouse navigation](/Mouse_navigation "Mouse navigation"), [Selection methods](/Selection_methods "Selection methods"), [Object name](/Object_name "Object name"), [Preferences](/Preferences_Editor "Preferences Editor"), [Workbenches](/Workbenches "Workbenches"), [Document structure](/Document_structure "Document structure"), [Properties](/Property "Property"), [Help FreeCAD](/Help_FreeCAD "Help FreeCAD"), [Donate](/Donate "Donate")

* * *

  * **Help:** [Tutorials](/Tutorials "Tutorials"), [Video tutorials](/Video_tutorials "Video tutorials")
  * **[Workbenches](/Workbenches "Workbenches"):** [Std Base](/Std_Base "Std Base"), [Assembly](/Assembly_Workbench "Assembly Workbench"), [BIM](/BIM_Workbench "BIM Workbench"), [CAM](/CAM_Workbench "CAM Workbench"), [Draft](/Draft_Workbench "Draft Workbench"), [FEM](/FEM_Workbench "FEM Workbench"), [Inspection](/Inspection_Workbench "Inspection Workbench"), [Material](/Material_Workbench "Material Workbench"), [Mesh](/Mesh_Workbench "Mesh Workbench"), [OpenSCAD](/OpenSCAD_Workbench "OpenSCAD Workbench"), [Part](/Part_Workbench "Part Workbench"), [PartDesign](/PartDesign_Workbench "PartDesign Workbench"), [Points](/Points_Workbench "Points Workbench"), [Reverse Engineering](/Reverse_Engineering_Workbench "Reverse Engineering Workbench"), [Robot](/Robot_Workbench "Robot Workbench"), [Sketcher](/Sketcher_Workbench "Sketcher Workbench"), [Spreadsheet](/Spreadsheet_Workbench "Spreadsheet Workbench"), [Surface](/Surface_Workbench "Surface Workbench"), [TechDraw](/TechDraw_Workbench "TechDraw Workbench"), [Test Framework](/Testing "Testing")

* * *

  * **[Addons](/Addon "Addon"):** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

