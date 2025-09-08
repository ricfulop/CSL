---
url: https://docs.blender.org/api/current/bpy.ops.asset.html
scraped_at: 2025-09-08T14:17:51.403418
title: Asset Operators¶
---

# Asset Operators¶

bpy.ops.asset.assign_action()¶

    

Set this pose Action as active Action on the active Object

File:

    

[addons_core/pose_library/operators.py:103](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/pose_library/operators.py#L103)

bpy.ops.asset.bundle_install(_*_ , _asset_library_reference_ , _filepath =''_,
_hide_props_region =True_, _check_existing =True_, _filter_blender =True_,
_filter_backup =False_, _filter_image =False_, _filter_movie =False_,
_filter_python =False_, _filter_font =False_, _filter_sound =False_,
_filter_text =False_, _filter_archive =False_, _filter_btx =False_,
_filter_collada =False_, _filter_alembic =False_, _filter_usd =False_,
_filter_obj =False_, _filter_volume =False_, _filter_folder =True_,
_filter_blenlib =False_, _filemode =8_, _display_type =DEFAULT_,
_sort_method_)¶

    

Copy the current .blend file into an Asset Library. Only works on standalone
.blend files (i.e. when no other files are referenced)

Parameters:

    

  * **asset_library_reference** (_enum in_ _[__]__,__(__optional_ _)_) – asset_library_reference

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

bpy.ops.asset.catalog_delete(_*_ , _catalog_id =''_)¶

    

Remove an asset catalog from the asset library (contained assets will not be
affected and show up as unassigned)

Parameters:

    

**catalog_id** (_string_ _,__(__optional_ _,__never None_ _)_) – Catalog ID,
ID of the catalog to delete

bpy.ops.asset.catalog_new(_*_ , _parent_path =''_)¶

    

Create a new catalog to put assets in

Parameters:

    

**parent_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Parent Path,
Optional path defining the location to put the new catalog under

bpy.ops.asset.catalog_redo()¶

    

Redo the last undone edit to the asset catalogs

bpy.ops.asset.catalog_undo()¶

    

Undo the last edit to the asset catalogs

bpy.ops.asset.catalog_undo_push()¶

    

Store the current state of the asset catalogs in the undo buffer

bpy.ops.asset.catalogs_save()¶

    

Make any edits to any catalogs permanent by writing the current set up to the
asset library

bpy.ops.asset.clear(_*_ , _set_fake_user =False_)¶

    

Delete all asset metadata and turn the selected asset data-blocks back into
normal data-blocks

Parameters:

    

**set_fake_user** (_boolean_ _,__(__optional_ _)_) – Set Fake User, Ensure the
data-block is saved, even when it is no longer marked as asset

bpy.ops.asset.clear_single(_*_ , _set_fake_user =False_)¶

    

Delete all asset metadata and turn the asset data-block back into a normal
data-block

Parameters:

    

**set_fake_user** (_boolean_ _,__(__optional_ _)_) – Set Fake User, Ensure the
data-block is saved, even when it is no longer marked as asset

bpy.ops.asset.library_refresh()¶

    

Reread assets and asset catalogs from the asset library on disk

bpy.ops.asset.mark()¶

    

Enable easier reuse of selected data-blocks through the Asset Browser, with
the help of customizable metadata (like previews, descriptions and tags)

bpy.ops.asset.mark_single()¶

    

Enable easier reuse of a data-block through the Asset Browser, with the help
of customizable metadata (like previews, descriptions and tags)

bpy.ops.asset.open_containing_blend_file()¶

    

Open the blend file that contains the active asset

File:

    

[startup/bl_operators/assets.py:103](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/assets.py#L103)

bpy.ops.asset.screenshot_preview(_*_ , _p1 =(0, 0)_, _p2 =(0, 0)_,
_force_square =True_)¶

    

Capture a screenshot to use as a preview for the selected asset

Parameters:

    

  * **p1** (_int array_ _of_ _2 items in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Point 1, First point of the screenshot in screenspace

  * **p2** (_int array_ _of_ _2 items in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Point 2, Second point of the screenshot in screenspace

  * **force_square** (_boolean_ _,__(__optional_ _)_) – Force Square, If enabled, the screenshot will have the same height as width

bpy.ops.asset.tag_add()¶

    

Add a new keyword tag to the active asset

File:

    

[startup/bl_operators/assets.py:42](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/assets.py#L42)

bpy.ops.asset.tag_remove()¶

    

Remove an existing keyword tag from the active asset

File:

    

[startup/bl_operators/assets.py:65](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/assets.py#L65)

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

