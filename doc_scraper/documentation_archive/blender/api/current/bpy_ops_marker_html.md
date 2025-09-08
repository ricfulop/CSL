---
url: https://docs.blender.org/api/current/bpy.ops.marker.html
scraped_at: 2025-09-08T14:18:24.537940
title: Marker Operators¶
---

# Marker Operators¶

bpy.ops.marker.add()¶

    

Add a new time marker

bpy.ops.marker.camera_bind()¶

    

Bind the selected camera to a marker on the current frame

bpy.ops.marker.delete(_*_ , _confirm =True_)¶

    

Delete selected time marker(s)

Parameters:

    

**confirm** (_boolean_ _,__(__optional_ _)_) – Confirm, Prompt for
confirmation

bpy.ops.marker.duplicate(_*_ , _frames =0_)¶

    

Duplicate selected time marker(s)

Parameters:

    

**frames** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Frames

bpy.ops.marker.make_links_scene(_*_ , _scene_)¶

    

Copy selected markers to another scene

Parameters:

    

**scene** (_enum in_ _[__]__,__(__optional_ _)_) – Scene

bpy.ops.marker.move(_*_ , _frames =0_, _tweak =False_)¶

    

Move selected time marker(s)

Parameters:

    

  * **frames** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Frames

  * **tweak** (_boolean_ _,__(__optional_ _)_) – Tweak, Operator has been activated using a click-drag event

bpy.ops.marker.rename(_*_ , _name ='RenamedMarker'_)¶

    

Rename first selected time marker

Parameters:

    

**name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, New name for
marker

bpy.ops.marker.select(_*_ , _wait_to_deselect_others =False_, _mouse_x =0_,
_mouse_y =0_, _extend =False_, _camera =False_)¶

    

Select time marker(s)

Parameters:

    

  * **wait_to_deselect_others** (_boolean_ _,__(__optional_ _)_) – Wait to Deselect Others

  * **mouse_x** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Mouse X

  * **mouse_y** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Mouse Y

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend the selection

  * **camera** (_boolean_ _,__(__optional_ _)_) – Camera, Select the camera

bpy.ops.marker.select_all(_*_ , _action =TOGGLE_)¶

    

Change selection of all time markers

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.marker.select_box(_*_ , _xmin =0_, _xmax =0_, _ymin =0_, _ymax =0_,
_wait_for_input =True_, _mode =SET_, _tweak =False_)¶

    

Select all time markers using box selection

Parameters:

    

  * **xmin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Min

  * **xmax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Max

  * **ymin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Min

  * **ymax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Max

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

  * **mode** (enum in [`SET`, `ADD`, `SUB`], (optional)) – 

Mode

    * `SET` Set – Set a new selection.

    * `ADD` Extend – Extend existing selection.

    * `SUB` Subtract – Subtract existing selection.

  * **tweak** (_boolean_ _,__(__optional_ _)_) – Tweak, Operator has been activated using a click-drag event

bpy.ops.marker.select_leftright(_*_ , _mode =LEFT_, _extend =False_)¶

    

Select markers on and left/right of the current frame

Parameters:

    

  * **mode** (enum in [`LEFT`, `RIGHT`], (optional)) – Mode

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend Select

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

