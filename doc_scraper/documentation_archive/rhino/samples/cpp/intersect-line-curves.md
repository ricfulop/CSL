---
url: https://developer.rhino3d.com/samples/cpp/intersect-line-curves/
scraped_at: 2025-09-08T15:47:54.654485
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

Intersect Line Curves

__

Windows only

Demonstrates how to intersect line curves.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select lines" );
      go.SetGeometryFilter( ON::curve_object );
      go.GetObjects( 2, 2 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      if( go.ObjectCount() != 2 )
        return failure;
    
      const ON_LineCurve* crv0 = ON_LineCurve::Cast( go.Object(0).Geometry() );
      const ON_LineCurve* crv1 = ON_LineCurve::Cast( go.Object(1).Geometry() );
      if( 0 == crv0 | 0 == crv1 )
        return failure;  
    
      ON_Line line0 = crv0->m_line;
      ON_Line line1 = crv1->m_line;
    
      ON_3dVector v0 = line0.to - line0.from;
      v0.Unitize();
    
      ON_3dVector v1 = line1.to - line1.from;
      v1.Unitize();
    
      if( v0.IsParallelTo(v1) != 0 )
      {
        RhinoApp().Print( L"Selected lines are parallel.\n" );
        return nothing;
      }
    
      ON_Line ray0( line0.from, line0.from + v0 );
      ON_Line ray1( line1.from, line1.from + v1 );
    
      double s = 0, t = 0;
      if( !ON_Intersect(ray0, ray1, &s, &t) )
      {
        RhinoApp().Print( L"No intersection found.\n" );
        return nothing;
      }
    
      ON_3dPoint pt0 = line0.from + s * v0;
      ON_3dPoint pt1 = line1.from + t * v1;
    
      // pt0 and pt1 should be equal, so we will
      // only add pt0 to the document
      context.m_doc.AddPointObject( pt0 );
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

