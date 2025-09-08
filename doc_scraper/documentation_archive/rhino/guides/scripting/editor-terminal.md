---
url: https://developer.rhino3d.com/guides/scripting/editor-terminal/#line-by-line-printing
scraped_at: 2025-09-08T16:04:30.090333
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

[Terminal Panel](https://developer.rhino3d.com/guides/scripting/editor-
terminal/)

  * Terminal Panel
  * Line By Line Printing

[Guides](https://developer.rhino3d.com/en/guides/) / [Scripting
Guides](https://developer.rhino3d.com/en/guides/scripting/) /

Terminal Panel

[New in 8](https://developer.rhino3d.com/8/new)

by [Ehsan Iran-Nejad](https://discourse.mcneel.com/u/eirannejad/) (Last
updated: Tuesday, October 8, 2024)

## Terminal Panel

Terminal panel shows printed output of last executed script. You can toggle
the terminal using the toggle button at the top-right of editor window.

The two _Copy_ and _Clear_ buttons can be used to copy or clear the terminal
contents.

![](https://developer.rhino3d.com/guides/scripting/editor-
terminal/terminal.png)

## Line By Line Printing

By default, the output of a script is captured during execution and printed on
the terminal all at once when execution is completed. This way the script is
not slowed down by frequent UI updates.

When debugging a script, this behaviour changes and script output is printed
on the terminal as the script is running. This helps seeing the messages being
printed from your script during debug.

Sometimes it is desired to see the script output during normal execution. An
examples is when a script is processing a series of files and needs to print
its progress to the terminal. Waiting for the script to end without seeing any
reports negates the point of reporting progress.

Use the _Line by Line_ toggle on the terminal header to print script output
during normal execution. You may also want to toggle auto-minimization from
_Run > Toggle Minimize Editor On Execute_ menu item to keep editor on screen:

![](https://developer.rhino3d.com/guides/scripting/editor-terminal/terminal-
linebyline.png)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/scripting/editor-
terminal/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/scripting/editor-
terminal/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

