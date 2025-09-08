---
url: https://docs.blender.org/api/current/bpy.types.Constraint.html
scraped_at: 2025-09-08T14:24:00.819334
title: Constraint(bpy_struct)¶
---

# Constraint(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

subclasses —
[`ActionConstraint`](bpy.types.ActionConstraint.html#bpy.types.ActionConstraint
"bpy.types.ActionConstraint"),
[`ArmatureConstraint`](bpy.types.ArmatureConstraint.html#bpy.types.ArmatureConstraint
"bpy.types.ArmatureConstraint"),
[`CameraSolverConstraint`](bpy.types.CameraSolverConstraint.html#bpy.types.CameraSolverConstraint
"bpy.types.CameraSolverConstraint"),
[`ChildOfConstraint`](bpy.types.ChildOfConstraint.html#bpy.types.ChildOfConstraint
"bpy.types.ChildOfConstraint"),
[`ClampToConstraint`](bpy.types.ClampToConstraint.html#bpy.types.ClampToConstraint
"bpy.types.ClampToConstraint"),
[`CopyLocationConstraint`](bpy.types.CopyLocationConstraint.html#bpy.types.CopyLocationConstraint
"bpy.types.CopyLocationConstraint"),
[`CopyRotationConstraint`](bpy.types.CopyRotationConstraint.html#bpy.types.CopyRotationConstraint
"bpy.types.CopyRotationConstraint"),
[`CopyScaleConstraint`](bpy.types.CopyScaleConstraint.html#bpy.types.CopyScaleConstraint
"bpy.types.CopyScaleConstraint"),
[`CopyTransformsConstraint`](bpy.types.CopyTransformsConstraint.html#bpy.types.CopyTransformsConstraint
"bpy.types.CopyTransformsConstraint"),
[`DampedTrackConstraint`](bpy.types.DampedTrackConstraint.html#bpy.types.DampedTrackConstraint
"bpy.types.DampedTrackConstraint"),
[`FloorConstraint`](bpy.types.FloorConstraint.html#bpy.types.FloorConstraint
"bpy.types.FloorConstraint"),
[`FollowPathConstraint`](bpy.types.FollowPathConstraint.html#bpy.types.FollowPathConstraint
"bpy.types.FollowPathConstraint"),
[`FollowTrackConstraint`](bpy.types.FollowTrackConstraint.html#bpy.types.FollowTrackConstraint
"bpy.types.FollowTrackConstraint"),
[`KinematicConstraint`](bpy.types.KinematicConstraint.html#bpy.types.KinematicConstraint
"bpy.types.KinematicConstraint"),
[`LimitDistanceConstraint`](bpy.types.LimitDistanceConstraint.html#bpy.types.LimitDistanceConstraint
"bpy.types.LimitDistanceConstraint"),
[`LimitLocationConstraint`](bpy.types.LimitLocationConstraint.html#bpy.types.LimitLocationConstraint
"bpy.types.LimitLocationConstraint"),
[`LimitRotationConstraint`](bpy.types.LimitRotationConstraint.html#bpy.types.LimitRotationConstraint
"bpy.types.LimitRotationConstraint"),
[`LimitScaleConstraint`](bpy.types.LimitScaleConstraint.html#bpy.types.LimitScaleConstraint
"bpy.types.LimitScaleConstraint"),
[`LockedTrackConstraint`](bpy.types.LockedTrackConstraint.html#bpy.types.LockedTrackConstraint
"bpy.types.LockedTrackConstraint"),
[`MaintainVolumeConstraint`](bpy.types.MaintainVolumeConstraint.html#bpy.types.MaintainVolumeConstraint
"bpy.types.MaintainVolumeConstraint"),
[`ObjectSolverConstraint`](bpy.types.ObjectSolverConstraint.html#bpy.types.ObjectSolverConstraint
"bpy.types.ObjectSolverConstraint"),
[`PivotConstraint`](bpy.types.PivotConstraint.html#bpy.types.PivotConstraint
"bpy.types.PivotConstraint"),
[`ShrinkwrapConstraint`](bpy.types.ShrinkwrapConstraint.html#bpy.types.ShrinkwrapConstraint
"bpy.types.ShrinkwrapConstraint"),
[`SplineIKConstraint`](bpy.types.SplineIKConstraint.html#bpy.types.SplineIKConstraint
"bpy.types.SplineIKConstraint"),
[`StretchToConstraint`](bpy.types.StretchToConstraint.html#bpy.types.StretchToConstraint
"bpy.types.StretchToConstraint"),
[`TrackToConstraint`](bpy.types.TrackToConstraint.html#bpy.types.TrackToConstraint
"bpy.types.TrackToConstraint"),
[`TransformCacheConstraint`](bpy.types.TransformCacheConstraint.html#bpy.types.TransformCacheConstraint
"bpy.types.TransformCacheConstraint"),
[`TransformConstraint`](bpy.types.TransformConstraint.html#bpy.types.TransformConstraint
"bpy.types.TransformConstraint")

_class _bpy.types.Constraint(_bpy_struct_)¶

    

Constraint modifying the transformation of objects and bones

active¶

    

Constraint is the one being edited

Type:

    

boolean, default False

enabled¶

    

Use the results of this constraint

Type:

    

boolean, default False

error_location¶

    

Amount of residual error in Blender space unit for constraints that work on
position

Type:

    

float in [-inf, inf], default 0.0, (readonly)

error_rotation¶

    

Amount of residual error in radians for constraints that work on orientation

Type:

    

