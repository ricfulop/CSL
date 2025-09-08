---
url: https://docs.blender.org/api/current/bpy.types.Bone.html
scraped_at: 2025-09-08T14:21:03.203066
title: Bone(bpy_struct)¶
---

# Bone(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.Bone(_bpy_struct_)¶

    

Bone in an Armature data-block

bbone_curveinx¶

    

X-axis handle offset for start of the B-Bone’s curve, adjusts curvature

Type:

    

float in [-inf, inf], default 0.0

bbone_curveinz¶

    

Z-axis handle offset for start of the B-Bone’s curve, adjusts curvature

Type:

    

float in [-inf, inf], default 0.0

bbone_curveoutx¶

    

X-axis handle offset for end of the B-Bone’s curve, adjusts curvature

Type:

    

float in [-inf, inf], default 0.0

bbone_curveoutz¶

    

Z-axis handle offset for end of the B-Bone’s curve, adjusts curvature

Type:

    

float in [-inf, inf], default 0.0

bbone_custom_handle_end¶

    

Bone that serves as the end handle for the B-Bone curve

Type:

    

`Bone`

bbone_custom_handle_start¶

    

Bone that serves as the start handle for the B-Bone curve

Type:

    

`Bone`

bbone_easein¶

    

Length of first Bézier Handle (for B-Bones only)

Type:

    

float in [-inf, inf], default 1.0

bbone_easeout¶

    

Length of second Bézier Handle (for B-Bones only)

Type:

    

float in [-inf, inf], default 1.0

bbone_handle_type_end¶

    

Selects how the end handle of the B-Bone is computed

  * `AUTO` Automatic – Use connected parent and children to compute the handle.

  * `ABSOLUTE` Absolute – Use the position of the specified bone to compute the handle.

  * `RELATIVE` Relative – Use the offset of the specified bone from rest pose to compute the handle.

  * `TANGENT` Tangent – Use the orientation of the specified bone to compute the handle, ignoring the location.

Type:

    

enum in [`AUTO`, `ABSOLUTE`, `RELATIVE`, `TANGENT`], default `AUTO`

bbone_handle_type_start¶

    

Selects how the start handle of the B-Bone is computed

  * `AUTO` Automatic – Use connected parent and children to compute the handle.

  * `ABSOLUTE` Absolute – Use the position of the specified bone to compute the handle.

  * `RELATIVE` Relative – Use the offset of the specified bone from rest pose to compute the handle.

  * `TANGENT` Tangent – Use the orientation of the specified bone to compute the handle, ignoring the location.

Type:

    

enum in [`AUTO`, `ABSOLUTE`, `RELATIVE`, `TANGENT`], default `AUTO`

bbone_handle_use_ease_end¶

    

Multiply the B-Bone Ease Out channel by the local Y scale value of the end
handle. This is done after the Scale Easing option and isn’t affected by it.

Type:

    

boolean, default False

bbone_handle_use_ease_start¶

    

Multiply the B-Bone Ease In channel by the local Y scale value of the start
handle. This is done after the Scale Easing option and isn’t affected by it.

Type:

    

boolean, default False

bbone_handle_use_scale_end¶

    

Multiply B-Bone Scale Out channels by the local scale values of the end
handle. This is done after the Scale Easing option and isn’t affected by it.

Type:

    

boolean array of 3 items, default (False, False, False)

bbone_handle_use_scale_start¶

    

Multiply B-Bone Scale In channels by the local scale values of the start
handle. This is done after the Scale Easing option and isn’t affected by it.

Type:

    

boolean array of 3 items, default (False, False, False)

bbone_mapping_mode¶

    

Selects how the vertices are mapped to B-Bone segments based on their position

  * `STRAIGHT` Straight – Fast mapping that is good for most situations, but ignores the rest pose curvature of the B-Bone.

  * `CURVED` Curved – Slower mapping that gives better deformation for B-Bones that are sharply curved in rest pose.

Type:

    

enum in [`STRAIGHT`, `CURVED`], default `STRAIGHT`

bbone_rollin¶

    

Roll offset for the start of the B-Bone, adjusts twist

Type:

    

float in [-inf, inf], default 0.0

bbone_rollout¶

    

Roll offset for the end of the B-Bone, adjusts twist

Type:

    

float in [-inf, inf], default 0.0

bbone_scalein¶

    

Scale factors for the start of the B-Bone, adjusts thickness (for tapering
effects)

Type:

    

