---
url: https://developer.rhino3d.com/samples/cpp/create-contour-curves/
scraped_at: 2025-09-08T15:47:24.092306
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

Create Contour Curves

__

Windows only

Demonstrates how to create contour curves through surfaces, breps, and meshes
using the MakeRhinoContours() function.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand(
          const CRhinoCommandContext& context )
    {
      unsigned int filter = CRhinoGetObject::surface_object |
                            CRhinoGetObject::polysrf_object |
                            CRhinoGetObject::mesh_object;
      // Prompt for object to contour
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select object to contour" );
      go.SetGeometryFilter( filter );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      // Validate selection
      const CRhinoObjRef& objref = go.Object(0);
      const ON_Geometry* geom = objref.Geometry();
      if( !geom )
        return failure;
    
      // Prompt for base point
      CRhinoGetPoint gp;
      gp.SetCommandPrompt( L"Contour plane base point" );
      gp.GetPoint();
      if( gp.CommandResult() != success )
        return gp.CommandResult();
    
      ON_3dPoint basept = gp.Point();
    
      // Prompt for end point
      gp.DrawLineFromPoint( basept, true );
      gp.SetCommandPrompt( L"Direction perpendicular to contour planes" );
      gp.GetPoint();
      if( gp.CommandResult() != success )
        return gp.CommandResult();
    
      // Verify base and end points are not the same
      ON_3dPoint endpt = gp.Point();
      if( basept.DistanceTo(endpt) < ON_ZERO_TOLERANCE )
        return nothing;
    
      // Prompt for distance between contours
      CRhinoGetDistance gd;
      gd.SetCommandPrompt( L"Distance between contours" );
      gd.SetDefaultNumber( 1.0 );
      gd.GetDistance();
      if( gd.CommandResult() != success )
        return gd.CommandResult();
    
      // Make sure interval is reasonable
      double interval = fabs( gd.Distance() );
      if( interval < ON_ZERO_TOLERANCE )
        return nothing;
    
      // Create contour input
      CRhinoContourInput contour;
      contour.m_geom.Append( geom );
      contour.m_basept = basept;
      contour.m_endpt = endpt;
      contour.m_interval = interval;
      contour.m_limit_range = false;
    
      // Create arrays for contour output
      ON_SimpleArray<ON_Polyline*> pline_array;
      ON_SimpleArray<ON_Curve*> crv_array;
    
      // Make the contours. Note, this function allocates memory
      // for new curves and polylines. Thus, we are responsible
      // for clean up the memory.
      bool rc = MakeRhinoContours( contour, pline_array, crv_array );
      if( !rc )
        return failure;
      context.m_doc.UnselectAll();
    
      // Process crves created by contouring surfaces and polysurfaces
      for( int i = 0; i < crv_array.Count(); i++)
      {
        ON_Curve* crv = crv_array[i];
        if( crv )
        {
          CRhinoCurveObject* crvobj = context.m_doc.AddCurveObject( *crv );
          if( crvobj )
            crvobj->Select();
    
          // CRhinoDoc::AddCurveObject() makes a copy of the input.
          // Thus, we must delete crv, otherwise we will leak memory.
          delete crv;
          crv_array[i] = 0;
        }
      }
    
      // Process polylines created by contouring meshes
      for( int i = 0; i < pline_array.Count(); i++)
      {
        ON_Polyline* pline = pline_array[i];
        if( pline )
        {
          CRhinoCurveObject* crvobj = context.m_doc.AddCurveObject( *pline );
          if( crvobj )
            crvobj->Select();
    
          // CRhinoDoc::AddCurveObject() makes a copy of the input.
          // Thus, we must delete pline, otherwise we will leak memory.
          delete pline;
          pline_array[i] = 0;
        }
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

