---
url: https://developer.rhino3d.com/samples/cpp/calculate-radius-of-curvature/
scraped_at: 2025-09-08T15:47:42.676859
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

Calculate Radius of Curvature

__

Windows only

Demonstrates how to compute the radius of curvature of a curve object at a
selected location.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select curve for curvature measurement" );
      go.SetGeometryFilter( CRhinoGetObject::curve_object );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      const ON_Curve* crv = go.Object(0).Curve();
      if( 0 == crv )
        return failure;
    
      CRhinoGetPoint gp;
      gp.SetCommandPrompt( L"Select point on curve for curvature measurement" );
      gp.Constrain( *crv );
      gp.GetPoint();
      if( gp.CommandResult() != success )
        return gp.CommandResult();
    
      ON_3dPoint pt = gp.Point();
    
      double t = 0.0;
      if( !crv->GetClosestPoint(pt, &t) )
      {
        RhinoApp().Print( L"Failed to compute radius of curvature.\n" );
        return failure;
      }
    
      ON_3dVector tangent = crv->TangentAt( t );
      if( tangent.IsTiny() )
      {
        RhinoApp().Print( L"Failed to compute radius of curvature. Curve may have stacked control points.\n" );
        return failure;
      }
    
      ON_3dVector curvature = crv->CurvatureAt( t );
      const double k = curvature.Length();
      if( k < ON_SQRT_EPSILON )
      {
        RhinoApp().Print( L"Radius of curvature: infinite.\n" );
        return failure;
      }
    
      ON_3dVector radius_vector = curvature / (k * k);
      ON_Circle circle;
      if ( !circle.Create(pt, tangent, pt + 2.0 * radius_vector) )
      {
        RhinoApp().Print( L"Failed to compute radius of curvature.\n" );
        return failure;
      }
    
      context.m_doc.AddCurveObject( circle );
      context.m_doc.AddPointObject( pt );
      context.m_doc.Redraw();
    
      ON_wString wRadius;
      RhinoFormatNumber( circle.Radius(), wRadius );
      RhinoApp().Print( L"Radius of curvature: %s.\n", wRadius );
    
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

