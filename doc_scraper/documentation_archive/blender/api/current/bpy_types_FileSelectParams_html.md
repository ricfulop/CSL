---
url: https://docs.blender.org/api/current/bpy.types.FileSelectParams.html
scraped_at: 2025-09-08T14:25:20.193915
title: FileSelectParams(bpy_struct)¶
---

# FileSelectParams(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

subclasses —
[`FileAssetSelectParams`](bpy.types.FileAssetSelectParams.html#bpy.types.FileAssetSelectParams
"bpy.types.FileAssetSelectParams")

_class _bpy.types.FileSelectParams(_bpy_struct_)¶

    

File Select Parameters

directory¶

    

Directory displayed in the file browser

Type:

    

byte string, default “”, (never None)

display_size¶

    

Change the size of thumbnails

Type:

    

int in [16, 256], default 96

display_size_discrete¶

    

Change the size of thumbnails in discrete steps

Type:

    

enum in [`TINY`, `SMALL`, `NORMAL`, `BIG`, `LARGE`], default `TINY`

display_type¶

    

Display mode for the file list

  * `LIST_VERTICAL` Vertical List – Display files as a vertical list.

  * `LIST_HORIZONTAL` Horizontal List – Display files as a horizontal list.

  * `THUMBNAIL` Thumbnails – Display files as thumbnails.

Type:

    

