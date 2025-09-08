---
url: https://docs.blender.org/api/current/bpy.types.Camera.html
scraped_at: 2025-09-08T14:21:34.267491
title: Camera(ID)¶
---

# Camera(ID)¶  
  
base classes — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct"), [`ID`](bpy.types.ID.html#bpy.types.ID "bpy.types.ID")

_class _bpy.types.Camera(_ID_)¶

    

Camera data-block for storing camera settings

angle¶

    

Camera lens field of view

Type:

    

float in [0.00640536, 3.01675], default 0.69115

angle_x¶

    

Camera lens horizontal field of view

Type:

    

float in [0.00640536, 3.01675], default 0.0

angle_y¶

    

Camera lens vertical field of view

Type:

    

float in [0.00640536, 3.01675], default 0.0

animation_data¶

    

Animation data for this data-block

Type:

    

[`AnimData`](bpy.types.AnimData.html#bpy.types.AnimData "bpy.types.AnimData"),
(readonly)

background_images¶

    

List of background images

Type:

    

[`CameraBackgroundImages`](bpy.types.CameraBackgroundImages.html#bpy.types.CameraBackgroundImages
"bpy.types.CameraBackgroundImages")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`CameraBackgroundImage`](bpy.types.CameraBackgroundImage.html#bpy.types.CameraBackgroundImage
"bpy.types.CameraBackgroundImage"), (readonly)

central_cylindrical_radius¶

    

Radius of the virtual cylinder

Type:

    

float in [1e-05, inf], default 1.0

central_cylindrical_range_u_max¶

    

Maximum Longitude value for the central cylindrical lens

Type:

    

float in [-inf, inf], default 3.14159

central_cylindrical_range_u_min¶

    

Minimum Longitude value for the central cylindrical lens

Type:

    

float in [-inf, inf], default -3.14159

central_cylindrical_range_v_max¶

    

Maximum Height value for the central cylindrical lens

Type:

    

float in [-inf, inf], default 1.0

central_cylindrical_range_v_min¶

    

Minimum Height value for the central cylindrical lens

Type:

    

float in [-inf, inf], default -1.0

clip_end¶

    

Camera far clipping distance

Type:

    

float in [1e-06, inf], default 1000.0

clip_start¶

    

Camera near clipping distance

Type:

    

float in [1e-06, inf], default 0.1

custom_bytecode¶

    

Compiled bytecode of the custom shader

Type:

    

string, default “”, (never None)

custom_bytecode_hash¶

    

Hash of the compiled bytecode of the custom shader, for quick equality
checking

Type:

    

string, default “”, (never None)

custom_filepath¶

    

Path to the shader defining the custom camera

Type:

    

string, default “”, (never None)

custom_mode¶

    

  * `INTERNAL` Internal – Use internal text data-block.

  * `EXTERNAL` External – Use external file.

Type:

    

enum in [`INTERNAL`, `EXTERNAL`], default `INTERNAL`

custom_shader¶

    

Shader defining the custom camera

Type:

    

