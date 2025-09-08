---
url: https://docs.blender.org/api/current/bpy.types.ColorManagedViewSettings.html
scraped_at: 2025-09-08T14:22:04.350064
title: ColorManagedViewSettings(bpy_struct)¶
---

# ColorManagedViewSettings(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.ColorManagedViewSettings(_bpy_struct_)¶

    

Color management settings used for displaying images on the display

curve_mapping¶

    

Color curve mapping applied before display transform

Type:

    

[`CurveMapping`](bpy.types.CurveMapping.html#bpy.types.CurveMapping
"bpy.types.CurveMapping"), (readonly)

exposure¶

    

Exposure (stops) applied before display transform, multiplying by 2^exposure

Type:

    

float in [-32, 32], default 0.0

gamma¶

    

Additional gamma encoding after display transform, for output with custom
gamma

Type:

    

float in [0, 5], default 1.0

look¶

    

Additional transform applied before view transform for artistic needs

  * `NONE` None – Do not modify image in an artistic manner.

Type:

    

enum in [`NONE`], default `NONE`

use_curve_mapping¶

    

Use RGB curved for pre-display transformation

Type:

    

boolean, default False

use_hdr_view¶

    

Enable high dynamic range display in rendered viewport, uncapping display
brightness. This requires a monitor with HDR support and a view transform
designed for HDR. ‘Filmic’ and ‘AgX’ do not generate HDR colors.

Type:

    

boolean, default False

use_white_balance¶

    

Perform chromatic adaption from a different white point

Type:

    

boolean, default False

view_transform¶

    

View used when converting image to a display space

  * `NONE` None – Do not perform any color transform on display, use old non-color managed technique for display.

Type:

    

enum in [`NONE`], default `NONE`

white_balance_temperature¶

    

Color temperature of the scene’s white point

Type:

    

float in [1800, 100000], default 6500.0

white_balance_tint¶

    

Color tint of the scene’s white point (the default of 10 matches daylight)

Type:

    

float in [-500, 500], default 10.0

white_balance_whitepoint¶

    

The color which gets mapped to white (automatically converted to/from
temperature and tint)

Type:

    

[`mathutils.Color`](mathutils.html#mathutils.Color "mathutils.Color") of 3
items in [0, inf], default (0.0, 0.0, 0.0)

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

  * [`ImageFormatSettings.view_settings`](bpy.types.ImageFormatSettings.html#bpy.types.ImageFormatSettings.view_settings "bpy.types.ImageFormatSettings.view_settings")

|

  * [`Scene.view_settings`](bpy.types.Scene.html#bpy.types.Scene.view_settings "bpy.types.Scene.view_settings")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

