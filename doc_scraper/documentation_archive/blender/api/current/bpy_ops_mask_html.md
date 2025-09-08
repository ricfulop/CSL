---
url: https://docs.blender.org/api/current/bpy.ops.mask.html
scraped_at: 2025-09-08T14:18:25.570318
title: Mask Operators¶
---

# Mask Operators¶

bpy.ops.mask.add_feather_vertex(_*_ , _location =(0.0, 0.0)_)¶

    

Add vertex to feather

Parameters:

    

**location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector
"mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location,
Location of vertex in normalized space

bpy.ops.mask.add_feather_vertex_slide(_*_ , _MASK_OT_add_feather_vertex
=None_, _MASK_OT_slide_point =None_)¶

    

Add new vertex to feather and slide it

Parameters:

    

  * **MASK_OT_add_feather_vertex** (`MASK_OT_add_feather_vertex`, (optional)) – Add Feather Vertex, Add vertex to feather

  * **MASK_OT_slide_point** (`MASK_OT_slide_point`, (optional)) – Slide Point, Slide control points

bpy.ops.mask.add_vertex(_*_ , _location =(0.0, 0.0)_)¶

    

Add vertex to active spline

Parameters:

    

**location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector
"mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location,
Location of vertex in normalized space

bpy.ops.mask.add_vertex_slide(_*_ , _MASK_OT_add_vertex =None_,
_MASK_OT_slide_point =None_)¶

    

Add new vertex and slide it

Parameters:

    

  * **MASK_OT_add_vertex** (`MASK_OT_add_vertex`, (optional)) – Add Vertex, Add vertex to active spline

  * **MASK_OT_slide_point** (`MASK_OT_slide_point`, (optional)) – Slide Point, Slide control points

bpy.ops.mask.copy_splines()¶

    

Copy the selected splines to the internal clipboard

bpy.ops.mask.cyclic_toggle()¶

    

Toggle cyclic for selected splines

bpy.ops.mask.delete(_*_ , _confirm =True_)¶

    

Delete selected control points or splines

Parameters:

    

**confirm** (_boolean_ _,__(__optional_ _)_) – Confirm, Prompt for
confirmation

bpy.ops.mask.duplicate()¶

    

Duplicate selected control points and segments between them

bpy.ops.mask.duplicate_move(_*_ , _MASK_OT_duplicate =None_,
_TRANSFORM_OT_translate =None_)¶

    

Duplicate mask and move

Parameters:

    

  * **MASK_OT_duplicate** (`MASK_OT_duplicate`, (optional)) – Duplicate Mask, Duplicate selected control points and segments between them

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.mask.feather_weight_clear()¶

    

Reset the feather weight to zero

bpy.ops.mask.handle_type_set(_*_ , _type =AUTO_)¶

    

Set type of handles for selected control points

Parameters:

    

**type** (enum in [`AUTO`, `VECTOR`, `ALIGNED`, `ALIGNED_DOUBLESIDE`, `FREE`],
(optional)) – Type, Spline type

bpy.ops.mask.hide_view_clear(_*_ , _select =True_)¶

    

Reveal temporarily hidden mask layers

Parameters:

    

**select** (_boolean_ _,__(__optional_ _)_) – Select

bpy.ops.mask.hide_view_set(_*_ , _unselected =False_)¶

    

Temporarily hide mask layers

Parameters:

    

**unselected** (_boolean_ _,__(__optional_ _)_) – Unselected, Hide unselected
rather than selected layers

bpy.ops.mask.layer_move(_*_ , _direction =UP_)¶

    

Move the active layer up/down in the list

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Direction, Direction to
move the active layer

bpy.ops.mask.layer_new(_*_ , _name =''_)¶

    

Add new mask layer for masking

Parameters:

    

**name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of new
mask layer

bpy.ops.mask.layer_remove()¶

    

Remove mask layer

bpy.ops.mask.new(_*_ , _name =''_)¶

    

Create new mask

Parameters:

    

**name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of new
mask

bpy.ops.mask.normals_make_consistent()¶

    

Recalculate the direction of selected handles

bpy.ops.mask.parent_clear()¶

    

Clear the mask’s parenting

bpy.ops.mask.parent_set()¶

    

Set the mask’s parenting

bpy.ops.mask.paste_splines()¶

    

Paste splines from the internal clipboard

bpy.ops.mask.primitive_circle_add(_*_ , _size =100.0_, _location =(0.0,
0.0)_)¶

    

Add new circle-shaped spline

Parameters:

    

  * **size** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Size, Size of new circle

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Location of new circle

bpy.ops.mask.primitive_square_add(_*_ , _size =100.0_, _location =(0.0,
0.0)_)¶

    

Add new square-shaped spline

Parameters:

    

  * **size** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Size, Size of new circle

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Location of new circle

