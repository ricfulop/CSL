---
url: https://developer.rhino3d.com/samples/cpp/intersect-curve-with-mesh/
scraped_at: 2025-09-08T15:47:53.652125
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

Intersect Curves with Meshes

__

Windows only

Demonstrates how to intersect a curve with a mesh.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject gm;
      gm.SetCommandPrompt( L"Select mesh to intersect" );
      gm.SetGeometryFilter( CRhinoGetObject::mesh_object );
      gm.GetObjects( 1, 1 );
      if( gm.CommandResult() != CRhinoCommand::success )
        return gm.CommandResult();
    
      const ON_Mesh* mesh = gm.Object(0).Mesh();
      if( 0 == mesh )
        return CRhinoCommand::failure;
    
      CRhinoGetObject gc;
      gc.SetCommandPrompt( L"Select curve to intersect with mesh" );
      gc.SetGeometryFilter( CRhinoGetObject::curve_object );
      gc.EnablePreSelect( false );
      gc.EnableDeselectAllBeforePostSelect( false );
      gc.GetObjects( 1, 1 );
      if( gc.CommandResult() != CRhinoCommand::success )
        return gc.CommandResult();
    
      const ON_Curve* curve = gc.Object(0).Curve();
      if( 0 == curve )
        return CRhinoCommand::failure;
    
      double tol = context.m_doc.AbsoluteTolerance();
    
      ON_PolylineCurve pline;
      if( RhinoConvertCurveToPolyline(*curve, 0, 0, 0, 0, 0.0, tol, 0.0, 0, pline) )
      {
        const ON_MeshTree* mesh_tree = mesh->MeshTree(true);
        if( mesh_tree )
        {
          ON_SimpleArray<ON_CMX_EVENT> cmx;
          if( mesh_tree->IntersectPolyline(pline.m_pline.Count(), pline.m_pline.Array(), cmx) )
          {
            int i;
            for( i = 0; i < cmx.Count(); i++ )
              context.m_doc.AddPointObject( cmx[i].m_M[0].m_P );
            context.m_doc.Redraw();
          }
          else
          {
            RhinoApp().Print( L"Objects do not intersect.\n" );
          }
        }
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

