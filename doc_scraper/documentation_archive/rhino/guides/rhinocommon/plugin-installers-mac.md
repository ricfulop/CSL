---
url: https://developer.rhino3d.com/guides/rhinocommon/plugin-installers-mac/#fnref:2
scraped_at: 2025-09-08T16:07:13.611917
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
(Mac)](https://developer.rhino3d.com/guides/rhinocommon/plugin-installers-
mac/)

  * Overview
  * Step-by-Step
  * Behind the Scenes
  * Maintaining Your Own Installer?
    * Version-Specific Installations
  * Related topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

Plugin Installers (Mac)

__

macOS only

by [Dan Rigdon-Bel](https://discourse.mcneel.com/u/dan/) (Last updated:
Monday, October 7, 2024)

__Warning __

⚠️ The .macrhi format is no longer in active development. Please see the
[Package Manager](https://developer.rhino3d.com/guides/yak/creating-a-rhino-
plugin-package/) instead.

It is presumed you have a plugin that successfully builds and runs already. If
you are not there yet, see [Your First Plugin
(Mac)](https://developer.rhino3d.com/guides/rhinocommon/your-first-plugin-
mac/).

## Overview

Rhino for Mac does not (yet) have a Plugin Manager. However, installing
plugins is very easy. You simply rename your plugin’s containing _folder_ with
an special extension (_.rhp_), compress the folder, and change the extension
from _.rhp.zip_ to _.macrhi_. Once this is done, you can double-click the
archive and Rhino will launch and install the plugin. You can also drag the
_.macrhi_ onto the dock icon of a running instance of Rhino and it will
install the plugin as well. You will, in any case, need to Quit an Restart
Rhino for the plugin to activate.

## Step-by-Step

  1. _Locate_ your plugin folder in _Finder_. Let’s imagine our plugin is called _HelloRhinoCommon_ and we have built it for _Release_ … ![Find Plugin In Finder](https://developer.rhino3d.com/images/plugin-installer-mac-01.png)
  2. _Single-click the name_ your plugin’s _Release_ (or _Debug_) folder to _Rename_ it. The new name should be your plugin assembly with a _.rhp_ suffix. For example, if your plugin is called _HelloRhinoCommon_ , rename the folder that contains this file _HelloRhinoCommon.rhp_ …
  3. You will be prompted to confirm this change. Click the “**Add** ” button: ![Click Add](https://developer.rhino3d.com/images/plugin-installer-mac-02.png)
  4. The icon of the folder1 should now look like this… ![New Icon](https://developer.rhino3d.com/images/plugin-installer-mac-03.png)
  5. _Archive_ the plugin _folder_. _Right-click_ (option-click) the plugin _.rhp_ _folder_ you created in the previous step and select “ _Compress_ (your plugin name).” This creates a zip archive of the contents of the folder.
  6. _Single-click the name_ of the new archive you created in step 5. This allows you _to rename_ the archive.
  7. Change the _extension_ from _.rhp.zip_ to _.macrhi_.
  8. You will be prompted to confirm this change. Select the “ _Use .macrhi_ ” button: ![Use rhi Extension](https://developer.rhino3d.com/images/plugin-installer-mac-04.png)
  9. Notice that _the icon changes_ from a zip archive to a Rhino RHI: ![use_macrhi_confirm](https://developer.rhino3d.com/images/plugin-installer-mac-05.png)
  10. If Rhino for Mac is open, _drag the_ _.macrhi_ archive onto Rhino for Mac’s icon in the _dock_ ; OR:
  11. If Rhino for Mac is _not_ currently open, _double-click the .macrhi archive_ to launch and install the plugin… ![plugin_loaded](https://developer.rhino3d.com/images/plugin-installer-mac-06.png)
  12. Click _OK_ then _Quit_ and _Restart_ Rhino. Your plugin should load.

## Behind the Scenes

The _.macrhi_ extension is a file extension associated with the Rhino for Mac
application (both _Rhinoceros.app_ and _RhinoWIP.app_). This extension denotes
a “Rhino for Mac plugin installer.” Rhino for Mac knows that such files are
actually .zip archives that need to be decompressed and copied into the user’s
Library folder at the appropriate location, specifically the
_~/Library/Application Support/McNeel/Rhinoceros/MacPlugIns/_ folder2.

When Rhino for Mac launches, it searches the contents of the

_~/Library/Application Support/McNeel/Rhinoceros/MacPlugIns/_

folder scanning the sub-folders looking for _.rhp_ files. When it finds such
“file” (which are actually packages), Rhino for Mac attempts to load the
assembly with the same name contained within this package. If it cannot load
the plugin, it will show an error at launch time.

For uninstallation/removal instructions, please see [Uninstalling Plugins
(Mac)](https://developer.rhino3d.com/guides/rhinocommon/uninstalling-plugins-
mac/).

#### User Library

By default, the User Library folder is hidden from view.

To make your Library visible in the Finder:

  1. In _Finder_ , navigate to your _Home_ (_~_) folder. You must be in your Home folder for this to work.
  2. Press `Command`+`J` to bring up the _Finder View_ options dialog… ![finder_view_options](https://developer.rhino3d.com/images/finder-view-options.png)
  3. Check the _Show Library Folder_ check box. Now your Library should show up in the view. You may want to drag this folder to your Favorites area of the Finder sidebar for easy access later.

## Maintaining Your Own Installer?

As explained above, when Rhino for Mac launches, it searches the contents of
the:

_~/Library/Application Support/McNeel/Rhinoceros/MacPlugIns/_

folder scanning the sub-folders looking for _.rhp_ files. When it finds such
“file” (which are actually packages), Rhino for Mac attempts to load the
assembly with the same name contained within this package. If you are
maintaining your own installer, simply writing your plugin to this folder
should be sufficient.

### Version-Specific Installations

_If you are maintaing your own installer_ , in Rhino 8 for Mac onward*, it is
possible to register version-specific installations. To do this, your
installer will need to create a _MacPlugIns_ folder _within the version
folder_ that resides in:

_~/Library/Application Support/McNeel/Rhinoceros/_

For example, to register a plugin that only Rhino 8 will load, your installer
should write to:

_~/Library/Application
Support/McNeel/Rhinoceros/8.0/MacPlugIns/YourPluginName_

__Package Manager __

* Rhino 7’s package manager already supports version-specific (and even platform-specific) targets. See the [Anatomy of a Package: Distributions section](https://developer.rhino3d.com/guides/yak/the-anatomy-of-a-package/#distributions) for more information.

## Related topics

  * [Your First Plugin (Mac)](https://developer.rhino3d.com/guides/rhinocommon/your-first-plugin-mac/)-crossplatform)
  * [Uninstalling Plugins (Mac)](https://developer.rhino3d.com/guides/rhinocommon/uninstalling-plugins-mac/)
  * [Plugin Installers (Windows)](https://developer.rhino3d.com/guides/rhinocommon/plugin-installers-windows/)

**Footnotes**

* * *

  1. macOS (and Unix) has a special kind of folder that masquerades as a file. These are called “packages.” (Most apps found in _/Applications/_ are actually packages called “bundles”). You can access the contents in Finder by _right-clicking_ on the package and selecting _Show Package Contents_. ↩︎

  2. Do not confuse this path with _/Library/Application Support/McNeel/Rhinoceros/_ , which is the system-wide Library location. ↩︎

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/plugin-
installers-mac/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/plugin-
installers-mac/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

