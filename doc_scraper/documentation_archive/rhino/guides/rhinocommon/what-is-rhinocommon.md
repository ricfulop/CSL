---
url: https://developer.rhino3d.com/guides/rhinocommon/what-is-rhinocommon/#types-of-plugins
scraped_at: 2025-09-08T16:06:12.535527
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

[What is RhinoCommon?](https://developer.rhino3d.com/guides/rhinocommon/what-
is-rhinocommon/)

  * Inside RhinoCommon
  * Types of Plugins

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

What is RhinoCommon?

by [Steve Baer](https://discourse.mcneel.com/u/stevebaer/) (Last updated:
Monday, October 7, 2024)

RhinoCommon is the cross-platform .NET plugin SDK available for:

  * Rhino for Windows
  * Rhino for Mac
  * Rhino.Python Scripting
  * Grasshopper

The term _Common_ is meant to be just that: an SDK that can be used across
Rhino platforms. A plugin built with RhinoCommon could potentially run on both
Windows and Mac platforms with no changes.

![](https://developer.rhino3d.com/images/rhinocommon-one-binary-two-
platforms.png)

RhinoCommon is available as [NuGet
package](https://www.nuget.org/packages/rhinocommon).

## Inside RhinoCommon

RhinoCommon is composed of the following components:

Assembly | Description  
---|---  
**RhinoCommon.dll** | [RhinoCommon](https://developer.rhino3d.com/api/rhinocommon/html/R_Project_RhinoCommon.htm?version=8.x) is the core .NET assembly that plugins reference in order to interact with Rhino.  
**Eto.dll** | [Eto](https://github.com/picoe/Eto) is a framework can be used to build user interfaces that run across multiple platforms using their native toolkit, with an easy to use API. This will make your plug-in look and work as a native application on all platforms, using a single UI codebase.  
**Rhino.UI.dll** | [Rhino.UI](https://developer.rhino3d.com/api/rhinocommon/rhino.ui) is a utility .NET assembly that contains Rhino-specific user interface and other miscellaneous classes.  
  
## Types of Plugins

RhinoCommon supports five different types of plugins:

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

As with all of our development tools, RhinoCommon is free, royalty free, and
includes free developer support.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/what-
is-rhinocommon/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/what-
is-rhinocommon/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

