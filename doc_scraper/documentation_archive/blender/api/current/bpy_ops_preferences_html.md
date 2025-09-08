---
url: https://docs.blender.org/api/current/bpy.ops.preferences.html
scraped_at: 2025-09-08T14:18:40.609123
title: Preferences Operators¶
---

# Preferences Operators¶

bpy.ops.preferences.addon_disable(_*_ , _module =''_)¶

    

Turn off this add-on

Parameters:

    

**module** (_string_ _,__(__optional_ _,__never None_ _)_) – Module, Module
name of the add-on to disable

File:

    

[startup/bl_operators/userpref.py:547](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L547)

bpy.ops.preferences.addon_enable(_*_ , _module =''_)¶

    

Turn on this add-on

Parameters:

    

**module** (_string_ _,__(__optional_ _,__never None_ _)_) – Module, Module
name of the add-on to enable

File:

    

[startup/bl_operators/userpref.py:483](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L483)

bpy.ops.preferences.addon_expand(_*_ , _module =''_)¶

    

Display information and preferences for this add-on

Parameters:

    

**module** (_string_ _,__(__optional_ _,__never None_ _)_) – Module, Module
name of the add-on to expand

File:

    

[startup/bl_operators/userpref.py:924](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L924)

bpy.ops.preferences.addon_install(_*_ , _overwrite =True_, _enable_on_install
=False_, _target_ , _filepath =''_, _filter_folder =True_, _filter_python
=True_, _filter_glob ='*.py;*.zip'_)¶

    

Install an add-on

Parameters:

    

  * **overwrite** (_boolean_ _,__(__optional_ _)_) – Overwrite, Remove existing add-ons with the same ID

  * **enable_on_install** (_boolean_ _,__(__optional_ _)_) – Enable on Install, Enable after installing

  * **target** (_enum in_ _[__]__,__(__optional_ _)_) – Target Path

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – filepath

  * **filter_folder** (_boolean_ _,__(__optional_ _)_) – Filter folders

  * **filter_python** (_boolean_ _,__(__optional_ _)_) – Filter Python

  * **filter_glob** (_string_ _,__(__optional_ _,__never None_ _)_) – filter_glob

File:

    

[startup/bl_operators/userpref.py:712](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L712)

bpy.ops.preferences.addon_refresh()¶

    

Scan add-on directories for new modules

File:

    

[startup/bl_operators/userpref.py:645](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L645)

bpy.ops.preferences.addon_remove(_*_ , _module =''_)¶

    

Delete the add-on from the file system

Parameters:

    

**module** (_string_ _,__(__optional_ _,__never None_ _)_) – Module, Module
name of the add-on to remove

File:

    

[startup/bl_operators/userpref.py:873](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L873)

bpy.ops.preferences.addon_show(_*_ , _module =''_)¶

    

Show add-on preferences

Parameters:

    

**module** (_string_ _,__(__optional_ _,__never None_ _)_) – Module, Module
name of the add-on to expand

File:

    

[startup/bl_operators/userpref.py:950](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L950)

bpy.ops.preferences.app_template_install(_*_ , _overwrite =True_, _filepath
=''_, _filter_folder =True_, _filter_glob ='*.zip'_)¶

    

Install an application template

Parameters:

    

  * **overwrite** (_boolean_ _,__(__optional_ _)_) – Overwrite, Remove existing template with the same ID

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – filepath

  * **filter_folder** (_boolean_ _,__(__optional_ _)_) – Filter folders

  * **filter_glob** (_string_ _,__(__optional_ _,__never None_ _)_) – filter_glob

File:

    

[startup/bl_operators/userpref.py:1000](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L1000)

bpy.ops.preferences.asset_library_add(_*_ , _directory =''_,
_hide_props_region =True_, _check_existing =False_, _filter_blender =False_,
_filter_backup =False_, _filter_image =False_, _filter_movie =False_,
_filter_python =False_, _filter_font =False_, _filter_sound =False_,
_filter_text =False_, _filter_archive =False_, _filter_btx =False_,
_filter_collada =False_, _filter_alembic =False_, _filter_usd =False_,
_filter_obj =False_, _filter_volume =False_, _filter_folder =True_,
_filter_blenlib =False_, _filemode =9_, _display_type =DEFAULT_,
_sort_method_)¶

    

Add a directory to be used by the Asset Browser as source of assets

