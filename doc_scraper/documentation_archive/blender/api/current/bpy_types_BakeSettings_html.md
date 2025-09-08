---
url: https://docs.blender.org/api/current/bpy.types.BakeSettings.html
scraped_at: 2025-09-08T14:20:04.960516
title: BakeSettings(bpy_struct)¶
---

# BakeSettings(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.BakeSettings(_bpy_struct_)¶

    

Bake data for a Scene data-block

cage_extrusion¶

    

Inflate the active object by the specified distance for baking. This helps
matching to points nearer to the outside of the selected object meshes.

Type:

    

float in [0, inf], default 0.0

cage_object¶

    

Object to use as cage instead of calculating the cage from the active object
with cage extrusion

Type:

    

[`Object`](bpy.types.Object.html#bpy.types.Object "bpy.types.Object")

filepath¶

    

Image filepath to use when saving externally

Type:

    

string, default “”, (never None, blend relative `//` prefix supported)

height¶

    

Vertical dimension of the baking map

Type:

    

int in [4, 10000], default 512

image_settings¶

    

Type:

    

[`ImageFormatSettings`](bpy.types.ImageFormatSettings.html#bpy.types.ImageFormatSettings
"bpy.types.ImageFormatSettings"), (readonly, never None)

margin¶

    

Extends the baked result as a post process filter

Type:

    

int in [0, 32767], default 16

margin_type¶

    

Algorithm to extend the baked result

Type:

    

enum in [Bake Margin Type
Items](bpy_types_enum_items/bake_margin_type_items.html#rna-enum-bake-margin-
type-items), default `ADJACENT_FACES`

max_ray_distance¶

    

The maximum ray distance for matching points between the active and selected
objects. If zero, there is no limit.

Type:

    

float in [0, inf], default 0.0

normal_b¶

    

Axis to bake in blue channel

Type:

    

enum in [Normal Swizzle
Items](bpy_types_enum_items/normal_swizzle_items.html#rna-enum-normal-swizzle-
items), default `POS_X`

normal_g¶

    

Axis to bake in green channel

Type:

    

enum in [Normal Swizzle
Items](bpy_types_enum_items/normal_swizzle_items.html#rna-enum-normal-swizzle-
items), default `POS_X`

normal_r¶

    

Axis to bake in red channel

Type:

    

enum in [Normal Swizzle
Items](bpy_types_enum_items/normal_swizzle_items.html#rna-enum-normal-swizzle-
items), default `POS_X`

normal_space¶

    

Choose normal space for baking

Type:

    

enum in [Normal Space Items](bpy_types_enum_items/normal_space_items.html#rna-
enum-normal-space-items), default `OBJECT`

pass_filter¶

    

Passes to include in the active baking pass

Type:

    

enum set in [Bake Pass Filter Type
Items](bpy_types_enum_items/bake_pass_filter_type_items.html#rna-enum-bake-
pass-filter-type-items), default `{}`, (readonly)

save_mode¶

    

Where to save baked image textures

Type:

    

enum in [Bake Save Mode
Items](bpy_types_enum_items/bake_save_mode_items.html#rna-enum-bake-save-mode-
items), default `INTERNAL`

target¶

    

Where to output the baked map

Type:

    

enum in [Bake Target Items](bpy_types_enum_items/bake_target_items.html#rna-
enum-bake-target-items), default `IMAGE_TEXTURES`

use_automatic_name¶

    

Automatically name the output file with the pass type (external only)

Type:

    

boolean, default False

use_cage¶

    

Cast rays to active object from a cage

Type:

    

boolean, default False

use_clear¶

    

Clear Images before baking (internal only)

Type:

    

boolean, default True

use_pass_color¶

    

Color the pass

Type:

    

boolean, default True

use_pass_diffuse¶

    

Add diffuse contribution

Type:

    

boolean, default True

use_pass_direct¶

    

Add direct lighting contribution

Type:

    

boolean, default True

use_pass_emit¶

    

Add emission contribution

Type:

    

boolean, default True

use_pass_glossy¶

    

Add glossy contribution

Type:

    

boolean, default True

use_pass_indirect¶

    

Add indirect lighting contribution

Type:

    

boolean, default True

use_pass_transmission¶

    

Add transmission contribution

Type:

    

boolean, default True

use_selected_to_active¶

    

Bake shading on the surface of selected objects to the active object

Type:

    

boolean, default False

use_split_materials¶

    

Split external images per material (external only)

Type:

    

boolean, default False

view_from¶

    

Source of reflection ray directions

  * `ABOVE_SURFACE` Above Surface – Cast rays from above the surface.

  * `ACTIVE_CAMERA` Active Camera – Use the active camera’s position to cast rays.

Type:

    

enum in [`ABOVE_SURFACE`, `ACTIVE_CAMERA`], default `ABOVE_SURFACE`

width¶

    

Horizontal dimension of the baking map

Type:

    

int in [4, 10000], default 512

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

  * [`RenderSettings.bake`](bpy.types.RenderSettings.html#bpy.types.RenderSettings.bake "bpy.types.RenderSettings.bake")

|

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

