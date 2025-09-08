---
url: https://docs.blender.org/api/current/bpy.ops.clip.html
scraped_at: 2025-09-08T14:17:57.494392
title: Clip Operators¶
---

# Clip Operators¶

bpy.ops.clip.add_marker(_*_ , _location =(0.0, 0.0)_)¶

    

Place new marker at specified location

Parameters:

    

**location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector
"mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location,
Location of marker on frame

bpy.ops.clip.add_marker_at_click()¶

    

Place new marker at the desired (clicked) position

bpy.ops.clip.add_marker_move(_*_ , _CLIP_OT_add_marker =None_,
_TRANSFORM_OT_translate =None_)¶

    

Add new marker and move it on movie

Parameters:

    

  * **CLIP_OT_add_marker** (`CLIP_OT_add_marker`, (optional)) – Add Marker, Place new marker at specified location

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.clip.add_marker_slide(_*_ , _CLIP_OT_add_marker =None_,
_TRANSFORM_OT_translate =None_)¶

    

Add new marker and slide it with mouse until mouse button release

Parameters:

    

  * **CLIP_OT_add_marker** (`CLIP_OT_add_marker`, (optional)) – Add Marker, Place new marker at specified location

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.clip.apply_solution_scale(_*_ , _distance =0.0_)¶

    

Apply scale on solution itself to make distance between selected tracks equals
to desired

Parameters:

    

**distance** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) –
Distance, Distance between selected tracks

bpy.ops.clip.average_tracks(_*_ , _keep_original =True_)¶

    

Average selected tracks into active

Parameters:

    

**keep_original** (_boolean_ _,__(__optional_ _)_) – Keep Original, Keep
original tracks

bpy.ops.clip.bundles_to_mesh()¶

    

Create vertex cloud using coordinates of reconstructed tracks

File:

    

[startup/bl_operators/clip.py:292](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L292)

bpy.ops.clip.camera_preset_add(_*_ , _name =''_, _remove_name =False_,
_remove_active =False_, _use_focal_length =True_)¶

    

Add or remove a Tracking Camera Intrinsics Preset

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the preset, used to make the path name

  * **remove_name** (_boolean_ _,__(__optional_ _)_) – remove_name

  * **remove_active** (_boolean_ _,__(__optional_ _)_) – remove_active

  * **use_focal_length** (_boolean_ _,__(__optional_ _)_) – Include Focal Length, Include focal length into the preset

File:

    

