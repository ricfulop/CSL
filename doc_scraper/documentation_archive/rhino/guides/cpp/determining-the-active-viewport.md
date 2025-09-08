---
url: https://developer.rhino3d.com/guides/cpp/determining-the-active-viewport/
scraped_at: 2025-09-08T15:38:55.411551
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

[Determining the Active
Viewport](https://developer.rhino3d.com/guides/cpp/determining-the-active-
viewport/)

  * Problem
  * Solution
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Determining the Active Viewport

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You are trying to determine if the current active view is a detail or a
standard view. You are having some trouble differentiating between an active
page layout and an active detail in a page layout.

## Solution

Standard Rhino views are represented by the `CRhinoView` class. Layout views
are represented by the `CRhinoPageView` class. This class is derived from
`CRhinoView`. A `CRhinoPageView` object maintains an array of
`CRhinoDetailViewObject` objects - one for each detail in the layout.

To determine whether a layout or one if it’s details is active, get the UUID
of the layout’s active detail object. If the returned UUID is `nil`, then the
layout itself is active. Otherwise, the detail object that has the returned
UUID is active.

## Sample

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoView* view = RhinoApp().ActiveView();
      if (nullptr == view)
        return CRhinoCommand::failure;
    
      CRhinoPageView* page_view = static_cast<CRhinoPageView*>(view);
      if (page_view)
      {
        ON_wString layout_name = page_view->MainViewport().Name();
        ON_UUID active_detail_uuid = page_view->ActiveDetailObject();
        if (ON_UuidIsNotNil(active_detail_uuid))
        {
          ON_wString detail_name = page_view->ActiveViewport().Name();
          RhinoApp().Print(L"The detail \"%s\" on layout \"%s\" is active.\n", 
            static_cast<const wchar_t*>(detail_name), 
            static_cast<const wchar_t*>(layout_name)
          );
        }
        else
        {
          RhinoApp().Print(L"The layout \"%s\" is active.\n", 
            static_cast<const wchar_t*>(layout_name)
          );
        }
      }
      else
      {
        ON_wString viewport_name = view->ActiveViewport().Name();
        RhinoApp().Print(L"The viewport \"%s\" is active.\n", 
          static_cast<const wchar_t*>(viewport_name)
        );
      }
    
      return CRhinoCommand::success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/determining-
the-active-viewport/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/determining-
the-active-viewport/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

