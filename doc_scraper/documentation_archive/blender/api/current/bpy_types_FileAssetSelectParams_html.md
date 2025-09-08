---
url: https://docs.blender.org/api/current/bpy.types.FileAssetSelectParams.html
scraped_at: 2025-09-08T14:25:15.197091
title: FileAssetSelectParams(FileSelectParams)¶
---

# FileAssetSelectParams(FileSelectParams)¶  
  
base classes — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct"),
[`FileSelectParams`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams
"bpy.types.FileSelectParams")

_class _bpy.types.FileAssetSelectParams(_FileSelectParams_)¶

    

Settings for the file selection in Asset Browser mode

asset_library_reference¶

    

  * `ALL` All Libraries – Show assets from all of the listed asset libraries.

  * `LOCAL` Current File – Show the assets currently available in this Blender session.

  * `ESSENTIALS` Essentials – Show the basic building blocks and utilities coming with Blender.

  * `CUSTOM` Custom – Show assets from the asset libraries configured in the Preferences.

Type:

    

enum in [`ALL`, `LOCAL`, `ESSENTIALS`, `CUSTOM`], default `ALL`

catalog_id¶

    

The UUID of the catalog shown in the browser

Type:

    

string, default “”, (never None)

filter_asset_id¶

    

Which asset types to show/hide, when browsing an asset library

Type:

    

[`FileAssetSelectIDFilter`](bpy.types.FileAssetSelectIDFilter.html#bpy.types.FileAssetSelectIDFilter
"bpy.types.FileAssetSelectIDFilter"), (readonly, never None)

import_method¶

    

Determine how the asset will be imported

  * `FOLLOW_PREFS` Follow Preferences – Use the import method set in the Preferences for this asset library, don’t override it for this Asset Browser.

  * `LINK` Link – Import the assets as linked data-block.

  * `APPEND` Append – Import the assets as copied data-block, with no link to the original asset data-block.

  * `APPEND_REUSE` Append (Reuse Data) – Import the assets as copied data-block while avoiding multiple copies of nested, typically heavy data. For example the textures of a material asset, or the mesh of an object asset, don’t have to be copied every time this asset is imported. The instances of the asset share the data instead.

Type:

    

enum in [`FOLLOW_PREFS`, `LINK`, `APPEND`, `APPEND_REUSE`], default `LINK`

instance_collections_on_append¶

    

Create instances for collections when appending, rather than adding them
directly to the scene

Type:

    

boolean, default False

instance_collections_on_link¶

    

Create instances for collections when linking, rather than adding them
directly to the scene

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
  * [`FileSelectParams.title`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.title "bpy.types.FileSelectParams.title")
  * [`FileSelectParams.directory`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.directory "bpy.types.FileSelectParams.directory")
  * [`FileSelectParams.filename`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.filename "bpy.types.FileSelectParams.filename")
  * [`FileSelectParams.use_library_browsing`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.use_library_browsing "bpy.types.FileSelectParams.use_library_browsing")
  * [`FileSelectParams.display_type`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.display_type "bpy.types.FileSelectParams.display_type")
  * [`FileSelectParams.recursion_level`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.recursion_level "bpy.types.FileSelectParams.recursion_level")
  * [`FileSelectParams.show_details_size`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.show_details_size "bpy.types.FileSelectParams.show_details_size")
  * [`FileSelectParams.show_details_datetime`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.show_details_datetime "bpy.types.FileSelectParams.show_details_datetime")
  * [`FileSelectParams.use_filter`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.use_filter "bpy.types.FileSelectParams.use_filter")
  * [`FileSelectParams.show_hidden`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.show_hidden "bpy.types.FileSelectParams.show_hidden")
  * [`FileSelectParams.sort_method`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.sort_method "bpy.types.FileSelectParams.sort_method")
  * [`FileSelectParams.use_sort_invert`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.use_sort_invert "bpy.types.FileSelectParams.use_sort_invert")
  * [`FileSelectParams.use_filter_image`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.use_filter_image "bpy.types.FileSelectParams.use_filter_image")
  * [`FileSelectParams.use_filter_blender`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.use_filter_blender "bpy.types.FileSelectParams.use_filter_blender")
  * [`FileSelectParams.use_filter_backup`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.use_filter_backup "bpy.types.FileSelectParams.use_filter_backup")

|

  * [`FileSelectParams.use_filter_movie`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.use_filter_movie "bpy.types.FileSelectParams.use_filter_movie")
  * [`FileSelectParams.use_filter_script`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.use_filter_script "bpy.types.FileSelectParams.use_filter_script")
  * [`FileSelectParams.use_filter_font`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.use_filter_font "bpy.types.FileSelectParams.use_filter_font")
  * [`FileSelectParams.use_filter_sound`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.use_filter_sound "bpy.types.FileSelectParams.use_filter_sound")
  * [`FileSelectParams.use_filter_text`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.use_filter_text "bpy.types.FileSelectParams.use_filter_text")
  * [`FileSelectParams.use_filter_volume`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.use_filter_volume "bpy.types.FileSelectParams.use_filter_volume")
  * [`FileSelectParams.use_filter_folder`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.use_filter_folder "bpy.types.FileSelectParams.use_filter_folder")
  * [`FileSelectParams.use_filter_blendid`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.use_filter_blendid "bpy.types.FileSelectParams.use_filter_blendid")
  * [`FileSelectParams.use_filter_asset_only`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.use_filter_asset_only "bpy.types.FileSelectParams.use_filter_asset_only")
  * [`FileSelectParams.filter_id`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.filter_id "bpy.types.FileSelectParams.filter_id")
  * [`FileSelectParams.filter_glob`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.filter_glob "bpy.types.FileSelectParams.filter_glob")
  * [`FileSelectParams.filter_search`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.filter_search "bpy.types.FileSelectParams.filter_search")
  * [`FileSelectParams.display_size`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.display_size "bpy.types.FileSelectParams.display_size")
  * [`FileSelectParams.display_size_discrete`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.display_size_discrete "bpy.types.FileSelectParams.display_size_discrete")
  * [`FileSelectParams.list_display_size`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.list_display_size "bpy.types.FileSelectParams.list_display_size")
  * [`FileSelectParams.list_column_size`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.list_column_size "bpy.types.FileSelectParams.list_column_size")

  
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
  * [`bpy_struct.keyframe_delete`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.keyframe_delete "bpy.types.bpy_struct.keyframe_delete")

|

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
  * [`FileSelectParams.bl_rna_get_subclass`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.bl_rna_get_subclass "bpy.types.FileSelectParams.bl_rna_get_subclass")
  * [`FileSelectParams.bl_rna_get_subclass_py`](bpy.types.FileSelectParams.html#bpy.types.FileSelectParams.bl_rna_get_subclass_py "bpy.types.FileSelectParams.bl_rna_get_subclass_py")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