[startup/bl_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.clip.change_frame(_*_ , _frame =0_)¶

    

Interactively change the current frame number

Parameters:

    

**frame** (_int in_ _[__-1048574_ _,__1048574_ _]__,__(__optional_ _)_) –
Frame

bpy.ops.clip.clean_tracks(_*_ , _frames =0_, _error =0.0_, _action =SELECT_)¶

    

Clean tracks with high error values or few frames

Parameters:

    

  * **frames** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Tracked Frames, Affect tracks which are tracked less than the specified number of frames

  * **error** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Reprojection Error, Affect tracks which have a larger reprojection error

  * **action** (enum in [`SELECT`, `DELETE_TRACK`, `DELETE_SEGMENTS`], (optional)) – 

Action, Cleanup action to execute

    * `SELECT` Select – Select unclean tracks.

    * `DELETE_TRACK` Delete Track – Delete unclean tracks.

    * `DELETE_SEGMENTS` Delete Segments – Delete unclean segments of tracks.

bpy.ops.clip.clear_solution()¶

    

Clear all calculated data

bpy.ops.clip.clear_track_path(_*_ , _action =REMAINED_, _clear_active
=False_)¶

    

Clear tracks after/before current position or clear the whole track

Parameters:

    

  * **action** (enum in [`UPTO`, `REMAINED`, `ALL`], (optional)) – 

Action, Clear action to execute

    * `UPTO` Clear Up To – Clear path up to current frame.

    * `REMAINED` Clear Remained – Clear path at remaining frames (after current).

    * `ALL` Clear All – Clear the whole path.

  * **clear_active** (_boolean_ _,__(__optional_ _)_) – Clear Active, Clear active track only instead of all selected tracks

bpy.ops.clip.constraint_to_fcurve()¶

    

Create F-Curves for object which will copy object’s movement caused by this
constraint

File:

    

[startup/bl_operators/clip.py:530](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L530)

bpy.ops.clip.copy_tracks()¶

    

Copy the selected tracks to the internal clipboard

bpy.ops.clip.create_plane_track()¶

    

Create new plane track out of selected point tracks

bpy.ops.clip.cursor_set(_*_ , _location =(0.0, 0.0)_)¶

    

Set 2D cursor location

Parameters:

    

**location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector
"mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Cursor
location in normalized clip coordinates

bpy.ops.clip.delete_marker(_*_ , _confirm =True_)¶

    

Delete marker for current frame from selected tracks

Parameters:

    

**confirm** (_boolean_ _,__(__optional_ _)_) – Confirm, Prompt for
confirmation

bpy.ops.clip.delete_proxy()¶

    

Delete movie clip proxy files from the hard drive

File:

    

[startup/bl_operators/clip.py:359](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L359)

bpy.ops.clip.delete_track(_*_ , _confirm =True_)¶

    

Delete selected tracks

Parameters:

    

**confirm** (_boolean_ _,__(__optional_ _)_) – Confirm, Prompt for
confirmation

bpy.ops.clip.detect_features(_*_ , _placement =FRAME_, _margin =16_,
_threshold =0.5_, _min_distance =120_)¶

    

Automatically detect features and place markers to track

Parameters:

    

  * **placement** (enum in [`FRAME`, `INSIDE_GPENCIL`, `OUTSIDE_GPENCIL`], (optional)) – 

Placement, Placement for detected features

    * `FRAME` Whole Frame – Place markers across the whole frame.

    * `INSIDE_GPENCIL` Inside Annotated Area – Place markers only inside areas outlined with the Annotation tool.

    * `OUTSIDE_GPENCIL` Outside Annotated Area – Place markers only outside areas outlined with the Annotation tool.

  * **margin** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Margin, Only features further than margin pixels from the image edges are considered

  * **threshold** (_float in_ _[__0.0001_ _,__inf_ _]__,__(__optional_ _)_) – Threshold, Threshold level to consider feature good enough for tracking

  * **min_distance** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Distance, Minimal distance accepted between two features

bpy.ops.clip.disable_markers(_*_ , _action =DISABLE_)¶

    

Disable/enable selected markers

Parameters:

    

**action** (enum in [`DISABLE`, `ENABLE`, `TOGGLE`], (optional)) –

Action, Disable action to execute

  * `DISABLE` Disable – Disable selected markers.

  * `ENABLE` Enable – Enable selected markers.

  * `TOGGLE` Toggle – Toggle disabled flag for selected markers.

bpy.ops.clip.dopesheet_select_channel(_*_ , _location =(0.0, 0.0)_, _extend
=False_)¶

    

Select movie tracking channel

Parameters:

    

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Mouse location to select channel

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection rather than clearing the existing selection

bpy.ops.clip.dopesheet_view_all()¶

    

Reset viewable area to show full keyframe range

bpy.ops.clip.filter_tracks(_*_ , _track_threshold =5.0_)¶

    

Filter tracks which has weirdly looking spikes in motion curves

Parameters:

    

**track_threshold** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) –
Track Threshold, Filter Threshold to select problematic tracks

File:

    

[startup/bl_operators/clip.py:206](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L206)

bpy.ops.clip.frame_jump(_*_ , _position =PATHSTART_)¶

    

Jump to special frame

Parameters:

    

**position** (enum in [`PATHSTART`, `PATHEND`, `FAILEDPREV`, `FAILNEXT`],
(optional)) –

