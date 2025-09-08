---
url: https://docs.blender.org/api/current/bpy.ops.action.html
scraped_at: 2025-09-08T14:17:48.426074
title: Action Operators¶
---

# Action Operators¶

bpy.ops.action.bake_keys()¶

    

Add keyframes on every frame between the selected keyframes

bpy.ops.action.clean(_*_ , _threshold =0.001_, _channels =False_)¶

    

Simplify F-Curves by removing closely spaced keyframes

Parameters:

    

  * **threshold** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Threshold

  * **channels** (_boolean_ _,__(__optional_ _)_) – Channels

bpy.ops.action.clickselect(_*_ , _wait_to_deselect_others =False_, _mouse_x
=0_, _mouse_y =0_, _extend =False_, _deselect_all =False_, _column =False_,
_channel =False_)¶

    

Select keyframes by clicking on them

Parameters:

    

  * **wait_to_deselect_others** (_boolean_ _,__(__optional_ _)_) – Wait to Deselect Others

  * **mouse_x** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Mouse X

  * **mouse_y** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Mouse Y

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend Select, Toggle keyframe selection instead of leaving newly selected keyframes only

  * **deselect_all** (_boolean_ _,__(__optional_ _)_) – Deselect On Nothing, Deselect all when nothing under the cursor

  * **column** (_boolean_ _,__(__optional_ _)_) – Column Select, Select all keyframes that occur on the same frame as the one under the mouse

  * **channel** (_boolean_ _,__(__optional_ _)_) – Only Channel, Select all the keyframes in the channel under the mouse

bpy.ops.action.copy()¶

    

Copy selected keyframes to the internal clipboard

bpy.ops.action.delete(_*_ , _confirm =True_)¶

    

Remove all selected keyframes

Parameters:

    

**confirm** (_boolean_ _,__(__optional_ _)_) – Confirm, Prompt for
confirmation

bpy.ops.action.duplicate()¶

    

Make a copy of all selected keyframes

bpy.ops.action.duplicate_move(_*_ , _ACTION_OT_duplicate =None_,
_TRANSFORM_OT_transform =None_)¶

    

Make a copy of all selected keyframes and move them

Parameters:

    

  * **ACTION_OT_duplicate** (`ACTION_OT_duplicate`, (optional)) – Duplicate Keyframes, Make a copy of all selected keyframes

  * **TRANSFORM_OT_transform** (`TRANSFORM_OT_transform`, (optional)) – Transform, Transform selected items by mode type

bpy.ops.action.easing_type(_*_ , _type =AUTO_)¶

    

Set easing type for the F-Curve segments starting from the selected keyframes

Parameters:

    

**type** (enum in [Beztriple Interpolation Easing
Items](bpy_types_enum_items/beztriple_interpolation_easing_items.html#rna-
enum-beztriple-interpolation-easing-items), (optional)) – Type

bpy.ops.action.extrapolation_type(_*_ , _type =CONSTANT_)¶

    

Set extrapolation mode for selected F-Curves

Parameters:

    

**type** (enum in [`CONSTANT`, `LINEAR`, `MAKE_CYCLIC`, `CLEAR_CYCLIC`],
(optional)) –

Type

  * `CONSTANT` Constant Extrapolation – Values on endpoint keyframes are held.

  * `LINEAR` Linear Extrapolation – Straight-line slope of end segments are extended past the endpoint keyframes.

  * `MAKE_CYCLIC` Make Cyclic (F-Modifier) – Add Cycles F-Modifier if one doesn’t exist already.

  * `CLEAR_CYCLIC` Clear Cyclic (F-Modifier) – Remove Cycles F-Modifier if not needed anymore.

bpy.ops.action.frame_jump()¶

    

Set the current frame to the average frame value of selected keyframes

bpy.ops.action.handle_type(_*_ , _type =FREE_)¶

    

Set type of handle for selected keyframes

Parameters:

    

**type** (enum in [Keyframe Handle Type
Items](bpy_types_enum_items/keyframe_handle_type_items.html#rna-enum-keyframe-
handle-type-items), (optional)) – Type

bpy.ops.action.interpolation_type(_*_ , _type =CONSTANT_)¶

    

Set interpolation mode for the F-Curve segments starting from the selected
keyframes

Parameters:

    

**type** (enum in [Beztriple Interpolation Mode
Items](bpy_types_enum_items/beztriple_interpolation_mode_items.html#rna-enum-
beztriple-interpolation-mode-items), (optional)) – Type

bpy.ops.action.keyframe_insert(_*_ , _type =ALL_)¶

    

Insert keyframes for the specified channels

Parameters:

    

**type** (enum in [`ALL`, `SEL`, `GROUP`], (optional)) – Type

bpy.ops.action.keyframe_type(_*_ , _type =KEYFRAME_)¶

    

Set type of keyframe for the selected keyframes

Parameters:

    

**type** (enum in [Beztriple Keyframe Type
Items](bpy_types_enum_items/beztriple_keyframe_type_items.html#rna-enum-
beztriple-keyframe-type-items), (optional)) – Type

bpy.ops.action.layer_next()¶

    

Switch to editing action in animation layer above the current action in the
NLA Stack

bpy.ops.action.layer_prev()¶

    

Switch to editing action in animation layer below the current action in the
NLA Stack

bpy.ops.action.markers_make_local()¶

    

