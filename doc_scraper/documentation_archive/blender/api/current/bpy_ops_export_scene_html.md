---
url: https://docs.blender.org/api/current/bpy.ops.export_scene.html
scraped_at: 2025-09-08T14:18:08.494046
title: Export Scene Operators¶
---

# Export Scene Operators¶

bpy.ops.export_scene.fbx(_*_ , _filepath =''_, _check_existing =True_,
_filter_glob ='*.fbx'_, _use_selection =False_, _use_visible =False_,
_use_active_collection =False_, _collection =''_, _global_scale =1.0_,
_apply_unit_scale =True_, _apply_scale_options =FBX_SCALE_NONE_,
_use_space_transform =True_, _bake_space_transform =False_, _object_types
={'ARMATURE', 'CAMERA', 'EMPTY', 'LIGHT', 'MESH', 'OTHER'}_,
_use_mesh_modifiers =True_, _use_mesh_modifiers_render =True_,
_mesh_smooth_type =OFF_, _colors_type =SRGB_, _prioritize_active_color
=False_, _use_subsurf =False_, _use_mesh_edges =False_, _use_tspace =False_,
_use_triangles =False_, _use_custom_props =False_, _add_leaf_bones =True_,
_primary_bone_axis =Y_, _secondary_bone_axis =X_, _use_armature_deform_only
=False_, _armature_nodetype =NULL_, _bake_anim =True_,
_bake_anim_use_all_bones =True_, _bake_anim_use_nla_strips =True_,
_bake_anim_use_all_actions =True_, _bake_anim_force_startend_keying =True_,
_bake_anim_step =1.0_, _bake_anim_simplify_factor =1.0_, _path_mode =AUTO_,
_embed_textures =False_, _batch_mode =OFF_, _use_batch_own_dir =True_,
_use_metadata =True_, _axis_forward =-Z_, _axis_up =Y_)¶

    

Write a FBX file

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Filepath used for exporting the file

  * **check_existing** (_boolean_ _,__(__optional_ _)_) – Check Existing, Check and warn on overwriting existing files

  * **filter_glob** (_string_ _,__(__optional_ _,__never None_ _)_) – filter_glob

  * **use_selection** (_boolean_ _,__(__optional_ _)_) – Selected Objects, Export selected and visible objects only

  * **use_visible** (_boolean_ _,__(__optional_ _)_) – Visible Objects, Export visible objects only

  * **use_active_collection** (_boolean_ _,__(__optional_ _)_) – Active Collection, Export only objects from the active collection (and its children)

  * **collection** (_string_ _,__(__optional_ _,__never None_ _)_) – Source Collection, Export only objects from this collection (and its children)

  * **global_scale** (_float in_ _[__0.001_ _,__1000_ _]__,__(__optional_ _)_) – Scale, Scale all data (Some importers do not support scaled armatures!)

  * **apply_unit_scale** (_boolean_ _,__(__optional_ _)_) – Apply Unit, Take into account current Blender units settings (if unset, raw Blender Units values are used as-is)

  * **apply_scale_options** (enum in [`FBX_SCALE_NONE`, `FBX_SCALE_UNITS`, `FBX_SCALE_CUSTOM`, `FBX_SCALE_ALL`], (optional)) – 

Apply Scalings, How to apply custom and units scalings in generated FBX file
(Blender uses FBX scale to detect units on import, but many other applications
do not handle the same way)

    * `FBX_SCALE_NONE` All Local – Apply custom scaling and units scaling to each object transformation, FBX scale remains at 1.0.

    * `FBX_SCALE_UNITS` FBX Units Scale – Apply custom scaling to each object transformation, and units scaling to FBX scale.

    * `FBX_SCALE_CUSTOM` FBX Custom Scale – Apply custom scaling to FBX scale, and units scaling to each object transformation.

    * `FBX_SCALE_ALL` FBX All – Apply custom scaling and units scaling to FBX scale.

  * **use_space_transform** (_boolean_ _,__(__optional_ _)_) – Use Space Transform, Apply global space transform to the object rotations. When disabled only the axis space is written to the file and all object transforms are left as-is

  * **bake_space_transform** (_boolean_ _,__(__optional_ _)_) – Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender’s space (WARNING! experimental option, use at own risk, known to be broken with armatures/animations)

  * **object_types** (enum set in {`EMPTY`, `CAMERA`, `LIGHT`, `ARMATURE`, `MESH`, `OTHER`}, (optional)) – 

