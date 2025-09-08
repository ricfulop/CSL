---
url: https://docs.blender.org/api/current/bpy.types.BoneCollections.html
scraped_at: 2025-09-08T14:21:06.129000
title: BoneCollections(bpy_struct)¶
---

# BoneCollections(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.BoneCollections(_bpy_struct_)¶

    

The Bone Collections of this Armature

active¶

    

Armature’s active bone collection

Type:

    

[`BoneCollection`](bpy.types.BoneCollection.html#bpy.types.BoneCollection
"bpy.types.BoneCollection")

active_index¶

    

The index of the Armature’s active bone collection; -1 when there is no active
collection. Note that this is indexing the underlying array of bone
collections, which may not be in the order you expect. Root collections are
listed first, and siblings are always sequential. Apart from that, bone
collections can be in any order, and thus incrementing or decrementing this
index can make the active bone collection jump around in unexpected ways. For
a more predictable interface, use `active` or `active_name`.

Type:

    

int in [-inf, inf], default 0

active_name¶

    

The name of the Armature’s active bone collection; empty when there is no
active collection

Type:

    

string, default “”, (never None)

is_solo_active¶

    

Read-only flag that indicates there is at least one bone collection marked as
‘solo’

Type:

    

boolean, default False, (readonly)

new(_name_ , _*_ , _parent =None_)¶

    

Add a new empty bone collection to the armature

Parameters:

    

  * **name** (_string_ _,__(__never None_ _)_) – Name, Name of the new collection. Blender will ensure it is unique within the collections of the Armature.

  * **parent** ([`BoneCollection`](bpy.types.BoneCollection.html#bpy.types.BoneCollection "bpy.types.BoneCollection"), (optional)) – Parent Collection, If not None, the new bone collection becomes a child of this collection

Returns:

    

Newly created bone collection

Return type:

    

[`BoneCollection`](bpy.types.BoneCollection.html#bpy.types.BoneCollection
"bpy.types.BoneCollection")

remove(_bone_collection_)¶

    

Remove the bone collection from the armature. If this bone collection has any
children, they will be reassigned to their grandparent; in other words, the
children will take the place of the removed bone collection.

Parameters:

    

**bone_collection**
([`BoneCollection`](bpy.types.BoneCollection.html#bpy.types.BoneCollection
"bpy.types.BoneCollection")) – Bone Collection, The bone collection to remove

move(_from_index_ , _to_index_)¶

    

Move a bone collection to a different position in the collection list. This
can only be used to reorder siblings, and not to change parent-child
relationships.

Parameters:

    

  * **from_index** (_int in_ _[__-inf_ _,__inf_ _]_) – From Index, Index to move

  * **to_index** (_int in_ _[__-inf_ _,__inf_ _]_) – To Index, Target index

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

  * [`Armature.collections`](bpy.types.Armature.html#bpy.types.Armature.collections "bpy.types.Armature.collections")

|

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

