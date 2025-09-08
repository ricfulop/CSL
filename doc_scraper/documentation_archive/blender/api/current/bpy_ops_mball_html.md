---
url: https://docs.blender.org/api/current/bpy.ops.mball.html
scraped_at: 2025-09-08T14:18:27.649630
title: Mball Operators¶
---

# Mball Operators¶

bpy.ops.mball.delete_metaelems(_*_ , _confirm =True_)¶

    

Delete selected metaball element(s)

Parameters:

    

**confirm** (_boolean_ _,__(__optional_ _)_) – Confirm, Prompt for
confirmation

bpy.ops.mball.duplicate_metaelems()¶

    

Duplicate selected metaball element(s)

bpy.ops.mball.duplicate_move(_*_ , _MBALL_OT_duplicate_metaelems =None_,
_TRANSFORM_OT_translate =None_)¶

    

Make copies of the selected metaball elements and move them

Parameters:

    

  * **MBALL_OT_duplicate_metaelems** (`MBALL_OT_duplicate_metaelems`, (optional)) – Duplicate Metaball Elements, Duplicate selected metaball element(s)

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.mball.hide_metaelems(_*_ , _unselected =False_)¶

    

Hide (un)selected metaball element(s)

Parameters:

    

**unselected** (_boolean_ _,__(__optional_ _)_) – Unselected, Hide unselected
rather than selected

bpy.ops.mball.reveal_metaelems(_*_ , _select =True_)¶

    

Reveal all hidden metaball elements

Parameters:

    

**select** (_boolean_ _,__(__optional_ _)_) – Select

bpy.ops.mball.select_all(_*_ , _action =TOGGLE_)¶

    

Change selection of all metaball elements

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.mball.select_random_metaelems(_*_ , _ratio =0.5_, _seed =0_, _action
=SELECT_)¶

    

Randomly select metaball elements

Parameters:

    

  * **ratio** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Ratio, Portion of items to select randomly

  * **seed** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Random Seed, Seed for the random number generator

  * **action** (enum in [`SELECT`, `DESELECT`], (optional)) – 

Action, Selection action to execute

    * `SELECT` Select – Select all elements.

    * `DESELECT` Deselect – Deselect all elements.

bpy.ops.mball.select_similar(_*_ , _type =TYPE_, _threshold =0.1_)¶

    

Select similar metaballs by property types

Parameters:

    

  * **type** (enum in [`TYPE`, `RADIUS`, `STIFFNESS`, `ROTATION`], (optional)) – Type

  * **threshold** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Threshold

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

