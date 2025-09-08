---
url: https://docs.blender.org/api/current/bpy.ops.screen.html
scraped_at: 2025-09-08T14:18:45.610533
title: Screen Operators¶
---

# Screen Operators¶

bpy.ops.screen.actionzone(_*_ , _modifier =0_)¶

    

Handle area action zones for mouse actions/gestures

Parameters:

    

**modifier** (_int in_ _[__0_ _,__2_ _]__,__(__optional_ _)_) – Modifier,
Modifier state

bpy.ops.screen.animation_cancel(_*_ , _restore_frame =True_)¶

    

Cancel animation, returning to the original frame

Parameters:

    

**restore_frame** (_boolean_ _,__(__optional_ _)_) – Restore Frame, Restore
the frame when animation was initialized

bpy.ops.screen.animation_play(_*_ , _reverse =False_, _sync =False_)¶

    

Play animation

Parameters:

    

  * **reverse** (_boolean_ _,__(__optional_ _)_) – Play in Reverse, Animation is played backwards

  * **sync** (_boolean_ _,__(__optional_ _)_) – Sync, Drop frames to maintain framerate

bpy.ops.screen.animation_step()¶

    

Step through animation by position

bpy.ops.screen.area_close()¶

    

Close selected area

bpy.ops.screen.area_dupli()¶

    

Duplicate selected area into new window

bpy.ops.screen.area_join(_*_ , _source_xy =(0, 0)_, _target_xy =(0, 0)_)¶

    

Join selected areas into new window

