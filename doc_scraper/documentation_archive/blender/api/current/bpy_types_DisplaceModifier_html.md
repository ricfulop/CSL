---
url: https://docs.blender.org/api/current/bpy.types.DisplaceModifier.html
scraped_at: 2025-09-08T14:24:34.971567
title: DisplaceModifier(Modifier)¶
---

# DisplaceModifier(Modifier)¶  
  
base classes — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct"),
[`Modifier`](bpy.types.Modifier.html#bpy.types.Modifier "bpy.types.Modifier")

_class _bpy.types.DisplaceModifier(_Modifier_)¶

    

Displacement modifier

direction¶

    

  * `X` X – Use the texture’s intensity value to displace in the X direction.

  * `Y` Y – Use the texture’s intensity value to displace in the Y direction.

  * `Z` Z – Use the texture’s intensity value to displace in the Z direction.

  * `NORMAL` Normal – Use the texture’s intensity value to displace along the vertex normal.

  * `CUSTOM_NORMAL` Custom Normal – Use the texture’s intensity value to displace along the (averaged) custom normal (falls back to vertex).

  * `RGB_TO_XYZ` RGB to XYZ – Use the texture’s RGB values to displace the mesh in the XYZ direction.

Type:

    

enum in [`X`, `Y`, `Z`, `NORMAL`, `CUSTOM_NORMAL`, `RGB_TO_XYZ`], default
`NORMAL`

invert_vertex_group¶

    

Invert vertex group influence

Type:

    

boolean, default False

mid_level¶

    

Material value that gives no displacement

Type:

    

float in [-inf, inf], default 0.5

space¶

    

  * `LOCAL` Local – Direction is defined in local coordinates.

  * `GLOBAL` Global – Direction is defined in global coordinates.

Type:

    

enum in [`LOCAL`, `GLOBAL`], default `LOCAL`

strength¶

    

Amount to displace geometry

Type:

    

float in [-inf, inf], default 1.0

texture¶

    

Type:

    

[`Texture`](bpy.types.Texture.html#bpy.types.Texture "bpy.types.Texture")

texture_coords¶

    

  * `LOCAL` Local – Use the local coordinate system for the texture coordinates.

  * `GLOBAL` Global – Use the global coordinate system for the texture coordinates.

  * `OBJECT` Object – Use the linked object’s local coordinate system for the texture coordinates.

  * `UV` UV – Use UV coordinates for the texture coordinates.

Type:

    

enum in [`LOCAL`, `GLOBAL`, `OBJECT`, `UV`], default `LOCAL`

texture_coords_bone¶

    

Bone to set the texture coordinates

Type:

    

string, default “”, (never None)

texture_coords_object¶

    

Object to set the texture coordinates

Type:

    

[`Object`](bpy.types.Object.html#bpy.types.Object "bpy.types.Object")

uv_layer¶

    

UV map name

Type:

    

string, default “”, (never None)

vertex_group¶

    

Name of Vertex Group which determines influence of modifier per point

Type:

    

string, default “”, (never None)

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
  * [`Modifier.name`](bpy.types.Modifier.html#bpy.types.Modifier.name "bpy.types.Modifier.name")
  * [`Modifier.type`](bpy.types.Modifier.html#bpy.types.Modifier.type "bpy.types.Modifier.type")
  * [`Modifier.show_viewport`](bpy.types.Modifier.html#bpy.types.Modifier.show_viewport "bpy.types.Modifier.show_viewport")
  * [`Modifier.show_render`](bpy.types.Modifier.html#bpy.types.Modifier.show_render "bpy.types.Modifier.show_render")
  * [`Modifier.show_in_editmode`](bpy.types.Modifier.html#bpy.types.Modifier.show_in_editmode "bpy.types.Modifier.show_in_editmode")
  * [`Modifier.show_on_cage`](bpy.types.Modifier.html#bpy.types.Modifier.show_on_cage "bpy.types.Modifier.show_on_cage")

|

  * [`Modifier.show_expanded`](bpy.types.Modifier.html#bpy.types.Modifier.show_expanded "bpy.types.Modifier.show_expanded")
  * [`Modifier.is_active`](bpy.types.Modifier.html#bpy.types.Modifier.is_active "bpy.types.Modifier.is_active")
  * [`Modifier.use_pin_to_last`](bpy.types.Modifier.html#bpy.types.Modifier.use_pin_to_last "bpy.types.Modifier.use_pin_to_last")
  * [`Modifier.is_override_data`](bpy.types.Modifier.html#bpy.types.Modifier.is_override_data "bpy.types.Modifier.is_override_data")
  * [`Modifier.use_apply_on_spline`](bpy.types.Modifier.html#bpy.types.Modifier.use_apply_on_spline "bpy.types.Modifier.use_apply_on_spline")
  * [`Modifier.execution_time`](bpy.types.Modifier.html#bpy.types.Modifier.execution_time "bpy.types.Modifier.execution_time")
  * [`Modifier.persistent_uid`](bpy.types.Modifier.html#bpy.types.Modifier.persistent_uid "bpy.types.Modifier.persistent_uid")

  
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
  * [`Modifier.bl_rna_get_subclass`](bpy.types.Modifier.html#bpy.types.Modifier.bl_rna_get_subclass "bpy.types.Modifier.bl_rna_get_subclass")
  * [`Modifier.bl_rna_get_subclass_py`](bpy.types.Modifier.html#bpy.types.Modifier.bl_rna_get_subclass_py "bpy.types.Modifier.bl_rna_get_subclass_py")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

