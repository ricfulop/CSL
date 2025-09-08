---
url: https://docs.blender.org/api/current/bpy.ops.uilist.html
scraped_at: 2025-09-08T14:18:58.668471
title: Uilist Operators¶
---

# Uilist Operators¶

bpy.ops.uilist.entry_add(_*_ , _list_path =''_, _active_index_path =''_)¶

    

Add an entry to the list after the current active item

Parameters:

    

  * **list_path** (_string_ _,__(__optional_ _,__never None_ _)_) – list_path

  * **active_index_path** (_string_ _,__(__optional_ _,__never None_ _)_) – active_index_path

File:

    

[startup/bl_ui/generic_ui_list.py:210](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_ui/generic_ui_list.py#L210)

bpy.ops.uilist.entry_move(_*_ , _list_path =''_, _active_index_path =''_,
_direction =UP_)¶

    

Move an entry in the list up or down

Parameters:

    

  * **list_path** (_string_ _,__(__optional_ _,__never None_ _)_) – list_path

  * **active_index_path** (_string_ _,__(__optional_ _,__never None_ _)_) – active_index_path

  * **direction** (enum in [`UP`, `DOWN`], (optional)) – 

Direction

    * `UP` UP – UP.

    * `DOWN` DOWN – DOWN.

File:

    

[startup/bl_ui/generic_ui_list.py:238](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_ui/generic_ui_list.py#L238)

bpy.ops.uilist.entry_remove(_*_ , _list_path =''_, _active_index_path =''_)¶

    

Remove the selected entry from the list

Parameters:

    

  * **list_path** (_string_ _,__(__optional_ _,__never None_ _)_) – list_path

  * **active_index_path** (_string_ _,__(__optional_ _,__never None_ _)_) – active_index_path

File:

    

[startup/bl_ui/generic_ui_list.py:193](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_ui/generic_ui_list.py#L193)

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

