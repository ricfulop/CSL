---
url: https://docs.blender.org/api/current/bpy.types.BrushCurvesSculptSettings.html
scraped_at: 2025-09-08T14:21:19.187626
title: BrushCurvesSculptSettings(bpy_struct)¶
---

# BrushCurvesSculptSettings(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.BrushCurvesSculptSettings(_bpy_struct_)¶

    

add_amount¶

    

Number of curves added by the Add brush

Type:

    

int in [1, inf], default 0

curve_length¶

    

Length of newly added curves when it is not interpolated from other curves

Type:

    

float in [0, inf], default 0.0

curve_parameter_falloff¶

    

Falloff that is applied from the tip to the root of each curve

Type:

    

[`CurveMapping`](bpy.types.CurveMapping.html#bpy.types.CurveMapping
"bpy.types.CurveMapping"), (readonly)

curve_radius¶

    

Radius of newly added curves when it is not interpolated from other curves

Type:

    

float in [0, inf], default 0.01

density_add_attempts¶

    

How many times the Density brush tries to add a new curve

Type:

    

int in [0, inf], default 0

density_mode¶

    

Determines whether the brush adds or removes curves

  * `AUTO` Auto – Either add or remove curves depending on the minimum distance of the curves under the cursor.

  * `ADD` Add – Add new curves between existing curves, taking the minimum distance into account.

  * `REMOVE` Remove – Remove curves whose root points are too close.

Type:

    

enum in [`AUTO`, `ADD`, `REMOVE`], default `AUTO`

minimum_distance¶

    

Goal distance between curve roots for the Density brush

Type:

    

float in [0, inf], default 0.0

minimum_length¶

    

Avoid shrinking curves shorter than this length

Type:

    

float in [0, inf], default 0.0

points_per_curve¶

    

Number of control points in a newly added curve

Type:

    

int in [2, inf], default 0

use_length_interpolate¶

    

Use length of the curves in close proximity

Type:

    

boolean, default False

use_point_count_interpolate¶

    

Use the number of points from the curves in close proximity

Type:

    

boolean, default False

use_radius_interpolate¶

    

Use radius of the curves in close proximity

Type:

    

boolean, default True

use_shape_interpolate¶

    

Use shape of the curves in close proximity

Type:

    

boolean, default False

use_uniform_scale¶

    

Grow or shrink curves by changing their size uniformly instead of using
trimming or extrapolation

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

  * [`Brush.curves_sculpt_settings`](bpy.types.Brush.html#bpy.types.Brush.curves_sculpt_settings "bpy.types.Brush.curves_sculpt_settings")

|

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

