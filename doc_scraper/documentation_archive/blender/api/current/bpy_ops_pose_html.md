---
url: https://docs.blender.org/api/current/bpy.ops.pose.html
scraped_at: 2025-09-08T14:18:38.598902
title: Pose Operators¶
---

# Pose Operators¶

bpy.ops.pose.armature_apply(_*_ , _selected =False_)¶

    

Apply the current pose as the new rest pose

Parameters:

    

**selected** (_boolean_ _,__(__optional_ _)_) – Selected Only, Only apply the
selected bones (with propagation to children)

bpy.ops.pose.autoside_names(_*_ , _axis =XAXIS_)¶

    

Automatically renames the selected bones according to which side of the target
axis they fall on

Parameters:

    

**axis** (enum in [`XAXIS`, `YAXIS`, `ZAXIS`], (optional)) –

Axis, Axis to tag names with

  * `XAXIS` X-Axis – Left/Right.

  * `YAXIS` Y-Axis – Front/Back.

  * `ZAXIS` Z-Axis – Top/Bottom.

bpy.ops.pose.blend_to_neighbor(_*_ , _factor =0.5_, _prev_frame =0_,
_next_frame =0_, _channels =ALL_, _axis_lock =FREE_)¶

    

Blend from current position to previous or next keyframe

Parameters:

    

  * **factor** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Factor, Weighting factor for which keyframe is favored more

  * **prev_frame** (_int in_ _[__-1048574_ _,__1048574_ _]__,__(__optional_ _)_) – Previous Keyframe, Frame number of keyframe immediately before the current frame

  * **next_frame** (_int in_ _[__-1048574_ _,__1048574_ _]__,__(__optional_ _)_) – Next Keyframe, Frame number of keyframe immediately after the current frame

  * **channels** (enum in [`ALL`, `LOC`, `ROT`, `SIZE`, `BBONE`, `CUSTOM`], (optional)) – 

Channels, Set of properties that are affected

    * `ALL` All Properties – All properties, including transforms, bendy bone shape, and custom properties.

    * `LOC` Location – Location only.

    * `ROT` Rotation – Rotation only.

    * `SIZE` Scale – Scale only.

    * `BBONE` Bendy Bone – Bendy Bone shape properties.

    * `CUSTOM` Custom Properties – Custom properties.

  * **axis_lock** (enum in [`FREE`, `X`, `Y`, `Z`], (optional)) – 

Axis Lock, Transform axis to restrict effects to

    * `FREE` Free – All axes are affected.

    * `X` X – Only X-axis transforms are affected.

    * `Y` Y – Only Y-axis transforms are affected.

    * `Z` Z – Only Z-axis transforms are affected.

bpy.ops.pose.blend_with_rest(_*_ , _factor =0.5_, _prev_frame =0_, _next_frame
=0_, _channels =ALL_, _axis_lock =FREE_)¶

    

Make the current pose more similar to, or further away from, the rest pose

Parameters:

    

  * **factor** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Factor, Weighting factor for which keyframe is favored more

  * **prev_frame** (_int in_ _[__-1048574_ _,__1048574_ _]__,__(__optional_ _)_) – Previous Keyframe, Frame number of keyframe immediately before the current frame

  * **next_frame** (_int in_ _[__-1048574_ _,__1048574_ _]__,__(__optional_ _)_) – Next Keyframe, Frame number of keyframe immediately after the current frame

  * **channels** (enum in [`ALL`, `LOC`, `ROT`, `SIZE`, `BBONE`, `CUSTOM`], (optional)) – 

Channels, Set of properties that are affected

    * `ALL` All Properties – All properties, including transforms, bendy bone shape, and custom properties.

    * `LOC` Location – Location only.

    * `ROT` Rotation – Rotation only.

    * `SIZE` Scale – Scale only.

    * `BBONE` Bendy Bone – Bendy Bone shape properties.

    * `CUSTOM` Custom Properties – Custom properties.

  * **axis_lock** (enum in [`FREE`, `X`, `Y`, `Z`], (optional)) – 