Position, Position to jump to

  * `PATHSTART` Path Start – Jump to start of current path.

  * `PATHEND` Path End – Jump to end of current path.

  * `FAILEDPREV` Previous Failed – Jump to previous failed frame.

  * `FAILNEXT` Next Failed – Jump to next failed frame.

bpy.ops.clip.graph_center_current_frame()¶

    

Scroll view so current frame would be centered

bpy.ops.clip.graph_delete_curve(_*_ , _confirm =True_)¶

    

Delete track corresponding to the selected curve

Parameters:

    

**confirm** (_boolean_ _,__(__optional_ _)_) – Confirm, Prompt for
confirmation

bpy.ops.clip.graph_delete_knot()¶

    

Delete curve knots

bpy.ops.clip.graph_disable_markers(_*_ , _action =DISABLE_)¶

    

Disable/enable selected markers

Parameters:

    

**action** (enum in [`DISABLE`, `ENABLE`, `TOGGLE`], (optional)) –

Action, Disable action to execute

  * `DISABLE` Disable – Disable selected markers.

  * `ENABLE` Enable – Enable selected markers.

  * `TOGGLE` Toggle – Toggle disabled flag for selected markers.

bpy.ops.clip.graph_select(_*_ , _location =(0.0, 0.0)_, _extend =False_)¶

    

Select graph curves

Parameters:

    

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Mouse location to select nearest entity

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection rather than clearing the existing selection

bpy.ops.clip.graph_select_all_markers(_*_ , _action =TOGGLE_)¶

    

Change selection of all markers of active track

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.clip.graph_select_box(_*_ , _xmin =0_, _xmax =0_, _ymin =0_, _ymax
=0_, _wait_for_input =True_, _deselect =False_, _extend =True_)¶

    

Select curve points using box selection

Parameters:

    

  * **xmin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Min

  * **xmax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Max

  * **ymin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Min

  * **ymax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Max

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

  * **deselect** (_boolean_ _,__(__optional_ _)_) – Deselect, Deselect rather than select items

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection instead of deselecting everything first

bpy.ops.clip.graph_view_all()¶

    

View all curves in editor

bpy.ops.clip.hide_tracks(_*_ , _unselected =False_)¶

    

Hide selected tracks

Parameters:

    

**unselected** (_boolean_ _,__(__optional_ _)_) – Unselected, Hide unselected
tracks

bpy.ops.clip.hide_tracks_clear()¶

    

Clear hide selected tracks

bpy.ops.clip.join_tracks()¶

    

Join selected tracks

bpy.ops.clip.keyframe_delete()¶

    

Delete a keyframe from selected tracks at current frame

bpy.ops.clip.keyframe_insert()¶

    

Insert a keyframe to selected tracks at current frame

bpy.ops.clip.lock_selection_toggle()¶

    

Toggle Lock Selection option of the current clip editor

bpy.ops.clip.lock_tracks(_*_ , _action =LOCK_)¶

    

Lock/unlock selected tracks

Parameters:

    

**action** (enum in [`LOCK`, `UNLOCK`, `TOGGLE`], (optional)) –

Action, Lock action to execute

  * `LOCK` Lock – Lock selected tracks.

  * `UNLOCK` Unlock – Unlock selected tracks.

  * `TOGGLE` Toggle – Toggle locked flag for selected tracks.

bpy.ops.clip.mode_set(_*_ , _mode =TRACKING_)¶

    

Set the clip interaction mode

Parameters:

    

**mode** (enum in [Clip Editor Mode
Items](bpy_types_enum_items/clip_editor_mode_items.html#rna-enum-clip-editor-
mode-items), (optional)) – Mode

bpy.ops.clip.new_image_from_plane_marker()¶

    

Create new image from the content of the plane marker

