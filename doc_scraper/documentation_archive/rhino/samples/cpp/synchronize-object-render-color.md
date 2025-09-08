---
url: https://developer.rhino3d.com/samples/cpp/synchronize-object-render-color/
scraped_at: 2025-09-08T15:48:45.873326
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

Synchronize Object Render Color

__

Windows only

Demonstrates how to synchronize the basic material color of an object with the
object's display color.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      int num_modified = 0;
      CRhinoObjectIterator it( CRhinoObjectIterator::normal_objects,
                               CRhinoObjectIterator::active_objects );
      it.IncludeLights( FALSE );
    
      CRhinoObject* obj = 0;
      for( obj = it.First(); obj; obj = it.Next() )
      {
        // If the object gets its color from its layer, then we will
        // let the layer handle its material color as well.
        ON::object-color_source color_source = obj->Attributes().ColorSource();
        if( color_source != ON::color_from_object )
          continue;
    
        int material_index = obj->Attributes().m_material_index;
        if( material_index < 0 )
        {
          // If material_index < 0, then the object does not have a
          // material assigned to it. So, we will create a new material
          // that is based on Rhino's default material, and add it
          // to the material table.
          ON_Material material( RhinoApp().AppSettings().DefaultMaterial() );
          material_index = context.m_doc.m_material_table.AddMaterial( material );
          if( material_index >= 0 )
          {
            // Now that we have added the new material,
            // assign it to the object.
            CRhinoObjectAttributes new_attributes( obj->Attributes() );
            new_attributes.m_material_index = material_index;
            // Make sure to set the material source to "from object"
            new_attributes.SetMaterialSource( ON::material_from_object );
            obj->ModifyAttributes( new_attributes );
          }
        }
        if( material_index < 0 )
          continue;
    
        const CRhinoMaterial& material = context.m_doc.m_material_table[material_index];
        if( obj->Attributes().DrawColor() == material.Diffuse() )
          continue;
    
        // Modify the material's basic,or diffuse, color
        ON_Material new_material( material );
        new_material.SetDiffuse( obj->Attributes().DrawColor() );
        context.m_doc.m_material_table.ModifyMaterial( new_material,
                                                       material.MaterialIndex(),
                                                       FALSE );
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

