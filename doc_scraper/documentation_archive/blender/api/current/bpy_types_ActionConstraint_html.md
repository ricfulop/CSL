---
url: https://docs.blender.org/api/current/bpy.types.ActionConstraint.html
scraped_at: 2025-09-08T14:19:14.748542
title: ActionConstraint(Constraint)¶
---

# ActionConstraint(Constraint)¶  
  
base classes — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct"),
[`Constraint`](bpy.types.Constraint.html#bpy.types.Constraint
"bpy.types.Constraint")

_class _bpy.types.ActionConstraint(_Constraint_)¶

    

Map an action to the transform axes of a bone

action¶

    

The constraining action

Type:

    

[`Action`](bpy.types.Action.html#bpy.types.Action "bpy.types.Action")

action_slot¶

    

The slot identifies which sub-set of the Action is considered to be for this
strip, and its name is used to find the right slot when assigning another
Action

Type:

    

[`ActionSlot`](bpy.types.ActionSlot.html#bpy.types.ActionSlot
"bpy.types.ActionSlot")

action_slot_handle¶

    

A number that identifies which sub-set of the Action is considered to be for
this Action Constraint

Type:

    

int in [-inf, inf], default 0

action_suitable_slots¶

    

The list of action slots suitable for this NLA strip

Type:

    

[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`ActionSlot`](bpy.types.ActionSlot.html#bpy.types.ActionSlot
"bpy.types.ActionSlot"), (readonly)

eval_time¶

    

Interpolates between Action Start and End frames

Type:

    

float in [0, 1], default 0.0

frame_end¶

    

Last frame of the Action to use

Type:

    

int in [-1048574, 1048574], default 0

frame_start¶

    

First frame of the Action to use

Type:

    

int in [-1048574, 1048574], default 0

last_slot_identifier¶

    

The identifier of the most recently assigned action slot. The slot identifies
which sub-set of the Action is considered to be for this constraint, and its
identifier is used to find the right slot when assigning an Action.

Type:

    

string, default “”, (never None)

max¶

    

Maximum value for target channel range

Type:

    

float in [-1000, 1000], default 0.0

min¶

    

Minimum value for target channel range

Type:

    

float in [-1000, 1000], default 0.0

mix_mode¶

    

Specify how existing transformations and the action channels are combined

  * `REPLACE` Replace – Replace the original transformation with the action channels.

  * `BEFORE_FULL` Before Original (Full) – Apply the action channels before the original transformation, as if applied to an imaginary parent in Full Inherit Scale mode. Will create shear when combining rotation and non-uniform scale..

  * `BEFORE` Before Original (Aligned) – Apply the action channels before the original transformation, as if applied to an imaginary parent in Aligned Inherit Scale mode. This effectively uses Full for location and Split Channels for rotation and scale..

  * `BEFORE_SPLIT` Before Original (Split Channels) – Apply the action channels before the original transformation, handling location, rotation and scale separately.

  * `AFTER_FULL` After Original (Full) – Apply the action channels after the original transformation, as if applied to an imaginary child in Full Inherit Scale mode. Will create shear when combining rotation and non-uniform scale..

  * `AFTER` After Original (Aligned) – Apply the action channels after the original transformation, as if applied to an imaginary child in Aligned Inherit Scale mode. This effectively uses Full for location and Split Channels for rotation and scale..

  * `AFTER_SPLIT` After Original (Split Channels) – Apply the action channels after the original transformation, handling location, rotation and scale separately.

Type:

    

enum in [`REPLACE`, `BEFORE_FULL`, `BEFORE`, `BEFORE_SPLIT`, `AFTER_FULL`,
`AFTER`, `AFTER_SPLIT`], default `AFTER_FULL`

subtarget¶

    

Armature bone, mesh or lattice vertex group, …

Type:

    

string, default “”, (never None)

target¶

    

Target object

Type:

    

[`Object`](bpy.types.Object.html#bpy.types.Object "bpy.types.Object")

transform_channel¶

    

Transformation channel from the target that is used to key the Action

Type:

    

enum in [`LOCATION_X`, `LOCATION_Y`, `LOCATION_Z`, `ROTATION_X`, `ROTATION_Y`,
`ROTATION_Z`, `SCALE_X`, `SCALE_Y`, `SCALE_Z`], default `ROTATION_X`

use_bone_object_action¶

    

Bones only: apply the object’s transformation channels of the action to the
constrained bone, instead of bone’s channels

Type:

    

boolean, default False

use_eval_time¶

    

Interpolate between Action Start and End frames, with the Evaluation Time
slider instead of the Target object/bone

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
  * [`Constraint.name`](bpy.types.Constraint.html#bpy.types.Constraint.name "bpy.types.Constraint.name")
  * [`Constraint.type`](bpy.types.Constraint.html#bpy.types.Constraint.type "bpy.types.Constraint.type")
  * [`Constraint.is_override_data`](bpy.types.Constraint.html#bpy.types.Constraint.is_override_data "bpy.types.Constraint.is_override_data")
  * [`Constraint.owner_space`](bpy.types.Constraint.html#bpy.types.Constraint.owner_space "bpy.types.Constraint.owner_space")
  * [`Constraint.target_space`](bpy.types.Constraint.html#bpy.types.Constraint.target_space "bpy.types.Constraint.target_space")
  * [`Constraint.space_object`](bpy.types.Constraint.html#bpy.types.Constraint.space_object "bpy.types.Constraint.space_object")
  * [`Constraint.space_subtarget`](bpy.types.Constraint.html#bpy.types.Constraint.space_subtarget "bpy.types.Constraint.space_subtarget")

|

  * [`Constraint.mute`](bpy.types.Constraint.html#bpy.types.Constraint.mute "bpy.types.Constraint.mute")
  * [`Constraint.enabled`](bpy.types.Constraint.html#bpy.types.Constraint.enabled "bpy.types.Constraint.enabled")
  * [`Constraint.show_expanded`](bpy.types.Constraint.html#bpy.types.Constraint.show_expanded "bpy.types.Constraint.show_expanded")
  * [`Constraint.is_valid`](bpy.types.Constraint.html#bpy.types.Constraint.is_valid "bpy.types.Constraint.is_valid")
  * [`Constraint.active`](bpy.types.Constraint.html#bpy.types.Constraint.active "bpy.types.Constraint.active")
  * [`Constraint.influence`](bpy.types.Constraint.html#bpy.types.Constraint.influence "bpy.types.Constraint.influence")
  * [`Constraint.error_location`](bpy.types.Constraint.html#bpy.types.Constraint.error_location "bpy.types.Constraint.error_location")
  * [`Constraint.error_rotation`](bpy.types.Constraint.html#bpy.types.Constraint.error_rotation "bpy.types.Constraint.error_rotation")

  
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
  * [`Constraint.bl_rna_get_subclass`](bpy.types.Constraint.html#bpy.types.Constraint.bl_rna_get_subclass "bpy.types.Constraint.bl_rna_get_subclass")
  * [`Constraint.bl_rna_get_subclass_py`](bpy.types.Constraint.html#bpy.types.Constraint.bl_rna_get_subclass_py "bpy.types.Constraint.bl_rna_get_subclass_py")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

