---
url: https://developer.rhino3d.com/samples/cpp/split-curve-into-multiple-segments/
scraped_at: 2025-09-08T15:47:57.660101
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

Split Curve Into Multiple Segments

__

Windows only

Demonstrates how to split a curve into multiple curve segments.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      // Select curve to split
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select curve to split" );
      go.SetGeometryFilter( CRhinoGetObject::curve_object );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      // Validate selection
      const CRhinoObjRef& crv_obj_ref = go.Object(0);
      const CRhinoObject* crv_obj = crv_obj_ref.Object();
      const ON_Curve* crv = crv_obj_ref.Curve();
      if( 0 == crv_obj | 0 == crv )
        return failure;
    
      // Number of segments to create
      CRhinoGetInteger gi;
      gi.SetCommandPrompt( L"Number of segments to create" );
      gi.SetLowerLimit( 2 );
      gi.SetUpperLimit( 100 );
      gi.GetInteger();
      if( gi.CommandResult() != success )
        return gi.CommandResult();
    
      int num_segments = gi.Number();
    
      // Generate an array of curve parameters where
      // the splitting will occur.
      ON_SimpleArray<double> curve_t( num_segments );
      bool rc = RhinoDivideCurve( *crv, num_segments, 0, false, true, 0, &curve_t );
      if( !rc )
      {
        RhinoApp().Print( L"Error dividing curve into segments.\n" );
        return failure;
      }
    
      // If the curve is closed, append the ending domain parameter
      ON_Interval dom = crv->Domain();
      if( crv->IsClosed() )
        curve_t.Append( dom.m_t[1] );
    
      ON_3dmObjectAttributes atts( crv_obj->Attributes() );
    
      // Do the splitting (or should I say trimming...)
      int i;
      for( i = 0; i < curve_t.Count() - 1; i++ )
      {
        // Build an interval to trim
        ON_Interval interval( curve_t[i], curve_t[i+1] );
        if( dom.Includes(interval) )
        {
          // Do the trim
          ON_Curve* new_crv = ON_TrimCurve( *crv, interval );
          if( new_crv )
          {
            // Add the "trimmed" curve
            CRhinoCurveObject* new_crv_obj = new CRhinoCurveObject( atts );
            new_crv_obj->SetCurve( new_crv );
            context.m_doc.AddObject( new_crv_obj );
          }
        }
      }
    
      // Delete the original object
      context.m_doc.DeleteObject( crv_obj_ref );
      context.m_doc.Redraw();
    
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

