---
url: https://developer.rhino3d.com/guides/yak/package-restore-in-grasshopper
scraped_at: 2025-09-08T16:07:21.029626
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

[Package Restore in
Grasshopper](https://developer.rhino3d.com/guides/yak/package-restore-in-
grasshopper/)

  * Overview
  * Matching
    * Naming
    * Version numbers

[Guides](https://developer.rhino3d.com/en/guides/) / [Package Manager
Guides](https://developer.rhino3d.com/en/guides/yak/) /

Package Restore in Grasshopper

by [Will Pearson](https://discourse.mcneel.com/u/will/) (Last updated:
Wednesday, October 21, 2020)

## Overview

For starters, this is less of a developer guide and more of a description of
how this feature works, so that you, the developer, can better understand how
your package and plug-in needs to be set up in order to leverage it.

It can be frustrating to open a Grasshopper definition only to find that the
required plug-ins aren’t installed on the system. The package manager can help
by streamlining the process of satisfying those dependencies.

Since Rhino 6, the “Unrecognized Objects” dialog presents the user with an
option to _download and install_ missing plug-ins. This feature is called
Package Restore.

![Grasshopper package restore](https://developer.rhino3d.com/images/yak-gh-
restore.gif)

Package Restore uses the name, ID and version of the missing plug-ins to
search the package server. If any packages match the search query then they
will be installed and, if possible, loaded prior to opening the definition1.

## Matching

### Naming

Ideally, the name of the Grasshopper plug-in and the package will match. In
case this isn’t possible – due to either the constraints of the package naming
scheme2 or the fact that there are multiple plug-ins in a package each with a
different name – the correct package can also be identified by the plug-in ID.

For each .gha file, the plug-in ID is extracted and added to the
`manifest.yml` when you run `yak build`.

### Version numbers

Package version numbers can either follow the [Semantic Versioning
2.0.0](https://semver.org) (SemVer) spec or they can be four-digits3, as per
`System.Version`. See the [package server](../the-package-server) guide for
more details on the allowed version number formats.

The server allows both SemVer and four-digit because some Grasshopper plug-ins
will specify their version number as a `string` in a class derived from
`GH_AssemblyInfo` whereas others will rely on the `AssemblyVersionAttribute`.

While restoring packages, if a package exists on the server that matches
either the name or ID of the missing plug-in, but the exact version doesn’t
exist, the latest stable version will be installed.

* * *

  1. Added to Grasshopper in December 2019. On-the-fly loading is only possible if another version of the Grasshopper library is not already installed and loaded. Otherwise, Rhino will need to be restarted to load the new version of the library. ↩︎

  2. Package names are pretty strict. They only allow letters, numbers, hyphens and underscores. ↩︎

  3. Support for four-digit (`System.Version`) version numbers was added in Yak 0.8. ↩︎

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/yak/package-
restore-in-grasshopper/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/yak/package-
restore-in-grasshopper/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

