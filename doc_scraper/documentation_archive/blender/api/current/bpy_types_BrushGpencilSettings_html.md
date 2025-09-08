---
url: https://docs.blender.org/api/current/bpy.types.BrushGpencilSettings.html
scraped_at: 2025-09-08T14:21:20.266180
title: BrushGpencilSettings(bpy_struct)¶
---

# BrushGpencilSettings(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.BrushGpencilSettings(_bpy_struct_)¶

    

Settings for Grease Pencil brush

active_smooth_factor¶

    

Amount of smoothing while drawing

Type:

    

float in [0, 1], default 0.0

angle¶

    

Direction of the stroke at which brush gives maximal thickness (0° for
horizontal)

Type:

    

float in [-1.5708, 1.5708], default 0.0

angle_factor¶

    

Reduce brush thickness by this factor when stroke is perpendicular to ‘Angle’
direction

Type:

    

float in [0, 1], default 0.0

aspect¶

    

Type:

    

[`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 2
items in [0.01, 1], default (1.0, 1.0)

brush_draw_mode¶

    

Preselected mode when using this brush

  * `ACTIVE` Active – Use current mode.

  * `MATERIAL` Material – Use always material mode.

  * `VERTEXCOLOR` Vertex Color – Use always Vertex Color mode.

Type:

    

enum in [`ACTIVE`, `MATERIAL`, `VERTEXCOLOR`], default `ACTIVE`

caps_type¶

    

The shape of the start and end of the stroke

Type:

    

enum in [`ROUND`, `FLAT`], default `ROUND`

curve_jitter¶

    

Curve used for the jitter effect

Type:

    

[`CurveMapping`](bpy.types.CurveMapping.html#bpy.types.CurveMapping
"bpy.types.CurveMapping"), (readonly)

curve_random_hue¶

    

Curve used for modulating effect

Type:

    

[`CurveMapping`](bpy.types.CurveMapping.html#bpy.types.CurveMapping
"bpy.types.CurveMapping"), (readonly)

curve_random_pressure¶

    

Curve used for modulating effect

Type:

    

[`CurveMapping`](bpy.types.CurveMapping.html#bpy.types.CurveMapping
"bpy.types.CurveMapping"), (readonly)

curve_random_saturation¶

    

Curve used for modulating effect

Type:

    

[`CurveMapping`](bpy.types.CurveMapping.html#bpy.types.CurveMapping
"bpy.types.CurveMapping"), (readonly)

curve_random_strength¶

    

Curve used for modulating effect

Type:

    

[`CurveMapping`](bpy.types.CurveMapping.html#bpy.types.CurveMapping
"bpy.types.CurveMapping"), (readonly)

curve_random_uv¶

    

Curve used for modulating effect

Type:

    

[`CurveMapping`](bpy.types.CurveMapping.html#bpy.types.CurveMapping
"bpy.types.CurveMapping"), (readonly)

curve_random_value¶

    

Curve used for modulating effect

Type:

    

[`CurveMapping`](bpy.types.CurveMapping.html#bpy.types.CurveMapping
"bpy.types.CurveMapping"), (readonly)

curve_sensitivity¶

    

Curve used for the sensitivity

Type:

    

[`CurveMapping`](bpy.types.CurveMapping.html#bpy.types.CurveMapping
"bpy.types.CurveMapping"), (readonly)

curve_strength¶

    

Curve used for the strength

Type:

    

[`CurveMapping`](bpy.types.CurveMapping.html#bpy.types.CurveMapping
"bpy.types.CurveMapping"), (readonly)

dilate¶

    

Number of pixels to expand or contract fill area

Type:

    

int in [-40, 40], default 1

eraser_mode¶

    

Eraser Mode

  * `SOFT` Dissolve – Erase strokes, fading their points strength and thickness.

  * `HARD` Point – Erase stroke points.

  * `STROKE` Stroke – Erase entire strokes.

Type:

    

enum in [`SOFT`, `HARD`, `STROKE`], default `SOFT`

eraser_strength_factor¶

    

Amount of erasing for strength

Type:

    

float in [0, 100], default 0.0

eraser_thickness_factor¶

    

Amount of erasing for thickness

Type:

    

float in [0, 100], default 0.0

extend_stroke_factor¶

    

Strokes end extension for closing gaps, use zero to disable

Type:

    

float in [0, 10], default 0.0

fill_direction¶

    

Direction of the fill

  * `NORMAL` Normal – Fill internal area.

  * `INVERT` Inverted – Fill inverted area.

Type:

    

enum in [`NORMAL`, `INVERT`], default `NORMAL`

fill_draw_mode¶

    

Mode to draw boundary limits

  * `BOTH` All – Use both visible strokes and edit lines as fill boundary limits.

  * `STROKE` Strokes – Use visible strokes as fill boundary limits.

  * `CONTROL` Edit Lines – Use edit lines as fill boundary limits.

Type:

    

enum in [`BOTH`, `STROKE`, `CONTROL`], default `BOTH`

fill_extend_mode¶

    

Types of stroke extensions used for closing gaps

  * `EXTEND` Extend – Extend strokes in straight lines.

  * `RADIUS` Radius – Connect endpoints that are close together.

Type:

    

enum in [`EXTEND`, `RADIUS`], default `EXTEND`

fill_factor¶

    

Factor for fill boundary accuracy, higher values are more accurate but slower

Type:

    

float in [0.05, 8], default 0.0

fill_layer_mode¶

    

Layers used as boundaries

  * `VISIBLE` Visible – Visible layers.

  * `ACTIVE` Active – Only active layer.

  * `ABOVE` Layer Above – Layer above active.

  * `BELOW` Layer Below – Layer below active.

  * `ALL_ABOVE` All Above – All layers above active.

  * `ALL_BELOW` All Below – All layers below active.

Type:

    

enum in [`VISIBLE`, `ACTIVE`, `ABOVE`, `BELOW`, `ALL_ABOVE`, `ALL_BELOW`],
default `VISIBLE`

fill_simplify_level¶

    

Number of simplify steps (large values reduce fill accuracy)

Type:

    

int in [0, 10], default 0

fill_threshold¶

    

Threshold to consider color transparent for filling

Type:

    

float in [0, 1], default 0.0

hardness¶

    

Gradient from the center of Dot and Box strokes (set to 1 for a solid stroke)

Type:

    

float in [0.001, 1], default 1.0

input_samples¶

    

Generated intermediate points for very fast mouse movements (Set to 0 to
disable)

Type:

    

int in [0, 10], default 0

material¶

    

Material used for strokes drawn using this brush

Type:

    

[`Material`](bpy.types.Material.html#bpy.types.Material "bpy.types.Material")

material_alt¶

    

Material used for secondary uses for this brush

Type:

    

[`Material`](bpy.types.Material.html#bpy.types.Material "bpy.types.Material")

outline_thickness_factor¶

    

Thickness of the outline stroke relative to current brush thickness

Type:

    

float in [0, 1], default 0.0

pen_jitter¶

    

Jitter factor of brush radius for new strokes

Type:

    

float in [0, 100], default 0.0

pen_smooth_factor¶

    

Amount of smoothing to apply after finish newly created strokes, to reduce
jitter/noise

Type:

    

float in [0, 2], default 0.0

pen_smooth_steps¶

    

Number of times to smooth newly created strokes

Type:

    

int in [0, 100], default 0

pen_strength¶

    

Color strength for new strokes (affect alpha factor of color)

Type:

    

float in [0, 1], default 0.0

pen_subdivision_steps¶

    

Number of times to subdivide newly created strokes, for less jagged strokes

Type:

    

int in [0, 3], default 0

pin_draw_mode¶

    

Pin the mode to the brush

Type:

    

boolean, default False

random_hue_factor¶

    

Random factor to modify original hue

Type:

    

float in [0, 1], default 0.0

random_pressure¶

    

Randomness factor for pressure in new strokes

Type:

    

float in [0, 1], default 0.0

random_saturation_factor¶

    

Random factor to modify original saturation

Type:

    

float in [0, 1], default 0.0

random_strength¶

    

Randomness factor strength in new strokes

Type:

    

float in [0, 1], default 0.0

random_value_factor¶

    

Random factor to modify original value

Type:

    

float in [0, 1], default 0.0

show_fill¶

    

Show transparent lines to use as boundary for filling

Type:

    

boolean, default True

show_fill_boundary¶

    

Show help lines for filling to see boundaries

Type:

    

boolean, default True

show_fill_extend¶

    

Show help lines for stroke extension

Type:

    

boolean, default True

show_lasso¶

    

Do not display fill color while drawing the stroke

Type:

    

boolean, default False

simplify_factor¶

    

Factor of Simplify using adaptive algorithm

Type:

    

float in [0, 100], default 0.0

simplify_pixel_threshold¶

    

Threshold in screen space used for the simplify algorithm. Points within this
threshold are treated as if they were in a straight line.

Type:

    

float in [0, 10], default 0.0

use_active_layer_only¶

    

Only edit the active layer of the object

Type:

    

boolean, default False

use_auto_remove_fill_guides¶

    

Automatically remove fill guide strokes after fill operation

Type:

    

boolean, default True

use_collide_strokes¶

    

Check if extend lines collide with strokes

Type:

    

boolean, default False

use_edit_position¶

    

The brush affects the position of the point

Type:

    

boolean, default False

use_edit_strength¶

    

The brush affects the color strength of the point

Type:

    

boolean, default False

use_edit_thickness¶

    

The brush affects the thickness of the point

Type:

    

boolean, default False

use_edit_uv¶

    

The brush affects the UV rotation of the point

Type:

    

boolean, default False

use_fill_limit¶

    

Fill only visible areas in viewport

Type:

    

boolean, default True

use_jitter_pressure¶

    

Use tablet pressure for jitter

Type:

    

boolean, default False

use_keep_caps_eraser¶

    

Keep the caps as they are and don’t flatten them when erasing

Type:

    

boolean, default False

use_material_pin¶

    

Keep material assigned to brush

Type:

    

boolean, default False

use_occlude_eraser¶

    

Erase only strokes visible and not occluded

Type:

    

boolean, default False

use_pressure¶

    

Use tablet pressure

Type:

    

boolean, default False

use_random_press_hue¶

    

Use pressure to modulate randomness

Type:

    

boolean, default False

use_random_press_radius¶

    

Use pressure to modulate randomness

Type:

    

boolean, default False

use_random_press_sat¶

    

Use pressure to modulate randomness

Type:

    

boolean, default False

use_random_press_strength¶

    

Use pressure to modulate randomness

Type:

    

boolean, default False

use_random_press_uv¶

    

Use pressure to modulate randomness

Type:

    

boolean, default False

use_random_press_val¶

    

Use pressure to modulate randomness

Type:

    

boolean, default False

use_settings_outline¶

    

Convert stroke to outline

Type:

    

boolean, default False

use_settings_postprocess¶

    

Additional post processing options for new strokes

Type:

    

boolean, default False

use_settings_random¶

    

Random brush settings

Type:

    

boolean, default False

use_settings_stabilizer¶

    

Draw lines with a delay to allow smooth strokes (press Shift key to override
while drawing)

Type:

    

boolean, default True

use_strength_pressure¶

    

Use tablet pressure for color strength

Type:

    

boolean, default False

use_stroke_random_hue¶

    

Use randomness at stroke level

Type:

    

boolean, default False

use_stroke_random_radius¶

    

Use randomness at stroke level

Type:

    

boolean, default False

use_stroke_random_sat¶

    

Use randomness at stroke level

Type:

    

boolean, default False

use_stroke_random_strength¶

    

Use randomness at stroke level

Type:

    

boolean, default False

use_stroke_random_uv¶

    

Use randomness at stroke level

Type:

    

boolean, default False

use_stroke_random_val¶

    

Use randomness at stroke level

Type:

    

boolean, default False

use_trim¶

    

Trim intersecting stroke ends

Type:

    

boolean, default False

uv_random¶

    

Random factor for auto-generated UV rotation

Type:

    

float in [0, 1], default 0.0

vertex_color_factor¶

    

Factor used to mix vertex color to get final color

Type:

    

float in [0, 1], default 0.0

vertex_mode¶

    

Defines how vertex color affect to the strokes

  * `STROKE` Stroke – Vertex Color affects to Stroke only.

  * `FILL` Fill – Vertex Color affects to Fill only.

  * `BOTH` Stroke & Fill – Vertex Color affects to Stroke and Fill.

Type:

    

enum in [`STROKE`, `FILL`, `BOTH`], default `STROKE`

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

  * [`Brush.gpencil_settings`](bpy.types.Brush.html#bpy.types.Brush.gpencil_settings "bpy.types.Brush.gpencil_settings")

|

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