float in [-inf, inf], default 0.0, (readonly)

influence¶

    

Amount of influence constraint will have on the final solution

Type:

    

float in [0, 1], default 0.0

is_override_data¶

    

In a local override object, whether this constraint comes from the linked
reference object, or is local to the override

Type:

    

boolean, default False, (readonly)

is_valid¶

    

Constraint has valid settings and can be evaluated

Type:

    

boolean, default False, (readonly)

mute¶

    

Enable/Disable Constraint

Type:

    

boolean, default False

name¶

    

Constraint name

Type:

    

string, default “”, (never None)

owner_space¶

    

Space that owner is evaluated in

  * `WORLD` World Space – The constraint is applied relative to the world coordinate system.

  * `CUSTOM` Custom Space – The constraint is applied in local space of a custom object/bone/vertex group.

  * `POSE` Pose Space – The constraint is applied in Pose Space, the object transformation is ignored.

  * `LOCAL_WITH_PARENT` Local With Parent – The constraint is applied relative to the rest pose local coordinate system of the bone, thus including the parent-induced transformation.

  * `LOCAL` Local Space – The constraint is applied relative to the local coordinate system of the object.

Type:

    

enum in [`WORLD`, `CUSTOM`, `POSE`, `LOCAL_WITH_PARENT`, `LOCAL`], default
`WORLD`

show_expanded¶

    

Constraint’s panel is expanded in UI

Type:

    

boolean, default False

space_object¶

    

Object for Custom Space

Type:

    

[`Object`](bpy.types.Object.html#bpy.types.Object "bpy.types.Object")

space_subtarget¶

    

Armature bone, mesh or lattice vertex group, …

Type:

    

string, default “”, (never None)

target_space¶

    

Space that target is evaluated in

  * `WORLD` World Space – The transformation of the target is evaluated relative to the world coordinate system.

  * `CUSTOM` Custom Space – The transformation of the target is evaluated relative to a custom object/bone/vertex group.

  * `POSE` Pose Space – The transformation of the target is only evaluated in the Pose Space, the target armature object transformation is ignored.

  * `LOCAL_WITH_PARENT` Local With Parent – The transformation of the target bone is evaluated relative to its rest pose local coordinate system, thus including the parent-induced transformation.

  * `LOCAL` Local Space – The transformation of the target is evaluated relative to its local coordinate system.

  * `LOCAL_OWNER_ORIENT` Local Space (Owner Orientation) – The transformation of the target bone is evaluated relative to its local coordinate system, followed by a correction for the difference in target and owner rest pose orientations. When applied as local transform to the owner produces the same global motion as the target if the parents are still in rest pose..

Type:

    

enum in [`WORLD`, `CUSTOM`, `POSE`, `LOCAL_WITH_PARENT`, `LOCAL`,
`LOCAL_OWNER_ORIENT`], default `WORLD`

type¶

    

Type:

    

enum in [Constraint Type
Items](bpy_types_enum_items/constraint_type_items.html#rna-enum-constraint-
type-items), default `CAMERA_SOLVER`, (readonly)

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

  * [`Object.constraints`](bpy.types.Object.html#bpy.types.Object.constraints "bpy.types.Object.constraints")
  * [`ObjectConstraints.active`](bpy.types.ObjectConstraints.html#bpy.types.ObjectConstraints.active "bpy.types.ObjectConstraints.active")
  * [`ObjectConstraints.copy`](bpy.types.ObjectConstraints.html#bpy.types.ObjectConstraints.copy "bpy.types.ObjectConstraints.copy")
  * [`ObjectConstraints.copy`](bpy.types.ObjectConstraints.html#bpy.types.ObjectConstraints.copy "bpy.types.ObjectConstraints.copy")
  * [`ObjectConstraints.new`](bpy.types.ObjectConstraints.html#bpy.types.ObjectConstraints.new "bpy.types.ObjectConstraints.new")
  * [`ObjectConstraints.remove`](bpy.types.ObjectConstraints.html#bpy.types.ObjectConstraints.remove "bpy.types.ObjectConstraints.remove")
  * [`Panel.custom_data`](bpy.types.Panel.html#bpy.types.Panel.custom_data "bpy.types.Panel.custom_data")

|

  * [`PoseBone.constraints`](bpy.types.PoseBone.html#bpy.types.PoseBone.constraints "bpy.types.PoseBone.constraints")
  * [`PoseBoneConstraints.active`](bpy.types.PoseBoneConstraints.html#bpy.types.PoseBoneConstraints.active "bpy.types.PoseBoneConstraints.active")
  * [`PoseBoneConstraints.copy`](bpy.types.PoseBoneConstraints.html#bpy.types.PoseBoneConstraints.copy "bpy.types.PoseBoneConstraints.copy")
  * [`PoseBoneConstraints.copy`](bpy.types.PoseBoneConstraints.html#bpy.types.PoseBoneConstraints.copy "bpy.types.PoseBoneConstraints.copy")
  * [`PoseBoneConstraints.new`](bpy.types.PoseBoneConstraints.html#bpy.types.PoseBoneConstraints.new "bpy.types.PoseBoneConstraints.new")
  * [`PoseBoneConstraints.remove`](bpy.types.PoseBoneConstraints.html#bpy.types.PoseBoneConstraints.remove "bpy.types.PoseBoneConstraints.remove")
  * [`UILayout.template_constraint_header`](bpy.types.UILayout.html#bpy.types.UILayout.template_constraint_header "bpy.types.UILayout.template_constraint_header")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

