---
url: https://developer.rhino3d.com/guides/cpp/toggling-status-bar/
scraped_at: 2025-09-08T15:40:16.754601
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

[Toggling the Status Bar](https://developer.rhino3d.com/guides/cpp/toggling-
status-bar/)

  * Overview
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Toggling the Status Bar

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

When you run the Options command, all Rhino’s options or application settings
that you see are maintained by a `CRhinoAppSettings` class stored on the Rhino
application object. This class is a container class as it holds several other
`CRhinoApp_xxx_Settings` classes that help to organize all the options.

The process for modifying any Rhino option is:

  1. Find the container class in `CRhinoAppSettings` that holds the option you want to change.
  2. Make a copy of that container class.
  3. Change the appropriate members.
  4. Replace Rhino’s copy of that container class with yours by calling one of `CRhinoAppSettings`’ `Set_xxx_Settings()` member functions.

## Sample

The following sample source code demonstrates how to show or hide Rhino’s
status bar using the Rhino C/C++ SDK…

    
    
    void ShowRhinoStatusBar( BOOL bShow )
    {
      // Copy the CRhinoAppAppearanceSettings class
      CRhinoAppAppearanceSettings settings = RhinoApp().AppSettings().AppearanceSettings( true );
      if( settings.m_show_statusbar != bShow )
      {
        // Modify the desired setting
        settings.m_show_statusbar = bShow;
        // Replace the CRhinoAppAppearanceSettings with the modified version
        RhinoApp().AppSettings().SetAppearanceSettings( settings );
      }
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/toggling-
status-bar/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/toggling-
status-bar/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

