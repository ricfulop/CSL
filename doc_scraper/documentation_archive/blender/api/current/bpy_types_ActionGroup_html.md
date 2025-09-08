---
url: https://docs.blender.org/api/current/bpy.types.ActionGroup.html
scraped_at: 2025-09-08T14:19:16.736835
title: ActionGroup(bpy_struct)¶
---

# ActionGroup(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.ActionGroup(_bpy_struct_)¶

    

Groups of F-Curves

channels¶

    

F-Curves in this group

Type:

    

[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`FCurve`](bpy.types.FCurve.html#bpy.types.FCurve "bpy.types.FCurve"),
(readonly)

color_set¶

    

Custom color set to use

Type:

    

enum in [Color Sets Items](bpy_types_enum_items/color_sets_items.html#rna-
enum-color-sets-items), default `DEFAULT`

colors¶

    

Copy of the colors associated with the group’s color set

Type:

    

[`ThemeBoneColorSet`](bpy.types.ThemeBoneColorSet.html#bpy.types.ThemeBoneColorSet
"bpy.types.ThemeBoneColorSet"), (readonly, never None)

is_custom_color_set¶

    

Color set is user-defined instead of a fixed theme color set

Type:

    

boolean, default False, (readonly)

lock¶

    

Action group is locked

Type:

    

boolean, default False

mute¶

    

Action group is muted

Type:

    

boolean, default False

name¶

    

Type:

    

string, default “”, (never None)

select¶

    

Action group is selected

Type:

    

boolean, default False

show_expanded¶

    

Action group is expanded except in graph editor

Type:

    

boolean, default False

show_expanded_graph¶

    

Action group is expanded in graph editor

Type:

    

boolean, default False

use_pin¶

    

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

  * [`Action.groups`](bpy.types.Action.html#bpy.types.Action.groups "bpy.types.Action.groups")
  * [`ActionChannelbag.groups`](bpy.types.ActionChannelbag.html#bpy.types.ActionChannelbag.groups "bpy.types.ActionChannelbag.groups")
  * [`ActionChannelbagGroups.new`](bpy.types.ActionChannelbagGroups.html#bpy.types.ActionChannelbagGroups.new "bpy.types.ActionChannelbagGroups.new")
  * [`ActionChannelbagGroups.remove`](bpy.types.ActionChannelbagGroups.html#bpy.types.ActionChannelbagGroups.remove "bpy.types.ActionChannelbagGroups.remove")

|

  * [`ActionGroups.new`](bpy.types.ActionGroups.html#bpy.types.ActionGroups.new "bpy.types.ActionGroups.new")
  * [`ActionGroups.remove`](bpy.types.ActionGroups.html#bpy.types.ActionGroups.remove "bpy.types.ActionGroups.remove")
  * [`FCurve.group`](bpy.types.FCurve.html#bpy.types.FCurve.group "bpy.types.FCurve.group")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