bpy.ops.clip.open(_*_ , _directory =''_, _files =None_, _hide_props_region
=True_, _check_existing =False_, _filter_blender =False_, _filter_backup
=False_, _filter_image =True_, _filter_movie =True_, _filter_python =False_,
_filter_font =False_, _filter_sound =False_, _filter_text =False_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =9_, _relative_path =True_, _show_multiview =False_, _use_multiview
=False_, _display_type =DEFAULT_, _sort_method_)¶

    

Load a sequence of frames or a movie file

Parameters:

    

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Directory, Directory of the file

  * **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – Files

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

  * **relative_path** (_boolean_ _,__(__optional_ _)_) – Relative Path, Select the file relative to the blend file

  * **show_multiview** (_boolean_ _,__(__optional_ _)_) – Enable Multi-View

  * **use_multiview** (_boolean_ _,__(__optional_ _)_) – Use Multi-View

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (enum in [`DEFAULT`, `FILE_SORT_ALPHA`, `FILE_SORT_EXTENSION`, `FILE_SORT_TIME`, `FILE_SORT_SIZE`, `ASSET_CATALOG`], (optional)) – 

File sorting mode

    * `DEFAULT` Default – Automatically determine sort method for files.

    * `FILE_SORT_ALPHA` Name – Sort the file list alphabetically.

    * `FILE_SORT_EXTENSION` Extension – Sort the file list by extension/type.

    * `FILE_SORT_TIME` Modified Date – Sort files by modification time.

    * `FILE_SORT_SIZE` Size – Sort files by size.

    * `ASSET_CATALOG` Asset Catalog – Sort the asset list so that assets in the same catalog are kept together. Within a single catalog, assets are ordered by name. The catalogs are in order of the flattened catalog hierarchy..

bpy.ops.clip.paste_tracks()¶

    

Paste tracks from the internal clipboard

bpy.ops.clip.prefetch()¶

    

Prefetch frames from disk for faster playback/tracking

bpy.ops.clip.rebuild_proxy()¶

    

Rebuild all selected proxies and timecode indices in the background

bpy.ops.clip.refine_markers(_*_ , _backwards =False_)¶

    

Refine selected markers positions by running the tracker from track’s
reference to current frame

Parameters:

    

**backwards** (_boolean_ _,__(__optional_ _)_) – Backwards, Do backwards
tracking

bpy.ops.clip.reload()¶

    

Reload clip

bpy.ops.clip.select(_*_ , _extend =False_, _deselect_all =False_, _location
=(0.0, 0.0)_)¶

    

Select tracking markers

Parameters:

    

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection rather than clearing the existing selection

  * **deselect_all** (_boolean_ _,__(__optional_ _)_) – Deselect On Nothing, Deselect all when nothing under the cursor

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds

bpy.ops.clip.select_all(_*_ , _action =TOGGLE_)¶

    

Change selection of all tracking markers

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.clip.select_box(_*_ , _xmin =0_, _xmax =0_, _ymin =0_, _ymax =0_,
_wait_for_input =True_, _mode =SET_)¶

    

Select markers using box selection

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

bpy.ops.clip.select_circle(_*_ , _x =0_, _y =0_, _radius =25_, _wait_for_input
=True_, _mode =SET_)¶

    

Select markers using circle selection

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

bpy.ops.clip.select_grouped(_*_ , _group =ESTIMATED_)¶

    

Select all tracks from specified group

Parameters:

    

**group** (enum in [`KEYFRAMED`, `ESTIMATED`, `TRACKED`, `LOCKED`, `DISABLED`,
`COLOR`, `FAILED`], (optional)) –

Action, Clear action to execute

  * `KEYFRAMED` Keyframed Tracks – Select all keyframed tracks.

  * `ESTIMATED` Estimated Tracks – Select all estimated tracks.

  * `TRACKED` Tracked Tracks – Select all tracked tracks.

  * `LOCKED` Locked Tracks – Select all locked tracks.

  * `DISABLED` Disabled Tracks – Select all disabled tracks.

  * `COLOR` Tracks with Same Color – Select all tracks with same color as active track.

  * `FAILED` Failed Tracks – Select all tracks which failed to be reconstructed.

