---
url: https://docs.blender.org/api/current/bpy.types.FieldSettings.html
scraped_at: 2025-09-08T14:25:13.128817
title: FieldSettings(bpy_struct)¶
---

# FieldSettings(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.FieldSettings(_bpy_struct_)¶

    

Field settings for an object in physics simulation

apply_to_location¶

    

Affect particle’s location

Type:

    

boolean, default False

apply_to_rotation¶

    

Affect particle’s dynamic rotation

Type:

    

boolean, default False

distance_max¶

    

Maximum distance for the field to work

Type:

    

float in [0, inf], default 0.0

distance_min¶

    

Minimum distance for the field’s falloff

Type:

    

float in [0, 1000], default 0.0

falloff_power¶

    

How quickly strength falls off with distance from the force field

Type:

    

float in [0, 10], default 0.0

falloff_type¶

    

Type:

    

enum in [`CONE`, `SPHERE`, `TUBE`], default `SPHERE`

flow¶

    

Convert effector force into air flow velocity

Type:

    

float in [-inf, inf], default 0.0

guide_clump_amount¶

    

Amount of clumping

Type:

    

float in [-1, 1], default 0.0

guide_clump_shape¶

    

Shape of clumping

Type:

    

float in [-0.999, 0.999], default 0.0

guide_free¶

    

Guide-free time from particle life’s end

Type:

    

float in [0, 0.99], default 0.0

guide_kink_amplitude¶

    

The amplitude of the offset

Type:

    

float in [0, 10], default 0.0

guide_kink_axis¶

    

Which axis to use for offset

Type:

    

enum in [Axis Xyz Items](bpy_types_enum_items/axis_xyz_items.html#rna-enum-
axis-xyz-items), default `X`

guide_kink_frequency¶

    

The frequency of the offset (1/total length)

Type:

    

float in [0, 10], default 0.0

guide_kink_shape¶

    

Adjust the offset to the beginning/end

Type:

    

float in [-0.999, 0.999], default 0.0

guide_kink_type¶

    

Type of periodic offset on the curve

Type:

    

enum in [`NONE`, `BRAID`, `CURL`, `RADIAL`, `ROLL`, `ROTATION`, `WAVE`],
default `NONE`

guide_minimum¶

    

The distance from which particles are affected fully

Type:

    

float in [-inf, inf], default 0.0

harmonic_damping¶

    

Damping of the harmonic force

Type:

    

float in [-inf, inf], default 0.0

inflow¶

    

Inwards component of the vortex force

Type:

    

float in [-inf, inf], default 0.0

linear_drag¶

    

Drag component proportional to velocity

Type:

    

float in [-inf, inf], default 0.0

noise¶

    

Amount of noise for the force strength

Type:

    

float in [0, 10], default 0.0

quadratic_drag¶

    

Drag component proportional to the square of velocity

Type:

    

float in [-inf, inf], default 0.0

radial_falloff¶

    

Radial falloff power (real gravitational falloff = 2)

Type:

    

float in [0, 10], default 0.0

radial_max¶

    

Maximum radial distance for the field to work

Type:

    

float in [0, 1000], default 0.0

radial_min¶

    

Minimum radial distance for the field’s falloff

Type:

    

float in [0, 1000], default 0.0

rest_length¶

    

Rest length of the harmonic force

Type:

    

float in [0, inf], default 0.0

seed¶

    

Seed of the noise

Type:

    

int in [1, 128], default 0

shape¶

    

Which direction is used to calculate the effector force

  * `POINT` Point – Field originates from the object center.

  * `LINE` Line – Field originates from the local Z axis of the object.

  * `PLANE` Plane – Field originates from the local XY plane of the object.

  * `SURFACE` Surface – Field originates from the surface of the object.

  * `POINTS` Every Point – Field originates from all of the vertices of the object.

Type:

    

enum in [`POINT`, `LINE`, `PLANE`, `SURFACE`, `POINTS`], default `POINT`

size¶

    

Size of the turbulence

Type:

    

float in [0, inf], default 0.0

source_object¶

    

Select domain object of the smoke simulation

Type:

    

