---
url: https://docs.blender.org/api/current/bpy.types.EffectorWeights.html
scraped_at: 2025-09-08T14:24:51.078128
title: EffectorWeights(bpy_struct)¶
---

# EffectorWeights(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.EffectorWeights(_bpy_struct_)¶

    

Effector weights for physics simulation

all¶

    

All effector’s weight

Type:

    

float in [-200, 200], default 0.0

apply_to_hair_growing¶

    

Use force fields when growing hair

Type:

    

boolean, default False

boid¶

    

Boid effector weight

Type:

    

float in [-200, 200], default 0.0

charge¶

    

Charge effector weight

Type:

    

float in [-200, 200], default 0.0

collection¶

    

Limit effectors to this collection

Type:

    

[`Collection`](bpy.types.Collection.html#bpy.types.Collection
"bpy.types.Collection")

curve_guide¶

    

Curve guide effector weight

Type:

    

float in [-200, 200], default 0.0

drag¶

    

Drag effector weight

Type:

    

float in [-200, 200], default 0.0

force¶

    

Force effector weight

Type:

    

float in [-200, 200], default 0.0

gravity¶

    

Global gravity weight

Type:

    

float in [-200, 200], default 0.0

harmonic¶

    

Harmonic effector weight

Type:

    

float in [-200, 200], default 0.0

lennardjones¶

    

Lennard-Jones effector weight

Type:

    

float in [-200, 200], default 0.0

magnetic¶

    

Magnetic effector weight

Type:

    

float in [-200, 200], default 0.0

smokeflow¶

    

Fluid Flow effector weight

Type:

    

float in [-200, 200], default 0.0

texture¶

    

Texture effector weight

Type:

    

float in [-200, 200], default 0.0

turbulence¶

    

Turbulence effector weight

Type:

    

float in [-200, 200], default 0.0

vortex¶

    

Vortex effector weight

Type:

    

float in [-200, 200], default 0.0

wind¶

    

Wind effector weight

Type:

    

float in [-200, 200], default 0.0

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

  * [`ClothSettings.effector_weights`](bpy.types.ClothSettings.html#bpy.types.ClothSettings.effector_weights "bpy.types.ClothSettings.effector_weights")
  * [`DynamicPaintSurface.effector_weights`](bpy.types.DynamicPaintSurface.html#bpy.types.DynamicPaintSurface.effector_weights "bpy.types.DynamicPaintSurface.effector_weights")
  * [`FluidDomainSettings.effector_weights`](bpy.types.FluidDomainSettings.html#bpy.types.FluidDomainSettings.effector_weights "bpy.types.FluidDomainSettings.effector_weights")

|

  * [`ParticleSettings.effector_weights`](bpy.types.ParticleSettings.html#bpy.types.ParticleSettings.effector_weights "bpy.types.ParticleSettings.effector_weights")
  * [`RigidBodyWorld.effector_weights`](bpy.types.RigidBodyWorld.html#bpy.types.RigidBodyWorld.effector_weights "bpy.types.RigidBodyWorld.effector_weights")
  * [`SoftBodySettings.effector_weights`](bpy.types.SoftBodySettings.html#bpy.types.SoftBodySettings.effector_weights "bpy.types.SoftBodySettings.effector_weights")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