bpy.ops.mask.select(_*_ , _extend =False_, _deselect =False_, _toggle =False_,
_deselect_all =False_, _select_passthrough =False_, _location =(0.0, 0.0)_)¶

    

Select spline points

Parameters:

    

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection instead of deselecting everything first

  * **deselect** (_boolean_ _,__(__optional_ _)_) – Deselect, Remove from selection

  * **toggle** (_boolean_ _,__(__optional_ _)_) – Toggle Selection, Toggle the selection

  * **deselect_all** (_boolean_ _,__(__optional_ _)_) – Deselect On Nothing, Deselect all when nothing under the cursor

  * **select_passthrough** (_boolean_ _,__(__optional_ _)_) – Only Select Unselected, Ignore the select action when the element is already selected

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Location of vertex in normalized space

bpy.ops.mask.select_all(_*_ , _action =TOGGLE_)¶

    

Change selection of all curve points

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.mask.select_box(_*_ , _xmin =0_, _xmax =0_, _ymin =0_, _ymax =0_,
_wait_for_input =True_, _mode =SET_)¶

    

Select curve points using box selection

Parameters:

    

  * **xmin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Min

  * **xmax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Max

  * **ymin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Min

  * **ymax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Max

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

  * **mode** (enum in [`SET`, `ADD`, `SUB`], (optional)) – 

Mode

    * `SET` Set – Set a new selection.

    * `ADD` Extend – Extend existing selection.

    * `SUB` Subtract – Subtract existing selection.

bpy.ops.mask.select_circle(_*_ , _x =0_, _y =0_, _radius =25_, _wait_for_input
=True_, _mode =SET_)¶

    

Select curve points using circle selection

Parameters:

    

  * **x** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X

  * **y** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y

  * **radius** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

  * **mode** (enum in [`SET`, `ADD`, `SUB`], (optional)) – 

Mode

    * `SET` Set – Set a new selection.

    * `ADD` Extend – Extend existing selection.

    * `SUB` Subtract – Subtract existing selection.

bpy.ops.mask.select_lasso(_*_ , _path =None_, _use_smooth_stroke =False_,
_smooth_stroke_factor =0.75_, _smooth_stroke_radius =35_, _mode =SET_)¶

    

Select curve points using lasso selection

Parameters:

    

  * **path** (`bpy_prop_collection` of `OperatorMousePath`, (optional)) – Path

  * **use_smooth_stroke** (_boolean_ _,__(__optional_ _)_) – Stabilize Stroke, Selection lags behind mouse and follows a smoother path

  * **smooth_stroke_factor** (_float in_ _[__0.5_ _,__0.99_ _]__,__(__optional_ _)_) – Smooth Stroke Factor, Higher values gives a smoother stroke

  * **smooth_stroke_radius** (_int in_ _[__10_ _,__200_ _]__,__(__optional_ _)_) – Smooth Stroke Radius, Minimum distance from last point before selection continues

  * **mode** (enum in [`SET`, `ADD`, `SUB`], (optional)) – 

Mode

    * `SET` Set – Set a new selection.

    * `ADD` Extend – Extend existing selection.

    * `SUB` Subtract – Subtract existing selection.

bpy.ops.mask.select_less()¶

    

Deselect spline points at the boundary of each selection region

bpy.ops.mask.select_linked()¶

    

Select all curve points linked to already selected ones

bpy.ops.mask.select_linked_pick(_*_ , _deselect =False_)¶

    

(De)select all points linked to the curve under the mouse cursor

Parameters:

    

**deselect** (_boolean_ _,__(__optional_ _)_) – Deselect

bpy.ops.mask.select_more()¶

    

Select more spline points connected to initial selection

bpy.ops.mask.shape_key_clear()¶

    

Remove mask shape keyframe for active mask layer at the current frame

bpy.ops.mask.shape_key_feather_reset()¶

    

Reset feather weights on all selected points animation values

bpy.ops.mask.shape_key_insert()¶

    

Insert mask shape keyframe for active mask layer at the current frame

bpy.ops.mask.shape_key_rekey(_*_ , _location =True_, _feather =True_)¶

    

Recalculate animation data on selected points for frames selected in the
dopesheet

Parameters:

    

  * **location** (_boolean_ _,__(__optional_ _)_) – Location

  * **feather** (_boolean_ _,__(__optional_ _)_) – Feather

bpy.ops.mask.slide_point(_*_ , _slide_feather =False_, _is_new_point =False_)¶

    

Slide control points

Parameters:

    

  * **slide_feather** (_boolean_ _,__(__optional_ _)_) – Slide Feather, First try to slide feather instead of vertex

  * **is_new_point** (_boolean_ _,__(__optional_ _)_) – Slide New Point, Newly created vertex is being slid

bpy.ops.mask.slide_spline_curvature()¶

    

Slide a point on the spline to define its curvature

bpy.ops.mask.switch_direction()¶

    

Switch direction of selected splines

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

