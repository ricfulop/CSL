---
url: https://docs.blender.org/api/current/bpy.ops.constraint.html
scraped_at: 2025-09-08T14:18:01.456784
title: Constraint Operators¶
---

# Constraint Operators¶

bpy.ops.constraint.add_target()¶

    

Add a target to the constraint

File:

    

[startup/bl_operators/constraint.py:26](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/constraint.py#L26)

bpy.ops.constraint.apply(_*_ , _constraint =''_, _owner =OBJECT_, _report
=False_)¶

    

Apply constraint and remove from the stack

Parameters:

    

  * **constraint** (_string_ _,__(__optional_ _,__never None_ _)_) – Constraint, Name of the constraint to edit

  * **owner** (enum in [`OBJECT`, `BONE`], (optional)) – 

Owner, The owner of this constraint

    * `OBJECT` Object – Edit a constraint on the active object.

    * `BONE` Bone – Edit a constraint on the active bone.

  * **report** (_boolean_ _,__(__optional_ _)_) – Report, Create a notification after the operation

bpy.ops.constraint.childof_clear_inverse(_*_ , _constraint =''_, _owner
=OBJECT_)¶

    

Clear inverse correction for Child Of constraint

Parameters:

    

  * **constraint** (_string_ _,__(__optional_ _,__never None_ _)_) – Constraint, Name of the constraint to edit

  * **owner** (enum in [`OBJECT`, `BONE`], (optional)) – 

Owner, The owner of this constraint

    * `OBJECT` Object – Edit a constraint on the active object.

    * `BONE` Bone – Edit a constraint on the active bone.

bpy.ops.constraint.childof_set_inverse(_*_ , _constraint =''_, _owner
=OBJECT_)¶

    

Set inverse correction for Child Of constraint

Parameters:

    

  * **constraint** (_string_ _,__(__optional_ _,__never None_ _)_) – Constraint, Name of the constraint to edit

  * **owner** (enum in [`OBJECT`, `BONE`], (optional)) – 

Owner, The owner of this constraint

    * `OBJECT` Object – Edit a constraint on the active object.

    * `BONE` Bone – Edit a constraint on the active bone.

bpy.ops.constraint.copy(_*_ , _constraint =''_, _owner =OBJECT_, _report
=False_)¶

    

Duplicate constraint at the same position in the stack

Parameters:

    

  * **constraint** (_string_ _,__(__optional_ _,__never None_ _)_) – Constraint, Name of the constraint to edit

  * **owner** (enum in [`OBJECT`, `BONE`], (optional)) – 

Owner, The owner of this constraint

    * `OBJECT` Object – Edit a constraint on the active object.

    * `BONE` Bone – Edit a constraint on the active bone.

  * **report** (_boolean_ _,__(__optional_ _)_) – Report, Create a notification after the operation

bpy.ops.constraint.copy_to_selected(_*_ , _constraint =''_, _owner =OBJECT_)¶

    

Copy constraint to other selected objects/bones

Parameters:

    

  * **constraint** (_string_ _,__(__optional_ _,__never None_ _)_) – Constraint, Name of the constraint to edit

  * **owner** (enum in [`OBJECT`, `BONE`], (optional)) – 

Owner, The owner of this constraint

    * `OBJECT` Object – Edit a constraint on the active object.

    * `BONE` Bone – Edit a constraint on the active bone.

bpy.ops.constraint.delete(_*_ , _constraint =''_, _owner =OBJECT_, _report
=False_)¶

    

Remove constraint from constraint stack

Parameters:

    

  * **constraint** (_string_ _,__(__optional_ _,__never None_ _)_) – Constraint, Name of the constraint to edit

  * **owner** (enum in [`OBJECT`, `BONE`], (optional)) – 

Owner, The owner of this constraint

    * `OBJECT` Object – Edit a constraint on the active object.

    * `BONE` Bone – Edit a constraint on the active bone.

  * **report** (_boolean_ _,__(__optional_ _)_) – Report, Create a notification after the operation

bpy.ops.constraint.disable_keep_transform()¶

    

Set the influence of this constraint to zero while trying to maintain the
object’s transformation. Other active constraints can still influence the
final transformation

File:

    

[startup/bl_operators/constraint.py:86](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/constraint.py#L86)

bpy.ops.constraint.followpath_path_animate(_*_ , _constraint =''_, _owner
=OBJECT_, _frame_start =1_, _length =100_)¶

    

Add default animation for path used by constraint if it isn’t animated already

Parameters:

    

  * **constraint** (_string_ _,__(__optional_ _,__never None_ _)_) – Constraint, Name of the constraint to edit

  * **owner** (enum in [`OBJECT`, `BONE`], (optional)) – 

Owner, The owner of this constraint

    * `OBJECT` Object – Edit a constraint on the active object.

    * `BONE` Bone – Edit a constraint on the active bone.

  * **frame_start** (_int in_ _[__-1048574_ _,__1048574_ _]__,__(__optional_ _)_) – Start Frame, First frame of path animation

  * **length** (_int in_ _[__0_ _,__1048574_ _]__,__(__optional_ _)_) – Length, Number of frames that path animation should take

bpy.ops.constraint.limitdistance_reset(_*_ , _constraint =''_, _owner
=OBJECT_)¶

    

Reset limiting distance for Limit Distance Constraint

Parameters:

    

  * **constraint** (_string_ _,__(__optional_ _,__never None_ _)_) – Constraint, Name of the constraint to edit

  * **owner** (enum in [`OBJECT`, `BONE`], (optional)) – 

Owner, The owner of this constraint

    * `OBJECT` Object – Edit a constraint on the active object.

    * `BONE` Bone – Edit a constraint on the active bone.

bpy.ops.constraint.move_down(_*_ , _constraint =''_, _owner =OBJECT_)¶

    

Move constraint down in constraint stack

Parameters:

    

  * **constraint** (_string_ _,__(__optional_ _,__never None_ _)_) – Constraint, Name of the constraint to edit

  * **owner** (enum in [`OBJECT`, `BONE`], (optional)) – 

Owner, The owner of this constraint

    * `OBJECT` Object – Edit a constraint on the active object.

    * `BONE` Bone – Edit a constraint on the active bone.

bpy.ops.constraint.move_to_index(_*_ , _constraint =''_, _owner =OBJECT_,
_index =0_)¶

    

Change the constraint’s position in the list so it evaluates after the set
number of others

Parameters:

    

  * **constraint** (_string_ _,__(__optional_ _,__never None_ _)_) – Constraint, Name of the constraint to edit

  * **owner** (enum in [`OBJECT`, `BONE`], (optional)) – 

Owner, The owner of this constraint

    * `OBJECT` Object – Edit a constraint on the active object.

    * `BONE` Bone – Edit a constraint on the active bone.

  * **index** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Index, The index to move the constraint to

bpy.ops.constraint.move_up(_*_ , _constraint =''_, _owner =OBJECT_)¶

    

Move constraint up in constraint stack

Parameters:

    

  * **constraint** (_string_ _,__(__optional_ _,__never None_ _)_) – Constraint, Name of the constraint to edit

  * **owner** (enum in [`OBJECT`, `BONE`], (optional)) – 

Owner, The owner of this constraint

    * `OBJECT` Object – Edit a constraint on the active object.

    * `BONE` Bone – Edit a constraint on the active bone.

bpy.ops.constraint.normalize_target_weights()¶

    

Normalize weights of all target bones

File:

    

[startup/bl_operators/constraint.py:61](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/constraint.py#L61)

bpy.ops.constraint.objectsolver_clear_inverse(_*_ , _constraint =''_, _owner
=OBJECT_)¶

    

Clear inverse correction for Object Solver constraint

Parameters:

    

  * **constraint** (_string_ _,__(__optional_ _,__never None_ _)_) – Constraint, Name of the constraint to edit

  * **owner** (enum in [`OBJECT`, `BONE`], (optional)) – 

Owner, The owner of this constraint

    * `OBJECT` Object – Edit a constraint on the active object.

    * `BONE` Bone – Edit a constraint on the active bone.

bpy.ops.constraint.objectsolver_set_inverse(_*_ , _constraint =''_, _owner
=OBJECT_)¶

    

Set inverse correction for Object Solver constraint

Parameters:

    

  * **constraint** (_string_ _,__(__optional_ _,__never None_ _)_) – Constraint, Name of the constraint to edit

  * **owner** (enum in [`OBJECT`, `BONE`], (optional)) – 

Owner, The owner of this constraint

    * `OBJECT` Object – Edit a constraint on the active object.

    * `BONE` Bone – Edit a constraint on the active bone.

bpy.ops.constraint.remove_target(_*_ , _index =0_)¶

    

Remove the target from the constraint

Parameters:

    

**index** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – index

File:

    

[startup/bl_operators/constraint.py:44](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/constraint.py#L44)

bpy.ops.constraint.stretchto_reset(_*_ , _constraint =''_, _owner =OBJECT_)¶

    

Reset original length of bone for Stretch To Constraint

Parameters:

    

  * **constraint** (_string_ _,__(__optional_ _,__never None_ _)_) – Constraint, Name of the constraint to edit

  * **owner** (enum in [`OBJECT`, `BONE`], (optional)) – 

Owner, The owner of this constraint

    * `OBJECT` Object – Edit a constraint on the active object.

    * `BONE` Bone – Edit a constraint on the active bone.

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

