---
url: https://docs.blender.org/api/current/bpy.types.BoidRule.html
scraped_at: 2025-09-08T14:20:54.084268
title: BoidRule(bpy_struct)¶
---

# BoidRule(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

subclasses —
[`BoidRuleAverageSpeed`](bpy.types.BoidRuleAverageSpeed.html#bpy.types.BoidRuleAverageSpeed
"bpy.types.BoidRuleAverageSpeed"),
[`BoidRuleAvoid`](bpy.types.BoidRuleAvoid.html#bpy.types.BoidRuleAvoid
"bpy.types.BoidRuleAvoid"),
[`BoidRuleAvoidCollision`](bpy.types.BoidRuleAvoidCollision.html#bpy.types.BoidRuleAvoidCollision
"bpy.types.BoidRuleAvoidCollision"),
[`BoidRuleFight`](bpy.types.BoidRuleFight.html#bpy.types.BoidRuleFight
"bpy.types.BoidRuleFight"),
[`BoidRuleFollowLeader`](bpy.types.BoidRuleFollowLeader.html#bpy.types.BoidRuleFollowLeader
"bpy.types.BoidRuleFollowLeader"),
[`BoidRuleGoal`](bpy.types.BoidRuleGoal.html#bpy.types.BoidRuleGoal
"bpy.types.BoidRuleGoal")

_class _bpy.types.BoidRule(_bpy_struct_)¶

    

name¶

    

Boid rule name

Type:

    

string, default “”, (never None)

type¶

    

Type:

    

enum in [Boidrule Type
Items](bpy_types_enum_items/boidrule_type_items.html#rna-enum-boidrule-type-
items), default `GOAL`, (readonly)

use_in_air¶

    

Use rule when boid is flying

Type:

    

boolean, default False

use_on_land¶

    

Use rule when boid is on land

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

  * [`BoidSettings.active_boid_state`](bpy.types.BoidSettings.html#bpy.types.BoidSettings.active_boid_state "bpy.types.BoidSettings.active_boid_state")
  * [`BoidState.active_boid_rule`](bpy.types.BoidState.html#bpy.types.BoidState.active_boid_rule "bpy.types.BoidState.active_boid_rule")

|

  * [`BoidState.rules`](bpy.types.BoidState.html#bpy.types.BoidState.rules "bpy.types.BoidState.rules")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

