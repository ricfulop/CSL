---
url: https://docs.blender.org/api/current/bpy.types.FCurveKeyframePoints.html
scraped_at: 2025-09-08T14:24:58.051660
title: FCurveKeyframePoints(bpy_struct)¶
---

# FCurveKeyframePoints(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.FCurveKeyframePoints(_bpy_struct_)¶

    

Collection of keyframe points

insert(_frame_ , _value_ , _*_ , _options ={}_, _keyframe_type =KEYFRAME_)¶

    

Add a keyframe point to a F-Curve

Parameters:

    

  * **frame** (_float in_ _[__-inf_ _,__inf_ _]_) – X Value of this keyframe point

  * **value** (_float in_ _[__-inf_ _,__inf_ _]_) – Y Value of this keyframe point

  * **options** (enum set in {`REPLACE`, `NEEDED`, `FAST`}, (optional)) – 

Keyframe options

    * `REPLACE` Replace – Don’t add any new keyframes, but just replace existing ones.

    * `NEEDED` Needed – Only adds keyframes that are needed.

    * `FAST` Fast – Fast keyframe insertion to avoid recalculating the curve each time.

  * **keyframe_type** (enum in [Beztriple Keyframe Type Items](bpy_types_enum_items/beztriple_keyframe_type_items.html#rna-enum-beztriple-keyframe-type-items), (optional)) – Type of keyframe to insert

Returns:

    

Newly created keyframe

Return type:

    

[`Keyframe`](bpy.types.Keyframe.html#bpy.types.Keyframe "bpy.types.Keyframe")

add(_count_)¶

    

Add a keyframe point to a F-Curve

Parameters:

    

**count** (_int in_ _[__0_ _,__inf_ _]_) – Number, Number of points to add to
the spline

remove(_keyframe_ , _*_ , _fast =False_)¶

    

Remove keyframe from an F-Curve

Parameters:

    

  * **keyframe** ([`Keyframe`](bpy.types.Keyframe.html#bpy.types.Keyframe "bpy.types.Keyframe"), (never None)) – Keyframe to remove

  * **fast** (_boolean_ _,__(__optional_ _)_) – Fast, Fast keyframe removal to avoid recalculating the curve each time

clear()¶

    

Remove all keyframes from an F-Curve

sort()¶

    

Ensure all keyframe points are chronologically sorted

deduplicate()¶

    

Ensure there are no duplicate keys. Assumes that the points have already been
sorted

handles_recalc()¶

    

Update handles after modifications to the keyframe points, to update things
like auto-clamping

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

  * [`FCurve.keyframe_points`](bpy.types.FCurve.html#bpy.types.FCurve.keyframe_points "bpy.types.FCurve.keyframe_points")

|

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

