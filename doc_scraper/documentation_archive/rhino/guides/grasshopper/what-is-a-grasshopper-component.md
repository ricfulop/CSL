---
url: https://developer.rhino3d.com/guides/grasshopper/what-is-a-grasshopper-component/
scraped_at: 2025-09-08T15:41:18.993790
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

[What is a Grasshopper
Component?](https://developer.rhino3d.com/guides/grasshopper/what-is-a-
grasshopper-component/)

  * Rhino Plugin Architecture
  * .NET Component Library
  * Assembly References
  * Related topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Grasshopper
Guides](https://developer.rhino3d.com/en/guides/grasshopper/) /

What is a Grasshopper Component?

by [David Rutten](https://discourse.mcneel.com/u/davidrutten/) (Last updated:
Wednesday, December 5, 2018)

This guide also explains the hierarchy of all assemblies involved with the
Grasshopper plugin. This is important for component developers so they know
which Assembly References they need to have in order to compile a Grasshopper
Component Library. It also provides some background information which is
useful when communicating with other developers.

## Rhino Plugin Architecture

Grasshopper is a .NET
([RhinoCommon](https://developer.rhino3d.com/guides/rhinocommon/what-is-
rhinocommon/)) plugin for Rhino 6 for Windows and later ([a version for Rhino
5 for Mac is currently in beta](http://www.grasshopper3d.com/page/grasshopper-
for-mac)). It was written using Microsoft Visual Studio Professional using
both VB.NET and C# source compiled against the .NET Framework. It is
recommended, though not required, that you target the same framework when
developing Grasshopper Component Libraries.

Our aim is to keep Grasshopper dependencies as conservative as possible.
However, it is possible that we will switch to a higher version number of
Rhino or .NET if this new version fixes crucial bugs or exposes useful
functions.

## .NET Component Library

The Grasshopper project type is _Class Library_ , meaning it cannot be run as
a stand-alone application. _Grasshopper.dll_ is loaded by a [Rhino
plugin](https://developer.rhino3d.com/guides/general/what-is-a-rhino-plugin/)
called _GrasshopperPlugin.rhp_.

## Assembly References

As a Class Library, Grasshopper references namespaces in addition to
_RhinoCommon.dll_ , some of these are standard namespaces provided by the .NET
Framework, others are 3rd-party assemblies and others still are written by
McNeel developers but are shipped separately for technical reasons. Some of
these assemblies need to be referenced by Component developers, while others
can be safely ignored. The following table lists all assemblies referenced by
_Grasshopper.dll_ :

Assembly | Author | Purpose | Required  
---|---|---|---  
_[RhinoCommon.dll](https://developer.rhino3d.com/guides/rhinocommon/what-is-rhinocommon/)_ | [McNeel](http://www.mcneel.com) | Rhinoceros .NET SDK | Yes  
_GH_IO.dll_ | [McNeel](http://www.mcneel.com) | Grasshopper Input/Output library required to read and write Grasshopper files. | Yes  
_GH_Util.dll_ | [McNeel](http://www.mcneel.com) | Grasshopper utility library containing some peripheral algorithms. | Optional  
_QWhale.*.dll_ | [Quantum Whale](http://www.qwhale.net/) | Syntax highlighter functionality. Contains a total of 5 dlls. | Optional  
_[System](https://msdn.microsoft.com/en-us/library/system\(v=vs.110\).aspx)_ | [Microsoft](https://www.microsoft.com/net) | Base .NET Namespace. | Yes  
_[System.Drawing](https://msdn.microsoft.com/en-us/library/system.drawing\(v=vs.110\).aspx)_ | [Microsoft](https://www.microsoft.com/net) | .NET namespace involved with drawing shapes and text. | Yes  
_[System.Windows.Forms](https://msdn.microsoft.com/en-us/library/system.windows.forms\(v=vs.110\).aspx)_ | [Microsoft](https://www.microsoft.com/net) | .NET namespace involved with dialogs and controls. | Yes  
_[System.Collections.Generic](https://msdn.microsoft.com/en-us/library/system.collections.generic\(v=vs.110\).aspx)_ | [Microsoft](https://www.microsoft.com/net) | .NET namespace containing useful list classes. | Yes  
  
## Related topics

  * [Developer Prerequities](https://developer.rhino3d.com/guides/general/rhino-developer-prerequisites/)
  * [What is a Rhino Plugin?](https://developer.rhino3d.com/guides/general/what-is-a-rhino-plugin/)
  * [What is RhinoCommon?](https://developer.rhino3d.com/guides/rhinocommon/what-is-rhinocommon/)
  * [Your First Component](https://developer.rhino3d.com/guides/grasshopper/your-first-component-windows/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/grasshopper/what-
is-a-grasshopper-component/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/grasshopper/what-
is-a-grasshopper-component/index.md) [
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

