---
url: https://docs.blender.org/api/current/bpy.types.BrushCapabilitiesSculpt.html
scraped_at: 2025-09-08T14:21:16.179678
title: BrushCapabilitiesSculpt(bpy_struct)¶
---

# BrushCapabilitiesSculpt(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.BrushCapabilitiesSculpt(_bpy_struct_)¶

    

Read-only indications of which brush operations are supported by the current
sculpt tool

has_accumulate¶

    

Type:

    

boolean, default False, (readonly)

has_auto_smooth¶

    

Type:

    

boolean, default False, (readonly)

has_color¶

    

Type:

    

boolean, default False, (readonly)

has_direction¶

    

Type:

    

boolean, default False, (readonly)

has_dyntopo¶

    

Type:

    

boolean, default False, (readonly)

has_gravity¶

    

Type:

    

boolean, default False, (readonly)

has_height¶

    

Type:

    

boolean, default False, (readonly)

has_jitter¶

    

Type:

    

boolean, default False, (readonly)

has_normal_weight¶

    

Type:

    

boolean, default False, (readonly)

has_persistence¶

    

Type:

    

boolean, default False, (readonly)

has_pinch_factor¶

    

Type:

    

boolean, default False, (readonly)

has_plane_depth¶

    

Type:

    

boolean, default False, (readonly)

has_plane_height¶

    

Type:

    

boolean, default False, (readonly)

has_plane_offset¶

    

Type:

    

boolean, default False, (readonly)

has_rake_factor¶

    

Type:

    

boolean, default False, (readonly)

has_random_texture_angle¶

    

Type:

    

boolean, default False, (readonly)

has_sculpt_plane¶

    

Type:

    

boolean, default False, (readonly)

has_secondary_color¶

    

Type:

    

boolean, default False, (readonly)

has_smooth_stroke¶

    

Type:

    

boolean, default False, (readonly)

has_space_attenuation¶

    

Type:

    

boolean, default False, (readonly)

has_strength_pressure¶

    

Type:

    

boolean, default False, (readonly)

has_tilt¶

    

Type:

    

boolean, default False, (readonly)

has_topology_rake¶

    

Type:

    

boolean, default False, (readonly)

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

  * [`Brush.sculpt_capabilities`](bpy.types.Brush.html#bpy.types.Brush.sculpt_capabilities "bpy.types.Brush.sculpt_capabilities")

|

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