Parameters:

    

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Directory, Directory of the file

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

bpy.ops.preferences.asset_library_remove(_*_ , _index =0_)¶

    

Remove a path to a .blend file, so the Asset Browser will not attempt to show
it anymore

Parameters:

    

**index** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Index

bpy.ops.preferences.associate_blend()¶

    

Use this installation for .blend files and to display thumbnails

bpy.ops.preferences.autoexec_path_add()¶

    

Add path to exclude from auto-execution

bpy.ops.preferences.autoexec_path_remove(_*_ , _index =0_)¶

    

Remove path to exclude from auto-execution

Parameters:

    

**index** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Index

bpy.ops.preferences.copy_prev()¶

    

Copy settings from previous version

File:

    

[startup/bl_operators/userpref.py:170](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L170)

bpy.ops.preferences.extension_repo_add(_*_ , _name =''_, _remote_url =''_,
_use_access_token =False_, _access_token =''_, _use_sync_on_startup =False_,
_use_custom_directory =False_, _custom_directory =''_, _type =REMOTE_)¶

    

Add a new repository used to store extensions

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Unique repository name

  * **remote_url** (_string_ _,__(__optional_ _,__never None_ _)_) – URL, Remote URL to the extension repository, the file-system may be referenced using the file URI scheme: “<file://>”

  * **use_access_token** (_boolean_ _,__(__optional_ _)_) – Requires Access Token, Repository requires an access token

  * **access_token** (_string_ _,__(__optional_ _,__never None_ _)_) – Secret, Personal access token, may be required by some repositories

  * **use_sync_on_startup** (_boolean_ _,__(__optional_ _)_) – Check for Updates on Startup, Allow Blender to check for updates upon launch

  * **use_custom_directory** (_boolean_ _,__(__optional_ _)_) – Custom Directory, Manually set the path for extensions to be stored. When disabled a user’s extensions directory is created.

  * **custom_directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Custom Directory, The local directory containing extensions

  * **type** (enum in [`REMOTE`, `LOCAL`], (optional)) – 

Type, The kind of repository to add

    * `REMOTE` Add Remote Repository – Add a repository referencing a remote repository with support for listing and updating extensions.

    * `LOCAL` Add Local Repository – Add a repository managed manually without referencing an external repository.

bpy.ops.preferences.extension_repo_remove(_*_ , _index =0_, _remove_files
=False_)¶

    

Remove an extension repository

Parameters:

    

  * **index** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Index

  * **remove_files** (_boolean_ _,__(__optional_ _)_) – Remove Files, Remove extension files when removing the repository

bpy.ops.preferences.extension_url_drop(_*_ , _url =''_)¶

    

Handle dropping an extension URL

Parameters:

    

**url** (_string_ _,__(__optional_ _,__never None_ _)_) – URL, Location of the
extension to install

