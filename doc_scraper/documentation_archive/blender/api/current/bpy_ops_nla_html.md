---
url: https://docs.blender.org/api/current/bpy.ops.nla.html
scraped_at: 2025-09-08T14:18:29.554572
title: Nla Operators¶
---

# Nla Operators¶

bpy.ops.nla.action_pushdown(_*_ , _track_index =-1_)¶

    

Push action down onto the top of the NLA stack as a new strip

Parameters:

    

**track_index** (_int in_ _[__-1_ _,__inf_ _]__,__(__optional_ _)_) – Track
Index, Index of NLA action track to perform pushdown operation on

bpy.ops.nla.action_sync_length(_*_ , _active =True_)¶

    

Synchronize the length of the referenced Action with the length used in the
strip

Parameters:

    

**active** (_boolean_ _,__(__optional_ _)_) – Active Strip Only, Only sync the
active length for the active strip

bpy.ops.nla.action_unlink(_*_ , _force_delete =False_)¶

    

Unlink this action from the active action slot (and/or exit Tweak Mode)

Parameters:

    

**force_delete** (_boolean_ _,__(__optional_ _)_) – Force Delete, Clear Fake
User and remove copy stashed in this data-block’s NLA stack

bpy.ops.nla.actionclip_add(_*_ , _action_)¶

    

Add an Action-Clip strip (i.e. an NLA Strip referencing an Action) to the
active track

Parameters:

    

**action** (_enum in_ _[__]__,__(__optional_ _)_) – Action

bpy.ops.nla.apply_scale()¶

    

Apply scaling of selected strips to their referenced Actions

bpy.ops.nla.bake(_*_ , _frame_start =1_, _frame_end =250_, _step =1_,
_only_selected =True_, _visual_keying =False_, _clear_constraints =False_,
_clear_parents =False_, _use_current_action =False_, _clean_curves =False_,
_bake_types ={'POSE'}_, _channel_types ={'BBONE', 'LOCATION', 'PROPS',
'ROTATION', 'SCALE'}_)¶

    

Bake all selected objects location/scale/rotation animation to an action

Parameters:

    

  * **frame_start** (_int in_ _[__0_ _,__300000_ _]__,__(__optional_ _)_) – Start Frame, Start frame for baking

  * **frame_end** (_int in_ _[__1_ _,__300000_ _]__,__(__optional_ _)_) – End Frame, End frame for baking

  * **step** (_int in_ _[__1_ _,__120_ _]__,__(__optional_ _)_) – Frame Step, Number of frames to skip forward while baking each frame

  * **only_selected** (_boolean_ _,__(__optional_ _)_) – Only Selected Bones, Only key selected bones (Pose baking only)

  * **visual_keying** (_boolean_ _,__(__optional_ _)_) – Visual Keying, Keyframe from the final transformations (with constraints applied)

  * **clear_constraints** (_boolean_ _,__(__optional_ _)_) – Clear Constraints, Remove all constraints from keyed object/bones. To get a correct bake with this setting Visual Keying should be enabled

  * **clear_parents** (_boolean_ _,__(__optional_ _)_) – Clear Parents, Bake animation onto the object then clear parents (objects only)

  * **use_current_action** (_boolean_ _,__(__optional_ _)_) – Overwrite Current Action, Bake animation into current action, instead of creating a new one (useful for baking only part of bones in an armature)

  * **clean_curves** (_boolean_ _,__(__optional_ _)_) – Clean Curves, After baking curves, remove redundant keys

  * **bake_types** (enum set in {`POSE`, `OBJECT`}, (optional)) – 

Bake Data, Which data’s transformations to bake

    * `POSE` Pose – Bake bones transformations.

    * `OBJECT` Object – Bake object transformations.

  * **channel_types** (enum set in {`LOCATION`, `ROTATION`, `SCALE`, `BBONE`, `PROPS`}, (optional)) – 

Channels, Which channels to bake

    * `LOCATION` Location – Bake location channels.

    * `ROTATION` Rotation – Bake rotation channels.

    * `SCALE` Scale – Bake scale channels.

    * `BBONE` B-Bone – Bake B-Bone channels.

    * `PROPS` Custom Properties – Bake custom properties.

File:

    

[startup/bl_operators/anim.py:273](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L273)

bpy.ops.nla.channels_click(_*_ , _extend =False_)¶

    

Handle clicks to select NLA tracks

Parameters:

    

**extend** (_boolean_ _,__(__optional_ _)_) – Extend Select

bpy.ops.nla.clear_scale()¶

    

Reset scaling of selected strips

bpy.ops.nla.click_select(_*_ , _wait_to_deselect_others =False_, _mouse_x =0_,
_mouse_y =0_, _extend =False_, _deselect_all =False_)¶

    

Handle clicks to select NLA Strips

Parameters:

    

  * **wait_to_deselect_others** (_boolean_ _,__(__optional_ _)_) – Wait to Deselect Others

  * **mouse_x** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Mouse X

  * **mouse_y** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Mouse Y

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend Select

  * **deselect_all** (_boolean_ _,__(__optional_ _)_) – Deselect On Nothing, Deselect all when nothing under the cursor

bpy.ops.nla.delete()¶

    

Delete selected strips

bpy.ops.nla.duplicate(_*_ , _linked =False_)¶

    

Duplicate selected NLA-Strips, adding the new strips to new track(s)

Parameters:

    

**linked** (_boolean_ _,__(__optional_ _)_) – Linked, When duplicating strips,
assign new copies of the actions they use

bpy.ops.nla.duplicate_linked_move(_*_ , _NLA_OT_duplicate =None_,
_TRANSFORM_OT_translate =None_)¶

    

Duplicate Linked selected NLA-Strips, adding the new strips to new track(s)

