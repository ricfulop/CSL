---
url: https://docs.blender.org/api/current/bpy.ops.import_anim.html
scraped_at: 2025-09-08T14:18:19.504617
title: Import Anim Operators¶
---

# Import Anim Operators¶

bpy.ops.import_anim.bvh(_*_ , _filepath =''_, _filter_glob ='*.bvh'_, _target
=ARMATURE_, _global_scale =1.0_, _frame_start =1_, _use_fps_scale =False_,
_update_scene_fps =False_, _update_scene_duration =False_, _use_cyclic
=False_, _rotate_mode =NATIVE_, _axis_forward =-Z_, _axis_up =Y_)¶

    

Load a BVH motion capture file

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Filepath used for importing the file

  * **filter_glob** (_string_ _,__(__optional_ _,__never None_ _)_) – filter_glob

  * **target** (enum in [`ARMATURE`, `OBJECT`], (optional)) – Target, Import target type

  * **global_scale** (_float in_ _[__0.0001_ _,__1e+06_ _]__,__(__optional_ _)_) – Scale, Scale the BVH by this value

  * **frame_start** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Start Frame, Starting frame for the animation

  * **use_fps_scale** (_boolean_ _,__(__optional_ _)_) – Scale FPS, Scale the framerate from the BVH to the current scenes, otherwise each BVH frame maps directly to a Blender frame

  * **update_scene_fps** (_boolean_ _,__(__optional_ _)_) – Update Scene FPS, Set the scene framerate to that of the BVH file (note that this nullifies the ‘Scale FPS’ option, as the scale will be 1:1)

  * **update_scene_duration** (_boolean_ _,__(__optional_ _)_) – Update Scene Duration, Extend the scene’s duration to the BVH duration (never shortens the scene)

  * **use_cyclic** (_boolean_ _,__(__optional_ _)_) – Loop, Loop the animation playback

  * **rotate_mode** (enum in [`QUATERNION`, `NATIVE`, `XYZ`, `XZY`, `YXZ`, `YZX`, `ZXY`, `ZYX`], (optional)) – 

Rotation, Rotation conversion

    * `QUATERNION` Quaternion – Convert rotations to quaternions.

    * `NATIVE` Euler (Native) – Use the rotation order defined in the BVH file.

    * `XYZ` Euler (XYZ) – Convert rotations to euler XYZ.

    * `XZY` Euler (XZY) – Convert rotations to euler XZY.

    * `YXZ` Euler (YXZ) – Convert rotations to euler YXZ.

    * `YZX` Euler (YZX) – Convert rotations to euler YZX.

    * `ZXY` Euler (ZXY) – Convert rotations to euler ZXY.

    * `ZYX` Euler (ZYX) – Convert rotations to euler ZYX.

  * **axis_forward** (enum in [`X`, `Y`, `Z`, `-X`, `-Y`, `-Z`], (optional)) – Forward

  * **axis_up** (enum in [`X`, `Y`, `Z`, `-X`, `-Y`, `-Z`], (optional)) – Up

File:

    

[addons_core/io_anim_bvh/__init__.py:116](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/io_anim_bvh/__init__.py#L116)

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

