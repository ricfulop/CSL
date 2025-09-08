---
url: https://docs.blender.org/api/current/bpy.ops.rigidbody.html
scraped_at: 2025-09-08T14:18:43.569749
title: Rigidbody Operators¶
---

# Rigidbody Operators¶

bpy.ops.rigidbody.bake_to_keyframes(_*_ , _frame_start =1_, _frame_end =250_,
_step =1_)¶

    

Bake rigid body transformations of selected objects to keyframes

Parameters:

    

  * **frame_start** (_int in_ _[__0_ _,__300000_ _]__,__(__optional_ _)_) – Start Frame, Start frame for baking

  * **frame_end** (_int in_ _[__1_ _,__300000_ _]__,__(__optional_ _)_) – End Frame, End frame for baking

  * **step** (_int in_ _[__1_ _,__120_ _]__,__(__optional_ _)_) – Frame Step, Frame Step

File:

    

[startup/bl_operators/rigidbody.py:108](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/rigidbody.py#L108)

bpy.ops.rigidbody.connect(_*_ , _con_type =FIXED_, _pivot_type =CENTER_,
_connection_pattern =SELECTED_TO_ACTIVE_)¶

    

Create rigid body constraints between selected rigid bodies

Parameters:

    

  * **con_type** (enum in [`FIXED`, `POINT`, `HINGE`, `SLIDER`, `PISTON`, `GENERIC`, `GENERIC_SPRING`, `MOTOR`], (optional)) – 

Type, Type of generated constraint

    * `FIXED` Fixed – Glue rigid bodies together.

    * `POINT` Point – Constrain rigid bodies to move around common pivot point.

    * `HINGE` Hinge – Restrict rigid body rotation to one axis.

    * `SLIDER` Slider – Restrict rigid body translation to one axis.

    * `PISTON` Piston – Restrict rigid body translation and rotation to one axis.

    * `GENERIC` Generic – Restrict translation and rotation to specified axes.

    * `GENERIC_SPRING` Generic Spring – Restrict translation and rotation to specified axes with springs.

    * `MOTOR` Motor – Drive rigid body around or along an axis.

  * **pivot_type** (enum in [`CENTER`, `ACTIVE`, `SELECTED`], (optional)) – 

Location, Constraint pivot location

    * `CENTER` Center – Pivot location is between the constrained rigid bodies.

    * `ACTIVE` Active – Pivot location is at the active object position.

    * `SELECTED` Selected – Pivot location is at the selected object position.

  * **connection_pattern** (enum in [`SELECTED_TO_ACTIVE`, `CHAIN_DISTANCE`], (optional)) – 

Connection Pattern, Pattern used to connect objects

    * `SELECTED_TO_ACTIVE` Selected to Active – Connect selected objects to the active object.

    * `CHAIN_DISTANCE` Chain by Distance – Connect objects as a chain based on distance, starting at the active object.

File:

    

[startup/bl_operators/rigidbody.py:270](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/rigidbody.py#L270)

bpy.ops.rigidbody.constraint_add(_*_ , _type =FIXED_)¶

    

Add Rigid Body Constraint to active object

Parameters:

    

**type** (enum in [Rigidbody Constraint Type
Items](bpy_types_enum_items/rigidbody_constraint_type_items.html#rna-enum-
rigidbody-constraint-type-items), (optional)) – Rigid Body Constraint Type

bpy.ops.rigidbody.constraint_remove()¶

    

Remove Rigid Body Constraint from Object

bpy.ops.rigidbody.mass_calculate(_*_ , _material =DEFAULT_, _density =1.0_)¶

    

Automatically calculate mass values for Rigid Body Objects based on volume

Parameters:

    

  * **material** (enum in [`DEFAULT`], (optional)) – Material Preset, Type of material that objects are made of (determines material density)

  * **density** (_float in_ _[__1.17549e-38_ _,__inf_ _]__,__(__optional_ _)_) – Density, Density value (kg/m^3), allows custom value if the ‘Custom’ preset is used

bpy.ops.rigidbody.object_add(_*_ , _type =ACTIVE_)¶

    

Add active object as Rigid Body

Parameters:

    

**type** (enum in [Rigidbody Object Type
Items](bpy_types_enum_items/rigidbody_object_type_items.html#rna-enum-
rigidbody-object-type-items), (optional)) – Rigid Body Type

bpy.ops.rigidbody.object_remove()¶

    

Remove Rigid Body settings from Object

bpy.ops.rigidbody.object_settings_copy()¶

    

Copy Rigid Body settings from active object to selected

File:

    

[startup/bl_operators/rigidbody.py:45](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/rigidbody.py#L45)

bpy.ops.rigidbody.objects_add(_*_ , _type =ACTIVE_)¶

    

Add selected objects as Rigid Bodies

Parameters:

    

**type** (enum in [Rigidbody Object Type
Items](bpy_types_enum_items/rigidbody_object_type_items.html#rna-enum-
rigidbody-object-type-items), (optional)) – Rigid Body Type

bpy.ops.rigidbody.objects_remove()¶

    

Remove selected objects from Rigid Body simulation

bpy.ops.rigidbody.shape_change(_*_ , _type =MESH_)¶

    

Change collision shapes for selected Rigid Body Objects

Parameters:

    

**type** (enum in [Rigidbody Object Shape
Items](bpy_types_enum_items/rigidbody_object_shape_items.html#rna-enum-
rigidbody-object-shape-items), (optional)) – Rigid Body Shape

bpy.ops.rigidbody.world_add()¶

    

Add Rigid Body simulation world to the current scene

bpy.ops.rigidbody.world_remove()¶

    

Remove Rigid Body simulation world from the current scene

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