Parameters:

    

  * **NLA_OT_duplicate** (`NLA_OT_duplicate`, (optional)) – Duplicate Strips, Duplicate selected NLA-Strips, adding the new strips to new track(s)

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.nla.duplicate_move(_*_ , _NLA_OT_duplicate =None_,
_TRANSFORM_OT_translate =None_)¶

    

Duplicate selected NLA-Strips, adding the new strips to new track(s)

Parameters:

    

  * **NLA_OT_duplicate** (`NLA_OT_duplicate`, (optional)) – Duplicate Strips, Duplicate selected NLA-Strips, adding the new strips to new track(s)

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.nla.fmodifier_add(_*_ , _type =NULL_, _only_active =True_)¶

    

Add F-Modifier to the active/selected NLA-Strips

Parameters:

    

  * **type** (enum in [Fmodifier Type Items](bpy_types_enum_items/fmodifier_type_items.html#rna-enum-fmodifier-type-items), (optional)) – Type

  * **only_active** (_boolean_ _,__(__optional_ _)_) – Only Active, Only add a F-Modifier of the specified type to the active strip

bpy.ops.nla.fmodifier_copy()¶

    

Copy the F-Modifier(s) of the active NLA-Strip

bpy.ops.nla.fmodifier_paste(_*_ , _only_active =True_, _replace =False_)¶

    

Add copied F-Modifiers to the selected NLA-Strips

Parameters:

    

  * **only_active** (_boolean_ _,__(__optional_ _)_) – Only Active, Only paste F-Modifiers on active strip

  * **replace** (_boolean_ _,__(__optional_ _)_) – Replace Existing, Replace existing F-Modifiers, instead of just appending to the end of the existing list

bpy.ops.nla.make_single_user(_*_ , _confirm =True_)¶

    

Make linked action local to each strip

Parameters:

    

**confirm** (_boolean_ _,__(__optional_ _)_) – Confirm, Prompt for
confirmation

bpy.ops.nla.meta_add()¶

    

Add new meta-strips incorporating the selected strips

bpy.ops.nla.meta_remove()¶

    

Separate out the strips held by the selected meta-strips

bpy.ops.nla.move_down()¶

    

Move selected strips down a track if there’s room

bpy.ops.nla.move_up()¶

    

Move selected strips up a track if there’s room

bpy.ops.nla.mute_toggle()¶

    

Mute or un-mute selected strips

bpy.ops.nla.previewrange_set()¶

    

Set Preview Range based on extends of selected strips

bpy.ops.nla.select_all(_*_ , _action =TOGGLE_)¶

    

Select or deselect all NLA-Strips

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.nla.select_box(_*_ , _axis_range =False_, _tweak =False_, _xmin =0_,
_xmax =0_, _ymin =0_, _ymax =0_, _wait_for_input =True_, _mode =SET_)¶

    

Use box selection to grab NLA-Strips

Parameters:

    

  * **axis_range** (_boolean_ _,__(__optional_ _)_) – Axis Range

  * **tweak** (_boolean_ _,__(__optional_ _)_) – Tweak, Operator has been activated using a click-drag event

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

bpy.ops.nla.select_leftright(_*_ , _mode =CHECK_, _extend =False_)¶

    

Select strips to the left or the right of the current frame

Parameters:

    

  * **mode** (enum in [`CHECK`, `LEFT`, `RIGHT`], (optional)) – Mode

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend Select

bpy.ops.nla.selected_objects_add()¶

    

Make selected objects appear in NLA Editor by adding Animation Data

bpy.ops.nla.snap(_*_ , _type =CFRA_)¶

    

Move start of strips to specified time

Parameters:

    

**type** (enum in [`CFRA`, `NEAREST_FRAME`, `NEAREST_SECOND`,
`NEAREST_MARKER`], (optional)) – Type

bpy.ops.nla.soundclip_add()¶

    

Add a strip for controlling when speaker plays its sound clip

bpy.ops.nla.split()¶

    

Split selected strips at their midpoints

bpy.ops.nla.swap()¶

    

Swap order of selected strips within tracks

bpy.ops.nla.tracks_add(_*_ , _above_selected =False_)¶

    

Add NLA-Tracks above/after the selected tracks

Parameters:

    

**above_selected** (_boolean_ _,__(__optional_ _)_) – Above Selected, Add a
new NLA Track above every existing selected one

bpy.ops.nla.tracks_delete()¶

    

Delete selected NLA-Tracks and the strips they contain

bpy.ops.nla.transition_add()¶

    

Add a transition strip between two adjacent selected strips

bpy.ops.nla.tweakmode_enter(_*_ , _isolate_action =False_,
_use_upper_stack_evaluation =False_)¶

    

Enter tweaking mode for the action referenced by the active strip to edit its
keyframes

Parameters:

    

  * **isolate_action** (_boolean_ _,__(__optional_ _)_) – Isolate Action, Enable ‘solo’ on the NLA Track containing the active strip, to edit it without seeing the effects of the NLA stack

  * **use_upper_stack_evaluation** (_boolean_ _,__(__optional_ _)_) – Evaluate Upper Stack, In tweak mode, display the effects of the tracks above the tweak strip

bpy.ops.nla.tweakmode_exit(_*_ , _isolate_action =False_)¶

    

Exit tweaking mode for the action referenced by the active strip

Parameters:

    

**isolate_action** (_boolean_ _,__(__optional_ _)_) – Isolate Action, Disable
‘solo’ on any of the NLA Tracks after exiting tweak mode to get things back to
normal

bpy.ops.nla.view_all()¶

    

Reset viewable area to show full strips range

bpy.ops.nla.view_frame()¶

    

Move the view to the current frame

bpy.ops.nla.view_selected()¶

    

Reset viewable area to show selected strips range

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

