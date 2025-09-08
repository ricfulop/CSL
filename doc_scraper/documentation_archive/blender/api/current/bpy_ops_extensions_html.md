---
url: https://docs.blender.org/api/current/bpy.ops.extensions.html
scraped_at: 2025-09-08T14:18:09.511212
title: Extensions Operators¶
---

# Extensions Operators¶

bpy.ops.extensions.package_disable()¶

    

Turn off this extension

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:3582](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L3582)

bpy.ops.extensions.package_install(_*_ , _repo_directory =''_, _repo_index
=-1_, _pkg_id =''_, _enable_on_install =True_, _url =''_, _do_legacy_replace
=False_)¶

    

Download and install the extension

Parameters:

    

  * **repo_directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Repo Directory

  * **repo_index** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Repo Index

  * **pkg_id** (_string_ _,__(__optional_ _,__never None_ _)_) – Package ID

  * **enable_on_install** (_boolean_ _,__(__optional_ _)_) – Enable on Install, Enable after installing

  * **url** (_string_ _,__(__optional_ _,__never None_ _)_) – URL

  * **do_legacy_replace** (_boolean_ _,__(__optional_ _)_) – Do Legacy Replace

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:1500](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L1500)

bpy.ops.extensions.package_install_files(_*_ , _filter_glob ='*.zip;*.py'_,
_directory =''_, _files =None_, _filepath =''_, _repo_ , _enable_on_install
=True_, _target_ , _overwrite =True_, _url =''_)¶

    

Install extensions from files into a locally managed repository

Parameters:

    

  * **filter_glob** (_string_ _,__(__optional_ _,__never None_ _)_) – filter_glob

  * **directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Directory

  * **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – files

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – filepath

  * **repo** (_enum in_ _[__]__,__(__optional_ _)_) – User Repository, The user repository to install extensions into

  * **enable_on_install** (_boolean_ _,__(__optional_ _)_) – Enable on Install, Enable after installing

  * **target** (_enum in_ _[__]__,__(__optional_ _)_) – Legacy Target Path, Path to install legacy add-on packages to

  * **overwrite** (_boolean_ _,__(__optional_ _)_) – Legacy Overwrite, Remove existing add-ons with the same ID

  * **url** (_string_ _,__(__optional_ _,__never None_ _)_) – URL

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:1500](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L1500)

bpy.ops.extensions.package_install_marked(_*_ , _enable_on_install =True_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

**enable_on_install** (_boolean_ _,__(__optional_ _)_) – Enable on Install,
Enable after installing

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:1500](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L1500)

bpy.ops.extensions.package_mark_clear(_*_ , _pkg_id =''_, _repo_index =-1_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

  * **pkg_id** (_string_ _,__(__optional_ _,__never None_ _)_) – Package ID

  * **repo_index** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Repo Index

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:3669](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L3669)

bpy.ops.extensions.package_mark_clear_all()¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:3716](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L3716)

bpy.ops.extensions.package_mark_set(_*_ , _pkg_id =''_, _repo_index =-1_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

  * **pkg_id** (_string_ _,__(__optional_ _,__never None_ _)_) – Package ID

  * **repo_index** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Repo Index

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:3655](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L3655)

bpy.ops.extensions.package_mark_set_all()¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:3680](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L3680)

bpy.ops.extensions.package_obsolete_marked()¶

    

Zeroes package versions, useful for development - to test upgrading

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:3773](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L3773)

bpy.ops.extensions.package_show_clear(_*_ , _pkg_id =''_, _repo_index =-1_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

  * **pkg_id** (_string_ _,__(__optional_ _,__never None_ _)_) – Package ID

  * **repo_index** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Repo Index

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:3742](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L3742)

bpy.ops.extensions.package_show_set(_*_ , _pkg_id =''_, _repo_index =-1_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

  * **pkg_id** (_string_ _,__(__optional_ _,__never None_ _)_) – Package ID

  * **repo_index** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Repo Index

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:3728](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L3728)

bpy.ops.extensions.package_show_settings(_*_ , _pkg_id =''_, _repo_index
=-1_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

  * **pkg_id** (_string_ _,__(__optional_ _,__never None_ _)_) – Package ID

  * **repo_index** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Repo Index

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:3756](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L3756)

