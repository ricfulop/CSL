---
url: https://docs.blender.org/api/current/bpy.types.DynamicPaintSurface.html
scraped_at: 2025-09-08T14:24:45.025246
title: DynamicPaintSurface(bpy_struct)¶
---

# DynamicPaintSurface(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.DynamicPaintSurface(_bpy_struct_)¶

    

A canvas surface layer

brush_collection¶

    

Only use brush objects from this collection

Type:

    

[`Collection`](bpy.types.Collection.html#bpy.types.Collection
"bpy.types.Collection")

brush_influence_scale¶

    

Adjust influence brush objects have on this surface

Type:

    

float in [0, 1], default 0.0

brush_radius_scale¶

    

Adjust radius of proximity brushes or particles for this surface

Type:

    

float in [0, 10], default 0.0

color_dry_threshold¶

    

The wetness level when colors start to shift to the background

Type:

    

float in [0, 1], default 0.0

color_spread_speed¶

    

How fast colors get mixed within wet paint

Type:

    

float in [0, 2], default 0.0

depth_clamp¶

    

Maximum level of depth intersection in object space (use 0.0 to disable)

Type:

    

float in [0, 50], default 0.0

displace_factor¶

    

Strength of displace when applied to the mesh

Type:

    

float in [-50, 50], default 0.0

displace_type¶

    

Type:

    

enum in [`DISPLACE`, `DEPTH`], default `DISPLACE`

dissolve_speed¶

    

Approximately in how many frames should dissolve happen

Type:

    

int in [1, 10000], default 0

drip_acceleration¶

    

How much surface acceleration affects dripping

Type:

    

float in [-200, 200], default 0.0

drip_velocity¶

    

How much surface velocity affects dripping

Type:

    

float in [-200, 200], default 0.0

dry_speed¶

    

Approximately in how many frames should drying happen

Type:

    

int in [1, 10000], default 0

effect_ui¶

    

Type:

    

enum in [`SPREAD`, `DRIP`, `SHRINK`], default `SPREAD`

effector_weights¶

    

Type:

    

[`EffectorWeights`](bpy.types.EffectorWeights.html#bpy.types.EffectorWeights
"bpy.types.EffectorWeights"), (readonly)

frame_end¶

    

Simulation end frame

Type:

    

int in [1, 1048574], default 0

frame_start¶

    

Simulation start frame

Type:

    

int in [1, 1048574], default 0

frame_substeps¶

    

Do extra frames between scene frames to ensure smooth motion

Type:

    

int in [0, 20], default 0

image_fileformat¶

    

Type:

    

enum in [`PNG`, `OPENEXR`], default `PNG`

image_output_path¶

    

Directory to save the textures

Type:

    

string, default “”, (never None, blend relative `//` prefix supported)

image_resolution¶

    

Output image resolution

Type:

    

int in [16, 4096], default 0

init_color¶

    

Initial color of the surface

Type:

    

float array of 4 items in [0, inf], default (0.0, 0.0, 0.0, 0.0)

init_color_type¶

    

Type:

    

enum in [`NONE`, `COLOR`, `TEXTURE`, `VERTEX_COLOR`], default `NONE`

init_layername¶

    

Type:

    

string, default “”, (never None)

init_texture¶

    

Type:

    

[`Texture`](bpy.types.Texture.html#bpy.types.Texture "bpy.types.Texture")

is_active¶

    

Toggle whether surface is processed or ignored

Type:

    

boolean, default False

is_cache_user¶

    

Type:

    

boolean, default False, (readonly)

name¶

    

Surface name

Type:

    

string, default “”, (never None)

output_name_a¶

    

Name used to save output from this surface

Type:

    

string, default “”, (never None)

output_name_b¶

    

Name used to save output from this surface

Type:

    

string, default “”, (never None)

point_cache¶

    

Type:

    

[`PointCache`](bpy.types.PointCache.html#bpy.types.PointCache
"bpy.types.PointCache"), (readonly, never None)

shrink_speed¶

    

How fast shrink effect moves on the canvas surface

Type:

    

float in [0.001, 10], default 0.0

spread_speed¶

    

How fast spread effect moves on the canvas surface

Type:

    

float in [0.001, 10], default 0.0

surface_format¶

    

Surface Format

Type:

    

enum in [`VERTEX`, `IMAGE`], default `VERTEX`

surface_type¶

    

Surface Type

Type:

    

enum in [`PAINT`], default `PAINT`

use_antialiasing¶

    

Use 5× multisampling to smooth paint edges

Type:

    

boolean, default False

use_dissolve¶

    

Enable to make surface changes disappear over time

Type:

    

boolean, default False

use_dissolve_log¶

    

Use logarithmic dissolve (makes high values to fade faster than low values)

Type:

    

boolean, default False

use_drip¶

    

Process drip effect (drip wet paint to gravity direction)

Type:

    

boolean, default False

use_dry_log¶

    

Use logarithmic drying (makes high values to dry faster than low values)

Type:

    

boolean, default False

use_drying¶

    

Enable to make surface wetness dry over time

Type:

    

boolean, default False

use_incremental_displace¶

    

New displace is added cumulatively on top of existing

Type:

    

boolean, default False

use_output_a¶

    

Save this output layer

Type:

    

boolean, default False

use_output_b¶

    

Save this output layer

Type:

    

boolean, default False

use_premultiply¶

    

Multiply color by alpha (recommended for Blender input)

Type:

    

boolean, default False

use_shrink¶

    

Process shrink effect (shrink paint areas)

Type:

    

boolean, default False

use_spread¶

    

Process spread effect (spread wet paint around surface)

Type:

    

boolean, default False

use_wave_open_border¶

    

Pass waves through mesh edges

Type:

    

boolean, default False

uv_layer¶

    

UV map name

Type:

    

string, default “”, (never None)

wave_damping¶

    

Wave damping factor

Type:

    

float in [0, 1], default 0.0

wave_smoothness¶

    

Limit maximum steepness of wave slope between simulation points (use higher
values for smoother waves at expense of reduced detail)

Type:

    

float in [0, 10], default 0.0

wave_speed¶

    

Wave propagation speed

Type:

    

float in [0.01, 5], default 0.0

wave_spring¶

    

Spring force that pulls water level back to zero

Type:

    

float in [0, 1], default 0.0

wave_timescale¶

    

Wave time scaling factor

Type:

    

float in [0.01, 3], default 0.0

output_exists(_object_ , _index_)¶

    

Checks if surface output layer of given name exists

Parameters:

    

**index** (_int in_ _[__0_ _,__1_ _]_) – Index

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

  * [`DynamicPaintCanvasSettings.canvas_surfaces`](bpy.types.DynamicPaintCanvasSettings.html#bpy.types.DynamicPaintCanvasSettings.canvas_surfaces "bpy.types.DynamicPaintCanvasSettings.canvas_surfaces")

|

  * [`DynamicPaintSurfaces.active`](bpy.types.DynamicPaintSurfaces.html#bpy.types.DynamicPaintSurfaces.active "bpy.types.DynamicPaintSurfaces.active")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

