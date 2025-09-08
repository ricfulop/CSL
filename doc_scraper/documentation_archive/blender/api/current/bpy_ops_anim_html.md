---
url: https://docs.blender.org/api/current/bpy.ops.anim.html
scraped_at: 2025-09-08T14:17:49.420290
title: Anim Operators¶
---

# Anim Operators¶

bpy.ops.anim.change_frame(_*_ , _frame =0.0_, _snap =False_, _seq_solo_preview
=False_)¶

    

Interactively change the current frame number

Parameters:

    

  * **frame** (_float in_ _[__-1.04857e+06_ _,__1.04857e+06_ _]__,__(__optional_ _)_) – Frame

  * **snap** (_boolean_ _,__(__optional_ _)_) – Snap

  * **seq_solo_preview** (_boolean_ _,__(__optional_ _)_) – Strip Preview

bpy.ops.anim.channel_select_keys(_*_ , _extend =False_)¶

    

Select all keyframes of channel under mouse

Parameters:

    

**extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection

bpy.ops.anim.channel_view_pick(_*_ , _include_handles =True_,
_use_preview_range =True_)¶

    

Reset viewable area to show the channel under the cursor

Parameters:

    

  * **include_handles** (_boolean_ _,__(__optional_ _)_) – Include Handles, Include handles of keyframes when calculating extents

  * **use_preview_range** (_boolean_ _,__(__optional_ _)_) – Use Preview Range, Ignore frames outside of the preview range

bpy.ops.anim.channels_bake(_*_ , _range =(0, 0)_, _step =1.0_,
_remove_outside_range =False_, _interpolation_type =BEZIER_, _bake_modifiers
=True_)¶

    

Create keyframes following the current shape of F-Curves of selected channels