bpy.ops.preferences.keyconfig_activate(_*_ , _filepath =''_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

**filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – filepath

File:

    

[startup/bl_operators/userpref.py:91](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L91)

bpy.ops.preferences.keyconfig_export(_*_ , _all =False_, _filepath =''_,
_filter_folder =True_, _filter_text =True_, _filter_python =True_)¶

    

Export key configuration to a Python script

Parameters:

    

  * **all** (_boolean_ _,__(__optional_ _)_) – All Keymaps, Write all keymaps (not just user modified)

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – filepath

  * **filter_folder** (_boolean_ _,__(__optional_ _)_) – Filter folders

  * **filter_text** (_boolean_ _,__(__optional_ _)_) – Filter text

  * **filter_python** (_boolean_ _,__(__optional_ _)_) – Filter Python

File:

    

[startup/bl_operators/userpref.py:324](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L324)

bpy.ops.preferences.keyconfig_import(_*_ , _filepath ='keymap.py'_,
_filter_folder =True_, _filter_text =True_, _filter_python =True_,
_keep_original =True_)¶

    

Import key configuration from a Python script

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – filepath

  * **filter_folder** (_boolean_ _,__(__optional_ _)_) – Filter folders

  * **filter_text** (_boolean_ _,__(__optional_ _)_) – Filter text

  * **filter_python** (_boolean_ _,__(__optional_ _)_) – Filter Python

  * **keep_original** (_boolean_ _,__(__optional_ _)_) – Keep Original, Keep original file after copying to configuration folder

File:

    

[startup/bl_operators/userpref.py:259](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L259)

bpy.ops.preferences.keyconfig_remove()¶

    

Remove key config

File:

    

[startup/bl_operators/userpref.py:463](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L463)

bpy.ops.preferences.keyconfig_test()¶

    

Test key configuration for conflicts

File:

    

[startup/bl_operators/userpref.py:194](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L194)

bpy.ops.preferences.keyitem_add()¶

    

Add key map item

File:

    

[startup/bl_operators/userpref.py:411](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L411)

bpy.ops.preferences.keyitem_remove(_*_ , _item_id =0_)¶

    

Remove key map item

Parameters:

    

**item_id** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Item
Identifier, Identifier of the item to remove

File:

    

[startup/bl_operators/userpref.py:443](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L443)

bpy.ops.preferences.keyitem_restore(_*_ , _item_id =0_)¶

    

Restore key map item

Parameters:

    

**item_id** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Item
Identifier, Identifier of the item to restore

File:

    

[startup/bl_operators/userpref.py:395](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L395)

bpy.ops.preferences.keymap_restore(_*_ , _all =False_)¶

    

Restore key map(s)

Parameters:

    

**all** (_boolean_ _,__(__optional_ _)_) – All Keymaps, Restore all keymaps to
default

File:

    

[startup/bl_operators/userpref.py:366](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L366)

bpy.ops.preferences.reset_default_theme()¶

    

Reset to the default theme colors

bpy.ops.preferences.script_directory_add(_*_ , _directory =''_, _filter_folder
=True_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – directory

  * **filter_folder** (_boolean_ _,__(__optional_ _)_) – Filter Folders

File:

    

[startup/bl_operators/userpref.py:1256](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L1256)

bpy.ops.preferences.script_directory_remove(_*_ , _index =0_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

**index** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Index, Index
of the script directory to remove

File:

    

[startup/bl_operators/userpref.py:1286](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L1286)

bpy.ops.preferences.studiolight_copy_settings(_*_ , _index =0_)¶

    

Copy Studio Light settings to the Studio Light editor

Parameters:

    

**index** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – index

File:

    

[startup/bl_operators/userpref.py:1227](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L1227)

bpy.ops.preferences.studiolight_install(_*_ , _files =None_, _directory =''_,
_filter_folder =True_, _filter_glob ='*.png;*.jpg;*.hdr;*.exr'_, _type
=MATCAP_)¶

    

Install a user defined light

Parameters:

    

  * **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – File Path

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – directory

  * **filter_folder** (_boolean_ _,__(__optional_ _)_) – Filter Folders

  * **filter_glob** (_string_ _,__(__optional_ _,__never None_ _)_) – filter_glob

  * **type** (enum in [`MATCAP`, `WORLD`, `STUDIO`], (optional)) – 

Type

    * `MATCAP` MatCap – Install custom MatCaps.

    * `WORLD` World – Install custom HDRIs.

    * `STUDIO` Studio – Install custom Studio Lights.

File:

    

[startup/bl_operators/userpref.py:1110](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L1110)

bpy.ops.preferences.studiolight_new(_*_ , _filename ='StudioLight'_)¶

    

Save custom studio light from the studio light editor settings

Parameters:

    

**filename** (_string_ _,__(__optional_ _,__never None_ _)_) – Name

File:

    

[startup/bl_operators/userpref.py:1157](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L1157)

bpy.ops.preferences.studiolight_uninstall(_*_ , _index =0_)¶

    

Delete Studio Light

Parameters:

    

**index** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – index

File:

    

[startup/bl_operators/userpref.py:1208](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L1208)

bpy.ops.preferences.theme_install(_*_ , _overwrite =True_, _filepath =''_,
_filter_folder =True_, _filter_glob ='*.xml'_)¶

    

Load and apply a Blender XML theme file

Parameters:

    

  * **overwrite** (_boolean_ _,__(__optional_ _)_) – Overwrite, Remove existing theme file if exists

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – filepath

  * **filter_folder** (_boolean_ _,__(__optional_ _)_) – Filter folders

  * **filter_glob** (_string_ _,__(__optional_ _,__never None_ _)_) – filter_glob

File:

    

[startup/bl_operators/userpref.py:598](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L598)

bpy.ops.preferences.unassociate_blend()¶

    

Remove this installation’s associations with .blend files

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

