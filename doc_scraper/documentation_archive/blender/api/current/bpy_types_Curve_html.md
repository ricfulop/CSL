---
url: https://docs.blender.org/api/current/bpy.types.Curve.html
scraped_at: 2025-09-08T14:24:11.880798
title: Curve(ID)¶
---

# Curve(ID)¶  
  
base classes — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct"), [`ID`](bpy.types.ID.html#bpy.types.ID "bpy.types.ID")

subclasses —
[`SurfaceCurve`](bpy.types.SurfaceCurve.html#bpy.types.SurfaceCurve
"bpy.types.SurfaceCurve"),
[`TextCurve`](bpy.types.TextCurve.html#bpy.types.TextCurve
"bpy.types.TextCurve")

_class _bpy.types.Curve(_ID_)¶

    

Curve data-block storing curves, splines and NURBS

animation_data¶

    

Animation data for this data-block

Type:

    

[`AnimData`](bpy.types.AnimData.html#bpy.types.AnimData "bpy.types.AnimData"),
(readonly)

bevel_depth¶

    

Radius of the bevel geometry, not including extrusion

Type:

    

float in [-inf, inf], default 0.0

bevel_factor_end¶

    

Define where along the spline the curve geometry ends (0 for the beginning, 1
for the end)

Type:

    

float in [0, 1], default 1.0

bevel_factor_mapping_end¶

    

Determine how the geometry end factor is mapped to a spline

  * `RESOLUTION` Resolution – Map the geometry factor to the number of subdivisions of a spline (U resolution).

  * `SEGMENTS` Segments – Map the geometry factor to the length of a segment and to the number of subdivisions of a segment.

  * `SPLINE` Spline – Map the geometry factor to the length of a spline.

Type:

    

enum in [`RESOLUTION`, `SEGMENTS`, `SPLINE`], default `RESOLUTION`

bevel_factor_mapping_start¶

    

Determine how the geometry start factor is mapped to a spline

  * `RESOLUTION` Resolution – Map the geometry factor to the number of subdivisions of a spline (U resolution).

  * `SEGMENTS` Segments – Map the geometry factor to the length of a segment and to the number of subdivisions of a segment.

  * `SPLINE` Spline – Map the geometry factor to the length of a spline.

Type:

    

enum in [`RESOLUTION`, `SEGMENTS`, `SPLINE`], default `RESOLUTION`

bevel_factor_start¶

    

Define where along the spline the curve geometry starts (0 for the beginning,
1 for the end)

Type:

    

float in [0, 1], default 0.0

bevel_mode¶

    

Determine how to build the curve’s bevel geometry

  * `ROUND` Round – Use circle for the section of the curve’s bevel geometry.

  * `OBJECT` Object – Use an object for the section of the curve’s bevel geometry segment.

  * `PROFILE` Profile – Use a custom profile for each quarter of curve’s bevel geometry.

Type:

    

enum in [`ROUND`, `OBJECT`, `PROFILE`], default `ROUND`

bevel_object¶

    

The name of the Curve object that defines the bevel shape

Type:

    

[`Object`](bpy.types.Object.html#bpy.types.Object "bpy.types.Object")

bevel_profile¶

    

The path for the curve’s custom profile

Type:

    

[`CurveProfile`](bpy.types.CurveProfile.html#bpy.types.CurveProfile
"bpy.types.CurveProfile"), (readonly)

bevel_resolution¶

    

The number of segments in each quarter-circle of the bevel

Type:

    

int in [0, 32], default 4

cycles¶

    

Cycles mesh settings

Type:

    

`CyclesMeshSettings`, (readonly)

dimensions¶

    

Select 2D or 3D curve type

  * `2D` 2D – Clamp the Z axis of the curve.

  * `3D` 3D – Allow editing on the Z axis of this curve, also allows tilt and curve radius to be used.

Type:

    

enum in [`2D`, `3D`], default `2D`

eval_time¶

    

Parametric position along the length of the curve that Objects ‘following’ it
should be at (position is evaluated by dividing by the ‘Path Length’ value)

Type:

    

float in [-inf, inf], default 0.0

extrude¶

    

Length of the depth added in the local Z direction along the curve,
perpendicular to its normals

Type:

    

float in [0, inf], default 0.0

fill_mode¶

    

Mode of filling curve

Type:

    

enum in [`FULL`, `BACK`, `FRONT`, `HALF`], default `FULL`

is_editmode¶

    

True when used in editmode

Type:

    

boolean, default False, (readonly)

materials¶

    

Type:

    

[`IDMaterials`](bpy.types.IDMaterials.html#bpy.types.IDMaterials
"bpy.types.IDMaterials")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Material`](bpy.types.Material.html#bpy.types.Material "bpy.types.Material"),
(readonly)

offset¶

    

Distance to move the curve parallel to its normals

Type:

    

float in [-inf, inf], default 0.0

path_duration¶

    

The number of frames that are needed to traverse the path, defining the
maximum value for the ‘Evaluation Time’ setting

Type:

    

int in [1, 1048574], default 100

render_resolution_u¶

    

Surface resolution in U direction used while rendering (zero uses preview
resolution)

Type:

    

int in [0, 1024], default 0

render_resolution_v¶

    

Surface resolution in V direction used while rendering (zero uses preview
resolution)

Type:

    

int in [0, 1024], default 0

resolution_u¶

    

Number of computed points in the U direction between every pair of control
points

Type:

    

int in [1, 1024], default 12

resolution_v¶

    

The number of computed points in the V direction between every pair of control
points

Type:

    

int in [1, 1024], default 12

shape_keys¶

    

Type:

    

[`Key`](bpy.types.Key.html#bpy.types.Key "bpy.types.Key"), (readonly)

splines¶

    

Collection of splines in this curve data object

Type:

    

[`CurveSplines`](bpy.types.CurveSplines.html#bpy.types.CurveSplines
"bpy.types.CurveSplines")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Spline`](bpy.types.Spline.html#bpy.types.Spline "bpy.types.Spline"),
(readonly)

taper_object¶

    

Curve object name that defines the taper (width)

Type:

    

[`Object`](bpy.types.Object.html#bpy.types.Object "bpy.types.Object")

taper_radius_mode¶

    

Determine how the effective radius of the spline point is computed when a
taper object is specified

  * `OVERRIDE` Override – Override the radius of the spline point with the taper radius.

  * `MULTIPLY` Multiply – Multiply the radius of the spline point by the taper radius.

  * `ADD` Add – Add the radius of the bevel point to the taper radius.

Type:

    

enum in [`OVERRIDE`, `MULTIPLY`, `ADD`], default `OVERRIDE`

texspace_location¶

    

Type:

    

[`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3
items in [-inf, inf], default (0.0, 0.0, 0.0)

texspace_size¶

    

Type:

    

[`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3
items in [-inf, inf], default (1.0, 1.0, 1.0)

twist_mode¶

    

The type of tilt calculation for 3D Curves

  * `Z_UP` Z-Up – Use Z-Up axis to calculate the curve twist at each point.

  * `MINIMUM` Minimum – Use the least twist over the entire curve.

  * `TANGENT` Tangent – Use the tangent to calculate twist.

Type:

    

enum in [`Z_UP`, `MINIMUM`, `TANGENT`], default `MINIMUM`

twist_smooth¶

    

Smoothing iteration for tangents

Type:

    

float in [-inf, inf], default 0.0

use_auto_texspace¶

    

Adjust active object’s texture space automatically when transforming object

Type:

    

boolean, default True

use_deform_bounds¶

    

Option for curve-deform: Use the mesh bounds to clamp the deformation

Type:

    

boolean, default False

use_fill_caps¶

    

Fill caps for beveled curves

Type:

    

boolean, default False

use_map_taper¶

    

Map effect of the taper object to the beveled part of the curve

Type:

    

boolean, default False

use_path¶

    

Enable the curve to become a translation path

Type:

    

boolean, default False

use_path_clamp¶

    

Clamp the curve path children so they can’t travel past the start/end point of
the curve

Type:

    

boolean, default False

use_path_follow¶

    

Make curve path children rotate along the path

Type:

    

boolean, default False

use_radius¶

    

Option for paths and curve-deform: apply the curve radius to objects following
it and to deformed objects

Type:

    

boolean, default True

use_stretch¶

    

Option for curve-deform: make deformed child stretch along entire path

Type:

    

boolean, default False

transform(_matrix_ , _*_ , _shape_keys =False_)¶

    

Transform curve by a matrix

Parameters:

    

  * **matrix** ([`mathutils.Matrix`](mathutils.html#mathutils.Matrix "mathutils.Matrix") of 4 * 4 items in [-inf, inf]) – Matrix

  * **shape_keys** (_boolean_ _,__(__optional_ _)_) – Transform Shape Keys

validate_material_indices()¶

    

Validate material indices of splines or letters, return True when the curve
has had invalid indices corrected (to default 0)

Returns:

    

Result

Return type:

    

boolean

update_gpu_tag()¶

    

update_gpu_tag

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
  * [`ID.name`](bpy.types.ID.html#bpy.types.ID.name "bpy.types.ID.name")
  * [`ID.name_full`](bpy.types.ID.html#bpy.types.ID.name_full "bpy.types.ID.name_full")
  * [`ID.id_type`](bpy.types.ID.html#bpy.types.ID.id_type "bpy.types.ID.id_type")
  * [`ID.session_uid`](bpy.types.ID.html#bpy.types.ID.session_uid "bpy.types.ID.session_uid")
  * [`ID.is_evaluated`](bpy.types.ID.html#bpy.types.ID.is_evaluated "bpy.types.ID.is_evaluated")
  * [`ID.original`](bpy.types.ID.html#bpy.types.ID.original "bpy.types.ID.original")
  * [`ID.users`](bpy.types.ID.html#bpy.types.ID.users "bpy.types.ID.users")
  * [`ID.use_fake_user`](bpy.types.ID.html#bpy.types.ID.use_fake_user "bpy.types.ID.use_fake_user")
  * [`ID.use_extra_user`](bpy.types.ID.html#bpy.types.ID.use_extra_user "bpy.types.ID.use_extra_user")
  * [`ID.is_embedded_data`](bpy.types.ID.html#bpy.types.ID.is_embedded_data "bpy.types.ID.is_embedded_data")

|

  * [`ID.is_missing`](bpy.types.ID.html#bpy.types.ID.is_missing "bpy.types.ID.is_missing")
  * [`ID.is_runtime_data`](bpy.types.ID.html#bpy.types.ID.is_runtime_data "bpy.types.ID.is_runtime_data")
  * [`ID.is_editable`](bpy.types.ID.html#bpy.types.ID.is_editable "bpy.types.ID.is_editable")
  * [`ID.tag`](bpy.types.ID.html#bpy.types.ID.tag "bpy.types.ID.tag")
  * [`ID.is_library_indirect`](bpy.types.ID.html#bpy.types.ID.is_library_indirect "bpy.types.ID.is_library_indirect")
  * [`ID.library`](bpy.types.ID.html#bpy.types.ID.library "bpy.types.ID.library")
  * [`ID.library_weak_reference`](bpy.types.ID.html#bpy.types.ID.library_weak_reference "bpy.types.ID.library_weak_reference")
  * [`ID.asset_data`](bpy.types.ID.html#bpy.types.ID.asset_data "bpy.types.ID.asset_data")
  * [`ID.override_library`](bpy.types.ID.html#bpy.types.ID.override_library "bpy.types.ID.override_library")
  * [`ID.preview`](bpy.types.ID.html#bpy.types.ID.preview "bpy.types.ID.preview")

  
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
  * [`bpy_struct.keyframe_delete`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.keyframe_delete "bpy.types.bpy_struct.keyframe_delete")
  * [`bpy_struct.keyframe_insert`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.keyframe_insert "bpy.types.bpy_struct.keyframe_insert")
  * [`bpy_struct.keys`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.keys "bpy.types.bpy_struct.keys")
  * [`bpy_struct.path_from_id`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.path_from_id "bpy.types.bpy_struct.path_from_id")
  * [`bpy_struct.path_resolve`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.path_resolve "bpy.types.bpy_struct.path_resolve")
  * [`bpy_struct.pop`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.pop "bpy.types.bpy_struct.pop")
  * [`bpy_struct.property_overridable_library_set`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.property_overridable_library_set "bpy.types.bpy_struct.property_overridable_library_set")
  * [`bpy_struct.property_unset`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.property_unset "bpy.types.bpy_struct.property_unset")
  * [`bpy_struct.rna_ancestors`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.rna_ancestors "bpy.types.bpy_struct.rna_ancestors")

|

  * [`bpy_struct.type_recast`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.type_recast "bpy.types.bpy_struct.type_recast")
  * [`bpy_struct.values`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.values "bpy.types.bpy_struct.values")
  * [`ID.rename`](bpy.types.ID.html#bpy.types.ID.rename "bpy.types.ID.rename")
  * [`ID.evaluated_get`](bpy.types.ID.html#bpy.types.ID.evaluated_get "bpy.types.ID.evaluated_get")
  * [`ID.copy`](bpy.types.ID.html#bpy.types.ID.copy "bpy.types.ID.copy")
  * [`ID.asset_mark`](bpy.types.ID.html#bpy.types.ID.asset_mark "bpy.types.ID.asset_mark")
  * [`ID.asset_clear`](bpy.types.ID.html#bpy.types.ID.asset_clear "bpy.types.ID.asset_clear")
  * [`ID.asset_generate_preview`](bpy.types.ID.html#bpy.types.ID.asset_generate_preview "bpy.types.ID.asset_generate_preview")
  * [`ID.override_create`](bpy.types.ID.html#bpy.types.ID.override_create "bpy.types.ID.override_create")
  * [`ID.override_hierarchy_create`](bpy.types.ID.html#bpy.types.ID.override_hierarchy_create "bpy.types.ID.override_hierarchy_create")
  * [`ID.user_clear`](bpy.types.ID.html#bpy.types.ID.user_clear "bpy.types.ID.user_clear")
  * [`ID.user_remap`](bpy.types.ID.html#bpy.types.ID.user_remap "bpy.types.ID.user_remap")
  * [`ID.make_local`](bpy.types.ID.html#bpy.types.ID.make_local "bpy.types.ID.make_local")
  * [`ID.user_of_id`](bpy.types.ID.html#bpy.types.ID.user_of_id "bpy.types.ID.user_of_id")
  * [`ID.animation_data_create`](bpy.types.ID.html#bpy.types.ID.animation_data_create "bpy.types.ID.animation_data_create")
  * [`ID.animation_data_clear`](bpy.types.ID.html#bpy.types.ID.animation_data_clear "bpy.types.ID.animation_data_clear")
  * [`ID.update_tag`](bpy.types.ID.html#bpy.types.ID.update_tag "bpy.types.ID.update_tag")
  * [`ID.preview_ensure`](bpy.types.ID.html#bpy.types.ID.preview_ensure "bpy.types.ID.preview_ensure")
  * [`ID.bl_rna_get_subclass`](bpy.types.ID.html#bpy.types.ID.bl_rna_get_subclass "bpy.types.ID.bl_rna_get_subclass")
  * [`ID.bl_rna_get_subclass_py`](bpy.types.ID.html#bpy.types.ID.bl_rna_get_subclass_py "bpy.types.ID.bl_rna_get_subclass_py")

  
---|---  
  
## References¶

  * [`bpy.context.curve`](bpy.context.html#bpy.context.curve "bpy.context.curve")
  * [`BlendData.curves`](bpy.types.BlendData.html#bpy.types.BlendData.curves "bpy.types.BlendData.curves")
  * [`BlendDataCurves.new`](bpy.types.BlendDataCurves.html#bpy.types.BlendDataCurves.new "bpy.types.BlendDataCurves.new")

|

  * [`BlendDataCurves.remove`](bpy.types.BlendDataCurves.html#bpy.types.BlendDataCurves.remove "bpy.types.BlendDataCurves.remove")
  * [`Object.to_curve`](bpy.types.Object.html#bpy.types.Object.to_curve "bpy.types.Object.to_curve")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

