---
url: https://developer.rhino3d.com/guides/cpp/migrate-your-plugin-manual-windows/
scraped_at: 2025-09-08T15:38:34.333960
title: Untitled
---

[RhinoDeveloper®](/)

[design, model, present, analyze, realize...](/)

[![Rhino Logo](https://developer.rhino3d.com/images/rhinodevlogo.png)](/)

__

[Guides](https://developer.rhino3d.com/guides)
[Samples](https://developer.rhino3d.com/samples)
[API](https://developer.rhino3d.com/api)
[Videos](https://developer.rhino3d.com/videos)
[Community](https://discourse.mcneel.com/c/rhino-developer) [my account
](https://www.rhino3d.com/my-account/ "Manage your account, licenses, and
teams")

[Migrate your plug-in project to Rhino
6](https://developer.rhino3d.com/guides/cpp/migrate-your-plugin-manual-
windows/)

  * Migrate the project
  * Remove 32-bit support
  * Rename build configurations
  * Add property sheet
  * Modify the project
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Migrate your plug-in project to Rhino 6

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated: Monday,
October 7, 2024)

It is presumed you already have the necessary tools installed and are ready to
go. If you are not there yet, see [Installing Tools
(Windows)](https://developer.rhino3d.com/guides/cpp/installing-tools-
windows/).

## Migrate the project

  1. Launch _Visual Studio 2017_ and click _File_ > _Open_ > _Project/Solution…_.
  2. Navigate to your project’s folder and open either your plugin project _(.vcxproj)_ or solution _(.sln)_
  3. When your plugin project opens, navigate to the project’s setting by clicking _Project_ > _Properties…_.
  4. In the project’s settings, set the _Configuration_ to _All Configurations_ , and set the platform to _x64_.
  5. Then, set the _Platform Toolset_ to _Visual Studio 2017 (v141)_ and the click _Apply_. ![Plugin Settings](https://developer.rhino3d.com/images/migrate-plugin-windows-cpp.png)

## Remove 32-bit support

Rhino 6 plugins are 64-bit only. If your plugin project has _Win32_ platform
support, then it is safe to remove it using _Visual Studio’s Configuration
Manager_.

  1. From _Visual Studio 2017_ , click _Build_ > _Configuration Manager…_. ![Configuration Manager](https://developer.rhino3d.com/images/migrate-plugin-windows-cpp-02.png)
  2. In _Project Contexts_ , click _Platform > Edit…_. ![Select Project Platforms](https://developer.rhino3d.com/images/migrate-plugin-windows-cpp-03.png)
  3. In _Edit Project Platforms_ , select the _Win32_ platform, click _Remove_ and then click _Close_. ![Edit Project Platforms](https://developer.rhino3d.com/images/migrate-plugin-windows-cpp-04.png)
  4. Repeat the above step for the solution by click _Active solution platform > Edit…_.
  5. In _Edit Solution Platforms_ , select the _Win32_ platform, click _Remove_ and then click _Close_.

## Rename build configurations

Rhino 6 plugin projects have different project build configuration names. In
order to use the new SDK Property Sheets, you will need to rename the plugin
project’s build configurations so they match the new build configuration
names.

  1. In _Project Contexts_ , click _Configuration > Edit…_. ![Select Project Configurations](https://developer.rhino3d.com/images/migrate-plugin-windows-cpp-05.png)
  2. In _Edit Project Configurations_ , remove the _Debug_ configuration.
  3. And then, rename the _PseudoDebug_ configuration to _Debug_. ![Edit Project Configurations](https://developer.rhino3d.com/images/migrate-plugin-windows-cpp-06.png)
  4. When you have finished renaming the configurations, click _Close_. ![Rename Project Configurations](https://developer.rhino3d.com/images/migrate-plugin-windows-cpp-07.png)
  5. Repeat the above step for the solution by click _Active solution Configuration > Edit…_.
  6. In _Edit Solution Configurations_ , remove the _Debug_ configuration, and then rename the _PseudoDebug_ configuration to _Debug_.
  7. When finished, click _Close_.
  8. Close _Configuration Manager_.

## Add property sheet

The Rhino C/C++ SDK includes Visual Studio Property Sheets that provide a
convenient way to synchronize or share common settings among other plugin
projects.

  1. From _Visual Studio 2017_ , click _View_ > _Property Manager_. ![Property Manager](https://developer.rhino3d.com/images/migrate-plugin-windows-cpp-08.png)
  2. Right-click on the _Debug | x64_ configuration and click _Add Existing Property Sheet_.
  3. Navigate to the following location: _C:\Program Files\Rhino 6.0 SDK\PropertySheets_
  4. Select _Rhino.Cpp.PlugIn.props_ and click _OK_.
  5. Repeat the above steps for the the _Release | x64_ configuration. ![Add Existing Property Sheet](https://developer.rhino3d.com/images/migrate-plugin-windows-cpp-09.png)

## Modify the project

The project’s pre-compiled header file, _stdafx.h_ , needs to be modified so
SDK header file inclusions point to the correct location. Also, the plugin
.cpp file needs to include an additional SDK header. Finally, Visual Studio’s
resource editor and compiler requires the project contain a _targetver.h_ file
that identifies the target platform.

  1. Using _Visual Studio’s Solution Explorer_ , open _stdafx.h_ and add the following preprocessor directive:
         
         /////////////////////////////////////////////////////////////////////////////
          // stdafx.h : include file for standard system include files,
          // or project specific include files that are used frequently, but
          // are changed infrequently
         
          #pragma once
         
          #ifndef VC_EXTRALEAN
          #define VC_EXTRALEAN        // Exclude rarely-used stuff from Windows headers
          #endif
         
          // Added for Rhino 6 Migration
          #define RHINO_V6_READY
         
          // If you want to use Rhino's MFC UI classes, then
          // uncomment the #define RHINO_SDK_MFC statement below. 
          // Note, doing so will require that your plug-in is
          // built with the same version of Visual Studio as was
          // used to build Rhino.
          //#define RHINO_SDK_MFC
         
          ...
         

  2. Also, remove the path specifiers to Rhino SDK header files found in _stdafx.h_ , as the path to the SDK is provided by the SDK Property Sheet added above.
         
         // Rhino SDK Preamble
          //#include "C:\Program Files (x86)\Rhino 5.0 x64 SDK\Inc\RhinoSdkStdafxPreamble.h"
          #include "RhinoSdkStdafxPreamble.h"
         
          ...
         
          // Rhino Plug-in
          //#include "C:\Program Files (x86)\Rhino 5.0 x64 SDK\Inc\RhinoSdk.h"
          #include "RhinoSdk.h"
         
          // Render Development Kit
          //#include "C:\Program Files (x86)\Rhino 5.0 x64 SDK\Inc\RhRdkHeaders.h"
          #include "RhRdkHeaders.h"
         
          ...
         
          // Rhino Plug-in Linking Pragmas
          //#include "C:\Program Files (x86)\Rhino 5.0 x64 SDK\Inc\rhinoSdkPlugInLinkingPragmas.h"
          #include "rhinoSdkPlugInLinkingPragmas.h"
         

  3. Using _Visual Studio’s Solution Explorer_ , open the project’s _PlugIn.cpp_ file and add the following SDK include statement:
         
         #include "StdAfx.h"
          #include "SamplePlugIn.h"
         
          // Added for Rhino 6 Migration
          #include "rhinoSdkPlugInDeclare.h"
         
          ...
         

  4. Using _Visual Studio’s Solution Explorer_ , right-click on the _Header Files_ folder and click _Add_ > _New Item…_.

  5. Add a new _Header File (.h)_ named _targetver.h_.

  6. Add the following content to it:
         
         #pragma once
         
          // Including SDKDDKVer.h defines the highest available Windows platform.
          // If you wish to build your application for a previous Windows platform,
          // include WinSDKVer.h and set the _WIN32_WINNT macro to the platform you
          // wish to support before including SDKDDKVer.h.
          #include "rhinoSdkWindowsVersion.h"
         
          #include <SDKDDKVer.h>
         

Your plugin project should now be ready to build with the Rhino 6 C/C++ SDK.

## Related Topics

  * [What is a Rhino Plugin?](https://developer.rhino3d.com/guides/general/what-is-a-rhino-plugin/)
  * [Installing Tools (Windows)](https://developer.rhino3d.com/guides/cpp/installing-tools-windows/)
  * [Migrate your plugin project to Rhino 6](https://developer.rhino3d.com/guides/cpp/migrate-your-plugin-windows/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/migrate-
your-plugin-manual-windows/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/migrate-
your-plugin-manual-windows/index.md) [
Admin](https://developer.rhino3d.com/admin)

[Find a Reseller](https://www.rhino3d.com/sales)

[Shop online](https://www.rhino3d.com/store) or find a
[Reseller](https://www.rhino3d.com/sales)

[Find a Reseller](https://www.rhino3d.com/sales)

[Privacy Policy](https://www.rhino3d.com/privacy) •
[About](https://www.rhino3d.com/mcneel/about) • [Contact
Us](https://www.rhino3d.com/mcneel/contact) • [
Language](https://www.rhino3d.com/language "Change to a different region or
language")

[Copyright © 1993-2025 Robert McNeel & Associates. All Rights
Reserved.](https://www.rhino3d.com/mcneel/about)

[](https://www.facebook.com/McNeelRhinoceros/)
[](https://twitter.com/bobmcneel) [](https://www.linkedin.com/groups/75313/)
[](https://www.youtube.com/user/RhinoGuide/videos) [](https://vimeo.com/rhino)
[![Blogger
icon](https://developer.rhino3d.com/images/blogger.svg)](http://blog.rhino3d.com/)
[![Food4Rhino](https://developer.rhino3d.com/images/f4r_icon_01.svg)](https://www.food4rhino.com)