[`Object`](bpy.types.Object.html#bpy.types.Object "bpy.types.Object")

strength¶

    

Strength of force field

Type:

    

float in [-inf, inf], default 0.0

texture¶

    

Texture to use as force

Type:

    

[`Texture`](bpy.types.Texture.html#bpy.types.Texture "bpy.types.Texture")

texture_mode¶

    

How the texture effect is calculated (RGB and Curl need a RGB texture, else
Gradient will be used instead)

Type:

    

enum in [`CURL`, `GRADIENT`, `RGB`], default `RGB`

texture_nabla¶

    

Defines size of derivative offset used for calculating gradient and curl

Type:

    

float in [0.0001, 1], default 0.0

type¶

    

Type of field

  * `NONE` None.

  * `BOID` Boid – Create a force that acts as a boid’s predators or target.

  * `CHARGE` Charge – Spherical forcefield based on the charge of particles, only influences other charge force fields.

  * `GUIDE` Curve Guide – Create a force along a curve object.

  * `DRAG` Drag – Create a force that dampens motion.

  * `FLUID_FLOW` Fluid Flow – Create a force based on fluid simulation velocities.

  * `FORCE` Force – Radial field toward the center of object.

  * `HARMONIC` Harmonic – The source of this force field is the zero point of a harmonic oscillator.

  * `LENNARDJ` Lennard-Jones – Forcefield based on the Lennard-Jones potential.

  * `MAGNET` Magnetic – Forcefield depends on the speed of the particles.

  * `TEXTURE` Texture – Force field based on a texture.

  * `TURBULENCE` Turbulence – Create turbulence with a noise field.

  * `VORTEX` Vortex – Spiraling force that twists the force object’s local Z axis.

  * `WIND` Wind – Constant force along the force object’s local Z axis.

Type:

    

enum in [`NONE`, `BOID`, `CHARGE`, `GUIDE`, `DRAG`, `FLUID_FLOW`, `FORCE`,
`HARMONIC`, `LENNARDJ`, `MAGNET`, `TEXTURE`, `TURBULENCE`, `VORTEX`, `WIND`],
default `NONE`

use_2d_force¶

    

Apply force only in 2D

Type:

    

boolean, default False

use_absorption¶

    

Force gets absorbed by collision objects

Type:

    

boolean, default False

use_global_coords¶

    

Use effector/global coordinates for turbulence

Type:

    

boolean, default False

use_gravity_falloff¶

    

Multiply force by 1/distance²

Type:

    

boolean, default False

use_guide_path_add¶

    

Based on distance/falloff it adds a portion of the entire path

Type:

    

boolean, default False

use_guide_path_weight¶

    

Use curve weights to influence the particle influence along the curve

Type:

    

boolean, default False

use_max_distance¶

    

Use a maximum distance for the field to work

Type:

    

boolean, default False

use_min_distance¶

    

Use a minimum distance for the field’s falloff

Type:

    

boolean, default False

use_multiple_springs¶

    

Every point is affected by multiple springs

Type:

    

boolean, default False

use_object_coords¶

    

Use object/global coordinates for texture

Type:

    

boolean, default False

use_radial_max¶

    

Use a maximum radial distance for the field to work

Type:

    

boolean, default False

use_radial_min¶

    

Use a minimum radial distance for the field’s falloff

Type:

    

boolean, default False

use_root_coords¶

    

Texture coordinates from root particle locations

Type:

    

boolean, default False

use_smoke_density¶

    

Adjust force strength based on smoke density

Type:

    

boolean, default False

wind_factor¶

    

How much the force is reduced when acting parallel to a surface, e.g. cloth

Type:

    

float in [0, 1], default 0.0

z_direction¶

    

Effect in full or only positive/negative Z direction

Type:

    

enum in [`POSITIVE`, `NEGATIVE`, `BOTH`], default `BOTH`

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

  * [`Object.field`](bpy.types.Object.html#bpy.types.Object.field "bpy.types.Object.field")
  * [`ParticleSettings.force_field_1`](bpy.types.ParticleSettings.html#bpy.types.ParticleSettings.force_field_1 "bpy.types.ParticleSettings.force_field_1")

|

  * [`ParticleSettings.force_field_2`](bpy.types.ParticleSettings.html#bpy.types.ParticleSettings.force_field_2 "bpy.types.ParticleSettings.force_field_2")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

