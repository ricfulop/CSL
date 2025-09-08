---
url: https://docs.blender.org/api/current/bpy.types.AreaLight.html
scraped_at: 2025-09-08T14:19:39.829014
title: AreaLight(Light)¶
---

# AreaLight(Light)¶  
  
base classes — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct"), [`ID`](bpy.types.ID.html#bpy.types.ID
"bpy.types.ID"), [`Light`](bpy.types.Light.html#bpy.types.Light
"bpy.types.Light")

_class _bpy.types.AreaLight(_Light_)¶

    

Directional area Light

energy¶

    

Light energy emitted over the entire area of the light in all directions, in
units of radiant power (W)

Type:

    

float in [-inf, inf], default 10.0

shadow_buffer_clip_start¶

    

Shadow map clip start, below which objects will not generate shadows

Type:

    

float in [1e-06, inf], default 0.05

shadow_filter_radius¶

    

Blur shadow aliasing using Percentage Closer Filtering

Type:

    

float in [0, inf], default 1.0

shadow_jitter_overblur¶

    

Apply shadow tracing to each jittered sample to reduce under-sampling
artifacts

Type:

    

float in [0, 100], default 10.0

shadow_maximum_resolution¶

    

Minimum size of a shadow map pixel. Higher values use less memory at the cost
of shadow quality.

Type:

    

float in [0, inf], default 0.001

shadow_soft_size¶

    

Light size for ray shadow sampling (Raytraced shadows)

Type:

    

float in [0, inf], default 0.0

shape¶

    

Shape of the area Light

Type:

    

enum in [`SQUARE`, `RECTANGLE`, `DISK`, `ELLIPSE`], default `SQUARE`

size¶

    

Size of the area of the area light, X direction size for rectangle shapes

Type:

    

float in [0, inf], default 0.25

size_y¶

    

Size of the area of the area light in the Y direction for rectangle shapes

Type:

    

float in [0, inf], default 0.25

spread¶

    

How widely the emitted light fans out, as in the case of a gridded softbox

Type:

    

float in [0, 3.14159], default 3.14159

use_absolute_resolution¶

    

Limit the resolution at 1 unit from the light origin instead of relative to
the shadowed pixel

Type:

    

boolean, default False

use_shadow_jitter¶

    

