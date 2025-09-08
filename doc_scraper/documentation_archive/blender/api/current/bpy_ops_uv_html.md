---
url: https://docs.blender.org/api/current/bpy.ops.uv.html
scraped_at: 2025-09-08T14:18:59.723996
title: Uv Operators¶
---

# Uv Operators¶

bpy.ops.uv.align(_*_ , _axis =ALIGN_AUTO_)¶

    

Aligns selected UV vertices on a line

Parameters:

    

**axis** (enum in [`ALIGN_S`, `ALIGN_T`, `ALIGN_U`, `ALIGN_AUTO`, `ALIGN_X`,
`ALIGN_Y`], (optional)) –

Axis, Axis to align UV locations on

  * `ALIGN_S` Straighten – Align UV vertices along the line defined by the endpoints.

  * `ALIGN_T` Straighten X – Align UV vertices, moving them horizontally to the line defined by the endpoints.

  * `ALIGN_U` Straighten Y – Align UV vertices, moving them vertically to the line defined by the endpoints.

  * `ALIGN_AUTO` Align Auto – Automatically choose the direction on which there is most alignment already.

  * `ALIGN_X` Align Vertically – Align UV vertices on a vertical line.

  * `ALIGN_Y` Align Horizontally – Align UV vertices on a horizontal line.

bpy.ops.uv.align_rotation(_*_ , _method =AUTO_, _axis =X_, _correct_aspect
=False_)¶

    

Align the UV island’s rotation

Parameters:

    

  * **method** (enum in [`AUTO`, `EDGE`, `GEOMETRY`], (optional)) – 

Method, Method to calculate rotation angle

    * `AUTO` Auto – Align from all edges.

    * `EDGE` Edge – Only selected edges.

    * `GEOMETRY` Geometry – Align to Geometry axis.

  * **axis** (enum in [`X`, `Y`, `Z`], (optional)) – 

Axis, Axis to align to

    * `X` X – X axis.

    * `Y` Y – Y axis.

    * `Z` Z – Z axis.

  * **correct_aspect** (_boolean_ _,__(__optional_ _)_) – Correct Aspect, Take image aspect ratio into account

File:

    

