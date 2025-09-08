---
url: https://docs.blender.org/api/current/bpy.ops.view3d.html
scraped_at: 2025-09-08T14:19:01.711583
title: View3D Operators¶
---

# View3D Operators¶

bpy.ops.view3d.bone_select_menu(_*_ , _name_ , _extend =False_, _deselect
=False_, _toggle =False_)¶

    

Menu bone selection

Parameters:

    

  * **name** (_enum in_ _[__]__,__(__optional_ _)_) – Bone Name

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend

  * **deselect** (_boolean_ _,__(__optional_ _)_) – Deselect

  * **toggle** (_boolean_ _,__(__optional_ _)_) – Toggle

bpy.ops.view3d.camera_background_image_add(_*_ , _filepath =''_,
_relative_path =True_, _name =''_, _session_uid =0_)¶

    

Add a new background image to the active camera

Parameters:

    

  * **filepath** (string, (optional, never None, blend relative `//` prefix supported)) – Filepath, Path to image file

  * **relative_path** (_boolean_ _,__(__optional_ _)_) – Relative Path, Select the file relative to the blend file

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the data-block to use by the operator

  * **session_uid** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

bpy.ops.view3d.camera_background_image_remove(_*_ , _index =0_)¶

    

Remove a background image from the camera

Parameters:

    

**index** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Index,
Background image index to remove

bpy.ops.view3d.camera_to_view()¶

    

Set camera view to active view

bpy.ops.view3d.camera_to_view_selected()¶

    

Move the camera so selected objects are framed

bpy.ops.view3d.clear_render_border()¶

    

Clear the boundaries of the border render and disable border render

bpy.ops.view3d.clip_border(_*_ , _xmin =0_, _xmax =0_, _ymin =0_, _ymax =0_,
_wait_for_input =True_)¶

    

Set the view clipping region

Parameters:

    

  * **xmin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Min

  * **xmax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Max

  * **ymin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Min

  * **ymax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Max

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

bpy.ops.view3d.copybuffer()¶

    

Copy the selected objects to the internal clipboard

bpy.ops.view3d.cursor3d(_*_ , _use_depth =True_, _orientation =VIEW_)¶

    

Set the location of the 3D cursor

Parameters:

    

  * **use_depth** (_boolean_ _,__(__optional_ _)_) – Surface Project, Project onto the surface

  * **orientation** (enum in [`NONE`, `VIEW`, `XFORM`, `GEOM`], (optional)) – 

Orientation, Preset viewpoint to use

    * `NONE` None – Leave orientation unchanged.

    * `VIEW` View – Orient to the viewport.

    * `XFORM` Transform – Orient to the current transform setting.

    * `GEOM` Geometry – Match the surface normal.

bpy.ops.view3d.dolly(_*_ , _mx =0_, _my =0_, _delta =0_, _use_cursor_init
=True_)¶

    

Dolly in/out in the view

Parameters:

    

  * **mx** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Region Position X

  * **my** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Region Position Y

  * **delta** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Delta

  * **use_cursor_init** (_boolean_ _,__(__optional_ _)_) – Use Mouse Position, Allow the initial mouse position to be used

bpy.ops.view3d.drop_world(_*_ , _name =''_, _session_uid =0_)¶

    

Drop a world into the scene

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the data-block to use by the operator

  * **session_uid** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

bpy.ops.view3d.edit_mesh_extrude_individual_move()¶

    

Extrude each individual face separately along local normals

File:

    

