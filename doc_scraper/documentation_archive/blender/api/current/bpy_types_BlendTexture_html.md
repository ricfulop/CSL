---
url: https://docs.blender.org/api/current/bpy.types.BlendTexture.html
scraped_at: 2025-09-08T14:20:52.110746
title: BlendTexture(Texture)¶
---

# BlendTexture(Texture)¶  
  
base classes — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct"), [`ID`](bpy.types.ID.html#bpy.types.ID
"bpy.types.ID"), [`Texture`](bpy.types.Texture.html#bpy.types.Texture
"bpy.types.Texture")

_class _bpy.types.BlendTexture(_Texture_)¶

    

Procedural color blending texture

progression¶

    

Style of the color blending

  * `LINEAR` Linear – Create a linear progression.

  * `QUADRATIC` Quadratic – Create a quadratic progression.

  * `EASING` Easing – Create a progression easing from one step to the next.

  * `DIAGONAL` Diagonal – Create a diagonal progression.

  * `SPHERICAL` Spherical – Create a spherical progression.

  * `QUADRATIC_SPHERE` Quadratic Sphere – Create a quadratic progression in the shape of a sphere.

  * `RADIAL` Radial – Create a radial progression.

Type:

    

enum in [`LINEAR`, `QUADRATIC`, `EASING`, `DIAGONAL`, `SPHERICAL`,
`QUADRATIC_SPHERE`, `RADIAL`], default `LINEAR`

use_flip_axis¶

    

Flip the texture’s X and Y axis

  * `HORIZONTAL` Horizontal – No flipping.

  * `VERTICAL` Vertical – Flip the texture’s X and Y axis.

Type:

    

enum in [`HORIZONTAL`, `VERTICAL`], default `HORIZONTAL`

users_material¶

    

Materials that use this texture

> type:
>  
>
> tuple of [`Material`](bpy.types.Material.html#bpy.types.Material
> "bpy.types.Material")
>
> Note
>
> Takes `O(len(bpy.data.materials) * len(material.texture_slots))` time.

(readonly)

users_object_modifier¶

    

Object modifiers that use this texture

> type:
>  
>
> tuple of [`Object`](bpy.types.Object.html#bpy.types.Object
> "bpy.types.Object")
>
> Note
>
> Takes `O(len(bpy.data.objects) * len(obj.modifiers))` time.

(readonly)

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

|

  * [`ID.override_library`](bpy.types.ID.html#bpy.types.ID.override_library "bpy.types.ID.override_library")
  * [`ID.preview`](bpy.types.ID.html#bpy.types.ID.preview "bpy.types.ID.preview")
  * [`Texture.type`](bpy.types.Texture.html#bpy.types.Texture.type "bpy.types.Texture.type")
  * [`Texture.use_clamp`](bpy.types.Texture.html#bpy.types.Texture.use_clamp "bpy.types.Texture.use_clamp")
  * [`Texture.use_color_ramp`](bpy.types.Texture.html#bpy.types.Texture.use_color_ramp "bpy.types.Texture.use_color_ramp")
  * [`Texture.color_ramp`](bpy.types.Texture.html#bpy.types.Texture.color_ramp "bpy.types.Texture.color_ramp")
  * [`Texture.intensity`](bpy.types.Texture.html#bpy.types.Texture.intensity "bpy.types.Texture.intensity")
  * [`Texture.contrast`](bpy.types.Texture.html#bpy.types.Texture.contrast "bpy.types.Texture.contrast")
  * [`Texture.saturation`](bpy.types.Texture.html#bpy.types.Texture.saturation "bpy.types.Texture.saturation")
  * [`Texture.factor_red`](bpy.types.Texture.html#bpy.types.Texture.factor_red "bpy.types.Texture.factor_red")
  * [`Texture.factor_green`](bpy.types.Texture.html#bpy.types.Texture.factor_green "bpy.types.Texture.factor_green")
  * [`Texture.factor_blue`](bpy.types.Texture.html#bpy.types.Texture.factor_blue "bpy.types.Texture.factor_blue")
  * [`Texture.use_preview_alpha`](bpy.types.Texture.html#bpy.types.Texture.use_preview_alpha "bpy.types.Texture.use_preview_alpha")
  * [`Texture.use_nodes`](bpy.types.Texture.html#bpy.types.Texture.use_nodes "bpy.types.Texture.use_nodes")
  * [`Texture.node_tree`](bpy.types.Texture.html#bpy.types.Texture.node_tree "bpy.types.Texture.node_tree")
  * [`Texture.animation_data`](bpy.types.Texture.html#bpy.types.Texture.animation_data "bpy.types.Texture.animation_data")
  * [`Texture.users_material`](bpy.types.Texture.html#bpy.types.Texture.users_material "bpy.types.Texture.users_material")
  * [`Texture.users_object_modifier`](bpy.types.Texture.html#bpy.types.Texture.users_object_modifier "bpy.types.Texture.users_object_modifier")

  
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
  * [`Texture.evaluate`](bpy.types.Texture.html#bpy.types.Texture.evaluate "bpy.types.Texture.evaluate")
  * [`Texture.bl_rna_get_subclass`](bpy.types.Texture.html#bpy.types.Texture.bl_rna_get_subclass "bpy.types.Texture.bl_rna_get_subclass")
  * [`Texture.bl_rna_get_subclass_py`](bpy.types.Texture.html#bpy.types.Texture.bl_rna_get_subclass_py "bpy.types.Texture.bl_rna_get_subclass_py")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

