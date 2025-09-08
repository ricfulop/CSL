---
url: https://developer.rhino3d.com/guides/general/rhino-installer-engine
scraped_at: 2025-09-08T16:06:57.289066
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

[Rhino Installer Engine](https://developer.rhino3d.com/guides/general/rhino-
installer-engine/)

  * Overview (Windows)
  * How It Works
    * File and folder structure
    * Installation and compatibility
  * Limitations
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [General
Guides](https://developer.rhino3d.com/en/guides/general/) /

Rhino Installer Engine

__

Windows only

by [Brian Gillespie](https://discourse.mcneel.com/u/brian/) and [Will
Pearson](https://discourse.mcneel.com/u/will/) (Last updated: Tuesday, July
27, 2021)

__Warning __

⚠️ This technology is obsolete as of Rhino 7 and has been replaced by the [yak
format along with the
PackageManager.](https://developer.rhino3d.com/guides/yak/)

## Overview (Windows)

The Rhino Installer Engine simplifies distribution, installation and updating
of plug-ins for Rhino for Windows.

## How It Works

### File and folder structure

A Rhino Installer package is a zip file with an _.rhi_ extension. The package
can include more than one version of a plug-in however all versions must share
the same GUID (i.e. they’re different versions of the _same_ plug-in).

There are no file structure or naming requirements. For example the two
packages below are functionally equivalent. Both contain versions of
“Marmoset” – a fictitious C++ plug-in compiled for Rhino 5 (32-bit and 64-bit)
and Rhino 61.

    
    
    Marmoset_tree.rhi/
    ├── Rhino 6/
    │   ├── Marmoset.rhp
    │   ├── Marmoset.dll
    │   └── Marmoset.rui
    └── Rhino 5.0/
        ├── x86/
        │   ├── Marmoset.rhp
        │   └── ...
        └── x64/
            ├── Marmoset.rhp
            └── ...
    
    
    
    Marmoset_flat.rhi/
    ├── Marmoset_rhino6.rhp
    ├── Marmoset_rhino5_x86.rhp
    ├── Marmoset_rhino5_x64.rhp
    ├── Marmoset_rhino6.dll
    ├── ...
    └── Marmoset.rui
    

You can include anything you want in the _.rhi_ package – supporting DLLs,
help files, documentation, [toolbar (_.rui_)
files](https://developer.rhino3d.com/guides/rhinocommon/create-deploy-plugin-
toolbar/), etc. The entire contents are unzipped to a directory on the user’s
machine.

### Installation and compatibility

The Rhino Installer Engine examines each _.rhp_ file and extracts the plugin
GUID, Title, Version, the SDK used (e.g. RhinoCommon, C++) and the SDK
version. This information is used to determine which version of the plug-in
will be installed for which installed version of Rhino for Windows; the newest
compatible plugin is registered with the corresponding version of Rhino.
RhinoCommon plug-ins compiled as `AnyCPU` will be installed for both 32- and
64-bit Rhino 51.

__Note __

**Since Rhino 6:** Where a RhinoCommon plug-in is found that has been compiled
against an earlier _major_ version of Rhino than is installed, an in-depth
compatibility check will be performed to determine whether the SDK of the
installed Rhino still supports the functionality used by the plug-in. If the
check is successful then the outdated plug-in will be installed.

## Limitations

  * The Rhino Installer Engine will copy files from the _.rhi_ archive, and will register the plug-ins it finds. No other execution is done.
  * Currently, it is not possible to digitally sign _.rhi_ files in order to verify the source of _.rhi_ files.
  * The Rhino Installer Engine is available with Rhino 5 and later.

## Related Topics

  * [Plugin Installers (Windows)](https://developer.rhino3d.com/guides/rhinocommon/plugin-installers-windows/)
  * [Plugin Installers (Mac)](https://developer.rhino3d.com/guides/rhinocommon/plugin-installers-mac/)

**Footnotes**

* * *

  1. Since version 6 Rhino for Windows has been 64-bit only. ↩︎ ↩︎

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/general/rhino-
installer-engine/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/general/rhino-
installer-engine/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

