---
url: https://docs.blender.org/api/current/bpy.ops.sequencer.html
scraped_at: 2025-09-08T14:18:49.861475
title: Sequencer Operators¶
---

# Sequencer Operators¶

bpy.ops.sequencer.change_effect_type(_*_ , _type =CROSS_)¶

    

Replace effect strip with another that takes the same number of inputs

Parameters:

    

**type** (enum in [`CROSS`, `ADD`, `SUBTRACT`, `ALPHA_OVER`, `ALPHA_UNDER`,
`GAMMA_CROSS`, `MULTIPLY`, `WIPE`, `GLOW`, `TRANSFORM`, `COLOR`, `SPEED`,
`MULTICAM`, `ADJUSTMENT`, `GAUSSIAN_BLUR`, `TEXT`, `COLORMIX`], (optional)) –

Type, Strip effect type

  * `CROSS` Crossfade – Fade out of one video, fading into another.

  * `ADD` Add – Add together color channels from two videos.

  * `SUBTRACT` Subtract – Subtract one strip’s color from another.

  * `ALPHA_OVER` Alpha Over – Blend alpha on top of another video.

  * `ALPHA_UNDER` Alpha Under – Blend alpha below another video.

  * `GAMMA_CROSS` Gamma Crossfade – Crossfade with color correction.

  * `MULTIPLY` Multiply – Multiply color channels from two videos.

  * `WIPE` Wipe – Sweep a transition line across the frame.

  * `GLOW` Glow – Add blur and brightness to light areas.

  * `TRANSFORM` Transform – Apply scale, rotation, or translation.

  * `COLOR` Color – Add a simple color strip.

  * `SPEED` Speed – Timewarp video strips, modifying playback speed.

  * `MULTICAM` Multicam Selector – Control active camera angles.

  * `ADJUSTMENT` Adjustment Layer – Apply nondestructive effects.

  * `GAUSSIAN_BLUR` Gaussian Blur – Soften details along axes.

  * `TEXT` Text – Add a simple text strip.

  * `COLORMIX` Color Mix – Combine two strips using blend modes.

