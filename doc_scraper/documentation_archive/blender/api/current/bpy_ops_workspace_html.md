---
url: https://docs.blender.org/api/current/bpy.ops.workspace.html
scraped_at: 2025-09-08T14:19:03.640951
title: Workspace Operators¶
---

# Workspace Operators¶

bpy.ops.workspace.add()¶

    

Add a new workspace by duplicating the current one or appending one from the
user configuration

bpy.ops.workspace.append_activate(_*_ , _idname =''_, _filepath =''_)¶

    

Append a workspace and make it the active one in the current window

Parameters:

    

  * **idname** (_string_ _,__(__optional_ _,__never None_ _)_) – Identifier, Name of the workspace to append and activate

  * **filepath** (string, (optional, never None, blend relative `//` prefix supported)) – Filepath, Path to the library

bpy.ops.workspace.delete()¶

    

Delete the active workspace

bpy.ops.workspace.duplicate()¶

    

Add a new workspace

bpy.ops.workspace.reorder_to_back()¶

    

Reorder workspace to be last in the list

bpy.ops.workspace.reorder_to_front()¶

    

Reorder workspace to be first in the list

bpy.ops.workspace.scene_pin_toggle()¶

    

Remember the last used scene for the current workspace and switch to it
whenever this workspace is activated again

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

