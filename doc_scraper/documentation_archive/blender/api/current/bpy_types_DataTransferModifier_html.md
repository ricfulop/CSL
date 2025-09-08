---
url: https://docs.blender.org/api/current/bpy.types.DataTransferModifier.html
scraped_at: 2025-09-08T14:24:29.941272
title: DataTransferModifier(Modifier)¶
---

# DataTransferModifier(Modifier)¶  
  
base classes — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct"),
[`Modifier`](bpy.types.Modifier.html#bpy.types.Modifier "bpy.types.Modifier")

_class _bpy.types.DataTransferModifier(_Modifier_)¶

    

Modifier transferring some data from a source mesh

data_types_edges¶

    

Which edge data layers to transfer

  * `SHARP_EDGE` Sharp – Transfer sharp mark.

  * `SEAM` UV Seam – Transfer UV seam mark.

  * `CREASE` Crease – Transfer subdivision crease values.

  * `BEVEL_WEIGHT_EDGE` Bevel Weight – Transfer bevel weights.

  * `FREESTYLE_EDGE` Freestyle – Transfer Freestyle edge mark.

Type:

    

enum set in {`SHARP_EDGE`, `SEAM`, `CREASE`, `BEVEL_WEIGHT_EDGE`,
`FREESTYLE_EDGE`}, default `{'SHARP_EDGE'}`

data_types_loops¶

    

Which face corner data layers to transfer

  * `CUSTOM_NORMAL` Custom Normals – Transfer custom normals.

  * `COLOR_CORNER` Colors – Transfer color attributes.

  * `UV` UVs – Transfer UV layers.

Type:

    

enum set in {`CUSTOM_NORMAL`, `COLOR_CORNER`, `UV`}, default
`{'CUSTOM_NORMAL'}`

data_types_polys¶

    

Which face data layers to transfer

  * `SMOOTH` Smooth – Transfer flat/smooth mark.

  * `FREESTYLE_FACE` Freestyle Mark – Transfer Freestyle face mark.

Type:

    

enum set in {`SMOOTH`, `FREESTYLE_FACE`}, default `{'SMOOTH'}`

data_types_verts¶

    

Which vertex data layers to transfer

  * `VGROUP_WEIGHTS` Vertex Groups – Transfer active or all vertex groups.

  * `BEVEL_WEIGHT_VERT` Bevel Weight – Transfer bevel weights.

  * `COLOR_VERTEX` Colors – Transfer color attributes.

Type:

    

enum set in {`VGROUP_WEIGHTS`, `BEVEL_WEIGHT_VERT`, `COLOR_VERTEX`}, default
`{'VGROUP_WEIGHTS'}`

edge_mapping¶

    

Method used to map source edges to destination ones

Type:

    

enum in [Dt Method Edge
Items](bpy_types_enum_items/dt_method_edge_items.html#rna-enum-dt-method-edge-
items), default `NEAREST`

invert_vertex_group¶

    

Invert vertex group influence

Type:

    

boolean, default False

islands_precision¶

    

Factor controlling precision of islands handling (typically, 0.1 should be
enough, higher values can make things really slow)

Type:

    

float in [0, 1], default 0.0

layers_uv_select_dst¶

    

How to match source and destination layers

Type:

    

enum in [Dt Layers Select Dst
Items](bpy_types_enum_items/dt_layers_select_dst_items.html#rna-enum-dt-
layers-select-dst-items), default `NAME`

layers_uv_select_src¶

    

Which layers to transfer, in case of multi-layers types

Type:

    

enum in [Dt Layers Select Src
Items](bpy_types_enum_items/dt_layers_select_src_items.html#rna-enum-dt-
layers-select-src-items), default `ALL`

layers_vcol_loop_select_dst¶

    

How to match source and destination layers

Type:

    

enum in [Dt Layers Select Dst
Items](bpy_types_enum_items/dt_layers_select_dst_items.html#rna-enum-dt-
layers-select-dst-items), default `NAME`

layers_vcol_loop_select_src¶

    

Which layers to transfer, in case of multi-layers types

Type:

    

enum in [Dt Layers Select Src
Items](bpy_types_enum_items/dt_layers_select_src_items.html#rna-enum-dt-
layers-select-src-items), default `ALL`

layers_vcol_vert_select_dst¶

    

How to match source and destination layers

Type:

    

enum in [Dt Layers Select Dst
Items](bpy_types_enum_items/dt_layers_select_dst_items.html#rna-enum-dt-
layers-select-dst-items), default `NAME`

layers_vcol_vert_select_src¶

    

Which layers to transfer, in case of multi-layers types

Type:

    

enum in [Dt Layers Select Src
Items](bpy_types_enum_items/dt_layers_select_src_items.html#rna-enum-dt-
layers-select-src-items), default `ALL`

layers_vgroup_select_dst¶

    

How to match source and destination layers

Type:

    

enum in [Dt Layers Select Dst
Items](bpy_types_enum_items/dt_layers_select_dst_items.html#rna-enum-dt-
layers-select-dst-items), default `NAME`

layers_vgroup_select_src¶

    

Which layers to transfer, in case of multi-layers types

Type:

    

enum in [Dt Layers Select Src
Items](bpy_types_enum_items/dt_layers_select_src_items.html#rna-enum-dt-
layers-select-src-items), default `ALL`

loop_mapping¶

    

Method used to map source faces’ corners to destination ones

Type:

    

enum in [Dt Method Loop
Items](bpy_types_enum_items/dt_method_loop_items.html#rna-enum-dt-method-loop-
items), default `NEAREST_POLYNOR`

max_distance¶

    

Maximum allowed distance between source and destination element, for non-
topology mappings

Type:

    

float in [0, inf], default 1.0

mix_factor¶

    

Factor to use when applying data to destination (exact behavior depends on mix
mode, multiplied with weights from vertex group when defined)

Type:

    

float in [0, 1], default 0.0

mix_mode¶

    

How to affect destination elements with source values

Type:

    

enum in [Dt Mix Mode Items](bpy_types_enum_items/dt_mix_mode_items.html#rna-
enum-dt-mix-mode-items), default `REPLACE`

object¶

    

Object to transfer data from

Type:

    

[`Object`](bpy.types.Object.html#bpy.types.Object "bpy.types.Object")

poly_mapping¶

    

Method used to map source faces to destination ones

Type:

    

enum in [Dt Method Poly
Items](bpy_types_enum_items/dt_method_poly_items.html#rna-enum-dt-method-poly-
items), default `NEAREST`

ray_radius¶

    

‘Width’ of rays (especially useful when raycasting against vertices or edges)

Type:

    

float in [0, inf], default 0.0

use_edge_data¶

    

Enable edge data transfer

Type:

    

boolean, default False

use_loop_data¶

    

Enable face corner data transfer

Type:

    

boolean, default False

use_max_distance¶

    

Source elements must be closer than given distance from destination one

Type:

    

boolean, default False

use_object_transform¶

    

Evaluate source and destination meshes in global space

Type:

    

boolean, default True

use_poly_data¶

    

Enable face data transfer

Type:

    

boolean, default False

use_vert_data¶

    

Enable vertex data transfer

Type:

    

boolean, default False

vert_mapping¶

    

Method used to map source vertices to destination ones

Type:

    

enum in [Dt Method Vertex
Items](bpy_types_enum_items/dt_method_vertex_items.html#rna-enum-dt-method-
vertex-items), default `NEAREST`

vertex_group¶

    

Vertex group name for selecting the affected areas

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

