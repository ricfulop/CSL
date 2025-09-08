---
url: https://docs.blender.org/api/current/bpy.ops.sculpt.html
scraped_at: 2025-09-08T14:18:47.682933
title: Sculpt Operators¶
---

# Sculpt Operators¶

bpy.ops.sculpt.brush_stroke(_*_ , _stroke =None_, _mode =NORMAL_, _pen_flip
=False_, _override_location =False_, _ignore_background_click =False_)¶

    

Sculpt a stroke into the geometry

Parameters:

    

  * **stroke** (`bpy_prop_collection` of `OperatorStrokeElement`, (optional)) – Stroke

  * **mode** (enum in [`NORMAL`, `INVERT`, `SMOOTH`, `ERASE`], (optional)) – 

Stroke Mode, Action taken when a paint stroke is made

    * `NORMAL` Regular – Apply brush normally.

    * `INVERT` Invert – Invert action of brush for duration of stroke.

    * `SMOOTH` Smooth – Switch brush to smooth mode for duration of stroke.

    * `ERASE` Erase – Switch brush to erase mode for duration of stroke.

  * **pen_flip** (_boolean_ _,__(__optional_ _)_) – Pen Flip, Whether a tablet’s eraser mode is being used

  * **override_location** (_boolean_ _,__(__optional_ _)_) – Override Location, Override the given location array by recalculating object space positions from the provided mouse_event positions

  * **ignore_background_click** (_boolean_ _,__(__optional_ _)_) – Ignore Background Click, Clicks on the background do not start the stroke

bpy.ops.sculpt.cloth_filter(_*_ , _start_mouse =(0, 0)_, _area_normal_radius
=0.25_, _strength =1.0_, _iteration_count =1_, _event_history =None_, _type
=GRAVITY_, _force_axis ={'X', 'Y', 'Z'}_, _orientation =LOCAL_, _cloth_mass
=1.0_, _cloth_damping =0.0_, _use_face_sets =False_, _use_collisions =False_)¶

    

Applies a cloth simulation deformation to the entire mesh

Parameters:

    

  * **start_mouse** (_int array_ _of_ _2 items in_ _[__0_ _,__16384_ _]__,__(__optional_ _)_) – Starting Mouse

  * **area_normal_radius** (_float in_ _[__0.001_ _,__5_ _]__,__(__optional_ _)_) – Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius

  * **strength** (_float in_ _[__-10_ _,__10_ _]__,__(__optional_ _)_) – Strength, Filter strength

  * **iteration_count** (_int in_ _[__1_ _,__10000_ _]__,__(__optional_ _)_) – Repeat, How many times to repeat the filter

  * **type** (enum in [`GRAVITY`, `INFLATE`, `EXPAND`, `PINCH`, `SCALE`], (optional)) – 

Filter Type, Operation that is going to be applied to the mesh

    * `GRAVITY` Gravity – Applies gravity to the simulation.

    * `INFLATE` Inflate – Inflates the cloth.

    * `EXPAND` Expand – Expands the cloth’s dimensions.

    * `PINCH` Pinch – Pulls the cloth to the cursor’s start position.

    * `SCALE` Scale – Scales the mesh as a soft body using the origin of the object as scale.

  * **force_axis** (enum set in {`X`, `Y`, `Z`}, (optional)) – 

Force Axis, Apply the force in the selected axis

    * `X` X – Apply force in the X axis.

    * `Y` Y – Apply force in the Y axis.

    * `Z` Z – Apply force in the Z axis.

  * **orientation** (enum in [`LOCAL`, `WORLD`, `VIEW`], (optional)) – 

Orientation, Orientation of the axis to limit the filter force

    * `LOCAL` Local – Use the local axis to limit the force and set the gravity direction.

    * `WORLD` World – Use the global axis to limit the force and set the gravity direction.

    * `VIEW` View – Use the view axis to limit the force and set the gravity direction.

  * **cloth_mass** (_float in_ _[__0_ _,__2_ _]__,__(__optional_ _)_) – Cloth Mass, Mass of each simulation particle

  * **cloth_damping** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Cloth Damping, How much the applied forces are propagated through the cloth

  * **use_face_sets** (_boolean_ _,__(__optional_ _)_) – Use Face Sets, Apply the filter only to the Face Set under the cursor

  * **use_collisions** (_boolean_ _,__(__optional_ _)_) – Use Collisions, Collide with other collider objects in the scene

bpy.ops.sculpt.color_filter(_*_ , _start_mouse =(0, 0)_, _area_normal_radius
=0.25_, _strength =1.0_, _iteration_count =1_, _event_history =None_, _type
=FILL_, _fill_color =(1.0, 1.0, 1.0)_)¶

    

Applies a filter to modify the active color attribute