bpy.ops.extensions.package_theme_disable(_*_ , _pkg_id =''_, _repo_index
=-1_)¶

    

Turn off this theme

Parameters:

    

  * **pkg_id** (_string_ _,__(__optional_ _,__never None_ _)_) – Package ID

  * **repo_index** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Repo Index

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:3610](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L3610)

bpy.ops.extensions.package_theme_enable(_*_ , _pkg_id =''_, _repo_index =-1_)¶

    

Turn off this theme

Parameters:

    

  * **pkg_id** (_string_ _,__(__optional_ _,__never None_ _)_) – Package ID

  * **repo_index** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Repo Index

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:3595](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L3595)

bpy.ops.extensions.package_uninstall(_*_ , _repo_directory =''_, _repo_index
=-1_, _pkg_id =''_)¶

    

Disable and uninstall the extension

Parameters:

    

  * **repo_directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Repo Directory

  * **repo_index** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Repo Index

  * **pkg_id** (_string_ _,__(__optional_ _,__never None_ _)_) – Package ID

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:1500](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L1500)

bpy.ops.extensions.package_uninstall_marked()¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:1500](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L1500)

bpy.ops.extensions.package_uninstall_system()¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:3573](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L3573)

bpy.ops.extensions.package_upgrade_all(_*_ , _use_active_only =False_)¶

    

Upgrade all the extensions to their latest version for all the remote
repositories

Parameters:

    

**use_active_only** (_boolean_ _,__(__optional_ _)_) – Active Only, Only sync
the active repository

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:1500](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L1500)

bpy.ops.extensions.repo_enable_from_drop(_*_ , _repo_index =-1_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

**repo_index** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Repo
Index

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:1830](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L1830)

bpy.ops.extensions.repo_lock_all()¶

    

Lock repositories - to test locking

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:3842](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L3842)

bpy.ops.extensions.repo_refresh_all(_*_ , _use_active_only =False_)¶

    

Scan extension & legacy add-ons for changes to modules & meta-data (similar to
restarting). Any issues are reported as warnings

Parameters:

    

**use_active_only** (_boolean_ _,__(__optional_ _)_) – Active Only, Only
refresh the active repository

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:1743](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L1743)

bpy.ops.extensions.repo_sync(_*_ , _repo_directory =''_, _repo_index =-1_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

  * **repo_directory** (_string_ _,__(__optional_ _,__never None_ _)_) – Repo Directory

  * **repo_index** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Repo Index

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:1500](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L1500)

bpy.ops.extensions.repo_sync_all(_*_ , _use_active_only =False_)¶

    

Refresh the list of extensions for all the remote repositories

Parameters:

    

**use_active_only** (_boolean_ _,__(__optional_ _)_) – Active Only, Only sync
the active repository

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:1500](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L1500)

bpy.ops.extensions.repo_unlock()¶

    

Remove the repository file-system lock

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:1917](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L1917)

bpy.ops.extensions.repo_unlock_all()¶

    

Unlock repositories - to test unlocking

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:3868](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L3868)

bpy.ops.extensions.status_clear()¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:3641](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L3641)

bpy.ops.extensions.status_clear_errors()¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:3630](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L3630)

bpy.ops.extensions.userpref_allow_online()¶

    

Allow internet access. Blender may access configured online extension
repositories. Installed third party add-ons may access the internet for their
own functionality

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:3993](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L3993)

bpy.ops.extensions.userpref_allow_online_popup()¶

    

Allow internet access. Blender may access configured online extension
repositories. Installed third party add-ons may access the internet for their
own functionality

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:4007](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L4007)

bpy.ops.extensions.userpref_show_for_update()¶

    

Open extensions preferences

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:3933](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L3933)

bpy.ops.extensions.userpref_show_online()¶

    

Show system preferences “Network” panel to allow online access

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:3973](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L3973)

bpy.ops.extensions.userpref_tags_set(_*_ , _value =False_, _data_path =''_)¶

    

Set the value of all tags

Parameters:

    

  * **value** (_boolean_ _,__(__optional_ _)_) – Value, Enable or disable all tags

  * **data_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Data Path

File:

    

[addons_core/bl_pkg/bl_extension_ops.py:3902](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/bl_pkg/bl_extension_ops.py#L3902)

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

