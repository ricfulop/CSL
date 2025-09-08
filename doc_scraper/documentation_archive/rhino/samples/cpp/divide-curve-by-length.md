---
url: https://developer.rhino3d.com/samples/cpp/divide-curve-by-length/
scraped_at: 2025-09-08T15:47:49.643045
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

Divide a Curve by Length

__

Windows only

Demonstrates how to divide a curve object by a specified length.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand(
          const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select curve to divide" );
      go.SetGeometryFilter( CRhinoGetObject::curve_object );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != CRhinoCommand::success )
        return go.CommandResult();
    
      const CRhinoObjRef& objref = go.Object(0);
      const ON_Curve* crv = objref.Curve();
      if( !crv )
        return CRhinoCommand::failure;
    
      double crv_length = 0.0;
      crv->GetLength( &crv_length );
      if( crv_length < ON_ZERO_TOLERANCE )
        return CRhinoCommand::failure;
    
      ON_wString s;
      s.Format( L"Curve length is %g. Segment Length", crv_length );
    
      CRhinoGetNumber gn;
      gn.SetCommandPrompt( s );
      gn.SetLowerLimit( 0.0, TRUE );
      gn.SetUpperLimit( crv_length, TRUE );
      gn.GetNumber();
      if( gn.CommandResult() != CRhinoCommand::success )
        return gn.CommandResult();
    
      double seg_length = gn.Number();
      int seg_count = (int)floor( crv_length / seg_length );
      double fractional_end = (seg_count * seg_length) / crv_length;
    
      double t0, t1;
      crv->GetDomain( &t0, &t1 );
      crv->GetNormalizedArcLengthPoint( fractional_end, &t1 );
    
      seg_count++;
      ON_SimpleArray<double> t( seg_count );
      t.SetCount( seg_count );
    
      for( int i = 0; i < seg_count; i++ )
      {
        double param = (double)i / ((double)seg_count-1);
        t[i] = param;
      }
    
      ON_Interval sub_domain( t0, t1 );
      crv->GetNormalizedArcLengthPoints( seg_count,
          (double*)&t[0], (double*)&t[0],
          0.0, 1.0e-8, &sub_domain );
    
      for( int i = 0; i < seg_count; i++ )
      {
        ON_3dPoint pt = crv->PointAt( t[i] );
        context.m_doc.AddPointObject( pt );
      }
    
      context.m_doc.Redraw();
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

