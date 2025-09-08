---
url: https://docs.blender.org/api/current/bpy.types.Brush.html
scraped_at: 2025-09-08T14:21:13.375357
title: Brush(ID)¶
---

# Brush(ID)¶  
  
base classes — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct"), [`ID`](bpy.types.ID.html#bpy.types.ID "bpy.types.ID")

_class _bpy.types.Brush(_ID_)¶

    

Brush data-block for storing brush settings for painting and sculpting

area_radius_factor¶

    

Ratio between the brush radius and the radius that is going to be used to
sample the area center

Type:

    

float in [0, 2], default 0.5

auto_smooth_factor¶

    

Amount of smoothing to automatically apply to each stroke

Type:

    

float in [0, 1], default 0.0

automasking_boundary_edges_propagation_steps¶

    

Distance where boundary edge automasking is going to protect vertices from the
fully masked edge

Type:

    

int in [1, 20], default 1

automasking_cavity_blur_steps¶

    

The number of times the cavity mask is blurred

Type:

    

int in [0, 25], default 0

automasking_cavity_curve¶

    

Curve used for the sensitivity

Type:

    

[`CurveMapping`](bpy.types.CurveMapping.html#bpy.types.CurveMapping
"bpy.types.CurveMapping"), (readonly)

automasking_cavity_factor¶

    

The contrast of the cavity mask

Type:

    

float in [0, 5], default 1.0

automasking_start_normal_falloff¶

    

Extend the angular range with a falloff gradient

Type:

    

float in [0.0001, 1], default 0.25

automasking_start_normal_limit¶

    

The range of angles that will be affected

Type:

    

float in [0.0001, 3.14159], default 0.349066

automasking_view_normal_falloff¶

    

Extend the angular range with a falloff gradient

Type:

    

float in [0.0001, 1], default 0.25

automasking_view_normal_limit¶

    

The range of angles that will be affected

Type:

    

float in [0.0001, 3.14159], default 1.5708

blend¶

    

Brush blending mode

  * `MIX` Mix – Use Mix blending mode while painting.

  * `DARKEN` Darken – Use Darken blending mode while painting.

  * `MUL` Multiply – Use Multiply blending mode while painting.

  * `COLORBURN` Color Burn – Use Color Burn blending mode while painting.

  * `LINEARBURN` Linear Burn – Use Linear Burn blending mode while painting.

  * `LIGHTEN` Lighten – Use Lighten blending mode while painting.

  * `SCREEN` Screen – Use Screen blending mode while painting.

  * `COLORDODGE` Color Dodge – Use Color Dodge blending mode while painting.

  * `ADD` Add – Use Add blending mode while painting.

  * `OVERLAY` Overlay – Use Overlay blending mode while painting.

  * `SOFTLIGHT` Soft Light – Use Soft Light blending mode while painting.

  * `HARDLIGHT` Hard Light – Use Hard Light blending mode while painting.

  * `VIVIDLIGHT` Vivid Light – Use Vivid Light blending mode while painting.

  * `LINEARLIGHT` Linear Light – Use Linear Light blending mode while painting.

  * `PINLIGHT` Pin Light – Use Pin Light blending mode while painting.

  * `DIFFERENCE` Difference – Use Difference blending mode while painting.

  * `EXCLUSION` Exclusion – Use Exclusion blending mode while painting.

  * `SUB` Subtract – Use Subtract blending mode while painting.

  * `HUE` Hue – Use Hue blending mode while painting.

  * `SATURATION` Saturation – Use Saturation blending mode while painting.

  * `COLOR` Color – Use Color blending mode while painting.

  * `LUMINOSITY` Value – Use Value blending mode while painting.

  * `ERASE_ALPHA` Erase Alpha – Erase alpha while painting.

  * `ADD_ALPHA` Add Alpha – Add alpha while painting.

Type:

    

enum in [`MIX`, `DARKEN`, `MUL`, `COLORBURN`, `LINEARBURN`, `LIGHTEN`,
`SCREEN`, `COLORDODGE`, `ADD`, `OVERLAY`, `SOFTLIGHT`, `HARDLIGHT`,
`VIVIDLIGHT`, `LINEARLIGHT`, `PINLIGHT`, `DIFFERENCE`, `EXCLUSION`, `SUB`,
`HUE`, `SATURATION`, `COLOR`, `LUMINOSITY`, `ERASE_ALPHA`, `ADD_ALPHA`],
default `MIX`

blur_kernel_radius¶

    

Radius of kernel used for soften and sharpen in pixels

Type:

    

int in [1, 10000], default 2

blur_mode¶

    

Type:

    

enum in [`BOX`, `GAUSSIAN`], default `GAUSSIAN`

boundary_deform_type¶

    

Deformation type that is used in the brush

Type:

    

enum in [`BEND`, `EXPAND`, `INFLATE`, `GRAB`, `TWIST`, `SMOOTH`], default
`BEND`

boundary_falloff_type¶

    

How the brush falloff is applied across the boundary

  * `CONSTANT` Constant – Applies the same deformation in the entire boundary.

  * `RADIUS` Brush Radius – Applies the deformation in a localized area limited by the brush radius.

  * `LOOP` Loop – Applies the brush falloff in a loop pattern.

  * `LOOP_INVERT` Loop and Invert – Applies the falloff radius in a loop pattern, inverting the displacement direction in each pattern repetition.

Type:

    

enum in [`CONSTANT`, `RADIUS`, `LOOP`, `LOOP_INVERT`], default `CONSTANT`

boundary_offset¶

    

Offset of the boundary origin in relation to the brush radius