[`Text`](bpy.types.Text.html#bpy.types.Text "bpy.types.Text")

cycles_custom¶

    

Parameters for custom (OSL-based) cameras

Type:

    

`CyclesCustomCameraSettings`, (readonly)

display_size¶

    

Apparent size of the Camera object in the 3D View

Type:

    

float in [0.01, 1000], default 1.0

dof¶

    

Type:

    

[`CameraDOFSettings`](bpy.types.CameraDOFSettings.html#bpy.types.CameraDOFSettings
"bpy.types.CameraDOFSettings"), (readonly)

fisheye_fov¶

    

Field of view for the fisheye lens

Type:

    

float in [0.1745, 31.4159], default 3.14159

fisheye_lens¶

    

Lens focal length (mm)

Type:

    

float in [0.01, 100], default 10.5

fisheye_polynomial_k0¶

    

Coefficient K0 of the lens polynomial

Type:

    

float in [-inf, inf], default -1.17351e-05

fisheye_polynomial_k1¶

    

Coefficient K1 of the lens polynomial

Type:

    

float in [-inf, inf], default -0.0199887

fisheye_polynomial_k2¶

    

Coefficient K2 of the lens polynomial

Type:

    

float in [-inf, inf], default -3.3525e-06

fisheye_polynomial_k3¶

    

Coefficient K3 of the lens polynomial

Type:

    

float in [-inf, inf], default 3.0993e-06

fisheye_polynomial_k4¶

    

Coefficient K4 of the lens polynomial

Type:

    

float in [-inf, inf], default -2.61e-08

latitude_max¶

    

Maximum latitude (vertical angle) for the equirectangular lens

Type:

    

float in [-1.5708, 1.5708], default 1.5708

latitude_min¶

    

Minimum latitude (vertical angle) for the equirectangular lens

Type:

    

float in [-1.5708, 1.5708], default -1.5708

lens¶

    

Perspective Camera focal length value in millimeters

Type:

    

float in [1, inf], default 50.0

lens_unit¶

    

Unit to edit lens in for the user interface

  * `MILLIMETERS` Millimeters – Specify focal length of the lens in millimeters.

  * `FOV` Field of View – Specify the lens as the field of view’s angle.

Type:

    

enum in [`MILLIMETERS`, `FOV`], default `MILLIMETERS`

longitude_max¶

    

Maximum longitude (horizontal angle) for the equirectangular lens

Type:

    

float in [-inf, inf], default 3.14159

longitude_min¶

    

Minimum longitude (horizontal angle) for the equirectangular lens

Type:

    

float in [-inf, inf], default -3.14159

ortho_scale¶

    

Orthographic Camera scale (similar to zoom)

Type:

    

float in [0, inf], default 6.0

panorama_type¶

    

Distortion to use for the calculation

  * `EQUIRECTANGULAR` Equirectangular – Spherical camera for environment maps, also known as Lat Long panorama.

  * `EQUIANGULAR_CUBEMAP_FACE` Equiangular Cubemap Face – Single face of an equiangular cubemap.

  * `MIRRORBALL` Mirror Ball – Mirror ball mapping for environment maps.

  * `FISHEYE_EQUIDISTANT` Fisheye Equidistant – Ideal for fulldomes, ignore the sensor dimensions.

  * `FISHEYE_EQUISOLID` Fisheye Equisolid – Similar to most fisheye modern lens, takes sensor dimensions into consideration.

  * `FISHEYE_LENS_POLYNOMIAL` Fisheye Lens Polynomial – Defines the lens projection as polynomial to allow real world camera lenses to be mimicked.

  * `CENTRAL_CYLINDRICAL` Central Cylindrical – Projection onto a virtual cylinder from its center, similar as a rotating panoramic camera.

Type:

    

enum in [`EQUIRECTANGULAR`, `EQUIANGULAR_CUBEMAP_FACE`, `MIRRORBALL`,
`FISHEYE_EQUIDISTANT`, `FISHEYE_EQUISOLID`, `FISHEYE_LENS_POLYNOMIAL`,
`CENTRAL_CYLINDRICAL`], default `FISHEYE_EQUISOLID`

passepartout_alpha¶

    

Opacity (alpha) of the darkened overlay in Camera view

Type:

    

float in [0, 1], default 0.5

sensor_fit¶

    

Method to fit image and field of view angle inside the sensor

  * `AUTO` Auto – Fit to the sensor width or height depending on image resolution.

  * `HORIZONTAL` Horizontal – Fit to the sensor width.

  * `VERTICAL` Vertical – Fit to the sensor height.

Type:

    

enum in [`AUTO`, `HORIZONTAL`, `VERTICAL`], default `AUTO`

sensor_height¶

    

Vertical size of the image sensor area in millimeters

Type:

    

float in [1, inf], default 24.0

sensor_width¶

    

Horizontal size of the image sensor area in millimeters

Type:

    

float in [1, inf], default 36.0

shift_x¶

    

Camera horizontal shift

Type:

    

float in [-inf, inf], default 0.0

shift_y¶

    

Camera vertical shift

Type:

    

float in [-inf, inf], default 0.0

show_background_images¶

    

Display reference images behind objects in the 3D View

Type:

    

boolean, default False

show_composition_center¶

    

Display center composition guide inside the camera view

Type:

    

boolean, default False

show_composition_center_diagonal¶

    

Display diagonal center composition guide inside the camera view

Type:

    

boolean, default False

show_composition_golden¶

    

Display golden ratio composition guide inside the camera view

Type:

    

boolean, default False

show_composition_golden_tria_a¶

    

Display golden triangle A composition guide inside the camera view

Type:

    

boolean, default False

show_composition_golden_tria_b¶

    

Display golden triangle B composition guide inside the camera view

Type:

    

boolean, default False

show_composition_harmony_tri_a¶

    

Display harmony A composition guide inside the camera view

Type:

    

boolean, default False

show_composition_harmony_tri_b¶

    

Display harmony B composition guide inside the camera view

Type:

    

boolean, default False

show_composition_thirds¶

    

Display rule of thirds composition guide inside the camera view

Type:

    

boolean, default False

show_limits¶

    

Display the clipping range and focus point on the camera

Type:

    

boolean, default False

show_mist¶

    

Display a line from the Camera to indicate the mist area

Type:

    

boolean, default False

show_name¶

    

Show the active Camera’s name in Camera view

Type:

    

boolean, default False

show_passepartout¶

    

Show a darkened overlay outside the image area in Camera view

Type:

    

boolean, default True

show_safe_areas¶

    

Show TV title safe and action safe areas in Camera view

Type:

    

boolean, default False

show_safe_center¶

    

Show safe areas to fit content in a different aspect ratio

Type:

    

boolean, default False

show_sensor¶

    

Show sensor size (film gate) in Camera view

Type:

    

boolean, default False

stereo¶

    

Type:

    

[`CameraStereoData`](bpy.types.CameraStereoData.html#bpy.types.CameraStereoData
"bpy.types.CameraStereoData"), (readonly, never None)

type¶

    

Camera types

Type:

    

enum in [`PERSP`, `ORTHO`, `PANO`, `CUSTOM`], default `PERSP`

view_frame(_*_ , _scene =None_)¶

    

Return 4 points for the cameras frame (before object transformation)

Parameters:

    

**scene** ([`Scene`](bpy.types.Scene.html#bpy.types.Scene "bpy.types.Scene"),
(optional)) – Scene to use for aspect calculation, when omitted 1:1 aspect is
used

Returns:

    

result_1, Result, [`mathutils.Vector`](mathutils.html#mathutils.Vector
"mathutils.Vector") of 3 items in [-inf, inf]

result_2, Result, [`mathutils.Vector`](mathutils.html#mathutils.Vector
"mathutils.Vector") of 3 items in [-inf, inf]

result_3, Result, [`mathutils.Vector`](mathutils.html#mathutils.Vector
"mathutils.Vector") of 3 items in [-inf, inf]

result_4, Result, [`mathutils.Vector`](mathutils.html#mathutils.Vector
"mathutils.Vector") of 3 items in [-inf, inf]

Return type:

    

([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3
items in [-inf, inf], [`mathutils.Vector`](mathutils.html#mathutils.Vector
"mathutils.Vector") of 3 items in [-inf, inf],
[`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3
items in [-inf, inf], [`mathutils.Vector`](mathutils.html#mathutils.Vector
"mathutils.Vector") of 3 items in [-inf, inf])

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

  * [`bpy.context.camera`](bpy.context.html#bpy.context.camera "bpy.context.camera")
  * [`BlendData.cameras`](bpy.types.BlendData.html#bpy.types.BlendData.cameras "bpy.types.BlendData.cameras")
  * [`BlendDataCameras.new`](bpy.types.BlendDataCameras.html#bpy.types.BlendDataCameras.new "bpy.types.BlendDataCameras.new")

|

  * [`BlendDataCameras.remove`](bpy.types.BlendDataCameras.html#bpy.types.BlendDataCameras.remove "bpy.types.BlendDataCameras.remove")
  * [`RenderEngine.update_custom_camera`](bpy.types.RenderEngine.html#bpy.types.RenderEngine.update_custom_camera "bpy.types.RenderEngine.update_custom_camera")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

