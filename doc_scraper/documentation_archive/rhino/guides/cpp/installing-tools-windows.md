---
url: https://developer.rhino3d.com/guides/cpp/installing-tools-windows/
scraped_at: 2025-09-08T15:38:29.310461
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
(Windows)](https://developer.rhino3d.com/guides/cpp/installing-tools-windows/)

  * Prerequisites
    * Rhino 8
    * Rhino 7
  * Install Visual Studio
    * Rhino 8
    * Rhino 7
  * Install the Rhino C/C++ SDK
    * Rhino 8
    * Rhino 7
  * Next Steps

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Installing Tools (Windows)

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated: Monday,
October 7, 2024)

By the end of this guide, you should have all the tools installed necessary
for authoring, building, and debugging C/C++ plugins using the Rhino C/C++ SDK
on Windows.

## Prerequisites

This guide presumes you have:

### Rhino 8

  * A PC running Microsoft Windows 10 or later.
  * [Rhino 8 for Windows](https://www.rhino3d.com/download).

### Rhino 7

  * A PC running Microsoft Windows 8.1 or later.
  * [Rhino 7 for Windows](https://www.rhino3d.com/download).

## Install Visual Studio

### Rhino 8

To write C++ plugins for Rhino 8 using the Rhino 8 C/C++ SDK, you will need a
version of Microsoft Visual Studio that includes the Visual Studio 2019 (v142)
platform toolset. Thus, you can use either [Visual Studio
2022](https://visualstudio.microsoft.com/downloads/) or [Visual Studio
2019](https://visualstudio.microsoft.com/vs/older-downloads/).

  1. Download **Microsoft Visual Studio** , either [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/) or [Visual Studio 2019](https://visualstudio.microsoft.com/vs/older-downloads/).

  2. Run the **Visual Studio installer** you just downloaded.

![Visual Studio Install](https://developer.rhino3d.com/images/installing-
tools-windows-cpp-01.png)

  3. Follow the onscreen prompts to install Visual Studio.

  4. Check the **Desktop development with C++** workload.

  5. Click the **Individual components** tab.

  6. Scroll to the **Compilers, build tools, and runtimes** section and check the following option:

     1. MSVC v142 - VS 2019 C++ x64/x86 build tools
  7. Scroll to the **SDKs, libraries, and frameworks** section and check the following options:

     1. C++ v14.2 ATL for v142 build tools (x86 & x64)
     2. C++ v14.2 MFC for v142 build tools (x86 & x64)
     3. Windows 10 SDK
  8. Check any additional features required for your project.

  9. When finished, click **Install**.

  10. Depending on your internet connection, this can take several minutes to complete.

If you already have Microsoft Visual Studio 2022 or 2019 installed, then you
will want to re-run the **Visual Studio Installer** and verify you have all
the the components installed.

### Rhino 7

To write C++ plugins for Rhino 7 using the Rhino 7 C/C++ SDK, you will need
[Microsoft Visual Studio 2019](https://visualstudio.microsoft.com/vs/older-
downloads/).

  1. Download **[Visual Studio 2019](https://visualstudio.microsoft.com/vs/older-downloads/)**.

  2. Run the **Visual Studio installer** you just downloaded.

![Visual Studio Install](https://developer.rhino3d.com/images/installing-
tools-windows-cpp-02.png)

  3. Follow the onscreen prompts to install Visual Studio.

  4. Check the **Desktop development with C++** workload.

  5. Click the **Individual components** tab.

  6. Scroll to the **SDKs, libraries, and frameworks** section and check the following option:

     1. Visual Studio SDK
  7. Check any additional features required for your project.

  8. When finished, click **Install**.

  9. Depending on your internet connection, this can take several minutes to complete.

If you already have Microsoft Visual Studio 2019 installed, then you will want
to re-run the **Visual Studio Installer** and verify you have all the the
components installed.

## Install the Rhino C/C++ SDK

The **Rhino C/C++ SDK** is a set of tools for creating plugin using the C++
language. The SDK includes headers, libraries and Visual Studio project
wizards to get you started creating plugins quickly.

### Rhino 8

  1. Exit **Visual Studio**.
  2. Download the **[Rhino 8 C/C++ SDK](https://www.rhino3d.com/download/rhino-sdk/8/latest/)**.
  3. Run the **SDK installer** you downloaded.
  4. Download the **[Rhino Visual Studio Extension (VSIX)](https://github.com/mcneel/RhinoVisualStudioExtensions/releases)**.
  5. Run the **VSIX installer** you downloaded.
  6. If the installation is successful, run Visual Studio.

### Rhino 7

  1. Exit **Visual Studio**.
  2. Download the **[Rhino 7 C/C++ SDK](https://www.rhino3d.com/download/Rhino-SDK/7.0/latest)**.
  3. Run the **SDK installer** you downloaded.
  4. If the installation is successful, run Visual Studio.

## Next Steps

**Congratulations!** You have the tools to build a C/C++ plugin for Rhino for
Windows. _Now what?_

Check out the [Creating your first C/C++ plugin for
Rhino](https://developer.rhino3d.com/guides/cpp/your-first-plugin-windows/)
guide for instructions building your first plugin.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/installing-
tools-windows/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/installing-
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

