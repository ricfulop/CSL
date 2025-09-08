---
url: https://docs.blender.org/api/current/bpy.ops.export_anim.html
scraped_at: 2025-09-08T14:18:07.479669
title: Export Anim Operators¶
---

# Export Anim Operators¶

bpy.ops.export_anim.bvh(_*_ , _filepath =''_, _check_existing =True_,
_filter_glob ='*.bvh'_, _global_scale =1.0_, _frame_start =0_, _frame_end =0_,
_rotate_mode =NATIVE_, _root_transform_only =False_)¶

    

Save a BVH motion capture file from an armature

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Filepath used for exporting the file

  * **check_existing** (_boolean_ _,__(__optional_ _)_) – Check Existing, Check and warn on overwriting existing files

  * **filter_glob** (_string_ _,__(__optional_ _,__never None_ _)_) – filter_glob

  * **global_scale** (_float in_ _[__0.0001_ _,__1e+06_ _]__,__(__optional_ _)_) – Scale, Scale the BVH by this value

  * **frame_start** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Start Frame, Starting frame to export

  * **frame_end** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – End Frame, End frame to export

  * **rotate_mode** (enum in [`NATIVE`, `XYZ`, `XZY`, `YXZ`, `YZX`, `ZXY`, `ZYX`], (optional)) – 

Rotation, Rotation conversion

    * `NATIVE` Euler (Native) – Use the rotation order defined in the BVH file.

    * `XYZ` Euler (XYZ) – Convert rotations to euler XYZ.

    * `XZY` Euler (XZY) – Convert rotations to euler XZY.

    * `YXZ` Euler (YXZ) – Convert rotations to euler YXZ.

    * `YZX` Euler (YZX) – Convert rotations to euler YZX.

    * `ZXY` Euler (ZXY) – Convert rotations to euler ZXY.

    * `ZYX` Euler (ZYX) – Convert rotations to euler ZYX.

  * **root_transform_only** (_boolean_ _,__(__optional_ _)_) – Root Translation Only, Only write out translation channels for the root bone

File:

    

[addons_core/io_anim_bvh/__init__.py:279](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/io_anim_bvh/__init__.py#L279)

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

