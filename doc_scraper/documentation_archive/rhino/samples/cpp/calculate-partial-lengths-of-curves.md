---
url: https://developer.rhino3d.com/samples/cpp/calculate-partial-lengths-of-curves/
scraped_at: 2025-09-08T15:47:43.599547
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

Calculating Partial Lengths of Curves

__

Windows only

Demonstrates how to calculate the length of a curve from the start point to
some point on the curve.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select curve" );
      go.SetGeometryFilter( CRhinoGetObject::curve_object );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != CRhinoCommand::success )
        return go.CommandResult();
    
      const ON_Curve* crv = go.Object(0).Curve();
      if( 0 == crv )
        return CRhinoCommand::failure;
    
      CRhinoGetPoint gp;
      gp.SetCommandPrompt( L"Point on surface" );
      gp.Constrain( *crv );
      gp.GetPoint();
      if( gp.CommandResult() != CRhinoCommand::success )
        return gp.CommandResult();
    
      ON_3dPoint pt = gp.Point();
    
      double t = 0.0;
      if( crv->GetClosestPoint(pt, &t) )
      {
        ON_Interval domain = crv->Domain();
        ON_Interval sub_domain( domain.Min(), t );
        double length = 0.0;
        if( crv->GetLength(&length, 0.0, &sub_domain) )
          RhinoApp().Print( L"Distance from start of curve = %f.\n", length );
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

