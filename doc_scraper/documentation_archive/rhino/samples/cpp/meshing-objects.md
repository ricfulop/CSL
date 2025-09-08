---
url: https://developer.rhino3d.com/samples/cpp/meshing-objects/
scraped_at: 2025-09-08T15:48:35.810121
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

Meshing Objects

__

Windows only

Demonstrates how to mesh surface and polysurface objects using the
RhinoMeshObjects function.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      // Select some geometry to mesh
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select surface or polysurface to mesh" );
      go.SetGeometryFilter( CRhinoGetObject::surface_object | CRhinoGetObject::polysrf_object );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      ON_SimpleArray<const CRhinoObject*> objects;
      objects.Append( go.Object(0).Object() );
    
      // RhinoMeshObjects need to know how to mesh the objects. This information is provided
      // by passing the function a ON_MeshParameters object. For details on this class, see
      // opennurbs_mesh.h.
    
      // In this example, instead of making up our own default mesh parameters, we will just
      // get some existing ones that we know work well.
      const CRhinoAppRenderMeshSettings& rms = RhinoApp().AppSettings().RenderMeshSettings();
      //ON_MeshParameters mp = rms.QualityMeshParameters();
      ON_MeshParameters mp = rms.FastMeshParameters();
    
      // Set the user interface style.
      int ui_style = 0; // simple ui
    
      ON_ClassArray<CRhinoObjectMesh> meshes;
    
      // Mesh the selected objects.
      CRhinoCommand::result rc = RhinoMeshObjects( objects, mp, ui_style, meshes );
      if( rc == success )
      {
        int i;
        for( i = 0; i < meshes.Count(); i++ )
        {
          CRhinoObjectMesh& mesh = meshes[i];
          CRhinoMeshObject* mesh_object = new CRhinoMeshObject( mesh.m_mesh_attributes );
          mesh_object->SetMesh( mesh.m_mesh );
          mesh.m_mesh = 0;
          context.m_doc.AddObject( mesh_object );
        }
    
        context.m_doc.Redraw();
      }
    
      return rc;
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

