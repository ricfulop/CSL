---
url: https://docs.blender.org/api/current/bpy.ops.sculpt_curves.html
scraped_at: 2025-09-08T14:18:48.636639
title: Sculpt Curves Operators¶
---

# Sculpt Curves Operators¶

bpy.ops.sculpt_curves.brush_stroke(_*_ , _stroke =None_, _mode =NORMAL_,
_pen_flip =False_)¶

    

Sculpt curves using a brush

Parameters:

    

  * **stroke** (`bpy_prop_collection` of `OperatorStrokeElement`, (optional)) – Stroke

  * **mode** (enum in [`NORMAL`, `INVERT`, `SMOOTH`, `ERASE`], (optional)) – 

Stroke Mode, Action taken when a paint stroke is made

    * `NORMAL` Regular – Apply brush normally.

    * `INVERT` Invert – Invert action of brush for duration of stroke.

    * `SMOOTH` Smooth – Switch brush to smooth mode for duration of stroke.

    * `ERASE` Erase – Switch brush to erase mode for duration of stroke.

  * **pen_flip** (_boolean_ _,__(__optional_ _)_) – Pen Flip, Whether a tablet’s eraser mode is being used

bpy.ops.sculpt_curves.min_distance_edit()¶

    

Change the minimum distance used by the density brush

bpy.ops.sculpt_curves.select_grow(_*_ , _distance =0.1_)¶

    

Select curves which are close to curves that are selected already

Parameters:

    

**distance** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) –
Distance, By how much to grow the selection

bpy.ops.sculpt_curves.select_random(_*_ , _seed =0_, _partial =False_,
_probability =0.5_, _min =0.0_, _constant_per_curve =True_)¶

    

Randomizes existing selection or create new random selection

Parameters:

    

  * **seed** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Seed, Source of randomness

  * **partial** (_boolean_ _,__(__optional_ _)_) – Partial, Allow points or curves to be selected partially

  * **probability** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Probability, Chance of every point or curve being included in the selection

  * **min** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Min, Minimum value for the random selection

  * **constant_per_curve** (_boolean_ _,__(__optional_ _)_) – Constant per Curve, The generated random number is the same for every control point of a curve

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