[startup/bl_operators/uvcalc_transform.py:299](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/uvcalc_transform.py#L299)

bpy.ops.uv.average_islands_scale(_*_ , _scale_uv =False_, _shear =False_)¶

    

Average the size of separate UV islands, based on their area in 3D space

Parameters:

    

  * **scale_uv** (_boolean_ _,__(__optional_ _)_) – Non-Uniform, Scale U and V independently

  * **shear** (_boolean_ _,__(__optional_ _)_) – Shear, Reduce shear within islands

bpy.ops.uv.copy()¶

    

Copy selected UV vertices

bpy.ops.uv.cube_project(_*_ , _cube_size =1.0_, _correct_aspect =True_,
_clip_to_bounds =False_, _scale_to_bounds =False_)¶

    

Project the UV vertices of the mesh over the six faces of a cube

Parameters:

    

  * **cube_size** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Cube Size, Size of the cube to project on

  * **correct_aspect** (_boolean_ _,__(__optional_ _)_) – Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account

  * **clip_to_bounds** (_boolean_ _,__(__optional_ _)_) – Clip to Bounds, Clip UV coordinates to bounds after unwrapping

  * **scale_to_bounds** (_boolean_ _,__(__optional_ _)_) – Scale to Bounds, Scale UV coordinates to bounds after unwrapping

bpy.ops.uv.cursor_set(_*_ , _location =(0.0, 0.0)_)¶

    

Set 2D cursor location

Parameters:

    

**location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector
"mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Cursor
location in normalized (0.0 to 1.0) coordinates

bpy.ops.uv.cylinder_project(_*_ , _direction =VIEW_ON_EQUATOR_, _align
=POLAR_ZX_, _pole =PINCH_, _seam =False_, _radius =1.0_, _correct_aspect
=True_, _clip_to_bounds =False_, _scale_to_bounds =False_)¶

    

Project the UV vertices of the mesh over the curved wall of a cylinder

Parameters:

    

  * **direction** (enum in [`VIEW_ON_EQUATOR`, `VIEW_ON_POLES`, `ALIGN_TO_OBJECT`], (optional)) – 

Direction, Direction of the sphere or cylinder

    * `VIEW_ON_EQUATOR` View on Equator – 3D view is on the equator.

    * `VIEW_ON_POLES` View on Poles – 3D view is on the poles.

    * `ALIGN_TO_OBJECT` Align to Object – Align according to object transform.

  * **align** (enum in [`POLAR_ZX`, `POLAR_ZY`], (optional)) – 

Align, How to determine rotation around the pole

    * `POLAR_ZX` Polar ZX – Polar 0 is X.

    * `POLAR_ZY` Polar ZY – Polar 0 is Y.

  * **pole** (enum in [`PINCH`, `FAN`], (optional)) – 

Pole, How to handle faces at the poles

    * `PINCH` Pinch – UVs are pinched at the poles.

    * `FAN` Fan – UVs are fanned at the poles.

  * **seam** (_boolean_ _,__(__optional_ _)_) – Preserve Seams, Separate projections by islands isolated by seams

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius, Radius of the sphere or cylinder

  * **correct_aspect** (_boolean_ _,__(__optional_ _)_) – Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account

  * **clip_to_bounds** (_boolean_ _,__(__optional_ _)_) – Clip to Bounds, Clip UV coordinates to bounds after unwrapping

  * **scale_to_bounds** (_boolean_ _,__(__optional_ _)_) – Scale to Bounds, Scale UV coordinates to bounds after unwrapping

bpy.ops.uv.export_layout(_*_ , _filepath =''_, _export_all =False_,
_export_tiles =NONE_, _modified =False_, _mode =PNG_, _size =(1024, 1024)_,
_opacity =0.25_, _check_existing =True_)¶

    

Export UV layout to file

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – filepath

  * **export_all** (_boolean_ _,__(__optional_ _)_) – All UVs, Export all UVs in this mesh (not just visible ones)

  * **export_tiles** (enum in [`NONE`, `UDIM`, `UV`], (optional)) – 

Export Tiles, Choose whether to export only the [0, 1] range, or all UV tiles

    * `NONE` None – Export only UVs in the [0, 1] range.

    * `UDIM` UDIM – Export tiles in the UDIM numbering scheme: 1001 + u_tile + 10*v_tile.

    * `UV` UVTILE – Export tiles in the UVTILE numbering scheme: u(u_tile + 1)_v(v_tile + 1).

  * **modified** (_boolean_ _,__(__optional_ _)_) – Modified, Exports UVs from the modified mesh

  * **mode** (enum in [`SVG`, `EPS`, `PNG`], (optional)) – 

Format, File format to export the UV layout to

    * `SVG` Scalable Vector Graphic (.svg) – Export the UV layout to a vector SVG file.

    * `EPS` Encapsulated PostScript (.eps) – Export the UV layout to a vector EPS file.

    * `PNG` PNG Image (.png) – Export the UV layout to a bitmap image.

  * **size** (_int array_ _of_ _2 items in_ _[__8_ _,__32768_ _]__,__(__optional_ _)_) – Size, Dimensions of the exported file

  * **opacity** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Fill Opacity, Set amount of opacity for exported UV layout

  * **check_existing** (_boolean_ _,__(__optional_ _)_) – check_existing

File:

    

[addons_core/io_mesh_uv_layout/__init__.py:137](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/io_mesh_uv_layout/__init__.py#L137)

bpy.ops.uv.follow_active_quads(_*_ , _mode =LENGTH_AVERAGE_)¶

    

Follow UVs from active quads along continuous face loops

Parameters:

    

**mode** (enum in [`EVEN`, `LENGTH`, `LENGTH_AVERAGE`], (optional)) –

Edge Length Mode, Method to space UV edge loops

  * `EVEN` Even – Space all UVs evenly.

  * `LENGTH` Length – Average space UVs edge length of each loop.

  * `LENGTH_AVERAGE` Length Average – Average space UVs edge length of each loop.

File:

    

[startup/bl_operators/uvcalc_follow_active.py:297](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/uvcalc_follow_active.py#L297)

bpy.ops.uv.hide(_*_ , _unselected =False_)¶

    

Hide (un)selected UV vertices

Parameters:

    

**unselected** (_boolean_ _,__(__optional_ _)_) – Unselected, Hide unselected
rather than selected

bpy.ops.uv.lightmap_pack(_*_ , _PREF_CONTEXT =SEL_FACES_, _PREF_PACK_IN_ONE
=True_, _PREF_NEW_UVLAYER =False_, _PREF_BOX_DIV =12_, _PREF_MARGIN_DIV
=0.1_)¶

    

Pack each face’s UVs into the UV bounds

Parameters:

    

  * **PREF_CONTEXT** (enum in [`SEL_FACES`, `ALL_FACES`], (optional)) – 

Selection

    * `SEL_FACES` Selected Faces – Space all UVs evenly.

    * `ALL_FACES` All Faces – Average space UVs edge length of each loop.

  * **PREF_PACK_IN_ONE** (_boolean_ _,__(__optional_ _)_) – Share Texture Space, Objects share texture space, map all objects into a single UV map

  * **PREF_NEW_UVLAYER** (_boolean_ _,__(__optional_ _)_) – New UV Map, Create a new UV map for every mesh packed

  * **PREF_BOX_DIV** (_int in_ _[__1_ _,__48_ _]__,__(__optional_ _)_) – Pack Quality, Quality of the packing. Higher values will be slower but waste less space

  * **PREF_MARGIN_DIV** (_float in_ _[__0.001_ _,__1_ _]__,__(__optional_ _)_) – Margin, Size of the margin as a division of the UV

File:

    

[startup/bl_operators/uvcalc_lightmap.py:662](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/uvcalc_lightmap.py#L662)

bpy.ops.uv.mark_seam(_*_ , _clear =False_)¶

    

Mark selected UV edges as seams

Parameters:

    

**clear** (_boolean_ _,__(__optional_ _)_) – Clear Seams, Clear instead of
marking seams

bpy.ops.uv.minimize_stretch(_*_ , _fill_holes =True_, _blend =0.0_,
_iterations =0_)¶

    

Reduce UV stretching by relaxing angles

Parameters:

    

  * **fill_holes** (_boolean_ _,__(__optional_ _)_) – Fill Holes, Virtually fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry

  * **blend** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Blend, Blend factor between stretch minimized and original

  * **iterations** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Iterations, Number of iterations to run, 0 is unlimited when run interactively

bpy.ops.uv.pack_islands(_*_ , _udim_source =CLOSEST_UDIM_, _rotate =True_,
_rotate_method =ANY_, _scale =True_, _merge_overlap =False_, _margin_method
=SCALED_, _margin =0.001_, _pin =False_, _pin_method =LOCKED_, _shape_method
=CONCAVE_)¶

    

Transform all islands so that they fill up the UV/UDIM space as much as
possible

Parameters:

    

  * **udim_source** (enum in [`CLOSEST_UDIM`, `ACTIVE_UDIM`, `ORIGINAL_AABB`], (optional)) – 

Pack to

    * `CLOSEST_UDIM` Closest UDIM – Pack islands to closest UDIM.

    * `ACTIVE_UDIM` Active UDIM – Pack islands to active UDIM image tile or UDIM grid tile where 2D cursor is located.

    * `ORIGINAL_AABB` Original bounding box – Pack to starting bounding box of islands.

  * **rotate** (_boolean_ _,__(__optional_ _)_) – Rotate, Rotate islands to improve layout

  * **rotate_method** (enum in [`ANY`, `CARDINAL`, `AXIS_ALIGNED`, `AXIS_ALIGNED_X`, `AXIS_ALIGNED_Y`], (optional)) – 

Rotation Method

    * `ANY` Any – Any angle is allowed for rotation.

    * `CARDINAL` Cardinal – Only 90 degree rotations are allowed.

    * `AXIS_ALIGNED` Axis-aligned – Rotated to a minimal rectangle, either vertical or horizontal.

    * `AXIS_ALIGNED_X` Axis-aligned (Horizontal) – Rotate islands to be aligned horizontally.

    * `AXIS_ALIGNED_Y` Axis-aligned (Vertical) – Rotate islands to be aligned vertically.

  * **scale** (_boolean_ _,__(__optional_ _)_) – Scale, Scale islands to fill unit square

  * **merge_overlap** (_boolean_ _,__(__optional_ _)_) – Merge Overlapping, Overlapping islands stick together

  * **margin_method** (enum in [`SCALED`, `ADD`, `FRACTION`], (optional)) – 

Margin Method

    * `SCALED` Scaled – Use scale of existing UVs to multiply margin.

    * `ADD` Add – Just add the margin, ignoring any UV scale.

    * `FRACTION` Fraction – Specify a precise fraction of final UV output.

  * **margin** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Margin, Space between islands

  * **pin** (_boolean_ _,__(__optional_ _)_) – Lock Pinned Islands, Constrain islands containing any pinned UV’s

  * **pin_method** (enum in [`SCALE`, `ROTATION`, `ROTATION_SCALE`, `LOCKED`], (optional)) – 

Pin Method

    * `SCALE` Scale – Pinned islands won’t rescale.

    * `ROTATION` Rotation – Pinned islands won’t rotate.

    * `ROTATION_SCALE` Rotation and Scale – Pinned islands will translate only.

    * `LOCKED` All – Pinned islands are locked in place.

  * **shape_method** (enum in [`CONCAVE`, `CONVEX`, `AABB`], (optional)) – 

Shape Method

    * `CONCAVE` Exact Shape (Concave) – Uses exact geometry.

    * `CONVEX` Boundary Shape (Convex) – Uses convex hull.

    * `AABB` Bounding Box – Uses bounding boxes.

bpy.ops.uv.paste()¶

    

Paste selected UV vertices

bpy.ops.uv.pin(_*_ , _clear =False_, _invert =False_)¶

    

Set/clear selected UV vertices as anchored between multiple unwrap operations

Parameters:

    

  * **clear** (_boolean_ _,__(__optional_ _)_) – Clear, Clear pinning for the selection instead of setting it

  * **invert** (_boolean_ _,__(__optional_ _)_) – Invert, Invert pinning for the selection instead of setting it

bpy.ops.uv.project_from_view(_*_ , _orthographic =False_, _camera_bounds
=True_, _correct_aspect =True_, _clip_to_bounds =False_, _scale_to_bounds
=False_)¶

    

Project the UV vertices of the mesh as seen in current 3D view

Parameters:

    

  * **orthographic** (_boolean_ _,__(__optional_ _)_) – Orthographic, Use orthographic projection

  * **camera_bounds** (_boolean_ _,__(__optional_ _)_) – Camera Bounds, Map UVs to the camera region taking resolution and aspect into account

  * **correct_aspect** (_boolean_ _,__(__optional_ _)_) – Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account

  * **clip_to_bounds** (_boolean_ _,__(__optional_ _)_) – Clip to Bounds, Clip UV coordinates to bounds after unwrapping

  * **scale_to_bounds** (_boolean_ _,__(__optional_ _)_) – Scale to Bounds, Scale UV coordinates to bounds after unwrapping

bpy.ops.uv.randomize_uv_transform(_*_ , _random_seed =0_, _use_loc =True_,
_loc =(0.0, 0.0)_, _use_rot =True_, _rot =0.0_, _use_scale =True_, _scale_even
=False_, _scale =(1.0, 1.0)_)¶

    

Randomize the UV island’s location, rotation, and scale

Parameters:

    

  * **random_seed** (_int in_ _[__0_ _,__10000_ _]__,__(__optional_ _)_) – Random Seed, Seed value for the random generator

  * **use_loc** (_boolean_ _,__(__optional_ _)_) – Randomize Location, Randomize the location values

  * **loc** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 2 items in [-100, 100], (optional)) – Location, Maximum distance the objects can spread over each axis

  * **use_rot** (_boolean_ _,__(__optional_ _)_) – Randomize Rotation, Randomize the rotation value

  * **rot** (_float in_ _[__-6.28319_ _,__6.28319_ _]__,__(__optional_ _)_) – Rotation, Maximum rotation

  * **use_scale** (_boolean_ _,__(__optional_ _)_) – Randomize Scale, Randomize the scale values

  * **scale_even** (_boolean_ _,__(__optional_ _)_) – Scale Even, Use the same scale value for both axes

  * **scale** (_float array_ _of_ _2 items in_ _[__-100_ _,__100_ _]__,__(__optional_ _)_) – Scale, Maximum scale randomization over each axis

File:

    

[startup/bl_operators/uvcalc_transform.py:473](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/uvcalc_transform.py#L473)

bpy.ops.uv.remove_doubles(_*_ , _threshold =0.02_, _use_unselected =False_,
_use_shared_vertex =False_)¶

    

Selected UV vertices that are within a radius of each other are welded
together

Parameters:

    

  * **threshold** (_float in_ _[__0_ _,__10_ _]__,__(__optional_ _)_) – Merge Distance, Maximum distance between welded vertices

  * **use_unselected** (_boolean_ _,__(__optional_ _)_) – Unselected, Merge selected to other unselected vertices

  * **use_shared_vertex** (_boolean_ _,__(__optional_ _)_) – Shared Vertex, Weld UVs based on shared vertices

bpy.ops.uv.reset()¶

    

Reset UV projection

bpy.ops.uv.reveal(_*_ , _select =True_)¶

    

Reveal all hidden UV vertices

Parameters:

    

**select** (_boolean_ _,__(__optional_ _)_) – Select

bpy.ops.uv.rip(_*_ , _mirror =False_, _release_confirm =False_, _use_accurate
=False_, _location =(0.0, 0.0)_)¶

    

Rip selected vertices or a selected region

Parameters:

    

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds

bpy.ops.uv.rip_move(_*_ , _UV_OT_rip =None_, _TRANSFORM_OT_translate =None_)¶

    

Unstitch UVs and move the result

Parameters:

    

  * **UV_OT_rip** (`UV_OT_rip`, (optional)) – UV Rip, Rip selected vertices or a selected region

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.uv.seams_from_islands(_*_ , _mark_seams =True_, _mark_sharp =False_)¶

    

Set mesh seams according to island setup in the UV editor

Parameters:

    

  * **mark_seams** (_boolean_ _,__(__optional_ _)_) – Mark Seams, Mark boundary edges as seams

  * **mark_sharp** (_boolean_ _,__(__optional_ _)_) – Mark Sharp, Mark boundary edges as sharp

bpy.ops.uv.select(_*_ , _extend =False_, _deselect =False_, _toggle =False_,
_deselect_all =False_, _select_passthrough =False_, _location =(0.0, 0.0)_)¶

    

Select UV vertices

Parameters:

    

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection instead of deselecting everything first

  * **deselect** (_boolean_ _,__(__optional_ _)_) – Deselect, Remove from selection

  * **toggle** (_boolean_ _,__(__optional_ _)_) – Toggle Selection, Toggle the selection

  * **deselect_all** (_boolean_ _,__(__optional_ _)_) – Deselect On Nothing, Deselect all when nothing under the cursor

  * **select_passthrough** (_boolean_ _,__(__optional_ _)_) – Only Select Unselected, Ignore the select action when the element is already selected

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds

bpy.ops.uv.select_all(_*_ , _action =TOGGLE_)¶

    

Change selection of all UV vertices

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.uv.select_box(_*_ , _pinned =False_, _xmin =0_, _xmax =0_, _ymin =0_,
_ymax =0_, _wait_for_input =True_, _mode =SET_)¶

    

Select UV vertices using box selection

Parameters:

    

  * **pinned** (_boolean_ _,__(__optional_ _)_) – Pinned, Border select pinned UVs only

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

bpy.ops.uv.select_circle(_*_ , _x =0_, _y =0_, _radius =25_, _wait_for_input
=True_, _mode =SET_)¶

    

Select UV vertices using circle selection

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

bpy.ops.uv.select_edge_ring(_*_ , _extend =False_, _location =(0.0, 0.0)_)¶

    

Select an edge ring of connected UV vertices

Parameters:

    

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection rather than clearing the existing selection

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds

bpy.ops.uv.select_lasso(_*_ , _path =None_, _use_smooth_stroke =False_,
_smooth_stroke_factor =0.75_, _smooth_stroke_radius =35_, _mode =SET_)¶

    

Select UVs using lasso selection

Parameters:

    

  * **path** (`bpy_prop_collection` of `OperatorMousePath`, (optional)) – Path

  * **use_smooth_stroke** (_boolean_ _,__(__optional_ _)_) – Stabilize Stroke, Selection lags behind mouse and follows a smoother path

  * **smooth_stroke_factor** (_float in_ _[__0.5_ _,__0.99_ _]__,__(__optional_ _)_) – Smooth Stroke Factor, Higher values gives a smoother stroke

  * **smooth_stroke_radius** (_int in_ _[__10_ _,__200_ _]__,__(__optional_ _)_) – Smooth Stroke Radius, Minimum distance from last point before selection continues

  * **mode** (enum in [`SET`, `ADD`, `SUB`], (optional)) – 

Mode

    * `SET` Set – Set a new selection.

    * `ADD` Extend – Extend existing selection.

    * `SUB` Subtract – Subtract existing selection.

bpy.ops.uv.select_less()¶

    

Deselect UV vertices at the boundary of each selection region

bpy.ops.uv.select_linked()¶

    

Select all UV vertices linked to the active UV map

bpy.ops.uv.select_linked_pick(_*_ , _extend =False_, _deselect =False_,
_location =(0.0, 0.0)_)¶

    

Select all UV vertices linked under the mouse

Parameters:

    

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection rather than clearing the existing selection

  * **deselect** (_boolean_ _,__(__optional_ _)_) – Deselect, Deselect linked UV vertices rather than selecting them

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds

bpy.ops.uv.select_loop(_*_ , _extend =False_, _location =(0.0, 0.0)_)¶

    

Select a loop of connected UV vertices

Parameters:

    

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection rather than clearing the existing selection

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds

bpy.ops.uv.select_mode(_*_ , _type =VERTEX_)¶

    

Change UV selection mode

Parameters:

    

**type** (enum in [Mesh Select Mode Uv
Items](bpy_types_enum_items/mesh_select_mode_uv_items.html#rna-enum-mesh-
select-mode-uv-items), (optional)) – Type

bpy.ops.uv.select_more()¶

    

Select more UV vertices connected to initial selection

bpy.ops.uv.select_overlap(_*_ , _extend =False_)¶

    

Select all UV faces which overlap each other

Parameters:

    

**extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection rather
than clearing the existing selection

bpy.ops.uv.select_pinned()¶

    

Select all pinned UV vertices

bpy.ops.uv.select_similar(_*_ , _type =PIN_, _compare =EQUAL_, _threshold
=0.0_)¶

    

Select similar UVs by property types

Parameters:

    

  * **type** (enum in [`PIN`, `LENGTH`, `LENGTH_3D`, `AREA`, `AREA_3D`, `MATERIAL`, `OBJECT`, `SIDES`, `WINDING`, `FACE`], (optional)) – Type

  * **compare** (enum in [`EQUAL`, `GREATER`, `LESS`], (optional)) – Compare

  * **threshold** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Threshold

bpy.ops.uv.select_split()¶

    

Select only entirely selected faces

bpy.ops.uv.shortest_path_pick(_*_ , _use_face_step =False_,
_use_topology_distance =False_, _use_fill =False_, _skip =0_, _nth =1_,
_offset =0_, _object_index =-1_, _index =-1_)¶

    

Select shortest path between two selections

Parameters:

    

  * **use_face_step** (_boolean_ _,__(__optional_ _)_) – Face Stepping, Traverse connected faces (includes diagonals and edge-rings)

  * **use_topology_distance** (_boolean_ _,__(__optional_ _)_) – Topology Distance, Find the minimum number of steps, ignoring spatial distance

  * **use_fill** (_boolean_ _,__(__optional_ _)_) – Fill Region, Select all paths between the source/destination elements

  * **skip** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Deselected, Number of deselected elements in the repetitive sequence

  * **nth** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Selected, Number of selected elements in the repetitive sequence

  * **offset** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Offset, Offset from the starting point

bpy.ops.uv.shortest_path_select(_*_ , _use_face_step =False_,
_use_topology_distance =False_, _use_fill =False_, _skip =0_, _nth =1_,
_offset =0_)¶

    

Selected shortest path between two vertices/edges/faces

Parameters:

    

  * **use_face_step** (_boolean_ _,__(__optional_ _)_) – Face Stepping, Traverse connected faces (includes diagonals and edge-rings)

  * **use_topology_distance** (_boolean_ _,__(__optional_ _)_) – Topology Distance, Find the minimum number of steps, ignoring spatial distance

  * **use_fill** (_boolean_ _,__(__optional_ _)_) – Fill Region, Select all paths between the source/destination elements

  * **skip** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Deselected, Number of deselected elements in the repetitive sequence

  * **nth** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Selected, Number of selected elements in the repetitive sequence

  * **offset** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Offset, Offset from the starting point

bpy.ops.uv.smart_project(_*_ , _angle_limit =1.15192_, _margin_method
=SCALED_, _rotate_method =AXIS_ALIGNED_Y_, _island_margin =0.0_, _area_weight
=0.0_, _correct_aspect =True_, _scale_to_bounds =False_)¶

    

Projection unwraps the selected faces of mesh objects

Parameters:

    

  * **angle_limit** (_float in_ _[__0_ _,__1.5708_ _]__,__(__optional_ _)_) – Angle Limit, Lower for more projection groups, higher for less distortion

  * **margin_method** (enum in [`SCALED`, `ADD`, `FRACTION`], (optional)) – 

Margin Method

    * `SCALED` Scaled – Use scale of existing UVs to multiply margin.

    * `ADD` Add – Just add the margin, ignoring any UV scale.

    * `FRACTION` Fraction – Specify a precise fraction of final UV output.

  * **rotate_method** (enum in [`AXIS_ALIGNED`, `AXIS_ALIGNED_X`, `AXIS_ALIGNED_Y`], (optional)) – 

Rotation Method

    * `AXIS_ALIGNED` Axis-aligned – Rotated to a minimal rectangle, either vertical or horizontal.

    * `AXIS_ALIGNED_X` Axis-aligned (Horizontal) – Rotate islands to be aligned horizontally.

    * `AXIS_ALIGNED_Y` Axis-aligned (Vertical) – Rotate islands to be aligned vertically.

  * **island_margin** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Island Margin, Margin to reduce bleed from adjacent islands

  * **area_weight** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Area Weight, Weight projection’s vector by faces with larger areas

  * **correct_aspect** (_boolean_ _,__(__optional_ _)_) – Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account

  * **scale_to_bounds** (_boolean_ _,__(__optional_ _)_) – Scale to Bounds, Scale UV coordinates to bounds after unwrapping

bpy.ops.uv.snap_cursor(_*_ , _target =PIXELS_)¶

    

Snap cursor to target type

Parameters:

    

**target** (enum in [`PIXELS`, `SELECTED`, `ORIGIN`], (optional)) – Target,
Target to snap the selected UVs to

bpy.ops.uv.snap_selected(_*_ , _target =PIXELS_)¶

    

Snap selected UV vertices to target type

Parameters:

    

**target** (enum in [`PIXELS`, `CURSOR`, `CURSOR_OFFSET`,
`ADJACENT_UNSELECTED`], (optional)) – Target, Target to snap the selected UVs
to

bpy.ops.uv.sphere_project(_*_ , _direction =VIEW_ON_EQUATOR_, _align
=POLAR_ZX_, _pole =PINCH_, _seam =False_, _correct_aspect =True_,
_clip_to_bounds =False_, _scale_to_bounds =False_)¶

    

Project the UV vertices of the mesh over the curved surface of a sphere

Parameters:

    

  * **direction** (enum in [`VIEW_ON_EQUATOR`, `VIEW_ON_POLES`, `ALIGN_TO_OBJECT`], (optional)) – 

Direction, Direction of the sphere or cylinder

    * `VIEW_ON_EQUATOR` View on Equator – 3D view is on the equator.

    * `VIEW_ON_POLES` View on Poles – 3D view is on the poles.

    * `ALIGN_TO_OBJECT` Align to Object – Align according to object transform.

  * **align** (enum in [`POLAR_ZX`, `POLAR_ZY`], (optional)) – 

Align, How to determine rotation around the pole

    * `POLAR_ZX` Polar ZX – Polar 0 is X.

    * `POLAR_ZY` Polar ZY – Polar 0 is Y.

  * **pole** (enum in [`PINCH`, `FAN`], (optional)) – 

Pole, How to handle faces at the poles

    * `PINCH` Pinch – UVs are pinched at the poles.

    * `FAN` Fan – UVs are fanned at the poles.

  * **seam** (_boolean_ _,__(__optional_ _)_) – Preserve Seams, Separate projections by islands isolated by seams

  * **correct_aspect** (_boolean_ _,__(__optional_ _)_) – Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account

  * **clip_to_bounds** (_boolean_ _,__(__optional_ _)_) – Clip to Bounds, Clip UV coordinates to bounds after unwrapping

  * **scale_to_bounds** (_boolean_ _,__(__optional_ _)_) – Scale to Bounds, Scale UV coordinates to bounds after unwrapping

bpy.ops.uv.stitch(_*_ , _use_limit =False_, _snap_islands =True_, _limit
=0.01_, _static_island =0_, _active_object_index =0_, _midpoint_snap =False_,
_clear_seams =True_, _mode =VERTEX_, _stored_mode =VERTEX_, _selection =None_,
_objects_selection_count =(0, 0, 0, 0, 0, 0)_)¶

    

Stitch selected UV vertices by proximity

Parameters:

    

  * **use_limit** (_boolean_ _,__(__optional_ _)_) – Use Limit, Stitch UVs within a specified limit distance

  * **snap_islands** (_boolean_ _,__(__optional_ _)_) – Snap Islands, Snap islands together (on edge stitch mode, rotates the islands too)

  * **limit** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Limit, Limit distance in normalized coordinates

  * **static_island** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Static Island, Island that stays in place when stitching islands

  * **active_object_index** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Active Object, Index of the active object

  * **midpoint_snap** (_boolean_ _,__(__optional_ _)_) – Snap at Midpoint, UVs are stitched at midpoint instead of at static island

  * **clear_seams** (_boolean_ _,__(__optional_ _)_) – Clear Seams, Clear seams of stitched edges

  * **mode** (enum in [`VERTEX`, `EDGE`], (optional)) – Operation Mode, Use vertex or edge stitching

  * **stored_mode** (enum in [`VERTEX`, `EDGE`], (optional)) – Stored Operation Mode, Use vertex or edge stitching

  * **selection** (`bpy_prop_collection` of `SelectedUvElement`, (optional)) – Selection

  * **objects_selection_count** (_int array_ _of_ _6 items in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Objects Selection Count

bpy.ops.uv.unwrap(_*_ , _method =CONFORMAL_, _fill_holes =False_,
_correct_aspect =True_, _use_subsurf_data =False_, _margin_method =SCALED_,
_margin =0.001_, _no_flip =False_, _iterations =10_, _use_weights =False_,
_weight_group ='uv_importance'_, _weight_factor =1.0_)¶

    

Unwrap the mesh of the object being edited

Parameters:

    

  * **method** (enum in [`ANGLE_BASED`, `CONFORMAL`, `MINIMUM_STRETCH`], (optional)) – Method, Unwrapping method (Angle Based usually gives better results than Conformal, while being somewhat slower)

  * **fill_holes** (_boolean_ _,__(__optional_ _)_) – Fill Holes, Virtually fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry

  * **correct_aspect** (_boolean_ _,__(__optional_ _)_) – Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account

  * **use_subsurf_data** (_boolean_ _,__(__optional_ _)_) – Use Subdivision Surface, Map UVs taking vertex position after Subdivision Surface modifier has been applied

  * **margin_method** (enum in [`SCALED`, `ADD`, `FRACTION`], (optional)) – 

Margin Method

    * `SCALED` Scaled – Use scale of existing UVs to multiply margin.

    * `ADD` Add – Just add the margin, ignoring any UV scale.

    * `FRACTION` Fraction – Specify a precise fraction of final UV output.

  * **margin** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Margin, Space between islands

  * **no_flip** (_boolean_ _,__(__optional_ _)_) – No Flip, Prevent flipping UV’s, flipping may lower distortion depending on the position of pins

  * **iterations** (_int in_ _[__0_ _,__10000_ _]__,__(__optional_ _)_) – Iterations, Number of iterations when “Minimum Stretch” method is used

  * **use_weights** (_boolean_ _,__(__optional_ _)_) – Importance Weights, Whether to take into account per-vertex importance weights

  * **weight_group** (_string_ _,__(__optional_ _,__never None_ _)_) – Weight Group, Vertex group name for importance weights (modulating the deform)

  * **weight_factor** (_float in_ _[__-10000_ _,__10000_ _]__,__(__optional_ _)_) – Weight Factor, How much influence the weightmap has for weighted parameterization, 0 being no influence

bpy.ops.uv.weld()¶

    

Weld selected UV vertices together

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

