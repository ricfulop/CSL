---
url: https://developer.rhino3d.com/guides/cpp/whats-new/
scraped_at: 2025-09-08T15:38:27.317042
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

[What's New?](https://developer.rhino3d.com/guides/cpp/whats-new/)

  * Overview
  * Rhino 8
    * Visual Studio 2019 (v142)
  * Rhino 7
    * Visual Studio 2019 (v142)
    * Subdivision Surfaces
  * Deprecation
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

What's New?

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated: Monday,
October 7, 2024)

## Overview

The Rhino C/C++ SDK is _not_ an abstract SDK. That is, the native classes and
functions that are made available in the SDK are also used internally by
Rhino. Thus, when the signatures of classes or functions change, all
developers, both internal and external, are required to modify their source
code to accommodate for the change.

For this reason, the Rhino C/C++ SDK was _not_ broken between Rhino 6, 7 and
8. Thus, plug-ins written for Rhino 7 using the Rhino 7 C/C++ SDK should load
and run without modification in Rhino 8. However, we do encourage developers
to migrate their plug-in projects to Rhino 8 so they can take advantage to new
and enhanced features.

## Rhino 8

### Visual Studio 2019 (v142)

To write C++ plug-ins for Rhino 8 using the Rhino 8 C/C++ SDK, you will need a
version of Microsoft Visual Studio that includes the Visual Studio 2019 (v142)
platform toolset. Thus, you can use either [Visual Studio
2022](https://visualstudio.microsoft.com/downloads/) or [Visual Studio
2019](https://visualstudio.microsoft.com/vs/older-downloads/).

There is a new [Rhino Visual Studio
Extension](https://github.com/mcneel/RhinoVisualStudioExtensions/releases),
which includes project and command templates, that installs independently of
Rhino C/C++ SDK.

## Rhino 7

### Visual Studio 2019 (v142)

To write C++ plug-ins for Rhino 7 using the Rhino 7 C/C++ SDK, you will need a
version of Microsoft Visual Studio that includes the Visual Studio 2019 (v142)
platform toolset. Thus, you can use either [Visual Studio
2022](https://visualstudio.microsoft.com/downloads/) or [Visual Studio
2019](https://visualstudio.microsoft.com/vs/older-downloads/).

Rhino 7 C/C++ SDK includes project and command wizards. Thus, you’ll need to
have Visual Studio 2019 installed on your system before installing the Rhino 7
C/C++ SDK.

### Subdivision Surfaces

A new subdivision surface object has been added to Rhino 7. The core geometry
component is `ON_SubD` class, which is also part of openNURBS. All subdivision
code will be available in the Rhino plug-in SDK.

The `ON_SubD` class has full support for Catmull-Clark quad subdivision
surfaces and for Loop-Warren triangle subdivision surfaces. The Rhino
subdivision surface control polygons have no limits on vertex valences (edge
and face counts) or facet edge counts.

Rhino subdivision objects are automatically converted to cubic NURBS
polysurfaces or meshes when a subdivision object is selected as input to a
command that is expecting a polysurface or mesh. This is how Rhino’s
lightweight extrusion object behaves.

## Deprecation

Obsolete functions from Rhino are marked as deprecated with a message to help
accomplish the same goal through alternate functions in the Rhino C/C++ SDK.
These deprecations will generate compiler warnings when plug-in code attempts
to call these functions.

Functions marked as deprecated may or may not continue to work in future Rhino
versions. Thus, you should replace all calls to deprecated functions with
calls to their replacements before distributing any plug-in.

## Related Topics

  * [Installing Tools (Windows)](https://developer.rhino3d.com/guides/cpp/installing-tools-windows/)
  * [C++ SDK samples on GitHub](https://github.com/mcneel/rhino-developer-samples)
  * [Migrate Rhino 6 plug-in projects to Rhino 7](https://developer.rhino3d.com/guides/cpp/migrate-your-plugin-windows/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/whats-
new/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/whats-
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

