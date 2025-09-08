---
url: https://docs.blender.org/api/current/bpy.ops.image.html
scraped_at: 2025-09-08T14:18:18.624258
title: Image Operators¶
---

# Image Operators¶

bpy.ops.image.add_render_slot()¶

    

Add a new render slot

bpy.ops.image.change_frame(_*_ , _frame =0_)¶

    

Interactively change the current frame number

Parameters:

    

**frame** (_int in_ _[__-1048574_ _,__1048574_ _]__,__(__optional_ _)_) –
Frame

bpy.ops.image.clear_render_border()¶

    

Clear the boundaries of the render region and disable render region

bpy.ops.image.clear_render_slot()¶

    

Clear the currently selected render slot

bpy.ops.image.clipboard_copy()¶

    

Copy the image to the clipboard

bpy.ops.image.clipboard_paste()¶

    

Paste new image from the clipboard

bpy.ops.image.convert_to_mesh_plane(_*_ , _interpolation =Linear_, _extension
=CLIP_, _alpha_mode =STRAIGHT_, _use_auto_refresh =True_, _relative =True_,
_shader =PRINCIPLED_, _emit_strength =1.0_, _use_transparency =True_,
_render_method =DITHERED_, _use_backface_culling =False_,
_show_transparent_back =True_, _overwrite_material =True_, _name_from
=OBJECT_, _delete_ref =True_)¶

    

Convert selected reference images to textured mesh plane

Parameters:

    

  * **interpolation** (enum in [`Linear`, `Closest`, `Cubic`, `Smart`], (optional)) – 

Interpolation, Texture interpolation

    * `Linear` Linear – Linear interpolation.

    * `Closest` Closest – No interpolation (sample closest texel).

    * `Cubic` Cubic – Cubic interpolation.

    * `Smart` Smart – Bicubic when magnifying, else bilinear (OSL only).

  * **extension** (enum in [`CLIP`, `EXTEND`, `REPEAT`], (optional)) – 

Extension, How the image is extrapolated past its original bounds

    * `CLIP` Clip – Clip to image size and set exterior pixels as transparent.

    * `EXTEND` Extend – Extend by repeating edge pixels of the image.

    * `REPEAT` Repeat – Cause the image to repeat horizontally and vertically.

  * **alpha_mode** (enum in [`STRAIGHT`, `PREMUL`, `CHANNEL_PACKED`, `NONE`], (optional)) – 

Alpha Mode, Representation of alpha in the image file, to convert to and from
when saving and loading the image

    * `STRAIGHT` Straight – Store RGB and alpha channels separately with alpha acting as a mask, also known as unassociated alpha. Commonly used by image editing applications and file formats like PNG..

    * `PREMUL` Premultiplied – Store RGB channels with alpha multiplied in, also known as associated alpha. The natural format for renders and used by file formats like OpenEXR..

    * `CHANNEL_PACKED` Channel Packed – Different images are packed in the RGB and alpha channels, and they should not affect each other. Channel packing is commonly used by game engines to save memory..

    * `NONE` None – Ignore alpha channel from the file and make image fully opaque.

  * **use_auto_refresh** (_boolean_ _,__(__optional_ _)_) – Auto Refresh, Always refresh image on frame changes

  * **relative** (_boolean_ _,__(__optional_ _)_) – Relative Paths, Use relative file paths

  * **shader** (enum in [`PRINCIPLED`, `SHADELESS`, `EMISSION`], (optional)) – 

Shader, Node shader to use

    * `PRINCIPLED` Principled – Principled shader.

    * `SHADELESS` Shadeless – Only visible to camera and reflections.

    * `EMISSION` Emission – Emission shader.

  * **emit_strength** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Emission Strength, Strength of emission

  * **use_transparency** (_boolean_ _,__(__optional_ _)_) – Use Alpha, Use alpha channel for transparency

  * **render_method** (enum in [`DITHERED`, `BLENDED`], (optional)) – 

