---
url: https://docs.blender.org/api/current/bpy.ops.text.html
scraped_at: 2025-09-08T14:18:53.640517
title: Text Operators¶
---

# Text Operators¶

bpy.ops.text.autocomplete()¶

    

Show a list of used text in the open document

bpy.ops.text.comment_toggle(_*_ , _type =TOGGLE_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

**type** (enum in [`TOGGLE`, `COMMENT`, `UNCOMMENT`], (optional)) – Type, Add
or remove comments

bpy.ops.text.convert_whitespace(_*_ , _type =SPACES_)¶

    

Convert whitespaces by type

Parameters:

    

**type** (enum in [`SPACES`, `TABS`], (optional)) – Type, Type of whitespace
to convert to

bpy.ops.text.copy()¶

    

Copy selected text to clipboard

bpy.ops.text.cursor_set(_*_ , _x =0_, _y =0_)¶

    

Set cursor position

Parameters:

    

  * **x** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X

  * **y** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y

bpy.ops.text.cut()¶

    

Cut selected text to clipboard

bpy.ops.text.delete(_*_ , _type =NEXT_CHARACTER_)¶

    

Delete text by cursor position

Parameters:

    

**type** (enum in [`NEXT_CHARACTER`, `PREVIOUS_CHARACTER`, `NEXT_WORD`,
`PREVIOUS_WORD`], (optional)) – Type, Which part of the text to delete

bpy.ops.text.duplicate_line()¶

    

Duplicate the current line

bpy.ops.text.find()¶

    

Find specified text

bpy.ops.text.find_set_selected()¶

    

Find specified text and set as selected

bpy.ops.text.indent()¶

    

Indent selected text

bpy.ops.text.indent_or_autocomplete()¶

    

Indent selected text or autocomplete

bpy.ops.text.insert(_*_ , _text =''_)¶

    

Insert text at cursor position

Parameters:

    

**text** (_string_ _,__(__optional_ _,__never None_ _)_) – Text, Text to
insert at the cursor position

bpy.ops.text.jump(_*_ , _line =1_)¶

    

Jump cursor to line

Parameters:

    

**line** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Line, Line
number to jump to

bpy.ops.text.jump_to_file_at_point(_*_ , _filepath =''_, _line =0_, _column
=0_)¶

    

Jump to a file for the text editor

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – Filepath

  * **line** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Line, Line to jump to

  * **column** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Column, Column to jump to

bpy.ops.text.line_break()¶

    

Insert line break at cursor position

bpy.ops.text.line_number()¶

    

The current line number

bpy.ops.text.make_internal()¶

    

Make active text file internal

bpy.ops.text.move(_*_ , _type =LINE_BEGIN_)¶

    

Move cursor to position type

Parameters:

    

**type** (enum in [`LINE_BEGIN`, `LINE_END`, `FILE_TOP`, `FILE_BOTTOM`,
`PREVIOUS_CHARACTER`, `NEXT_CHARACTER`, `PREVIOUS_WORD`, `NEXT_WORD`,
`PREVIOUS_LINE`, `NEXT_LINE`, `PREVIOUS_PAGE`, `NEXT_PAGE`], (optional)) –
Type, Where to move cursor to

bpy.ops.text.move_lines(_*_ , _direction =DOWN_)¶

    

Move the currently selected line(s) up/down

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Direction

bpy.ops.text.move_select(_*_ , _type =LINE_BEGIN_)¶

    

Move the cursor while selecting

Parameters:

    

**type** (enum in [`LINE_BEGIN`, `LINE_END`, `FILE_TOP`, `FILE_BOTTOM`,
`PREVIOUS_CHARACTER`, `NEXT_CHARACTER`, `PREVIOUS_WORD`, `NEXT_WORD`,
`PREVIOUS_LINE`, `NEXT_LINE`, `PREVIOUS_PAGE`, `NEXT_PAGE`], (optional)) –
Type, Where to move cursor to, to make a selection

bpy.ops.text.new()¶

    

Create a new text data-block

bpy.ops.text.open(_*_ , _filepath =''_, _hide_props_region =True_,
_check_existing =False_, _filter_blender =False_, _filter_backup =False_,
_filter_image =False_, _filter_movie =False_, _filter_python =True_,
_filter_font =False_, _filter_sound =False_, _filter_text =True_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =9_, _display_type =DEFAULT_, _sort_method_ , _internal =False_)¶

    

Open a new text data-block

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

  * **sort_method** (enum in [`DEFAULT`, `FILE_SORT_ALPHA`, `FILE_SORT_EXTENSION`, `FILE_SORT_TIME`, `FILE_SORT_SIZE`, `ASSET_CATALOG`], (optional)) – 

File sorting mode

    * `DEFAULT` Default – Automatically determine sort method for files.

    * `FILE_SORT_ALPHA` Name – Sort the file list alphabetically.

    * `FILE_SORT_EXTENSION` Extension – Sort the file list by extension/type.

    * `FILE_SORT_TIME` Modified Date – Sort files by modification time.

    * `FILE_SORT_SIZE` Size – Sort files by size.

    * `ASSET_CATALOG` Asset Catalog – Sort the asset list so that assets in the same catalog are kept together. Within a single catalog, assets are ordered by name. The catalogs are in order of the flattened catalog hierarchy..

  * **internal** (_boolean_ _,__(__optional_ _)_) – Make Internal, Make text file internal after loading

bpy.ops.text.overwrite_toggle()¶

    

Toggle overwrite while typing

bpy.ops.text.paste(_*_ , _selection =False_)¶

    

Paste text from clipboard

Parameters:

    

**selection** (_boolean_ _,__(__optional_ _)_) – Selection, Paste text
selected elsewhere rather than copied (X11/Wayland only)

bpy.ops.text.reload()¶

    

Reload active text data-block from its file

bpy.ops.text.replace(_*_ , _all =False_)¶

    

Replace text with the specified text

Parameters:

    

**all** (_boolean_ _,__(__optional_ _)_) – Replace All, Replace all
occurrences

bpy.ops.text.replace_set_selected()¶

    

Replace text with specified text and set as selected

bpy.ops.text.resolve_conflict(_*_ , _resolution =IGNORE_)¶

    

When external text is out of sync, resolve the conflict

Parameters:

    

**resolution** (enum in [`IGNORE`, `RELOAD`, `SAVE`, `MAKE_INTERNAL`],
(optional)) – Resolution, How to solve conflict due to differences in internal
and external text

bpy.ops.text.run_script()¶

    

Run active script

bpy.ops.text.save()¶

    

Save active text data-block

bpy.ops.text.save_as(_*_ , _filepath =''_, _hide_props_region =True_,
_check_existing =True_, _filter_blender =False_, _filter_backup =False_,
_filter_image =False_, _filter_movie =False_, _filter_python =True_,
_filter_font =False_, _filter_sound =False_, _filter_text =True_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =9_, _display_type =DEFAULT_, _sort_method_)¶

    

Save active text file with options

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

bpy.ops.text.scroll(_*_ , _lines =1_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

**lines** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Lines,
Number of lines to scroll

bpy.ops.text.scroll_bar(_*_ , _lines =1_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

**lines** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Lines,
Number of lines to scroll

bpy.ops.text.select_all()¶

    

Select all text

bpy.ops.text.select_line()¶

    

Select text by line

bpy.ops.text.select_word()¶

    

Select word under cursor

bpy.ops.text.selection_set()¶

    

Set text selection

bpy.ops.text.start_find()¶

    

Start searching text

bpy.ops.text.to_3d_object(_*_ , _split_lines =False_)¶

    

Create 3D text object from active text data-block

Parameters:

    

**split_lines** (_boolean_ _,__(__optional_ _)_) – Split Lines, Create one
object per line in the text

bpy.ops.text.unindent()¶

    

Unindent selected text

bpy.ops.text.unlink()¶

    

Unlink active text data-block

bpy.ops.text.update_shader()¶

    

Update users of this shader, such as custom cameras and script nodes, with its
new sockets and options

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