bpy.ops.clip.select_lasso(_*_ , _path =None_, _use_smooth_stroke =False_,
_smooth_stroke_factor =0.75_, _smooth_stroke_radius =35_, _mode =SET_)¶

    

Select markers using lasso selection

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

bpy.ops.clip.set_active_clip()¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

File:

    

[startup/bl_operators/clip.py:221](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L221)

bpy.ops.clip.set_axis(_*_ , _axis =X_)¶

    

Set the direction of a scene axis by rotating the camera (or its parent if
present). This assumes that the selected track lies on a real axis connecting
it to the origin

Parameters:

    

**axis** (enum in [`X`, `Y`], (optional)) –

Axis, Axis to use to align bundle along

  * `X` X – Align bundle align X axis.

  * `Y` Y – Align bundle align Y axis.

bpy.ops.clip.set_origin(_*_ , _use_median =False_)¶

    

Set active marker as origin by moving camera (or its parent if present) in 3D
space

Parameters:

    

**use_median** (_boolean_ _,__(__optional_ _)_) – Use Median, Set origin to
median point of selected bundles

bpy.ops.clip.set_plane(_*_ , _plane =FLOOR_)¶

    

Set plane based on 3 selected bundles by moving camera (or its parent if
present) in 3D space

Parameters:

    

**plane** (enum in [`FLOOR`, `WALL`], (optional)) –

Plane, Plane to be used for orientation

  * `FLOOR` Floor – Set floor plane.

  * `WALL` Wall – Set wall plane.

bpy.ops.clip.set_scale(_*_ , _distance =0.0_)¶

    

Set scale of scene by scaling camera (or its parent if present)

Parameters:

    

**distance** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) –
Distance, Distance between selected tracks

bpy.ops.clip.set_scene_frames()¶

    

Set scene’s start and end frame to match clip’s start frame and length

bpy.ops.clip.set_solution_scale(_*_ , _distance =0.0_)¶

    

Set object solution scale using distance between two selected tracks

Parameters:

    

**distance** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) –
Distance, Distance between selected tracks

bpy.ops.clip.set_solver_keyframe(_*_ , _keyframe =KEYFRAME_A_)¶

    

Set keyframe used by solver

Parameters:

    

**keyframe** (enum in [`KEYFRAME_A`, `KEYFRAME_B`], (optional)) – Keyframe,
Keyframe to set

bpy.ops.clip.set_viewport_background()¶

    

Set current movie clip as a camera background in 3D Viewport (works only when
a 3D Viewport is visible)

File:

    

[startup/bl_operators/clip.py:420](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L420)

bpy.ops.clip.setup_tracking_scene()¶

    

Prepare scene for compositing 3D objects into this footage

File:

    

[startup/bl_operators/clip.py:991](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L991)

bpy.ops.clip.slide_marker(_*_ , _offset =(0.0, 0.0)_)¶

    

Slide marker areas

Parameters:

    

