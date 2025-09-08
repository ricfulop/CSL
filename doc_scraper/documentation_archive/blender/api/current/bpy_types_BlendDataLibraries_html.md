---
url: https://docs.blender.org/api/current/bpy.types.BlendDataLibraries.html
scraped_at: 2025-09-08T14:20:21.966984
title: BlendDataLibraries(bpy_struct)¶
---

# BlendDataLibraries(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.BlendDataLibraries(_bpy_struct_)¶

    

Collection of libraries

tag(_value_)¶

    

tag

Parameters:

    

**value** (_boolean_) – Value

remove(_library_ , _*_ , _do_unlink =True_, _do_id_user =True_, _do_ui_user
=True_)¶

    

Remove a library from the current blendfile

Parameters:

    

  * **library** ([`Library`](bpy.types.Library.html#bpy.types.Library "bpy.types.Library"), (never None)) – Library to remove

  * **do_unlink** (_boolean_ _,__(__optional_ _)_) – Unlink all usages of this library before deleting it

  * **do_id_user** (_boolean_ _,__(__optional_ _)_) – Decrement user counter of all datablocks used by this library

  * **do_ui_user** (_boolean_ _,__(__optional_ _)_) – Make sure interface does not reference this library

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

load(_filepath_ , _link =False_, _relative =False_, _assets_only =False_,
_create_liboverrides =False_, _reuse_liboverrides =False_,
_create_liboverrides_runtime =False_)¶

    

Returns a context manager which exposes 2 library objects on entering. Each
object has attributes matching bpy.data which are lists of strings to be
linked.

Parameters:

    

  * **filepath** (_str_ _|__bytes_) – The path to a blend file.

  * **link** (_bool_) – When False reference to the original file is lost.

  * **relative** (_bool_) – When True the path is stored relative to the open blend file.

  * **assets_only** (_bool_) – If True, only list data-blocks marked as assets.

  * **create_liboverrides** (_bool_) – If True and `link` is True, liboverrides will be created for linked data.

  * **reuse_liboverrides** (_bool_) – If True and `create_liboverride` is True, search for existing liboverride first.

  * **create_liboverrides_runtime** (_bool_) – If True and `create_liboverride` is True, create (or search for existing) runtime liboverride.

    
    
    import bpy
    
    filepath = "//link_library.blend"
    
    # Load a single scene we know the name of.
    with bpy.data.libraries.load(filepath) as (data_from, data_to):
        data_to.scenes = ["Scene"]
    
    
    # Load all meshes.
    with bpy.data.libraries.load(filepath) as (data_from, data_to):
        data_to.meshes = data_from.meshes
    
    
    # Link all objects starting with "A".
    with bpy.data.libraries.load(filepath, link=True) as (data_from, data_to):
        data_to.objects = [name for name in data_from.objects if name.startswith("A")]
    
    
    # Append everything.
    with bpy.data.libraries.load(filepath) as (data_from, data_to):
        for attr in dir(data_to):
            setattr(data_to, attr, getattr(data_from, attr))
    
    
    # The loaded objects can be accessed from 'data_to' outside of the context
    # since loading the data replaces the strings for the data-blocks or None
    # if the data-block could not be loaded.
    with bpy.data.libraries.load(filepath) as (data_from, data_to):
        data_to.meshes = data_from.meshes
    # Now operate directly on the loaded data.
    for mesh in data_to.meshes:
        if mesh is not None:
            print(mesh.name)
    

write(_filepath_ , _datablocks_ , _path_remap =False_, _fake_user =False_,
_compress =False_)¶

    

Write data-blocks into a blend file.

Note

Indirectly referenced data-blocks will be expanded and written too.

Parameters:

    

  * **filepath** (_str_ _|__bytes_) – The path to write the blend-file.

  * **datablocks** (set[[`bpy.types.ID`](bpy.types.ID.html#bpy.types.ID "bpy.types.ID")]) – set of data-blocks.

  * **path_remap** (_str_) – 

Optionally remap paths when writing the file:

    * `NONE` No path manipulation (default).

    * `RELATIVE` Remap paths that are already relative to the new location.

    * `RELATIVE_ALL` Remap all paths to be relative to the new location.

    * `ABSOLUTE` Make all paths absolute on writing.

  * **fake_user** (_bool_) – When True, data-blocks will be written with fake-user flag enabled.

  * **compress** (_bool_) – When True, write a compressed blend file.

    
    
    import bpy
    
    filepath = "//new_library.blend"
    
    # Write selected objects and their data to a blend file.
    data_blocks = set(bpy.context.selected_objects)
    bpy.data.libraries.write(filepath, data_blocks)
    
    
    # Write all meshes starting with a capital letter and
    # set them with fake-user enabled so they aren't lost on re-saving.
    data_blocks = {mesh for mesh in bpy.data.meshes if mesh.name[:1].isupper()}
    bpy.data.libraries.write(filepath, data_blocks, fake_user=True)
    
    
    # Write all materials, textures and node groups to a library.
    data_blocks = {*bpy.data.materials, *bpy.data.textures, *bpy.data.node_groups}
    bpy.data.libraries.write(filepath, data_blocks)
    

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

  * [`BlendData.libraries`](bpy.types.BlendData.html#bpy.types.BlendData.libraries "bpy.types.BlendData.libraries")

|

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