enum in [`LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], default
`LIST_VERTICAL`

filename¶

    

Active file in the file browser

Type:

    

string, default “”, (never None)

filter_glob¶

    

UNIX shell-like filename patterns matching, supports wildcards (‘*’) and list
of patterns separated by ‘;’

Type:

    

string, default “”, (never None)

filter_id¶

    

Which ID types to show/hide, when browsing a library

Type:

    

[`FileSelectIDFilter`](bpy.types.FileSelectIDFilter.html#bpy.types.FileSelectIDFilter
"bpy.types.FileSelectIDFilter"), (readonly, never None)

filter_search¶

    

Filter by name or tag, supports ‘*’ wildcard

Type:

    

string, default “”, (never None)

list_column_size¶

    

The width of columns in horizontal list views

Type:

    

int in [32, 750], default 32

list_display_size¶

    

Change the size of thumbnails in list views

Type:

    

int in [16, 128], default 32

recursion_level¶

    

Numbers of dirtree levels to show simultaneously

  * `NONE` None – Only list current directory’s content, with no recursion.

  * `BLEND` Blend File – List .blend files’ content.

  * `ALL_1` One Level – List all sub-directories’ content, one level of recursion.

  * `ALL_2` Two Levels – List all sub-directories’ content, two levels of recursion.

  * `ALL_3` Three Levels – List all sub-directories’ content, three levels of recursion.

Type:

    

enum in [`NONE`, `BLEND`, `ALL_1`, `ALL_2`, `ALL_3`], default `NONE`

show_details_datetime¶

    

Show a column listing the date and time of modification for each file

Type:

    

boolean, default False

show_details_size¶

    

Show a column listing the size of each file

Type:

    

boolean, default False

show_hidden¶

    

Show hidden dot files

Type:

    

boolean, default False

sort_method¶

    

Type:

    

enum in [Fileselect Params Sort
Items](bpy_types_enum_items/fileselect_params_sort_items.html#rna-enum-
fileselect-params-sort-items), default `FILE_SORT_ALPHA`

title¶

    

Title for the file browser

Type:

    

string, default “”, (readonly, never None)

use_filter¶

    

Enable filtering of files

Type:

    

boolean, default False

use_filter_asset_only¶

    

Hide .blend files items that are not data-blocks with asset metadata

Type:

    

boolean, default False

use_filter_backup¶

    

Show .blend1, .blend2, etc. files

Type:

    

boolean, default False

use_filter_blender¶

    

Show .blend files

Type:

    

boolean, default False

use_filter_blendid¶

    

Show .blend files items (objects, materials, etc.)

Type:

    

boolean, default False

use_filter_folder¶

    

Show folders

Type:

    

boolean, default False

use_filter_font¶

    

Show font files

Type:

    

boolean, default False

use_filter_image¶

    

Show image files

Type:

    

boolean, default False

use_filter_movie¶

    

Show movie files

Type:

    

boolean, default False

use_filter_script¶

    

Show script files

Type:

    

boolean, default False

use_filter_sound¶

    

Show sound files

Type:

    

boolean, default False

use_filter_text¶

    

Show text files

Type:

    

boolean, default False

use_filter_volume¶

    

Show 3D volume files

Type:

    

boolean, default False

use_library_browsing¶

    

Whether we may browse Blender files’ content or not

Type:

    

boolean, default False, (readonly)

use_sort_invert¶

    

Sort items descending, from highest value to lowest

Type:

    

boolean, default False

_classmethod _bl_rna_get_subclass(_id_ , _default =None_, _/_)¶

    

Parameters:

    

**id** (_str_) – The RNA type identifier.

Returns:

    

The RNA type or default when not found.

Return type:

    

[`bpy.types.Struct`](bpy.types.Struct.html#bpy.types.Struct
"bpy.types.Struct") subclass

_classmethod _bl_rna_get_subclass_py(_id_ , _default =None_, _/_)¶

    

Parameters:

    

**id** (_str_) – The RNA type identifier.

Returns:

    

The class or default when not found.

Return type:

    

type

## Inherited Properties¶

  * [`bpy_struct.id_data`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.id_data "bpy.types.bpy_struct.id_data")

|

  
---|---  
  
## Inherited Functions¶

  * [`bpy_struct.as_pointer`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.as_pointer "bpy.types.bpy_struct.as_pointer")
  * [`bpy_struct.driver_add`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.driver_add "bpy.types.bpy_struct.driver_add")
  * [`bpy_struct.driver_remove`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.driver_remove "bpy.types.bpy_struct.driver_remove")
  * [`bpy_struct.get`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.get "bpy.types.bpy_struct.get")
  * [`bpy_struct.id_properties_clear`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.id_properties_clear "bpy.types.bpy_struct.id_properties_clear")
  * [`bpy_struct.id_properties_ensure`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.id_properties_ensure "bpy.types.bpy_struct.id_properties_ensure")
  * [`bpy_struct.id_properties_ui`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.id_properties_ui "bpy.types.bpy_struct.id_properties_ui")
  * [`bpy_struct.is_property_hidden`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.is_property_hidden "bpy.types.bpy_struct.is_property_hidden")
  * [`bpy_struct.is_property_overridable_library`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.is_property_overridable_library "bpy.types.bpy_struct.is_property_overridable_library")
  * [`bpy_struct.is_property_readonly`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.is_property_readonly "bpy.types.bpy_struct.is_property_readonly")
  * [`bpy_struct.is_property_set`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.is_property_set "bpy.types.bpy_struct.is_property_set")
  * [`bpy_struct.items`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.items "bpy.types.bpy_struct.items")

|

  * [`bpy_struct.keyframe_delete`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.keyframe_delete "bpy.types.bpy_struct.keyframe_delete")
  * [`bpy_struct.keyframe_insert`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.keyframe_insert "bpy.types.bpy_struct.keyframe_insert")
  * [`bpy_struct.keys`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.keys "bpy.types.bpy_struct.keys")
  * [`bpy_struct.path_from_id`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.path_from_id "bpy.types.bpy_struct.path_from_id")
  * [`bpy_struct.path_resolve`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.path_resolve "bpy.types.bpy_struct.path_resolve")
  * [`bpy_struct.pop`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.pop "bpy.types.bpy_struct.pop")
  * [`bpy_struct.property_overridable_library_set`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.property_overridable_library_set "bpy.types.bpy_struct.property_overridable_library_set")
  * [`bpy_struct.property_unset`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.property_unset "bpy.types.bpy_struct.property_unset")
  * [`bpy_struct.rna_ancestors`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.rna_ancestors "bpy.types.bpy_struct.rna_ancestors")
  * [`bpy_struct.type_recast`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.type_recast "bpy.types.bpy_struct.type_recast")
  * [`bpy_struct.values`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.values "bpy.types.bpy_struct.values")

  
---|---  
  
## References¶

  * [`SpaceFileBrowser.params`](bpy.types.SpaceFileBrowser.html#bpy.types.SpaceFileBrowser.params "bpy.types.SpaceFileBrowser.params")

|

  * [`UILayout.template_file_select_path`](bpy.types.UILayout.html#bpy.types.UILayout.template_file_select_path "bpy.types.UILayout.template_file_select_path")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

