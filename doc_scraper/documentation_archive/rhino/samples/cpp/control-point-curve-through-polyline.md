---
url: https://developer.rhino3d.com/samples/cpp/control-point-curve-through-polyline/
scraped_at: 2025-09-08T15:47:44.494531
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

Control Point Curve Through Polyline

__

Windows only

Demonstrates how to create a control points curve through a polyline.

C/C++

    
    
    ON_NurbsCurve* RhControlPointsCurveThroughPolyline(
        const ON_Polyline& polyline,
        int degree
        )
    {
      const int count = polyline.Count();
      if( count < 2 )
        return 0;
    
      degree = ( count <= degree) ? count - 1 : degree;
    
      ON_NurbsCurve* curve = ON_NurbsCurve::New();
      if( curve )
      {
        bool rc = false;
        if( polyline.IsClosed() )
          rc = curve->CreatePeriodicUniformNurbs( 3, degree + 1, count - 1, polyline );
        else
          rc = curve->CreateClampedUniformNurbs( 3, degree + 1, count, polyline );
    
        if( !rc )
        {
          delete curve;
          curve = 0;
        }
      }
    
      return curve;
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

