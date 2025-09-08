---
url: https://developer.rhino3d.com/guides/rhinocommon/what-is-a-zoo-plugin/
scraped_at: 2025-09-08T15:36:53.095450
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

[What is a LAN Zoo
Plugin?](https://developer.rhino3d.com/guides/rhinocommon/what-is-a-zoo-
plugin/)

  * Next Steps
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

What is a LAN Zoo Plugin?

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated: Friday,
June 25, 2021)

The LAN Zoo keeps your licenses on your private LAN server and lets you share
them among the Rhino users on your network.

A LAN Zoo plugin is a software module, developed by a 3rd party, that extends
the functionality of the LAN Zoo by allowing it to validate product licenses.

![zoo with plugins](https://developer.rhino3d.com/images/what-is-a-zoo-
plugin-01.png)

When Rhino and Rhino-based products are installed as workgroup nodes, instead
of standalone nodes, licensing works like this:

  * When a workgroup node starts, it requests a license from the LAN Zoo.
  * An unused license is assigned to the node.
  * When a node shuts down, the license is returned to the LAN Zoo’s license pool.

#### What is required to build a plugin?

LAN Zoo plugins are .NET Framework 4.8 assemblies. Thus, to create a plugin
for the LAN Zoo, you will need one of the following development tools:

  1. Microsoft Visual C#
  2. Microsoft Visual Basic .NET

Also, all plugins that use the LAN Zoo license system must be signed with an
Authenticode certificate issued by McNeel Plugin Security. These certificates
are free, but must be requested by each developer. Developers must agree to
the Terms of Use before a certificate is issued. For more information on
plugin signing, see [Digitally Signing Plugins for LAN
Zoo](https://developer.rhino3d.com/guides/rhinocommon/digitally-signing-
plugins-for-zoo/).

## Next Steps

Check out the [Creating LAN Zoo
Plugins](https://developer.rhino3d.com/guides/rhinocommon/creating-zoo-
plugins/) guide for instructions building - your guessed it - a LAN Zoo
Plugin.

## Related Topics

  * [Creating LAN Zoo Plugins](https://developer.rhino3d.com/guides/rhinocommon/creating-zoo-plugins/)
  * [Digitally Signing Plugins for LAN Zoo](https://developer.rhino3d.com/guides/rhinocommon/digitally-signing-plugins-for-zoo/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/what-
is-a-zoo-plugin/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/what-
is-a-zoo-plugin/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

