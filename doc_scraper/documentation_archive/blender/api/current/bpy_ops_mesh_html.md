---
url: https://docs.blender.org/api/current/bpy.ops.mesh.html
scraped_at: 2025-09-08T14:18:28.875589
title: Mesh Operators¶
---

# Mesh Operators¶

bpy.ops.mesh.attribute_set(_*_ , _value_float =0.0_, _value_float_vector_2d
=(0.0, 0.0)_, _value_float_vector_3d =(0.0, 0.0, 0.0)_, _value_int =0_,
_value_int_vector_2d =(0, 0)_, _value_color =(1.0, 1.0, 1.0, 1.0)_,
_value_bool =False_)¶

    

Set values of the active attribute for selected elements

Parameters:

    

  * **value_float** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Value

  * **value_float_vector_2d** (_float array_ _of_ _2 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Value

  * **value_float_vector_3d** (_float array_ _of_ _3 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Value

  * **value_int** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Value

  * **value_int_vector_2d** (_int array_ _of_ _2 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Value

  * **value_color** (_float array_ _of_ _4 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Value

  * **value_bool** (_boolean_ _,__(__optional_ _)_) – Value

bpy.ops.mesh.average_normals(_*_ , _average_type =CUSTOM_NORMAL_, _weight
=50_, _threshold =0.01_)¶

    

Average custom normals of selected vertices

Parameters:

    

  * **average_type** (enum in [`CUSTOM_NORMAL`, `FACE_AREA`, `CORNER_ANGLE`], (optional)) – 

Type, Averaging method

    * `CUSTOM_NORMAL` Custom Normal – Take average of vertex normals.

    * `FACE_AREA` Face Area – Set all vertex normals by face area.

    * `CORNER_ANGLE` Corner Angle – Set all vertex normals by corner angle.

  * **weight** (_int in_ _[__1_ _,__100_ _]__,__(__optional_ _)_) – Weight, Weight applied per face

  * **threshold** (_float in_ _[__0_ _,__10_ _]__,__(__optional_ _)_) – Threshold, Threshold value for different weights to be considered equal

bpy.ops.mesh.beautify_fill(_*_ , _angle_limit =3.14159_)¶

    

Rearrange some faces to try to get less degenerated geometry

Parameters:

    

**angle_limit** (_float in_ _[__0_ _,__3.14159_ _]__,__(__optional_ _)_) – Max
Angle, Angle limit

bpy.ops.mesh.bevel(_*_ , _offset_type =OFFSET_, _offset =0.0_, _profile_type
=SUPERELLIPSE_, _offset_pct =0.0_, _segments =1_, _profile =0.5_, _affect
=EDGES_, _clamp_overlap =False_, _loop_slide =True_, _mark_seam =False_,
_mark_sharp =False_, _material =-1_, _harden_normals =False_,
_face_strength_mode =NONE_, _miter_outer =SHARP_, _miter_inner =SHARP_,
_spread =0.1_, _vmesh_method =ADJ_, _release_confirm =False_)¶

    

Cut into selected items at an angle to create bevel or chamfer

Parameters:

    

  * **offset_type** (enum in [`OFFSET`, `WIDTH`, `DEPTH`, `PERCENT`, `ABSOLUTE`], (optional)) – 

Width Type, The method for determining the size of the bevel

    * `OFFSET` Offset – Amount is offset of new edges from original.

    * `WIDTH` Width – Amount is width of new face.

    * `DEPTH` Depth – Amount is perpendicular distance from original edge to bevel face.

    * `PERCENT` Percent – Amount is percent of adjacent edge length.

    * `ABSOLUTE` Absolute – Amount is absolute distance along adjacent edge.

  * **offset** (_float in_ _[__0_ _,__1e+06_ _]__,__(__optional_ _)_) – Width, Bevel amount

  * **profile_type** (enum in [`SUPERELLIPSE`, `CUSTOM`], (optional)) – 

Profile Type, The type of shape used to rebuild a beveled section

    * `SUPERELLIPSE` Superellipse – The profile can be a concave or convex curve.

    * `CUSTOM` Custom – The profile can be any arbitrary path between its endpoints.

  * **offset_pct** (_float in_ _[__0_ _,__100_ _]__,__(__optional_ _)_) – Width Percent, Bevel amount for percentage method

  * **segments** (_int in_ _[__1_ _,__1000_ _]__,__(__optional_ _)_) – Segments, Segments for curved edge

  * **profile** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Profile, Controls profile shape (0.5 = round)

  * **affect** (enum in [`VERTICES`, `EDGES`], (optional)) – 

Affect, Affect edges or vertices

    * `VERTICES` Vertices – Affect only vertices.

    * `EDGES` Edges – Affect only edges.

  * **clamp_overlap** (_boolean_ _,__(__optional_ _)_) – Clamp Overlap, Do not allow beveled edges/vertices to overlap each other

  * **loop_slide** (_boolean_ _,__(__optional_ _)_) – Loop Slide, Prefer sliding along edges to even widths

  * **mark_seam** (_boolean_ _,__(__optional_ _)_) – Mark Seams, Mark Seams along beveled edges

  * **mark_sharp** (_boolean_ _,__(__optional_ _)_) – Mark Sharp, Mark beveled edges as sharp

  * **material** (_int in_ _[__-1_ _,__inf_ _]__,__(__optional_ _)_) – Material Index, Material for bevel faces (-1 means use adjacent faces)

  * **harden_normals** (_boolean_ _,__(__optional_ _)_) – Harden Normals, Match normals of new faces to adjacent faces

  * **face_strength_mode** (enum in [`NONE`, `NEW`, `AFFECTED`, `ALL`], (optional)) – 

Face Strength Mode, Whether to set face strength, and which faces to set face
strength on

    * `NONE` None – Do not set face strength.

    * `NEW` New – Set face strength on new faces only.

    * `AFFECTED` Affected – Set face strength on new and modified faces only.

    * `ALL` All – Set face strength on all faces.

  * **miter_outer** (enum in [`SHARP`, `PATCH`, `ARC`], (optional)) – 

Outer Miter, Pattern to use for outside of miters

    * `SHARP` Sharp – Outside of miter is sharp.

    * `PATCH` Patch – Outside of miter is squared-off patch.

    * `ARC` Arc – Outside of miter is arc.

  * **miter_inner** (enum in [`SHARP`, `ARC`], (optional)) – 

Inner Miter, Pattern to use for inside of miters

    * `SHARP` Sharp – Inside of miter is sharp.

    * `ARC` Arc – Inside of miter is arc.

  * **spread** (_float in_ _[__0_ _,__1e+06_ _]__,__(__optional_ _)_) – Spread, Amount to spread arcs for arc inner miters

  * **vmesh_method** (enum in [`ADJ`, `CUTOFF`], (optional)) – 

Vertex Mesh Method, The method to use to create meshes at intersections

    * `ADJ` Grid Fill – Default patterned fill.

    * `CUTOFF` Cutoff – A cutoff at each profile’s end before the intersection.

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release

bpy.ops.mesh.bisect(_*_ , _plane_co =(0.0, 0.0, 0.0)_, _plane_no =(0.0, 0.0,
0.0)_, _use_fill =False_, _clear_inner =False_, _clear_outer =False_,
_threshold =0.0001_, _xstart =0_, _xend =0_, _ystart =0_, _yend =0_, _flip
=False_, _cursor =5_)¶

    

Cut geometry along a plane (click-drag to define plane)

Parameters:

    

  * **plane_co** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Plane Point, A point on the plane

  * **plane_no** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-1, 1], (optional)) – Plane Normal, The direction the plane points

  * **use_fill** (_boolean_ _,__(__optional_ _)_) – Fill, Fill in the cut

  * **clear_inner** (_boolean_ _,__(__optional_ _)_) – Clear Inner, Remove geometry behind the plane

  * **clear_outer** (_boolean_ _,__(__optional_ _)_) – Clear Outer, Remove geometry in front of the plane

  * **threshold** (_float in_ _[__0_ _,__10_ _]__,__(__optional_ _)_) – Axis Threshold, Preserves the existing geometry along the cut plane

  * **xstart** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Start

  * **xend** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X End

  * **ystart** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Start

  * **yend** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y End

  * **flip** (_boolean_ _,__(__optional_ _)_) – Flip

  * **cursor** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Cursor, Mouse cursor style to use during the modal operator

bpy.ops.mesh.blend_from_shape(_*_ , _shape_ , _blend =1.0_, _add =True_)¶

    

Blend in shape from a shape key

Parameters:

    

  * **shape** (_enum in_ _[__]__,__(__optional_ _)_) – Shape, Shape key to use for blending

  * **blend** (_float in_ _[__-1000_ _,__1000_ _]__,__(__optional_ _)_) – Blend, Blending factor

  * **add** (_boolean_ _,__(__optional_ _)_) – Add, Add rather than blend between shapes

bpy.ops.mesh.bridge_edge_loops(_*_ , _type =SINGLE_, _use_merge =False_,
_merge_factor =0.5_, _twist_offset =0_, _number_cuts =0_, _interpolation
=PATH_, _smoothness =1.0_, _profile_shape_factor =0.0_, _profile_shape
=SMOOTH_)¶

    

Create a bridge of faces between two or more selected edge loops

Parameters:

    

  * **type** (enum in [`SINGLE`, `CLOSED`, `PAIRS`], (optional)) – Connect Loops, Method of bridging multiple loops

  * **use_merge** (_boolean_ _,__(__optional_ _)_) – Merge, Merge rather than creating faces

  * **merge_factor** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Merge Factor

  * **twist_offset** (_int in_ _[__-1000_ _,__1000_ _]__,__(__optional_ _)_) – Twist, Twist offset for closed loops

  * **number_cuts** (_int in_ _[__0_ _,__1000_ _]__,__(__optional_ _)_) – Number of Cuts

  * **interpolation** (enum in [`LINEAR`, `PATH`, `SURFACE`], (optional)) – Interpolation, Interpolation method

  * **smoothness** (_float in_ _[__0_ _,__1000_ _]__,__(__optional_ _)_) – Smoothness, Smoothness factor

  * **profile_shape_factor** (_float in_ _[__-1000_ _,__1000_ _]__,__(__optional_ _)_) – Profile Factor, How much intermediary new edges are shrunk/expanded

  * **profile_shape** (enum in [Proportional Falloff Curve Only Items](bpy_types_enum_items/proportional_falloff_curve_only_items.html#rna-enum-proportional-falloff-curve-only-items), (optional)) – Profile Shape, Shape of the profile

bpy.ops.mesh.colors_reverse()¶

    

Flip direction of face corner color attribute inside faces

bpy.ops.mesh.colors_rotate(_*_ , _use_ccw =False_)¶

    

Rotate face corner color attribute inside faces

Parameters:

    

**use_ccw** (_boolean_ _,__(__optional_ _)_) – Counter Clockwise

bpy.ops.mesh.convex_hull(_*_ , _delete_unused =True_, _use_existing_faces
=True_, _make_holes =False_, _join_triangles =True_, _face_threshold
=0.698132_, _shape_threshold =0.698132_, _topology_influence =0.0_, _uvs
=False_, _vcols =False_, _seam =False_, _sharp =False_, _materials =False_,
_deselect_joined =False_)¶

    

Enclose selected vertices in a convex polyhedron

Parameters:

    

  * **delete_unused** (_boolean_ _,__(__optional_ _)_) – Delete Unused, Delete selected elements that are not used by the hull

  * **use_existing_faces** (_boolean_ _,__(__optional_ _)_) – Use Existing Faces, Skip hull triangles that are covered by a pre-existing face

  * **make_holes** (_boolean_ _,__(__optional_ _)_) – Make Holes, Delete selected faces that are used by the hull

  * **join_triangles** (_boolean_ _,__(__optional_ _)_) – Join Triangles, Merge adjacent triangles into quads

  * **face_threshold** (_float in_ _[__0_ _,__3.14159_ _]__,__(__optional_ _)_) – Max Face Angle, Face angle limit

  * **shape_threshold** (_float in_ _[__0_ _,__3.14159_ _]__,__(__optional_ _)_) – Max Shape Angle, Shape angle limit

  * **topology_influence** (_float in_ _[__0_ _,__2_ _]__,__(__optional_ _)_) – Topology Influence, How much to prioritize regular grids of quads as well as quads that touch existing quads

  * **uvs** (_boolean_ _,__(__optional_ _)_) – Compare UVs

  * **vcols** (_boolean_ _,__(__optional_ _)_) – Compare Color Attributes

  * **seam** (_boolean_ _,__(__optional_ _)_) – Compare Seam

  * **sharp** (_boolean_ _,__(__optional_ _)_) – Compare Sharp

  * **materials** (_boolean_ _,__(__optional_ _)_) – Compare Materials

  * **deselect_joined** (_boolean_ _,__(__optional_ _)_) – Deselect Joined, Only select remaining triangles that were not merged

bpy.ops.mesh.customdata_custom_splitnormals_add()¶

    

Add a custom split normals layer, if none exists yet

bpy.ops.mesh.customdata_custom_splitnormals_clear()¶

    

Remove the custom split normals layer, if it exists

bpy.ops.mesh.customdata_mask_clear()¶

    

Clear vertex sculpt masking data from the mesh

bpy.ops.mesh.customdata_skin_add()¶

    

Add a vertex skin layer

bpy.ops.mesh.customdata_skin_clear()¶

    

Clear vertex skin layer

bpy.ops.mesh.decimate(_*_ , _ratio =1.0_, _use_vertex_group =False_,
_vertex_group_factor =1.0_, _invert_vertex_group =False_, _use_symmetry
=False_, _symmetry_axis =Y_)¶

    

Simplify geometry by collapsing edges

Parameters:

    

  * **ratio** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Ratio

  * **use_vertex_group** (_boolean_ _,__(__optional_ _)_) – Vertex Group, Use active vertex group as an influence

  * **vertex_group_factor** (_float in_ _[__0_ _,__1000_ _]__,__(__optional_ _)_) – Weight, Vertex group strength

  * **invert_vertex_group** (_boolean_ _,__(__optional_ _)_) – Invert, Invert vertex group influence

  * **use_symmetry** (_boolean_ _,__(__optional_ _)_) – Symmetry, Maintain symmetry on an axis

  * **symmetry_axis** (enum in [Axis Xyz Items](bpy_types_enum_items/axis_xyz_items.html#rna-enum-axis-xyz-items), (optional)) – Axis, Axis of symmetry

bpy.ops.mesh.delete(_*_ , _type =VERT_)¶

    

Delete selected vertices, edges or faces

Parameters:

    

**type** (enum in [`VERT`, `EDGE`, `FACE`, `EDGE_FACE`, `ONLY_FACE`],
(optional)) – Type, Method used for deleting mesh data

bpy.ops.mesh.delete_edgeloop(_*_ , _use_face_split =True_)¶

    

Delete an edge loop by merging the faces on each side

Parameters:

    

**use_face_split** (_boolean_ _,__(__optional_ _)_) – Face Split, Split off
face corners to maintain surrounding geometry

bpy.ops.mesh.delete_loose(_*_ , _use_verts =True_, _use_edges =True_,
_use_faces =False_)¶

    

Delete loose vertices, edges or faces

Parameters:

    

  * **use_verts** (_boolean_ _,__(__optional_ _)_) – Vertices, Remove loose vertices

  * **use_edges** (_boolean_ _,__(__optional_ _)_) – Edges, Remove loose edges

  * **use_faces** (_boolean_ _,__(__optional_ _)_) – Faces, Remove loose faces

bpy.ops.mesh.dissolve_degenerate(_*_ , _threshold =0.0001_)¶

    

Dissolve zero area faces and zero length edges

Parameters:

    

**threshold** (_float in_ _[__1e-06_ _,__50_ _]__,__(__optional_ _)_) – Merge
Distance, Maximum distance between elements to merge

bpy.ops.mesh.dissolve_edges(_*_ , _use_verts =True_, _angle_threshold
=3.14159_, _use_face_split =False_)¶

    

Dissolve edges, merging faces

Parameters:

    

  * **use_verts** (_boolean_ _,__(__optional_ _)_) – Dissolve Vertices, Dissolve remaining vertices which connect to only two edges

  * **angle_threshold** (_float in_ _[__0_ _,__3.14159_ _]__,__(__optional_ _)_) – Angle Threshold, Remaining vertices which separate edge pairs are preserved if their edge angle exceeds this threshold.

  * **use_face_split** (_boolean_ _,__(__optional_ _)_) – Face Split, Split off face corners to maintain surrounding geometry

bpy.ops.mesh.dissolve_faces(_*_ , _use_verts =False_)¶

    

Dissolve faces

Parameters:

    

**use_verts** (_boolean_ _,__(__optional_ _)_) – Dissolve Vertices, Dissolve
remaining vertices which connect to only two edges

bpy.ops.mesh.dissolve_limited(_*_ , _angle_limit =0.0872665_,
_use_dissolve_boundaries =False_, _delimit ={'NORMAL'}_)¶

    

Dissolve selected edges and vertices, limited by the angle of surrounding
geometry

Parameters:

    

  * **angle_limit** (_float in_ _[__0_ _,__3.14159_ _]__,__(__optional_ _)_) – Max Angle, Angle limit

  * **use_dissolve_boundaries** (_boolean_ _,__(__optional_ _)_) – All Boundaries, Dissolve all vertices in between face boundaries

  * **delimit** (enum set in [Mesh Delimit Mode Items](bpy_types_enum_items/mesh_delimit_mode_items.html#rna-enum-mesh-delimit-mode-items), (optional)) – Delimit, Delimit dissolve operation

bpy.ops.mesh.dissolve_mode(_*_ , _use_verts =False_, _angle_threshold
=3.14159_, _use_face_split =False_, _use_boundary_tear =False_)¶

    

Dissolve geometry based on the selection mode

Parameters:

    

  * **use_verts** (_boolean_ _,__(__optional_ _)_) – Dissolve Vertices, Dissolve remaining vertices which connect to only two edges

  * **angle_threshold** (_float in_ _[__0_ _,__3.14159_ _]__,__(__optional_ _)_) – Angle Threshold, Remaining vertices which separate edge pairs are preserved if their edge angle exceeds this threshold.

  * **use_face_split** (_boolean_ _,__(__optional_ _)_) – Face Split, Split off face corners to maintain surrounding geometry

  * **use_boundary_tear** (_boolean_ _,__(__optional_ _)_) – Tear Boundary, Split off face corners instead of merging faces

bpy.ops.mesh.dissolve_verts(_*_ , _use_face_split =False_, _use_boundary_tear
=False_)¶

    

Dissolve vertices, merge edges and faces

Parameters:

    

  * **use_face_split** (_boolean_ _,__(__optional_ _)_) – Face Split, Split off face corners to maintain surrounding geometry

  * **use_boundary_tear** (_boolean_ _,__(__optional_ _)_) – Tear Boundary, Split off face corners instead of merging faces

bpy.ops.mesh.dupli_extrude_cursor(_*_ , _rotate_source =True_)¶

    

Duplicate and extrude selected vertices, edges or faces towards the mouse
cursor

Parameters:

    

**rotate_source** (_boolean_ _,__(__optional_ _)_) – Rotate Source, Rotate
initial selection giving better shape

bpy.ops.mesh.duplicate(_*_ , _mode =1_)¶

    

Duplicate selected vertices, edges or faces

Parameters:

    

**mode** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Mode

bpy.ops.mesh.duplicate_move(_*_ , _MESH_OT_duplicate =None_,
_TRANSFORM_OT_translate =None_)¶

    

Duplicate mesh and move

Parameters:

    

  * **MESH_OT_duplicate** (`MESH_OT_duplicate`, (optional)) – Duplicate, Duplicate selected vertices, edges or faces

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.mesh.edge_collapse()¶

    

Collapse isolated edge and face regions, merging data such as UVs and color
attributes. This can collapse edge-rings as well as regions of connected faces
into vertices

bpy.ops.mesh.edge_face_add()¶

    

Add an edge or face to selected

bpy.ops.mesh.edge_rotate(_*_ , _use_ccw =False_)¶

    

Rotate selected edge or adjoining faces

Parameters:

    

**use_ccw** (_boolean_ _,__(__optional_ _)_) – Counter Clockwise

bpy.ops.mesh.edge_split(_*_ , _type =EDGE_)¶

    

Split selected edges so that each neighbor face gets its own copy

Parameters:

    

**type** (enum in [`EDGE`, `VERT`], (optional)) –

Type, Method to use for splitting

  * `EDGE` Faces by Edges – Split faces along selected edges.

  * `VERT` Faces & Edges by Vertices – Split faces and edges connected to selected vertices.

bpy.ops.mesh.edgering_select(_*_ , _extend =False_, _deselect =False_, _toggle
=False_, _ring =True_)¶

    

Select an edge ring

Parameters:

    

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend the selection

  * **deselect** (_boolean_ _,__(__optional_ _)_) – Deselect, Remove from the selection

  * **toggle** (_boolean_ _,__(__optional_ _)_) – Toggle Select, Toggle the selection

  * **ring** (_boolean_ _,__(__optional_ _)_) – Select Ring, Select ring

bpy.ops.mesh.edges_select_sharp(_*_ , _sharpness =0.523599_)¶

    

Select all sharp enough edges

Parameters:

    

**sharpness** (_float in_ _[__0.000174533_ _,__3.14159_ _]__,__(__optional_
_)_) – Sharpness

bpy.ops.mesh.extrude_context(_*_ , _use_normal_flip =False_,
_use_dissolve_ortho_edges =False_, _mirror =False_)¶

    

Extrude selection

Parameters:

    

  * **use_normal_flip** (_boolean_ _,__(__optional_ _)_) – Flip Normals

  * **use_dissolve_ortho_edges** (_boolean_ _,__(__optional_ _)_) – Dissolve Orthogonal Edges

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

bpy.ops.mesh.extrude_context_move(_*_ , _MESH_OT_extrude_context =None_,
_TRANSFORM_OT_translate =None_)¶

    

Extrude region together along the average normal

Parameters:

    

  * **MESH_OT_extrude_context** (`MESH_OT_extrude_context`, (optional)) – Extrude Context, Extrude selection

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.mesh.extrude_edges_indiv(_*_ , _use_normal_flip =False_, _mirror
=False_)¶

    

Extrude individual edges only

Parameters:

    

  * **use_normal_flip** (_boolean_ _,__(__optional_ _)_) – Flip Normals

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

bpy.ops.mesh.extrude_edges_move(_*_ , _MESH_OT_extrude_edges_indiv =None_,
_TRANSFORM_OT_translate =None_)¶

    

Extrude edges and move result

Parameters:

    

  * **MESH_OT_extrude_edges_indiv** (`MESH_OT_extrude_edges_indiv`, (optional)) – Extrude Only Edges, Extrude individual edges only

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.mesh.extrude_faces_indiv(_*_ , _mirror =False_)¶

    

Extrude individual faces only

Parameters:

    

**mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

bpy.ops.mesh.extrude_faces_move(_*_ , _MESH_OT_extrude_faces_indiv =None_,
_TRANSFORM_OT_shrink_fatten =None_)¶

    

Extrude each individual face separately along local normals

Parameters:

    

  * **MESH_OT_extrude_faces_indiv** (`MESH_OT_extrude_faces_indiv`, (optional)) – Extrude Individual Faces, Extrude individual faces only

  * **TRANSFORM_OT_shrink_fatten** (`TRANSFORM_OT_shrink_fatten`, (optional)) – Shrink/Fatten, Shrink/fatten selected vertices along normals

bpy.ops.mesh.extrude_manifold(_*_ , _MESH_OT_extrude_region =None_,
_TRANSFORM_OT_translate =None_)¶

    

Extrude, dissolves edges whose faces form a flat surface and intersect new
edges

Parameters:

    

  * **MESH_OT_extrude_region** (`MESH_OT_extrude_region`, (optional)) – Extrude Region, Extrude region of faces

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.mesh.extrude_region(_*_ , _use_normal_flip =False_,
_use_dissolve_ortho_edges =False_, _mirror =False_)¶

    

Extrude region of faces

Parameters:

    

  * **use_normal_flip** (_boolean_ _,__(__optional_ _)_) – Flip Normals

  * **use_dissolve_ortho_edges** (_boolean_ _,__(__optional_ _)_) – Dissolve Orthogonal Edges

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

bpy.ops.mesh.extrude_region_move(_*_ , _MESH_OT_extrude_region =None_,
_TRANSFORM_OT_translate =None_)¶

    

Extrude region and move result

Parameters:

    

  * **MESH_OT_extrude_region** (`MESH_OT_extrude_region`, (optional)) – Extrude Region, Extrude region of faces

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.mesh.extrude_region_shrink_fatten(_*_ , _MESH_OT_extrude_region
=None_, _TRANSFORM_OT_shrink_fatten =None_)¶

    

Extrude region together along local normals

Parameters:

    

  * **MESH_OT_extrude_region** (`MESH_OT_extrude_region`, (optional)) – Extrude Region, Extrude region of faces

  * **TRANSFORM_OT_shrink_fatten** (`TRANSFORM_OT_shrink_fatten`, (optional)) – Shrink/Fatten, Shrink/fatten selected vertices along normals

bpy.ops.mesh.extrude_repeat(_*_ , _steps =10_, _offset =(0.0, 0.0, 0.0)_,
_scale_offset =1.0_)¶

    

Extrude selected vertices, edges or faces repeatedly

Parameters:

    

  * **steps** (_int in_ _[__0_ _,__1000000_ _]__,__(__optional_ _)_) – Steps

  * **offset** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-100000, 100000], (optional)) – Offset, Offset vector

  * **scale_offset** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Scale Offset

bpy.ops.mesh.extrude_vertices_move(_*_ , _MESH_OT_extrude_verts_indiv =None_,
_TRANSFORM_OT_translate =None_)¶

    

Extrude vertices and move result

Parameters:

    

  * **MESH_OT_extrude_verts_indiv** (`MESH_OT_extrude_verts_indiv`, (optional)) – Extrude Only Vertices, Extrude individual vertices only

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.mesh.extrude_verts_indiv(_*_ , _mirror =False_)¶

    

Extrude individual vertices only

Parameters:

    

**mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

bpy.ops.mesh.face_make_planar(_*_ , _factor =1.0_, _repeat =1_)¶

    

Flatten selected faces

Parameters:

    

  * **factor** (_float in_ _[__-10_ _,__10_ _]__,__(__optional_ _)_) – Factor

  * **repeat** (_int in_ _[__1_ _,__10000_ _]__,__(__optional_ _)_) – Iterations

bpy.ops.mesh.face_split_by_edges()¶

    

Weld loose edges into faces (splitting them into new faces)

bpy.ops.mesh.faces_mirror_uv(_*_ , _direction =POSITIVE_, _precision =3_)¶

    

Copy mirror UV coordinates on the X axis based on a mirrored mesh

Parameters:

    

  * **direction** (enum in [`POSITIVE`, `NEGATIVE`], (optional)) – Axis Direction

  * **precision** (_int in_ _[__1_ _,__16_ _]__,__(__optional_ _)_) – Precision, Tolerance for finding vertex duplicates

File:

    

[startup/bl_operators/mesh.py:134](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/mesh.py#L134)

bpy.ops.mesh.faces_select_linked_flat(_*_ , _sharpness =0.0174533_)¶

    

Select linked faces by angle

Parameters:

    

**sharpness** (_float in_ _[__0.000174533_ _,__3.14159_ _]__,__(__optional_
_)_) – Sharpness

bpy.ops.mesh.faces_shade_flat()¶

    

Display faces flat

bpy.ops.mesh.faces_shade_smooth()¶

    

Display faces smooth (using vertex normals)

bpy.ops.mesh.fill(_*_ , _use_beauty =True_)¶

    

Fill a selected edge loop with faces

Parameters:

    

**use_beauty** (_boolean_ _,__(__optional_ _)_) – Beauty, Use best
triangulation division

bpy.ops.mesh.fill_grid(_*_ , _span =1_, _offset =0_, _use_interp_simple
=False_)¶

    

Fill grid from two loops

Parameters:

    

  * **span** (_int in_ _[__1_ _,__1000_ _]__,__(__optional_ _)_) – Span, Number of grid columns

  * **offset** (_int in_ _[__-1000_ _,__1000_ _]__,__(__optional_ _)_) – Offset, Vertex that is the corner of the grid

  * **use_interp_simple** (_boolean_ _,__(__optional_ _)_) – Simple Blending, Use simple interpolation of grid vertices

bpy.ops.mesh.fill_holes(_*_ , _sides =4_)¶

    

Fill in holes (boundary edge loops)

Parameters:

    

**sides** (_int in_ _[__0_ _,__1000_ _]__,__(__optional_ _)_) – Sides, Number
of sides in hole required to fill (zero fills all holes)

bpy.ops.mesh.flip_normals(_*_ , _only_clnors =False_)¶

    

Flip the direction of selected faces’ normals (and of their vertices)

Parameters:

    

**only_clnors** (_boolean_ _,__(__optional_ _)_) – Custom Normals Only, Only
flip the custom loop normals of the selected elements

bpy.ops.mesh.flip_quad_tessellation()¶

    

Flips the tessellation of selected quads

bpy.ops.mesh.hide(_*_ , _unselected =False_)¶

    

Hide (un)selected vertices, edges or faces

Parameters:

    

**unselected** (_boolean_ _,__(__optional_ _)_) – Unselected, Hide unselected
rather than selected

bpy.ops.mesh.inset(_*_ , _use_boundary =True_, _use_even_offset =True_,
_use_relative_offset =False_, _use_edge_rail =False_, _thickness =0.0_, _depth
=0.0_, _use_outset =False_, _use_select_inset =False_, _use_individual
=False_, _use_interpolate =True_, _release_confirm =False_)¶

    

Inset new faces into selected faces

Parameters:

    

  * **use_boundary** (_boolean_ _,__(__optional_ _)_) – Boundary, Inset face boundaries

  * **use_even_offset** (_boolean_ _,__(__optional_ _)_) – Offset Even, Scale the offset to give more even thickness

  * **use_relative_offset** (_boolean_ _,__(__optional_ _)_) – Offset Relative, Scale the offset by surrounding geometry

  * **use_edge_rail** (_boolean_ _,__(__optional_ _)_) – Edge Rail, Inset the region along existing edges

  * **thickness** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Thickness

  * **depth** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Depth

  * **use_outset** (_boolean_ _,__(__optional_ _)_) – Outset, Outset rather than inset

  * **use_select_inset** (_boolean_ _,__(__optional_ _)_) – Select Outer, Select the new inset faces

  * **use_individual** (_boolean_ _,__(__optional_ _)_) – Individual, Individual face inset

  * **use_interpolate** (_boolean_ _,__(__optional_ _)_) – Interpolate, Blend face data across the inset

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release

bpy.ops.mesh.intersect(_*_ , _mode =SELECT_UNSELECT_, _separate_mode =CUT_,
_threshold =1e-06_, _solver =EXACT_)¶

    

Cut an intersection into faces

Parameters:

    

  * **mode** (enum in [`SELECT`, `SELECT_UNSELECT`], (optional)) – 

Source

    * `SELECT` Self Intersect – Self intersect selected faces.

    * `SELECT_UNSELECT` Selected/Unselected – Intersect selected with unselected faces.

  * **separate_mode** (enum in [`ALL`, `CUT`, `NONE`], (optional)) – 

Separate Mode

    * `ALL` All – Separate all geometry from intersections.

    * `CUT` Cut – Cut into geometry keeping each side separate (Selected/Unselected only).

    * `NONE` Merge – Merge all geometry from the intersection.

  * **threshold** (_float in_ _[__0_ _,__0.01_ _]__,__(__optional_ _)_) – Merge Threshold

  * **solver** (enum in [`FAST`, `EXACT`], (optional)) – 

Solver, Which Intersect solver to use

    * `FAST` Float – Simple solver with good performance, without support for overlapping geometry.

    * `EXACT` Exact – Slower solver with the best results for coplanar faces.

bpy.ops.mesh.intersect_boolean(_*_ , _operation =DIFFERENCE_, _use_swap
=False_, _use_self =False_, _threshold =1e-06_, _solver =EXACT_)¶

    

Cut solid geometry from selected to unselected

Parameters:

    

  * **operation** (enum in [`INTERSECT`, `UNION`, `DIFFERENCE`], (optional)) – Boolean Operation, Which boolean operation to apply

  * **use_swap** (_boolean_ _,__(__optional_ _)_) – Swap, Use with difference intersection to swap which side is kept

  * **use_self** (_boolean_ _,__(__optional_ _)_) – Self Intersection, Do self-union or self-intersection

  * **threshold** (_float in_ _[__0_ _,__0.01_ _]__,__(__optional_ _)_) – Merge Threshold

  * **solver** (enum in [`FAST`, `EXACT`], (optional)) – 

Solver, Which Boolean solver to use

    * `FAST` Fast – Faster solver, some limitations.

    * `EXACT` Exact – Exact solver, slower, handles more cases.

bpy.ops.mesh.knife_project(_*_ , _cut_through =False_)¶

    

Use other objects outlines and boundaries to project knife cuts

Parameters:

    

**cut_through** (_boolean_ _,__(__optional_ _)_) – Cut Through, Cut through
all faces, not just visible ones

bpy.ops.mesh.knife_tool(_*_ , _use_occlude_geometry =True_, _only_selected
=False_, _xray =True_, _visible_measurements =NONE_, _angle_snapping =NONE_,
_angle_snapping_increment =0.523599_, _wait_for_input =True_)¶

    

Cut new topology

Parameters:

    

  * **use_occlude_geometry** (_boolean_ _,__(__optional_ _)_) – Occlude Geometry, Only cut the front most geometry

  * **only_selected** (_boolean_ _,__(__optional_ _)_) – Only Selected, Only cut selected geometry

  * **xray** (_boolean_ _,__(__optional_ _)_) – X-Ray, Show cuts hidden by geometry

  * **visible_measurements** (enum in [`NONE`, `BOTH`, `DISTANCE`, `ANGLE`], (optional)) – 

Measurements, Visible distance and angle measurements

    * `NONE` None – Show no measurements.

    * `BOTH` Both – Show both distances and angles.

    * `DISTANCE` Distance – Show just distance measurements.

    * `ANGLE` Angle – Show just angle measurements.

  * **angle_snapping** (enum in [`NONE`, `SCREEN`, `RELATIVE`], (optional)) – 

Angle Snapping, Angle snapping mode

    * `NONE` None – No angle snapping.

    * `SCREEN` Screen – Screen space angle snapping.

    * `RELATIVE` Relative – Angle snapping relative to the previous cut edge.

  * **angle_snapping_increment** (_float in_ _[__0_ _,__3.14159_ _]__,__(__optional_ _)_) – Angle Snap Increment, The angle snap increment used when in constrained angle mode

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

bpy.ops.mesh.loop_multi_select(_*_ , _ring =False_)¶

    

Select a loop of connected edges by connection type

Parameters:

    

**ring** (_boolean_ _,__(__optional_ _)_) – Ring

bpy.ops.mesh.loop_select(_*_ , _extend =False_, _deselect =False_, _toggle
=False_, _ring =False_)¶

    

Select a loop of connected edges

Parameters:

    

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend Select, Extend the selection

  * **deselect** (_boolean_ _,__(__optional_ _)_) – Deselect, Remove from the selection

  * **toggle** (_boolean_ _,__(__optional_ _)_) – Toggle Select, Toggle the selection

  * **ring** (_boolean_ _,__(__optional_ _)_) – Select Ring, Select ring

bpy.ops.mesh.loop_to_region(_*_ , _select_bigger =False_)¶

    

Select region of faces inside of a selected loop of edges

Parameters:

    

**select_bigger** (_boolean_ _,__(__optional_ _)_) – Select Bigger, Select
bigger regions instead of smaller ones

bpy.ops.mesh.loopcut(_*_ , _number_cuts =1_, _smoothness =0.0_, _falloff
=INVERSE_SQUARE_, _object_index =-1_, _edge_index =-1_, _mesh_select_mode_init
=(False, False, False)_)¶

    

Add a new loop between existing loops

Parameters:

    

  * **number_cuts** (_int in_ _[__1_ _,__1000000_ _]__,__(__optional_ _)_) – Number of Cuts

  * **smoothness** (_float in_ _[__-1000_ _,__1000_ _]__,__(__optional_ _)_) – Smoothness, Smoothness factor

  * **falloff** (enum in [Proportional Falloff Curve Only Items](bpy_types_enum_items/proportional_falloff_curve_only_items.html#rna-enum-proportional-falloff-curve-only-items), (optional)) – Falloff, Falloff type of the feather

  * **object_index** (_int in_ _[__-1_ _,__inf_ _]__,__(__optional_ _)_) – Object Index

  * **edge_index** (_int in_ _[__-1_ _,__inf_ _]__,__(__optional_ _)_) – Edge Index

bpy.ops.mesh.loopcut_slide(_*_ , _MESH_OT_loopcut =None_,
_TRANSFORM_OT_edge_slide =None_)¶

    

Cut mesh loop and slide it

Parameters:

    

  * **MESH_OT_loopcut** (`MESH_OT_loopcut`, (optional)) – Loop Cut, Add a new loop between existing loops

  * **TRANSFORM_OT_edge_slide** (`TRANSFORM_OT_edge_slide`, (optional)) – Edge Slide, Slide an edge loop along a mesh

bpy.ops.mesh.mark_freestyle_edge(_*_ , _clear =False_)¶

    

(Un)mark selected edges as Freestyle feature edges

Parameters:

    

**clear** (_boolean_ _,__(__optional_ _)_) – Clear

bpy.ops.mesh.mark_freestyle_face(_*_ , _clear =False_)¶

    

(Un)mark selected faces for exclusion from Freestyle feature edge detection

Parameters:

    

**clear** (_boolean_ _,__(__optional_ _)_) – Clear

bpy.ops.mesh.mark_seam(_*_ , _clear =False_)¶

    

(Un)mark selected edges as a seam

Parameters:

    

**clear** (_boolean_ _,__(__optional_ _)_) – Clear

bpy.ops.mesh.mark_sharp(_*_ , _clear =False_, _use_verts =False_)¶

    

(Un)mark selected edges as sharp

Parameters:

    

  * **clear** (_boolean_ _,__(__optional_ _)_) – Clear

  * **use_verts** (_boolean_ _,__(__optional_ _)_) – Vertices, Consider vertices instead of edges to select which edges to (un)tag as sharp

bpy.ops.mesh.merge(_*_ , _type =CENTER_, _uvs =False_)¶

    

Merge selected vertices

Parameters:

    

  * **type** (enum in [`CENTER`, `CURSOR`, `COLLAPSE`, `FIRST`, `LAST`], (optional)) – Type, Merge method to use

  * **uvs** (_boolean_ _,__(__optional_ _)_) – UVs, Move UVs according to merge

bpy.ops.mesh.merge_normals()¶

    

Merge custom normals of selected vertices

bpy.ops.mesh.mod_weighted_strength(_*_ , _set =False_, _face_strength
=MEDIUM_)¶

    

Set/Get strength of face (used in Weighted Normal modifier)

Parameters:

    

  * **set** (_boolean_ _,__(__optional_ _)_) – Set Value, Set value of faces

  * **face_strength** (enum in [`WEAK`, `MEDIUM`, `STRONG`], (optional)) – Face Strength, Strength to use for assigning or selecting face influence for weighted normal modifier

bpy.ops.mesh.normals_make_consistent(_*_ , _inside =False_)¶

    

Make face and vertex normals point either outside or inside the mesh

Parameters:

    

**inside** (_boolean_ _,__(__optional_ _)_) – Inside

bpy.ops.mesh.normals_tools(_*_ , _mode =COPY_, _absolute =False_)¶

    

Custom normals tools using Normal Vector of UI

Parameters:

    

  * **mode** (enum in [`COPY`, `PASTE`, `ADD`, `MULTIPLY`, `RESET`], (optional)) – 

Mode, Mode of tools taking input from interface

    * `COPY` Copy Normal – Copy normal to the internal clipboard.

    * `PASTE` Paste Normal – Paste normal from the internal clipboard.

    * `ADD` Add Normal – Add normal vector with selection.

    * `MULTIPLY` Multiply Normal – Multiply normal vector with selection.

    * `RESET` Reset Normal – Reset the internal clipboard and/or normal of selected element.

  * **absolute** (_boolean_ _,__(__optional_ _)_) – Absolute Coordinates, Copy Absolute coordinates of Normal vector

bpy.ops.mesh.offset_edge_loops(_*_ , _use_cap_endpoint =False_)¶

    

Create offset edge loop from the current selection

Parameters:

    

**use_cap_endpoint** (_boolean_ _,__(__optional_ _)_) – Cap Endpoint, Extend
loop around end-points

bpy.ops.mesh.offset_edge_loops_slide(_*_ , _MESH_OT_offset_edge_loops =None_,
_TRANSFORM_OT_edge_slide =None_)¶

    

Offset edge loop slide

Parameters:

    

  * **MESH_OT_offset_edge_loops** (`MESH_OT_offset_edge_loops`, (optional)) – Offset Edge Loop, Create offset edge loop from the current selection

  * **TRANSFORM_OT_edge_slide** (`TRANSFORM_OT_edge_slide`, (optional)) – Edge Slide, Slide an edge loop along a mesh

bpy.ops.mesh.point_normals(_*_ , _mode =COORDINATES_, _invert =False_, _align
=False_, _target_location =(0.0, 0.0, 0.0)_, _spherize =False_,
_spherize_strength =0.1_)¶

    

Point selected custom normals to specified Target

Parameters:

    

  * **mode** (enum in [`COORDINATES`, `MOUSE`], (optional)) – 

Mode, How to define coordinates to point custom normals to

    * `COORDINATES` Coordinates – Use static coordinates (defined by various means).

    * `MOUSE` Mouse – Follow mouse cursor.

  * **invert** (_boolean_ _,__(__optional_ _)_) – Invert, Invert affected normals

  * **align** (_boolean_ _,__(__optional_ _)_) – Align, Make all affected normals parallel

  * **target_location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Target, Target location to which normals will point

  * **spherize** (_boolean_ _,__(__optional_ _)_) – Spherize, Interpolate between original and new normals

  * **spherize_strength** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Spherize Strength, Ratio of spherized normal to original normal

bpy.ops.mesh.poke(_*_ , _offset =0.0_, _use_relative_offset =False_,
_center_mode =MEDIAN_WEIGHTED_)¶

    

Split a face into a fan

Parameters:

    

  * **offset** (_float in_ _[__-1000_ _,__1000_ _]__,__(__optional_ _)_) – Poke Offset, Poke Offset

  * **use_relative_offset** (_boolean_ _,__(__optional_ _)_) – Offset Relative, Scale the offset by surrounding geometry

  * **center_mode** (enum in [`MEDIAN_WEIGHTED`, `MEDIAN`, `BOUNDS`], (optional)) – 

Poke Center, Poke face center calculation

    * `MEDIAN_WEIGHTED` Weighted Median – Weighted median face center.

    * `MEDIAN` Median – Median face center.

    * `BOUNDS` Bounds – Face bounds center.

bpy.ops.mesh.polybuild_delete_at_cursor(_*_ , _mirror =False_,
_use_proportional_edit =False_, _proportional_edit_falloff =SMOOTH_,
_proportional_size =1.0_, _use_proportional_connected =False_,
_use_proportional_projected =False_, _release_confirm =False_, _use_accurate
=False_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

  * **use_proportional_edit** (_boolean_ _,__(__optional_ _)_) – Proportional Editing

  * **proportional_edit_falloff** (enum in [Proportional Falloff Items](bpy_types_enum_items/proportional_falloff_items.html#rna-enum-proportional-falloff-items), (optional)) – Proportional Falloff, Falloff type for proportional editing mode

  * **proportional_size** (_float in_ _[__1e-06_ _,__inf_ _]__,__(__optional_ _)_) – Proportional Size

  * **use_proportional_connected** (_boolean_ _,__(__optional_ _)_) – Connected

  * **use_proportional_projected** (_boolean_ _,__(__optional_ _)_) – Projected (2D)

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

bpy.ops.mesh.polybuild_dissolve_at_cursor()¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

bpy.ops.mesh.polybuild_extrude_at_cursor_move(_*_ ,
_MESH_OT_polybuild_transform_at_cursor =None_, _MESH_OT_extrude_edges_indiv
=None_, _TRANSFORM_OT_translate =None_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

  * **MESH_OT_polybuild_transform_at_cursor** (`MESH_OT_polybuild_transform_at_cursor`, (optional)) – Poly Build Transform at Cursor

  * **MESH_OT_extrude_edges_indiv** (`MESH_OT_extrude_edges_indiv`, (optional)) – Extrude Only Edges, Extrude individual edges only

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.mesh.polybuild_face_at_cursor(_*_ , _create_quads =True_, _mirror
=False_, _use_proportional_edit =False_, _proportional_edit_falloff =SMOOTH_,
_proportional_size =1.0_, _use_proportional_connected =False_,
_use_proportional_projected =False_, _release_confirm =False_, _use_accurate
=False_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

  * **create_quads** (_boolean_ _,__(__optional_ _)_) – Create Quads, Automatically split edges in triangles to maintain quad topology

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

  * **use_proportional_edit** (_boolean_ _,__(__optional_ _)_) – Proportional Editing

  * **proportional_edit_falloff** (enum in [Proportional Falloff Items](bpy_types_enum_items/proportional_falloff_items.html#rna-enum-proportional-falloff-items), (optional)) – Proportional Falloff, Falloff type for proportional editing mode

  * **proportional_size** (_float in_ _[__1e-06_ _,__inf_ _]__,__(__optional_ _)_) – Proportional Size

  * **use_proportional_connected** (_boolean_ _,__(__optional_ _)_) – Connected

  * **use_proportional_projected** (_boolean_ _,__(__optional_ _)_) – Projected (2D)

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

bpy.ops.mesh.polybuild_face_at_cursor_move(_*_ ,
_MESH_OT_polybuild_face_at_cursor =None_, _TRANSFORM_OT_translate =None_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

  * **MESH_OT_polybuild_face_at_cursor** (`MESH_OT_polybuild_face_at_cursor`, (optional)) – Poly Build Face at Cursor

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.mesh.polybuild_split_at_cursor(_*_ , _mirror =False_,
_use_proportional_edit =False_, _proportional_edit_falloff =SMOOTH_,
_proportional_size =1.0_, _use_proportional_connected =False_,
_use_proportional_projected =False_, _release_confirm =False_, _use_accurate
=False_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

  * **use_proportional_edit** (_boolean_ _,__(__optional_ _)_) – Proportional Editing

  * **proportional_edit_falloff** (enum in [Proportional Falloff Items](bpy_types_enum_items/proportional_falloff_items.html#rna-enum-proportional-falloff-items), (optional)) – Proportional Falloff, Falloff type for proportional editing mode

  * **proportional_size** (_float in_ _[__1e-06_ _,__inf_ _]__,__(__optional_ _)_) – Proportional Size

  * **use_proportional_connected** (_boolean_ _,__(__optional_ _)_) – Connected

  * **use_proportional_projected** (_boolean_ _,__(__optional_ _)_) – Projected (2D)

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

bpy.ops.mesh.polybuild_split_at_cursor_move(_*_ ,
_MESH_OT_polybuild_split_at_cursor =None_, _TRANSFORM_OT_translate =None_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

  * **MESH_OT_polybuild_split_at_cursor** (`MESH_OT_polybuild_split_at_cursor`, (optional)) – Poly Build Split at Cursor

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.mesh.polybuild_transform_at_cursor(_*_ , _mirror =False_,
_use_proportional_edit =False_, _proportional_edit_falloff =SMOOTH_,
_proportional_size =1.0_, _use_proportional_connected =False_,
_use_proportional_projected =False_, _release_confirm =False_, _use_accurate
=False_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

  * **use_proportional_edit** (_boolean_ _,__(__optional_ _)_) – Proportional Editing

  * **proportional_edit_falloff** (enum in [Proportional Falloff Items](bpy_types_enum_items/proportional_falloff_items.html#rna-enum-proportional-falloff-items), (optional)) – Proportional Falloff, Falloff type for proportional editing mode

  * **proportional_size** (_float in_ _[__1e-06_ _,__inf_ _]__,__(__optional_ _)_) – Proportional Size

  * **use_proportional_connected** (_boolean_ _,__(__optional_ _)_) – Connected

  * **use_proportional_projected** (_boolean_ _,__(__optional_ _)_) – Projected (2D)

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

bpy.ops.mesh.polybuild_transform_at_cursor_move(_*_ ,
_MESH_OT_polybuild_transform_at_cursor =None_, _TRANSFORM_OT_translate
=None_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

  * **MESH_OT_polybuild_transform_at_cursor** (`MESH_OT_polybuild_transform_at_cursor`, (optional)) – Poly Build Transform at Cursor

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.mesh.primitive_circle_add(_*_ , _vertices =32_, _radius =1.0_,
_fill_type =NOTHING_, _calc_uvs =True_, _enter_editmode =False_, _align
=WORLD_, _location =(0.0, 0.0, 0.0)_, _rotation =(0.0, 0.0, 0.0)_, _scale
=(0.0, 0.0, 0.0)_)¶

    

Construct a circle mesh

Parameters:

    

  * **vertices** (_int in_ _[__3_ _,__10000000_ _]__,__(__optional_ _)_) – Vertices

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **fill_type** (enum in [`NOTHING`, `NGON`, `TRIFAN`], (optional)) – 

Fill Type

    * `NOTHING` Nothing – Don’t fill at all.

    * `NGON` N-Gon – Use n-gons.

    * `TRIFAN` Triangle Fan – Use triangle fans.

  * **calc_uvs** (_boolean_ _,__(__optional_ _)_) – Generate UVs, Generate a default UV map

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.mesh.primitive_cone_add(_*_ , _vertices =32_, _radius1 =1.0_, _radius2
=0.0_, _depth =2.0_, _end_fill_type =NGON_, _calc_uvs =True_, _enter_editmode
=False_, _align =WORLD_, _location =(0.0, 0.0, 0.0)_, _rotation =(0.0, 0.0,
0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Construct a conic mesh

Parameters:

    

  * **vertices** (_int in_ _[__3_ _,__10000000_ _]__,__(__optional_ _)_) – Vertices

  * **radius1** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius 1

  * **radius2** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius 2

  * **depth** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Depth

  * **end_fill_type** (enum in [`NOTHING`, `NGON`, `TRIFAN`], (optional)) – 

Base Fill Type

    * `NOTHING` Nothing – Don’t fill at all.

    * `NGON` N-Gon – Use n-gons.

    * `TRIFAN` Triangle Fan – Use triangle fans.

  * **calc_uvs** (_boolean_ _,__(__optional_ _)_) – Generate UVs, Generate a default UV map

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.mesh.primitive_cube_add(_*_ , _size =2.0_, _calc_uvs =True_,
_enter_editmode =False_, _align =WORLD_, _location =(0.0, 0.0, 0.0)_,
_rotation =(0.0, 0.0, 0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Construct a cube mesh that consists of six square faces

Parameters:

    

  * **size** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Size

  * **calc_uvs** (_boolean_ _,__(__optional_ _)_) – Generate UVs, Generate a default UV map

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.mesh.primitive_cube_add_gizmo(_*_ , _calc_uvs =True_, _enter_editmode
=False_, _align =WORLD_, _location =(0.0, 0.0, 0.0)_, _rotation =(0.0, 0.0,
0.0)_, _scale =(0.0, 0.0, 0.0)_, _matrix =((0.0, 0.0, 0.0, 0.0), (0.0, 0.0,
0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))_)¶

    

Construct a cube mesh

Parameters:

    

  * **calc_uvs** (_boolean_ _,__(__optional_ _)_) – Generate UVs, Generate a default UV map

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

  * **matrix** ([`mathutils.Matrix`](mathutils.html#mathutils.Matrix "mathutils.Matrix") of 4 * 4 items in [-inf, inf], (optional)) – Matrix

bpy.ops.mesh.primitive_cylinder_add(_*_ , _vertices =32_, _radius =1.0_,
_depth =2.0_, _end_fill_type =NGON_, _calc_uvs =True_, _enter_editmode
=False_, _align =WORLD_, _location =(0.0, 0.0, 0.0)_, _rotation =(0.0, 0.0,
0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Construct a cylinder mesh

Parameters:

    

  * **vertices** (_int in_ _[__3_ _,__10000000_ _]__,__(__optional_ _)_) – Vertices

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **depth** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Depth

  * **end_fill_type** (enum in [`NOTHING`, `NGON`, `TRIFAN`], (optional)) – 

Cap Fill Type

    * `NOTHING` Nothing – Don’t fill at all.

    * `NGON` N-Gon – Use n-gons.

    * `TRIFAN` Triangle Fan – Use triangle fans.

  * **calc_uvs** (_boolean_ _,__(__optional_ _)_) – Generate UVs, Generate a default UV map

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.mesh.primitive_grid_add(_*_ , _x_subdivisions =10_, _y_subdivisions
=10_, _size =2.0_, _calc_uvs =True_, _enter_editmode =False_, _align =WORLD_,
_location =(0.0, 0.0, 0.0)_, _rotation =(0.0, 0.0, 0.0)_, _scale =(0.0, 0.0,
0.0)_)¶

    

Construct a subdivided plane mesh

Parameters:

    

  * **x_subdivisions** (_int in_ _[__1_ _,__10000000_ _]__,__(__optional_ _)_) – X Subdivisions

  * **y_subdivisions** (_int in_ _[__1_ _,__10000000_ _]__,__(__optional_ _)_) – Y Subdivisions

  * **size** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Size

  * **calc_uvs** (_boolean_ _,__(__optional_ _)_) – Generate UVs, Generate a default UV map

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.mesh.primitive_ico_sphere_add(_*_ , _subdivisions =2_, _radius =1.0_,
_calc_uvs =True_, _enter_editmode =False_, _align =WORLD_, _location =(0.0,
0.0, 0.0)_, _rotation =(0.0, 0.0, 0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Construct a spherical mesh that consists of equally sized triangles

Parameters:

    

  * **subdivisions** (_int in_ _[__1_ _,__10_ _]__,__(__optional_ _)_) – Subdivisions

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **calc_uvs** (_boolean_ _,__(__optional_ _)_) – Generate UVs, Generate a default UV map

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.mesh.primitive_monkey_add(_*_ , _size =2.0_, _calc_uvs =True_,
_enter_editmode =False_, _align =WORLD_, _location =(0.0, 0.0, 0.0)_,
_rotation =(0.0, 0.0, 0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Construct a Suzanne mesh

Parameters:

    

  * **size** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Size

  * **calc_uvs** (_boolean_ _,__(__optional_ _)_) – Generate UVs, Generate a default UV map

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.mesh.primitive_plane_add(_*_ , _size =2.0_, _calc_uvs =True_,
_enter_editmode =False_, _align =WORLD_, _location =(0.0, 0.0, 0.0)_,
_rotation =(0.0, 0.0, 0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Construct a filled planar mesh with 4 vertices

Parameters:

    

  * **size** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Size

  * **calc_uvs** (_boolean_ _,__(__optional_ _)_) – Generate UVs, Generate a default UV map

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.mesh.primitive_torus_add(_*_ , _align =WORLD_, _location =(0.0, 0.0,
0.0)_, _rotation =(0.0, 0.0, 0.0)_, _major_segments =48_, _minor_segments
=12_, _mode =MAJOR_MINOR_, _major_radius =1.0_, _minor_radius =0.25_,
_abso_major_rad =1.25_, _abso_minor_rad =0.75_, _generate_uvs =True_)¶

    

Construct a torus mesh

Parameters:

    

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation

  * **major_segments** (_int in_ _[__3_ _,__256_ _]__,__(__optional_ _)_) – Major Segments, Number of segments for the main ring of the torus

  * **minor_segments** (_int in_ _[__3_ _,__256_ _]__,__(__optional_ _)_) – Minor Segments, Number of segments for the minor ring of the torus

  * **mode** (enum in [`MAJOR_MINOR`, `EXT_INT`], (optional)) – 

Dimensions Mode

    * `MAJOR_MINOR` Major/Minor – Use the major/minor radii for torus dimensions.

    * `EXT_INT` Exterior/Interior – Use the exterior/interior radii for torus dimensions.

  * **major_radius** (_float in_ _[__0_ _,__10000_ _]__,__(__optional_ _)_) – Major Radius, Radius from the origin to the center of the cross sections

  * **minor_radius** (_float in_ _[__0_ _,__10000_ _]__,__(__optional_ _)_) – Minor Radius, Radius of the torus’ cross section

  * **abso_major_rad** (_float in_ _[__0_ _,__10000_ _]__,__(__optional_ _)_) – Exterior Radius, Total Exterior Radius of the torus

  * **abso_minor_rad** (_float in_ _[__0_ _,__10000_ _]__,__(__optional_ _)_) – Interior Radius, Total Interior Radius of the torus

  * **generate_uvs** (_boolean_ _,__(__optional_ _)_) – Generate UVs, Generate a default UV map

File:

    

[startup/bl_operators/add_mesh_torus.py:222](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/add_mesh_torus.py#L222)

bpy.ops.mesh.primitive_uv_sphere_add(_*_ , _segments =32_, _ring_count =16_,
_radius =1.0_, _calc_uvs =True_, _enter_editmode =False_, _align =WORLD_,
_location =(0.0, 0.0, 0.0)_, _rotation =(0.0, 0.0, 0.0)_, _scale =(0.0, 0.0,
0.0)_)¶

    

Construct a spherical mesh with quad faces, except for triangle faces at the
top and bottom

Parameters:

    

  * **segments** (_int in_ _[__3_ _,__100000_ _]__,__(__optional_ _)_) – Segments

  * **ring_count** (_int in_ _[__3_ _,__100000_ _]__,__(__optional_ _)_) – Rings

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **calc_uvs** (_boolean_ _,__(__optional_ _)_) – Generate UVs, Generate a default UV map

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.mesh.quads_convert_to_tris(_*_ , _quad_method =BEAUTY_, _ngon_method
=BEAUTY_)¶

    

Triangulate selected faces

Parameters:

    

  * **quad_method** (enum in [Modifier Triangulate Quad Method Items](bpy_types_enum_items/modifier_triangulate_quad_method_items.html#rna-enum-modifier-triangulate-quad-method-items), (optional)) – Quad Method, Method for splitting the quads into triangles

  * **ngon_method** (enum in [Modifier Triangulate Ngon Method Items](bpy_types_enum_items/modifier_triangulate_ngon_method_items.html#rna-enum-modifier-triangulate-ngon-method-items), (optional)) – N-gon Method, Method for splitting the n-gons into triangles

bpy.ops.mesh.region_to_loop()¶

    

Select boundary edges around the selected faces

bpy.ops.mesh.remove_doubles(_*_ , _threshold =0.0001_, _use_unselected
=False_, _use_sharp_edge_from_normals =False_)¶

    

Merge vertices based on their proximity

Parameters:

    

  * **threshold** (_float in_ _[__1e-06_ _,__50_ _]__,__(__optional_ _)_) – Merge Distance, Maximum distance between elements to merge

  * **use_unselected** (_boolean_ _,__(__optional_ _)_) – Unselected, Merge selected to other unselected vertices

  * **use_sharp_edge_from_normals** (_boolean_ _,__(__optional_ _)_) – Sharp Edges, Calculate sharp edges using custom normal data (when available)

bpy.ops.mesh.reveal(_*_ , _select =True_)¶

    

Reveal all hidden vertices, edges and faces

Parameters:

    

**select** (_boolean_ _,__(__optional_ _)_) – Select

bpy.ops.mesh.rip(_*_ , _mirror =False_, _use_proportional_edit =False_,
_proportional_edit_falloff =SMOOTH_, _proportional_size =1.0_,
_use_proportional_connected =False_, _use_proportional_projected =False_,
_release_confirm =False_, _use_accurate =False_, _use_fill =False_)¶

    

Disconnect vertex or edges from connected geometry

Parameters:

    

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

  * **use_proportional_edit** (_boolean_ _,__(__optional_ _)_) – Proportional Editing

  * **proportional_edit_falloff** (enum in [Proportional Falloff Items](bpy_types_enum_items/proportional_falloff_items.html#rna-enum-proportional-falloff-items), (optional)) – Proportional Falloff, Falloff type for proportional editing mode

  * **proportional_size** (_float in_ _[__1e-06_ _,__inf_ _]__,__(__optional_ _)_) – Proportional Size

  * **use_proportional_connected** (_boolean_ _,__(__optional_ _)_) – Connected

  * **use_proportional_projected** (_boolean_ _,__(__optional_ _)_) – Projected (2D)

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

  * **use_fill** (_boolean_ _,__(__optional_ _)_) – Fill, Fill the ripped region

bpy.ops.mesh.rip_edge(_*_ , _mirror =False_, _use_proportional_edit =False_,
_proportional_edit_falloff =SMOOTH_, _proportional_size =1.0_,
_use_proportional_connected =False_, _use_proportional_projected =False_,
_release_confirm =False_, _use_accurate =False_)¶

    

Extend vertices along the edge closest to the cursor

Parameters:

    

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

  * **use_proportional_edit** (_boolean_ _,__(__optional_ _)_) – Proportional Editing

  * **proportional_edit_falloff** (enum in [Proportional Falloff Items](bpy_types_enum_items/proportional_falloff_items.html#rna-enum-proportional-falloff-items), (optional)) – Proportional Falloff, Falloff type for proportional editing mode

  * **proportional_size** (_float in_ _[__1e-06_ _,__inf_ _]__,__(__optional_ _)_) – Proportional Size

  * **use_proportional_connected** (_boolean_ _,__(__optional_ _)_) – Connected

  * **use_proportional_projected** (_boolean_ _,__(__optional_ _)_) – Projected (2D)

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

bpy.ops.mesh.rip_edge_move(_*_ , _MESH_OT_rip_edge =None_,
_TRANSFORM_OT_translate =None_)¶

    

Extend vertices and move the result

Parameters:

    

  * **MESH_OT_rip_edge** (`MESH_OT_rip_edge`, (optional)) – Extend Vertices, Extend vertices along the edge closest to the cursor

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.mesh.rip_move(_*_ , _MESH_OT_rip =None_, _TRANSFORM_OT_translate
=None_)¶

    

Rip polygons and move the result

Parameters:

    

  * **MESH_OT_rip** (`MESH_OT_rip`, (optional)) – Rip, Disconnect vertex or edges from connected geometry

  * **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.mesh.screw(_*_ , _steps =9_, _turns =1_, _center =(0.0, 0.0, 0.0)_,
_axis =(0.0, 0.0, 0.0)_)¶

    

Extrude selected vertices in screw-shaped rotation around the cursor in
indicated viewport

Parameters:

    

  * **steps** (_int in_ _[__1_ _,__100000_ _]__,__(__optional_ _)_) – Steps, Steps

  * **turns** (_int in_ _[__1_ _,__100000_ _]__,__(__optional_ _)_) – Turns, Turns

  * **center** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Center, Center in global view space

  * **axis** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-1, 1], (optional)) – Axis, Axis in global view space

bpy.ops.mesh.select_all(_*_ , _action =TOGGLE_)¶

    

(De)select all vertices, edges or faces

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.mesh.select_axis(_*_ , _orientation =LOCAL_, _sign =POS_, _axis =X_,
_threshold =0.0001_)¶

    

Select all data in the mesh on a single axis

Parameters:

    

  * **orientation** (enum in [Transform Orientation Items](bpy_types_enum_items/transform_orientation_items.html#rna-enum-transform-orientation-items), (optional)) – Axis Mode, Axis orientation

  * **sign** (enum in [`POS`, `NEG`, `ALIGN`], (optional)) – Axis Sign, Side to select

  * **axis** (enum in [Axis Xyz Items](bpy_types_enum_items/axis_xyz_items.html#rna-enum-axis-xyz-items), (optional)) – Axis, Select the axis to compare each vertex on

  * **threshold** (_float in_ _[__1e-06_ _,__50_ _]__,__(__optional_ _)_) – Threshold

bpy.ops.mesh.select_by_attribute()¶

    

Select elements based on the active boolean attribute

bpy.ops.mesh.select_by_pole_count(_*_ , _pole_count =4_, _type =NOTEQUAL_,
_extend =False_, _exclude_nonmanifold =True_)¶

    

Select vertices at poles by the number of connected edges. In edge and face
mode the geometry connected to the vertices is selected

Parameters:

    

  * **pole_count** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Pole Count

  * **type** (enum in [`LESS`, `EQUAL`, `GREATER`, `NOTEQUAL`], (optional)) – Type, Type of comparison to make

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend the selection

  * **exclude_nonmanifold** (_boolean_ _,__(__optional_ _)_) – Exclude Non Manifold, Exclude non-manifold poles

bpy.ops.mesh.select_face_by_sides(_*_ , _number =4_, _type =EQUAL_, _extend
=True_)¶

    

Select vertices or faces by the number of face sides

Parameters:

    

  * **number** (_int in_ _[__3_ _,__inf_ _]__,__(__optional_ _)_) – Number of Vertices

  * **type** (enum in [`LESS`, `EQUAL`, `GREATER`, `NOTEQUAL`], (optional)) – Type, Type of comparison to make

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend the selection

bpy.ops.mesh.select_interior_faces()¶

    

Select faces where all edges have more than 2 face users

bpy.ops.mesh.select_less(_*_ , _use_face_step =True_)¶

    

Deselect vertices, edges or faces at the boundary of each selection region

Parameters:

    

**use_face_step** (_boolean_ _,__(__optional_ _)_) – Face Step, Connected
faces (instead of edges)

bpy.ops.mesh.select_linked(_*_ , _delimit ={'SEAM'}_)¶

    

Select all vertices connected to the current selection

Parameters:

    

**delimit** (enum set in [Mesh Delimit Mode
Items](bpy_types_enum_items/mesh_delimit_mode_items.html#rna-enum-mesh-
delimit-mode-items), (optional)) – Delimit, Delimit selected region

bpy.ops.mesh.select_linked_pick(_*_ , _deselect =False_, _delimit ={'SEAM'}_,
_object_index =-1_, _index =-1_)¶

    

(De)select all vertices linked to the edge under the mouse cursor

Parameters:

    

  * **deselect** (_boolean_ _,__(__optional_ _)_) – Deselect

  * **delimit** (enum set in [Mesh Delimit Mode Items](bpy_types_enum_items/mesh_delimit_mode_items.html#rna-enum-mesh-delimit-mode-items), (optional)) – Delimit, Delimit selected region

bpy.ops.mesh.select_loose(_*_ , _extend =False_)¶

    

Select loose geometry based on the selection mode

Parameters:

    

**extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend the selection

bpy.ops.mesh.select_mirror(_*_ , _axis ={'X'}_, _extend =False_)¶

    

Select mesh items at mirrored locations

Parameters:

    

  * **axis** (enum set in [Axis Flag Xyz Items](bpy_types_enum_items/axis_flag_xyz_items.html#rna-enum-axis-flag-xyz-items), (optional)) – Axis

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend the existing selection

bpy.ops.mesh.select_mode(_*_ , _use_extend =False_, _use_expand =False_, _type
=VERT_, _action =TOGGLE_)¶

    

Change selection mode

Parameters:

    

  * **use_extend** (_boolean_ _,__(__optional_ _)_) – Extend

  * **use_expand** (_boolean_ _,__(__optional_ _)_) – Expand

  * **type** (enum in [Mesh Select Mode Items](bpy_types_enum_items/mesh_select_mode_items.html#rna-enum-mesh-select-mode-items), (optional)) – Type

  * **action** (enum in [`DISABLE`, `ENABLE`, `TOGGLE`], (optional)) – 

Action, Selection action to execute

    * `DISABLE` Disable – Disable selected markers.

    * `ENABLE` Enable – Enable selected markers.

    * `TOGGLE` Toggle – Toggle disabled flag for selected markers.

bpy.ops.mesh.select_more(_*_ , _use_face_step =True_)¶

    

Select more vertices, edges or faces connected to initial selection

Parameters:

    

**use_face_step** (_boolean_ _,__(__optional_ _)_) – Face Step, Connected
faces (instead of edges)

bpy.ops.mesh.select_next_item()¶

    

Select the next element (using selection order)

File:

    

[startup/bl_operators/mesh.py:206](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/mesh.py#L206)

bpy.ops.mesh.select_non_manifold(_*_ , _extend =True_, _use_wire =True_,
_use_boundary =True_, _use_multi_face =True_, _use_non_contiguous =True_,
_use_verts =True_)¶

    

Select all non-manifold vertices or edges

Parameters:

    

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend the selection

  * **use_wire** (_boolean_ _,__(__optional_ _)_) – Wire, Wire edges

  * **use_boundary** (_boolean_ _,__(__optional_ _)_) – Boundaries, Boundary edges

  * **use_multi_face** (_boolean_ _,__(__optional_ _)_) – Multiple Faces, Edges shared by more than two faces

  * **use_non_contiguous** (_boolean_ _,__(__optional_ _)_) – Non Contiguous, Edges between faces pointing in alternate directions

  * **use_verts** (_boolean_ _,__(__optional_ _)_) – Vertices, Vertices connecting multiple face regions

bpy.ops.mesh.select_nth(_*_ , _skip =1_, _nth =1_, _offset =0_)¶

    

Deselect every Nth element starting from the active vertex, edge or face

Parameters:

    

  * **skip** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Deselected, Number of deselected elements in the repetitive sequence

  * **nth** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Selected, Number of selected elements in the repetitive sequence

  * **offset** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Offset, Offset from the starting point

bpy.ops.mesh.select_prev_item()¶

    

Select the previous element (using selection order)

File:

    

[startup/bl_operators/mesh.py:231](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/mesh.py#L231)

bpy.ops.mesh.select_random(_*_ , _ratio =0.5_, _seed =0_, _action =SELECT_)¶

    

Randomly select vertices

Parameters:

    

  * **ratio** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Ratio, Portion of items to select randomly

  * **seed** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Random Seed, Seed for the random number generator

  * **action** (enum in [`SELECT`, `DESELECT`], (optional)) – 

Action, Selection action to execute

    * `SELECT` Select – Select all elements.

    * `DESELECT` Deselect – Deselect all elements.

bpy.ops.mesh.select_similar(_*_ , _type =VERT_NORMAL_, _compare =EQUAL_,
_threshold =0.0_)¶

    

Select similar vertices, edges or faces by property types

Parameters:

    

  * **type** (enum in [`VERT_NORMAL`, `VERT_FACES`, `VERT_GROUPS`, `VERT_EDGES`, `VERT_CREASE`, `EDGE_LENGTH`, `EDGE_DIR`, `EDGE_FACES`, `EDGE_FACE_ANGLE`, `EDGE_CREASE`, `EDGE_BEVEL`, `EDGE_SEAM`, `EDGE_SHARP`, `EDGE_FREESTYLE`, `FACE_MATERIAL`, `FACE_AREA`, `FACE_SIDES`, `FACE_PERIMETER`, `FACE_NORMAL`, `FACE_COPLANAR`, `FACE_SMOOTH`, `FACE_FREESTYLE`], (optional)) – Type

  * **compare** (enum in [`EQUAL`, `GREATER`, `LESS`], (optional)) – Compare

  * **threshold** (_float in_ _[__0_ _,__100000_ _]__,__(__optional_ _)_) – Threshold

bpy.ops.mesh.select_similar_region()¶

    

Select similar face regions to the current selection

bpy.ops.mesh.select_ungrouped(_*_ , _extend =False_)¶

    

Select vertices without a group

Parameters:

    

**extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend the selection

bpy.ops.mesh.separate(_*_ , _type =SELECTED_)¶

    

Separate selected geometry into a new mesh

Parameters:

    

**type** (enum in [`SELECTED`, `MATERIAL`, `LOOSE`], (optional)) – Type

bpy.ops.mesh.set_normals_from_faces(_*_ , _keep_sharp =False_)¶

    

Set the custom normals from the selected faces ones

Parameters:

    

**keep_sharp** (_boolean_ _,__(__optional_ _)_) – Keep Sharp Edges, Do not set
sharp edges to face

bpy.ops.mesh.set_sharpness_by_angle(_*_ , _angle =0.523599_, _extend =False_)¶

    

Set edge sharpness based on the angle between neighboring faces

Parameters:

    

  * **angle** (_float in_ _[__0.000174533_ _,__3.14159_ _]__,__(__optional_ _)_) – Angle

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Add new sharp edges without clearing existing sharp edges

bpy.ops.mesh.shape_propagate_to_all()¶

    

Apply selected vertex locations to all other shape keys

bpy.ops.mesh.shortest_path_pick(_*_ , _edge_mode =SELECT_, _use_face_step
=False_, _use_topology_distance =False_, _use_fill =False_, _skip =0_, _nth
=1_, _offset =0_, _index =-1_)¶

    

Select shortest path between two selections

Parameters:

    

  * **edge_mode** (enum in [`SELECT`, `SEAM`, `SHARP`, `CREASE`, `BEVEL`, `FREESTYLE`], (optional)) – Edge Tag, The edge flag to tag when selecting the shortest path

  * **use_face_step** (_boolean_ _,__(__optional_ _)_) – Face Stepping, Traverse connected faces (includes diagonals and edge-rings)

  * **use_topology_distance** (_boolean_ _,__(__optional_ _)_) – Topology Distance, Find the minimum number of steps, ignoring spatial distance

  * **use_fill** (_boolean_ _,__(__optional_ _)_) – Fill Region, Select all paths between the source/destination elements

  * **skip** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Deselected, Number of deselected elements in the repetitive sequence

  * **nth** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Selected, Number of selected elements in the repetitive sequence

  * **offset** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Offset, Offset from the starting point

bpy.ops.mesh.shortest_path_select(_*_ , _edge_mode =SELECT_, _use_face_step
=False_, _use_topology_distance =False_, _use_fill =False_, _skip =0_, _nth
=1_, _offset =0_)¶

    

Selected shortest path between two vertices/edges/faces

Parameters:

    

  * **edge_mode** (enum in [`SELECT`, `SEAM`, `SHARP`, `CREASE`, `BEVEL`, `FREESTYLE`], (optional)) – Edge Tag, The edge flag to tag when selecting the shortest path

  * **use_face_step** (_boolean_ _,__(__optional_ _)_) – Face Stepping, Traverse connected faces (includes diagonals and edge-rings)

  * **use_topology_distance** (_boolean_ _,__(__optional_ _)_) – Topology Distance, Find the minimum number of steps, ignoring spatial distance

  * **use_fill** (_boolean_ _,__(__optional_ _)_) – Fill Region, Select all paths between the source/destination elements

  * **skip** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Deselected, Number of deselected elements in the repetitive sequence

  * **nth** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Selected, Number of selected elements in the repetitive sequence

  * **offset** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Offset, Offset from the starting point

bpy.ops.mesh.smooth_normals(_*_ , _factor =0.5_)¶

    

Smooth custom normals based on adjacent vertex normals

Parameters:

    

**factor** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Factor,
Specifies weight of smooth vs original normal

bpy.ops.mesh.solidify(_*_ , _thickness =0.01_)¶

    

Create a solid skin by extruding, compensating for sharp angles

Parameters:

    

**thickness** (_float in_ _[__-10000_ _,__10000_ _]__,__(__optional_ _)_) –
Thickness

bpy.ops.mesh.sort_elements(_*_ , _type =VIEW_ZAXIS_, _elements ={'VERT'}_,
_reverse =False_, _seed =0_)¶

    

The order of selected vertices/edges/faces is modified, based on a given
method

Parameters:

    

  * **type** (enum in [`VIEW_ZAXIS`, `VIEW_XAXIS`, `CURSOR_DISTANCE`, `MATERIAL`, `SELECTED`, `RANDOMIZE`, `REVERSE`], (optional)) – 

Type, Type of reordering operation to apply

    * `VIEW_ZAXIS` View Z Axis – Sort selected elements from farthest to nearest one in current view.

    * `VIEW_XAXIS` View X Axis – Sort selected elements from left to right one in current view.

    * `CURSOR_DISTANCE` Cursor Distance – Sort selected elements from nearest to farthest from 3D cursor.

    * `MATERIAL` Material – Sort selected faces from smallest to greatest material index.

    * `SELECTED` Selected – Move all selected elements in first places, preserving their relative order. Warning: This will affect unselected elements’ indices as well.

    * `RANDOMIZE` Randomize – Randomize order of selected elements.

    * `REVERSE` Reverse – Reverse current order of selected elements.

  * **elements** (enum set in {`VERT`, `EDGE`, `FACE`}, (optional)) – Elements, Which elements to affect (vertices, edges and/or faces)

  * **reverse** (_boolean_ _,__(__optional_ _)_) – Reverse, Reverse the sorting effect

  * **seed** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Seed, Seed for random-based operations

bpy.ops.mesh.spin(_*_ , _steps =12_, _dupli =False_, _angle =1.5708_,
_use_auto_merge =True_, _use_normal_flip =False_, _center =(0.0, 0.0, 0.0)_,
_axis =(0.0, 0.0, 0.0)_)¶

    

Extrude selected vertices in a circle around the cursor in indicated viewport

Parameters:

    

  * **steps** (_int in_ _[__0_ _,__1000000_ _]__,__(__optional_ _)_) – Steps, Steps

  * **dupli** (_boolean_ _,__(__optional_ _)_) – Use Duplicates

  * **angle** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Angle, Rotation for each step

  * **use_auto_merge** (_boolean_ _,__(__optional_ _)_) – Auto Merge, Merge first/last when the angle is a full revolution

  * **use_normal_flip** (_boolean_ _,__(__optional_ _)_) – Flip Normals

  * **center** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Center, Center in global view space

  * **axis** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-1, 1], (optional)) – Axis, Axis in global view space

bpy.ops.mesh.split()¶

    

Split off selected geometry from connected unselected geometry

bpy.ops.mesh.split_normals()¶

    

Split custom normals of selected vertices

bpy.ops.mesh.subdivide(_*_ , _number_cuts =1_, _smoothness =0.0_, _ngon
=True_, _quadcorner =STRAIGHT_CUT_, _fractal =0.0_, _fractal_along_normal
=0.0_, _seed =0_)¶

    

Subdivide selected edges

Parameters:

    

  * **number_cuts** (_int in_ _[__1_ _,__100_ _]__,__(__optional_ _)_) – Number of Cuts

  * **smoothness** (_float in_ _[__0_ _,__1000_ _]__,__(__optional_ _)_) – Smoothness, Smoothness factor

  * **ngon** (_boolean_ _,__(__optional_ _)_) – Create N-Gons, When disabled, newly created faces are limited to 3 and 4 sided faces

  * **quadcorner** (enum in [`INNERVERT`, `PATH`, `STRAIGHT_CUT`, `FAN`], (optional)) – Quad Corner Type, How to subdivide quad corners (anything other than Straight Cut will prevent n-gons)

  * **fractal** (_float in_ _[__0_ _,__1e+06_ _]__,__(__optional_ _)_) – Fractal, Fractal randomness factor

  * **fractal_along_normal** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Along Normal, Apply fractal displacement along normal only

  * **seed** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Random Seed, Seed for the random number generator

bpy.ops.mesh.subdivide_edgering(_*_ , _number_cuts =10_, _interpolation
=PATH_, _smoothness =1.0_, _profile_shape_factor =0.0_, _profile_shape
=SMOOTH_)¶

    

Subdivide perpendicular edges to the selected edge-ring

Parameters:

    

  * **number_cuts** (_int in_ _[__0_ _,__1000_ _]__,__(__optional_ _)_) – Number of Cuts

  * **interpolation** (enum in [`LINEAR`, `PATH`, `SURFACE`], (optional)) – Interpolation, Interpolation method

  * **smoothness** (_float in_ _[__0_ _,__1000_ _]__,__(__optional_ _)_) – Smoothness, Smoothness factor

  * **profile_shape_factor** (_float in_ _[__-1000_ _,__1000_ _]__,__(__optional_ _)_) – Profile Factor, How much intermediary new edges are shrunk/expanded

  * **profile_shape** (enum in [Proportional Falloff Curve Only Items](bpy_types_enum_items/proportional_falloff_curve_only_items.html#rna-enum-proportional-falloff-curve-only-items), (optional)) – Profile Shape, Shape of the profile

bpy.ops.mesh.symmetrize(_*_ , _direction =NEGATIVE_X_, _threshold =0.0001_)¶

    

Enforce symmetry (both form and topological) across an axis

Parameters:

    

  * **direction** (enum in [Symmetrize Direction Items](bpy_types_enum_items/symmetrize_direction_items.html#rna-enum-symmetrize-direction-items), (optional)) – Direction, Which sides to copy from and to

  * **threshold** (_float in_ _[__0_ _,__10_ _]__,__(__optional_ _)_) – Threshold, Limit for snap middle vertices to the axis center

bpy.ops.mesh.symmetry_snap(_*_ , _direction =NEGATIVE_X_, _threshold =0.05_,
_factor =0.5_, _use_center =True_)¶

    

Snap vertex pairs to their mirrored locations

Parameters:

    

  * **direction** (enum in [Symmetrize Direction Items](bpy_types_enum_items/symmetrize_direction_items.html#rna-enum-symmetrize-direction-items), (optional)) – Direction, Which sides to copy from and to

  * **threshold** (_float in_ _[__0_ _,__10_ _]__,__(__optional_ _)_) – Threshold, Distance within which matching vertices are searched

  * **factor** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Factor, Mix factor of the locations of the vertices

  * **use_center** (_boolean_ _,__(__optional_ _)_) – Center, Snap middle vertices to the axis center

bpy.ops.mesh.tris_convert_to_quads(_*_ , _face_threshold =0.698132_,
_shape_threshold =0.698132_, _topology_influence =0.0_, _uvs =False_, _vcols
=False_, _seam =False_, _sharp =False_, _materials =False_, _deselect_joined
=False_)¶

    

Merge triangles into four sided polygons where possible

Parameters:

    

  * **face_threshold** (_float in_ _[__0_ _,__3.14159_ _]__,__(__optional_ _)_) – Max Face Angle, Face angle limit

  * **shape_threshold** (_float in_ _[__0_ _,__3.14159_ _]__,__(__optional_ _)_) – Max Shape Angle, Shape angle limit

  * **topology_influence** (_float in_ _[__0_ _,__2_ _]__,__(__optional_ _)_) – Topology Influence, How much to prioritize regular grids of quads as well as quads that touch existing quads

  * **uvs** (_boolean_ _,__(__optional_ _)_) – Compare UVs

  * **vcols** (_boolean_ _,__(__optional_ _)_) – Compare Color Attributes

  * **seam** (_boolean_ _,__(__optional_ _)_) – Compare Seam

  * **sharp** (_boolean_ _,__(__optional_ _)_) – Compare Sharp

  * **materials** (_boolean_ _,__(__optional_ _)_) – Compare Materials

  * **deselect_joined** (_boolean_ _,__(__optional_ _)_) – Deselect Joined, Only select remaining triangles that were not merged

bpy.ops.mesh.unsubdivide(_*_ , _iterations =2_)¶

    

Un-subdivide selected edges and faces

Parameters:

    

**iterations** (_int in_ _[__1_ _,__1000_ _]__,__(__optional_ _)_) –
Iterations, Number of times to un-subdivide

bpy.ops.mesh.uv_texture_add()¶

    

Add UV map

bpy.ops.mesh.uv_texture_remove()¶

    

Remove UV map

bpy.ops.mesh.uvs_reverse()¶

    

Flip direction of UV coordinates inside faces

bpy.ops.mesh.uvs_rotate(_*_ , _use_ccw =False_)¶

    

Rotate UV coordinates inside faces

Parameters:

    

**use_ccw** (_boolean_ _,__(__optional_ _)_) – Counter Clockwise

bpy.ops.mesh.vert_connect()¶

    

Connect selected vertices of faces, splitting the face

bpy.ops.mesh.vert_connect_concave()¶

    

Make all faces convex

bpy.ops.mesh.vert_connect_nonplanar(_*_ , _angle_limit =0.0872665_)¶

    

Split non-planar faces that exceed the angle threshold

Parameters:

    

**angle_limit** (_float in_ _[__0_ _,__3.14159_ _]__,__(__optional_ _)_) – Max
Angle, Angle limit

bpy.ops.mesh.vert_connect_path()¶

    

Connect vertices by their selection order, creating edges, splitting faces

bpy.ops.mesh.vertices_smooth(_*_ , _factor =0.0_, _repeat =1_, _xaxis =True_,
_yaxis =True_, _zaxis =True_, _wait_for_input =True_)¶

    

Flatten angles of selected vertices

Parameters:

    

  * **factor** (_float in_ _[__-10_ _,__10_ _]__,__(__optional_ _)_) – Smoothing, Smoothing factor

  * **repeat** (_int in_ _[__1_ _,__1000_ _]__,__(__optional_ _)_) – Repeat, Number of times to smooth the mesh

  * **xaxis** (_boolean_ _,__(__optional_ _)_) – X-Axis, Smooth along the X axis

  * **yaxis** (_boolean_ _,__(__optional_ _)_) – Y-Axis, Smooth along the Y axis

  * **zaxis** (_boolean_ _,__(__optional_ _)_) – Z-Axis, Smooth along the Z axis

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

bpy.ops.mesh.vertices_smooth_laplacian(_*_ , _repeat =1_, _lambda_factor
=1.0_, _lambda_border =5e-05_, _use_x =True_, _use_y =True_, _use_z =True_,
_preserve_volume =True_)¶

    

Laplacian smooth of selected vertices

Parameters:

    

  * **repeat** (_int in_ _[__1_ _,__1000_ _]__,__(__optional_ _)_) – Number of iterations to smooth the mesh

  * **lambda_factor** (_float in_ _[__1e-07_ _,__1000_ _]__,__(__optional_ _)_) – Lambda factor

  * **lambda_border** (_float in_ _[__1e-07_ _,__1000_ _]__,__(__optional_ _)_) – Lambda factor in border

  * **use_x** (_boolean_ _,__(__optional_ _)_) – Smooth X Axis, Smooth object along X axis

  * **use_y** (_boolean_ _,__(__optional_ _)_) – Smooth Y Axis, Smooth object along Y axis

  * **use_z** (_boolean_ _,__(__optional_ _)_) – Smooth Z Axis, Smooth object along Z axis

  * **preserve_volume** (_boolean_ _,__(__optional_ _)_) – Preserve Volume, Apply volume preservation after smooth

bpy.ops.mesh.wireframe(_*_ , _use_boundary =True_, _use_even_offset =True_,
_use_relative_offset =False_, _use_replace =True_, _thickness =0.01_, _offset
=0.01_, _use_crease =False_, _crease_weight =0.01_)¶

    

Create a solid wireframe from faces

Parameters:

    

  * **use_boundary** (_boolean_ _,__(__optional_ _)_) – Boundary, Inset face boundaries

  * **use_even_offset** (_boolean_ _,__(__optional_ _)_) – Offset Even, Scale the offset to give more even thickness

  * **use_relative_offset** (_boolean_ _,__(__optional_ _)_) – Offset Relative, Scale the offset by surrounding geometry

  * **use_replace** (_boolean_ _,__(__optional_ _)_) – Replace, Remove original faces

  * **thickness** (_float in_ _[__0_ _,__10000_ _]__,__(__optional_ _)_) – Thickness

  * **offset** (_float in_ _[__0_ _,__10000_ _]__,__(__optional_ _)_) – Offset

  * **use_crease** (_boolean_ _,__(__optional_ _)_) – Crease, Crease hub edges for an improved subdivision surface

  * **crease_weight** (_float in_ _[__0_ _,__1000_ _]__,__(__optional_ _)_) – Crease Weight

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

