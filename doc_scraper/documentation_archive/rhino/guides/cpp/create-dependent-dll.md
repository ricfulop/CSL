---
url: https://developer.rhino3d.com/guides/cpp/create-dependent-dll/
scraped_at: 2025-09-08T15:40:22.778266
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

[Creating a Rhino-dependent C++
DLL](https://developer.rhino3d.com/guides/cpp/create-dependent-dll/)

  * Overview
  * Create the DLL

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Creating a Rhino-dependent C++ DLL

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated: Monday,
October 7, 2024)

## Overview

A Rhino-dependent C++ DLL is one that links with Rhino C++ SDK libraries, and
that can be used to add functionality that can be shared between multiple C++
plug-ins, or that can be used to add Platform Invoke (PInvoke), interop
functionality to RhinoCommon or Grasshopper plug-ins.

## Create the DLL

To create a Rhino-dependent C++ DLL:

  1. Download and install the [Rhino C++ SDK](https://developer.rhino3d.com/guides/cpp/installing-tools-windows/).
  2. Launch Visual Studio.
  3. Create a new [Rhino C/C++ plug-in project](https://developer.rhino3d.com/guides/cpp/your-first-plugin-windows/).
  4. Using **Solution Explorer** , delete the `<Project>PlugIn` .cpp and .h files, and delete the `<Project>Command` .cpp file.
  5. Using **Property Manager** , remove the `Rhino.Cpp.PlugIn` property page from both the `Debug|x64` and the `Release|x64` build configurations.
  6. Again using **Property Manager** , add the `Rhino.Cpp.PlugInComponent.props` property page to both the `Debug|x64` and the `Release|x64` build configurations. The property page file is found in the `PropertySheets`` folder in the Rhino C++ SDK installation folder.
  7. Build the project.

Done! You now have a Rhino-dependent DLL project. Now you are ready to add
your functionality; either by adding or linking in other libraries, or by
exporting custom C++ functions.

# More information

[Wrapping Native
Libraries](https://developer.rhino3d.com/guides/rhinocommon/wrapping-native-
libraries/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/create-
dependent-dll/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/create-
dependent-dll/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

