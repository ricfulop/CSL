---
url: https://developer.rhino3d.com/guides/cpp/what-is-the-cpp-sdk/
scraped_at: 2025-09-08T15:38:26.303704
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

[What is the C/C++ SDK?](https://developer.rhino3d.com/guides/cpp/what-is-the-
cpp-sdk/)

  * Types of Plugins

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

What is the C/C++ SDK?

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated: Monday,
October 7, 2024)

The Rhino C/C++ Software Development Kit (SDK) is an set of developer
resources for customizing and extending Rhino for Windows. The SDK provides
tools that provide direct access to its database structures, geometry,
graphics system, file I/O, command definitions, and much more.

The Rhino C/C++ SDK consists primarily of C++ headers and libraries that can
be used to build Rhino extensions called _Plugins_. Plugins are Windows DLLs
that can be loaded into the Rhino process and interact directly with the Rhino
application. Rhino plugin modules use the file extension _.rhp_ instead of the
more common _.dll_.

The Rhino C/C++ SDK is for Rhino for Windows only. There currently is no Rhino
C/C++ SDK for Rhino for Mac.

## Types of Plugins

Rhino supports five different types of plugins:

Type | Description  
---|---  
**General Utility** | A general purpose utility that can contain one or more commands.  
**File Import** | Imports data from other file formats into Rhino; can support multiple file formats.  
**File Export** | Exports data from Rhino to other file formats; can support multiple file formats.  
**Custom Rendering** | Applies materials, textures, and lights to a scene to produce rendered images.  
**3D Digitizing** | Interfaces with 3D digitizing and other alternative input devices.  
  
Note: File Import, File Export, Custom Rendering and 3D Digitizing plugins are
all specialized enhancements to the General Utility plugin. Thus, all plugin
types can contain one or more commands.

As with all of our development tools, the Rhino C/C++ SDK is free, royalty
free, and includes free developer support.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/what-
is-the-cpp-sdk/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/what-
is-the-cpp-sdk/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

