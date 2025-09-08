---
url: https://developer.rhino3d.com/samples/cpp/curve-evaluation/
scraped_at: 2025-09-08T15:47:47.617881
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

Curve Evaluation

__

Windows only

Demonstrates how to evaluate a curve.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select curve for evaluation" );
      go.SetGeometryFilter( CRhinoGetObject::curve_object );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      const ON_Curve* crv = go.Object(0).Curve();
      if( 0 == crv )
        return failure;
    
      CRhinoGetPoint gp;
      gp.SetCommandPrompt( L"Pick point on curve for evaluation" );
      gp.Constrain( *crv );
      gp.GetPoint();
      if( gp.CommandResult() != success )
        return gp.CommandResult();
    
      double t = 0.0;
      if( 0 == gp.PointOnCurve(&t) )
        return nothing;
    
      CRhinoGetInteger gi;
      gi.SetCommandPrompt( L"Number of derivatives to calculate" );
      gi.SetDefaultInteger( 1 );
      gi.SetLowerLimit( 0 );
      gi.SetUpperLimit( 4 );
      gi.GetNumber();
      if( gi.CommandResult() != success )
        return gi.CommandResult();
    
      int der_count = gi.Number();
    
      // Allocate memory for results
      int v_stride = 3;
      int v_count = v_stride * ( der_count + 1 );
      ON_SimpleArray<double> v_array( v_count );
      v_array.SetCount( v_count );
    
      // Do the curve evaluation
      if( crv->Evaluate(t, der_count, v_stride, v_array.Array()) )
      {
        const double* v = v_array.Array();
        int i;
        for( i = 0; i < der_count + 1; i++ )
        {
          RhinoApp().Print( L"Derivative %d = (%.3f,%.3f,%.3f)\n", i, v[0], v[1], v[2] );
          v += v_stride;
        }
      }
      else
      {
        RhinoApp().Print( L"Failed to evaluate curve.\n" );
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

