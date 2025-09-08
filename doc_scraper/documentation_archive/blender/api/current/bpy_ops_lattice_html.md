---
url: https://docs.blender.org/api/current/bpy.ops.lattice.html
scraped_at: 2025-09-08T14:18:23.523755
title: Lattice Operators¶
---

# Lattice Operators¶

bpy.ops.lattice.flip(_*_ , _axis =U_)¶

    

Mirror all control points without inverting the lattice deform

Parameters:

    

**axis** (enum in [`U`, `V`, `W`], (optional)) – Flip Axis, Coordinates along
this axis get flipped

bpy.ops.lattice.make_regular()¶

    

Set UVW control points a uniform distance apart

bpy.ops.lattice.select_all(_*_ , _action =TOGGLE_)¶

    

Change selection of all UVW control points

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.lattice.select_less()¶

    

Deselect vertices at the boundary of each selection region

bpy.ops.lattice.select_mirror(_*_ , _axis ={'X'}_, _extend =False_)¶

    

Select mirrored lattice points

Parameters:

    

  * **axis** (enum set in [Axis Flag Xyz Items](bpy_types_enum_items/axis_flag_xyz_items.html#rna-enum-axis-flag-xyz-items), (optional)) – Axis

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend the selection

bpy.ops.lattice.select_more()¶

    

Select vertex directly linked to already selected ones

bpy.ops.lattice.select_random(_*_ , _ratio =0.5_, _seed =0_, _action
=SELECT_)¶

    

Randomly select UVW control points

Parameters:

    

  * **ratio** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Ratio, Portion of items to select randomly

  * **seed** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Random Seed, Seed for the random number generator

  * **action** (enum in [`SELECT`, `DESELECT`], (optional)) – 

Action, Selection action to execute

    * `SELECT` Select – Select all elements.

    * `DESELECT` Deselect – Deselect all elements.

bpy.ops.lattice.select_ungrouped(_*_ , _extend =False_)¶

    

Select vertices without a group

Parameters:

    

**extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend the selection

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

