---
url: https://docs.blender.org/api/current/bpy.ops.particle.html
scraped_at: 2025-09-08T14:18:36.610312
title: Particle Operators¶
---

# Particle Operators¶

bpy.ops.particle.brush_edit(_*_ , _stroke =None_, _pen_flip =False_)¶

    

Apply a stroke of brush to the particles

Parameters:

    

  * **stroke** (`bpy_prop_collection` of `OperatorStrokeElement`, (optional)) – Stroke

  * **pen_flip** (_boolean_ _,__(__optional_ _)_) – Pen Flip, Whether a tablet’s eraser mode is being used

bpy.ops.particle.connect_hair(_*_ , _all =False_)¶

    

Connect hair to the emitter mesh

Parameters:

    

**all** (_boolean_ _,__(__optional_ _)_) – All Hair, Connect all hair systems
to the emitter mesh

bpy.ops.particle.copy_particle_systems(_*_ , _space =OBJECT_,
_remove_target_particles =True_, _use_active =False_)¶

    

Copy particle systems from the active object to selected objects

Parameters:

    

  * **space** (enum in [`OBJECT`, `WORLD`], (optional)) – 

Space, Space transform for copying from one object to another

    * `OBJECT` Object – Copy inside each object’s local space.

    * `WORLD` World – Copy in world space.

  * **remove_target_particles** (_boolean_ _,__(__optional_ _)_) – Remove Target Particles, Remove particle systems on the target objects

  * **use_active** (_boolean_ _,__(__optional_ _)_) – Use Active, Use the active particle system from the context

bpy.ops.particle.delete(_*_ , _type =PARTICLE_)¶

    

Delete selected particles or keys

Parameters:

    

**type** (enum in [`PARTICLE`, `KEY`], (optional)) – Type, Delete a full
particle or only keys

bpy.ops.particle.disconnect_hair(_*_ , _all =False_)¶

    

Disconnect hair from the emitter mesh

Parameters:

    

**all** (_boolean_ _,__(__optional_ _)_) – All Hair, Disconnect all hair
systems from the emitter mesh

bpy.ops.particle.duplicate_particle_system(_*_ , _use_duplicate_settings
=False_)¶

    

Duplicate particle system within the active object

Parameters:

    

**use_duplicate_settings** (_boolean_ _,__(__optional_ _)_) – Duplicate
Settings, Duplicate settings as well, so the new particle system uses its own
settings

bpy.ops.particle.dupliob_copy()¶

    

Duplicate the current instance object

bpy.ops.particle.dupliob_move_down()¶

    

Move instance object down in the list

bpy.ops.particle.dupliob_move_up()¶

    

Move instance object up in the list

bpy.ops.particle.dupliob_refresh()¶

    

Refresh list of instance objects and their weights

bpy.ops.particle.dupliob_remove()¶

    

Remove the selected instance object

bpy.ops.particle.edited_clear()¶

    

Undo all edition performed on the particle system

bpy.ops.particle.hair_dynamics_preset_add(_*_ , _name =''_, _remove_name
=False_, _remove_active =False_)¶

    

Add or remove a Hair Dynamics Preset

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the preset, used to make the path name

  * **remove_name** (_boolean_ _,__(__optional_ _)_) – remove_name

  * **remove_active** (_boolean_ _,__(__optional_ _)_) – remove_active

File:

    

[startup/bl_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.particle.hide(_*_ , _unselected =False_)¶

    

Hide selected particles

Parameters:

    

**unselected** (_boolean_ _,__(__optional_ _)_) – Unselected, Hide unselected
rather than selected

bpy.ops.particle.mirror()¶

    

Duplicate and mirror the selected particles along the local X axis

bpy.ops.particle.new()¶

    

Add new particle settings

bpy.ops.particle.new_target()¶

    

Add a new particle target

bpy.ops.particle.particle_edit_toggle()¶

    

Toggle particle edit mode

bpy.ops.particle.rekey(_*_ , _keys_number =2_)¶

    

Change the number of keys of selected particles (root and tip keys included)

Parameters:

    

**keys_number** (_int in_ _[__2_ _,__inf_ _]__,__(__optional_ _)_) – Number of
Keys

bpy.ops.particle.remove_doubles(_*_ , _threshold =0.0002_)¶

    

Remove selected particles close enough of others

Parameters:

    

**threshold** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Merge
Distance, Threshold distance within which particles are removed

bpy.ops.particle.reveal(_*_ , _select =True_)¶

    

Show hidden particles

Parameters:

    

**select** (_boolean_ _,__(__optional_ _)_) – Select

bpy.ops.particle.select_all(_*_ , _action =TOGGLE_)¶

    

(De)select all particles’ keys

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.particle.select_less()¶

    

Deselect boundary selected keys of each particle

bpy.ops.particle.select_linked()¶

    

Select all keys linked to already selected ones

bpy.ops.particle.select_linked_pick(_*_ , _deselect =False_, _location =(0,
0)_)¶

    

Select nearest particle from mouse pointer

Parameters:

    

  * **deselect** (_boolean_ _,__(__optional_ _)_) – Deselect, Deselect linked keys rather than selecting them

  * **location** (_int array_ _of_ _2 items in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Location

bpy.ops.particle.select_more()¶

    

Select keys linked to boundary selected keys of each particle

bpy.ops.particle.select_random(_*_ , _ratio =0.5_, _seed =0_, _action
=SELECT_, _type =HAIR_)¶

    

Select a randomly distributed set of hair or points

Parameters:

    

  * **ratio** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Ratio, Portion of items to select randomly

  * **seed** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Random Seed, Seed for the random number generator

  * **action** (enum in [`SELECT`, `DESELECT`], (optional)) – 

Action, Selection action to execute

    * `SELECT` Select – Select all elements.

    * `DESELECT` Deselect – Deselect all elements.

  * **type** (enum in [`HAIR`, `POINTS`], (optional)) – Type, Select either hair or points

bpy.ops.particle.select_roots(_*_ , _action =SELECT_)¶

    

Select roots of all visible particles

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.particle.select_tips(_*_ , _action =SELECT_)¶

    

Select tips of all visible particles

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.particle.shape_cut()¶

    

Cut hair to conform to the set shape object

bpy.ops.particle.subdivide()¶

    

Subdivide selected particles segments (adds keys)

bpy.ops.particle.target_move_down()¶

    

Move particle target down in the list

bpy.ops.particle.target_move_up()¶

    

Move particle target up in the list

bpy.ops.particle.target_remove()¶

    

Remove the selected particle target

bpy.ops.particle.unify_length()¶

    

Make selected hair the same length

bpy.ops.particle.weight_set(_*_ , _factor =1.0_)¶

    

Set the weight of selected keys

Parameters:

    

**factor** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Factor,
Interpolation factor between current brush weight, and keys’ weights

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

