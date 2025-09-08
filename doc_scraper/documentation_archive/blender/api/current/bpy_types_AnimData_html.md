---
url: https://docs.blender.org/api/current/bpy.types.AnimData.html
scraped_at: 2025-09-08T14:19:33.797391
title: AnimData(bpy_struct)¶
---

# AnimData(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.AnimData(_bpy_struct_)¶

    

Animation data for data-block

action¶

    

Active Action for this data-block

Type:

    

[`Action`](bpy.types.Action.html#bpy.types.Action "bpy.types.Action")

action_blend_type¶

    

Method used for combining Active Action’s result with result of NLA stack

  * `REPLACE` Replace – The strip values replace the accumulated results by amount specified by influence.

  * `COMBINE` Combine – The strip values are combined with accumulated results by appropriately using addition, multiplication, or quaternion math, based on channel type.

  * `ADD` Add – Weighted result of strip is added to the accumulated results.

  * `SUBTRACT` Subtract – Weighted result of strip is removed from the accumulated results.

  * `MULTIPLY` Multiply – Weighted result of strip is multiplied with the accumulated results.

Type:

    

enum in [`REPLACE`, `COMBINE`, `ADD`, `SUBTRACT`, `MULTIPLY`], default
`REPLACE`

action_extrapolation¶

    

Action to take for gaps past the Active Action’s range (when evaluating with
NLA)

  * `NOTHING` Nothing – Strip has no influence past its extents.

  * `HOLD` Hold – Hold the first frame if no previous strips in track, and always hold last frame.

  * `HOLD_FORWARD` Hold Forward – Only hold last frame.

Type:

    

enum in [`NOTHING`, `HOLD`, `HOLD_FORWARD`], default `HOLD`

action_influence¶

    

Amount the Active Action contributes to the result of the NLA stack

Type:

    

float in [0, 1], default 1.0

action_slot¶

    

The slot identifies which sub-set of the Action is considered to be for this
data-block, and its name is used to find the right slot when assigning an
Action

Type:

    

[`ActionSlot`](bpy.types.ActionSlot.html#bpy.types.ActionSlot
"bpy.types.ActionSlot")

action_slot_handle¶

    

A number that identifies which sub-set of the Action is considered to be for
this data-block

Type:

    

int in [-inf, inf], default 0

action_slot_handle_tweak_storage¶

    

Storage to temporarily hold the main action slot while in tweak mode

Type:

    

int in [-inf, inf], default 0

action_suitable_slots¶

    

The list of slots in this animation data-block

Type:

    

[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`ActionSlot`](bpy.types.ActionSlot.html#bpy.types.ActionSlot
"bpy.types.ActionSlot"), (readonly)

action_tweak_storage¶

    

Storage to temporarily hold the main action while in tweak mode

Type:

    

[`Action`](bpy.types.Action.html#bpy.types.Action "bpy.types.Action")

drivers¶

    

The Drivers/Expressions for this data-block

Type:

    

[`AnimDataDrivers`](bpy.types.AnimDataDrivers.html#bpy.types.AnimDataDrivers
"bpy.types.AnimDataDrivers")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`FCurve`](bpy.types.FCurve.html#bpy.types.FCurve "bpy.types.FCurve"),
(readonly)

last_slot_identifier¶

    

The identifier of the most recently assigned action slot. The slot identifies
which sub-set of the Action is considered to be for this data-block, and its
identifier is used to find the right slot when assigning an Action.

Type:

    

string, default “”, (never None)

nla_tracks¶

    

NLA Tracks (i.e. Animation Layers)

Type:

    

[`NlaTracks`](bpy.types.NlaTracks.html#bpy.types.NlaTracks
"bpy.types.NlaTracks")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`NlaTrack`](bpy.types.NlaTrack.html#bpy.types.NlaTrack "bpy.types.NlaTrack"),
(readonly)

use_nla¶

    

NLA stack is evaluated when evaluating this block

Type:

    

boolean, default False

use_pin¶

    

Type:

    

boolean, default False

use_tweak_mode¶

    

Whether to enable or disable tweak mode in NLA

Type:

    

boolean, default False

nla_tweak_strip_time_to_scene(_frame_ , _*_ , _invert =False_)¶

    

Convert a time value from the local time of the tweaked strip to scene time,
exactly as done by built-in key editing tools. Returns the input time
unchanged if not tweaking.

Parameters:

    

  * **frame** (_float in_ _[__-1.04857e+06_ _,__1.04857e+06_ _]_) – Input time

  * **invert** (_boolean_ _,__(__optional_ _)_) – Invert, Convert scene time to action time

Returns:

    

Converted time

Return type:

    

float in [-1.04857e+06, 1.04857e+06]

fix_paths_rename_all(_*_ , _prefix =''_, _old_name =''_, _new_name =''_)¶

    

Rename the property paths in the animation system, since properties are
animated via string paths, it’s needed to keep them valid after properties has
been renamed

Parameters:

    

  * **prefix** (_string_ _,__(__optional_ _,__never None_ _)_) – Prefix, Name prefix

  * **old_name** (_string_ _,__(__optional_ _,__never None_ _)_) – Old Name, Old name

  * **new_name** (_string_ _,__(__optional_ _,__never None_ _)_) – New Name, New name

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

  * [`Armature.animation_data`](bpy.types.Armature.html#bpy.types.Armature.animation_data "bpy.types.Armature.animation_data")
  * [`CacheFile.animation_data`](bpy.types.CacheFile.html#bpy.types.CacheFile.animation_data "bpy.types.CacheFile.animation_data")
  * [`Camera.animation_data`](bpy.types.Camera.html#bpy.types.Camera.animation_data "bpy.types.Camera.animation_data")
  * [`Curve.animation_data`](bpy.types.Curve.html#bpy.types.Curve.animation_data "bpy.types.Curve.animation_data")
  * [`Curves.animation_data`](bpy.types.Curves.html#bpy.types.Curves.animation_data "bpy.types.Curves.animation_data")
  * [`FreestyleLineStyle.animation_data`](bpy.types.FreestyleLineStyle.html#bpy.types.FreestyleLineStyle.animation_data "bpy.types.FreestyleLineStyle.animation_data")
  * [`GreasePencil.animation_data`](bpy.types.GreasePencil.html#bpy.types.GreasePencil.animation_data "bpy.types.GreasePencil.animation_data")
  * [`GreasePencilv3.animation_data`](bpy.types.GreasePencilv3.html#bpy.types.GreasePencilv3.animation_data "bpy.types.GreasePencilv3.animation_data")
  * [`ID.animation_data_create`](bpy.types.ID.html#bpy.types.ID.animation_data_create "bpy.types.ID.animation_data_create")
  * [`Key.animation_data`](bpy.types.Key.html#bpy.types.Key.animation_data "bpy.types.Key.animation_data")
  * [`Lattice.animation_data`](bpy.types.Lattice.html#bpy.types.Lattice.animation_data "bpy.types.Lattice.animation_data")
  * [`Light.animation_data`](bpy.types.Light.html#bpy.types.Light.animation_data "bpy.types.Light.animation_data")
  * [`LightProbe.animation_data`](bpy.types.LightProbe.html#bpy.types.LightProbe.animation_data "bpy.types.LightProbe.animation_data")
  * [`Mask.animation_data`](bpy.types.Mask.html#bpy.types.Mask.animation_data "bpy.types.Mask.animation_data")

|

  * [`Material.animation_data`](bpy.types.Material.html#bpy.types.Material.animation_data "bpy.types.Material.animation_data")
  * [`Mesh.animation_data`](bpy.types.Mesh.html#bpy.types.Mesh.animation_data "bpy.types.Mesh.animation_data")
  * [`MetaBall.animation_data`](bpy.types.MetaBall.html#bpy.types.MetaBall.animation_data "bpy.types.MetaBall.animation_data")
  * [`MovieClip.animation_data`](bpy.types.MovieClip.html#bpy.types.MovieClip.animation_data "bpy.types.MovieClip.animation_data")
  * [`NodeTree.animation_data`](bpy.types.NodeTree.html#bpy.types.NodeTree.animation_data "bpy.types.NodeTree.animation_data")
  * [`Object.animation_data`](bpy.types.Object.html#bpy.types.Object.animation_data "bpy.types.Object.animation_data")
  * [`ParticleSettings.animation_data`](bpy.types.ParticleSettings.html#bpy.types.ParticleSettings.animation_data "bpy.types.ParticleSettings.animation_data")
  * [`PointCloud.animation_data`](bpy.types.PointCloud.html#bpy.types.PointCloud.animation_data "bpy.types.PointCloud.animation_data")
  * [`Scene.animation_data`](bpy.types.Scene.html#bpy.types.Scene.animation_data "bpy.types.Scene.animation_data")
  * [`Speaker.animation_data`](bpy.types.Speaker.html#bpy.types.Speaker.animation_data "bpy.types.Speaker.animation_data")
  * [`Texture.animation_data`](bpy.types.Texture.html#bpy.types.Texture.animation_data "bpy.types.Texture.animation_data")
  * [`Volume.animation_data`](bpy.types.Volume.html#bpy.types.Volume.animation_data "bpy.types.Volume.animation_data")
  * [`World.animation_data`](bpy.types.World.html#bpy.types.World.animation_data "bpy.types.World.animation_data")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

