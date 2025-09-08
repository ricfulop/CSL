---
url: https://docs.blender.org/api/current/bpy.ops.curve.html
scraped_at: 2025-09-08T14:18:02.504820
title: Curve Operators¶
---

# Curve Operators¶

bpy.ops.curve.cyclic_toggle(_*_ , _direction =CYCLIC_U_)¶

    

Make active spline closed/opened loop

Parameters:

    

**direction** (enum in [`CYCLIC_U`, `CYCLIC_V`], (optional)) – Direction,
Direction to make surface cyclic in

bpy.ops.curve.de_select_first()¶

    

(De)select first of visible part of each NURBS

bpy.ops.curve.de_select_last()¶

    

(De)select last of visible part of each NURBS

bpy.ops.curve.decimate(_*_ , _ratio =1.0_)¶

    

Simplify selected curves

Parameters:

    

**ratio** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Ratio

bpy.ops.curve.delete(_*_ , _type =VERT_)¶

    

Delete selected control points or segments

Parameters:

    

**type** (enum in [`VERT`, `SEGMENT`], (optional)) – Type, Which elements to
delete

bpy.ops.curve.dissolve_verts()¶

    

Delete selected control points, correcting surrounding handles

bpy.ops.curve.draw(_*_ , _error_threshold =0.0_, _fit_method =REFIT_,
_corner_angle =1.22173_, _use_cyclic =True_, _stroke =None_, _wait_for_input
=True_)¶

    

Draw a freehand spline

