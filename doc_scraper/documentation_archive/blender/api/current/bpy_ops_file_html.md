---
url: https://docs.blender.org/api/current/bpy.ops.file.html
scraped_at: 2025-09-08T14:18:10.485363
title: File Operators¶
---

# File Operators¶

bpy.ops.file.autopack_toggle()¶

    

Automatically pack all external files into the .blend file

bpy.ops.file.bookmark_add()¶

    

Add a bookmark for the selected/active directory

bpy.ops.file.bookmark_cleanup()¶

    

Delete all invalid bookmarks

bpy.ops.file.bookmark_delete(_*_ , _index =-1_)¶

    

Delete selected bookmark

Parameters:

    

**index** (_int in_ _[__-1_ _,__20000_ _]__,__(__optional_ _)_) – Index

bpy.ops.file.bookmark_move(_*_ , _direction =TOP_)¶

    

Move the active bookmark up/down in the list

Parameters:

    

**direction** (enum in [`TOP`, `UP`, `DOWN`, `BOTTOM`], (optional)) –

Direction, Direction to move the active bookmark towards

  * `TOP` Top – Top of the list.

  * `UP` Up.

  * `DOWN` Down.

  * `BOTTOM` Bottom – Bottom of the list.

bpy.ops.file.cancel()¶

    

Cancel file operation

bpy.ops.file.delete()¶

    

Move selected files to the trash or recycle bin

bpy.ops.file.directory_new(_*_ , _directory =''_, _open =False_, _confirm
=True_)¶

    

Create a new directory

Parameters:

    

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Directory, Name of new directory

  * **open** (_boolean_ _,__(__optional_ _)_) – Open, Open new directory

  * **confirm** (_boolean_ _,__(__optional_ _)_) – Confirm, Prompt for confirmation

bpy.ops.file.edit_directory_path()¶

    

Start editing directory field

bpy.ops.file.execute()¶

    

Execute selected file

bpy.ops.file.external_operation(_*_ , _filepath =''_, _operation =OPEN_)¶

    

Perform external operation on a file or folder

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File or folder path

  * **operation** (enum in [`OPEN`, `FOLDER_OPEN`, `EDIT`, `NEW`, `FIND`, `SHOW`, `PLAY`, `BROWSE`, `PREVIEW`, `PRINT`, `INSTALL`, `RUNAS`, `PROPERTIES`, `FOLDER_FIND`, `CMD`], (optional)) – 

Operation, Operation to perform on the file or path

    * `OPEN` Open – Open the file.

    * `FOLDER_OPEN` Open Folder – Open the folder.

    * `EDIT` Edit – Edit the file.

    * `NEW` New – Create a new file of this type.

    * `FIND` Find File – Search for files of this type.

    * `SHOW` Show – Show this file.

    * `PLAY` Play – Play this file.

    * `BROWSE` Browse – Browse this file.

    * `PREVIEW` Preview – Preview this file.

    * `PRINT` Print – Print this file.

    * `INSTALL` Install – Install this file.

    * `RUNAS` Run As User – Run as specific user.

    * `PROPERTIES` Properties – Show OS Properties for this item.

    * `FOLDER_FIND` Find in Folder – Search for items in this folder.

    * `CMD` Command Prompt Here – Open a command prompt here.

bpy.ops.file.filenum(_*_ , _increment =1_)¶

    

Increment number in filename

Parameters:

    

**increment** (_int in_ _[__-100_ _,__100_ _]__,__(__optional_ _)_) –
Increment