Type:

    

float in [0, 30], default 0.0

brush_capabilities¶

    

Brush’s capabilities

Type:

    

[`BrushCapabilities`](bpy.types.BrushCapabilities.html#bpy.types.BrushCapabilities
"bpy.types.BrushCapabilities"), (readonly, never None)

cloth_constraint_softbody_strength¶

    

How much the cloth preserves the original shape, acting as a soft body

Type:

    

float in [0, 1], default 0.0

cloth_damping¶

    

How much the applied forces are propagated through the cloth

Type:

    

float in [0.01, 1], default 0.01

cloth_deform_type¶

    

Deformation type that is used in the brush

Type:

    

enum in [`DRAG`, `PUSH`, `PINCH_POINT`, `PINCH_PERPENDICULAR`, `INFLATE`,
`GRAB`, `EXPAND`, `SNAKE_HOOK`], default `DRAG`

cloth_force_falloff_type¶

    

Shape used in the brush to apply force to the cloth

Type:

    

enum in [`RADIAL`, `PLANE`], default `RADIAL`

cloth_mass¶

    

Mass of each simulation particle

Type:

    

float in [0.01, 2], default 1.0

cloth_sim_falloff¶

    

Area to apply deformation falloff to the effects of the simulation

Type:

    

float in [0, 1], default 0.75

cloth_sim_limit¶

    

Factor added relative to the size of the radius to limit the cloth simulation
effects

Type:

    

float in [0.1, 10], default 2.5

cloth_simulation_area_type¶

    

Part of the mesh that is going to be simulated when the stroke is active

  * `LOCAL` Local – Simulates only a specific area around the brush limited by a fixed radius.

  * `GLOBAL` Global – Simulates the entire mesh.

  * `DYNAMIC` Dynamic – The active simulation area moves with the brush.

Type:

    

enum in [`LOCAL`, `GLOBAL`, `DYNAMIC`], default `LOCAL`

color¶

    

Type:

    

