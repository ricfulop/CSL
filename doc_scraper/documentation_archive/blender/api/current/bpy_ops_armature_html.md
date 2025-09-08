---
url: https://docs.blender.org/api/current/bpy.ops.armature.html
scraped_at: 2025-09-08T14:17:50.424606
title: Armature Operators¶
---

# Armature Operators¶

bpy.ops.armature.align()¶

    

Align selected bones to the active bone (or to their parent)

bpy.ops.armature.assign_to_collection(_*_ , _collection_index =-1_,
_new_collection_name =''_)¶

    

Assign all selected bones to a collection, or unassign them, depending on
whether the active bone is already assigned or not

Parameters:

    

  * **collection_index** (_int in_ _[__-1_ _,__inf_ _]__,__(__optional_ _)_) – Collection Index, Index of the collection to assign selected bones to. When the operator should create a new bone collection, use new_collection_name to define the collection name, and set this parameter to the parent index of the new bone collection

  * **new_collection_name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of a to-be-added bone collection. Only pass this if you want to create a new bone collection and assign the selected bones to it. To assign to an existing collection, do not include this parameter and use collection_index

bpy.ops.armature.autoside_names(_*_ , _type =XAXIS_)¶

    

Automatically renames the selected bones according to which side of the target
axis they fall on

Parameters:

    

**type** (enum in [`XAXIS`, `YAXIS`, `ZAXIS`], (optional)) –

Axis, Axis to tag names with

  * `XAXIS` X-Axis – Left/Right.

  * `YAXIS` Y-Axis – Front/Back.

  * `ZAXIS` Z-Axis – Top/Bottom.

bpy.ops.armature.bone_primitive_add(_*_ , _name =''_)¶

    

Add a new bone located at the 3D cursor

Parameters:

    

**name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the
newly created bone

bpy.ops.armature.calculate_roll(_*_ , _type =POS_X_, _axis_flip =False_,
_axis_only =False_)¶

    

Automatically fix alignment of select bones’ axes

Parameters:

    

  * **type** (enum in [`POS_X`, `POS_Z`, `GLOBAL_POS_X`, `GLOBAL_POS_Y`, `GLOBAL_POS_Z`, `NEG_X`, `NEG_Z`, `GLOBAL_NEG_X`, `GLOBAL_NEG_Y`, `GLOBAL_NEG_Z`, `ACTIVE`, `VIEW`, `CURSOR`], (optional)) – Type

  * **axis_flip** (_boolean_ _,__(__optional_ _)_) – Flip Axis, Negate the alignment axis

  * **axis_only** (_boolean_ _,__(__optional_ _)_) – Shortest Rotation, Ignore the axis direction, use the shortest rotation to align

bpy.ops.armature.click_extrude()¶

    

Create a new bone going from the last selected joint to the mouse position

bpy.ops.armature.collection_add()¶

    

Add a new bone collection

bpy.ops.armature.collection_assign(_*_ , _name =''_)¶

    

Add selected bones to the chosen bone collection

Parameters:

    

**name** (_string_ _,__(__optional_ _,__never None_ _)_) – Bone Collection,
Name of the bone collection to assign this bone to; empty to assign to the
active bone collection

bpy.ops.armature.collection_create_and_assign(_*_ , _name =''_)¶

    

Create a new bone collection and assign all selected bones

Parameters:

    

**name** (_string_ _,__(__optional_ _,__never None_ _)_) – Bone Collection,
Name of the bone collection to create

bpy.ops.armature.collection_deselect()¶

    

Deselect bones of active Bone Collection

bpy.ops.armature.collection_move(_*_ , _direction =UP_)¶

    

Change position of active Bone Collection in list of Bone collections

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Direction, Direction to
move the active Bone Collection towards

bpy.ops.armature.collection_remove()¶

    

Remove the active bone collection

bpy.ops.armature.collection_remove_unused()¶

    

Remove all bone collections that have neither bones nor children. This is done
recursively, so bone collections that only have unused children are also
removed

File:

    

[startup/bl_operators/anim.py:606](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L606)

bpy.ops.armature.collection_select()¶

    

Select bones in active Bone Collection

bpy.ops.armature.collection_show_all()¶

    

Show all bone collections

File:

    

[startup/bl_operators/anim.py:561](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L561)

