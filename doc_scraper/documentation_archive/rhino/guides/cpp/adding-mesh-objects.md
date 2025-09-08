---
url: https://developer.rhino3d.com/guides/cpp/adding-mesh-objects/
scraped_at: 2025-09-08T15:38:40.371793
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

[Adding Mesh Objects](https://developer.rhino3d.com/guides/cpp/adding-mesh-
objects/)

  * Overview
  * Example

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Adding Mesh Objects

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

To create an `ON_Mesh`:

  1. Create the `ON_Mesh` object. The constructor requires the number of faces and vertices, and whether or not you have vertex normals or texture coordinates.
  2. Fill in the mesh vertex array, `ON_Mesh::m_V`. You can also use `ON_Mesh::SetVertex`.
  3. Fill in the mesh faces array, `ON_Mesh::m_F`. You can also use `ON_Mesh::SetTriangle` and `ON_Mesh::SetQuad`.
  4. If you have vertex normals, fill in the normals array, `ON_Mesh::m_N`. You can also use `ON_Mesh::SetVertexNormal`.
  5. If you have texture coordinates, fill in the texture coordinate array, `ON_Mesh::m_T`. You can also use `ON_Mesh::SetTextureCoordinate`.
  6. If you did not specify vertex normals, have Rhino compute them for you using `ON_Mesh::ComputeVertexNormals()`.
  7. Clean up everything using `ON_Mesh::Compact`.

You are now ready to add this mesh object to the document. The
_opennurbs_mesh.h_ header file is well documented. It’s worth reading through
at least once.

## Example

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      // Example demonstrates how to create a mesh and add it to Rhino
    
      // Create a mesh to write.
      // The mesh is a pyramid with 4 triangular sides and a quadranglar
      // base.  The mesh has 5 vertices and 5 faces.  
      // The side faces share normals at their common vertices.  The
      // quadrangular base has normals different from the side normal.
      // Coincident vertices that have distinct normals must be
      // duplicated in the vertex list.
      //
      // The apex will be at (1,1.5,4) with normal (0,0,1).
      // The base corners will be at (0,0,0), (0,2,0), (2,3,0), (0,3,0).
    
      bool bHasVertexNormals = true; // we will specify vertex normals
      bool bHasTexCoords = false;    // we will not specify texture coordinates
      const int vertex_count = 5+4;  // 4 duplicates for different base normals
      const int face_count = 5;      // 4 triangle sides and a quad base
      ON_Mesh mesh( face_count, vertex_count, bHasVertexNormals, bHasTexCoords );
    
      // The SetVertex(), SetNormal(), SetTCoord() and SetFace() functions
      // return true if successful and false if input is illegal.  It is
      // a good idea to inspect this returned value.
    
      // vertex #0: apex location and normal
      mesh.SetVertex( 0, ON_3dPoint(1.0,  1.5,  5.0) );
      mesh.SetVertexNormal( 0, ON_3dVector(0.0,  0.0,  1.0) );
    
      // vertex #1: SW corner vertex for sides
      mesh.SetVertex( 1, ON_3dPoint(0.0,  0.0,  0.0) );
      mesh.SetVertexNormal( 1, ON_3dVector(-1.0, -1.0,  0.0) ); // set normal will unitize if needed
    
      // vertex #2: SE corner vertex for sides
      mesh.SetVertex( 2, ON_3dPoint(2.0,  0.0,  0.0) );
      mesh.SetVertexNormal( 2, ON_3dVector(+1.0, -1.0,  0.0) );
    
      // vertex #3: NE corner vertex for sides
      mesh.SetVertex( 3, ON_3dPoint(2.0,  3.0,  0.0) );
      mesh.SetVertexNormal( 3, ON_3dVector(+1.0, +1.0,  0.0) );
    
      // vertex #4: NW corner vertex for sides
      mesh.SetVertex( 4, ON_3dPoint(0.0,  3.0,  0.0) );
      mesh.SetVertexNormal( 4, ON_3dVector(-1.0, +1.0,  0.0) );
    
      // vertex #5: SW corner vertex for base
      mesh.SetVertex( 5, ON_3dPoint(0.0,  0.0,  0.0) ); // == location of v1
      mesh.SetVertexNormal( 5, ON_3dVector(0.0,  0.0, -1.0) );
    
      // vertex #6: SE corner vertex for base
      mesh.SetVertex( 6, ON_3dPoint(2.0,  0.0,  0.0) ); // == location of v2
      mesh.SetVertexNormal( 6, ON_3dVector(0.0,  0.0, -1.0) );
    
      // vertex #7: SW corner vertex for base
      mesh.SetVertex( 7, ON_3dPoint(2.0,  3.0,  0.0) ); // == location of v3
      mesh.SetVertexNormal( 7, ON_3dVector(0.0,  0.0, -1.0) );
    
      // vertex #8: SW corner vertex for base
      mesh.SetVertex( 8, ON_3dPoint(0.0,  3.0,  0.0) ); // == location of v4
      mesh.SetVertexNormal( 8, ON_3dVector(0.0,  0.0, -1.0) );
    
      // Faces have vertices ordered counter-clockwise
    
      // South side triangle
      mesh.SetTriangle( 0, 1, 2, 0 );
    
      // East side triangle
      mesh.SetTriangle( 1, 2, 3, 0 );
    
      // North side triangle
      mesh.SetTriangle( 2, 3, 4, 0 );
    
      // West side triangle
      mesh.SetTriangle( 3, 4, 1, 0 );
    
      // last face is quadrangular base
      mesh.SetQuad( 4, 5, 8, 7, 6 );
    
      //////////////////////////////////////////////////////////////
      //////////////////////////////////////////////////////////////
    
      if( mesh.IsValid() )
      {
        // Most applications expect vertex normals.
        // If they are not present, ComputeVertexNormals sets
        // them by averaging face normals.
        if ( !mesh.HasVertexNormals() )
          mesh.ComputeVertexNormals();
    
        context.m_doc.AddMeshObject( mesh );
        context.m_doc.Redraw();
      }
    
      return success;
    }
    

