---
url: https://developer.rhino3d.com/samples/cpp/get-brep-face-vertices/
scraped_at: 2025-09-08T15:48:30.819164
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

Get Brep Face Vertices

__

Windows only

Demonstrates how to get the vertices of a Brep face.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select surface" );
      go.SetGeometryFilter( CRhinoGetObject::surface_object );
      go.EnableSubObjectSelect();
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != CRhinoCommand::success )
        return go.CommandResult();
    
      const ON_BrepFace* face = go.Object(0).Face();
      if( 0 == face )
        return CRhinoCommand::failure;
    
      const ON_Brep* brep = face->Brep();
      if( 0 == brep )
        return CRhinoCommand::failure;
    
      ON_SimpleArray<int> vertices;
      int i = 0;
    
      const ON_BrepLoop* loop = face->OuterLoop();
      if( loop )
      {
        for( i = 0; i < loop->TrimCount(); i++ )
        {
          const ON_BrepTrim* trim = loop->Trim( i );
          if( trim )
          {
            const ON_BrepVertex* vertex = trim->Vertex( 0 );
            if( vertex )
              vertices.Append( vertex->m_vertex_index );
            vertex = trim->Vertex( 1 );
            if( vertex )
              vertices.Append( vertex->m_vertex_index );
          }
        }
      }
    
      if( 0 == vertices.Count() )
        return CRhinoCommand::failure;
    
      // sort
      vertices.QuickSort( &ON_CompareIncreasing<int> );
    
      // cull
      int vi = -1;
      for( i = vertices.Count() - 1; i >= 0; i-- )
      {
        if( vertices[i] == vi )
          vertices.Remove(i);
        else
          vi = vertices[i];
      }
    
      // Add
      for( i = 0; i < vertices.Count(); i++ )
        context.m_doc.AddPointObject( brep->m_V[vertices[i]].Point() );
    
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

