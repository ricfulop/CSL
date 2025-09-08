---
url: https://developer.rhino3d.com/guides/cpp/offsetting-curves-on-surfaces/
scraped_at: 2025-09-08T15:39:08.492283
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

[Offsetting Curves on
Surfaces](https://developer.rhino3d.com/guides/cpp/offsetting-curves-on-
surfaces/)

  * Problem
  * Solution
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Offsetting Curves on Surfaces

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You are using the `RhinoOffsetCurveOnSrf` function to offset a curve which was
interpolated on a cylindrical surface. The problem is that the results do not
seem to match those of Rhino’s `OffsetCrvOnSrf` command. That is, the offset
curve does not extend to the edges of the surfaces. Why is this?

## Solution

After calculating the offset curve, the `OffsetCrvOnSrf` command extends both
ends of that curve to the surface edge using `RhinoExtendCrvOnSrf`. Below is
an sample of how you can do this using the SDK…

## Sample

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      // Select curve on surface
      CRhinoGetObject gc;
      gc.SetCommandPrompt( L"Select curve on surface" );
      gc.SetGeometryFilter( CRhinoGetObject::curve_object );
      gc.GetObjects( 1, 1 );
      if( gc.CommandResult() != CRhinoCommand::success )
        return gc.CommandResult();
    
      // Validate curve
      const ON_Curve* crv = gc.Object(0).Curve();
      if( 0 == crv )
        return CRhinoCommand::failure;
    
      // Select base surface
      CRhinoGetObject gs;
      gs.SetCommandPrompt( L"Select base surface" );
      gs.SetGeometryFilter( CRhinoGetObject::surface_object );
      gs.EnablePreSelect( false );
      gs.EnableDeselectAllBeforePostSelect( false );
      gs.GetObjects( 1, 1 );
      if( gs.CommandResult() != CRhinoCommand::success )
        return gs.CommandResult();
    
      // Validate face
      const ON_BrepFace* face = gs.Object(0).Face();
      if( 0 == face )
        return CRhinoCommand::failure;
    
      // Validate brep
      const ON_Brep* brep = face->Brep();
      if( 0 == brep )
        return CRhinoCommand::failure;
    
      // Specify offset distance
      CRhinoGetNumber gd;
      gd.SetCommandPrompt( L"Offset distance" );
      gd.SetDefaultNumber( 1.0 );
      gd.GetNumber();
      if( gd.CommandResult() != CRhinoCommand::success )
        return gd.CommandResult();
    
      double dist = gd.Number();
    
      // Do offset curve on surface
      double tol = context.m_doc.AbsoluteTolerance();
      ON_SimpleArray<ON_Curve*> offset_curves;
      CRhinoCommand::result cmdrc = RhinoOffsetCurveOnSrf( crv, brep, face->m_face_index, dist, tol, offset_curves );
      if( cmdrc == CRhinoCommand::success )
      {
        int i = 0;
        ON_SimpleArray<const ON_Curve*> curves_to_join;
        curves_to_join.Append( offset_curves.Count(), offset_curves.Array() );
    
        // Try joining the offset curves
        ON_SimpleArray<ON_Curve*> joined_curves;
        BOOL rc = RhinoMergeCurves( curves_to_join, joined_curves, 2.0 * tol, TRUE );
    
        for( i = 0; i < curves_to_join.Count(); i++ )
          curves_to_join[i] = 0;
    
        if( rc )
        {
          for( i = 0; i < joined_curves.Count(); i++ )
          {
            ON_Curve* pC = joined_curves[i];
            if( pC )
            {
              // Extend both ends to edge of the surface
              if( !pC->IsClosed() )
                RhinoExtendCrvOnSrf( *face, pC );
    
              // Add to document
              CRhinoCurveObject* crv_obj = new CRhinoCurveObject();
              crv_obj->SetCurve( pC );
              context.m_doc.AddObject( crv_obj );
    
              joined_curves[i] = 0;
            }
          }
    
          // Do not leak memory
          for( i = 0; i < offset_curves.Count(); i++ )
          {
            if( offset_curves[i] )
            {
              delete offset_curves[i];
              offset_curves[i] = 0;
            }
          }
        }
        else
        {
          for( i = 0; i < offset_curves.Count(); i++)
          {
            ON_Curve* pC = offset_curves[i];
            if( pC )
            {
              // Extend both ends to edge of the surface
              if( !pC->IsClosed() )
                RhinoExtendCrvOnSrf( *face, pC );
    
              // Add to document
              CRhinoCurveObject* crv_obj = new CRhinoCurveObject();
              crv_obj->SetCurve( pC );
              context.m_doc.AddObject( crv_obj );
    
              offset_curves[i] = 0;
            }
          }
        }
      }
    
      context.m_doc.Redraw();
    
      return CRhinoCommand::success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/offsetting-
curves-on-surfaces/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/offsetting-
curves-on-surfaces/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

