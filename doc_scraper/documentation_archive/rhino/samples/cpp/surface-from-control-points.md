---
url: https://developer.rhino3d.com/samples/cpp/surface-from-control-points/
scraped_at: 2025-09-08T15:47:33.123445
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

Surface from Control Points

__

Windows only

Demonstrates how to create a surface from a grid of control points.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      // Degree 3 surface
      int degree[2];
      degree[0] = 3;
      degree[1] = 3;
    
      // Four columns of four points
      int point_count[2];
      point_count[0] = 4;
      point_count[1] = 4;
    
      ON_3dPointArray point_array( point_count[0] * point_count[1] );
    
      point_array.Append( ON_3dPoint(0,0,0) );
      point_array.Append( ON_3dPoint(0,3.33,0) );
      point_array.Append( ON_3dPoint(0,6.67,0) );
      point_array.Append( ON_3dPoint(0,10,0) );
    
      point_array.Append( ON_3dPoint(6.68,0,-0.0296) );
      point_array.Append( ON_3dPoint(6.68,3.33,-0.0296) );
      point_array.Append( ON_3dPoint(6.68,6.67,-0.0296) );
      point_array.Append( ON_3dPoint(6.68,10,-0.0296) );
    
      point_array.Append( ON_3dPoint(13.3,0,2.77) );
      point_array.Append( ON_3dPoint(13.3,3.33,2.77) );
      point_array.Append( ON_3dPoint(13.3,6.67,2.77) );
      point_array.Append( ON_3dPoint(13.3,10,2.77) );
    
      point_array.Append( ON_3dPoint(17.9,0,7.58) );
      point_array.Append( ON_3dPoint(17.9,3.33,7.58) );
      point_array.Append( ON_3dPoint(17.9,6.67,7.58) );
      point_array.Append( ON_3dPoint(17.9,10,7.58) );
    
      ON_NurbsSurface srf;
      if( RhinoSrfControlPtGrid( point_count, degree, point_array, &srf) )
      {
        context.m_doc.AddSurfaceObject( srf );
        context.m_doc.Redraw();
      }
    
      return success;
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

