---
url: https://developer.rhino3d.com/samples/cpp/fillet-curve/
scraped_at: 2025-09-08T15:47:31.123700
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

Fillet Curve

__

Windows only

Demonstrates how to create a fillet between two curves.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      ON_3dPoint point0( 10.0,  0.0, 0.0 );
      ON_3dPoint point1( 10.0, 10.0, 0.0 );
      ON_3dPoint point2(  0.0, 10.0, 0.0 );
    
      // Create the line curves to fillet
      ON_LineCurve curve0( point0, point1 );
      ON_LineCurve curve1( point2, point1 );
    
      // Fillet at the end points of the line curves
      double curve0_t = curve0.Domain().Max();
      double curve1_t = curve1.Domain().Max();
    
      // Fillet radius
      double radius = 1.0;
    
      // Do the fillet calculation
      double t0 = 0.0, t1 = 0.0;
      ON_Plane plane;
      if( RhinoGetFilletPoints(curve0, curve1, radius, curve0_t, curve1_t, t0, t1, plane) )
      {
        // Trim back the two line curves
        ON_Interval domain0( curve0.Domain().Min(), t0 );
        curve0.Trim( domain0 );
    
        ON_Interval domain1( curve1.Domain().Min(), t1 );
        curve1.Trim( domain1 );
    
        // Compute the fillet curve
        ON_3dVector radial0 = curve0.PointAt(t0) - plane.Origin();
        radial0.Unitize();
    
        ON_3dVector radial1 = curve1.PointAt(t1) - plane.Origin();
        radial1.Unitize();
    
        double angle = acos( radial0 * radial1 );
        ON_Plane fillet_plane( plane.Origin(), radial0, radial1 );
        ON_Arc fillet( fillet_plane, plane.Origin(), radius, angle );
    
        // Add the geometry
        context.m_doc.AddCurveObject( curve0 );
        context.m_doc.AddCurveObject( curve1 );
        context.m_doc.AddCurveObject( fillet );
    
        context.m_doc.Redraw();
      }
    
      return CRhinoCommand::success;
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

