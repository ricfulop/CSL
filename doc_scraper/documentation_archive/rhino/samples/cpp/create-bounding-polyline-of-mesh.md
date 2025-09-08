---
url: https://developer.rhino3d.com/samples/cpp/create-bounding-polyline-of-mesh/
scraped_at: 2025-09-08T15:47:46.622708
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

Create Bounding Polyline of a Mesh

__

Windows only

Demonstrates how to create a bounding polyline of a mesh object.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      // Select an open mesh object
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select open mesh" );
      go.SetGeometryFilter( CRhinoGetObject::mesh_object );
      go.SetGeometryAttributeFilter( CRhinoGetObject::open_mesh );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      // Validate the selection
      const CRhinoObjRef& ref = go.Object(0);
      const ON_Mesh* mesh = ref.Mesh();
      if( 0 == mesh  )
        return failure;
    
      // Get the mesh's topology
      const ON_MeshTopology& mesh_top = mesh->Topology();
      ON_SimpleArray<const ON_Curve*> lines( mesh_top.m_tope.Count() );
    
      // Find all of the mesh edges that have only a single mesh face
      int i;
      for( i = 0; i < mesh_top.m_tope.Count(); i++ )
      {
        const ON_MeshTopologyEdge& mesh_edge = mesh_top.m_tope[i];
        if( mesh_edge.m_topf_count == 1 )
        {
          ON_3fPoint p0 = mesh_top.TopVertexPoint( mesh_edge.m_topvi[0] );
          ON_3fPoint p1 = mesh_top.TopVertexPoint( mesh_edge.m_topvi[1] );
          ON_LineCurve* line = new ON_LineCurve( ON_3dPoint(p0), ON_3dPoint(p1) );
          lines.Append( line );
        }
      }
    
      ON_SimpleArray<ON_Curve*> output;
      double tolerance = 2.1 * context.m_doc.AbsoluteTolerance();
    
      // Join all of the line segments
      if( RhinoMergeCurves(lines, output, tolerance) )
      {
        for( i = 0; i < output.Count(); i++ )
        {
          CRhinoCurveObject* crv = new CRhinoCurveObject;
          crv->SetCurve( output[i] );
          if( context.m_doc.AddObject(crv) )
            crv->Select();
          else
            delete crv;
        }
      }
    
      // Clean up so we don't leak memory
      for( i = 0; i < lines.Count(); i++ )
        delete lines[i];
    
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

