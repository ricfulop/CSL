---
url: https://developer.rhino3d.com/guides/rhinocommon/uninstalling-plugins-mac/#fnref:1
scraped_at: 2025-09-08T16:07:57.279107
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

[Uninstalling Plugins
(Mac)](https://developer.rhino3d.com/guides/rhinocommon/uninstalling-plugins-
mac/)

  * Overview
  * Step-by-Step
  * Behind the Scenes
  * Related topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

Uninstalling Plugins (Mac)

__

macOS only

by [Dan Rigdon-Bel](https://discourse.mcneel.com/u/dan/) (Last updated:
Friday, September 3, 2021)

This guide presumes you have plugins installed that you would like to remove.

## Overview

Rhino for Mac does not (yet) have a Plugin Manager. However, uninstalling
plugins is very easy. You simply remove the plugin folder from the
_~/Library/Application Support/McNeel/Rhinoceros/MacPlugIns/_ folder1 and then
restart Rhino.

## Step-by-Step

  1. _Quit Rhino_ , if it is current running.
  2. In _Finder_ , navigate to the _~/Library/Application Support/McNeel/Rhinoceros/MacPlugIns/_ folder. If you [can’t find this folder](https://developer.rhino3d.com/guides/rhinocommon/uninstalling-plugins-mac/#user-library), you can do the following… 
     1. In the _Finder_ toolbar, in the _Go_ menu, select _Go to Folder…_ ![finder_go](https://developer.rhino3d.com/images/uninstalling-plugins-mac-01.png)
     2. In the _Go to Folder_ dialog, paste the following path: _~/Library/Application Support/McNeel/Rhinoceros/MacPlugIns/_ ![paste_path](https://developer.rhino3d.com/images/uninstalling-plugins-mac-02.png)
     3. Click _Go_. A Finder window should open showing the contents of the folder.
  3. _Remove_ (move or delete) the plugin’s folder from the _MacPlugIns_ folder… ![drag_to_trash](https://developer.rhino3d.com/images/uninstalling-plugins-mac-03.png)
  4. _Restart_ Rhino.

## Behind the Scenes

When Rhino for Mac launches, it searches the contents of the:

_~/Library/Application Support/McNeel/Rhinoceros/MacPlugIns/_

folder scanning the sub-folders recursively looking for _.rhp_ files. When it
finds such file, Rhino for Mac attempts to load this plugin. If it cannot find
a plugin, it will not load said plugin…it’s _that_ simple.

#### User Library

By default, the User Library folder is hidden from view.

To make your Library visible in the Finder:

  1. In _Finder_ , navigate to your _Home_ (_~_) folder. You must be in your Home folder for this to work.
  2. Press `Command`+`J` to bring up the _Finder View_ options dialog… ![finder_view_options](https://developer.rhino3d.com/images/finder-view-options.png)
  3. Check the _Show Library Folder_ check box. Now your Library should show up in the view. You may want to drag this folder to your Favorites area of the Finder sidebar for easy access later.

## Related topics

  * [Creating a Plugin Installer (Mac)](https://developer.rhino3d.com/guides/rhinocommon/plugin-installers-mac/)

**Footnotes**

* * *

  1. Do not confuse this path with _/Library/Application Support/McNeel/Rhinoceros/_ , which is the system-wide Library location. ↩︎

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/uninstalling-
plugins-mac/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/uninstalling-
plugins-mac/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

