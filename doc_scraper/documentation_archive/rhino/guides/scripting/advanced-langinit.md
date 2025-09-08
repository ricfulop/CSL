---
url: https://developer.rhino3d.com/guides/scripting/advanced-langinit/#resetting-root-directory
scraped_at: 2025-09-08T16:05:33.627242
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

[Scripting Languages
Initialization](https://developer.rhino3d.com/guides/scripting/advanced-
langinit/)

  * Scripting Root Directory
    * Changing Root Directory
    * Resetting Root Directory

[Guides](https://developer.rhino3d.com/en/guides/) / [Scripting
Guides](https://developer.rhino3d.com/en/guides/scripting/) /

Scripting Languages Initialization

[New in 8](https://developer.rhino3d.com/8/new)

by [Ehsan Iran-Nejad](https://discourse.mcneel.com/u/eirannejad/) (Last
updated: Thursday, August 15, 2024)

## Scripting Root Directory

All languages initialize their runtimes under the scripting root directory.
This is usually placed under:

  * `%USERPROFILE%\.rhinocode` on Window
  * `~/.rhinocode` on macOS (and other Unix-like)

For example, in Rhino 8, Python 3 (CPython) and Python 2 (IronPython) deploy
their runtimes and modules under these directories respectively:

  * `~/.rhinocode/py39-rh8/` for Python 3
  * `~/.rhinocode/py27-rh8/` for Python 2

Alongside language runtimes, root directory also holds:

  * `logs/` for application log files
  * `stage/` for temporary scripts
  * `libs/` for cache for script libraries
  * `component.json` for configurations for Script Components
  * `editor.json` for configurations for Script Editor

### Changing Root Directory

It is sometimes necessary to change the location of this directory. As
mentioned above, Python 3 deploys its runtime in the scripting root directory
and needs to run Python executive binary (`python.exe` on Windows) to start
the language server and install packages from PyPI.org

If this is something you need to block for security reasons, you can change
the scripting root directory to a different location with execute priviledges.

To change the scripting root directory:

  * Open Rhino
  * Do not interact with the scripting tools, meaning do not open ScriptEditor, Grasshopper, and do not run RunPythonCommand
  * Go to **Rhino - > Tools -> Options -> Advanced**, and override the default empty value of `RhinoCodePlugin.RootPath` with your desired root directory path. This needs to be an absolute path and must be writable with execute priviledges for user running Rhino
  * Close and Reopen Rhino
  * Open ScriptEditor and let it initialize languages in this new root directory
  * Open Grasshopper and drop a Script component on the canvas so the `component.json` file is also created in root directory

![](https://developer.rhino3d.com/guides/scripting/advanced-langinit/01.png)

### Resetting Root Directory

To change the scripting root directory back to default, clear the override set
on `RhinoCodePlugin.RootPath` in **Advanced** options as shown above.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/scripting/advanced-
langinit/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/scripting/advanced-
langinit/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

