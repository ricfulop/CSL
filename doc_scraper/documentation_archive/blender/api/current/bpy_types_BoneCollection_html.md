---
url: https://docs.blender.org/api/current/bpy.types.BoneCollection.html
scraped_at: 2025-09-08T14:21:04.115441
title: BoneCollection(bpy_struct)¶
---

# BoneCollection(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.BoneCollection(_bpy_struct_)¶

    

Bone collection in an Armature data-block

bones¶

    

Bones assigned to this bone collection. In armature edit mode this will always
return an empty list of bones, as the bone collection memberships are only
synchronized when exiting edit mode.

Type:

    

[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Bone`](bpy.types.Bone.html#bpy.types.Bone "bpy.types.Bone"), (readonly)

child_number¶

    

Index of this collection into its parent’s list of children. Note that finding
this index requires a scan of all the bone collections, so do access this with
care.

Type:

    

int in [-inf, inf], default 0

children¶

    

Type:

    

[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of `BoneCollection`, (readonly)

index¶

    

Index of this bone collection in the armature.collections_all array. Note that
finding this index requires a scan of all the bone collections, so do access
this with care.

Type:

    

int in [-inf, inf], default 0, (readonly)

is_editable¶

    

This collection is owned by a local Armature, or was added via a library
override in the current blend file

Type:

    

boolean, default False, (readonly)

is_expanded¶

    

This bone collection is expanded in the bone collections tree view

Type:

    

boolean, default False

is_local_override¶

    

This collection was added via a library override in the current blend file

Type:

    

boolean, default False, (readonly)

is_solo¶

    

Show only this bone collection, and others also marked as ‘solo’

Type:

    

boolean, default False

is_visible¶

    

Bones in this collection will be visible in pose/object mode

Type:

    

boolean, default False

is_visible_ancestors¶

    

True when all of the ancestors of this bone collection are marked as visible;
always True for root bone collections

Type:

    

boolean, default False, (readonly)

is_visible_effectively¶

    

Whether this bone collection is effectively visible in the viewport. This is
True when this bone collection and all of its ancestors are visible, or when
it is marked as ‘solo’.

Type:

    

boolean, default False, (readonly)

name¶

    

Unique within the Armature

Type:

    

string, default “”, (never None)

parent¶

    

Parent bone collection. Note that accessing this requires a scan of all the
bone collections to find the parent.

Type:

    

`BoneCollection`

bones_recursive¶

    

A set of all bones assigned to this bone collection and its child collections.

(readonly)

assign(_bone_)¶

    

Assign the given bone to this collection

Parameters:

    

**bone** ([`AnyType`](bpy.types.AnyType.html#bpy.types.AnyType
"bpy.types.AnyType")) – Bone, PoseBone, or EditBone to assign to this
collection

Returns:

    

Assigned, Whether the bone was actually assigned; will be false if the bone
was already member of the collection

Return type:

    

boolean

unassign(_bone_)¶

    

Remove the given bone from this collection

Parameters:

    

**bone** ([`AnyType`](bpy.types.AnyType.html#bpy.types.AnyType
"bpy.types.AnyType")) – Bone, PoseBone, or EditBone to remove from this
collection

Returns:

    

Unassigned, Whether the bone was actually removed; will be false if the bone
was not a member of the collection to begin with

Return type:

    

boolean

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
  * [`Armature.collections_all`](bpy.types.Armature.html#bpy.types.Armature.collections_all "bpy.types.Armature.collections_all")
  * [`Bone.collections`](bpy.types.Bone.html#bpy.types.Bone.collections "bpy.types.Bone.collections")
  * `BoneCollection.children`
  * `BoneCollection.parent`

|

  * [`BoneCollections.active`](bpy.types.BoneCollections.html#bpy.types.BoneCollections.active "bpy.types.BoneCollections.active")
  * [`BoneCollections.new`](bpy.types.BoneCollections.html#bpy.types.BoneCollections.new "bpy.types.BoneCollections.new")
  * [`BoneCollections.new`](bpy.types.BoneCollections.html#bpy.types.BoneCollections.new "bpy.types.BoneCollections.new")
  * [`BoneCollections.remove`](bpy.types.BoneCollections.html#bpy.types.BoneCollections.remove "bpy.types.BoneCollections.remove")
  * [`EditBone.collections`](bpy.types.EditBone.html#bpy.types.EditBone.collections "bpy.types.EditBone.collections")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

