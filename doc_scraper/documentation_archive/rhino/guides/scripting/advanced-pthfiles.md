---
url: https://developer.rhino3d.com/guides/scripting/advanced-pthfiles/#path-file-naming
scraped_at: 2025-09-08T16:05:35.943273
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

[Python Path Files](https://developer.rhino3d.com/guides/scripting/advanced-
pthfiles/)

  * Path Files
  * Path File Naming

[Guides](https://developer.rhino3d.com/en/guides/) / [Scripting
Guides](https://developer.rhino3d.com/en/guides/scripting/) /

Python Path Files

[New in 8](https://developer.rhino3d.com/8/new)

by [Ehsan Iran-Nejad](https://discourse.mcneel.com/u/eirannejad/) (Last
updated: Thursday, August 15, 2024)

## Path Files

Path files are simple ascii files with one search path per line. These files
are similar to [Python 3 path configuration
files](https://docs.python.org/3/library/site.html) except that they can only
contain search paths and no code inside these files will be parsed or
executed. First path in the file would be the first path to be search for a
module, so the order is important.

Script editor stores search paths configured in the options window, in these
files:

  * `.rhinocode/python-2.pth`
  * `.rhinocode/python-3.pth`

You can edit these files manually and Rhino will use the paths on next launch.

By default, Rhino adds all the paths specified in python path files (*.pth)
under these locations to Python 2 and 3 search paths (`sys.path`):

On Windows:

  * `%PROGRAMDATA%\McNeel\Rhinoceros\<version>.0\scripts` (if exists)
  * `%APPDATA%\McNeel\Rhinoceros\<version>.0\scripts`
  * `.rhinocode`

On macOS:

  * `/Users/Shared/McNeel/Rhinoceros/<version>.0/scripts` (if exists)
  * `~/Library/Application Support/McNeel/Rhinoceros/<version>.0/scripts`
  * `.rhinocode`

## Path File Naming

As you might have noticed, the name of the `.pth` file specifies language
specification and follows the format below with minor and patch numbers being
optional:

`<language>-<major>.<minor>.<patch>`

So `python-3.pth` specifies Python of version 3. The names can be more
specific as in `python-3.9.10.pth`. You can also include other text after the
language specification as in `python-3_dev.pth`. Any text after the language
specification is only for creating unique path file names and will be ignored.

For example, to make sure custom python modules are importable, a Rhino plugin
developer can:

  * place their python modules under shared `scripts/`

OR

  * place a `python-3_pluginname.pth` file under shared `scripts/` and list more that one search path pointing to where the python modules are located

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/scripting/advanced-
pthfiles/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/scripting/advanced-
pthfiles/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

