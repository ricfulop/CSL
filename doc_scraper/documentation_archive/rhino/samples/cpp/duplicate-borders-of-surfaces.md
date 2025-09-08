---
url: https://developer.rhino3d.com/samples/cpp/duplicate-borders-of-surfaces/
scraped_at: 2025-09-08T15:48:06.697333
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

Duplicate the Borders of Surfaces

__

Windows only

Demonstrates how to duplicate the borders of surfaces and polysurfaces.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select surface or polysurface" );
      go.SetGeometryFilter( CRhinoGetObject::surface_object |
                            CRhinoGetObject::polysrf_object );
      go.AcceptNothing();
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      const CRhinoObjRef& object_ref = go.Object(0);
      const CRhinoObject* object = object_ref.Object();
      const ON_Brep* brep = object_ref.Brep();
      if( !object | !brep )
        return failure;
    
      object->Select( false );
    
      ON_SimpleArray<const ON_Curve*> curve_array( brep->m_E.Count() );
    
      for( int i = 0; i < brep->m_E.Count(); i++ )
      {
        const ON_BrepEdge& edge = brep->m_E[i];
    
        // Find only the naked edges
        if( edge.m_ti.Count() == 1 && edge.m_c3i >= 0 )
        {
          ON_Curve* curve = edge.DuplicateCurve();
    
          // Make the curve direction go in the natural
          // boundary loop direction so that the curve
          // directions come out consistantly
          if( brep->m_T[edge.m_ti[0]].m_bRev3d )
            curve->Reverse();
          if( brep->m_T[edge.m_ti[0]].Face()->m_bRev)
            curve->Reverse();
    
          curve_array.Append( curve );
        }
      }
    
      double tol = 2.1 * RhinoApp().ActiveDoc()->AbsoluteTolerance();
      ON_SimpleArray<ON_Curve*> output_array;
    
      // Join the curves
      if( RhinoMergeCurves(curve_array, output_array, tol) )
      {
        for( int i = 0; i < output_array.Count(); i++ )
        {
          CRhinoCurveObject* curve_object = new CRhinoCurveObject;
          curve_object->SetCurve( output_array[i]);
          if( context.m_doc.AddObject(curve_object) )
            curve_object->Select();
          else
            delete curve_object;
        }
      }
    
      // Don't leak memory
      for( int i = 0; i < curve_array.Count(); i++ )
        delete curve_array[i];
    
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

