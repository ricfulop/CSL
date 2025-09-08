---
url: https://docs.blender.org/api/current/bpy.ops.graph.html
scraped_at: 2025-09-08T14:18:16.607518
title: Graph Operators¶
---

# Graph Operators¶

bpy.ops.graph.bake_keys()¶

    

Add keyframes on every frame between the selected keyframes

bpy.ops.graph.blend_offset(_*_ , _factor =0.0_)¶

    

Shift selected keys to the value of the neighboring keys as a block

Parameters:

    

**factor** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Offset
Factor, Control which key to offset towards and how far

bpy.ops.graph.blend_to_default(_*_ , _factor =0.0_)¶

    

Blend selected keys to their default value from their current position

Parameters:

    

**factor** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Factor,
How much to blend to the default value

bpy.ops.graph.blend_to_ease(_*_ , _factor =0.0_)¶

    

Blends keyframes from current state to an ease-in or ease-out curve

Parameters:

    

**factor** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Blend,
Favor either original data or ease curve

bpy.ops.graph.blend_to_neighbor(_*_ , _factor =0.0_)¶

    

Blend selected keyframes to their left or right neighbor

Parameters:

    

**factor** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Blend,
The blend factor with 0 being the current frame

bpy.ops.graph.breakdown(_*_ , _factor =0.0_)¶

    

Move selected keyframes to an inbetween position relative to adjacent keys

Parameters:

    

**factor** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Factor,
Favor either the left or the right key

bpy.ops.graph.butterworth_smooth(_*_ , _cutoff_frequency =3.0_, _filter_order
=4_, _samples_per_frame =1_, _blend =1.0_, _blend_in_out =1_)¶

    

Smooth an F-Curve while maintaining the general shape of the curve

Parameters:

    

  * **cutoff_frequency** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Frequency Cutoff (Hz), Lower values give a smoother curve

  * **filter_order** (_int in_ _[__1_ _,__32_ _]__,__(__optional_ _)_) – Filter Order, Higher values produce a harder frequency cutoff

  * **samples_per_frame** (_int in_ _[__1_ _,__64_ _]__,__(__optional_ _)_) – Samples per Frame, How many samples to calculate per frame, helps with subframe data

  * **blend** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Blend, How much to blend to the smoothed curve

  * **blend_in_out** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Blend In/Out, Linearly blend the smooth data to the border frames of the selection

bpy.ops.graph.clean(_*_ , _threshold =0.001_, _channels =False_)¶

    

Simplify F-Curves by removing closely spaced keyframes

Parameters:

    

  * **threshold** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Threshold

  * **channels** (_boolean_ _,__(__optional_ _)_) – Channels

bpy.ops.graph.click_insert(_*_ , _frame =1.0_, _value =1.0_, _extend =False_)¶

    

Insert new keyframe at the cursor position for the active F-Curve

Parameters:

    

  * **frame** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Frame Number, Frame to insert keyframe on

  * **value** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Value, Value for keyframe on

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection instead of deselecting everything first

bpy.ops.graph.clickselect(_*_ , _wait_to_deselect_others =False_, _mouse_x
=0_, _mouse_y =0_, _extend =False_, _deselect_all =False_, _column =False_,
_curves =False_)¶

    

Select keyframes by clicking on them

Parameters:

    

  * **wait_to_deselect_others** (_boolean_ _,__(__optional_ _)_) – Wait to Deselect Others

  * **mouse_x** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Mouse X

  * **mouse_y** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Mouse Y

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend Select, Toggle keyframe selection instead of leaving newly selected keyframes only

  * **deselect_all** (_boolean_ _,__(__optional_ _)_) – Deselect On Nothing, Deselect all when nothing under the cursor

  * **column** (_boolean_ _,__(__optional_ _)_) – Column Select, Select all keyframes that occur on the same frame as the one under the mouse

  * **curves** (_boolean_ _,__(__optional_ _)_) – Only Curves, Select all the keyframes in the curve

bpy.ops.graph.copy()¶

    

Copy selected keyframes to the internal clipboard

