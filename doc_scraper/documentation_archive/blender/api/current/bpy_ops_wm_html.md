---
url: https://docs.blender.org/api/current/bpy.ops.wm.html
scraped_at: 2025-09-08T14:19:03.230635
title: Wm Operators¶
---

# Wm Operators¶

bpy.ops.wm.alembic_export(_*_ , _filepath =''_, _check_existing =True_,
_filter_blender =False_, _filter_backup =False_, _filter_image =False_,
_filter_movie =False_, _filter_python =False_, _filter_font =False_,
_filter_sound =False_, _filter_text =False_, _filter_archive =False_,
_filter_btx =False_, _filter_collada =False_, _filter_alembic =True_,
_filter_usd =False_, _filter_obj =False_, _filter_volume =False_,
_filter_folder =True_, _filter_blenlib =False_, _filemode =8_, _display_type
=DEFAULT_, _sort_method_ , _filter_glob ='*.abc'_, _start =-2147483648_, _end
=-2147483648_, _xsamples =1_, _gsamples =1_, _sh_open =0.0_, _sh_close =1.0_,
_selected =False_, _visible_objects_only =False_, _flatten =False_,
_collection =''_, _uvs =True_, _packuv =True_, _normals =True_, _vcolors
=False_, _orcos =True_, _face_sets =False_, _subdiv_schema =False_,
_apply_subdiv =False_, _curves_as_mesh =False_, _use_instancing =True_,
_global_scale =1.0_, _triangulate =False_, _quad_method =SHORTEST_DIAGONAL_,
_ngon_method =BEAUTY_, _export_hair =True_, _export_particles =True_,
_export_custom_properties =True_, _as_background_job =False_, _evaluation_mode
=RENDER_, _init_scene_frame_range =True_)¶

    

