---
url: https://docs.blender.org/api/current/bpy.ops.view2d.html
scraped_at: 2025-09-08T14:19:00.656303
title: View2D Operators¶
---

# View2D Operators¶

bpy.ops.view2d.edge_pan(_*_ , _inside_padding =1.0_, _outside_padding =0.0_,
_speed_ramp =1.0_, _max_speed =500.0_, _delay =1.0_, _zoom_influence =0.0_)¶

    

Pan the view when the mouse is held at an edge

Parameters:

    

  * **inside_padding** (_float in_ _[__0_ _,__100_ _]__,__(__optional_ _)_) – Inside Padding, Inside distance in UI units from the edge of the region within which to start panning

  * **outside_padding** (_float in_ _[__0_ _,__100_ _]__,__(__optional_ _)_) – Outside Padding, Outside distance in UI units from the edge of the region at which to stop panning

  * **speed_ramp** (_float in_ _[__0_ _,__100_ _]__,__(__optional_ _)_) – Speed Ramp, Width of the zone in UI units where speed increases with distance from the edge

  * **max_speed** (_float in_ _[__0_ _,__10000_ _]__,__(__optional_ _)_) – Max Speed, Maximum speed in UI units per second

  * **delay** (_float in_ _[__0_ _,__10_ _]__,__(__optional_ _)_) – Delay, Delay in seconds before maximum speed is reached

  * **zoom_influence** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Zoom Influence, Influence of the zoom factor on scroll speed

bpy.ops.view2d.ndof()¶

    

Use a 3D mouse device to pan/zoom the view

bpy.ops.view2d.pan(_*_ , _deltax =0_, _deltay =0_)¶

    

Pan the view

Parameters:

    

  * **deltax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Delta X

  * **deltay** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Delta Y

bpy.ops.view2d.reset()¶

    

Reset the view

bpy.ops.view2d.scroll_down(_*_ , _deltax =0_, _deltay =0_, _page =False_)¶

    

Scroll the view down

Parameters:

    

  * **deltax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Delta X

  * **deltay** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Delta Y

  * **page** (_boolean_ _,__(__optional_ _)_) – Page, Scroll down one page

bpy.ops.view2d.scroll_left(_*_ , _deltax =0_, _deltay =0_)¶

    

Scroll the view left

Parameters:

    

  * **deltax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Delta X

  * **deltay** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Delta Y

bpy.ops.view2d.scroll_right(_*_ , _deltax =0_, _deltay =0_)¶

    

Scroll the view right

Parameters:

    

  * **deltax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Delta X

  * **deltay** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Delta Y

bpy.ops.view2d.scroll_up(_*_ , _deltax =0_, _deltay =0_, _page =False_)¶

    

Scroll the view up

Parameters:

    

  * **deltax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Delta X

  * **deltay** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Delta Y

  * **page** (_boolean_ _,__(__optional_ _)_) – Page, Scroll up one page

bpy.ops.view2d.scroller_activate()¶

    

Scroll view by mouse click and drag

bpy.ops.view2d.smoothview(_*_ , _xmin =0_, _xmax =0_, _ymin =0_, _ymax =0_,
_wait_for_input =True_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

  * **xmin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Min

  * **xmax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Max

  * **ymin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Min

  * **ymax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Max

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

bpy.ops.view2d.zoom(_*_ , _deltax =0.0_, _deltay =0.0_, _use_cursor_init
=True_)¶

    

Zoom in/out the view

Parameters:

    

  * **deltax** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Delta X

  * **deltay** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Delta Y

  * **use_cursor_init** (_boolean_ _,__(__optional_ _)_) – Use Mouse Position, Allow the initial mouse position to be used

bpy.ops.view2d.zoom_border(_*_ , _xmin =0_, _xmax =0_, _ymin =0_, _ymax =0_,
_wait_for_input =True_, _zoom_out =False_)¶

    

Zoom in the view to the nearest item contained in the border

Parameters:

    

  * **xmin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Min

  * **xmax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Max

  * **ymin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Min

  * **ymax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Max

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

  * **zoom_out** (_boolean_ _,__(__optional_ _)_) – Zoom Out

bpy.ops.view2d.zoom_in(_*_ , _zoomfacx =0.0_, _zoomfacy =0.0_)¶

    

Zoom in the view

Parameters:

    

  * **zoomfacx** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Zoom Factor X

  * **zoomfacy** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Zoom Factor Y

bpy.ops.view2d.zoom_out(_*_ , _zoomfacx =0.0_, _zoomfacy =0.0_)¶

    

Zoom out the view

Parameters:

    

  * **zoomfacx** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Zoom Factor X

  * **zoomfacy** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Zoom Factor Y

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

