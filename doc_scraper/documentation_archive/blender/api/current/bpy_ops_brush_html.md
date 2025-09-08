---
url: https://docs.blender.org/api/current/bpy.ops.brush.html
scraped_at: 2025-09-08T14:17:53.440375
title: Brush Operators¶
---

# Brush Operators¶

bpy.ops.brush.asset_activate(_*_ , _asset_library_type =LOCAL_,
_asset_library_identifier =''_, _relative_asset_identifier =''_, _use_toggle
=False_)¶

    

Activate a brush asset as current sculpt and paint tool

Parameters:

    

  * **asset_library_type** (enum in [Asset Library Type Items](bpy_types_enum_items/asset_library_type_items.html#rna-enum-asset-library-type-items), (optional)) – Asset Library Type

  * **asset_library_identifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Asset Library Identifier

  * **relative_asset_identifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Relative Asset Identifier

  * **use_toggle** (_boolean_ _,__(__optional_ _)_) – Toggle, Switch between the current and assigned brushes on consecutive uses.

bpy.ops.brush.asset_delete()¶

    

Delete the active brush asset

bpy.ops.brush.asset_edit_metadata(_*_ , _catalog_path =''_, _author =''_,
_description =''_)¶

    

Edit asset information like the catalog, preview image, tags, or author

Parameters:

    

  * **catalog_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Catalog, The asset’s catalog path

  * **author** (_string_ _,__(__optional_ _,__never None_ _)_) – Author

  * **description** (_string_ _,__(__optional_ _,__never None_ _)_) – Description

bpy.ops.brush.asset_load_preview(_*_ , _filepath =''_, _hide_props_region
=True_, _check_existing =False_, _filter_blender =False_, _filter_backup
=False_, _filter_image =True_, _filter_movie =False_, _filter_python =False_,
_filter_font =False_, _filter_sound =False_, _filter_text =False_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =9_, _show_multiview =False_, _use_multiview =False_, _display_type
=DEFAULT_, _sort_method_)¶

    

Choose a preview image for the brush

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

bpy.ops.brush.asset_revert()¶

    

Revert the active brush settings to the default values from the asset library

bpy.ops.brush.asset_save()¶

    

Update the active brush asset in the asset library with current settings

bpy.ops.brush.asset_save_as(_*_ , _name =''_, _asset_library_reference_ ,
_catalog_path =''_)¶

    

Save a copy of the active brush asset into the default asset library, and make
it the active brush

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name for the new brush asset

  * **asset_library_reference** (_enum in_ _[__]__,__(__optional_ _)_) – Library, Asset library used to store the new brush

  * **catalog_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Catalog, Catalog to use for the new asset

bpy.ops.brush.curve_preset(_*_ , _shape =SMOOTH_)¶

    

Set brush shape

Parameters:

    

**shape** (enum in [`SHARP`, `SMOOTH`, `MAX`, `LINE`, `ROUND`, `ROOT`],
(optional)) – Mode

bpy.ops.brush.scale_size(_*_ , _scalar =1.0_)¶

    

Change brush size by a scalar

Parameters:

    

**scalar** (_float in_ _[__0_ _,__2_ _]__,__(__optional_ _)_) – Scalar, Factor
to scale brush size by

bpy.ops.brush.sculpt_curves_falloff_preset(_*_ , _shape =SMOOTH_)¶

    

Set Curve Falloff Preset

Parameters:

    

**shape** (enum in [`SHARP`, `SMOOTH`, `MAX`, `LINE`, `ROUND`, `ROOT`],
(optional)) – Mode

bpy.ops.brush.stencil_control(_*_ , _mode =TRANSLATION_, _texmode =PRIMARY_)¶

    

Control the stencil brush

Parameters:

    

  * **mode** (enum in [`TRANSLATION`, `SCALE`, `ROTATION`], (optional)) – Tool

  * **texmode** (enum in [`PRIMARY`, `SECONDARY`], (optional)) – Tool

bpy.ops.brush.stencil_fit_image_aspect(_*_ , _use_repeat =True_, _use_scale
=True_, _mask =False_)¶

    

When using an image texture, adjust the stencil size to fit the image aspect
ratio

Parameters:

    

  * **use_repeat** (_boolean_ _,__(__optional_ _)_) – Use Repeat, Use repeat mapping values

  * **use_scale** (_boolean_ _,__(__optional_ _)_) – Use Scale, Use texture scale values

  * **mask** (_boolean_ _,__(__optional_ _)_) – Modify Mask Stencil, Modify either the primary or mask stencil

bpy.ops.brush.stencil_reset_transform(_*_ , _mask =False_)¶

    

Reset the stencil transformation to the default

Parameters:

    

**mask** (_boolean_ _,__(__optional_ _)_) – Modify Mask Stencil, Modify either
the primary or mask stencil

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

