---
url: https://developer.rhino3d.com/samples/cpp/calculate-curve-intersections/
scraped_at: 2025-09-08T15:47:41.632495
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

Calculate Curve Intersections

__

Windows only

Demonstrates how to calculate the intersection of two curves and obtain their
intersection points.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand(
          const CRhinoCommandContext& context
          )
    {
      // Select two curves to intersect
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select two curves" );
      go.SetGeometryFilter( ON::curve_object );
      go.GetObjects( 2, 2 );
      if( go.CommandResult() != CRhinoCommand::success )
        return go.CommandResult();
    
      // Validate input
      const ON_Curve* curveA = go.Object(0).Curve();
      const ON_Curve* curveB = go.Object(1).Curve();
      if( 0 == curveA | 0 == curveB )
        return CRhinoCommand::failure;
    
      // Calculate the intersection
      double intersection_tolerance = 0.001;
      double overlap_tolerance = 0.0;
      ON_SimpleArray<ON_X_EVENT> events;
      int count = curveA->IntersectCurve(
            curveB,
            events,
            intersection_tolerance,
            overlap_tolerance
            );
    
      // Process the results
      if( count > 0 )
      {
        int i;
        for( i = 0; i < events.Count(); i++ )
        {
          const ON_X_EVENT& e = events[i];
          context.m_doc.AddPointObject( e.m_A[0] );
          if( e.m_A[0].DistanceTo(e.m_B[0]) > ON_EPSILON )
          {
            context.m_doc.AddPointObject( e.m_B[0] );
            context.m_doc.AddCurveObject( ON_Line(e.m_A[0], e.m_B[0]) );
          }
        }
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

