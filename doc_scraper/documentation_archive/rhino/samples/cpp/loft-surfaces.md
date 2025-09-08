---
url: https://developer.rhino3d.com/samples/cpp/loft-surfaces/
scraped_at: 2025-09-08T15:48:08.701280
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

Loft Surfaces

__

Windows only

Demonstrates how to use the CArgsRhinoLoft class and the RhinoSdkLoftSurface
function.

C/C++

    
    
    //The following sample code demonstrates how to use the CArgsRhinoLoft class and the RhinoSdkLoftSurface function.
    //The definitions of these can be found in rhinoSdkLoft.h.
    //Note, this example does not perform any curve sorting or direction matching.
    //This is the responsibility of the the SDK developer.
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      // Select curves to loft
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select curves to loft" );
      go.SetGeometryFilter( CRhinoGetObject::curve_object );
      go.SetGeometryAttributeFilter( CRhinoGetObject::open_curve );
      go.EnableSubObjectSelect( FALSE );
      go.GetObjects( 2, 0 );
      if( go.CommandResult() != CRhinoCommand::success )
        return go.CommandResult();
    
      // Fill in loft arguments class
      CArgsRhinoLoft args;
      args.m_bAllowStartTangent = FALSE;
      args.m_bAllowEndTangent = FALSE;
      args.m_bUseStartpoint = FALSE;
      args.m_bUseEndpoint = FALSE;
      args.m_bClosed = FALSE;
      args.m_loft_type = CArgsRhinoLoft::ltTight;
      args.m_simplify_method = CArgsRhinoLoft::lsNone;
      args.m_start_condition = CArgsRhinoLoft::leNatural;
      args.m_end_condition = CArgsRhinoLoft::leNatural;
      args.m_rebuild_point_count = 10;
      args.m_refit_tolerance = context.m_doc.AbsoluteTolerance();
    
      int i, object_count = go.ObjectCount();
      args.m_loftcurves.SetCapacity( object_count );
    
      // Add loft curves
      for( i = 0; i < object_count; i++ )
      {
        const ON_Curve* curve = go.Object(i).Curve();
        if( curve )
        {
          CRhinoLoftCurve* loft_curve = new CRhinoLoftCurve;
          loft_curve->m_curve = curve->DuplicateCurve();
          loft_curve->m_curve->RemoveShortSegments( ON_ZERO_TOLERANCE, true );
          loft_curve->m_pick-point = ON_UNSET_POINT;
          loft_curve->m_pick_t = ON_UNSET_VALUE;
          loft_curve->m_trim = 0;
          loft_curve->m_bClosed =
              loft_curve->m_curve->IsClosed() ? true : false;
          loft_curve->m_bPlanar =
              loft_curve->m_curve->IsPlanar(&loft_curve->m_plane)? true : false;
          args.m_loftcurves.Append( loft_curve );
        }
      }
    
      // Do the loft operation
      ON_SimpleArray<ON_NurbsSurface*> surface_list;
      bool rc = RhinoSdkLoftSurface( args, surface_list );
    
      // Delete the loft curves used in the surface calculation
      for( i = 0; i < args.m_loftcurves.Count(); i++ )
        delete args.m_loftcurves[i];
      args.m_loftcurves.Empty();
    
      // If only one surface was calculated, add it to Rhino
      if( surface_list.Count() == 1 )
      {
        CRhinoSurfaceObject* surf_obj = context.m_doc.AddSurfaceObject(*surface_list[0]);
    
        // AddSurfaceObject make a copy...
        delete surface_list[0];
    
        if( surf_obj )
          context.m_doc.Redraw();
    
        return ( surf_obj ? success : failure );
      }
    
      // If more than one surface was calculated, create a list of breps.
      ON_SimpleArray<ON_Brep*> brep_list;
      for( i = 0; i < surface_list.Count(); i++)
      {
        if( surface_list[i]->IsValid() )
        {
          ON_Brep* brep = ON_Brep::New();
          brep->NewFace( *surface_list[i] );
          delete surface_list[i];
          brep_list.Append( brep );
        }
      }
    
      // Try joining all breps
      ON_Brep* brep = RhinoJoinBreps( brep_list, context.m_doc.AbsoluteTolerance() );
      if( brep )
      {
        CRhinoBrepObject* brep_object = context.m_doc.AddBrepObject( *brep );
    
        // AddBrepObject makes a copy...
        delete brep;
    
        if( brep_object )
          context.m_doc.Redraw();
    
        return ( brep_object ? success : failure );
      }
    
      // Othewise just add the individual breps to Rhino.
      for( i = 0; i < brep_list.Count(); i++ )
      {
        if( brep_list[i] )
        {
          CRhinoBrepObject* brep_object = context.m_doc.AddBrepObject( *brep_list[i] );
    
          // AddBrepObject make a copy...
          delete brep_list[i];
        }
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