bpy.ops.graph.cursor_set(_*_ , _frame =0.0_, _value =0.0_)¶

    

Interactively set the current frame and value cursor

Parameters:

    

  * **frame** (_float in_ _[__-1.04857e+06_ _,__1.04857e+06_ _]__,__(__optional_ _)_) – Frame

  * **value** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Value

bpy.ops.graph.decimate(_*_ , _mode =RATIO_, _factor =0.333333_,
_remove_error_margin =0.0_)¶

    

Decimate F-Curves by removing keyframes that influence the curve shape the
least

Parameters:

    

  * **mode** (enum in [`RATIO`, `ERROR`], (optional)) – 

Mode, Which mode to use for decimation

    * `RATIO` Ratio – Use a percentage to specify how many keyframes you want to remove.

    * `ERROR` Error Margin – Use an error margin to specify how much the curve is allowed to deviate from the original path.

  * **factor** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Factor, The ratio of keyframes to remove

  * **remove_error_margin** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Max Error Margin, How much the new decimated curve is allowed to deviate from the original

bpy.ops.graph.delete(_*_ , _confirm =True_)¶

    

Remove all selected keyframes

Parameters:

    

**confirm** (_boolean_ _,__(__optional_ _)_) – Confirm, Prompt for
confirmation

bpy.ops.graph.driver_delete_invalid()¶

    

Delete all visible drivers considered invalid

bpy.ops.graph.driver_variables_copy()¶

    

Copy the driver variables of the active driver

bpy.ops.graph.driver_variables_paste(_*_ , _replace =False_)¶

    

Add copied driver variables to the active driver

Parameters:

    

**replace** (_boolean_ _,__(__optional_ _)_) – Replace Existing, Replace
existing driver variables, instead of just appending to the end of the
existing list

bpy.ops.graph.duplicate(_*_ , _mode =TRANSLATION_)¶

    

Make a copy of all selected keyframes

Parameters:

    

**mode** (enum in [Transform Mode Type
Items](bpy_types_enum_items/transform_mode_type_items.html#rna-enum-transform-
mode-type-items), (optional)) – Mode

bpy.ops.graph.duplicate_move(_*_ , _GRAPH_OT_duplicate =None_,
_TRANSFORM_OT_translate =None_)¶

    

Make a copy of all selected keyframes and move them

Parameters:

    

  * **GRAPH_OT_duplicate** (`GRAPH_OT_duplicate`, (optional)) – Duplicate Keyframes, Make a copy of all selected keyframes

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.graph.ease(_*_ , _factor =0.0_, _sharpness =2.0_)¶

    

Align keyframes on a ease-in or ease-out curve

Parameters:

    

  * **factor** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Curve Bend, Defines if the keys should be aligned on an ease-in or ease-out curve

  * **sharpness** (_float in_ _[__0.001_ _,__inf_ _]__,__(__optional_ _)_) – Sharpness, Higher values make the change more abrupt

bpy.ops.graph.easing_type(_*_ , _type =AUTO_)¶

    

Set easing type for the F-Curve segments starting from the selected keyframes

Parameters:

    

**type** (enum in [Beztriple Interpolation Easing
Items](bpy_types_enum_items/beztriple_interpolation_easing_items.html#rna-
enum-beztriple-interpolation-easing-items), (optional)) – Type

bpy.ops.graph.equalize_handles(_*_ , _side =LEFT_, _handle_length =5.0_,
_flatten =False_)¶

    

Ensure selected keyframes’ handles have equal length, optionally making them
horizontal. Automatic, Automatic Clamped, or Vector handle types will be
converted to Aligned

Parameters:

    

  * **side** (enum in [`LEFT`, `RIGHT`, `BOTH`], (optional)) – 

Side, Side of the keyframes’ Bézier handles to affect

    * `LEFT` Left – Equalize selected keyframes’ left handles.

    * `RIGHT` Right – Equalize selected keyframes’ right handles.

    * `BOTH` Both – Equalize both of a keyframe’s handles.

  * **handle_length** (_float in_ _[__0.1_ _,__inf_ _]__,__(__optional_ _)_) – Handle Length, Length to make selected keyframes’ Bézier handles

  * **flatten** (_boolean_ _,__(__optional_ _)_) – Flatten, Make the values of the selected keyframes’ handles the same as their respective keyframes

