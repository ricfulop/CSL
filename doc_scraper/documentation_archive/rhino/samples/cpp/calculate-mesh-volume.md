---
url: https://developer.rhino3d.com/samples/cpp/calculate-mesh-volume/
scraped_at: 2025-09-08T15:48:25.655946
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

Calculate Mesh Volume

__

Windows only

Demonstrates how to calculate the volumes of mesh objects.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select solid meshes for volume calculation" );
      go.SetGeometryFilter( CRhinoGetObject::mesh_object );
      go.SetGeometryAttributeFilter( CRhinoGetObject::closed_mesh );
      go.EnableSubObjectSelect( FALSE );
      go.EnableGroupSelect();
      go.GetObjects( 1, 0 );
      if( go.CommandResult() != CRhinoCommand::success )
        return go.CommandResult();
    
      int i;
      ON_SimpleArray<const ON_Mesh*> meshes;
      for( i = 0; i < go.ObjectCount(); i++ )
      {
        const ON_Mesh* mesh = go.Object(i).Mesh();
        if( mesh )
          meshes.Append( mesh );
      }
    
      const int mesh_count = meshes.Count();
      if( 0 == mesh_count )
        return nothing;
    
      ON_BoundingBox bbox;
      for( i = 0; i < mesh_count; i++ )
        meshes[i]->GetBoundingBox( bbox, TRUE );
      ON_3dPoint base_point = bbox.Center();
    
      double total_volume = 0.0;
      double total_error_estimate = 0.0;
      for( i = 0; i < mesh_count; i++ )
      {
        double error_estimate = 0.0;
        double volume = meshes[i]->Volume( base_point, &error_estimate );
        RhinoApp().Print( L"Mesh%d = %f (+/- %f)\n", i, volume, error_estimate );
        total_volume += volume;
        total_error_estimate += error_estimate;
      }
    
      RhinoApp().Print( L"Total volume = %f (+/- %f)\n",
                        total_volume,
                        total_error_estimate );
    
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

