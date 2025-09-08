---
url: https://developer.rhino3d.com/guides/rhinocommon/plugin-installers-windows/#fnref:2
scraped_at: 2025-09-08T16:07:01.257177
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

[Plugin Installers
(Windows)](https://developer.rhino3d.com/guides/rhinocommon/plugin-installers-
windows/)

  * Overview
  * An Example
  * Everything but the kitchen sink
  * Related topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

Plugin Installers (Windows)

__

Windows only

by [Brian Gillespie](https://discourse.mcneel.com/u/brian/) and [Will
Pearson](https://discourse.mcneel.com/u/will/) (Last updated: Tuesday, July
27, 2021)

__Warning __

⚠️ The Rhino Installer Engine is no longer in active development. Please see
the [Package Manager](https://developer.rhino3d.com/guides/yak/creating-a-
rhino-plugin-package/) instead.

__Note __

**Note** : This process is the same for both C/C++ and RhinoCommon plug-ins!

## Overview

Creating a plugin installer is very easy. You simply add your compiled plugin
to a zip archive and change the extension from _.zip_ to _.rhi_. Once this is
done, you can double-click the archive and the [Rhino Installer
Engine](https://developer.rhino3d.com/guides/general/rhino-installer-engine/)
will begin to install your plugin. That’s all there is to it!

__Note __

This is intended to be a quickstart guide. For a more general overview please
see the [Rhino Installer
Engine](https://developer.rhino3d.com/guides/general/rhino-installer-engine)
guide.

## An Example

Imagine you have a plugin and want to support multiple versions of Rhino. For
example, you want to:

  * Install the latest version of the plugin for Rhino WIP
  * Install an older version of the plugin for 64-bit Rhino 5
  * Install yet another version of the plugin for 32-bit Rhino 5
  * Include a custom toolbar file (e.g. _MyToolbar.rui_)

This is possible. You need to:

  1. Create an “installer image” folder. In this example, the folder is the name of the product – _Marmoset_. This folder will contain only the files you want to install on the user’s system.
         
         Marmoset/
          ├── Rhino 6/
          │   ├── Marmoset.rhp
          │   └── required_wip.dll
          ├── Rhino 5.0/
          │   ├── x86/
          │   │   ├── Marmoset.rhp
          │   │   └── required_v5_x86.dll
          │   └── x64/
          │       ├── Marmoset.rhp
          │       └── required_v5_x86.dll
          ├── Marmoset.rui
          ├── Marmoset.chm
          └── README.txt
         

  2. Copy the appropriate files into the folders1. Note that all three versions of the plugin can have the same name, so long as they are in different folders.

  3. Add all the files inside the “installer image” folder to a new ZIP2 archive

  4. Change the extension from _.zip_ to _.rhi_

## Everything but the kitchen sink

Because the Rhino Plugin Installer Engine unzips your _.rhi_ file into a
directory specific to your plugin, you can include anything you want: help
files, documentation, etc. These files will end up inside your plugin
directory; The Rhino Installer Engine cannot be used to install files to other
parts of the hard drive.

## Related topics

  * [Rhino Installer Engine](https://developer.rhino3d.com/guides/general/rhino-installer-engine/)
  * [Plugin Installers (Mac)](https://developer.rhino3d.com/guides/rhinocommon/plugin-installers-mac/)

**Footnotes**

* * *

  1. Folder names are not important; the _.rhp_ files themselves are inspected to determine for which versions of Rhino they will be installed. ↩︎

  2. Other compression algorithms are not supported. ↩︎

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/plugin-
installers-windows/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/plugin-
installers-windows/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

