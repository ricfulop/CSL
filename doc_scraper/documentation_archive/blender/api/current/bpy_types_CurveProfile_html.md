---
url: https://docs.blender.org/api/current/bpy.types.CurveProfile.html
scraped_at: 2025-09-08T14:24:19.890152
title: CurveProfile(bpy_struct)¶
---

# CurveProfile(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.CurveProfile(_bpy_struct_)¶

    

Profile Path editor used to build a profile path

points¶

    

Profile control points

Type:

    

[`CurveProfilePoints`](bpy.types.CurveProfilePoints.html#bpy.types.CurveProfilePoints
"bpy.types.CurveProfilePoints")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`CurveProfilePoint`](bpy.types.CurveProfilePoint.html#bpy.types.CurveProfilePoint
"bpy.types.CurveProfilePoint"), (readonly)

preset¶

    

  * `LINE` Line – Default.

  * `SUPPORTS` Support Loops – Loops on each side of the profile.

  * `CORNICE` Cornice Molding.

  * `CROWN` Crown Molding.

  * `STEPS` Steps – A number of steps defined by the segments.

Type:

    

enum in [`LINE`, `SUPPORTS`, `CORNICE`, `CROWN`, `STEPS`], default `LINE`

segments¶

    

Segments sampled from control points

Type:

    

[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`CurveProfilePoint`](bpy.types.CurveProfilePoint.html#bpy.types.CurveProfilePoint
"bpy.types.CurveProfilePoint"), (readonly)

use_clip¶

    

Force the path view to fit a defined boundary

Type:

    

boolean, default False

use_sample_even_lengths¶

    

Sample edges with even lengths

Type:

    

boolean, default False

use_sample_straight_edges¶

    

Sample edges with vector handles

Type:

    

boolean, default False

update()¶

    

Refresh internal data, remove doubles and clip points

reset_view()¶

    

Reset the curve profile grid to its clipping size

initialize(_totsegments_)¶

    

Set the number of display segments and fill tables

Parameters:

    

**totsegments** (_int in_ _[__1_ _,__1000_ _]__,__(__never None_ _)_) – The
number of segment values to initialize the segments table with

evaluate(_length_portion_)¶

    

Evaluate the at the given portion of the path length

Parameters:

    

**length_portion** (_float in_ _[__0_ _,__1_ _]_) – Length Portion, Portion of
the path length to travel before evaluation

Returns:

    

Location, The location at the given portion of the profile

Return type:

    

[`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 2
items in [-100, 100]

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

  * [`BevelModifier.custom_profile`](bpy.types.BevelModifier.html#bpy.types.BevelModifier.custom_profile "bpy.types.BevelModifier.custom_profile")
  * [`Curve.bevel_profile`](bpy.types.Curve.html#bpy.types.Curve.bevel_profile "bpy.types.Curve.bevel_profile")

|

  * [`ToolSettings.custom_bevel_profile_preset`](bpy.types.ToolSettings.html#bpy.types.ToolSettings.custom_bevel_profile_preset "bpy.types.ToolSettings.custom_bevel_profile_preset")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

