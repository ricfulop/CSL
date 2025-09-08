---
url: https://developer.rhino3d.com/guides/cpp/finding-rhino-installation-folder/
scraped_at: 2025-09-08T15:38:58.523880
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

[Finding Rhino's Installation
Folder](https://developer.rhino3d.com/guides/cpp/finding-rhino-installation-
folder/)

  * Problem
  * Solution
    * Rhino 8, 7, and 6
    * Rhino 5

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Finding Rhino's Installation Folder

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated: Monday,
August 26, 2024)

## Problem

You are putting together an installer for your Rhino plugin. You would like to
know how you can, programatically, get Rhino’s installation folder.

## Solution

### Rhino 8, 7, and 6

If you are looking for Rhino 8, 7, or 6, then you can find the location of
Rhino’s installation folder by looking in the Windows Registry in this
location:

    
    
    Hive:  HKEY_LOCAL_MACHINE
    Key:   SOFTWARE\McNeel\Rhinoceros\<version>\Install
    Name:  InstallPath
    Type:  REG_SZ
    

If you are looking for Rhino 8, for example, replace `<version>` with `8.0`.

### Rhino 5

If you are looking for Rhino 5 64-bit, then you can find the location of
Rhino’s installation folder by looking in the Windows Registry in this
location:

    
    
    Hive:  HKEY_LOCAL_MACHINE
    Key:   SOFTWARE\McNeel\Rhinoceros\5.0x64\Install
    Name:  InstallPath
    Type:  REG_SZ
    

If you are looking for Rhino 5 32-bit, then you can find the location of
Rhino’s installation folder by looking in the Windows Registry in this
location:

    
    
    Hive:  HKEY_LOCAL_MACHINE
    Key:   SOFTWARE\WOW6432Node\McNeel\Rhinoceros\5.0\Install
    Name:  InstallPath
    Type:  REG_SZ
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/finding-
rhino-installation-folder/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/finding-
rhino-installation-folder/index.md) [
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

