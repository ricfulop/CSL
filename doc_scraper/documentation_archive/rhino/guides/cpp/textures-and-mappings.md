---
url: https://developer.rhino3d.com/guides/cpp/textures-and-mappings/
scraped_at: 2025-09-08T15:40:41.876226
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

[Textures and Mappings](https://developer.rhino3d.com/guides/cpp/textures-and-
mappings/)

  * Overview
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Textures and Mappings

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) and [Jussi
Aaltonen](https://discourse.mcneel.com/u/Jussi_Aaltonen/) (Last updated:
Monday, October 7, 2024)

## Overview

Broadly speaking, there are six concepts that are important to understand when
dealing with materials, textures, and mappings:

  * **Texture Bitmap** : A bitmap image, usually saved in a file.
  * **Texture Coordinates** : In Rhino these are 2d and 3d points that are saved in an `ON_Mesh` in the `m_T[]` or `m_TC[]` arrays. They should always be set by a texture mapping and never modified directly.
  * **Texture Mapping** : A function that sets texture coordinates. Persistent texture mappings are stored in `CRhinoDoc::m_texture_mapping_table[]`.
  * **Surface parameters** : A set of 2d points stored in an `ON_Mesh` in the `m_S[]` array. They are used by the surface parameter mapping.
  * **Render Material** : A collection of rendering color and shading information, including the names of texture bitmaps. Rendering materials are stored in `CRhinoDoc::m_material_table[]`.
  * **Object Attributes** : Attributes of a Rhino object, including the rendering materials and texture mappings the object uses, are stored in the `CRhinoObjectAttributes` class returned by `CRhinoObject::Attributes()`.

## Sample

The following sample creates a material with a bitmap texture, then modifies a
mesh object’s attributes, sets up surface parameters and applies a surface
parameter mapping so the bitmap is projected onto the mesh along the world Z
axis…

    
    
      CRhinoDoc* pDoc = context.Document();
      if (nullptr == pDoc)
        return CRhinoCommand::failure;
      CRhinoDoc& doc = *pDoc;
    
      // Id of the currently active render plug-in
      const UUID renderPlugInId = RhinoApp().CurrentRenderPlugIn()->PlugInID();
    
      // Create a material with a texture bitmap
      ON_Texture tex;
      tex.m_image_file_reference.SetFullPath(L"C:/my-texture-folder/sample-texture.bmp", true);
      tex.m_bOn = true;
      tex.m_type = ON_Texture::TYPE::bitmap_texture;
      tex.m_mode = ON_Texture::MODE::modulate_texture;
      tex.m_mapping_channel_id = 1;
    
      ON_Material mat;
      mat.m_diffuse.SetRGB(150, 0, 0);
      mat.m_specular.SetRGB(200, 200, 200);
      mat.m_shine = 0.5 * ON_Material::MaxShine;
      mat.AddTexture(tex);
    
      int mat_index = doc.m_material_table.AddMaterial(mat);
      if (mat_index < 0)
        return CRhinoCommand::failure;
    
      // Select a mesh to modify
      CRhinoGetObject go;
      go.SetGeometryFilter(ON::mesh_object);
      go.SetCommandPrompt(L"Select a mesh");
      go.GetObjects(1, 1);
      if (CRhinoCommand::success != go.CommandResult())
        return go.CommandResult();
      const CRhinoMeshObject* mesh0_object =
        CRhinoMeshObject::Cast(go.Object(0).Object());
      if (0 == mesh0_object)
        return CRhinoCommand::failure;
      const ON_Mesh* mesh0 = mesh0_object->Mesh();
      if (0 == mesh0)
        return CRhinoCommand::failure;
    
      // Copy the mesh
      ON_Mesh* mesh1 = new ON_Mesh(*mesh0);
      ON_BoundingBox bbox = mesh1->BoundingBox();
      ON_Interval x_extents(bbox.m_min.x, bbox.m_max.x);
      ON_Interval y_extents(bbox.m_min.y, bbox.m_max.y);
    
      // Set up surface parameters.
      // They will be used by a surface parameter mapping.
      const int vertex_count = mesh1->m_V.Count();
      mesh1->m_S.Reserve(vertex_count);
      mesh1->m_S.SetCount(0);
      for (int vi = 0; vi < vertex_count; vi++)
      {
        const ON_3dPoint& V = mesh0->m_V[vi];
        ON_2dPoint& tc = mesh1->m_S.AppendNew();
        tc.x = (float)x_extents.NormalizedParameterAt(V.x);
        tc.y = (float)y_extents.NormalizedParameterAt(V.y);
      }
    
      // Adjust surface packing settings so that surface parameter
      // mapping will create vertex coordinates 1-to-1 with the
      // surface parameters.
      mesh1->m_srf_domain[0].Set(0.0, 1.0);
      mesh1->m_srf_domain[1].Set(0.0, 1.0);
      mesh1->m_srf_scale[0] = 0.0;
      mesh1->m_srf_scale[1] = 0.0;
      mesh1->m_packed_tex_domain[0].Set(0.0, 1.0);
      mesh1->m_packed_tex_domain[1].Set(0.0, 1.0);
      mesh1->m_packed_tex_rotate = false;
    
      // Update the mesh
      CRhinoMeshObject* mesh1_object = new CRhinoMeshObject();
      mesh1_object->SetMesh(mesh1);
      doc.ReplaceObject(CRhinoObjRef(mesh0_object), mesh1_object);
    
      // Make a copy of the object attributes in order to apply some changes
      ON_3dmObjectAttributes att = mesh1_object->Attributes();
    
      // Update the object to use the new material
      att.m_material_index = mat_index;
      att.SetMaterialSource(ON::material_from_object);
    
      // Add new texture mapping to the document texture mapping table
      const int textureMappingIndex = doc.m_texture_mapping_table.AddTextureMapping(ON_TextureMapping::SurfaceParameterTextureMapping);
      // Look up the mapping id of the newly added texture mapping
      const UUID textureMappingId = doc.m_texture_mapping_table[textureMappingIndex].Id();
      // Remove all texture mappings from the object attributes
      att.m_rendering_attributes.m_mappings.Destroy();
      // Add the newly added texture mapping on the mapping channel that the texture uses
      att.m_rendering_attributes.AddMappingChannel(renderPlugInId, tex.m_mapping_channel_id, textureMappingId);
    
      // Apply the modified attributes to the mesh object
      doc.ModifyObjectAttributes(CRhinoObjRef(mesh1_object), att);
    
      doc.Redraw();
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/textures-
and-mappings/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/textures-
and-mappings/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

