---
url: https://developer.rhino3d.com/guides/rhinocommon/creating-zoo-plugins/
scraped_at: 2025-09-08T15:36:53.770019
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

[Creating LAN Zoo
Plugins](https://developer.rhino3d.com/guides/rhinocommon/creating-zoo-
plugins/)

  * Overview
  * Prerequisites
  * Writing a LAN Zoo Plugin
  * Installing a LAN Zoo Plugin
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

Creating LAN Zoo Plugins

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated: Friday,
June 25, 2021)

## Overview

The LAN Zoo allows third party plugin developers add licensing support for
their products.

When a customer attempts to add a product license to the LAN Zoo, the
product’s plugin is called to validate the user’s request. Upon validation,
the plugin will return the product’s licensing information back to the Zoo. In
turn, the LAN Zoo will serialize, maintain, and distribute this license.

## Prerequisites

LAN Zoo plugins are .NET Framework 4.8 assemblies. To create a plugins for the
LAN Zoo, you need one of the following development tools:

  1. Microsoft Visual C#.
  2. Microsoft Visual Basic .NET.

Also, all plugins that use the LAN Zoo license system must be signed with an
_Authenticode_ certificate issued by _McNeel Plugin Security_. These
certificates are free, but must be requested by each developer. Developers
must agree to the _Terms of Use_ before a certificate is issued. For more
information on plugin signing, see [Digitally Signing Plugins for LAN
Zoo](https://developer.rhino3d.com/guides/rhinocommon/digitally-signing-
plugins-for-zoo/).

## Writing a LAN Zoo Plugin

The general steps required to create a Zoo plugin are:

  1. Make sure you have the LAN Zoo installed.
  2. Launch Microsoft Visual Studio.
  3. Create a new _Class Library_ project using either Visual C# or Visual Basic .NET.
  4. Add a reference to _ZooPlugin.dll_ , which is found in the LAN Zoo installation folder. Make sure to set the reference’s _Copy Local_ property to `False`.
  5. Create a new public class that inherits from the `IZooPlugin3` interface.
  6. Implement the interface members. (For detailed information about the interface members, see the sample LAN Zoo plugin listed below.)
  7. Build your plugin.
  8. [Digitally sign your plugin](https://developer.rhino3d.com/guides/rhinocommon/digitally-signing-plugins-for-zoo/).

## Installing a LAN Zoo Plugin

Once you have built your LAN Zoo plugin, you can install it and test it:

  1. Run _ZooAdmin.Wpf.exe_ and make sure the LAN Zoo licensing service has stopped.
  2. Copy your plugin assembly (_.dll_) and any dependent support libraries to the lan Zoo’s plugin folder (i.e. _C:\Program Files\Zoo 7\Plugins_).
  3. Restart the Zoo license service.
  4. When the service has restarted, click the _Add License_ button. Your product should be one of the available products for which to add a license.

## Related Topics

  * [Digitally Signing Plugins for LAN Zoo](https://developer.rhino3d.com/guides/rhinocommon/digitally-signing-plugins-for-zoo/)
  * [Creating Plugins that use the LAN Zoo (RhinoCommon)](https://developer.rhino3d.com/guides/rhinocommon/rhinocommon-zoo-plugins/)
  * [Creating Plugins that use the LAN Zoo (C/C++)](https://developer.rhino3d.com/guides/cpp/creating-zoo-plugins/)
  * [Sample LAN Zoo Plugin Projects (on GitHub)](https://github.com/mcneel/rhino-developer-samples/tree/6/zoo)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/creating-
zoo-plugins/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/creating-
zoo-plugins/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

