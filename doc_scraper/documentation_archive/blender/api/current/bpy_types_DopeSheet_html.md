---
url: https://docs.blender.org/api/current/bpy.types.DopeSheet.html
scraped_at: 2025-09-08T14:24:38.030597
title: DopeSheet(bpy_struct)¶
---

# DopeSheet(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.DopeSheet(_bpy_struct_)¶

    

Settings for filtering the channels shown in animation editors

filter_collection¶

    

Collection that included object should be a member of

Type:

    

[`Collection`](bpy.types.Collection.html#bpy.types.Collection
"bpy.types.Collection")

filter_fcurve_name¶

    

F-Curve live filtering string

Type:

    

string, default “”, (never None)

filter_text¶

    

Live filtering string

Type:

    

string, default “”, (never None)

show_armatures¶

    

Include visualization of armature related animation data

Type:

    

boolean, default False

show_cache_files¶

    

Include visualization of cache file related animation data

Type:

    

boolean, default False

show_cameras¶

    

Include visualization of camera related animation data

Type:

    

boolean, default False

show_curves¶

    

Include visualization of curve related animation data

Type:

    

boolean, default False

show_datablock_filters¶

    

Show options for whether channels related to certain types of data are
included

Type:

    

boolean, default False

show_driver_fallback_as_error¶

    

Include drivers that relied on any fallback values for their evaluation in the
Only Show Errors filter, even if the driver evaluation succeeded

Type:

    

boolean, default False

show_expanded_summary¶

    

Collapse summary when shown, so all other channels get hidden (Dope Sheet
editors only)

Type:

    

boolean, default False

show_gpencil¶

    

Include visualization of Grease Pencil related animation data and frames

Type:

    

boolean, default False

show_hair_curves¶

    

Include visualization of hair related animation data

Type:

    

boolean, default False

show_hidden¶

    

Include channels from objects/bone that are not visible

Type:

    

boolean, default False

show_lattices¶

    

Include visualization of lattice related animation data

Type:

    

boolean, default False

show_lightprobes¶

    

Include visualization of lightprobe related animation data

Type:

    

boolean, default False

show_lights¶

    

Include visualization of light related animation data

Type:

    

boolean, default False

show_linestyles¶

    

Include visualization of Line Style related Animation data

Type:

    

boolean, default False

show_materials¶

    

Include visualization of material related animation data

Type:

    

boolean, default False

show_meshes¶

    

Include visualization of mesh related animation data

Type:

    

boolean, default False

show_metaballs¶

    

Include visualization of metaball related animation data

Type:

    

boolean, default False

show_missing_nla¶

    

Include animation data-blocks with no NLA data (NLA editor only)

Type:

    

boolean, default False

show_modifiers¶

    

Include visualization of animation data related to data-blocks linked to
modifiers

Type:

    

boolean, default False

show_movieclips¶

    

Include visualization of movie clip related animation data

Type:

    

boolean, default False

show_nodes¶

    

Include visualization of node related animation data

Type:

    

boolean, default False

show_only_errors¶

    

Only include F-Curves and drivers that are disabled or have errors

Type:

    

boolean, default False

show_only_selected¶

    

Only include channels relating to selected objects and data

Type:

    

boolean, default False

show_only_slot_of_active_object¶

    

Only show the slot of the active Object. Otherwise show all the Action’s Slots

Type:

    

boolean, default False

show_particles¶

    

Include visualization of particle related animation data

Type:

    

boolean, default False

show_pointclouds¶

    

Include visualization of point cloud related animation data

Type:

    

boolean, default False

show_scenes¶

    

Include visualization of scene related animation data

Type:

    

boolean, default False

show_shapekeys¶

    

Include visualization of shape key related animation data

Type:

    

boolean, default False

show_speakers¶

    

Include visualization of speaker related animation data

Type:

    

boolean, default False

show_summary¶

    

Display an additional ‘summary’ line (Dope Sheet editors only)

Type:

    

boolean, default False

show_textures¶

    

Include visualization of texture related animation data

Type:

    

boolean, default False

show_transforms¶

    

Include visualization of object-level animation data (mostly transforms)

Type:

    

boolean, default False

show_volumes¶

    

Include visualization of volume related animation data

Type:

    

boolean, default False

show_worlds¶

    

Include visualization of world related animation data

Type:

    

boolean, default False

source¶

    

ID-Block representing source data, usually ID_SCE (i.e. Scene)

Type:

    

[`ID`](bpy.types.ID.html#bpy.types.ID "bpy.types.ID"), (readonly)

use_datablock_sort¶

    

Alphabetically sorts data-blocks - mainly objects in the scene (disable to
increase viewport speed)

Type:

    

boolean, default False

use_filter_invert¶

    

Invert filter search

Type:

    

boolean, default False

use_multi_word_filter¶

    

Perform fuzzy/multi-word matching. Warning: May be slow

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

  * [`SpaceDopeSheetEditor.dopesheet`](bpy.types.SpaceDopeSheetEditor.html#bpy.types.SpaceDopeSheetEditor.dopesheet "bpy.types.SpaceDopeSheetEditor.dopesheet")
  * [`SpaceGraphEditor.dopesheet`](bpy.types.SpaceGraphEditor.html#bpy.types.SpaceGraphEditor.dopesheet "bpy.types.SpaceGraphEditor.dopesheet")

|

  * [`SpaceNLA.dopesheet`](bpy.types.SpaceNLA.html#bpy.types.SpaceNLA.dopesheet "bpy.types.SpaceNLA.dopesheet")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