Axis Lock, Transform axis to restrict effects to

    * `FREE` Free – All axes are affected.

    * `X` X – Only X-axis transforms are affected.

    * `Y` Y – Only Y-axis transforms are affected.

    * `Z` Z – Only Z-axis transforms are affected.

bpy.ops.pose.breakdown(_*_ , _factor =0.5_, _prev_frame =0_, _next_frame =0_,
_channels =ALL_, _axis_lock =FREE_)¶

    

Create a suitable breakdown pose on the current frame

Parameters:

    

  * **factor** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Factor, Weighting factor for which keyframe is favored more

  * **prev_frame** (_int in_ _[__-1048574_ _,__1048574_ _]__,__(__optional_ _)_) – Previous Keyframe, Frame number of keyframe immediately before the current frame

  * **next_frame** (_int in_ _[__-1048574_ _,__1048574_ _]__,__(__optional_ _)_) – Next Keyframe, Frame number of keyframe immediately after the current frame

  * **channels** (enum in [`ALL`, `LOC`, `ROT`, `SIZE`, `BBONE`, `CUSTOM`], (optional)) – 

Channels, Set of properties that are affected

    * `ALL` All Properties – All properties, including transforms, bendy bone shape, and custom properties.

    * `LOC` Location – Location only.

    * `ROT` Rotation – Rotation only.

    * `SIZE` Scale – Scale only.

    * `BBONE` Bendy Bone – Bendy Bone shape properties.

    * `CUSTOM` Custom Properties – Custom properties.

  * **axis_lock** (enum in [`FREE`, `X`, `Y`, `Z`], (optional)) – 

Axis Lock, Transform axis to restrict effects to

    * `FREE` Free – All axes are affected.

    * `X` X – Only X-axis transforms are affected.

    * `Y` Y – Only Y-axis transforms are affected.

    * `Z` Z – Only Z-axis transforms are affected.

bpy.ops.pose.constraint_add(_*_ , _type_)¶

    

Add a constraint to the active bone

Parameters:

    

**type** (enum in [Constraint Type
Items](bpy_types_enum_items/constraint_type_items.html#rna-enum-constraint-
type-items), (optional)) – Type

bpy.ops.pose.constraint_add_with_targets(_*_ , _type_)¶

    

Add a constraint to the active bone, with target (where applicable) set to the
selected Objects/Bones

Parameters:

    

**type** (enum in [Constraint Type
Items](bpy_types_enum_items/constraint_type_items.html#rna-enum-constraint-
type-items), (optional)) – Type

bpy.ops.pose.constraints_clear()¶

    

Clear all constraints from the selected bones

bpy.ops.pose.constraints_copy()¶

    

Copy constraints to other selected bones

bpy.ops.pose.copy()¶

    

Copy the current pose of the selected bones to the internal clipboard

bpy.ops.pose.flip_names(_*_ , _do_strip_numbers =False_)¶

    

Flips (and corrects) the axis suffixes of the names of selected bones

Parameters:

    

**do_strip_numbers** (_boolean_ _,__(__optional_ _)_) – Strip Numbers, Try to
remove right-most dot-number from flipped names.Warning: May result in
incoherent naming in some cases

bpy.ops.pose.hide(_*_ , _unselected =False_)¶

    

Tag selected bones to not be visible in Pose Mode

Parameters:

    

**unselected** (_boolean_ _,__(__optional_ _)_) – Unselected

bpy.ops.pose.ik_add(_*_ , _with_targets =True_)¶

    

Add IK Constraint to the active Bone

Parameters:

    

**with_targets** (_boolean_ _,__(__optional_ _)_) – With Targets, Assign IK
Constraint with targets derived from the select bones/objects

bpy.ops.pose.ik_clear()¶

    

Remove all IK Constraints from selected bones

bpy.ops.pose.loc_clear()¶

    

Reset locations of selected bones to their default values

bpy.ops.pose.paste(_*_ , _flipped =False_, _selected_mask =False_)¶

    

Paste the stored pose on to the current pose

Parameters:

    

  * **flipped** (_boolean_ _,__(__optional_ _)_) – Flipped on X-Axis, Paste the stored pose flipped on to current pose

  * **selected_mask** (_boolean_ _,__(__optional_ _)_) – On Selected Only, Only paste the stored pose on to selected bones in the current pose

