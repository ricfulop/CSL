---
url: https://docs.blender.org/api/current/bpy.types.ClothSettings.html
scraped_at: 2025-09-08T14:21:47.300415
title: ClothSettings(bpy_struct)¶
---

# ClothSettings(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.ClothSettings(_bpy_struct_)¶

    

Cloth simulation settings for an object

air_damping¶

    

Air has normally some thickness which slows falling things down

Type:

    

float in [0, 10], default 1.0

bending_damping¶

    

Amount of damping in bending behavior

Type:

    

float in [0, 1000], default 0.5

bending_model¶

    

Physical model for simulating bending forces

  * `ANGULAR` Angular – Cloth model with angular bending springs.

  * `LINEAR` Linear – Cloth model with linear bending springs (legacy).

Type:

    

enum in [`ANGULAR`, `LINEAR`], default `ANGULAR`

bending_stiffness¶

    

How much the material resists bending

Type:

    

float in [0, 10000], default 0.5

bending_stiffness_max¶

    

Maximum bending stiffness value

Type:

    

float in [0, 10000], default 0.5

collider_friction¶

    

Type:

    

float in [0, 1], default 0.0

compression_damping¶

    

Amount of damping in compression behavior

Type:

    

float in [0, 50], default 5.0

compression_stiffness¶

    

How much the material resists compression

Type:

    

float in [0, 10000], default 15.0

compression_stiffness_max¶

    

Maximum compression stiffness value

Type:

    

float in [0, 10000], default 15.0

density_strength¶

    

Influence of target density on the simulation

Type:

    

float in [0, 1], default 0.0

density_target¶

    

Maximum density of hair

Type:

    

float in [0, 10000], default 0.0

effector_weights¶

    

Type:

    

[`EffectorWeights`](bpy.types.EffectorWeights.html#bpy.types.EffectorWeights
"bpy.types.EffectorWeights"), (readonly)

fluid_density¶

    

Density (kg/l) of the fluid contained inside the object, used to create a
hydrostatic pressure gradient simulating the weight of the internal fluid, or
buoyancy from the surrounding fluid if negative

Type:

    

float in [-inf, inf], default 0.0

goal_default¶

    

Default Goal (vertex target position) value, when no Vertex Group used

Type:

    

float in [0, 1], default 0.0

goal_friction¶

    

Goal (vertex target position) friction

Type:

    

float in [0, 50], default 0.0

goal_max¶

    

Goal maximum, vertex group weights are scaled to match this range

Type:

    

float in [0, 1], default 1.0

goal_min¶

    

Goal minimum, vertex group weights are scaled to match this range

Type:

    

float in [0, 1], default 0.0

goal_spring¶

    

Goal (vertex target position) spring stiffness

Type:

    

float in [0, 0.999], default 1.0

gravity¶

    

Gravity or external force vector

Type:

    