**offset** ([`mathutils.Vector`](mathutils.html#mathutils.Vector
"mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Offset, Offset in
floating-point units, 1.0 is the width and height of the image

bpy.ops.clip.slide_plane_marker()¶

    

Slide plane marker areas

bpy.ops.clip.solve_camera()¶

    

Solve camera motion from tracks

bpy.ops.clip.stabilize_2d_add()¶

    

Add selected tracks to 2D translation stabilization

bpy.ops.clip.stabilize_2d_remove()¶

    

Remove selected track from translation stabilization

bpy.ops.clip.stabilize_2d_rotation_add()¶

    

Add selected tracks to 2D rotation stabilization

bpy.ops.clip.stabilize_2d_rotation_remove()¶

    

Remove selected track from rotation stabilization

bpy.ops.clip.stabilize_2d_rotation_select()¶

    

Select tracks which are used for rotation stabilization

bpy.ops.clip.stabilize_2d_select()¶

    

Select tracks which are used for translation stabilization

bpy.ops.clip.track_color_preset_add(_*_ , _name =''_, _remove_name =False_,
_remove_active =False_)¶

    

Add or remove a Clip Track Color Preset

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the preset, used to make the path name

  * **remove_name** (_boolean_ _,__(__optional_ _)_) – remove_name

  * **remove_active** (_boolean_ _,__(__optional_ _)_) – remove_active

File:

    

[startup/bl_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.clip.track_copy_color()¶

    

Copy color to all selected tracks

bpy.ops.clip.track_markers(_*_ , _backwards =False_, _sequence =False_)¶

    

Track selected markers

Parameters:

    

  * **backwards** (_boolean_ _,__(__optional_ _)_) – Backwards, Do backwards tracking

  * **sequence** (_boolean_ _,__(__optional_ _)_) – Track Sequence, Track marker during image sequence rather than single image

bpy.ops.clip.track_settings_as_default()¶

    

Copy tracking settings from active track to default settings

File:

    

[startup/bl_operators/clip.py:1020](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L1020)

bpy.ops.clip.track_settings_to_track()¶

    

Copy tracking settings from active track to selected tracks

File:

    

[startup/bl_operators/clip.py:1069](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L1069)

bpy.ops.clip.track_to_empty()¶

    

Create an Empty object which will be copying movement of active track

File:

    

[startup/bl_operators/clip.py:268](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L268)

bpy.ops.clip.tracking_object_new()¶

    

Add new object for tracking

bpy.ops.clip.tracking_object_remove()¶

    

Remove object for tracking

bpy.ops.clip.tracking_settings_preset_add(_*_ , _name =''_, _remove_name
=False_, _remove_active =False_)¶

    

Add or remove a motion tracking settings preset

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the preset, used to make the path name

  * **remove_name** (_boolean_ _,__(__optional_ _)_) – remove_name

  * **remove_active** (_boolean_ _,__(__optional_ _)_) – remove_active

File:

    

[startup/bl_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.clip.update_image_from_plane_marker()¶

    

Update current image used by plane marker from the content of the plane marker

bpy.ops.clip.view_all(_*_ , _fit_view =False_)¶

    

View whole image with markers

Parameters:

    

**fit_view** (_boolean_ _,__(__optional_ _)_) – Fit View, Fit frame to the
viewport

bpy.ops.clip.view_center_cursor()¶

    

Center the view so that the cursor is in the middle of the view

bpy.ops.clip.view_ndof()¶

    

Use a 3D mouse device to pan/zoom the view

bpy.ops.clip.view_pan(_*_ , _offset =(0.0, 0.0)_)¶

    

Pan the view

Parameters:

    

**offset** ([`mathutils.Vector`](mathutils.html#mathutils.Vector
"mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Offset, Offset in
floating-point units, 1.0 is the width and height of the image

bpy.ops.clip.view_selected()¶

    

View all selected elements

bpy.ops.clip.view_zoom(_*_ , _factor =0.0_, _use_cursor_init =True_)¶

    

Zoom in/out the view

Parameters:

    

  * **factor** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Factor, Zoom factor, values higher than 1.0 zoom in, lower values zoom out

  * **use_cursor_init** (_boolean_ _,__(__optional_ _)_) – Use Mouse Position, Allow the initial mouse position to be used

bpy.ops.clip.view_zoom_in(_*_ , _location =(0.0, 0.0)_)¶

    

Zoom in the view

Parameters:

    

**location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector
"mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Cursor
location in screen coordinates

bpy.ops.clip.view_zoom_out(_*_ , _location =(0.0, 0.0)_)¶

    

Zoom out the view

Parameters:

    

**location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector
"mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Cursor
location in normalized (0.0 to 1.0) coordinates

bpy.ops.clip.view_zoom_ratio(_*_ , _ratio =0.0_)¶

    

Set the zoom ratio (based on clip size)

Parameters:

    

**ratio** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Ratio,
Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

