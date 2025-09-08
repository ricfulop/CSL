---
url: https://docs.blender.org/api/current/bpy.types.DynamicPaintBrushSettings.html
scraped_at: 2025-09-08T14:24:41.994983
title: DynamicPaintBrushSettings(bpy_struct)¶
---

# DynamicPaintBrushSettings(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.DynamicPaintBrushSettings(_bpy_struct_)¶

    

Brush settings

invert_proximity¶

    

Proximity falloff is applied inside the volume

Type:

    

boolean, default False

paint_alpha¶

    

Paint alpha

Type:

    

float in [0, 1], default 0.0

paint_color¶

    

Color of the paint

Type:

    

[`mathutils.Color`](mathutils.html#mathutils.Color "mathutils.Color") of 3
items in [0, inf], default (0.0, 0.0, 0.0)

paint_distance¶

    

Maximum distance from brush to mesh surface to affect paint

Type:

    

float in [0, 500], default 0.0

paint_ramp¶

    

Color ramp used to define proximity falloff

Type:

    

[`ColorRamp`](bpy.types.ColorRamp.html#bpy.types.ColorRamp
"bpy.types.ColorRamp"), (readonly)

paint_source¶

    

Type:

    

enum in [`PARTICLE_SYSTEM`, `POINT`, `DISTANCE`, `VOLUME_DISTANCE`, `VOLUME`],
default `VOLUME`

paint_wetness¶

    

Paint wetness, visible in wetmap (some effects only affect wet paint)

Type:

    

float in [0, 1], default 0.0

particle_system¶

    

The particle system to paint with

Type:

    

[`ParticleSystem`](bpy.types.ParticleSystem.html#bpy.types.ParticleSystem
"bpy.types.ParticleSystem")

proximity_falloff¶

    

Proximity falloff type

Type:

    

enum in [`SMOOTH`, `CONSTANT`, `RAMP`], default `CONSTANT`

ray_direction¶

    

Ray direction to use for projection (if brush object is located in that
direction it’s painted)

Type:

    

enum in [`CANVAS`, `BRUSH`, `Z_AXIS`], default `CANVAS`

smooth_radius¶

    

Smooth falloff added after solid radius

Type:

    

float in [0, 10], default 0.0

smudge_strength¶

    

Smudge effect strength

Type:

    

float in [0, 1], default 0.0

solid_radius¶

    

Radius that will be painted solid

Type:

    

float in [0.01, 10], default 0.0

use_absolute_alpha¶

    

Only increase alpha value if paint alpha is higher than existing

Type:

    

boolean, default False

use_negative_volume¶

    

Negate influence inside the volume

Type:

    

boolean, default False

use_paint_erase¶

    

Erase / remove paint instead of adding it

Type:

    

boolean, default False

use_particle_radius¶

    

Use radius from particle settings

Type:

    

boolean, default False

use_proximity_project¶

    

Brush is projected to canvas from defined direction within brush proximity

Type:

    

boolean, default False

use_proximity_ramp_alpha¶

    

Only read color ramp alpha

Type:

    

boolean, default False

use_smudge¶

    

Make this brush to smudge existing paint as it moves

Type:

    

boolean, default False

use_velocity_alpha¶

    

Multiply brush influence by velocity color ramp alpha

Type:

    

boolean, default False

use_velocity_color¶

    

Replace brush color by velocity color ramp

Type:

    

boolean, default False

use_velocity_depth¶

    

Multiply brush intersection depth (displace, waves) by velocity ramp alpha

Type:

    

boolean, default False

velocity_max¶

    

Velocity considered as maximum influence (Blender units per frame)

Type:

    

float in [0.0001, 10], default 0.0

velocity_ramp¶

    

Color ramp used to define brush velocity effect

Type:

    

[`ColorRamp`](bpy.types.ColorRamp.html#bpy.types.ColorRamp
"bpy.types.ColorRamp"), (readonly)

wave_clamp¶

    

Maximum level of surface intersection used to influence waves (use 0.0 to
disable)

Type:

    

float in [0, 50], default 0.0

wave_factor¶

    

Multiplier for wave influence of this brush

Type:

    

float in [-2, 2], default 0.0

wave_type¶

    

Type:

    

enum in [`CHANGE`, `DEPTH`, `FORCE`, `REFLECT`], default `DEPTH`

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

  * [`DynamicPaintModifier.brush_settings`](bpy.types.DynamicPaintModifier.html#bpy.types.DynamicPaintModifier.brush_settings "bpy.types.DynamicPaintModifier.brush_settings")

|

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

