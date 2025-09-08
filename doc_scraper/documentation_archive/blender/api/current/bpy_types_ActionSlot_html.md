---
url: https://docs.blender.org/api/current/bpy.types.ActionSlot.html
scraped_at: 2025-09-08T14:19:22.790136
title: ActionSlot(bpy_struct)¶
---

# ActionSlot(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.ActionSlot(_bpy_struct_)¶

    

Identifier for a set of channels in this Action, that can be used by a data-
block to specify what it gets animated by

active¶

    

Whether this is the active slot, can be set by assigning to
action.slots.active

Type:

    

boolean, default False, (readonly)

handle¶

    

Number specific to this Slot, unique within the Action. This is used, for
example, on a ActionKeyframeStrip to look up the ActionChannelbag for this
Slot

Type:

    

int in [-inf, inf], default 0, (readonly)

identifier¶

    

Used when connecting an Action to a data-block, to find the correct slot
handle. This is the display name, prefixed by two characters determined by the
slot’s ID type

Type:

    

string, default “”, (never None)

name_display¶

    

Name of the slot, for display in the user interface. This name combined with
the slot’s data-block type is unique within its Action

Type:

    

string, default “”, (never None)

select¶

    

Selection state of the slot

Type:

    

boolean, default False

show_expanded¶

    

Expanded state of the slot

Type:

    

boolean, default False

target_id_type¶

    

Type of data-block that this slot is intended to animate; can be set when
‘UNSPECIFIED’ but is otherwise read-only

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

target_id_type_icon¶

    

Type:

    

int in [-inf, inf], default 0, (readonly)

users()¶

    

Return the data-blocks that are animated by this slot of this action

Returns:

    

users

Return type:

    

[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of [`ID`](bpy.types.ID.html#bpy.types.ID
"bpy.types.ID")

duplicate()¶

    

Duplicate this slot, including all the animation data associated with it

Returns:

    

Duplicated Slot, The slot created by duplicating this one

Return type:

    

`ActionSlot`

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

  * [`Action.slots`](bpy.types.Action.html#bpy.types.Action.slots "bpy.types.Action.slots")
  * [`ActionChannelbag.slot`](bpy.types.ActionChannelbag.html#bpy.types.ActionChannelbag.slot "bpy.types.ActionChannelbag.slot")
  * [`ActionChannelbags.new`](bpy.types.ActionChannelbags.html#bpy.types.ActionChannelbags.new "bpy.types.ActionChannelbags.new")
  * [`ActionConstraint.action_slot`](bpy.types.ActionConstraint.html#bpy.types.ActionConstraint.action_slot "bpy.types.ActionConstraint.action_slot")
  * [`ActionConstraint.action_suitable_slots`](bpy.types.ActionConstraint.html#bpy.types.ActionConstraint.action_suitable_slots "bpy.types.ActionConstraint.action_suitable_slots")
  * [`ActionKeyframeStrip.channelbag`](bpy.types.ActionKeyframeStrip.html#bpy.types.ActionKeyframeStrip.channelbag "bpy.types.ActionKeyframeStrip.channelbag")
  * [`ActionKeyframeStrip.key_insert`](bpy.types.ActionKeyframeStrip.html#bpy.types.ActionKeyframeStrip.key_insert "bpy.types.ActionKeyframeStrip.key_insert")
  * `ActionSlot.duplicate`

|

  * [`ActionSlots.active`](bpy.types.ActionSlots.html#bpy.types.ActionSlots.active "bpy.types.ActionSlots.active")
  * [`ActionSlots.new`](bpy.types.ActionSlots.html#bpy.types.ActionSlots.new "bpy.types.ActionSlots.new")
  * [`ActionSlots.remove`](bpy.types.ActionSlots.html#bpy.types.ActionSlots.remove "bpy.types.ActionSlots.remove")
  * [`AnimData.action_slot`](bpy.types.AnimData.html#bpy.types.AnimData.action_slot "bpy.types.AnimData.action_slot")
  * [`AnimData.action_suitable_slots`](bpy.types.AnimData.html#bpy.types.AnimData.action_suitable_slots "bpy.types.AnimData.action_suitable_slots")
  * [`NlaStrip.action_slot`](bpy.types.NlaStrip.html#bpy.types.NlaStrip.action_slot "bpy.types.NlaStrip.action_slot")
  * [`NlaStrip.action_suitable_slots`](bpy.types.NlaStrip.html#bpy.types.NlaStrip.action_suitable_slots "bpy.types.NlaStrip.action_suitable_slots")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

