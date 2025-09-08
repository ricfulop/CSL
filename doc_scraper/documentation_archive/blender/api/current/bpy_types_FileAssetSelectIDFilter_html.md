---
url: https://docs.blender.org/api/current/bpy.types.FileAssetSelectIDFilter.html
scraped_at: 2025-09-08T14:25:14.155548
title: FileAssetSelectIDFilter(bpy_struct)¶
---

# FileAssetSelectIDFilter(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.FileAssetSelectIDFilter(_bpy_struct_)¶

    

Which asset types to show/hide, when browsing an asset library

experimental_filter_armature¶

    

Show Armature data-blocks

Type:

    

boolean, default False

experimental_filter_cachefile¶

    

Show Cache File data-blocks

Type:

    

boolean, default False

experimental_filter_camera¶

    

Show Camera data-blocks

Type:

    

boolean, default False

experimental_filter_curve¶

    

Show Curve data-blocks

Type:

    

boolean, default False

experimental_filter_curves¶

    

Show/hide Curves data-blocks

Type:

    

boolean, default False

experimental_filter_font¶

    

Show Font data-blocks

Type:

    

boolean, default False

experimental_filter_grease_pencil¶

    

Show Grease Pencil data-blocks

Type:

    

boolean, default False

experimental_filter_image¶

    

Show Image data-blocks

Type:

    

boolean, default False

experimental_filter_lattice¶

    

Show Lattice data-blocks

Type:

    

boolean, default False

experimental_filter_light¶

    

Show Light data-blocks

Type:

    

boolean, default False

experimental_filter_light_probe¶

    

Show Light Probe data-blocks

Type:

    

boolean, default False

experimental_filter_linestyle¶

    

Show Freestyle’s Line Style data-blocks

Type:

    

boolean, default False

experimental_filter_mask¶

    

Show Mask data-blocks

Type:

    

boolean, default False

experimental_filter_mesh¶

    

Show Mesh data-blocks

Type:

    

boolean, default False

experimental_filter_metaball¶

    

Show Metaball data-blocks

Type:

    

boolean, default False

experimental_filter_movie_clip¶

    

Show Movie Clip data-blocks

Type:

    

boolean, default False

experimental_filter_paint_curve¶

    

Show Paint Curve data-blocks

Type:

    

boolean, default False

experimental_filter_palette¶

    

Show Palette data-blocks

Type:

    

boolean, default False

experimental_filter_particle_settings¶

    

Show Particle Settings data-blocks

Type:

    

boolean, default False

experimental_filter_pointcloud¶

    

Show/hide Point Cloud data-blocks

Type:

    

boolean, default False

experimental_filter_scene¶

    

Show Scene data-blocks

Type:

    

boolean, default False

experimental_filter_sound¶

    

Show Sound data-blocks

Type:

    

boolean, default False

experimental_filter_speaker¶

    

Show Speaker data-blocks

Type:

    

boolean, default False

experimental_filter_text¶

    

Show Text data-blocks

Type:

    

boolean, default False

experimental_filter_texture¶

    

Show Texture data-blocks

Type:

    

boolean, default False

experimental_filter_volume¶

    

Show/hide Volume data-blocks

Type:

    

boolean, default False

experimental_filter_work_space¶

    

Show workspace data-blocks

Type:

    

boolean, default False

filter_action¶

    

Show Action data-blocks

Type:

    

boolean, default False

filter_brush¶

    

Show Brushes data-blocks

Type:

    

boolean, default False

filter_group¶

    

Show Collection data-blocks

Type:

    

boolean, default False

filter_material¶

    

Show Material data-blocks

Type:

    

boolean, default False

filter_node_tree¶

    

Show Node Tree data-blocks

Type:

    

boolean, default False

filter_object¶

    

Show Object data-blocks

Type:

    

boolean, default False

filter_world¶

    

Show World data-blocks

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

|

  
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

|

  * [`bpy_struct.keyframe_delete`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.keyframe_delete "bpy.types.bpy_struct.keyframe_delete")
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

  
---|---  
  
## References¶

  * [`FileAssetSelectParams.filter_asset_id`](bpy.types.FileAssetSelectParams.html#bpy.types.FileAssetSelectParams.filter_asset_id "bpy.types.FileAssetSelectParams.filter_asset_id")

|

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

