---
url: https://docs.blender.org/api/current/bpy.ops.paintcurve.html
scraped_at: 2025-09-08T14:18:34.608502
title: Paintcurve Operators¶
---

# Paintcurve Operators¶

bpy.ops.paintcurve.add_point(_*_ , _location =(0, 0)_)¶

    

Add New Paint Curve Point

Parameters:

    

**location** (_int array_ _of_ _2 items in_ _[__0_ _,__32767_
_]__,__(__optional_ _)_) – Location, Location of vertex in area space

bpy.ops.paintcurve.add_point_slide(_*_ , _PAINTCURVE_OT_add_point =None_,
_PAINTCURVE_OT_slide =None_)¶

    

Add new curve point and slide it

Parameters:

    

  * **PAINTCURVE_OT_add_point** (`PAINTCURVE_OT_add_point`, (optional)) – Add New Paint Curve Point, Add New Paint Curve Point

  * **PAINTCURVE_OT_slide** (`PAINTCURVE_OT_slide`, (optional)) – Slide Paint Curve Point, Select and slide paint curve point

bpy.ops.paintcurve.cursor()¶

    

Place cursor

bpy.ops.paintcurve.delete_point()¶

    

Remove Paint Curve Point

bpy.ops.paintcurve.draw()¶

    

Draw curve

bpy.ops.paintcurve.new()¶

    

Add new paint curve

bpy.ops.paintcurve.select(_*_ , _location =(0, 0)_, _toggle =False_, _extend
=False_)¶

    

Select a paint curve point

Parameters:

    

  * **location** (_int array_ _of_ _2 items in_ _[__0_ _,__32767_ _]__,__(__optional_ _)_) – Location, Location of vertex in area space

  * **toggle** (_boolean_ _,__(__optional_ _)_) – Toggle, (De)select all

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection

bpy.ops.paintcurve.slide(_*_ , _align =False_, _select =True_)¶

    

Select and slide paint curve point

Parameters:

    

  * **align** (_boolean_ _,__(__optional_ _)_) – Align Handles, Aligns opposite point handle during transform

  * **select** (_boolean_ _,__(__optional_ _)_) – Select, Attempt to select a point handle before transform

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

