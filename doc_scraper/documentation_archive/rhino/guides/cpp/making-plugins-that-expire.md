---
url: https://developer.rhino3d.com/guides/cpp/making-plugins-that-expire/
scraped_at: 2025-09-08T15:39:59.670531
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

[Making Plugins That Expire](https://developer.rhino3d.com/guides/cpp/making-
plugins-that-expire/)

  * Problem
  * Solution
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Making Plugins That Expire

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You would like to release a work-in-progress, or WIP, version of your plugin
so you can get some customer feedback before shipping. You would like the
plugin to expire after a number of days. Is there something in Rhino that
could help with this?

## Solution

Rhino does not have any feature that can help with this. But, it is not too
difficult to compare the compile date of the plugin with the current date to
see if you plugin should load or not. The following example code demonstrates
this…

## Sample

    
    
    BOOL CTestPlugIn::OnLoadPlugIn()
    {
    #if defined(WIP)
    
      // Easy cheezy way of testing to see if plugin has expired.
      COleDateTime compile_time;
      compile_time.ParseDateTime( ON_wString(__DATE__" "__TIME__), 0, 0x0409 );
    
      COleDateTime current_time( COleDateTime::GetCurrentTime() );
    
      COleDateTimeSpan span = current_time - compile_time;
      int elapsed_days = span.GetDays();
    
      const int warn_after_days = 30;   // or whatever...
      const int expire_after_days = 40; // or whatever...
    
      if( elapsed_days >= warn_after_days )
      {
        HWND hWnd = RhinoApp().MainWnd();
        if( elapsed_days >= expire_after_days )
        {
          ON_wString str = L"This WIP has expired. Please download the latest and greatest...";
          ::MessageBox( hWnd, str, PlugInName(), MB_OK | MB_ICONERROR );
          return -1; // This will cause the plugin not to load and not display an Rhino error.
        }
        else
        {
          ON_wString str;
          str.Format( L"This WIP will expire in %d days. Please download the latest and greatest...", expire_after_days - elapsed_days );
          ::MessageBox( hWnd, str, PlugInName(), MB_OK | MB_ICONEXCLAMATION );
        }
      }
    #endif
    
      // If we got here, then the WIP was good.
      // So, do other plugin initialization
      // and return TRUE to run.
    
      return TRUE;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/making-
plugins-that-expire/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/making-
plugins-that-expire/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