Enable jittered soft shadows to increase shadow precision (disabled in
viewport unless enabled in the render settings). Has a high performance
impact.

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
  * [`ID.name`](bpy.types.ID.html#bpy.types.ID.name "bpy.types.ID.name")
  * [`ID.name_full`](bpy.types.ID.html#bpy.types.ID.name_full "bpy.types.ID.name_full")
  * [`ID.id_type`](bpy.types.ID.html#bpy.types.ID.id_type "bpy.types.ID.id_type")
  * [`ID.session_uid`](bpy.types.ID.html#bpy.types.ID.session_uid "bpy.types.ID.session_uid")
  * [`ID.is_evaluated`](bpy.types.ID.html#bpy.types.ID.is_evaluated "bpy.types.ID.is_evaluated")
  * [`ID.original`](bpy.types.ID.html#bpy.types.ID.original "bpy.types.ID.original")
  * [`ID.users`](bpy.types.ID.html#bpy.types.ID.users "bpy.types.ID.users")
  * [`ID.use_fake_user`](bpy.types.ID.html#bpy.types.ID.use_fake_user "bpy.types.ID.use_fake_user")
  * [`ID.use_extra_user`](bpy.types.ID.html#bpy.types.ID.use_extra_user "bpy.types.ID.use_extra_user")
  * [`ID.is_embedded_data`](bpy.types.ID.html#bpy.types.ID.is_embedded_data "bpy.types.ID.is_embedded_data")
  * [`ID.is_missing`](bpy.types.ID.html#bpy.types.ID.is_missing "bpy.types.ID.is_missing")
  * [`ID.is_runtime_data`](bpy.types.ID.html#bpy.types.ID.is_runtime_data "bpy.types.ID.is_runtime_data")
  * [`ID.is_editable`](bpy.types.ID.html#bpy.types.ID.is_editable "bpy.types.ID.is_editable")
  * [`ID.tag`](bpy.types.ID.html#bpy.types.ID.tag "bpy.types.ID.tag")
  * [`ID.is_library_indirect`](bpy.types.ID.html#bpy.types.ID.is_library_indirect "bpy.types.ID.is_library_indirect")
  * [`ID.library`](bpy.types.ID.html#bpy.types.ID.library "bpy.types.ID.library")
  * [`ID.library_weak_reference`](bpy.types.ID.html#bpy.types.ID.library_weak_reference "bpy.types.ID.library_weak_reference")
  * [`ID.asset_data`](bpy.types.ID.html#bpy.types.ID.asset_data "bpy.types.ID.asset_data")
  * [`ID.override_library`](bpy.types.ID.html#bpy.types.ID.override_library "bpy.types.ID.override_library")

|

  * [`ID.preview`](bpy.types.ID.html#bpy.types.ID.preview "bpy.types.ID.preview")
  * [`Light.type`](bpy.types.Light.html#bpy.types.Light.type "bpy.types.Light.type")
  * [`Light.use_temperature`](bpy.types.Light.html#bpy.types.Light.use_temperature "bpy.types.Light.use_temperature")
  * [`Light.color`](bpy.types.Light.html#bpy.types.Light.color "bpy.types.Light.color")
  * [`Light.temperature`](bpy.types.Light.html#bpy.types.Light.temperature "bpy.types.Light.temperature")
  * [`Light.temperature_color`](bpy.types.Light.html#bpy.types.Light.temperature_color "bpy.types.Light.temperature_color")
  * [`Light.specular_factor`](bpy.types.Light.html#bpy.types.Light.specular_factor "bpy.types.Light.specular_factor")
  * [`Light.diffuse_factor`](bpy.types.Light.html#bpy.types.Light.diffuse_factor "bpy.types.Light.diffuse_factor")
  * [`Light.transmission_factor`](bpy.types.Light.html#bpy.types.Light.transmission_factor "bpy.types.Light.transmission_factor")
  * [`Light.volume_factor`](bpy.types.Light.html#bpy.types.Light.volume_factor "bpy.types.Light.volume_factor")
  * [`Light.use_custom_distance`](bpy.types.Light.html#bpy.types.Light.use_custom_distance "bpy.types.Light.use_custom_distance")
  * [`Light.cutoff_distance`](bpy.types.Light.html#bpy.types.Light.cutoff_distance "bpy.types.Light.cutoff_distance")
  * [`Light.use_shadow`](bpy.types.Light.html#bpy.types.Light.use_shadow "bpy.types.Light.use_shadow")
  * [`Light.exposure`](bpy.types.Light.html#bpy.types.Light.exposure "bpy.types.Light.exposure")
  * [`Light.normalize`](bpy.types.Light.html#bpy.types.Light.normalize "bpy.types.Light.normalize")
  * [`Light.node_tree`](bpy.types.Light.html#bpy.types.Light.node_tree "bpy.types.Light.node_tree")
  * [`Light.use_nodes`](bpy.types.Light.html#bpy.types.Light.use_nodes "bpy.types.Light.use_nodes")
  * [`Light.animation_data`](bpy.types.Light.html#bpy.types.Light.animation_data "bpy.types.Light.animation_data")
  * [`Light.cycles`](bpy.types.Light.html#bpy.types.Light.cycles "bpy.types.Light.cycles")

  
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
  * [`bpy_struct.pop`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.pop "bpy.types.bpy_struct.pop")
  * [`bpy_struct.property_overridable_library_set`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.property_overridable_library_set "bpy.types.bpy_struct.property_overridable_library_set")
  * [`bpy_struct.property_unset`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.property_unset "bpy.types.bpy_struct.property_unset")
  * [`bpy_struct.rna_ancestors`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.rna_ancestors "bpy.types.bpy_struct.rna_ancestors")
  * [`bpy_struct.type_recast`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.type_recast "bpy.types.bpy_struct.type_recast")

|

  * [`bpy_struct.values`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.values "bpy.types.bpy_struct.values")
  * [`ID.rename`](bpy.types.ID.html#bpy.types.ID.rename "bpy.types.ID.rename")
  * [`ID.evaluated_get`](bpy.types.ID.html#bpy.types.ID.evaluated_get "bpy.types.ID.evaluated_get")
  * [`ID.copy`](bpy.types.ID.html#bpy.types.ID.copy "bpy.types.ID.copy")
  * [`ID.asset_mark`](bpy.types.ID.html#bpy.types.ID.asset_mark "bpy.types.ID.asset_mark")
  * [`ID.asset_clear`](bpy.types.ID.html#bpy.types.ID.asset_clear "bpy.types.ID.asset_clear")
  * [`ID.asset_generate_preview`](bpy.types.ID.html#bpy.types.ID.asset_generate_preview "bpy.types.ID.asset_generate_preview")
  * [`ID.override_create`](bpy.types.ID.html#bpy.types.ID.override_create "bpy.types.ID.override_create")
  * [`ID.override_hierarchy_create`](bpy.types.ID.html#bpy.types.ID.override_hierarchy_create "bpy.types.ID.override_hierarchy_create")
  * [`ID.user_clear`](bpy.types.ID.html#bpy.types.ID.user_clear "bpy.types.ID.user_clear")
  * [`ID.user_remap`](bpy.types.ID.html#bpy.types.ID.user_remap "bpy.types.ID.user_remap")
  * [`ID.make_local`](bpy.types.ID.html#bpy.types.ID.make_local "bpy.types.ID.make_local")
  * [`ID.user_of_id`](bpy.types.ID.html#bpy.types.ID.user_of_id "bpy.types.ID.user_of_id")
  * [`ID.animation_data_create`](bpy.types.ID.html#bpy.types.ID.animation_data_create "bpy.types.ID.animation_data_create")
  * [`ID.animation_data_clear`](bpy.types.ID.html#bpy.types.ID.animation_data_clear "bpy.types.ID.animation_data_clear")
  * [`ID.update_tag`](bpy.types.ID.html#bpy.types.ID.update_tag "bpy.types.ID.update_tag")
  * [`ID.preview_ensure`](bpy.types.ID.html#bpy.types.ID.preview_ensure "bpy.types.ID.preview_ensure")
  * [`ID.bl_rna_get_subclass`](bpy.types.ID.html#bpy.types.ID.bl_rna_get_subclass "bpy.types.ID.bl_rna_get_subclass")
  * [`ID.bl_rna_get_subclass_py`](bpy.types.ID.html#bpy.types.ID.bl_rna_get_subclass_py "bpy.types.ID.bl_rna_get_subclass_py")
  * [`Light.area`](bpy.types.Light.html#bpy.types.Light.area "bpy.types.Light.area")
  * [`Light.bl_rna_get_subclass`](bpy.types.Light.html#bpy.types.Light.bl_rna_get_subclass "bpy.types.Light.bl_rna_get_subclass")
  * [`Light.bl_rna_get_subclass_py`](bpy.types.Light.html#bpy.types.Light.bl_rna_get_subclass_py "bpy.types.Light.bl_rna_get_subclass_py")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

