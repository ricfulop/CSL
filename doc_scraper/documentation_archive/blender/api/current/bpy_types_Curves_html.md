---
url: https://docs.blender.org/api/current/bpy.types.Curves.html
scraped_at: 2025-09-08T14:24:24.947845
title: Curves(ID)¶
---

# Curves(ID)¶  
  
base classes — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct"), [`ID`](bpy.types.ID.html#bpy.types.ID "bpy.types.ID")

_class _bpy.types.Curves(_ID_)¶

    

Hair data-block for hair curves

animation_data¶

    

Animation data for this data-block

Type:

    

[`AnimData`](bpy.types.AnimData.html#bpy.types.AnimData "bpy.types.AnimData"),
(readonly)

attributes¶

    

Geometry attributes

Type:

    

[`AttributeGroupCurves`](bpy.types.AttributeGroupCurves.html#bpy.types.AttributeGroupCurves
"bpy.types.AttributeGroupCurves")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Attribute`](bpy.types.Attribute.html#bpy.types.Attribute
"bpy.types.Attribute"), (readonly)

color_attributes¶

    

Geometry color attributes

Type:

    

[`AttributeGroupCurves`](bpy.types.AttributeGroupCurves.html#bpy.types.AttributeGroupCurves
"bpy.types.AttributeGroupCurves")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Attribute`](bpy.types.Attribute.html#bpy.types.Attribute
"bpy.types.Attribute"), (readonly)

curve_offset_data¶

    

Type:

    

[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`IntAttributeValue`](bpy.types.IntAttributeValue.html#bpy.types.IntAttributeValue
"bpy.types.IntAttributeValue"), (readonly)

curves¶

    

All curves in the data-block

Type:

    

[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`CurveSlice`](bpy.types.CurveSlice.html#bpy.types.CurveSlice
"bpy.types.CurveSlice"), (readonly)

materials¶

    

Type:

    

