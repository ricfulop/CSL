---
url: https://docs.blender.org/api/current/bpy.ops.node.html
scraped_at: 2025-09-08T14:18:30.658408
title: Node Operators¶
---

# Node Operators¶

bpy.ops.node.activate_viewer()¶

    

Activate selected viewer node in compositor and geometry nodes

bpy.ops.node.add_closure_zone(_*_ , _use_transform =False_, _settings =None_,
_offset =(150.0, 0.0)_)¶

    

Add a Closure zone

Parameters:

    

  * **use_transform** (_boolean_ _,__(__optional_ _)_) – Use Transform, Start transform operator after inserting the node

  * **settings** (`bpy_prop_collection` of `NodeSetting`, (optional)) – Settings, Settings to be applied on the newly created node

  * **offset** (_float array_ _of_ _2 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Offset, Offset of nodes from the cursor when added

File:

    

[startup/bl_operators/node.py:218](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L218)

bpy.ops.node.add_collection(_*_ , _name =''_, _session_uid =0_)¶

    

Add a collection info node to the current node editor

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the data-block to use by the operator

  * **session_uid** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

bpy.ops.node.add_color(_*_ , _color =(0.0, 0.0, 0.0, 0.0)_, _gamma =False_,
_has_alpha =False_)¶

    

Add a color node to the current node editor

Parameters:

    

  * **color** (_float array_ _of_ _4 items in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Color, Source color

  * **gamma** (_boolean_ _,__(__optional_ _)_) – Gamma Corrected, The source color is gamma corrected

  * **has_alpha** (_boolean_ _,__(__optional_ _)_) – Has Alpha, The source color contains an Alpha component

bpy.ops.node.add_empty_group(_*_ , _use_transform =False_, _settings =None_)¶

    

Add a group node with an empty group

Parameters:

    

  * **use_transform** (_boolean_ _,__(__optional_ _)_) – Use Transform, Start transform operator after inserting the node

  * **settings** (`bpy_prop_collection` of `NodeSetting`, (optional)) – Settings, Settings to be applied on the newly created node

File:

    

[startup/bl_operators/node.py:185](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L185)

bpy.ops.node.add_foreach_geometry_element_zone(_*_ , _use_transform =False_,
_settings =None_, _offset =(150.0, 0.0)_)¶

    

Add a For Each Geometry Element zone that allows executing nodes e.g. for each
vertex separately

Parameters:

    

  * **use_transform** (_boolean_ _,__(__optional_ _)_) – Use Transform, Start transform operator after inserting the node

  * **settings** (`bpy_prop_collection` of `NodeSetting`, (optional)) – Settings, Settings to be applied on the newly created node

  * **offset** (_float array_ _of_ _2 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Offset, Offset of nodes from the cursor when added

File:

    

[startup/bl_operators/node.py:218](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L218)

bpy.ops.node.add_group(_*_ , _name =''_, _session_uid =0_,
_show_datablock_in_node =True_)¶

    

Add an existing node group to the current node editor

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the data-block to use by the operator

  * **session_uid** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

  * **show_datablock_in_node** (_boolean_ _,__(__optional_ _)_) – Show the datablock selector in the node

bpy.ops.node.add_group_asset(_*_ , _asset_library_type =LOCAL_,
_asset_library_identifier =''_, _relative_asset_identifier =''_)¶

    

Add a node group asset to the active node tree

Parameters:

    

  * **asset_library_type** (enum in [Asset Library Type Items](bpy_types_enum_items/asset_library_type_items.html#rna-enum-asset-library-type-items), (optional)) – Asset Library Type

  * **asset_library_identifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Asset Library Identifier

  * **relative_asset_identifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Relative Asset Identifier

bpy.ops.node.add_group_input_node(_*_ , _socket_identifier =''_,
_panel_identifier =0_)¶

    

Add a Group Input node with selected sockets to the current node editor

Parameters:

    

  * **socket_identifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Socket Identifier, Socket to include in the added group input/output node

  * **panel_identifier** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Panel Identifier, Panel from which to add sockets to the added group input/output node

bpy.ops.node.add_image(_*_ , _filepath =''_, _directory =''_, _files =None_,
_hide_props_region =True_, _check_existing =False_, _filter_blender =False_,
_filter_backup =False_, _filter_image =True_, _filter_movie =True_,
_filter_python =False_, _filter_font =False_, _filter_sound =False_,
_filter_text =False_, _filter_archive =False_, _filter_btx =False_,
_filter_collada =False_, _filter_alembic =False_, _filter_usd =False_,
_filter_obj =False_, _filter_volume =False_, _filter_folder =True_,
_filter_blenlib =False_, _filemode =9_, _relative_path =True_, _show_multiview
=False_, _use_multiview =False_, _display_type =DEFAULT_, _sort_method_ ,
_name =''_, _session_uid =0_)¶

    

Add a image/movie file as node to the current node editor

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Directory, Directory of the file

  * **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – Files

  * **hide_props_region** (_boolean_ _,__(__optional_ _)_) – Hide Operator Properties, Collapse the region displaying the operator settings

  * **check_existing** (_boolean_ _,__(__optional_ _)_) – Check Existing, Check and warn on overwriting existing files

  * **filter_blender** (_boolean_ _,__(__optional_ _)_) – Filter .blend files

  * **filter_backup** (_boolean_ _,__(__optional_ _)_) – Filter .blend files

  * **filter_image** (_boolean_ _,__(__optional_ _)_) – Filter image files

  * **filter_movie** (_boolean_ _,__(__optional_ _)_) – Filter movie files

  * **filter_python** (_boolean_ _,__(__optional_ _)_) – Filter Python files

  * **filter_font** (_boolean_ _,__(__optional_ _)_) – Filter font files

  * **filter_sound** (_boolean_ _,__(__optional_ _)_) – Filter sound files

  * **filter_text** (_boolean_ _,__(__optional_ _)_) – Filter text files

  * **filter_archive** (_boolean_ _,__(__optional_ _)_) – Filter archive files

  * **filter_btx** (_boolean_ _,__(__optional_ _)_) – Filter btx files

  * **filter_collada** (_boolean_ _,__(__optional_ _)_) – Filter COLLADA files

  * **filter_alembic** (_boolean_ _,__(__optional_ _)_) – Filter Alembic files

  * **filter_usd** (_boolean_ _,__(__optional_ _)_) – Filter USD files

  * **filter_obj** (_boolean_ _,__(__optional_ _)_) – Filter OBJ files

  * **filter_volume** (_boolean_ _,__(__optional_ _)_) – Filter OpenVDB volume files

  * **filter_folder** (_boolean_ _,__(__optional_ _)_) – Filter folders

  * **filter_blenlib** (_boolean_ _,__(__optional_ _)_) – Filter Blender IDs

  * **filemode** (_int in_ _[__1_ _,__9_ _]__,__(__optional_ _)_) – File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

  * **relative_path** (_boolean_ _,__(__optional_ _)_) – Relative Path, Select the file relative to the blend file

  * **show_multiview** (_boolean_ _,__(__optional_ _)_) – Enable Multi-View

  * **use_multiview** (_boolean_ _,__(__optional_ _)_) – Use Multi-View

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (enum in [`DEFAULT`, `FILE_SORT_ALPHA`, `FILE_SORT_EXTENSION`, `FILE_SORT_TIME`, `FILE_SORT_SIZE`, `ASSET_CATALOG`], (optional)) – 

File sorting mode

    * `DEFAULT` Default – Automatically determine sort method for files.

    * `FILE_SORT_ALPHA` Name – Sort the file list alphabetically.

    * `FILE_SORT_EXTENSION` Extension – Sort the file list by extension/type.

    * `FILE_SORT_TIME` Modified Date – Sort files by modification time.

    * `FILE_SORT_SIZE` Size – Sort files by size.

    * `ASSET_CATALOG` Asset Catalog – Sort the asset list so that assets in the same catalog are kept together. Within a single catalog, assets are ordered by name. The catalogs are in order of the flattened catalog hierarchy..

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the data-block to use by the operator

  * **session_uid** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

bpy.ops.node.add_import_node(_*_ , _directory =''_, _files =None_)¶

    

Add an import node to the node tree

Parameters:

    

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Directory, Directory of the file

  * **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – Files

bpy.ops.node.add_mask(_*_ , _name =''_, _session_uid =0_)¶

    

Add a mask node to the current node editor

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the data-block to use by the operator

  * **session_uid** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

bpy.ops.node.add_material(_*_ , _name =''_, _session_uid =0_)¶

    

Add a material node to the current node editor

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the data-block to use by the operator

  * **session_uid** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

bpy.ops.node.add_node(_*_ , _use_transform =False_, _settings =None_, _type
=''_, _visible_output =''_)¶

    

Add a node to the active tree

Parameters:

    

  * **use_transform** (_boolean_ _,__(__optional_ _)_) – Use Transform, Start transform operator after inserting the node

  * **settings** (`bpy_prop_collection` of `NodeSetting`, (optional)) – Settings, Settings to be applied on the newly created node

  * **type** (_string_ _,__(__optional_ _,__never None_ _)_) – Node Type, Node type

  * **visible_output** (_string_ _,__(__optional_ _,__never None_ _)_) – Output Name, If provided, all outputs that are named differently will be hidden

File:

    

[startup/bl_operators/node.py:149](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L149)

bpy.ops.node.add_object(_*_ , _name =''_, _session_uid =0_)¶

    

Add an object info node to the current node editor

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the data-block to use by the operator

  * **session_uid** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

bpy.ops.node.add_repeat_zone(_*_ , _use_transform =False_, _settings =None_,
_offset =(150.0, 0.0)_)¶

    

Add a repeat zone that allows executing nodes a dynamic number of times

Parameters:

    

  * **use_transform** (_boolean_ _,__(__optional_ _)_) – Use Transform, Start transform operator after inserting the node

  * **settings** (`bpy_prop_collection` of `NodeSetting`, (optional)) – Settings, Settings to be applied on the newly created node

  * **offset** (_float array_ _of_ _2 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Offset, Offset of nodes from the cursor when added

File:

    

[startup/bl_operators/node.py:218](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L218)

bpy.ops.node.add_reroute(_*_ , _path =None_, _cursor =11_)¶

    

Add a reroute node

Parameters:

    

  * **path** (`bpy_prop_collection` of `OperatorMousePath`, (optional)) – Path

  * **cursor** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Cursor

bpy.ops.node.add_simulation_zone(_*_ , _use_transform =False_, _settings
=None_, _offset =(150.0, 0.0)_)¶

    

Add simulation zone input and output nodes to the active tree

Parameters:

    

  * **use_transform** (_boolean_ _,__(__optional_ _)_) – Use Transform, Start transform operator after inserting the node

  * **settings** (`bpy_prop_collection` of `NodeSetting`, (optional)) – Settings, Settings to be applied on the newly created node

  * **offset** (_float array_ _of_ _2 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Offset, Offset of nodes from the cursor when added

File:

    

[startup/bl_operators/node.py:218](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L218)

bpy.ops.node.attach()¶

    

Attach active node to a frame

bpy.ops.node.backimage_fit()¶

    

Fit the background image to the view

bpy.ops.node.backimage_move()¶

    

Move node backdrop

bpy.ops.node.backimage_sample()¶

    

Use mouse to sample background image

bpy.ops.node.backimage_zoom(_*_ , _factor =1.2_)¶

    

Zoom in/out the background image

Parameters:

    

**factor** (_float in_ _[__0_ _,__10_ _]__,__(__optional_ _)_) – Factor

bpy.ops.node.bake_node_item_add()¶

    

Add item below active item

bpy.ops.node.bake_node_item_move(_*_ , _direction =UP_)¶

    

Move active item

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Direction, Move direction

bpy.ops.node.bake_node_item_remove()¶

    

Remove active item

bpy.ops.node.capture_attribute_item_add()¶

    

Add item below active item

bpy.ops.node.capture_attribute_item_move(_*_ , _direction =UP_)¶

    

Move active item

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Direction, Move direction

bpy.ops.node.capture_attribute_item_remove()¶

    

Remove active item

bpy.ops.node.clear_viewer_border()¶

    

Clear the boundaries for viewer operations

bpy.ops.node.clipboard_copy()¶

    

Copy the selected nodes to the internal clipboard

bpy.ops.node.clipboard_paste(_*_ , _offset =(0.0, 0.0)_)¶

    

Paste nodes from the internal clipboard to the active node tree

Parameters:

    

**offset** (_float array_ _of_ _2 items in_ _[__-inf_ _,__inf_
_]__,__(__optional_ _)_) – Location, The 2D view location for the center of
the new nodes, or unchanged if not set

bpy.ops.node.closure_input_item_add()¶

    

Add item below active item

bpy.ops.node.closure_input_item_move(_*_ , _direction =UP_)¶

    

Move active item

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Direction, Move direction

bpy.ops.node.closure_input_item_remove()¶

    

Remove active item

bpy.ops.node.closure_output_item_add()¶

    

Add item below active item

bpy.ops.node.closure_output_item_move(_*_ , _direction =UP_)¶

    

Move active item

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Direction, Move direction

bpy.ops.node.closure_output_item_remove()¶

    

Remove active item

bpy.ops.node.collapse_hide_unused_toggle()¶

    

Toggle collapsed nodes and hide unused sockets

File:

    

[startup/bl_operators/node.py:299](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L299)

bpy.ops.node.combine_bundle_item_add()¶

    

Add item below active item

bpy.ops.node.combine_bundle_item_move(_*_ , _direction =UP_)¶

    

Move active item

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Direction, Move direction

bpy.ops.node.combine_bundle_item_remove()¶

    

Remove active item

bpy.ops.node.connect_to_output(_*_ , _run_in_geometry_nodes =True_)¶

    

Connect active node to the active output node of the node tree

Parameters:

    

**run_in_geometry_nodes** (_boolean_ _,__(__optional_ _)_) – Run in Geometry
Nodes Editor

File:

    

[startup/bl_operators/connect_to_output.py:251](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/connect_to_output.py#L251)

bpy.ops.node.cryptomatte_layer_add()¶

    

Add a new input layer to a Cryptomatte node

bpy.ops.node.cryptomatte_layer_remove()¶

    

Remove layer from a Cryptomatte node

bpy.ops.node.deactivate_viewer()¶

    

Deactivate selected viewer node in geometry nodes

bpy.ops.node.default_group_width_set()¶

    

Set the width based on the parent group node in the current context

bpy.ops.node.delete()¶

    

Remove selected nodes

bpy.ops.node.delete_reconnect()¶

    

Remove nodes and reconnect nodes as if deletion was muted

bpy.ops.node.detach()¶

    

Detach selected nodes from parents

bpy.ops.node.detach_translate_attach(_*_ , _NODE_OT_detach =None_,
_TRANSFORM_OT_translate =None_, _NODE_OT_attach =None_)¶

    

Detach nodes, move and attach to frame

Parameters:

    

  * **NODE_OT_detach** (`NODE_OT_detach`, (optional)) – Detach Nodes, Detach selected nodes from parents

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

  * **NODE_OT_attach** (`NODE_OT_attach`, (optional)) – Attach Nodes, Attach active node to a frame

bpy.ops.node.duplicate(_*_ , _keep_inputs =False_, _linked =True_)¶

    

Duplicate selected nodes

Parameters:

    

  * **keep_inputs** (_boolean_ _,__(__optional_ _)_) – Keep Inputs, Keep the input links to duplicated nodes

  * **linked** (_boolean_ _,__(__optional_ _)_) – Linked, Duplicate node but not node trees, linking to the original data

bpy.ops.node.duplicate_move(_*_ , _NODE_OT_duplicate =None_,
_NODE_OT_translate_attach =None_)¶

    

Duplicate selected nodes and move them

Parameters:

    

  * **NODE_OT_duplicate** (`NODE_OT_duplicate`, (optional)) – Duplicate Nodes, Duplicate selected nodes

  * **NODE_OT_translate_attach** (`NODE_OT_translate_attach`, (optional)) – Move and Attach, Move nodes and attach to frame

bpy.ops.node.duplicate_move_keep_inputs(_*_ , _NODE_OT_duplicate =None_,
_NODE_OT_translate_attach =None_)¶

    

Duplicate selected nodes keeping input links and move them

Parameters:

    

  * **NODE_OT_duplicate** (`NODE_OT_duplicate`, (optional)) – Duplicate Nodes, Duplicate selected nodes

  * **NODE_OT_translate_attach** (`NODE_OT_translate_attach`, (optional)) – Move and Attach, Move nodes and attach to frame

bpy.ops.node.duplicate_move_linked(_*_ , _NODE_OT_duplicate =None_,
_NODE_OT_translate_attach =None_)¶

    

Duplicate selected nodes, but not their node trees, and move them

Parameters:

    

  * **NODE_OT_duplicate** (`NODE_OT_duplicate`, (optional)) – Duplicate Nodes, Duplicate selected nodes

  * **NODE_OT_translate_attach** (`NODE_OT_translate_attach`, (optional)) – Move and Attach, Move nodes and attach to frame

bpy.ops.node.enum_definition_item_add()¶

    

Add item below active item

bpy.ops.node.enum_definition_item_move(_*_ , _direction =UP_)¶

    

Move active item

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Direction, Move direction

bpy.ops.node.enum_definition_item_remove()¶

    

Remove active item

bpy.ops.node.evaluate_closure_input_item_add()¶

    

Add item below active item

bpy.ops.node.evaluate_closure_input_item_move(_*_ , _direction =UP_)¶

    

Move active item

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Direction, Move direction

bpy.ops.node.evaluate_closure_input_item_remove()¶

    

Remove active item

bpy.ops.node.evaluate_closure_output_item_add()¶

    

Add item below active item

bpy.ops.node.evaluate_closure_output_item_move(_*_ , _direction =UP_)¶

    

Move active item

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Direction, Move direction

bpy.ops.node.evaluate_closure_output_item_remove()¶

    

Remove active item

bpy.ops.node.find_node()¶

    

Search for a node by name and focus and select it

bpy.ops.node.foreach_geometry_element_zone_generation_item_add()¶

    

Add item below active item

bpy.ops.node.foreach_geometry_element_zone_generation_item_move(_*_ ,
_direction =UP_)¶

    

Move active item

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Direction, Move direction

bpy.ops.node.foreach_geometry_element_zone_generation_item_remove()¶

    

Remove active item

bpy.ops.node.foreach_geometry_element_zone_input_item_add()¶

    

Add item below active item

bpy.ops.node.foreach_geometry_element_zone_input_item_move(_*_ , _direction
=UP_)¶

    

Move active item

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Direction, Move direction

bpy.ops.node.foreach_geometry_element_zone_input_item_remove()¶

    

Remove active item

bpy.ops.node.foreach_geometry_element_zone_main_item_add()¶

    

Add item below active item

bpy.ops.node.foreach_geometry_element_zone_main_item_move(_*_ , _direction
=UP_)¶

    

Move active item

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Direction, Move direction

bpy.ops.node.foreach_geometry_element_zone_main_item_remove()¶

    

Remove active item

bpy.ops.node.format_string_item_add()¶

    

Add item below active item

bpy.ops.node.format_string_item_move(_*_ , _direction =UP_)¶

    

Move active item

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Direction, Move direction

bpy.ops.node.format_string_item_remove()¶

    

Remove active item

bpy.ops.node.gltf_settings_node_operator()¶

    

Add a node to the active tree for glTF export

File:

    

[addons_core/io_scene_gltf2/blender/com/gltf2_blender_ui.py:35](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/io_scene_gltf2/blender/com/gltf2_blender_ui.py#L35)

bpy.ops.node.group_edit(_*_ , _exit =False_)¶

    

Edit node group

Parameters:

    

**exit** (_boolean_ _,__(__optional_ _)_) – Exit

bpy.ops.node.group_insert()¶

    

Insert selected nodes into a node group

bpy.ops.node.group_make()¶

    

Make group from selected nodes

bpy.ops.node.group_separate(_*_ , _type =COPY_)¶

    

Separate selected nodes from the node group

Parameters:

    

**type** (enum in [`COPY`, `MOVE`], (optional)) –

Type

  * `COPY` Copy – Copy to parent node tree, keep group intact.

  * `MOVE` Move – Move to parent node tree, remove from group.

bpy.ops.node.group_ungroup()¶

    

Ungroup selected nodes

bpy.ops.node.hide_socket_toggle()¶

    

Toggle unused node socket display

bpy.ops.node.hide_toggle()¶

    

Toggle hiding of selected nodes

bpy.ops.node.index_switch_item_add()¶

    

Add bake item

bpy.ops.node.index_switch_item_remove(_*_ , _index =0_)¶

    

Remove an item from the index switch

Parameters:

    

**index** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Index, Index to
remove

bpy.ops.node.insert_offset()¶

    

Automatically offset nodes on insertion

bpy.ops.node.interface_item_duplicate()¶

    

Add a copy of the active item to the interface

File:

    

[startup/bl_operators/node.py:456](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L456)

bpy.ops.node.interface_item_make_panel_toggle()¶

    

Make the active boolean socket a toggle for its parent panel

File:

    

[startup/bl_operators/node.py:527](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L527)

bpy.ops.node.interface_item_new(_*_ , _item_type_)¶

    

Add a new item to the interface

Parameters:

    

**item_type** (_enum in_ _[__]__,__(__optional_ _)_) – Item Type, Type of the
item to create

File:

    

[startup/bl_operators/node.py:399](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L399)

bpy.ops.node.interface_item_remove()¶

    

Remove active item from the interface

File:

    

[startup/bl_operators/node.py:475](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L475)

bpy.ops.node.interface_item_unlink_panel_toggle()¶

    

Make the panel toggle a stand-alone socket

File:

    

[startup/bl_operators/node.py:575](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L575)

bpy.ops.node.join()¶

    

Attach selected nodes to a new common frame

bpy.ops.node.join_named(_*_ , _NODE_OT_join =None_, _WM_OT_call_panel =None_)¶

    

Create a new frame node around the selected nodes and name it immediately

Parameters:

    

  * **NODE_OT_join** (`NODE_OT_join`, (optional)) – Join Nodes, Attach selected nodes to a new common frame

  * **WM_OT_call_panel** (`WM_OT_call_panel`, (optional)) – Call Panel, Open a predefined panel

bpy.ops.node.link(_*_ , _detach =False_, _drag_start =(0.0, 0.0)_,
_inside_padding =2.0_, _outside_padding =0.0_, _speed_ramp =1.0_, _max_speed
=26.0_, _delay =0.5_, _zoom_influence =0.5_)¶

    

Use the mouse to create a link between two nodes

Parameters:

    

  * **detach** (_boolean_ _,__(__optional_ _)_) – Detach, Detach and redirect existing links

  * **drag_start** (_float array_ _of_ _2 items in_ _[__-6_ _,__6_ _]__,__(__optional_ _)_) – Drag Start, The position of the mouse cursor at the start of the operation

  * **inside_padding** (_float in_ _[__0_ _,__100_ _]__,__(__optional_ _)_) – Inside Padding, Inside distance in UI units from the edge of the region within which to start panning

  * **outside_padding** (_float in_ _[__0_ _,__100_ _]__,__(__optional_ _)_) – Outside Padding, Outside distance in UI units from the edge of the region at which to stop panning

  * **speed_ramp** (_float in_ _[__0_ _,__100_ _]__,__(__optional_ _)_) – Speed Ramp, Width of the zone in UI units where speed increases with distance from the edge

  * **max_speed** (_float in_ _[__0_ _,__10000_ _]__,__(__optional_ _)_) – Max Speed, Maximum speed in UI units per second

  * **delay** (_float in_ _[__0_ _,__10_ _]__,__(__optional_ _)_) – Delay, Delay in seconds before maximum speed is reached

  * **zoom_influence** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Zoom Influence, Influence of the zoom factor on scroll speed

bpy.ops.node.link_make(_*_ , _replace =False_)¶

    

Make a link between selected output and input sockets

Parameters:

    

**replace** (_boolean_ _,__(__optional_ _)_) – Replace, Replace socket
connections with the new links

bpy.ops.node.link_viewer()¶

    

Link to viewer node

bpy.ops.node.links_cut(_*_ , _path =None_, _cursor =15_)¶

    

Use the mouse to cut (remove) some links

Parameters:

    

  * **path** (`bpy_prop_collection` of `OperatorMousePath`, (optional)) – Path

  * **cursor** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Cursor

bpy.ops.node.links_detach()¶

    

Remove all links to selected nodes, and try to connect neighbor nodes together

bpy.ops.node.links_mute(_*_ , _path =None_, _cursor =39_)¶

    

Use the mouse to mute links

Parameters:

    

  * **path** (`bpy_prop_collection` of `OperatorMousePath`, (optional)) – Path

  * **cursor** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Cursor

bpy.ops.node.move_detach_links(_*_ , _NODE_OT_links_detach =None_,
_TRANSFORM_OT_translate =None_)¶

    

Move a node to detach links

Parameters:

    

  * **NODE_OT_links_detach** (`NODE_OT_links_detach`, (optional)) – Detach Links, Remove all links to selected nodes, and try to connect neighbor nodes together

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.node.move_detach_links_release(_*_ , _NODE_OT_links_detach =None_,
_NODE_OT_translate_attach =None_)¶

    

Move a node to detach links

Parameters:

    

  * **NODE_OT_links_detach** (`NODE_OT_links_detach`, (optional)) – Detach Links, Remove all links to selected nodes, and try to connect neighbor nodes together

  * **NODE_OT_translate_attach** (`NODE_OT_translate_attach`, (optional)) – Move and Attach, Move nodes and attach to frame

bpy.ops.node.mute_toggle()¶

    

Toggle muting of selected nodes

bpy.ops.node.new_geometry_node_group_assign()¶

    

Create a new geometry node group and assign it to the active modifier

File:

    

[startup/bl_operators/geometry_nodes.py:337](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/geometry_nodes.py#L337)

bpy.ops.node.new_geometry_node_group_tool()¶

    

Create a new geometry node group for a tool

File:

    

[startup/bl_operators/geometry_nodes.py:358](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/geometry_nodes.py#L358)

bpy.ops.node.new_geometry_nodes_modifier()¶

    

Create a new modifier with a new geometry node group

File:

    

[startup/bl_operators/geometry_nodes.py:314](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/geometry_nodes.py#L314)

bpy.ops.node.new_node_tree(_*_ , _type_ , _name ='NodeTree'_)¶

    

Create a new node tree

Parameters:

    

  * **type** (_enum in_ _[__]__,__(__optional_ _)_) – Tree Type

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name

bpy.ops.node.node_color_preset_add(_*_ , _name =''_, _remove_name =False_,
_remove_active =False_)¶

    

Add or remove a Node Color Preset

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the preset, used to make the path name

  * **remove_name** (_boolean_ _,__(__optional_ _)_) – remove_name

  * **remove_active** (_boolean_ _,__(__optional_ _)_) – remove_active

File:

    

[startup/bl_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.node.node_copy_color()¶

    

Copy color to all selected nodes

bpy.ops.node.options_toggle()¶

    

Toggle option buttons display for selected nodes

bpy.ops.node.output_file_add_socket(_*_ , _file_path =''_)¶

    

Add a new input to a file output node

Parameters:

    

**file_path** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path,
Subpath of the output file

bpy.ops.node.output_file_move_active_socket(_*_ , _direction =DOWN_)¶

    

Move the active input of a file output node up or down the list

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Direction

bpy.ops.node.output_file_remove_active_socket()¶

    

Remove the active input from a file output node

bpy.ops.node.parent_set()¶

    

Attach selected nodes

bpy.ops.node.preview_toggle()¶

    

Toggle preview display for selected nodes

bpy.ops.node.read_viewlayers()¶

    

Read all render layers of all used scenes

bpy.ops.node.render_changed()¶

    

Render current scene, when input node’s layer has been changed

bpy.ops.node.repeat_zone_item_add()¶

    

Add item below active item

bpy.ops.node.repeat_zone_item_move(_*_ , _direction =UP_)¶

    

Move active item

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Direction, Move direction

bpy.ops.node.repeat_zone_item_remove()¶

    

Remove active item

bpy.ops.node.resize()¶

    

Resize a node

bpy.ops.node.select(_*_ , _extend =False_, _deselect =False_, _toggle =False_,
_deselect_all =False_, _select_passthrough =False_, _location =(0, 0)_,
_socket_select =False_, _clear_viewer =False_)¶

    

Select the node under the cursor

Parameters:

    

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection instead of deselecting everything first

  * **deselect** (_boolean_ _,__(__optional_ _)_) – Deselect, Remove from selection

  * **toggle** (_boolean_ _,__(__optional_ _)_) – Toggle Selection, Toggle the selection

  * **deselect_all** (_boolean_ _,__(__optional_ _)_) – Deselect On Nothing, Deselect all when nothing under the cursor

  * **select_passthrough** (_boolean_ _,__(__optional_ _)_) – Only Select Unselected, Ignore the select action when the element is already selected

  * **location** (_int array_ _of_ _2 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Location, Mouse location

  * **socket_select** (_boolean_ _,__(__optional_ _)_) – Socket Select

  * **clear_viewer** (_boolean_ _,__(__optional_ _)_) – Clear Viewer, Deactivate geometry nodes viewer when clicking in empty space

bpy.ops.node.select_all(_*_ , _action =TOGGLE_)¶

    

(De)select all nodes

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.node.select_box(_*_ , _tweak =False_, _xmin =0_, _xmax =0_, _ymin =0_,
_ymax =0_, _wait_for_input =True_, _mode =SET_)¶

    

Use box selection to select nodes

Parameters:

    

  * **tweak** (_boolean_ _,__(__optional_ _)_) – Tweak, Only activate when mouse is not over a node (useful for tweak gesture)

  * **xmin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Min

  * **xmax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Max

  * **ymin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Min

  * **ymax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Max

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

  * **mode** (enum in [`SET`, `ADD`, `SUB`], (optional)) – 

Mode

    * `SET` Set – Set a new selection.

    * `ADD` Extend – Extend existing selection.

    * `SUB` Subtract – Subtract existing selection.

bpy.ops.node.select_circle(_*_ , _x =0_, _y =0_, _radius =25_, _wait_for_input
=True_, _mode =SET_)¶

    

Use circle selection to select nodes

Parameters:

    

  * **x** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X

  * **y** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y

  * **radius** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

  * **mode** (enum in [`SET`, `ADD`, `SUB`], (optional)) – 

Mode

    * `SET` Set – Set a new selection.

    * `ADD` Extend – Extend existing selection.

    * `SUB` Subtract – Subtract existing selection.

bpy.ops.node.select_grouped(_*_ , _extend =False_, _type =TYPE_)¶

    

Select nodes with similar properties

Parameters:

    

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection instead of deselecting everything first

  * **type** (enum in [`TYPE`, `COLOR`, `PREFIX`, `SUFFIX`], (optional)) – Type

bpy.ops.node.select_lasso(_*_ , _tweak =False_, _path =None_,
_use_smooth_stroke =False_, _smooth_stroke_factor =0.75_,
_smooth_stroke_radius =35_, _mode =SET_)¶

    

Select nodes using lasso selection

Parameters:

    

  * **tweak** (_boolean_ _,__(__optional_ _)_) – Tweak, Only activate when mouse is not over a node (useful for tweak gesture)

  * **path** (`bpy_prop_collection` of `OperatorMousePath`, (optional)) – Path

  * **use_smooth_stroke** (_boolean_ _,__(__optional_ _)_) – Stabilize Stroke, Selection lags behind mouse and follows a smoother path

  * **smooth_stroke_factor** (_float in_ _[__0.5_ _,__0.99_ _]__,__(__optional_ _)_) – Smooth Stroke Factor, Higher values gives a smoother stroke

  * **smooth_stroke_radius** (_int in_ _[__10_ _,__200_ _]__,__(__optional_ _)_) – Smooth Stroke Radius, Minimum distance from last point before selection continues

  * **mode** (enum in [`SET`, `ADD`, `SUB`], (optional)) – 

Mode

    * `SET` Set – Set a new selection.

    * `ADD` Extend – Extend existing selection.

    * `SUB` Subtract – Subtract existing selection.

bpy.ops.node.select_link_viewer(_*_ , _NODE_OT_select =None_,
_NODE_OT_link_viewer =None_)¶

    

Select node and link it to a viewer node

Parameters:

    

  * **NODE_OT_select** (`NODE_OT_select`, (optional)) – Select, Select the node under the cursor

  * **NODE_OT_link_viewer** (`NODE_OT_link_viewer`, (optional)) – Link to Viewer Node, Link to viewer node

bpy.ops.node.select_linked_from()¶

    

Select nodes linked from the selected ones

bpy.ops.node.select_linked_to()¶

    

Select nodes linked to the selected ones

bpy.ops.node.select_same_type_step(_*_ , _prev =False_)¶

    

Activate and view same node type, step by step

Parameters:

    

**prev** (_boolean_ _,__(__optional_ _)_) – Previous

bpy.ops.node.separate_bundle_item_add()¶

    

Add item below active item

bpy.ops.node.separate_bundle_item_move(_*_ , _direction =UP_)¶

    

Move active item

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Direction, Move direction

bpy.ops.node.separate_bundle_item_remove()¶

    

Remove active item

bpy.ops.node.shader_script_update()¶

    

Update shader script node with new sockets and options from the script

bpy.ops.node.simulation_zone_item_add()¶

    

Add item below active item

bpy.ops.node.simulation_zone_item_move(_*_ , _direction =UP_)¶

    

Move active item

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Direction, Move direction

bpy.ops.node.simulation_zone_item_remove()¶

    

Remove active item

bpy.ops.node.translate_attach(_*_ , _TRANSFORM_OT_translate =None_,
_NODE_OT_attach =None_)¶

    

Move nodes and attach to frame

Parameters:

    

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

  * **NODE_OT_attach** (`NODE_OT_attach`, (optional)) – Attach Nodes, Attach active node to a frame

bpy.ops.node.translate_attach_remove_on_cancel(_*_ , _TRANSFORM_OT_translate
=None_, _NODE_OT_attach =None_)¶

    

Move nodes and attach to frame

Parameters:

    

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

  * **NODE_OT_attach** (`NODE_OT_attach`, (optional)) – Attach Nodes, Attach active node to a frame

bpy.ops.node.tree_path_parent()¶

    

Go to parent node tree

File:

    

[startup/bl_operators/node.py:329](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L329)

bpy.ops.node.view_all()¶

    

Resize view so you can see all nodes

bpy.ops.node.view_selected()¶

    

Resize view so you can see selected nodes

bpy.ops.node.viewer_border(_*_ , _xmin =0_, _xmax =0_, _ymin =0_, _ymax =0_,
_wait_for_input =True_)¶

    

Set the boundaries for viewer operations

Parameters:

    

  * **xmin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Min

  * **xmax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Max

  * **ymin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Min

  * **ymax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Max

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

bpy.ops.node.viewer_shortcut_get(_*_ , _viewer_index =0_)¶

    

Activate a specific viewer node using 1,2,..,9 keys

Parameters:

    

**viewer_index** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) –
Viewer Index, Index corresponding to the shortcut, e.g. number key 1
corresponds to index 1 etc..

File:

    

[startup/bl_operators/node.py:689](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L689)

bpy.ops.node.viewer_shortcut_set(_*_ , _viewer_index =0_)¶

    

Create a viewer shortcut for the selected node by pressing ctrl+1,2,..9

Parameters:

    

**viewer_index** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) –
Viewer Index, Index corresponding to the shortcut, e.g. number key 1
corresponds to index 1 etc..

File:

    

[startup/bl_operators/node.py:629](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L629)

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

