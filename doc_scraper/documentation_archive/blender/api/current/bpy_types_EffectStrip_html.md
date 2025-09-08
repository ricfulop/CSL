---
url: https://docs.blender.org/api/current/bpy.types.EffectStrip.html
scraped_at: 2025-09-08T14:24:50.021452
title: EffectStrip(Strip)¶
---

# EffectStrip(Strip)¶  
  
base classes — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct"), [`Strip`](bpy.types.Strip.html#bpy.types.Strip
"bpy.types.Strip")

subclasses — [`AddStrip`](bpy.types.AddStrip.html#bpy.types.AddStrip
"bpy.types.AddStrip"),
[`AdjustmentStrip`](bpy.types.AdjustmentStrip.html#bpy.types.AdjustmentStrip
"bpy.types.AdjustmentStrip"),
[`AlphaOverStrip`](bpy.types.AlphaOverStrip.html#bpy.types.AlphaOverStrip
"bpy.types.AlphaOverStrip"),
[`AlphaUnderStrip`](bpy.types.AlphaUnderStrip.html#bpy.types.AlphaUnderStrip
"bpy.types.AlphaUnderStrip"),
[`ColorMixStrip`](bpy.types.ColorMixStrip.html#bpy.types.ColorMixStrip
"bpy.types.ColorMixStrip"),
[`ColorStrip`](bpy.types.ColorStrip.html#bpy.types.ColorStrip
"bpy.types.ColorStrip"),
[`CrossStrip`](bpy.types.CrossStrip.html#bpy.types.CrossStrip
"bpy.types.CrossStrip"),
[`GammaCrossStrip`](bpy.types.GammaCrossStrip.html#bpy.types.GammaCrossStrip
"bpy.types.GammaCrossStrip"),
[`GaussianBlurStrip`](bpy.types.GaussianBlurStrip.html#bpy.types.GaussianBlurStrip
"bpy.types.GaussianBlurStrip"),
[`GlowStrip`](bpy.types.GlowStrip.html#bpy.types.GlowStrip
"bpy.types.GlowStrip"),
[`MulticamStrip`](bpy.types.MulticamStrip.html#bpy.types.MulticamStrip
"bpy.types.MulticamStrip"),
[`MultiplyStrip`](bpy.types.MultiplyStrip.html#bpy.types.MultiplyStrip
"bpy.types.MultiplyStrip"),
[`SpeedControlStrip`](bpy.types.SpeedControlStrip.html#bpy.types.SpeedControlStrip
"bpy.types.SpeedControlStrip"),
[`SubtractStrip`](bpy.types.SubtractStrip.html#bpy.types.SubtractStrip
"bpy.types.SubtractStrip"),
[`TextStrip`](bpy.types.TextStrip.html#bpy.types.TextStrip
"bpy.types.TextStrip"),
[`TransformStrip`](bpy.types.TransformStrip.html#bpy.types.TransformStrip
"bpy.types.TransformStrip"),
[`WipeStrip`](bpy.types.WipeStrip.html#bpy.types.WipeStrip
"bpy.types.WipeStrip")

_class _bpy.types.EffectStrip(_Strip_)¶

    

Sequence strip applying an effect on the images created by other strips

alpha_mode¶

    

Representation of alpha information in the RGBA pixels

  * `STRAIGHT` Straight – RGB channels in transparent pixels are unaffected by the alpha channel.

  * `PREMUL` Premultiplied – RGB channels in transparent pixels are multiplied by the alpha channel.

Type:

    

enum in [`STRAIGHT`, `PREMUL`], default `STRAIGHT`

color_multiply¶

    

Type:

    

float in [0, 20], default 1.0

color_saturation¶

    

Adjust the intensity of the input’s color

Type:

    

float in [0, 20], default 1.0

crop¶

    

Type:

    

[`StripCrop`](bpy.types.StripCrop.html#bpy.types.StripCrop
"bpy.types.StripCrop"), (readonly)

multiply_alpha¶

    

Multiply alpha along with color channels

Type:

    

boolean, default False

proxy¶

    

Type:

    

[`StripProxy`](bpy.types.StripProxy.html#bpy.types.StripProxy
"bpy.types.StripProxy"), (readonly)

strobe¶

    

Only display every nth frame

Type:

    

float in [1, 30], default 0.0

transform¶

    

Type:

    

[`StripTransform`](bpy.types.StripTransform.html#bpy.types.StripTransform
"bpy.types.StripTransform"), (readonly)

use_deinterlace¶

    

Remove fields from video movies

Type:

    

boolean, default False

use_flip_x¶

    

Flip on the X axis

Type:

    

boolean, default False

use_flip_y¶

    

Flip on the Y axis

Type:

    

boolean, default False

use_float¶

    

Convert input to float data

Type:

    

boolean, default False

use_proxy¶

    

Use a preview proxy and/or time-code index for this strip

Type:

    

boolean, default False

use_reverse_frames¶

    

Reverse frame order

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

|

  * [`Strip.frame_final_end`](bpy.types.Strip.html#bpy.types.Strip.frame_final_end "bpy.types.Strip.frame_final_end")
  * [`Strip.frame_offset_start`](bpy.types.Strip.html#bpy.types.Strip.frame_offset_start "bpy.types.Strip.frame_offset_start")
  * [`Strip.frame_offset_end`](bpy.types.Strip.html#bpy.types.Strip.frame_offset_end "bpy.types.Strip.frame_offset_end")
  * [`Strip.channel`](bpy.types.Strip.html#bpy.types.Strip.channel "bpy.types.Strip.channel")
  * [`Strip.use_linear_modifiers`](bpy.types.Strip.html#bpy.types.Strip.use_linear_modifiers "bpy.types.Strip.use_linear_modifiers")
  * [`Strip.blend_type`](bpy.types.Strip.html#bpy.types.Strip.blend_type "bpy.types.Strip.blend_type")
  * [`Strip.blend_alpha`](bpy.types.Strip.html#bpy.types.Strip.blend_alpha "bpy.types.Strip.blend_alpha")
  * [`Strip.effect_fader`](bpy.types.Strip.html#bpy.types.Strip.effect_fader "bpy.types.Strip.effect_fader")
  * [`Strip.use_default_fade`](bpy.types.Strip.html#bpy.types.Strip.use_default_fade "bpy.types.Strip.use_default_fade")
  * [`Strip.color_tag`](bpy.types.Strip.html#bpy.types.Strip.color_tag "bpy.types.Strip.color_tag")
  * [`Strip.modifiers`](bpy.types.Strip.html#bpy.types.Strip.modifiers "bpy.types.Strip.modifiers")
  * [`Strip.show_retiming_keys`](bpy.types.Strip.html#bpy.types.Strip.show_retiming_keys "bpy.types.Strip.show_retiming_keys")

  
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

|

  * [`bpy_struct.path_resolve`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.path_resolve "bpy.types.bpy_struct.path_resolve")
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

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

