---
url: https://docs.blender.org/api/current/bpy.types.ActionKeyframeStrip.html
scraped_at: 2025-09-08T14:19:18.704065
title: ActionKeyframeStrip(ActionStrip)¶
---

# ActionKeyframeStrip(ActionStrip)¶  
  
base classes — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct"),
[`ActionStrip`](bpy.types.ActionStrip.html#bpy.types.ActionStrip
"bpy.types.ActionStrip")

_class _bpy.types.ActionKeyframeStrip(_ActionStrip_)¶

    

Strip with a set of F-Curves for each action slot

channelbags¶

    

Type:

    

[`ActionChannelbags`](bpy.types.ActionChannelbags.html#bpy.types.ActionChannelbags
"bpy.types.ActionChannelbags")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`ActionChannelbag`](bpy.types.ActionChannelbag.html#bpy.types.ActionChannelbag
"bpy.types.ActionChannelbag"), (readonly)

channelbag(_slot_ , _*_ , _ensure =False_)¶

    

Find the ActionChannelbag for a specific Slot

Parameters:

    

  * **slot** ([`ActionSlot`](bpy.types.ActionSlot.html#bpy.types.ActionSlot "bpy.types.ActionSlot")) – Slot, The slot for which to find the channelbag

  * **ensure** (_boolean_ _,__(__optional_ _)_) – Create if necessary, Ensure the channelbag exists for this slot, creating it if necessary

Returns:

    

Channels

Return type:

    

[`ActionChannelbag`](bpy.types.ActionChannelbag.html#bpy.types.ActionChannelbag
"bpy.types.ActionChannelbag")

key_insert(_slot_ , _data_path_ , _array_index_ , _value_ , _time_)¶

    

key_insert

Parameters:

    

  * **slot** ([`ActionSlot`](bpy.types.ActionSlot.html#bpy.types.ActionSlot "bpy.types.ActionSlot")) – Slot, The slot that identifies which ‘thing’ should be keyed

  * **data_path** (_string_ _,__(__never None_ _)_) – Data Path, F-Curve data path

  * **array_index** (_int in_ _[__-inf_ _,__inf_ _]_) – Array Index, Index of the animated array element, or -1 if the property is not an array

  * **value** (_float in_ _[__-inf_ _,__inf_ _]_) – Value to key, Value of the animated property

  * **time** (_float in_ _[__-inf_ _,__inf_ _]_) – Time of the key, Time, in frames, of the key

Returns:

    

Success, Whether the key was successfully inserted

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

  * [`ActionStrip.type`](bpy.types.ActionStrip.html#bpy.types.ActionStrip.type "bpy.types.ActionStrip.type")

  
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
  * [`ActionStrip.bl_rna_get_subclass`](bpy.types.ActionStrip.html#bpy.types.ActionStrip.bl_rna_get_subclass "bpy.types.ActionStrip.bl_rna_get_subclass")
  * [`ActionStrip.bl_rna_get_subclass_py`](bpy.types.ActionStrip.html#bpy.types.ActionStrip.bl_rna_get_subclass_py "bpy.types.ActionStrip.bl_rna_get_subclass_py")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

