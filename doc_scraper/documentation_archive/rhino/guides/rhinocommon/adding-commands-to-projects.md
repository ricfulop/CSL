---
url: https://developer.rhino3d.com/guides/rhinocommon/adding-commands-to-projects/#related-topics
scraped_at: 2025-09-08T16:07:39.512560
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

[Adding Commands to
Projects](https://developer.rhino3d.com/guides/rhinocommon/adding-commands-to-
projects/)

  * Problem
  * Solution
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

Adding Commands to Projects

by [Dan Rigdon-Bel](https://discourse.mcneel.com/u/dan/) (Last updated:
Friday, September 3, 2021)

## Problem

The RhinoCommon Project Wizard
([Windows](https://developer.rhino3d.com/guides/rhinocommon/installing-tools-
windows/#rhinocommon-templates) or
[Mac](https://developer.rhino3d.com/guides/rhinocommon/installing-tools-
mac/#install-the-rhino-add-in)) creates a skeleton plugin project with a
single command. However, plugins can contain more than one command. How does
one add additional commands to plugin projects?

## Solution

To add a new command to your RhinoCommon plugin project, you simply need to
define a new class that inherits from `Rhino.Commands.Command`.

An easy way to do this is to just use the _Empty RhinoCommmon Command_
template. Here is how you do that:

  1. Make sure you have the RhinoCommon Project Wizard ([Windows](https://developer.rhino3d.com/guides/rhinocommon/installing-tools-windows/#rhinocommon-templates) or [Mac](https://developer.rhino3d.com/guides/rhinocommon/installing-tools-mac/#install-the-rhino-add-in)) installed.
  2. Launch _Visual Studio_ and open your plugin project.
  3. From _Visual Studio_ , navigate to _Project_ > _Add New Item_ menu item. From _Visual Studio for Mac_ , right-click on the project name in the _Solution Explorer_ and navigate to _Add_ > _New File…_.
  4. Select the _Empty RhinoCommmon Command_ template from the list of installed templates.
  5. Provide a unique file name that relates to the command you are adding.
  6. In _Visual Studio for Windows_ , click the _Add_ button. In _Visual Studio for Mac_ , click the _New_ button.

## Related Topics

  * [Installing Tools (Windows)](https://developer.rhino3d.com/guides/rhinocommon/installing-tools-windows/)
  * [Installing Tools (Mac)](https://developer.rhino3d.com/guides/rhinocommon/installing-tools-mac/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/adding-
commands-to-projects/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/adding-
commands-to-projects/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

