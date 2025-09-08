---
url: https://docs.blender.org/api/current/bpy.types.CurvesSculpt.html
scraped_at: 2025-09-08T14:24:26.929957
title: CurvesSculpt(Paint)¶
---

# CurvesSculpt(Paint)¶  
  
base classes — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct"), [`Paint`](bpy.types.Paint.html#bpy.types.Paint
"bpy.types.Paint")

_class _bpy.types.CurvesSculpt(_Paint_)¶

    

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
  * [`Paint.brush`](bpy.types.Paint.html#bpy.types.Paint.brush "bpy.types.Paint.brush")
  * [`Paint.brush_asset_reference`](bpy.types.Paint.html#bpy.types.Paint.brush_asset_reference "bpy.types.Paint.brush_asset_reference")
  * [`Paint.eraser_brush`](bpy.types.Paint.html#bpy.types.Paint.eraser_brush "bpy.types.Paint.eraser_brush")
  * [`Paint.eraser_brush_asset_reference`](bpy.types.Paint.html#bpy.types.Paint.eraser_brush_asset_reference "bpy.types.Paint.eraser_brush_asset_reference")
  * [`Paint.palette`](bpy.types.Paint.html#bpy.types.Paint.palette "bpy.types.Paint.palette")
  * [`Paint.show_brush`](bpy.types.Paint.html#bpy.types.Paint.show_brush "bpy.types.Paint.show_brush")
  * [`Paint.show_brush_on_surface`](bpy.types.Paint.html#bpy.types.Paint.show_brush_on_surface "bpy.types.Paint.show_brush_on_surface")
  * [`Paint.show_low_resolution`](bpy.types.Paint.html#bpy.types.Paint.show_low_resolution "bpy.types.Paint.show_low_resolution")
  * [`Paint.use_sculpt_delay_updates`](bpy.types.Paint.html#bpy.types.Paint.use_sculpt_delay_updates "bpy.types.Paint.use_sculpt_delay_updates")

|

  * [`Paint.use_symmetry_x`](bpy.types.Paint.html#bpy.types.Paint.use_symmetry_x "bpy.types.Paint.use_symmetry_x")
  * [`Paint.use_symmetry_y`](bpy.types.Paint.html#bpy.types.Paint.use_symmetry_y "bpy.types.Paint.use_symmetry_y")
  * [`Paint.use_symmetry_z`](bpy.types.Paint.html#bpy.types.Paint.use_symmetry_z "bpy.types.Paint.use_symmetry_z")
  * [`Paint.use_symmetry_feather`](bpy.types.Paint.html#bpy.types.Paint.use_symmetry_feather "bpy.types.Paint.use_symmetry_feather")
  * [`Paint.cavity_curve`](bpy.types.Paint.html#bpy.types.Paint.cavity_curve "bpy.types.Paint.cavity_curve")
  * [`Paint.use_cavity`](bpy.types.Paint.html#bpy.types.Paint.use_cavity "bpy.types.Paint.use_cavity")
  * [`Paint.tile_offset`](bpy.types.Paint.html#bpy.types.Paint.tile_offset "bpy.types.Paint.tile_offset")
  * [`Paint.tile_x`](bpy.types.Paint.html#bpy.types.Paint.tile_x "bpy.types.Paint.tile_x")
  * [`Paint.tile_y`](bpy.types.Paint.html#bpy.types.Paint.tile_y "bpy.types.Paint.tile_y")
  * [`Paint.tile_z`](bpy.types.Paint.html#bpy.types.Paint.tile_z "bpy.types.Paint.tile_z")

  
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
  * [`Paint.bl_rna_get_subclass`](bpy.types.Paint.html#bpy.types.Paint.bl_rna_get_subclass "bpy.types.Paint.bl_rna_get_subclass")
  * [`Paint.bl_rna_get_subclass_py`](bpy.types.Paint.html#bpy.types.Paint.bl_rna_get_subclass_py "bpy.types.Paint.bl_rna_get_subclass_py")

  
---|---  
  
## References¶

  * [`ToolSettings.curves_sculpt`](bpy.types.ToolSettings.html#bpy.types.ToolSettings.curves_sculpt "bpy.types.ToolSettings.curves_sculpt")

|

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

