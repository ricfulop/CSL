---
url: https://developer.rhino3d.com/guides/yak/the-package-server/
scraped_at: 2025-09-08T15:58:02.923700
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

[The Package Server](https://developer.rhino3d.com/guides/yak/the-package-
server/)

  * Authentication and authorization
  * Conventions
    * Naming
    * Versioning

[Guides](https://developer.rhino3d.com/en/guides/) / [Package Manager
Guides](https://developer.rhino3d.com/en/guides/yak/) /

The Package Server

by [Will Pearson](https://discourse.mcneel.com/u/will/) (Last updated:
Wednesday, August 26, 2020)

We host a public package server for everyone to use. You don’t need to
configure anything. Both the Yak CLI tool and Rhino already know where to
look.

Packages shared on the public package server are free to download and install.
They may be free to use or require a license – see the [Cloud
Zoo](https://developer.rhino3d.com/guides/rhinocommon/cloudzoo/cloudzoo-
overview/) and
[Zoo](https://developer.rhino3d.com/guides/rhinocommon/rhinocommon-zoo-
plugins/) guides for ways to implement licensing in your plug-in using our
tools.

Below are a few useful facts about our package server.

## Authentication and authorization

Authentication, provided by [Rhino Accounts](https://accounts.rhino3d.com), is
only required for [publishing packages](../pushing-a-package-to-the-server),
not for downloading/installing.

Once a package author has published a package, only they can publish future
versions using the same package name.

__Note __

Functionality to add “collaborators” will be added in the future.

## Conventions

The package server has a few conventions that must be followed.

### Naming

Package names are pretty strict. They only allow letters, numbers, hyphens and
underscores, e.g. `Hello_World` or `hello-world1`.

Package names adopt the case used in the very first version that was uploaded.
Future uploads ignore the case of the package name and all queries are case-
insensitive.

### Versioning

Package version numbers must either follow [Semantic Versioning
2.0.0](http://semver.org/spec/v2.0.0.html) (e.g. `1.1.0-beta`) or
`System.Version` a.k.a. Microsoft’s four-digit standard (e.g. `1.2.3.4`).

It’s recommended to use Semantic Versioning because it allows package authors
to specify prerelease versions. These are handy for limited testing, since by
default the latest _stable_ version is installed.

Four-digit version numbers were added in v0.8 (August 2019) to support
existing plug-ins that use `System.Version`-style version numbers. They do not
support pre-release or build metadata.

#### Partial version numbers and normalisation

When a package is created you may notice that the version number in the
filename is different to the one in `manifest.yml`. This is due to version
number normalisation. This same process happens behind the scenes on the
package server and is done to avoid ambiguity between semantically equivalent
versions.

There are two cases where version numbers can be semantically equivalent.

  * Semantic versions that only differ in build metadata1, i.e. `1.0.0+build.1` and `1.0.0+build.2`
  * A four-digit version and semantic version that are identical except for a “0” fourth digit (no prerelease or build metadata), e.g. `1.2.3` and `1.2.3.0`

Normalisation is different to expansion of partial (e.g. `1.0`) version
numbers. Partial versions numbers are expanded and stored in their full form.
For example, if you upload a package as `1.0`, it will actually be saved as
`1.0.0`. Subsequently, any requests (REST, CLI, etc.) for version `1.0` will
be automatically redirected.

* * *

  1. [_“Build metadata MUST be ignored when determining version precedence. Thus two versions that differ only in the build metadata, have the same precedence.”_](https://semver.org/#spec-item-10) ↩︎

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/yak/the-
package-server/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/yak/the-
package-server/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

