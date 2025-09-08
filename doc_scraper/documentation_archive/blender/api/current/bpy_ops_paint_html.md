---
url: https://docs.blender.org/api/current/bpy.ops.paint.html
scraped_at: 2025-09-08T14:18:33.637494
title: Paint Operators¶
---

# Paint Operators¶

bpy.ops.paint.add_simple_uvs()¶

    

Add cube map UVs on mesh

bpy.ops.paint.add_texture_paint_slot(_*_ , _type =BASE_COLOR_, _slot_type
=IMAGE_, _name ='Untitled'_, _color =(0.0, 0.0, 0.0, 1.0)_, _width =1024_,
_height =1024_, _alpha =True_, _generated_type =BLANK_, _float =False_,
_domain =POINT_, _data_type =FLOAT_COLOR_)¶

    

Add a paint slot

Parameters:

    

  * **type** (enum in [`BASE_COLOR`, `SPECULAR`, `ROUGHNESS`, `METALLIC`, `NORMAL`, `BUMP`, `DISPLACEMENT`], (optional)) – Material Layer Type, Material layer type of new paint slot

  * **slot_type** (enum in [`IMAGE`, `COLOR_ATTRIBUTE`], (optional)) – Slot Type, Type of new paint slot

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name for new paint slot source

  * **color** (_float array_ _of_ _4 items in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Color, Default fill color

  * **width** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Width, Image width

  * **height** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Height, Image height

  * **alpha** (_boolean_ _,__(__optional_ _)_) – Alpha, Create an image with an alpha channel

  * **generated_type** (enum in [Image Generated Type Items](bpy_types_enum_items/image_generated_type_items.html#rna-enum-image-generated-type-items), (optional)) – Generated Type, Fill the image with a grid for UV map testing

  * **float** (_boolean_ _,__(__optional_ _)_) – 32-bit Float, Create image with 32-bit floating-point bit depth

  * **domain** (enum in [Color Attribute Domain Items](bpy_types_enum_items/color_attribute_domain_items.html#rna-enum-color-attribute-domain-items), (optional)) – Domain, Type of element that attribute is stored on

  * **data_type** (enum in [Color Attribute Type Items](bpy_types_enum_items/color_attribute_type_items.html#rna-enum-color-attribute-type-items), (optional)) – Data Type, Type of data stored in attribute

bpy.ops.paint.brush_colors_flip()¶

    

Swap primary and secondary brush colors

bpy.ops.paint.face_select_all(_*_ , _action =TOGGLE_)¶

    

Change selection for all faces

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.paint.face_select_hide(_*_ , _unselected =False_)¶

    

Hide selected faces

Parameters:

    

**unselected** (_boolean_ _,__(__optional_ _)_) – Unselected, Hide unselected
rather than selected objects

bpy.ops.paint.face_select_less(_*_ , _face_step =True_)¶

    

Deselect Faces connected to existing selection

Parameters:

    

**face_step** (_boolean_ _,__(__optional_ _)_) – Face Step, Also deselect
faces that only touch on a corner

bpy.ops.paint.face_select_linked()¶

    

Select linked faces

bpy.ops.paint.face_select_linked_pick(_*_ , _deselect =False_)¶

    

Select linked faces under the cursor

Parameters:

    

**deselect** (_boolean_ _,__(__optional_ _)_) – Deselect, Deselect rather than
select items

bpy.ops.paint.face_select_loop(_*_ , _select =True_, _extend =False_)¶

    

Select face loop under the cursor

Parameters:

    

  * **select** (_boolean_ _,__(__optional_ _)_) – Select, If false, faces will be deselected

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend the selection

bpy.ops.paint.face_select_more(_*_ , _face_step =True_)¶

    

Select Faces connected to existing selection

Parameters:

    

**face_step** (_boolean_ _,__(__optional_ _)_) – Face Step, Also select faces
that only touch on a corner

bpy.ops.paint.face_vert_reveal(_*_ , _select =True_)¶

    

Reveal hidden faces and vertices

Parameters:

    

**select** (_boolean_ _,__(__optional_ _)_) – Select, Specifies whether the
newly revealed geometry should be selected

bpy.ops.paint.grab_clone(_*_ , _delta =(0.0, 0.0)_)¶

    

Move the clone source image

Parameters:

    

**delta** ([`mathutils.Vector`](mathutils.html#mathutils.Vector
"mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Delta, Delta
offset of clone image in 0.0 to 1.0 coordinates

bpy.ops.paint.hide_show(_*_ , _xmin =0_, _xmax =0_, _ymin =0_, _ymax =0_,
_wait_for_input =True_, _action =HIDE_, _area =Inside_, _use_front_faces_only
=False_)¶

    

Hide/show some vertices

Parameters:

    

  * **xmin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Min

  * **xmax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Max

  * **ymin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Min

  * **ymax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Max

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

  * **action** (enum in [`HIDE`, `SHOW`], (optional)) – 

Visibility Action, Whether to hide or show vertices

    * `HIDE` Hide – Hide vertices.

    * `SHOW` Show – Show vertices.

  * **area** (enum in [`OUTSIDE`, `Inside`], (optional)) – 

Visibility Area, Which vertices to hide or show

    * `OUTSIDE` Outside – Hide or show vertices outside the selection.

    * `Inside` Inside – Hide or show vertices inside the selection.

  * **use_front_faces_only** (_boolean_ _,__(__optional_ _)_) – Front Faces Only, Affect only faces facing towards the view

bpy.ops.paint.hide_show_all(_*_ , _action =HIDE_)¶

    

Hide/show all vertices

Parameters:

    

**action** (enum in [`HIDE`, `SHOW`], (optional)) –

Visibility Action, Whether to hide or show vertices

  * `HIDE` Hide – Hide vertices.

  * `SHOW` Show – Show vertices.

bpy.ops.paint.hide_show_lasso_gesture(_*_ , _path =None_, _use_smooth_stroke
=False_, _smooth_stroke_factor =0.75_, _smooth_stroke_radius =35_, _action
=HIDE_, _area =Inside_, _use_front_faces_only =False_)¶

    

Hide/show some vertices

Parameters:

    

  * **path** (`bpy_prop_collection` of `OperatorMousePath`, (optional)) – Path

  * **use_smooth_stroke** (_boolean_ _,__(__optional_ _)_) – Stabilize Stroke, Selection lags behind mouse and follows a smoother path

  * **smooth_stroke_factor** (_float in_ _[__0.5_ _,__0.99_ _]__,__(__optional_ _)_) – Smooth Stroke Factor, Higher values gives a smoother stroke

  * **smooth_stroke_radius** (_int in_ _[__10_ _,__200_ _]__,__(__optional_ _)_) – Smooth Stroke Radius, Minimum distance from last point before selection continues

  * **action** (enum in [`HIDE`, `SHOW`], (optional)) – 

Visibility Action, Whether to hide or show vertices

    * `HIDE` Hide – Hide vertices.

    * `SHOW` Show – Show vertices.

  * **area** (enum in [`OUTSIDE`, `Inside`], (optional)) – 

Visibility Area, Which vertices to hide or show

    * `OUTSIDE` Outside – Hide or show vertices outside the selection.

    * `Inside` Inside – Hide or show vertices inside the selection.

  * **use_front_faces_only** (_boolean_ _,__(__optional_ _)_) – Front Faces Only, Affect only faces facing towards the view

bpy.ops.paint.hide_show_line_gesture(_*_ , _xstart =0_, _xend =0_, _ystart
=0_, _yend =0_, _flip =False_, _cursor =5_, _action =HIDE_, _area =Inside_,
_use_front_faces_only =False_, _use_limit_to_segment =False_)¶

    

Hide/show some vertices

Parameters:

    

  * **xstart** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Start

  * **xend** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X End

  * **ystart** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Start

  * **yend** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y End

  * **flip** (_boolean_ _,__(__optional_ _)_) – Flip

  * **cursor** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Cursor, Mouse cursor style to use during the modal operator

  * **action** (enum in [`HIDE`, `SHOW`], (optional)) – 

Visibility Action, Whether to hide or show vertices

    * `HIDE` Hide – Hide vertices.

    * `SHOW` Show – Show vertices.

  * **area** (enum in [`OUTSIDE`, `Inside`], (optional)) – 

Visibility Area, Which vertices to hide or show

    * `OUTSIDE` Outside – Hide or show vertices outside the selection.

    * `Inside` Inside – Hide or show vertices inside the selection.

  * **use_front_faces_only** (_boolean_ _,__(__optional_ _)_) – Front Faces Only, Affect only faces facing towards the view

  * **use_limit_to_segment** (_boolean_ _,__(__optional_ _)_) – Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line

bpy.ops.paint.hide_show_masked(_*_ , _action =HIDE_)¶

    

Hide/show all masked vertices above a threshold

Parameters:

    

**action** (enum in [`HIDE`, `SHOW`], (optional)) –

Visibility Action, Whether to hide or show vertices

  * `HIDE` Hide – Hide vertices.

  * `SHOW` Show – Show vertices.

bpy.ops.paint.hide_show_polyline_gesture(_*_ , _path =None_, _action =HIDE_,
_area =Inside_, _use_front_faces_only =False_)¶

    

Hide/show some vertices

Parameters:

    

  * **path** (`bpy_prop_collection` of `OperatorMousePath`, (optional)) – Path

  * **action** (enum in [`HIDE`, `SHOW`], (optional)) – 

Visibility Action, Whether to hide or show vertices

    * `HIDE` Hide – Hide vertices.

    * `SHOW` Show – Show vertices.

  * **area** (enum in [`OUTSIDE`, `Inside`], (optional)) – 

Visibility Area, Which vertices to hide or show

    * `OUTSIDE` Outside – Hide or show vertices outside the selection.

    * `Inside` Inside – Hide or show vertices inside the selection.

  * **use_front_faces_only** (_boolean_ _,__(__optional_ _)_) – Front Faces Only, Affect only faces facing towards the view

bpy.ops.paint.image_from_view(_*_ , _filepath =''_)¶

    

Make an image from biggest 3D view for reprojection

Parameters:

    

**filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Name
of the file

bpy.ops.paint.image_paint(_*_ , _stroke =None_, _mode =NORMAL_, _pen_flip
=False_)¶

    

Paint a stroke into the image

Parameters:

    

  * **stroke** (`bpy_prop_collection` of `OperatorStrokeElement`, (optional)) – Stroke

  * **mode** (enum in [`NORMAL`, `INVERT`, `SMOOTH`, `ERASE`], (optional)) – 

Stroke Mode, Action taken when a paint stroke is made

    * `NORMAL` Regular – Apply brush normally.

    * `INVERT` Invert – Invert action of brush for duration of stroke.

    * `SMOOTH` Smooth – Switch brush to smooth mode for duration of stroke.

    * `ERASE` Erase – Switch brush to erase mode for duration of stroke.

  * **pen_flip** (_boolean_ _,__(__optional_ _)_) – Pen Flip, Whether a tablet’s eraser mode is being used

bpy.ops.paint.mask_box_gesture(_*_ , _xmin =0_, _xmax =0_, _ymin =0_, _ymax
=0_, _wait_for_input =True_, _use_front_faces_only =False_, _mode =VALUE_,
_value =1.0_)¶

    

Mask within a rectangle defined by the cursor

Parameters:

    

  * **xmin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Min

  * **xmax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Max

  * **ymin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Min

  * **ymax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Max

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

  * **use_front_faces_only** (_boolean_ _,__(__optional_ _)_) – Front Faces Only, Affect only faces facing towards the view

  * **mode** (enum in [`VALUE`, `VALUE_INVERSE`, `INVERT`], (optional)) – 

Mode

    * `VALUE` Value – Set mask to the level specified by the ‘value’ property.

    * `VALUE_INVERSE` Value Inverted – Set mask to the level specified by the inverted ‘value’ property.

    * `INVERT` Invert – Invert the mask.

  * **value** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Value, Mask level to use when mode is ‘Value’; zero means no masking and one is fully masked

bpy.ops.paint.mask_flood_fill(_*_ , _mode =VALUE_, _value =0.0_)¶

    

Fill the whole mask with a given value, or invert its values

Parameters:

    

  * **mode** (enum in [`VALUE`, `VALUE_INVERSE`, `INVERT`], (optional)) – 

Mode

    * `VALUE` Value – Set mask to the level specified by the ‘value’ property.

    * `VALUE_INVERSE` Value Inverted – Set mask to the level specified by the inverted ‘value’ property.

    * `INVERT` Invert – Invert the mask.

  * **value** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Value, Mask level to use when mode is ‘Value’; zero means no masking and one is fully masked

bpy.ops.paint.mask_lasso_gesture(_*_ , _path =None_, _use_smooth_stroke
=False_, _smooth_stroke_factor =0.75_, _smooth_stroke_radius =35_,
_use_front_faces_only =False_, _mode =VALUE_, _value =1.0_)¶

    

Mask within a shape defined by the cursor

Parameters:

    

  * **path** (`bpy_prop_collection` of `OperatorMousePath`, (optional)) – Path

  * **use_smooth_stroke** (_boolean_ _,__(__optional_ _)_) – Stabilize Stroke, Selection lags behind mouse and follows a smoother path

  * **smooth_stroke_factor** (_float in_ _[__0.5_ _,__0.99_ _]__,__(__optional_ _)_) – Smooth Stroke Factor, Higher values gives a smoother stroke

  * **smooth_stroke_radius** (_int in_ _[__10_ _,__200_ _]__,__(__optional_ _)_) – Smooth Stroke Radius, Minimum distance from last point before selection continues

  * **use_front_faces_only** (_boolean_ _,__(__optional_ _)_) – Front Faces Only, Affect only faces facing towards the view

  * **mode** (enum in [`VALUE`, `VALUE_INVERSE`, `INVERT`], (optional)) – 

Mode

    * `VALUE` Value – Set mask to the level specified by the ‘value’ property.

    * `VALUE_INVERSE` Value Inverted – Set mask to the level specified by the inverted ‘value’ property.

    * `INVERT` Invert – Invert the mask.

  * **value** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Value, Mask level to use when mode is ‘Value’; zero means no masking and one is fully masked

bpy.ops.paint.mask_line_gesture(_*_ , _xstart =0_, _xend =0_, _ystart =0_,
_yend =0_, _flip =False_, _cursor =5_, _use_front_faces_only =False_,
_use_limit_to_segment =False_, _mode =VALUE_, _value =1.0_)¶

    

Mask to one side of a line defined by the cursor

Parameters:

    

  * **xstart** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Start

  * **xend** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X End

  * **ystart** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Start

  * **yend** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y End

  * **flip** (_boolean_ _,__(__optional_ _)_) – Flip

  * **cursor** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Cursor, Mouse cursor style to use during the modal operator

  * **use_front_faces_only** (_boolean_ _,__(__optional_ _)_) – Front Faces Only, Affect only faces facing towards the view

  * **use_limit_to_segment** (_boolean_ _,__(__optional_ _)_) – Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line

  * **mode** (enum in [`VALUE`, `VALUE_INVERSE`, `INVERT`], (optional)) – 

Mode

    * `VALUE` Value – Set mask to the level specified by the ‘value’ property.

    * `VALUE_INVERSE` Value Inverted – Set mask to the level specified by the inverted ‘value’ property.

    * `INVERT` Invert – Invert the mask.

  * **value** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Value, Mask level to use when mode is ‘Value’; zero means no masking and one is fully masked

bpy.ops.paint.mask_polyline_gesture(_*_ , _path =None_, _use_front_faces_only
=False_, _mode =VALUE_, _value =1.0_)¶

    

Mask within a shape defined by the cursor

Parameters:

    

  * **path** (`bpy_prop_collection` of `OperatorMousePath`, (optional)) – Path

  * **use_front_faces_only** (_boolean_ _,__(__optional_ _)_) – Front Faces Only, Affect only faces facing towards the view

  * **mode** (enum in [`VALUE`, `VALUE_INVERSE`, `INVERT`], (optional)) – 

Mode

    * `VALUE` Value – Set mask to the level specified by the ‘value’ property.

    * `VALUE_INVERSE` Value Inverted – Set mask to the level specified by the inverted ‘value’ property.

    * `INVERT` Invert – Invert the mask.

  * **value** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Value, Mask level to use when mode is ‘Value’; zero means no masking and one is fully masked

bpy.ops.paint.project_image(_*_ , _image_)¶

    

Project an edited render from the active camera back onto the object

Parameters:

    

**image** (_enum in_ _[__]__,__(__optional_ _)_) – Image

bpy.ops.paint.sample_color(_*_ , _location =(0, 0)_, _merged =False_, _palette
=False_)¶

    

Use the mouse to sample a color in the image

Parameters:

    

  * **location** (_int array_ _of_ _2 items in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Location

  * **merged** (_boolean_ _,__(__optional_ _)_) – Sample Merged, Sample the output display color

  * **palette** (_boolean_ _,__(__optional_ _)_) – Add to Palette

bpy.ops.paint.texture_paint_toggle()¶

    

Toggle texture paint mode in 3D view

bpy.ops.paint.vert_select_all(_*_ , _action =TOGGLE_)¶

    

Change selection for all vertices

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.paint.vert_select_hide(_*_ , _unselected =False_)¶

    

Hide selected vertices

Parameters:

    

**unselected** (_boolean_ _,__(__optional_ _)_) – Unselected, Hide unselected
rather than selected vertices

bpy.ops.paint.vert_select_less(_*_ , _face_step =True_)¶

    

Deselect Vertices connected to existing selection

Parameters:

    

**face_step** (_boolean_ _,__(__optional_ _)_) – Face Step, Also deselect
faces that only touch on a corner

bpy.ops.paint.vert_select_linked()¶

    

Select linked vertices

bpy.ops.paint.vert_select_linked_pick(_*_ , _select =True_)¶

    

Select linked vertices under the cursor

Parameters:

    

**select** (_boolean_ _,__(__optional_ _)_) – Select, Whether to select or
deselect linked vertices under the cursor

bpy.ops.paint.vert_select_more(_*_ , _face_step =True_)¶

    

Select Vertices connected to existing selection

Parameters:

    

**face_step** (_boolean_ _,__(__optional_ _)_) – Face Step, Also select faces
that only touch on a corner

bpy.ops.paint.vert_select_ungrouped(_*_ , _extend =False_)¶

    

Select vertices without a group

Parameters:

    

**extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend the selection

bpy.ops.paint.vertex_color_brightness_contrast(_*_ , _brightness =0.0_,
_contrast =0.0_)¶

    

Adjust vertex color brightness/contrast

Parameters:

    

  * **brightness** (_float in_ _[__-100_ _,__100_ _]__,__(__optional_ _)_) – Brightness

  * **contrast** (_float in_ _[__-100_ _,__100_ _]__,__(__optional_ _)_) – Contrast

bpy.ops.paint.vertex_color_dirt(_*_ , _blur_strength =1.0_, _blur_iterations
=1_, _clean_angle =3.14159_, _dirt_angle =0.0_, _dirt_only =False_, _normalize
=True_)¶

    

Generate a dirt map gradient based on cavity

Parameters:

    

  * **blur_strength** (_float in_ _[__0.01_ _,__1_ _]__,__(__optional_ _)_) – Blur Strength, Blur strength per iteration

  * **blur_iterations** (_int in_ _[__0_ _,__40_ _]__,__(__optional_ _)_) – Blur Iterations, Number of times to blur the colors (higher blurs more)

  * **clean_angle** (_float in_ _[__0_ _,__3.14159_ _]__,__(__optional_ _)_) – Highlight Angle, Less than 90 limits the angle used in the tonal range

  * **dirt_angle** (_float in_ _[__0_ _,__3.14159_ _]__,__(__optional_ _)_) – Dirt Angle, Less than 90 limits the angle used in the tonal range

  * **dirt_only** (_boolean_ _,__(__optional_ _)_) – Dirt Only, Don’t calculate cleans for convex areas

  * **normalize** (_boolean_ _,__(__optional_ _)_) – Normalize, Normalize the colors, increasing the contrast

File:

    

[startup/bl_operators/vertexpaint_dirt.py:179](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/vertexpaint_dirt.py#L179)

bpy.ops.paint.vertex_color_from_weight()¶

    

Convert active weight into gray scale vertex colors

bpy.ops.paint.vertex_color_hsv(_*_ , _h =0.5_, _s =1.0_, _v =1.0_)¶

    

Adjust vertex color Hue/Saturation/Value

Parameters:

    

  * **h** (_float in_ _[__0_ _,__1_ _]__,__(__optional_ _)_) – Hue

  * **s** (_float in_ _[__0_ _,__2_ _]__,__(__optional_ _)_) – Saturation

  * **v** (_float in_ _[__0_ _,__2_ _]__,__(__optional_ _)_) – Value

bpy.ops.paint.vertex_color_invert()¶

    

Invert RGB values

bpy.ops.paint.vertex_color_levels(_*_ , _offset =0.0_, _gain =1.0_)¶

    

Adjust levels of vertex colors

Parameters:

    

  * **offset** (_float in_ _[__-1_ _,__1_ _]__,__(__optional_ _)_) – Offset, Value to add to colors

  * **gain** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Gain, Value to multiply colors by

bpy.ops.paint.vertex_color_set(_*_ , _use_alpha =True_)¶

    

Fill the active vertex color layer with the current paint color

Parameters:

    

**use_alpha** (_boolean_ _,__(__optional_ _)_) – Affect Alpha, Set color
completely opaque instead of reusing existing alpha

bpy.ops.paint.vertex_color_smooth()¶

    

Smooth colors across vertices

bpy.ops.paint.vertex_paint(_*_ , _stroke =None_, _mode =NORMAL_, _pen_flip
=False_, _override_location =False_)¶

    

Paint a stroke in the active color attribute layer

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

bpy.ops.paint.vertex_paint_toggle()¶

    

Toggle the vertex paint mode in 3D view

bpy.ops.paint.visibility_filter(_*_ , _action =GROW_, _iterations =1_,
_auto_iteration_count =True_)¶

    

Edit the visibility of the current mesh

Parameters:

    

  * **action** (enum in [`GROW`, `SHRINK`], (optional)) – 

Action

    * `GROW` Grow Visibility – Grow the visibility by one face based on mesh topology.

    * `SHRINK` Shrink Visibility – Shrink the visibility by one face based on mesh topology.

  * **iterations** (_int in_ _[__1_ _,__100_ _]__,__(__optional_ _)_) – Iterations, Number of times that the filter is going to be applied

  * **auto_iteration_count** (_boolean_ _,__(__optional_ _)_) – Auto Iteration Count, Use an automatic number of iterations based on the number of vertices of the sculpt

bpy.ops.paint.visibility_invert()¶

    

Invert the visibility of all vertices

bpy.ops.paint.weight_from_bones(_*_ , _type =AUTOMATIC_)¶

    

Set the weights of the groups matching the attached armature’s selected bones,
using the distance between the vertices and the bones

Parameters:

    

**type** (enum in [`AUTOMATIC`, `ENVELOPES`], (optional)) –

Type, Method to use for assigning weights

  * `AUTOMATIC` Automatic – Automatic weights from bones.

  * `ENVELOPES` From Envelopes – Weights from envelopes with user defined radius.

bpy.ops.paint.weight_gradient(_*_ , _type =LINEAR_, _xstart =0_, _xend =0_,
_ystart =0_, _yend =0_, _flip =False_, _cursor =5_)¶

    

Draw a line to apply a weight gradient to selected vertices

Parameters:

    

  * **type** (enum in [`LINEAR`, `RADIAL`], (optional)) – Type

  * **xstart** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Start

  * **xend** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X End

  * **ystart** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Start

  * **yend** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y End

  * **flip** (_boolean_ _,__(__optional_ _)_) – Flip

  * **cursor** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Cursor, Mouse cursor style to use during the modal operator

bpy.ops.paint.weight_paint(_*_ , _stroke =None_, _mode =NORMAL_, _pen_flip
=False_, _override_location =False_)¶

    

Paint a stroke in the current vertex group’s weights

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

bpy.ops.paint.weight_paint_toggle()¶

    

Toggle weight paint mode in 3D view

bpy.ops.paint.weight_sample()¶

    

Use the mouse to sample a weight in the 3D view

bpy.ops.paint.weight_sample_group()¶

    

Select one of the vertex groups available under current mouse position

bpy.ops.paint.weight_set()¶

    

Fill the active vertex group with the current paint weight

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