Render Method

    * `DITHERED` Dithered – Allows for grayscale hashed transparency, and compatible with render passes and ray-tracing. Also known as deferred rendering..

    * `BLENDED` Blended – Allows for colored transparency, but incompatible with render passes and ray-tracing. Also known as forward rendering..

  * **use_backface_culling** (_boolean_ _,__(__optional_ _)_) – Backface Culling, Use backface culling to hide the back side of faces

  * **show_transparent_back** (_boolean_ _,__(__optional_ _)_) – Show Backface, Render multiple transparent layers (may introduce transparency sorting problems)

  * **overwrite_material** (_boolean_ _,__(__optional_ _)_) – Overwrite Material, Overwrite existing material with the same name

  * **name_from** (enum in [`OBJECT`, `IMAGE`], (optional)) – 

Name After, Name for new mesh object and material

    * `OBJECT` Source Object – Name after object source with a suffix.

    * `IMAGE` Source Image – Name from loaded image.

  * **delete_ref** (_boolean_ _,__(__optional_ _)_) – Delete Reference Object, Delete empty image object once mesh plane is created

File:

    

[startup/bl_operators/image_as_planes.py:1146](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/image_as_planes.py#L1146)

bpy.ops.image.curves_point_set(_*_ , _point =BLACK_POINT_, _size =1_)¶

    

Set black point or white point for curves

Parameters:

    

  * **point** (enum in [`BLACK_POINT`, `WHITE_POINT`], (optional)) – Point, Set black point or white point for curves

  * **size** (_int in_ _[__1_ _,__128_ _]__,__(__optional_ _)_) – Sample Size

bpy.ops.image.cycle_render_slot(_*_ , _reverse =False_)¶

    

Cycle through all non-void render slots

Parameters:

    

**reverse** (_boolean_ _,__(__optional_ _)_) – Cycle in Reverse

bpy.ops.image.external_edit(_*_ , _filepath =''_)¶

    

Edit image in an external application

Parameters:

    

**filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – filepath

File:

    

[startup/bl_operators/image.py:54](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/image.py#L54)

bpy.ops.image.file_browse(_*_ , _filepath =''_, _hide_props_region =True_,
_check_existing =False_, _filter_blender =False_, _filter_backup =False_,
_filter_image =True_, _filter_movie =True_, _filter_python =False_,
_filter_font =False_, _filter_sound =False_, _filter_text =False_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =9_, _relative_path =True_, _show_multiview =False_, _use_multiview
=False_, _display_type =DEFAULT_, _sort_method_)¶

    

Open an image file browser, hold Shift to open the file, Alt to browse
containing directory

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

  * **relative_path** (_boolean_ _,__(__optional_ _)_) – Relative Path, Select the file relative to the blend file

  * **show_multiview** (_boolean_ _,__(__optional_ _)_) – Enable Multi-View

  * **use_multiview** (_boolean_ _,__(__optional_ _)_) – Use Multi-View

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

bpy.ops.image.flip(_*_ , _use_flip_x =False_, _use_flip_y =False_)¶

    

Flip the image

Parameters:

    

  * **use_flip_x** (_boolean_ _,__(__optional_ _)_) – Horizontal, Flip the image horizontally

  * **use_flip_y** (_boolean_ _,__(__optional_ _)_) – Vertical, Flip the image vertically

bpy.ops.image.import_as_mesh_planes(_*_ , _interpolation =Linear_, _extension
=CLIP_, _alpha_mode =STRAIGHT_, _use_auto_refresh =True_, _relative =True_,
_shader =PRINCIPLED_, _emit_strength =1.0_, _use_transparency =True_,
_render_method =DITHERED_, _use_backface_culling =False_,
_show_transparent_back =True_, _overwrite_material =True_, _filepath =''_,
_align =WORLD_, _location =(0.0, 0.0, 0.0)_, _rotation =(0.0, 0.0, 0.0)_,
_files =None_, _directory =''_, _filter_image =True_, _filter_movie =True_,
_filter_folder =True_, _force_reload =False_, _image_sequence =False_, _offset
=True_, _offset_axis =+X_, _offset_amount =0.1_, _align_axis =CAM_AX_,
_prev_align_axis =NONE_, _align_track =False_, _size_mode =ABSOLUTE_,
_fill_mode =FILL_, _height =1.0_, _factor =600.0_)¶

    

Create mesh plane(s) from image files with the appropriate aspect ratio

Parameters:

    

  * **interpolation** (enum in [`Linear`, `Closest`, `Cubic`, `Smart`], (optional)) – 

Interpolation, Texture interpolation

    * `Linear` Linear – Linear interpolation.

    * `Closest` Closest – No interpolation (sample closest texel).

    * `Cubic` Cubic – Cubic interpolation.

    * `Smart` Smart – Bicubic when magnifying, else bilinear (OSL only).

  * **extension** (enum in [`CLIP`, `EXTEND`, `REPEAT`], (optional)) – 

Extension, How the image is extrapolated past its original bounds

    * `CLIP` Clip – Clip to image size and set exterior pixels as transparent.

    * `EXTEND` Extend – Extend by repeating edge pixels of the image.

    * `REPEAT` Repeat – Cause the image to repeat horizontally and vertically.

  * **alpha_mode** (enum in [`STRAIGHT`, `PREMUL`, `CHANNEL_PACKED`, `NONE`], (optional)) – 

Alpha Mode, Representation of alpha in the image file, to convert to and from
when saving and loading the image

    * `STRAIGHT` Straight – Store RGB and alpha channels separately with alpha acting as a mask, also known as unassociated alpha. Commonly used by image editing applications and file formats like PNG..

    * `PREMUL` Premultiplied – Store RGB channels with alpha multiplied in, also known as associated alpha. The natural format for renders and used by file formats like OpenEXR..

    * `CHANNEL_PACKED` Channel Packed – Different images are packed in the RGB and alpha channels, and they should not affect each other. Channel packing is commonly used by game engines to save memory..

    * `NONE` None – Ignore alpha channel from the file and make image fully opaque.

  * **use_auto_refresh** (_boolean_ _,__(__optional_ _)_) – Auto Refresh, Always refresh image on frame changes

  * **relative** (_boolean_ _,__(__optional_ _)_) – Relative Paths, Use relative file paths

  * **shader** (enum in [`PRINCIPLED`, `SHADELESS`, `EMISSION`], (optional)) – 

Shader, Node shader to use

    * `PRINCIPLED` Principled – Principled shader.

    * `SHADELESS` Shadeless – Only visible to camera and reflections.

    * `EMISSION` Emission – Emission shader.

  * **emit_strength** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Emission Strength, Strength of emission

  * **use_transparency** (_boolean_ _,__(__optional_ _)_) – Use Alpha, Use alpha channel for transparency

  * **render_method** (enum in [`DITHERED`, `BLENDED`], (optional)) – 

Render Method

    * `DITHERED` Dithered – Allows for grayscale hashed transparency, and compatible with render passes and ray-tracing. Also known as deferred rendering..

    * `BLENDED` Blended – Allows for colored transparency, but incompatible with render passes and ray-tracing. Also known as forward rendering..

  * **use_backface_culling** (_boolean_ _,__(__optional_ _)_) – Backface Culling, Use backface culling to hide the back side of faces

  * **show_transparent_back** (_boolean_ _,__(__optional_ _)_) – Show Backface, Render multiple transparent layers (may introduce transparency sorting problems)

  * **overwrite_material** (_boolean_ _,__(__optional_ _)_) – Overwrite Material, Overwrite existing material with the same name

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Filepath used for importing the file

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation

  * **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – files

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – directory

  * **filter_image** (_boolean_ _,__(__optional_ _)_) – filter_image

  * **filter_movie** (_boolean_ _,__(__optional_ _)_) – filter_movie

  * **filter_folder** (_boolean_ _,__(__optional_ _)_) – filter_folder

  * **force_reload** (_boolean_ _,__(__optional_ _)_) – Force Reload, Force reload the image if it is already opened elsewhere in Blender

  * **image_sequence** (_boolean_ _,__(__optional_ _)_) – Detect Image Sequences, Import sequentially numbered images as an animated image sequence instead of separate planes

  * **offset** (_boolean_ _,__(__optional_ _)_) – Offset Planes, Offset planes from each other. If disabled, multiple planes will be created at the same location

  * **offset_axis** (enum in [`+X`, `+Y`, `+Z`, `-X`, `-Y`, `-Z`], (optional)) – 

Offset Direction, How planes are oriented relative to each others’ local axis

    * `+X` +X – Side by Side to the Left.

    * `+Y` +Y – Side by Side, Downward.

    * `+Z` +Z – Stacked Above.

    * `-X` -X – Side by Side to the Right.

    * `-Y` -Y – Side by Side, Upward.

    * `-Z` -Z – Stacked Below.

  * **offset_amount** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Offset Distance, Set distance between each plane

  * **align_axis** (enum in [`+X`, `+Y`, `+Z`, `-X`, `-Y`, `-Z`, `CAM`, `CAM_AX`], (optional)) – 

Align, How to align the planes

    * `+X` +X – Facing positive X.

    * `+Y` +Y – Facing positive Y.

    * `+Z` +Z – Facing positive Z.

    * `-X` -X – Facing negative X.

    * `-Y` -Y – Facing negative Y.

    * `-Z` -Z – Facing negative Z.

    * `CAM` Face Camera – Facing camera.

    * `CAM_AX` Camera’s Main Axis – Facing the camera’s dominant axis.

  * **prev_align_axis** (enum in [`+X`, `+Y`, `+Z`, `-X`, `-Y`, `-Z`, `CAM`, `CAM_AX`, `NONE`], (optional)) – 

prev_align_axis

    * `+X` +X – Facing positive X.

    * `+Y` +Y – Facing positive Y.

    * `+Z` +Z – Facing positive Z.

    * `-X` -X – Facing negative X.

    * `-Y` -Y – Facing negative Y.

    * `-Z` -Z – Facing negative Z.

    * `CAM` Face Camera – Facing camera.

    * `CAM_AX` Camera’s Main Axis – Facing the camera’s dominant axis.

    * `NONE` Undocumented.

  * **align_track** (_boolean_ _,__(__optional_ _)_) – Track Camera, Add a constraint to make the planes track the camera

  * **size_mode** (enum in [`ABSOLUTE`, `CAMERA`, `DPI`, `DPBU`], (optional)) – 

Size Mode, Method for computing the plane size

    * `ABSOLUTE` Absolute – Use absolute size.

    * `CAMERA` Scale to Camera Frame – Scale to fit or fill the camera frame.

    * `DPI` Pixels per Inch – Scale based on pixels per inch.

    * `DPBU` Pixels per Blender Unit – Scale based on pixels per Blender Unit.

  * **fill_mode** (enum in [`FILL`, `FIT`], (optional)) – 

Scale, Method to scale the plane with the camera frame

    * `FILL` Fill – Fill camera frame, spilling outside the frame.

    * `FIT` Fit – Fit entire image within the camera frame.

  * **height** (_float in_ _[__0.001_ _,__inf_ _]__,__(__optional_ _)_) – Height, Height of the created plane

  * **factor** (_float in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Definition, Number of pixels per inch or Blender Unit

File:

    

[startup/bl_operators/image_as_planes.py:868](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/image_as_planes.py#L868)

bpy.ops.image.invert(_*_ , _invert_r =False_, _invert_g =False_, _invert_b
=False_, _invert_a =False_)¶

    

Invert image’s channels

Parameters:

    

  * **invert_r** (_boolean_ _,__(__optional_ _)_) – Red, Invert red channel

  * **invert_g** (_boolean_ _,__(__optional_ _)_) – Green, Invert green channel

  * **invert_b** (_boolean_ _,__(__optional_ _)_) – Blue, Invert blue channel

  * **invert_a** (_boolean_ _,__(__optional_ _)_) – Alpha, Invert alpha channel

bpy.ops.image.match_movie_length()¶

    

Set image’s user’s length to the one of this video

bpy.ops.image.new(_*_ , _name ='Untitled'_, _width =1024_, _height =1024_,
_color =(0.0, 0.0, 0.0, 1.0)_, _alpha =True_, _generated_type =BLANK_, _float
=False_, _use_stereo_3d =False_, _tiled =False_)¶

    

Create a new image

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Image data-block name

  * **width** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Width, Image width

  * **height** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Height, Image height

  * **color** (_float array_ _of_ _4 items in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Color, Default fill color

  * **alpha** (_boolean_ _,__(__optional_ _)_) – Alpha, Create an image with an alpha channel

  * **generated_type** (enum in [Image Generated Type Items](bpy_types_enum_items/image_generated_type_items.html#rna-enum-image-generated-type-items), (optional)) – Generated Type, Fill the image with a grid for UV map testing

  * **float** (_boolean_ _,__(__optional_ _)_) – 32-bit Float, Create image with 32-bit floating-point bit depth

  * **use_stereo_3d** (_boolean_ _,__(__optional_ _)_) – Stereo 3D, Create an image with left and right views

  * **tiled** (_boolean_ _,__(__optional_ _)_) – Tiled, Create a tiled image

bpy.ops.image.open(_*_ , _allow_path_tokens =True_, _filepath =''_, _directory
=''_, _files =None_, _hide_props_region =True_, _check_existing =False_,
_filter_blender =False_, _filter_backup =False_, _filter_image =True_,
_filter_movie =True_, _filter_python =False_, _filter_font =False_,
_filter_sound =False_, _filter_text =False_, _filter_archive =False_,
_filter_btx =False_, _filter_collada =False_, _filter_alembic =False_,
_filter_usd =False_, _filter_obj =False_, _filter_volume =False_,
_filter_folder =True_, _filter_blenlib =False_, _filemode =9_, _relative_path
=True_, _show_multiview =False_, _use_multiview =False_, _display_type
=DEFAULT_, _sort_method_ , _use_sequence_detection =True_, _use_udim_detecting
=True_)¶

    

Open image

Parameters:

    

  * **allow_path_tokens** (_boolean_ _,__(__optional_ _)_) – Allow the path to contain substitution tokens

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

  * **show_multiview** (_boolean_ _,__(__optional_ _)_) – Enable Multi-View

  * **use_multiview** (_boolean_ _,__(__optional_ _)_) – Use Multi-View

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **use_sequence_detection** (_boolean_ _,__(__optional_ _)_) – Detect Sequences, Automatically detect animated sequences in selected images (based on file names)

  * **use_udim_detecting** (_boolean_ _,__(__optional_ _)_) – Detect UDIMs, Detect selected UDIM files and load all matching tiles

bpy.ops.image.open_images(_*_ , _directory =''_, _files =None_, _relative_path
=True_, _use_sequence_detection =True_, _use_udim_detection =True_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – directory

  * **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – files

  * **relative_path** (_boolean_ _,__(__optional_ _)_) – Use relative path

  * **use_sequence_detection** (_boolean_ _,__(__optional_ _)_) – Use sequence detection

  * **use_udim_detection** (_boolean_ _,__(__optional_ _)_) – Use UDIM detection

File:

    

[startup/bl_operators/image.py:238](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/image.py#L238)

bpy.ops.image.pack()¶

    

Pack an image as embedded data into the .blend file

bpy.ops.image.project_apply()¶

    

Project edited image back onto the object

File:

    

[startup/bl_operators/image.py:192](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/image.py#L192)

bpy.ops.image.project_edit()¶

    

Edit a snapshot of the 3D Viewport in an external image editor

File:

    

[startup/bl_operators/image.py:122](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/image.py#L122)

bpy.ops.image.read_viewlayers()¶

    

Read all the current scene’s view layers from cache, as needed

bpy.ops.image.reload()¶

    

Reload current image from disk

bpy.ops.image.remove_render_slot()¶

    

Remove the current render slot

bpy.ops.image.render_border(_*_ , _xmin =0_, _xmax =0_, _ymin =0_, _ymax =0_,
_wait_for_input =True_)¶

    

Set the boundaries of the render region and enable render region

Parameters:

    

  * **xmin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Min

  * **xmax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Max

  * **ymin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Min

  * **ymax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Max

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

bpy.ops.image.replace(_*_ , _filepath =''_, _hide_props_region =True_,
_check_existing =False_, _filter_blender =False_, _filter_backup =False_,
_filter_image =True_, _filter_movie =True_, _filter_python =False_,
_filter_font =False_, _filter_sound =False_, _filter_text =False_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =9_, _relative_path =True_, _show_multiview =False_, _use_multiview
=False_, _display_type =DEFAULT_, _sort_method_)¶

    

Replace current image by another one from disk

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

  * **relative_path** (_boolean_ _,__(__optional_ _)_) – Relative Path, Select the file relative to the blend file

  * **show_multiview** (_boolean_ _,__(__optional_ _)_) – Enable Multi-View

  * **use_multiview** (_boolean_ _,__(__optional_ _)_) – Use Multi-View

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

bpy.ops.image.resize(_*_ , _size =(0, 0)_, _all_udims =False_)¶

    

Resize the image

Parameters:

    

  * **size** (_int array_ _of_ _2 items in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Size

  * **all_udims** (_boolean_ _,__(__optional_ _)_) – All UDIM Tiles, Scale all the image’s UDIM tiles

bpy.ops.image.rotate_orthogonal(_*_ , _degrees =90_)¶

    

Rotate the image

Parameters:

    

**degrees** (enum in [`90`, `180`, `270`], (optional)) –

Degrees, Amount of rotation in degrees (90, 180, 270)

  * `90` 90 Degrees – Rotate 90 degrees clockwise.

  * `180` 180 Degrees – Rotate 180 degrees clockwise.

  * `270` 270 Degrees – Rotate 270 degrees clockwise.

bpy.ops.image.sample(_*_ , _size =1_)¶

    

Use mouse to sample a color in current image

Parameters:

    

**size** (_int in_ _[__1_ _,__128_ _]__,__(__optional_ _)_) – Sample Size

bpy.ops.image.sample_line(_*_ , _xstart =0_, _xend =0_, _ystart =0_, _yend
=0_, _flip =False_, _cursor =5_)¶

    

Sample a line and show it in Scope panels

Parameters:

    

  * **xstart** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Start

  * **xend** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X End

  * **ystart** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Start

  * **yend** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y End

  * **flip** (_boolean_ _,__(__optional_ _)_) – Flip

  * **cursor** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Cursor, Mouse cursor style to use during the modal operator

bpy.ops.image.save()¶

    

Save the image with current name and settings

bpy.ops.image.save_all_modified()¶

    

Save all modified images

bpy.ops.image.save_as(_*_ , _save_as_render =False_, _copy =False_,
_allow_path_tokens =True_, _filepath =''_, _check_existing =True_,
_filter_blender =False_, _filter_backup =False_, _filter_image =True_,
_filter_movie =True_, _filter_python =False_, _filter_font =False_,
_filter_sound =False_, _filter_text =False_, _filter_archive =False_,
_filter_btx =False_, _filter_collada =False_, _filter_alembic =False_,
_filter_usd =False_, _filter_obj =False_, _filter_volume =False_,
_filter_folder =True_, _filter_blenlib =False_, _filemode =9_, _relative_path
=True_, _show_multiview =False_, _use_multiview =False_, _display_type
=DEFAULT_, _sort_method_)¶

    

Save the image with another name and/or settings

Parameters:

    

  * **save_as_render** (_boolean_ _,__(__optional_ _)_) – Save As Render, Save image with render color management.For display image formats like PNG, apply view and display transform.For intermediate image formats like OpenEXR, use the default render output color space

  * **copy** (_boolean_ _,__(__optional_ _)_) – Copy, Create a new image file without modifying the current image in Blender

  * **allow_path_tokens** (_boolean_ _,__(__optional_ _)_) – Allow the path to contain substitution tokens

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

  * **relative_path** (_boolean_ _,__(__optional_ _)_) – Relative Path, Select the file relative to the blend file

  * **show_multiview** (_boolean_ _,__(__optional_ _)_) – Enable Multi-View

  * **use_multiview** (_boolean_ _,__(__optional_ _)_) – Use Multi-View

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

bpy.ops.image.save_sequence()¶

    

Save a sequence of images

bpy.ops.image.tile_add(_*_ , _number =1002_, _count =1_, _label =''_, _fill
=True_, _color =(0.0, 0.0, 0.0, 1.0)_, _generated_type =BLANK_, _width =1024_,
_height =1024_, _float =False_, _alpha =True_)¶

    

Adds a tile to the image

Parameters:

    

  * **number** (_int in_ _[__1001_ _,__2000_ _]__,__(__optional_ _)_) – Number, UDIM number of the tile

  * **count** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Count, How many tiles to add

  * **label** (_string_ _,__(__optional_ _,__never None_ _)_) – Label, Optional tile label

  * **fill** (_boolean_ _,__(__optional_ _)_) – Fill, Fill new tile with a generated image

  * **color** (_float array_ _of_ _4 items in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Color, Default fill color

  * **generated_type** (enum in [Image Generated Type Items](bpy_types_enum_items/image_generated_type_items.html#rna-enum-image-generated-type-items), (optional)) – Generated Type, Fill the image with a grid for UV map testing

  * **width** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Width, Image width

  * **height** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Height, Image height

  * **float** (_boolean_ _,__(__optional_ _)_) – 32-bit Float, Create image with 32-bit floating-point bit depth

  * **alpha** (_boolean_ _,__(__optional_ _)_) – Alpha, Create an image with an alpha channel

bpy.ops.image.tile_fill(_*_ , _color =(0.0, 0.0, 0.0, 1.0)_, _generated_type
=BLANK_, _width =1024_, _height =1024_, _float =False_, _alpha =True_)¶

    

Fill the current tile with a generated image

Parameters:

    

  * **color** (_float array_ _of_ _4 items in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Color, Default fill color

  * **generated_type** (enum in [Image Generated Type Items](bpy_types_enum_items/image_generated_type_items.html#rna-enum-image-generated-type-items), (optional)) – Generated Type, Fill the image with a grid for UV map testing

  * **width** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Width, Image width

  * **height** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Height, Image height

  * **float** (_boolean_ _,__(__optional_ _)_) – 32-bit Float, Create image with 32-bit floating-point bit depth

  * **alpha** (_boolean_ _,__(__optional_ _)_) – Alpha, Create an image with an alpha channel

bpy.ops.image.tile_remove()¶

    

Removes a tile from the image

bpy.ops.image.unpack(_*_ , _method =USE_LOCAL_, _id =''_)¶

    

Save an image packed in the .blend file to disk

Parameters:

    

  * **method** (enum in [Unpack Method Items](bpy_types_enum_items/unpack_method_items.html#rna-enum-unpack-method-items), (optional)) – Method, How to unpack

  * **id** (_string_ _,__(__optional_ _,__never None_ _)_) – Image Name, Image data-block name to unpack

bpy.ops.image.view_all(_*_ , _fit_view =False_)¶

    

View the entire image

Parameters:

    

**fit_view** (_boolean_ _,__(__optional_ _)_) – Fit View, Fit frame to the
viewport

bpy.ops.image.view_center_cursor()¶

    

Center the view so that the cursor is in the middle of the view

bpy.ops.image.view_cursor_center(_*_ , _fit_view =False_)¶

    

Set 2D Cursor To Center View location

Parameters:

    

**fit_view** (_boolean_ _,__(__optional_ _)_) – Fit View, Fit frame to the
viewport

bpy.ops.image.view_ndof()¶

    

Use a 3D mouse device to pan/zoom the view

bpy.ops.image.view_pan(_*_ , _offset =(0.0, 0.0)_)¶

    

Pan the view

Parameters:

    

**offset** ([`mathutils.Vector`](mathutils.html#mathutils.Vector
"mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Offset, Offset in
floating-point units, 1.0 is the width and height of the image

bpy.ops.image.view_selected()¶

    

View all selected UVs

bpy.ops.image.view_zoom(_*_ , _factor =0.0_, _use_cursor_init =True_)¶

    

Zoom in/out the image

Parameters:

    

  * **factor** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Factor, Zoom factor, values higher than 1.0 zoom in, lower values zoom out

  * **use_cursor_init** (_boolean_ _,__(__optional_ _)_) – Use Mouse Position, Allow the initial mouse position to be used

bpy.ops.image.view_zoom_border(_*_ , _xmin =0_, _xmax =0_, _ymin =0_, _ymax
=0_, _wait_for_input =True_, _zoom_out =False_)¶

    

Zoom in the view to the nearest item contained in the border

Parameters:

    

  * **xmin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Min

  * **xmax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Max

  * **ymin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Min

  * **ymax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Max

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

  * **zoom_out** (_boolean_ _,__(__optional_ _)_) – Zoom Out

bpy.ops.image.view_zoom_in(_*_ , _location =(0.0, 0.0)_)¶

    

Zoom in the image (centered around 2D cursor)

Parameters:

    

**location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector
"mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Cursor
location in screen coordinates

bpy.ops.image.view_zoom_out(_*_ , _location =(0.0, 0.0)_)¶

    

Zoom out the image (centered around 2D cursor)

Parameters:

    

**location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector
"mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Cursor
location in screen coordinates

bpy.ops.image.view_zoom_ratio(_*_ , _ratio =0.0_)¶

    

Set zoom ratio of the view

Parameters:

    

**ratio** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Ratio,
Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