Parameters:

    

  * **error_threshold** (_float in_ _[__0_ _,__10_ _]__,__(__optional_ _)_) – Error, Error distance threshold (in object units)

  * **fit_method** (enum in [Curve Fit Method Items](bpy_types_enum_items/curve_fit_method_items.html#rna-enum-curve-fit-method-items), (optional)) – Fit Method

  * **corner_angle** (_float in_ _[__0_ _,__3.14159_ _]__,__(__optional_ _)_) – Corner Angle

  * **use_cyclic** (_boolean_ _,__(__optional_ _)_) – Cyclic

  * **stroke** (`bpy_prop_collection` of `OperatorStrokeElement`, (optional)) – Stroke

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

bpy.ops.curve.duplicate()¶

    

Duplicate selected control points

bpy.ops.curve.duplicate_move(_*_ , _CURVE_OT_duplicate =None_,
_TRANSFORM_OT_translate =None_)¶

    

Duplicate curve and move

Parameters:

    

  * **CURVE_OT_duplicate** (`CURVE_OT_duplicate`, (optional)) – Duplicate Curve, Duplicate selected control points

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.curve.extrude(_*_ , _mode =TRANSLATION_)¶

    

Extrude selected control point(s)

Parameters:

    

**mode** (enum in [Transform Mode Type
Items](bpy_types_enum_items/transform_mode_type_items.html#rna-enum-transform-
mode-type-items), (optional)) – Mode

bpy.ops.curve.extrude_move(_*_ , _CURVE_OT_extrude =None_,
_TRANSFORM_OT_translate =None_)¶

    

Extrude curve and move result

Parameters:

    

  * **CURVE_OT_extrude** (`CURVE_OT_extrude`, (optional)) – Extrude, Extrude selected control point(s)

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.curve.handle_type_set(_*_ , _type =AUTOMATIC_)¶

    

Set type of handles for selected control points

Parameters:

    

**type** (enum in [`AUTOMATIC`, `VECTOR`, `ALIGNED`, `FREE_ALIGN`,
`TOGGLE_FREE_ALIGN`], (optional)) – Type, Spline type

bpy.ops.curve.hide(_*_ , _unselected =False_)¶

    

Hide (un)selected control points

Parameters:

    

**unselected** (_boolean_ _,__(__optional_ _)_) – Unselected, Hide unselected
rather than selected

bpy.ops.curve.make_segment()¶

    

Join two curves by their selected ends

bpy.ops.curve.match_texture_space()¶

    

Match texture space to object’s bounding box

bpy.ops.curve.normals_make_consistent(_*_ , _calc_length =False_)¶

    

Recalculate the direction of selected handles

Parameters:

    

**calc_length** (_boolean_ _,__(__optional_ _)_) – Length, Recalculate handle
length

bpy.ops.curve.pen(_*_ , _extend =False_, _deselect =False_, _toggle =False_,
_deselect_all =False_, _select_passthrough =False_, _extrude_point =False_,
_extrude_handle =VECTOR_, _delete_point =False_, _insert_point =False_,
_move_segment =False_, _select_point =False_, _move_point =False_,
_close_spline =True_, _close_spline_method =OFF_, _toggle_vector =False_,
_cycle_handle_type =False_)¶

    

Construct and edit splines

Parameters:

    

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection instead of deselecting everything first

  * **deselect** (_boolean_ _,__(__optional_ _)_) – Deselect, Remove from selection

  * **toggle** (_boolean_ _,__(__optional_ _)_) – Toggle Selection, Toggle the selection

  * **deselect_all** (_boolean_ _,__(__optional_ _)_) – Deselect On Nothing, Deselect all when nothing under the cursor

  * **select_passthrough** (_boolean_ _,__(__optional_ _)_) – Only Select Unselected, Ignore the select action when the element is already selected

  * **extrude_point** (_boolean_ _,__(__optional_ _)_) – Extrude Point, Add a point connected to the last selected point

  * **extrude_handle** (enum in [`AUTO`, `VECTOR`], (optional)) – Extrude Handle Type, Type of the extruded handle

  * **delete_point** (_boolean_ _,__(__optional_ _)_) – Delete Point, Delete an existing point

  * **insert_point** (_boolean_ _,__(__optional_ _)_) – Insert Point, Insert Point into a curve segment

  * **move_segment** (_boolean_ _,__(__optional_ _)_) – Move Segment, Delete an existing point

  * **select_point** (_boolean_ _,__(__optional_ _)_) – Select Point, Select a point or its handles

  * **move_point** (_boolean_ _,__(__optional_ _)_) – Move Point, Move a point or its handles

  * **close_spline** (_boolean_ _,__(__optional_ _)_) – Close Spline, Make a spline cyclic by clicking endpoints

  * **close_spline_method** (enum in [`OFF`, `ON_PRESS`, `ON_CLICK`], (optional)) – 

Close Spline Method, The condition for close spline to activate

    * `OFF` None.

    * `ON_PRESS` On Press – Move handles after closing the spline.

    * `ON_CLICK` On Click – Spline closes on release if not dragged.

  * **toggle_vector** (_boolean_ _,__(__optional_ _)_) – Toggle Vector, Toggle between Vector and Auto handles

  * **cycle_handle_type** (_boolean_ _,__(__optional_ _)_) – Cycle Handle Type, Cycle between all four handle types

bpy.ops.curve.primitive_bezier_circle_add(_*_ , _radius =1.0_, _enter_editmode
=False_, _align =WORLD_, _location =(0.0, 0.0, 0.0)_, _rotation =(0.0, 0.0,
0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Construct a Bézier Circle

Parameters:

    

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.curve.primitive_bezier_curve_add(_*_ , _radius =1.0_, _enter_editmode
=False_, _align =WORLD_, _location =(0.0, 0.0, 0.0)_, _rotation =(0.0, 0.0,
0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Construct a Bézier Curve

Parameters:

    

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.curve.primitive_nurbs_circle_add(_*_ , _radius =1.0_, _enter_editmode
=False_, _align =WORLD_, _location =(0.0, 0.0, 0.0)_, _rotation =(0.0, 0.0,
0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Construct a Nurbs Circle

Parameters:

    

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.curve.primitive_nurbs_curve_add(_*_ , _radius =1.0_, _enter_editmode
=False_, _align =WORLD_, _location =(0.0, 0.0, 0.0)_, _rotation =(0.0, 0.0,
0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Construct a Nurbs Curve

Parameters:

    

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.curve.primitive_nurbs_path_add(_*_ , _radius =1.0_, _enter_editmode
=False_, _align =WORLD_, _location =(0.0, 0.0, 0.0)_, _rotation =(0.0, 0.0,
0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Construct a Path

Parameters:

    

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.curve.radius_set(_*_ , _radius =1.0_)¶

    

Set per-point radius which is used for bevel tapering

Parameters:

    

**radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

bpy.ops.curve.reveal(_*_ , _select =True_)¶

    

Reveal hidden control points

Parameters:

    

**select** (_boolean_ _,__(__optional_ _)_) – Select

bpy.ops.curve.select_all(_*_ , _action =TOGGLE_)¶

    

(De)select all control points

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.curve.select_less()¶

    

Deselect control points at the boundary of each selection region

bpy.ops.curve.select_linked()¶

    

Select all control points linked to the current selection

bpy.ops.curve.select_linked_pick(_*_ , _deselect =False_)¶

    

Select all control points linked to already selected ones

Parameters:

    

**deselect** (_boolean_ _,__(__optional_ _)_) – Deselect, Deselect linked
control points rather than selecting them

bpy.ops.curve.select_more()¶

    

Select control points at the boundary of each selection region

bpy.ops.curve.select_next()¶

    

Select control points following already selected ones along the curves

bpy.ops.curve.select_nth(_*_ , _skip =1_, _nth =1_, _offset =0_)¶

    

Deselect every Nth point starting from the active one

Parameters:

    

  * **skip** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Deselected, Number of deselected elements in the repetitive sequence

  * **nth** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Selected, Number of selected elements in the repetitive sequence

  * **offset** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Offset, Offset from the starting point

bpy.ops.curve.select_previous()¶

    

Select control points preceding already selected ones along the curves

bpy.ops.curve.select_random(_*_ , _ratio =0.5_, _seed =0_, _action =SELECT_)¶

    

Randomly select some control points

Parameters:

    

  * **ratio** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Ratio, Portion of items to select randomly

  * **seed** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Random Seed, Seed for the random number generator

  * **action** (enum in [`SELECT`, `DESELECT`], (optional)) – 

Action, Selection action to execute

    * `SELECT` Select – Select all elements.

    * `DESELECT` Deselect – Deselect all elements.

bpy.ops.curve.select_row()¶

    

Select a row of control points including active one. Successive use on the
same point switches between U/V directions

bpy.ops.curve.select_similar(_*_ , _type =WEIGHT_, _compare =EQUAL_,
_threshold =0.1_)¶

    

Select similar curve points by property type

Parameters:

    

  * **type** (enum in [`TYPE`, `RADIUS`, `WEIGHT`, `DIRECTION`], (optional)) – Type

  * **compare** (enum in [`EQUAL`, `GREATER`, `LESS`], (optional)) – Compare

  * **threshold** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Threshold

bpy.ops.curve.separate()¶

    

Separate selected points from connected unselected points into a new object

bpy.ops.curve.shade_flat()¶

    

Set shading to flat

bpy.ops.curve.shade_smooth()¶

    

Set shading to smooth

bpy.ops.curve.shortest_path_pick()¶

    

Select shortest path between two selections

bpy.ops.curve.smooth()¶

    

Flatten angles of selected points

bpy.ops.curve.smooth_radius()¶

    

Interpolate radii of selected points

bpy.ops.curve.smooth_tilt()¶

    

Interpolate tilt of selected points

bpy.ops.curve.smooth_weight()¶

    

Interpolate weight of selected points

bpy.ops.curve.spin(_*_ , _center =(0.0, 0.0, 0.0)_, _axis =(0.0, 0.0, 0.0)_)¶

    

Extrude selected boundary row around pivot point and current view axis

Parameters:

    

  * **center** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Center, Center in global view space

  * **axis** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-1, 1], (optional)) – Axis, Axis in global view space

bpy.ops.curve.spline_type_set(_*_ , _type =POLY_, _use_handles =False_)¶

    

Set type of active spline

Parameters:

    

  * **type** (enum in [`POLY`, `BEZIER`, `NURBS`], (optional)) – Type, Spline type

  * **use_handles** (_boolean_ _,__(__optional_ _)_) – Handles, Use handles when converting Bézier curves into polygons

bpy.ops.curve.spline_weight_set(_*_ , _weight =1.0_)¶

    

Set softbody goal weight for selected points

Parameters:

    

**weight** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Weight

bpy.ops.curve.split()¶

    

Split off selected points from connected unselected points

bpy.ops.curve.subdivide(_*_ , _number_cuts =1_)¶

    

Subdivide selected segments

Parameters:

    

**number_cuts** (_int in_ _[__1_ _,__1000_ _]__,__(__optional_ _)_) – Number
of Cuts

bpy.ops.curve.switch_direction()¶

    

Switch direction of selected splines

bpy.ops.curve.tilt_clear()¶

    

Clear the tilt of selected control points

bpy.ops.curve.vertex_add(_*_ , _location =(0.0, 0.0, 0.0)_)¶

    

Add a new control point (linked to only selected end-curve one, if any)

Parameters:

    

**location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector
"mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location,
Location to add new vertex at

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

