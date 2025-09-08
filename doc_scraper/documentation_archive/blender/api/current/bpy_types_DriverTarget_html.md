---
url: https://docs.blender.org/api/current/bpy.types.DriverTarget.html
scraped_at: 2025-09-08T14:24:39.981875
title: DriverTarget(bpy_struct)¶
---

# DriverTarget(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.DriverTarget(_bpy_struct_)¶

    

Source of input values for driver variables

bone_target¶

    

Name of PoseBone to use as target

Type:

    

string, default “”, (never None)

context_property¶

    

Type of a context-dependent data-block to access property from

  * `ACTIVE_SCENE` Active Scene – Currently evaluating scene.

  * `ACTIVE_VIEW_LAYER` Active View Layer – Currently evaluating view layer.

Type:

    

enum in [`ACTIVE_SCENE`, `ACTIVE_VIEW_LAYER`], default `ACTIVE_SCENE`

data_path¶

    

RNA Path (from ID-block) to property used

Type:

    

string, default “”, (never None)

fallback_value¶

    

The value to use if the data path can’t be resolved

Type:

    

float in [-inf, inf], default 0.0

id¶

    

ID-block that the specific property used can be found from (id_type property
must be set first)

Type:

    

[`ID`](bpy.types.ID.html#bpy.types.ID "bpy.types.ID")

id_type¶

    

Type of ID-block that can be used

Type:

    

enum in [Id Type Items](bpy_types_enum_items/id_type_items.html#rna-enum-id-
type-items), default `OBJECT`

is_fallback_used¶

    

Indicates that the most recent variable evaluation used the fallback value

Type:

    

boolean, default False, (readonly)

rotation_mode¶

    

Mode for calculating rotation channel values

Type:

    

enum in [Driver Target Rotation Mode
Items](bpy_types_enum_items/driver_target_rotation_mode_items.html#rna-enum-
driver-target-rotation-mode-items), default `AUTO`

transform_space¶

    

Space in which transforms are used

  * `WORLD_SPACE` World Space – Transforms include effects of parenting/restpose and constraints.

  * `TRANSFORM_SPACE` Transform Space – Transforms don’t include parenting/restpose or constraints.

  * `LOCAL_SPACE` Local Space – Transforms include effects of constraints but not parenting/restpose.

Type:

    

enum in [`WORLD_SPACE`, `TRANSFORM_SPACE`, `LOCAL_SPACE`], default
`WORLD_SPACE`

transform_type¶

    

Driver variable type

Type:

    

enum in [`LOC_X`, `LOC_Y`, `LOC_Z`, `ROT_X`, `ROT_Y`, `ROT_Z`, `ROT_W`,
`SCALE_X`, `SCALE_Y`, `SCALE_Z`, `SCALE_AVG`], default `LOC_X`

use_fallback_value¶

    

Use the fallback value if the data path can’t be resolved, instead of failing
to evaluate the driver

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

  * [`DriverVariable.targets`](bpy.types.DriverVariable.html#bpy.types.DriverVariable.targets "bpy.types.DriverVariable.targets")

|

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

