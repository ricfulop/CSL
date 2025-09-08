---
url: https://docs.blender.org/api/current/bpy.types.BlendImportContext.html
scraped_at: 2025-09-08T14:20:47.101297
title: BlendImportContext(bpy_struct)¶
---

# BlendImportContext(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.BlendImportContext(_bpy_struct_)¶

    

Contextual data for a blendfile library/linked-data related operation.
Currently only exposed as read-only data for the pre/post blendimport handlers

import_items¶

    

Type:

    

[`BlendImportContextItems`](bpy.types.BlendImportContextItems.html#bpy.types.BlendImportContextItems
"bpy.types.BlendImportContextItems")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`BlendImportContextItem`](bpy.types.BlendImportContextItem.html#bpy.types.BlendImportContextItem
"bpy.types.BlendImportContextItem"), (readonly)

options¶

    

Options for this blendfile import operation

  * `LINK` Only link data, instead of appending it.

  * `MAKE_PATHS_RELATIVE` Make paths of used library blendfiles relative to current blendfile.

  * `USE_PLACEHOLDERS` Generate a placeholder (empty ID) if not found in any library files.

  * `FORCE_INDIRECT` Force loaded ID to be tagged as indirectly linked (used in reload context only).

  * `APPEND_SET_FAKEUSER` Set fake user on appended IDs.

  * `APPEND_RECURSIVE` Append (make local) also indirect dependencies of appended IDs coming from other libraries. NOTE: All IDs (including indirectly linked ones) coming from the same initial library are always made local.

  * `APPEND_LOCAL_ID_REUSE` Try to re-use previously appended matching IDs when appending them again, instead of creating local duplicates.

  * `APPEND_ASSET_DATA_CLEAR` Clear the asset data on append (it is always kept for linked data).

  * `SELECT_OBJECTS` Automatically select imported objects.

  * `USE_ACTIVE_COLLECTION` Use the active Collection of the current View Layer to instantiate imported collections and objects.

  * `OBDATA_INSTANCE` Instantiate object data IDs (i.e. create objects for them if needed).

  * `COLLECTION_INSTANCE` Instantiate collections as empties, instead of linking them into the current view layer.

Type:

    

enum set in {`LINK`, `MAKE_PATHS_RELATIVE`, `USE_PLACEHOLDERS`,
`FORCE_INDIRECT`, `APPEND_SET_FAKEUSER`, `APPEND_RECURSIVE`,
`APPEND_LOCAL_ID_REUSE`, `APPEND_ASSET_DATA_CLEAR`, `SELECT_OBJECTS`,
`USE_ACTIVE_COLLECTION`, `OBDATA_INSTANCE`, `COLLECTION_INSTANCE`}, default
`{'LINK'}`, (readonly)

process_stage¶

    

Current stage of the import process

  * `INIT` Blendfile import context has been initialized and filled with a list of items to import, no data has been linked or appended yet.

  * `DONE` All data has been imported and is available in the list of ``import_items``.

Type:

    

enum in [`INIT`, `DONE`], default `INIT`, (readonly)

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
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

