---
url: https://docs.blender.org/api/current/bpy.types.FreestyleLineSet.html
scraped_at: 2025-09-08T14:25:44.244062
title: FreestyleLineSet(bpy_struct)¶
---

# FreestyleLineSet(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.FreestyleLineSet(_bpy_struct_)¶

    

Line set for associating lines and style parameters

collection¶

    

A collection of objects based on which feature edges are selected

Type:

    

[`Collection`](bpy.types.Collection.html#bpy.types.Collection
"bpy.types.Collection")

collection_negation¶

    

Specify either inclusion or exclusion of feature edges belonging to a
collection of objects

  * `INCLUSIVE` Inclusive – Select feature edges belonging to some object in the group.

  * `EXCLUSIVE` Exclusive – Select feature edges not belonging to any object in the group.

Type:

    

enum in [`INCLUSIVE`, `EXCLUSIVE`], default `INCLUSIVE`

edge_type_combination¶

    

Specify a logical combination of selection conditions on feature edge types

  * `OR` Logical OR – Select feature edges satisfying at least one of edge type conditions.

  * `AND` Logical AND – Select feature edges satisfying all edge type conditions.

Type:

    

enum in [`OR`, `AND`], default `OR`

edge_type_negation¶

    

Specify either inclusion or exclusion of feature edges selected by edge types

  * `INCLUSIVE` Inclusive – Select feature edges satisfying the given edge type conditions.

  * `EXCLUSIVE` Exclusive – Select feature edges not satisfying the given edge type conditions.

Type:

    

enum in [`INCLUSIVE`, `EXCLUSIVE`], default `INCLUSIVE`

exclude_border¶

    

Exclude border edges

Type:

    

boolean, default False

exclude_contour¶

    

Exclude contours

Type:

    

boolean, default False

exclude_crease¶

    

Exclude crease edges

Type:

    

boolean, default False

exclude_edge_mark¶

    

Exclude edge marks

Type:

    

boolean, default False

exclude_external_contour¶

    

Exclude external contours

Type:

    

boolean, default False

exclude_material_boundary¶

    

Exclude edges at material boundaries

Type:

    

boolean, default False

exclude_ridge_valley¶

    

Exclude ridges and valleys

Type:

    

boolean, default False

exclude_silhouette¶

    

Exclude silhouette edges

Type:

    

boolean, default False

exclude_suggestive_contour¶

    

Exclude suggestive contours

Type:

    

boolean, default False

face_mark_condition¶

    

Specify a feature edge selection condition based on face marks

  * `ONE` One Face – Select a feature edge if either of its adjacent faces is marked.

  * `BOTH` Both Faces – Select a feature edge if both of its adjacent faces are marked.

Type:

    

enum in [`ONE`, `BOTH`], default `ONE`

face_mark_negation¶

    

Specify either inclusion or exclusion of feature edges selected by face marks

  * `INCLUSIVE` Inclusive – Select feature edges satisfying the given face mark conditions.

  * `EXCLUSIVE` Exclusive – Select feature edges not satisfying the given face mark conditions.

Type:

    

enum in [`INCLUSIVE`, `EXCLUSIVE`], default `INCLUSIVE`

linestyle¶

    

Line style settings

Type:

    

[`FreestyleLineStyle`](bpy.types.FreestyleLineStyle.html#bpy.types.FreestyleLineStyle
"bpy.types.FreestyleLineStyle"), (never None)

name¶

    

Line set name

Type:

    

string, default “”, (never None)

qi_end¶

    

Last QI value of the QI range

Type:

    

int in [0, inf], default 0

qi_start¶

    

First QI value of the QI range

Type:

    

int in [0, inf], default 0

select_border¶

    

Select border edges (open mesh edges)

Type:

    

boolean, default False

select_by_collection¶

    

Select feature edges based on a collection of objects

Type:

    

boolean, default False

select_by_edge_types¶

    

Select feature edges based on edge types

Type:

    

boolean, default False

select_by_face_marks¶

    

Select feature edges by face marks

Type:

    

boolean, default False

select_by_image_border¶

    

Select feature edges by image border (less memory consumption)

Type:

    

boolean, default False

select_by_visibility¶

    

Select feature edges based on visibility

Type:

    

boolean, default False

select_contour¶

    

Select contours (outer silhouettes of each object)

Type:

    

boolean, default False

select_crease¶

    

Select crease edges (those between two faces making an angle smaller than the
Crease Angle)

Type:

    

boolean, default False

select_edge_mark¶

    

Select edge marks (edges annotated by Freestyle edge marks)

Type:

    

boolean, default False

select_external_contour¶

    

Select external contours (outer silhouettes of occluding and occluded objects)

Type:

    

boolean, default False

select_material_boundary¶

    

Select edges at material boundaries

Type:

    

boolean, default False

select_ridge_valley¶

    

