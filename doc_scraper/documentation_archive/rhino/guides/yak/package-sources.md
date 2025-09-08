---
url: https://developer.rhino3d.com/guides/yak/package-sources/
scraped_at: 2025-09-08T15:58:04.944568
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

[Custom Package
Repositories](https://developer.rhino3d.com/guides/yak/package-sources/)

  * Tips for shared folders
  * Administrator-Enforced Settings
  * Performance

[Guides](https://developer.rhino3d.com/en/guides/) / [Package Manager
Guides](https://developer.rhino3d.com/en/guides/yak/) /

Custom Package Repositories

by [Will Pearson](https://discourse.mcneel.com/u/will/) (Last updated: Friday,
February 12, 2021)

By default Rhino uses the official McNeel package server -
<https://yak.rhino3d.com>. In addition (or instead!), it’s possible to
configure Rhino to use your own package repositories.

A custom package repository is simply a folder that contains .yak package
files. The folder can be on the local machine or on a shared file server. You
can configure Rhino to include packages from this repository in the Package
Manager by following the steps below.

  1. Go to _Options > Advanced_ and look for the `Rhino.Options.PackageManager.Sources` setting.
  2. Add the full path to your package repository folder, separating it from the default package server with a semi-colon, e.g. `https://yak.rhino3d.com;C:\rhino_packages`.
  3. Run the `_PackageManager` command and search for one of the packages that you added to the new package repository.

for now it just supports whatever Directory.EnumerateFiles() supports, which
as far as I can tell is regular paths, mapped drives (Windows), UNC paths
(Windows) and mounted shares (macOS)

### Tips for shared folders

On Windows use the UNC path, i.e. `\\server\share\packages`. If the share
requires credentials then first navigate to `\\server` in Explorer, log in and
check the “remember my credentials” box.

On macOS the file share needs to be mounted first in Finder via _Go > Connect
to Server…_ (`⌘` \+ `K`). Enter the address (`smb://server/share`) and provide
credentials if required. Now the mounted path can be used as a package source,
i.e. `/Volumes/share/packages`. The mount isn’t persistent, so it’ll need to
be remounted in future.

### Administrator-Enforced Settings

See [Administrator-Enforced Settings](https://docs.mcneel.com/rhino/8/help/en-
us/index.htm#information/admin-enforced_settings.htm) for tips on how to
deploy and enforce this setting for Windows users in your organisation.

### Performance

Rhino 8.15 included some performance improvements for private package
repositories.

The yak.exe tool has a new “cache” command that, when run inside the private
package folder, will generate an index of the available packages. When the
package manager sees this index file, it will use it _instead of_ traversing
the directory. This greatly reduces the time it takes for the Package Manager
to load when dealing with private repositories with many packages, large
packages, or slow network connections.

    
    
    $ cd X:\private\repo\directory
    $ "C:\Program Files\Rhino 8\System\yak.exe" cache
    
    Building cache for local package repository in X:\private\repo\directory
    
    [...]
    

Make sure to re-build the cache if package files are added or removed from the
directory. Remove the _.cache*_ files from the directory to revert to the old
behaviour.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/yak/package-
sources/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/yak/package-
sources/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

