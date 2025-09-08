---
url: https://developer.rhino3d.com/samples/cpp/mesh-boolean-difference/
scraped_at: 2025-09-08T15:48:33.810489
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

Mesh Boolean Difference

__

Windows only

Demonstrates how to use the RhinoMeshBooleanDifference function.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go0;
      go0.SetCommandPrompt( L"Select first set of meshes" );
      go0.SetGeometryFilter( CRhinoGetObject::mesh_object );
      go0.GetObjects( 1, 0 );
      if( go0.CommandResult() != success )
        return go0.CommandResult();
    
      CRhinoGetObject go1;
      go1.SetCommandPrompt( L"Select second set of meshes" );
      go1.SetGeometryFilter( CRhinoGetObject::mesh_object );
      go1.EnablePreSelect( false );
      go1.EnableDeselectAllBeforePostSelect( false );
      go1.GetObjects( 1, 0 );
      if( go1.CommandResult() != success )
        return go1.CommandResult();
    
      ON_SimpleArray<const CRhinoObject*> DeleteList( go0.ObjectCount() + go1.ObjectCount() );
      int i = 0;
    
      ON_SimpleArray<const ON_Mesh*> InMeshes0( go0.ObjectCount() );
      ON_SimpleArray<const ON_3dmObjectAttributes*> InAttributes0( go0.ObjectCount() );
      for( i = 0; i < go0.ObjectCount(); i++ )
      {
        const CRhinoObject* p = go0.Object(i).Object();
        if( !p )
          return failure;
    
        const ON_Mesh* mesh = ON_Mesh::Cast( p->Geometry() );
        if( !mesh )
          return failure;
    
        InMeshes0.Append( mesh );
        InAttributes0.Append( &p->Attributes() );
    
        DeleteList.Append( p );
      }
    
      ON_SimpleArray<const ON_Mesh*> InMeshes1( go1.ObjectCount() );
      for( i = 0; i < go1.ObjectCount(); i++ )
      {
        const CRhinoObject* p = go1.Object(i).Object();
        if( !p )
          return failure;
    
        const ON_Mesh* mesh = ON_Mesh::Cast( p->Geometry() );
        if( !mesh )
          return failure;
    
        InMeshes1.Append( mesh );
    
        DeleteList.Append( p );
      }
    
      ON_SimpleArray<ON_Mesh*> OutMeshes;
      ON_SimpleArray<const ON_3dmObjectAttributes*> OutAttributes;
      bool bResult = false;
      bool rc = RhinoMeshBooleanDifference(
            InMeshes0,
            InMeshes1,
            ON_SQRT_EPSILON*10,
            ON_SQRT_EPSILON*10,
            &bResult,
            OutMeshes,
            &InAttributes0,
            &OutAttributes
            );
    
      if( !rc )
        return failure;
    
      for( i = 0; i < OutMeshes.Count(); i++ )
      {
        CRhinoMeshObject* pMeshObj = 0;
        if( i < OutAttributes.Count() )
          pMeshObj = new CRhinoMeshObject( *OutAttributes[i] );
        else
          pMeshObj = new CRhinoMeshObject();
    
        if( pMeshObj )
        {
          pMeshObj->SetMesh( OutMeshes[i] );
          context.m_doc.AddObject( pMeshObj );
        }
        else
        {
          delete OutMeshes[i];
        }
        OutMeshes[i] = 0;
      }
    
      for( i = 0; i < DeleteList.Count(); i++ )
      {
        if( DeleteList[i] )
          context.m_doc.DeleteObject( DeleteList[i] );
      }
    
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

