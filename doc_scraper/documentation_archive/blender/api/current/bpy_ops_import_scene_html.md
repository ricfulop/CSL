---
url: https://docs.blender.org/api/current/bpy.ops.import_scene.html
scraped_at: 2025-09-08T14:18:21.513942
title: Import Scene Operators¶
---

# Import Scene Operators¶

bpy.ops.import_scene.fbx(_*_ , _filepath =''_, _directory =''_, _filter_glob
='*.fbx'_, _files =None_, _ui_tab =MAIN_, _use_manual_orientation =False_,
_global_scale =1.0_, _bake_space_transform =False_, _use_custom_normals
=True_, _colors_type =SRGB_, _use_image_search =True_, _use_alpha_decals
=False_, _decal_offset =0.0_, _use_anim =True_, _anim_offset =1.0_,
_use_subsurf =False_, _use_custom_props =True_,
_use_custom_props_enum_as_string =True_, _ignore_leaf_bones =False_,
_force_connect_children =False_, _automatic_bone_orientation =False_,
_primary_bone_axis =Y_, _secondary_bone_axis =X_, _use_prepost_rot =True_,
_axis_forward =-Z_, _axis_up =Y_)¶

    

Load a FBX file

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Filepath used for importing the file

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – directory

  * **filter_glob** (_string_ _,__(__optional_ _,__never None_ _)_) – filter_glob

  * **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – File Path

  * **ui_tab** (enum in [`MAIN`, `ARMATURE`], (optional)) – 

ui_tab, Import options categories

    * `MAIN` Main – Main basic settings.

    * `ARMATURE` Armatures – Armature-related settings.

  * **use_manual_orientation** (_boolean_ _,__(__optional_ _)_) – Manual Orientation, Specify orientation and scale, instead of using embedded data in FBX file

  * **global_scale** (_float in_ _[__0.001_ _,__1000_ _]__,__(__optional_ _)_) – Scale

  * **bake_space_transform** (_boolean_ _,__(__optional_ _)_) – Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender’s space (WARNING! experimental option, use at own risk, known to be broken with armatures/animations)

  * **use_custom_normals** (_boolean_ _,__(__optional_ _)_) – Custom Normals, Import custom normals, if available (otherwise Blender will recompute them)

  * **colors_type** (enum in [`NONE`, `SRGB`, `LINEAR`], (optional)) – 

Vertex Colors, Import vertex color attributes

    * `NONE` None – Do not import color attributes.

    * `SRGB` sRGB – Expect file colors in sRGB color space.

    * `LINEAR` Linear – Expect file colors in linear color space.

  * **use_image_search** (_boolean_ _,__(__optional_ _)_) – Image Search, Search subdirs for any associated images (WARNING: may be slow)

  * **use_alpha_decals** (_boolean_ _,__(__optional_ _)_) – Alpha Decals, Treat materials with alpha as decals (no shadow casting)

  * **decal_offset** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Decal Offset, Displace geometry of alpha meshes

  * **use_anim** (_boolean_ _,__(__optional_ _)_) – Import Animation, Import FBX animation

  * **anim_offset** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Animation Offset, Offset to apply to animation during import, in frames

  * **use_subsurf** (_boolean_ _,__(__optional_ _)_) – Subdivision Data, Import FBX subdivision information as subdivision surface modifiers

  * **use_custom_props** (_boolean_ _,__(__optional_ _)_) – Custom Properties, Import user properties as custom properties

  * **use_custom_props_enum_as_string** (_boolean_ _,__(__optional_ _)_) – Import Enums As Strings, Store enumeration values as strings

  * **ignore_leaf_bones** (_boolean_ _,__(__optional_ _)_) – Ignore Leaf Bones, Ignore the last bone at the end of each chain (used to mark the length of the previous bone)

  * **force_connect_children** (_boolean_ _,__(__optional_ _)_) – Force Connect Children, Force connection of children bones to their parent, even if their computed head/tail positions do not match (can be useful with pure-joints-type armatures)

  * **automatic_bone_orientation** (_boolean_ _,__(__optional_ _)_) – Automatic Bone Orientation, Try to align the major bone axis with the bone children

  * **primary_bone_axis** (enum in [`X`, `Y`, `Z`, `-X`, `-Y`, `-Z`], (optional)) – Primary Bone Axis

  * **secondary_bone_axis** (enum in [`X`, `Y`, `Z`, `-X`, `-Y`, `-Z`], (optional)) – Secondary Bone Axis

  * **use_prepost_rot** (_boolean_ _,__(__optional_ _)_) – Use Pre/Post Rotation, Use pre/post rotation from FBX transform (you may have to disable that in some cases)

  * **axis_forward** (enum in [`X`, `Y`, `Z`, `-X`, `-Y`, `-Z`], (optional)) – Forward

  * **axis_up** (enum in [`X`, `Y`, `Z`, `-X`, `-Y`, `-Z`], (optional)) – Up

