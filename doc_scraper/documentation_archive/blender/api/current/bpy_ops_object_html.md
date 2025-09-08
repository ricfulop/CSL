---
url: https://docs.blender.org/api/current/bpy.ops.object.html
scraped_at: 2025-09-08T14:18:31.969499
title: Object Operators¶
---

# Object Operators¶

bpy.ops.object.add(_*_ , _radius =1.0_, _type =EMPTY_, _enter_editmode
=False_, _align =WORLD_, _location =(0.0, 0.0, 0.0)_, _rotation =(0.0, 0.0,
0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Add an object to the scene

Parameters:

    

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **type** (enum in [Object Type Items](bpy_types_enum_items/object_type_items.html#rna-enum-object-type-items), (optional)) – Type

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.add_modifier_menu()¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

File:

    

[startup/bl_ui/properties_data_modifier.py:283](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_ui/properties_data_modifier.py#L283)

bpy.ops.object.add_named(_*_ , _linked =False_, _name =''_, _session_uid =0_,
_matrix =((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0),
(0.0, 0.0, 0.0, 0.0))_, _drop_x =0_, _drop_y =0_)¶

    

Add named object

Parameters:

    

  * **linked** (_boolean_ _,__(__optional_ _)_) – Linked, Duplicate object but not object data, linking to the original data

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the data-block to use by the operator

  * **session_uid** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

  * **matrix** ([`mathutils.Matrix`](mathutils.html#mathutils.Matrix "mathutils.Matrix") of 4 * 4 items in [-inf, inf], (optional)) – Matrix

  * **drop_x** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Drop X, X-coordinate (screen space) to place the new object under

  * **drop_y** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Drop Y, Y-coordinate (screen space) to place the new object under

bpy.ops.object.align(_*_ , _bb_quality =True_, _align_mode =OPT_2_,
_relative_to =OPT_4_, _align_axis ={}_)¶

    

Align objects

Parameters:

    

  * **bb_quality** (_boolean_ _,__(__optional_ _)_) – High Quality, Enables high quality but slow calculation of the bounding box for perfect results on complex shape meshes with rotation/scale

  * **align_mode** (enum in [`OPT_1`, `OPT_2`, `OPT_3`], (optional)) – Align Mode, Side of object to use for alignment

  * **relative_to** (enum in [`OPT_1`, `OPT_2`, `OPT_3`, `OPT_4`], (optional)) – 

Relative To, Reference location to align to

    * `OPT_1` Scene Origin – Use the scene origin as the position for the selected objects to align to.

    * `OPT_2` 3D Cursor – Use the 3D cursor as the position for the selected objects to align to.

    * `OPT_3` Selection – Use the selected objects as the position for the selected objects to align to.

    * `OPT_4` Active – Use the active object as the position for the selected objects to align to.

  * **align_axis** (enum set in {`X`, `Y`, `Z`}, (optional)) – Align, Align to axis

File:

    

[startup/bl_operators/object_align.py:386](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_align.py#L386)

bpy.ops.object.anim_transforms_to_deltas()¶

    

Convert object animation for normal transforms to delta transforms

File:

    

[startup/bl_operators/object.py:821](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L821)

bpy.ops.object.armature_add(_*_ , _radius =1.0_, _enter_editmode =False_,
_align =WORLD_, _location =(0.0, 0.0, 0.0)_, _rotation =(0.0, 0.0, 0.0)_,
_scale =(0.0, 0.0, 0.0)_)¶

    

Add an armature object to the scene

Parameters:

    

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.assign_property_defaults(_*_ , _process_data =True_,
_process_bones =True_)¶

    

Assign the current values of custom properties as their defaults, for use as
part of the rest pose state in NLA track mixing

Parameters:

    

  * **process_data** (_boolean_ _,__(__optional_ _)_) – Process data properties

  * **process_bones** (_boolean_ _,__(__optional_ _)_) – Process bone properties

File:

    

[startup/bl_operators/object.py:974](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L974)

bpy.ops.object.bake(_*_ , _type =COMBINED_, _pass_filter ={}_, _filepath =''_,
_width =512_, _height =512_, _margin =16_, _margin_type =EXTEND_,
_use_selected_to_active =False_, _max_ray_distance =0.0_, _cage_extrusion
=0.0_, _cage_object =''_, _normal_space =TANGENT_, _normal_r =POS_X_,
_normal_g =POS_Y_, _normal_b =POS_Z_, _target =IMAGE_TEXTURES_, _save_mode
=INTERNAL_, _use_clear =False_, _use_cage =False_, _use_split_materials
=False_, _use_automatic_name =False_, _uv_layer =''_)¶

    

Bake image textures of selected objects

Parameters:

    

  * **type** (enum in [Bake Pass Type Items](bpy_types_enum_items/bake_pass_type_items.html#rna-enum-bake-pass-type-items), (optional)) – Type, Type of pass to bake, some of them may not be supported by the current render engine

  * **pass_filter** (enum set in [Bake Pass Filter Type Items](bpy_types_enum_items/bake_pass_filter_type_items.html#rna-enum-bake-pass-filter-type-items), (optional)) – Pass Filter, Filter to combined, diffuse, glossy, transmission and subsurface passes

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Image filepath to use when saving externally

  * **width** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Width, Horizontal dimension of the baking map (external only)

  * **height** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Height, Vertical dimension of the baking map (external only)

  * **margin** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Margin, Extends the baked result as a post process filter

  * **margin_type** (enum in [Bake Margin Type Items](bpy_types_enum_items/bake_margin_type_items.html#rna-enum-bake-margin-type-items), (optional)) – Margin Type, Which algorithm to use to generate the margin

  * **use_selected_to_active** (_boolean_ _,__(__optional_ _)_) – Selected to Active, Bake shading on the surface of selected objects to the active object

  * **max_ray_distance** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Max Ray Distance, The maximum ray distance for matching points between the active and selected objects. If zero, there is no limit

  * **cage_extrusion** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Cage Extrusion, Inflate the active object by the specified distance for baking. This helps matching to points nearer to the outside of the selected object meshes

  * **cage_object** (_string_ _,__(__optional_ _,__never None_ _)_) – Cage Object, Object to use as cage, instead of calculating the cage from the active object with cage extrusion

  * **normal_space** (enum in [Normal Space Items](bpy_types_enum_items/normal_space_items.html#rna-enum-normal-space-items), (optional)) – Normal Space, Choose normal space for baking

  * **normal_r** (enum in [Normal Swizzle Items](bpy_types_enum_items/normal_swizzle_items.html#rna-enum-normal-swizzle-items), (optional)) – R, Axis to bake in red channel

  * **normal_g** (enum in [Normal Swizzle Items](bpy_types_enum_items/normal_swizzle_items.html#rna-enum-normal-swizzle-items), (optional)) – G, Axis to bake in green channel

  * **normal_b** (enum in [Normal Swizzle Items](bpy_types_enum_items/normal_swizzle_items.html#rna-enum-normal-swizzle-items), (optional)) – B, Axis to bake in blue channel

  * **target** (enum in [Bake Target Items](bpy_types_enum_items/bake_target_items.html#rna-enum-bake-target-items), (optional)) – Target, Where to output the baked map

  * **save_mode** (enum in [Bake Save Mode Items](bpy_types_enum_items/bake_save_mode_items.html#rna-enum-bake-save-mode-items), (optional)) – Save Mode, Where to save baked image textures

  * **use_clear** (_boolean_ _,__(__optional_ _)_) – Clear, Clear images before baking (only for internal saving)

  * **use_cage** (_boolean_ _,__(__optional_ _)_) – Cage, Cast rays to active object from a cage

  * **use_split_materials** (_boolean_ _,__(__optional_ _)_) – Split Materials, Split baked maps per material, using material name in output file (external only)

  * **use_automatic_name** (_boolean_ _,__(__optional_ _)_) – Automatic Name, Automatically name the output file with the pass type

  * **uv_layer** (_string_ _,__(__optional_ _,__never None_ _)_) – UV Layer, UV layer to override active

bpy.ops.object.bake_image()¶

    

Bake image textures of selected objects

bpy.ops.object.camera_add(_*_ , _enter_editmode =False_, _align =WORLD_,
_location =(0.0, 0.0, 0.0)_, _rotation =(0.0, 0.0, 0.0)_, _scale =(0.0, 0.0,
0.0)_)¶

    

Add a camera object to the scene

Parameters:

    

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.camera_custom_update()¶

    

Update custom camera with new parameters from the shader

bpy.ops.object.clear_override_library()¶

    

Delete the selected local overrides and relink their usages to the linked
data-blocks if possible, else reset them and mark them as non editable

bpy.ops.object.collection_add()¶

    

Add an object to a new collection

bpy.ops.object.collection_external_asset_drop(_*_ , _session_uid =0_, _align
=WORLD_, _location =(0.0, 0.0, 0.0)_, _rotation =(0.0, 0.0, 0.0)_, _scale
=(0.0, 0.0, 0.0)_, _use_instance =True_, _drop_x =0_, _drop_y =0_,
_collection_)¶

    

Add the dragged collection to the scene

Parameters:

    

  * **session_uid** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

  * **use_instance** (_boolean_ _,__(__optional_ _)_) – Instance, Add the dropped collection as collection instance

  * **drop_x** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Drop X, X-coordinate (screen space) to place the new object under

  * **drop_y** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Drop Y, Y-coordinate (screen space) to place the new object under

  * **collection** (_enum in_ _[__]__,__(__optional_ _)_) – Collection

bpy.ops.object.collection_instance_add(_*_ , _name ='Collection'_,
_collection_ , _align =WORLD_, _location =(0.0, 0.0, 0.0)_, _rotation =(0.0,
0.0, 0.0)_, _scale =(0.0, 0.0, 0.0)_, _session_uid =0_, _drop_x =0_, _drop_y
=0_)¶

    

Add a collection instance

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Collection name to add

  * **collection** (_enum in_ _[__]__,__(__optional_ _)_) – Collection

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

  * **session_uid** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

  * **drop_x** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Drop X, X-coordinate (screen space) to place the new object under

  * **drop_y** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Drop Y, Y-coordinate (screen space) to place the new object under

bpy.ops.object.collection_link(_*_ , _collection_)¶

    

Add an object to an existing collection

Parameters:

    

**collection** (_enum in_ _[__]__,__(__optional_ _)_) – Collection

bpy.ops.object.collection_objects_select()¶

    

Select all objects in collection

bpy.ops.object.collection_remove()¶

    

Remove the active object from this collection

bpy.ops.object.collection_unlink()¶

    

Unlink the collection from all objects

bpy.ops.object.constraint_add(_*_ , _type_)¶

    

Add a constraint to the active object

Parameters:

    

**type** (_enum in_ _[__]__,__(__optional_ _)_) – Type

bpy.ops.object.constraint_add_with_targets(_*_ , _type_)¶

    

Add a constraint to the active object, with target (where applicable) set to
the selected objects/bones

Parameters:

    

**type** (_enum in_ _[__]__,__(__optional_ _)_) – Type

bpy.ops.object.constraints_clear()¶

    

Clear all constraints from the selected objects

bpy.ops.object.constraints_copy()¶

    

Copy constraints to other selected objects

bpy.ops.object.convert(_*_ , _target =MESH_, _keep_original =False_,
_merge_customdata =True_, _thickness =5_, _faces =True_, _offset =0.01_)¶

    

Convert selected objects to another type

Parameters:

    

  * **target** (enum in [`CURVE`, `MESH`, `POINTCLOUD`, `CURVES`, `GREASEPENCIL`], (optional)) – 

Target, Type of object to convert to

    * `CURVE` Curve – Curve from Mesh or Text objects.

    * `MESH` Mesh – Mesh from Curve, Surface, Metaball, Text, or Point Cloud objects.

    * `POINTCLOUD` Point Cloud – Point Cloud from Mesh objects.

    * `CURVES` Curves – Curves from evaluated curve data.

    * `GREASEPENCIL` Grease Pencil – Grease Pencil from Curve or Mesh objects.

  * **keep_original** (_boolean_ _,__(__optional_ _)_) – Keep Original, Keep original objects instead of replacing them

  * **merge_customdata** (_boolean_ _,__(__optional_ _)_) – Merge UVs, Merge UV coordinates that share a vertex to account for imprecision in some modifiers

  * **thickness** (_int in_ _[__1_ _,__100_ _]__,__(__optional_ _)_) – Thickness

  * **faces** (_boolean_ _,__(__optional_ _)_) – Export Faces, Export faces as filled strokes

  * **offset** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Stroke Offset, Offset strokes from fill

bpy.ops.object.correctivesmooth_bind(_*_ , _modifier =''_)¶

    

Bind base pose in Corrective Smooth modifier

Parameters:

    

**modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name
of the modifier to edit

bpy.ops.object.curves_empty_hair_add(_*_ , _align =WORLD_, _location =(0.0,
0.0, 0.0)_, _rotation =(0.0, 0.0, 0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Add an empty curve object to the scene with the selected mesh as surface

Parameters:

    

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.curves_random_add(_*_ , _align =WORLD_, _location =(0.0, 0.0,
0.0)_, _rotation =(0.0, 0.0, 0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Add a curves object with random curves to the scene

Parameters:

    

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.data_instance_add(_*_ , _name =''_, _session_uid =0_, _type
=ACTION_, _align =WORLD_, _location =(0.0, 0.0, 0.0)_, _rotation =(0.0, 0.0,
0.0)_, _scale =(0.0, 0.0, 0.0)_, _drop_x =0_, _drop_y =0_)¶

    

Add an object data instance

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the data-block to use by the operator

  * **session_uid** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

  * **type** (enum in [Id Type Items](bpy_types_enum_items/id_type_items.html#rna-enum-id-type-items), (optional)) – Type

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

  * **drop_x** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Drop X, X-coordinate (screen space) to place the new object under

  * **drop_y** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Drop Y, Y-coordinate (screen space) to place the new object under

bpy.ops.object.data_transfer(_*_ , _use_reverse_transfer =False_, _use_freeze
=False_, _data_type_ , _use_create =True_, _vert_mapping =NEAREST_,
_edge_mapping =NEAREST_, _loop_mapping =NEAREST_POLYNOR_, _poly_mapping
=NEAREST_, _use_auto_transform =False_, _use_object_transform =True_,
_use_max_distance =False_, _max_distance =1.0_, _ray_radius =0.0_,
_islands_precision =0.1_, _layers_select_src =ACTIVE_, _layers_select_dst
=ACTIVE_, _mix_mode =REPLACE_, _mix_factor =1.0_)¶

    

Transfer data layer(s) (weights, edge sharp, etc.) from active to selected
meshes

Parameters:

    

  * **use_reverse_transfer** (_boolean_ _,__(__optional_ _)_) – Reverse Transfer, Transfer from selected objects to active one

  * **use_freeze** (_boolean_ _,__(__optional_ _)_) – Freeze Operator, Prevent changes to settings to re-run the operator, handy to change several things at once with heavy geometry

  * **data_type** (enum in [`VGROUP_WEIGHTS`, `BEVEL_WEIGHT_VERT`, `COLOR_VERTEX`, `SHARP_EDGE`, `SEAM`, `CREASE`, `BEVEL_WEIGHT_EDGE`, `FREESTYLE_EDGE`, `CUSTOM_NORMAL`, `COLOR_CORNER`, `UV`, `SMOOTH`, `FREESTYLE_FACE`], (optional)) – 

Data Type, Which data to transfer

    * `VGROUP_WEIGHTS` Vertex Group(s) – Transfer active or all vertex groups.

    * `BEVEL_WEIGHT_VERT` Bevel Weight – Transfer bevel weights.

    * `COLOR_VERTEX` Colors – Color Attributes.

    * `SHARP_EDGE` Sharp – Transfer sharp mark.

    * `SEAM` UV Seam – Transfer UV seam mark.

    * `CREASE` Subdivision Crease – Transfer crease values.

    * `BEVEL_WEIGHT_EDGE` Bevel Weight – Transfer bevel weights.

    * `FREESTYLE_EDGE` Freestyle Mark – Transfer Freestyle edge mark.

    * `CUSTOM_NORMAL` Custom Normals – Transfer custom normals.

    * `COLOR_CORNER` Colors – Color Attributes.

    * `UV` UVs – Transfer UV layers.

    * `SMOOTH` Smooth – Transfer flat/smooth mark.

    * `FREESTYLE_FACE` Freestyle Mark – Transfer Freestyle face mark.

  * **use_create** (_boolean_ _,__(__optional_ _)_) – Create Data, Add data layers on destination meshes if needed

  * **vert_mapping** (enum in [Dt Method Vertex Items](bpy_types_enum_items/dt_method_vertex_items.html#rna-enum-dt-method-vertex-items), (optional)) – Vertex Mapping, Method used to map source vertices to destination ones

  * **edge_mapping** (enum in [Dt Method Edge Items](bpy_types_enum_items/dt_method_edge_items.html#rna-enum-dt-method-edge-items), (optional)) – Edge Mapping, Method used to map source edges to destination ones

  * **loop_mapping** (enum in [Dt Method Loop Items](bpy_types_enum_items/dt_method_loop_items.html#rna-enum-dt-method-loop-items), (optional)) – Face Corner Mapping, Method used to map source faces’ corners to destination ones

  * **poly_mapping** (enum in [Dt Method Poly Items](bpy_types_enum_items/dt_method_poly_items.html#rna-enum-dt-method-poly-items), (optional)) – Face Mapping, Method used to map source faces to destination ones

  * **use_auto_transform** (_boolean_ _,__(__optional_ _)_) – Auto Transform, Automatically compute transformation to get the best possible match between source and destination meshes.Warning: Results will never be as good as manual matching of objects

  * **use_object_transform** (_boolean_ _,__(__optional_ _)_) – Object Transform, Evaluate source and destination meshes in global space

  * **use_max_distance** (_boolean_ _,__(__optional_ _)_) – Only Neighbor Geometry, Source elements must be closer than given distance from destination one

  * **max_distance** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Max Distance, Maximum allowed distance between source and destination element, for non-topology mappings

  * **ray_radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Ray Radius, ‘Width’ of rays (especially useful when raycasting against vertices or edges)

  * **islands_precision** (_float in_ _[__0_ _,__10_ _]__,__(__optional_ _)_) – Islands Precision, Factor controlling precision of islands handling (the higher, the better the results)

  * **layers_select_src** (enum in [Dt Layers Select Src Items](bpy_types_enum_items/dt_layers_select_src_items.html#rna-enum-dt-layers-select-src-items), (optional)) – Source Layers Selection, Which layers to transfer, in case of multi-layers types

  * **layers_select_dst** (enum in [Dt Layers Select Dst Items](bpy_types_enum_items/dt_layers_select_dst_items.html#rna-enum-dt-layers-select-dst-items), (optional)) – Destination Layers Matching, How to match source and destination layers

  * **mix_mode** (enum in [Dt Mix Mode Items](bpy_types_enum_items/dt_mix_mode_items.html#rna-enum-dt-mix-mode-items), (optional)) – Mix Mode, How to affect destination elements with source values

  * **mix_factor** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Mix Factor, Factor to use when applying data to destination (exact behavior depends on mix mode)

bpy.ops.object.datalayout_transfer(_*_ , _modifier =''_, _data_type_ ,
_use_delete =False_, _layers_select_src =ACTIVE_, _layers_select_dst
=ACTIVE_)¶

    

Transfer layout of data layer(s) from active to selected meshes

Parameters:

    

  * **modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name of the modifier to edit

  * **data_type** (enum in [`VGROUP_WEIGHTS`, `BEVEL_WEIGHT_VERT`, `COLOR_VERTEX`, `SHARP_EDGE`, `SEAM`, `CREASE`, `BEVEL_WEIGHT_EDGE`, `FREESTYLE_EDGE`, `CUSTOM_NORMAL`, `COLOR_CORNER`, `UV`, `SMOOTH`, `FREESTYLE_FACE`], (optional)) – 

Data Type, Which data to transfer

    * `VGROUP_WEIGHTS` Vertex Group(s) – Transfer active or all vertex groups.

    * `BEVEL_WEIGHT_VERT` Bevel Weight – Transfer bevel weights.

    * `COLOR_VERTEX` Colors – Color Attributes.

    * `SHARP_EDGE` Sharp – Transfer sharp mark.

    * `SEAM` UV Seam – Transfer UV seam mark.

    * `CREASE` Subdivision Crease – Transfer crease values.

    * `BEVEL_WEIGHT_EDGE` Bevel Weight – Transfer bevel weights.

    * `FREESTYLE_EDGE` Freestyle Mark – Transfer Freestyle edge mark.

    * `CUSTOM_NORMAL` Custom Normals – Transfer custom normals.

    * `COLOR_CORNER` Colors – Color Attributes.

    * `UV` UVs – Transfer UV layers.

    * `SMOOTH` Smooth – Transfer flat/smooth mark.

    * `FREESTYLE_FACE` Freestyle Mark – Transfer Freestyle face mark.

  * **use_delete** (_boolean_ _,__(__optional_ _)_) – Exact Match, Also delete some data layers from destination if necessary, so that it matches exactly source

  * **layers_select_src** (enum in [Dt Layers Select Src Items](bpy_types_enum_items/dt_layers_select_src_items.html#rna-enum-dt-layers-select-src-items), (optional)) – Source Layers Selection, Which layers to transfer, in case of multi-layers types

  * **layers_select_dst** (enum in [Dt Layers Select Dst Items](bpy_types_enum_items/dt_layers_select_dst_items.html#rna-enum-dt-layers-select-dst-items), (optional)) – Destination Layers Matching, How to match source and destination layers

bpy.ops.object.delete(_*_ , _use_global =False_, _confirm =True_)¶

    

Delete selected objects

Parameters:

    

  * **use_global** (_boolean_ _,__(__optional_ _)_) – Delete Globally, Remove object from all scenes

  * **confirm** (_boolean_ _,__(__optional_ _)_) – Confirm, Prompt for confirmation

bpy.ops.object.drop_geometry_nodes(_*_ , _session_uid =0_,
_show_datablock_in_modifier =True_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

  * **session_uid** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Session UID, Session UID of the geometry node group being dropped

  * **show_datablock_in_modifier** (_boolean_ _,__(__optional_ _)_) – Show the datablock selector in the modifier

bpy.ops.object.drop_named_material(_*_ , _name =''_, _session_uid =0_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the data-block to use by the operator

  * **session_uid** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

bpy.ops.object.duplicate(_*_ , _linked =False_, _mode =TRANSLATION_)¶

    

Duplicate selected objects

Parameters:

    

  * **linked** (_boolean_ _,__(__optional_ _)_) – Linked, Duplicate object but not object data, linking to the original data

  * **mode** (enum in [Transform Mode Type Items](bpy_types_enum_items/transform_mode_type_items.html#rna-enum-transform-mode-type-items), (optional)) – Mode

bpy.ops.object.duplicate_move(_*_ , _OBJECT_OT_duplicate =None_,
_TRANSFORM_OT_translate =None_)¶

    

Duplicate the selected objects and move them

Parameters:

    

  * **OBJECT_OT_duplicate** (`OBJECT_OT_duplicate`, (optional)) – Duplicate Objects, Duplicate selected objects

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.object.duplicate_move_linked(_*_ , _OBJECT_OT_duplicate =None_,
_TRANSFORM_OT_translate =None_)¶

    

Duplicate the selected objects, but not their object data, and move them

Parameters:

    

  * **OBJECT_OT_duplicate** (`OBJECT_OT_duplicate`, (optional)) – Duplicate Objects, Duplicate selected objects

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.object.duplicates_make_real(_*_ , _use_base_parent =False_,
_use_hierarchy =False_)¶

    

Make instanced objects attached to this object real

Parameters:

    

  * **use_base_parent** (_boolean_ _,__(__optional_ _)_) – Parent, Parent newly created objects to the original instancer

  * **use_hierarchy** (_boolean_ _,__(__optional_ _)_) – Keep Hierarchy, Maintain parent child relationships

bpy.ops.object.editmode_toggle()¶

    

Toggle object’s edit mode

bpy.ops.object.effector_add(_*_ , _type =FORCE_, _radius =1.0_,
_enter_editmode =False_, _align =WORLD_, _location =(0.0, 0.0, 0.0)_,
_rotation =(0.0, 0.0, 0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Add an empty object with a physics effector to the scene

Parameters:

    

  * **type** (enum in [`FORCE`, `WIND`, `VORTEX`, `MAGNET`, `HARMONIC`, `CHARGE`, `LENNARDJ`, `TEXTURE`, `GUIDE`, `BOID`, `TURBULENCE`, `DRAG`, `FLUID`], (optional)) – Type

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.empty_add(_*_ , _type =PLAIN_AXES_, _radius =1.0_, _align
=WORLD_, _location =(0.0, 0.0, 0.0)_, _rotation =(0.0, 0.0, 0.0)_, _scale
=(0.0, 0.0, 0.0)_)¶

    

Add an empty object to the scene

Parameters:

    

  * **type** (enum in [Object Empty Drawtype Items](bpy_types_enum_items/object_empty_drawtype_items.html#rna-enum-object-empty-drawtype-items), (optional)) – Type

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.empty_image_add(_*_ , _filepath =''_, _hide_props_region
=True_, _check_existing =False_, _filter_blender =False_, _filter_backup
=False_, _filter_image =True_, _filter_movie =True_, _filter_python =False_,
_filter_font =False_, _filter_sound =False_, _filter_text =False_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =9_, _relative_path =True_, _show_multiview =False_, _use_multiview
=False_, _display_type =DEFAULT_, _sort_method_ , _name =''_, _session_uid
=0_, _align =WORLD_, _location =(0.0, 0.0, 0.0)_, _rotation =(0.0, 0.0, 0.0)_,
_scale =(0.0, 0.0, 0.0)_, _background =False_)¶

    

Add an empty image type to scene with data

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

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

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

  * **background** (_boolean_ _,__(__optional_ _)_) – Put in Background, Make the image render behind all objects

bpy.ops.object.explode_refresh(_*_ , _modifier =''_)¶

    

Refresh data in the Explode modifier

Parameters:

    

**modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name
of the modifier to edit

bpy.ops.object.forcefield_toggle()¶

    

Toggle object’s force field

bpy.ops.object.geometry_node_bake_delete_single(_*_ , _session_uid =0_,
_modifier_name =''_, _bake_id =0_)¶

    

Delete baked data of a single bake node or simulation

Parameters:

    

  * **session_uid** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

  * **modifier_name** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier Name, Name of the modifier that contains the node

  * **bake_id** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Bake ID, Nested node id of the node

bpy.ops.object.geometry_node_bake_pack_single(_*_ , _session_uid =0_,
_modifier_name =''_, _bake_id =0_)¶

    

Pack baked data from disk into the .blend file

Parameters:

    

  * **session_uid** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

  * **modifier_name** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier Name, Name of the modifier that contains the node

  * **bake_id** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Bake ID, Nested node id of the node

bpy.ops.object.geometry_node_bake_single(_*_ , _session_uid =0_,
_modifier_name =''_, _bake_id =0_)¶

    

Bake a single bake node or simulation

Parameters:

    

  * **session_uid** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

  * **modifier_name** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier Name, Name of the modifier that contains the node

  * **bake_id** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Bake ID, Nested node id of the node

bpy.ops.object.geometry_node_bake_unpack_single(_*_ , _session_uid =0_,
_modifier_name =''_, _bake_id =0_, _method =USE_LOCAL_)¶

    

Unpack baked data from the .blend file to disk

Parameters:

    

  * **session_uid** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

  * **modifier_name** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier Name, Name of the modifier that contains the node

  * **bake_id** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Bake ID, Nested node id of the node

  * **method** (enum in [`USE_LOCAL`, `WRITE_LOCAL`, `USE_ORIGINAL`, `WRITE_ORIGINAL`], (optional)) – Method, How to unpack

bpy.ops.object.geometry_node_tree_copy_assign()¶

    

Copy the active geometry node group and assign it to the active modifier

bpy.ops.object.geometry_nodes_input_attribute_toggle(_*_ , _input_name =''_,
_modifier_name =''_)¶

    

Switch between an attribute and a single value to define the data for every
element

Parameters:

    

  * **input_name** (_string_ _,__(__optional_ _,__never None_ _)_) – Input Name

  * **modifier_name** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier Name

bpy.ops.object.geometry_nodes_move_to_nodes(_*_ , _use_selected_objects
=False_)¶

    

Move inputs and outputs from in the modifier to a new node group

Parameters:

    

**use_selected_objects** (_boolean_ _,__(__optional_ _)_) – Selected Objects,
Affect all selected objects instead of just the active object

File:

    

[startup/bl_operators/geometry_nodes.py:277](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/geometry_nodes.py#L277)

bpy.ops.object.grease_pencil_add(_*_ , _type=EMPTY_ , _use_in_front=True_ ,
_stroke_depth_offset=0.05_ , _use_lights=True_ , _stroke_depth_order=3D_ ,
_radius=1.0_ , _align=WORLD_ , _location=(0.0_ , _0.0_ , _0.0)_ ,
_rotation=(0.0_ , _0.0_ , _0.0)_ , _scale=(0.0_ , _0.0_ , _0.0)_)¶

    

Add a Grease Pencil object to the scene

Parameters:

    

  * **type** (enum in [Object Gpencil Type Items](bpy_types_enum_items/object_gpencil_type_items.html#rna-enum-object-gpencil-type-items), (optional)) – Type

  * **use_in_front** (_boolean_ _,__(__optional_ _)_) – Show In Front, Show Line Art Grease Pencil in front of everything

  * **stroke_depth_offset** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Stroke Offset, Stroke offset for the Line Art modifier

  * **use_lights** (_boolean_ _,__(__optional_ _)_) – Use Lights, Use lights for this Grease Pencil object

  * **stroke_depth_order** (enum in [`2D`, `3D`], (optional)) – 

Stroke Depth Order, Defines how the strokes are ordered in 3D space (for
objects not displayed ‘In Front’)

    * `2D` 2D Layers – Display strokes using Grease Pencil layers to define order.

    * `3D` 3D Location – Display strokes using real 3D position in 3D space.

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.grease_pencil_dash_modifier_segment_add(_*_ , _modifier =''_)¶

    

Add a segment to the dash modifier

Parameters:

    

**modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name
of the modifier to edit

bpy.ops.object.grease_pencil_dash_modifier_segment_move(_*_ , _modifier =''_,
_type =UP_)¶

    

Move the active dash segment up or down

Parameters:

    

  * **modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name of the modifier to edit

  * **type** (enum in [`UP`, `DOWN`], (optional)) – Type

bpy.ops.object.grease_pencil_dash_modifier_segment_remove(_*_ , _modifier
=''_, _index =0_)¶

    

Remove the active segment from the dash modifier

Parameters:

    

  * **modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name of the modifier to edit

  * **index** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Index, Index of the segment to remove

bpy.ops.object.grease_pencil_time_modifier_segment_add(_*_ , _modifier =''_)¶

    

Add a segment to the time modifier

Parameters:

    

**modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name
of the modifier to edit

bpy.ops.object.grease_pencil_time_modifier_segment_move(_*_ , _modifier =''_,
_type =UP_)¶

    

Move the active time segment up or down

Parameters:

    

  * **modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name of the modifier to edit

  * **type** (enum in [`UP`, `DOWN`], (optional)) – Type

bpy.ops.object.grease_pencil_time_modifier_segment_remove(_*_ , _modifier
=''_, _index =0_)¶

    

Remove the active segment from the time modifier

Parameters:

    

  * **modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name of the modifier to edit

  * **index** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Index, Index of the segment to remove

bpy.ops.object.hide_collection(_*_ , _collection_index =-1_, _toggle =False_,
_extend =False_)¶

    

Show only objects in collection (Shift to extend)

Parameters:

    

  * **collection_index** (_int in_ _[__-1_ _,__inf_ _]__,__(__optional_ _)_) – Collection Index, Index of the collection to change visibility

  * **toggle** (_boolean_ _,__(__optional_ _)_) – Toggle, Toggle visibility

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend visibility

bpy.ops.object.hide_render_clear_all()¶

    

Reveal all render objects by setting the hide render flag

File:

    

[startup/bl_operators/object.py:728](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L728)

bpy.ops.object.hide_view_clear(_*_ , _select =True_)¶

    

Reveal temporarily hidden objects

Parameters:

    

**select** (_boolean_ _,__(__optional_ _)_) – Select, Select revealed objects

bpy.ops.object.hide_view_set(_*_ , _unselected =False_)¶

    

Temporarily hide objects from the viewport

Parameters:

    

**unselected** (_boolean_ _,__(__optional_ _)_) – Unselected, Hide unselected
rather than selected objects

bpy.ops.object.hook_add_newob()¶

    

Hook selected vertices to a newly created object

bpy.ops.object.hook_add_selob(_*_ , _use_bone =False_)¶

    

Hook selected vertices to the first selected object

Parameters:

    

**use_bone** (_boolean_ _,__(__optional_ _)_) – Active Bone, Assign the hook
to the hook object’s active bone

bpy.ops.object.hook_assign(_*_ , _modifier_)¶

    

Assign the selected vertices to a hook

Parameters:

    

**modifier** (_enum in_ _[__]__,__(__optional_ _)_) – Modifier, Modifier
number to assign to

bpy.ops.object.hook_recenter(_*_ , _modifier_)¶

    

Set hook center to cursor position

Parameters:

    

**modifier** (_enum in_ _[__]__,__(__optional_ _)_) – Modifier, Modifier
number to assign to

bpy.ops.object.hook_remove(_*_ , _modifier_)¶

    

Remove a hook from the active object

Parameters:

    

**modifier** (_enum in_ _[__]__,__(__optional_ _)_) – Modifier, Modifier
number to remove

bpy.ops.object.hook_reset(_*_ , _modifier_)¶

    

Recalculate and clear offset transformation

Parameters:

    

**modifier** (_enum in_ _[__]__,__(__optional_ _)_) – Modifier, Modifier
number to assign to

bpy.ops.object.hook_select(_*_ , _modifier_)¶

    

Select affected vertices on mesh

Parameters:

    

**modifier** (_enum in_ _[__]__,__(__optional_ _)_) – Modifier, Modifier
number to remove

bpy.ops.object.instance_offset_from_cursor()¶

    

Set offset used for collection instances based on cursor position

File:

    

[startup/bl_operators/object.py:909](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L909)

bpy.ops.object.instance_offset_from_object()¶

    

Set offset used for collection instances based on the active object position

File:

    

[startup/bl_operators/object.py:941](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L941)

bpy.ops.object.instance_offset_to_cursor()¶

    

Set cursor position to the offset used for collection instances

File:

    

[startup/bl_operators/object.py:924](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L924)

bpy.ops.object.isolate_type_render()¶

    

Hide unselected render objects of same type as active by setting the hide
render flag

File:

    

[startup/bl_operators/object.py:708](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L708)

bpy.ops.object.join()¶

    

Join selected objects into active object

bpy.ops.object.join_shapes()¶

    

Add the vertex positions of selected objects as shape keys or update existing
shape keys with matching names

bpy.ops.object.join_uvs()¶

    

Transfer UV Maps from active to selected objects (needs matching geometry)

File:

    

[startup/bl_operators/object.py:609](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L609)

bpy.ops.object.laplaciandeform_bind(_*_ , _modifier =''_)¶

    

Bind mesh to system in laplacian deform modifier

Parameters:

    

**modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name
of the modifier to edit

bpy.ops.object.light_add(_*_ , _type =POINT_, _radius =1.0_, _align =WORLD_,
_location =(0.0, 0.0, 0.0)_, _rotation =(0.0, 0.0, 0.0)_, _scale =(0.0, 0.0,
0.0)_)¶

    

Add a light object to the scene

Parameters:

    

  * **type** (enum in [Light Type Items](bpy_types_enum_items/light_type_items.html#rna-enum-light-type-items), (optional)) – Type

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.light_linking_blocker_collection_new()¶

    

Create new light linking collection used by the active emitter

bpy.ops.object.light_linking_blockers_link(_*_ , _link_state =INCLUDE_)¶

    

Light link selected blockers to the active emitter object

Parameters:

    

**link_state** (enum in [`INCLUDE`, `EXCLUDE`], (optional)) –

Link State, State of the shadow linking

  * `INCLUDE` Include – Include selected blockers to cast shadows from the active emitter.

  * `EXCLUDE` Exclude – Exclude selected blockers from casting shadows from the active emitter.

bpy.ops.object.light_linking_blockers_select()¶

    

Select all objects which block light from this emitter

bpy.ops.object.light_linking_receiver_collection_new()¶

    

Create new light linking collection used by the active emitter

bpy.ops.object.light_linking_receivers_link(_*_ , _link_state =INCLUDE_)¶

    

Light link selected receivers to the active emitter object

Parameters:

    

**link_state** (enum in [`INCLUDE`, `EXCLUDE`], (optional)) –

Link State, State of the light linking

  * `INCLUDE` Include – Include selected receivers to receive light from the active emitter.

  * `EXCLUDE` Exclude – Exclude selected receivers from receiving light from the active emitter.

bpy.ops.object.light_linking_receivers_select()¶

    

Select all objects which receive light from this emitter

bpy.ops.object.light_linking_unlink_from_collection()¶

    

Remove this object or collection from the light linking collection

bpy.ops.object.lightprobe_add(_*_ , _type =SPHERE_, _radius =1.0_,
_enter_editmode =False_, _align =WORLD_, _location =(0.0, 0.0, 0.0)_,
_rotation =(0.0, 0.0, 0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Add a light probe object

Parameters:

    

  * **type** (enum in [`SPHERE`, `PLANE`, `VOLUME`], (optional)) – 

Type

    * `SPHERE` Sphere – Light probe that captures precise lighting from all directions at a single point in space.

    * `PLANE` Plane – Light probe that captures incoming light from a single direction on a plane.

    * `VOLUME` Volume – Light probe that captures low frequency lighting inside a volume.

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.lightprobe_cache_bake(_*_ , _subset =ALL_)¶

    

Bake irradiance volume light cache

Parameters:

    

**subset** (enum in [`ALL`, `SELECTED`, `ACTIVE`], (optional)) –

Subset, Subset of probes to update

  * `ALL` All Volumes – Bake all light probe volumes.

  * `SELECTED` Selected Only – Only bake selected light probe volumes.

  * `ACTIVE` Active Only – Only bake the active light probe volume.

bpy.ops.object.lightprobe_cache_free(_*_ , _subset =SELECTED_)¶

    

Delete cached indirect lighting

Parameters:

    

**subset** (enum in [`ALL`, `SELECTED`, `ACTIVE`], (optional)) –

Subset, Subset of probes to update

  * `ALL` All Light Probes – Delete all light probes’ baked lighting data.

  * `SELECTED` Selected Only – Only delete selected light probes’ baked lighting data.

  * `ACTIVE` Active Only – Only delete the active light probe’s baked lighting data.

bpy.ops.object.lineart_bake_strokes(_*_ , _bake_all =False_)¶

    

Bake Line Art for current Grease Pencil object

Parameters:

    

**bake_all** (_boolean_ _,__(__optional_ _)_) – Bake All, Bake all Line Art
modifiers

bpy.ops.object.lineart_clear(_*_ , _clear_all =False_)¶

    

Clear all strokes in current Grease Pencil object

Parameters:

    

**clear_all** (_boolean_ _,__(__optional_ _)_) – Clear All, Clear all Line Art
modifier bakes

bpy.ops.object.link_to_collection(_*_ , _collection_index =-1_, _is_new
=False_, _new_collection_name =''_)¶

    

Link objects to a collection

Parameters:

    

  * **collection_index** (_int in_ _[__-1_ _,__inf_ _]__,__(__optional_ _)_) – Collection Index, Index of the collection to move to

  * **is_new** (_boolean_ _,__(__optional_ _)_) – New, Move objects to a new collection

  * **new_collection_name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the newly added collection

bpy.ops.object.location_clear(_*_ , _clear_delta =False_)¶

    

Clear the object’s location

Parameters:

    

**clear_delta** (_boolean_ _,__(__optional_ _)_) – Clear Delta, Clear delta
location in addition to clearing the normal location transform

bpy.ops.object.make_dupli_face()¶

    

Convert objects into instanced faces

File:

    

[startup/bl_operators/object.py:691](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L691)

bpy.ops.object.make_links_data(_*_ , _type =OBDATA_)¶

    

Transfer data from active object to selected objects

Parameters:

    

**type** (enum in [`OBDATA`, `MATERIAL`, `ANIMATION`, `GROUPS`,
`DUPLICOLLECTION`, `FONTS`, `MODIFIERS`, `EFFECTS`], (optional)) –

Type

  * `OBDATA` Link Object Data – Replace assigned Object Data.

  * `MATERIAL` Link Materials – Replace assigned Materials.

  * `ANIMATION` Link Animation Data – Replace assigned Animation Data.

  * `GROUPS` Link Collections – Replace assigned Collections.

  * `DUPLICOLLECTION` Link Instance Collection – Replace assigned Collection Instance.

  * `FONTS` Link Fonts to Text – Replace Text object Fonts.

  * `MODIFIERS` Copy Modifiers – Replace Modifiers.

  * `EFFECTS` Copy Grease Pencil Effects – Replace Grease Pencil Effects.

bpy.ops.object.make_links_scene(_*_ , _scene_)¶

    

Link selection to another scene

Parameters:

    

**scene** (_enum in_ _[__]__,__(__optional_ _)_) – Scene

bpy.ops.object.make_local(_*_ , _type =SELECT_OBJECT_)¶

    

Make library linked data-blocks local to this file

Parameters:

    

**type** (enum in [`SELECT_OBJECT`, `SELECT_OBDATA`, `SELECT_OBDATA_MATERIAL`,
`ALL`], (optional)) – Type

bpy.ops.object.make_override_library(_*_ , _collection =0_)¶

    

Create a local override of the selected linked objects, and their hierarchy of
dependencies

Parameters:

    

**collection** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) –
Override Collection, Session UID of the directly linked collection containing
the selected object, to make an override from

bpy.ops.object.make_single_user(_*_ , _type =SELECTED_OBJECTS_, _object
=False_, _obdata =False_, _material =False_, _animation =False_,
_obdata_animation =False_)¶

    

Make linked data local to each object

Parameters:

    

  * **type** (enum in [`SELECTED_OBJECTS`, `ALL`], (optional)) – Type

  * **object** (_boolean_ _,__(__optional_ _)_) – Object, Make single user objects

  * **obdata** (_boolean_ _,__(__optional_ _)_) – Object Data, Make single user object data

  * **material** (_boolean_ _,__(__optional_ _)_) – Materials, Make materials local to each data-block

  * **animation** (_boolean_ _,__(__optional_ _)_) – Object Animation, Make object animation data local to each object

  * **obdata_animation** (_boolean_ _,__(__optional_ _)_) – Object Data Animation, Make object data (mesh, curve etc.) animation data local to each object

bpy.ops.object.material_slot_add()¶

    

Add a new material slot

bpy.ops.object.material_slot_assign()¶

    

Assign active material slot to selection

bpy.ops.object.material_slot_copy()¶

    

Copy material to selected objects

bpy.ops.object.material_slot_deselect()¶

    

Deselect by active material slot

bpy.ops.object.material_slot_move(_*_ , _direction =UP_)¶

    

Move the active material up/down in the list

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Direction, Direction to
move the active material towards

bpy.ops.object.material_slot_remove()¶

    

Remove the selected material slot

bpy.ops.object.material_slot_remove_all()¶

    

Remove all materials

bpy.ops.object.material_slot_remove_unused()¶

    

Remove unused material slots

bpy.ops.object.material_slot_select()¶

    

Select by active material slot

bpy.ops.object.meshdeform_bind(_*_ , _modifier =''_)¶

    

Bind mesh to cage in mesh deform modifier

Parameters:

    

**modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name
of the modifier to edit

bpy.ops.object.metaball_add(_*_ , _type =BALL_, _radius =2.0_, _enter_editmode
=False_, _align =WORLD_, _location =(0.0, 0.0, 0.0)_, _rotation =(0.0, 0.0,
0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Add an metaball object to the scene

Parameters:

    

  * **type** (enum in [Metaelem Type Items](bpy_types_enum_items/metaelem_type_items.html#rna-enum-metaelem-type-items), (optional)) – Primitive

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.mode_set(_*_ , _mode =OBJECT_, _toggle =False_)¶

    

Sets the object interaction mode

Parameters:

    

  * **mode** (enum in [Object Mode Items](bpy_types_enum_items/object_mode_items.html#rna-enum-object-mode-items), (optional)) – Mode

  * **toggle** (_boolean_ _,__(__optional_ _)_) – Toggle

bpy.ops.object.mode_set_with_submode(_*_ , _mode =OBJECT_, _toggle =False_,
_mesh_select_mode ={}_)¶

    

Sets the object interaction mode

Parameters:

    

  * **mode** (enum in [Object Mode Items](bpy_types_enum_items/object_mode_items.html#rna-enum-object-mode-items), (optional)) – Mode

  * **toggle** (_boolean_ _,__(__optional_ _)_) – Toggle

  * **mesh_select_mode** (enum set in [Mesh Select Mode Items](bpy_types_enum_items/mesh_select_mode_items.html#rna-enum-mesh-select-mode-items), (optional)) – Mesh Mode

bpy.ops.object.modifier_add(_*_ , _type =SUBSURF_, _use_selected_objects
=False_)¶

    

Add a procedural operation/effect to the active object

Parameters:

    

  * **type** (enum in [Object Modifier Type Items](bpy_types_enum_items/object_modifier_type_items.html#rna-enum-object-modifier-type-items), (optional)) – Type

  * **use_selected_objects** (_boolean_ _,__(__optional_ _)_) – Selected Objects, Affect all selected objects instead of just the active object

bpy.ops.object.modifier_add_node_group(_*_ , _asset_library_type =LOCAL_,
_asset_library_identifier =''_, _relative_asset_identifier =''_, _session_uid
=0_, _use_selected_objects =False_)¶

    

Add a procedural operation/effect to the active object

Parameters:

    

  * **asset_library_type** (enum in [Asset Library Type Items](bpy_types_enum_items/asset_library_type_items.html#rna-enum-asset-library-type-items), (optional)) – Asset Library Type

  * **asset_library_identifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Asset Library Identifier

  * **relative_asset_identifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Relative Asset Identifier

  * **session_uid** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

  * **use_selected_objects** (_boolean_ _,__(__optional_ _)_) – Selected Objects, Affect all selected objects instead of just the active object

bpy.ops.object.modifier_apply(_*_ , _modifier =''_, _report =False_,
_merge_customdata =True_, _single_user =False_, _all_keyframes =False_,
_use_selected_objects =False_)¶

    

Apply modifier and remove from the stack

Parameters:

    

  * **modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name of the modifier to edit

  * **report** (_boolean_ _,__(__optional_ _)_) – Report, Create a notification after the operation

  * **merge_customdata** (_boolean_ _,__(__optional_ _)_) – Merge UVs, For mesh objects, merge UV coordinates that share a vertex to account for imprecision in some modifiers

  * **single_user** (_boolean_ _,__(__optional_ _)_) – Make Data Single User, Make the object’s data single user if needed

  * **all_keyframes** (_boolean_ _,__(__optional_ _)_) – Apply to all keyframes, For Grease Pencil objects, apply the modifier to all the keyframes

  * **use_selected_objects** (_boolean_ _,__(__optional_ _)_) – Selected Objects, Affect all selected objects instead of just the active object

bpy.ops.object.modifier_apply_as_shapekey(_*_ , _keep_modifier =False_,
_modifier =''_, _report =False_, _use_selected_objects =False_)¶

    

Apply modifier as a new shape key and remove from the stack

Parameters:

    

  * **keep_modifier** (_boolean_ _,__(__optional_ _)_) – Keep Modifier, Do not remove the modifier from stack

  * **modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name of the modifier to edit

  * **report** (_boolean_ _,__(__optional_ _)_) – Report, Create a notification after the operation

  * **use_selected_objects** (_boolean_ _,__(__optional_ _)_) – Selected Objects, Affect all selected objects instead of just the active object

bpy.ops.object.modifier_convert(_*_ , _modifier =''_)¶

    

Convert particles to a mesh object

Parameters:

    

**modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name
of the modifier to edit

bpy.ops.object.modifier_copy(_*_ , _modifier =''_, _use_selected_objects
=False_)¶

    

Duplicate modifier at the same position in the stack

Parameters:

    

  * **modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name of the modifier to edit

  * **use_selected_objects** (_boolean_ _,__(__optional_ _)_) – Selected Objects, Affect all selected objects instead of just the active object

bpy.ops.object.modifier_copy_to_selected(_*_ , _modifier =''_)¶

    

Copy the modifier from the active object to all selected objects

Parameters:

    

**modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name
of the modifier to edit

bpy.ops.object.modifier_move_down(_*_ , _modifier =''_)¶

    

Move modifier down in the stack

Parameters:

    

**modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name
of the modifier to edit

bpy.ops.object.modifier_move_to_index(_*_ , _modifier =''_, _index =0_,
_use_selected_objects =False_)¶

    

Change the modifier’s index in the stack so it evaluates after the set number
of others

Parameters:

    

  * **modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name of the modifier to edit

  * **index** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Index, The index to move the modifier to

  * **use_selected_objects** (_boolean_ _,__(__optional_ _)_) – Selected Objects, Affect all selected objects instead of just the active object

bpy.ops.object.modifier_move_up(_*_ , _modifier =''_)¶

    

Move modifier up in the stack

Parameters:

    

**modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name
of the modifier to edit

bpy.ops.object.modifier_remove(_*_ , _modifier =''_, _report =False_,
_use_selected_objects =False_)¶

    

Remove a modifier from the active object

Parameters:

    

  * **modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name of the modifier to edit

  * **report** (_boolean_ _,__(__optional_ _)_) – Report, Create a notification after the operation

  * **use_selected_objects** (_boolean_ _,__(__optional_ _)_) – Selected Objects, Affect all selected objects instead of just the active object

bpy.ops.object.modifier_set_active(_*_ , _modifier =''_)¶

    

Activate the modifier to use as the context

Parameters:

    

**modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name
of the modifier to edit

bpy.ops.object.modifiers_clear()¶

    

Clear all modifiers from the selected objects

bpy.ops.object.modifiers_copy_to_selected()¶

    

Copy modifiers to other selected objects

bpy.ops.object.move_to_collection(_*_ , _collection_index =-1_, _is_new
=False_, _new_collection_name =''_)¶

    

Move objects to a collection

Parameters:

    

  * **collection_index** (_int in_ _[__-1_ _,__inf_ _]__,__(__optional_ _)_) – Collection Index, Index of the collection to move to

  * **is_new** (_boolean_ _,__(__optional_ _)_) – New, Move objects to a new collection

  * **new_collection_name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the newly added collection

bpy.ops.object.multires_base_apply(_*_ , _modifier =''_)¶

    

Modify the base mesh to conform to the displaced mesh

Parameters:

    

**modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name
of the modifier to edit

bpy.ops.object.multires_external_pack()¶

    

Pack displacements from an external file

bpy.ops.object.multires_external_save(_*_ , _filepath =''_, _hide_props_region
=True_, _check_existing =True_, _filter_blender =False_, _filter_backup
=False_, _filter_image =False_, _filter_movie =False_, _filter_python =False_,
_filter_font =False_, _filter_sound =False_, _filter_text =False_,
_filter_archive =False_, _filter_btx =True_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =9_, _relative_path =True_, _display_type =DEFAULT_, _sort_method_ ,
_modifier =''_)¶

    

Save displacements to an external file

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

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

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name of the modifier to edit

bpy.ops.object.multires_higher_levels_delete(_*_ , _modifier =''_)¶

    

Deletes the higher resolution mesh, potential loss of detail

Parameters:

    

**modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name
of the modifier to edit

bpy.ops.object.multires_rebuild_subdiv(_*_ , _modifier =''_)¶

    

Rebuilds all possible subdivisions levels to generate a lower resolution base
mesh

Parameters:

    

**modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name
of the modifier to edit

bpy.ops.object.multires_reshape(_*_ , _modifier =''_)¶

    

Copy vertex coordinates from other object

Parameters:

    

**modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name
of the modifier to edit

bpy.ops.object.multires_subdivide(_*_ , _modifier =''_, _mode
=CATMULL_CLARK_)¶

    

Add a new level of subdivision

Parameters:

    

  * **modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name of the modifier to edit

  * **mode** (enum in [`CATMULL_CLARK`, `SIMPLE`, `LINEAR`], (optional)) – 

Subdivision Mode, How the mesh is going to be subdivided to create a new level

    * `CATMULL_CLARK` Catmull-Clark – Create a new level using Catmull-Clark subdivisions.

    * `SIMPLE` Simple – Create a new level using simple subdivisions.

    * `LINEAR` Linear – Create a new level using linear interpolation of the sculpted displacement.

bpy.ops.object.multires_unsubdivide(_*_ , _modifier =''_)¶

    

Rebuild a lower subdivision level of the current base mesh

Parameters:

    

**modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name
of the modifier to edit

bpy.ops.object.ocean_bake(_*_ , _modifier =''_, _free =False_)¶

    

Bake an image sequence of ocean data

Parameters:

    

  * **modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name of the modifier to edit

  * **free** (_boolean_ _,__(__optional_ _)_) – Free, Free the bake, rather than generating it

bpy.ops.object.origin_clear()¶

    

Clear the object’s origin

bpy.ops.object.origin_set(_*_ , _type =GEOMETRY_ORIGIN_, _center =MEDIAN_)¶

    

Set the object’s origin, by either moving the data, or set to center of data,
or use 3D cursor

Parameters:

    

  * **type** (enum in [`GEOMETRY_ORIGIN`, `ORIGIN_GEOMETRY`, `ORIGIN_CURSOR`, `ORIGIN_CENTER_OF_MASS`, `ORIGIN_CENTER_OF_VOLUME`], (optional)) – 

Type

    * `GEOMETRY_ORIGIN` Geometry to Origin – Move object geometry to object origin.

    * `ORIGIN_GEOMETRY` Origin to Geometry – Calculate the center of geometry based on the current pivot point (median, otherwise bounding box).

    * `ORIGIN_CURSOR` Origin to 3D Cursor – Move object origin to position of the 3D cursor.

    * `ORIGIN_CENTER_OF_MASS` Origin to Center of Mass (Surface) – Calculate the center of mass from the surface area.

    * `ORIGIN_CENTER_OF_VOLUME` Origin to Center of Mass (Volume) – Calculate the center of mass from the volume (must be manifold geometry with consistent normals).

  * **center** (enum in [`MEDIAN`, `BOUNDS`], (optional)) – Center

bpy.ops.object.parent_clear(_*_ , _type =CLEAR_)¶

    

Clear the object’s parenting

Parameters:

    

**type** (enum in [`CLEAR`, `CLEAR_KEEP_TRANSFORM`, `CLEAR_INVERSE`],
(optional)) –

Type

  * `CLEAR` Clear Parent – Completely clear the parenting relationship, including involved modifiers if any.

  * `CLEAR_KEEP_TRANSFORM` Clear and Keep Transformation – As ‘Clear Parent’, but keep the current visual transformations of the object.

  * `CLEAR_INVERSE` Clear Parent Inverse – Reset the transform corrections applied to the parenting relationship, does not remove parenting itself.

bpy.ops.object.parent_inverse_apply()¶

    

Apply the object’s parent inverse to its data

bpy.ops.object.parent_no_inverse_set(_*_ , _keep_transform =False_)¶

    

Set the object’s parenting without setting the inverse parent correction

Parameters:

    

**keep_transform** (_boolean_ _,__(__optional_ _)_) – Keep Transform, Preserve
the world transform throughout parenting

bpy.ops.object.parent_set(_*_ , _type =OBJECT_, _xmirror =False_,
_keep_transform =False_)¶

    

Set the object’s parenting

Parameters:

    

  * **type** (enum in [`OBJECT`, `ARMATURE`, `ARMATURE_NAME`, `ARMATURE_AUTO`, `ARMATURE_ENVELOPE`, `BONE`, `BONE_RELATIVE`, `CURVE`, `FOLLOW`, `PATH_CONST`, `LATTICE`, `VERTEX`, `VERTEX_TRI`], (optional)) – Type

  * **xmirror** (_boolean_ _,__(__optional_ _)_) – X Mirror, Apply weights symmetrically along X axis, for Envelope/Automatic vertex groups creation

  * **keep_transform** (_boolean_ _,__(__optional_ _)_) – Keep Transform, Apply transformation before parenting

bpy.ops.object.particle_system_add()¶

    

Add a particle system

bpy.ops.object.particle_system_remove()¶

    

Remove the selected particle system

bpy.ops.object.paths_calculate(_*_ , _display_type =RANGE_, _range =SCENE_)¶

    

Generate motion paths for the selected objects

Parameters:

    

  * **display_type** (enum in [Motionpath Display Type Items](bpy_types_enum_items/motionpath_display_type_items.html#rna-enum-motionpath-display-type-items), (optional)) – Display type

  * **range** (enum in [Motionpath Range Items](bpy_types_enum_items/motionpath_range_items.html#rna-enum-motionpath-range-items), (optional)) – Computation Range

bpy.ops.object.paths_clear(_*_ , _only_selected =False_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

**only_selected** (_boolean_ _,__(__optional_ _)_) – Only Selected, Only clear
motion paths of selected objects

bpy.ops.object.paths_update()¶

    

Recalculate motion paths for selected objects

bpy.ops.object.paths_update_visible()¶

    

Recalculate all visible motion paths for objects and poses

bpy.ops.object.pointcloud_random_add(_*_ , _align =WORLD_, _location =(0.0,
0.0, 0.0)_, _rotation =(0.0, 0.0, 0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Add a point cloud object to the scene

Parameters:

    

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.posemode_toggle()¶

    

Enable or disable posing/selecting bones

bpy.ops.object.quadriflow_remesh(_*_ , _use_mesh_symmetry =True_,
_use_preserve_sharp =False_, _use_preserve_boundary =False_,
_preserve_attributes =False_, _smooth_normals =False_, _mode =FACES_,
_target_ratio =1.0_, _target_edge_length =0.1_, _target_faces =4000_,
_mesh_area =-1.0_, _seed =0_)¶

    

Create a new quad based mesh using the surface data of the current mesh. All
data layers will be lost

Parameters:

    

  * **use_mesh_symmetry** (_boolean_ _,__(__optional_ _)_) – Use Mesh Symmetry, Generates a symmetrical mesh using the mesh symmetry configuration

  * **use_preserve_sharp** (_boolean_ _,__(__optional_ _)_) – Preserve Sharp, Try to preserve sharp features on the mesh

  * **use_preserve_boundary** (_boolean_ _,__(__optional_ _)_) – Preserve Mesh Boundary, Try to preserve mesh boundary on the mesh

  * **preserve_attributes** (_boolean_ _,__(__optional_ _)_) – Preserve Attributes, Reproject attributes onto the new mesh

  * **smooth_normals** (_boolean_ _,__(__optional_ _)_) – Smooth Normals, Set the output mesh normals to smooth

  * **mode** (enum in [`RATIO`, `EDGE`, `FACES`], (optional)) – 

Mode, How to specify the amount of detail for the new mesh

    * `RATIO` Ratio – Specify target number of faces relative to the current mesh.

    * `EDGE` Edge Length – Input target edge length in the new mesh.

    * `FACES` Faces – Input target number of faces in the new mesh.

  * **target_ratio** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Ratio, Relative number of faces compared to the current mesh

  * **target_edge_length** (_float in_ _[__1e-07_ _,__inf_ _]__,__(__optional_ _)_) – Edge Length, Target edge length in the new mesh

  * **target_faces** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Number of Faces, Approximate number of faces (quads) in the new mesh

  * **mesh_area** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Old Object Face Area, This property is only used to cache the object area for later calculations

  * **seed** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Seed, Random seed to use with the solver. Different seeds will cause the remesher to come up with different quad layouts on the mesh

bpy.ops.object.quick_explode(_*_ , _style =EXPLODE_, _amount =100_,
_frame_duration =50_, _frame_start =1_, _frame_end =10_, _velocity =1.0_,
_fade =True_)¶

    

Make selected objects explode

Parameters:

    

  * **style** (enum in [`EXPLODE`, `BLEND`], (optional)) – Explode Style

  * **amount** (_int in_ _[__2_ _,__10000_ _]__,__(__optional_ _)_) – Number of Pieces

  * **frame_duration** (_int in_ _[__1_ _,__300000_ _]__,__(__optional_ _)_) – Duration

  * **frame_start** (_int in_ _[__1_ _,__300000_ _]__,__(__optional_ _)_) – Start Frame

  * **frame_end** (_int in_ _[__1_ _,__300000_ _]__,__(__optional_ _)_) – End Frame

  * **velocity** (_float in_ _[__0_ _,__300000_ _]__,__(__optional_ _)_) – Outwards Velocity

  * **fade** (_boolean_ _,__(__optional_ _)_) – Fade, Fade the pieces over time

File:

    

[startup/bl_operators/object_quick_effects.py:260](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_quick_effects.py#L260)

bpy.ops.object.quick_fur(_*_ , _density =MEDIUM_, _length =0.1_, _radius
=0.001_, _view_percentage =1.0_, _apply_hair_guides =True_, _use_noise =True_,
_use_frizz =True_)¶

    

Add a fur setup to the selected objects

Parameters:

    

  * **density** (enum in [`LOW`, `MEDIUM`, `HIGH`], (optional)) – Density

  * **length** (_float in_ _[__0.001_ _,__100_ _]__,__(__optional_ _)_) – Length

  * **radius** (_float in_ _[__0_ _,__10_ _]__,__(__optional_ _)_) – Hair Radius

  * **view_percentage** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – View Percentage

  * **apply_hair_guides** (_boolean_ _,__(__optional_ _)_) – Apply Hair Guides

  * **use_noise** (_boolean_ _,__(__optional_ _)_) – Noise

  * **use_frizz** (_boolean_ _,__(__optional_ _)_) – Frizz

File:

    

[startup/bl_operators/object_quick_effects.py:91](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_quick_effects.py#L91)

bpy.ops.object.quick_liquid(_*_ , _show_flows =False_)¶

    

Make selected objects liquid

Parameters:

    

**show_flows** (_boolean_ _,__(__optional_ _)_) – Render Liquid Objects, Keep
the liquid objects visible during rendering

File:

    

[startup/bl_operators/object_quick_effects.py:546](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_quick_effects.py#L546)

bpy.ops.object.quick_smoke(_*_ , _style =SMOKE_, _show_flows =False_)¶

    

Use selected objects as smoke emitters

Parameters:

    

  * **style** (enum in [`SMOKE`, `FIRE`, `BOTH`], (optional)) – Smoke Style

  * **show_flows** (_boolean_ _,__(__optional_ _)_) – Render Smoke Objects, Keep the smoke objects visible during rendering

File:

    

[startup/bl_operators/object_quick_effects.py:437](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_quick_effects.py#L437)

bpy.ops.object.randomize_transform(_*_ , _random_seed =0_, _use_delta =False_,
_use_loc =True_, _loc =(0.0, 0.0, 0.0)_, _use_rot =True_, _rot =(0.0, 0.0,
0.0)_, _use_scale =True_, _scale_even =False_, _scale =(1.0, 1.0, 1.0)_)¶

    

Randomize objects location, rotation, and scale

Parameters:

    

  * **random_seed** (_int in_ _[__0_ _,__10000_ _]__,__(__optional_ _)_) – Random Seed, Seed value for the random generator

  * **use_delta** (_boolean_ _,__(__optional_ _)_) – Transform Delta, Randomize delta transform values instead of regular transform

  * **use_loc** (_boolean_ _,__(__optional_ _)_) – Randomize Location, Randomize the location values

  * **loc** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-100, 100], (optional)) – Location, Maximum distance the objects can spread over each axis

  * **use_rot** (_boolean_ _,__(__optional_ _)_) – Randomize Rotation, Randomize the rotation values

  * **rot** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-3.14159, 3.14159], (optional)) – Rotation, Maximum rotation over each axis

  * **use_scale** (_boolean_ _,__(__optional_ _)_) – Randomize Scale, Randomize the scale values

  * **scale_even** (_boolean_ _,__(__optional_ _)_) – Scale Even, Use the same scale value for all axis

  * **scale** (_float array_ _of_ _3 items in_ _[__-100_ _,__100_ _]__,__(__optional_ _)_) – Scale, Maximum scale randomization over each axis

File:

    

[startup/bl_operators/object_randomize_transform.py:161](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_randomize_transform.py#L161)

bpy.ops.object.reset_override_library()¶

    

Reset the selected local overrides to their linked references values

bpy.ops.object.rotation_clear(_*_ , _clear_delta =False_)¶

    

Clear the object’s rotation

Parameters:

    

**clear_delta** (_boolean_ _,__(__optional_ _)_) – Clear Delta, Clear delta
rotation in addition to clearing the normal rotation transform

bpy.ops.object.scale_clear(_*_ , _clear_delta =False_)¶

    

Clear the object’s scale

Parameters:

    

**clear_delta** (_boolean_ _,__(__optional_ _)_) – Clear Delta, Clear delta
scale in addition to clearing the normal scale transform

bpy.ops.object.select_all(_*_ , _action =TOGGLE_)¶

    

Change selection of all visible objects in scene

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.object.select_by_type(_*_ , _extend =False_, _type =MESH_)¶

    

Select all visible objects that are of a type

Parameters:

    

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection instead of deselecting everything first

  * **type** (enum in [Object Type Items](bpy_types_enum_items/object_type_items.html#rna-enum-object-type-items), (optional)) – Type

bpy.ops.object.select_camera(_*_ , _extend =False_)¶

    

Select the active camera

Parameters:

    

**extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend the selection

File:

    

[startup/bl_operators/object.py:122](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L122)

bpy.ops.object.select_grouped(_*_ , _extend =False_, _type
=CHILDREN_RECURSIVE_)¶

    

Select all visible objects grouped by various properties

Parameters:

    

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection instead of deselecting everything first

  * **type** (enum in [`CHILDREN_RECURSIVE`, `CHILDREN`, `PARENT`, `SIBLINGS`, `TYPE`, `COLLECTION`, `HOOK`, `PASS`, `COLOR`, `KEYINGSET`, `LIGHT_TYPE`], (optional)) – 

Type

    * `CHILDREN_RECURSIVE` Children.

    * `CHILDREN` Immediate Children.

    * `PARENT` Parent.

    * `SIBLINGS` Siblings – Shared parent.

    * `TYPE` Type – Shared object type.

    * `COLLECTION` Collection – Shared collection.

    * `HOOK` Hook.

    * `PASS` Pass – Render pass index.

    * `COLOR` Color – Object color.

    * `KEYINGSET` Keying Set – Objects included in active Keying Set.

    * `LIGHT_TYPE` Light Type – Matching light types.

bpy.ops.object.select_hierarchy(_*_ , _direction =PARENT_, _extend =False_)¶

    

Select object relative to the active object’s position in the hierarchy

Parameters:

    

  * **direction** (enum in [`PARENT`, `CHILD`], (optional)) – Direction, Direction to select in the hierarchy

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend the existing selection

File:

    

[startup/bl_operators/object.py:172](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L172)

bpy.ops.object.select_less()¶

    

Deselect objects at the boundaries of parent/child relationships

bpy.ops.object.select_linked(_*_ , _extend =False_, _type =OBDATA_)¶

    

Select all visible objects that are linked

Parameters:

    

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection instead of deselecting everything first

  * **type** (enum in [`OBDATA`, `MATERIAL`, `DUPGROUP`, `PARTICLE`, `LIBRARY`, `LIBRARY_OBDATA`], (optional)) – Type

bpy.ops.object.select_mirror(_*_ , _extend =False_)¶

    

Select the mirror objects of the selected object e.g. “L.sword” and “R.sword”

Parameters:

    

**extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection instead
of deselecting everything first

bpy.ops.object.select_more()¶

    

Select connected parent/child objects

bpy.ops.object.select_pattern(_*_ , _pattern ='*'_, _case_sensitive =False_,
_extend =True_)¶

    

Select objects matching a naming pattern

Parameters:

    

  * **pattern** (_string_ _,__(__optional_ _,__never None_ _)_) – Pattern, Name filter using ‘*’, ‘?’ and ‘[abc]’ unix style wildcards

  * **case_sensitive** (_boolean_ _,__(__optional_ _)_) – Case Sensitive, Do a case sensitive compare

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend the existing selection

File:

    

[startup/bl_operators/object.py:45](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L45)

bpy.ops.object.select_random(_*_ , _ratio =0.5_, _seed =0_, _action =SELECT_)¶

    

Select or deselect random visible objects

Parameters:

    

  * **ratio** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Ratio, Portion of items to select randomly

  * **seed** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Random Seed, Seed for the random number generator

  * **action** (enum in [`SELECT`, `DESELECT`], (optional)) – 

Action, Selection action to execute

    * `SELECT` Select – Select all elements.

    * `DESELECT` Deselect – Deselect all elements.

bpy.ops.object.select_same_collection(_*_ , _collection =''_)¶

    

Select object in the same collection

Parameters:

    

**collection** (_string_ _,__(__optional_ _,__never None_ _)_) – Collection,
Name of the collection to select

bpy.ops.object.shade_auto_smooth(_*_ , _use_auto_smooth =True_, _angle
=0.523599_)¶

    

Add modifier to automatically set the sharpness of mesh edges based on the
angle between the neighboring faces

Parameters:

    

  * **use_auto_smooth** (_boolean_ _,__(__optional_ _)_) – Auto Smooth, Add modifier to set edge sharpness automatically

  * **angle** (_float in_ _[__0_ _,__3.14159_ _]__,__(__optional_ _)_) – Angle, Maximum angle between face normals that will be considered as smooth

bpy.ops.object.shade_flat(_*_ , _keep_sharp_edges =True_)¶

    

Render and display faces uniform, using face normals

Parameters:

    

**keep_sharp_edges** (_boolean_ _,__(__optional_ _)_) – Keep Sharp Edges,
Don’t remove sharp edges, which are redundant with faces shaded smooth

bpy.ops.object.shade_smooth(_*_ , _keep_sharp_edges =True_)¶

    

Render and display faces smooth, using interpolated vertex normals

Parameters:

    

**keep_sharp_edges** (_boolean_ _,__(__optional_ _)_) – Keep Sharp Edges,
Don’t remove sharp edges. Tagged edges will remain sharp

bpy.ops.object.shade_smooth_by_angle(_*_ , _angle =0.523599_,
_keep_sharp_edges =True_)¶

    

Set the sharpness of mesh edges based on the angle between the neighboring
faces

Parameters:

    

  * **angle** (_float in_ _[__0_ _,__3.14159_ _]__,__(__optional_ _)_) – Angle, Maximum angle between face normals that will be considered as smooth

  * **keep_sharp_edges** (_boolean_ _,__(__optional_ _)_) – Keep Sharp Edges, Only add sharp edges instead of clearing existing tags first

bpy.ops.object.shaderfx_add(_*_ , _type =FX_BLUR_)¶

    

Add a visual effect to the active object

Parameters:

    

**type** (enum in [Object Shaderfx Type
Items](bpy_types_enum_items/object_shaderfx_type_items.html#rna-enum-object-
shaderfx-type-items), (optional)) – Type

bpy.ops.object.shaderfx_copy(_*_ , _shaderfx =''_)¶

    

Duplicate effect at the same position in the stack

Parameters:

    

**shaderfx** (_string_ _,__(__optional_ _,__never None_ _)_) – Shader, Name of
the shaderfx to edit

bpy.ops.object.shaderfx_move_down(_*_ , _shaderfx =''_)¶

    

Move effect down in the stack

Parameters:

    

**shaderfx** (_string_ _,__(__optional_ _,__never None_ _)_) – Shader, Name of
the shaderfx to edit

bpy.ops.object.shaderfx_move_to_index(_*_ , _shaderfx =''_, _index =0_)¶

    

Change the effect’s position in the list so it evaluates after the set number
of others

Parameters:

    

  * **shaderfx** (_string_ _,__(__optional_ _,__never None_ _)_) – Shader, Name of the shaderfx to edit

  * **index** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Index, The index to move the effect to

bpy.ops.object.shaderfx_move_up(_*_ , _shaderfx =''_)¶

    

Move effect up in the stack

Parameters:

    

**shaderfx** (_string_ _,__(__optional_ _,__never None_ _)_) – Shader, Name of
the shaderfx to edit

bpy.ops.object.shaderfx_remove(_*_ , _shaderfx =''_, _report =False_)¶

    

Remove a effect from the active Grease Pencil object

Parameters:

    

  * **shaderfx** (_string_ _,__(__optional_ _,__never None_ _)_) – Shader, Name of the shaderfx to edit

  * **report** (_boolean_ _,__(__optional_ _)_) – Report, Create a notification after the operation

bpy.ops.object.shape_key_add(_*_ , _from_mix =True_)¶

    

Add shape key to the object

Parameters:

    

**from_mix** (_boolean_ _,__(__optional_ _)_) – From Mix, Create the new shape
key from the existing mix of keys

bpy.ops.object.shape_key_clear()¶

    

Reset the weights of all shape keys to 0 or to the closest value respecting
the limits

bpy.ops.object.shape_key_copy()¶

    

Duplicate the active shape key

bpy.ops.object.shape_key_lock(_*_ , _action =LOCK_)¶

    

Change the lock state of all shape keys of active object

Parameters:

    

**action** (enum in [`LOCK`, `UNLOCK`], (optional)) –

Action, Lock action to execute on vertex groups

  * `LOCK` Lock – Lock all shape keys.

  * `UNLOCK` Unlock – Unlock all shape keys.

bpy.ops.object.shape_key_mirror(_*_ , _use_topology =False_)¶

    

Mirror the current shape key along the local X axis

Parameters:

    

**use_topology** (_boolean_ _,__(__optional_ _)_) – Topology Mirror, Use
topology based mirroring (for when both sides of mesh have matching, unique
topology)

bpy.ops.object.shape_key_move(_*_ , _type =TOP_)¶

    

Move the active shape key up/down in the list

Parameters:

    

**type** (enum in [`TOP`, `UP`, `DOWN`, `BOTTOM`], (optional)) –

Type

  * `TOP` Top – Top of the list.

  * `UP` Up.

  * `DOWN` Down.

  * `BOTTOM` Bottom – Bottom of the list.

bpy.ops.object.shape_key_remove(_*_ , _all =False_, _apply_mix =False_)¶

    

Remove shape key from the object

Parameters:

    

  * **all** (_boolean_ _,__(__optional_ _)_) – All, Remove all shape keys

  * **apply_mix** (_boolean_ _,__(__optional_ _)_) – Apply Mix, Apply current mix of shape keys to the geometry before removing them

bpy.ops.object.shape_key_retime()¶

    

Resets the timing for absolute shape keys

bpy.ops.object.shape_key_transfer(_*_ , _mode =OFFSET_, _use_clamp =False_)¶

    

Copy the active shape key of another selected object to this one

Parameters:

    

  * **mode** (enum in [`OFFSET`, `RELATIVE_FACE`, `RELATIVE_EDGE`], (optional)) – 

Transformation Mode, Relative shape positions to the new shape method

    * `OFFSET` Offset – Apply the relative positional offset.

    * `RELATIVE_FACE` Relative Face – Calculate relative position (using faces).

    * `RELATIVE_EDGE` Relative Edge – Calculate relative position (using edges).

  * **use_clamp** (_boolean_ _,__(__optional_ _)_) – Clamp Offset, Clamp the transformation to the distance each vertex moves in the original shape

File:

    

[startup/bl_operators/object.py:501](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L501)

bpy.ops.object.simulation_nodes_cache_bake(_*_ , _selected =False_)¶

    

Bake simulations in geometry nodes modifiers

Parameters:

    

**selected** (_boolean_ _,__(__optional_ _)_) – Selected, Bake cache on all
selected objects

bpy.ops.object.simulation_nodes_cache_calculate_to_frame(_*_ , _selected
=False_)¶

    

Calculate simulations in geometry nodes modifiers from the start to current
frame

Parameters:

    

**selected** (_boolean_ _,__(__optional_ _)_) – Selected, Calculate all
selected objects instead of just the active object

bpy.ops.object.simulation_nodes_cache_delete(_*_ , _selected =False_)¶

    

Delete cached/baked simulations in geometry nodes modifiers

Parameters:

    

**selected** (_boolean_ _,__(__optional_ _)_) – Selected, Delete cache on all
selected objects

bpy.ops.object.skin_armature_create(_*_ , _modifier =''_)¶

    

Create an armature that parallels the skin layout

Parameters:

    

**modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name
of the modifier to edit

bpy.ops.object.skin_loose_mark_clear(_*_ , _action =MARK_)¶

    

Mark/clear selected vertices as loose

Parameters:

    

**action** (enum in [`MARK`, `CLEAR`], (optional)) –

Action

  * `MARK` Mark – Mark selected vertices as loose.

  * `CLEAR` Clear – Set selected vertices as not loose.

bpy.ops.object.skin_radii_equalize()¶

    

Make skin radii of selected vertices equal on each axis

bpy.ops.object.skin_root_mark()¶

    

Mark selected vertices as roots

bpy.ops.object.speaker_add(_*_ , _enter_editmode =False_, _align =WORLD_,
_location =(0.0, 0.0, 0.0)_, _rotation =(0.0, 0.0, 0.0)_, _scale =(0.0, 0.0,
0.0)_)¶

    

Add a speaker object to the scene

Parameters:

    

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.subdivision_set(_*_ , _level =1_, _relative =False_,
_ensure_modifier =True_)¶

    

Sets a Subdivision Surface level (1 to 5)

Parameters:

    

  * **level** (_int in_ _[__-100_ _,__100_ _]__,__(__optional_ _)_) – Level

  * **relative** (_boolean_ _,__(__optional_ _)_) – Relative, Apply the subdivision surface level as an offset relative to the current level

  * **ensure_modifier** (_boolean_ _,__(__optional_ _)_) – Ensure Modifier, Create the corresponding modifier if it does not exist

File:

    

[startup/bl_operators/object.py:245](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L245)

bpy.ops.object.surfacedeform_bind(_*_ , _modifier =''_)¶

    

Bind mesh to target in surface deform modifier

Parameters:

    

**modifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Modifier, Name
of the modifier to edit

bpy.ops.object.text_add(_*_ , _radius =1.0_, _enter_editmode =False_, _align
=WORLD_, _location =(0.0, 0.0, 0.0)_, _rotation =(0.0, 0.0, 0.0)_, _scale
=(0.0, 0.0, 0.0)_)¶

    

Add a text object to the scene

Parameters:

    

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.track_clear(_*_ , _type =CLEAR_)¶

    

Clear tracking constraint or flag from object

Parameters:

    

**type** (enum in [`CLEAR`, `CLEAR_KEEP_TRANSFORM`], (optional)) – Type

bpy.ops.object.track_set(_*_ , _type =DAMPTRACK_)¶

    

Make the object track another object, using various methods/constraints

Parameters:

    

**type** (enum in [`DAMPTRACK`, `TRACKTO`, `LOCKTRACK`], (optional)) – Type

bpy.ops.object.transfer_mode(_*_ , _use_flash_on_transfer =True_)¶

    

Switches the active object and assigns the same mode to a new one under the
mouse cursor, leaving the active mode in the current one

Parameters:

    

**use_flash_on_transfer** (_boolean_ _,__(__optional_ _)_) – Flash On
Transfer, Flash the target object when transferring the mode

bpy.ops.object.transform_apply(_*_ , _location =True_, _rotation =True_,
_scale =True_, _properties =True_, _isolate_users =False_)¶

    

Apply the object’s transformation to its data

Parameters:

    

  * **location** (_boolean_ _,__(__optional_ _)_) – Location

  * **rotation** (_boolean_ _,__(__optional_ _)_) – Rotation

  * **scale** (_boolean_ _,__(__optional_ _)_) – Scale

  * **properties** (_boolean_ _,__(__optional_ _)_) – Apply Properties, Modify properties such as curve vertex radius, font size and bone envelope

  * **isolate_users** (_boolean_ _,__(__optional_ _)_) – Isolate Multi User Data, Create new object-data users if needed

bpy.ops.object.transform_axis_target()¶

    

Interactively point cameras and lights to a location (Ctrl translates)

bpy.ops.object.transform_to_mouse(_*_ , _name =''_, _session_uid =0_, _matrix
=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0,
0.0, 0.0))_, _drop_x =0_, _drop_y =0_)¶

    

Snap selected item(s) to the mouse location

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Object name to place (uses the active object when this and ‘session_uid’ are unset)

  * **session_uid** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Session UUID, Session UUID of the object to place (uses the active object when this and ‘name’ are unset)

  * **matrix** ([`mathutils.Matrix`](mathutils.html#mathutils.Matrix "mathutils.Matrix") of 4 * 4 items in [-inf, inf], (optional)) – Matrix

  * **drop_x** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Drop X, X-coordinate (screen space) to place the new object under

  * **drop_y** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Drop Y, Y-coordinate (screen space) to place the new object under

bpy.ops.object.transforms_to_deltas(_*_ , _mode =ALL_, _reset_values =True_)¶

    

Convert normal object transforms to delta transforms, any existing delta
transforms will be included as well

Parameters:

    

  * **mode** (enum in [`ALL`, `LOC`, `ROT`, `SCALE`], (optional)) – 

Mode, Which transforms to transfer

    * `ALL` All Transforms – Transfer location, rotation, and scale transforms.

    * `LOC` Location – Transfer location transforms only.

    * `ROT` Rotation – Transfer rotation transforms only.

    * `SCALE` Scale – Transfer scale transforms only.

  * **reset_values** (_boolean_ _,__(__optional_ _)_) – Reset Values, Clear transform values after transferring to deltas

File:

    

[startup/bl_operators/object.py:763](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L763)

bpy.ops.object.unlink_data()¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

bpy.ops.object.update_shapes()¶

    

Update existing shape keys with the vertex positions of selected objects with
matching names

bpy.ops.object.vertex_group_add()¶

    

Add a new vertex group to the active object

bpy.ops.object.vertex_group_assign()¶

    

Assign the selected vertices to the active vertex group

bpy.ops.object.vertex_group_assign_new()¶

    

Assign the selected vertices to a new vertex group

bpy.ops.object.vertex_group_clean(_*_ , _group_select_mode_ , _limit =0.0_,
_keep_single =False_)¶

    

Remove vertex group assignments which are not required

Parameters:

    

  * **group_select_mode** (_enum in_ _[__]__,__(__optional_ _)_) – Subset, Define which subset of groups shall be used

  * **limit** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Limit, Remove vertices which weight is below or equal to this limit

  * **keep_single** (_boolean_ _,__(__optional_ _)_) – Keep Single, Keep verts assigned to at least one group when cleaning

bpy.ops.object.vertex_group_copy()¶

    

Make a copy of the active vertex group

bpy.ops.object.vertex_group_copy_to_selected()¶

    

Replace vertex groups of selected objects by vertex groups of active object

bpy.ops.object.vertex_group_deselect()¶

    

Deselect all selected vertices assigned to the active vertex group

bpy.ops.object.vertex_group_invert(_*_ , _group_select_mode_ , _auto_assign
=True_, _auto_remove =True_)¶

    

Invert active vertex group’s weights

Parameters:

    

  * **group_select_mode** (_enum in_ _[__]__,__(__optional_ _)_) – Subset, Define which subset of groups shall be used

  * **auto_assign** (_boolean_ _,__(__optional_ _)_) – Add Weights, Add vertices from groups that have zero weight before inverting

  * **auto_remove** (_boolean_ _,__(__optional_ _)_) – Remove Weights, Remove vertices from groups that have zero weight after inverting

bpy.ops.object.vertex_group_levels(_*_ , _group_select_mode_ , _offset =0.0_,
_gain =1.0_)¶

    

Add some offset and multiply with some gain the weights of the active vertex
group

Parameters:

    

  * **group_select_mode** (_enum in_ _[__]__,__(__optional_ _)_) – Subset, Define which subset of groups shall be used

  * **offset** (_float in_ _[__-1_ _,__1_ _]__,__(__optional_ _)_) – Offset, Value to add to weights

  * **gain** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Gain, Value to multiply weights by

bpy.ops.object.vertex_group_limit_total(_*_ , _group_select_mode_ , _limit
=4_)¶

    

Limit deform weights associated with a vertex to a specified number by
removing lowest weights

Parameters:

    

  * **group_select_mode** (_enum in_ _[__]__,__(__optional_ _)_) – Subset, Define which subset of groups shall be used

  * **limit** (_int in_ _[__1_ _,__32_ _]__,__(__optional_ _)_) – Limit, Maximum number of deform weights

bpy.ops.object.vertex_group_lock(_*_ , _action =TOGGLE_, _mask =ALL_)¶

    

Change the lock state of all or some vertex groups of active object

Parameters:

    

  * **action** (enum in [`TOGGLE`, `LOCK`, `UNLOCK`, `INVERT`], (optional)) – 

Action, Lock action to execute on vertex groups

    * `TOGGLE` Toggle – Unlock all vertex groups if there is at least one locked group, lock all in other case.

    * `LOCK` Lock – Lock all vertex groups.

    * `UNLOCK` Unlock – Unlock all vertex groups.

    * `INVERT` Invert – Invert the lock state of all vertex groups.

  * **mask** (enum in [`ALL`, `SELECTED`, `UNSELECTED`, `INVERT_UNSELECTED`], (optional)) – 

Mask, Apply the action based on vertex group selection

    * `ALL` All – Apply action to all vertex groups.

    * `SELECTED` Selected – Apply to selected vertex groups.

    * `UNSELECTED` Unselected – Apply to unselected vertex groups.

    * `INVERT_UNSELECTED` Invert Unselected – Apply the opposite of Lock/Unlock to unselected vertex groups.

bpy.ops.object.vertex_group_mirror(_*_ , _mirror_weights =True_,
_flip_group_names =True_, _all_groups =False_, _use_topology =False_)¶

    

Mirror vertex group, flip weights and/or names, editing only selected
vertices, flipping when both sides are selected otherwise copy from unselected

Parameters:

    

  * **mirror_weights** (_boolean_ _,__(__optional_ _)_) – Mirror Weights, Mirror weights

  * **flip_group_names** (_boolean_ _,__(__optional_ _)_) – Flip Group Names, Flip vertex group names

  * **all_groups** (_boolean_ _,__(__optional_ _)_) – All Groups, Mirror all vertex groups weights

  * **use_topology** (_boolean_ _,__(__optional_ _)_) – Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology)

bpy.ops.object.vertex_group_move(_*_ , _direction =UP_)¶

    

Move the active vertex group up/down in the list

Parameters:

    

**direction** (enum in [`UP`, `DOWN`], (optional)) – Direction, Direction to
move the active vertex group towards

bpy.ops.object.vertex_group_normalize()¶

    

Normalize weights of the active vertex group, so that the highest ones are now
1.0

bpy.ops.object.vertex_group_normalize_all(_*_ , _group_select_mode_ ,
_lock_active =True_)¶

    

Normalize all weights of all vertex groups, so that for each vertex, the sum
of all weights is 1.0

Parameters:

    

  * **group_select_mode** (_enum in_ _[__]__,__(__optional_ _)_) – Subset, Define which subset of groups shall be used

  * **lock_active** (_boolean_ _,__(__optional_ _)_) – Lock Active, Keep the values of the active group while normalizing others

bpy.ops.object.vertex_group_quantize(_*_ , _group_select_mode_ , _steps =4_)¶

    

Set weights to a fixed number of steps

Parameters:

    

  * **group_select_mode** (_enum in_ _[__]__,__(__optional_ _)_) – Subset, Define which subset of groups shall be used

  * **steps** (_int in_ _[__1_ _,__1000_ _]__,__(__optional_ _)_) – Steps, Number of steps between 0 and 1

bpy.ops.object.vertex_group_remove(_*_ , _all =False_, _all_unlocked =False_)¶

    

Delete the active or all vertex groups from the active object

Parameters:

    

  * **all** (_boolean_ _,__(__optional_ _)_) – All, Remove all vertex groups

  * **all_unlocked** (_boolean_ _,__(__optional_ _)_) – All Unlocked, Remove all unlocked vertex groups

bpy.ops.object.vertex_group_remove_from(_*_ , _use_all_groups =False_,
_use_all_verts =False_)¶

    

Remove the selected vertices from active or all vertex group(s)

Parameters:

    

  * **use_all_groups** (_boolean_ _,__(__optional_ _)_) – All Groups, Remove from all groups

  * **use_all_verts** (_boolean_ _,__(__optional_ _)_) – All Vertices, Clear the active group

bpy.ops.object.vertex_group_select()¶

    

Select all the vertices assigned to the active vertex group

bpy.ops.object.vertex_group_set_active(_*_ , _group_)¶

    

Set the active vertex group

Parameters:

    

**group** (_enum in_ _[__]__,__(__optional_ _)_) – Group, Vertex group to set
as active

bpy.ops.object.vertex_group_smooth(_*_ , _group_select_mode_ , _factor =0.5_,
_repeat =1_, _expand =0.0_)¶

    

Smooth weights for selected vertices

Parameters:

    

  * **group_select_mode** (_enum in_ _[__]__,__(__optional_ _)_) – Subset, Define which subset of groups shall be used

  * **factor** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Factor

  * **repeat** (_int in_ _[__1_ _,__10000_ _]__,__(__optional_ _)_) – Iterations

  * **expand** (_float in_ _[__-1_ _,__1_ _]__,__(__optional_ _)_) – Expand/Contract, Expand/contract weights

bpy.ops.object.vertex_group_sort(_*_ , _sort_type =NAME_)¶

    

Sort vertex groups

Parameters:

    

**sort_type** (enum in [`NAME`, `BONE_HIERARCHY`], (optional)) – Sort Type,
Sort type

bpy.ops.object.vertex_parent_set()¶

    

Parent selected objects to the selected vertices

bpy.ops.object.vertex_weight_copy()¶

    

Copy weights from active to selected

bpy.ops.object.vertex_weight_delete(_*_ , _weight_group =-1_)¶

    

Delete this weight from the vertex (disabled if vertex group is locked)

Parameters:

    

**weight_group** (_int in_ _[__-1_ _,__inf_ _]__,__(__optional_ _)_) – Weight
Index, Index of source weight in active vertex group

bpy.ops.object.vertex_weight_normalize_active_vertex()¶

    

Normalize active vertex’s weights

bpy.ops.object.vertex_weight_paste(_*_ , _weight_group =-1_)¶

    

Copy this group’s weight to other selected vertices (disabled if vertex group
is locked)

Parameters:

    

**weight_group** (_int in_ _[__-1_ _,__inf_ _]__,__(__optional_ _)_) – Weight
Index, Index of source weight in active vertex group

bpy.ops.object.vertex_weight_set_active(_*_ , _weight_group =-1_)¶

    

Set as active vertex group

Parameters:

    

**weight_group** (_int in_ _[__-1_ _,__inf_ _]__,__(__optional_ _)_) – Weight
Index, Index of source weight in active vertex group

bpy.ops.object.visual_geometry_to_objects()¶

    

Convert geometry and instances into editable objects and collections

bpy.ops.object.visual_transform_apply()¶

    

Apply the object’s visual transformation to its data

bpy.ops.object.volume_add(_*_ , _align =WORLD_, _location =(0.0, 0.0, 0.0)_,
_rotation =(0.0, 0.0, 0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Add a volume object to the scene

Parameters:

    

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.volume_import(_*_ , _filepath =''_, _directory =''_, _files
=None_, _hide_props_region =True_, _check_existing =False_, _filter_blender
=False_, _filter_backup =False_, _filter_image =False_, _filter_movie =False_,
_filter_python =False_, _filter_font =False_, _filter_sound =False_,
_filter_text =False_, _filter_archive =False_, _filter_btx =False_,
_filter_collada =False_, _filter_alembic =False_, _filter_usd =False_,
_filter_obj =False_, _filter_volume =True_, _filter_folder =True_,
_filter_blenlib =False_, _filemode =9_, _relative_path =True_, _display_type
=DEFAULT_, _sort_method_ , _use_sequence_detection =True_, _align =WORLD_,
_location =(0.0, 0.0, 0.0)_, _rotation =(0.0, 0.0, 0.0)_, _scale =(0.0, 0.0,
0.0)_)¶

    

Import OpenVDB volume file

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

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **use_sequence_detection** (_boolean_ _,__(__optional_ _)_) – Detect Sequences, Automatically detect animated sequences in selected volume files (based on file names)

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.voxel_remesh()¶

    

Calculates a new manifold mesh based on the volume of the current mesh. All
data layers will be lost

bpy.ops.object.voxel_size_edit()¶

    

Modify the mesh voxel size interactively used in the voxel remesher

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