Here is another example:

    
    
    CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
    {
      int face_count = 6;
      int vertex_count = 12;
      BOOL bVertexNormals = FALSE;
      BOOL bTextureCoordinates = FALSE;
    
      ON_Mesh mesh( face_count, vertex_count, bVertexNormals, bTextureCoordinates );
      mesh.SetVertex(  0, ON_3fPoint(0.0f, 0.0f, 1.0f) );
      mesh.SetVertex(  1, ON_3fPoint(1.0f, 0.0f, 1.0f) );
      mesh.SetVertex(  2, ON_3fPoint(2.0f, 0.0f, 1.0f) );
      mesh.SetVertex(  3, ON_3fPoint(3.0f, 0.0f, 0.0f) );
      mesh.SetVertex(  4, ON_3fPoint(0.0f, 1.0f, 1.0f) );
      mesh.SetVertex(  5, ON_3fPoint(1.0f, 1.0f, 2.0f) );
      mesh.SetVertex(  6, ON_3fPoint(2.0f, 1.0f, 1.0f) );
      mesh.SetVertex(  7, ON_3fPoint(3.0f, 1.0f, 0.0f) );
      mesh.SetVertex(  8, ON_3fPoint(0.0f, 2.0f, 1.0f) );
      mesh.SetVertex(  9, ON_3fPoint(1.0f, 2.0f, 1.0f) );
      mesh.SetVertex( 10, ON_3fPoint(2.0f, 2.0f, 1.0f) );
      mesh.SetVertex( 11, ON_3fPoint(3.0f, 2.0f, 1.0f) );
      mesh.SetQuad( 0, 0, 1,  5,  4 );
      mesh.SetQuad( 1, 1, 2,  6,  5 );
      mesh.SetQuad( 2, 2, 3,  7,  6 );
      mesh.SetQuad( 3, 4, 5,  9,  8 );
      mesh.SetQuad( 4, 5, 6, 10,  9 );
      mesh.SetQuad( 5, 6, 7, 11, 10 );
      mesh.ComputeVertexNormals();
      mesh.Compact();
    
      context.m_doc.AddMeshObject( mesh );
      context.m_doc.Redraw();
      return CRhinoCommand::success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/adding-
mesh-objects/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/adding-
mesh-objects/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

