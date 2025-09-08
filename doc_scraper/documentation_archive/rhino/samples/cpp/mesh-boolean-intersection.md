---
url: https://developer.rhino3d.com/samples/cpp/mesh-boolean-intersection/
scraped_at: 2025-09-08T15:48:34.814967
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

Mesh Boolean Intersection

__

Windows only

Demonstrates how to intersect meshes.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      int i = 0;
    
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select first set of meshes" );
      go.SetGeometryFilter( CRhinoGetObject::mesh_object );
      go.GetObjects( 1, 0 );
      if( go.CommandResult() != CRhinoCommand::success )
        return go.CommandResult();
    
      ON_SimpleArray<const ON_Mesh*> InMeshes0( go.ObjectCount() );
      for( i = 0; i < go.ObjectCount(); i++ )
      {
        const ON_Mesh* mesh = go.Object(i).Mesh();
        if( 0 == mesh )
          return CRhinoCommand::failure;
        InMeshes0.Append( mesh );
      }
    
      go.SetCommandPrompt( L"Select second set of meshes" );
      go.EnablePreSelect( false );
      go.EnableDeselectAllBeforePostSelect( false );
      go.GetObjects( 1, 0 );
      if( go.CommandResult() != CRhinoCommand::success )
        return go.CommandResult();
    
      ON_SimpleArray<const ON_Mesh*> InMeshes1( go.ObjectCount() );
      for( i = 0; i < go.ObjectCount(); i++ )
      {
        const ON_Mesh* mesh = go.Object(i).Mesh();
        if( 0 == mesh )
          return CRhinoCommand::failure;
        InMeshes1.Append( mesh );
      }
    
      double intersection_tolerance = ON_SQRT_EPSILON * 10;
      double overlap_tolerance = ON_SQRT_EPSILON * 10;
    
      ON_SimpleArray<ON_Mesh*> OutMeshes;
      bool bSomethingHappened = false;
      bool rc = RhinoMeshBooleanIntersection(
            InMeshes0,
            InMeshes1,
            intersection_tolerance,
            overlap_tolerance,
            &bSomethingHappened,
            OutMeshes
            );
    
      if( !rc )
      {
        RhinoApp().Print( L"No mesh intersections found.\n" );
        return CRhinoCommand::nothing;
      }
    
      for( i = 0; i < OutMeshes.Count(); i++ )
      {
        CRhinoMeshObject* mesh_obj = new CRhinoMeshObject();
        mesh_obj->SetMesh( OutMeshes[i] );
    
        OutMeshes[i] = 0;
    
        if( context.m_doc.AddObject(mesh_obj) )
          mesh_obj->Select( true );
        else
          delete mesh_obj;
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