[`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3
items in [-100, 100], default (0.0, 0.0, -9.81)

internal_compression_stiffness¶

    

How much the material resists compression

Type:

    

float in [0, 10000], default 15.0

internal_compression_stiffness_max¶

    

Maximum compression stiffness value

Type:

    

float in [0, 10000], default 15.0

internal_friction¶

    

Type:

    

float in [0, 1], default 0.0

internal_spring_max_diversion¶

    

How much the rays used to connect the internal points can diverge from the
vertex normal

Type:

    

float in [0, 0.785398], default 0.785398

internal_spring_max_length¶

    

The maximum length an internal spring can have during creation. If the
distance between internal points is greater than this, no internal spring will
be created between these points. A length of zero means that there is no
length limit.

Type:

    

float in [0, 1000], default 0.0

internal_spring_normal_check¶

    

Require the points the internal springs connect to have opposite normal
directions

Type:

    

boolean, default True

internal_tension_stiffness¶

    

How much the material resists stretching

Type:

    

float in [0, 10000], default 15.0

internal_tension_stiffness_max¶

    

Maximum tension stiffness value

Type:

    

float in [0, 10000], default 15.0

mass¶

    

The mass of each vertex on the cloth material

Type:

    

float in [0, inf], default 0.3

pin_stiffness¶

    

Pin (vertex target position) spring stiffness

Type:

    

float in [0, 50], default 1.0

pressure_factor¶

    

Ambient pressure (kPa) that balances out between the inside and outside of the
object when it has the target volume

Type:

    

float in [0, 10000], default 1.0

quality¶

    

Quality of the simulation in steps per frame (higher is better quality but
slower)

Type:

    

int in [1, inf], default 5

rest_shape_key¶

    

Shape key to use the rest spring lengths from

Type:

    

[`ShapeKey`](bpy.types.ShapeKey.html#bpy.types.ShapeKey "bpy.types.ShapeKey")

sewing_force_max¶

    

Maximum sewing force

Type:

    

float in [0, 10000], default 0.0

shear_damping¶

    

Amount of damping in shearing behavior

Type:

    

float in [0, 50], default 5.0

shear_stiffness¶

    

How much the material resists shearing

Type:

    

float in [0, 10000], default 5.0

shear_stiffness_max¶

    

Maximum shear scaling value

Type:

    

float in [0, 10000], default 5.0

shrink_max¶

    

Max amount to shrink cloth by

Type:

    

float in [-inf, 1], default 0.0

shrink_min¶

    

Factor by which to shrink cloth

Type:

    

float in [-inf, 1], default 0.0

target_volume¶

    

The mesh volume where the inner/outer pressure will be the same. If set to
zero the change in volume will not affect pressure.

Type:

    

float in [0, 10000], default 0.0

tension_damping¶

    

Amount of damping in stretching behavior

Type:

    

float in [0, 50], default 5.0

tension_stiffness¶

    

How much the material resists stretching

Type:

    

float in [0, 10000], default 15.0

tension_stiffness_max¶

    

Maximum tension stiffness value

Type:

    

float in [0, 10000], default 15.0

time_scale¶

    

Cloth speed is multiplied by this value

Type:

    

float in [0, inf], default 1.0

uniform_pressure_force¶

    

The uniform pressure that is constantly applied to the mesh, in units of
Pressure Scale. Can be negative.

Type:

    

float in [-10000, 10000], default 0.0

use_dynamic_mesh¶

    

Make simulation respect deformations in the base mesh

Type:

    

boolean, default False

use_internal_springs¶

    

Simulate an internal volume structure by creating springs connecting the
opposite sides of the mesh

Type:

    

boolean, default False

use_pressure¶

    

Simulate pressure inside a closed cloth mesh

Type:

    

boolean, default False

use_pressure_volume¶

    

Use the Target Volume parameter as the initial volume, instead of calculating
it from the mesh itself

Type:

    

boolean, default False

use_sewing_springs¶

    

Pulls loose edges together

Type:

    

boolean, default False

vertex_group_bending¶

    

Vertex group for fine control over bending stiffness

Type:

    

string, default “”, (never None)

vertex_group_intern¶

    

Vertex group for fine control over the internal spring stiffness

Type:

    

string, default “”, (never None)

vertex_group_mass¶

    

Vertex Group for pinning of vertices

Type:

    

string, default “”, (never None)

vertex_group_pressure¶

    

Vertex Group for where to apply pressure. Zero weight means no pressure while
a weight of one means full pressure. Faces with a vertex that has zero weight
will be excluded from the volume calculation.

Type:

    

string, default “”, (never None)

vertex_group_shear_stiffness¶

    

Vertex group for fine control over shear stiffness

Type:

    

string, default “”, (never None)

vertex_group_shrink¶

    

Vertex Group for shrinking cloth

Type:

    

string, default “”, (never None)

vertex_group_structural_stiffness¶

    

Vertex group for fine control over structural stiffness

Type:

    

string, default “”, (never None)

voxel_cell_size¶

    

Size of the voxel grid cells for interaction effects

Type:

    

float in [0.0001, 10000], default 0.1

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

  * [`ClothModifier.settings`](bpy.types.ClothModifier.html#bpy.types.ClothModifier.settings "bpy.types.ClothModifier.settings")

|

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

