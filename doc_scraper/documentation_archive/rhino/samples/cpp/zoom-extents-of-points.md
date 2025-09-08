---
url: https://developer.rhino3d.com/samples/cpp/zoom-extents-of-points/
scraped_at: 2025-09-08T15:48:22.775820
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

Zoom Extents of Points

__

Windows only

Demonstrates how to zoom to the extends of an array of 3D points.

C/C++

    
    
    static void ZoomExtents( CRhinoView* view, const ON_3dPointArray& point_array )
    {
      if( 0 == view )
        return;
    
      const ON_Viewport& current_vp = view->ActiveViewport().VP();
      ON_Viewport zoomed_vp;
    
      ON_Xform w2c;
      current_vp.GetXform( ON::world_cs, ON::camera_cs, w2c );
    
      ON_BoundingBox bbox = point_array.BoundingBox();
      if( bbox.IsValid() )
      {
        double border = 1.1;
    
        double dx = bbox.m_max.x - bbox.m_min.x;
        dx *= 0.5 * (border - 1.0);
        bbox.m_max.x += dx;
        bbox.m_min.x -= dx;
    
        double dy = bbox.m_max.y - bbox.m_min.y;
        dy *= 0.5 * (border - 1.0);
        bbox.m_max.y += dy;
        bbox.m_min.y -= dy;
    
        if( RhinoDollyExtents(current_vp, bbox, zoomed_vp) )
        {
          view->ActiveViewport().SetVP( zoomed_vp, true );
          view->Redraw();
        }
      }
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