bpy.ops.pose.paths_calculate(_*_ , _display_type =RANGE_, _range =SCENE_,
_bake_location =HEADS_)¶

    

Calculate paths for the selected bones

Parameters:

    

  * **display_type** (enum in [Motionpath Display Type Items](bpy_types_enum_items/motionpath_display_type_items.html#rna-enum-motionpath-display-type-items), (optional)) – Display type

  * **range** (enum in [Motionpath Range Items](bpy_types_enum_items/motionpath_range_items.html#rna-enum-motionpath-range-items), (optional)) – Computation Range

  * **bake_location** (enum in [Motionpath Bake Location Items](bpy_types_enum_items/motionpath_bake_location_items.html#rna-enum-motionpath-bake-location-items), (optional)) – Bake Location, Which point on the bones is used when calculating paths

bpy.ops.pose.paths_clear(_*_ , _only_selected =False_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

**only_selected** (_boolean_ _,__(__optional_ _)_) – Only Selected, Only clear
motion paths of selected bones

bpy.ops.pose.paths_range_update()¶

    

Update frame range for motion paths from the Scene’s current frame range

bpy.ops.pose.paths_update()¶

    

Recalculate paths for bones that already have them

bpy.ops.pose.propagate(_*_ , _mode =NEXT_KEY_, _end_frame =250.0_)¶

    

Copy selected aspects of the current pose to subsequent poses already
keyframed

Parameters:

    

  * **mode** (enum in [`NEXT_KEY`, `LAST_KEY`, `BEFORE_FRAME`, `BEFORE_END`, `SELECTED_KEYS`, `SELECTED_MARKERS`], (optional)) – 

Terminate Mode, Method used to determine when to stop propagating pose to
keyframes

    * `NEXT_KEY` To Next Keyframe – Propagate pose to first keyframe following the current frame only.

    * `LAST_KEY` To Last Keyframe – Propagate pose to the last keyframe only (i.e. making action cyclic).

    * `BEFORE_FRAME` Before Frame – Propagate pose to all keyframes between current frame and ‘Frame’ property.

    * `BEFORE_END` Before Last Keyframe – Propagate pose to all keyframes from current frame until no more are found.

    * `SELECTED_KEYS` On Selected Keyframes – Propagate pose to all selected keyframes.

    * `SELECTED_MARKERS` On Selected Markers – Propagate pose to all keyframes occurring on frames with Scene Markers after the current frame.

  * **end_frame** (_float in_ _[__1.17549e-38_ _,__inf_ _]__,__(__optional_ _)_) – End Frame, Frame to stop propagating frames to (for ‘Before Frame’ mode)

bpy.ops.pose.push(_*_ , _factor =0.5_, _prev_frame =0_, _next_frame =0_,
_channels =ALL_, _axis_lock =FREE_)¶

    

Exaggerate the current pose in regards to the breakdown pose

Parameters:

    

  * **factor** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Factor, Weighting factor for which keyframe is favored more

  * **prev_frame** (_int in_ _[__-1048574_ _,__1048574_ _]__,__(__optional_ _)_) – Previous Keyframe, Frame number of keyframe immediately before the current frame

  * **next_frame** (_int in_ _[__-1048574_ _,__1048574_ _]__,__(__optional_ _)_) – Next Keyframe, Frame number of keyframe immediately after the current frame

  * **channels** (enum in [`ALL`, `LOC`, `ROT`, `SIZE`, `BBONE`, `CUSTOM`], (optional)) – 

Channels, Set of properties that are affected

    * `ALL` All Properties – All properties, including transforms, bendy bone shape, and custom properties.

    * `LOC` Location – Location only.

    * `ROT` Rotation – Rotation only.

    * `SIZE` Scale – Scale only.

    * `BBONE` Bendy Bone – Bendy Bone shape properties.

    * `CUSTOM` Custom Properties – Custom properties.

  * **axis_lock** (enum in [`FREE`, `X`, `Y`, `Z`], (optional)) – 

Axis Lock, Transform axis to restrict effects to

    * `FREE` Free – All axes are affected.

    * `X` X – Only X-axis transforms are affected.

    * `Y` Y – Only Y-axis transforms are affected.

    * `Z` Z – Only Z-axis transforms are affected.

bpy.ops.pose.quaternions_flip()¶

    

Flip quaternion values to achieve desired rotations, while maintaining the
same orientations

bpy.ops.pose.relax(_*_ , _factor =0.5_, _prev_frame =0_, _next_frame =0_,
_channels =ALL_, _axis_lock =FREE_)¶

    

Make the current pose more similar to its breakdown pose

Parameters:

    

  * **factor** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Factor, Weighting factor for which keyframe is favored more

  * **prev_frame** (_int in_ _[__-1048574_ _,__1048574_ _]__,__(__optional_ _)_) – Previous Keyframe, Frame number of keyframe immediately before the current frame

  * **next_frame** (_int in_ _[__-1048574_ _,__1048574_ _]__,__(__optional_ _)_) – Next Keyframe, Frame number of keyframe immediately after the current frame

  * **channels** (enum in [`ALL`, `LOC`, `ROT`, `SIZE`, `BBONE`, `CUSTOM`], (optional)) – 

Channels, Set of properties that are affected

    * `ALL` All Properties – All properties, including transforms, bendy bone shape, and custom properties.

    * `LOC` Location – Location only.

    * `ROT` Rotation – Rotation only.

    * `SIZE` Scale – Scale only.

    * `BBONE` Bendy Bone – Bendy Bone shape properties.

    * `CUSTOM` Custom Properties – Custom properties.

  * **axis_lock** (enum in [`FREE`, `X`, `Y`, `Z`], (optional)) – 

Axis Lock, Transform axis to restrict effects to

    * `FREE` Free – All axes are affected.

    * `X` X – Only X-axis transforms are affected.

    * `Y` Y – Only Y-axis transforms are affected.

    * `Z` Z – Only Z-axis transforms are affected.

bpy.ops.pose.reveal(_*_ , _select =True_)¶

    

Reveal all bones hidden in Pose Mode

Parameters:

    

**select** (_boolean_ _,__(__optional_ _)_) – Select

bpy.ops.pose.rot_clear()¶

    

Reset rotations of selected bones to their default values

bpy.ops.pose.rotation_mode_set(_*_ , _type =QUATERNION_)¶

    

Set the rotation representation used by selected bones

Parameters:

    

**type** (enum in [Object Rotation Mode
Items](bpy_types_enum_items/object_rotation_mode_items.html#rna-enum-object-
rotation-mode-items), (optional)) – Rotation Mode

bpy.ops.pose.scale_clear()¶

    

Reset scaling of selected bones to their default values

bpy.ops.pose.select_all(_*_ , _action =TOGGLE_)¶

    

Toggle selection status of all bones

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.pose.select_constraint_target()¶

    

Select bones used as targets for the currently selected bones

bpy.ops.pose.select_grouped(_*_ , _extend =False_, _type =COLLECTION_)¶

    

Select all visible bones grouped by similar properties

Parameters:

    

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection instead of deselecting everything first

  * **type** (enum in [`COLLECTION`, `COLOR`, `KEYINGSET`, `CHILDREN`, `CHILDREN_IMMEDIATE`, `PARENT`, `SIBILINGS`], (optional)) – 

Type

    * `COLLECTION` Collection – Same collections as the active bone.

    * `COLOR` Color – Same color as the active bone.

    * `KEYINGSET` Keying Set – All bones affected by active Keying Set.

    * `CHILDREN` Children – Select all children of currently selected bones.

    * `CHILDREN_IMMEDIATE` Immediate Children – Select direct children of currently selected bones.

    * `PARENT` Parents – Select the parents of currently selected bones.

    * `SIBILINGS` Siblings – Select all bones that have the same parent as currently selected bones.

bpy.ops.pose.select_hierarchy(_*_ , _direction =PARENT_, _extend =False_)¶

    

Select immediate parent/children of selected bones

Parameters:

    

  * **direction** (enum in [`PARENT`, `CHILD`], (optional)) – Direction

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend the selection

bpy.ops.pose.select_linked()¶

    

Select all bones linked by parent/child connections to the current selection

bpy.ops.pose.select_linked_pick(_*_ , _extend =False_)¶

    

Select bones linked by parent/child connections under the mouse cursor

Parameters:

    

**extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection instead
of deselecting everything first

bpy.ops.pose.select_mirror(_*_ , _only_active =False_, _extend =False_)¶

    

Mirror the bone selection

Parameters:

    

  * **only_active** (_boolean_ _,__(__optional_ _)_) – Active Only, Only operate on the active bone

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend the selection

bpy.ops.pose.select_parent()¶

    

Select bones that are parents of the currently selected bones

bpy.ops.pose.selection_set_add()¶

    

Create a new empty Selection Set

File:

    

[startup/bl_operators/bone_selection_sets.py:143](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/bone_selection_sets.py#L143)

bpy.ops.pose.selection_set_add_and_assign()¶

    

Create a new Selection Set with the currently selected bones

File:

    

[startup/bl_operators/bone_selection_sets.py:274](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/bone_selection_sets.py#L274)

bpy.ops.pose.selection_set_assign()¶

    

Add selected bones to Selection Set

File:

    

[startup/bl_operators/bone_selection_sets.py:190](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/bone_selection_sets.py#L190)

bpy.ops.pose.selection_set_copy()¶

    

Copy the selected Selection Set(s) to the clipboard

File:

    

[startup/bl_operators/bone_selection_sets.py:286](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/bone_selection_sets.py#L286)

bpy.ops.pose.selection_set_delete_all()¶

    

Remove all Selection Sets from this Armature

File:

    

[startup/bl_operators/bone_selection_sets.py:73](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/bone_selection_sets.py#L73)

bpy.ops.pose.selection_set_deselect()¶

    

Remove Selection Set bones from current selection

File:

    

[startup/bl_operators/bone_selection_sets.py:257](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/bone_selection_sets.py#L257)

bpy.ops.pose.selection_set_move(_*_ , _direction =UP_)¶

    

Move the active Selection Set up/down the list of sets

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Move Direction, Direction
to move the active Selection Set: UP (default) or DOWN

File:

    

[startup/bl_operators/bone_selection_sets.py:122](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/bone_selection_sets.py#L122)

bpy.ops.pose.selection_set_paste()¶

    

Add new Selection Set(s) from the clipboard

File:

    

[startup/bl_operators/bone_selection_sets.py:298](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/bone_selection_sets.py#L298)

bpy.ops.pose.selection_set_remove()¶

    

Remove a Selection Set from this Armature

File:

    

[startup/bl_operators/bone_selection_sets.py:161](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/bone_selection_sets.py#L161)

bpy.ops.pose.selection_set_remove_bones()¶

    

Remove the selected bones from all Selection Sets

File:

    

[startup/bl_operators/bone_selection_sets.py:85](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/bone_selection_sets.py#L85)

bpy.ops.pose.selection_set_select(_*_ , _selection_set_index =-1_)¶

    

Select the bones from this Selection Set

Parameters:

    

**selection_set_index** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_)
– Selection Set Index, Which Selection Set to select; -1 uses the active
Selection Set

File:

    

[startup/bl_operators/bone_selection_sets.py:235](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/bone_selection_sets.py#L235)

bpy.ops.pose.selection_set_unassign()¶

    

Remove selected bones from Selection Set

File:

    

[startup/bl_operators/bone_selection_sets.py:209](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/bone_selection_sets.py#L209)

bpy.ops.pose.transforms_clear()¶

    

Reset location, rotation, and scaling of selected bones to their default
values

bpy.ops.pose.user_transforms_clear(_*_ , _only_selected =True_)¶

    

Reset pose bone transforms to keyframed state

Parameters:

    

**only_selected** (_boolean_ _,__(__optional_ _)_) – Only Selected, Only
visible/selected bones

bpy.ops.pose.visual_transform_apply()¶

    

Apply final constrained position of pose bones to their transform

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

