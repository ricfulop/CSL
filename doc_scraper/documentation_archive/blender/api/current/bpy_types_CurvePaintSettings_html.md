---
url: https://docs.blender.org/api/current/bpy.types.CurvePaintSettings.html
scraped_at: 2025-09-08T14:24:17.943997
title: CurvePaintSettings(bpy_struct)¶
---

# CurvePaintSettings(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.CurvePaintSettings(_bpy_struct_)¶

    

corner_angle¶

    

Angles above this are considered corners

Type:

    

float in [0, 3.14159], default 1.22173

curve_type¶

    

Type of curve to use for new strokes

Type:

    

enum in [`POLY`, `BEZIER`], default `BEZIER`

depth_mode¶

    

Method of projecting depth

Type:

    

enum in [`CURSOR`, `SURFACE`], default `CURSOR`

error_threshold¶

    

Allow deviation for a smoother, less precise line

Type:

    

int in [1, 100], default 8

fit_method¶

    

Curve fitting method

Type:

    

enum in [Curve Fit Method
Items](bpy_types_enum_items/curve_fit_method_items.html#rna-enum-curve-fit-
method-items), default `REFIT`

radius_max¶

    

Radius to use when the maximum pressure is applied (or when a tablet isn’t
used)

Type:

    

float in [0, 100], default 1.0

radius_min¶

    

Minimum radius when the minimum pressure is applied (also the minimum when
tapering)

Type:

    

float in [0, 100], default 0.0

radius_taper_end¶

    

Taper factor for the radius of each point along the curve

Type:

    

float in [0, 10], default 0.0

radius_taper_start¶

    

Taper factor for the radius of each point along the curve

Type:

    

float in [0, 1], default 0.0

surface_offset¶

    

Offset the stroke from the surface

Type:

    

float in [-10, 10], default 0.0

surface_plane¶

    

Plane for projected stroke

  * `NORMAL_VIEW` Normal to Surface – Draw in a plane perpendicular to the surface.

  * `NORMAL_SURFACE` Tangent to Surface – Draw in the surface plane.

  * `VIEW` View – Draw in a plane aligned to the viewport.

Type:

    

enum in [`NORMAL_VIEW`, `NORMAL_SURFACE`, `VIEW`], default `NORMAL_VIEW`

use_corners_detect¶

    

Detect corners and use non-aligned handles

Type:

    

boolean, default True

use_offset_absolute¶

    

Apply a fixed offset (don’t scale by the radius)

Type:

    

boolean, default False

use_pressure_radius¶

    

Map tablet pressure to curve radius

Type:

    

boolean, default False

use_project_only_selected¶

    

Project the strokes only onto selected objects

Type:

    

boolean, default False

use_stroke_endpoints¶

    

Use the start of the stroke for the depth

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

  * [`ToolSettings.curve_paint_settings`](bpy.types.ToolSettings.html#bpy.types.ToolSettings.curve_paint_settings "bpy.types.ToolSettings.curve_paint_settings")

|

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

