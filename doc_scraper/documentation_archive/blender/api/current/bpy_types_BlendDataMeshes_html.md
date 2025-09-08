---
url: https://docs.blender.org/api/current/bpy.types.BlendDataMeshes.html
scraped_at: 2025-09-08T14:20:26.977224
title: BlendDataMeshes(bpy_struct)¶
---

# BlendDataMeshes(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.BlendDataMeshes(_bpy_struct_)¶

    

Collection of meshes

new(_name_)¶

    

Add a new mesh to the main database

Parameters:

    

**name** (_string_ _,__(__never None_ _)_) – New name for the data-block

Returns:

    

New mesh data-block

Return type:

    

[`Mesh`](bpy.types.Mesh.html#bpy.types.Mesh "bpy.types.Mesh")

new_from_object(_object_ , _*_ , _preserve_all_data_layers =False_, _depsgraph
=None_)¶

    

Add a new mesh created from given object (undeformed geometry if object is
original, and final evaluated geometry, with all modifiers etc., if object is
evaluated)

Parameters:

    

  * **object** ([`Object`](bpy.types.Object.html#bpy.types.Object "bpy.types.Object"), (never None)) – Object to create mesh from

  * **preserve_all_data_layers** (_boolean_ _,__(__optional_ _)_) – Preserve all data layers in the mesh, like UV maps and vertex groups. By default Blender only computes the subset of data layers needed for viewport display and rendering, for better performance.

  * **depsgraph** ([`Depsgraph`](bpy.types.Depsgraph.html#bpy.types.Depsgraph "bpy.types.Depsgraph"), (optional)) – Dependency Graph, Evaluated dependency graph which is required when preserve_all_data_layers is true

Returns:

    

Mesh created from object, remove it if it is only used for export

Return type:

    

[`Mesh`](bpy.types.Mesh.html#bpy.types.Mesh "bpy.types.Mesh")

remove(_mesh_ , _*_ , _do_unlink =True_, _do_id_user =True_, _do_ui_user
=True_)¶

    

Remove a mesh from the current blendfile

Parameters:

    

  * **mesh** ([`Mesh`](bpy.types.Mesh.html#bpy.types.Mesh "bpy.types.Mesh"), (never None)) – Mesh to remove

  * **do_unlink** (_boolean_ _,__(__optional_ _)_) – Unlink all usages of this mesh before deleting it (WARNING: will also delete objects instancing that mesh data)

  * **do_id_user** (_boolean_ _,__(__optional_ _)_) – Decrement user counter of all datablocks used by this mesh data

  * **do_ui_user** (_boolean_ _,__(__optional_ _)_) – Make sure interface does not reference this mesh data

tag(_value_)¶

    

tag

Parameters:

    

**value** (_boolean_) – Value

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

  * [`BlendData.meshes`](bpy.types.BlendData.html#bpy.types.BlendData.meshes "bpy.types.BlendData.meshes")

|

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