Parameters:

    

  * **range** (_int array_ _of_ _2 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Frame Range, The range in which to create new keys

  * **step** (_float in_ _[__0.01_ _,__inf_ _]__,__(__optional_ _)_) – Frame Step, At which interval to add keys

  * **remove_outside_range** (_boolean_ _,__(__optional_ _)_) – Remove Outside Range, Removes keys outside the given range, leaving only the newly baked

  * **interpolation_type** (enum in [`BEZIER`, `LIN`, `CONST`], (optional)) – 

Interpolation Type, Choose the interpolation type with which new keys will be
added

    * `BEZIER` Bézier – New keys will be Bézier.

    * `LIN` Linear – New keys will be linear.

    * `CONST` Constant – New keys will be constant.

  * **bake_modifiers** (_boolean_ _,__(__optional_ _)_) – Bake Modifiers, Bake Modifiers into keyframes and delete them after

bpy.ops.anim.channels_clean_empty()¶

    

Delete all empty animation data containers from visible data-blocks

bpy.ops.anim.channels_click(_*_ , _extend =False_, _extend_range =False_,
_children_only =False_)¶

    

Handle mouse clicks over animation channels

Parameters:

    

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend Select

  * **extend_range** (_boolean_ _,__(__optional_ _)_) – Extend Range, Selection of active channel to clicked channel

  * **children_only** (_boolean_ _,__(__optional_ _)_) – Select Children Only

bpy.ops.anim.channels_collapse(_*_ , _all =True_)¶

    

Collapse (close) all selected expandable animation channels

Parameters:

    

**all** (_boolean_ _,__(__optional_ _)_) – All, Collapse all channels (not
just selected ones)

bpy.ops.anim.channels_delete()¶

    

Delete all selected animation channels

bpy.ops.anim.channels_editable_toggle(_*_ , _mode =TOGGLE_, _type =PROTECT_)¶

    

Toggle editability of selected channels

Parameters:

    

  * **mode** (enum in [`TOGGLE`, `DISABLE`, `ENABLE`, `INVERT`], (optional)) – Mode

  * **type** (enum in [`PROTECT`, `MUTE`], (optional)) – Type

bpy.ops.anim.channels_expand(_*_ , _all =True_)¶

    

Expand (open) all selected expandable animation channels

Parameters:

    

**all** (_boolean_ _,__(__optional_ _)_) – All, Expand all channels (not just
selected ones)

bpy.ops.anim.channels_fcurves_enable()¶

    

Clear ‘disabled’ tag from all F-Curves to get broken F-Curves working again

bpy.ops.anim.channels_group(_*_ , _name ='New Group'_)¶

    

Add selected F-Curves to a new group

Parameters:

    

**name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of newly
created group

bpy.ops.anim.channels_move(_*_ , _direction =DOWN_)¶

    

Rearrange selected animation channels

Parameters:

    

**direction** (enum in [`TOP`, `UP`, `DOWN`, `BOTTOM`], (optional)) –
Direction

bpy.ops.anim.channels_rename()¶

    

Rename animation channel under mouse

bpy.ops.anim.channels_select_all(_*_ , _action =TOGGLE_)¶

    

Toggle selection of all animation channels

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.anim.channels_select_box(_*_ , _xmin =0_, _xmax =0_, _ymin =0_, _ymax
=0_, _wait_for_input =True_, _deselect =False_, _extend =True_)¶

    

Select all animation channels within the specified region

Parameters:

    

  * **xmin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Min

  * **xmax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Max

  * **ymin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Min

  * **ymax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Max

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

  * **deselect** (_boolean_ _,__(__optional_ _)_) – Deselect, Deselect rather than select items

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection instead of deselecting everything first

bpy.ops.anim.channels_select_filter()¶

    

Start entering text which filters the set of channels shown to only include
those with matching names

bpy.ops.anim.channels_setting_disable(_*_ , _mode =DISABLE_, _type =PROTECT_)¶

    

Disable specified setting on all selected animation channels

Parameters:

    

  * **mode** (enum in [`TOGGLE`, `DISABLE`, `ENABLE`, `INVERT`], (optional)) – Mode

  * **type** (enum in [`PROTECT`, `MUTE`], (optional)) – Type

bpy.ops.anim.channels_setting_enable(_*_ , _mode =ENABLE_, _type =PROTECT_)¶

    

Enable specified setting on all selected animation channels

Parameters:

    

  * **mode** (enum in [`TOGGLE`, `DISABLE`, `ENABLE`, `INVERT`], (optional)) – Mode

  * **type** (enum in [`PROTECT`, `MUTE`], (optional)) – Type

bpy.ops.anim.channels_setting_toggle(_*_ , _mode =TOGGLE_, _type =PROTECT_)¶

    

Toggle specified setting on all selected animation channels

Parameters:

    

  * **mode** (enum in [`TOGGLE`, `DISABLE`, `ENABLE`, `INVERT`], (optional)) – Mode

  * **type** (enum in [`PROTECT`, `MUTE`], (optional)) – Type

bpy.ops.anim.channels_ungroup()¶

    

Remove selected F-Curves from their current groups

bpy.ops.anim.channels_view_selected(_*_ , _include_handles =True_,
_use_preview_range =True_)¶

    

Reset viewable area to show the selected channels

Parameters:

    

  * **include_handles** (_boolean_ _,__(__optional_ _)_) – Include Handles, Include handles of keyframes when calculating extents

  * **use_preview_range** (_boolean_ _,__(__optional_ _)_) – Use Preview Range, Ignore frames outside of the preview range

bpy.ops.anim.clear_useless_actions(_*_ , _only_unused =True_)¶

    

Mark actions with no F-Curves for deletion after save and reload of file
preserving “action libraries”

Parameters:

    

**only_unused** (_boolean_ _,__(__optional_ _)_) – Only Unused, Only unused
(Fake User only) actions get considered

File:

    

[startup/bl_operators/anim.py:354](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L354)

bpy.ops.anim.convert_legacy_action()¶

    

Convert a legacy Action to a layered Action on the active object

bpy.ops.anim.copy_driver_button()¶

    

Copy the driver for the highlighted button

bpy.ops.anim.driver_button_add()¶

    

Add driver for the property under the cursor

bpy.ops.anim.driver_button_edit()¶

    

Edit the drivers for the connected property represented by the highlighted
button

bpy.ops.anim.driver_button_remove(_*_ , _all =True_)¶

    

Remove the driver(s) for the connected property(s) represented by the
highlighted button

Parameters:

    

**all** (_boolean_ _,__(__optional_ _)_) – All, Delete drivers for all
elements of the array

bpy.ops.anim.end_frame_set()¶

    

Set the current frame as the preview or scene end frame

bpy.ops.anim.keyframe_clear_button(_*_ , _all =True_)¶

    

Clear all keyframes on the currently active property

Parameters:

    

**all** (_boolean_ _,__(__optional_ _)_) – All, Clear keyframes from all
elements of the array

bpy.ops.anim.keyframe_clear_v3d(_*_ , _confirm =True_)¶

    

Remove all keyframe animation for selected objects

Parameters:

    

**confirm** (_boolean_ _,__(__optional_ _)_) – Confirm, Prompt for
confirmation

bpy.ops.anim.keyframe_delete(_*_ , _type =DEFAULT_)¶

    

Delete keyframes on the current frame for all properties in the specified
Keying Set

Parameters:

    

**type** (enum in [`DEFAULT`], (optional)) – Keying Set, The Keying Set to use

bpy.ops.anim.keyframe_delete_button(_*_ , _all =True_)¶

    

Delete current keyframe of current UI-active property

Parameters:

    

**all** (_boolean_ _,__(__optional_ _)_) – All, Delete keyframes from all
elements of the array

bpy.ops.anim.keyframe_delete_by_name(_*_ , _type =''_)¶

    

Alternate access to ‘Delete Keyframe’ for keymaps to use

Parameters:

    

**type** (_string_ _,__(__optional_ _,__never None_ _)_) – Keying Set, The
Keying Set to use

bpy.ops.anim.keyframe_delete_v3d(_*_ , _confirm =True_)¶

    

Remove keyframes on current frame for selected objects and bones

Parameters:

    

**confirm** (_boolean_ _,__(__optional_ _)_) – Confirm, Prompt for
confirmation

bpy.ops.anim.keyframe_insert(_*_ , _type =DEFAULT_)¶

    

Insert keyframes on the current frame using either the active keying set, or
the user preferences if no keying set is active

Parameters:

    

**type** (enum in [`DEFAULT`], (optional)) – Keying Set, The Keying Set to use

bpy.ops.anim.keyframe_insert_button(_*_ , _all =True_)¶

    

Insert a keyframe for current UI-active property

Parameters:

    

**all** (_boolean_ _,__(__optional_ _)_) – All, Insert a keyframe for all
element of the array

bpy.ops.anim.keyframe_insert_by_name(_*_ , _type =''_)¶

    

Alternate access to ‘Insert Keyframe’ for keymaps to use

Parameters:

    

**type** (_string_ _,__(__optional_ _,__never None_ _)_) – Keying Set, The
Keying Set to use

bpy.ops.anim.keyframe_insert_menu(_*_ , _type =DEFAULT_, _always_prompt
=False_)¶

    

Insert Keyframes for specified Keying Set, with menu of available Keying Sets
if undefined

Parameters:

    

  * **type** (enum in [`DEFAULT`], (optional)) – Keying Set, The Keying Set to use

  * **always_prompt** (_boolean_ _,__(__optional_ _)_) – Always Show Menu

bpy.ops.anim.keying_set_active_set(_*_ , _type =DEFAULT_)¶

    

Set a new active keying set

Parameters:

    

**type** (enum in [`DEFAULT`], (optional)) – Keying Set, The Keying Set to use

bpy.ops.anim.keying_set_add()¶

    

Add a new (empty) keying set to the active Scene

bpy.ops.anim.keying_set_export(_*_ , _filepath =''_, _filter_folder =True_,
_filter_text =True_, _filter_python =True_)¶

    

Export Keying Set to a Python script

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – filepath

  * **filter_folder** (_boolean_ _,__(__optional_ _)_) – Filter folders

  * **filter_text** (_boolean_ _,__(__optional_ _)_) – Filter text

  * **filter_python** (_boolean_ _,__(__optional_ _)_) – Filter Python

File:

    

[startup/bl_operators/anim.py:46](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L46)

bpy.ops.anim.keying_set_path_add()¶

    

Add empty path to active keying set

bpy.ops.anim.keying_set_path_remove()¶

    

Remove active Path from active keying set

bpy.ops.anim.keying_set_remove()¶

    

Remove the active keying set

bpy.ops.anim.keyingset_button_add(_*_ , _all =True_)¶

    

Add current UI-active property to current keying set

Parameters:

    

**all** (_boolean_ _,__(__optional_ _)_) – All, Add all elements of the array
to a Keying Set

bpy.ops.anim.keyingset_button_remove()¶

    

Remove current UI-active property from current keying set

bpy.ops.anim.merge_animation()¶

    

Merge the animation of the selected objects into the action of the active
object. Actions are not deleted by this, but might end up with zero users

bpy.ops.anim.paste_driver_button()¶

    

Paste the driver in the internal clipboard to the highlighted button

bpy.ops.anim.previewrange_clear()¶

    

Clear preview range

bpy.ops.anim.previewrange_set(_*_ , _xmin =0_, _xmax =0_, _ymin =0_, _ymax
=0_, _wait_for_input =True_)¶

    

Interactively define frame range used for playback

Parameters:

    

  * **xmin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Min

  * **xmax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Max

  * **ymin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Min

  * **ymax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Max

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

bpy.ops.anim.scene_range_frame()¶

    

Reset the horizontal view to the current scene frame range, taking the preview
range into account if it is active

bpy.ops.anim.separate_slots()¶

    

Move all slots of the action on the active object into newly created, separate
actions. All users of those slots will be reassigned to the new actions. The
current action won’t be deleted but will be empty and might end up having zero
users

bpy.ops.anim.slot_channels_move_to_new_action()¶

    

Move the selected slots into a newly created action

bpy.ops.anim.slot_new_for_id()¶

    

Create a new action slot for this data-block, to hold its animation

File:

    

[startup/bl_operators/anim.py:708](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L708)

bpy.ops.anim.slot_unassign_from_constraint()¶

    

Un-assign the action slot from this constraint

File:

    

[startup/bl_operators/anim.py:766](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L766)

bpy.ops.anim.slot_unassign_from_id()¶

    

Un-assign the action slot, effectively making this data-block non-animated

File:

    

[startup/bl_operators/anim.py:745](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L745)

bpy.ops.anim.slot_unassign_from_nla_strip()¶

    

Un-assign the action slot from this NLA strip, effectively making it non-
animated

File:

    

[startup/bl_operators/anim.py:766](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L766)

bpy.ops.anim.start_frame_set()¶

    

Set the current frame as the preview or scene start frame

bpy.ops.anim.update_animated_transform_constraints(_*_ ,
_use_convert_to_radians =True_)¶

    

Update f-curves/drivers affecting Transform constraints (use it with files
from 2.70 and earlier)

Parameters:

    

**use_convert_to_radians** (_boolean_ _,__(__optional_ _)_) – Convert to
Radians, Convert f-curves/drivers affecting rotations to radians.Warning: Use
this only once

File:

    

[startup/bl_operators/anim.py:389](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L389)

bpy.ops.anim.view_curve_in_graph_editor(_*_ , _all =False_, _isolate =False_)¶

    

Frame the property under the cursor in the Graph Editor

Parameters:

    

  * **all** (_boolean_ _,__(__optional_ _)_) – Show All, Frame the whole array property instead of only the index under the cursor

  * **isolate** (_boolean_ _,__(__optional_ _)_) – Isolate, Hides all F-Curves other than the ones being framed

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

