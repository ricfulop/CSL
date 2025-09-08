---
url: https://docs.blender.org/api/current/bpy.ops.geometry.html
scraped_at: 2025-09-08T14:18:13.478864
title: Geometry Operators¶
---

# Geometry Operators¶

bpy.ops.geometry.attribute_add(_*_ , _name =''_, _domain =POINT_, _data_type
=FLOAT_)¶

    

Add attribute to geometry

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of new attribute

  * **domain** (enum in [Attribute Domain Items](bpy_types_enum_items/attribute_domain_items.html#rna-enum-attribute-domain-items), (optional)) – Domain, Type of element that attribute is stored on

  * **data_type** (enum in [Attribute Type Items](bpy_types_enum_items/attribute_type_items.html#rna-enum-attribute-type-items), (optional)) – Data Type, Type of data stored in attribute

bpy.ops.geometry.attribute_convert(_*_ , _mode =GENERIC_, _domain =POINT_,
_data_type =FLOAT_)¶

    

Change how the attribute is stored

Parameters:

    

  * **mode** (enum in [`GENERIC`, `VERTEX_GROUP`], (optional)) – Mode

  * **domain** (enum in [Attribute Domain Items](bpy_types_enum_items/attribute_domain_items.html#rna-enum-attribute-domain-items), (optional)) – Domain, Which geometry element to move the attribute to

  * **data_type** (enum in [Attribute Type Items](bpy_types_enum_items/attribute_type_items.html#rna-enum-attribute-type-items), (optional)) – Data Type

bpy.ops.geometry.attribute_remove()¶

    

Remove attribute from geometry

bpy.ops.geometry.color_attribute_add(_*_ , _name =''_, _domain =POINT_,
_data_type =FLOAT_COLOR_, _color =(0.0, 0.0, 0.0, 1.0)_)¶

    

Add color attribute to geometry

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of new color attribute

  * **domain** (enum in [Color Attribute Domain Items](bpy_types_enum_items/color_attribute_domain_items.html#rna-enum-color-attribute-domain-items), (optional)) – Domain, Type of element that attribute is stored on

  * **data_type** (enum in [Color Attribute Type Items](bpy_types_enum_items/color_attribute_type_items.html#rna-enum-color-attribute-type-items), (optional)) – Data Type, Type of data stored in attribute

  * **color** (_float array_ _of_ _4 items in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Color, Default fill color

bpy.ops.geometry.color_attribute_convert(_*_ , _domain =POINT_, _data_type
=FLOAT_COLOR_)¶

    

Change how the color attribute is stored

Parameters:

    

  * **domain** (enum in [Color Attribute Domain Items](bpy_types_enum_items/color_attribute_domain_items.html#rna-enum-color-attribute-domain-items), (optional)) – Domain, Type of element that attribute is stored on

  * **data_type** (enum in [Color Attribute Type Items](bpy_types_enum_items/color_attribute_type_items.html#rna-enum-color-attribute-type-items), (optional)) – Data Type, Type of data stored in attribute

bpy.ops.geometry.color_attribute_duplicate()¶

    

Duplicate color attribute

bpy.ops.geometry.color_attribute_remove()¶

    

Remove color attribute from geometry

bpy.ops.geometry.color_attribute_render_set(_*_ , _name ='Color'_)¶

    

Set default color attribute used for rendering

Parameters:

    

**name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of color
attribute

bpy.ops.geometry.execute_node_group(_*_ , _asset_library_type =LOCAL_,
_asset_library_identifier =''_, _relative_asset_identifier =''_, _name =''_,
_session_uid =0_, _mouse_position =(0, 0)_, _region_size =(0, 0)_,
_cursor_position =(0.0, 0.0, 0.0)_, _cursor_rotation =(0.0, 0.0, 0.0, 0.0)_,
_viewport_projection_matrix =(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)_, _viewport_view_matrix =(0.0, 0.0, 0.0,
0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)_,
_viewport_is_perspective =False_)¶

    

Execute a node group on geometry

Parameters:

    

  * **asset_library_type** (enum in [Asset Library Type Items](bpy_types_enum_items/asset_library_type_items.html#rna-enum-asset-library-type-items), (optional)) – Asset Library Type

  * **asset_library_identifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Asset Library Identifier

  * **relative_asset_identifier** (_string_ _,__(__optional_ _,__never None_ _)_) – Relative Asset Identifier

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the data-block to use by the operator

  * **session_uid** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

  * **mouse_position** (_int array_ _of_ _2 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Mouse Position, Mouse coordinates in region space

  * **region_size** (_int array_ _of_ _2 items in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Region Size

  * **cursor_position** (_float array_ _of_ _3 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – 3D Cursor Position

  * **cursor_rotation** (_float array_ _of_ _4 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – 3D Cursor Rotation

  * **viewport_projection_matrix** (_float array_ _of_ _16 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Viewport Projection Transform

  * **viewport_view_matrix** (_float array_ _of_ _16 items in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Viewport View Transform

  * **viewport_is_perspective** (_boolean_ _,__(__optional_ _)_) – Viewport Is Perspective

bpy.ops.geometry.geometry_randomization(_*_ , _value =False_)¶

    

Toggle geometry randomization for debugging purposes

Parameters:

    

**value** (_boolean_ _,__(__optional_ _)_) – Value, Randomize the order of
geometry elements (e.g. vertices or edges) after some operations where there
are no guarantees about the order. This avoids accidentally depending on
something that may change in the future

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