bpy.ops.file.filepath_drop(_*_ , _filepath ='Path'_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

bpy.ops.file.find_missing_files(_*_ , _find_all =False_, _directory =''_,
_hide_props_region =True_, _check_existing =False_, _filter_blender =False_,
_filter_backup =False_, _filter_image =False_, _filter_movie =False_,
_filter_python =False_, _filter_font =False_, _filter_sound =False_,
_filter_text =False_, _filter_archive =False_, _filter_btx =False_,
_filter_collada =False_, _filter_alembic =False_, _filter_usd =False_,
_filter_obj =False_, _filter_volume =False_, _filter_folder =False_,
_filter_blenlib =False_, _filemode =9_, _display_type =DEFAULT_,
_sort_method_)¶

    

Try to find missing external files

Parameters:

    

  * **find_all** (_boolean_ _,__(__optional_ _)_) – Find All, Find all files in the search path (not just missing)

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Directory, Directory of the file

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

bpy.ops.file.hidedot()¶

    

Toggle hide hidden dot files

bpy.ops.file.highlight()¶

    

Highlight selected file(s)

bpy.ops.file.make_paths_absolute()¶

    

Make all paths to external files absolute

bpy.ops.file.make_paths_relative()¶

    

Make all paths to external files relative to current .blend

bpy.ops.file.mouse_execute()¶

    

Perform the current execute action for the file under the cursor (e.g. open
the file)

bpy.ops.file.next()¶

    

Move to next folder

bpy.ops.file.pack_all()¶

    

Pack all used external files into this .blend

bpy.ops.file.pack_libraries()¶

    

Store all data-blocks linked from other .blend files in the current .blend
file. Library references are preserved so the linked data-blocks can be
unpacked again

bpy.ops.file.parent()¶

    

Move to parent directory

bpy.ops.file.previous()¶

    

Move to previous folder

bpy.ops.file.refresh()¶

    

Refresh the file list

bpy.ops.file.rename()¶

    

Rename file or file directory

bpy.ops.file.report_missing_files()¶

    

Report all missing external files

bpy.ops.file.reset_recent()¶

    

Reset recent files

bpy.ops.file.select(_*_ , _wait_to_deselect_others =False_, _mouse_x =0_,
_mouse_y =0_, _extend =False_, _fill =False_, _open =True_, _deselect_all
=False_, _only_activate_if_selected =False_, _pass_through =False_)¶

    

Handle mouse clicks to select and activate items

Parameters:

    

  * **wait_to_deselect_others** (_boolean_ _,__(__optional_ _)_) – Wait to Deselect Others

  * **mouse_x** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Mouse X

  * **mouse_y** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Mouse Y

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection instead of deselecting everything first

  * **fill** (_boolean_ _,__(__optional_ _)_) – Fill, Select everything beginning with the last selection

  * **open** (_boolean_ _,__(__optional_ _)_) – Open, Open a directory when selecting it

  * **deselect_all** (_boolean_ _,__(__optional_ _)_) – Deselect On Nothing, Deselect all when nothing under the cursor

  * **only_activate_if_selected** (_boolean_ _,__(__optional_ _)_) – Only Activate if Selected, Do not change selection if the item under the cursor is already selected, only activate it

  * **pass_through** (_boolean_ _,__(__optional_ _)_) – Pass Through, Even on successful execution, pass the event on so other operators can execute on it as well

bpy.ops.file.select_all(_*_ , _action =TOGGLE_)¶

    

Select or deselect all files

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.file.select_bookmark(_*_ , _dir =''_)¶

    

Select a bookmarked directory

Parameters:

    

**dir** (_string_ _,__(__optional_ _,__never None_ _)_) – Directory

bpy.ops.file.select_box(_*_ , _xmin =0_, _xmax =0_, _ymin =0_, _ymax =0_,
_wait_for_input =True_, _mode =SET_)¶

    

Activate/select the file(s) contained in the border

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

bpy.ops.file.select_walk(_*_ , _direction =UP_, _extend =False_, _fill
=False_)¶

    

Select/Deselect files by walking through them

Parameters:

    

  * **direction** (enum in [`UP`, `DOWN`, `LEFT`, `RIGHT`], (optional)) – Walk Direction, Select/Deselect element in this direction

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection instead of deselecting everything first

  * **fill** (_boolean_ _,__(__optional_ _)_) – Fill, Select everything beginning with the last selection

bpy.ops.file.smoothscroll()¶

    

Smooth scroll to make editable file visible

bpy.ops.file.sort_column_ui_context()¶

    

Change sorting to use column under cursor

bpy.ops.file.start_filter()¶

    

Start entering filter text

bpy.ops.file.unpack_all(_*_ , _method =USE_LOCAL_)¶

    

Unpack all files packed into this .blend to external ones

Parameters:

    

**method** (enum in [`USE_LOCAL`, `WRITE_LOCAL`, `USE_ORIGINAL`,
`WRITE_ORIGINAL`, `KEEP`, `REMOVE`], (optional)) – Method, How to unpack

bpy.ops.file.unpack_item(_*_ , _method =USE_LOCAL_, _id_name =''_, _id_type
=19785_)¶

    

Unpack this file to an external file

Parameters:

    

  * **method** (enum in [`USE_LOCAL`, `WRITE_LOCAL`, `USE_ORIGINAL`, `WRITE_ORIGINAL`], (optional)) – Method, How to unpack

  * **id_name** (_string_ _,__(__optional_ _,__never None_ _)_) – ID Name, Name of ID block to unpack

  * **id_type** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – ID Type, Identifier type of ID block

bpy.ops.file.unpack_libraries()¶

    

Restore all packed linked data-blocks to their original locations

bpy.ops.file.view_selected()¶

    

Scroll the selected files into view

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

