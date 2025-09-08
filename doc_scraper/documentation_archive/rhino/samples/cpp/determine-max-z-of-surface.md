---
url: https://developer.rhino3d.com/samples/cpp/determine-max-z-of-surface/
scraped_at: 2025-09-08T15:48:05.675635
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

Determine the Maximum Z Coordinate Value of a Surface

__

Windows only

Demonstrates how determine the maximum Z coordinate value of a surface or
polysurface given some X,Y coordinate.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      double x = 0.0, y = 0.0;
      ON_wString sx, sy, sz;
    
      // Pick a brep to evaluate
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select surface or polysurface to evaluate" );
      go.SetGeometryFilter( CRhinoGetObject::surface_object|CRhinoGetObject::polysrf_object );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      // Get the brep geometry
      const CRhinoObjRef& ref = go.Object(0);
      const ON_Brep* brep = ref.Brep();
      if( !brep )
        return failure;
    
      // Prompt for an X coordinate value
      CRhinoGetNumber gn;
      gn.SetCommandPrompt( L"Value of X coordinate" );
      gn.SetDefaultNumber( x );
      gn.GetNumber();
      if( gn.CommandResult() != success )
        return gn.CommandResult();
    
      x = gn.Number();
      RhinoFormatNumber( x, sx );
    
      // Prompt for a Y coordinate value
      gn.SetCommandPrompt( L"Value of Y coordinate" );
      gn.SetDefaultNumber( y );
      gn.GetNumber();
      if( gn.CommandResult() != success )
        return gn.CommandResult();
    
      y = gn.Number();
      RhinoFormatNumber( y, sy );
    
      // Now that we have all of the input, we want to intersect
      // a line curve with the brep. To determine the magnitude of
      // the line, we will first get the brep's bounding box.
      ON_BoundingBox bbox;
      if( !brep->GetTightBoundingBox(bbox) )
        return failure;
    
      // Calculate the height of the bounding box
      ON_3dVector v = bbox.Corner(0,0,1) - bbox.Corner(0,0,0);
    
      // Starting point of line
      ON_3dPoint p0( x, y, 0.0 );
    
      // Ending point of line. To make sure the line
      // completely intersects the brep, we will double
      // the height.
      ON_3dPoint p1( x, y, v.Length() * 2 );
    
      // Create the line curve
      ON_LineCurve line( p0, p1 );
    
      // Intersect the line with the brep
      ON_SimpleArray<ON_Curve*> curves;
      ON_3dPointArray points;
      bool rc = RhinoCurveBrepIntersect( line, *brep, context.m_doc.AbsoluteTolerance(), curves, points );
      if( false == rc | 0 == points.Count() )
      {
        RhinoApp().Print( L"No maximum surface Z coordinate at %s,%s found.\n", sx, sy );
        return nothing;
      }
    
      // Because it is possible that our line might intersect
      // the brep in more than one place, find the intersection
      // point that is farthest from our input coordinate.
      int i;
      ON_3dPoint pt = p0;
      for( i = 0; i < points.Count(); i++ )
      {
        if( p0.DistanceTo(points[i]) > p0.DistanceTo(pt) )
          pt = points[i];
      }
    
      // Print results
      RhinoFormatNumber( pt.z, sz );
      RhinoApp().Print( L"Maximum surface Z coordinate at %s,%s is %s.\n", sx, sy, sz );
    
      // Optional, add a point object
      context.m_doc.AddPointObject( pt );
    
      // Delete any overlap intersection curves that might have been calculated
      for( i = 0; i < curves.Count(); i++ )
      {
        delete curves[i];
        curves[i] = 0;
      }
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

