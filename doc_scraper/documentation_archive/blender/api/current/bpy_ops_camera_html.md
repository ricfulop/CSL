---
url: https://docs.blender.org/api/current/bpy.ops.camera.html
scraped_at: 2025-09-08T14:17:56.388689
title: Camera Operators¶
---

# Camera Operators¶

bpy.ops.camera.preset_add(_*_ , _name =''_, _remove_name =False_,
_remove_active =False_, _use_focal_length =False_)¶

    

Add or remove a Camera Preset

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the preset, used to make the path name

  * **remove_name** (_boolean_ _,__(__optional_ _)_) – remove_name

  * **remove_active** (_boolean_ _,__(__optional_ _)_) – remove_active

  * **use_focal_length** (_boolean_ _,__(__optional_ _)_) – Include Focal Length, Include focal length into the preset

File:

    

[startup/bl_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.camera.safe_areas_preset_add(_*_ , _name =''_, _remove_name =False_,
_remove_active =False_)¶

    

Add or remove a Safe Areas Preset

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the preset, used to make the path name

  * **remove_name** (_boolean_ _,__(__optional_ _)_) – remove_name

  * **remove_active** (_boolean_ _,__(__optional_ _)_) – remove_active

File:

    

[startup/bl_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