[`IDMaterials`](bpy.types.IDMaterials.html#bpy.types.IDMaterials
"bpy.types.IDMaterials")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Material`](bpy.types.Material.html#bpy.types.Material "bpy.types.Material"),
(readonly)

normals¶

    

The curve normal value at each of the curve’s control points

Type:

    

[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`FloatVectorValueReadOnly`](bpy.types.FloatVectorValueReadOnly.html#bpy.types.FloatVectorValueReadOnly
"bpy.types.FloatVectorValueReadOnly"), (readonly)

points¶

    

Control points of all curves

Type:

    

[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`CurvePoint`](bpy.types.CurvePoint.html#bpy.types.CurvePoint
"bpy.types.CurvePoint"), (readonly)

position_data¶

    

Type:

    

[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`FloatVectorAttributeValue`](bpy.types.FloatVectorAttributeValue.html#bpy.types.FloatVectorAttributeValue
"bpy.types.FloatVectorAttributeValue"), (readonly)

selection_domain¶

    

Type:

    

enum in [Attribute Curves Domain
Items](bpy_types_enum_items/attribute_curves_domain_items.html#rna-enum-
attribute-curves-domain-items), default `POINT`

surface¶

    

Mesh object that the curves can be attached to

Type:

    

[`Object`](bpy.types.Object.html#bpy.types.Object "bpy.types.Object")

surface_collision_distance¶

    

Distance to keep the curves away from the surface

Type:

    

float in [1.192e-07, inf], default 0.005

surface_uv_map¶

    

The name of the attribute on the surface mesh used to define the attachment of
each curve

Type:

    

string, default “”, (never None)

use_mirror_x¶

    

Enable symmetry in the X axis

Type:

    

boolean, default False

use_mirror_y¶

    

Enable symmetry in the Y axis

Type:

    

boolean, default False

use_mirror_z¶

    

Enable symmetry in the Z axis

Type:

    

boolean, default False

use_sculpt_collision¶

    

Enable collision with the surface while sculpting

Type:

    

boolean, default False

add_curves(_sizes_)¶

    

add_curves

Parameters:

    

**sizes** (_int array_ _of_ _1 items in_ _[__0_ _,__inf_ _]_) – Sizes, The
number of points in each curve

remove_curves(_*_ , _indices =(0,)_)¶

    

Remove all curves. If indices are provided, remove only the curves with the
given indices.

Parameters:

    

**indices** (_int array_ _of_ _1 items in_ _[__0_ _,__inf_ _]__,__(__optional_
_)_) – Indices, The indices of the curves to remove

resize_curves(_sizes_ , _*_ , _indices =(0,)_)¶

    

Resize all existing curves. If indices are provided, resize only the curves
with the given indices. If the new size for a curve is smaller, the curve is
trimmed. If the new size for a curve is larger, the new end values are default
initialized.

Parameters:

    

  * **sizes** (_int array_ _of_ _1 items in_ _[__1_ _,__inf_ _]_) – Sizes, The number of points in each curve

  * **indices** (_int array_ _of_ _1 items in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Indices, The indices of the curves to resize

reorder_curves(_new_indices_)¶

    

Reorder the curves by the new indices.

Parameters:

    

**new_indices** (_int array_ _of_ _1 items in_ _[__0_ _,__inf_ _]_) – New
indices, The new index for each of the curves

set_types(_*_ , _type =CATMULL_ROM_, _indices =(0,)_)¶

    

Set the curve type. If indices are provided, set only the types with the given
curve indices.

Parameters:

    

  * **type** (enum in [Curves Type Items](bpy_types_enum_items/curves_type_items.html#rna-enum-curves-type-items), (optional)) – Type

  * **indices** (_int array_ _of_ _1 items in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Indices, The indices of the curves to resize

unit_test_compare(_*_ , _curves =None_, _threshold =7.1526e-06_)¶

    

unit_test_compare

Parameters:

    

  * **curves** (`Curves`, (optional)) – Curves to compare to

  * **threshold** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Threshold, Comparison tolerance threshold

Returns:

    

Return value, String description of result of comparison

Return type:

    

string, (never None)

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

|

  * [`ID.is_missing`](bpy.types.ID.html#bpy.types.ID.is_missing "bpy.types.ID.is_missing")
  * [`ID.is_runtime_data`](bpy.types.ID.html#bpy.types.ID.is_runtime_data "bpy.types.ID.is_runtime_data")
  * [`ID.is_editable`](bpy.types.ID.html#bpy.types.ID.is_editable "bpy.types.ID.is_editable")
  * [`ID.tag`](bpy.types.ID.html#bpy.types.ID.tag "bpy.types.ID.tag")
  * [`ID.is_library_indirect`](bpy.types.ID.html#bpy.types.ID.is_library_indirect "bpy.types.ID.is_library_indirect")
  * [`ID.library`](bpy.types.ID.html#bpy.types.ID.library "bpy.types.ID.library")
  * [`ID.library_weak_reference`](bpy.types.ID.html#bpy.types.ID.library_weak_reference "bpy.types.ID.library_weak_reference")
  * [`ID.asset_data`](bpy.types.ID.html#bpy.types.ID.asset_data "bpy.types.ID.asset_data")
  * [`ID.override_library`](bpy.types.ID.html#bpy.types.ID.override_library "bpy.types.ID.override_library")
  * [`ID.preview`](bpy.types.ID.html#bpy.types.ID.preview "bpy.types.ID.preview")

  
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

|

  * [`bpy_struct.type_recast`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.type_recast "bpy.types.bpy_struct.type_recast")
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

  
---|---  
  
## References¶

  * [`BlendData.hair_curves`](bpy.types.BlendData.html#bpy.types.BlendData.hair_curves "bpy.types.BlendData.hair_curves")
  * [`BlendDataHairCurves.new`](bpy.types.BlendDataHairCurves.html#bpy.types.BlendDataHairCurves.new "bpy.types.BlendDataHairCurves.new")

|

  * [`BlendDataHairCurves.remove`](bpy.types.BlendDataHairCurves.html#bpy.types.BlendDataHairCurves.remove "bpy.types.BlendDataHairCurves.remove")
  * `Curves.unit_test_compare`

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

