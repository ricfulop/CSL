---
url: https://developer.rhino3d.com/guides/yak/the-anatomy-of-a-package#distributions
scraped_at: 2025-09-08T16:07:18.983415
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

[The Anatomy of a Package](https://developer.rhino3d.com/guides/yak/the-
anatomy-of-a-package/)

  * Package Structure
    * A note on .NET multi-targeting
  * Requirements
  * Distributions
  * Next Steps

[Guides](https://developer.rhino3d.com/en/guides/) / [Package Manager
Guides](https://developer.rhino3d.com/en/guides/yak/) /

The Anatomy of a Package

by [Will Pearson](https://discourse.mcneel.com/u/will/) and [Callum
Sykes](https://discourse.mcneel.com/u/Callumsykes/) (Last updated: Tuesday,
July 29, 2025)

## Package Structure

Packages are simply ZIP archives with a .yak extension. Take this simple
example…

    
    
    howler-0.4.0-any-any.yak
    ├── manifest.yml
    ├── Howler.rhp
    ├── Howler.rui
    ├── HowlerCommon.dll
    ├── HowlerGrasshopper.gha
    └── misc/
        ├── README.md
        └── LICENSE.txt
    

### A note on .NET multi-targeting

From Rhino 8 onwards, Yak also supports multi-targeted applications so that
your Rhino Plugin can be run in either dotnet core or dotnet framework. Note
that the `manifest.yml` must now be outside the framework directory, rather
than inside of it.

    
    
    howler-0.4.0-rh8-any.yak
    ├── manifest.yml
    ├── net48/
    │  ├── Howler.rhp
    │  ├── Howler.rui
    │  ├── HowlerCommon.dll
    │  ├── HowlerGrasshopper.gha
    │  └── misc/
    │     ├── README.md
    │     └── LICENSE.txt
    └── net7.0/
       ├── Howler.rhp
       ├── Howler.rui
       ├── HowlerCommon.dll
       ├── HowlerGrasshopper.gha
       └── misc/
          ├── README.md
          └── LICENSE.txt
    

## Requirements

  1. Packages **must** have a `manifest.yml` file in the top-level directory. Details about the manifest can be found in the [Manifest Reference Guide](../the-package-manifest).
  2. Any plug-ins (`.rhp`, `.gha`, `.ghpy` files) **must** be in the top-level directory, or a [multi-targeting directory](https://developer.rhino3d.com/guides/yak/the-anatomy-of-a-package/#a-note-on-net-multi-targeting), so that Rhino and Grasshopper can find and load them.
  3. Package version numbers **must** either follow [Semantic Versioning 2.0.0](http://semver.org/spec/v2.0.0.html) (e.g. `1.1.0-beta`) or `System.Version` a.k.a. Microsoft’s four-digit standard (e.g. `1.2.3.4`). It’s recommended to use Semantic Versioning because it allows package authors to specify prerelease versions. These are handy for limited testing, since by default the latest _stable_ version is installed.

## Distributions

For a single package version it’s possible to upload multiple “distributions”
to target different Rhino versions and platforms. This information is encoded
in a “distribution tag” that is appended to the filename of the package, e.g.
_example-1.0.0-rh7-win.yak_.

The distribution tag consists of an “app” identifier and version, and a
platform. Currently the only supported apps are `rh` and `any` – Grasshopper
ships with Rhino so it doesn’t need its own identifier. Unless the app is
`any`, an app version must be included in the form `<major>_<minor>`. The
minor version is optional and is useful if a plug-in relies on an SDK change
made in a service release. The platform can be `win`, `mac` or `any` (i.e.
cross-platform).

A few examples…

  * `rh7-win` \- Rhino 7 for Windows >= 7.0
  * `rh6_14-mac` \- Rhino 6 for Mac >= 6.14
  * `rh6_9-any` \- Rhino 6 (both platforms) >= 6.9
  * `any-any` \- anything goes! (existing behaviour)

When installing packages, the package manager checks whether a compatible
distribution exists for the requested version. Only package versions that have
at least one compatible distribution will show up when the `_PackageManager`
command is run in Rhino 7+.

The updated server works seamlessly with existing packages and old versions of
Rhino. Pre-existing versions on the server (without distributions) will be
treated as `any-any` when installing. New package versions that do not include
a distribution tag, e.g. those created by previous versions of the CLI, will
also be treated as `any-any` when publishing.

## Next Steps

Now that you’ve have seen what is in a package, why not create a package:

  * [Create a Grasshopper package](../pushing-a-package-to-the-server) of your plugin.
  * [Create a Rhino package](../pushing-a-package-to-the-server) for everyone.
  * [Create a multi-targeted package](../creating-a-multi-targeted-rhino-plugin-package) for Rhino 8.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/yak/the-
anatomy-of-a-package/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/yak/the-
anatomy-of-a-package/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