[`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3
items in [-inf, inf], default (1.0, 1.0, 1.0)

bbone_scaleout¶

    

Scale factors for the end of the B-Bone, adjusts thickness (for tapering
effects)

Type:

    

[`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3
items in [-inf, inf], default (1.0, 1.0, 1.0)

bbone_segments¶

    

Number of subdivisions of bone (for B-Bones only)

Type:

    

int in [1, 32], default 0

bbone_x¶

    

B-Bone X size

Type:

    

float in [-inf, inf], default 0.0

bbone_z¶

    

B-Bone Z size

Type:

    

float in [-inf, inf], default 0.0

children¶

    

Bones which are children of this bone

Type:

    

[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of `Bone`, (readonly)

collections¶

    

Bone Collections that contain this bone

Type:

    

[`BoneCollectionMemberships`](bpy.types.BoneCollectionMemberships.html#bpy.types.BoneCollectionMemberships
"bpy.types.BoneCollectionMemberships")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`BoneCollection`](bpy.types.BoneCollection.html#bpy.types.BoneCollection
"bpy.types.BoneCollection"), (readonly)

color¶

    

Type:

    

[`BoneColor`](bpy.types.BoneColor.html#bpy.types.BoneColor
"bpy.types.BoneColor"), (readonly)

display_type¶

    

  * `ARMATURE_DEFINED` Armature Defined – Use display mode from armature (default).

  * `OCTAHEDRAL` Octahedral – Display bones as octahedral shape.

  * `STICK` Stick – Display bones as simple 2D lines with dots.

  * `BBONE` B-Bone – Display bones as boxes, showing subdivision and B-Splines.

  * `ENVELOPE` Envelope – Display bones as extruded spheres, showing deformation influence volume.

  * `WIRE` Wire – Display bones as thin wires, showing subdivision and B-Splines.

Type:

    

enum in [`ARMATURE_DEFINED`, `OCTAHEDRAL`, `STICK`, `BBONE`, `ENVELOPE`,
`WIRE`], default `OCTAHEDRAL`

envelope_distance¶

    

Bone deformation distance (for Envelope deform only)

Type:

    

float in [0, 1000], default 0.0

envelope_weight¶

    

Bone deformation weight (for Envelope deform only)

Type:

    

float in [0, 1000], default 0.0

head¶

    

Location of head end of the bone relative to its parent

Type:

    

[`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3
items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

head_local¶

    

Location of head end of the bone relative to armature

Type:

    

[`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3
items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

head_radius¶

    

Radius of head of bone (for Envelope deform only)

Type:

    

float in [-inf, inf], default 0.0

hide¶

    

Bone is not visible when it is not in Edit Mode (i.e. in Object or Pose Modes)

Type:

    

boolean, default False

hide_select¶

    

Bone is able to be selected

Type:

    

boolean, default False

inherit_scale¶

    

Specifies how the bone inherits scaling from the parent bone

  * `FULL` Full – Inherit all effects of parent scaling.

  * `FIX_SHEAR` Fix Shear – Inherit scaling, but remove shearing of the child in the rest orientation.

  * `ALIGNED` Aligned – Rotate non-uniform parent scaling to align with the child, applying parent X scale to child X axis, and so forth.

  * `AVERAGE` Average – Inherit uniform scaling representing the overall change in the volume of the parent.

  * `NONE` None – Completely ignore parent scaling.

  * `NONE_LEGACY` None (Legacy) – Ignore parent scaling without compensating for parent shear. Replicates the effect of disabling the original Inherit Scale checkbox..

Type:

    

enum in [`FULL`, `FIX_SHEAR`, `ALIGNED`, `AVERAGE`, `NONE`, `NONE_LEGACY`],
default `FULL`

length¶

    

Length of the bone

Type:

    

float in [-inf, inf], default 0.0, (readonly)

matrix¶

    

3×3 bone matrix

Type:

    

[`mathutils.Matrix`](mathutils.html#mathutils.Matrix "mathutils.Matrix") of 3
* 3 items in [-inf, inf], default ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0,
0.0, 0.0)), (readonly)

matrix_local¶

    

4×4 bone matrix relative to armature

Type:

    

[`mathutils.Matrix`](mathutils.html#mathutils.Matrix "mathutils.Matrix") of 4
* 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0),
(0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), (readonly)

name¶

    

Type:

    

string, default “”, (never None)

parent¶

    

Parent bone (in same Armature)

Type:

    

`Bone`, (readonly)

select¶

    

Type:

    

boolean, default False

select_head¶

    

Type:

    

boolean, default False

select_tail¶

    

Type:

    

boolean, default False

show_wire¶

    

Bone is always displayed in wireframe regardless of viewport shading mode
(useful for non-obstructive custom bone shapes)

Type:

    

boolean, default False

tail¶

    

Location of tail end of the bone relative to its parent

Type:

    

[`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3
items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

tail_local¶

    

Location of tail end of the bone relative to armature

Type:

    

[`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3
items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

tail_radius¶

    

Radius of tail of bone (for Envelope deform only)

Type:

    

float in [-inf, inf], default 0.0

use_connect¶

    

When bone has a parent, bone’s head is stuck to the parent’s tail

Type:

    

boolean, default False, (readonly)

use_cyclic_offset¶

    

When bone doesn’t have a parent, it receives cyclic offset effects
(Deprecated)

Type:

    

boolean, default False

use_deform¶

    

Enable Bone to deform geometry

Type:

    

boolean, default False

use_endroll_as_inroll¶

    

Add Roll Out of the Start Handle bone to the Roll In value

Type:

    

boolean, default False

use_envelope_multiply¶

    

When deforming bone, multiply effects of Vertex Group weights with Envelope
influence

Type:

    

boolean, default False

use_inherit_rotation¶

    

Bone inherits rotation or scale from parent bone

Type:

    

boolean, default False

use_local_location¶

    

Bone location is set in local space

Type:

    

boolean, default False

use_relative_parent¶

    

Object children will use relative transform, like deform

Type:

    

boolean, default False

use_scale_easing¶

    

Multiply the final easing values by the Scale In/Out Y factors

Type:

    

boolean, default False

basename¶

    

The name of this bone before any ‘.’ character

(readonly)

center¶

    

The midpoint between the head and the tail.

(readonly)

children_recursive¶

    

A list of all children from this bone.

> Note
>
> Takes `O(len(bones)**2)` time.

(readonly)

children_recursive_basename¶

    

Returns a chain of children with the same base name as this bone. Only direct
chains are supported, forks caused by multiple children with matching base
names will terminate the function and not be returned.

Note

Takes `O(len(bones)**2)` time.

(readonly)

parent_recursive¶

    

A list of parents, starting with the immediate parent

(readonly)

vector¶

    

The direction this bone is pointing. Utility function for (tail - head)

(readonly)

x_axis¶

    

Vector pointing down the x-axis of the bone.

(readonly)

y_axis¶

    

Vector pointing down the y-axis of the bone.

(readonly)

z_axis¶

    

Vector pointing down the z-axis of the bone.

(readonly)

evaluate_envelope(_point_)¶

    

Calculate bone envelope at given point

Parameters:

    

**point** ([`mathutils.Vector`](mathutils.html#mathutils.Vector
"mathutils.Vector") of 3 items in [-inf, inf]) – Point, Position in 3d space
to evaluate

Returns:

    

Factor, Envelope factor

Return type:

    

float in [-inf, inf]

convert_local_to_pose(_matrix_ , _matrix_local_ , _*_ , _parent_matrix =((0.0,
0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0,
0.0))_, _parent_matrix_local =((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0),
(0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))_, _invert =False_)¶

    

Transform a matrix from Local to Pose space (or back), taking into account
options like Inherit Scale and Local Location. Unlike Object.convert_space,
this uses custom rest and pose matrices provided by the caller. If the parent
matrices are omitted, the bone is assumed to have no parent.

Parameters:

    

  * **matrix** ([`mathutils.Matrix`](mathutils.html#mathutils.Matrix "mathutils.Matrix") of 4 * 4 items in [-inf, inf]) – The matrix to transform

  * **matrix_local** ([`mathutils.Matrix`](mathutils.html#mathutils.Matrix "mathutils.Matrix") of 4 * 4 items in [-inf, inf]) – The custom rest matrix of this bone (Bone.matrix_local)

  * **parent_matrix** ([`mathutils.Matrix`](mathutils.html#mathutils.Matrix "mathutils.Matrix") of 4 * 4 items in [-inf, inf], (optional)) – The custom pose matrix of the parent bone (PoseBone.matrix)

  * **parent_matrix_local** ([`mathutils.Matrix`](mathutils.html#mathutils.Matrix "mathutils.Matrix") of 4 * 4 items in [-inf, inf], (optional)) – The custom rest matrix of the parent bone (Bone.matrix_local)

  * **invert** (_boolean_ _,__(__optional_ _)_) – Convert from Pose to Local space

Returns:

    

The transformed matrix

Return type:

    

[`mathutils.Matrix`](mathutils.html#mathutils.Matrix "mathutils.Matrix") of 4
* 4 items in [-inf, inf]

This method enables conversions between Local and Pose space for bones in the
middle of updating the armature without having to update dependencies after
each change, by manually carrying updated matrices in a recursive walk.

    
    
    def set_pose_matrices(obj, matrix_map):
        "Assign pose space matrices of all bones at once, ignoring constraints."
    
        def rec(pbone, parent_matrix):
            if pbone.name in matrix_map:
                matrix = matrix_map[pbone.name]
    
                # # Instead of:
                # pbone.matrix = matrix
                # bpy.context.view_layer.update()
    
                # Compute and assign local matrix, using the new parent matrix.
                if pbone.parent:
                    pbone.matrix_basis = pbone.bone.convert_local_to_pose(
                        matrix,
                        pbone.bone.matrix_local,
                        parent_matrix=parent_matrix,
                        parent_matrix_local=pbone.parent.bone.matrix_local,
                        invert=True
                    )
                else:
                    pbone.matrix_basis = pbone.bone.convert_local_to_pose(
                        matrix,
                        pbone.bone.matrix_local,
                        invert=True
                    )
            else:
                # Compute the updated pose matrix from local and new parent matrix.
                if pbone.parent:
                    matrix = pbone.bone.convert_local_to_pose(
                        pbone.matrix_basis,
                        pbone.bone.matrix_local,
                        parent_matrix=parent_matrix,
                        parent_matrix_local=pbone.parent.bone.matrix_local,
                    )
                else:
                    matrix = pbone.bone.convert_local_to_pose(
                        pbone.matrix_basis,
                        pbone.bone.matrix_local,
                    )
    
            # Recursively process children, passing the new matrix through.
            for child in pbone.children:
                rec(child, matrix)
    
        # Scan all bone trees from their roots.
        for pbone in obj.pose.bones:
            if not pbone.parent:
                rec(pbone, None)
    

_classmethod _MatrixFromAxisRoll(_axis_ , _roll_)¶

    

Convert the axis + roll representation to a matrix

Parameters:

    

  * **axis** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (never None)) – The main axis of the bone (tail - head)

  * **roll** (_float in_ _[__-inf_ _,__inf_ _]_) – The roll of the bone

Returns:

    

The resulting orientation matrix

Return type:

    

[`mathutils.Matrix`](mathutils.html#mathutils.Matrix "mathutils.Matrix") of 3
* 3 items in [-inf, inf]

_classmethod _AxisRollFromMatrix(_matrix_ , _*_ , _axis =(0.0, 0.0, 0.0)_)¶

    

Convert a rotational matrix to the axis + roll representation. Note that the
resulting value of the roll may not be as expected if the matrix has shear or
negative determinant.

Parameters:

    

  * **matrix** ([`mathutils.Matrix`](mathutils.html#mathutils.Matrix "mathutils.Matrix") of 3 * 3 items in [-inf, inf], (never None)) – The orientation matrix of the bone

  * **axis** (_float array_ _of_ _3 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – The optional override for the axis (finds closest approximation for the matrix)

Returns:

    

result_axis, The main axis of the bone,
[`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3
items in [-inf, inf]

result_roll, The roll of the bone, float in [-inf, inf]

Return type:

    

([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3
items in [-inf, inf], float in [-inf, inf])

parent_index(_parent_test_)¶

    

The same as ‘bone in other_bone.parent_recursive’ but saved generating a list.

translate(_vec_)¶

    

Utility function to add _vec_ to the head and tail of this bone

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

  * [`bpy.context.active_bone`](bpy.context.html#bpy.context.active_bone "bpy.context.active_bone")
  * [`bpy.context.bone`](bpy.context.html#bpy.context.bone "bpy.context.bone")
  * [`Armature.bones`](bpy.types.Armature.html#bpy.types.Armature.bones "bpy.types.Armature.bones")
  * [`ArmatureBones.active`](bpy.types.ArmatureBones.html#bpy.types.ArmatureBones.active "bpy.types.ArmatureBones.active")
  * `Bone.bbone_custom_handle_end`

|

  * `Bone.bbone_custom_handle_start`
  * `Bone.children`
  * `Bone.parent`
  * [`BoneCollection.bones`](bpy.types.BoneCollection.html#bpy.types.BoneCollection.bones "bpy.types.BoneCollection.bones")
  * [`PoseBone.bone`](bpy.types.PoseBone.html#bpy.types.PoseBone.bone "bpy.types.PoseBone.bone")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

