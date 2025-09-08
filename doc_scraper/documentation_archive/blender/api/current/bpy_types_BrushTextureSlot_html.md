---
url: https://docs.blender.org/api/current/bpy.types.BrushTextureSlot.html
scraped_at: 2025-09-08T14:21:21.194655
title: BrushTextureSlot(TextureSlot)¶
---

# BrushTextureSlot(TextureSlot)¶  
  
base classes — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct"),
[`TextureSlot`](bpy.types.TextureSlot.html#bpy.types.TextureSlot
"bpy.types.TextureSlot")

_class _bpy.types.BrushTextureSlot(_TextureSlot_)¶

    

Texture slot for textures in a Brush data-block

angle¶

    

Brush texture rotation

Type:

    

float in [0, 6.28319], default 0.0

has_random_texture_angle¶

    

Type:

    

boolean, default False, (readonly)

has_texture_angle¶

    

Type:

    

boolean, default False, (readonly)

has_texture_angle_source¶

    

Type:

    

boolean, default False, (readonly)

map_mode¶

    

Type:

    

enum in [`VIEW_PLANE`, `AREA_PLANE`, `TILED`, `3D`, `RANDOM`, `STENCIL`],
default `VIEW_PLANE`

mask_map_mode¶

    

Type:

    

enum in [`VIEW_PLANE`, `TILED`, `RANDOM`, `STENCIL`], default `VIEW_PLANE`

random_angle¶

    

Brush texture random angle

Type:

    

float in [0, 6.28319], default 6.28319

use_rake¶

    

Type:

    

boolean, default False

use_random¶

    

Type:

    

boolean, default False

_classmethod _bl_rna_get_subclass(_id_ , _default =None_, _/_)¶

    

Parameters:

    

**id** (_str_) – The RNA type identifier.

Returns:

    

The RNA type or default when not found.

Return type:

    

[`bpy.types.Struct`](bpy.types.Struct.html#bpy.types.Struct
"bpy.types.Struct") subclass

_classmethod _bl_rna_get_subclass_py(_id_ , _default =None_, _/_)¶

    

Parameters:

    

**id** (_str_) – The RNA type identifier.

Returns:

    

The class or default when not found.

Return type:

    

type

## Inherited Properties¶

  * [`bpy_struct.id_data`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.id_data "bpy.types.bpy_struct.id_data")
  * [`TextureSlot.texture`](bpy.types.TextureSlot.html#bpy.types.TextureSlot.texture "bpy.types.TextureSlot.texture")
  * [`TextureSlot.name`](bpy.types.TextureSlot.html#bpy.types.TextureSlot.name "bpy.types.TextureSlot.name")
  * [`TextureSlot.offset`](bpy.types.TextureSlot.html#bpy.types.TextureSlot.offset "bpy.types.TextureSlot.offset")
  * [`TextureSlot.scale`](bpy.types.TextureSlot.html#bpy.types.TextureSlot.scale "bpy.types.TextureSlot.scale")

|

  * [`TextureSlot.color`](bpy.types.TextureSlot.html#bpy.types.TextureSlot.color "bpy.types.TextureSlot.color")
  * [`TextureSlot.blend_type`](bpy.types.TextureSlot.html#bpy.types.TextureSlot.blend_type "bpy.types.TextureSlot.blend_type")
  * [`TextureSlot.default_value`](bpy.types.TextureSlot.html#bpy.types.TextureSlot.default_value "bpy.types.TextureSlot.default_value")
  * [`TextureSlot.output_node`](bpy.types.TextureSlot.html#bpy.types.TextureSlot.output_node "bpy.types.TextureSlot.output_node")

  
---|---  
  
## Inherited Functions¶

  * [`bpy_struct.as_pointer`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.as_pointer "bpy.types.bpy_struct.as_pointer")
  * [`bpy_struct.driver_add`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.driver_add "bpy.types.bpy_struct.driver_add")
  * [`bpy_struct.driver_remove`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.driver_remove "bpy.types.bpy_struct.driver_remove")
  * [`bpy_struct.get`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.get "bpy.types.bpy_struct.get")
  * [`bpy_struct.id_properties_clear`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.id_properties_clear "bpy.types.bpy_struct.id_properties_clear")
  * [`bpy_struct.id_properties_ensure`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.id_properties_ensure "bpy.types.bpy_struct.id_properties_ensure")
  * [`bpy_struct.id_properties_ui`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.id_properties_ui "bpy.types.bpy_struct.id_properties_ui")
  * [`bpy_struct.is_property_hidden`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.is_property_hidden "bpy.types.bpy_struct.is_property_hidden")
  * [`bpy_struct.is_property_overridable_library`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.is_property_overridable_library "bpy.types.bpy_struct.is_property_overridable_library")
  * [`bpy_struct.is_property_readonly`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.is_property_readonly "bpy.types.bpy_struct.is_property_readonly")
  * [`bpy_struct.is_property_set`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.is_property_set "bpy.types.bpy_struct.is_property_set")
  * [`bpy_struct.items`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.items "bpy.types.bpy_struct.items")
  * [`bpy_struct.keyframe_delete`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.keyframe_delete "bpy.types.bpy_struct.keyframe_delete")

|

  * [`bpy_struct.keyframe_insert`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.keyframe_insert "bpy.types.bpy_struct.keyframe_insert")
  * [`bpy_struct.keys`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.keys "bpy.types.bpy_struct.keys")
  * [`bpy_struct.path_from_id`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.path_from_id "bpy.types.bpy_struct.path_from_id")
  * [`bpy_struct.path_resolve`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.path_resolve "bpy.types.bpy_struct.path_resolve")
  * [`bpy_struct.pop`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.pop "bpy.types.bpy_struct.pop")
  * [`bpy_struct.property_overridable_library_set`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.property_overridable_library_set "bpy.types.bpy_struct.property_overridable_library_set")
  * [`bpy_struct.property_unset`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.property_unset "bpy.types.bpy_struct.property_unset")
  * [`bpy_struct.rna_ancestors`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.rna_ancestors "bpy.types.bpy_struct.rna_ancestors")
  * [`bpy_struct.type_recast`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.type_recast "bpy.types.bpy_struct.type_recast")
  * [`bpy_struct.values`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.values "bpy.types.bpy_struct.values")
  * [`TextureSlot.bl_rna_get_subclass`](bpy.types.TextureSlot.html#bpy.types.TextureSlot.bl_rna_get_subclass "bpy.types.TextureSlot.bl_rna_get_subclass")
  * [`TextureSlot.bl_rna_get_subclass_py`](bpy.types.TextureSlot.html#bpy.types.TextureSlot.bl_rna_get_subclass_py "bpy.types.TextureSlot.bl_rna_get_subclass_py")

  
---|---  
  
## References¶

  * [`Brush.mask_texture_slot`](bpy.types.Brush.html#bpy.types.Brush.mask_texture_slot "bpy.types.Brush.mask_texture_slot")

|

  * [`Brush.texture_slot`](bpy.types.Brush.html#bpy.types.Brush.texture_slot "bpy.types.Brush.texture_slot")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