[startup/bl_operators/view3d.py:30](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/view3d.py#L30)

bpy.ops.view3d.edit_mesh_extrude_manifold_normal()¶

    

Extrude manifold region along normals

File:

    

[startup/bl_operators/view3d.py:198](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/view3d.py#L198)

bpy.ops.view3d.edit_mesh_extrude_move_normal(_*_ , _dissolve_and_intersect
=False_)¶

    

Extrude region together along the average normal

Parameters:

    

**dissolve_and_intersect** (_boolean_ _,__(__optional_ _)_) –
dissolve_and_intersect, Dissolves adjacent faces and intersects new geometry

File:

    

[startup/bl_operators/view3d.py:166](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/view3d.py#L166)

bpy.ops.view3d.edit_mesh_extrude_move_shrink_fatten()¶

    

Extrude region together along local normals

File:

    

[startup/bl_operators/view3d.py:182](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/view3d.py#L182)

bpy.ops.view3d.fly()¶

    

Interactively fly around the scene

bpy.ops.view3d.interactive_add(_*_ , _primitive_type =CUBE_,
_plane_origin_base =EDGE_, _plane_origin_depth =EDGE_, _plane_aspect_base
=FREE_, _plane_aspect_depth =FREE_, _wait_for_input =True_)¶

    

Interactively add an object

Parameters:

    

  * **primitive_type** (enum in [`CUBE`, `CYLINDER`, `CONE`, `SPHERE_UV`, `SPHERE_ICO`], (optional)) – Primitive

  * **plane_origin_base** (enum in [`EDGE`, `CENTER`], (optional)) – 

Origin, The initial position for placement

    * `EDGE` Edge – Start placing the edge position.

    * `CENTER` Center – Start placing the center position.

  * **plane_origin_depth** (enum in [`EDGE`, `CENTER`], (optional)) – 

Origin, The initial position for placement

    * `EDGE` Edge – Start placing the edge position.

    * `CENTER` Center – Start placing the center position.

  * **plane_aspect_base** (enum in [`FREE`, `FIXED`], (optional)) – 

Aspect, The initial aspect setting

    * `FREE` Free – Use an unconstrained aspect.

    * `FIXED` Fixed – Use a fixed 1:1 aspect.

  * **plane_aspect_depth** (enum in [`FREE`, `FIXED`], (optional)) – 

Aspect, The initial aspect setting

    * `FREE` Free – Use an unconstrained aspect.

    * `FIXED` Fixed – Use a fixed 1:1 aspect.

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

bpy.ops.view3d.localview(_*_ , _frame_selected =True_)¶

    

Toggle display of selected object(s) separately and centered in view

Parameters:

    

**frame_selected** (_boolean_ _,__(__optional_ _)_) – Frame Selected, Move the
view to frame the selected objects

bpy.ops.view3d.localview_remove_from()¶

    

Move selected objects out of local view

bpy.ops.view3d.move(_*_ , _use_cursor_init =True_)¶

    

Move the view

Parameters:

    

**use_cursor_init** (_boolean_ _,__(__optional_ _)_) – Use Mouse Position,
Allow the initial mouse position to be used

bpy.ops.view3d.navigate()¶

    

Interactively navigate around the scene (uses the mode (walk/fly) preference)

bpy.ops.view3d.ndof_all()¶

    

Pan and rotate the view with the 3D mouse

bpy.ops.view3d.ndof_orbit()¶

    

Orbit the view using the 3D mouse

bpy.ops.view3d.ndof_orbit_zoom()¶

    

Orbit and zoom the view using the 3D mouse

bpy.ops.view3d.ndof_pan()¶

    

Pan the view with the 3D mouse

bpy.ops.view3d.object_as_camera()¶

    

Set the active object as the active camera for this view or scene

bpy.ops.view3d.object_mode_pie_or_toggle()¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

bpy.ops.view3d.pastebuffer(_*_ , _autoselect =True_, _active_collection
=True_)¶

    

Paste objects from the internal clipboard

Parameters:

    

  * **autoselect** (_boolean_ _,__(__optional_ _)_) – Select, Select pasted objects

  * **active_collection** (_boolean_ _,__(__optional_ _)_) – Active Collection, Put pasted objects in the active collection

bpy.ops.view3d.render_border(_*_ , _xmin =0_, _xmax =0_, _ymin =0_, _ymax =0_,
_wait_for_input =True_)¶

    

Set the boundaries of the border render and enable border render

Parameters:

    

  * **xmin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Min

  * **xmax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Max

  * **ymin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Min

  * **ymax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Max

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

bpy.ops.view3d.rotate(_*_ , _use_cursor_init =True_)¶

    

Rotate the view

Parameters:

    

**use_cursor_init** (_boolean_ _,__(__optional_ _)_) – Use Mouse Position,
Allow the initial mouse position to be used

bpy.ops.view3d.ruler_add()¶

    

Add ruler

bpy.ops.view3d.ruler_remove()¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

bpy.ops.view3d.select(_*_ , _extend =False_, _deselect =False_, _toggle
=False_, _deselect_all =False_, _select_passthrough =False_, _center =False_,
_enumerate =False_, _object =False_, _location =(0, 0)_)¶

    

Select and activate item(s)

Parameters:

    

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection instead of deselecting everything first

  * **deselect** (_boolean_ _,__(__optional_ _)_) – Deselect, Remove from selection

  * **toggle** (_boolean_ _,__(__optional_ _)_) – Toggle Selection, Toggle the selection

  * **deselect_all** (_boolean_ _,__(__optional_ _)_) – Deselect On Nothing, Deselect all when nothing under the cursor

  * **select_passthrough** (_boolean_ _,__(__optional_ _)_) – Only Select Unselected, Ignore the select action when the element is already selected

  * **center** (_boolean_ _,__(__optional_ _)_) – Center, Use the object center when selecting, in edit mode used to extend object selection

  * **enumerate** (_boolean_ _,__(__optional_ _)_) – Enumerate, List objects under the mouse (object mode only)

  * **object** (_boolean_ _,__(__optional_ _)_) – Object, Use object selection (edit mode only)

  * **location** (_int array_ _of_ _2 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Location, Mouse location

bpy.ops.view3d.select_box(_*_ , _xmin =0_, _xmax =0_, _ymin =0_, _ymax =0_,
_wait_for_input =True_, _mode =SET_)¶

    

Select items using box selection

Parameters:

    

  * **xmin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Min

  * **xmax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Max

  * **ymin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Min

  * **ymax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Max

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

  * **mode** (enum in [`SET`, `ADD`, `SUB`, `XOR`, `AND`], (optional)) – 

Mode

    * `SET` Set – Set a new selection.

    * `ADD` Extend – Extend existing selection.

    * `SUB` Subtract – Subtract existing selection.

    * `XOR` Difference – Invert existing selection.

    * `AND` Intersect – Intersect existing selection.

bpy.ops.view3d.select_circle(_*_ , _x =0_, _y =0_, _radius =25_,
_wait_for_input =True_, _mode =SET_)¶

    

Select items using circle selection

Parameters:

    

  * **x** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X

  * **y** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y

  * **radius** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

  * **mode** (enum in [`SET`, `ADD`, `SUB`], (optional)) – 

Mode

    * `SET` Set – Set a new selection.

    * `ADD` Extend – Extend existing selection.

    * `SUB` Subtract – Subtract existing selection.

bpy.ops.view3d.select_lasso(_*_ , _path =None_, _use_smooth_stroke =False_,
_smooth_stroke_factor =0.75_, _smooth_stroke_radius =35_, _mode =SET_)¶

    

Select items using lasso selection

Parameters:

    

  * **path** (`bpy_prop_collection` of `OperatorMousePath`, (optional)) – Path

  * **use_smooth_stroke** (_boolean_ _,__(__optional_ _)_) – Stabilize Stroke, Selection lags behind mouse and follows a smoother path

  * **smooth_stroke_factor** (_float in_ _[__0.5_ _,__0.99_ _]__,__(__optional_ _)_) – Smooth Stroke Factor, Higher values gives a smoother stroke

  * **smooth_stroke_radius** (_int in_ _[__10_ _,__200_ _]__,__(__optional_ _)_) – Smooth Stroke Radius, Minimum distance from last point before selection continues

  * **mode** (enum in [`SET`, `ADD`, `SUB`, `XOR`, `AND`], (optional)) – 

Mode

    * `SET` Set – Set a new selection.

    * `ADD` Extend – Extend existing selection.

    * `SUB` Subtract – Subtract existing selection.

    * `XOR` Difference – Invert existing selection.

    * `AND` Intersect – Intersect existing selection.

bpy.ops.view3d.select_menu(_*_ , _name_ , _extend =False_, _deselect =False_,
_toggle =False_)¶

    

Menu object selection

Parameters:

    

  * **name** (_enum in_ _[__]__,__(__optional_ _)_) – Object Name

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend

  * **deselect** (_boolean_ _,__(__optional_ _)_) – Deselect

  * **toggle** (_boolean_ _,__(__optional_ _)_) – Toggle

bpy.ops.view3d.smoothview()¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

bpy.ops.view3d.snap_cursor_to_active()¶

    

Snap 3D cursor to the active item

bpy.ops.view3d.snap_cursor_to_center()¶

    

Snap 3D cursor to the world origin

bpy.ops.view3d.snap_cursor_to_grid()¶

    

Snap 3D cursor to the nearest grid division

bpy.ops.view3d.snap_cursor_to_selected()¶

    

Snap 3D cursor to the middle of the selected item(s)

bpy.ops.view3d.snap_selected_to_active()¶

    

Snap selected item(s) to the active item

bpy.ops.view3d.snap_selected_to_cursor(_*_ , _use_offset =True_, _use_rotation
=False_)¶

    

Snap selected item(s) to the 3D cursor

Parameters:

    

  * **use_offset** (_boolean_ _,__(__optional_ _)_) – Offset, If the selection should be snapped as a whole or by each object center

  * **use_rotation** (_boolean_ _,__(__optional_ _)_) – Rotation, If the selection should be rotated to match the cursor

bpy.ops.view3d.snap_selected_to_grid()¶

    

Snap selected item(s) to their nearest grid division

bpy.ops.view3d.toggle_matcap_flip()¶

    

Flip MatCap

bpy.ops.view3d.toggle_shading(_*_ , _type =WIREFRAME_)¶

    

Toggle shading type in 3D viewport

Parameters:

    

**type** (enum in [`WIREFRAME`, `SOLID`, `MATERIAL`, `RENDERED`], (optional))
–

Type, Shading type to toggle

  * `WIREFRAME` Wireframe – Toggle wireframe shading.

  * `SOLID` Solid – Toggle solid shading.

  * `MATERIAL` Material Preview – Toggle material preview shading.

  * `RENDERED` Rendered – Toggle rendered shading.

bpy.ops.view3d.toggle_xray()¶

    

Transparent scene display. Allow selecting through items

bpy.ops.view3d.transform_gizmo_set(_*_ , _extend =False_, _type ={}_)¶

    

Set the current transform gizmo

Parameters:

    

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend

  * **type** (enum set in {`TRANSLATE`, `ROTATE`, `SCALE`}, (optional)) – Type

File:

    

[startup/bl_operators/view3d.py:245](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/view3d.py#L245)

bpy.ops.view3d.view_all(_*_ , _use_all_regions =False_, _center =False_)¶

    

View all objects in scene

Parameters:

    

  * **use_all_regions** (_boolean_ _,__(__optional_ _)_) – All Regions, View selected for all regions

  * **center** (_boolean_ _,__(__optional_ _)_) – Center

bpy.ops.view3d.view_axis(_*_ , _type =LEFT_, _align_active =False_, _relative
=False_)¶

    

Use a preset viewpoint

Parameters:

    

  * **type** (enum in [`LEFT`, `RIGHT`, `BOTTOM`, `TOP`, `FRONT`, `BACK`], (optional)) – 

View, Preset viewpoint to use

    * `LEFT` Left – View from the left.

    * `RIGHT` Right – View from the right.

    * `BOTTOM` Bottom – View from the bottom.

    * `TOP` Top – View from the top.

    * `FRONT` Front – View from the front.

    * `BACK` Back – View from the back.

  * **align_active** (_boolean_ _,__(__optional_ _)_) – Align Active, Align to the active object’s axis

  * **relative** (_boolean_ _,__(__optional_ _)_) – Relative, Rotate relative to the current orientation

bpy.ops.view3d.view_camera()¶

    

Toggle the camera view

bpy.ops.view3d.view_center_camera()¶

    

Center the camera view, resizing the view to fit its bounds

bpy.ops.view3d.view_center_cursor()¶

    

Center the view so that the cursor is in the middle of the view

bpy.ops.view3d.view_center_lock()¶

    

Center the view lock offset

bpy.ops.view3d.view_center_pick()¶

    

Center the view to the Z-depth position under the mouse cursor

bpy.ops.view3d.view_lock_clear()¶

    

Clear all view locking

bpy.ops.view3d.view_lock_to_active()¶

    

Lock the view to the active object/bone

bpy.ops.view3d.view_orbit(_*_ , _angle =0.0_, _type =ORBITLEFT_)¶

    

Orbit the view

Parameters:

    

  * **angle** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Roll

  * **type** (enum in [`ORBITLEFT`, `ORBITRIGHT`, `ORBITUP`, `ORBITDOWN`], (optional)) – 

Orbit, Direction of View Orbit

    * `ORBITLEFT` Orbit Left – Orbit the view around to the left.

    * `ORBITRIGHT` Orbit Right – Orbit the view around to the right.

    * `ORBITUP` Orbit Up – Orbit the view up.

    * `ORBITDOWN` Orbit Down – Orbit the view down.

bpy.ops.view3d.view_pan(_*_ , _type =PANLEFT_)¶

    

Pan the view in a given direction

Parameters:

    

**type** (enum in [`PANLEFT`, `PANRIGHT`, `PANUP`, `PANDOWN`], (optional)) –

Pan, Direction of View Pan

  * `PANLEFT` Pan Left – Pan the view to the left.

  * `PANRIGHT` Pan Right – Pan the view to the right.

  * `PANUP` Pan Up – Pan the view up.

  * `PANDOWN` Pan Down – Pan the view down.

bpy.ops.view3d.view_persportho()¶

    

Switch the current view from perspective/orthographic projection

bpy.ops.view3d.view_roll(_*_ , _angle =0.0_, _type =ANGLE_)¶

    

Roll the view

Parameters:

    

  * **angle** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Roll

  * **type** (enum in [`ANGLE`, `LEFT`, `RIGHT`], (optional)) – 

Roll Angle Source, How roll angle is calculated

    * `ANGLE` Roll Angle – Roll the view using an angle value.

    * `LEFT` Roll Left – Roll the view around to the left.

    * `RIGHT` Roll Right – Roll the view around to the right.

bpy.ops.view3d.view_selected(_*_ , _use_all_regions =False_)¶

    

Move the view to the selection center

Parameters:

    

**use_all_regions** (_boolean_ _,__(__optional_ _)_) – All Regions, View
selected for all regions

bpy.ops.view3d.walk()¶

    

Interactively walk around the scene

bpy.ops.view3d.zoom(_*_ , _mx =0_, _my =0_, _delta =0_, _use_cursor_init
=True_)¶

    

Zoom in/out in the view

Parameters:

    

  * **mx** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Region Position X

  * **my** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Region Position Y

  * **delta** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Delta

  * **use_cursor_init** (_boolean_ _,__(__optional_ _)_) – Use Mouse Position, Allow the initial mouse position to be used

bpy.ops.view3d.zoom_border(_*_ , _xmin =0_, _xmax =0_, _ymin =0_, _ymax =0_,
_wait_for_input =True_, _zoom_out =False_)¶

    

Zoom in the view to the nearest object contained in the border

Parameters:

    

  * **xmin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Min

  * **xmax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Max

  * **ymin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Min

  * **ymax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Max

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

  * **zoom_out** (_boolean_ _,__(__optional_ _)_) – Zoom Out

bpy.ops.view3d.zoom_camera_1_to_1()¶

    

Match the camera to 1:1 to the render output

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

