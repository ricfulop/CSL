---
url: https://docs.blender.org/api/current/bpy.types.CollisionSettings.html
scraped_at: 2025-09-08T14:21:59.335054
title: CollisionSettings(bpy_struct)¶
---

# CollisionSettings(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.CollisionSettings(_bpy_struct_)¶

    

Collision settings for object in physics simulation

absorption¶

    

How much of effector force gets lost during collision with this object (in
percent)

Type:

    

float in [0, 1], default 0.0

cloth_friction¶

    

Friction for cloth collisions

Type:

    

float in [0, 80], default 0.0

damping¶

    

Amount of damping during collision

Type:

    

float in [0, 1], default 0.0

damping_factor¶

    

Amount of damping during particle collision

Type:

    

float in [0, 1], default 0.0

damping_random¶

    

Random variation of damping

Type:

    

float in [0, 1], default 0.0

friction_factor¶

    

Amount of friction during particle collision

Type:

    

float in [0, 1], default 0.0

friction_random¶

    

Random variation of friction

Type:

    

float in [0, 1], default 0.0

permeability¶

    

Chance that the particle will pass through the mesh

Type:

    

float in [0, 1], default 0.0

stickiness¶

    

Amount of stickiness to surface collision

Type:

    

float in [0, 10], default 0.0

thickness_inner¶

    

Inner face thickness (only used by softbodies)

Type:

    

float in [0.001, 1], default 0.0

thickness_outer¶

    

Outer face thickness

Type:

    

float in [0.001, 1], default 0.0

use¶

    

Enable this object as a collider for physics systems

Type:

    

boolean, default False

use_culling¶

    

Cloth collision acts with respect to the collider normals (improves
penetration recovery)

Type:

    

boolean, default False

use_normal¶

    

Cloth collision impulses act in the direction of the collider normals (more
reliable in some cases)

Type:

    

boolean, default False

use_particle_kill¶

    

Kill collided particles

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

  * [`CollisionModifier.settings`](bpy.types.CollisionModifier.html#bpy.types.CollisionModifier.settings "bpy.types.CollisionModifier.settings")

|

  * [`Object.collision`](bpy.types.Object.html#bpy.types.Object.collision "bpy.types.Object.collision")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

