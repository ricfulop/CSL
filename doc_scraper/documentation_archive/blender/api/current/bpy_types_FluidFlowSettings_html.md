---
url: https://docs.blender.org/api/current/bpy.types.FluidFlowSettings.html
scraped_at: 2025-09-08T14:25:36.223301
title: FluidFlowSettings(bpy_struct)¶
---

# FluidFlowSettings(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.FluidFlowSettings(_bpy_struct_)¶

    

Fluid flow settings

density¶

    

Type:

    

float in [0, 10], default 1.0

density_vertex_group¶

    

Name of vertex group which determines surface emission rate

Type:

    

string, default “”, (never None)

flow_behavior¶

    

Change flow behavior in the simulation

  * `INFLOW` Inflow – Add fluid to simulation.

  * `OUTFLOW` Outflow – Delete fluid from simulation.

  * `GEOMETRY` Geometry – Only use given geometry for fluid.

Type:

    

enum in [`INFLOW`, `OUTFLOW`, `GEOMETRY`], default `GEOMETRY`

flow_source¶

    

Change how fluid is emitted

Type:

    

enum in [`NONE`], default `NONE`

flow_type¶

    

Change type of fluid in the simulation

  * `SMOKE` Smoke – Add smoke.

  * `BOTH` Fire + Smoke – Add fire and smoke.

  * `FIRE` Fire – Add fire.

  * `LIQUID` Liquid – Add liquid.

Type:

    

enum in [`SMOKE`, `BOTH`, `FIRE`, `LIQUID`], default `SMOKE`

fuel_amount¶

    

Type:

    

float in [0, 10], default 1.0

noise_texture¶

    

Texture that controls emission strength

Type:

    

[`Texture`](bpy.types.Texture.html#bpy.types.Texture "bpy.types.Texture")

particle_size¶

    

Particle size in simulation cells

Type:

    

float in [0.1, inf], default 1.0

particle_system¶

    

Particle systems emitted from the object

Type:

    

[`ParticleSystem`](bpy.types.ParticleSystem.html#bpy.types.ParticleSystem
"bpy.types.ParticleSystem")

smoke_color¶

    

Color of smoke

Type:

    

[`mathutils.Color`](mathutils.html#mathutils.Color "mathutils.Color") of 3
items in [0, inf], default (0.7, 0.7, 0.7)

subframes¶

    

Number of additional samples to take between frames to improve quality of fast
moving flows

Type:

    

int in [0, 200], default 0

surface_distance¶

    

Height (in domain grid units) of fluid emission above the mesh surface. Higher
values result in emission further away from the mesh surface. If this value
and the emitter size are smaller than the domain grid unit, fluid will not be
created

Type:

    

float in [0, 10], default 1.0

temperature¶

    

Temperature difference to ambient temperature

Type:

    

float in [-10, 10], default 1.0

texture_map_type¶

    

Texture mapping type

  * `AUTO` Generated – Generated coordinates centered to flow object.

  * `UV` UV – Use UV layer for texture coordinates.

Type:

    

enum in [`AUTO`, `UV`], default `AUTO`

texture_offset¶

    

Z-offset of texture mapping

Type:

    

float in [0, 200], default 0.0

texture_size¶

    

Size of texture mapping

Type:

    

float in [0.01, 10], default 1.0

use_absolute¶

    

Only allow given density value in emitter area and will not add up

Type:

    

boolean, default True

use_inflow¶

    

Control when to apply fluid flow

Type:

    

boolean, default True

use_initial_velocity¶

    

Fluid has some initial velocity when it is emitted

Type:

    

boolean, default False

use_particle_size¶

    

Set particle size in simulation cells or use nearest cell

Type:

    

boolean, default True

use_plane_init¶

    

Treat this object as a planar and unclosed mesh. Fluid will only be emitted
from the mesh surface and based on the surface emission value.

Type:

    

boolean, default False

use_texture¶

    

Use a texture to control emission strength

Type:

    

boolean, default False

uv_layer¶

    

UV map name

Type:

    

string, default “”, (never None)

velocity_coord¶

    

Additional initial velocity in X, Y and Z direction (added to source velocity)

Type:

    

[`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3
items in [-1000.1, 1000.1], default (0.0, 0.0, 0.0)

velocity_factor¶

    

Multiplier of source velocity passed to fluid (source velocity is non-zero
only if object is moving)

Type:

    

float in [-100, 100], default 1.0

velocity_normal¶

    

Amount of normal directional velocity

Type:

    

float in [-100, 100], default 0.0

velocity_random¶

    

Amount of random velocity

Type:

    

float in [0, 10], default 0.0

volume_density¶

    

Controls fluid emission from within the mesh (higher value results in greater
emissions from inside the mesh)

Type:

    

float in [0, 1], default 0.0

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

  * [`FluidModifier.flow_settings`](bpy.types.FluidModifier.html#bpy.types.FluidModifier.flow_settings "bpy.types.FluidModifier.flow_settings")

|

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