Object Types, Which kind of object to export

    * `EMPTY` Empty.

    * `CAMERA` Camera.

    * `LIGHT` Lamp.

    * `ARMATURE` Armature – WARNING: not supported in dupli/group instances.

    * `MESH` Mesh.

    * `OTHER` Other – Other geometry types, like curve, metaball, etc. (converted to meshes).

  * **use_mesh_modifiers** (_boolean_ _,__(__optional_ _)_) – Apply Modifiers, Apply modifiers to mesh objects (except Armature ones) - WARNING: prevents exporting shape keys

  * **use_mesh_modifiers_render** (_boolean_ _,__(__optional_ _)_) – Use Modifiers Render Setting, Use render settings when applying modifiers to mesh objects (DISABLED in Blender 2.8)

  * **mesh_smooth_type** (enum in [`OFF`, `FACE`, `EDGE`, `SMOOTH_GROUP`], (optional)) – 

Smoothing, Export smoothing information (prefer ‘Normals Only’ option if your
target importer understand split normals)

    * `OFF` Normals Only – Export only normals instead of writing edge or face smoothing data.

    * `FACE` Face – Write face smoothing.

    * `EDGE` Edge – Write edge smoothing.

    * `SMOOTH_GROUP` Smoothing Groups – Write face smoothing groups.

  * **colors_type** (enum in [`NONE`, `SRGB`, `LINEAR`], (optional)) – 

Vertex Colors, Export vertex color attributes

    * `NONE` None – Do not export color attributes.

    * `SRGB` sRGB – Export colors in sRGB color space.

    * `LINEAR` Linear – Export colors in linear color space.

  * **prioritize_active_color** (_boolean_ _,__(__optional_ _)_) – Prioritize Active Color, Make sure active color will be exported first. Could be important since some other software can discard other color attributes besides the first one

  * **use_subsurf** (_boolean_ _,__(__optional_ _)_) – Export Subdivision Surface, Export the last Catmull-Rom subdivision modifier as FBX subdivision (does not apply the modifier even if ‘Apply Modifiers’ is enabled)

  * **use_mesh_edges** (_boolean_ _,__(__optional_ _)_) – Loose Edges, Export loose edges (as two-vertices polygons)

  * **use_tspace** (_boolean_ _,__(__optional_ _)_) – Tangent Space, Add binormal and tangent vectors, together with normal they form the tangent space (will only work correctly with tris/quads only meshes!)

  * **use_triangles** (_boolean_ _,__(__optional_ _)_) – Triangulate Faces, Convert all faces to triangles

  * **use_custom_props** (_boolean_ _,__(__optional_ _)_) – Custom Properties, Export custom properties

  * **add_leaf_bones** (_boolean_ _,__(__optional_ _)_) – Add Leaf Bones, Append a final bone to the end of each chain to specify last bone length (use this when you intend to edit the armature from exported data)

  * **primary_bone_axis** (enum in [`X`, `Y`, `Z`, `-X`, `-Y`, `-Z`], (optional)) – Primary Bone Axis

  * **secondary_bone_axis** (enum in [`X`, `Y`, `Z`, `-X`, `-Y`, `-Z`], (optional)) – Secondary Bone Axis

  * **use_armature_deform_only** (_boolean_ _,__(__optional_ _)_) – Only Deform Bones, Only write deforming bones (and non-deforming ones when they have deforming children)

  * **armature_nodetype** (enum in [`NULL`, `ROOT`, `LIMBNODE`], (optional)) – 

Armature FBXNode Type, FBX type of node (object) used to represent Blender’s
armatures (use the Null type unless you experience issues with the other app,
as other choices may not import back perfectly into Blender…)

    * `NULL` Null – ‘Null’ FBX node, similar to Blender’s Empty (default).

    * `ROOT` Root – ‘Root’ FBX node, supposed to be the root of chains of bones….

    * `LIMBNODE` LimbNode – ‘LimbNode’ FBX node, a regular joint between two bones….

  * **bake_anim** (_boolean_ _,__(__optional_ _)_) – Baked Animation, Export baked keyframe animation

  * **bake_anim_use_all_bones** (_boolean_ _,__(__optional_ _)_) – Key All Bones, Force exporting at least one key of animation for all bones (needed with some target applications, like UE4)

  * **bake_anim_use_nla_strips** (_boolean_ _,__(__optional_ _)_) – NLA Strips, Export each non-muted NLA strip as a separated FBX’s AnimStack, if any, instead of global scene animation

  * **bake_anim_use_all_actions** (_boolean_ _,__(__optional_ _)_) – All Actions, Export each action as a separated FBX’s AnimStack, instead of global scene animation (note that animated objects will get all actions compatible with them, others will get no animation at all)

  * **bake_anim_force_startend_keying** (_boolean_ _,__(__optional_ _)_) – Force Start/End Keying, Always add a keyframe at start and end of actions for animated channels

  * **bake_anim_step** (_float in_ _[__0.01_ _,__100_ _]__,__(__optional_ _)_) – Sampling Rate, How often to evaluate animated values (in frames)

  * **bake_anim_simplify_factor** (_float in_ _[__0_ _,__100_ _]__,__(__optional_ _)_) – Simplify, How much to simplify baked values (0.0 to disable, the higher the more simplified)

  * **path_mode** (enum in [`AUTO`, `ABSOLUTE`, `RELATIVE`, `MATCH`, `STRIP`, `COPY`], (optional)) – 

