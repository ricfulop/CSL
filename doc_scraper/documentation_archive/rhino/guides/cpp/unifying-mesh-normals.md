---
url: https://developer.rhino3d.com/guides/cpp/unifying-mesh-normals/
scraped_at: 2025-09-08T15:40:19.767100
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

[Unifying Mesh Normals](https://developer.rhino3d.com/guides/cpp/unifying-
mesh-normals/)

  * Problem
  * Solution
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Unifying Mesh Normals

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You have found that `RhinoUnifyMeshNormals` C/C++ functions seems to behave
differently than the _UnifyMeshNormals_ command. How can one achieve the same
functionality in a plugin?

## Solution

In addition to calling the `RhinoUnifyMeshNormals` function, the
_UnifyMeshNormals_ command also recomputes the mesh’s vertex normals, based on
the new face normals, using `ON_Mesh::ComputeVertexNormals`.

## Sample

The following sample demonstrates this.

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select mesh to unify normals" );
      go.SetGeometryFilter( CRhinoGetObject::mesh_object );
      go.GetObjects( 1, 1 );
      CRhinoCommand::result rc = go.CommandResult();
      if( rc != CRhinoCommand::success )
        return rc;
    
      const CRhinoObjRef ref = go.Object(0);
      const ON_Mesh* mesh = ref.Mesh();
      if( 0 == mesh )
        return CRhinoCommand::failure;
    
      int count = 0;
      ON_Mesh* new_mesh = RhinoUnifyMeshNormals( *mesh, 0, false, &count );
      if( new_mesh && new_mesh->IsValid() )
      {
        new_mesh->ComputeVertexNormals();
    
        CRhinoMeshObject* new_obj = new CRhinoMeshObject();
        new_obj->SetMesh( new_mesh );
    
        context.m_doc.ReplaceObject( ref, new_obj );
        context.m_doc.Redraw();
    
        RhinoApp().Print( L"Reversed the orientation of %d faces.\n", count );
        rc = CRhinoCommand::success;
      }
      else
      {
        if( 0 != count )
        {
          RhinoApp().Print( L"Unable to unify mesh normals.\n" );
          rc = CRhinoCommand::failure;
        }
        else
        {
          RhinoApp().Print( L"All face normals are already oriented in the same direction.\n" );
          rc = CRhinoCommand::nothing;
        }
      }
    
      return rc;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/unifying-
mesh-normals/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/unifying-
mesh-normals/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

