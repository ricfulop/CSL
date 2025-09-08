---
url: https://developer.rhino3d.com/guides/scripting/editor-configs/#editor-paths
scraped_at: 2025-09-08T16:04:33.458701
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

[Script Editor Options](https://developer.rhino3d.com/guides/scripting/editor-
configs/)

  * General Options
  * Editing Options
  * Language Support Options
  * Python Paths
    * Scripts Path
    * Editor Paths

[Guides](https://developer.rhino3d.com/en/guides/) / [Scripting
Guides](https://developer.rhino3d.com/en/guides/scripting/) /

Script Editor Options

[New in 8](https://developer.rhino3d.com/8/new)

by [Ehsan Iran-Nejad](https://discourse.mcneel.com/u/eirannejad/) (Last
updated: Thursday, August 15, 2024)

**Editor Options** dialog (_Tools > Options_ menu) provides access to editor
and language settings that are persistent.

Hovering over help icons provides more information about each option:

![](https://developer.rhino3d.com/guides/scripting/editor-configs/editor-
options-tipdot.png)

## General Options

General options are under **General** tab of _Editor Options_ dialog and are
self explanatory:

![](https://developer.rhino3d.com/guides/scripting/editor-configs/editor-
options-general.png)

Grasshopper Script Editor has a few layout options under _General_ tab.
_Window_ menu also shows toggles for these options:

![](https://developer.rhino3d.com/guides/scripting/editor-configs/editor-
options-general-embedded.png)

_Window > Toggle *_ menu items provide toggles for Editor UI elements. Editor
remembers the last UI layout before it is closed. See [Layout Options:
Python](https://developer.rhino3d.com/guides/scripting/scripting-gh-
python/#layout-options) or
[C#](https://developer.rhino3d.com/guides/scripting/scripting-gh-
csharp/#layout-options) for more information on these options.

## Editing Options

Editing options are language-specific. Each language tab has its own editing
options:

![](https://developer.rhino3d.com/guides/scripting/editor-configs/editor-
options-editing.png)

_Edit > Toggle *_ menu items provide toggles for some of the options. These
changes are in-session only and do not get saved to settings file. See
[Editing Features](https://developer.rhino3d.com/guides/scripting/editor-
editing/) for more information on these options.

## Language Support Options

Language Support options are language-specific. Each language tab has its own
language options:

![](https://developer.rhino3d.com/guides/scripting/editor-configs/editor-
options-langserver.png)

_Edit > Toggle *_ menu items provide toggles for some of the options. These
changes are in-session only and do not get saved to settings file. See
[Editing Features](https://developer.rhino3d.com/guides/scripting/editor-
editing/) for more information on these options.

## Python Paths

### Scripts Path

By default, Rhino adds these paths to Python 2 and 3 search paths
(`sys.path`):

On Windows:

  * **Shared** `%PROGRAMDATA%\McNeel\Rhinoceros\<version>.0\scripts` (if exists)
  * **User** `%APPDATA%\McNeel\Rhinoceros\<version>.0\scripts`

On macOS:

  * **Shared** `/Users/Shared/McNeel/Rhinoceros/<version>.0/scripts` (if exists)
  * **User** `~/Library/Application Support/McNeel/Rhinoceros/<version>.0/scripts`

Note that the first path on either platform, is the shared path and takes
precedence over the user path. So if python module `test` is available in both
paths, the one under shared path will be imported. Shared `scripts` path are
not created by default so there is not a conflict unless you, your system
admin, or other third-party plugin intentionally places python modules or
scripts in this path.

### Editor Paths

You can add a list of other search paths for each Python version in Editor
options:

![](https://developer.rhino3d.com/guides/scripting/editor-configs/editor-
options-python-paths.png)

Note that the order of these paths is important. First path on the list would
be the first path to be search for a module.

Editor stores these paths in two `.rhinocode/python-3.pth` and
`.rhinocode/python-2.pth` files. See [Path
Files](https://developer.rhino3d.com/guides/scripting/advanced-pthfiles/) for
more information.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/scripting/editor-
configs/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/scripting/editor-
configs/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