[`mathutils.Color`](mathutils.html#mathutils.Color "mathutils.Color") of 3
items in [0, inf], default (1.0, 1.0, 1.0)

color_type¶

    

Use single color or gradient when painting

  * `COLOR` Color – Paint with a single color.

  * `GRADIENT` Gradient – Paint with a gradient.

Type:

    

enum in [`COLOR`, `GRADIENT`], default `COLOR`

crease_pinch_factor¶

    

How much the crease brush pinches

Type:

    

float in [0, 1], default 0.5

cursor_color_add¶

    

Color of cursor when adding

Type:

    

float array of 4 items in [0, inf], default (1.0, 0.39, 0.39, 0.9)

cursor_color_subtract¶

    

Color of cursor when subtracting

Type:

    

float array of 4 items in [0, inf], default (0.39, 0.39, 1.0, 0.9)

cursor_overlay_alpha¶

    

Type:

    

int in [0, 100], default 33

curve¶

    

Editable falloff curve

Type:

    

[`CurveMapping`](bpy.types.CurveMapping.html#bpy.types.CurveMapping
"bpy.types.CurveMapping"), (readonly, never None)

curve_preset¶

    

Type:

    

enum in [Brush Curve Preset
Items](bpy_types_enum_items/brush_curve_preset_items.html#rna-enum-brush-
curve-preset-items), default `CUSTOM`

curve_random_hue¶

    

Curve used for modulating effect

Type:

    

[`CurveMapping`](bpy.types.CurveMapping.html#bpy.types.CurveMapping
"bpy.types.CurveMapping"), (readonly)

curve_random_saturation¶

    

Curve used for modulating effect

Type:

    

[`CurveMapping`](bpy.types.CurveMapping.html#bpy.types.CurveMapping
"bpy.types.CurveMapping"), (readonly)

curve_random_value¶

    

Curve used for modulating effect

Type:

    

[`CurveMapping`](bpy.types.CurveMapping.html#bpy.types.CurveMapping
"bpy.types.CurveMapping"), (readonly)

curves_sculpt_settings¶

    

Type:

    

[`BrushCurvesSculptSettings`](bpy.types.BrushCurvesSculptSettings.html#bpy.types.BrushCurvesSculptSettings
"bpy.types.BrushCurvesSculptSettings"), (readonly)

curves_sculpt_tool¶

    

Type:

    

enum in [Brush Curves Sculpt Brush Type
Items](bpy_types_enum_items/brush_curves_sculpt_brush_type_items.html#rna-
enum-brush-curves-sculpt-brush-type-items), default `COMB`

dash_ratio¶

    

Ratio of samples in a cycle that the brush is enabled

Type:

    

float in [0, 1], default 1.0

dash_samples¶

    

Length of a dash cycle measured in stroke samples

Type:

    

int in [1, 10000], default 20

deform_target¶

    

How the deformation of the brush will affect the object

  * `GEOMETRY` Geometry – Brush deformation displaces the vertices of the mesh.

  * `CLOTH_SIM` Cloth Simulation – Brush deforms the mesh by deforming the constraints of a cloth simulation.

Type:

    

enum in [`GEOMETRY`, `CLOTH_SIM`], default `GEOMETRY`

density¶

    

Amount of random elements that are going to be affected by the brush

Type:

    

float in [0, 1], default 0.0

direction¶

    

  * `ADD` Add – Add effect of brush.

  * `SUBTRACT` Subtract – Subtract effect of brush.

Type:

    

enum in [`ADD`, `SUBTRACT`], default `ADD`

disconnected_distance_max¶

    

Maximum distance to search for disconnected loose parts in the mesh

Type:

    

float in [0, 10], default 0.1

elastic_deform_type¶

    

Deformation type that is used in the brush

Type:

    

enum in [`GRAB`, `GRAB_BISCALE`, `GRAB_TRISCALE`, `SCALE`, `TWIST`], default
`GRAB`

elastic_deform_volume_preservation¶

    

Poisson ratio for elastic deformation. Higher values preserve volume more, but
also lead to more bulging.

Type:

    

float in [0, 0.9], default 0.0

falloff_angle¶

    

Paint most on faces pointing towards the view according to this angle

Type:

    

float in [0, 1.5708], default 0.0

falloff_shape¶

    

Use projected or spherical falloff

  * `SPHERE` Sphere – Apply brush influence in a Sphere, outwards from the center.

  * `PROJECTED` Projected – Apply brush influence in a 2D circle, projected from the view.

Type:

    

enum in [`SPHERE`, `PROJECTED`], default `SPHERE`

fill_threshold¶

    

Threshold above which filling is not propagated

Type:

    

float in [0, 100], default 0.2

flow¶

    

Amount of paint that is applied per stroke sample

Type:

    

float in [0, 1], default 0.0

gpencil_sculpt_tool¶

    

Type:

    

enum in [Brush Gpencil Sculpt Types
Items](bpy_types_enum_items/brush_gpencil_sculpt_types_items.html#rna-enum-
brush-gpencil-sculpt-types-items), default `SMOOTH`

gpencil_settings¶

    

Type:

    

[`BrushGpencilSettings`](bpy.types.BrushGpencilSettings.html#bpy.types.BrushGpencilSettings
"bpy.types.BrushGpencilSettings"), (readonly)

gpencil_tool¶

    

Type:

    

enum in [Brush Gpencil Types
Items](bpy_types_enum_items/brush_gpencil_types_items.html#rna-enum-brush-
gpencil-types-items), default `DRAW`

gpencil_vertex_tool¶

    

Type:

    

enum in [Brush Gpencil Vertex Types
Items](bpy_types_enum_items/brush_gpencil_vertex_types_items.html#rna-enum-
brush-gpencil-vertex-types-items), default `DRAW`

gpencil_weight_tool¶

    

Type:

    

enum in [Brush Gpencil Weight Types
Items](bpy_types_enum_items/brush_gpencil_weight_types_items.html#rna-enum-
brush-gpencil-weight-types-items), default `WEIGHT`

grad_spacing¶

    

Spacing before brush gradient goes full circle

Type:

    

int in [1, 10000], default 0

gradient¶

    

Type:

    

[`ColorRamp`](bpy.types.ColorRamp.html#bpy.types.ColorRamp
"bpy.types.ColorRamp"), (readonly)

gradient_fill_mode¶

    

Type:

    

enum in [`LINEAR`, `RADIAL`], default `LINEAR`

gradient_stroke_mode¶

    

Type:

    

enum in [`PRESSURE`, `SPACING_REPEAT`, `SPACING_CLAMP`], default `PRESSURE`

hardness¶

    

How close the brush falloff starts from the edge of the brush

Type:

    

float in [0, 1], default 0.0

has_unsaved_changes¶

    

Indicates that there are any user visible changes since the brush has been
imported or read from the file

Type:

    

boolean, default False, (readonly)

height¶

    

Affectable height of brush (i.e. the layer height for the layer tool)

Type:

    

float in [0, 1], default 0.5

hue_jitter¶

    

Color jitter effect on hue

Type:

    

float in [0, 1], default 0.0

icon_filepath¶

    

File path to brush icon

Type:

    

string, default “”, (never None, blend relative `//` prefix supported)

image_paint_capabilities¶

    

Type:

    

[`BrushCapabilitiesImagePaint`](bpy.types.BrushCapabilitiesImagePaint.html#bpy.types.BrushCapabilitiesImagePaint
"bpy.types.BrushCapabilitiesImagePaint"), (readonly, never None)

image_tool¶

    

Type:

    

enum in [Brush Image Brush Type
Items](bpy_types_enum_items/brush_image_brush_type_items.html#rna-enum-brush-
image-brush-type-items), default `DRAW`

input_samples¶

    

Number of input samples to average together to smooth the brush stroke

Type:

    

int in [1, 64], default 1

invert_density_pressure¶

    

Invert the modulation of pressure in density

Type:

    

boolean, default False

invert_flow_pressure¶

    

Invert the modulation of pressure in flow

Type:

    

boolean, default False

invert_hardness_pressure¶

    

Invert the modulation of pressure in hardness

Type:

    

boolean, default False

invert_to_scrape_fill¶

    

Use Scrape or Fill brush when inverting this brush instead of inverting its
displacement direction

Type:

    

boolean, default False

invert_wet_mix_pressure¶

    

Invert the modulation of pressure in wet mix

Type:

    

boolean, default False

invert_wet_persistence_pressure¶

    

Invert the modulation of pressure in wet persistence

Type:

    

boolean, default False

jitter¶

    

Jitter the position of the brush while painting

Type:

    

float in [0, 1000], default 0.0

jitter_absolute¶

    

Jitter the position of the brush in pixels while painting

Type:

    

int in [0, 1000000], default 0

jitter_unit¶

    

Jitter in screen space or relative to brush size

  * `VIEW` View – Jittering happens in screen space, in pixels.

  * `BRUSH` Brush – Jittering happens relative to the brush size.

Type:

    

enum in [`VIEW`, `BRUSH`], default `BRUSH`

mask_overlay_alpha¶

    

Type:

    

int in [0, 100], default 33

mask_stencil_dimension¶

    

Dimensions of mask stencil in viewport

Type:

    

[`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 2
items in [-inf, inf], default (256.0, 256.0)

mask_stencil_pos¶

    

Position of mask stencil in viewport

Type:

    

[`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 2
items in [-inf, inf], default (256.0, 256.0)

mask_texture¶

    

Type:

    

[`Texture`](bpy.types.Texture.html#bpy.types.Texture "bpy.types.Texture")

mask_texture_slot¶

    

Type:

    

[`BrushTextureSlot`](bpy.types.BrushTextureSlot.html#bpy.types.BrushTextureSlot
"bpy.types.BrushTextureSlot"), (readonly)

mask_tool¶

    

Type:

    

enum in [`DRAW`, `SMOOTH`], default `DRAW`

multiplane_scrape_angle¶

    

Angle between the planes of the crease

Type:

    

float in [0, 160], default 0.0

normal_radius_factor¶

    

Ratio between the brush radius and the radius that is going to be used to
sample the normal

Type:

    

float in [0, 2], default 0.5

normal_weight¶

    

How much grab will pull vertices out of surface during a grab

Type:

    

float in [0, 1], default 0.0

paint_curve¶

    

Active paint curve

Type:

    

[`PaintCurve`](bpy.types.PaintCurve.html#bpy.types.PaintCurve
"bpy.types.PaintCurve")

plane_depth¶

    

The maximum distance below the plane for affected vertices. Increasing the
depth affects vertices farther below the plane.

Type:

    

float in [0, 1], default 0.0

plane_height¶

    

The maximum distance above the plane for affected vertices. Increasing the
height affects vertices farther above the plane.

Type:

    

float in [0, 1], default 1.0

plane_inversion_mode¶

    

Inversion Mode

  * `INVERT_DISPLACEMENT` Invert Displacement – Displace the vertices away from the plane..

  * `SWAP_DEPTH_AND_HEIGHT` Swap Height and Depth – Swap the roles of Height and Depth..

Type:

    

enum in [`INVERT_DISPLACEMENT`, `SWAP_DEPTH_AND_HEIGHT`], default
`INVERT_DISPLACEMENT`

plane_offset¶

    

Adjust plane on which the brush acts towards or away from the object surface

Type:

    

float in [-2, 2], default 0.0

plane_trim¶

    

If a vertex is further away from offset plane than this, then it is not
affected

Type:

    

float in [0, 1], default 0.5

pose_deform_type¶

    

Deformation type that is used in the brush

Type:

    

enum in [`ROTATE_TWIST`, `SCALE_TRANSLATE`, `SQUASH_STRETCH`], default
`ROTATE_TWIST`

pose_ik_segments¶

    

Number of segments of the inverse kinematics chain that will deform the mesh

Type:

    

int in [1, 20], default 1

pose_offset¶

    

Offset of the pose origin in relation to the brush radius

Type:

    

float in [0, 2], default 0.0

pose_origin_type¶

    

Method to set the rotation origins for the segments of the brush

  * `TOPOLOGY` Topology – Sets the rotation origin automatically using the topology and shape of the mesh as a guide.

  * `FACE_SETS` Face Sets – Creates a pose segment per face sets, starting from the active face set.

  * `FACE_SETS_FK` Face Sets FK – Simulates an FK deformation using the Face Set under the cursor as control.

Type:

    

enum in [`TOPOLOGY`, `FACE_SETS`, `FACE_SETS_FK`], default `TOPOLOGY`

pose_smooth_iterations¶

    

Smooth iterations applied after calculating the pose factor of each vertex

Type:

    

int in [0, 100], default 4

rake_factor¶

    

How much grab will follow cursor rotation

Type:

    

float in [0, 10], default 0.0

rate¶

    

Interval between paints for Airbrush

Type:

    

float in [0.0001, 10000], default 0.1

saturation_jitter¶

    

Color jitter effect on saturation

Type:

    

float in [0, 1], default 0.0

sculpt_capabilities¶

    

Type:

    

[`BrushCapabilitiesSculpt`](bpy.types.BrushCapabilitiesSculpt.html#bpy.types.BrushCapabilitiesSculpt
"bpy.types.BrushCapabilitiesSculpt"), (readonly, never None)

sculpt_plane¶

    

Type:

    

enum in [`AREA`, `VIEW`, `X`, `Y`, `Z`], default `AREA`

sculpt_tool¶

    

Type:

    

enum in [Brush Sculpt Brush Type
Items](bpy_types_enum_items/brush_sculpt_brush_type_items.html#rna-enum-brush-
sculpt-brush-type-items), default `DRAW`

secondary_color¶

    

Type:

    

[`mathutils.Color`](mathutils.html#mathutils.Color "mathutils.Color") of 3
items in [0, inf], default (0.0, 0.0, 0.0)

sharp_threshold¶

    

Threshold below which, no sharpening is done

Type:

    

float in [0, 100], default 0.0

show_multiplane_scrape_planes_preview¶

    

Preview the scrape planes in the cursor during the stroke

Type:

    

boolean, default False

size¶

    

Radius of the brush in pixels

Type:

    

int in [1, 5000], default 35

slide_deform_type¶

    

Deformation type that is used in the brush

Type:

    

enum in [`DRAG`, `PINCH`, `EXPAND`], default `DRAG`

smear_deform_type¶

    

Deformation type that is used in the brush

Type:

    

enum in [`DRAG`, `PINCH`, `EXPAND`], default `DRAG`

smooth_deform_type¶

    

Deformation type that is used in the brush

  * `LAPLACIAN` Laplacian – Smooths the surface and the volume.

  * `SURFACE` Surface – Smooths the surface of the mesh, preserving the volume.

Type:

    

enum in [`LAPLACIAN`, `SURFACE`], default `LAPLACIAN`

smooth_stroke_factor¶

    

Higher values give a smoother stroke

Type:

    

float in [0.5, 0.99], default 0.9

smooth_stroke_radius¶

    

Minimum distance from last point before stroke continues

Type:

    

int in [10, 200], default 75

snake_hook_deform_type¶

    

Deformation type that is used in the brush

  * `FALLOFF` Radius Falloff – Applies the brush falloff in the tip of the brush.

  * `ELASTIC` Elastic – Modifies the entire mesh using elastic deform.

Type:

    

enum in [`FALLOFF`, `ELASTIC`], default `FALLOFF`

spacing¶

    

Spacing between brush daubs as a percentage of brush diameter

Type:

    

int in [1, 1000], default 10

stabilize_normal¶

    

Stabilize the orientation of the brush plane.

Type:

    

float in [0, 1], default 0.0

stabilize_plane¶

    

Stabilize the center of the brush plane.

Type:

    

float in [0, 1], default 0.0

stencil_dimension¶

    

Dimensions of stencil in viewport

Type:

    

[`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 2
items in [-inf, inf], default (256.0, 256.0)

stencil_pos¶

    

Position of stencil in viewport

Type:

    

[`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 2
items in [-inf, inf], default (256.0, 256.0)

strength¶

    

How powerful the effect of the brush is when applied

Type:

    

float in [0, 10], default 1.0

stroke_method¶

    

  * `DOTS` Dots – Apply paint on each mouse move step.

  * `DRAG_DOT` Drag Dot – Allows a single dot to be carefully positioned.

  * `SPACE` Space – Limit brush application to the distance specified by spacing.

  * `AIRBRUSH` Airbrush – Keep applying paint effect while holding mouse (spray).

  * `ANCHORED` Anchored – Keep the brush anchored to the initial location.

  * `LINE` Line – Draw a line with dabs separated according to spacing.

  * `CURVE` Curve – Define the stroke curve with a Bézier curve (dabs are separated according to spacing).

Type:

    

enum in [`DOTS`, `DRAG_DOT`, `SPACE`, `AIRBRUSH`, `ANCHORED`, `LINE`,
`CURVE`], default `DOTS`

surface_smooth_current_vertex¶

    

How much the position of each individual vertex influences the final result

Type:

    

float in [0, 1], default 0.0

surface_smooth_iterations¶

    

Number of smoothing iterations per brush step

Type:

    

int in [1, 10], default 0

surface_smooth_shape_preservation¶

    

How much of the original shape is preserved when smoothing

Type:

    

float in [0, 1], default 0.0

texture¶

    

Type:

    

[`Texture`](bpy.types.Texture.html#bpy.types.Texture "bpy.types.Texture")

texture_overlay_alpha¶

    

Type:

    

int in [0, 100], default 33

texture_sample_bias¶

    

Value added to texture samples

Type:

    

float in [-1, 1], default 0.0

texture_slot¶

    

Type:

    

[`BrushTextureSlot`](bpy.types.BrushTextureSlot.html#bpy.types.BrushTextureSlot
"bpy.types.BrushTextureSlot"), (readonly)

tilt_strength_factor¶

    

How much the tilt of the pen will affect the brush. Negative values indicate
inverting the tilt directions.

Type:

    

float in [-1, 1], default 0.0

tip_roundness¶

    

Roundness of the brush tip

Type:

    

float in [0, 1], default 1.0

tip_scale_x¶

    

Scale of the brush tip in the X axis

Type:

    

float in [0.0001, 1], default 1.0

topology_rake_factor¶

    

Automatically align edges to the brush direction to generate cleaner topology
and define sharp features. Best used on low-poly meshes as it has a
performance impact.

Type:

    

float in [0, 1], default 0.0

unprojected_radius¶

    

Radius of brush in Blender units

Type:

    

float in [0.001, inf], default 0.05

use_accumulate¶

    

Accumulate stroke daubs on top of each other

Type:

    

boolean, default False

use_adaptive_space¶

    

Space daubs according to surface orientation instead of screen space

Type:

    

boolean, default False

use_airbrush¶

    

Keep applying paint effect while holding mouse (spray)

Type:

    

boolean, default False

use_alpha¶

    

When this is disabled, lock alpha while painting

Type:

    

boolean, default True

use_anchor¶

    

Keep the brush anchored to the initial location

Type:

    

boolean, default False

use_automasking_boundary_edges¶

    

Do not affect non manifold boundary edges

Type:

    

boolean, default False

use_automasking_boundary_face_sets¶

    

Do not affect vertices that belong to a Face Set boundary

Type:

    

boolean, default False

use_automasking_cavity¶

    

Do not affect vertices on peaks, based on the surface curvature

Type:

    

boolean, default False

use_automasking_cavity_inverted¶

    

Do not affect vertices within crevices, based on the surface curvature

Type:

    

boolean, default False

use_automasking_custom_cavity_curve¶

    

Use custom curve

Type:

    

boolean, default False

use_automasking_face_sets¶

    

Affect only vertices that share Face Sets with the active vertex

Type:

    

boolean, default False

use_automasking_start_normal¶

    

Affect only vertices with a similar normal to where the stroke starts

Type:

    

boolean, default False

use_automasking_topology¶

    

Affect only vertices connected to the active vertex under the brush

Type:

    

boolean, default False

use_automasking_view_normal¶

    

Affect only vertices with a normal that faces the viewer

Type:

    

boolean, default False

use_automasking_view_occlusion¶

    

Only affect vertices that are not occluded by other faces (slower performance)

Type:

    

boolean, default False

use_cloth_collision¶

    

Collide with objects during the simulation

Type:

    

boolean, default False

use_cloth_pin_simulation_boundary¶

    

Lock the position of the vertices in the simulation falloff area to avoid
artifacts and create a softer transition with unaffected areas

Type:

    

boolean, default False

use_color_as_displacement¶

    

Handle each pixel color as individual vector for displacement (area plane
mapping only)

Type:

    

boolean, default False

use_color_jitter¶

    

Jitter brush color

Type:

    

boolean, default False

use_connected_only¶

    

Affect only topologically connected elements

Type:

    

boolean, default False

use_cursor_overlay¶

    

Show cursor in viewport

Type:

    

boolean, default False

use_cursor_overlay_override¶

    

Don’t show overlay during a stroke

Type:

    

boolean, default False

use_curve¶

    

Define the stroke curve with a Bézier curve. Dabs are separated according to
spacing.

Type:

    

boolean, default False

use_custom_icon¶

    

Set the brush icon from an image file

Type:

    

boolean, default False

use_density_pressure¶

    

Use pressure to modulate density

Type:

    

boolean, default False

use_edge_to_edge¶

    

Drag anchor brush from edge-to-edge

Type:

    

boolean, default False

use_flow_pressure¶

    

Use pressure to modulate flow

Type:

    

boolean, default False

use_frontface¶

    

Brush only affects vertices that face the viewer

Type:

    

boolean, default False

use_frontface_falloff¶

    

Blend brush influence by how much they face the front

Type:

    

boolean, default False

use_grab_active_vertex¶

    

Apply the maximum grab strength to the active vertex instead of the cursor
location

Type:

    

boolean, default False

use_grab_silhouette¶

    

Grabs trying to automask the silhouette of the object

Type:

    

boolean, default False

use_hardness_pressure¶

    

Use pressure to modulate hardness

Type:

    

boolean, default False

use_inverse_smooth_pressure¶

    

Lighter pressure causes more smoothing to be applied

Type:

    

boolean, default False

use_line¶

    

Draw a line with dabs separated according to spacing

Type:

    

boolean, default False

use_locked_size¶

    

Measure brush size relative to the view or the scene

  * `VIEW` View – Measure brush size relative to the view.

  * `SCENE` Scene – Measure brush size relative to the scene.

Type:

    

enum in [`VIEW`, `SCENE`], default `VIEW`

use_multiplane_scrape_dynamic¶

    

The angle between the planes changes during the stroke to fit the surface
under the cursor

Type:

    

boolean, default False

use_offset_pressure¶

    

Enable tablet pressure sensitivity for offset

Type:

    

boolean, default False

use_original_normal¶

    

When locked keep using normal of surface where stroke was initiated

Type:

    

boolean, default False

use_original_plane¶

    

When locked keep using the plane origin of surface where stroke was initiated

Type:

    

boolean, default False

use_paint_antialiasing¶

    

Smooths the edges of the strokes

Type:

    

boolean, default True

use_paint_grease_pencil¶

    

Use this brush in Grease Pencil drawing mode

Type:

    

boolean, default False

use_paint_image¶

    

Use this brush in texture paint mode

Type:

    

boolean, default True

use_paint_sculpt¶

    

Use this brush in sculpt mode

Type:

    

boolean, default True

use_paint_sculpt_curves¶

    

Use this brush in sculpt curves mode

Type:

    

boolean, default False

use_paint_uv_sculpt¶

    

Use this brush in UV sculpt mode

Type:

    

boolean, default False

use_paint_vertex¶

    

Use this brush in vertex paint mode

Type:

    

boolean, default True

use_paint_weight¶

    

Use this brush in weight paint mode

Type:

    

boolean, default True

use_persistent¶

    

Sculpt on a persistent layer of the mesh

Type:

    

boolean, default False

use_plane_trim¶

    

Limit the distance from the offset plane that a vertex can be affected

Type:

    

boolean, default False

use_pose_ik_anchored¶

    

Keep the position of the last segment in the IK chain fixed

Type:

    

boolean, default False

use_pose_lock_rotation¶

    

Do not rotate the segment when using the scale deform mode

Type:

    

boolean, default False

use_pressure_area_radius¶

    

Enable tablet pressure sensitivity for area radius

Type:

    

boolean, default False

use_pressure_jitter¶

    

Enable tablet pressure sensitivity for jitter

Type:

    

boolean, default False

use_pressure_masking¶

    

Pen pressure makes texture influence smaller

Type:

    

enum in [`NONE`, `RAMP`, `CUTOFF`], default `NONE`

use_pressure_size¶

    

Enable tablet pressure sensitivity for size

Type:

    

boolean, default False

use_pressure_spacing¶

    

Enable tablet pressure sensitivity for spacing

Type:

    

boolean, default False

use_pressure_strength¶

    

Enable tablet pressure sensitivity for strength

Type:

    

boolean, default True

use_primary_overlay¶

    

Show texture in viewport

Type:

    

boolean, default False

use_primary_overlay_override¶

    

Don’t show overlay during a stroke

Type:

    

boolean, default False

use_random_press_hue¶

    

Use pressure to modulate randomness

Type:

    

boolean, default False

use_random_press_sat¶

    

Use pressure to modulate randomness

Type:

    

boolean, default False

use_random_press_val¶

    

Use pressure to modulate randomness

Type:

    

boolean, default False

use_restore_mesh¶

    

Allow a single dot to be carefully positioned

Type:

    

boolean, default False

use_scene_spacing¶

    

Calculate the brush spacing using view or scene distance

  * `VIEW` View – Calculate brush spacing relative to the view.

  * `SCENE` Scene – Calculate brush spacing relative to the scene using the stroke location.

Type:

    

enum in [`VIEW`, `SCENE`], default `VIEW`

use_secondary_overlay¶

    

Show texture in viewport

Type:

    

boolean, default False

use_secondary_overlay_override¶

    

Don’t show overlay during a stroke

Type:

    

boolean, default False

use_smooth_stroke¶

    

Brush lags behind mouse and follows a smoother path

Type:

    

boolean, default False

use_space¶

    

Limit brush application to the distance specified by spacing

Type:

    

boolean, default True

use_space_attenuation¶

    

Automatically adjust strength to give consistent results for different
spacings

Type:

    

boolean, default True

use_stroke_random_hue¶

    

Use randomness at stroke level

Type:

    

boolean, default False

use_stroke_random_sat¶

    

Use randomness at stroke level

Type:

    

boolean, default False

use_stroke_random_val¶

    

Use randomness at stroke level

Type:

    

boolean, default False

use_vertex_grease_pencil¶

    

Use this brush in Grease Pencil vertex color mode

Type:

    

boolean, default False

use_wet_mix_pressure¶

    

Use pressure to modulate wet mix

Type:

    

boolean, default False

use_wet_persistence_pressure¶

    

Use pressure to modulate wet persistence

Type:

    

boolean, default False

value_jitter¶

    

Color jitter effect on value

Type:

    

float in [0, 1], default 0.0

vertex_paint_capabilities¶

    

Type:

    

[`BrushCapabilitiesVertexPaint`](bpy.types.BrushCapabilitiesVertexPaint.html#bpy.types.BrushCapabilitiesVertexPaint
"bpy.types.BrushCapabilitiesVertexPaint"), (readonly, never None)

vertex_tool¶

    

Type:

    

enum in [Brush Vertex Brush Type
Items](bpy_types_enum_items/brush_vertex_brush_type_items.html#rna-enum-brush-
vertex-brush-type-items), default `DRAW`

weight¶

    

Vertex weight when brush is applied

Type:

    

float in [0, 1], default 1.0

weight_paint_capabilities¶

    

Type:

    

[`BrushCapabilitiesWeightPaint`](bpy.types.BrushCapabilitiesWeightPaint.html#bpy.types.BrushCapabilitiesWeightPaint
"bpy.types.BrushCapabilitiesWeightPaint"), (readonly, never None)

weight_tool¶

    

Type:

    

enum in [Brush Weight Brush Type
Items](bpy_types_enum_items/brush_weight_brush_type_items.html#rna-enum-brush-
weight-brush-type-items), default `DRAW`

wet_mix¶

    

Amount of paint that is picked from the surface into the brush color

Type:

    

float in [0, 1], default 0.0

wet_paint_radius_factor¶

    

Ratio between the brush radius and the radius that is going to be used to
sample the color to blend in wet paint

Type:

    

float in [0, 2], default 0.5

wet_persistence¶

    

Amount of wet paint that stays in the brush after applying paint to the
surface

Type:

    

float in [0, 1], default 0.0

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
  * [`ID.name`](bpy.types.ID.html#bpy.types.ID.name "bpy.types.ID.name")
  * [`ID.name_full`](bpy.types.ID.html#bpy.types.ID.name_full "bpy.types.ID.name_full")
  * [`ID.id_type`](bpy.types.ID.html#bpy.types.ID.id_type "bpy.types.ID.id_type")
  * [`ID.session_uid`](bpy.types.ID.html#bpy.types.ID.session_uid "bpy.types.ID.session_uid")
  * [`ID.is_evaluated`](bpy.types.ID.html#bpy.types.ID.is_evaluated "bpy.types.ID.is_evaluated")
  * [`ID.original`](bpy.types.ID.html#bpy.types.ID.original "bpy.types.ID.original")
  * [`ID.users`](bpy.types.ID.html#bpy.types.ID.users "bpy.types.ID.users")
  * [`ID.use_fake_user`](bpy.types.ID.html#bpy.types.ID.use_fake_user "bpy.types.ID.use_fake_user")
  * [`ID.use_extra_user`](bpy.types.ID.html#bpy.types.ID.use_extra_user "bpy.types.ID.use_extra_user")
  * [`ID.is_embedded_data`](bpy.types.ID.html#bpy.types.ID.is_embedded_data "bpy.types.ID.is_embedded_data")

|

  * [`ID.is_missing`](bpy.types.ID.html#bpy.types.ID.is_missing "bpy.types.ID.is_missing")
  * [`ID.is_runtime_data`](bpy.types.ID.html#bpy.types.ID.is_runtime_data "bpy.types.ID.is_runtime_data")
  * [`ID.is_editable`](bpy.types.ID.html#bpy.types.ID.is_editable "bpy.types.ID.is_editable")
  * [`ID.tag`](bpy.types.ID.html#bpy.types.ID.tag "bpy.types.ID.tag")
  * [`ID.is_library_indirect`](bpy.types.ID.html#bpy.types.ID.is_library_indirect "bpy.types.ID.is_library_indirect")
  * [`ID.library`](bpy.types.ID.html#bpy.types.ID.library "bpy.types.ID.library")
  * [`ID.library_weak_reference`](bpy.types.ID.html#bpy.types.ID.library_weak_reference "bpy.types.ID.library_weak_reference")
  * [`ID.asset_data`](bpy.types.ID.html#bpy.types.ID.asset_data "bpy.types.ID.asset_data")
  * [`ID.override_library`](bpy.types.ID.html#bpy.types.ID.override_library "bpy.types.ID.override_library")
  * [`ID.preview`](bpy.types.ID.html#bpy.types.ID.preview "bpy.types.ID.preview")

  
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
  * [`bpy_struct.keyframe_delete`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.keyframe_delete "bpy.types.bpy_struct.keyframe_delete")
  * [`bpy_struct.keyframe_insert`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.keyframe_insert "bpy.types.bpy_struct.keyframe_insert")
  * [`bpy_struct.keys`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.keys "bpy.types.bpy_struct.keys")
  * [`bpy_struct.path_from_id`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.path_from_id "bpy.types.bpy_struct.path_from_id")
  * [`bpy_struct.path_resolve`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.path_resolve "bpy.types.bpy_struct.path_resolve")
  * [`bpy_struct.pop`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.pop "bpy.types.bpy_struct.pop")
  * [`bpy_struct.property_overridable_library_set`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.property_overridable_library_set "bpy.types.bpy_struct.property_overridable_library_set")
  * [`bpy_struct.property_unset`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.property_unset "bpy.types.bpy_struct.property_unset")
  * [`bpy_struct.rna_ancestors`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.rna_ancestors "bpy.types.bpy_struct.rna_ancestors")

|

  * [`bpy_struct.type_recast`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.type_recast "bpy.types.bpy_struct.type_recast")
  * [`bpy_struct.values`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.values "bpy.types.bpy_struct.values")
  * [`ID.rename`](bpy.types.ID.html#bpy.types.ID.rename "bpy.types.ID.rename")
  * [`ID.evaluated_get`](bpy.types.ID.html#bpy.types.ID.evaluated_get "bpy.types.ID.evaluated_get")
  * [`ID.copy`](bpy.types.ID.html#bpy.types.ID.copy "bpy.types.ID.copy")
  * [`ID.asset_mark`](bpy.types.ID.html#bpy.types.ID.asset_mark "bpy.types.ID.asset_mark")
  * [`ID.asset_clear`](bpy.types.ID.html#bpy.types.ID.asset_clear "bpy.types.ID.asset_clear")
  * [`ID.asset_generate_preview`](bpy.types.ID.html#bpy.types.ID.asset_generate_preview "bpy.types.ID.asset_generate_preview")
  * [`ID.override_create`](bpy.types.ID.html#bpy.types.ID.override_create "bpy.types.ID.override_create")
  * [`ID.override_hierarchy_create`](bpy.types.ID.html#bpy.types.ID.override_hierarchy_create "bpy.types.ID.override_hierarchy_create")
  * [`ID.user_clear`](bpy.types.ID.html#bpy.types.ID.user_clear "bpy.types.ID.user_clear")
  * [`ID.user_remap`](bpy.types.ID.html#bpy.types.ID.user_remap "bpy.types.ID.user_remap")
  * [`ID.make_local`](bpy.types.ID.html#bpy.types.ID.make_local "bpy.types.ID.make_local")
  * [`ID.user_of_id`](bpy.types.ID.html#bpy.types.ID.user_of_id "bpy.types.ID.user_of_id")
  * [`ID.animation_data_create`](bpy.types.ID.html#bpy.types.ID.animation_data_create "bpy.types.ID.animation_data_create")
  * [`ID.animation_data_clear`](bpy.types.ID.html#bpy.types.ID.animation_data_clear "bpy.types.ID.animation_data_clear")
  * [`ID.update_tag`](bpy.types.ID.html#bpy.types.ID.update_tag "bpy.types.ID.update_tag")
  * [`ID.preview_ensure`](bpy.types.ID.html#bpy.types.ID.preview_ensure "bpy.types.ID.preview_ensure")
  * [`ID.bl_rna_get_subclass`](bpy.types.ID.html#bpy.types.ID.bl_rna_get_subclass "bpy.types.ID.bl_rna_get_subclass")
  * [`ID.bl_rna_get_subclass_py`](bpy.types.ID.html#bpy.types.ID.bl_rna_get_subclass_py "bpy.types.ID.bl_rna_get_subclass_py")

  
---|---  
  
## References¶

  * [`bpy.context.brush`](bpy.context.html#bpy.context.brush "bpy.context.brush")
  * [`BlendData.brushes`](bpy.types.BlendData.html#bpy.types.BlendData.brushes "bpy.types.BlendData.brushes")
  * [`BlendDataBrushes.create_gpencil_data`](bpy.types.BlendDataBrushes.html#bpy.types.BlendDataBrushes.create_gpencil_data "bpy.types.BlendDataBrushes.create_gpencil_data")
  * [`BlendDataBrushes.new`](bpy.types.BlendDataBrushes.html#bpy.types.BlendDataBrushes.new "bpy.types.BlendDataBrushes.new")

|

  * [`BlendDataBrushes.remove`](bpy.types.BlendDataBrushes.html#bpy.types.BlendDataBrushes.remove "bpy.types.BlendDataBrushes.remove")
  * [`Paint.brush`](bpy.types.Paint.html#bpy.types.Paint.brush "bpy.types.Paint.brush")
  * [`Paint.eraser_brush`](bpy.types.Paint.html#bpy.types.Paint.eraser_brush "bpy.types.Paint.eraser_brush")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

