---
url: https://developer.rhino3d.com/guides/cpp/migrate-your-plugin-windows/
scraped_at: 2025-09-08T15:38:33.217869
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
7](https://developer.rhino3d.com/guides/cpp/migrate-your-plugin-windows/)

  * Prerequisites
  * Migrate the project
  * Replace property sheets
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Migrate your plug-in project to Rhino 7

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated: Friday,
August 28, 2020)

## Prerequisites

It is presumed you already have the necessary tools installed and are ready to
go. If you are not there yet, see [Installing Tools
(Windows)](https://developer.rhino3d.com/guides/cpp/installing-tools-windows/)

## Migrate the project

To migrate your Rhino 6 C++ plugin project to Rhino 7:

  1. Launch _Visual Studio 2019_ and click _File_ > _Open_ > _Project/Solution…_.
  2. Navigate to your project’s folder and open either your plugin project _(.vcxproj)_ or solution _(.sln)_
  3. When your plugin project opens, Visual Studio will display the _Retarget Projects_ dialog box. Specify the following actions and then click _OK_.  
![Retarget Projects](https://developer.rhino3d.com/images/migrate-plugin-
windows-cpp-02.png)

## Replace property sheets

The Rhino C/C++ SDK includes Visual Studio Property Sheets that provide a
convenient way to synchronize or share common settings among other plugin
projects. You will need to remove references to Rhino 6 C/C++ SDK property
sheets and replace them with references to Rhino 7 C/C++ SDK property sheets.

  1. From _Visual Studio 2019_ , click _View_ > _Property Manager_. ![Property Manager](https://developer.rhino3d.com/images/migrate-plugin-windows-cpp-01.png)
  2. Right-click on the _Rhino.Cpp.PlugIn_ property sheets in both _Debug | x64_ and _Release | x64_ configurations and click _Remove_.
  3. Right-click on the _Debug | x64_ configuration and click _Add Existing Property Sheet_.
  4. Navigate to the following location: _C:\Program Files\Rhino 7.0 SDK\PropertySheets_
  5. Select _Rhino.Cpp.PlugIn.props_ and click _OK_.
  6. Repeat the above steps for the the _Release | x64_ configuration.
  7. Save the changes to your solution.

Your plugin project should now be ready to build with the Rhino 7 C/C++ SDK.

## Related Topics

  * [What’s New?](https://developer.rhino3d.com/guides/cpp/whats-new/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/migrate-
your-plugin-windows/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/migrate-
your-plugin-windows/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

