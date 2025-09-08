---
url: https://docs.blender.org/api/current/bpy.ops.transform.html
scraped_at: 2025-09-08T14:18:56.780782
title: Transform Operators¶
---

# Transform Operators¶

bpy.ops.transform.bbone_resize(_*_ , _value =(1.0, 1.0, 1.0)_, _orient_type
=GLOBAL_, _orient_matrix =((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0,
0.0))_, _orient_matrix_type =GLOBAL_, _constraint_axis =(False, False,
False)_, _mirror =False_, _release_confirm =False_, _use_accurate =False_)¶

    

Scale selected bendy bones display size

Parameters:

    

  * **value** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Display Size

  * **orient_type** (_enum in_ _[__]__,__(__optional_ _)_) – Orientation, Transformation orientation

  * **orient_matrix** ([`mathutils.Matrix`](mathutils.html#mathutils.Matrix "mathutils.Matrix") of 3 * 3 items in [-inf, inf], (optional)) – Matrix

  * **orient_matrix_type** (_enum in_ _[__]__,__(__optional_ _)_) – Matrix Orientation

  * **constraint_axis** (_boolean array_ _of_ _3 items_ _,__(__optional_ _)_) – Constraint Axis

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

bpy.ops.transform.bend(_*_ , _value =0.0_, _mirror =False_,
_use_proportional_edit =False_, _proportional_edit_falloff =SMOOTH_,
_proportional_size =1.0_, _use_proportional_connected =False_,
_use_proportional_projected =False_, _snap =False_, _gpencil_strokes =False_,
_center_override =(0.0, 0.0, 0.0)_, _release_confirm =False_, _use_accurate
=False_)¶

    

Bend selected items between the 3D cursor and the mouse

Parameters:

    

  * **value** (_float array_ _of_ _1 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Angle

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

  * **use_proportional_edit** (_boolean_ _,__(__optional_ _)_) – Proportional Editing

  * **proportional_edit_falloff** (enum in [Proportional Falloff Items](bpy_types_enum_items/proportional_falloff_items.html#rna-enum-proportional-falloff-items), (optional)) – Proportional Falloff, Falloff type for proportional editing mode

  * **proportional_size** (_float in_ _[__1e-06_ _,__inf_ _]__,__(__optional_ _)_) – Proportional Size

  * **use_proportional_connected** (_boolean_ _,__(__optional_ _)_) – Connected

  * **use_proportional_projected** (_boolean_ _,__(__optional_ _)_) – Projected (2D)

  * **snap** (_boolean_ _,__(__optional_ _)_) – Use Snapping Options

  * **gpencil_strokes** (_boolean_ _,__(__optional_ _)_) – Edit Grease Pencil, Edit selected Grease Pencil strokes

  * **center_override** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Center Override, Force using this center value (when set)

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

bpy.ops.transform.create_orientation(_*_ , _name =''_, _use_view =False_, _use
=False_, _overwrite =False_)¶

    

Create transformation orientation from selection

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the new custom orientation

  * **use_view** (_boolean_ _,__(__optional_ _)_) – Use View, Use the current view instead of the active object to create the new orientation

  * **use** (_boolean_ _,__(__optional_ _)_) – Use After Creation, Select orientation after its creation

  * **overwrite** (_boolean_ _,__(__optional_ _)_) – Overwrite Previous, Overwrite previously created orientation with same name

bpy.ops.transform.delete_orientation()¶

    

Delete transformation orientation

bpy.ops.transform.edge_bevelweight(_*_ , _value =0.0_, _snap =False_,
_release_confirm =False_, _use_accurate =False_)¶

    

Change the bevel weight of edges

Parameters:

    

  * **value** (_float in_ _[__-1_ _,__1_ _]__,__(__optional_ _)_) – Factor

  * **snap** (_boolean_ _,__(__optional_ _)_) – Use Snapping Options

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

bpy.ops.transform.edge_crease(_*_ , _value =0.0_, _snap =False_,
_release_confirm =False_, _use_accurate =False_)¶

    

Change the crease of edges

Parameters:

    

  * **value** (_float in_ _[__-1_ _,__1_ _]__,__(__optional_ _)_) – Factor

  * **snap** (_boolean_ _,__(__optional_ _)_) – Use Snapping Options

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

bpy.ops.transform.edge_slide(_*_ , _value =0.0_, _single_side =False_,
_use_even =False_, _flipped =False_, _use_clamp =True_, _mirror =False_, _snap
=False_, _snap_elements ={'INCREMENT'}_, _use_snap_project =False_,
_snap_target =CLOSEST_, _use_snap_self =True_, _use_snap_edit =True_,
_use_snap_nonedit =True_, _use_snap_selectable =False_, _snap_point =(0.0,
0.0, 0.0)_, _correct_uv =True_, _release_confirm =False_, _use_accurate
=False_)¶

    

Slide an edge loop along a mesh

Parameters:

    

  * **value** (_float in_ _[__-10_ _,__10_ _]__,__(__optional_ _)_) – Factor

  * **single_side** (_boolean_ _,__(__optional_ _)_) – Single Side

  * **use_even** (_boolean_ _,__(__optional_ _)_) – Even, Make the edge loop match the shape of the adjacent edge loop

  * **flipped** (_boolean_ _,__(__optional_ _)_) – Flipped, When Even mode is active, flips between the two adjacent edge loops

  * **use_clamp** (_boolean_ _,__(__optional_ _)_) – Clamp, Clamp within the edge extents

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

  * **snap** (_boolean_ _,__(__optional_ _)_) – Use Snapping Options

  * **snap_elements** (enum set in [Snap Element Items](bpy_types_enum_items/snap_element_items.html#rna-enum-snap-element-items), (optional)) – Snap to Elements

  * **use_snap_project** (_boolean_ _,__(__optional_ _)_) – Project Individual Elements

  * **snap_target** (enum in [Snap Source Items](bpy_types_enum_items/snap_source_items.html#rna-enum-snap-source-items), (optional)) – Snap Base, Point on source that will snap to target

  * **use_snap_self** (_boolean_ _,__(__optional_ _)_) – Target: Include Active

  * **use_snap_edit** (_boolean_ _,__(__optional_ _)_) – Target: Include Edit

  * **use_snap_nonedit** (_boolean_ _,__(__optional_ _)_) – Target: Include Non-Edited

  * **use_snap_selectable** (_boolean_ _,__(__optional_ _)_) – Target: Exclude Non-Selectable

  * **snap_point** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Point

  * **correct_uv** (_boolean_ _,__(__optional_ _)_) – Correct UVs, Correct UV coordinates when transforming

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

bpy.ops.transform.from_gizmo()¶

    

Transform selected items by mode type

bpy.ops.transform.mirror(_*_ , _orient_type =GLOBAL_, _orient_matrix =((0.0,
0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0))_, _orient_matrix_type =GLOBAL_,
_constraint_axis =(False, False, False)_, _gpencil_strokes =False_,
_center_override =(0.0, 0.0, 0.0)_, _release_confirm =False_, _use_accurate
=False_)¶

    

Mirror selected items around one or more axes

Parameters:

    

  * **orient_type** (_enum in_ _[__]__,__(__optional_ _)_) – Orientation, Transformation orientation

  * **orient_matrix** ([`mathutils.Matrix`](mathutils.html#mathutils.Matrix "mathutils.Matrix") of 3 * 3 items in [-inf, inf], (optional)) – Matrix

  * **orient_matrix_type** (_enum in_ _[__]__,__(__optional_ _)_) – Matrix Orientation

  * **constraint_axis** (_boolean array_ _of_ _3 items_ _,__(__optional_ _)_) – Constraint Axis

  * **gpencil_strokes** (_boolean_ _,__(__optional_ _)_) – Edit Grease Pencil, Edit selected Grease Pencil strokes

  * **center_override** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Center Override, Force using this center value (when set)

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

bpy.ops.transform.push_pull(_*_ , _value =0.0_, _mirror =False_,
_use_proportional_edit =False_, _proportional_edit_falloff =SMOOTH_,
_proportional_size =1.0_, _use_proportional_connected =False_,
_use_proportional_projected =False_, _snap =False_, _center_override =(0.0,
0.0, 0.0)_, _release_confirm =False_, _use_accurate =False_)¶

    

Push/Pull selected items

Parameters:

    

  * **value** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Distance

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

  * **use_proportional_edit** (_boolean_ _,__(__optional_ _)_) – Proportional Editing

  * **proportional_edit_falloff** (enum in [Proportional Falloff Items](bpy_types_enum_items/proportional_falloff_items.html#rna-enum-proportional-falloff-items), (optional)) – Proportional Falloff, Falloff type for proportional editing mode

  * **proportional_size** (_float in_ _[__1e-06_ _,__inf_ _]__,__(__optional_ _)_) – Proportional Size

  * **use_proportional_connected** (_boolean_ _,__(__optional_ _)_) – Connected

  * **use_proportional_projected** (_boolean_ _,__(__optional_ _)_) – Projected (2D)

  * **snap** (_boolean_ _,__(__optional_ _)_) – Use Snapping Options

  * **center_override** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Center Override, Force using this center value (when set)

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

bpy.ops.transform.resize(_*_ , _value =(1.0, 1.0, 1.0)_, _mouse_dir_constraint
=(0.0, 0.0, 0.0)_, _orient_type =GLOBAL_, _orient_matrix =((0.0, 0.0, 0.0),
(0.0, 0.0, 0.0), (0.0, 0.0, 0.0))_, _orient_matrix_type =GLOBAL_,
_constraint_axis =(False, False, False)_, _mirror =False_,
_use_proportional_edit =False_, _proportional_edit_falloff =SMOOTH_,
_proportional_size =1.0_, _use_proportional_connected =False_,
_use_proportional_projected =False_, _snap =False_, _snap_elements
={'INCREMENT'}_, _use_snap_project =False_, _snap_target =CLOSEST_,
_use_snap_self =True_, _use_snap_edit =True_, _use_snap_nonedit =True_,
_use_snap_selectable =False_, _snap_point =(0.0, 0.0, 0.0)_, _gpencil_strokes
=False_, _texture_space =False_, _remove_on_cancel =False_,
_use_duplicated_keyframes =False_, _center_override =(0.0, 0.0, 0.0)_,
_release_confirm =False_, _use_accurate =False_)¶

    

Scale (resize) selected items

Parameters:

    

  * **value** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale

  * **mouse_dir_constraint** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Mouse Directional Constraint

  * **orient_type** (_enum in_ _[__]__,__(__optional_ _)_) – Orientation, Transformation orientation

  * **orient_matrix** ([`mathutils.Matrix`](mathutils.html#mathutils.Matrix "mathutils.Matrix") of 3 * 3 items in [-inf, inf], (optional)) – Matrix

  * **orient_matrix_type** (_enum in_ _[__]__,__(__optional_ _)_) – Matrix Orientation

  * **constraint_axis** (_boolean array_ _of_ _3 items_ _,__(__optional_ _)_) – Constraint Axis

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

  * **use_proportional_edit** (_boolean_ _,__(__optional_ _)_) – Proportional Editing

  * **proportional_edit_falloff** (enum in [Proportional Falloff Items](bpy_types_enum_items/proportional_falloff_items.html#rna-enum-proportional-falloff-items), (optional)) – Proportional Falloff, Falloff type for proportional editing mode

  * **proportional_size** (_float in_ _[__1e-06_ _,__inf_ _]__,__(__optional_ _)_) – Proportional Size

  * **use_proportional_connected** (_boolean_ _,__(__optional_ _)_) – Connected

  * **use_proportional_projected** (_boolean_ _,__(__optional_ _)_) – Projected (2D)

  * **snap** (_boolean_ _,__(__optional_ _)_) – Use Snapping Options

  * **snap_elements** (enum set in [Snap Element Items](bpy_types_enum_items/snap_element_items.html#rna-enum-snap-element-items), (optional)) – Snap to Elements

  * **use_snap_project** (_boolean_ _,__(__optional_ _)_) – Project Individual Elements

  * **snap_target** (enum in [Snap Source Items](bpy_types_enum_items/snap_source_items.html#rna-enum-snap-source-items), (optional)) – Snap Base, Point on source that will snap to target

  * **use_snap_self** (_boolean_ _,__(__optional_ _)_) – Target: Include Active

  * **use_snap_edit** (_boolean_ _,__(__optional_ _)_) – Target: Include Edit

  * **use_snap_nonedit** (_boolean_ _,__(__optional_ _)_) – Target: Include Non-Edited

  * **use_snap_selectable** (_boolean_ _,__(__optional_ _)_) – Target: Exclude Non-Selectable

  * **snap_point** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Point

  * **gpencil_strokes** (_boolean_ _,__(__optional_ _)_) – Edit Grease Pencil, Edit selected Grease Pencil strokes

  * **texture_space** (_boolean_ _,__(__optional_ _)_) – Edit Texture Space, Edit object data texture space

  * **remove_on_cancel** (_boolean_ _,__(__optional_ _)_) – Remove on Cancel, Remove elements on cancel

  * **use_duplicated_keyframes** (_boolean_ _,__(__optional_ _)_) – Duplicated Keyframes, Transform duplicated keyframes

  * **center_override** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Center Override, Force using this center value (when set)

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

bpy.ops.transform.rotate(_*_ , _value =0.0_, _orient_axis =Z_, _orient_type
=GLOBAL_, _orient_matrix =((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0,
0.0))_, _orient_matrix_type =GLOBAL_, _constraint_axis =(False, False,
False)_, _mirror =False_, _use_proportional_edit =False_,
_proportional_edit_falloff =SMOOTH_, _proportional_size =1.0_,
_use_proportional_connected =False_, _use_proportional_projected =False_,
_snap =False_, _snap_elements ={'INCREMENT'}_, _use_snap_project =False_,
_snap_target =CLOSEST_, _use_snap_self =True_, _use_snap_edit =True_,
_use_snap_nonedit =True_, _use_snap_selectable =False_, _snap_point =(0.0,
0.0, 0.0)_, _gpencil_strokes =False_, _center_override =(0.0, 0.0, 0.0)_,
_release_confirm =False_, _use_accurate =False_)¶

    

Rotate selected items

Parameters:

    

  * **value** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Angle

  * **orient_axis** (enum in [Axis Xyz Items](bpy_types_enum_items/axis_xyz_items.html#rna-enum-axis-xyz-items), (optional)) – Axis

  * **orient_type** (_enum in_ _[__]__,__(__optional_ _)_) – Orientation, Transformation orientation

  * **orient_matrix** ([`mathutils.Matrix`](mathutils.html#mathutils.Matrix "mathutils.Matrix") of 3 * 3 items in [-inf, inf], (optional)) – Matrix

  * **orient_matrix_type** (_enum in_ _[__]__,__(__optional_ _)_) – Matrix Orientation

  * **constraint_axis** (_boolean array_ _of_ _3 items_ _,__(__optional_ _)_) – Constraint Axis

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

  * **use_proportional_edit** (_boolean_ _,__(__optional_ _)_) – Proportional Editing

  * **proportional_edit_falloff** (enum in [Proportional Falloff Items](bpy_types_enum_items/proportional_falloff_items.html#rna-enum-proportional-falloff-items), (optional)) – Proportional Falloff, Falloff type for proportional editing mode

  * **proportional_size** (_float in_ _[__1e-06_ _,__inf_ _]__,__(__optional_ _)_) – Proportional Size

  * **use_proportional_connected** (_boolean_ _,__(__optional_ _)_) – Connected

  * **use_proportional_projected** (_boolean_ _,__(__optional_ _)_) – Projected (2D)

  * **snap** (_boolean_ _,__(__optional_ _)_) – Use Snapping Options

  * **snap_elements** (enum set in [Snap Element Items](bpy_types_enum_items/snap_element_items.html#rna-enum-snap-element-items), (optional)) – Snap to Elements

  * **use_snap_project** (_boolean_ _,__(__optional_ _)_) – Project Individual Elements

  * **snap_target** (enum in [Snap Source Items](bpy_types_enum_items/snap_source_items.html#rna-enum-snap-source-items), (optional)) – Snap Base, Point on source that will snap to target

  * **use_snap_self** (_boolean_ _,__(__optional_ _)_) – Target: Include Active

  * **use_snap_edit** (_boolean_ _,__(__optional_ _)_) – Target: Include Edit

  * **use_snap_nonedit** (_boolean_ _,__(__optional_ _)_) – Target: Include Non-Edited

  * **use_snap_selectable** (_boolean_ _,__(__optional_ _)_) – Target: Exclude Non-Selectable

  * **snap_point** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Point

  * **gpencil_strokes** (_boolean_ _,__(__optional_ _)_) – Edit Grease Pencil, Edit selected Grease Pencil strokes

  * **center_override** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Center Override, Force using this center value (when set)

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

bpy.ops.transform.rotate_normal(_*_ , _value =0.0_, _orient_axis =Z_,
_orient_type =GLOBAL_, _orient_matrix =((0.0, 0.0, 0.0), (0.0, 0.0, 0.0),
(0.0, 0.0, 0.0))_, _orient_matrix_type =GLOBAL_, _constraint_axis =(False,
False, False)_, _mirror =False_, _release_confirm =False_, _use_accurate
=False_)¶

    

Rotate split normal of selected items

Parameters:

    

  * **value** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Angle

  * **orient_axis** (enum in [Axis Xyz Items](bpy_types_enum_items/axis_xyz_items.html#rna-enum-axis-xyz-items), (optional)) – Axis

  * **orient_type** (_enum in_ _[__]__,__(__optional_ _)_) – Orientation, Transformation orientation

  * **orient_matrix** ([`mathutils.Matrix`](mathutils.html#mathutils.Matrix "mathutils.Matrix") of 3 * 3 items in [-inf, inf], (optional)) – Matrix

  * **orient_matrix_type** (_enum in_ _[__]__,__(__optional_ _)_) – Matrix Orientation

  * **constraint_axis** (_boolean array_ _of_ _3 items_ _,__(__optional_ _)_) – Constraint Axis

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

bpy.ops.transform.select_orientation(_*_ , _orientation =GLOBAL_)¶

    

Select transformation orientation

Parameters:

    

**orientation** (_enum in_ _[__]__,__(__optional_ _)_) – Orientation,
Transformation orientation

bpy.ops.transform.seq_slide(_*_ , _value =(0.0, 0.0)_,
_use_restore_handle_selection =False_, _snap =False_, _view2d_edge_pan
=False_, _release_confirm =False_, _use_accurate =False_)¶

    

Slide a sequence strip in time

Parameters:

    

  * **value** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Offset

  * **use_restore_handle_selection** (_boolean_ _,__(__optional_ _)_) – Restore Handle Selection, Restore handle selection after tweaking

  * **snap** (_boolean_ _,__(__optional_ _)_) – Use Snapping Options

  * **view2d_edge_pan** (_boolean_ _,__(__optional_ _)_) – Edge Pan, Enable edge panning in 2D view

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

bpy.ops.transform.shear(_*_ , _value =0.0_, _orient_axis =Z_,
_orient_axis_ortho =X_, _orient_type =GLOBAL_, _orient_matrix =((0.0, 0.0,
0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0))_, _orient_matrix_type =GLOBAL_,
_mirror =False_, _use_proportional_edit =False_, _proportional_edit_falloff
=SMOOTH_, _proportional_size =1.0_, _use_proportional_connected =False_,
_use_proportional_projected =False_, _snap =False_, _gpencil_strokes =False_,
_release_confirm =False_, _use_accurate =False_)¶

    

Shear selected items along the given axis

Parameters:

    

  * **value** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Offset

  * **orient_axis** (enum in [Axis Xyz Items](bpy_types_enum_items/axis_xyz_items.html#rna-enum-axis-xyz-items), (optional)) – Axis

  * **orient_axis_ortho** (enum in [Axis Xyz Items](bpy_types_enum_items/axis_xyz_items.html#rna-enum-axis-xyz-items), (optional)) – Axis Ortho

  * **orient_type** (_enum in_ _[__]__,__(__optional_ _)_) – Orientation, Transformation orientation

  * **orient_matrix** ([`mathutils.Matrix`](mathutils.html#mathutils.Matrix "mathutils.Matrix") of 3 * 3 items in [-inf, inf], (optional)) – Matrix

  * **orient_matrix_type** (_enum in_ _[__]__,__(__optional_ _)_) – Matrix Orientation

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

  * **use_proportional_edit** (_boolean_ _,__(__optional_ _)_) – Proportional Editing

  * **proportional_edit_falloff** (enum in [Proportional Falloff Items](bpy_types_enum_items/proportional_falloff_items.html#rna-enum-proportional-falloff-items), (optional)) – Proportional Falloff, Falloff type for proportional editing mode

  * **proportional_size** (_float in_ _[__1e-06_ _,__inf_ _]__,__(__optional_ _)_) – Proportional Size

  * **use_proportional_connected** (_boolean_ _,__(__optional_ _)_) – Connected

  * **use_proportional_projected** (_boolean_ _,__(__optional_ _)_) – Projected (2D)

  * **snap** (_boolean_ _,__(__optional_ _)_) – Use Snapping Options

  * **gpencil_strokes** (_boolean_ _,__(__optional_ _)_) – Edit Grease Pencil, Edit selected Grease Pencil strokes

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

bpy.ops.transform.shrink_fatten(_*_ , _value =0.0_, _use_even_offset =False_,
_mirror =False_, _use_proportional_edit =False_, _proportional_edit_falloff
=SMOOTH_, _proportional_size =1.0_, _use_proportional_connected =False_,
_use_proportional_projected =False_, _snap =False_, _release_confirm =False_,
_use_accurate =False_)¶

    

Shrink/fatten selected vertices along normals

Parameters:

    

  * **value** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Offset

  * **use_even_offset** (_boolean_ _,__(__optional_ _)_) – Offset Even, Scale the offset to give more even thickness

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

  * **use_proportional_edit** (_boolean_ _,__(__optional_ _)_) – Proportional Editing

  * **proportional_edit_falloff** (enum in [Proportional Falloff Items](bpy_types_enum_items/proportional_falloff_items.html#rna-enum-proportional-falloff-items), (optional)) – Proportional Falloff, Falloff type for proportional editing mode

  * **proportional_size** (_float in_ _[__1e-06_ _,__inf_ _]__,__(__optional_ _)_) – Proportional Size

  * **use_proportional_connected** (_boolean_ _,__(__optional_ _)_) – Connected

  * **use_proportional_projected** (_boolean_ _,__(__optional_ _)_) – Projected (2D)

  * **snap** (_boolean_ _,__(__optional_ _)_) – Use Snapping Options

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

bpy.ops.transform.skin_resize(_*_ , _value =(1.0, 1.0, 1.0)_, _orient_type
=GLOBAL_, _orient_matrix =((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0,
0.0))_, _orient_matrix_type =GLOBAL_, _constraint_axis =(False, False,
False)_, _mirror =False_, _use_proportional_edit =False_,
_proportional_edit_falloff =SMOOTH_, _proportional_size =1.0_,
_use_proportional_connected =False_, _use_proportional_projected =False_,
_snap =False_, _snap_elements ={'INCREMENT'}_, _use_snap_project =False_,
_snap_target =CLOSEST_, _use_snap_self =True_, _use_snap_edit =True_,
_use_snap_nonedit =True_, _use_snap_selectable =False_, _snap_point =(0.0,
0.0, 0.0)_, _release_confirm =False_, _use_accurate =False_)¶

    

Scale selected vertices’ skin radii

Parameters:

    

  * **value** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale

  * **orient_type** (_enum in_ _[__]__,__(__optional_ _)_) – Orientation, Transformation orientation

  * **orient_matrix** ([`mathutils.Matrix`](mathutils.html#mathutils.Matrix "mathutils.Matrix") of 3 * 3 items in [-inf, inf], (optional)) – Matrix

  * **orient_matrix_type** (_enum in_ _[__]__,__(__optional_ _)_) – Matrix Orientation

  * **constraint_axis** (_boolean array_ _of_ _3 items_ _,__(__optional_ _)_) – Constraint Axis

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

  * **use_proportional_edit** (_boolean_ _,__(__optional_ _)_) – Proportional Editing

  * **proportional_edit_falloff** (enum in [Proportional Falloff Items](bpy_types_enum_items/proportional_falloff_items.html#rna-enum-proportional-falloff-items), (optional)) – Proportional Falloff, Falloff type for proportional editing mode

  * **proportional_size** (_float in_ _[__1e-06_ _,__inf_ _]__,__(__optional_ _)_) – Proportional Size

  * **use_proportional_connected** (_boolean_ _,__(__optional_ _)_) – Connected

  * **use_proportional_projected** (_boolean_ _,__(__optional_ _)_) – Projected (2D)

  * **snap** (_boolean_ _,__(__optional_ _)_) – Use Snapping Options

  * **snap_elements** (enum set in [Snap Element Items](bpy_types_enum_items/snap_element_items.html#rna-enum-snap-element-items), (optional)) – Snap to Elements

  * **use_snap_project** (_boolean_ _,__(__optional_ _)_) – Project Individual Elements

  * **snap_target** (enum in [Snap Source Items](bpy_types_enum_items/snap_source_items.html#rna-enum-snap-source-items), (optional)) – Snap Base, Point on source that will snap to target

  * **use_snap_self** (_boolean_ _,__(__optional_ _)_) – Target: Include Active

  * **use_snap_edit** (_boolean_ _,__(__optional_ _)_) – Target: Include Edit

  * **use_snap_nonedit** (_boolean_ _,__(__optional_ _)_) – Target: Include Non-Edited

  * **use_snap_selectable** (_boolean_ _,__(__optional_ _)_) – Target: Exclude Non-Selectable

  * **snap_point** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Point

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

bpy.ops.transform.tilt(_*_ , _value =0.0_, _mirror =False_,
_use_proportional_edit =False_, _proportional_edit_falloff =SMOOTH_,
_proportional_size =1.0_, _use_proportional_connected =False_,
_use_proportional_projected =False_, _snap =False_, _release_confirm =False_,
_use_accurate =False_)¶

    

Tilt selected control vertices of 3D curve

Parameters:

    

  * **value** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Angle

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

  * **use_proportional_edit** (_boolean_ _,__(__optional_ _)_) – Proportional Editing

  * **proportional_edit_falloff** (enum in [Proportional Falloff Items](bpy_types_enum_items/proportional_falloff_items.html#rna-enum-proportional-falloff-items), (optional)) – Proportional Falloff, Falloff type for proportional editing mode

  * **proportional_size** (_float in_ _[__1e-06_ _,__inf_ _]__,__(__optional_ _)_) – Proportional Size

  * **use_proportional_connected** (_boolean_ _,__(__optional_ _)_) – Connected

  * **use_proportional_projected** (_boolean_ _,__(__optional_ _)_) – Projected (2D)

  * **snap** (_boolean_ _,__(__optional_ _)_) – Use Snapping Options

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

bpy.ops.transform.tosphere(_*_ , _value =0.0_, _mirror =False_,
_use_proportional_edit =False_, _proportional_edit_falloff =SMOOTH_,
_proportional_size =1.0_, _use_proportional_connected =False_,
_use_proportional_projected =False_, _snap =False_, _gpencil_strokes =False_,
_center_override =(0.0, 0.0, 0.0)_, _release_confirm =False_, _use_accurate
=False_)¶

    

Move selected items outward in a spherical shape around geometric center

Parameters:

    

  * **value** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Factor

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

  * **use_proportional_edit** (_boolean_ _,__(__optional_ _)_) – Proportional Editing

  * **proportional_edit_falloff** (enum in [Proportional Falloff Items](bpy_types_enum_items/proportional_falloff_items.html#rna-enum-proportional-falloff-items), (optional)) – Proportional Falloff, Falloff type for proportional editing mode

  * **proportional_size** (_float in_ _[__1e-06_ _,__inf_ _]__,__(__optional_ _)_) – Proportional Size

  * **use_proportional_connected** (_boolean_ _,__(__optional_ _)_) – Connected

  * **use_proportional_projected** (_boolean_ _,__(__optional_ _)_) – Projected (2D)

  * **snap** (_boolean_ _,__(__optional_ _)_) – Use Snapping Options

  * **gpencil_strokes** (_boolean_ _,__(__optional_ _)_) – Edit Grease Pencil, Edit selected Grease Pencil strokes

  * **center_override** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Center Override, Force using this center value (when set)

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

bpy.ops.transform.trackball(_*_ , _value =(0.0, 0.0)_, _mirror =False_,
_use_proportional_edit =False_, _proportional_edit_falloff =SMOOTH_,
_proportional_size =1.0_, _use_proportional_connected =False_,
_use_proportional_projected =False_, _snap =False_, _gpencil_strokes =False_,
_center_override =(0.0, 0.0, 0.0)_, _release_confirm =False_, _use_accurate
=False_)¶

    

Trackball style rotation of selected items

Parameters:

    

  * **value** (_float array_ _of_ _2 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Angle

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

  * **use_proportional_edit** (_boolean_ _,__(__optional_ _)_) – Proportional Editing

  * **proportional_edit_falloff** (enum in [Proportional Falloff Items](bpy_types_enum_items/proportional_falloff_items.html#rna-enum-proportional-falloff-items), (optional)) – Proportional Falloff, Falloff type for proportional editing mode

  * **proportional_size** (_float in_ _[__1e-06_ _,__inf_ _]__,__(__optional_ _)_) – Proportional Size

  * **use_proportional_connected** (_boolean_ _,__(__optional_ _)_) – Connected

  * **use_proportional_projected** (_boolean_ _,__(__optional_ _)_) – Projected (2D)

  * **snap** (_boolean_ _,__(__optional_ _)_) – Use Snapping Options

  * **gpencil_strokes** (_boolean_ _,__(__optional_ _)_) – Edit Grease Pencil, Edit selected Grease Pencil strokes

  * **center_override** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Center Override, Force using this center value (when set)

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

bpy.ops.transform.transform(_*_ , _mode =TRANSLATION_, _value =(0.0, 0.0, 0.0,
0.0)_, _orient_axis =Z_, _orient_type =GLOBAL_, _orient_matrix =((0.0, 0.0,
0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0))_, _orient_matrix_type =GLOBAL_,
_constraint_axis =(False, False, False)_, _mirror =False_,
_use_proportional_edit =False_, _proportional_edit_falloff =SMOOTH_,
_proportional_size =1.0_, _use_proportional_connected =False_,
_use_proportional_projected =False_, _snap =False_, _snap_elements
={'INCREMENT'}_, _use_snap_project =False_, _snap_target =CLOSEST_,
_use_snap_self =True_, _use_snap_edit =True_, _use_snap_nonedit =True_,
_use_snap_selectable =False_, _snap_point =(0.0, 0.0, 0.0)_, _snap_align
=False_, _snap_normal =(0.0, 0.0, 0.0)_, _gpencil_strokes =False_,
_texture_space =False_, _remove_on_cancel =False_, _use_duplicated_keyframes
=False_, _center_override =(0.0, 0.0, 0.0)_, _release_confirm =False_,
_use_accurate =False_, _use_automerge_and_split =False_)¶

    

Transform selected items by mode type

Parameters:

    

  * **mode** (enum in [Transform Mode Type Items](bpy_types_enum_items/transform_mode_type_items.html#rna-enum-transform-mode-type-items), (optional)) – Mode

  * **value** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 4 items in [-inf, inf], (optional)) – Values

  * **orient_axis** (enum in [Axis Xyz Items](bpy_types_enum_items/axis_xyz_items.html#rna-enum-axis-xyz-items), (optional)) – Axis

  * **orient_type** (enum in [Transform Orientation Items](bpy_types_enum_items/transform_orientation_items.html#rna-enum-transform-orientation-items), (optional)) – Orientation, Transformation orientation

  * **orient_matrix** ([`mathutils.Matrix`](mathutils.html#mathutils.Matrix "mathutils.Matrix") of 3 * 3 items in [-inf, inf], (optional)) – Matrix

  * **orient_matrix_type** (enum in [Transform Orientation Items](bpy_types_enum_items/transform_orientation_items.html#rna-enum-transform-orientation-items), (optional)) – Matrix Orientation

  * **constraint_axis** (_boolean array_ _of_ _3 items_ _,__(__optional_ _)_) – Constraint Axis

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

  * **use_proportional_edit** (_boolean_ _,__(__optional_ _)_) – Proportional Editing

  * **proportional_edit_falloff** (enum in [Proportional Falloff Items](bpy_types_enum_items/proportional_falloff_items.html#rna-enum-proportional-falloff-items), (optional)) – Proportional Falloff, Falloff type for proportional editing mode

  * **proportional_size** (_float in_ _[__1e-06_ _,__inf_ _]__,__(__optional_ _)_) – Proportional Size

  * **use_proportional_connected** (_boolean_ _,__(__optional_ _)_) – Connected

  * **use_proportional_projected** (_boolean_ _,__(__optional_ _)_) – Projected (2D)

  * **snap** (_boolean_ _,__(__optional_ _)_) – Use Snapping Options

  * **snap_elements** (enum set in [Snap Element Items](bpy_types_enum_items/snap_element_items.html#rna-enum-snap-element-items), (optional)) – Snap to Elements

  * **use_snap_project** (_boolean_ _,__(__optional_ _)_) – Project Individual Elements

  * **snap_target** (enum in [Snap Source Items](bpy_types_enum_items/snap_source_items.html#rna-enum-snap-source-items), (optional)) – Snap Base, Point on source that will snap to target

  * **use_snap_self** (_boolean_ _,__(__optional_ _)_) – Target: Include Active

  * **use_snap_edit** (_boolean_ _,__(__optional_ _)_) – Target: Include Edit

  * **use_snap_nonedit** (_boolean_ _,__(__optional_ _)_) – Target: Include Non-Edited

  * **use_snap_selectable** (_boolean_ _,__(__optional_ _)_) – Target: Exclude Non-Selectable

  * **snap_point** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Point

  * **snap_align** (_boolean_ _,__(__optional_ _)_) – Align with Point Normal

  * **snap_normal** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Normal

  * **gpencil_strokes** (_boolean_ _,__(__optional_ _)_) – Edit Grease Pencil, Edit selected Grease Pencil strokes

  * **texture_space** (_boolean_ _,__(__optional_ _)_) – Edit Texture Space, Edit object data texture space

  * **remove_on_cancel** (_boolean_ _,__(__optional_ _)_) – Remove on Cancel, Remove elements on cancel

  * **use_duplicated_keyframes** (_boolean_ _,__(__optional_ _)_) – Duplicated Keyframes, Transform duplicated keyframes

  * **center_override** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Center Override, Force using this center value (when set)

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

  * **use_automerge_and_split** (_boolean_ _,__(__optional_ _)_) – Auto Merge & Split, Forces the use of Auto Merge and Split

bpy.ops.transform.translate(_*_ , _value =(0.0, 0.0, 0.0)_, _orient_type
=GLOBAL_, _orient_matrix =((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0,
0.0))_, _orient_matrix_type =GLOBAL_, _constraint_axis =(False, False,
False)_, _mirror =False_, _use_proportional_edit =False_,
_proportional_edit_falloff =SMOOTH_, _proportional_size =1.0_,
_use_proportional_connected =False_, _use_proportional_projected =False_,
_snap =False_, _snap_elements ={'INCREMENT'}_, _use_snap_project =False_,
_snap_target =CLOSEST_, _use_snap_self =True_, _use_snap_edit =True_,
_use_snap_nonedit =True_, _use_snap_selectable =False_, _snap_point =(0.0,
0.0, 0.0)_, _snap_align =False_, _snap_normal =(0.0, 0.0, 0.0)_,
_gpencil_strokes =False_, _cursor_transform =False_, _texture_space =False_,
_remove_on_cancel =False_, _use_duplicated_keyframes =False_, _view2d_edge_pan
=False_, _release_confirm =False_, _use_accurate =False_,
_use_automerge_and_split =False_, _translate_origin =False_)¶

    

Move selected items

Parameters:

    

  * **value** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Move

  * **orient_type** (enum in [Transform Orientation Items](bpy_types_enum_items/transform_orientation_items.html#rna-enum-transform-orientation-items), (optional)) – Orientation, Transformation orientation

  * **orient_matrix** ([`mathutils.Matrix`](mathutils.html#mathutils.Matrix "mathutils.Matrix") of 3 * 3 items in [-inf, inf], (optional)) – Matrix

  * **orient_matrix_type** (enum in [Transform Orientation Items](bpy_types_enum_items/transform_orientation_items.html#rna-enum-transform-orientation-items), (optional)) – Matrix Orientation

  * **constraint_axis** (_boolean array_ _of_ _3 items_ _,__(__optional_ _)_) – Constraint Axis

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

  * **use_proportional_edit** (_boolean_ _,__(__optional_ _)_) – Proportional Editing

  * **proportional_edit_falloff** (enum in [Proportional Falloff Items](bpy_types_enum_items/proportional_falloff_items.html#rna-enum-proportional-falloff-items), (optional)) – Proportional Falloff, Falloff type for proportional editing mode

  * **proportional_size** (_float in_ _[__1e-06_ _,__inf_ _]__,__(__optional_ _)_) – Proportional Size

  * **use_proportional_connected** (_boolean_ _,__(__optional_ _)_) – Connected

  * **use_proportional_projected** (_boolean_ _,__(__optional_ _)_) – Projected (2D)

  * **snap** (_boolean_ _,__(__optional_ _)_) – Use Snapping Options

  * **snap_elements** (enum set in [Snap Element Items](bpy_types_enum_items/snap_element_items.html#rna-enum-snap-element-items), (optional)) – Snap to Elements

  * **use_snap_project** (_boolean_ _,__(__optional_ _)_) – Project Individual Elements

  * **snap_target** (enum in [Snap Source Items](bpy_types_enum_items/snap_source_items.html#rna-enum-snap-source-items), (optional)) – Snap Base, Point on source that will snap to target

  * **use_snap_self** (_boolean_ _,__(__optional_ _)_) – Target: Include Active

  * **use_snap_edit** (_boolean_ _,__(__optional_ _)_) – Target: Include Edit

  * **use_snap_nonedit** (_boolean_ _,__(__optional_ _)_) – Target: Include Non-Edited

  * **use_snap_selectable** (_boolean_ _,__(__optional_ _)_) – Target: Exclude Non-Selectable

  * **snap_point** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Point

  * **snap_align** (_boolean_ _,__(__optional_ _)_) – Align with Point Normal

  * **snap_normal** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Normal

  * **gpencil_strokes** (_boolean_ _,__(__optional_ _)_) – Edit Grease Pencil, Edit selected Grease Pencil strokes

  * **cursor_transform** (_boolean_ _,__(__optional_ _)_) – Transform Cursor

  * **texture_space** (_boolean_ _,__(__optional_ _)_) – Edit Texture Space, Edit object data texture space

  * **remove_on_cancel** (_boolean_ _,__(__optional_ _)_) – Remove on Cancel, Remove elements on cancel

  * **use_duplicated_keyframes** (_boolean_ _,__(__optional_ _)_) – Duplicated Keyframes, Transform duplicated keyframes

  * **view2d_edge_pan** (_boolean_ _,__(__optional_ _)_) – Edge Pan, Enable edge panning in 2D view

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

  * **use_automerge_and_split** (_boolean_ _,__(__optional_ _)_) – Auto Merge & Split, Forces the use of Auto Merge and Split

  * **translate_origin** (_boolean_ _,__(__optional_ _)_) – Translate Origin, Translate origin instead of selection

bpy.ops.transform.vert_crease(_*_ , _value =0.0_, _snap =False_,
_release_confirm =False_, _use_accurate =False_)¶

    

Change the crease of vertices

Parameters:

    

  * **value** (_float in_ _[__-1_ _,__1_ _]__,__(__optional_ _)_) – Factor

  * **snap** (_boolean_ _,__(__optional_ _)_) – Use Snapping Options

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

bpy.ops.transform.vert_slide(_*_ , _value =0.0_, _use_even =False_, _flipped
=False_, _use_clamp =True_, _mirror =False_, _snap =False_, _snap_elements
={'INCREMENT'}_, _use_snap_project =False_, _snap_target =CLOSEST_,
_use_snap_self =True_, _use_snap_edit =True_, _use_snap_nonedit =True_,
_use_snap_selectable =False_, _snap_point =(0.0, 0.0, 0.0)_, _correct_uv
=True_, _release_confirm =False_, _use_accurate =False_)¶

    

Slide a vertex along a mesh

Parameters:

    

  * **value** (_float in_ _[__-10_ _,__10_ _]__,__(__optional_ _)_) – Factor

  * **use_even** (_boolean_ _,__(__optional_ _)_) – Even, Make the edge loop match the shape of the adjacent edge loop

  * **flipped** (_boolean_ _,__(__optional_ _)_) – Flipped, When Even mode is active, flips between the two adjacent edge loops

  * **use_clamp** (_boolean_ _,__(__optional_ _)_) – Clamp, Clamp within the edge extents

  * **mirror** (_boolean_ _,__(__optional_ _)_) – Mirror Editing

  * **snap** (_boolean_ _,__(__optional_ _)_) – Use Snapping Options

  * **snap_elements** (enum set in [Snap Element Items](bpy_types_enum_items/snap_element_items.html#rna-enum-snap-element-items), (optional)) – Snap to Elements

  * **use_snap_project** (_boolean_ _,__(__optional_ _)_) – Project Individual Elements

  * **snap_target** (enum in [Snap Source Items](bpy_types_enum_items/snap_source_items.html#rna-enum-snap-source-items), (optional)) – Snap Base, Point on source that will snap to target

  * **use_snap_self** (_boolean_ _,__(__optional_ _)_) – Target: Include Active

  * **use_snap_edit** (_boolean_ _,__(__optional_ _)_) – Target: Include Edit

  * **use_snap_nonedit** (_boolean_ _,__(__optional_ _)_) – Target: Include Non-Edited

  * **use_snap_selectable** (_boolean_ _,__(__optional_ _)_) – Target: Exclude Non-Selectable

  * **snap_point** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Point

  * **correct_uv** (_boolean_ _,__(__optional_ _)_) – Correct UVs, Correct UV coordinates when transforming

  * **release_confirm** (_boolean_ _,__(__optional_ _)_) – Confirm on Release, Always confirm operation when releasing button

  * **use_accurate** (_boolean_ _,__(__optional_ _)_) – Accurate, Use accurate transformation

bpy.ops.transform.vertex_random(_*_ , _offset =0.0_, _uniform =0.0_, _normal
=0.0_, _seed =0_, _wait_for_input =True_)¶

    

Randomize vertices

Parameters:

    

  * **offset** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Amount, Distance to offset

  * **uniform** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Uniform, Increase for uniform offset distance

  * **normal** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Normal, Align offset direction to normals

  * **seed** (_int in_ _[__0_ _,__10000_ _]__,__(__optional_ _)_) – Random Seed, Seed for the random number generator

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

bpy.ops.transform.vertex_warp(_*_ , _warp_angle =6.28319_, _offset_angle
=0.0_, _min =-1.0_, _max =1.0_, _viewmat =((0.0, 0.0, 0.0, 0.0), (0.0, 0.0,
0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))_, _center =(0.0, 0.0,
0.0)_)¶

    

Warp vertices around the cursor

Parameters:

    

  * **warp_angle** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Warp Angle, Amount to warp about the cursor

  * **offset_angle** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Offset Angle, Angle to use as the basis for warping

  * **min** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Min

  * **max** (_float in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Max

  * **viewmat** ([`mathutils.Matrix`](mathutils.html#mathutils.Matrix "mathutils.Matrix") of 4 * 4 items in [-inf, inf], (optional)) – Matrix

  * **center** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Center

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