bpy.ops.sequencer.change_path(_*_ , _filepath =''_, _directory =''_, _files
=None_, _hide_props_region =True_, _check_existing =False_, _filter_blender
=False_, _filter_backup =False_, _filter_image =False_, _filter_movie =False_,
_filter_python =False_, _filter_font =False_, _filter_sound =False_,
_filter_text =False_, _filter_archive =False_, _filter_btx =False_,
_filter_collada =False_, _filter_alembic =False_, _filter_usd =False_,
_filter_obj =False_, _filter_volume =False_, _filter_folder =True_,
_filter_blenlib =False_, _filemode =9_, _relative_path =True_, _display_type
=DEFAULT_, _sort_method_ , _use_placeholders =False_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

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

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **use_placeholders** (_boolean_ _,__(__optional_ _)_) – Use Placeholders, Use placeholders for missing frames of the strip

bpy.ops.sequencer.change_scene(_*_ , _scene_)¶

    

Change Scene assigned to Strip

Parameters:

    

**scene** (_enum in_ _[__]__,__(__optional_ _)_) – Scene

bpy.ops.sequencer.connect(_*_ , _toggle =True_)¶

    

Link selected strips together for simplified group selection

Parameters:

    

**toggle** (_boolean_ _,__(__optional_ _)_) – Toggle, Toggle strip connections

bpy.ops.sequencer.copy()¶

    

Copy the selected strips to the internal clipboard

bpy.ops.sequencer.crossfade_sounds()¶

    

Do cross-fading volume animation of two selected sound strips

File:

    

[startup/bl_operators/sequencer.py:40](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/sequencer.py#L40)

bpy.ops.sequencer.cursor_set(_*_ , _location =(0.0, 0.0)_)¶

    

Set 2D cursor location

Parameters:

    

**location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector
"mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Cursor
location in normalized preview coordinates

bpy.ops.sequencer.deinterlace_selected_movies()¶

    

Deinterlace all selected movie sources

File:

    

[startup/bl_operators/sequencer.py:128](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/sequencer.py#L128)

bpy.ops.sequencer.delete(_*_ , _delete_data =False_)¶

    

Delete selected strips from the sequencer

Parameters:

    

**delete_data** (_boolean_ _,__(__optional_ _)_) – Delete Data, After removing
the Strip, delete the associated data also

bpy.ops.sequencer.disconnect()¶

    

Unlink selected strips so that they can be selected individually

bpy.ops.sequencer.duplicate()¶

    

Duplicate the selected strips

bpy.ops.sequencer.duplicate_move(_*_ , _SEQUENCER_OT_duplicate =None_,
_TRANSFORM_OT_seq_slide =None_)¶

    

Duplicate selected strips and move them

Parameters:

    

  * **SEQUENCER_OT_duplicate** (`SEQUENCER_OT_duplicate`, (optional)) – Duplicate Strips, Duplicate the selected strips

  * **TRANSFORM_OT_seq_slide** (`TRANSFORM_OT_seq_slide`, (optional)) – Sequence Slide, Slide a sequence strip in time

bpy.ops.sequencer.effect_strip_add(_*_ , _type =CROSS_, _frame_start =0_,
_frame_end =0_, _channel =1_, _replace_sel =True_, _overlap =False_,
_overlap_shuffle_override =False_, _skip_locked_or_muted_channels =True_,
_color =(0.0, 0.0, 0.0)_)¶

    

Add an effect to the sequencer, most are applied on top of existing strips

Parameters:

    

  * **type** (enum in [`CROSS`, `ADD`, `SUBTRACT`, `ALPHA_OVER`, `ALPHA_UNDER`, `GAMMA_CROSS`, `MULTIPLY`, `WIPE`, `GLOW`, `TRANSFORM`, `COLOR`, `SPEED`, `MULTICAM`, `ADJUSTMENT`, `GAUSSIAN_BLUR`, `TEXT`, `COLORMIX`], (optional)) – 

Type, Sequencer effect type

    * `CROSS` Crossfade – Fade out of one video, fading into another.

    * `ADD` Add – Add together color channels from two videos.

    * `SUBTRACT` Subtract – Subtract one strip’s color from another.

    * `ALPHA_OVER` Alpha Over – Blend alpha on top of another video.

    * `ALPHA_UNDER` Alpha Under – Blend alpha below another video.

    * `GAMMA_CROSS` Gamma Crossfade – Crossfade with color correction.

    * `MULTIPLY` Multiply – Multiply color channels from two videos.

    * `WIPE` Wipe – Sweep a transition line across the frame.

    * `GLOW` Glow – Add blur and brightness to light areas.

    * `TRANSFORM` Transform – Apply scale, rotation, or translation.

    * `COLOR` Color – Add a simple color strip.

    * `SPEED` Speed – Timewarp video strips, modifying playback speed.

    * `MULTICAM` Multicam Selector – Control active camera angles.

    * `ADJUSTMENT` Adjustment Layer – Apply nondestructive effects.

    * `GAUSSIAN_BLUR` Gaussian Blur – Soften details along axes.

    * `TEXT` Text – Add a simple text strip.

    * `COLORMIX` Color Mix – Combine two strips using blend modes.

  * **frame_start** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Start Frame, Start frame of the sequence strip

  * **frame_end** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – End Frame, End frame for the color strip

  * **channel** (_int in_ _[__1_ _,__128_ _]__,__(__optional_ _)_) – Channel, Channel to place this strip into

  * **replace_sel** (_boolean_ _,__(__optional_ _)_) – Replace Selection, Deselect previously selected strips

  * **overlap** (_boolean_ _,__(__optional_ _)_) – Allow Overlap, Don’t correct overlap on new sequence strips

  * **overlap_shuffle_override** (_boolean_ _,__(__optional_ _)_) – Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips

  * **skip_locked_or_muted_channels** (_boolean_ _,__(__optional_ _)_) – Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips

  * **color** ([`mathutils.Color`](mathutils.html#mathutils.Color "mathutils.Color") of 3 items in [0, 1], (optional)) – Color, Initialize the strip with this color

bpy.ops.sequencer.enable_proxies(_*_ , _proxy_25 =False_, _proxy_50 =False_,
_proxy_75 =False_, _proxy_100 =False_, _overwrite =False_)¶

    

Enable selected proxies on all selected Movie and Image strips

Parameters:

    

  * **proxy_25** (_boolean_ _,__(__optional_ _)_) – 25%

  * **proxy_50** (_boolean_ _,__(__optional_ _)_) – 50%

  * **proxy_75** (_boolean_ _,__(__optional_ _)_) – 75%

  * **proxy_100** (_boolean_ _,__(__optional_ _)_) – 100%

  * **overwrite** (_boolean_ _,__(__optional_ _)_) – Overwrite

bpy.ops.sequencer.export_subtitles(_*_ , _filepath =''_, _hide_props_region
=True_, _check_existing =True_, _filter_blender =False_, _filter_backup
=False_, _filter_image =False_, _filter_movie =False_, _filter_python =False_,
_filter_font =False_, _filter_sound =False_, _filter_text =False_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =8_, _display_type =DEFAULT_, _sort_method_)¶

    

Export .srt file containing text strips

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

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

bpy.ops.sequencer.fades_add(_*_ , _duration_seconds =1.0_, _type =IN_OUT_)¶

    

Adds or updates a fade animation for either visual or audio strips

Parameters:

    

  * **duration_seconds** (_float in_ _[__0.01_ _,__inf_ _]__,__(__optional_ _)_) – Fade Duration, Duration of the fade in seconds

  * **type** (enum in [`IN_OUT`, `IN`, `OUT`, `CURSOR_FROM`, `CURSOR_TO`], (optional)) – 

Fade Type, Fade in, out, both in and out, to, or from the current frame.
Default is both in and out

    * `IN_OUT` Fade In and Out – Fade selected strips in and out.

    * `IN` Fade In – Fade in selected strips.

    * `OUT` Fade Out – Fade out selected strips.

    * `CURSOR_FROM` From Current Frame – Fade from the time cursor to the end of overlapping strips.

    * `CURSOR_TO` To Current Frame – Fade from the start of strips under the time cursor to the current frame.

File:

    

[startup/bl_operators/sequencer.py:206](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/sequencer.py#L206)

bpy.ops.sequencer.fades_clear()¶

    

Removes fade animation from selected strips

File:

    

[startup/bl_operators/sequencer.py:147](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/sequencer.py#L147)

bpy.ops.sequencer.gap_insert(_*_ , _frames =10_)¶

    

Insert gap at current frame to first strips at the right, independent of
selection or locked state of strips

Parameters:

    

**frames** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Frames, Frames
to insert after current strip

bpy.ops.sequencer.gap_remove(_*_ , _all =False_)¶

    

Remove gap at current frame to first strip at the right, independent of
selection or locked state of strips

Parameters:

    

**all** (_boolean_ _,__(__optional_ _)_) – All Gaps, Do all gaps to right of
current frame

bpy.ops.sequencer.image_strip_add(_*_ , _directory =''_, _files =None_,
_check_existing =False_, _filter_blender =False_, _filter_backup =False_,
_filter_image =True_, _filter_movie =False_, _filter_python =False_,
_filter_font =False_, _filter_sound =False_, _filter_text =False_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =9_, _relative_path =True_, _show_multiview =False_, _use_multiview
=False_, _display_type =DEFAULT_, _sort_method_ , _frame_start =0_, _frame_end
=0_, _channel =1_, _replace_sel =True_, _overlap =False_,
_overlap_shuffle_override =False_, _skip_locked_or_muted_channels =True_,
_fit_method =FIT_, _set_view_transform =True_, _use_placeholders =False_)¶

    

Add an image or image sequence to the sequencer

Parameters:

    

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Directory, Directory of the file

  * **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – Files

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

  * **frame_start** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Start Frame, Start frame of the sequence strip

  * **frame_end** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – End Frame, End frame for the color strip

  * **channel** (_int in_ _[__1_ _,__128_ _]__,__(__optional_ _)_) – Channel, Channel to place this strip into

  * **replace_sel** (_boolean_ _,__(__optional_ _)_) – Replace Selection, Deselect previously selected strips

  * **overlap** (_boolean_ _,__(__optional_ _)_) – Allow Overlap, Don’t correct overlap on new sequence strips

  * **overlap_shuffle_override** (_boolean_ _,__(__optional_ _)_) – Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips

  * **skip_locked_or_muted_channels** (_boolean_ _,__(__optional_ _)_) – Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips

  * **fit_method** (enum in [`FIT`, `FILL`, `STRETCH`, `ORIGINAL`], (optional)) – 

Fit Method, Scale fit method

    * `FIT` Scale to Fit – Scale image to fit within the canvas.

    * `FILL` Scale to Fill – Scale image to completely fill the canvas.

    * `STRETCH` Stretch to Fill – Stretch image to fill the canvas.

    * `ORIGINAL` Use Original Size – Keep image at its original size.

  * **set_view_transform** (_boolean_ _,__(__optional_ _)_) – Set View Transform, Set appropriate view transform based on media color space

  * **use_placeholders** (_boolean_ _,__(__optional_ _)_) – Use Placeholders, Use placeholders for missing frames of the strip

bpy.ops.sequencer.images_separate(_*_ , _length =1_)¶

    

On image sequence strips, it returns a strip for each image

Parameters:

    

**length** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Length, Length
of each frame

bpy.ops.sequencer.lock()¶

    

Lock strips so they can’t be transformed

bpy.ops.sequencer.mask_strip_add(_*_ , _frame_start =0_, _channel =1_,
_replace_sel =True_, _overlap =False_, _overlap_shuffle_override =False_,
_skip_locked_or_muted_channels =True_, _mask_)¶

    

Add a mask strip to the sequencer

Parameters:

    

  * **frame_start** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Start Frame, Start frame of the sequence strip

  * **channel** (_int in_ _[__1_ _,__128_ _]__,__(__optional_ _)_) – Channel, Channel to place this strip into

  * **replace_sel** (_boolean_ _,__(__optional_ _)_) – Replace Selection, Deselect previously selected strips

  * **overlap** (_boolean_ _,__(__optional_ _)_) – Allow Overlap, Don’t correct overlap on new sequence strips

  * **overlap_shuffle_override** (_boolean_ _,__(__optional_ _)_) – Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips

  * **skip_locked_or_muted_channels** (_boolean_ _,__(__optional_ _)_) – Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips

  * **mask** (_enum in_ _[__]__,__(__optional_ _)_) – Mask

bpy.ops.sequencer.meta_make()¶

    

Group selected strips into a meta-strip

bpy.ops.sequencer.meta_separate()¶

    

Put the contents of a meta-strip back in the sequencer

bpy.ops.sequencer.meta_toggle()¶

    

Toggle a meta-strip (to edit enclosed strips)

bpy.ops.sequencer.movie_strip_add(_*_ , _filepath =''_, _directory =''_,
_files =None_, _check_existing =False_, _filter_blender =False_,
_filter_backup =False_, _filter_image =False_, _filter_movie =True_,
_filter_python =False_, _filter_font =False_, _filter_sound =False_,
_filter_text =False_, _filter_archive =False_, _filter_btx =False_,
_filter_collada =False_, _filter_alembic =False_, _filter_usd =False_,
_filter_obj =False_, _filter_volume =False_, _filter_folder =True_,
_filter_blenlib =False_, _filemode =9_, _relative_path =True_, _show_multiview
=False_, _use_multiview =False_, _display_type =DEFAULT_, _sort_method_ ,
_frame_start =0_, _channel =1_, _replace_sel =True_, _overlap =False_,
_overlap_shuffle_override =False_, _skip_locked_or_muted_channels =True_,
_fit_method =FIT_, _set_view_transform =True_, _adjust_playback_rate =True_,
_sound =True_, _use_framerate =True_)¶

    

Add a movie strip to the sequencer

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Directory, Directory of the file

  * **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – Files

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

  * **frame_start** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Start Frame, Start frame of the sequence strip

  * **channel** (_int in_ _[__1_ _,__128_ _]__,__(__optional_ _)_) – Channel, Channel to place this strip into

  * **replace_sel** (_boolean_ _,__(__optional_ _)_) – Replace Selection, Deselect previously selected strips

  * **overlap** (_boolean_ _,__(__optional_ _)_) – Allow Overlap, Don’t correct overlap on new sequence strips

  * **overlap_shuffle_override** (_boolean_ _,__(__optional_ _)_) – Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips

  * **skip_locked_or_muted_channels** (_boolean_ _,__(__optional_ _)_) – Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips

  * **fit_method** (enum in [`FIT`, `FILL`, `STRETCH`, `ORIGINAL`], (optional)) – 

Fit Method, Scale fit method

    * `FIT` Scale to Fit – Scale image to fit within the canvas.

    * `FILL` Scale to Fill – Scale image to completely fill the canvas.

    * `STRETCH` Stretch to Fill – Stretch image to fill the canvas.

    * `ORIGINAL` Use Original Size – Keep image at its original size.

  * **set_view_transform** (_boolean_ _,__(__optional_ _)_) – Set View Transform, Set appropriate view transform based on media color space

  * **adjust_playback_rate** (_boolean_ _,__(__optional_ _)_) – Adjust Playback Rate, Play at normal speed regardless of scene FPS

  * **sound** (_boolean_ _,__(__optional_ _)_) – Sound, Load sound with the movie

  * **use_framerate** (_boolean_ _,__(__optional_ _)_) – Set Scene Frame Rate, Set frame rate of the current scene to the frame rate of the movie

bpy.ops.sequencer.movieclip_strip_add(_*_ , _frame_start =0_, _channel =1_,
_replace_sel =True_, _overlap =False_, _overlap_shuffle_override =False_,
_skip_locked_or_muted_channels =True_, _clip_)¶

    

Add a movieclip strip to the sequencer

Parameters:

    

  * **frame_start** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Start Frame, Start frame of the sequence strip

  * **channel** (_int in_ _[__1_ _,__128_ _]__,__(__optional_ _)_) – Channel, Channel to place this strip into

  * **replace_sel** (_boolean_ _,__(__optional_ _)_) – Replace Selection, Deselect previously selected strips

  * **overlap** (_boolean_ _,__(__optional_ _)_) – Allow Overlap, Don’t correct overlap on new sequence strips

  * **overlap_shuffle_override** (_boolean_ _,__(__optional_ _)_) – Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips

  * **skip_locked_or_muted_channels** (_boolean_ _,__(__optional_ _)_) – Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips

  * **clip** (_enum in_ _[__]__,__(__optional_ _)_) – Clip

bpy.ops.sequencer.mute(_*_ , _unselected =False_)¶

    

Mute (un)selected strips

Parameters:

    

**unselected** (_boolean_ _,__(__optional_ _)_) – Unselected, Mute unselected
rather than selected strips

bpy.ops.sequencer.offset_clear()¶

    

Clear strip offsets from the start and end frames

bpy.ops.sequencer.paste(_*_ , _keep_offset =False_)¶

    

Paste strips from the internal clipboard

Parameters:

    

**keep_offset** (_boolean_ _,__(__optional_ _)_) – Keep Offset, Keep strip
offset relative to the current frame when pasting

bpy.ops.sequencer.preview_duplicate_move(_*_ , _SEQUENCER_OT_duplicate =None_,
_TRANSFORM_OT_translate =None_)¶

    

Duplicate selected strips and move them

Parameters:

    

  * **SEQUENCER_OT_duplicate** (`SEQUENCER_OT_duplicate`, (optional)) – Duplicate Strips, Duplicate the selected strips

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.sequencer.reassign_inputs()¶

    

Reassign the inputs for the effect strip

bpy.ops.sequencer.rebuild_proxy()¶

    

Rebuild all selected proxies and timecode indices

bpy.ops.sequencer.refresh_all()¶

    

Refresh the sequencer editor

bpy.ops.sequencer.reload(_*_ , _adjust_length =False_)¶

    

Reload strips in the sequencer

Parameters:

    

**adjust_length** (_boolean_ _,__(__optional_ _)_) – Adjust Length, Adjust
length of strips to their data length

bpy.ops.sequencer.rename_channel()¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

bpy.ops.sequencer.rendersize()¶

    

Set render size and aspect from active strip

bpy.ops.sequencer.retiming_add_freeze_frame_slide(_*_ ,
_SEQUENCER_OT_retiming_freeze_frame_add =None_, _TRANSFORM_OT_seq_slide
=None_)¶

    

Add freeze frame and move it

Parameters:

    

  * **SEQUENCER_OT_retiming_freeze_frame_add** (`SEQUENCER_OT_retiming_freeze_frame_add`, (optional)) – Add Freeze Frame, Add freeze frame

  * **TRANSFORM_OT_seq_slide** (`TRANSFORM_OT_seq_slide`, (optional)) – Sequence Slide, Slide a sequence strip in time

bpy.ops.sequencer.retiming_add_transition_slide(_*_ ,
_SEQUENCER_OT_retiming_transition_add =None_, _TRANSFORM_OT_seq_slide =None_)¶

    

Add smooth transition between 2 retimed segments and change its duration

Parameters:

    

  * **SEQUENCER_OT_retiming_transition_add** (`SEQUENCER_OT_retiming_transition_add`, (optional)) – Add Speed Transition, Add smooth transition between 2 retimed segments

  * **TRANSFORM_OT_seq_slide** (`TRANSFORM_OT_seq_slide`, (optional)) – Sequence Slide, Slide a sequence strip in time

bpy.ops.sequencer.retiming_freeze_frame_add(_*_ , _duration =0_)¶

    

Add freeze frame

Parameters:

    

**duration** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Duration,
Duration of freeze frame segment

bpy.ops.sequencer.retiming_key_add(_*_ , _timeline_frame =0_)¶

    

Add retiming Key

Parameters:

    

**timeline_frame** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) –
Timeline Frame, Frame where key will be added

bpy.ops.sequencer.retiming_key_delete()¶

    

Delete selected retiming keys from the sequencer

bpy.ops.sequencer.retiming_reset()¶

    

Reset strip retiming

bpy.ops.sequencer.retiming_segment_speed_set(_*_ , _speed =100.0_,
_keep_retiming =True_)¶

    

Set speed of retimed segment

Parameters:

    

  * **speed** (_float in_ _[__0.001_ _,__inf_ _]__,__(__optional_ _)_) – Speed, New speed of retimed segment

  * **keep_retiming** (_boolean_ _,__(__optional_ _)_) – Preserve Current Retiming, Keep speed of other segments unchanged, change strip length instead

bpy.ops.sequencer.retiming_show()¶

    

Show retiming keys in selected strips

bpy.ops.sequencer.retiming_transition_add(_*_ , _duration =0_)¶

    

Add smooth transition between 2 retimed segments

Parameters:

    

**duration** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Duration,
Duration of freeze frame segment

bpy.ops.sequencer.sample(_*_ , _size =1_)¶

    

Use mouse to sample color in current frame

Parameters:

    

**size** (_int in_ _[__1_ _,__128_ _]__,__(__optional_ _)_) – Sample Size

bpy.ops.sequencer.scene_frame_range_update()¶

    

Update frame range of scene strip

bpy.ops.sequencer.scene_strip_add(_*_ , _frame_start =0_, _channel =1_,
_replace_sel =True_, _overlap =False_, _overlap_shuffle_override =False_,
_skip_locked_or_muted_channels =True_, _scene_)¶

    

Add a strip to the sequencer using a Blender scene as a source

Parameters:

    

  * **frame_start** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Start Frame, Start frame of the sequence strip

  * **channel** (_int in_ _[__1_ _,__128_ _]__,__(__optional_ _)_) – Channel, Channel to place this strip into

  * **replace_sel** (_boolean_ _,__(__optional_ _)_) – Replace Selection, Deselect previously selected strips

  * **overlap** (_boolean_ _,__(__optional_ _)_) – Allow Overlap, Don’t correct overlap on new sequence strips

  * **overlap_shuffle_override** (_boolean_ _,__(__optional_ _)_) – Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips

  * **skip_locked_or_muted_channels** (_boolean_ _,__(__optional_ _)_) – Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips

  * **scene** (_enum in_ _[__]__,__(__optional_ _)_) – Scene

bpy.ops.sequencer.scene_strip_add_new(_*_ , _frame_start =0_, _channel =1_,
_replace_sel =True_, _overlap =False_, _overlap_shuffle_override =False_,
_skip_locked_or_muted_channels =True_, _type =NEW_)¶

    

Create a new Strip and assign a new Scene as source

Parameters:

    

  * **frame_start** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Start Frame, Start frame of the sequence strip

  * **channel** (_int in_ _[__1_ _,__128_ _]__,__(__optional_ _)_) – Channel, Channel to place this strip into

  * **replace_sel** (_boolean_ _,__(__optional_ _)_) – Replace Selection, Deselect previously selected strips

  * **overlap** (_boolean_ _,__(__optional_ _)_) – Allow Overlap, Don’t correct overlap on new sequence strips

  * **overlap_shuffle_override** (_boolean_ _,__(__optional_ _)_) – Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips

  * **skip_locked_or_muted_channels** (_boolean_ _,__(__optional_ _)_) – Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips

  * **type** (enum in [`NEW`, `EMPTY`, `LINK_COPY`, `FULL_COPY`], (optional)) – 

Type

    * `NEW` New – Add new Strip with a new empty Scene with default settings.

    * `EMPTY` Copy Settings – Add a new Strip, with an empty scene, and copy settings from the current scene.

    * `LINK_COPY` Linked Copy – Add a Strip and link in the collections from the current scene (shallow copy).

    * `FULL_COPY` Full Copy – Add a Strip and make a full copy of the current scene.

bpy.ops.sequencer.select(_*_ , _wait_to_deselect_others =False_, _mouse_x =0_,
_mouse_y =0_, _extend =False_, _deselect =False_, _toggle =False_,
_deselect_all =False_, _select_passthrough =False_, _center =False_,
_linked_handle =False_, _linked_time =False_, _side_of_frame =False_,
_ignore_connections =False_)¶

    

Select a strip (last selected becomes the “active strip”)

Parameters:

    

  * **wait_to_deselect_others** (_boolean_ _,__(__optional_ _)_) – Wait to Deselect Others

  * **mouse_x** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Mouse X

  * **mouse_y** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Mouse Y

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection instead of deselecting everything first

  * **deselect** (_boolean_ _,__(__optional_ _)_) – Deselect, Remove from selection

  * **toggle** (_boolean_ _,__(__optional_ _)_) – Toggle Selection, Toggle the selection

  * **deselect_all** (_boolean_ _,__(__optional_ _)_) – Deselect On Nothing, Deselect all when nothing under the cursor

  * **select_passthrough** (_boolean_ _,__(__optional_ _)_) – Only Select Unselected, Ignore the select action when the element is already selected

  * **center** (_boolean_ _,__(__optional_ _)_) – Center, Use the object center when selecting, in edit mode used to extend object selection

  * **linked_handle** (_boolean_ _,__(__optional_ _)_) – Linked Handle, Select handles next to the active strip

  * **linked_time** (_boolean_ _,__(__optional_ _)_) – Linked Time, Select other strips or handles at the same time, or all retiming keys after the current in retiming mode

  * **side_of_frame** (_boolean_ _,__(__optional_ _)_) – Side of Frame, Select all strips on same side of the current frame as the mouse cursor

  * **ignore_connections** (_boolean_ _,__(__optional_ _)_) – Ignore Connections, Select strips individually whether or not they are connected

bpy.ops.sequencer.select_all(_*_ , _action =TOGGLE_)¶

    

Select or deselect all strips

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.sequencer.select_box(_*_ , _xmin =0_, _xmax =0_, _ymin =0_, _ymax =0_,
_wait_for_input =True_, _mode =SET_, _tweak =False_, _include_handles =False_,
_ignore_connections =False_)¶

    

Select strips using box selection

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

  * **tweak** (_boolean_ _,__(__optional_ _)_) – Tweak, Make box select pass through to sequence slide when the cursor is hovering on a strip

  * **include_handles** (_boolean_ _,__(__optional_ _)_) – Select Handles, Select the strips and their handles

  * **ignore_connections** (_boolean_ _,__(__optional_ _)_) – Ignore Connections, Select strips individually whether or not they are connected

bpy.ops.sequencer.select_grouped(_*_ , _type =TYPE_, _extend =False_,
_use_active_channel =False_)¶

    

Select all strips grouped by various properties

Parameters:

    

  * **type** (enum in [`TYPE`, `TYPE_BASIC`, `TYPE_EFFECT`, `DATA`, `EFFECT`, `EFFECT_LINK`, `OVERLAP`], (optional)) – 

Type

    * `TYPE` Type – Shared strip type.

    * `TYPE_BASIC` Global Type – All strips of same basic type (graphical or sound).

    * `TYPE_EFFECT` Effect Type – Shared strip effect type (if active strip is not an effect one, select all non-effect strips).

    * `DATA` Data – Shared data (scene, image, sound, etc.).

    * `EFFECT` Effect – Shared effects.

    * `EFFECT_LINK` Effect/Linked – Other strips affected by the active one (sharing some time, and below or effect-assigned).

    * `OVERLAP` Overlap – Overlapping time.

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection instead of deselecting everything first

  * **use_active_channel** (_boolean_ _,__(__optional_ _)_) – Same Channel, Only consider strips on the same channel as the active one

bpy.ops.sequencer.select_handle(_*_ , _wait_to_deselect_others =False_,
_mouse_x =0_, _mouse_y =0_, _ignore_connections =False_)¶

    

Select strip handle

Parameters:

    

  * **wait_to_deselect_others** (_boolean_ _,__(__optional_ _)_) – Wait to Deselect Others

  * **mouse_x** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Mouse X

  * **mouse_y** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Mouse Y

  * **ignore_connections** (_boolean_ _,__(__optional_ _)_) – Ignore Connections, Select strips individually whether or not they are connected

bpy.ops.sequencer.select_handles(_*_ , _side =BOTH_)¶

    

Select gizmo handles on the sides of the selected strip

Parameters:

    

**side** (enum in [`LEFT`, `RIGHT`, `BOTH`, `LEFT_NEIGHBOR`, `RIGHT_NEIGHBOR`,
`BOTH_NEIGHBORS`], (optional)) – Side, The side of the handle that is selected

bpy.ops.sequencer.select_less()¶

    

Shrink the current selection of adjacent selected strips

bpy.ops.sequencer.select_linked()¶

    

Select all strips adjacent to the current selection

bpy.ops.sequencer.select_linked_pick(_*_ , _extend =False_)¶

    

Select a chain of linked strips nearest to the mouse pointer

Parameters:

    

**extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend the selection

bpy.ops.sequencer.select_more()¶

    

Select more strips adjacent to the current selection

bpy.ops.sequencer.select_side(_*_ , _side =BOTH_)¶

    

Select strips on the nominated side of the selected strips

Parameters:

    

**side** (enum in [`MOUSE`, `LEFT`, `RIGHT`, `BOTH`, `NO_CHANGE`], (optional))
– Side, The side to which the selection is applied

bpy.ops.sequencer.select_side_of_frame(_*_ , _extend =False_, _side =LEFT_)¶

    

Select strips relative to the current frame

Parameters:

    

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend the selection

  * **side** (enum in [`LEFT`, `RIGHT`, `CURRENT`], (optional)) – 

Side

    * `LEFT` Left – Select to the left of the current frame.

    * `RIGHT` Right – Select to the right of the current frame.

    * `CURRENT` Current Frame – Select intersecting with the current frame.

bpy.ops.sequencer.set_range_to_strips(_*_ , _preview =False_)¶

    

Set the frame range to the selected strips start and end

Parameters:

    

**preview** (_boolean_ _,__(__optional_ _)_) – Preview, Set the preview range
instead

bpy.ops.sequencer.slip(_*_ , _offset =0.0_, _slip_keyframes =False_)¶

    

Slip the contents of selected strips

Parameters:

    

  * **offset** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Offset, Offset to the data of the strip

  * **slip_keyframes** (_boolean_ _,__(__optional_ _)_) – Slip Keyframes, Move the keyframes alongside the media

bpy.ops.sequencer.snap(_*_ , _frame =0_)¶

    

Frame where selected strips will be snapped

Parameters:

    

**frame** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Frame, Frame
where selected strips will be snapped

bpy.ops.sequencer.sound_strip_add(_*_ , _filepath =''_, _directory =''_,
_files =None_, _check_existing =False_, _filter_blender =False_,
_filter_backup =False_, _filter_image =False_, _filter_movie =False_,
_filter_python =False_, _filter_font =False_, _filter_sound =True_,
_filter_text =False_, _filter_archive =False_, _filter_btx =False_,
_filter_collada =False_, _filter_alembic =False_, _filter_usd =False_,
_filter_obj =False_, _filter_volume =False_, _filter_folder =True_,
_filter_blenlib =False_, _filemode =9_, _relative_path =True_, _display_type
=DEFAULT_, _sort_method_ , _frame_start =0_, _channel =1_, _replace_sel
=True_, _overlap =False_, _overlap_shuffle_override =False_,
_skip_locked_or_muted_channels =True_, _cache =False_, _mono =False_)¶

    

Add a sound strip to the sequencer

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Directory, Directory of the file

  * **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – Files

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

  * **frame_start** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Start Frame, Start frame of the sequence strip

  * **channel** (_int in_ _[__1_ _,__128_ _]__,__(__optional_ _)_) – Channel, Channel to place this strip into

  * **replace_sel** (_boolean_ _,__(__optional_ _)_) – Replace Selection, Deselect previously selected strips

  * **overlap** (_boolean_ _,__(__optional_ _)_) – Allow Overlap, Don’t correct overlap on new sequence strips

  * **overlap_shuffle_override** (_boolean_ _,__(__optional_ _)_) – Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips

  * **skip_locked_or_muted_channels** (_boolean_ _,__(__optional_ _)_) – Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips

  * **cache** (_boolean_ _,__(__optional_ _)_) – Cache, Cache the sound in memory

  * **mono** (_boolean_ _,__(__optional_ _)_) – Mono, Merge all the sound’s channels into one

bpy.ops.sequencer.split(_*_ , _frame =0_, _channel =0_, _type =SOFT_,
_use_cursor_position =False_, _side =MOUSE_, _ignore_selection =False_)¶

    

Split the selected strips in two

Parameters:

    

  * **frame** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Frame, Frame where selected strips will be split

  * **channel** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Channel, Channel in which strip will be cut

  * **type** (enum in [`SOFT`, `HARD`], (optional)) – Type, The type of split operation to perform on strips

  * **use_cursor_position** (_boolean_ _,__(__optional_ _)_) – Use Cursor Position, Split at position of the cursor instead of current frame

  * **side** (enum in [`MOUSE`, `LEFT`, `RIGHT`, `BOTH`, `NO_CHANGE`], (optional)) – Side, The side that remains selected after splitting

  * **ignore_selection** (_boolean_ _,__(__optional_ _)_) – Ignore Selection, Make cut even if strip is not selected preserving selection state after cut

bpy.ops.sequencer.split_multicam(_*_ , _camera =1_)¶

    

Split multicam strip and select camera

Parameters:

    

**camera** (_int in_ _[__1_ _,__32_ _]__,__(__optional_ _)_) – Camera

File:

    

[startup/bl_operators/sequencer.py:95](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/sequencer.py#L95)

bpy.ops.sequencer.strip_color_tag_set(_*_ , _color =NONE_)¶

    

Set a color tag for the selected strips

Parameters:

    

**color** (enum in [Strip Color
Items](bpy_types_enum_items/strip_color_items.html#rna-enum-strip-color-
items), (optional)) – Color Tag

bpy.ops.sequencer.strip_jump(_*_ , _next =True_, _center =True_)¶

    

Move frame to previous edit point

Parameters:

    

  * **next** (_boolean_ _,__(__optional_ _)_) – Next Strip

  * **center** (_boolean_ _,__(__optional_ _)_) – Use Strip Center

bpy.ops.sequencer.strip_modifier_add(_*_ , _type_)¶

    

Add a modifier to the strip

Parameters:

    

**type** (_enum in_ _[__]__,__(__optional_ _)_) – Type

bpy.ops.sequencer.strip_modifier_copy(_*_ , _type =REPLACE_)¶

    

Copy modifiers of the active strip to all selected strips

Parameters:

    

**type** (enum in [`REPLACE`, `APPEND`], (optional)) –

Type

  * `REPLACE` Replace – Replace modifiers in destination.

  * `APPEND` Append – Append active modifiers to selected strips.

bpy.ops.sequencer.strip_modifier_equalizer_redefine(_*_ , _graphs =SIMPLE_,
_name ='Name'_)¶

    

Redefine equalizer graphs

Parameters:

    

  * **graphs** (enum in [`SIMPLE`, `DOUBLE`, `TRIPLE`], (optional)) – 

Graphs, Number of graphs

    * `SIMPLE` Unique – One unique graphical definition.

    * `DOUBLE` Double – Graphical definition in 2 sections.

    * `TRIPLE` Triplet – Graphical definition in 3 sections.

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of modifier to redefine

bpy.ops.sequencer.strip_modifier_move(_*_ , _name ='Name'_, _direction =UP_)¶

    

Move modifier up and down in the stack

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of modifier to remove

  * **direction** (enum in [`UP`, `DOWN`], (optional)) – 

Type

    * `UP` Up – Move modifier up in the stack.

    * `DOWN` Down – Move modifier down in the stack.

bpy.ops.sequencer.strip_modifier_remove(_*_ , _name ='Name'_)¶

    

Remove a modifier from the strip

Parameters:

    

**name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of
modifier to remove

bpy.ops.sequencer.strip_transform_clear(_*_ , _property =ALL_)¶

    

Reset image transformation to default value

Parameters:

    

**property** (enum in [`POSITION`, `SCALE`, `ROTATION`, `ALL`], (optional)) –

Property, Strip transform property to be reset

  * `POSITION` Position – Reset strip transform location.

  * `SCALE` Scale – Reset strip transform scale.

  * `ROTATION` Rotation – Reset strip transform rotation.

  * `ALL` All – Reset strip transform location, scale and rotation.

bpy.ops.sequencer.strip_transform_fit(_*_ , _fit_method =FIT_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

**fit_method** (enum in [`FIT`, `FILL`, `STRETCH`], (optional)) –

Fit Method, Scale fit fit_method

  * `FIT` Scale to Fit – Scale image so fits in preview.

  * `FILL` Scale to Fill – Scale image so it fills preview completely.

  * `STRETCH` Stretch to Fill – Stretch image so it fills preview.

bpy.ops.sequencer.swap(_*_ , _side =RIGHT_)¶

    

Swap active strip with strip to the right or left

Parameters:

    

**side** (enum in [`LEFT`, `RIGHT`], (optional)) – Side, Side of the strip to
swap

bpy.ops.sequencer.swap_data()¶

    

Swap 2 sequencer strips

bpy.ops.sequencer.swap_inputs()¶

    

Swap the two inputs of the effect strip

bpy.ops.sequencer.text_cursor_move(_*_ , _type =LINE_BEGIN_, _select_text
=False_)¶

    

Move cursor in text

Parameters:

    

  * **type** (enum in [`LINE_BEGIN`, `LINE_END`, `TEXT_BEGIN`, `TEXT_END`, `PREVIOUS_CHARACTER`, `NEXT_CHARACTER`, `PREVIOUS_WORD`, `NEXT_WORD`, `PREVIOUS_LINE`, `NEXT_LINE`], (optional)) – Type, Where to move cursor to, to make a selection

  * **select_text** (_boolean_ _,__(__optional_ _)_) – Select Text, Select text while moving cursor

bpy.ops.sequencer.text_cursor_set(_*_ , _select_text =False_)¶

    

Set cursor position in text

Parameters:

    

**select_text** (_boolean_ _,__(__optional_ _)_) – Select Text, Select text
while moving cursor

bpy.ops.sequencer.text_delete(_*_ , _type =NEXT_OR_SELECTION_)¶

    

Delete text at cursor position

Parameters:

    

**type** (enum in [`NEXT_OR_SELECTION`, `PREVIOUS_OR_SELECTION`], (optional))
– Type, Which part of the text to delete

bpy.ops.sequencer.text_deselect_all()¶

    

Deselect all characters

bpy.ops.sequencer.text_edit_copy()¶

    

Copy text to clipboard

bpy.ops.sequencer.text_edit_cut()¶

    

Cut text to clipboard

bpy.ops.sequencer.text_edit_mode_toggle()¶

    

Toggle text editing

bpy.ops.sequencer.text_edit_paste()¶

    

Paste text from clipboard

bpy.ops.sequencer.text_insert(_*_ , _string =''_)¶

    

Insert text at cursor position

Parameters:

    

**string** (_string_ _,__(__optional_ _,__never None_ _)_) – String, String to
be inserted at cursor position

bpy.ops.sequencer.text_line_break()¶

    

Insert line break at cursor position

bpy.ops.sequencer.text_select_all()¶

    

Select all characters

bpy.ops.sequencer.unlock()¶

    

Unlock strips so they can be transformed

bpy.ops.sequencer.unmute(_*_ , _unselected =False_)¶

    

Unmute (un)selected strips

Parameters:

    

**unselected** (_boolean_ _,__(__optional_ _)_) – Unselected, Unmute
unselected rather than selected strips

bpy.ops.sequencer.view_all()¶

    

View all the strips in the sequencer

bpy.ops.sequencer.view_all_preview()¶

    

Zoom preview to fit in the area

bpy.ops.sequencer.view_frame()¶

    

Move the view to the current frame

bpy.ops.sequencer.view_ghost_border(_*_ , _xmin =0_, _xmax =0_, _ymin =0_,
_ymax =0_, _wait_for_input =True_)¶

    

Set the boundaries of the border used for offset view

Parameters:

    

  * **xmin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Min

  * **xmax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Max

  * **ymin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Min

  * **ymax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Max

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

bpy.ops.sequencer.view_selected()¶

    

Zoom the sequencer on the selected strips

bpy.ops.sequencer.view_zoom_ratio(_*_ , _ratio =1.0_)¶

    

Change zoom ratio of sequencer preview

Parameters:

    

**ratio** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Ratio,
Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

