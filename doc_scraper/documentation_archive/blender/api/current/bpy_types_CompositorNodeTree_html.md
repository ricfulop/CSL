---
url: https://docs.blender.org/api/current/bpy.types.CompositorNodeTree.html
scraped_at: 2025-09-08T14:23:53.782938
title: CompositorNodeTree(NodeTree)¶
---

# CompositorNodeTree(NodeTree)¶  
  
base classes — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct"), [`ID`](bpy.types.ID.html#bpy.types.ID
"bpy.types.ID"), [`NodeTree`](bpy.types.NodeTree.html#bpy.types.NodeTree
"bpy.types.NodeTree")

_class _bpy.types.CompositorNodeTree(_NodeTree_)¶

    

Node tree consisting of linked nodes used for compositing

use_viewer_border¶

    

Use boundaries for viewer nodes and composite backdrop

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
  * [`ID.is_missing`](bpy.types.ID.html#bpy.types.ID.is_missing "bpy.types.ID.is_missing")
  * [`ID.is_runtime_data`](bpy.types.ID.html#bpy.types.ID.is_runtime_data "bpy.types.ID.is_runtime_data")
  * [`ID.is_editable`](bpy.types.ID.html#bpy.types.ID.is_editable "bpy.types.ID.is_editable")
  * [`ID.tag`](bpy.types.ID.html#bpy.types.ID.tag "bpy.types.ID.tag")
  * [`ID.is_library_indirect`](bpy.types.ID.html#bpy.types.ID.is_library_indirect "bpy.types.ID.is_library_indirect")
  * [`ID.library`](bpy.types.ID.html#bpy.types.ID.library "bpy.types.ID.library")
  * [`ID.library_weak_reference`](bpy.types.ID.html#bpy.types.ID.library_weak_reference "bpy.types.ID.library_weak_reference")

|

  * [`ID.asset_data`](bpy.types.ID.html#bpy.types.ID.asset_data "bpy.types.ID.asset_data")
  * [`ID.override_library`](bpy.types.ID.html#bpy.types.ID.override_library "bpy.types.ID.override_library")
  * [`ID.preview`](bpy.types.ID.html#bpy.types.ID.preview "bpy.types.ID.preview")
  * [`NodeTree.color_tag`](bpy.types.NodeTree.html#bpy.types.NodeTree.color_tag "bpy.types.NodeTree.color_tag")
  * [`NodeTree.default_group_node_width`](bpy.types.NodeTree.html#bpy.types.NodeTree.default_group_node_width "bpy.types.NodeTree.default_group_node_width")
  * [`NodeTree.view_center`](bpy.types.NodeTree.html#bpy.types.NodeTree.view_center "bpy.types.NodeTree.view_center")
  * [`NodeTree.description`](bpy.types.NodeTree.html#bpy.types.NodeTree.description "bpy.types.NodeTree.description")
  * [`NodeTree.animation_data`](bpy.types.NodeTree.html#bpy.types.NodeTree.animation_data "bpy.types.NodeTree.animation_data")
  * [`NodeTree.nodes`](bpy.types.NodeTree.html#bpy.types.NodeTree.nodes "bpy.types.NodeTree.nodes")
  * [`NodeTree.links`](bpy.types.NodeTree.html#bpy.types.NodeTree.links "bpy.types.NodeTree.links")
  * [`NodeTree.grease_pencil`](bpy.types.NodeTree.html#bpy.types.NodeTree.grease_pencil "bpy.types.NodeTree.grease_pencil")
  * [`NodeTree.type`](bpy.types.NodeTree.html#bpy.types.NodeTree.type "bpy.types.NodeTree.type")
  * [`NodeTree.interface`](bpy.types.NodeTree.html#bpy.types.NodeTree.interface "bpy.types.NodeTree.interface")
  * [`NodeTree.bl_idname`](bpy.types.NodeTree.html#bpy.types.NodeTree.bl_idname "bpy.types.NodeTree.bl_idname")
  * [`NodeTree.bl_label`](bpy.types.NodeTree.html#bpy.types.NodeTree.bl_label "bpy.types.NodeTree.bl_label")
  * [`NodeTree.bl_description`](bpy.types.NodeTree.html#bpy.types.NodeTree.bl_description "bpy.types.NodeTree.bl_description")
  * [`NodeTree.bl_icon`](bpy.types.NodeTree.html#bpy.types.NodeTree.bl_icon "bpy.types.NodeTree.bl_icon")
  * [`NodeTree.bl_use_group_interface`](bpy.types.NodeTree.html#bpy.types.NodeTree.bl_use_group_interface "bpy.types.NodeTree.bl_use_group_interface")

  
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
  * [`bpy_struct.type_recast`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.type_recast "bpy.types.bpy_struct.type_recast")
  * [`bpy_struct.values`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.values "bpy.types.bpy_struct.values")
  * [`ID.rename`](bpy.types.ID.html#bpy.types.ID.rename "bpy.types.ID.rename")
  * [`ID.evaluated_get`](bpy.types.ID.html#bpy.types.ID.evaluated_get "bpy.types.ID.evaluated_get")

|

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
  * [`NodeTree.interface_update`](bpy.types.NodeTree.html#bpy.types.NodeTree.interface_update "bpy.types.NodeTree.interface_update")
  * [`NodeTree.contains_tree`](bpy.types.NodeTree.html#bpy.types.NodeTree.contains_tree "bpy.types.NodeTree.contains_tree")
  * [`NodeTree.poll`](bpy.types.NodeTree.html#bpy.types.NodeTree.poll "bpy.types.NodeTree.poll")
  * [`NodeTree.update`](bpy.types.NodeTree.html#bpy.types.NodeTree.update "bpy.types.NodeTree.update")
  * [`NodeTree.get_from_context`](bpy.types.NodeTree.html#bpy.types.NodeTree.get_from_context "bpy.types.NodeTree.get_from_context")
  * [`NodeTree.valid_socket_type`](bpy.types.NodeTree.html#bpy.types.NodeTree.valid_socket_type "bpy.types.NodeTree.valid_socket_type")
  * [`NodeTree.debug_lazy_function_graph`](bpy.types.NodeTree.html#bpy.types.NodeTree.debug_lazy_function_graph "bpy.types.NodeTree.debug_lazy_function_graph")
  * [`NodeTree.bl_rna_get_subclass`](bpy.types.NodeTree.html#bpy.types.NodeTree.bl_rna_get_subclass "bpy.types.NodeTree.bl_rna_get_subclass")
  * [`NodeTree.bl_rna_get_subclass_py`](bpy.types.NodeTree.html#bpy.types.NodeTree.bl_rna_get_subclass_py "bpy.types.NodeTree.bl_rna_get_subclass_py")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