Path Mode, Method used to reference paths

    * `AUTO` Auto – Use relative paths with subdirectories only.

    * `ABSOLUTE` Absolute – Always write absolute paths.

    * `RELATIVE` Relative – Write relative paths where possible.

    * `MATCH` Match – Match absolute/relative setting with input path.

    * `STRIP` Strip – Filename only.

    * `COPY` Copy – Copy the file to the destination path (or subdirectory).

  * **embed_textures** (_boolean_ _,__(__optional_ _)_) – Embed Textures, Embed textures in FBX binary file (only for “Copy” path mode!)

  * **batch_mode** (enum in [`OFF`, `SCENE`, `COLLECTION`, `SCENE_COLLECTION`, `ACTIVE_SCENE_COLLECTION`], (optional)) – 

Batch Mode

    * `OFF` Off – Active scene to file.

    * `SCENE` Scene – Each scene as a file.

    * `COLLECTION` Collection – Each collection (data-block ones) as a file, does not include content of children collections.

    * `SCENE_COLLECTION` Scene Collections – Each collection (including master, non-data-block ones) of each scene as a file, including content from children collections.

    * `ACTIVE_SCENE_COLLECTION` Active Scene Collections – Each collection (including master, non-data-block one) of the active scene as a file, including content from children collections.

  * **use_batch_own_dir** (_boolean_ _,__(__optional_ _)_) – Batch Own Dir, Create a dir for each exported file

  * **use_metadata** (_boolean_ _,__(__optional_ _)_) – Use Metadata

  * **axis_forward** (enum in [`X`, `Y`, `Z`, `-X`, `-Y`, `-Z`], (optional)) – Forward

  * **axis_up** (enum in [`X`, `Y`, `Z`, `-X`, `-Y`, `-Z`], (optional)) – Up

File:

    