bpy.ops.graph.euler_filter()¶

    

Fix large jumps and flips in the selected Euler Rotation F-Curves arising from
rotation values being clipped when baking physics

bpy.ops.graph.extrapolation_type(_*_ , _type =CONSTANT_)¶

    

Set extrapolation mode for selected F-Curves

Parameters:

    

**type** (enum in [`CONSTANT`, `LINEAR`, `MAKE_CYCLIC`, `CLEAR_CYCLIC`],
(optional)) –

Type

  * `CONSTANT` Constant Extrapolation – Values on endpoint keyframes are held.

  * `LINEAR` Linear Extrapolation – Straight-line slope of end segments are extended past the endpoint keyframes.

  * `MAKE_CYCLIC` Make Cyclic (F-Modifier) – Add Cycles F-Modifier if one doesn’t exist already.

  * `CLEAR_CYCLIC` Clear Cyclic (F-Modifier) – Remove Cycles F-Modifier if not needed anymore.

bpy.ops.graph.fmodifier_add(_*_ , _type =NULL_, _only_active =False_)¶

    

Add F-Modifier to the active/selected F-Curves

Parameters:

    

  * **type** (enum in [Fmodifier Type Items](bpy_types_enum_items/fmodifier_type_items.html#rna-enum-fmodifier-type-items), (optional)) – Type

  * **only_active** (_boolean_ _,__(__optional_ _)_) – Only Active, Only add F-Modifier to active F-Curve

bpy.ops.graph.fmodifier_copy()¶

    

Copy the F-Modifier(s) of the active F-Curve

bpy.ops.graph.fmodifier_paste(_*_ , _only_active =False_, _replace =False_)¶

    

Add copied F-Modifiers to the selected F-Curves

Parameters:

    

  * **only_active** (_boolean_ _,__(__optional_ _)_) – Only Active, Only paste F-Modifiers on active F-Curve

  * **replace** (_boolean_ _,__(__optional_ _)_) – Replace Existing, Replace existing F-Modifiers, instead of just appending to the end of the existing list

bpy.ops.graph.frame_jump()¶

    

Place the cursor on the midpoint of selected keyframes

bpy.ops.graph.gaussian_smooth(_*_ , _factor =1.0_, _sigma =0.33_,
_filter_width =6_)¶

    

Smooth the curve using a Gaussian filter

Parameters:

    

  * **factor** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Factor, How much to blend to the default value

  * **sigma** (_float in_ _[__0.001_ _,__inf_ _]__,__(__optional_ _)_) – Sigma, The shape of the gaussian distribution, lower values make it sharper

  * **filter_width** (_int in_ _[__1_ _,__64_ _]__,__(__optional_ _)_) – Filter Width, How far to each side the operator will average the key values

bpy.ops.graph.ghost_curves_clear()¶

    

Clear F-Curve snapshots (Ghosts) for active Graph Editor

bpy.ops.graph.ghost_curves_create()¶

    

Create snapshot (Ghosts) of selected F-Curves as background aid for active
Graph Editor

bpy.ops.graph.handle_type(_*_ , _type =FREE_)¶

    

Set type of handle for selected keyframes

Parameters:

    

**type** (enum in [Keyframe Handle Type
Items](bpy_types_enum_items/keyframe_handle_type_items.html#rna-enum-keyframe-
handle-type-items), (optional)) – Type

bpy.ops.graph.hide(_*_ , _unselected =False_)¶

    

Hide selected curves from Graph Editor view

Parameters:

    

**unselected** (_boolean_ _,__(__optional_ _)_) – Unselected, Hide unselected
rather than selected curves

bpy.ops.graph.interpolation_type(_*_ , _type =CONSTANT_)¶

    

Set interpolation mode for the F-Curve segments starting from the selected
keyframes

Parameters:

    

**type** (enum in [Beztriple Interpolation Mode
Items](bpy_types_enum_items/beztriple_interpolation_mode_items.html#rna-enum-
beztriple-interpolation-mode-items), (optional)) – Type

bpy.ops.graph.keyframe_insert(_*_ , _type =ALL_)¶

    

Insert keyframes for the specified channels

Parameters:

    

**type** (enum in [`ALL`, `SEL`, `ACTIVE`, `CURSOR_ACTIVE`, `CURSOR_SEL`],
(optional)) –

Type

  * `ALL` All Channels – Insert a keyframe on all visible and editable F-Curves using each curve’s current value.

  * `SEL` Only Selected Channels – Insert a keyframe on selected F-Curves using each curve’s current value.

  * `ACTIVE` Only Active F-Curve – Insert a keyframe on the active F-Curve using the curve’s current value.

  * `CURSOR_ACTIVE` Active Channels at Cursor – Insert a keyframe for the active F-Curve at the cursor point.

  * `CURSOR_SEL` Selected Channels at Cursor – Insert a keyframe for selected F-Curves at the cursor point.

bpy.ops.graph.keyframe_jump(_*_ , _next =True_)¶

    

Jump to previous/next keyframe

Parameters:

    

**next** (_boolean_ _,__(__optional_ _)_) – Next Keyframe

bpy.ops.graph.keys_to_samples()¶

    

Convert selected channels to an uneditable set of samples to save storage
space

bpy.ops.graph.match_slope(_*_ , _factor =0.0_)¶

    

Blend selected keys to the slope of neighboring ones

Parameters:

    

**factor** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Factor,
Defines which keys to use as slope and how much to blend towards them

bpy.ops.graph.mirror(_*_ , _type =CFRA_)¶

    

Flip selected keyframes over the selected mirror line

Parameters:

    

**type** (enum in [`CFRA`, `VALUE`, `YAXIS`, `XAXIS`, `MARKER`], (optional)) –

Type

  * `CFRA` By Times Over Current Frame – Flip times of selected keyframes using the current frame as the mirror line.

  * `VALUE` By Values Over Cursor Value – Flip values of selected keyframes using the cursor value (Y/Horizontal component) as the mirror line.

  * `YAXIS` By Times Over Zero Time – Flip times of selected keyframes, effectively reversing the order they appear in.

  * `XAXIS` By Values Over Zero Value – Flip values of selected keyframes (i.e. negative values become positive, and vice versa).

  * `MARKER` By Times Over First Selected Marker – Flip times of selected keyframes using the first selected marker as the reference point.

bpy.ops.graph.paste(_*_ , _offset =START_, _value_offset =NONE_, _merge =MIX_,
_flipped =False_)¶

    

Paste keyframes from the internal clipboard for the selected channels,
starting on the current frame

Parameters:

    

  * **offset** (enum in [Keyframe Paste Offset Items](bpy_types_enum_items/keyframe_paste_offset_items.html#rna-enum-keyframe-paste-offset-items), (optional)) – Frame Offset, Paste time offset of keys

  * **value_offset** (enum in [Keyframe Paste Offset Value Items](bpy_types_enum_items/keyframe_paste_offset_value_items.html#rna-enum-keyframe-paste-offset-value-items), (optional)) – Value Offset, Paste keys with a value offset

  * **merge** (enum in [Keyframe Paste Merge Items](bpy_types_enum_items/keyframe_paste_merge_items.html#rna-enum-keyframe-paste-merge-items), (optional)) – Type, Method of merging pasted keys and existing

  * **flipped** (_boolean_ _,__(__optional_ _)_) – Flipped, Paste keyframes from mirrored bones if they exist

bpy.ops.graph.previewrange_set()¶

    

Set Preview Range based on range of selected keyframes

bpy.ops.graph.push_pull(_*_ , _factor =1.0_)¶

    

Exaggerate or minimize the value of the selected keys

Parameters:

    

**factor** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Factor,
Control how far to push or pull the keys

bpy.ops.graph.reveal(_*_ , _select =True_)¶

    

Make previously hidden curves visible again in Graph Editor view

Parameters:

    

**select** (_boolean_ _,__(__optional_ _)_) – Select

bpy.ops.graph.samples_to_keys()¶

    

Convert selected channels from samples to keyframes

bpy.ops.graph.scale_average(_*_ , _factor =1.0_)¶

    

Scale selected key values by their combined average

Parameters:

    

**factor** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Scale
Factor, The scale factor applied to the curve segments

bpy.ops.graph.scale_from_neighbor(_*_ , _factor =0.0_, _anchor =LEFT_)¶

    

Increase or decrease the value of selected keys in relationship to the
neighboring one

Parameters:

    

  * **factor** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Factor, The factor to scale keys with

  * **anchor** (enum in [`LEFT`, `RIGHT`], (optional)) – Reference Key, Which end of the segment to use as a reference to scale from

bpy.ops.graph.select_all(_*_ , _action =TOGGLE_)¶

    

Toggle selection of all keyframes

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.graph.select_box(_*_ , _axis_range =False_, _include_handles =True_,
_tweak =False_, _use_curve_selection =True_, _xmin =0_, _xmax =0_, _ymin =0_,
_ymax =0_, _wait_for_input =True_, _mode =SET_)¶

    

Select all keyframes within the specified region

Parameters:

    

  * **axis_range** (_boolean_ _,__(__optional_ _)_) – Axis Range

  * **include_handles** (_boolean_ _,__(__optional_ _)_) – Include Handles, Are handles tested individually against the selection criteria, independently from their keys. When unchecked, handles are (de)selected in unison with their keys

  * **tweak** (_boolean_ _,__(__optional_ _)_) – Tweak, Operator has been activated using a click-drag event

  * **use_curve_selection** (_boolean_ _,__(__optional_ _)_) – Select Curves, Allow selecting all the keyframes of a curve by selecting the calculated F-curve

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

bpy.ops.graph.select_circle(_*_ , _x =0_, _y =0_, _radius =25_,
_wait_for_input =True_, _mode =SET_, _include_handles =True_,
_use_curve_selection =True_)¶

    

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

  * **include_handles** (_boolean_ _,__(__optional_ _)_) – Include Handles, Are handles tested individually against the selection criteria, independently from their keys. When unchecked, handles are (de)selected in unison with their keys

  * **use_curve_selection** (_boolean_ _,__(__optional_ _)_) – Select Curves, Allow selecting all the keyframes of a curve by selecting the curve itself

bpy.ops.graph.select_column(_*_ , _mode =KEYS_)¶

    

Select all keyframes on the specified frame(s)

Parameters:

    

**mode** (enum in [`KEYS`, `CFRA`, `MARKERS_COLUMN`, `MARKERS_BETWEEN`],
(optional)) – Mode

bpy.ops.graph.select_key_handles(_*_ , _left_handle_action =SELECT_,
_right_handle_action =SELECT_, _key_action =KEEP_)¶

    

For selected keyframes, select/deselect any combination of the key itself and
its handles

Parameters:

    

  * **left_handle_action** (enum in [`SELECT`, `DESELECT`, `KEEP`], (optional)) – 

Left Handle, Effect on the left handle

    * `SELECT` Select.

    * `DESELECT` Deselect.

    * `KEEP` Keep – Leave as is.

  * **right_handle_action** (enum in [`SELECT`, `DESELECT`, `KEEP`], (optional)) – 

Right Handle, Effect on the right handle

    * `SELECT` Select.

    * `DESELECT` Deselect.

    * `KEEP` Keep – Leave as is.

  * **key_action** (enum in [`SELECT`, `DESELECT`, `KEEP`], (optional)) – 

Key, Effect on the key itself

    * `SELECT` Select.

    * `DESELECT` Deselect.

    * `KEEP` Keep – Leave as is.

bpy.ops.graph.select_lasso(_*_ , _path =None_, _use_smooth_stroke =False_,
_smooth_stroke_factor =0.75_, _smooth_stroke_radius =35_, _mode =SET_,
_include_handles =True_, _use_curve_selection =True_)¶

    

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

  * **include_handles** (_boolean_ _,__(__optional_ _)_) – Include Handles, Are handles tested individually against the selection criteria, independently from their keys. When unchecked, handles are (de)selected in unison with their keys

  * **use_curve_selection** (_boolean_ _,__(__optional_ _)_) – Select Curves, Allow selecting all the keyframes of a curve by selecting the curve itself

bpy.ops.graph.select_leftright(_*_ , _mode =CHECK_, _extend =False_)¶

    

Select keyframes to the left or the right of the current frame

Parameters:

    

  * **mode** (enum in [`CHECK`, `LEFT`, `RIGHT`], (optional)) – Mode

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend Select

bpy.ops.graph.select_less()¶

    

Deselect keyframes on ends of selection islands

bpy.ops.graph.select_linked()¶

    

Select keyframes occurring in the same F-Curves as selected ones

bpy.ops.graph.select_more()¶

    

Select keyframes beside already selected ones

bpy.ops.graph.shear(_*_ , _factor =0.0_, _direction =FROM_LEFT_)¶

    

Affect the value of the keys linearly, keeping the same relationship between
them using either the left or the right key as reference

Parameters:

    

  * **factor** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Shear Factor, The amount of shear to apply

  * **direction** (enum in [`FROM_LEFT`, `FROM_RIGHT`], (optional)) – 

Direction, Which end of the segment to use as a reference to shear from

    * `FROM_LEFT` From Left – Shear the keys using the left key as reference.

    * `FROM_RIGHT` From Right – Shear the keys using the right key as reference.

bpy.ops.graph.smooth()¶

    

Apply weighted moving means to make selected F-Curves less bumpy

bpy.ops.graph.snap(_*_ , _type =CFRA_)¶

    

Snap selected keyframes to the chosen times/values

Parameters:

    

**type** (enum in [`CFRA`, `VALUE`, `NEAREST_FRAME`, `NEAREST_SECOND`,
`NEAREST_MARKER`, `HORIZONTAL`], (optional)) –

Type

  * `CFRA` Selection to Current Frame – Snap selected keyframes to the current frame.

  * `VALUE` Selection to Cursor Value – Set values of selected keyframes to the cursor value (Y/Horizontal component).

  * `NEAREST_FRAME` Selection to Nearest Frame – Snap selected keyframes to the nearest (whole) frame (use to fix accidental subframe offsets).

  * `NEAREST_SECOND` Selection to Nearest Second – Snap selected keyframes to the nearest second.

  * `NEAREST_MARKER` Selection to Nearest Marker – Snap selected keyframes to the nearest marker.

  * `HORIZONTAL` Flatten Handles – Flatten handles for a smoother transition.

bpy.ops.graph.snap_cursor_value()¶

    

Place the cursor value on the average value of selected keyframes

bpy.ops.graph.sound_to_samples(_*_ , _filepath =''_, _check_existing =False_,
_filter_blender =False_, _filter_backup =False_, _filter_image =False_,
_filter_movie =True_, _filter_python =False_, _filter_font =False_,
_filter_sound =True_, _filter_text =False_, _filter_archive =False_,
_filter_btx =False_, _filter_collada =False_, _filter_alembic =False_,
_filter_usd =False_, _filter_obj =False_, _filter_volume =False_,
_filter_folder =True_, _filter_blenlib =False_, _filemode =9_, _show_multiview
=False_, _use_multiview =False_, _display_type =DEFAULT_, _sort_method_ , _low
=0.0_, _high =100000.0_, _attack =0.005_, _release =0.2_, _threshold =0.0_,
_use_accumulate =False_, _use_additive =False_, _use_square =False_,
_sthreshold =0.1_)¶

    

Bakes a sound wave to samples on selected channels

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

  * **check_existing** (_boolean_ _,__(__optional_ _)_) – Check Existing, Check and warn on overwriting existing files

  * **filter_blender** (_boolean_ _,__(__optional_ _)_) – Filter .blend files

  * **filter_backup** (_boolean_ _,__(__optional_ _)_) – Filter .blend files

  * **filter_image** (_boolean_ _,__(__optional_ _)_) – Filter image files

  * **filter_movie** (_boolean_ _,__(__optional_ _)_) – Filter movie files

  * **filter_python** (_boolean_ _,__(__optional_ _)_) – Filter Python files

  * **filter_font** (_boolean_ _,__(__optional_ _)_) – Filter font files

  * **filter_sound** (_boolean_ _,__(__optional_ _)_) – Filter sound files

  * **filter_text** (_boolean_ _,__(__optional_ _)_) – Filter text files

  * **filter_archive** (_boolean_ _,__(__optional_ _)_) – Filter archive files

  * **filter_btx** (_boolean_ _,__(__optional_ _)_) – Filter btx files

  * **filter_collada** (_boolean_ _,__(__optional_ _)_) – Filter COLLADA files

  * **filter_alembic** (_boolean_ _,__(__optional_ _)_) – Filter Alembic files

  * **filter_usd** (_boolean_ _,__(__optional_ _)_) – Filter USD files

  * **filter_obj** (_boolean_ _,__(__optional_ _)_) – Filter OBJ files

  * **filter_volume** (_boolean_ _,__(__optional_ _)_) – Filter OpenVDB volume files

  * **filter_folder** (_boolean_ _,__(__optional_ _)_) – Filter folders

  * **filter_blenlib** (_boolean_ _,__(__optional_ _)_) – Filter Blender IDs

  * **filemode** (_int in_ _[__1_ _,__9_ _]__,__(__optional_ _)_) – File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

  * **show_multiview** (_boolean_ _,__(__optional_ _)_) – Enable Multi-View

  * **use_multiview** (_boolean_ _,__(__optional_ _)_) – Use Multi-View

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **low** (_float in_ _[__0_ _,__100000_ _]__,__(__optional_ _)_) – Lowest Frequency, Cutoff frequency of a high-pass filter that is applied to the audio data

  * **high** (_float in_ _[__0_ _,__100000_ _]__,__(__optional_ _)_) – Highest Frequency, Cutoff frequency of a low-pass filter that is applied to the audio data

  * **attack** (_float in_ _[__0_ _,__2_ _]__,__(__optional_ _)_) – Attack Time, Value for the envelope calculation that tells how fast the envelope can rise (the lower the value the steeper it can rise)

  * **release** (_float in_ _[__0_ _,__5_ _]__,__(__optional_ _)_) – Release Time, Value for the envelope calculation that tells how fast the envelope can fall (the lower the value the steeper it can fall)

  * **threshold** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Threshold, Minimum amplitude value needed to influence the envelope

  * **use_accumulate** (_boolean_ _,__(__optional_ _)_) – Accumulate, Only the positive differences of the envelope amplitudes are summarized to produce the output

  * **use_additive** (_boolean_ _,__(__optional_ _)_) – Additive, The amplitudes of the envelope are summarized (or, when Accumulate is enabled, both positive and negative differences are accumulated)

  * **use_square** (_boolean_ _,__(__optional_ _)_) – Square, The output is a square curve (negative values always result in -1, and positive ones in 1)

  * **sthreshold** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Square Threshold, Square only: all values with an absolute amplitude lower than that result in 0

bpy.ops.graph.time_offset(_*_ , _frame_offset =0.0_)¶

    

Shifts the value of selected keys in time

Parameters:

    

**frame_offset** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) –
Frame Offset, How far in frames to offset the animation

bpy.ops.graph.view_all(_*_ , _include_handles =True_)¶

    

Reset viewable area to show full keyframe range

Parameters:

    

**include_handles** (_boolean_ _,__(__optional_ _)_) – Include Handles,
Include handles of keyframes when calculating extents

bpy.ops.graph.view_frame()¶

    

Move the view to the current frame

bpy.ops.graph.view_selected(_*_ , _include_handles =True_)¶

    

Reset viewable area to show selected keyframe range

Parameters:

    

**include_handles** (_boolean_ _,__(__optional_ _)_) – Include Handles,
Include handles of keyframes when calculating extents

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

