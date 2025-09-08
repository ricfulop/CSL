---
url: https://docs.blender.org/api/current/bpy.ops.pointcloud.html
scraped_at: 2025-09-08T14:18:37.567489
title: Pointcloud Operators¶
---

# Pointcloud Operators¶

bpy.ops.pointcloud.attribute_set(_*_ , _value_float =0.0_,
_value_float_vector_2d =(0.0, 0.0)_, _value_float_vector_3d =(0.0, 0.0, 0.0)_,
_value_int =0_, _value_int_vector_2d =(0, 0)_, _value_color =(1.0, 1.0, 1.0,
1.0)_, _value_bool =False_)¶

    

Set values of the active attribute for selected elements

Parameters:

    

  * **value_float** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Value

  * **value_float_vector_2d** (_float array_ _of_ _2 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Value

  * **value_float_vector_3d** (_float array_ _of_ _3 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Value

  * **value_int** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Value

  * **value_int_vector_2d** (_int array_ _of_ _2 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Value

  * **value_color** (_float array_ _of_ _4 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Value

  * **value_bool** (_boolean_ _,__(__optional_ _)_) – Value

bpy.ops.pointcloud.delete()¶

    

Remove selected points

bpy.ops.pointcloud.duplicate()¶

    

Copy selected points

bpy.ops.pointcloud.duplicate_move(_*_ , _POINTCLOUD_OT_duplicate =None_,
_TRANSFORM_OT_translate =None_)¶

    

Make copies of selected elements and move them

Parameters:

    

  * **POINTCLOUD_OT_duplicate** (`POINTCLOUD_OT_duplicate`, (optional)) – Duplicate, Copy selected points

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.pointcloud.select_all(_*_ , _action =TOGGLE_)¶

    

(De)select all point cloud

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.pointcloud.select_random(_*_ , _seed =0_, _probability =0.5_)¶

    

Randomizes existing selection or create new random selection

Parameters:

    

  * **seed** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Seed, Source of randomness

  * **probability** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Probability, Chance of every point being included in the selection

bpy.ops.pointcloud.separate()¶

    

Separate selected geometry into a new point cloud

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