bpy.ops.armature.collection_unassign(_*_ , _name =''_)¶

    

Remove selected bones from the active bone collection

Parameters:

    

**name** (_string_ _,__(__optional_ _,__never None_ _)_) – Bone Collection,
Name of the bone collection to unassign this bone from; empty to unassign from
the active bone collection

bpy.ops.armature.collection_unassign_named(_*_ , _name =''_, _bone_name =''_)¶

    

Unassign the named bone from this bone collection

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Bone Collection, Name of the bone collection to unassign this bone from; empty to unassign from the active bone collection

  * **bone_name** (_string_ _,__(__optional_ _,__never None_ _)_) – Bone Name, Name of the bone to unassign from the collection; empty to use the active bone

bpy.ops.armature.collection_unsolo_all()¶

    

Clear the ‘solo’ setting on all bone collections

File:

    

[startup/bl_operators/anim.py:584](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L584)

bpy.ops.armature.copy_bone_color_to_selected(_*_ , _bone_type =EDIT_)¶

    

Copy the bone color of the active bone to all selected bones

Parameters:

    

**bone_type** (enum in [`EDIT`, `POSE`], (optional)) –

Type

  * `EDIT` Bone – Copy Bone colors from the active bone to all selected bones.

  * `POSE` Pose Bone – Copy Pose Bone colors from the active pose bone to all selected pose bones.

File:

    

[startup/bl_operators/anim.py:480](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L480)

bpy.ops.armature.delete(_*_ , _confirm =True_)¶

    

Remove selected bones from the armature

Parameters:

    

**confirm** (_boolean_ _,__(__optional_ _)_) – Confirm, Prompt for
confirmation

bpy.ops.armature.dissolve()¶

    

Dissolve selected bones from the armature

bpy.ops.armature.duplicate(_*_ , _do_flip_names =False_)¶

    

Make copies of the selected bones within the same armature

Parameters:

    

**do_flip_names** (_boolean_ _,__(__optional_ _)_) – Flip Names, Try to flip
names of the bones, if possible, instead of adding a number extension

bpy.ops.armature.duplicate_move(_*_ , _ARMATURE_OT_duplicate =None_,
_TRANSFORM_OT_translate =None_)¶

    

Make copies of the selected bones within the same armature and move them

Parameters:

    

  * **ARMATURE_OT_duplicate** (`ARMATURE_OT_duplicate`, (optional)) – Duplicate Selected Bone(s), Make copies of the selected bones within the same armature

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.armature.extrude(_*_ , _forked =False_)¶

    

Create new bones from the selected joints

Parameters:

    

**forked** (_boolean_ _,__(__optional_ _)_) – Forked

bpy.ops.armature.extrude_forked(_*_ , _ARMATURE_OT_extrude =None_,
_TRANSFORM_OT_translate =None_)¶

    

Create new bones from the selected joints and move them

Parameters:

    

  * **ARMATURE_OT_extrude** (`ARMATURE_OT_extrude`, (optional)) – Extrude, Create new bones from the selected joints

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.armature.extrude_move(_*_ , _ARMATURE_OT_extrude =None_,
_TRANSFORM_OT_translate =None_)¶

    

Create new bones from the selected joints and move them

Parameters:

    

  * **ARMATURE_OT_extrude** (`ARMATURE_OT_extrude`, (optional)) – Extrude, Create new bones from the selected joints

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.armature.fill()¶

    

Add bone between selected joint(s) and/or 3D cursor

bpy.ops.armature.flip_names(_*_ , _do_strip_numbers =False_)¶

    

Flips (and corrects) the axis suffixes of the names of selected bones

Parameters:

    

**do_strip_numbers** (_boolean_ _,__(__optional_ _)_) – Strip Numbers, Try to
remove right-most dot-number from flipped names.Warning: May result in
incoherent naming in some cases

bpy.ops.armature.hide(_*_ , _unselected =False_)¶

    

Tag selected bones to not be visible in Edit Mode

Parameters:

    

**unselected** (_boolean_ _,__(__optional_ _)_) – Unselected, Hide unselected
rather than selected

bpy.ops.armature.move_to_collection(_*_ , _collection_index =-1_,
_new_collection_name =''_)¶

    

Move bones to a collection

