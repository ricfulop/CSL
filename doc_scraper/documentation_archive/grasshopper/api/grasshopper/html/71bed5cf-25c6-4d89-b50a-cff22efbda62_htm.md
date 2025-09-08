---
url: https://developer.rhino3d.com/api/grasshopper/html/71bed5cf-25c6-4d89-b50a-cff22efbda62.htm#ManualDebugStartAction
scraped_at: 2025-09-08T16:25:07.476784
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Development](../html/8b9acc0a-5165-4427-aea5-1873faffb4ff.htm "Development")

[GHA Assembly Wizards](../html/d5ac95cc-3592-49a7-9162-d1bd981fb6c5.htm "GHA
Assembly Wizards")

[Assembly Hierarchy](../html/bc188193-19ff-4ae5-a3ed-2e78c34a306e.htm
"Assembly Hierarchy")

[Project Setup (VB.NET)](../html/99f64b89-5975-4ebe-adc6-24da038e915f.htm
"Project Setup \(VB.NET\)")

[Project Setup (C#)](../html/f00ac74b-492c-44fe-8da3-b28265dc820f.htm "Project
Setup \(C#\)")

[Project Setup (VS.Express)](../html/71bed5cf-25c6-4d89-b50a-cff22efbda62.htm
"Project Setup \(VS.Express\)")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# Project Setup (VS.Express)  
  
---  
  
**Please note that we now have[Assembly Wizards for
Grasshopper](d5ac95cc-3592-49a7-9162-d1bd981fb6c5.htm) and it is no longer
necessary to manually create a GHA project in Visual Studio.**

If you are using the Express version of Visual Studio, then you might not be
able to apply all required settings through the VS User Interface. In this
case you'll have to modify the project files manually to apply the settings.

**If you are using Visual Studio Professional, you can safely ignore this
page.**

This document outlines how to manually modify _csproj_ and _vbproj_ files.

  * Override Configuration Folders
  * Add Post-Build Events
  * Set Debug Start Action

![](../icons/SectionExpanded.png)Override Configuration Folders

It is useful to override the Visual Studio default behaviour regarding build
configuration output. By default, DEBUG and RELEASE configurations (or
'flavours') are outputted to unique folders. This can cause confusion during
debugging.

In order to override the output folders, open the project file in a text
editor. If you're using VB then the project file will have the _*.vbproj_
extension. If you're using C# then the project file will have the _*.csproj_
extension. Ideally you should use a text editor that understands xml-
formatting, but Notepad will do.

Inside the project file, locate the property group that has to do with the
Debug and Release configurations. They will probably be called:

XML

Copy

    
    
    <PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Debug|AnyCPU' ">
    <PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Release|AnyCPU' ">

Inside these property groups you will find OutputPath nodes:

XML

Copy

    
    
    <OutputPath>bin\Debug\</OutputPath>
    <OutputPath>bin\Release\</OutputPath>

You'll have to change these to point to the same folder. We recommend:

XML

Copy

    
    
    <OutputPath>bin\</OutputPath>

![](../icons/SectionExpanded.png)Add Post-Build Events

It is vital to add a Post-Build event to a Grasshopper Component Library since
Grasshopper will only consider _*.gha_ files during plug-in loading. Since
your project is a _Class Library_ , it will automatically be compiled into a
_*.dll_ file.

In order to override the output folders, open the project file in a text
editor. If you're using VB then the project file will have the _*.vbproj_
extension. If you're using C# then the project file will have the _*.csproj_
extension. Ideally you should use a text editor that understands xml-
formatting, but Notepad will do.

By default, a project file (vbproj for VB.NET; csproj for C#) does not contain
any Build Events, so you'll have to add the entire section in the project file
Xml data. Navigate towards the bottom of the project file. Just before the
closing </Project> tag, insert the following PropertyGroup:

XML

Copy

    
    
    <PropertyGroup>
      <PostBuildEvent>Copy "$(TargetPath)" "$(TargetDir)\$(ProjectName).gha"
                      Erase "$(TargetPath)"
      </PostBuildEvent>
    </PropertyGroup>

![](../icons/SectionExpanded.png)Set Debug Start Action

It is not possible to directly debug a Grasshopper Component Library, since it
must be loaded by Grasshopper, which in turn must be loaded by Rhinoceros. So,
in order to debug a _*.gha_ file you must first start Rhino. This is called a
_Debug Start Action_ and VS Express does not allow you to set one via its own
UI.

TODO, Finish this topic...

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

