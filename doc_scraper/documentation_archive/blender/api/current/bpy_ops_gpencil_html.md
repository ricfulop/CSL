---
url: https://docs.blender.org/api/current/bpy.ops.gpencil.html
scraped_at: 2025-09-08T14:18:15.465768
title: Gpencil Operators¶
---

# Gpencil Operators¶

bpy.ops.gpencil.annotate(_*_ , _mode =DRAW_, _arrowstyle_start =NONE_,
_arrowstyle_end =NONE_, _use_stabilizer =False_, _stabilizer_factor =0.75_,
_stabilizer_radius =35_, _stroke =None_, _wait_for_input =True_)¶

    

Make annotations on the active data

Parameters:

    

  * **mode** (enum in [`DRAW`, `DRAW_STRAIGHT`, `DRAW_POLY`, `ERASER`], (optional)) – 

Mode, Way to interpret mouse movements

    * `DRAW` Draw Freehand – Draw freehand stroke(s).

    * `DRAW_STRAIGHT` Draw Straight Lines – Draw straight line segment(s).

    * `DRAW_POLY` Draw Poly Line – Click to place endpoints of straight line segments (connected).

    * `ERASER` Eraser – Erase Annotation strokes.

  * **arrowstyle_start** (enum in [`NONE`, `ARROW`, `ARROW_OPEN`, `ARROW_OPEN_INVERTED`, `DIAMOND`], (optional)) – 

Start Arrow Style, Stroke start style

    * `NONE` None – Don’t use any arrow/style in corner.

    * `ARROW` Arrow – Use closed arrow style.

    * `ARROW_OPEN` Open Arrow – Use open arrow style.

    * `ARROW_OPEN_INVERTED` Segment – Use perpendicular segment style.

    * `DIAMOND` Square – Use square style.

  * **arrowstyle_end** (enum in [`NONE`, `ARROW`, `ARROW_OPEN`, `ARROW_OPEN_INVERTED`, `DIAMOND`], (optional)) – 

End Arrow Style, Stroke end style

    * `NONE` None – Don’t use any arrow/style in corner.

    * `ARROW` Arrow – Use closed arrow style.

    * `ARROW_OPEN` Open Arrow – Use open arrow style.

    * `ARROW_OPEN_INVERTED` Segment – Use perpendicular segment style.

    * `DIAMOND` Square – Use square style.

  * **use_stabilizer** (_boolean_ _,__(__optional_ _)_) – Stabilize Stroke, Helper to draw smooth and clean lines. Press Shift for an invert effect (even if this option is not active)

  * **stabilizer_factor** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Stabilizer Stroke Factor, Higher values gives a smoother stroke

  * **stabilizer_radius** (_int in_ _[__0_ _,__200_ _]__,__(__optional_ _)_) – Stabilizer Stroke Radius, Minimum distance from last point before stroke continues

  * **stroke** (`bpy_prop_collection` of `OperatorStrokeElement`, (optional)) – Stroke

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input, Wait for first click instead of painting immediately

bpy.ops.gpencil.annotation_active_frame_delete()¶

    

Delete the active frame for the active Annotation Layer

bpy.ops.gpencil.annotation_add()¶

    

Add new Annotation data-block

bpy.ops.gpencil.data_unlink()¶

    

Unlink active Annotation data-block

bpy.ops.gpencil.layer_annotation_add()¶

    

Add new Annotation layer or note for the active data-block

bpy.ops.gpencil.layer_annotation_move(_*_ , _type =UP_)¶

    

Move the active Annotation layer up/down in the list

Parameters:

    

**type** (enum in [`UP`, `DOWN`], (optional)) – Type

bpy.ops.gpencil.layer_annotation_remove()¶

    

Remove active Annotation layer

bpy.ops.gpencil.tint_flip()¶

    

Switch tint colors

File:

    

[startup/bl_ui/properties_grease_pencil_common.py:709](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_ui/properties_grease_pencil_common.py#L709)

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

