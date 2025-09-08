---
url: https://developer.rhino3d.com/samples/cpp/get-point-at-mouse-location/
scraped_at: 2025-09-08T15:48:02.558126
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

Get Point at Mouse Location

__

Windows only

Discusses how to convert a 2D screen point into a 3D world point.

C/C++

    
    
    static bool GetPointAtCursorPos( ON_3dPoint& point )
    {
      bool rc = false;
      CRhinoView* view = RhinoApp().ActiveView();
      if (view)
      {
        POINT pt;
        if (::GetCursorPos(&pt) )
        {
          view->ScreenToClient( &pt );
          ON_Xform xform;
          if( view->ActiveViewport().VP().GetXform(ON::screen_cs, ON::world_cs, xform) )
          {
            point = ON_3dPoint( pt.x, pt.y, 0.0 );
            point.Transform( xform );
            rc = true;
          }
        }
      }
      return rc;
    }
    

  

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