Parameters:

    

  * **source_xy** (_int array_ _of_ _2 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Source location

  * **target_xy** (_int array_ _of_ _2 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Target location

bpy.ops.screen.area_move(_*_ , _x =0_, _y =0_, _delta =0_)¶

    

Move selected area edges

Parameters:

    

  * **x** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X

  * **y** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y

  * **delta** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Delta

bpy.ops.screen.area_options()¶

    

Operations for splitting and merging

bpy.ops.screen.area_split(_*_ , _direction =HORIZONTAL_, _factor =0.5_,
_cursor =(0, 0)_)¶

    

Split selected area into new windows

Parameters:

    

  * **direction** (enum in [`HORIZONTAL`, `VERTICAL`], (optional)) – Direction

  * **factor** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Factor

  * **cursor** (_int array_ _of_ _2 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Cursor

bpy.ops.screen.area_swap(_*_ , _cursor =(0, 0)_)¶

    

Swap selected areas screen positions

Parameters:

    

**cursor** (_int array_ _of_ _2 items in_ _[__-inf_ _,__inf_
_]__,__(__optional_ _)_) – Cursor

bpy.ops.screen.back_to_previous()¶

    

Revert back to the original screen layout, before fullscreen area overlay

bpy.ops.screen.delete()¶

    

Delete active screen

bpy.ops.screen.drivers_editor_show()¶

    

Show drivers editor in a separate window

bpy.ops.screen.frame_jump(_*_ , _end =False_)¶

    

Jump to first/last frame in frame range

Parameters:

    

**end** (_boolean_ _,__(__optional_ _)_) – Last Frame, Jump to the last frame
of the frame range

bpy.ops.screen.frame_offset(_*_ , _delta =0_)¶

    

Move current frame forward/backward by a given number

Parameters:

    

**delta** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Delta

bpy.ops.screen.header_toggle_menus()¶

    

Expand or collapse the header pull-down menus

bpy.ops.screen.info_log_show()¶

    

Show info log in a separate window

bpy.ops.screen.keyframe_jump(_*_ , _next =True_)¶

    

Jump to previous/next keyframe

Parameters:

    

**next** (_boolean_ _,__(__optional_ _)_) – Next Keyframe

bpy.ops.screen.marker_jump(_*_ , _next =True_)¶

    

Jump to previous/next marker

Parameters:

    

**next** (_boolean_ _,__(__optional_ _)_) – Next Marker

bpy.ops.screen.new()¶

    

Add a new screen

bpy.ops.screen.redo_last()¶

    

Display parameters for last action performed

bpy.ops.screen.region_blend()¶

    

Blend in and out overlapping region

bpy.ops.screen.region_context_menu()¶

    

Display region context menu

bpy.ops.screen.region_flip()¶

    

Toggle the region’s alignment (left/right or top/bottom)

bpy.ops.screen.region_quadview()¶

    

Split selected area into camera, front, right, and top views

bpy.ops.screen.region_scale()¶

    

Scale selected area

bpy.ops.screen.region_toggle(_*_ , _region_type =WINDOW_)¶

    

Hide or unhide the region

Parameters:

    

**region_type** (enum in [Region Type
Items](bpy_types_enum_items/region_type_items.html#rna-enum-region-type-
items), (optional)) – Region Type, Type of the region to toggle

bpy.ops.screen.repeat_history(_*_ , _index =0_)¶

    

Display menu for previous actions performed

Parameters:

    

**index** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Index

bpy.ops.screen.repeat_last()¶

    

Repeat last action

bpy.ops.screen.screen_full_area(_*_ , _use_hide_panels =False_)¶

    

Toggle display selected area as fullscreen/maximized

Parameters:

    

**use_hide_panels** (_boolean_ _,__(__optional_ _)_) – Hide Panels, Hide all
the panels

bpy.ops.screen.screen_set(_*_ , _delta =1_)¶

    

Cycle through available screens

Parameters:

    

**delta** (_int in_ _[__-1_ _,__1_ _]__,__(__optional_ _)_) – Delta

bpy.ops.screen.screenshot(_*_ , _filepath =''_, _hide_props_region =True_,
_check_existing =True_, _filter_blender =False_, _filter_backup =False_,
_filter_image =True_, _filter_movie =False_, _filter_python =False_,
_filter_font =False_, _filter_sound =False_, _filter_text =False_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =9_, _show_multiview =False_, _use_multiview =False_, _display_type
=DEFAULT_, _sort_method_)¶

    

Capture a picture of the whole Blender window

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

  * **hide_props_region** (_boolean_ _,__(__optional_ _)_) – Hide Operator Properties, Collapse the region displaying the operator settings

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

bpy.ops.screen.screenshot_area(_*_ , _filepath =''_, _hide_props_region
=True_, _check_existing =True_, _filter_blender =False_, _filter_backup
=False_, _filter_image =True_, _filter_movie =False_, _filter_python =False_,
_filter_font =False_, _filter_sound =False_, _filter_text =False_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =9_, _show_multiview =False_, _use_multiview =False_, _display_type
=DEFAULT_, _sort_method_)¶

    

Capture a picture of an editor

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

  * **hide_props_region** (_boolean_ _,__(__optional_ _)_) – Hide Operator Properties, Collapse the region displaying the operator settings

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

bpy.ops.screen.space_context_cycle(_*_ , _direction =NEXT_)¶

    

Cycle through the editor context by activating the next/previous one

Parameters:

    

**direction** (enum in [`PREV`, `NEXT`], (optional)) – Direction, Direction to
cycle through

bpy.ops.screen.space_type_set_or_cycle(_*_ , _space_type =EMPTY_)¶

    

Set the space type or cycle subtype

Parameters:

    

**space_type** (enum in [Space Type
Items](bpy_types_enum_items/space_type_items.html#rna-enum-space-type-items),
(optional)) – Type

bpy.ops.screen.spacedata_cleanup()¶

    

Remove unused settings for invisible editors

bpy.ops.screen.userpref_show(_*_ , _section =INTERFACE_)¶

    

Edit user preferences and system settings

Parameters:

    

**section** (enum in [Preference Section
Items](bpy_types_enum_items/preference_section_items.html#rna-enum-preference-
section-items), (optional)) – Section to activate in the Preferences

bpy.ops.screen.workspace_cycle(_*_ , _direction =NEXT_)¶

    

Cycle through workspaces

Parameters:

    

**direction** (enum in [`PREV`, `NEXT`], (optional)) – Direction, Direction to
cycle through

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