Select ridges and valleys (boundary lines between convex and concave areas of
surface)

Type:

    

boolean, default False

select_silhouette¶

    

Select silhouettes (edges at the boundary of visible and hidden faces)

Type:

    

boolean, default False

select_suggestive_contour¶

    

Select suggestive contours (almost silhouette/contour edges)

Type:

    

boolean, default False

show_render¶

    

Enable or disable this line set during stroke rendering

Type:

    

boolean, default False

visibility¶

    

Determine how to use visibility for feature edge selection

  * `VISIBLE` Visible – Select visible feature edges.

  * `HIDDEN` Hidden – Select hidden feature edges.

  * `RANGE` Quantitative Invisibility – Select feature edges within a range of quantitative invisibility (QI) values.

Type:

    

enum in [`VISIBLE`, `HIDDEN`, `RANGE`], default `VISIBLE`

_classmethod _bl_rna_get_subclass(_id_ , _default =None_, _/_)¶

    

Parameters:

    

**id** (_str_) – The RNA type identifier.

Returns:

    

The RNA type or default when not found.

Return type:

    

[`bpy.types.Struct`](bpy.types.Struct.html#bpy.types.Struct
"bpy.types.Struct") subclass

_classmethod _bl_rna_get_subclass_py(_id_ , _default =None_, _/_)¶

    

Parameters:

    

**id** (_str_) – The RNA type identifier.

Returns:

    

The class or default when not found.

Return type:

    

type

## Inherited Properties¶

  * [`bpy_struct.id_data`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.id_data "bpy.types.bpy_struct.id_data")

|

  
---|---  
  
## Inherited Functions¶

  * [`bpy_struct.as_pointer`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.as_pointer "bpy.types.bpy_struct.as_pointer")
  * [`bpy_struct.driver_add`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.driver_add "bpy.types.bpy_struct.driver_add")
  * [`bpy_struct.driver_remove`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.driver_remove "bpy.types.bpy_struct.driver_remove")
  * [`bpy_struct.get`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.get "bpy.types.bpy_struct.get")
  * [`bpy_struct.id_properties_clear`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.id_properties_clear "bpy.types.bpy_struct.id_properties_clear")
  * [`bpy_struct.id_properties_ensure`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.id_properties_ensure "bpy.types.bpy_struct.id_properties_ensure")
  * [`bpy_struct.id_properties_ui`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.id_properties_ui "bpy.types.bpy_struct.id_properties_ui")
  * [`bpy_struct.is_property_hidden`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.is_property_hidden "bpy.types.bpy_struct.is_property_hidden")
  * [`bpy_struct.is_property_overridable_library`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.is_property_overridable_library "bpy.types.bpy_struct.is_property_overridable_library")
  * [`bpy_struct.is_property_readonly`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.is_property_readonly "bpy.types.bpy_struct.is_property_readonly")
  * [`bpy_struct.is_property_set`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.is_property_set "bpy.types.bpy_struct.is_property_set")
  * [`bpy_struct.items`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.items "bpy.types.bpy_struct.items")

|

  * [`bpy_struct.keyframe_delete`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.keyframe_delete "bpy.types.bpy_struct.keyframe_delete")
  * [`bpy_struct.keyframe_insert`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.keyframe_insert "bpy.types.bpy_struct.keyframe_insert")
  * [`bpy_struct.keys`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.keys "bpy.types.bpy_struct.keys")
  * [`bpy_struct.path_from_id`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.path_from_id "bpy.types.bpy_struct.path_from_id")
  * [`bpy_struct.path_resolve`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.path_resolve "bpy.types.bpy_struct.path_resolve")
  * [`bpy_struct.pop`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.pop "bpy.types.bpy_struct.pop")
  * [`bpy_struct.property_overridable_library_set`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.property_overridable_library_set "bpy.types.bpy_struct.property_overridable_library_set")
  * [`bpy_struct.property_unset`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.property_unset "bpy.types.bpy_struct.property_unset")
  * [`bpy_struct.rna_ancestors`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.rna_ancestors "bpy.types.bpy_struct.rna_ancestors")
  * [`bpy_struct.type_recast`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.type_recast "bpy.types.bpy_struct.type_recast")
  * [`bpy_struct.values`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.values "bpy.types.bpy_struct.values")

  
---|---  
  
## References¶

  * [`Linesets.active`](bpy.types.Linesets.html#bpy.types.Linesets.active "bpy.types.Linesets.active")
  * [`Linesets.new`](bpy.types.Linesets.html#bpy.types.Linesets.new "bpy.types.Linesets.new")

|

  * [`Linesets.remove`](bpy.types.Linesets.html#bpy.types.Linesets.remove "bpy.types.Linesets.remove")
  * [`FreestyleSettings.linesets`](bpy.types.FreestyleSettings.html#bpy.types.FreestyleSettings.linesets "bpy.types.FreestyleSettings.linesets")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

