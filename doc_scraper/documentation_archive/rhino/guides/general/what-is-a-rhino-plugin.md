---
url: https://developer.rhino3d.com/guides/general/what-is-a-rhino-plugin/#related-topics
scraped_at: 2025-09-08T15:57:56.570933
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

[What is a Rhino Plugin?](https://developer.rhino3d.com/guides/general/what-
is-a-rhino-plugin/)

  * Types of Plugins
  * Plugin Compatibility
  * Related topics

[Guides](https://developer.rhino3d.com/en/guides/) / [General
Guides](https://developer.rhino3d.com/en/guides/general/) /

What is a Rhino Plugin?

by [Dan Rigdon-Bel](https://discourse.mcneel.com/u/dan/) (Last updated:
Friday, September 3, 2021)

A Rhino plugin is a software module that extends the functionality of Rhino or
Grasshopper by adding commands, features, or capabilities. A Rhino plugin is a
Dynamic Link Library, or DLL.

On Windows, a Rhino plugin built with the [C/C++
SDK](https://developer.rhino3d.com/guides/cpp/what-is-the-cpp-sdk/) is a
regular DLL using shared MFC DLL.

On Windows and Mac, a Rhino plugin built with the [RhinoCommon
SDK](https://developer.rhino3d.com/guides/rhinocommon/what-is-rhinocommon/) is
a .NET assembly.

Examples of Rhino plugins include [Grasshopper](http://www.grasshopper3d.com),
[Brazil](http://brazil.rhino3d.com/), [Flamingo](http://nxt.flamingo3d.com/),
and [Bongo](http://bongo.rhino3d.com/). See
[food4rhino.com](http://www.food4rhino.com/) for more.

## Types of Plugins

Rhino supports five different types of plugins:

  1. _General Utility_ : A general purpose utility that can contain one or more commands.
  2. _File Import_ : Imports data from other file formats into Rhino; can support more that one format.
  3. _File Export_ : Exports data from Rhino to other file formats; can support more than one format.
  4. _Custom Rendering_ : Applies materials, textures, and lights to a scene to produce rendered images.
  5. _3D Digitizing_ : Interfaces with 3D digitizing devices, such as those made by MicroScribe, Faro, & Romer.

_**Note**_ : File Import, File Export, Custom Rendering and 3D Digitizing
plugins are all specialized enhancements to the General Utility plugin. Thus,
all plugin types can contain one or more commands.

## Plugin Compatibility

For Rhino to successfully load and run your plugin, several conditions must be
met:

  1. The “RhinoSdkVersion” number of your plugin must match the “RhinoSdkVersion” of Rhino.
  2. The “RhinoSdkServiceRelease” number of Rhino must be greater than or equal to the “RhinoSdkServiceRelease” of your plugin.

We occasionally make changes to our SDKs. When we do, we change the
“RhinoSdkServiceRelease” number.

As a plugin developer you are unlikely to encounter a problem with the first
condition. This would occur, for instance, if a user tried to load a plugin
built for Rhino 6 in Rhino 4.

You may however, occassionally encounter problems with the second condition.
If you compiled your plugin using the 6.2
(RhinoSdkVersion.RhinoSdkServiceRelease) SDK and a user running a 6.1 Rhino
tries to run it, they will get an error message and the plugin will refuse to
load. If your customer gets this message, they need to get the latest Rhino
(could be 6.2 or greater in this example) and that should resolve the problem.

## Related topics

  * [Developer Prerequisites](https://developer.rhino3d.com/guides/general/rhino-developer-prerequisites/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/general/what-
is-a-rhino-plugin/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/general/what-
is-a-rhino-plugin/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

