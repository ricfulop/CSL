---
url: https://developer.rhino3d.com/samples/cpp/calculate-solid-volumes/
scraped_at: 2025-09-08T15:48:04.690257
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

Calculate Solid Volumes

__

Windows only

Demonstrates how to calculating the volumes of closed surface, polysurface,
and mesh objects.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select solids for volume calculation" );
      go.SetGeometryFilter(
            CRhinoGetObject::surface_object |
            CRhinoGetObject::polysrf_object |
            CRhinoGetObject::mesh_object
            );
      go.SetGeometryAttributeFilter(
            CRhinoGetObject::closed_surface |
            CRhinoGetObject::closed_polysrf |
            CRhinoGetObject::closed_mesh
            );
      go.EnableSubObjectSelect( false );
      go.EnableGroupSelect( true );
      go.GetObjects( 1, 0 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      ON_SimpleArray<const ON_Geometry*> geom( go.ObjectCount() );
      int i;
      for( i = 0; i < go.ObjectCount(); i++ )
      {
        const ON_Geometry* geo = go.Object(i).Geometry();
        if( 0 == geo )
          return failure;
        geom.Append( geo );
      }
    
      // Get bounding box of all objects
      ON_BoundingBox bbox;
      for( i = 0; i < geom.Count(); i++ )
        geom[i]->GetBoundingBox( bbox, bbox.IsValid() );
    
      ON_3dPoint base_point = bbox.Center();
    
      ON_SimpleArray<ON_MassProperties> MassProp;
      MassProp.Reserve( geom.Count() );
    
      for( i = 0; i < geom.Count(); i++ )
      {
        ON_MassProperties* mp = &MassProp.AppendNew();
    
        if( const ON_Surface* srf = ON_Surface::Cast(geom[i]) )
          srf->VolumeMassProperties( *mp, true, false, false, false, base_point );       
    
        else if( const ON_Brep* brep = ON_Brep::Cast(geom[i]) )
          brep->VolumeMassProperties( *mp, true, false, false, false, base_point );
    
        else if( const ON_Mesh* mesh = ON_Mesh::Cast(geom[i]) )
          mesh->VolumeMassProperties( *mp, true, false, false, false, base_point );
      }
    
      ON_MassProperties results;
      results.Sum( MassProp.Count(), MassProp.Array() );
      RhinoApp().Print( L"Volume = %g\n", results.Volume() );
    
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

