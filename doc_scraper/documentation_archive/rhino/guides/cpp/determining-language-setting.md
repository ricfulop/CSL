---
url: https://developer.rhino3d.com/guides/cpp/determining-language-setting/
scraped_at: 2025-09-08T15:39:43.599798
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

[Determining Language
Setting](https://developer.rhino3d.com/guides/cpp/determining-language-
setting/)

  * Overview
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Determining Language Setting

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

Rhino provides support for multiple languages. Rhino’s language setting is
independent of the operating system’s language setting. Thus, as a plugin
developer, knowing Rhino’s current language setting is important if you plan
on supporting multiple languages.

Rhino stores its current Locale ID (LCID) in a `CRhinoAppAppearanceSettings`
object that is held within Rhino applications settings object, or
`CRhinoAppSettings`.

## Sample

The following is an example of how to determine Rhino’s current language
setting.

    
    
    ON_wString wstr;
    CRhinoAppSettings settings = ::RhinoApp().AppSettings();
    CRhinoAppAppearanceSettings appearance = settings.AppearanceSettings();
    
    switch( appearance.m_language_identifier )
    {
    case 1028: // zh-tw
      wstr = L"Chinese - Taiwan";
      break;
    case 1029: // cs
      wstr = L"Czech";
      break;
    case 1031: // de-de
      wstr = L"German - Germany";
      break;
    case 1033: // en-us
      wstr = L"English - United States";
      break;
    case 1034: // es-es
      wstr = L"Spanish - Spain";
      break;
    case 1036: // fr-fr
      wstr = L"French - France";
      break;
    case 1040: // it-it
      wstr = L"Italian - Italy";
      break;
    case 1041: // ja
      wstr = L"Japanese";
      break;
    case 1042: // ko
      wstr = L"Korean";
      break;
    case 1045: // pl
      wstr = L"Polish";
      break;
    case 2052: // zh-cn
      wstr = L"Chinese - China";
      break;
    default:
      wstr = L"unknown";
      break;
    }
    ::RhinoApp().Print( L"The current language is \"%s\ , wstr );
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/determining-
language-setting/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/determining-
language-setting/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

