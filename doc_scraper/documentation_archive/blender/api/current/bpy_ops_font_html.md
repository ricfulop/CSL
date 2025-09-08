---
url: https://docs.blender.org/api/current/bpy.ops.font.html
scraped_at: 2025-09-08T14:18:12.533474
title: Font Operators¶
---

# Font Operators¶

bpy.ops.font.case_set(_*_ , _case =LOWER_)¶

    

Set font case

Parameters:

    

**case** (enum in [`LOWER`, `UPPER`], (optional)) – Case, Lower or upper case

bpy.ops.font.case_toggle()¶

    

Toggle font case

bpy.ops.font.change_character(_*_ , _delta =1_)¶

    

Change font character code

Parameters:

    

**delta** (_int in_ _[__-255_ _,__255_ _]__,__(__optional_ _)_) – Delta,
Number to increase or decrease character code with

bpy.ops.font.change_spacing(_*_ , _delta =1.0_)¶

    

Change font spacing

Parameters:

    

**delta** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Delta,
Amount to decrease or increase character spacing with

bpy.ops.font.delete(_*_ , _type =PREVIOUS_CHARACTER_)¶

    

Delete text by cursor position

Parameters:

    

**type** (enum in [`NEXT_CHARACTER`, `PREVIOUS_CHARACTER`, `NEXT_WORD`,
`PREVIOUS_WORD`, `SELECTION`, `NEXT_OR_SELECTION`, `PREVIOUS_OR_SELECTION`],
(optional)) – Type, Which part of the text to delete

bpy.ops.font.line_break()¶

    

Insert line break at cursor position

bpy.ops.font.move(_*_ , _type =LINE_BEGIN_)¶

    

Move cursor to position type

Parameters:

    

**type** (enum in [`LINE_BEGIN`, `LINE_END`, `TEXT_BEGIN`, `TEXT_END`,
`PREVIOUS_CHARACTER`, `NEXT_CHARACTER`, `PREVIOUS_WORD`, `NEXT_WORD`,
`PREVIOUS_LINE`, `NEXT_LINE`, `PREVIOUS_PAGE`, `NEXT_PAGE`], (optional)) –
Type, Where to move cursor to

bpy.ops.font.move_select(_*_ , _type =LINE_BEGIN_)¶

    

Move the cursor while selecting

Parameters:

    

**type** (enum in [`LINE_BEGIN`, `LINE_END`, `TEXT_BEGIN`, `TEXT_END`,
`PREVIOUS_CHARACTER`, `NEXT_CHARACTER`, `PREVIOUS_WORD`, `NEXT_WORD`,
`PREVIOUS_LINE`, `NEXT_LINE`, `PREVIOUS_PAGE`, `NEXT_PAGE`], (optional)) –
Type, Where to move cursor to, to make a selection

bpy.ops.font.open(_*_ , _filepath =''_, _hide_props_region =True_,
_check_existing =False_, _filter_blender =False_, _filter_backup =False_,
_filter_image =False_, _filter_movie =False_, _filter_python =False_,
_filter_font =True_, _filter_sound =False_, _filter_text =False_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =9_, _relative_path =True_, _display_type =THUMBNAIL_,
_sort_method_)¶

    

Load a new font from a file

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

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

bpy.ops.font.select_all()¶

    

Select all text

bpy.ops.font.select_word()¶

    

Select word under cursor

bpy.ops.font.selection_set()¶

    

Set cursor selection

bpy.ops.font.style_set(_*_ , _style =BOLD_, _clear =False_)¶

    

Set font style

Parameters:

    

  * **style** (enum in [`BOLD`, `ITALIC`, `UNDERLINE`, `SMALL_CAPS`], (optional)) – Style, Style to set selection to

  * **clear** (_boolean_ _,__(__optional_ _)_) – Clear, Clear style rather than setting it

bpy.ops.font.style_toggle(_*_ , _style =BOLD_)¶

    

Toggle font style

Parameters:

    

**style** (enum in [`BOLD`, `ITALIC`, `UNDERLINE`, `SMALL_CAPS`], (optional))
– Style, Style to set selection to

bpy.ops.font.text_copy()¶

    

Copy selected text to clipboard

bpy.ops.font.text_cut()¶

    

Cut selected text to clipboard

bpy.ops.font.text_insert(_*_ , _text =''_, _accent =False_)¶

    

Insert text at cursor position

Parameters:

    

  * **text** (_string_ _,__(__optional_ _,__never None_ _)_) – Text, Text to insert at the cursor position

  * **accent** (_boolean_ _,__(__optional_ _)_) – Accent Mode, Next typed character will strike through previous, for special character input

bpy.ops.font.text_insert_unicode()¶

    

Insert Unicode Character

bpy.ops.font.text_paste(_*_ , _selection =False_)¶

    

Paste text from clipboard

Parameters:

    

**selection** (_boolean_ _,__(__optional_ _)_) – Selection, Paste text
selected elsewhere rather than copied (X11/Wayland only)

bpy.ops.font.text_paste_from_file(_*_ , _filepath =''_, _hide_props_region
=True_, _check_existing =False_, _filter_blender =False_, _filter_backup
=False_, _filter_image =False_, _filter_movie =False_, _filter_python =False_,
_filter_font =False_, _filter_sound =False_, _filter_text =True_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =9_, _display_type =DEFAULT_, _sort_method_)¶

    

Paste contents from file

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

bpy.ops.font.textbox_add()¶

    

Add a new text box

bpy.ops.font.textbox_remove(_*_ , _index =0_)¶

    

Remove the text box

Parameters:

    

**index** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Index, The
current text box

bpy.ops.font.unlink()¶

    

Unlink active font data-block

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

