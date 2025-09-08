---
url: https://docs.blender.org/api/current/bpy.types.ArrayModifier.html
scraped_at: 2025-09-08T14:19:47.826872
title: ArrayModifier(Modifier)¶
---

# ArrayModifier(Modifier)¶  
  
base classes — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct"),
[`Modifier`](bpy.types.Modifier.html#bpy.types.Modifier "bpy.types.Modifier")

_class _bpy.types.ArrayModifier(_Modifier_)¶

    

Array duplication modifier

constant_offset_displace¶

    

Value for the distance between arrayed items

Type:

    

[`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3
items in [-inf, inf], default (1.0, 0.0, 0.0)

count¶

    

Number of duplicates to make

Type:

    

int in [1, inf], default 2

curve¶

    

Curve object to fit array length to

Type:

    

[`Object`](bpy.types.Object.html#bpy.types.Object "bpy.types.Object")

end_cap¶

    

Mesh object to use as an end cap

Type:

    

[`Object`](bpy.types.Object.html#bpy.types.Object "bpy.types.Object")

fit_length¶

    

Length to fit array within

Type:

    

float in [0, inf], default 0.0

fit_type¶

    

Array length calculation method

  * `FIXED_COUNT` Fixed Count – Duplicate the object a certain number of times.

  * `FIT_LENGTH` Fit Length – Duplicate the object as many times as fits in a certain length.

  * `FIT_CURVE` Fit Curve – Fit the duplicated objects to a curve.

Type:

    

enum in [`FIXED_COUNT`, `FIT_LENGTH`, `FIT_CURVE`], default `FIXED_COUNT`

merge_threshold¶

    

Limit below which to merge vertices

Type:

    

float in [0, inf], default 0.01

offset_object¶

    

Use the location and rotation of another object to determine the distance and
rotational change between arrayed items

Type:

    

[`Object`](bpy.types.Object.html#bpy.types.Object "bpy.types.Object")

offset_u¶

    

Amount to offset array UVs on the U axis

Type:

    

float in [-1, 1], default 0.0

offset_v¶

    

Amount to offset array UVs on the V axis

Type:

    

float in [-1, 1], default 0.0

relative_offset_displace¶

    

The size of the geometry will determine the distance between arrayed items

Type:

    

[`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3
items in [-inf, inf], default (1.0, 0.0, 0.0)

start_cap¶

    

Mesh object to use as a start cap

Type:

    

[`Object`](bpy.types.Object.html#bpy.types.Object "bpy.types.Object")

use_constant_offset¶

    

Add a constant offset

Type:

    

boolean, default False

use_merge_vertices¶

    

Merge vertices in adjacent duplicates

Type:

    

boolean, default False

use_merge_vertices_cap¶

    

Merge vertices in first and last duplicates

Type:

    

boolean, default False

use_object_offset¶

    

Add another object’s transformation to the total offset

Type:

    

boolean, default False

use_relative_offset¶

    

Add an offset relative to the object’s bounding box

Type:

    

boolean, default True

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
  * [`Modifier.name`](bpy.types.Modifier.html#bpy.types.Modifier.name "bpy.types.Modifier.name")
  * [`Modifier.type`](bpy.types.Modifier.html#bpy.types.Modifier.type "bpy.types.Modifier.type")
  * [`Modifier.show_viewport`](bpy.types.Modifier.html#bpy.types.Modifier.show_viewport "bpy.types.Modifier.show_viewport")
  * [`Modifier.show_render`](bpy.types.Modifier.html#bpy.types.Modifier.show_render "bpy.types.Modifier.show_render")
  * [`Modifier.show_in_editmode`](bpy.types.Modifier.html#bpy.types.Modifier.show_in_editmode "bpy.types.Modifier.show_in_editmode")
  * [`Modifier.show_on_cage`](bpy.types.Modifier.html#bpy.types.Modifier.show_on_cage "bpy.types.Modifier.show_on_cage")

|

  * [`Modifier.show_expanded`](bpy.types.Modifier.html#bpy.types.Modifier.show_expanded "bpy.types.Modifier.show_expanded")
  * [`Modifier.is_active`](bpy.types.Modifier.html#bpy.types.Modifier.is_active "bpy.types.Modifier.is_active")
  * [`Modifier.use_pin_to_last`](bpy.types.Modifier.html#bpy.types.Modifier.use_pin_to_last "bpy.types.Modifier.use_pin_to_last")
  * [`Modifier.is_override_data`](bpy.types.Modifier.html#bpy.types.Modifier.is_override_data "bpy.types.Modifier.is_override_data")
  * [`Modifier.use_apply_on_spline`](bpy.types.Modifier.html#bpy.types.Modifier.use_apply_on_spline "bpy.types.Modifier.use_apply_on_spline")
  * [`Modifier.execution_time`](bpy.types.Modifier.html#bpy.types.Modifier.execution_time "bpy.types.Modifier.execution_time")
  * [`Modifier.persistent_uid`](bpy.types.Modifier.html#bpy.types.Modifier.persistent_uid "bpy.types.Modifier.persistent_uid")

  
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
  * [`Modifier.bl_rna_get_subclass`](bpy.types.Modifier.html#bpy.types.Modifier.bl_rna_get_subclass "bpy.types.Modifier.bl_rna_get_subclass")
  * [`Modifier.bl_rna_get_subclass_py`](bpy.types.Modifier.html#bpy.types.Modifier.bl_rna_get_subclass_py "bpy.types.Modifier.bl_rna_get_subclass_py")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

