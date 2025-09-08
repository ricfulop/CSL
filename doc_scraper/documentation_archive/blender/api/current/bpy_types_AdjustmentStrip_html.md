---
url: https://docs.blender.org/api/current/bpy.types.AdjustmentStrip.html
scraped_at: 2025-09-08T14:19:30.788672
title: AdjustmentStrip(EffectStrip)¶
---

# AdjustmentStrip(EffectStrip)¶  
  
base classes — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct"), [`Strip`](bpy.types.Strip.html#bpy.types.Strip
"bpy.types.Strip"),
[`EffectStrip`](bpy.types.EffectStrip.html#bpy.types.EffectStrip
"bpy.types.EffectStrip")

_class _bpy.types.AdjustmentStrip(_EffectStrip_)¶

    

Sequence strip to perform filter adjustments to layers below

animation_offset_end¶

    

Animation end offset (trim end)

Type:

    

int in [0, inf], default 0

animation_offset_start¶

    

Animation start offset (trim start)

Type:

    

int in [0, inf], default 0

input_count¶

    

Type:

    

int in [0, inf], default 0, (readonly)

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
  * [`Strip.name`](bpy.types.Strip.html#bpy.types.Strip.name "bpy.types.Strip.name")
  * [`Strip.type`](bpy.types.Strip.html#bpy.types.Strip.type "bpy.types.Strip.type")
  * [`Strip.select`](bpy.types.Strip.html#bpy.types.Strip.select "bpy.types.Strip.select")
  * [`Strip.select_left_handle`](bpy.types.Strip.html#bpy.types.Strip.select_left_handle "bpy.types.Strip.select_left_handle")
  * [`Strip.select_right_handle`](bpy.types.Strip.html#bpy.types.Strip.select_right_handle "bpy.types.Strip.select_right_handle")
  * [`Strip.mute`](bpy.types.Strip.html#bpy.types.Strip.mute "bpy.types.Strip.mute")
  * [`Strip.lock`](bpy.types.Strip.html#bpy.types.Strip.lock "bpy.types.Strip.lock")
  * [`Strip.frame_final_duration`](bpy.types.Strip.html#bpy.types.Strip.frame_final_duration "bpy.types.Strip.frame_final_duration")
  * [`Strip.frame_duration`](bpy.types.Strip.html#bpy.types.Strip.frame_duration "bpy.types.Strip.frame_duration")
  * [`Strip.frame_start`](bpy.types.Strip.html#bpy.types.Strip.frame_start "bpy.types.Strip.frame_start")
  * [`Strip.frame_final_start`](bpy.types.Strip.html#bpy.types.Strip.frame_final_start "bpy.types.Strip.frame_final_start")
  * [`Strip.frame_final_end`](bpy.types.Strip.html#bpy.types.Strip.frame_final_end "bpy.types.Strip.frame_final_end")
  * [`Strip.frame_offset_start`](bpy.types.Strip.html#bpy.types.Strip.frame_offset_start "bpy.types.Strip.frame_offset_start")
  * [`Strip.frame_offset_end`](bpy.types.Strip.html#bpy.types.Strip.frame_offset_end "bpy.types.Strip.frame_offset_end")
  * [`Strip.channel`](bpy.types.Strip.html#bpy.types.Strip.channel "bpy.types.Strip.channel")
  * [`Strip.use_linear_modifiers`](bpy.types.Strip.html#bpy.types.Strip.use_linear_modifiers "bpy.types.Strip.use_linear_modifiers")
  * [`Strip.blend_type`](bpy.types.Strip.html#bpy.types.Strip.blend_type "bpy.types.Strip.blend_type")
  * [`Strip.blend_alpha`](bpy.types.Strip.html#bpy.types.Strip.blend_alpha "bpy.types.Strip.blend_alpha")

|

  * [`Strip.effect_fader`](bpy.types.Strip.html#bpy.types.Strip.effect_fader "bpy.types.Strip.effect_fader")
  * [`Strip.use_default_fade`](bpy.types.Strip.html#bpy.types.Strip.use_default_fade "bpy.types.Strip.use_default_fade")
  * [`Strip.color_tag`](bpy.types.Strip.html#bpy.types.Strip.color_tag "bpy.types.Strip.color_tag")
  * [`Strip.modifiers`](bpy.types.Strip.html#bpy.types.Strip.modifiers "bpy.types.Strip.modifiers")
  * [`Strip.show_retiming_keys`](bpy.types.Strip.html#bpy.types.Strip.show_retiming_keys "bpy.types.Strip.show_retiming_keys")
  * [`EffectStrip.use_deinterlace`](bpy.types.EffectStrip.html#bpy.types.EffectStrip.use_deinterlace "bpy.types.EffectStrip.use_deinterlace")
  * [`EffectStrip.alpha_mode`](bpy.types.EffectStrip.html#bpy.types.EffectStrip.alpha_mode "bpy.types.EffectStrip.alpha_mode")
  * [`EffectStrip.use_flip_x`](bpy.types.EffectStrip.html#bpy.types.EffectStrip.use_flip_x "bpy.types.EffectStrip.use_flip_x")
  * [`EffectStrip.use_flip_y`](bpy.types.EffectStrip.html#bpy.types.EffectStrip.use_flip_y "bpy.types.EffectStrip.use_flip_y")
  * [`EffectStrip.use_float`](bpy.types.EffectStrip.html#bpy.types.EffectStrip.use_float "bpy.types.EffectStrip.use_float")
  * [`EffectStrip.use_reverse_frames`](bpy.types.EffectStrip.html#bpy.types.EffectStrip.use_reverse_frames "bpy.types.EffectStrip.use_reverse_frames")
  * [`EffectStrip.color_multiply`](bpy.types.EffectStrip.html#bpy.types.EffectStrip.color_multiply "bpy.types.EffectStrip.color_multiply")
  * [`EffectStrip.multiply_alpha`](bpy.types.EffectStrip.html#bpy.types.EffectStrip.multiply_alpha "bpy.types.EffectStrip.multiply_alpha")
  * [`EffectStrip.color_saturation`](bpy.types.EffectStrip.html#bpy.types.EffectStrip.color_saturation "bpy.types.EffectStrip.color_saturation")
  * [`EffectStrip.strobe`](bpy.types.EffectStrip.html#bpy.types.EffectStrip.strobe "bpy.types.EffectStrip.strobe")
  * [`EffectStrip.transform`](bpy.types.EffectStrip.html#bpy.types.EffectStrip.transform "bpy.types.EffectStrip.transform")
  * [`EffectStrip.crop`](bpy.types.EffectStrip.html#bpy.types.EffectStrip.crop "bpy.types.EffectStrip.crop")
  * [`EffectStrip.use_proxy`](bpy.types.EffectStrip.html#bpy.types.EffectStrip.use_proxy "bpy.types.EffectStrip.use_proxy")
  * [`EffectStrip.proxy`](bpy.types.EffectStrip.html#bpy.types.EffectStrip.proxy "bpy.types.EffectStrip.proxy")

  
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
  * [`bpy_struct.keyframe_insert`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.keyframe_insert "bpy.types.bpy_struct.keyframe_insert")
  * [`bpy_struct.keys`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.keys "bpy.types.bpy_struct.keys")
  * [`bpy_struct.path_from_id`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.path_from_id "bpy.types.bpy_struct.path_from_id")
  * [`bpy_struct.path_resolve`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.path_resolve "bpy.types.bpy_struct.path_resolve")

|

  * [`bpy_struct.pop`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.pop "bpy.types.bpy_struct.pop")
  * [`bpy_struct.property_overridable_library_set`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.property_overridable_library_set "bpy.types.bpy_struct.property_overridable_library_set")
  * [`bpy_struct.property_unset`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.property_unset "bpy.types.bpy_struct.property_unset")
  * [`bpy_struct.rna_ancestors`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.rna_ancestors "bpy.types.bpy_struct.rna_ancestors")
  * [`bpy_struct.type_recast`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.type_recast "bpy.types.bpy_struct.type_recast")
  * [`bpy_struct.values`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.values "bpy.types.bpy_struct.values")
  * [`Strip.strip_elem_from_frame`](bpy.types.Strip.html#bpy.types.Strip.strip_elem_from_frame "bpy.types.Strip.strip_elem_from_frame")
  * [`Strip.swap`](bpy.types.Strip.html#bpy.types.Strip.swap "bpy.types.Strip.swap")
  * [`Strip.move_to_meta`](bpy.types.Strip.html#bpy.types.Strip.move_to_meta "bpy.types.Strip.move_to_meta")
  * [`Strip.parent_meta`](bpy.types.Strip.html#bpy.types.Strip.parent_meta "bpy.types.Strip.parent_meta")
  * [`Strip.invalidate_cache`](bpy.types.Strip.html#bpy.types.Strip.invalidate_cache "bpy.types.Strip.invalidate_cache")
  * [`Strip.split`](bpy.types.Strip.html#bpy.types.Strip.split "bpy.types.Strip.split")
  * [`Strip.bl_rna_get_subclass`](bpy.types.Strip.html#bpy.types.Strip.bl_rna_get_subclass "bpy.types.Strip.bl_rna_get_subclass")
  * [`Strip.bl_rna_get_subclass_py`](bpy.types.Strip.html#bpy.types.Strip.bl_rna_get_subclass_py "bpy.types.Strip.bl_rna_get_subclass_py")
  * [`EffectStrip.bl_rna_get_subclass`](bpy.types.EffectStrip.html#bpy.types.EffectStrip.bl_rna_get_subclass "bpy.types.EffectStrip.bl_rna_get_subclass")
  * [`EffectStrip.bl_rna_get_subclass_py`](bpy.types.EffectStrip.html#bpy.types.EffectStrip.bl_rna_get_subclass_py "bpy.types.EffectStrip.bl_rna_get_subclass_py")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