File:

    

[addons_core/io_scene_fbx/__init__.py:210](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/io_scene_fbx/__init__.py#L210)

bpy.ops.import_scene.gltf(_*_ , _filepath =''_,
_export_import_convert_lighting_mode =SPEC_, _filter_glob ='*.glb;*.gltf'_,
_directory =''_, _files =None_, _loglevel =0_, _import_pack_images =True_,
_merge_vertices =False_, _import_shading =NORMALS_, _bone_heuristic =BLENDER_,
_disable_bone_shape =False_, _bone_shape_scale_factor =1.0_,
_guess_original_bind_pose =True_, _import_webp_texture =False_,
_import_unused_materials =False_, _import_select_created_objects =True_,
_import_scene_extras =True_, _import_scene_as_collection =True_,
_import_merge_material_slots =True_)¶

    

Load a glTF 2.0 file

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Filepath used for importing the file

  * **export_import_convert_lighting_mode** (enum in [`SPEC`, `COMPAT`, `RAW`], (optional)) – 

Lighting Mode, Optional backwards compatibility for non-standard render
engines. Applies to lights

    * `SPEC` Standard – Physically-based glTF lighting units (cd, lx, nt).

    * `COMPAT` Unitless – Non-physical, unitless lighting. Useful when exposure controls are not available.

    * `RAW` Raw (Deprecated) – Blender lighting strengths with no conversion.

  * **filter_glob** (_string_ _,__(__optional_ _,__never None_ _)_) – filter_glob

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – directory

  * **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – File Path

  * **loglevel** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Log Level, Log Level

  * **import_pack_images** (_boolean_ _,__(__optional_ _)_) – Pack Images, Pack all images into .blend file

  * **merge_vertices** (_boolean_ _,__(__optional_ _)_) – Merge Vertices, The glTF format requires discontinuous normals, UVs, and other vertex attributes to be stored as separate vertices, as required for rendering on typical graphics hardware. This option attempts to combine co-located vertices where possible. Currently cannot combine verts with different normals

  * **import_shading** (enum in [`NORMALS`, `FLAT`, `SMOOTH`], (optional)) – Shading, How normals are computed during import

  * **bone_heuristic** (enum in [`BLENDER`, `TEMPERANCE`, `FORTUNE`], (optional)) – 

Bone Dir, Heuristic for placing bones. Tries to make bones pretty

    * `BLENDER` Blender (best for import/export round trip) – Good for re-importing glTFs exported from Blender, and re-exporting glTFs to glTFs after Blender editing. Bone tips are placed on their local +Y axis (in glTF space).

    * `TEMPERANCE` Temperance (average) – Decent all-around strategy. A bone with one child has its tip placed on the local axis closest to its child.

    * `FORTUNE` Fortune (may look better, less accurate) – Might look better than Temperance, but also might have errors. A bone with one child has its tip placed at its child’s root. Non-uniform scalings may get messed up though, so beware.

  * **disable_bone_shape** (_boolean_ _,__(__optional_ _)_) – Disable Bone Shape, Do not create bone shapes

  * **bone_shape_scale_factor** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Bone Shape Scale, Scale factor for bone shapes

  * **guess_original_bind_pose** (_boolean_ _,__(__optional_ _)_) – Guess Original Bind Pose, Try to guess the original bind pose for skinned meshes from the inverse bind matrices. When off, use default/rest pose as bind pose

  * **import_webp_texture** (_boolean_ _,__(__optional_ _)_) – Import WebP Textures, If a texture exists in WebP format, loads the WebP texture instead of the fallback PNG/JPEG one

  * **import_unused_materials** (_boolean_ _,__(__optional_ _)_) – Import Unused Materials & Images, Import materials & Images not assigned to any mesh

  * **import_select_created_objects** (_boolean_ _,__(__optional_ _)_) – Select Imported Objects, Select created objects at the end of the import

  * **import_scene_extras** (_boolean_ _,__(__optional_ _)_) – Import Scene Extras, Import scene extras as custom properties. Existing custom properties will be overwritten

  * **import_scene_as_collection** (_boolean_ _,__(__optional_ _)_) – Import Scene as Collection, Import the scene as a collection

  * **import_merge_material_slots** (_boolean_ _,__(__optional_ _)_) – Merge Material Slot when possible, Merge material slots when possible

File:

    

[addons_core/io_scene_gltf2/__init__.py:2010](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/io_scene_gltf2/__init__.py#L2010)

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