Export current scene in an Alembic archive

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

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

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **start** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Start Frame, Start frame of the export, use the default value to take the start frame of the current scene

  * **end** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – End Frame, End frame of the export, use the default value to take the end frame of the current scene

  * **xsamples** (_int in_ _[__1_ _,__128_ _]__,__(__optional_ _)_) – Transform Samples, Number of times per frame transformations are sampled

  * **gsamples** (_int in_ _[__1_ _,__128_ _]__,__(__optional_ _)_) – Geometry Samples, Number of times per frame object data are sampled

  * **sh_open** (_float in_ _[__-1_ _,__1_ _]__,__(__optional_ _)_) – Shutter Open, Time at which the shutter is open

  * **sh_close** (_float in_ _[__-1_ _,__1_ _]__,__(__optional_ _)_) – Shutter Close, Time at which the shutter is closed

  * **selected** (_boolean_ _,__(__optional_ _)_) – Selected Objects Only, Export only selected objects

  * **visible_objects_only** (_boolean_ _,__(__optional_ _)_) – Visible Objects Only, Export only objects that are visible

  * **flatten** (_boolean_ _,__(__optional_ _)_) – Flatten Hierarchy, Do not preserve objects’ parent/children relationship

  * **collection** (_string_ _,__(__optional_ _,__never None_ _)_) – Collection

  * **uvs** (_boolean_ _,__(__optional_ _)_) – UV Coordinates, Export UV coordinates

  * **packuv** (_boolean_ _,__(__optional_ _)_) – Merge UVs

  * **normals** (_boolean_ _,__(__optional_ _)_) – Normals, Export normals

  * **vcolors** (_boolean_ _,__(__optional_ _)_) – Color Attributes, Export color attributes

  * **orcos** (_boolean_ _,__(__optional_ _)_) – Generated Coordinates, Export undeformed mesh vertex coordinates

  * **face_sets** (_boolean_ _,__(__optional_ _)_) – Face Sets, Export per face shading group assignments

  * **subdiv_schema** (_boolean_ _,__(__optional_ _)_) – Use Subdivision Schema, Export meshes using Alembic’s subdivision schema

  * **apply_subdiv** (_boolean_ _,__(__optional_ _)_) – Apply Subdivision Surface, Export subdivision surfaces as meshes

  * **curves_as_mesh** (_boolean_ _,__(__optional_ _)_) – Curves as Mesh, Export curves and NURBS surfaces as meshes

  * **use_instancing** (_boolean_ _,__(__optional_ _)_) – Use Instancing, Export data of duplicated objects as Alembic instances; speeds up the export and can be disabled for compatibility with other software

  * **global_scale** (_float in_ _[__0.0001_ _,__1000_ _]__,__(__optional_ _)_) – Scale, Value by which to enlarge or shrink the objects with respect to the world’s origin

  * **triangulate** (_boolean_ _,__(__optional_ _)_) – Triangulate, Export polygons (quads and n-gons) as triangles

  * **quad_method** (enum in [Modifier Triangulate Quad Method Items](bpy_types_enum_items/modifier_triangulate_quad_method_items.html#rna-enum-modifier-triangulate-quad-method-items), (optional)) – Quad Method, Method for splitting the quads into triangles

  * **ngon_method** (enum in [Modifier Triangulate Ngon Method Items](bpy_types_enum_items/modifier_triangulate_ngon_method_items.html#rna-enum-modifier-triangulate-ngon-method-items), (optional)) – N-gon Method, Method for splitting the n-gons into triangles

  * **export_hair** (_boolean_ _,__(__optional_ _)_) – Export Hair, Exports hair particle systems as animated curves

  * **export_particles** (_boolean_ _,__(__optional_ _)_) – Export Particles, Exports non-hair particle systems

  * **export_custom_properties** (_boolean_ _,__(__optional_ _)_) – Export Custom Properties, Export custom properties to Alembic .userProperties

  * **as_background_job** (_boolean_ _,__(__optional_ _)_) – Run as Background Job, Enable this to run the import in the background, disable to block Blender while importing. This option is deprecated; EXECUTE this operator to run in the foreground, and INVOKE it to run as a background job

  * **evaluation_mode** (enum in [`RENDER`, `VIEWPORT`], (optional)) – 

Settings, Determines visibility of objects, modifier settings, and other areas
where there are different settings for viewport and rendering

    * `RENDER` Render – Use Render settings for object visibility, modifier settings, etc.

    * `VIEWPORT` Viewport – Use Viewport settings for object visibility, modifier settings, etc.

bpy.ops.wm.alembic_import(_*_ , _filepath =''_, _directory =''_, _files
=None_, _check_existing =False_, _filter_blender =False_, _filter_backup
=False_, _filter_image =False_, _filter_movie =False_, _filter_python =False_,
_filter_font =False_, _filter_sound =False_, _filter_text =False_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =True_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =8_, _relative_path =True_, _display_type =DEFAULT_, _sort_method_ ,
_filter_glob ='*.abc'_, _scale =1.0_, _set_frame_range =True_,
_validate_meshes =False_, _always_add_cache_reader =False_, _is_sequence
=False_, _as_background_job =False_)¶

    

Load an Alembic archive

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Directory, Directory of the file

  * **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – Files

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

  * **scale** (_float in_ _[__0.0001_ _,__1000_ _]__,__(__optional_ _)_) – Scale, Value by which to enlarge or shrink the objects with respect to the world’s origin

  * **set_frame_range** (_boolean_ _,__(__optional_ _)_) – Set Frame Range, If checked, update scene’s start and end frame to match those of the Alembic archive

  * **validate_meshes** (_boolean_ _,__(__optional_ _)_) – Validate Meshes, Ensure the data is valid (when disabled, data may be imported which causes crashes displaying or editing)

  * **always_add_cache_reader** (_boolean_ _,__(__optional_ _)_) – Always Add Cache Reader, Add cache modifiers and constraints to imported objects even if they are not animated so that they can be updated when reloading the Alembic archive

  * **is_sequence** (_boolean_ _,__(__optional_ _)_) – Is Sequence, Set to true if the cache is split into separate files

  * **as_background_job** (_boolean_ _,__(__optional_ _)_) – Run as Background Job, Enable this to run the export in the background, disable to block Blender while exporting. This option is deprecated; EXECUTE this operator to run in the foreground, and INVOKE it to run as a background job

bpy.ops.wm.append(_*_ , _filepath =''_, _directory =''_, _filename =''_,
_files =None_, _check_existing =False_, _filter_blender =True_, _filter_backup
=False_, _filter_image =False_, _filter_movie =False_, _filter_python =False_,
_filter_font =False_, _filter_sound =False_, _filter_text =False_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =True_,
_filemode =1_, _display_type =DEFAULT_, _sort_method_ , _link =False_,
_do_reuse_local_id =False_, _clear_asset_data =False_, _autoselect =True_,
_active_collection =True_, _instance_collections =False_,
_instance_object_data =True_, _set_fake =False_, _use_recursive =True_)¶

    

Append from a Library .blend file

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Directory, Directory of the file

  * **filename** (_string_ _,__(__optional_ _,__never None_ _)_) – File Name, Name of the file

  * **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – Files

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

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **link** (_boolean_ _,__(__optional_ _)_) – Link, Link the objects or data-blocks rather than appending

  * **do_reuse_local_id** (_boolean_ _,__(__optional_ _)_) – Re-Use Local Data, Try to re-use previously matching appended data-blocks instead of appending a new copy

  * **clear_asset_data** (_boolean_ _,__(__optional_ _)_) – Clear Asset Data, Don’t add asset meta-data or tags from the original data-block

  * **autoselect** (_boolean_ _,__(__optional_ _)_) – Select, Select new objects

  * **active_collection** (_boolean_ _,__(__optional_ _)_) – Active Collection, Put new objects on the active collection

  * **instance_collections** (_boolean_ _,__(__optional_ _)_) – Instance Collections, Create instances for collections, rather than adding them directly to the scene

  * **instance_object_data** (_boolean_ _,__(__optional_ _)_) – Instance Object Data, Create instances for object data which are not referenced by any objects

  * **set_fake** (_boolean_ _,__(__optional_ _)_) – Fake User, Set “Fake User” for appended items (except objects and collections)

  * **use_recursive** (_boolean_ _,__(__optional_ _)_) – Localize All, Localize all appended data, including those indirectly linked from other libraries

bpy.ops.wm.batch_rename(_*_ , _data_type =OBJECT_, _data_source =SELECT_,
_actions =None_)¶

    

Rename multiple items at once

Parameters:

    

  * **data_type** (enum in [`OBJECT`, `COLLECTION`, `MATERIAL`, `MESH`, `CURVE`, `META`, `VOLUME`, `GPENCIL`, `ARMATURE`, `LATTICE`, `LIGHT`, `LIGHT_PROBE`, `CAMERA`, `SPEAKER`, `BONE`, `NODE`, `SEQUENCE_STRIP`, `ACTION_CLIP`, `SCENE`, `BRUSH`], (optional)) – Type, Type of data to rename

  * **data_source** (enum in [`SELECT`, `ALL`], (optional)) – Source

  * **actions** (`bpy_prop_collection` of `BatchRenameAction`, (optional)) – actions

File:

    

[startup/bl_operators/wm.py:3270](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L3270)

bpy.ops.wm.blend_strings_utf8_validate()¶

    

Check and fix all strings in current .blend file to be valid UTF-8 Unicode
(needed for some old, 2.4x area files)

File:

    

[startup/bl_operators/file.py:289](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/file.py#L289)

bpy.ops.wm.call_asset_shelf_popover(_*_ , _name =''_)¶

    

Open a predefined asset shelf in a popup

Parameters:

    

**name** (_string_ _,__(__optional_ _,__never None_ _)_) – Asset Shelf Name,
Identifier of the asset shelf to display

bpy.ops.wm.call_menu(_*_ , _name =''_)¶

    

Open a predefined menu

Parameters:

    

**name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the
menu

bpy.ops.wm.call_menu_pie(_*_ , _name =''_)¶

    

Open a predefined pie menu

Parameters:

    

**name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the
pie menu

bpy.ops.wm.call_panel(_*_ , _name =''_, _keep_open =True_)¶

    

Open a predefined panel

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the menu

  * **keep_open** (_boolean_ _,__(__optional_ _)_) – Keep Open

bpy.ops.wm.clear_recent_files(_*_ , _remove =ALL_)¶

    

Clear the recent files list

Parameters:

    

**remove** (enum in [`ALL`, `MISSING`], (optional)) – Remove

bpy.ops.wm.collada_export(_*_ , _filepath =''_, _check_existing =True_,
_filter_blender =False_, _filter_backup =False_, _filter_image =False_,
_filter_movie =False_, _filter_python =False_, _filter_font =False_,
_filter_sound =False_, _filter_text =False_, _filter_archive =False_,
_filter_btx =False_, _filter_collada =True_, _filter_alembic =False_,
_filter_usd =False_, _filter_obj =False_, _filter_volume =False_,
_filter_folder =True_, _filter_blenlib =False_, _filemode =8_, _display_type
=DEFAULT_, _sort_method_ , _filter_glob ='*.dae'_, _prop_bc_export_ui_section
=main_, _apply_modifiers =False_, _export_mesh_type =0_,
_export_mesh_type_selection =view_, _export_global_forward_selection =Y_,
_export_global_up_selection =Z_, _apply_global_orientation =False_, _selected
=False_, _include_children =False_, _include_armatures =False_,
_include_shapekeys =False_, _deform_bones_only =False_, _include_animations
=True_, _include_all_actions =True_, _export_animation_type_selection
=sample_, _sampling_rate =1_, _keep_smooth_curves =False_, _keep_keyframes
=False_, _keep_flat_curves =False_, _active_uv_only =False_,
_use_texture_copies =True_, _triangulate =True_, _use_object_instantiation
=True_, _use_blender_profile =True_, _sort_by_name =False_,
_export_object_transformation_type =0_,
_export_object_transformation_type_selection =matrix_,
_export_animation_transformation_type =0_,
_export_animation_transformation_type_selection =matrix_, _open_sim =False_,
_limit_precision =False_, _keep_bind_info =False_)¶

    

Save a Collada file (Deprecated)

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

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

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **prop_bc_export_ui_section** (enum in [`main`, `geometry`, `armature`, `animation`, `collada`], (optional)) – 

Export Section, Only for User Interface organization

    * `main` Main – Data export section.

    * `geometry` Geom – Geometry export section.

    * `armature` Arm – Armature export section.

    * `animation` Anim – Animation export section.

    * `collada` Extra – Collada export section.

  * **apply_modifiers** (_boolean_ _,__(__optional_ _)_) – Apply Modifiers, Apply modifiers to exported mesh (non destructive)

  * **export_mesh_type** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Resolution, Modifier resolution for export

  * **export_mesh_type_selection** (enum in [`view`, `render`], (optional)) – 

Resolution, Modifier resolution for export

    * `view` Viewport – Apply modifier’s viewport settings.

    * `render` Render – Apply modifier’s render settings.

  * **export_global_forward_selection** (enum in [`X`, `Y`, `Z`, `-X`, `-Y`, `-Z`], (optional)) – 

Global Forward Axis, Global Forward axis for export

    * `X` X – Global Forward is positive X Axis.

    * `Y` Y – Global Forward is positive Y Axis.

    * `Z` Z – Global Forward is positive Z Axis.

    * `-X` -X – Global Forward is negative X Axis.

    * `-Y` -Y – Global Forward is negative Y Axis.

    * `-Z` -Z – Global Forward is negative Z Axis.

  * **export_global_up_selection** (enum in [`X`, `Y`, `Z`, `-X`, `-Y`, `-Z`], (optional)) – 

Global Up Axis, Global Up axis for export

    * `X` X – Global UP is positive X Axis.

    * `Y` Y – Global UP is positive Y Axis.

    * `Z` Z – Global UP is positive Z Axis.

    * `-X` -X – Global UP is negative X Axis.

    * `-Y` -Y – Global UP is negative Y Axis.

    * `-Z` -Z – Global UP is negative Z Axis.

  * **apply_global_orientation** (_boolean_ _,__(__optional_ _)_) – Apply Global Orientation, Rotate all root objects to match the global orientation settings otherwise set the global orientation per Collada asset

  * **selected** (_boolean_ _,__(__optional_ _)_) – Selection Only, Export only selected elements

  * **include_children** (_boolean_ _,__(__optional_ _)_) – Include Children, Export all children of selected objects (even if not selected)

  * **include_armatures** (_boolean_ _,__(__optional_ _)_) – Include Armatures, Export related armatures (even if not selected)

  * **include_shapekeys** (_boolean_ _,__(__optional_ _)_) – Include Shape Keys, Export all Shape Keys from Mesh Objects

  * **deform_bones_only** (_boolean_ _,__(__optional_ _)_) – Deform Bones Only, Only export deforming bones with armatures

  * **include_animations** (_boolean_ _,__(__optional_ _)_) – Include Animations, Export animations if available (exporting animations will enforce the decomposition of node transforms into <translation> <rotation> and <scale> components)

  * **include_all_actions** (_boolean_ _,__(__optional_ _)_) – Include all Actions, Export also unassigned actions (this allows you to export entire animation libraries for your character(s))

  * **export_animation_type_selection** (enum in [`sample`, `keys`], (optional)) – 

Key Type, Type for exported animations (use sample keys or Curve keys)

    * `sample` Samples – Export Sampled points guided by sampling rate.

    * `keys` Curves – Export Curves (note: guided by curve keys).

  * **sampling_rate** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Sampling Rate, The distance between 2 keyframes (1 to key every frame)

  * **keep_smooth_curves** (_boolean_ _,__(__optional_ _)_) – Keep Smooth curves, Export also the curve handles (if available) (this does only work when the inverse parent matrix is the unity matrix, otherwise you may end up with odd results)

  * **keep_keyframes** (_boolean_ _,__(__optional_ _)_) – Keep Keyframes, Use existing keyframes as additional sample points (this helps when you want to keep manual tweaks)

  * **keep_flat_curves** (_boolean_ _,__(__optional_ _)_) – All Keyed Curves, Export also curves which have only one key or are totally flat

  * **active_uv_only** (_boolean_ _,__(__optional_ _)_) – Only Selected UV Map, Export only the selected UV Map

  * **use_texture_copies** (_boolean_ _,__(__optional_ _)_) – Copy, Copy textures to same folder where the .dae file is exported

  * **triangulate** (_boolean_ _,__(__optional_ _)_) – Triangulate, Export polygons (quads and n-gons) as triangles

  * **use_object_instantiation** (_boolean_ _,__(__optional_ _)_) – Use Object Instances, Instantiate multiple Objects from same Data

  * **use_blender_profile** (_boolean_ _,__(__optional_ _)_) – Use Blender Profile, Export additional Blender specific information (for material, shaders, bones, etc.)

  * **sort_by_name** (_boolean_ _,__(__optional_ _)_) – Sort by Object name, Sort exported data by Object name

  * **export_object_transformation_type** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Transform, Object Transformation type for translation, scale and rotation

  * **export_object_transformation_type_selection** (enum in [`matrix`, `decomposed`], (optional)) – 

Transform, Object Transformation type for translation, scale and rotation

    * `matrix` Matrix – Use <matrix> representation for exported transformations.

    * `decomposed` Decomposed – Use <rotate>, <translate> and <scale> representation for exported transformations.

  * **export_animation_transformation_type** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Transform, Transformation type for translation, scale and rotation. Note: The Animation transformation type in the Anim Tab is always equal to the Object transformation type in the Geom tab

  * **export_animation_transformation_type_selection** (enum in [`matrix`, `decomposed`], (optional)) – 

Transform, Transformation type for translation, scale and rotation. Note: The
Animation transformation type in the Anim Tab is always equal to the Object
transformation type in the Geom tab

    * `matrix` Matrix – Use <matrix> representation for exported transformations.

    * `decomposed` Decomposed – Use <rotate>, <translate> and <scale> representation for exported transformations.

  * **open_sim** (_boolean_ _,__(__optional_ _)_) – Export to SL/OpenSim, Compatibility mode for Second Life, OpenSimulator and other compatible online worlds

  * **limit_precision** (_boolean_ _,__(__optional_ _)_) – Limit Precision, Reduce the precision of the exported data to 6 digits

  * **keep_bind_info** (_boolean_ _,__(__optional_ _)_) – Keep Bind Info, Store Bindpose information in custom bone properties for later use during Collada export

bpy.ops.wm.collada_import(_*_ , _filepath =''_, _check_existing =False_,
_filter_blender =False_, _filter_backup =False_, _filter_image =False_,
_filter_movie =False_, _filter_python =False_, _filter_font =False_,
_filter_sound =False_, _filter_text =False_, _filter_archive =False_,
_filter_btx =False_, _filter_collada =True_, _filter_alembic =False_,
_filter_usd =False_, _filter_obj =False_, _filter_volume =False_,
_filter_folder =True_, _filter_blenlib =False_, _filemode =8_, _display_type
=DEFAULT_, _sort_method_ , _filter_glob ='*.dae'_, _import_units =False_,
_custom_normals =True_, _fix_orientation =False_, _find_chains =False_,
_auto_connect =False_, _min_chain_length =0_, _keep_bind_info =False_)¶

    

Load a Collada file (Deprecated)

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

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

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **import_units** (_boolean_ _,__(__optional_ _)_) – Import Units, If disabled match import to Blender’s current Unit settings, otherwise use the settings from the Imported scene

  * **custom_normals** (_boolean_ _,__(__optional_ _)_) – Custom Normals, Import custom normals, if available (otherwise Blender will compute them)

  * **fix_orientation** (_boolean_ _,__(__optional_ _)_) – Fix Leaf Bones, Fix Orientation of Leaf Bones (Collada does only support Joints)

  * **find_chains** (_boolean_ _,__(__optional_ _)_) – Find Bone Chains, Find best matching Bone Chains and ensure bones in chain are connected

  * **auto_connect** (_boolean_ _,__(__optional_ _)_) – Auto Connect, Set use_connect for parent bones which have exactly one child bone

  * **min_chain_length** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Minimum Chain Length, When searching Bone Chains disregard chains of length below this value

  * **keep_bind_info** (_boolean_ _,__(__optional_ _)_) – Keep Bind Info, Store Bindpose information in custom bone properties for later use during Collada export

bpy.ops.wm.collection_export_all()¶

    

Invoke all configured exporters for all collections

bpy.ops.wm.context_collection_boolean_set(_*_ , _data_path_iter =''_,
_data_path_item =''_, _type =TOGGLE_)¶

    

Set boolean values for a collection of items

Parameters:

    

  * **data_path_iter** (_string_ _,__(__optional_ _,__never None_ _)_) – data_path_iter, The data path relative to the context, must point to an iterable

  * **data_path_item** (_string_ _,__(__optional_ _,__never None_ _)_) – data_path_item, The data path from each iterable to the value (int or float)

  * **type** (enum in [`TOGGLE`, `ENABLE`, `DISABLE`], (optional)) – Type

File:

    

[startup/bl_operators/wm.py:875](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L875)

bpy.ops.wm.context_cycle_array(_*_ , _data_path =''_, _reverse =False_)¶

    

Set a context array value (useful for cycling the active mesh edit mode)

Parameters:

    

  * **data_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Context Attributes, Context data-path (expanded using visible windows in the current .blend file)

  * **reverse** (_boolean_ _,__(__optional_ _)_) – Reverse, Cycle backwards

File:

    

[startup/bl_operators/wm.py:673](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L673)

bpy.ops.wm.context_cycle_enum(_*_ , _data_path =''_, _reverse =False_, _wrap
=False_)¶

    

Toggle a context value

Parameters:

    

  * **data_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Context Attributes, Context data-path (expanded using visible windows in the current .blend file)

  * **reverse** (_boolean_ _,__(__optional_ _)_) – Reverse, Cycle backwards

  * **wrap** (_boolean_ _,__(__optional_ _)_) – Wrap, Wrap back to the first/last values

File:

    

[startup/bl_operators/wm.py:624](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L624)

bpy.ops.wm.context_cycle_int(_*_ , _data_path =''_, _reverse =False_, _wrap
=False_)¶

    

Set a context value (useful for cycling active material, shape keys, groups,
etc.)

Parameters:

    

  * **data_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Context Attributes, Context data-path (expanded using visible windows in the current .blend file)

  * **reverse** (_boolean_ _,__(__optional_ _)_) – Reverse, Cycle backwards

  * **wrap** (_boolean_ _,__(__optional_ _)_) – Wrap, Wrap back to the first/last values

File:

    

[startup/bl_operators/wm.py:584](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L584)

bpy.ops.wm.context_menu_enum(_*_ , _data_path =''_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

**data_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Context
Attributes, Context data-path (expanded using visible windows in the current
.blend file)

File:

    

[startup/bl_operators/wm.py:703](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L703)

bpy.ops.wm.context_modal_mouse(_*_ , _data_path_iter =''_, _data_path_item
=''_, _header_text =''_, _input_scale =0.01_, _invert =False_, _initial_x
=0_)¶

    

Adjust arbitrary values with mouse input

Parameters:

    

  * **data_path_iter** (_string_ _,__(__optional_ _,__never None_ _)_) – data_path_iter, The data path relative to the context, must point to an iterable

  * **data_path_item** (_string_ _,__(__optional_ _,__never None_ _)_) – data_path_item, The data path from each iterable to the value (int or float)

  * **header_text** (_string_ _,__(__optional_ _,__never None_ _)_) – Header Text, Text to display in header during scale

  * **input_scale** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – input_scale, Scale the mouse movement by this value before applying the delta

  * **invert** (_boolean_ _,__(__optional_ _)_) – invert, Invert the mouse input

  * **initial_x** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – initial_x

File:

    

[startup/bl_operators/wm.py:1014](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L1014)

bpy.ops.wm.context_pie_enum(_*_ , _data_path =''_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

**data_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Context
Attributes, Context data-path (expanded using visible windows in the current
.blend file)

File:

    

[startup/bl_operators/wm.py:735](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L735)

bpy.ops.wm.context_scale_float(_*_ , _data_path =''_, _value =1.0_)¶

    

Scale a float context value

Parameters:

    

  * **data_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Context Attributes, Context data-path (expanded using visible windows in the current .blend file)

  * **value** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Value, Assign value

File:

    

[startup/bl_operators/wm.py:338](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L338)

bpy.ops.wm.context_scale_int(_*_ , _data_path =''_, _value =1.0_, _always_step
=True_)¶

    

Scale an int context value

Parameters:

    

  * **data_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Context Attributes, Context data-path (expanded using visible windows in the current .blend file)

  * **value** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Value, Assign value

  * **always_step** (_boolean_ _,__(__optional_ _)_) – Always Step, Always adjust the value by a minimum of 1 when ‘value’ is not 1.0

File:

    

[startup/bl_operators/wm.py:376](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L376)

bpy.ops.wm.context_set_boolean(_*_ , _data_path =''_, _value =True_)¶

    

Set a context value

Parameters:

    

  * **data_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Context Attributes, Context data-path (expanded using visible windows in the current .blend file)

  * **value** (_boolean_ _,__(__optional_ _)_) – Value, Assignment value

File:

    

[startup/bl_operators/wm.py:267](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L267)

bpy.ops.wm.context_set_enum(_*_ , _data_path =''_, _value =''_)¶

    

Set a context value

Parameters:

    

  * **data_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Context Attributes, Context data-path (expanded using visible windows in the current .blend file)

  * **value** (_string_ _,__(__optional_ _,__never None_ _)_) – Value, Assignment value (as a string)

File:

    

[startup/bl_operators/wm.py:267](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L267)

bpy.ops.wm.context_set_float(_*_ , _data_path =''_, _value =0.0_, _relative
=False_)¶

    

Set a context value

Parameters:

    

  * **data_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Context Attributes, Context data-path (expanded using visible windows in the current .blend file)

  * **value** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Value, Assignment value

  * **relative** (_boolean_ _,__(__optional_ _)_) – Relative, Apply relative to the current value (delta)

File:

    

[startup/bl_operators/wm.py:267](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L267)

bpy.ops.wm.context_set_id(_*_ , _data_path =''_, _value =''_)¶

    

Set a context value to an ID data-block

Parameters:

    

  * **data_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Context Attributes, Context data-path (expanded using visible windows in the current .blend file)

  * **value** (_string_ _,__(__optional_ _,__never None_ _)_) – Value, Assign value

File:

    

[startup/bl_operators/wm.py:817](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L817)

bpy.ops.wm.context_set_int(_*_ , _data_path =''_, _value =0_, _relative
=False_)¶

    

Set a context value

Parameters:

    

  * **data_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Context Attributes, Context data-path (expanded using visible windows in the current .blend file)

  * **value** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Value, Assign value

  * **relative** (_boolean_ _,__(__optional_ _)_) – Relative, Apply relative to the current value (delta)

File:

    

[startup/bl_operators/wm.py:267](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L267)

bpy.ops.wm.context_set_string(_*_ , _data_path =''_, _value =''_)¶

    

Set a context value

Parameters:

    

  * **data_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Context Attributes, Context data-path (expanded using visible windows in the current .blend file)

  * **value** (_string_ _,__(__optional_ _,__never None_ _)_) – Value, Assign value

File:

    

[startup/bl_operators/wm.py:267](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L267)

bpy.ops.wm.context_set_value(_*_ , _data_path =''_, _value =''_)¶

    

Set a context value

Parameters:

    

  * **data_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Context Attributes, Context data-path (expanded using visible windows in the current .blend file)

  * **value** (_string_ _,__(__optional_ _,__never None_ _)_) – Value, Assignment value (as a string)

File:

    

[startup/bl_operators/wm.py:480](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L480)

bpy.ops.wm.context_toggle(_*_ , _data_path =''_, _module =''_)¶

    

Toggle a context value

Parameters:

    

  * **data_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Context Attributes, Context data-path (expanded using visible windows in the current .blend file)

  * **module** (_string_ _,__(__optional_ _,__never None_ _)_) – Module, Optionally override the context with a module

File:

    

[startup/bl_operators/wm.py:504](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L504)

bpy.ops.wm.context_toggle_enum(_*_ , _data_path =''_, _value_1 =''_, _value_2
=''_)¶

    

Toggle a context value

Parameters:

    

  * **data_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Context Attributes, Context data-path (expanded using visible windows in the current .blend file)

  * **value_1** (_string_ _,__(__optional_ _,__never None_ _)_) – Value, Toggle enum

  * **value_2** (_string_ _,__(__optional_ _,__never None_ _)_) – Value, Toggle enum

File:

    

[startup/bl_operators/wm.py:545](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L545)

bpy.ops.wm.debug_menu(_*_ , _debug_value =0_)¶

    

Open a popup to set the debug level

Parameters:

    

**debug_value** (_int in_ _[__-32768_ _,__32767_ _]__,__(__optional_ _)_) –
Debug Value

bpy.ops.wm.doc_view(_*_ , _doc_id =''_)¶

    

Open online reference docs in a web browser

Parameters:

    

**doc_id** (_string_ _,__(__optional_ _,__never None_ _)_) – Doc ID

File:

    

[startup/bl_operators/wm.py:1358](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L1358)

bpy.ops.wm.doc_view_manual(_*_ , _doc_id =''_)¶

    

Load online manual

Parameters:

    

**doc_id** (_string_ _,__(__optional_ _,__never None_ _)_) – Doc ID

File:

    

[startup/bl_operators/wm.py:1331](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L1331)

bpy.ops.wm.doc_view_manual_ui_context()¶

    

View a context based online manual in a web browser

bpy.ops.wm.drop_blend_file(_*_ , _filepath =''_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

**filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – filepath

File:

    

[startup/bl_operators/wm.py:3633](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L3633)

bpy.ops.wm.drop_import_file(_*_ , _directory =''_, _files =None_)¶

    

Operator that allows file handlers to receive file drops

Parameters:

    

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Directory, Directory of the file

  * **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – Files

bpy.ops.wm.fbx_import(_*_ , _filepath =''_, _directory =''_, _files =None_,
_check_existing =False_, _filter_blender =False_, _filter_backup =False_,
_filter_image =False_, _filter_movie =False_, _filter_python =False_,
_filter_font =False_, _filter_sound =False_, _filter_text =False_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =8_, _display_type =DEFAULT_, _sort_method_ , _global_scale =1.0_,
_import_colors =SRGB_, _use_custom_normals =True_, _use_custom_props =True_,
_use_custom_props_enum_as_string =True_, _import_subdivision =False_,
_ignore_leaf_bones =False_, _validate_meshes =True_, _use_anim =True_,
_anim_offset =1.0_, _filter_glob ='*.fbx'_)¶

    

Import FBX file into current scene

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Directory, Directory of the file

  * **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – Files

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

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **global_scale** (_float in_ _[__1e-06_ _,__1e+06_ _]__,__(__optional_ _)_) – Scale

  * **import_colors** (enum in [`NONE`, `SRGB`, `LINEAR`], (optional)) – 

Vertex Colors, Import vertex color attributes

    * `NONE` None – Do not import color attributes.

    * `SRGB` sRGB – Vertex colors in the file are in sRGB color space.

    * `LINEAR` Linear – Vertex colors in the file are in linear color space.

  * **use_custom_normals** (_boolean_ _,__(__optional_ _)_) – Custom Normals, Import custom normals, if available (otherwise Blender will compute them)

  * **use_custom_props** (_boolean_ _,__(__optional_ _)_) – Custom Properties, Import user properties as custom properties

  * **use_custom_props_enum_as_string** (_boolean_ _,__(__optional_ _)_) – Enums As Strings, Store custom property enumeration values as strings

  * **import_subdivision** (_boolean_ _,__(__optional_ _)_) – Subdivision Data, Import FBX subdivision information as subdivision surface modifiers

  * **ignore_leaf_bones** (_boolean_ _,__(__optional_ _)_) – Ignore Leaf Bones, Ignore the last bone at the end of each chain (used to mark the length of the previous bone)

  * **validate_meshes** (_boolean_ _,__(__optional_ _)_) – Validate Meshes, Ensure the data is valid (when disabled, data may be imported which causes crashes displaying or editing)

  * **use_anim** (_boolean_ _,__(__optional_ _)_) – Import Animation, Import FBX animation

  * **anim_offset** (_float in_ _[__-1e+06_ _,__1e+06_ _]__,__(__optional_ _)_) – Offset, Offset to apply to animation timestamps, in frames

  * **filter_glob** (_string_ _,__(__optional_ _,__never None_ _)_) – Extension Filter

bpy.ops.wm.grease_pencil_export_pdf(_*_ , _filepath =''_, _check_existing
=True_, _filter_blender =False_, _filter_backup =False_, _filter_image
=False_, _filter_movie =False_, _filter_python =False_, _filter_font =False_,
_filter_sound =False_, _filter_text =False_, _filter_archive =False_,
_filter_btx =False_, _filter_collada =False_, _filter_alembic =False_,
_filter_usd =False_, _filter_obj =True_, _filter_volume =False_,
_filter_folder =True_, _filter_blenlib =False_, _filemode =8_, _display_type
=DEFAULT_, _sort_method_ , _use_fill =True_, _selected_object_type =ACTIVE_,
_frame_mode =ACTIVE_, _stroke_sample =0.0_, _use_uniform_width =False_)¶

    

Export Grease Pencil to PDF

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

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

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **use_fill** (_boolean_ _,__(__optional_ _)_) – Fill, Export strokes with fill enabled

  * **selected_object_type** (enum in [`ACTIVE`, `SELECTED`, `VISIBLE`], (optional)) – 

Object, Which objects to include in the export

    * `ACTIVE` Active – Include only the active object.

    * `SELECTED` Selected – Include selected objects.

    * `VISIBLE` Visible – Include all visible objects.

  * **frame_mode** (enum in [`ACTIVE`, `SELECTED`, `SCENE`], (optional)) – 

Frames, Which frames to include in the export

    * `ACTIVE` Active – Include only active frame.

    * `SELECTED` Selected – Include selected frames.

    * `SCENE` Scene – Include all scene frames.

  * **stroke_sample** (_float in_ _[__0_ _,__100_ _]__,__(__optional_ _)_) – Sampling, Precision of stroke sampling. Low values mean a more precise result, and zero disables sampling

  * **use_uniform_width** (_boolean_ _,__(__optional_ _)_) – Uniform Width, Export strokes with uniform width

bpy.ops.wm.grease_pencil_export_svg(_*_ , _filepath =''_, _check_existing
=True_, _filter_blender =False_, _filter_backup =False_, _filter_image
=False_, _filter_movie =False_, _filter_python =False_, _filter_font =False_,
_filter_sound =False_, _filter_text =False_, _filter_archive =False_,
_filter_btx =False_, _filter_collada =False_, _filter_alembic =False_,
_filter_usd =False_, _filter_obj =True_, _filter_volume =False_,
_filter_folder =True_, _filter_blenlib =False_, _filemode =8_, _display_type
=DEFAULT_, _sort_method_ , _use_fill =True_, _selected_object_type =ACTIVE_,
_frame_mode =ACTIVE_, _stroke_sample =0.0_, _use_uniform_width =False_,
_use_clip_camera =False_)¶

    

Export Grease Pencil to SVG

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

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

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **use_fill** (_boolean_ _,__(__optional_ _)_) – Fill, Export strokes with fill enabled

  * **selected_object_type** (enum in [`ACTIVE`, `SELECTED`, `VISIBLE`], (optional)) – 

Object, Which objects to include in the export

    * `ACTIVE` Active – Include only the active object.

    * `SELECTED` Selected – Include selected objects.

    * `VISIBLE` Visible – Include all visible objects.

  * **frame_mode** (enum in [`ACTIVE`, `SELECTED`, `SCENE`], (optional)) – 

Frames, Which frames to include in the export

    * `ACTIVE` Active – Include only active frame.

    * `SELECTED` Selected – Include selected frames.

    * `SCENE` Scene – Include all scene frames.

  * **stroke_sample** (_float in_ _[__0_ _,__100_ _]__,__(__optional_ _)_) – Sampling, Precision of stroke sampling. Low values mean a more precise result, and zero disables sampling

  * **use_uniform_width** (_boolean_ _,__(__optional_ _)_) – Uniform Width, Export strokes with uniform width

  * **use_clip_camera** (_boolean_ _,__(__optional_ _)_) – Clip Camera, Clip drawings to camera size when exporting in camera view

bpy.ops.wm.grease_pencil_import_svg(_*_ , _filepath =''_, _directory =''_,
_files =None_, _check_existing =False_, _filter_blender =False_,
_filter_backup =False_, _filter_image =False_, _filter_movie =False_,
_filter_python =False_, _filter_font =False_, _filter_sound =False_,
_filter_text =False_, _filter_archive =False_, _filter_btx =False_,
_filter_collada =False_, _filter_alembic =False_, _filter_usd =False_,
_filter_obj =True_, _filter_volume =False_, _filter_folder =True_,
_filter_blenlib =False_, _filemode =8_, _relative_path =True_, _display_type
=DEFAULT_, _sort_method_ , _resolution =10_, _scale =10.0_, _use_scene_unit
=False_)¶

    

Import SVG into Grease Pencil

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Directory, Directory of the file

  * **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – Files

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

  * **resolution** (_int in_ _[__1_ _,__100000_ _]__,__(__optional_ _)_) – Resolution, Resolution of the generated strokes

  * **scale** (_float in_ _[__1e-06_ _,__1e+06_ _]__,__(__optional_ _)_) – Scale, Scale of the final strokes

  * **use_scene_unit** (_boolean_ _,__(__optional_ _)_) – Scene Unit, Apply current scene’s unit (as defined by unit scale) to imported data

bpy.ops.wm.id_linked_relocate(_*_ , _id_session_uid =0_, _filepath =''_,
_directory =''_, _filename =''_, _check_existing =False_, _filter_blender
=True_, _filter_backup =False_, _filter_image =False_, _filter_movie =False_,
_filter_python =False_, _filter_font =False_, _filter_sound =False_,
_filter_text =False_, _filter_archive =False_, _filter_btx =False_,
_filter_collada =False_, _filter_alembic =False_, _filter_usd =False_,
_filter_obj =False_, _filter_volume =False_, _filter_folder =True_,
_filter_blenlib =True_, _filemode =1_, _relative_path =True_, _display_type
=DEFAULT_, _sort_method_ , _link =True_, _do_reuse_local_id =False_,
_clear_asset_data =False_, _autoselect =True_, _active_collection =False_,
_instance_collections =False_, _instance_object_data =False_)¶

    

Relocate a linked ID, i.e. select another ID to link, and remap its local
usages to that newly linked data-block). Currently only designed as an
internal operator, not directly exposed to the user

Parameters:

    

  * **id_session_uid** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Linked ID Session UID, Unique runtime identifier for the linked ID to relocate

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Directory, Directory of the file

  * **filename** (_string_ _,__(__optional_ _,__never None_ _)_) – File Name, Name of the file

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

  * **link** (_boolean_ _,__(__optional_ _)_) – Link, Link the objects or data-blocks rather than appending

  * **do_reuse_local_id** (_boolean_ _,__(__optional_ _)_) – Re-Use Local Data, Try to re-use previously matching appended data-blocks instead of appending a new copy

  * **clear_asset_data** (_boolean_ _,__(__optional_ _)_) – Clear Asset Data, Don’t add asset meta-data or tags from the original data-block

  * **autoselect** (_boolean_ _,__(__optional_ _)_) – Select, Select new objects

  * **active_collection** (_boolean_ _,__(__optional_ _)_) – Active Collection, Put new objects on the active collection

  * **instance_collections** (_boolean_ _,__(__optional_ _)_) – Instance Collections, Create instances for collections, rather than adding them directly to the scene

  * **instance_object_data** (_boolean_ _,__(__optional_ _)_) – Instance Object Data, Create instances for object data which are not referenced by any objects

bpy.ops.wm.interface_theme_preset_add(_*_ , _name =''_, _remove_name =False_,
_remove_active =False_)¶

    

Add a custom theme to the preset list

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the preset, used to make the path name

  * **remove_name** (_boolean_ _,__(__optional_ _)_) – remove_name

  * **remove_active** (_boolean_ _,__(__optional_ _)_) – remove_active

File:

    

[startup/bl_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.wm.interface_theme_preset_remove(_*_ , _name =''_, _remove_name
=False_, _remove_active =True_)¶

    

Remove a custom theme from the preset list

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the preset, used to make the path name

  * **remove_name** (_boolean_ _,__(__optional_ _)_) – remove_name

  * **remove_active** (_boolean_ _,__(__optional_ _)_) – remove_active

File:

    

[startup/bl_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.wm.interface_theme_preset_save(_*_ , _name =''_, _remove_name =False_,
_remove_active =True_)¶

    

Save a custom theme in the preset list

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the preset, used to make the path name

  * **remove_name** (_boolean_ _,__(__optional_ _)_) – remove_name

  * **remove_active** (_boolean_ _,__(__optional_ _)_) – remove_active

File:

    

[startup/bl_operators/presets.py:710](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L710)

bpy.ops.wm.keyconfig_preset_add(_*_ , _name =''_, _remove_name =False_,
_remove_active =False_)¶

    

Add a custom keymap configuration to the preset list

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the preset, used to make the path name

  * **remove_name** (_boolean_ _,__(__optional_ _)_) – remove_name

  * **remove_active** (_boolean_ _,__(__optional_ _)_) – remove_active

File:

    

[startup/bl_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.wm.keyconfig_preset_remove(_*_ , _name =''_, _remove_name =False_,
_remove_active =True_)¶

    

Remove a custom keymap configuration from the preset list

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the preset, used to make the path name

  * **remove_name** (_boolean_ _,__(__optional_ _)_) – remove_name

  * **remove_active** (_boolean_ _,__(__optional_ _)_) – remove_active

File:

    

[startup/bl_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.wm.lib_reload(_*_ , _library =''_, _filepath =''_, _directory =''_,
_filename =''_, _hide_props_region =True_, _check_existing =False_,
_filter_blender =True_, _filter_backup =False_, _filter_image =False_,
_filter_movie =False_, _filter_python =False_, _filter_font =False_,
_filter_sound =False_, _filter_text =False_, _filter_archive =False_,
_filter_btx =False_, _filter_collada =False_, _filter_alembic =False_,
_filter_usd =False_, _filter_obj =False_, _filter_volume =False_,
_filter_folder =True_, _filter_blenlib =False_, _filemode =8_, _relative_path
=True_, _display_type =DEFAULT_, _sort_method_)¶

    

Reload the given library

Parameters:

    

  * **library** (_string_ _,__(__optional_ _,__never None_ _)_) – Library, Library to reload

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Directory, Directory of the file

  * **filename** (_string_ _,__(__optional_ _,__never None_ _)_) – File Name, Name of the file

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

bpy.ops.wm.lib_relocate(_*_ , _library =''_, _filepath =''_, _directory =''_,
_filename =''_, _files =None_, _hide_props_region =True_, _check_existing
=False_, _filter_blender =True_, _filter_backup =False_, _filter_image
=False_, _filter_movie =False_, _filter_python =False_, _filter_font =False_,
_filter_sound =False_, _filter_text =False_, _filter_archive =False_,
_filter_btx =False_, _filter_collada =False_, _filter_alembic =False_,
_filter_usd =False_, _filter_obj =False_, _filter_volume =False_,
_filter_folder =True_, _filter_blenlib =False_, _filemode =8_, _relative_path
=True_, _display_type =DEFAULT_, _sort_method_)¶

    

Relocate the given library to one or several others

Parameters:

    

  * **library** (_string_ _,__(__optional_ _,__never None_ _)_) – Library, Library to relocate

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Directory, Directory of the file

  * **filename** (_string_ _,__(__optional_ _,__never None_ _)_) – File Name, Name of the file

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

bpy.ops.wm.link(_*_ , _filepath =''_, _directory =''_, _filename =''_, _files
=None_, _check_existing =False_, _filter_blender =True_, _filter_backup
=False_, _filter_image =False_, _filter_movie =False_, _filter_python =False_,
_filter_font =False_, _filter_sound =False_, _filter_text =False_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =True_,
_filemode =1_, _relative_path =True_, _display_type =DEFAULT_, _sort_method_ ,
_link =True_, _do_reuse_local_id =False_, _clear_asset_data =False_,
_autoselect =True_, _active_collection =True_, _instance_collections =True_,
_instance_object_data =True_)¶

    

Link from a Library .blend file

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Directory, Directory of the file

  * **filename** (_string_ _,__(__optional_ _,__never None_ _)_) – File Name, Name of the file

  * **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – Files

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

  * **link** (_boolean_ _,__(__optional_ _)_) – Link, Link the objects or data-blocks rather than appending

  * **do_reuse_local_id** (_boolean_ _,__(__optional_ _)_) – Re-Use Local Data, Try to re-use previously matching appended data-blocks instead of appending a new copy

  * **clear_asset_data** (_boolean_ _,__(__optional_ _)_) – Clear Asset Data, Don’t add asset meta-data or tags from the original data-block

  * **autoselect** (_boolean_ _,__(__optional_ _)_) – Select, Select new objects

  * **active_collection** (_boolean_ _,__(__optional_ _)_) – Active Collection, Put new objects on the active collection

  * **instance_collections** (_boolean_ _,__(__optional_ _)_) – Instance Collections, Create instances for collections, rather than adding them directly to the scene

  * **instance_object_data** (_boolean_ _,__(__optional_ _)_) – Instance Object Data, Create instances for object data which are not referenced by any objects

bpy.ops.wm.memory_statistics()¶

    

Print memory statistics to the console

bpy.ops.wm.obj_export(_*_ , _filepath =''_, _check_existing =True_,
_filter_blender =False_, _filter_backup =False_, _filter_image =False_,
_filter_movie =False_, _filter_python =False_, _filter_font =False_,
_filter_sound =False_, _filter_text =False_, _filter_archive =False_,
_filter_btx =False_, _filter_collada =False_, _filter_alembic =False_,
_filter_usd =False_, _filter_obj =False_, _filter_volume =False_,
_filter_folder =True_, _filter_blenlib =False_, _filemode =8_, _display_type
=DEFAULT_, _sort_method_ , _export_animation =False_, _start_frame
=-2147483648_, _end_frame =2147483647_, _forward_axis =NEGATIVE_Z_, _up_axis
=Y_, _global_scale =1.0_, _apply_modifiers =True_, _export_eval_mode
=DAG_EVAL_VIEWPORT_, _export_selected_objects =False_, _export_uv =True_,
_export_normals =True_, _export_colors =False_, _export_materials =True_,
_export_pbr_extensions =False_, _path_mode =AUTO_, _export_triangulated_mesh
=False_, _export_curves_as_nurbs =False_, _export_object_groups =False_,
_export_material_groups =False_, _export_vertex_groups =False_,
_export_smooth_groups =False_, _smooth_group_bitflags =False_, _filter_glob
='*.obj;*.mtl'_, _collection =''_)¶

    

Save the scene to a Wavefront OBJ file

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

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

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **export_animation** (_boolean_ _,__(__optional_ _)_) – Export Animation, Export multiple frames instead of the current frame only

  * **start_frame** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Start Frame, The first frame to be exported

  * **end_frame** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – End Frame, The last frame to be exported

  * **forward_axis** (enum in [`X`, `Y`, `Z`, `NEGATIVE_X`, `NEGATIVE_Y`, `NEGATIVE_Z`], (optional)) – 

Forward Axis

    * `X` X – Positive X axis.

    * `Y` Y – Positive Y axis.

    * `Z` Z – Positive Z axis.

    * `NEGATIVE_X` -X – Negative X axis.

    * `NEGATIVE_Y` -Y – Negative Y axis.

    * `NEGATIVE_Z` -Z – Negative Z axis.

  * **up_axis** (enum in [`X`, `Y`, `Z`, `NEGATIVE_X`, `NEGATIVE_Y`, `NEGATIVE_Z`], (optional)) – 

Up Axis

    * `X` X – Positive X axis.

    * `Y` Y – Positive Y axis.

    * `Z` Z – Positive Z axis.

    * `NEGATIVE_X` -X – Negative X axis.

    * `NEGATIVE_Y` -Y – Negative Y axis.

    * `NEGATIVE_Z` -Z – Negative Z axis.

  * **global_scale** (_float in_ _[__0.0001_ _,__10000_ _]__,__(__optional_ _)_) – Scale, Value by which to enlarge or shrink the objects with respect to the world’s origin

  * **apply_modifiers** (_boolean_ _,__(__optional_ _)_) – Apply Modifiers, Apply modifiers to exported meshes

  * **export_eval_mode** (enum in [`DAG_EVAL_RENDER`, `DAG_EVAL_VIEWPORT`], (optional)) – 

Object Properties, Determines properties like object visibility, modifiers
etc., where they differ for Render and Viewport

    * `DAG_EVAL_RENDER` Render – Export objects as they appear in render.

    * `DAG_EVAL_VIEWPORT` Viewport – Export objects as they appear in the viewport.

  * **export_selected_objects** (_boolean_ _,__(__optional_ _)_) – Export Selected Objects, Export only selected objects instead of all supported objects

  * **export_uv** (_boolean_ _,__(__optional_ _)_) – Export UVs

  * **export_normals** (_boolean_ _,__(__optional_ _)_) – Export Normals, Export per-face normals if the face is flat-shaded, per-face-corner normals if smooth-shaded

  * **export_colors** (_boolean_ _,__(__optional_ _)_) – Export Colors, Export per-vertex colors

  * **export_materials** (_boolean_ _,__(__optional_ _)_) – Export Materials, Export MTL library. There must be a Principled-BSDF node for image textures to be exported to the MTL file

  * **export_pbr_extensions** (_boolean_ _,__(__optional_ _)_) – Export Materials with PBR Extensions, Export MTL library using PBR extensions (roughness, metallic, sheen, coat, anisotropy, transmission)

  * **path_mode** (enum in [`AUTO`, `ABSOLUTE`, `RELATIVE`, `MATCH`, `STRIP`, `COPY`], (optional)) – 

Path Mode, Method used to reference paths

    * `AUTO` Auto – Use relative paths with subdirectories only.

    * `ABSOLUTE` Absolute – Always write absolute paths.

    * `RELATIVE` Relative – Write relative paths where possible.

    * `MATCH` Match – Match absolute/relative setting with input path.

    * `STRIP` Strip – Write filename only.

    * `COPY` Copy – Copy the file to the destination path.

  * **export_triangulated_mesh** (_boolean_ _,__(__optional_ _)_) – Export Triangulated Mesh, All ngons with four or more vertices will be triangulated. Meshes in the scene will not be affected. Behaves like Triangulate Modifier with ngon-method: “Beauty”, quad-method: “Shortest Diagonal”, min vertices: 4

  * **export_curves_as_nurbs** (_boolean_ _,__(__optional_ _)_) – Export Curves as NURBS, Export curves in parametric form instead of exporting as mesh

  * **export_object_groups** (_boolean_ _,__(__optional_ _)_) – Export Object Groups, Append mesh name to object name, separated by a ‘_’

  * **export_material_groups** (_boolean_ _,__(__optional_ _)_) – Export Material Groups, Generate an OBJ group for each part of a geometry using a different material

  * **export_vertex_groups** (_boolean_ _,__(__optional_ _)_) – Export Vertex Groups, Export the name of the vertex group of a face. It is approximated by choosing the vertex group with the most members among the vertices of a face

  * **export_smooth_groups** (_boolean_ _,__(__optional_ _)_) – Export Smooth Groups, Generate smooth groups identifiers for each group of smooth faces, as unique integer values by default

  * **smooth_group_bitflags** (_boolean_ _,__(__optional_ _)_) – Bitflags Smooth Groups, If exporting smoothgroups, generate ‘bitflags’ values for the groups, instead of unique integer values. The same bitflag value can be re-used for different groups of smooth faces, as long as they have no common sharp edges or vertices

  * **filter_glob** (_string_ _,__(__optional_ _,__never None_ _)_) – Extension Filter

  * **collection** (_string_ _,__(__optional_ _,__never None_ _)_) – Collection

bpy.ops.wm.obj_import(_*_ , _filepath =''_, _directory =''_, _files =None_,
_check_existing =False_, _filter_blender =False_, _filter_backup =False_,
_filter_image =False_, _filter_movie =False_, _filter_python =False_,
_filter_font =False_, _filter_sound =False_, _filter_text =False_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =8_, _display_type =DEFAULT_, _sort_method_ , _global_scale =1.0_,
_clamp_size =0.0_, _forward_axis =NEGATIVE_Z_, _up_axis =Y_,
_use_split_objects =True_, _use_split_groups =False_, _import_vertex_groups
=False_, _validate_meshes =True_, _close_spline_loops =True_,
_collection_separator =''_, _filter_glob ='*.obj;*.mtl'_)¶

    

Load a Wavefront OBJ scene

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Directory, Directory of the file

  * **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – Files

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

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **global_scale** (_float in_ _[__0.0001_ _,__10000_ _]__,__(__optional_ _)_) – Scale, Value by which to enlarge or shrink the objects with respect to the world’s origin

  * **clamp_size** (_float in_ _[__0_ _,__1000_ _]__,__(__optional_ _)_) – Clamp Bounding Box, Resize the objects to keep bounding box under this value. Value 0 disables clamping

  * **forward_axis** (enum in [`X`, `Y`, `Z`, `NEGATIVE_X`, `NEGATIVE_Y`, `NEGATIVE_Z`], (optional)) – 

Forward Axis

    * `X` X – Positive X axis.

    * `Y` Y – Positive Y axis.

    * `Z` Z – Positive Z axis.

    * `NEGATIVE_X` -X – Negative X axis.

    * `NEGATIVE_Y` -Y – Negative Y axis.

    * `NEGATIVE_Z` -Z – Negative Z axis.

  * **up_axis** (enum in [`X`, `Y`, `Z`, `NEGATIVE_X`, `NEGATIVE_Y`, `NEGATIVE_Z`], (optional)) – 

Up Axis

    * `X` X – Positive X axis.

    * `Y` Y – Positive Y axis.

    * `Z` Z – Positive Z axis.

    * `NEGATIVE_X` -X – Negative X axis.

    * `NEGATIVE_Y` -Y – Negative Y axis.

    * `NEGATIVE_Z` -Z – Negative Z axis.

  * **use_split_objects** (_boolean_ _,__(__optional_ _)_) – Split By Object, Import each OBJ ‘o’ as a separate object

  * **use_split_groups** (_boolean_ _,__(__optional_ _)_) – Split By Group, Import each OBJ ‘g’ as a separate object

  * **import_vertex_groups** (_boolean_ _,__(__optional_ _)_) – Vertex Groups, Import OBJ groups as vertex groups

  * **validate_meshes** (_boolean_ _,__(__optional_ _)_) – Validate Meshes, Ensure the data is valid (when disabled, data may be imported which causes crashes displaying or editing)

  * **close_spline_loops** (_boolean_ _,__(__optional_ _)_) – Detect Cyclic Curves, Join curve endpoints if overlapping control points are detected (if disabled, no curves will be cyclic)

  * **collection_separator** (_string_ _,__(__optional_ _,__never None_ _)_) – Path Separator, Character used to separate objects name into hierarchical structure

  * **filter_glob** (_string_ _,__(__optional_ _,__never None_ _)_) – Extension Filter

bpy.ops.wm.open_mainfile(_*_ , _filepath =''_, _hide_props_region =True_,
_check_existing =False_, _filter_blender =True_, _filter_backup =False_,
_filter_image =False_, _filter_movie =False_, _filter_python =False_,
_filter_font =False_, _filter_sound =False_, _filter_text =False_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =8_, _display_type =DEFAULT_, _sort_method_ , _load_ui =True_,
_use_scripts =False_, _display_file_selector =True_, _state =0_)¶

    

Open a Blender file

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

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **load_ui** (_boolean_ _,__(__optional_ _)_) – Load UI, Load user interface setup in the .blend file

  * **use_scripts** (_boolean_ _,__(__optional_ _)_) – Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences

  * **display_file_selector** (_boolean_ _,__(__optional_ _)_) – Display File Selector

  * **state** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – State

bpy.ops.wm.operator_cheat_sheet()¶

    

List all the operators in a text-block, useful for scripting

File:

    

[startup/bl_operators/wm.py:2246](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2246)

bpy.ops.wm.operator_defaults()¶

    

Set the active operator to its default values

bpy.ops.wm.operator_pie_enum(_*_ , _data_path =''_, _prop_string =''_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

  * **data_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Operator, Operator name (in Python as string)

  * **prop_string** (_string_ _,__(__optional_ _,__never None_ _)_) – Property, Property name (as a string)

File:

    

[startup/bl_operators/wm.py:777](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L777)

bpy.ops.wm.operator_preset_add(_*_ , _name =''_, _remove_name =False_,
_remove_active =False_, _operator =''_)¶

    

Add or remove an Operator Preset

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the preset, used to make the path name

  * **remove_name** (_boolean_ _,__(__optional_ _)_) – remove_name

  * **remove_active** (_boolean_ _,__(__optional_ _)_) – remove_active

  * **operator** (_string_ _,__(__optional_ _,__never None_ _)_) – Operator

File:

    

[startup/bl_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.wm.operator_presets_cleanup(_*_ , _operator =''_, _properties =None_)¶

    

Remove outdated operator properties from presets that may cause problems

Parameters:

    

  * **operator** (_string_ _,__(__optional_ _,__never None_ _)_) – operator

  * **properties** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – properties

File:

    

[startup/bl_operators/presets.py:923](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L923)

bpy.ops.wm.owner_disable(_*_ , _owner_id =''_)¶

    

Disable add-on for workspace

Parameters:

    

**owner_id** (_string_ _,__(__optional_ _,__never None_ _)_) – UI Tag

File:

    

[startup/bl_operators/wm.py:2294](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2294)

bpy.ops.wm.owner_enable(_*_ , _owner_id =''_)¶

    

Enable add-on for workspace

Parameters:

    

**owner_id** (_string_ _,__(__optional_ _,__never None_ _)_) – UI Tag

File:

    

[startup/bl_operators/wm.py:2279](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2279)

bpy.ops.wm.path_open(_*_ , _filepath =''_)¶

    

Open a path in a file browser

Parameters:

    

**filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – filepath

File:

    

[startup/bl_operators/wm.py:1167](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L1167)

bpy.ops.wm.ply_export(_*_ , _filepath =''_, _check_existing =True_,
_filter_blender =False_, _filter_backup =False_, _filter_image =False_,
_filter_movie =False_, _filter_python =False_, _filter_font =False_,
_filter_sound =False_, _filter_text =False_, _filter_archive =False_,
_filter_btx =False_, _filter_collada =False_, _filter_alembic =False_,
_filter_usd =False_, _filter_obj =False_, _filter_volume =False_,
_filter_folder =True_, _filter_blenlib =False_, _filemode =8_, _display_type
=DEFAULT_, _sort_method_ , _forward_axis =Y_, _up_axis =Z_, _global_scale
=1.0_, _apply_modifiers =True_, _export_selected_objects =False_, _collection
=''_, _export_uv =True_, _export_normals =False_, _export_colors =SRGB_,
_export_attributes =True_, _export_triangulated_mesh =False_, _ascii_format
=False_, _filter_glob ='*.ply'_)¶

    

Save the scene to a PLY file

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

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

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **forward_axis** (enum in [`X`, `Y`, `Z`, `NEGATIVE_X`, `NEGATIVE_Y`, `NEGATIVE_Z`], (optional)) – 

Forward Axis

    * `X` X – Positive X axis.

    * `Y` Y – Positive Y axis.

    * `Z` Z – Positive Z axis.

    * `NEGATIVE_X` -X – Negative X axis.

    * `NEGATIVE_Y` -Y – Negative Y axis.

    * `NEGATIVE_Z` -Z – Negative Z axis.

  * **up_axis** (enum in [`X`, `Y`, `Z`, `NEGATIVE_X`, `NEGATIVE_Y`, `NEGATIVE_Z`], (optional)) – 

Up Axis

    * `X` X – Positive X axis.

    * `Y` Y – Positive Y axis.

    * `Z` Z – Positive Z axis.

    * `NEGATIVE_X` -X – Negative X axis.

    * `NEGATIVE_Y` -Y – Negative Y axis.

    * `NEGATIVE_Z` -Z – Negative Z axis.

  * **global_scale** (_float in_ _[__0.0001_ _,__10000_ _]__,__(__optional_ _)_) – Scale, Value by which to enlarge or shrink the objects with respect to the world’s origin

  * **apply_modifiers** (_boolean_ _,__(__optional_ _)_) – Apply Modifiers, Apply modifiers to exported meshes

  * **export_selected_objects** (_boolean_ _,__(__optional_ _)_) – Export Selected Objects, Export only selected objects instead of all supported objects

  * **collection** (_string_ _,__(__optional_ _,__never None_ _)_) – Source Collection, Export only objects from this collection (and its children)

  * **export_uv** (_boolean_ _,__(__optional_ _)_) – Export UVs

  * **export_normals** (_boolean_ _,__(__optional_ _)_) – Export Vertex Normals, Export specific vertex normals if available, export calculated normals otherwise

  * **export_colors** (enum in [`NONE`, `SRGB`, `LINEAR`], (optional)) – 

Export Vertex Colors, Export vertex color attributes

    * `NONE` None – Do not import/export color attributes.

    * `SRGB` sRGB – Vertex colors in the file are in sRGB color space.

    * `LINEAR` Linear – Vertex colors in the file are in linear color space.

  * **export_attributes** (_boolean_ _,__(__optional_ _)_) – Export Vertex Attributes, Export custom vertex attributes

  * **export_triangulated_mesh** (_boolean_ _,__(__optional_ _)_) – Export Triangulated Mesh, All ngons with four or more vertices will be triangulated. Meshes in the scene will not be affected. Behaves like Triangulate Modifier with ngon-method: “Beauty”, quad-method: “Shortest Diagonal”, min vertices: 4

  * **ascii_format** (_boolean_ _,__(__optional_ _)_) – ASCII Format, Export file in ASCII format, export as binary otherwise

  * **filter_glob** (_string_ _,__(__optional_ _,__never None_ _)_) – Extension Filter

bpy.ops.wm.ply_import(_*_ , _filepath =''_, _directory =''_, _files =None_,
_check_existing =False_, _filter_blender =False_, _filter_backup =False_,
_filter_image =False_, _filter_movie =False_, _filter_python =False_,
_filter_font =False_, _filter_sound =False_, _filter_text =False_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =8_, _display_type =DEFAULT_, _sort_method_ , _global_scale =1.0_,
_use_scene_unit =False_, _forward_axis =Y_, _up_axis =Z_, _merge_verts
=False_, _import_colors =SRGB_, _import_attributes =True_, _filter_glob
='*.ply'_)¶

    

Import an PLY file as an object

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Directory, Directory of the file

  * **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – Files

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

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **global_scale** (_float in_ _[__1e-06_ _,__1e+06_ _]__,__(__optional_ _)_) – Scale

  * **use_scene_unit** (_boolean_ _,__(__optional_ _)_) – Scene Unit, Apply current scene’s unit (as defined by unit scale) to imported data

  * **forward_axis** (enum in [`X`, `Y`, `Z`, `NEGATIVE_X`, `NEGATIVE_Y`, `NEGATIVE_Z`], (optional)) – 

Forward Axis

    * `X` X – Positive X axis.

    * `Y` Y – Positive Y axis.

    * `Z` Z – Positive Z axis.

    * `NEGATIVE_X` -X – Negative X axis.

    * `NEGATIVE_Y` -Y – Negative Y axis.

    * `NEGATIVE_Z` -Z – Negative Z axis.

  * **up_axis** (enum in [`X`, `Y`, `Z`, `NEGATIVE_X`, `NEGATIVE_Y`, `NEGATIVE_Z`], (optional)) – 

Up Axis

    * `X` X – Positive X axis.

    * `Y` Y – Positive Y axis.

    * `Z` Z – Positive Z axis.

    * `NEGATIVE_X` -X – Negative X axis.

    * `NEGATIVE_Y` -Y – Negative Y axis.

    * `NEGATIVE_Z` -Z – Negative Z axis.

  * **merge_verts** (_boolean_ _,__(__optional_ _)_) – Merge Vertices, Merges vertices by distance

  * **import_colors** (enum in [`NONE`, `SRGB`, `LINEAR`], (optional)) – 

Vertex Colors, Import vertex color attributes

    * `NONE` None – Do not import/export color attributes.

    * `SRGB` sRGB – Vertex colors in the file are in sRGB color space.

    * `LINEAR` Linear – Vertex colors in the file are in linear color space.

  * **import_attributes** (_boolean_ _,__(__optional_ _)_) – Vertex Attributes, Import custom vertex attributes

  * **filter_glob** (_string_ _,__(__optional_ _,__never None_ _)_) – Extension Filter

bpy.ops.wm.previews_batch_clear(_*_ , _files =None_, _directory =''_,
_filter_blender =True_, _filter_folder =True_, _use_scenes =True_,
_use_collections =True_, _use_objects =True_, _use_intern_data =True_,
_use_trusted =False_, _use_backups =True_)¶

    

Clear selected .blend file’s previews

Parameters:

    

  * **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – files

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – directory

  * **filter_blender** (_boolean_ _,__(__optional_ _)_) – filter_blender

  * **filter_folder** (_boolean_ _,__(__optional_ _)_) – filter_folder

  * **use_scenes** (_boolean_ _,__(__optional_ _)_) – Scenes, Clear scenes’ previews

  * **use_collections** (_boolean_ _,__(__optional_ _)_) – Collections, Clear collections’ previews

  * **use_objects** (_boolean_ _,__(__optional_ _)_) – Objects, Clear objects’ previews

  * **use_intern_data** (_boolean_ _,__(__optional_ _)_) – Materials & Textures, Clear ‘internal’ previews (materials, textures, images, etc.)

  * **use_trusted** (_boolean_ _,__(__optional_ _)_) – Trusted Blend Files, Enable Python evaluation for selected files

  * **use_backups** (_boolean_ _,__(__optional_ _)_) – Save Backups, Keep a backup (.blend1) version of the files when saving with cleared previews

File:

    

[startup/bl_operators/file.py:204](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/file.py#L204)

bpy.ops.wm.previews_batch_generate(_*_ , _files =None_, _directory =''_,
_filter_blender =True_, _filter_folder =True_, _use_scenes =True_,
_use_collections =True_, _use_objects =True_, _use_intern_data =True_,
_use_trusted =False_, _use_backups =True_)¶

    

Generate selected .blend file’s previews

Parameters:

    

  * **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – Collection of file paths with common `directory` root

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Root path of all files listed in `files` collection

  * **filter_blender** (_boolean_ _,__(__optional_ _)_) – Show Blender files in the File Browser

  * **filter_folder** (_boolean_ _,__(__optional_ _)_) – Show folders in the File Browser

  * **use_scenes** (_boolean_ _,__(__optional_ _)_) – Scenes, Generate scenes’ previews

  * **use_collections** (_boolean_ _,__(__optional_ _)_) – Collections, Generate collections’ previews

  * **use_objects** (_boolean_ _,__(__optional_ _)_) – Objects, Generate objects’ previews

  * **use_intern_data** (_boolean_ _,__(__optional_ _)_) – Materials & Textures, Generate ‘internal’ previews (materials, textures, images, etc.)

  * **use_trusted** (_boolean_ _,__(__optional_ _)_) – Trusted Blend Files, Enable Python evaluation for selected files

  * **use_backups** (_boolean_ _,__(__optional_ _)_) – Save Backups, Keep a backup (.blend1) version of the files when saving with generated previews

File:

    

[startup/bl_operators/file.py:95](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/file.py#L95)

bpy.ops.wm.previews_clear(_*_ , _id_type ={}_)¶

    

Clear data-block previews (only for some types like objects, materials,
textures, etc.)

Parameters:

    

**id_type** (enum set in {`ALL`, `GEOMETRY`, `SHADING`, `SCENE`, `COLLECTION`,
`OBJECT`, `MATERIAL`, `LIGHT`, `WORLD`, `TEXTURE`, `IMAGE`}, (optional)) –

Data-Block Type, Which data-block previews to clear

  * `ALL` All Types.

  * `GEOMETRY` All Geometry Types – Clear previews for scenes, collections and objects.

  * `SHADING` All Shading Types – Clear previews for materials, lights, worlds, textures and images.

  * `SCENE` Scenes.

  * `COLLECTION` Collections.

  * `OBJECT` Objects.

  * `MATERIAL` Materials.

  * `LIGHT` Lights.

  * `WORLD` Worlds.

  * `TEXTURE` Textures.

  * `IMAGE` Images.

bpy.ops.wm.previews_ensure()¶

    

Ensure data-block previews are available and up-to-date (to be saved in .blend
file, only for some types like materials, textures, etc.)

bpy.ops.wm.properties_add(_*_ , _data_path =''_)¶

    

Add your own property to the data-block

Parameters:

    

**data_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Property Edit,
Property data_path edit

File:

    

[startup/bl_operators/wm.py:2128](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2128)

bpy.ops.wm.properties_context_change(_*_ , _context =''_)¶

    

Jump to a different tab inside the properties editor

Parameters:

    

**context** (_string_ _,__(__optional_ _,__never None_ _)_) – Context

File:

    

[startup/bl_operators/wm.py:2171](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2171)

bpy.ops.wm.properties_edit(_*_ , _data_path =''_, _property_name =''_,
_property_type =FLOAT_, _is_overridable_library =False_, _description =''_,
_use_soft_limits =False_, _array_length =3_, _default_int =(0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0)_, _min_int =-10000_, _max_int =10000_, _soft_min_int =-10000_,
_soft_max_int =10000_, _step_int =1_, _default_bool =(False, False, False,
False, False, False, False, False, False, False, False, False, False, False,
False, False, False, False, False, False, False, False, False, False, False,
False, False, False, False, False, False, False)_, _default_float =(0.0, 0.0,
0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)_,
_min_float =-10000.0_, _max_float =-10000.0_, _soft_min_float =-10000.0_,
_soft_max_float =-10000.0_, _precision =3_, _step_float =0.1_, _subtype_ ,
_default_string =''_, _id_type =OBJECT_, _eval_string =''_)¶

    

Change a custom property’s type, or adjust how it is displayed in the
interface

Parameters:

    

  * **data_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Property Edit, Property data_path edit

  * **property_name** (_string_ _,__(__optional_ _,__never None_ _)_) – Property Name, Property name edit

  * **property_type** (enum in [`FLOAT`, `FLOAT_ARRAY`, `INT`, `INT_ARRAY`, `BOOL`, `BOOL_ARRAY`, `STRING`, `DATA_BLOCK`, `PYTHON`], (optional)) – 

Type

    * `FLOAT` Float – A single floating-point value.

    * `FLOAT_ARRAY` Float Array – An array of floating-point values.

    * `INT` Integer – A single integer.

    * `INT_ARRAY` Integer Array – An array of integers.

    * `BOOL` Boolean – A true or false value.

    * `BOOL_ARRAY` Boolean Array – An array of true or false values.

    * `STRING` String – A string value.

    * `DATA_BLOCK` Data-Block – A data-block value.

    * `PYTHON` Python – Edit a Python value directly, for unsupported property types.

  * **is_overridable_library** (_boolean_ _,__(__optional_ _)_) – Library Overridable, Allow the property to be overridden when the data-block is linked

  * **description** (_string_ _,__(__optional_ _,__never None_ _)_) – Description

  * **use_soft_limits** (_boolean_ _,__(__optional_ _)_) – Soft Limits, Limits the Property Value slider to a range, values outside the range must be inputted numerically

  * **array_length** (_int in_ _[__1_ _,__32_ _]__,__(__optional_ _)_) – Array Length

  * **default_int** (_int array_ _of_ _32 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Default Value

  * **min_int** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Min

  * **max_int** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Max

  * **soft_min_int** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Soft Min

  * **soft_max_int** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Soft Max

  * **step_int** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Step

  * **default_bool** (_boolean array_ _of_ _32 items_ _,__(__optional_ _)_) – Default Value

  * **default_float** (_float array_ _of_ _32 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Default Value

  * **min_float** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Min

  * **max_float** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Max

  * **soft_min_float** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Soft Min

  * **soft_max_float** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Soft Max

  * **precision** (_int in_ _[__0_ _,__8_ _]__,__(__optional_ _)_) – Precision

  * **step_float** (_float in_ _[__0.001_ _,__inf_ _]__,__(__optional_ _)_) – Step

  * **subtype** (_enum in_ _[__]__,__(__optional_ _)_) – Subtype

  * **default_string** (_string_ _,__(__optional_ _,__never None_ _)_) – Default Value

  * **id_type** (enum in [`ACTION`, `ARMATURE`, `BRUSH`, `CACHEFILE`, `CAMERA`, `COLLECTION`, `CURVE`, `CURVES`, `FONT`, `GREASEPENCIL`, `GREASEPENCIL_V3`, `IMAGE`, `KEY`, `LATTICE`, `LIBRARY`, `LIGHT`, `LIGHT_PROBE`, `LINESTYLE`, `MASK`, `MATERIAL`, `MESH`, `META`, `MOVIECLIP`, `NODETREE`, `OBJECT`, `PAINTCURVE`, `PALETTE`, `PARTICLE`, `POINTCLOUD`, `SCENE`, `SCREEN`, `SOUND`, `SPEAKER`, `TEXT`, `TEXTURE`, `VOLUME`, `WINDOWMANAGER`, `WORKSPACE`, `WORLD`], (optional)) – ID Type

  * **eval_string** (_string_ _,__(__optional_ _,__never None_ _)_) – Value, Python value for unsupported custom property types

File:

    

[startup/bl_operators/wm.py:1861](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L1861)

bpy.ops.wm.properties_edit_value(_*_ , _data_path =''_, _property_name =''_,
_eval_string =''_)¶

    

Edit the value of a custom property

Parameters:

    

  * **data_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Property Edit, Property data_path edit

  * **property_name** (_string_ _,__(__optional_ _,__never None_ _)_) – Property Name, Property name edit

  * **eval_string** (_string_ _,__(__optional_ _,__never None_ _)_) – Value, Value for custom property types that can only be edited as a Python expression

File:

    

[startup/bl_operators/wm.py:2085](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2085)

bpy.ops.wm.properties_remove(_*_ , _data_path =''_, _property_name =''_)¶

    

Internal use (edit a property data_path)

Parameters:

    

  * **data_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Property Edit, Property data_path edit

  * **property_name** (_string_ _,__(__optional_ _,__never None_ _)_) – Property Name, Property name edit

File:

    

[startup/bl_operators/wm.py:2185](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2185)

bpy.ops.wm.quit_blender()¶

    

Quit Blender

bpy.ops.wm.radial_control(_*_ , _data_path_primary =''_, _data_path_secondary
=''_, _use_secondary =''_, _rotation_path =''_, _color_path =''_,
_fill_color_path =''_, _fill_color_override_path =''_,
_fill_color_override_test_path =''_, _zoom_path =''_, _image_id =''_,
_secondary_tex =False_, _release_confirm =False_)¶

    

Set some size property (e.g. brush size) with mouse wheel

Parameters:

    

  * **data_path_primary** (_string_ _,__(__optional_ _,__never None_ _)_) – Primary Data Path, Primary path of property to be set by the radial control

  * **data_path_secondary** (_string_ _,__(__optional_ _,__never None_ _)_) – Secondary Data Path, Secondary path of property to be set by the radial control

  * **use_secondary** (_string_ _,__(__optional_ _,__never None_ _)_) – Use Secondary, Path of property to select between the primary and secondary data paths

  * **rotation_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Rotation Path, Path of property used to rotate the texture display

  * **color_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Color Path, Path of property used to set the color of the control

  * **fill_color_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Fill Color Path, Path of property used to set the fill color of the control

  * **fill_color_override_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Fill Color Override Path

  * **fill_color_override_test_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Fill Color Override Test

  * **zoom_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Zoom Path, Path of property used to set the zoom level for the control

  * **image_id** (_string_ _,__(__optional_ _,__never None_ _)_) – Image ID, Path of ID that is used to generate an image for the control

  * **secondary_tex** (_boolean_ _,__(__optional_ _)_) – Secondary Texture, Tweak brush secondary/mask texture

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm On Release, Finish operation on key release

bpy.ops.wm.read_factory_settings(_*_ , _use_factory_startup_app_template_only
=False_, _app_template ='Template'_, _use_empty =False_)¶

    

Load factory default startup file and preferences. To make changes permanent,
use “Save Startup File” and “Save Preferences”

Parameters:

    

  * **use_factory_startup_app_template_only** (_boolean_ _,__(__optional_ _)_) – Factory Startup App-Template Only

  * **use_empty** (_boolean_ _,__(__optional_ _)_) – Empty, After loading, remove everything except scenes, windows, and workspaces. This makes it possible to load the startup file with its scene configuration and window layout intact, but no objects, materials, animations, …

bpy.ops.wm.read_factory_userpref(_*_ , _use_factory_startup_app_template_only
=False_)¶

    

Load factory default preferences. To make changes to preferences permanent,
use “Save Preferences”

Parameters:

    

**use_factory_startup_app_template_only** (_boolean_ _,__(__optional_ _)_) –
Factory Startup App-Template Only

bpy.ops.wm.read_history()¶

    

Reloads history and bookmarks

bpy.ops.wm.read_homefile(_*_ , _filepath =''_, _load_ui =True_, _use_splash
=False_, _use_factory_startup =False_, _use_factory_startup_app_template_only
=False_, _app_template ='Template'_, _use_empty =False_)¶

    

Open the default file

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to an alternative start-up file

  * **load_ui** (_boolean_ _,__(__optional_ _)_) – Load UI, Load user interface setup from the .blend file

  * **use_splash** (_boolean_ _,__(__optional_ _)_) – Splash

  * **use_factory_startup** (_boolean_ _,__(__optional_ _)_) – Factory Startup, Load the default (‘factory startup’) blend file. This is independent of the normal start-up file that the user can save

  * **use_factory_startup_app_template_only** (_boolean_ _,__(__optional_ _)_) – Factory Startup App-Template Only

  * **use_empty** (_boolean_ _,__(__optional_ _)_) – Empty, After loading, remove everything except scenes, windows, and workspaces. This makes it possible to load the startup file with its scene configuration and window layout intact, but no objects, materials, animations, …

bpy.ops.wm.read_userpref()¶

    

Load last saved preferences

bpy.ops.wm.recover_auto_save(_*_ , _filepath =''_, _hide_props_region =True_,
_check_existing =False_, _filter_blender =True_, _filter_backup =False_,
_filter_image =False_, _filter_movie =False_, _filter_python =False_,
_filter_font =False_, _filter_sound =False_, _filter_text =False_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =False_, _filter_blenlib =False_,
_filemode =8_, _display_type =LIST_VERTICAL_, _sort_method_ , _use_scripts
=False_)¶

    

Open an automatically saved file to recover it

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

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **use_scripts** (_boolean_ _,__(__optional_ _)_) – Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences

bpy.ops.wm.recover_last_session(_*_ , _use_scripts =False_)¶

    

Open the last closed file (“quit.blend”)

Parameters:

    

**use_scripts** (_boolean_ _,__(__optional_ _)_) – Trusted Source, Allow
.blend file to execute scripts automatically, default available from system
preferences

bpy.ops.wm.redraw_timer(_*_ , _type =DRAW_, _iterations =10_, _time_limit
=0.0_)¶

    

Simple redraw timer to test the speed of updating the interface

Parameters:

    

  * **type** (enum in [`DRAW`, `DRAW_SWAP`, `DRAW_WIN`, `DRAW_WIN_SWAP`, `ANIM_STEP`, `ANIM_PLAY`, `UNDO`], (optional)) – 

Type

    * `DRAW` Draw Region – Draw region.

    * `DRAW_SWAP` Draw Region & Swap – Draw region and swap.

    * `DRAW_WIN` Draw Window – Draw window.

    * `DRAW_WIN_SWAP` Draw Window & Swap – Draw window and swap.

    * `ANIM_STEP` Animation Step – Animation steps.

    * `ANIM_PLAY` Animation Play – Animation playback.

    * `UNDO` Undo/Redo – Undo and redo.

  * **iterations** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Iterations, Number of times to redraw

  * **time_limit** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Time Limit, Seconds to run the test for (override iterations)

bpy.ops.wm.revert_mainfile(_*_ , _use_scripts =False_)¶

    

Reload the saved file

Parameters:

    

**use_scripts** (_boolean_ _,__(__optional_ _)_) – Trusted Source, Allow
.blend file to execute scripts automatically, default available from system
preferences

bpy.ops.wm.save_as_mainfile(_*_ , _filepath =''_, _hide_props_region =True_,
_check_existing =True_, _filter_blender =True_, _filter_backup =False_,
_filter_image =False_, _filter_movie =False_, _filter_python =False_,
_filter_font =False_, _filter_sound =False_, _filter_text =False_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =8_, _display_type =DEFAULT_, _sort_method_ , _compress =False_,
_relative_remap =True_, _copy =False_)¶

    

Save the current file in the desired location

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

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **compress** (_boolean_ _,__(__optional_ _)_) – Compress, Write compressed .blend file

  * **relative_remap** (_boolean_ _,__(__optional_ _)_) – Remap Relative, Remap relative paths when saving to a different directory

  * **copy** (_boolean_ _,__(__optional_ _)_) – Save Copy, Save a copy of the actual working state but does not make saved file active

bpy.ops.wm.save_homefile()¶

    

Make the current file the default startup file

bpy.ops.wm.save_mainfile(_*_ , _filepath =''_, _hide_props_region =True_,
_check_existing =True_, _filter_blender =True_, _filter_backup =False_,
_filter_image =False_, _filter_movie =False_, _filter_python =False_,
_filter_font =False_, _filter_sound =False_, _filter_text =False_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =8_, _display_type =DEFAULT_, _sort_method_ , _compress =False_,
_relative_remap =False_, _exit =False_, _incremental =False_)¶

    

Save the current Blender file

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

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **compress** (_boolean_ _,__(__optional_ _)_) – Compress, Write compressed .blend file

  * **relative_remap** (_boolean_ _,__(__optional_ _)_) – Remap Relative, Remap relative paths when saving to a different directory

  * **exit** (_boolean_ _,__(__optional_ _)_) – Exit, Exit Blender after saving

  * **incremental** (_boolean_ _,__(__optional_ _)_) – Incremental, Save the current Blender file with a numerically incremented name that does not overwrite any existing files

bpy.ops.wm.save_userpref()¶

    

Make the current preferences default

bpy.ops.wm.search_menu()¶

    

Pop-up a search over all menus in the current context

bpy.ops.wm.search_operator()¶

    

Pop-up a search over all available operators in current context

bpy.ops.wm.search_single_menu(_*_ , _menu_idname =''_, _initial_query =''_)¶

    

Pop-up a search for a menu in current context

Parameters:

    

  * **menu_idname** (_string_ _,__(__optional_ _,__never None_ _)_) – Menu Name, Menu to search in

  * **initial_query** (_string_ _,__(__optional_ _,__never None_ _)_) – Initial Query, Query to insert into the search box

bpy.ops.wm.set_stereo_3d(_*_ , _display_mode =ANAGLYPH_, _anaglyph_type
=RED_CYAN_, _interlace_type =ROW_INTERLEAVED_, _use_interlace_swap =False_,
_use_sidebyside_crosseyed =False_)¶

    

Toggle 3D stereo support for current window (or change the display mode)

Parameters:

    

  * **display_mode** (enum in [Stereo3D Display Items](bpy_types_enum_items/stereo3d_display_items.html#rna-enum-stereo3d-display-items), (optional)) – Display Mode

  * **anaglyph_type** (enum in [Stereo3D Anaglyph Type Items](bpy_types_enum_items/stereo3d_anaglyph_type_items.html#rna-enum-stereo3d-anaglyph-type-items), (optional)) – Anaglyph Type

  * **interlace_type** (enum in [Stereo3D Interlace Type Items](bpy_types_enum_items/stereo3d_interlace_type_items.html#rna-enum-stereo3d-interlace-type-items), (optional)) – Interlace Type

  * **use_interlace_swap** (_boolean_ _,__(__optional_ _)_) – Swap Left/Right, Swap left and right stereo channels

  * **use_sidebyside_crosseyed** (_boolean_ _,__(__optional_ _)_) – Cross-Eyed, Right eye should see left image and vice versa

bpy.ops.wm.splash()¶

    

Open the splash screen with release info

bpy.ops.wm.splash_about()¶

    

Open a window with information about Blender

bpy.ops.wm.stl_export(_*_ , _filepath =''_, _check_existing =True_,
_filter_blender =False_, _filter_backup =False_, _filter_image =False_,
_filter_movie =False_, _filter_python =False_, _filter_font =False_,
_filter_sound =False_, _filter_text =False_, _filter_archive =False_,
_filter_btx =False_, _filter_collada =False_, _filter_alembic =False_,
_filter_usd =False_, _filter_obj =False_, _filter_volume =False_,
_filter_folder =True_, _filter_blenlib =False_, _filemode =8_, _display_type
=DEFAULT_, _sort_method_ , _ascii_format =False_, _use_batch =False_,
_export_selected_objects =False_, _collection =''_, _global_scale =1.0_,
_use_scene_unit =False_, _forward_axis =Y_, _up_axis =Z_, _apply_modifiers
=True_, _filter_glob ='*.stl'_)¶

    

Save the scene to an STL file

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

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

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **ascii_format** (_boolean_ _,__(__optional_ _)_) – ASCII Format, Export file in ASCII format, export as binary otherwise

  * **use_batch** (_boolean_ _,__(__optional_ _)_) – Batch Export, Export each object to a separate file

  * **export_selected_objects** (_boolean_ _,__(__optional_ _)_) – Export Selected Objects, Export only selected objects instead of all supported objects

  * **collection** (_string_ _,__(__optional_ _,__never None_ _)_) – Source Collection, Export only objects from this collection (and its children)

  * **global_scale** (_float in_ _[__1e-06_ _,__1e+06_ _]__,__(__optional_ _)_) – Scale

  * **use_scene_unit** (_boolean_ _,__(__optional_ _)_) – Scene Unit, Apply current scene’s unit (as defined by unit scale) to exported data

  * **forward_axis** (enum in [`X`, `Y`, `Z`, `NEGATIVE_X`, `NEGATIVE_Y`, `NEGATIVE_Z`], (optional)) – 

Forward Axis

    * `X` X – Positive X axis.

    * `Y` Y – Positive Y axis.

    * `Z` Z – Positive Z axis.

    * `NEGATIVE_X` -X – Negative X axis.

    * `NEGATIVE_Y` -Y – Negative Y axis.

    * `NEGATIVE_Z` -Z – Negative Z axis.

  * **up_axis** (enum in [`X`, `Y`, `Z`, `NEGATIVE_X`, `NEGATIVE_Y`, `NEGATIVE_Z`], (optional)) – 

Up Axis

    * `X` X – Positive X axis.

    * `Y` Y – Positive Y axis.

    * `Z` Z – Positive Z axis.

    * `NEGATIVE_X` -X – Negative X axis.

    * `NEGATIVE_Y` -Y – Negative Y axis.

    * `NEGATIVE_Z` -Z – Negative Z axis.

  * **apply_modifiers** (_boolean_ _,__(__optional_ _)_) – Apply Modifiers, Apply modifiers to exported meshes

  * **filter_glob** (_string_ _,__(__optional_ _,__never None_ _)_) – Extension Filter

bpy.ops.wm.stl_import(_*_ , _filepath =''_, _directory =''_, _files =None_,
_check_existing =False_, _filter_blender =False_, _filter_backup =False_,
_filter_image =False_, _filter_movie =False_, _filter_python =False_,
_filter_font =False_, _filter_sound =False_, _filter_text =False_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =8_, _display_type =DEFAULT_, _sort_method_ , _global_scale =1.0_,
_use_scene_unit =False_, _use_facet_normal =False_, _forward_axis =Y_,
_up_axis =Z_, _use_mesh_validate =True_, _filter_glob ='*.stl'_)¶

    

Import an STL file as an object

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Directory, Directory of the file

  * **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – Files

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

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **global_scale** (_float in_ _[__1e-06_ _,__1e+06_ _]__,__(__optional_ _)_) – Scale

  * **use_scene_unit** (_boolean_ _,__(__optional_ _)_) – Scene Unit, Apply current scene’s unit (as defined by unit scale) to imported data

  * **use_facet_normal** (_boolean_ _,__(__optional_ _)_) – Facet Normals, Use (import) facet normals (note that this will still give flat shading)

  * **forward_axis** (enum in [`X`, `Y`, `Z`, `NEGATIVE_X`, `NEGATIVE_Y`, `NEGATIVE_Z`], (optional)) – 

Forward Axis

    * `X` X – Positive X axis.

    * `Y` Y – Positive Y axis.

    * `Z` Z – Positive Z axis.

    * `NEGATIVE_X` -X – Negative X axis.

    * `NEGATIVE_Y` -Y – Negative Y axis.

    * `NEGATIVE_Z` -Z – Negative Z axis.

  * **up_axis** (enum in [`X`, `Y`, `Z`, `NEGATIVE_X`, `NEGATIVE_Y`, `NEGATIVE_Z`], (optional)) – 

Up Axis

    * `X` X – Positive X axis.

    * `Y` Y – Positive Y axis.

    * `Z` Z – Positive Z axis.

    * `NEGATIVE_X` -X – Negative X axis.

    * `NEGATIVE_Y` -Y – Negative Y axis.

    * `NEGATIVE_Z` -Z – Negative Z axis.

  * **use_mesh_validate** (_boolean_ _,__(__optional_ _)_) – Validate Mesh, Ensure the data is valid (when disabled, data may be imported which causes crashes displaying or editing)

  * **filter_glob** (_string_ _,__(__optional_ _,__never None_ _)_) – Extension Filter

bpy.ops.wm.sysinfo(_*_ , _filepath =''_)¶

    

Generate system information, saved into a text file

Parameters:

    

**filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – filepath

File:

    

[startup/bl_operators/wm.py:2214](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2214)

bpy.ops.wm.tool_set_by_brush_type(_*_ , _brush_type =''_, _space_type
=EMPTY_)¶

    

Look up the most appropriate tool for the given brush type and activate that

Parameters:

    

  * **brush_type** (_string_ _,__(__optional_ _,__never None_ _)_) – Brush Type, Brush type identifier for which the most appropriate tool will be looked up

  * **space_type** (enum in [`EMPTY`, `VIEW_3D`, `IMAGE_EDITOR`, `NODE_EDITOR`, `SEQUENCE_EDITOR`, `CLIP_EDITOR`, `DOPESHEET_EDITOR`, `GRAPH_EDITOR`, `NLA_EDITOR`, `TEXT_EDITOR`, `CONSOLE`, `INFO`, `TOPBAR`, `STATUSBAR`, `OUTLINER`, `PROPERTIES`, `FILE_BROWSER`, `SPREADSHEET`, `PREFERENCES`], (optional)) – Type

File:

    

[startup/bl_operators/wm.py:2428](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2428)

bpy.ops.wm.tool_set_by_id(_*_ , _name =''_, _cycle =False_, _as_fallback
=False_, _space_type =EMPTY_)¶

    

Set the tool by name (for key-maps)

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Identifier, Identifier of the tool

  * **cycle** (_boolean_ _,__(__optional_ _)_) – Cycle, Cycle through tools in this group

  * **as_fallback** (_boolean_ _,__(__optional_ _)_) – Set Fallback, Set the fallback tool instead of the primary tool

  * **space_type** (enum in [`EMPTY`, `VIEW_3D`, `IMAGE_EDITOR`, `NODE_EDITOR`, `SEQUENCE_EDITOR`, `CLIP_EDITOR`, `DOPESHEET_EDITOR`, `GRAPH_EDITOR`, `NLA_EDITOR`, `TEXT_EDITOR`, `CONSOLE`, `INFO`, `TOPBAR`, `STATUSBAR`, `OUTLINER`, `PROPERTIES`, `FILE_BROWSER`, `SPREADSHEET`, `PREFERENCES`], (optional)) – Type

File:

    

[startup/bl_operators/wm.py:2337](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2337)

bpy.ops.wm.tool_set_by_index(_*_ , _index =0_, _cycle =False_, _expand =True_,
_as_fallback =False_, _space_type =EMPTY_)¶

    

Set the tool by index (for key-maps)

Parameters:

    

  * **index** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Index in Toolbar

  * **cycle** (_boolean_ _,__(__optional_ _)_) – Cycle, Cycle through tools in this group

  * **expand** (_boolean_ _,__(__optional_ _)_) – expand, Include tool subgroups

  * **as_fallback** (_boolean_ _,__(__optional_ _)_) – Set Fallback, Set the fallback tool instead of the primary

  * **space_type** (enum in [`EMPTY`, `VIEW_3D`, `IMAGE_EDITOR`, `NODE_EDITOR`, `SEQUENCE_EDITOR`, `CLIP_EDITOR`, `DOPESHEET_EDITOR`, `GRAPH_EDITOR`, `NLA_EDITOR`, `TEXT_EDITOR`, `CONSOLE`, `INFO`, `TOPBAR`, `STATUSBAR`, `OUTLINER`, `PROPERTIES`, `FILE_BROWSER`, `SPREADSHEET`, `PREFERENCES`], (optional)) – Type

File:

    

[startup/bl_operators/wm.py:2387](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2387)

bpy.ops.wm.toolbar()¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

File:

    

[startup/bl_operators/wm.py:2495](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2495)

bpy.ops.wm.toolbar_fallback_pie()¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

File:

    

[startup/bl_operators/wm.py:2519](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2519)

bpy.ops.wm.toolbar_prompt()¶

    

Leader key like functionality for accessing tools

File:

    

[startup/bl_operators/wm.py:2619](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2619)

bpy.ops.wm.url_open(_*_ , _url =''_)¶

    

Open a website in the web browser

Parameters:

    

**url** (_string_ _,__(__optional_ _,__never None_ _)_) – URL, URL to open

File:

    

[startup/bl_operators/wm.py:1074](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L1074)

bpy.ops.wm.url_open_preset(_*_ , _type_)¶

    

Open a preset website in the web browser

Parameters:

    

**type** (_enum in_ _[__]__,__(__optional_ _)_) – Site

File:

    

[startup/bl_operators/wm.py:1144](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L1144)

bpy.ops.wm.usd_export(_*_ , _filepath =''_, _check_existing =True_,
_filter_blender =False_, _filter_backup =False_, _filter_image =False_,
_filter_movie =False_, _filter_python =False_, _filter_font =False_,
_filter_sound =False_, _filter_text =False_, _filter_archive =False_,
_filter_btx =False_, _filter_collada =False_, _filter_alembic =False_,
_filter_usd =True_, _filter_obj =False_, _filter_volume =False_,
_filter_folder =True_, _filter_blenlib =False_, _filemode =8_, _display_type
=DEFAULT_, _sort_method_ , _filter_glob ='*.usd'_, _selected_objects_only
=False_, _visible_objects_only =True_, _collection =''_, _export_animation
=False_, _export_hair =False_, _export_uvmaps =True_, _rename_uvmaps =True_,
_export_mesh_colors =True_, _export_normals =True_, _export_materials =True_,
_export_subdivision =BEST_MATCH_, _export_armatures =True_, _only_deform_bones
=False_, _export_shapekeys =True_, _use_instancing =False_, _evaluation_mode
=RENDER_, _generate_preview_surface =True_, _generate_materialx_network
=False_, _convert_orientation =False_, _export_global_forward_selection
=NEGATIVE_Z_, _export_global_up_selection =Y_, _export_textures =False_,
_export_textures_mode =NEW_, _overwrite_textures =False_, _relative_paths
=True_, _xform_op_mode =TRS_, _root_prim_path ='/root'_,
_export_custom_properties =True_, _custom_properties_namespace
='userProperties'_, _author_blender_name =True_, _convert_world_material
=True_, _allow_unicode =False_, _export_meshes =True_, _export_lights =True_,
_export_cameras =True_, _export_curves =True_, _export_points =True_,
_export_volumes =True_, _triangulate_meshes =False_, _quad_method
=SHORTEST_DIAGONAL_, _ngon_method =BEAUTY_, _usdz_downscale_size =KEEP_,
_usdz_downscale_custom_size =128_, _merge_parent_xform =False_,
_convert_scene_units =METERS_, _meters_per_unit =1.0_)¶

    

Export current scene in a USD archive

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

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

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **selected_objects_only** (_boolean_ _,__(__optional_ _)_) – Selection Only, Only export selected objects. Unselected parents of selected objects are exported as empty transform

  * **visible_objects_only** (_boolean_ _,__(__optional_ _)_) – Visible Only, Only export visible objects. Invisible parents of exported objects are exported as empty transforms

  * **collection** (_string_ _,__(__optional_ _,__never None_ _)_) – Collection

  * **export_animation** (_boolean_ _,__(__optional_ _)_) – Animation, Export all frames in the render frame range, rather than only the current frame

  * **export_hair** (_boolean_ _,__(__optional_ _)_) – Hair, Export hair particle systems as USD curves

  * **export_uvmaps** (_boolean_ _,__(__optional_ _)_) – UV Maps, Include all mesh UV maps in the export

  * **rename_uvmaps** (_boolean_ _,__(__optional_ _)_) – Rename UV Maps, Rename active render UV map to “st” to match USD conventions

  * **export_mesh_colors** (_boolean_ _,__(__optional_ _)_) – Color Attributes, Include mesh color attributes in the export

  * **export_normals** (_boolean_ _,__(__optional_ _)_) – Normals, Include normals of exported meshes in the export

  * **export_materials** (_boolean_ _,__(__optional_ _)_) – Materials, Export viewport settings of materials as USD preview materials, and export material assignments as geometry subsets

  * **export_subdivision** (enum in [`IGNORE`, `TESSELLATE`, `BEST_MATCH`], (optional)) – 

Subdivision, Choose how subdivision modifiers will be mapped to the USD
subdivision scheme during export

    * `IGNORE` Ignore – Scheme = None. Export base mesh without subdivision.

    * `TESSELLATE` Tessellate – Scheme = None. Export subdivided mesh.

    * `BEST_MATCH` Best Match – Scheme = Catmull-Clark, when possible. Reverts to exporting the subdivided mesh for the Simple subdivision type.

  * **export_armatures** (_boolean_ _,__(__optional_ _)_) – Armatures, Export armatures and meshes with armature modifiers as USD skeletons and skinned meshes

  * **only_deform_bones** (_boolean_ _,__(__optional_ _)_) – Only Deform Bones, Only export deform bones and their parents

  * **export_shapekeys** (_boolean_ _,__(__optional_ _)_) – Shape Keys, Export shape keys as USD blend shapes

  * **use_instancing** (_boolean_ _,__(__optional_ _)_) – Instancing, Export instanced objects as references in USD rather than real objects

  * **evaluation_mode** (enum in [`RENDER`, `VIEWPORT`], (optional)) – 

Use Settings for, Determines visibility of objects, modifier settings, and
other areas where there are different settings for viewport and rendering

    * `RENDER` Render – Use Render settings for object visibility, modifier settings, etc.

    * `VIEWPORT` Viewport – Use Viewport settings for object visibility, modifier settings, etc.

  * **generate_preview_surface** (_boolean_ _,__(__optional_ _)_) – USD Preview Surface Network, Generate an approximate USD Preview Surface shader representation of a Principled BSDF node network

  * **generate_materialx_network** (_boolean_ _,__(__optional_ _)_) – MaterialX Network, Generate a MaterialX network representation of the materials

  * **convert_orientation** (_boolean_ _,__(__optional_ _)_) – Convert Orientation, Convert orientation axis to a different convention to match other applications

  * **export_global_forward_selection** (enum in [`X`, `Y`, `Z`, `NEGATIVE_X`, `NEGATIVE_Y`, `NEGATIVE_Z`], (optional)) – 

Forward Axis

    * `X` X – Positive X axis.

    * `Y` Y – Positive Y axis.

    * `Z` Z – Positive Z axis.

    * `NEGATIVE_X` -X – Negative X axis.

    * `NEGATIVE_Y` -Y – Negative Y axis.

    * `NEGATIVE_Z` -Z – Negative Z axis.

  * **export_global_up_selection** (enum in [`X`, `Y`, `Z`, `NEGATIVE_X`, `NEGATIVE_Y`, `NEGATIVE_Z`], (optional)) – 

Up Axis

    * `X` X – Positive X axis.

    * `Y` Y – Positive Y axis.

    * `Z` Z – Positive Z axis.

    * `NEGATIVE_X` -X – Negative X axis.

    * `NEGATIVE_Y` -Y – Negative Y axis.

    * `NEGATIVE_Z` -Z – Negative Z axis.

  * **export_textures** (_boolean_ _,__(__optional_ _)_) – Export Textures, If exporting materials, export textures referenced by material nodes to a ‘textures’ directory in the same directory as the USD file

  * **export_textures_mode** (enum in [`KEEP`, `PRESERVE`, `NEW`], (optional)) – 

Export Textures, Texture export method

    * `KEEP` Keep – Use original location of textures.

    * `PRESERVE` Preserve – Preserve file paths of textures from already imported USD files. Export remaining textures to a ‘textures’ folder next to the USD file.

    * `NEW` New Path – Export textures to a ‘textures’ folder next to the USD file.

  * **overwrite_textures** (_boolean_ _,__(__optional_ _)_) – Overwrite Textures, Overwrite existing files when exporting textures

  * **relative_paths** (_boolean_ _,__(__optional_ _)_) – Relative Paths, Use relative paths to reference external files (i.e. textures, volumes) in USD, otherwise use absolute paths

  * **xform_op_mode** (enum in [`TRS`, `TOS`, `MAT`], (optional)) – 

Xform Ops, The type of transform operators to write

    * `TRS` Translate, Rotate, Scale – Export with translate, rotate, and scale Xform operators.

    * `TOS` Translate, Orient, Scale – Export with translate, orient quaternion, and scale Xform operators.

    * `MAT` Matrix – Export matrix operator.

  * **root_prim_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Root Prim, If set, add a transform primitive with the given path to the stage as the parent of all exported data

  * **export_custom_properties** (_boolean_ _,__(__optional_ _)_) – Custom Properties, Export custom properties as USD attributes

  * **custom_properties_namespace** (_string_ _,__(__optional_ _,__never None_ _)_) – Namespace, If set, add the given namespace as a prefix to exported custom property names. This only applies to property names that do not already have a prefix (e.g., it would apply to name ‘bar’ but not ‘foo:bar’) and does not apply to blender object and data names which are always exported in the ‘userProperties:blender’ namespace

  * **author_blender_name** (_boolean_ _,__(__optional_ _)_) – Blender Names, Author USD custom attributes containing the original Blender object and object data names

  * **convert_world_material** (_boolean_ _,__(__optional_ _)_) – World Dome Light, Convert the world material to a USD dome light. Currently works for simple materials, consisting of an environment texture connected to a background shader, with an optional vector multiply of the texture color

  * **allow_unicode** (_boolean_ _,__(__optional_ _)_) – Allow Unicode, Preserve UTF-8 encoded characters when writing USD prim and property names (requires software utilizing USD 24.03 or greater when opening the resulting files)

  * **export_meshes** (_boolean_ _,__(__optional_ _)_) – Meshes, Export all meshes

  * **export_lights** (_boolean_ _,__(__optional_ _)_) – Lights, Export all lights

  * **export_cameras** (_boolean_ _,__(__optional_ _)_) – Cameras, Export all cameras

  * **export_curves** (_boolean_ _,__(__optional_ _)_) – Curves, Export all curves

  * **export_points** (_boolean_ _,__(__optional_ _)_) – Point Clouds, Export all point clouds

  * **export_volumes** (_boolean_ _,__(__optional_ _)_) – Volumes, Export all volumes

  * **triangulate_meshes** (_boolean_ _,__(__optional_ _)_) – Triangulate Meshes, Triangulate meshes during export

  * **quad_method** (enum in [Modifier Triangulate Quad Method Items](bpy_types_enum_items/modifier_triangulate_quad_method_items.html#rna-enum-modifier-triangulate-quad-method-items), (optional)) – Quad Method, Method for splitting the quads into triangles

  * **ngon_method** (enum in [Modifier Triangulate Ngon Method Items](bpy_types_enum_items/modifier_triangulate_ngon_method_items.html#rna-enum-modifier-triangulate-ngon-method-items), (optional)) – N-gon Method, Method for splitting the n-gons into triangles

  * **usdz_downscale_size** (enum in [`KEEP`, `256`, `512`, `1024`, `2048`, `4096`, `CUSTOM`], (optional)) – 

USDZ Texture Downsampling, Choose a maximum size for all exported textures

    * `KEEP` Keep – Keep all current texture sizes.

    * `256` 256 – Resize to a maximum of 256 pixels.

    * `512` 512 – Resize to a maximum of 512 pixels.

    * `1024` 1024 – Resize to a maximum of 1024 pixels.

    * `2048` 2048 – Resize to a maximum of 2048 pixels.

    * `4096` 4096 – Resize to a maximum of 4096 pixels.

    * `CUSTOM` Custom – Specify a custom size.

  * **usdz_downscale_custom_size** (_int in_ _[__64_ _,__16384_ _]__,__(__optional_ _)_) – USDZ Custom Downscale Size, Custom size for downscaling exported textures

  * **merge_parent_xform** (_boolean_ _,__(__optional_ _)_) – Merge parent Xform, Merge USD primitives with their Xform parent if possible. USD does not allow nested UsdGeomGprims, intermediary Xform prims will be defined to keep the USD file valid when encountering object hierarchies.

  * **convert_scene_units** (enum in [`METERS`, `KILOMETERS`, `CENTIMETERS`, `MILLIMETERS`, `INCHES`, `FEET`, `YARDS`, `CUSTOM`], (optional)) – 

Units, Set the USD Stage meters per unit to the chosen measurement, or a
custom value

    * `METERS` Meters – Scene meters per unit to 1.0.

    * `KILOMETERS` Kilometers – Scene meters per unit to 1000.0.

    * `CENTIMETERS` Centimeters – Scene meters per unit to 0.01.

    * `MILLIMETERS` Millimeters – Scene meters per unit to 0.001.

    * `INCHES` Inches – Scene meters per unit to 0.0254.

    * `FEET` Feet – Scene meters per unit to 0.3048.

    * `YARDS` Yards – Scene meters per unit to 0.9144.

    * `CUSTOM` Custom – Specify a custom scene meters per unit value.

  * **meters_per_unit** (_float in_ _[__0.0001_ _,__1000_ _]__,__(__optional_ _)_) – Meters Per Unit, Custom value for meters per unit in the USD Stage

bpy.ops.wm.usd_import(_*_ , _filepath =''_, _check_existing =False_,
_filter_blender =False_, _filter_backup =False_, _filter_image =False_,
_filter_movie =False_, _filter_python =False_, _filter_font =False_,
_filter_sound =False_, _filter_text =False_, _filter_archive =False_,
_filter_btx =False_, _filter_collada =False_, _filter_alembic =False_,
_filter_usd =True_, _filter_obj =False_, _filter_volume =False_,
_filter_folder =True_, _filter_blenlib =False_, _filemode =8_, _relative_path
=True_, _display_type =DEFAULT_, _sort_method_ , _filter_glob ='*.usd'_,
_scale =1.0_, _set_frame_range =True_, _import_cameras =True_, _import_curves
=True_, _import_lights =True_, _import_materials =True_, _import_meshes
=True_, _import_volumes =True_, _import_shapes =True_, _import_skeletons
=True_, _import_blendshapes =True_, _import_points =True_, _import_subdiv
=False_, _support_scene_instancing =True_, _import_visible_only =True_,
_create_collection =False_, _read_mesh_uvs =True_, _read_mesh_colors =True_,
_read_mesh_attributes =True_, _prim_path_mask =''_, _import_guide =False_,
_import_proxy =False_, _import_render =True_, _import_all_materials =False_,
_import_usd_preview =True_, _set_material_blend =True_, _light_intensity_scale
=1.0_, _mtl_purpose =MTL_FULL_, _mtl_name_collision_mode =MAKE_UNIQUE_,
_import_textures_mode =IMPORT_PACK_, _import_textures_dir ='//textures/'_,
_tex_name_collision_mode =USE_EXISTING_, _attr_import_mode =ALL_,
_validate_meshes =False_, _create_world_material =True_, _import_defined_only
=True_, _merge_parent_xform =True_, _apply_unit_conversion_scale =True_)¶

    

Import USD stage into current scene

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

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

  * **scale** (_float in_ _[__0.0001_ _,__1000_ _]__,__(__optional_ _)_) – Scale, Value by which to enlarge or shrink the objects with respect to the world’s origin

  * **set_frame_range** (_boolean_ _,__(__optional_ _)_) – Set Frame Range, Update the scene’s start and end frame to match those of the USD archive

  * **import_cameras** (_boolean_ _,__(__optional_ _)_) – Cameras

  * **import_curves** (_boolean_ _,__(__optional_ _)_) – Curves

  * **import_lights** (_boolean_ _,__(__optional_ _)_) – Lights

  * **import_materials** (_boolean_ _,__(__optional_ _)_) – Materials

  * **import_meshes** (_boolean_ _,__(__optional_ _)_) – Meshes

  * **import_volumes** (_boolean_ _,__(__optional_ _)_) – Volumes

  * **import_shapes** (_boolean_ _,__(__optional_ _)_) – USD Shapes

  * **import_skeletons** (_boolean_ _,__(__optional_ _)_) – Armatures

  * **import_blendshapes** (_boolean_ _,__(__optional_ _)_) – Shape Keys

  * **import_points** (_boolean_ _,__(__optional_ _)_) – Point Clouds

  * **import_subdiv** (_boolean_ _,__(__optional_ _)_) – Import Subdivision Scheme, Create subdivision surface modifiers based on the USD SubdivisionScheme attribute

  * **support_scene_instancing** (_boolean_ _,__(__optional_ _)_) – Scene Instancing, Import USD scene graph instances as collection instances

  * **import_visible_only** (_boolean_ _,__(__optional_ _)_) – Visible Primitives Only, Do not import invisible USD primitives. Only applies to primitives with a non-animated visibility attribute. Primitives with animated visibility will always be imported

  * **create_collection** (_boolean_ _,__(__optional_ _)_) – Create Collection, Add all imported objects to a new collection

  * **read_mesh_uvs** (_boolean_ _,__(__optional_ _)_) – UV Coordinates, Read mesh UV coordinates

  * **read_mesh_colors** (_boolean_ _,__(__optional_ _)_) – Color Attributes, Read mesh color attributes

  * **read_mesh_attributes** (_boolean_ _,__(__optional_ _)_) – Mesh Attributes, Read USD Primvars as mesh attributes

  * **prim_path_mask** (_string_ _,__(__optional_ _,__never None_ _)_) – Path Mask, Import only the primitive at the given path and its descendants. Multiple paths may be specified in a list delimited by commas or semicolons

  * **import_guide** (_boolean_ _,__(__optional_ _)_) – Guide, Import guide geometry

  * **import_proxy** (_boolean_ _,__(__optional_ _)_) – Proxy, Import proxy geometry

  * **import_render** (_boolean_ _,__(__optional_ _)_) – Render, Import final render geometry

  * **import_all_materials** (_boolean_ _,__(__optional_ _)_) – Import All Materials, Also import materials that are not used by any geometry. Note that when this option is false, materials referenced by geometry will still be imported

  * **import_usd_preview** (_boolean_ _,__(__optional_ _)_) – Import USD Preview, Convert UsdPreviewSurface shaders to Principled BSDF shader networks

  * **set_material_blend** (_boolean_ _,__(__optional_ _)_) – Set Material Blend, If the Import USD Preview option is enabled, the material blend method will automatically be set based on the shader’s opacity and opacityThreshold inputs

  * **light_intensity_scale** (_float in_ _[__0.0001_ _,__10000_ _]__,__(__optional_ _)_) – Light Intensity Scale, Scale for the intensity of imported lights

  * **mtl_purpose** (enum in [`MTL_ALL_PURPOSE`, `MTL_PREVIEW`, `MTL_FULL`], (optional)) – 

Material Purpose, Attempt to import materials with the given purpose. If no
material with this purpose is bound to the primitive, fall back on loading any
other bound material

    * `MTL_ALL_PURPOSE` All Purpose – Attempt to import ‘allPurpose’ materials..

    * `MTL_PREVIEW` Preview – Attempt to import ‘preview’ materials. Load ‘allPurpose’ materials as a fallback.

    * `MTL_FULL` Full – Attempt to import ‘full’ materials. Load ‘allPurpose’ or ‘preview’ materials, in that order, as a fallback.

  * **mtl_name_collision_mode** (enum in [`MAKE_UNIQUE`, `REFERENCE_EXISTING`], (optional)) – 

Material Name Collision, Behavior when the name of an imported material
conflicts with an existing material

    * `MAKE_UNIQUE` Make Unique – Import each USD material as a unique Blender material.

    * `REFERENCE_EXISTING` Reference Existing – If a material with the same name already exists, reference that instead of importing.

  * **import_textures_mode** (enum in [`IMPORT_NONE`, `IMPORT_PACK`, `IMPORT_COPY`], (optional)) – 

Import Textures, Behavior when importing textures from a USDZ archive

    * `IMPORT_NONE` None – Don’t import textures.

    * `IMPORT_PACK` Packed – Import textures as packed data.

    * `IMPORT_COPY` Copy – Copy files to textures directory.

  * **import_textures_dir** (_string_ _,__(__optional_ _,__never None_ _)_) – Textures Directory, Path to the directory where imported textures will be copied

  * **tex_name_collision_mode** (enum in [`USE_EXISTING`, `OVERWRITE`], (optional)) – 

File Name Collision, Behavior when the name of an imported texture file
conflicts with an existing file

    * `USE_EXISTING` Use Existing – If a file with the same name already exists, use that instead of copying.

    * `OVERWRITE` Overwrite – Overwrite existing files.

  * **attr_import_mode** (enum in [`NONE`, `USER`, `ALL`], (optional)) – 

Custom Properties, Behavior when importing USD attributes as Blender custom
properties

    * `NONE` None – Do not import USD custom attributes.

    * `USER` User – Import USD attributes in the ‘userProperties’ namespace as Blender custom properties. The namespace will be stripped from the property names.

    * `ALL` All Custom – Import all USD custom attributes as Blender custom properties. Namespaces will be retained in the property names.

  * **validate_meshes** (_boolean_ _,__(__optional_ _)_) – Validate Meshes, Ensure the data is valid (when disabled, data may be imported which causes crashes displaying or editing)

  * **create_world_material** (_boolean_ _,__(__optional_ _)_) – World Dome Light, Convert the first discovered USD dome light to a world background shader

  * **import_defined_only** (_boolean_ _,__(__optional_ _)_) – Defined Primitives Only, Import only defined USD primitives. When disabled this allows importing USD primitives which are not defined, such as those with an override specifier

  * **merge_parent_xform** (_boolean_ _,__(__optional_ _)_) – Merge parent Xform, Allow USD primitives to merge with their Xform parent if they are the only child in the hierarchy

  * **apply_unit_conversion_scale** (_boolean_ _,__(__optional_ _)_) – Apply Unit Conversion Scale, Scale the scene objects by the USD stage’s meters per unit value. This scaling is applied in addition to the value specified in the Scale option

bpy.ops.wm.window_close()¶

    

Close the current window

bpy.ops.wm.window_fullscreen_toggle()¶

    

Toggle the current window full-screen

bpy.ops.wm.window_new()¶

    

Create a new window

bpy.ops.wm.window_new_main()¶

    

Create a new main window with its own workspace and scene selection

bpy.ops.wm.xr_navigation_fly(_*_ , _mode =VIEWER_FORWARD_, _lock_location_z
=False_, _lock_direction =False_, _speed_frame_based =True_, _speed_min
=0.018_, _speed_max =0.054_, _speed_interpolation0 =(0.0, 0.0)_,
_speed_interpolation1 =(1.0, 1.0)_)¶

    

Move/turn relative to the VR viewer or controller

Parameters:

    

  * **mode** (enum in [`FORWARD`, `BACK`, `LEFT`, `RIGHT`, `UP`, `DOWN`, `TURNLEFT`, `TURNRIGHT`, `VIEWER_FORWARD`, `VIEWER_BACK`, `VIEWER_LEFT`, `VIEWER_RIGHT`, `CONTROLLER_FORWARD`], (optional)) – 

Mode, Fly mode

    * `FORWARD` Forward – Move along navigation forward axis.

    * `BACK` Back – Move along navigation back axis.

    * `LEFT` Left – Move along navigation left axis.

    * `RIGHT` Right – Move along navigation right axis.

    * `UP` Up – Move along navigation up axis.

    * `DOWN` Down – Move along navigation down axis.

    * `TURNLEFT` Turn Left – Turn counter-clockwise around navigation up axis.

    * `TURNRIGHT` Turn Right – Turn clockwise around navigation up axis.

    * `VIEWER_FORWARD` Viewer Forward – Move along viewer’s forward axis.

    * `VIEWER_BACK` Viewer Back – Move along viewer’s back axis.

    * `VIEWER_LEFT` Viewer Left – Move along viewer’s left axis.

    * `VIEWER_RIGHT` Viewer Right – Move along viewer’s right axis.

    * `CONTROLLER_FORWARD` Controller Forward – Move along controller’s forward axis.

  * **lock_location_z** (_boolean_ _,__(__optional_ _)_) – Lock Elevation, Prevent changes to viewer elevation

  * **lock_direction** (_boolean_ _,__(__optional_ _)_) – Lock Direction, Limit movement to viewer’s initial direction

  * **speed_frame_based** (_boolean_ _,__(__optional_ _)_) – Frame Based Speed, Apply fixed movement deltas every update

  * **speed_min** (_float in_ _[__0_ _,__1000_ _]__,__(__optional_ _)_) – Minimum Speed, Minimum move (turn) speed in meters (radians) per second or frame

  * **speed_max** (_float in_ _[__0_ _,__1000_ _]__,__(__optional_ _)_) – Maximum Speed, Maximum move (turn) speed in meters (radians) per second or frame

  * **speed_interpolation0** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 2 items in [0, 1], (optional)) – Speed Interpolation 0, First cubic spline control point between min/max speeds

  * **speed_interpolation1** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 2 items in [0, 1], (optional)) – Speed Interpolation 1, Second cubic spline control point between min/max speeds

bpy.ops.wm.xr_navigation_grab(_*_ , _lock_location =False_, _lock_location_z
=False_, _lock_rotation =False_, _lock_rotation_z =False_, _lock_scale
=False_)¶

    

Navigate the VR scene by grabbing with controllers

Parameters:

    

  * **lock_location** (_boolean_ _,__(__optional_ _)_) – Lock Location, Prevent changes to viewer location

  * **lock_location_z** (_boolean_ _,__(__optional_ _)_) – Lock Elevation, Prevent changes to viewer elevation

  * **lock_rotation** (_boolean_ _,__(__optional_ _)_) – Lock Rotation, Prevent changes to viewer rotation

  * **lock_rotation_z** (_boolean_ _,__(__optional_ _)_) – Lock Up Orientation, Prevent changes to viewer up orientation

  * **lock_scale** (_boolean_ _,__(__optional_ _)_) – Lock Scale, Prevent changes to viewer scale

bpy.ops.wm.xr_navigation_reset(_*_ , _location =True_, _rotation =True_,
_scale =True_)¶

    

Reset VR navigation deltas relative to session base pose

Parameters:

    

  * **location** (_boolean_ _,__(__optional_ _)_) – Location, Reset location deltas

  * **rotation** (_boolean_ _,__(__optional_ _)_) – Rotation, Reset rotation deltas

  * **scale** (_boolean_ _,__(__optional_ _)_) – Scale, Reset scale deltas

bpy.ops.wm.xr_navigation_teleport(_*_ , _teleport_axes =(True, True, True)_,
_interpolation =1.0_, _offset =0.0_, _selectable_only =True_, _distance
=1.70141e+38_, _from_viewer =False_, _axis =(0.0, 0.0, -1.0)_, _color =(0.35,
0.35, 1.0, 1.0)_)¶

    

Set VR viewer location to controller raycast hit location

Parameters:

    

  * **teleport_axes** (_boolean array_ _of_ _3 items_ _,__(__optional_ _)_) – Teleport Axes, Enabled teleport axes in navigation space

  * **interpolation** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Interpolation, Interpolation factor between viewer and hit locations

  * **offset** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Offset, Offset along hit normal to subtract from final location

  * **selectable_only** (_boolean_ _,__(__optional_ _)_) – Selectable Only, Only allow selectable objects to influence raycast result

  * **distance** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Maximum raycast distance

  * **from_viewer** (_boolean_ _,__(__optional_ _)_) – From Viewer, Use viewer pose as raycast origin

  * **axis** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-1, 1], (optional)) – Axis, Raycast axis in controller/viewer space

  * **color** (_float array_ _of_ _4 items in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Color, Raycast color

bpy.ops.wm.xr_session_toggle()¶

    

Open a view for use with virtual reality headsets, or close it if already
opened

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