Parameters:

    

  * **start_mouse** (_int array_ _of_ _2 items in_ _[__0_ _,__16384_ _]__,__(__optional_ _)_) – Starting Mouse

  * **area_normal_radius** (_float in_ _[__0.001_ _,__5_ _]__,__(__optional_ _)_) – Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius

  * **strength** (_float in_ _[__-10_ _,__10_ _]__,__(__optional_ _)_) – Strength, Filter strength

  * **iteration_count** (_int in_ _[__1_ _,__10000_ _]__,__(__optional_ _)_) – Repeat, How many times to repeat the filter

  * **type** (enum in [`FILL`, `HUE`, `SATURATION`, `VALUE`, `BRIGHTNESS`, `CONTRAST`, `SMOOTH`, `RED`, `GREEN`, `BLUE`], (optional)) – 

Filter Type

    * `FILL` Fill – Fill with a specific color.

    * `HUE` Hue – Change hue.

    * `SATURATION` Saturation – Change saturation.

    * `VALUE` Value – Change value.

    * `BRIGHTNESS` Brightness – Change brightness.

    * `CONTRAST` Contrast – Change contrast.

    * `SMOOTH` Smooth – Smooth colors.

    * `RED` Red – Change red channel.

    * `GREEN` Green – Change green channel.

    * `BLUE` Blue – Change blue channel.

  * **fill_color** ([`mathutils.Color`](mathutils.html#mathutils.Color "mathutils.Color") of 3 items in [0, inf], (optional)) – Fill Color

bpy.ops.sculpt.detail_flood_fill()¶

    

Flood fill the mesh with the selected detail setting

bpy.ops.sculpt.dynamic_topology_toggle()¶

    

Dynamic topology alters the mesh topology while sculpting

bpy.ops.sculpt.dyntopo_detail_size_edit()¶

    

Modify the detail size of dyntopo interactively

bpy.ops.sculpt.expand(_*_ , _target =MASK_, _falloff_type =GEODESIC_, _invert
=False_, _use_mask_preserve =False_, _use_falloff_gradient =False_,
_use_modify_active =False_, _use_reposition_pivot =True_,
_max_geodesic_move_preview =10000_, _use_auto_mask =False_,
_normal_falloff_smooth =2_)¶

    

Generic sculpt expand operator

Parameters:

    

  * **target** (enum in [`MASK`, `FACE_SETS`, `COLOR`], (optional)) – Data Target, Data that is going to be modified in the expand operation

  * **falloff_type** (enum in [`GEODESIC`, `TOPOLOGY`, `TOPOLOGY_DIAGONALS`, `NORMALS`, `SPHERICAL`, `BOUNDARY_TOPOLOGY`, `BOUNDARY_FACE_SET`, `ACTIVE_FACE_SET`], (optional)) – Falloff Type, Initial falloff of the expand operation

  * **invert** (_boolean_ _,__(__optional_ _)_) – Invert, Invert the expand active elements

  * **use_mask_preserve** (_boolean_ _,__(__optional_ _)_) – Preserve Previous, Preserve the previous state of the target data

  * **use_falloff_gradient** (_boolean_ _,__(__optional_ _)_) – Falloff Gradient, Expand Using a linear falloff

  * **use_modify_active** (_boolean_ _,__(__optional_ _)_) – Modify Active, Modify the active Face Set instead of creating a new one

  * **use_reposition_pivot** (_boolean_ _,__(__optional_ _)_) – Reposition Pivot, Reposition the sculpt transform pivot to the boundary of the expand active area

  * **max_geodesic_move_preview** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Max Vertex Count for Geodesic Move Preview, Maximum number of vertices in the mesh for using geodesic falloff when moving the origin of expand. If the total number of vertices is greater than this value, the falloff will be set to spherical when moving

  * **use_auto_mask** (_boolean_ _,__(__optional_ _)_) – Auto Create, Fill in mask if nothing is already masked

  * **normal_falloff_smooth** (_int in_ _[__0_ _,__10_ _]__,__(__optional_ _)_) – Normal Smooth, Blurring steps for normal falloff

bpy.ops.sculpt.face_set_box_gesture(_*_ , _xmin =0_, _xmax =0_, _ymin =0_,
_ymax =0_, _wait_for_input =True_, _use_front_faces_only =False_)¶

    

Add a face set in a rectangle defined by the cursor

Parameters:

    

  * **xmin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Min

  * **xmax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Max

  * **ymin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Min

  * **ymax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Max

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

  * **use_front_faces_only** (_boolean_ _,__(__optional_ _)_) – Front Faces Only, Affect only faces facing towards the view

bpy.ops.sculpt.face_set_change_visibility(_*_ , _mode =TOGGLE_)¶

    

Change the visibility of the Face Sets of the sculpt

Parameters:

    

**mode** (enum in [`TOGGLE`, `SHOW_ACTIVE`, `HIDE_ACTIVE`], (optional)) –

Mode

  * `TOGGLE` Toggle Visibility – Hide all Face Sets except for the active one.

  * `SHOW_ACTIVE` Show Active Face Set – Show Active Face Set.

  * `HIDE_ACTIVE` Hide Active Face Sets – Hide Active Face Sets.

bpy.ops.sculpt.face_set_edit(_*_ , _active_face_set =1_, _mode =GROW_,
_strength =1.0_, _modify_hidden =False_)¶

    

Edits the current active Face Set

Parameters:

    

  * **active_face_set** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Active Face Set

  * **mode** (enum in [`GROW`, `SHRINK`, `DELETE_GEOMETRY`, `FAIR_POSITIONS`, `FAIR_TANGENCY`], (optional)) – 

Mode

    * `GROW` Grow Face Set – Grows the Face Sets boundary by one face based on mesh topology.

    * `SHRINK` Shrink Face Set – Shrinks the Face Sets boundary by one face based on mesh topology.

    * `DELETE_GEOMETRY` Delete Geometry – Deletes the faces that are assigned to the Face Set.

    * `FAIR_POSITIONS` Fair Positions – Creates a smooth as possible geometry patch from the Face Set minimizing changes in vertex positions.

    * `FAIR_TANGENCY` Fair Tangency – Creates a smooth as possible geometry patch from the Face Set minimizing changes in vertex tangents.

  * **strength** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Strength

  * **modify_hidden** (_boolean_ _,__(__optional_ _)_) – Modify Hidden, Apply the edit operation to hidden geometry

bpy.ops.sculpt.face_set_extract(_*_ , _add_boundary_loop =True_,
_smooth_iterations =4_, _apply_shrinkwrap =True_, _add_solidify =True_)¶

    

Create a new mesh object from the selected Face Set

Parameters:

    

  * **add_boundary_loop** (_boolean_ _,__(__optional_ _)_) – Add Boundary Loop, Add an extra edge loop to better preserve the shape when applying a subdivision surface modifier

  * **smooth_iterations** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Smooth Iterations, Smooth iterations applied to the extracted mesh

  * **apply_shrinkwrap** (_boolean_ _,__(__optional_ _)_) – Project to Sculpt, Project the extracted mesh into the original sculpt

  * **add_solidify** (_boolean_ _,__(__optional_ _)_) – Extract as Solid, Extract the mask as a solid object with a solidify modifier

bpy.ops.sculpt.face_set_lasso_gesture(_*_ , _path =None_, _use_smooth_stroke
=False_, _smooth_stroke_factor =0.75_, _smooth_stroke_radius =35_,
_use_front_faces_only =False_)¶

    

Add a face set in a shape defined by the cursor

Parameters:

    

  * **path** (`bpy_prop_collection` of `OperatorMousePath`, (optional)) – Path

  * **use_smooth_stroke** (_boolean_ _,__(__optional_ _)_) – Stabilize Stroke, Selection lags behind mouse and follows a smoother path

  * **smooth_stroke_factor** (_float in_ _[__0.5_ _,__0.99_ _]__,__(__optional_ _)_) – Smooth Stroke Factor, Higher values gives a smoother stroke

  * **smooth_stroke_radius** (_int in_ _[__10_ _,__200_ _]__,__(__optional_ _)_) – Smooth Stroke Radius, Minimum distance from last point before selection continues

  * **use_front_faces_only** (_boolean_ _,__(__optional_ _)_) – Front Faces Only, Affect only faces facing towards the view

bpy.ops.sculpt.face_set_line_gesture(_*_ , _xstart =0_, _xend =0_, _ystart
=0_, _yend =0_, _flip =False_, _cursor =5_, _use_front_faces_only =False_,
_use_limit_to_segment =False_)¶

    

Add a face set to one side of a line defined by the cursor

Parameters:

    

  * **xstart** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Start

  * **xend** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X End

  * **ystart** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Start

  * **yend** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y End

  * **flip** (_boolean_ _,__(__optional_ _)_) – Flip

  * **cursor** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Cursor, Mouse cursor style to use during the modal operator

  * **use_front_faces_only** (_boolean_ _,__(__optional_ _)_) – Front Faces Only, Affect only faces facing towards the view

  * **use_limit_to_segment** (_boolean_ _,__(__optional_ _)_) – Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line

bpy.ops.sculpt.face_set_polyline_gesture(_*_ , _path =None_,
_use_front_faces_only =False_)¶

    

Add a face set in a shape defined by the cursor

Parameters:

    

  * **path** (`bpy_prop_collection` of `OperatorMousePath`, (optional)) – Path

  * **use_front_faces_only** (_boolean_ _,__(__optional_ _)_) – Front Faces Only, Affect only faces facing towards the view

bpy.ops.sculpt.face_sets_create(_*_ , _mode =MASKED_)¶

    

Create a new Face Set

Parameters:

    

**mode** (enum in [`MASKED`, `VISIBLE`, `ALL`, `SELECTION`], (optional)) –

Mode

  * `MASKED` Face Set from Masked – Create a new Face Set from the masked faces.

  * `VISIBLE` Face Set from Visible – Create a new Face Set from the visible vertices.

  * `ALL` Face Set Full Mesh – Create an unique Face Set with all faces in the sculpt.

  * `SELECTION` Face Set from Edit Mode Selection – Create an Face Set corresponding to the Edit Mode face selection.

bpy.ops.sculpt.face_sets_init(_*_ , _mode =LOOSE_PARTS_, _threshold =0.5_)¶

    

Initializes all Face Sets in the mesh

Parameters:

    

  * **mode** (enum in [`LOOSE_PARTS`, `MATERIALS`, `NORMALS`, `UV_SEAMS`, `CREASES`, `BEVEL_WEIGHT`, `SHARP_EDGES`, `FACE_SET_BOUNDARIES`], (optional)) – 

Mode

    * `LOOSE_PARTS` Face Sets from Loose Parts – Create a Face Set per loose part in the mesh.

    * `MATERIALS` Face Sets from Material Slots – Create a Face Set per Material Slot.

    * `NORMALS` Face Sets from Mesh Normals – Create Face Sets for Faces that have similar normal.

    * `UV_SEAMS` Face Sets from UV Seams – Create Face Sets using UV Seams as boundaries.

    * `CREASES` Face Sets from Edge Creases – Create Face Sets using Edge Creases as boundaries.

    * `BEVEL_WEIGHT` Face Sets from Bevel Weight – Create Face Sets using Bevel Weights as boundaries.

    * `SHARP_EDGES` Face Sets from Sharp Edges – Create Face Sets using Sharp Edges as boundaries.

    * `FACE_SET_BOUNDARIES` Face Sets from Face Set Boundaries – Create a Face Set per isolated Face Set.

  * **threshold** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Threshold, Minimum value to consider a certain attribute a boundary when creating the Face Sets

bpy.ops.sculpt.face_sets_randomize_colors()¶

    

Generates a new set of random colors to render the Face Sets in the viewport

bpy.ops.sculpt.mask_by_color(_*_ , _contiguous =False_, _invert =False_,
_preserve_previous_mask =False_, _threshold =0.35_, _location =(0, 0)_)¶

    

Creates a mask based on the active color attribute

Parameters:

    

  * **contiguous** (_boolean_ _,__(__optional_ _)_) – Contiguous, Mask only contiguous color areas

  * **invert** (_boolean_ _,__(__optional_ _)_) – Invert, Invert the generated mask

  * **preserve_previous_mask** (_boolean_ _,__(__optional_ _)_) – Preserve Previous Mask, Preserve the previous mask and add or subtract the new one generated by the colors

  * **threshold** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Threshold, How much changes in color affect the mask generation

  * **location** (_int array_ _of_ _2 items in_ _[__0_ _,__32767_ _]__,__(__optional_ _)_) – Location, Region coordinates of sampling

bpy.ops.sculpt.mask_filter(_*_ , _filter_type =SMOOTH_, _iterations =1_,
_auto_iteration_count =True_)¶

    

Applies a filter to modify the current mask

Parameters:

    

  * **filter_type** (enum in [`SMOOTH`, `SHARPEN`, `GROW`, `SHRINK`, `CONTRAST_INCREASE`, `CONTRAST_DECREASE`], (optional)) – Type, Filter that is going to be applied to the mask

  * **iterations** (_int in_ _[__1_ _,__100_ _]__,__(__optional_ _)_) – Iterations, Number of times that the filter is going to be applied

  * **auto_iteration_count** (_boolean_ _,__(__optional_ _)_) – Auto Iteration Count, Use an automatic number of iterations based on the number of vertices of the sculpt

bpy.ops.sculpt.mask_from_boundary(_*_ , _mix_mode =MIX_, _mix_factor =1.0_,
_settings_source =OPERATOR_, _boundary_mode =MESH_, _propagation_steps =1_)¶

    

Creates a mask based on the boundaries of the surface

Parameters:

    

  * **mix_mode** (enum in [`MIX`, `MULTIPLY`, `DIVIDE`, `ADD`, `SUBTRACT`], (optional)) – Mode, Mix mode

  * **mix_factor** (_float in_ _[__0_ _,__5_ _]__,__(__optional_ _)_) – Mix Factor

  * **settings_source** (enum in [`OPERATOR`, `BRUSH`, `SCENE`], (optional)) – 

Settings, Use settings from here

    * `OPERATOR` Operator – Use settings from operator properties.

    * `BRUSH` Brush – Use settings from brush.

    * `SCENE` Scene – Use settings from scene.

  * **boundary_mode** (enum in [`MESH`, `FACE_SETS`], (optional)) – 

Mode, Boundary type to mask

    * `MESH` Mesh – Calculate the boundary mask based on disconnected mesh topology islands.

    * `FACE_SETS` Face Sets – Calculate the boundary mask between face sets.

  * **propagation_steps** (_int in_ _[__1_ _,__20_ _]__,__(__optional_ _)_) – Propagation Steps

bpy.ops.sculpt.mask_from_cavity(_*_ , _mix_mode =MIX_, _mix_factor =1.0_,
_settings_source =OPERATOR_, _factor =0.5_, _blur_steps =2_, _use_curve
=False_, _invert =False_)¶

    

Creates a mask based on the curvature of the surface

Parameters:

    

  * **mix_mode** (enum in [`MIX`, `MULTIPLY`, `DIVIDE`, `ADD`, `SUBTRACT`], (optional)) – Mode, Mix mode

  * **mix_factor** (_float in_ _[__0_ _,__5_ _]__,__(__optional_ _)_) – Mix Factor

  * **settings_source** (enum in [`OPERATOR`, `BRUSH`, `SCENE`], (optional)) – 

Settings, Use settings from here

    * `OPERATOR` Operator – Use settings from operator properties.

    * `BRUSH` Brush – Use settings from brush.

    * `SCENE` Scene – Use settings from scene.

  * **factor** (_float in_ _[__0_ _,__5_ _]__,__(__optional_ _)_) – Factor, The contrast of the cavity mask

  * **blur_steps** (_int in_ _[__0_ _,__25_ _]__,__(__optional_ _)_) – Blur, The number of times the cavity mask is blurred

  * **use_curve** (_boolean_ _,__(__optional_ _)_) – Custom Curve

  * **invert** (_boolean_ _,__(__optional_ _)_) – Cavity (Inverted)

bpy.ops.sculpt.mask_init(_*_ , _mode =RANDOM_PER_VERTEX_)¶

    

Creates a new mask for the entire mesh

Parameters:

    

**mode** (enum in [`RANDOM_PER_VERTEX`, `RANDOM_PER_FACE_SET`,
`RANDOM_PER_LOOSE_PART`], (optional)) – Mode

bpy.ops.sculpt.mesh_filter(_*_ , _start_mouse =(0, 0)_, _area_normal_radius
=0.25_, _strength =1.0_, _iteration_count =1_, _event_history =None_, _type
=INFLATE_, _deform_axis ={'X', 'Y', 'Z'}_, _orientation =LOCAL_,
_surface_smooth_shape_preservation =0.5_, _surface_smooth_current_vertex
=0.5_, _sharpen_smooth_ratio =0.35_, _sharpen_intensify_detail_strength =0.0_,
_sharpen_curvature_smooth_iterations =0_)¶

    

Applies a filter to modify the current mesh

Parameters:

    

  * **start_mouse** (_int array_ _of_ _2 items in_ _[__0_ _,__16384_ _]__,__(__optional_ _)_) – Starting Mouse

  * **area_normal_radius** (_float in_ _[__0.001_ _,__5_ _]__,__(__optional_ _)_) – Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius

  * **strength** (_float in_ _[__-10_ _,__10_ _]__,__(__optional_ _)_) – Strength, Filter strength

  * **iteration_count** (_int in_ _[__1_ _,__10000_ _]__,__(__optional_ _)_) – Repeat, How many times to repeat the filter

  * **type** (enum in [`SMOOTH`, `SCALE`, `INFLATE`, `SPHERE`, `RANDOM`, `RELAX`, `RELAX_FACE_SETS`, `SURFACE_SMOOTH`, `SHARPEN`, `ENHANCE_DETAILS`, `ERASE_DISPLACEMENT`], (optional)) – 

Filter Type, Operation that is going to be applied to the mesh

    * `SMOOTH` Smooth – Smooth mesh.

    * `SCALE` Scale – Scale mesh.

    * `INFLATE` Inflate – Inflate mesh.

    * `SPHERE` Sphere – Morph into sphere.

    * `RANDOM` Random – Randomize vertex positions.

    * `RELAX` Relax – Relax mesh.

    * `RELAX_FACE_SETS` Relax Face Sets – Smooth the edges of all the Face Sets.

    * `SURFACE_SMOOTH` Surface Smooth – Smooth the surface of the mesh, preserving the volume.

    * `SHARPEN` Sharpen – Sharpen the cavities of the mesh.

    * `ENHANCE_DETAILS` Enhance Details – Enhance the high frequency surface detail.

    * `ERASE_DISPLACEMENT` Erase Displacement – Deletes the displacement of the Multires Modifier.

  * **deform_axis** (enum set in {`X`, `Y`, `Z`}, (optional)) – 

Deform Axis, Apply the deformation in the selected axis

    * `X` X – Deform in the X axis.

    * `Y` Y – Deform in the Y axis.

    * `Z` Z – Deform in the Z axis.

  * **orientation** (enum in [`LOCAL`, `WORLD`, `VIEW`], (optional)) – 

Orientation, Orientation of the axis to limit the filter displacement

    * `LOCAL` Local – Use the local axis to limit the displacement.

    * `WORLD` World – Use the global axis to limit the displacement.

    * `VIEW` View – Use the view axis to limit the displacement.

  * **surface_smooth_shape_preservation** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Shape Preservation, How much of the original shape is preserved when smoothing

  * **surface_smooth_current_vertex** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Per Vertex Displacement, How much the position of each individual vertex influences the final result

  * **sharpen_smooth_ratio** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Smooth Ratio, How much smoothing is applied to polished surfaces

  * **sharpen_intensify_detail_strength** (_float in_ _[__0_ _,__10_ _]__,__(__optional_ _)_) – Intensify Details, How much creases and valleys are intensified

  * **sharpen_curvature_smooth_iterations** (_int in_ _[__0_ _,__10_ _]__,__(__optional_ _)_) – Curvature Smooth Iterations, How much smooth the resulting shape is, ignoring high frequency details

bpy.ops.sculpt.optimize()¶

    

Recalculate the sculpt BVH to improve performance

bpy.ops.sculpt.paint_mask_extract(_*_ , _mask_threshold =0.5_,
_add_boundary_loop =True_, _smooth_iterations =4_, _apply_shrinkwrap =True_,
_add_solidify =True_)¶

    

Create a new mesh object from the current paint mask

Parameters:

    

  * **mask_threshold** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Threshold, Minimum mask value to consider the vertex valid to extract a face from the original mesh

  * **add_boundary_loop** (_boolean_ _,__(__optional_ _)_) – Add Boundary Loop, Add an extra edge loop to better preserve the shape when applying a subdivision surface modifier

  * **smooth_iterations** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Smooth Iterations, Smooth iterations applied to the extracted mesh

  * **apply_shrinkwrap** (_boolean_ _,__(__optional_ _)_) – Project to Sculpt, Project the extracted mesh into the original sculpt

  * **add_solidify** (_boolean_ _,__(__optional_ _)_) – Extract as Solid, Extract the mask as a solid object with a solidify modifier

bpy.ops.sculpt.paint_mask_slice(_*_ , _mask_threshold =0.5_, _fill_holes
=True_, _new_object =True_)¶

    

Slices the paint mask from the mesh

Parameters:

    

  * **mask_threshold** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Threshold, Minimum mask value to consider the vertex valid to extract a face from the original mesh

  * **fill_holes** (_boolean_ _,__(__optional_ _)_) – Fill Holes, Fill holes after slicing the mask

  * **new_object** (_boolean_ _,__(__optional_ _)_) – Slice to New Object, Create a new object from the sliced mask

bpy.ops.sculpt.project_line_gesture(_*_ , _xstart =0_, _xend =0_, _ystart =0_,
_yend =0_, _flip =False_, _cursor =5_, _use_front_faces_only =False_,
_use_limit_to_segment =False_)¶

    

Project the geometry onto a plane defined by a line

Parameters:

    

  * **xstart** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Start

  * **xend** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X End

  * **ystart** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Start

  * **yend** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y End

  * **flip** (_boolean_ _,__(__optional_ _)_) – Flip

  * **cursor** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Cursor, Mouse cursor style to use during the modal operator

  * **use_front_faces_only** (_boolean_ _,__(__optional_ _)_) – Front Faces Only, Affect only faces facing towards the view

  * **use_limit_to_segment** (_boolean_ _,__(__optional_ _)_) – Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line

bpy.ops.sculpt.sample_color()¶

    

Sample the vertex color of the active vertex

bpy.ops.sculpt.sample_detail_size(_*_ , _location =(0, 0)_, _mode =DYNTOPO_)¶

    

Sample the mesh detail on clicked point

Parameters:

    

  * **location** (_int array_ _of_ _2 items in_ _[__0_ _,__32767_ _]__,__(__optional_ _)_) – Location, Screen coordinates of sampling

  * **mode** (enum in [`DYNTOPO`, `VOXEL`], (optional)) – 

Detail Mode, Target sculpting workflow that is going to use the sampled size

    * `DYNTOPO` Dyntopo – Sample dyntopo detail.

    * `VOXEL` Voxel – Sample mesh voxel size.

bpy.ops.sculpt.sculptmode_toggle()¶

    

Toggle sculpt mode in 3D view

bpy.ops.sculpt.set_persistent_base()¶

    

Reset the copy of the mesh that is being sculpted on

bpy.ops.sculpt.set_pivot_position(_*_ , _mode =UNMASKED_, _mouse_x =0.0_,
_mouse_y =0.0_)¶

    

Sets the sculpt transform pivot position

Parameters:

    

  * **mode** (enum in [`ORIGIN`, `UNMASKED`, `BORDER`, `ACTIVE`, `SURFACE`], (optional)) – 

Mode

    * `ORIGIN` Origin – Sets the pivot to the origin of the sculpt.

    * `UNMASKED` Unmasked – Sets the pivot position to the average position of the unmasked vertices.

    * `BORDER` Mask Border – Sets the pivot position to the center of the border of the mask.

    * `ACTIVE` Active Vertex – Sets the pivot position to the active vertex position.

    * `SURFACE` Surface – Sets the pivot position to the surface under the cursor.

  * **mouse_x** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Mouse Position X, Position of the mouse used for “Surface” and “Active Vertex” mode

  * **mouse_y** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Mouse Position Y, Position of the mouse used for “Surface” and “Active Vertex” mode

bpy.ops.sculpt.symmetrize(_*_ , _merge_tolerance =0.0005_)¶

    

Symmetrize the topology modifications

Parameters:

    

**merge_tolerance** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) –
Merge Distance, Distance within which symmetrical vertices are merged

bpy.ops.sculpt.trim_box_gesture(_*_ , _xmin =0_, _xmax =0_, _ymin =0_, _ymax
=0_, _wait_for_input =True_, _use_front_faces_only =False_, _location =(0,
0)_, _trim_mode =DIFFERENCE_, _use_cursor_depth =False_, _trim_orientation
=VIEW_, _trim_extrude_mode =FIXED_, _trim_solver =MANIFOLD_)¶

    

Execute a boolean operation on the mesh and a rectangle defined by the cursor

Parameters:

    

  * **xmin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Min

  * **xmax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Max

  * **ymin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Min

  * **ymax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Max

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

  * **use_front_faces_only** (_boolean_ _,__(__optional_ _)_) – Front Faces Only, Affect only faces facing towards the view

  * **location** (_int array_ _of_ _2 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Location, Mouse location

  * **trim_mode** (enum in [`DIFFERENCE`, `UNION`, `JOIN`], (optional)) – 

Trim Mode

    * `DIFFERENCE` Difference – Use a difference boolean operation.

    * `UNION` Union – Use a union boolean operation.

    * `JOIN` Join – Join the new mesh as separate geometry, without performing any boolean operation.

  * **use_cursor_depth** (_boolean_ _,__(__optional_ _)_) – Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape

  * **trim_orientation** (enum in [`VIEW`, `SURFACE`], (optional)) – 

Shape Orientation

    * `VIEW` View – Use the view to orientate the trimming shape.

    * `SURFACE` Surface – Use the surface normal to orientate the trimming shape.

  * **trim_extrude_mode** (enum in [`PROJECT`, `FIXED`], (optional)) – 

Extrude Mode

    * `PROJECT` Project – Align trim geometry with the perspective of the current view for a tapered shape.

    * `FIXED` Fixed – Align trim geometry orthogonally for a shape with 90 degree angles.

  * **trim_solver** (enum in [`EXACT`, `FLOAT`, `MANIFOLD`], (optional)) – 

Solver

    * `EXACT` Exact – Slower solver with the best results for coplanar faces.

    * `FLOAT` Float – Simple solver with good performance, without support for overlapping geometry.

    * `MANIFOLD` Manifold – Fastest solver that works only on manifold meshes but gives better results.

bpy.ops.sculpt.trim_lasso_gesture(_*_ , _path =None_, _use_smooth_stroke
=False_, _smooth_stroke_factor =0.75_, _smooth_stroke_radius =35_,
_use_front_faces_only =False_, _location =(0, 0)_, _trim_mode =DIFFERENCE_,
_use_cursor_depth =False_, _trim_orientation =VIEW_, _trim_extrude_mode
=FIXED_, _trim_solver =MANIFOLD_)¶

    

Execute a boolean operation on the mesh and a shape defined by the cursor

Parameters:

    

  * **path** (`bpy_prop_collection` of `OperatorMousePath`, (optional)) – Path

  * **use_smooth_stroke** (_boolean_ _,__(__optional_ _)_) – Stabilize Stroke, Selection lags behind mouse and follows a smoother path

  * **smooth_stroke_factor** (_float in_ _[__0.5_ _,__0.99_ _]__,__(__optional_ _)_) – Smooth Stroke Factor, Higher values gives a smoother stroke

  * **smooth_stroke_radius** (_int in_ _[__10_ _,__200_ _]__,__(__optional_ _)_) – Smooth Stroke Radius, Minimum distance from last point before selection continues

  * **use_front_faces_only** (_boolean_ _,__(__optional_ _)_) – Front Faces Only, Affect only faces facing towards the view

  * **location** (_int array_ _of_ _2 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Location, Mouse location

  * **trim_mode** (enum in [`DIFFERENCE`, `UNION`, `JOIN`], (optional)) – 

Trim Mode

    * `DIFFERENCE` Difference – Use a difference boolean operation.

    * `UNION` Union – Use a union boolean operation.

    * `JOIN` Join – Join the new mesh as separate geometry, without performing any boolean operation.

  * **use_cursor_depth** (_boolean_ _,__(__optional_ _)_) – Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape

  * **trim_orientation** (enum in [`VIEW`, `SURFACE`], (optional)) – 

Shape Orientation

    * `VIEW` View – Use the view to orientate the trimming shape.

    * `SURFACE` Surface – Use the surface normal to orientate the trimming shape.

  * **trim_extrude_mode** (enum in [`PROJECT`, `FIXED`], (optional)) – 

Extrude Mode

    * `PROJECT` Project – Align trim geometry with the perspective of the current view for a tapered shape.

    * `FIXED` Fixed – Align trim geometry orthogonally for a shape with 90 degree angles.

  * **trim_solver** (enum in [`EXACT`, `FLOAT`, `MANIFOLD`], (optional)) – 

Solver

    * `EXACT` Exact – Slower solver with the best results for coplanar faces.

    * `FLOAT` Float – Simple solver with good performance, without support for overlapping geometry.

    * `MANIFOLD` Manifold – Fastest solver that works only on manifold meshes but gives better results.

bpy.ops.sculpt.trim_line_gesture(_*_ , _xstart =0_, _xend =0_, _ystart =0_,
_yend =0_, _flip =False_, _cursor =5_, _use_front_faces_only =False_,
_use_limit_to_segment =False_, _location =(0, 0)_, _trim_mode =DIFFERENCE_,
_use_cursor_depth =False_, _trim_orientation =VIEW_, _trim_extrude_mode
=FIXED_, _trim_solver =MANIFOLD_)¶

    

Remove a portion of the mesh on one side of a line

Parameters:

    

  * **xstart** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Start

  * **xend** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X End

  * **ystart** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Start

  * **yend** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y End

  * **flip** (_boolean_ _,__(__optional_ _)_) – Flip

  * **cursor** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Cursor, Mouse cursor style to use during the modal operator

  * **use_front_faces_only** (_boolean_ _,__(__optional_ _)_) – Front Faces Only, Affect only faces facing towards the view

  * **use_limit_to_segment** (_boolean_ _,__(__optional_ _)_) – Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line

  * **location** (_int array_ _of_ _2 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Location, Mouse location

  * **trim_mode** (enum in [`DIFFERENCE`, `UNION`, `JOIN`], (optional)) – 

Trim Mode

    * `DIFFERENCE` Difference – Use a difference boolean operation.

    * `UNION` Union – Use a union boolean operation.

    * `JOIN` Join – Join the new mesh as separate geometry, without performing any boolean operation.

  * **use_cursor_depth** (_boolean_ _,__(__optional_ _)_) – Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape

  * **trim_orientation** (enum in [`VIEW`, `SURFACE`], (optional)) – 

Shape Orientation

    * `VIEW` View – Use the view to orientate the trimming shape.

    * `SURFACE` Surface – Use the surface normal to orientate the trimming shape.

  * **trim_extrude_mode** (enum in [`PROJECT`, `FIXED`], (optional)) – 

Extrude Mode

    * `PROJECT` Project – Align trim geometry with the perspective of the current view for a tapered shape.

    * `FIXED` Fixed – Align trim geometry orthogonally for a shape with 90 degree angles.

  * **trim_solver** (enum in [`EXACT`, `FLOAT`, `MANIFOLD`], (optional)) – 

Solver

    * `EXACT` Exact – Slower solver with the best results for coplanar faces.

    * `FLOAT` Float – Simple solver with good performance, without support for overlapping geometry.

    * `MANIFOLD` Manifold – Fastest solver that works only on manifold meshes but gives better results.

bpy.ops.sculpt.trim_polyline_gesture(_*_ , _path =None_, _use_front_faces_only
=False_, _location =(0, 0)_, _trim_mode =DIFFERENCE_, _use_cursor_depth
=False_, _trim_orientation =VIEW_, _trim_extrude_mode =FIXED_, _trim_solver
=MANIFOLD_)¶

    

Execute a boolean operation on the mesh and a polygonal shape defined by the
cursor

Parameters:

    

  * **path** (`bpy_prop_collection` of `OperatorMousePath`, (optional)) – Path

  * **use_front_faces_only** (_boolean_ _,__(__optional_ _)_) – Front Faces Only, Affect only faces facing towards the view

  * **location** (_int array_ _of_ _2 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Location, Mouse location

  * **trim_mode** (enum in [`DIFFERENCE`, `UNION`, `JOIN`], (optional)) – 

Trim Mode

    * `DIFFERENCE` Difference – Use a difference boolean operation.

    * `UNION` Union – Use a union boolean operation.

    * `JOIN` Join – Join the new mesh as separate geometry, without performing any boolean operation.

  * **use_cursor_depth** (_boolean_ _,__(__optional_ _)_) – Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape

  * **trim_orientation** (enum in [`VIEW`, `SURFACE`], (optional)) – 

Shape Orientation

    * `VIEW` View – Use the view to orientate the trimming shape.

    * `SURFACE` Surface – Use the surface normal to orientate the trimming shape.

  * **trim_extrude_mode** (enum in [`PROJECT`, `FIXED`], (optional)) – 

Extrude Mode

    * `PROJECT` Project – Align trim geometry with the perspective of the current view for a tapered shape.

    * `FIXED` Fixed – Align trim geometry orthogonally for a shape with 90 degree angles.

  * **trim_solver** (enum in [`EXACT`, `FLOAT`, `MANIFOLD`], (optional)) – 

Solver

    * `EXACT` Exact – Slower solver with the best results for coplanar faces.

    * `FLOAT` Float – Simple solver with good performance, without support for overlapping geometry.

    * `MANIFOLD` Manifold – Fastest solver that works only on manifold meshes but gives better results.

bpy.ops.sculpt.uv_sculpt_grab(_*_ , _use_invert =False_)¶

    

Grab UVs

Parameters:

    

**use_invert** (_boolean_ _,__(__optional_ _)_) – Invert, Invert action for
the duration of the stroke

bpy.ops.sculpt.uv_sculpt_pinch(_*_ , _use_invert =False_)¶

    

Pinch UVs

Parameters:

    

**use_invert** (_boolean_ _,__(__optional_ _)_) – Invert, Invert action for
the duration of the stroke

bpy.ops.sculpt.uv_sculpt_relax(_*_ , _use_invert =False_, _relax_method
=COTAN_)¶

    

Relax UVs

Parameters:

    

  * **use_invert** (_boolean_ _,__(__optional_ _)_) – Invert, Invert action for the duration of the stroke

  * **relax_method** (enum in [`LAPLACIAN`, `HC`, `COTAN`], (optional)) – 

Relax Method, Algorithm used for UV relaxation

    * `LAPLACIAN` Laplacian – Use Laplacian method for relaxation.

    * `HC` HC – Use HC method for relaxation.

    * `COTAN` Geometry – Use Geometry (cotangent) relaxation, making UVs follow the underlying 3D geometry.

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

