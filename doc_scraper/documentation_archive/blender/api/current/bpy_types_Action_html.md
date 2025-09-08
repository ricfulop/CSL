---
url: https://docs.blender.org/api/current/bpy.types.Action.html
scraped_at: 2025-09-08T14:19:09.732463
title: Action(ID)¶
---

# Action(ID)¶  
  
base classes — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct"), [`ID`](bpy.types.ID.html#bpy.types.ID "bpy.types.ID")

_class _bpy.types.Action(_ID_)¶

    

A collection of F-Curves for animation

curve_frame_range¶

    

The combined frame range of all F-Curves within this action

Type:

    

[`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 2
items in [-inf, inf], default (0.0, 0.0), (readonly)

fcurves¶

    

Legacy API, for backward compatibility with code that does not handle slotted
actions yet. This collection contains the F-Curves for the action’s first slot

Type:

    

[`ActionFCurves`](bpy.types.ActionFCurves.html#bpy.types.ActionFCurves
"bpy.types.ActionFCurves")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`FCurve`](bpy.types.FCurve.html#bpy.types.FCurve "bpy.types.FCurve"),
(readonly)

frame_end¶

    

The end frame of the manually set intended playback range

Type:

    

float in [-1.04857e+06, 1.04857e+06], default 0.0

frame_range¶

    

The intended playback frame range of this action, using the manually set range
if available, or the combined frame range of all F-Curves within this action
if not (assigning sets the manual frame range)

Type:

    

[`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 2
items in [-inf, inf], default (0.0, 0.0)

frame_start¶

    

The start frame of the manually set intended playback range

Type:

    

float in [-1.04857e+06, 1.04857e+06], default 0.0

groups¶

    

Legacy API, for backward compatibility with code that does not handle slotted
actions yet. This collection contains the F-Curve groups for the action’s
first slot

Type:

    

[`ActionGroups`](bpy.types.ActionGroups.html#bpy.types.ActionGroups
"bpy.types.ActionGroups")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`ActionGroup`](bpy.types.ActionGroup.html#bpy.types.ActionGroup
"bpy.types.ActionGroup"), (readonly)

id_root¶

    

Legacy API, for backward compatibility with code that does not handle slotted
actions yet. Type of data-block that the action’s first slot can be used on.
Do not change unless you know what you are doing

  * `ACTION` Action.

  * `ARMATURE` Armature.

  * `BRUSH` Brush.

  * `CACHEFILE` Cache File.

  * `CAMERA` Camera.

  * `COLLECTION` Collection.

  * `CURVE` Curve.

  * `CURVES` Curves.

  * `FONT` Font.

  * `GREASEPENCIL` Grease Pencil.

  * `GREASEPENCIL_V3` Grease Pencil v3.

  * `IMAGE` Image.

  * `KEY` Key.

  * `LATTICE` Lattice.

  * `LIBRARY` Library.

  * `LIGHT` Light.

  * `LIGHT_PROBE` Light Probe.

  * `LINESTYLE` Line Style.

  * `MASK` Mask.

  * `MATERIAL` Material.

  * `MESH` Mesh.

  * `META` Metaball.

  * `MOVIECLIP` Movie Clip.

  * `NODETREE` Node Tree.

  * `OBJECT` Object.

  * `PAINTCURVE` Paint Curve.

  * `PALETTE` Palette.

  * `PARTICLE` Particle.

  * `POINTCLOUD` Point Cloud.

  * `SCENE` Scene.

  * `SCREEN` Screen.

  * `SOUND` Sound.

  * `SPEAKER` Speaker.

  * `TEXT` Text.

  * `TEXTURE` Texture.

  * `VOLUME` Volume.

  * `WINDOWMANAGER` Window Manager.

  * `WORKSPACE` Workspace.

  * `WORLD` World.

  * `UNSPECIFIED` Unspecified – Not yet specified. When this slot is first assigned to a data-block, this will be set to the type of that data-block.

Type:

    

enum in [`ACTION`, `ARMATURE`, `BRUSH`, `CACHEFILE`, `CAMERA`, `COLLECTION`,
`CURVE`, `CURVES`, `FONT`, `GREASEPENCIL`, `GREASEPENCIL_V3`, `IMAGE`, `KEY`,
`LATTICE`, `LIBRARY`, `LIGHT`, `LIGHT_PROBE`, `LINESTYLE`, `MASK`, `MATERIAL`,
`MESH`, `META`, `MOVIECLIP`, `NODETREE`, `OBJECT`, `PAINTCURVE`, `PALETTE`,
`PARTICLE`, `POINTCLOUD`, `SCENE`, `SCREEN`, `SOUND`, `SPEAKER`, `TEXT`,
`TEXTURE`, `VOLUME`, `WINDOWMANAGER`, `WORKSPACE`, `WORLD`, `UNSPECIFIED`],
default `UNSPECIFIED`

is_action_layered¶

    

Return whether this is a layered Action. An empty Action is considered as both
a ‘legacy’ and a ‘layered’ Action.

Type:

    

boolean, default False, (readonly)

is_action_legacy¶

    

Return whether this is a legacy Action. Legacy Actions have no layers or
slots. An empty Action is considered as both a ‘legacy’ and a ‘layered’
Action. Since Blender 4.4 actions are automatically updated to layered
actions, and thus this will only return True when the action is empty

Type:

    

boolean, default False, (readonly)

