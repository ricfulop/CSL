---
url: https://docs.blender.org/api/current/bpy.ops.ed.html
scraped_at: 2025-09-08T14:18:06.448279
title: Ed Operators¶
---

# Ed Operators¶

bpy.ops.ed.flush_edits()¶

    

Flush edit data from active editing modes

bpy.ops.ed.lib_id_fake_user_toggle()¶

    

Save this data-block even if it has no users

bpy.ops.ed.lib_id_generate_preview()¶

    

Create an automatic preview for the selected data-block

bpy.ops.ed.lib_id_generate_preview_from_object()¶

    

Create a preview for this asset by rendering the active object

bpy.ops.ed.lib_id_load_custom_preview(_*_ , _filepath =''_, _hide_props_region
=True_, _check_existing =False_, _filter_blender =False_, _filter_backup
=False_, _filter_image =True_, _filter_movie =False_, _filter_python =False_,
_filter_font =False_, _filter_sound =False_, _filter_text =False_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =9_, _show_multiview =False_, _use_multiview =False_, _display_type
=DEFAULT_, _sort_method_)¶

    

Choose an image to help identify the data-block visually

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

bpy.ops.ed.lib_id_override_editable_toggle()¶

    

Set if this library override data-block can be edited

bpy.ops.ed.lib_id_remove_preview()¶

    

Remove the preview of this data-block

bpy.ops.ed.lib_id_unlink()¶

    

Remove a usage of a data-block, clearing the assignment

bpy.ops.ed.redo()¶

    

Redo previous action

bpy.ops.ed.undo()¶

    

Undo previous action

bpy.ops.ed.undo_history(_*_ , _item =0_)¶

    

Redo specific action in history

Parameters:

    

**item** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Item

bpy.ops.ed.undo_push(_*_ , _message ='Add an undo step *function may be
moved*'_)¶

    

Add an undo state (internal use only)

Parameters:

    

**message** (_string_ _,__(__optional_ _,__never None_ _)_) – Undo Message

bpy.ops.ed.undo_redo()¶

    

Undo and redo previous action

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

