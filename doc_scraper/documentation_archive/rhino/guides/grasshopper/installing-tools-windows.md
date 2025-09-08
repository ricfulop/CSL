---
url: https://developer.rhino3d.com/guides/grasshopper/installing-tools-windows/
scraped_at: 2025-09-08T15:41:20.034348
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

[Installing Tools
(Windows)](https://developer.rhino3d.com/guides/grasshopper/installing-tools-
windows/)

  * Prerequisites
  * Install Visual Studio
  * Grasshopper Templates
  * Next Steps

[Guides](https://developer.rhino3d.com/en/guides/) / [Grasshopper
Guides](https://developer.rhino3d.com/en/guides/grasshopper/) /

Installing Tools (Windows)

__

Windows only

by [Dan Rigdon-Bel](https://discourse.mcneel.com/u/dan/) (Last updated:
Monday, October 7, 2024)

By the end of this guide, you should have all the tools installed necessary
for authoring, building, and debugging custom Grasshopper components in Rhino
for Windows.

## Prerequisites

This guide presumes you have an:

  * A PC running Microsoft Windows 10 or later.
  * [Rhino 7 for Windows](https://www.rhino3d.com/download)

## Install Visual Studio

[Visual Studio](https://www.visualstudio.com/en-us/visual-studio-homepage-
vs.aspx) is Microsoft’s flagship development platform and Integrated
Development Environment (IDE). Visual Studio now comes in three major
“streams”: Visual Studio Code1, Visual Studio Online2, and Visual Studio
“proper”3. In order to author custom Grasshopper components, you will need
Visual Studio “proper” (Visual Studio Code and Visual Studio Online are not
supported).

__Visual Studio Editions __

For the purposes of this guide, we will presume you are using Visual Studio
2022 Community Edition.

#### Step-by-Step

  1. **[Visual Studio Community Edition](https://visualstudio.microsoft.com/vs/)** is free from Microsoft for students, open-source contributors, and small teams. [Details here](https://www.visualstudio.com/en-us/support/legal/mt171547). Click the **Community** button to download the installer.
  2. Run the **Visual Studio installer** you downloaded from Microsoft, in this case _VisualStudioSetup.exe_.
  3. Follow the onscreen prompts to install Visual Studio. You will need the “.NET desktop development” workload for RhinoCommon based plug-in development. When successfully installed, click the _Launch_ button.

## Grasshopper Templates

The [RhinoCommon and Grasshopper templates for Rhino
7](https://marketplace.visualstudio.com/items?itemName=McNeel.Rhino7Templates2022)
contains wizards to get you started creating components quickly.

#### Step-by-Step

  1. Launch **Visual Studio**.
  2. Navigate to **Extensions** > **Manage Extensions**
  3. In the left-hand sidebar, expand the **Online** section, then select the **Visual Studio Marketplace** entry… ![Extensions and Updates](https://developer.rhino3d.com/images/installing-tools-windows-grasshopper-01.png)
  4. In the **Search** field, search for _RhinoCommon_. This filters the gallery list below.
  5. Find **RhinoCommon and Grasshopper templates for Rhino 7** and select it.
  6. Click the **Download** button. The extension installation should begin.
  7. You must **Accept** the license agreement by clicking on the **Install** button.
  8. Press the **Close** button and **Quit** Visual Studio.
  9. The extension installer should start once you quit. Click the **Modify** button to install the extension.
  10. Once this is done, the extension should appear in your list of **Installed** extensions in **Extensions** > **Manage Extensions**.

## Next Steps

**Congratulations!** You have the tools to build custom Grasshopper components
for Grasshopper for Windows. **Now what?**

Check out the [Your First Component
(Windows)](https://developer.rhino3d.com/guides/grasshopper/your-first-
component-windows/) guide for instructions building - your guessed it - your
first component.

**Footnotes**

* * *

  1. Visual Studio Code is Microsoft’s cross-platform source code editor for Windows, Linux, and macOS. At the time of this writing, Visual Studio code does not yet support the features required to author Grasshopper components ↩︎

  2. Visual Studio Online is Microsoft’s online counterpart to the desktop edition of Visual Studio (referred to as Visual Studio “proper” above). We have not tested using Visual Studio Online to debug Grasshopper components as having a copy of Rhino and Grasshopper running would prove logistically difficult. ↩︎

  3. Visual Studio “proper” is the desktop version of Visual Studio…we are only attaching the “proper” epithet to distinguish it from the Visual Studio Code and Visual Studio Online. In subsequent guides this will be referred to as simply “Visual Studio.” ↩︎

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/grasshopper/installing-
tools-windows/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/grasshopper/installing-
tools-windows/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

