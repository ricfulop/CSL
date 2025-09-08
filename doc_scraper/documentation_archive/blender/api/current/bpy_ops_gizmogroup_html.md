---
url: https://docs.blender.org/api/current/bpy.ops.gizmogroup.html
scraped_at: 2025-09-08T14:18:14.516661
title: Gizmogroup Operators¶
---

# Gizmogroup Operators¶

bpy.ops.gizmogroup.gizmo_select(_*_ , _extend =False_, _deselect =False_,
_toggle =False_, _deselect_all =False_, _select_passthrough =False_)¶

    

Select the currently highlighted gizmo

Parameters:

    

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection instead of deselecting everything first

  * **deselect** (_boolean_ _,__(__optional_ _)_) – Deselect, Remove from selection

  * **toggle** (_boolean_ _,__(__optional_ _)_) – Toggle Selection, Toggle the selection

  * **deselect_all** (_boolean_ _,__(__optional_ _)_) – Deselect On Nothing, Deselect all when nothing under the cursor

  * **select_passthrough** (_boolean_ _,__(__optional_ _)_) – Only Select Unselected, Ignore the select action when the element is already selected

bpy.ops.gizmogroup.gizmo_tweak()¶

    

Tweak the active gizmo

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

