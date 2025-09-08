---
url: https://developer.rhino3d.com/samples/cpp/synchronize-layer-render-color/
scraped_at: 2025-09-08T15:48:01.569535
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

Synchronize Layer Render Color

__

Windows only

Demonstrates how to synchronize the basic material color of a layer with the
layer's color.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
    {
      CRhinoLayerTable& layer_table = context.m_doc.m_layer_table;
      CRhinoMaterialTable& material_table = context.m_doc.m_material_table;
      int num_modified = 0;
    
      int i, layer_count = layer_table.LayerCount();
      for( i = 0; i < layer_count; i++ )
      {
        const CRhinoLayer& layer = layer_table[i];
        if( layer.IsDeleted() | layer.IsReference() )
          continue;
    
        int material_index = layer.RenderMaterialIndex();
        if( material_index < 0 )
        {
          // If material_index < 0, then the layer does not have a
          // material assigned to it. So, we will create a new material
          // that is based on Rhino's default material, and add it
          // to the material table.
    
          ON_Material material( RhinoApp().AppSettings().DefaultMaterial() );
          material_index = material_table.AddMaterial( material );
          if( material_index >= 0 )
          {
            // Now that we have added the new material,
            // assign it to the layer.
            ON_Layer new_layer( layer );
            new_layer.SetRenderMaterialIndex( material_index );
            layer_table.ModifyLayer( new_layer, layer.LayerIndex() );
          }
        }
    
        if( material_index < 0 )
          continue;
    
        const CRhinoMaterial& material = material_table[material_index];
        if( layer.Color() == material.Diffuse() )
          continue;
    
        // Modify the material's basic, or diffuse, color
        ON_Material new_material( material );
        new_material.SetDiffuse( layer.Color() );
        material_table.ModifyMaterial( new_material, material.MaterialIndex(), FALSE );
    
        num_modified++;
      }
    
      if( num_modified > 0 )
        context.m_doc.Regen();
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