[addons_core/io_scene_fbx/__init__.py:582](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/io_scene_fbx/__init__.py#L582)

bpy.ops.export_scene.gltf(_*_ , _filepath =''_, _check_existing =True_,
_export_import_convert_lighting_mode =SPEC_, _gltf_export_id =''_,
_export_use_gltfpack =False_, _export_gltfpack_tc =True_, _export_gltfpack_tq
=8_, _export_gltfpack_si =1.0_, _export_gltfpack_sa =False_,
_export_gltfpack_slb =False_, _export_gltfpack_vp =14_, _export_gltfpack_vt
=12_, _export_gltfpack_vn =8_, _export_gltfpack_vc =8_, _export_gltfpack_vpi
=Integer_, _export_gltfpack_noq =True_, _export_gltfpack_kn =False_,
_export_format_ , _ui_tab =GENERAL_, _export_copyright =''_,
_export_image_format =AUTO_, _export_image_add_webp =False_,
_export_image_webp_fallback =False_, _export_texture_dir =''_,
_export_jpeg_quality =75_, _export_image_quality =75_, _export_keep_originals
=False_, _export_texcoords =True_, _export_normals =True_, _export_gn_mesh
=False_, _export_draco_mesh_compression_enable =False_,
_export_draco_mesh_compression_level =6_, _export_draco_position_quantization
=14_, _export_draco_normal_quantization =10_,
_export_draco_texcoord_quantization =12_, _export_draco_color_quantization
=10_, _export_draco_generic_quantization =12_, _export_tangents =False_,
_export_materials =EXPORT_, _export_unused_images =False_,
_export_unused_textures =False_, _export_vertex_color =MATERIAL_,
_export_vertex_color_name ='Color'_, _export_all_vertex_colors =True_,
_export_active_vertex_color_when_no_material =True_, _export_attributes
=False_, _use_mesh_edges =False_, _use_mesh_vertices =False_, _export_cameras
=False_, _use_selection =False_, _use_visible =False_, _use_renderable
=False_, _use_active_collection_with_nested =True_, _use_active_collection
=False_, _use_active_scene =False_, _collection =''_, _at_collection_center
=False_, _export_extras =False_, _export_yup =True_, _export_apply =False_,
_export_shared_accessors =False_, _export_animations =True_,
_export_frame_range =False_, _export_frame_step =1_, _export_force_sampling
=True_, _export_sampling_interpolation_fallback =LINEAR_,
_export_pointer_animation =False_, _export_animation_mode =ACTIONS_,
_export_nla_strips_merged_animation_name ='Animation'_, _export_def_bones
=False_, _export_hierarchy_flatten_bones =False_,
_export_hierarchy_flatten_objs =False_, _export_armature_object_remove
=False_, _export_leaf_bone =False_, _export_optimize_animation_size =True_,
_export_optimize_animation_keep_anim_armature =True_,
_export_optimize_animation_keep_anim_object =False_,
_export_optimize_disable_viewport =False_, _export_negative_frame =SLIDE_,
_export_anim_slide_to_zero =False_, _export_bake_animation =False_,
_export_merge_animation =ACTION_, _export_anim_single_armature =True_,
_export_reset_pose_bones =True_, _export_current_frame =False_,
_export_rest_position_armature =True_, _export_anim_scene_split_object =True_,
_export_skins =True_, _export_influence_nb =4_, _export_all_influences
=False_, _export_morph =True_, _export_morph_normal =True_,
_export_morph_tangent =False_, _export_morph_animation =True_,
_export_morph_reset_sk_data =True_, _export_lights =False_,
_export_try_sparse_sk =True_, _export_try_omit_sparse_sk =False_,
_export_gpu_instances =False_, _export_action_filter =False_,
_export_convert_animation_pointer =False_, _export_nla_strips =True_,
_export_original_specular =False_, _will_save_settings =False_,
_export_hierarchy_full_collections =False_, _export_extra_animations =False_,
_export_loglevel =-1_, _filter_glob ='*.glb'_)¶

    

Export scene as glTF 2.0 file

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Filepath used for exporting the file

  * **check_existing** (_boolean_ _,__(__optional_ _)_) – Check Existing, Check and warn on overwriting existing files

  * **export_import_convert_lighting_mode** (enum in [`SPEC`, `COMPAT`, `RAW`], (optional)) – 

Lighting Mode, Optional backwards compatibility for non-standard render
engines. Applies to lights

    * `SPEC` Standard – Physically-based glTF lighting units (cd, lx, nt).

    * `COMPAT` Unitless – Non-physical, unitless lighting. Useful when exposure controls are not available.

    * `RAW` Raw (Deprecated) – Blender lighting strengths with no conversion.

  * **gltf_export_id** (_string_ _,__(__optional_ _,__never None_ _)_) – Identifier, Identifier of caller (in case of add-on calling this exporter). Can be useful in case of Extension added by other add-ons

  * **export_use_gltfpack** (_boolean_ _,__(__optional_ _)_) – Use Gltfpack, Use gltfpack to simplify the mesh and/or compress its textures

  * **export_gltfpack_tc** (_boolean_ _,__(__optional_ _)_) – KTX2 Compression, Convert all textures to KTX2 with BasisU supercompression

  * **export_gltfpack_tq** (_int in_ _[__1_ _,__10_ _]__,__(__optional_ _)_) – Texture Encoding Quality, Texture encoding quality

  * **export_gltfpack_si** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Mesh Simplification Ratio, Simplify meshes targeting triangle count ratio

  * **export_gltfpack_sa** (_boolean_ _,__(__optional_ _)_) – Aggressive Mesh Simplification, Aggressively simplify to the target ratio disregarding quality

  * **export_gltfpack_slb** (_boolean_ _,__(__optional_ _)_) – Lock Mesh Border Vertices, Lock border vertices during simplification to avoid gaps on connected meshes

  * **export_gltfpack_vp** (_int in_ _[__1_ _,__16_ _]__,__(__optional_ _)_) – Position Quantization, Use N-bit quantization for positions

  * **export_gltfpack_vt** (_int in_ _[__1_ _,__16_ _]__,__(__optional_ _)_) – Texture Coordinate Quantization, Use N-bit quantization for texture coordinates

  * **export_gltfpack_vn** (_int in_ _[__1_ _,__16_ _]__,__(__optional_ _)_) – Normal/Tangent Quantization, Use N-bit quantization for normals and tangents

  * **export_gltfpack_vc** (_int in_ _[__1_ _,__16_ _]__,__(__optional_ _)_) – Vertex Color Quantization, Use N-bit quantization for colors

  * **export_gltfpack_vpi** (enum in [`Integer`, `Normalized`, `Floating-point`], (optional)) – 

Vertex Position Attributes, Type to use for vertex position attributes

    * `Integer` Integer – Use integer attributes for positions.

    * `Normalized` Normalized – Use normalized attributes for positions.

    * `Floating-point` Floating-point – Use floating-point attributes for positions.

  * **export_gltfpack_noq** (_boolean_ _,__(__optional_ _)_) – Disable Quantization, Disable quantization; produces much larger glTF files with no extensions

  * **export_gltfpack_kn** (_boolean_ _,__(__optional_ _)_) – Keep Named Nodes, Restrict some optimization to keep named nodes and meshes attached to named nodes so that named nodes can be transformed externally

  * **export_format** (_enum in_ _[__]__,__(__optional_ _)_) – Format, Output format. Binary is most efficient, but JSON may be easier to edit later

  * **ui_tab** (enum in [`GENERAL`, `MESHES`, `OBJECTS`, `ANIMATION`], (optional)) – 

ui_tab, Export setting categories

    * `GENERAL` General – General settings.

    * `MESHES` Meshes – Mesh settings.

    * `OBJECTS` Objects – Object settings.

    * `ANIMATION` Animation – Animation settings.

  * **export_copyright** (_string_ _,__(__optional_ _,__never None_ _)_) – Copyright, Legal rights and conditions for the model

  * **export_image_format** (enum in [`AUTO`, `JPEG`, `WEBP`, `NONE`], (optional)) – 

Images, Output format for images. PNG is lossless and generally preferred, but
JPEG might be preferable for web applications due to the smaller file size.
Alternatively they can be omitted if they are not needed

    * `AUTO` Automatic – Save PNGs as PNGs, JPEGs as JPEGs, WebPs as WebPs. For other formats, use PNG.

    * `JPEG` JPEG Format (.jpg) – Save images as JPEGs. (Images that need alpha are saved as PNGs though.) Be aware of a possible loss in quality.

    * `WEBP` WebP Format – Save images as WebPs as main image (no fallback).

    * `NONE` None – Don’t export images.

  * **export_image_add_webp** (_boolean_ _,__(__optional_ _)_) – Create WebP, Creates WebP textures for every texture. For already WebP textures, nothing happens

  * **export_image_webp_fallback** (_boolean_ _,__(__optional_ _)_) – WebP Fallback, For all WebP textures, create a PNG fallback texture

  * **export_texture_dir** (_string_ _,__(__optional_ _,__never None_ _)_) – Textures, Folder to place texture files in. Relative to the .gltf file

  * **export_jpeg_quality** (_int in_ _[__0_ _,__100_ _]__,__(__optional_ _)_) – JPEG Quality, Quality of JPEG export

  * **export_image_quality** (_int in_ _[__0_ _,__100_ _]__,__(__optional_ _)_) – Image Quality, Quality of image export

  * **export_keep_originals** (_boolean_ _,__(__optional_ _)_) – Keep Original, Keep original textures files if possible. WARNING: if you use more than one texture, where pbr standard requires only one, only one texture will be used. This can lead to unexpected results

  * **export_texcoords** (_boolean_ _,__(__optional_ _)_) – UVs, Export UVs (texture coordinates) with meshes

  * **export_normals** (_boolean_ _,__(__optional_ _)_) – Normals, Export vertex normals with meshes

  * **export_gn_mesh** (_boolean_ _,__(__optional_ _)_) – Geometry Nodes Instances (Experimental), Export Geometry nodes instance meshes

  * **export_draco_mesh_compression_enable** (_boolean_ _,__(__optional_ _)_) – Draco Mesh Compression, Compress mesh using Draco

  * **export_draco_mesh_compression_level** (_int in_ _[__0_ _,__10_ _]__,__(__optional_ _)_) – Compression Level, Compression level (0 = most speed, 6 = most compression, higher values currently not supported)

  * **export_draco_position_quantization** (_int in_ _[__0_ _,__30_ _]__,__(__optional_ _)_) – Position Quantization Bits, Quantization bits for position values (0 = no quantization)

  * **export_draco_normal_quantization** (_int in_ _[__0_ _,__30_ _]__,__(__optional_ _)_) – Normal Quantization Bits, Quantization bits for normal values (0 = no quantization)

  * **export_draco_texcoord_quantization** (_int in_ _[__0_ _,__30_ _]__,__(__optional_ _)_) – Texcoord Quantization Bits, Quantization bits for texture coordinate values (0 = no quantization)

  * **export_draco_color_quantization** (_int in_ _[__0_ _,__30_ _]__,__(__optional_ _)_) – Color Quantization Bits, Quantization bits for color values (0 = no quantization)

  * **export_draco_generic_quantization** (_int in_ _[__0_ _,__30_ _]__,__(__optional_ _)_) – Generic Quantization Bits, Quantization bits for generic values like weights or joints (0 = no quantization)

  * **export_tangents** (_boolean_ _,__(__optional_ _)_) – Tangents, Export vertex tangents with meshes

  * **export_materials** (enum in [`EXPORT`, `PLACEHOLDER`, `VIEWPORT`, `NONE`], (optional)) – 

Materials, Export materials

    * `EXPORT` Export – Export all materials used by included objects.

    * `PLACEHOLDER` Placeholder – Do not export materials, but write multiple primitive groups per mesh, keeping material slot information.

    * `VIEWPORT` Viewport – Export minimal materials as defined in Viewport display properties.

    * `NONE` No export – Do not export materials, and combine mesh primitive groups, losing material slot information.

  * **export_unused_images** (_boolean_ _,__(__optional_ _)_) – Unused Images, Export images not assigned to any material

  * **export_unused_textures** (_boolean_ _,__(__optional_ _)_) – Prepare Unused Textures, Export image texture nodes not assigned to any material. This feature is not standard and needs an external extension to be included in the glTF file

  * **export_vertex_color** (enum in [`MATERIAL`, `ACTIVE`, `NAME`, `NONE`], (optional)) – 

Use Vertex Color, How to export vertex color

    * `MATERIAL` Material – Export vertex color when used by material.

    * `ACTIVE` Active – Export active vertex color.

    * `NAME` Name – Export vertex color with this name.

    * `NONE` None – Do not export vertex color.

  * **export_vertex_color_name** (_string_ _,__(__optional_ _,__never None_ _)_) – Vertex Color Name, Name of vertex color to export

  * **export_all_vertex_colors** (_boolean_ _,__(__optional_ _)_) – Export All Vertex Colors, Export all vertex colors, even if not used by any material. If no Vertex Color is used in the mesh materials, a fake COLOR_0 will be created, in order to keep material unchanged

  * **export_active_vertex_color_when_no_material** (_boolean_ _,__(__optional_ _)_) – Export Active Vertex Color When No Material, When there is no material on object, export active vertex color

  * **export_attributes** (_boolean_ _,__(__optional_ _)_) – Attributes, Export Attributes (when starting with underscore)

  * **use_mesh_edges** (_boolean_ _,__(__optional_ _)_) – Loose Edges, Export loose edges as lines, using the material from the first material slot

  * **use_mesh_vertices** (_boolean_ _,__(__optional_ _)_) – Loose Points, Export loose points as glTF points, using the material from the first material slot

  * **export_cameras** (_boolean_ _,__(__optional_ _)_) – Cameras, Export cameras

  * **use_selection** (_boolean_ _,__(__optional_ _)_) – Selected Objects, Export selected objects only

  * **use_visible** (_boolean_ _,__(__optional_ _)_) – Visible Objects, Export visible objects only

  * **use_renderable** (_boolean_ _,__(__optional_ _)_) – Renderable Objects, Export renderable objects only

  * **use_active_collection_with_nested** (_boolean_ _,__(__optional_ _)_) – Include Nested Collections, Include active collection and nested collections

  * **use_active_collection** (_boolean_ _,__(__optional_ _)_) – Active Collection, Export objects in the active collection only

  * **use_active_scene** (_boolean_ _,__(__optional_ _)_) – Active Scene, Export active scene only

  * **collection** (_string_ _,__(__optional_ _,__never None_ _)_) – Source Collection, Export only objects from this collection (and its children)

  * **at_collection_center** (_boolean_ _,__(__optional_ _)_) – Export at Collection Center, Export at Collection center of mass of root objects of the collection

  * **export_extras** (_boolean_ _,__(__optional_ _)_) – Custom Properties, Export custom properties as glTF extras

  * **export_yup** (_boolean_ _,__(__optional_ _)_) – +Y Up, Export using glTF convention, +Y up

  * **export_apply** (_boolean_ _,__(__optional_ _)_) – Apply Modifiers, Apply modifiers (excluding Armatures) to mesh objects -WARNING: prevents exporting shape keys

  * **export_shared_accessors** (_boolean_ _,__(__optional_ _)_) – Shared Accessors, Export Primitives using shared accessors for attributes

  * **export_animations** (_boolean_ _,__(__optional_ _)_) – Animations, Exports active actions and NLA tracks as glTF animations

  * **export_frame_range** (_boolean_ _,__(__optional_ _)_) – Limit to Playback Range, Clips animations to selected playback range

  * **export_frame_step** (_int in_ _[__1_ _,__120_ _]__,__(__optional_ _)_) – Sampling Rate, How often to evaluate animated values (in frames)

  * **export_force_sampling** (_boolean_ _,__(__optional_ _)_) – Always Sample Animations, Apply sampling to all animations

  * **export_sampling_interpolation_fallback** (enum in [`LINEAR`, `STEP`], (optional)) – 

Sampling Interpolation Fallback, Interpolation fallback for sampled
animations, when the property is not keyed

    * `LINEAR` Linear – Linear interpolation between keyframes.

    * `STEP` Step – No interpolation between keyframes.

  * **export_pointer_animation** (_boolean_ _,__(__optional_ _)_) – Export Animation Pointer (Experimental), Export material, Light & Camera animation as Animation Pointer. Available only for baked animation mode ‘NLA Tracks’ and ‘Scene’

  * **export_animation_mode** (enum in [`ACTIONS`, `ACTIVE_ACTIONS`, `BROADCAST`, `NLA_TRACKS`, `SCENE`], (optional)) – 

Animation Mode, Export Animation mode

    * `ACTIONS` Actions – Export actions (actives and on NLA tracks) as separate animations.

    * `ACTIVE_ACTIONS` Active actions merged – All the currently assigned actions become one glTF animation.

    * `BROADCAST` Broadcast actions – Broadcast all compatible actions to all objects. Animated objects will get all actions compatible with them, others will get no animation at all.

    * `NLA_TRACKS` NLA Tracks – Export individual NLA Tracks as separate animation.

    * `SCENE` Scene – Export baked scene as a single animation.

  * **export_nla_strips_merged_animation_name** (_string_ _,__(__optional_ _,__never None_ _)_) – Merged Animation Name, Name of single glTF animation to be exported

  * **export_def_bones** (_boolean_ _,__(__optional_ _)_) – Export Deformation Bones Only, Export Deformation bones only

  * **export_hierarchy_flatten_bones** (_boolean_ _,__(__optional_ _)_) – Flatten Bone Hierarchy, Flatten Bone Hierarchy. Useful in case of non decomposable transformation matrix

  * **export_hierarchy_flatten_objs** (_boolean_ _,__(__optional_ _)_) – Flatten Object Hierarchy, Flatten Object Hierarchy. Useful in case of non decomposable transformation matrix

  * **export_armature_object_remove** (_boolean_ _,__(__optional_ _)_) – Remove Armature Object, Remove Armature object if possible. If Armature has multiple root bones, object will not be removed

  * **export_leaf_bone** (_boolean_ _,__(__optional_ _)_) – Add Leaf Bones, Append a final bone to the end of each chain to specify last bone length (use this when you intend to edit the armature from exported data)

  * **export_optimize_animation_size** (_boolean_ _,__(__optional_ _)_) – Optimize Animation Size, Reduce exported file size by removing duplicate keyframes

  * **export_optimize_animation_keep_anim_armature** (_boolean_ _,__(__optional_ _)_) – Force Keeping Channels for Bones, If all keyframes are identical in a rig, force keeping the minimal animation. When off, all possible channels for the bones will be exported, even if empty (minimal animation, 2 keyframes)

  * **export_optimize_animation_keep_anim_object** (_boolean_ _,__(__optional_ _)_) – Force Keeping Channel for Objects, If all keyframes are identical for object transformations, force keeping the minimal animation

  * **export_optimize_disable_viewport** (_boolean_ _,__(__optional_ _)_) – Disable Viewport for Other Objects, When exporting animations, disable viewport for other objects, for performance

  * **export_negative_frame** (enum in [`SLIDE`, `CROP`], (optional)) – 

Negative Frames, Negative Frames are slid or cropped

    * `SLIDE` Slide – Slide animation to start at frame 0.

    * `CROP` Crop – Keep only frames above frame 0.

  * **export_anim_slide_to_zero** (_boolean_ _,__(__optional_ _)_) – Set All glTF Animation Starting at 0, Set all glTF animation starting at 0.0s. Can be useful for looping animations

  * **export_bake_animation** (_boolean_ _,__(__optional_ _)_) – Bake All Objects Animations, Force exporting animation on every object. Can be useful when using constraints or driver. Also useful when exporting only selection

  * **export_merge_animation** (enum in [`NLA_TRACK`, `ACTION`, `NONE`], (optional)) – 

Merge Animation, Merge Animations

    * `NLA_TRACK` NLA Track Names – Merge by NLA Track Names.

    * `ACTION` Actions – Merge by Actions.

    * `NONE` No Merge – Do Not Merge Animations.

  * **export_anim_single_armature** (_boolean_ _,__(__optional_ _)_) – Export all Armature Actions, Export all actions, bound to a single armature. WARNING: Option does not support exports including multiple armatures

  * **export_reset_pose_bones** (_boolean_ _,__(__optional_ _)_) – Reset Pose Bones Between Actions, Reset pose bones between each action exported. This is needed when some bones are not keyed on some animations

  * **export_current_frame** (_boolean_ _,__(__optional_ _)_) – Use Current Frame as Object Rest Transformations, Export the scene in the current animation frame. When off, frame 0 is used as rest transformations for objects

  * **export_rest_position_armature** (_boolean_ _,__(__optional_ _)_) – Use Rest Position Armature, Export armatures using rest position as joints’ rest pose. When off, current frame pose is used as rest pose

  * **export_anim_scene_split_object** (_boolean_ _,__(__optional_ _)_) – Split Animation by Object, Export Scene as seen in Viewport, But split animation by Object

  * **export_skins** (_boolean_ _,__(__optional_ _)_) – Skinning, Export skinning (armature) data

  * **export_influence_nb** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Bone Influences, Choose how many Bone influences to export

  * **export_all_influences** (_boolean_ _,__(__optional_ _)_) – Include All Bone Influences, Allow export of all joint vertex influences. Models may appear incorrectly in many viewers

  * **export_morph** (_boolean_ _,__(__optional_ _)_) – Shape Keys, Export shape keys (morph targets)

  * **export_morph_normal** (_boolean_ _,__(__optional_ _)_) – Shape Key Normals, Export vertex normals with shape keys (morph targets)

  * **export_morph_tangent** (_boolean_ _,__(__optional_ _)_) – Shape Key Tangents, Export vertex tangents with shape keys (morph targets)

  * **export_morph_animation** (_boolean_ _,__(__optional_ _)_) – Shape Key Animations, Export shape keys animations (morph targets)

  * **export_morph_reset_sk_data** (_boolean_ _,__(__optional_ _)_) – Reset Shape Keys Between Actions, Reset shape keys between each action exported. This is needed when some SK channels are not keyed on some animations

  * **export_lights** (_boolean_ _,__(__optional_ _)_) – Punctual Lights, Export directional, point, and spot lights. Uses “KHR_lights_punctual” glTF extension

  * **export_try_sparse_sk** (_boolean_ _,__(__optional_ _)_) – Use Sparse Accessor if Better, Try using Sparse Accessor if it saves space

  * **export_try_omit_sparse_sk** (_boolean_ _,__(__optional_ _)_) – Omitting Sparse Accessor if Data is Empty, Omitting Sparse Accessor if data is empty

  * **export_gpu_instances** (_boolean_ _,__(__optional_ _)_) – GPU Instances, Export using EXT_mesh_gpu_instancing. Limited to children of a given Empty. Multiple materials might be omitted

  * **export_action_filter** (_boolean_ _,__(__optional_ _)_) – Filter Actions, Filter Actions to be exported

  * **export_convert_animation_pointer** (_boolean_ _,__(__optional_ _)_) – Convert TRS/Weights to Animation Pointer, Export TRS and weights as Animation Pointer. Using KHR_animation_pointer extension

  * **export_nla_strips** (_boolean_ _,__(__optional_ _)_) – Group by NLA Track, When on, multiple actions become part of the same glTF animation if they’re pushed onto NLA tracks with the same name. When off, all the currently assigned actions become one glTF animation

  * **export_original_specular** (_boolean_ _,__(__optional_ _)_) – Export Original PBR Specular, Export original glTF PBR Specular, instead of Blender Principled Shader Specular

  * **will_save_settings** (_boolean_ _,__(__optional_ _)_) – Remember Export Settings, Store glTF export settings in the Blender project

  * **export_hierarchy_full_collections** (_boolean_ _,__(__optional_ _)_) – Full Collection Hierarchy, Export full hierarchy, including intermediate collections

  * **export_extra_animations** (_boolean_ _,__(__optional_ _)_) – Prepare Extra Animations, Export additional animations.This feature is not standard and needs an external extension to be included in the glTF file

  * **export_loglevel** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Log Level, Log Level

  * **filter_glob** (_string_ _,__(__optional_ _,__never None_ _)_) – filter_glob

File:

    

[addons_core/io_scene_gltf2/__init__.py:1082](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/io_scene_gltf2/__init__.py#L1082)

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

