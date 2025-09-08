---
url: https://docs.blender.org/api/current/bpy.ops.info.html
scraped_at: 2025-09-08T14:18:22.541782
title: Info Operators¶
---

# Info Operators¶

bpy.ops.info.report_copy()¶

    

Copy selected reports to clipboard

bpy.ops.info.report_delete()¶

    

Delete selected reports

bpy.ops.info.report_replay()¶

    

Replay selected reports

bpy.ops.info.reports_display_update()¶

    

Update the display of reports in Blender UI (internal use)

bpy.ops.info.select_all(_*_ , _action =SELECT_)¶

    

Change selection of all visible reports

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.info.select_box(_*_ , _xmin =0_, _xmax =0_, _ymin =0_, _ymax =0_,
_wait_for_input =True_, _mode =SET_)¶

    

Toggle box selection

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

bpy.ops.info.select_pick(_*_ , _report_index =0_, _extend =False_)¶

    

Select reports by index

Parameters:

    

  * **report_index** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Report, Index of the report

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend report selection

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