Move selected scene markers to the active Action as local ‘pose’ markers

bpy.ops.action.mirror(_*_ , _type =CFRA_)¶

    

Flip selected keyframes over the selected mirror line

Parameters:

    

**type** (enum in [`CFRA`, `XAXIS`, `MARKER`], (optional)) –

Type

  * `CFRA` By Times Over Current Frame – Flip times of selected keyframes using the current frame as the mirror line.

  * `XAXIS` By Values Over Zero Value – Flip values of selected keyframes (i.e. negative values become positive, and vice versa).

  * `MARKER` By Times Over First Selected Marker – Flip times of selected keyframes using the first selected marker as the reference point.

bpy.ops.action.new()¶

    

Create new action

bpy.ops.action.paste(_*_ , _offset =START_, _merge =MIX_, _flipped =False_)¶

    

Paste keyframes from the internal clipboard for the selected channels,
starting on the current frame

Parameters:

    

  * **offset** (enum in [Keyframe Paste Offset Items](bpy_types_enum_items/keyframe_paste_offset_items.html#rna-enum-keyframe-paste-offset-items), (optional)) – Offset, Paste time offset of keys

  * **merge** (enum in [Keyframe Paste Merge Items](bpy_types_enum_items/keyframe_paste_merge_items.html#rna-enum-keyframe-paste-merge-items), (optional)) – Type, Method of merging pasted keys and existing

  * **flipped** (_boolean_ _,__(__optional_ _)_) – Flipped, Paste keyframes from mirrored bones if they exist

bpy.ops.action.previewrange_set()¶

    

Set Preview Range based on extents of selected Keyframes

bpy.ops.action.push_down()¶

    

Push action down on to the NLA stack as a new strip

bpy.ops.action.select_all(_*_ , _action =TOGGLE_)¶

    

Toggle selection of all keyframes

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.action.select_box(_*_ , _axis_range =False_, _xmin =0_, _xmax =0_,
_ymin =0_, _ymax =0_, _wait_for_input =True_, _mode =SET_, _tweak =False_)¶

    

Select all keyframes within the specified region

Parameters:

    

  * **axis_range** (_boolean_ _,__(__optional_ _)_) – Axis Range

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

  * **tweak** (_boolean_ _,__(__optional_ _)_) – Tweak, Operator has been activated using a click-drag event

bpy.ops.action.select_circle(_*_ , _x =0_, _y =0_, _radius =25_,
_wait_for_input =True_, _mode =SET_)¶

    

Select keyframe points using circle selection

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

bpy.ops.action.select_column(_*_ , _mode =KEYS_)¶

    

Select all keyframes on the specified frame(s)

Parameters:

    

**mode** (enum in [`KEYS`, `CFRA`, `MARKERS_COLUMN`, `MARKERS_BETWEEN`],
(optional)) – Mode

bpy.ops.action.select_lasso(_*_ , _path =None_, _use_smooth_stroke =False_,
_smooth_stroke_factor =0.75_, _smooth_stroke_radius =35_, _mode =SET_)¶

    

Select keyframe points using lasso selection

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

bpy.ops.action.select_leftright(_*_ , _mode =CHECK_, _extend =False_)¶

    

Select keyframes to the left or the right of the current frame

Parameters:

    

  * **mode** (enum in [`CHECK`, `LEFT`, `RIGHT`], (optional)) – Mode

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend Select

bpy.ops.action.select_less()¶

    

Deselect keyframes on ends of selection islands

bpy.ops.action.select_linked()¶

    

Select keyframes occurring in the same F-Curves as selected ones

bpy.ops.action.select_more()¶

    

Select keyframes beside already selected ones

bpy.ops.action.snap(_*_ , _type =CFRA_)¶

    

Snap selected keyframes to the times specified

Parameters:

    

**type** (enum in [`CFRA`, `NEAREST_FRAME`, `NEAREST_SECOND`,
`NEAREST_MARKER`], (optional)) –

Type

  * `CFRA` Selection to Current Frame – Snap selected keyframes to the current frame.

  * `NEAREST_FRAME` Selection to Nearest Frame – Snap selected keyframes to the nearest (whole) frame (use to fix accidental subframe offsets).

  * `NEAREST_SECOND` Selection to Nearest Second – Snap selected keyframes to the nearest second.

  * `NEAREST_MARKER` Selection to Nearest Marker – Snap selected keyframes to the nearest marker.

bpy.ops.action.stash(_*_ , _create_new =True_)¶

    

Store this action in the NLA stack as a non-contributing strip for later use

Parameters:

    

**create_new** (_boolean_ _,__(__optional_ _)_) – Create New Action, Create a
new action once the existing one has been safely stored

bpy.ops.action.stash_and_create()¶

    

Store this action in the NLA stack as a non-contributing strip for later use,
and create a new action

bpy.ops.action.unlink(_*_ , _force_delete =False_)¶

    

Unlink this action from the active action slot (and/or exit Tweak Mode)

Parameters:

    

**force_delete** (_boolean_ _,__(__optional_ _)_) – Force Delete, Clear Fake
User and remove copy stashed in this data-block’s NLA stack

bpy.ops.action.view_all()¶

    

Reset viewable area to show full keyframe range

bpy.ops.action.view_frame()¶

    

Move the view to the current frame

bpy.ops.action.view_selected()¶

    

Reset viewable area to show selected keyframes range

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

