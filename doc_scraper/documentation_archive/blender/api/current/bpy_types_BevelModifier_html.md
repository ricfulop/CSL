---
url: https://docs.blender.org/api/current/bpy.types.BevelModifier.html
scraped_at: 2025-09-08T14:20:05.912727
title: BevelModifier(Modifier)¶
---

# BevelModifier(Modifier)¶  
  
base classes — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct"),
[`Modifier`](bpy.types.Modifier.html#bpy.types.Modifier "bpy.types.Modifier")

_class _bpy.types.BevelModifier(_Modifier_)¶

    

Bevel modifier to make edges and vertices more rounded

affect¶

    

Affect edges or vertices

  * `VERTICES` Vertices – Affect only vertices.

  * `EDGES` Edges – Affect only edges.

Type:

    

enum in [`VERTICES`, `EDGES`], default `EDGES`

angle_limit¶

    

Angle above which to bevel edges

Type:

    

float in [0, 3.14159], default 0.523599

custom_profile¶

    

The path for the custom profile

Type:

    

[`CurveProfile`](bpy.types.CurveProfile.html#bpy.types.CurveProfile
"bpy.types.CurveProfile"), (readonly)

edge_weight¶

    

Attribute name for edge weight

Type:

    

string, default “”, (never None)

face_strength_mode¶

    

Whether to set face strength, and which faces to set it on

  * `FSTR_NONE` None – Do not set face strength.

  * `FSTR_NEW` New – Set face strength on new faces only.

  * `FSTR_AFFECTED` Affected – Set face strength on new and affected faces only.

  * `FSTR_ALL` All – Set face strength on all faces.

Type:

    

enum in [`FSTR_NONE`, `FSTR_NEW`, `FSTR_AFFECTED`, `FSTR_ALL`], default
`FSTR_NONE`

harden_normals¶

    

Match normals of new faces to adjacent faces

Type:

    

boolean, default False

invert_vertex_group¶

    

Invert vertex group influence

Type:

    

boolean, default False

limit_method¶

    

  * `NONE` None – Bevel the entire mesh by a constant amount.

  * `ANGLE` Angle – Only bevel edges with sharp enough angles between faces.

  * `WEIGHT` Weight – Use bevel weights to determine how much bevel is applied in edge mode.

  * `VGROUP` Vertex Group – Use vertex group weights to select whether vertex or edge is beveled.

Type:

    

enum in [`NONE`, `ANGLE`, `WEIGHT`, `VGROUP`], default `ANGLE`

loop_slide¶

    

Prefer sliding along edges to having even widths

Type:

    

boolean, default True

mark_seam¶

    

Mark Seams along beveled edges

Type:

    

boolean, default False

mark_sharp¶

    

Mark beveled edges as sharp

Type:

    

boolean, default False

material¶

    

Material index of generated faces, -1 for automatic

Type:

    

int in [-1, 32767], default -1

miter_inner¶

    

Pattern to use for inside of miters

  * `MITER_SHARP` Sharp – Inside of miter is sharp.

  * `MITER_ARC` Arc – Inside of miter is arc.

Type:

    

enum in [`MITER_SHARP`, `MITER_ARC`], default `MITER_SHARP`

miter_outer¶

    

Pattern to use for outside of miters

  * `MITER_SHARP` Sharp – Outside of miter is sharp.

  * `MITER_PATCH` Patch – Outside of miter is squared-off patch.

  * `MITER_ARC` Arc – Outside of miter is arc.

Type:

    

enum in [`MITER_SHARP`, `MITER_PATCH`, `MITER_ARC`], default `MITER_SHARP`

offset_type¶

    

What distance Width measures

  * `OFFSET` Offset – Amount is offset of new edges from original.

  * `WIDTH` Width – Amount is width of new face.

  * `DEPTH` Depth – Amount is perpendicular distance from original edge to bevel face.

  * `PERCENT` Percent – Amount is percent of adjacent edge length.

  * `ABSOLUTE` Absolute – Amount is absolute distance along adjacent edge.

Type:

    

enum in [`OFFSET`, `WIDTH`, `DEPTH`, `PERCENT`, `ABSOLUTE`], default `OFFSET`

profile¶

    

The profile shape (0.5 = round)

Type:

    

float in [0, 1], default 0.5

profile_type¶

    

The type of shape used to rebuild a beveled section

  * `SUPERELLIPSE` Superellipse – The profile can be a concave or convex curve.

  * `CUSTOM` Custom – The profile can be any arbitrary path between its endpoints.

Type:

    

enum in [`SUPERELLIPSE`, `CUSTOM`], default `SUPERELLIPSE`

segments¶

    

Number of segments for round edges/verts

Type:

    

int in [1, 1000], default 1

spread¶

    

Spread distance for inner miter arcs

Type:

    

float in [0, inf], default 0.1

use_clamp_overlap¶

    

Clamp the width to avoid overlap

Type:

    

boolean, default True

vertex_group¶

    

Vertex group name

Type:

    

string, default “”, (never None)

vertex_weight¶

    

Attribute name for vertex weight

Type:

    

string, default “”, (never None)

vmesh_method¶

    

The method to use to create the mesh at intersections

  * `ADJ` Grid Fill – Default patterned fill.

  * `CUTOFF` Cutoff – A cut-off at the end of each profile before the intersection.

Type:

    

enum in [`ADJ`, `CUTOFF`], default `ADJ`

width¶

    

Bevel amount

Type:

    

float in [0, inf], default 0.1

width_pct¶

    

Bevel amount for percentage method

Type:

    

float in [0, inf], default 0.1

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

