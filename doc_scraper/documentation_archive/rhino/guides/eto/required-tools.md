---
url: https://developer.rhino3d.com/guides/eto/required-tools/
scraped_at: 2025-09-08T15:43:29.451102
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

Required Tools

Getting set up with Eto tools

# Inside Rhino

## Scripting in the Script Editor (Rhino or GH)

Recommended

The [Script Editor](https://developer.rhino3d.com/guides/scripting/) offers
very quick ways to write, review, build and publish plugins with Eto UIs from
Rhino or Grasshopper (As of Rhino 8). It is recommended to use this when
learning.

## Working from a C# Rhino Plugin

If you are not familiar with Rhino, or setting up Rhino plugins, it is advised
to read this guide on creating your first plugin before diving into Eto.

  * [Your First Plugin Windows](https://developer.rhino3d.com/guides/rhinocommon/your-first-plugin-windows/)
  * [Your First Plugin Mac](https://developer.rhino3d.com/guides/rhinocommon/your-first-plugin-mac/)

One you have a working plugin, it would be best to create a new command you
can use for debugging.

# Outside of Rhino

If you wish to work on eto outside of Rhino, you’ll need to install some
tools.

Open up your command line and run the following line.

    
    
    dotnet new install Eto.Forms.Templates
    

# Workflow Recommendations

## Feedback loop

The shorter the loop between `Code Written` → `File Saved` → `UI Updated`, the
quicker and easier it will be for you to try, experiment and learn.

## Hot Reload in C#

Hot reload reduces the feedback loop length by avoiding re-compiling and re-
running commands. You can change your UI instantly avoiding repetitive and
tiring re-compile cycles.

Within Rhino, Hot Reload is only available on Windows, and works best with
Visual Studio.

Outside of Rhino, Hot Reload works on both platforms as of net8.0 onwards, for
Mac this means Visual Studio Code or other IDEs such as Rider.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/eto/required-
tools/_index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/eto/required-
tools/_index.md) [ Admin](https://developer.rhino3d.com/admin)

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

