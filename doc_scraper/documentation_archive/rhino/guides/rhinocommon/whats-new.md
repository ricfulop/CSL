---
url: https://developer.rhino3d.com/guides/rhinocommon/whats-new/#rhino-7
scraped_at: 2025-09-08T16:06:17.922702
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

[What's New?](https://developer.rhino3d.com/guides/rhinocommon/whats-new/)

  * Overview
  * Rhino 8
  * Rhino 7

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

What's New?

by [Steve Baer](https://discourse.mcneel.com/u/stevebaer/) (Last updated:
Friday, April 25, 2025)

## Overview

The following document describes what has been added, what has changed, and
how to deal with these changes in the RhinoCommon SDK. A lot of effort has
been put into keeping RhinoCommon compatible with versions found in earlier
Rhino releaes. One goal of this document is to describe these breaking changes
and what to do about them.

## Rhino 8

Rhino 8 now uses the open source [.NET Core
Runtime](https://github.com/dotnet/runtime) for running .NET code on both
Windows and Mac. This brings some performance improvements and aligns the .NET
runtimes used across platforms. Previously, Rhino 7 and earlier used the [Mono
runtime](https://www.mono-project.com/) on Mac, and .NET Framework exclusively
on Windows.

On Windows, you can still optionally run using the .NET Framework runtime in
the case of compatibility issues or running inside other software that
requires it (e.g. Rhino.Inside Revit).

Most plugins are already compatible when running in .NET Core without any
recompilation, but in the case of any incompatibilities you may need to update
your plugin.

For more details, see [Moving to .NET
Core](https://developer.rhino3d.com/guides/rhinocommon/moving-to-dotnet-
core/).

Also, we’ve updated the [Rhino Visual Studio
Extension](https://github.com/mcneel/RhinoVisualStudioExtensions/releases) for
both Windows and Mac.

And, there is an all new [RhinoCommon API
Reference](https://developer.rhino3d.com/api/rhinocommon/html/R_Project_RhinoCommon.htm)
online.

Here is what is new in [RhinoCommon
8](https://developer.rhino3d.com/api/rhinocommon/whatsnew/8.0).

## Rhino 7

RhinoCommon plug-ins for Rhino 7 are based on the Microsoft .NET Framework
4.8.

To developer plug-is Windows, use either [Visual Studio
2022](https://visualstudio.microsoft.com/downloads/) or [Visual Studio
2019](https://visualstudio.microsoft.com/vs/older-downloads/).

To develop plug-in on Mac, use [Visual Studio 2022 for
Mac](https://visualstudio.microsoft.com/vs/mac/). Visual Studio 2019 for Mac
should work as well.

Here is what is new in [RhinoCommon
7](https://developer.rhino3d.com/api/rhinocommon/whatsnew/7.0).

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/whats-
new/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/whats-
new/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

