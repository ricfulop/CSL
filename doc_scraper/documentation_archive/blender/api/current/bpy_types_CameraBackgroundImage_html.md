---
url: https://docs.blender.org/api/current/bpy.types.CameraBackgroundImage.html
scraped_at: 2025-09-08T14:21:35.235049
title: CameraBackgroundImage(bpy_struct)¶
---

# CameraBackgroundImage(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.CameraBackgroundImage(_bpy_struct_)¶

    

Image and settings for display in the 3D View background

alpha¶

    

Image opacity to blend the image against the background color

Type:

    

float in [0, 1], default 0.0

clip¶

    

Movie clip displayed and edited in this space

Type:

    

[`MovieClip`](bpy.types.MovieClip.html#bpy.types.MovieClip
"bpy.types.MovieClip")

clip_user¶

    

Parameters defining which frame of the movie clip is displayed

Type:

    

[`MovieClipUser`](bpy.types.MovieClipUser.html#bpy.types.MovieClipUser
"bpy.types.MovieClipUser"), (readonly, never None)

display_depth¶

    

Display under or over everything

Type:

    

enum in [`BACK`, `FRONT`], default `BACK`

frame_method¶

    

How the image fits in the camera frame

Type:

    

enum in [`STRETCH`, `FIT`, `CROP`], default `STRETCH`

image¶

    

Image displayed and edited in this space

Type:

    

[`Image`](bpy.types.Image.html#bpy.types.Image "bpy.types.Image")

image_user¶

    

Parameters defining which layer, pass and frame of the image is displayed

Type:

    

[`ImageUser`](bpy.types.ImageUser.html#bpy.types.ImageUser
"bpy.types.ImageUser"), (readonly, never None)

is_override_data¶

    

In a local override camera, whether this background image comes from the
linked reference camera, or is local to the override

Type:

    

boolean, default False, (readonly)

offset¶

    

Type:

    

[`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 2
items in [-inf, inf], default (0.0, 0.0)

rotation¶

    

Rotation for the background image (ortho view only)

Type:

    

float in [-inf, inf], default 0.0

scale¶

    

Scale the background image

Type:

    

float in [0, inf], default 0.0

show_background_image¶

    

Show this image as background

Type:

    

boolean, default False

show_expanded¶

    

Show the details in the user interface

Type:

    

boolean, default False

show_on_foreground¶

    

Show this image in front of objects in viewport

Type:

    

boolean, default False

source¶

    

Data source used for background

Type:

    

enum in [`IMAGE`, `MOVIE_CLIP`], default `IMAGE`

use_camera_clip¶

    

Use movie clip from active scene camera

Type:

    

boolean, default False

use_flip_x¶

    

Flip the background image horizontally

Type:

    

boolean, default False

use_flip_y¶

    

Flip the background image vertically

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

  * [`Camera.background_images`](bpy.types.Camera.html#bpy.types.Camera.background_images "bpy.types.Camera.background_images")
  * [`CameraBackgroundImages.new`](bpy.types.CameraBackgroundImages.html#bpy.types.CameraBackgroundImages.new "bpy.types.CameraBackgroundImages.new")

|

  * [`CameraBackgroundImages.remove`](bpy.types.CameraBackgroundImages.html#bpy.types.CameraBackgroundImages.remove "bpy.types.CameraBackgroundImages.remove")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

