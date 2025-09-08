---
url: https://docs.blender.org/api/current/bpy.ops.scene.html
scraped_at: 2025-09-08T14:18:44.642058
title: Scene Operators¶
---

# Scene Operators¶

bpy.ops.scene.delete()¶

    

Delete active scene

bpy.ops.scene.freestyle_add_edge_marks_to_keying_set()¶

    

Add the data paths to the Freestyle Edge Mark property of selected edges to
the active keying set

File:

    

[startup/bl_operators/freestyle.py:136](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/freestyle.py#L136)

bpy.ops.scene.freestyle_add_face_marks_to_keying_set()¶

    

Add the data paths to the Freestyle Face Mark property of selected polygons to
the active keying set

File:

    

[startup/bl_operators/freestyle.py:167](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/freestyle.py#L167)

bpy.ops.scene.freestyle_alpha_modifier_add(_*_ , _type =ALONG_STROKE_)¶

    

Add an alpha transparency modifier to the line style associated with the
active lineset

Parameters:

    

**type** (enum in [Linestyle Alpha Modifier Type
Items](bpy_types_enum_items/linestyle_alpha_modifier_type_items.html#rna-enum-
linestyle-alpha-modifier-type-items), (optional)) – Type

bpy.ops.scene.freestyle_color_modifier_add(_*_ , _type =ALONG_STROKE_)¶

    

Add a line color modifier to the line style associated with the active lineset

Parameters:

    

**type** (enum in [Linestyle Color Modifier Type
Items](bpy_types_enum_items/linestyle_color_modifier_type_items.html#rna-enum-
linestyle-color-modifier-type-items), (optional)) – Type

bpy.ops.scene.freestyle_fill_range_by_selection(_*_ , _type =COLOR_, _name
=''_)¶

    

Fill the Range Min/Max entries by the min/max distance between selected mesh
objects and the source object (either a user-specified object or the active
camera)

Parameters:

    

  * **type** (enum in [`COLOR`, `ALPHA`, `THICKNESS`], (optional)) – 

Type, Type of the modifier to work on

    * `COLOR` Color – Color modifier type.

    * `ALPHA` Alpha – Alpha modifier type.

    * `THICKNESS` Thickness – Thickness modifier type.

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the modifier to work on

File:

    

[startup/bl_operators/freestyle.py:42](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/freestyle.py#L42)

bpy.ops.scene.freestyle_geometry_modifier_add(_*_ , _type=2D_OFFSET_)¶

    

Add a stroke geometry modifier to the line style associated with the active
lineset

Parameters:

    

**type** (enum in [Linestyle Geometry Modifier Type
Items](bpy_types_enum_items/linestyle_geometry_modifier_type_items.html#rna-
enum-linestyle-geometry-modifier-type-items), (optional)) – Type

bpy.ops.scene.freestyle_lineset_add()¶

    

Add a line set into the list of line sets

bpy.ops.scene.freestyle_lineset_copy()¶

    

Copy the active line set to the internal clipboard

bpy.ops.scene.freestyle_lineset_move(_*_ , _direction =UP_)¶

    

Change the position of the active line set within the list of line sets

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Direction, Direction to
move the active line set towards

bpy.ops.scene.freestyle_lineset_paste()¶

    

Paste the internal clipboard content to the active line set

bpy.ops.scene.freestyle_lineset_remove()¶

    

Remove the active line set from the list of line sets

bpy.ops.scene.freestyle_linestyle_new()¶

    

Create a new line style, reusable by multiple line sets

bpy.ops.scene.freestyle_modifier_copy()¶

    

Duplicate the modifier within the list of modifiers

bpy.ops.scene.freestyle_modifier_move(_*_ , _direction =UP_)¶

    

Move the modifier within the list of modifiers

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Direction, Direction to
move the chosen modifier towards

bpy.ops.scene.freestyle_modifier_remove()¶

    

Remove the modifier from the list of modifiers

bpy.ops.scene.freestyle_module_add()¶

    

Add a style module into the list of modules

bpy.ops.scene.freestyle_module_move(_*_ , _direction =UP_)¶

    

Change the position of the style module within in the list of style modules

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Direction, Direction to
move the chosen style module towards

bpy.ops.scene.freestyle_module_open(_*_ , _filepath =''_, _make_internal
=True_)¶

    

Open a style module file

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – filepath

  * **make_internal** (_boolean_ _,__(__optional_ _)_) – Make internal, Make module file internal after loading

File:

    

[startup/bl_operators/freestyle.py:212](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/freestyle.py#L212)

bpy.ops.scene.freestyle_module_remove()¶

    

Remove the style module from the stack

bpy.ops.scene.freestyle_stroke_material_create()¶

    

Create Freestyle stroke material for testing

bpy.ops.scene.freestyle_thickness_modifier_add(_*_ , _type =ALONG_STROKE_)¶

    

Add a line thickness modifier to the line style associated with the active
lineset

Parameters:

    

**type** (enum in [Linestyle Thickness Modifier Type
Items](bpy_types_enum_items/linestyle_thickness_modifier_type_items.html#rna-
enum-linestyle-thickness-modifier-type-items), (optional)) – Type

bpy.ops.scene.gltf2_action_filter_refresh()¶

    

Refresh list of actions

File:

    

[addons_core/io_scene_gltf2/blender/com/gltf2_blender_ui.py:624](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/io_scene_gltf2/blender/com/gltf2_blender_ui.py#L624)

bpy.ops.scene.gpencil_brush_preset_add(_*_ , _name =''_, _remove_name =False_,
_remove_active =False_)¶

    

Add or remove grease pencil brush preset

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the preset, used to make the path name

  * **remove_name** (_boolean_ _,__(__optional_ _)_) – remove_name

  * **remove_active** (_boolean_ _,__(__optional_ _)_) – remove_active

File:

    

[startup/bl_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.scene.gpencil_material_preset_add(_*_ , _name =''_, _remove_name
=False_, _remove_active =False_)¶

    

Add or remove Grease Pencil material preset

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the preset, used to make the path name

  * **remove_name** (_boolean_ _,__(__optional_ _)_) – remove_name

  * **remove_active** (_boolean_ _,__(__optional_ _)_) – remove_active

File:

    

[startup/bl_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.scene.new(_*_ , _type =NEW_)¶

    

Add new scene by type

Parameters:

    

**type** (enum in [`NEW`, `EMPTY`, `LINK_COPY`, `FULL_COPY`], (optional)) –

Type

  * `NEW` New – Add a new, empty scene with default settings.

  * `EMPTY` Copy Settings – Add a new, empty scene, and copy settings from the current scene.

  * `LINK_COPY` Linked Copy – Link in the collections from the current scene (shallow copy).

  * `FULL_COPY` Full Copy – Make a full copy of the current scene.

bpy.ops.scene.new_sequencer(_*_ , _type =NEW_)¶

    

Add new scene by type in the sequence editor and assign to active strip

Parameters:

    

**type** (enum in [`NEW`, `EMPTY`, `LINK_COPY`, `FULL_COPY`], (optional)) –

Type

  * `NEW` New – Add a new, empty scene with default settings.

  * `EMPTY` Copy Settings – Add a new, empty scene, and copy settings from the current scene.

  * `LINK_COPY` Linked Copy – Link in the collections from the current scene (shallow copy).

  * `FULL_COPY` Full Copy – Make a full copy of the current scene.

bpy.ops.scene.render_view_add()¶

    

Add a render view

bpy.ops.scene.render_view_remove()¶

    

Remove the selected render view

bpy.ops.scene.view_layer_add(_*_ , _type =NEW_)¶

    

Add a view layer

Parameters:

    

**type** (enum in [`NEW`, `COPY`, `EMPTY`], (optional)) –

Type

  * `NEW` New – Add a new view layer.

  * `COPY` Copy Settings – Copy settings of current view layer.

  * `EMPTY` Blank – Add a new view layer with all collections disabled.

bpy.ops.scene.view_layer_add_aov()¶

    

Add a Shader AOV

bpy.ops.scene.view_layer_add_lightgroup(_*_ , _name =''_)¶

    

Add a Light Group

Parameters:

    

**name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of newly
created lightgroup

bpy.ops.scene.view_layer_add_used_lightgroups()¶

    

Add all used Light Groups

bpy.ops.scene.view_layer_remove()¶

    

Remove the selected view layer

bpy.ops.scene.view_layer_remove_aov()¶

    

Remove Active AOV

bpy.ops.scene.view_layer_remove_lightgroup()¶

    

Remove Active Lightgroup

bpy.ops.scene.view_layer_remove_unused_lightgroups()¶

    

Remove all unused Light Groups

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