Parameters:

    

  * **collection_index** (_int in_ _[__-1_ _,__inf_ _]__,__(__optional_ _)_) – Collection Index, Index of the collection to move selected bones to. When the operator should create a new bone collection, do not include this parameter and pass new_collection_name

  * **new_collection_name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of a to-be-added bone collection. Only pass this if you want to create a new bone collection and move the selected bones to it. To move to an existing collection, do not include this parameter and use collection_index

bpy.ops.armature.parent_clear(_*_ , _type =CLEAR_)¶

    

Remove the parent-child relationship between selected bones and their parents

Parameters:

    

**type** (enum in [`CLEAR`, `DISCONNECT`], (optional)) – Clear Type, What way
to clear parenting

bpy.ops.armature.parent_set(_*_ , _type =CONNECTED_)¶

    

Set the active bone as the parent of the selected bones

Parameters:

    

**type** (enum in [`CONNECTED`, `OFFSET`], (optional)) – Parent Type, Type of
parenting

bpy.ops.armature.reveal(_*_ , _select =True_)¶

    

Reveal all bones hidden in Edit Mode

Parameters:

    

**select** (_boolean_ _,__(__optional_ _)_) – Select

bpy.ops.armature.roll_clear(_*_ , _roll =0.0_)¶

    

Clear roll for selected bones

Parameters:

    

**roll** (_float in_ _[__-6.28319_ _,__6.28319_ _]__,__(__optional_ _)_) –
Roll

bpy.ops.armature.select_all(_*_ , _action =TOGGLE_)¶

    

Toggle selection status of all bones

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.armature.select_hierarchy(_*_ , _direction =PARENT_, _extend =False_)¶

    

Select immediate parent/children of selected bones

Parameters:

    

  * **direction** (enum in [`PARENT`, `CHILD`], (optional)) – Direction

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend the selection

bpy.ops.armature.select_less()¶

    

Deselect those bones at the boundary of each selection region

bpy.ops.armature.select_linked(_*_ , _all_forks =False_)¶

    

Select all bones linked by parent/child connections to the current selection

Parameters:

    

**all_forks** (_boolean_ _,__(__optional_ _)_) – All Forks, Follow forks in
the parents chain

bpy.ops.armature.select_linked_pick(_*_ , _deselect =False_, _all_forks
=False_)¶

    

(De)select bones linked by parent/child connections under the mouse cursor

Parameters:

    

  * **deselect** (_boolean_ _,__(__optional_ _)_) – Deselect

  * **all_forks** (_boolean_ _,__(__optional_ _)_) – All Forks, Follow forks in the parents chain

bpy.ops.armature.select_mirror(_*_ , _only_active =False_, _extend =False_)¶

    

Mirror the bone selection

Parameters:

    

  * **only_active** (_boolean_ _,__(__optional_ _)_) – Active Only, Only operate on the active bone

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend the selection

bpy.ops.armature.select_more()¶

    

Select those bones connected to the initial selection

bpy.ops.armature.select_similar(_*_ , _type =LENGTH_, _threshold =0.1_)¶

    

Select similar bones by property types

Parameters:

    

  * **type** (enum in [`CHILDREN`, `CHILDREN_IMMEDIATE`, `SIBLINGS`, `LENGTH`, `DIRECTION`, `PREFIX`, `SUFFIX`, `BONE_COLLECTION`, `COLOR`, `SHAPE`], (optional)) – Type

  * **threshold** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Threshold

bpy.ops.armature.separate()¶

    

Isolate selected bones into a separate armature

bpy.ops.armature.shortest_path_pick()¶

    

Select shortest path between two bones

bpy.ops.armature.split()¶

    

Split off selected bones from connected unselected bones

bpy.ops.armature.subdivide(_*_ , _number_cuts =1_)¶

    

Break selected bones into chains of smaller bones

Parameters:

    

**number_cuts** (_int in_ _[__1_ _,__1000_ _]__,__(__optional_ _)_) – Number
of Cuts

bpy.ops.armature.switch_direction()¶

    

Change the direction that a chain of bones points in (head and tail swap)

bpy.ops.armature.symmetrize(_*_ , _direction =NEGATIVE_X_)¶

    

Enforce symmetry, make copies of the selection or use existing

Parameters:

    

**direction** (enum in [`NEGATIVE_X`, `POSITIVE_X`], (optional)) – Direction,
Which sides to copy from and to (when both are selected)

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

