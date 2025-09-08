---
url: https://wiki.freecad.org/Branding
title: Branding
scraped_at: 2025-09-08 16:44:53
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Overview
  * 2 Warning
  * 3 General
  * 4 Images
  * 5 Branding XML

# Branding

  * [Page](/Branding "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Branding&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Branding)
  * [Edit](/index.php?title=Branding&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Branding&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Branding.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Branding&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Branding)
  * [Edit](/index.php?title=Branding&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Branding&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Branding&action=history)

General

  * [What links here](/Special:WhatLinksHere/Branding "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Branding "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Branding&oldid=1609327 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Branding&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Branding&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Branding&action=page&filter=&language=en)This is the approved revision of this
page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Branding&language=&task=view "Start translation for this language")
  * [Deutsch](/Branding/de "Markenbildung \(100% translated\)")
  * English
  * [Türkçe](/Branding/tr "Branding \(5% translated\)")
  * [español](/Branding/es "Branding \(16% translated\)")
  * [français](/Branding/fr "Branding \(100% translated\)")
  * [hrvatski](/Branding/hr "Branding/hr \(5% translated\)")
  * [italiano](/Branding/it "Marchiare o Personalizzare FreeCAD \(100% translated\)")
  * [polski](/Branding/pl "FreeCAD jako produkt obcej marki \(100% translated\)")
  * [português do Brasil](/Branding/pt-br "Branding \(42% translated\)")
  * [română](/Branding/ro "Branding \(16% translated\)")
  * [svenska](/Branding/sv "Branding \(16% translated\)")
  * [čeština](/Branding/cs "Branding \(5% translated\)")
  * [русский](/Branding/ru "Брендирование \(21% translated\)")
  * [中文（中国大陆）](/Branding/zh-cn "品牌化 \(63% translated\)")
  * [日本語](/Branding/ja "ブランディング \(5% translated\)")
  * [한국어](/Branding/ko "프리캐드 개조하기 \(26% translated\)")

![](/images/6/6f/Arrow-left.svg) [Continuous
Integration](/Continuous_Integration "Continuous Integration")

[Localisation](/Localisation "Localisation") ![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

## Overview

This article describes the **Branding** of FreeCAD. Branding means to create
your own application based on FreeCAD. That can be only your own executable or
[splash screen](/Splash_screen "Splash screen") till a complete reworked
program. On base of the flexible architecture of FreeCAD it's easy to use it
as base for your own special purpose program.

## Warning

Although FreeCAD is offered to you free of charge, and the FreeCAD community
is happy to see other applications emerging, that are based on FreeCAD, we
have on the other hand seen a lot of unfair use of the information contained
on this page by people who simply rebranded FreeCAD into a closed-source
application to make profit from it.

Although the [LGPL license](/License "License") allows to use the FreeCAD
source code in closed-source applications, it also gives strict rules to do
so, and does not allow simply taking FreeCAD, renaming it and stripping it of
its license.

Would you be interested in using FreeCAD in a closed-source application, be
sure to check thoroughly the implications of the LGPL license, and, even
better, contact any FreeCAD developer, administrator or moderator before doing
so.

## General

Most of the branding is done in the MainCmd.cpp or MainGui.cpp. These Projects
generate the executable files of FreeCAD. To make your own Brand just copy the
Main or MainGui projects and give the executable its own name, e.g.
FooApp.exe. The most important settings for a new look are made in one place
in the main() function. Here is the code section that controls the branding:

    
    
    int main( int argc, char ** argv )
    {
        // Name and Version of the Application
        App::Application::Config()["ExeName"] = "FooApp";
        App::Application::Config()["ExeVersion"] = "0.7";
    
        // set the banner (for loging and console)
        App::Application::Config()["CopyrightInfo"] = sBanner;
        App::Application::Config()["AppIcon"] = "FooAppIcon";
        App::Application::Config()["SplashScreen"] = "FooAppSplasher";
        App::Application::Config()["StartWorkbench"] = "Part design";
        App::Application::Config()["HiddenDockWindow"] = "Property editor";
        App::Application::Config()["SplashAlignment" ] = "Bottom|Left";
        App::Application::Config()["SplashTextColor" ] = "#000000"; // black
    
        // Inits the Application 
        App::Application::Config()["RunMode"] = "Gui";
        App::Application::init(argc,argv);
    
        Gui::BitmapFactory().addXPM("FooAppSplasher", ( const char** ) splash_screen);
    
        Gui::Application::initApplication();
        Gui::Application::runApplication();
        App::Application::destruct();
    
        return 0;
    }
    

The first Config entry defines the program name. This is not the executable
name, which can be changed by renaming or by compiler settings, but the name
that is displayed in the task bar on windows or in the program list on Unix
systems.

The next lines define the Config entries of your FooApp Application. A
description of the Config and its entries you find in [Start up and
Configuration](/Start_up_and_Configuration "Start up and Configuration").

## Images

Image resources are compiled into FreeCAD using [Qt's resource
system](https://doc.qt.io/qt-6/resources.html). Therefore you have to write a
.qrc file, an XML-based file format that lists image files on the disk but
also any other kind of resource files. To load the compiled resources inside
the application you have to add a line

    
    
    Q_INIT_RESOURCE(FooApp);
    

into the main() function. Alternatively, if you have an image in XPM format
you can directly include it into your main.cpp and add the following line to
register it:

    
    
    Gui::BitmapFactory().addXPM("FooAppSplasher", ( const char** ) splash_screen);
    

## Branding XML

In FreeCAD there is also a method supported without writing a customized
main() function. For this method you must write a file name called
branding.xml and put it into the installation directory of FreeCAD. Here is an
example with all supported tags:

    
    
    <?xml version="1.0" encoding="utf-8"?>
    <Branding>
        <Application>FooApp</Application>
        <WindowTitle>Foo App in title bar</WindowTitle>
        <BuildVersionMajor>1</BuildVersionMajor>
        <BuildVersionMinor>0</BuildVersionMinor>
        <BuildRevision>1234</BuildRevision>
        <BuildRevisionDate>2014/1/1</BuildRevisionDate>
        <CopyrightInfo>(c) My copyright</CopyrightInfo>
        <MaintainerUrl>Foo App URL</MaintainerUrl>
        <ProgramLogo>Path to logo (appears in bottom right corner)</ProgramLogo>
        <WindowIcon>Path to icon file</WindowIcon>
        <ProgramIcons>Path to program icons</ProgramIcons>
        <SplashScreen>splashscreen.png</SplashScreen>
        <SplashAlignment>Bottom|Left</SplashAlignment>
        <SplashTextColor>#ffffff</SplashTextColor>
        <SplashInfoColor>#c8c8c8</SplashInfoColor>
        <StartWorkbench>PartDesignWorkbench</StartWorkbench>
    </Branding>
    

All listed tags are optional.

  

![](/images/6/6f/Arrow-left.svg) [Continuous
Integration](/Continuous_Integration "Continuous Integration")

[Localisation](/Localisation "Localisation") ![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

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

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

