---
url: https://developer.rhino3d.com/guides/cpp/running-rhino-from-command-line/
scraped_at: 2025-09-08T15:40:10.718991
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

[Running Rhino from the Command
Line](https://developer.rhino3d.com/guides/cpp/running-rhino-from-command-
line/)

  * Overview
  * Rhino for Windows
    * Command line options

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Running Rhino from the Command Line

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

Under some circumstances, it is useful to run Rhino from the command prompt.
Perhaps you are batch processing many files, or maybe you need to run Rhino
from a render farm management system. Rhino provides command line options
(arguments) to allow you to do exactly this.

## Rhino for Windows

The format is:

    
    
    Rhino.exe /runscript="-command -secondCommand"
    

For example, if you want to start Rhino with a file called `hdri_test.3dm`,
render it with the built-in renderer, save the file, and exit Rhino, you would
pass this:

    
    
    "C:\Program Files\Rhinoceros 5 (64-bit)\System\Rhino.exe" /runscript="_SetCurrentRenderPlugIn Rhinoceros _Render _-SaveRenderWindowAs test.jpg _-CloseRenderWindow _-Exit" test.3dm
    

### Command line options

The following command line options are available in Rhino for Windows:

  * `/safemode`: Start in safe mode.
  * `/nosplash`: Suppress startup splash screen.
  * `/bigdump`: When Rhino crashes, include the full memory content and, also, call stack information. This can generate huge crash dumps – as big as the amount of RAM Rhino is using when it crashes.
  * `/notemplate`: Start Rhino with a default model based on hard-coded defaults.
  * `/language`: Set the startup language. For example, to start in Spanish, pass `/language=1034`.
  * `/scheme`: Use a custom scheme. This is used by third party developers that include custom schemes.
  * `/runscript`: Run a script at startup.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/running-
rhino-from-command-line/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/running-
rhino-from-command-line/index.md) [
Admin](https://developer.rhino3d.com/admin)

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

