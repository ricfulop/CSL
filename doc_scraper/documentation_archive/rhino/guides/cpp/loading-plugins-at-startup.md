---
url: https://developer.rhino3d.com/guides/cpp/loading-plugins-at-startup/
scraped_at: 2025-09-08T15:39:57.662012
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

[Loading Plugins at Startup](https://developer.rhino3d.com/guides/cpp/loading-
plugins-at-startup/)

  * Problem
  * Solution
  * Sample
  * Details

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Loading Plugins at Startup

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You would like your plugin to load at Rhino’s startup.

## Solution

Rhino will load plugins in two ways:

  1. When Needed (Default). Plugin will not be loaded when Rhino starts. Plugin will be loaded when a plugin defined command is run, when a user selects a plugin defined file import/export type, or if a 3DM file has user data that was created by your plugin.
  2. At Startup. Plugin is loaded when Rhino is loaded and initialized.

To set your plugin to load on startup, you need to override your plugin
object’s `CRhinoPlugIn::PlugInLoadTime()` virtual function and return the
`CRhinoPlugIn::load_plugin_at_startup` enumerated value. See
_rhinoSdkPlugIn.h_ for details.

## Sample

    
    
    // Description:
    //    Called by Rhino when writing plug-in information to the registry.  This
    //    information will be read the next time Rhino starts to identify properly
    //    installed plug-ins.
    CRhinoPlugIn::plugin_load_time CTestPlugIn::PlugInLoadTime()
    {
      return CRhinoPlugIn::load_plugin_at_startup;
    }
    

## Details

If you have already loaded your plugin using Rhino’s plugin manager, when
debugging for example, then you will need to either remove your plugin’s
registry key, which can be found here:

    
    
    HKEY_LOCAL_MACHINE\SOFTWARE\McNeel\Rhinoceros\<version>\<rhino_build_date>\Plug-Ins\<your_plugin_guid>
    

#### WARNING

if you are running on a system with limited rights, with user-account control
enabled for example, then there will be a corresponding key in
HKEY_CURRENT_USER

Or, you can just modify your plugin’s “LoadMode” registry key value. The
available values for this key are as follows:

Load mode |  |  | Registry Value |  |  | Description  
---|---|---|---|---|---|---  
load_plugin_when_needed |  |  | 2 - REG_DWORD, Decimal |  |  | Default. Load the first time a plugin command used  
load_plugin_at_startup |  |  | 1 - REG_DWORD, Decimal |  |  | Load when Rhino is loaded  
  
The reason this step is required is that the “LoadMode” Registry key value is
only written the first time the plugin is loaded (when it is initially
installed or registered). This will not be an issue for customers of your
plugin for the correct registry key value will be written the first time they
load your plugin.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/loading-
plugins-at-startup/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/loading-
plugins-at-startup/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

