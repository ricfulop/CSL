---
url: https://docs.blender.org/api/current/bpy.types.BoidSettings.html
scraped_at: 2025-09-08T14:21:01.111658
title: BoidSettings(bpy_struct)¶
---

# BoidSettings(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.BoidSettings(_bpy_struct_)¶

    

Settings for boid physics

accuracy¶

    

Accuracy of attack

Type:

    

float in [0, 1], default 0.0

active_boid_state¶

    

Type:

    

[`BoidRule`](bpy.types.BoidRule.html#bpy.types.BoidRule "bpy.types.BoidRule"),
(readonly)

active_boid_state_index¶

    

Type:

    

int in [0, inf], default 0

aggression¶

    

Boid will fight this times stronger enemy

Type:

    

float in [0, 100], default 0.0

air_acc_max¶

    

Maximum acceleration in air (relative to maximum speed)

Type:

    

float in [0, 1], default 0.0

air_ave_max¶

    

Maximum angular velocity in air (relative to 180 degrees)

Type:

    

float in [0, 1], default 0.0

air_personal_space¶

    

Radius of boids personal space in air (% of particle size)

Type:

    

float in [0, 10], default 0.0

air_speed_max¶

    

Maximum speed in air

Type:

    

float in [0, 100], default 0.0

air_speed_min¶

    

Minimum speed in air (relative to maximum speed)

Type:

    

float in [0, 1], default 0.0

bank¶

    

Amount of rotation around velocity vector on turns

Type:

    

float in [0, 2], default 0.0

health¶

    

Initial boid health when born

Type:

    

float in [0, 100], default 0.0

height¶

    

Boid height relative to particle size

Type:

    

float in [0, 2], default 0.0

land_acc_max¶

    

Maximum acceleration on land (relative to maximum speed)

Type:

    

float in [0, 1], default 0.0

land_ave_max¶

    

Maximum angular velocity on land (relative to 180 degrees)

Type:

    

float in [0, 1], default 0.0

land_jump_speed¶

    

Maximum speed for jumping

Type:

    

float in [0, 100], default 0.0

land_personal_space¶

    

Radius of boids personal space on land (% of particle size)

Type:

    

float in [0, 10], default 0.0

land_smooth¶

    

How smoothly the boids land

Type:

    

float in [0, 10], default 0.0

land_speed_max¶

    

Maximum speed on land

Type:

    

float in [0, 100], default 0.0

land_stick_force¶

    

How strong a force must be to start effecting a boid on land

Type:

    

float in [0, 1000], default 0.0

pitch¶

    

Amount of rotation around side vector

Type:

    

float in [0, 2], default 0.0

range¶

    

Maximum distance from which a boid can attack

Type:

    

float in [0, 100], default 0.0

states¶

    

Type:

    

[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`BoidState`](bpy.types.BoidState.html#bpy.types.BoidState
"bpy.types.BoidState"), (readonly)

strength¶

    

Maximum caused damage on attack per second

Type:

    

float in [0, 100], default 0.0

use_climb¶

    

Allow boids to climb goal objects

Type:

    

boolean, default False

use_flight¶

    

Allow boids to move in air

Type:

    

boolean, default False

use_land¶

    

Allow boids to move on land

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

  * [`ParticleSettings.boids`](bpy.types.ParticleSettings.html#bpy.types.ParticleSettings.boids "bpy.types.ParticleSettings.boids")

|

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

