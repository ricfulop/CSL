---
url: https://developer.rhino3d.com/guides/cpp/moving-mesh-vertices/
scraped_at: 2025-09-08T15:40:02.686030
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

[Moving Mesh Vertices](https://developer.rhino3d.com/guides/cpp/moving-mesh-
vertices/)

  * Problem
  * Solution
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Moving Mesh Vertices

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You would like to modify a particular point, or vertex, of `CRhinoMeshObject`
object.

## Solution

A `CRhinoMeshObject`’s geometric data member is an `ON_Mesh` object. For
information on the `ON_Mesh` class, the _opennurbs_mesh.h_ header file.

Mesh vertices are stored on an `ON_Mesh` in an `m_V` data member, which is
simply an array of points. So, if you want to modify the vertices of a mesh,
you need to modify the data in this array.

In order to modify anything in Rhino, you might:

  1. Get the object.
  2. Make a copy of the object.
  3. Modify this copied object.
  4. Call one of the `CRhinoDoc::ReplaceObject` overrides to update the object.

## Sample

The following sample demonstrates how you might do this from a command…

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject gv;
      gv.SetCommandPrompt( L"Select mesh vertex to move" );
      gv.SetGeometryFilter( CRhinoGetObject::meshvertex_object );
      gv.GetObjects( 1, 1 );
      if( gv.CommandResult() != success )
        return gv.CommandResult();
    
      const CRhinoObject* obj = gv.Object(0).Object();
      const ON_MeshVertexRef* vertex = gv.Object(0).MeshVertex();
      if( 0 == obj | 0 == vertex )
        return failure;
    
      const ON_Mesh* mesh = vertex->m_mesh;
      if( 0 == mesh )
       return failure;
    
      ON_3dPoint pt = mesh->m_V[vertex->m_mesh_vi];
    
      CRhinoGetPoint gp;
      gp.SetCommandPrompt( L"New location" );
      gp.SetBasePoint( pt );
      gp.DrawLineFromPoint( pt, TRUE );
      gp.GetPoint();
      if( gp.CommandResult() != success )
        return gp.CommandResult();
    
      ON_Mesh dupe_mesh( *mesh );
      dupe_mesh.SetVertex( vertex->m_mesh_vi, gp.Point() );
    
      // Since we've modified ON_Mesh.m_V array,
      // we need to invalidate a few things so they
      // can be recalculated based on the new data.
      dupe_mesh.InvalidateVertexBoundingBox();
      dupe_mesh.InvalidateVertexNormalBoundingBox();
      dupe_mesh.InvalidateCurvatureStats();
      dupe_mesh.m_FN.SetCount(0);
      dupe_mesh.m_N.SetCount(0);
      dupe_mesh.ComputeFaceNormals();
      dupe_mesh.ComputeVertexNormals();
      dupe_mesh.SetClosed(-1);
    
      if( dupe_mesh.IsValid() )
      {
        context.m_doc.ReplaceObject( CRhinoObjRef(obj), dupe_mesh );
        context.m_doc.Redraw();
      }
    
      return success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/moving-
mesh-vertices/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/moving-
mesh-vertices/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