is_empty¶

    

False when there is any Layer, Slot, or legacy F-Curve

Type:

    

boolean, default False, (readonly)

layers¶

    

The list of layers that make up this Action

Type:

    

[`ActionLayers`](bpy.types.ActionLayers.html#bpy.types.ActionLayers
"bpy.types.ActionLayers")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`ActionLayer`](bpy.types.ActionLayer.html#bpy.types.ActionLayer
"bpy.types.ActionLayer"), (readonly)

pose_markers¶

    

Markers specific to this action, for labeling poses

Type:

    

[`ActionPoseMarkers`](bpy.types.ActionPoseMarkers.html#bpy.types.ActionPoseMarkers
"bpy.types.ActionPoseMarkers")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`TimelineMarker`](bpy.types.TimelineMarker.html#bpy.types.TimelineMarker
"bpy.types.TimelineMarker"), (readonly)

slots¶

    

The list of slots in this Action

Type:

    

[`ActionSlots`](bpy.types.ActionSlots.html#bpy.types.ActionSlots
"bpy.types.ActionSlots")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`ActionSlot`](bpy.types.ActionSlot.html#bpy.types.ActionSlot
"bpy.types.ActionSlot"), (readonly)

use_cyclic¶

    

The action is intended to be used as a cycle looping over its manually set
playback frame range (enabling this doesn’t automatically make it loop)

Type:

    

boolean, default False

use_frame_range¶

    

Manually specify the intended playback frame range for the action (this range
is used by some tools, but does not affect animation evaluation)

Type:

    

boolean, default False

deselect_keys()¶

    

Deselects all keys of the Action. The selection status of F-Curves is
unchanged.

fcurve_ensure_for_datablock(_datablock_ , _data_path_ , _*_ , _index =0_)¶

    

Ensure that an F-Curve exists, with the given data path and array index, for
the given data-block. This action must already be assigned to the data-block.
This function will also create the layer, keyframe strip, and action slot if
necessary, and take care of assigning the action slot too

Parameters:

    

  * **datablock** ([`ID`](bpy.types.ID.html#bpy.types.ID "bpy.types.ID"), (never None)) – The data-block animated by this action, for which to ensure the F-Curve exists. This action must already be assigned to the data-block

  * **data_path** (_string_ _,__(__never None_ _)_) – Data Path, F-Curve data path

  * **index** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Index, Array index

Returns:

    

The found or created F-Curve

Return type:

    

[`FCurve`](bpy.types.FCurve.html#bpy.types.FCurve "bpy.types.FCurve")

flip_with_pose(_object_)¶

    

Flip the action around the X axis using a pose

Parameters:

    

**object** ([`Object`](bpy.types.Object.html#bpy.types.Object
"bpy.types.Object"), (never None)) – The reference armature object to use when
flipping

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

  * [`bpy.context.active_action`](bpy.context.html#bpy.context.active_action "bpy.context.active_action")
  * [`bpy.context.selected_editable_actions`](bpy.context.html#bpy.context.selected_editable_actions "bpy.context.selected_editable_actions")
  * [`bpy.context.selected_visible_actions`](bpy.context.html#bpy.context.selected_visible_actions "bpy.context.selected_visible_actions")
  * [`ActionConstraint.action`](bpy.types.ActionConstraint.html#bpy.types.ActionConstraint.action "bpy.types.ActionConstraint.action")
  * [`AnimData.action`](bpy.types.AnimData.html#bpy.types.AnimData.action "bpy.types.AnimData.action")
  * [`AnimData.action_tweak_storage`](bpy.types.AnimData.html#bpy.types.AnimData.action_tweak_storage "bpy.types.AnimData.action_tweak_storage")
  * [`BlendData.actions`](bpy.types.BlendData.html#bpy.types.BlendData.actions "bpy.types.BlendData.actions")
  * [`BlendDataActions.new`](bpy.types.BlendDataActions.html#bpy.types.BlendDataActions.new "bpy.types.BlendDataActions.new")
  * [`BlendDataActions.remove`](bpy.types.BlendDataActions.html#bpy.types.BlendDataActions.remove "bpy.types.BlendDataActions.remove")

|

  * `GLTF2_filter_action.action`
  * [`NlaStrip.action`](bpy.types.NlaStrip.html#bpy.types.NlaStrip.action "bpy.types.NlaStrip.action")
  * [`NlaStrips.new`](bpy.types.NlaStrips.html#bpy.types.NlaStrips.new "bpy.types.NlaStrips.new")
  * [`Pose.apply_pose_from_action`](bpy.types.Pose.html#bpy.types.Pose.apply_pose_from_action "bpy.types.Pose.apply_pose_from_action")
  * [`Pose.backup_create`](bpy.types.Pose.html#bpy.types.Pose.backup_create "bpy.types.Pose.backup_create")
  * [`Pose.blend_pose_from_action`](bpy.types.Pose.html#bpy.types.Pose.blend_pose_from_action "bpy.types.Pose.blend_pose_from_action")
  * [`SpaceDopeSheetEditor.action`](bpy.types.SpaceDopeSheetEditor.html#bpy.types.SpaceDopeSheetEditor.action "bpy.types.SpaceDopeSheetEditor.action")
  * [`WindowManager.poselib_previous_action`](bpy.types.WindowManager.html#bpy.types.WindowManager.poselib_previous_action "bpy.types.WindowManager.poselib_previous_action")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

