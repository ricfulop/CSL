---
url: https://docs.blender.org/api/current/bpy.types.CurveMapping.html
scraped_at: 2025-09-08T14:24:15.912196
title: CurveMapping(bpy_struct)¶
---

# CurveMapping(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.CurveMapping(_bpy_struct_)¶

    

Curve mapping to map color, vector and scalar values to other values using a
user defined curve

black_level¶

    

For RGB curves, the color that black is mapped to

Type:

    

[`mathutils.Color`](mathutils.html#mathutils.Color "mathutils.Color") of 3
items in [-inf, inf], default (0.0, 0.0, 0.0)

clip_max_x¶

    

Type:

    

float in [-100, 100], default 0.0

clip_max_y¶

    

Type:

    

float in [-100, 100], default 0.0

clip_min_x¶

    

Type:

    

float in [-100, 100], default 0.0

clip_min_y¶

    

Type:

    

float in [-100, 100], default 0.0

curves¶

    

Type:

    

[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`CurveMap`](bpy.types.CurveMap.html#bpy.types.CurveMap "bpy.types.CurveMap"),
(readonly)

extend¶

    

Extrapolate the curve or extend it horizontally

Type:

    

enum in [`HORIZONTAL`, `EXTRAPOLATED`], default `HORIZONTAL`

tone¶

    

Tone of the curve

  * `STANDARD` Standard – Combined curve is applied to each channel individually, which may result in a change of hue.

  * `FILMLIKE` Filmlike – Keeps the hue constant.

Type:

    

enum in [`STANDARD`, `FILMLIKE`], default `STANDARD`

use_clip¶

    

Force the curve view to fit a defined boundary

Type:

    

boolean, default False

white_level¶

    

For RGB curves, the color that white is mapped to

Type:

    

[`mathutils.Color`](mathutils.html#mathutils.Color "mathutils.Color") of 3
items in [-inf, inf], default (0.0, 0.0, 0.0)

update()¶

    

Update curve mapping after making changes

reset_view()¶

    

Reset the curve mapping grid to its clipping size

initialize()¶

    

Initialize curve

evaluate(_curve_ , _position_)¶

    

Evaluate curve at given location

Parameters:

    

  * **curve** ([`CurveMap`](bpy.types.CurveMap.html#bpy.types.CurveMap "bpy.types.CurveMap"), (never None)) – curve, Curve to evaluate

  * **position** (_float in_ _[__-inf_ _,__inf_ _]_) – Position, Position to evaluate curve at

Returns:

    

Value, Value of curve at given location

Return type:

    

float in [-inf, inf]

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

  * [`Brush.automasking_cavity_curve`](bpy.types.Brush.html#bpy.types.Brush.automasking_cavity_curve "bpy.types.Brush.automasking_cavity_curve")
  * [`Brush.curve`](bpy.types.Brush.html#bpy.types.Brush.curve "bpy.types.Brush.curve")
  * [`Brush.curve_random_hue`](bpy.types.Brush.html#bpy.types.Brush.curve_random_hue "bpy.types.Brush.curve_random_hue")
  * [`Brush.curve_random_saturation`](bpy.types.Brush.html#bpy.types.Brush.curve_random_saturation "bpy.types.Brush.curve_random_saturation")
  * [`Brush.curve_random_value`](bpy.types.Brush.html#bpy.types.Brush.curve_random_value "bpy.types.Brush.curve_random_value")
  * [`BrushCurvesSculptSettings.curve_parameter_falloff`](bpy.types.BrushCurvesSculptSettings.html#bpy.types.BrushCurvesSculptSettings.curve_parameter_falloff "bpy.types.BrushCurvesSculptSettings.curve_parameter_falloff")
  * [`BrushGpencilSettings.curve_jitter`](bpy.types.BrushGpencilSettings.html#bpy.types.BrushGpencilSettings.curve_jitter "bpy.types.BrushGpencilSettings.curve_jitter")
  * [`BrushGpencilSettings.curve_random_hue`](bpy.types.BrushGpencilSettings.html#bpy.types.BrushGpencilSettings.curve_random_hue "bpy.types.BrushGpencilSettings.curve_random_hue")
  * [`BrushGpencilSettings.curve_random_pressure`](bpy.types.BrushGpencilSettings.html#bpy.types.BrushGpencilSettings.curve_random_pressure "bpy.types.BrushGpencilSettings.curve_random_pressure")
  * [`BrushGpencilSettings.curve_random_saturation`](bpy.types.BrushGpencilSettings.html#bpy.types.BrushGpencilSettings.curve_random_saturation "bpy.types.BrushGpencilSettings.curve_random_saturation")
  * [`BrushGpencilSettings.curve_random_strength`](bpy.types.BrushGpencilSettings.html#bpy.types.BrushGpencilSettings.curve_random_strength "bpy.types.BrushGpencilSettings.curve_random_strength")
  * [`BrushGpencilSettings.curve_random_uv`](bpy.types.BrushGpencilSettings.html#bpy.types.BrushGpencilSettings.curve_random_uv "bpy.types.BrushGpencilSettings.curve_random_uv")
  * [`BrushGpencilSettings.curve_random_value`](bpy.types.BrushGpencilSettings.html#bpy.types.BrushGpencilSettings.curve_random_value "bpy.types.BrushGpencilSettings.curve_random_value")
  * [`BrushGpencilSettings.curve_sensitivity`](bpy.types.BrushGpencilSettings.html#bpy.types.BrushGpencilSettings.curve_sensitivity "bpy.types.BrushGpencilSettings.curve_sensitivity")
  * [`BrushGpencilSettings.curve_strength`](bpy.types.BrushGpencilSettings.html#bpy.types.BrushGpencilSettings.curve_strength "bpy.types.BrushGpencilSettings.curve_strength")
  * [`ColorManagedViewSettings.curve_mapping`](bpy.types.ColorManagedViewSettings.html#bpy.types.ColorManagedViewSettings.curve_mapping "bpy.types.ColorManagedViewSettings.curve_mapping")
  * [`CompositorNodeCurveRGB.mapping`](bpy.types.CompositorNodeCurveRGB.html#bpy.types.CompositorNodeCurveRGB.mapping "bpy.types.CompositorNodeCurveRGB.mapping")
  * [`CompositorNodeCurveVec.mapping`](bpy.types.CompositorNodeCurveVec.html#bpy.types.CompositorNodeCurveVec.mapping "bpy.types.CompositorNodeCurveVec.mapping")
  * [`CompositorNodeHueCorrect.mapping`](bpy.types.CompositorNodeHueCorrect.html#bpy.types.CompositorNodeHueCorrect.mapping "bpy.types.CompositorNodeHueCorrect.mapping")
  * [`CompositorNodeTime.curve`](bpy.types.CompositorNodeTime.html#bpy.types.CompositorNodeTime.curve "bpy.types.CompositorNodeTime.curve")
  * [`CurvesModifier.curve_mapping`](bpy.types.CurvesModifier.html#bpy.types.CurvesModifier.curve_mapping "bpy.types.CurvesModifier.curve_mapping")
  * [`EQCurveMappingData.curve_mapping`](bpy.types.EQCurveMappingData.html#bpy.types.EQCurveMappingData.curve_mapping "bpy.types.EQCurveMappingData.curve_mapping")
  * [`GPencilInterpolateSettings.interpolation_curve`](bpy.types.GPencilInterpolateSettings.html#bpy.types.GPencilInterpolateSettings.interpolation_curve "bpy.types.GPencilInterpolateSettings.interpolation_curve")
  * [`GPencilSculptSettings.multiframe_falloff_curve`](bpy.types.GPencilSculptSettings.html#bpy.types.GPencilSculptSettings.multiframe_falloff_curve "bpy.types.GPencilSculptSettings.multiframe_falloff_curve")
  * [`GPencilSculptSettings.thickness_primitive_curve`](bpy.types.GPencilSculptSettings.html#bpy.types.GPencilSculptSettings.thickness_primitive_curve "bpy.types.GPencilSculptSettings.thickness_primitive_curve")
  * [`GreasePencilColorModifier.custom_curve`](bpy.types.GreasePencilColorModifier.html#bpy.types.GreasePencilColorModifier.custom_curve "bpy.types.GreasePencilColorModifier.custom_curve")
  * [`GreasePencilHookModifier.custom_curve`](bpy.types.GreasePencilHookModifier.html#bpy.types.GreasePencilHookModifier.custom_curve "bpy.types.GreasePencilHookModifier.custom_curve")
  * [`GreasePencilNoiseModifier.custom_curve`](bpy.types.GreasePencilNoiseModifier.html#bpy.types.GreasePencilNoiseModifier.custom_curve "bpy.types.GreasePencilNoiseModifier.custom_curve")
  * [`GreasePencilOpacityModifier.custom_curve`](bpy.types.GreasePencilOpacityModifier.html#bpy.types.GreasePencilOpacityModifier.custom_curve "bpy.types.GreasePencilOpacityModifier.custom_curve")
  * [`GreasePencilSmoothModifier.custom_curve`](bpy.types.GreasePencilSmoothModifier.html#bpy.types.GreasePencilSmoothModifier.custom_curve "bpy.types.GreasePencilSmoothModifier.custom_curve")
  * [`GreasePencilThickModifierData.custom_curve`](bpy.types.GreasePencilThickModifierData.html#bpy.types.GreasePencilThickModifierData.custom_curve "bpy.types.GreasePencilThickModifierData.custom_curve")
  * [`GreasePencilTintModifier.custom_curve`](bpy.types.GreasePencilTintModifier.html#bpy.types.GreasePencilTintModifier.custom_curve "bpy.types.GreasePencilTintModifier.custom_curve")
  * [`HookModifier.falloff_curve`](bpy.types.HookModifier.html#bpy.types.HookModifier.falloff_curve "bpy.types.HookModifier.falloff_curve")

|

  * [`HueCorrectModifier.curve_mapping`](bpy.types.HueCorrectModifier.html#bpy.types.HueCorrectModifier.curve_mapping "bpy.types.HueCorrectModifier.curve_mapping")
  * [`LineStyleAlphaModifier_AlongStroke.curve`](bpy.types.LineStyleAlphaModifier_AlongStroke.html#bpy.types.LineStyleAlphaModifier_AlongStroke.curve "bpy.types.LineStyleAlphaModifier_AlongStroke.curve")
  * [`LineStyleAlphaModifier_CreaseAngle.curve`](bpy.types.LineStyleAlphaModifier_CreaseAngle.html#bpy.types.LineStyleAlphaModifier_CreaseAngle.curve "bpy.types.LineStyleAlphaModifier_CreaseAngle.curve")
  * [`LineStyleAlphaModifier_Curvature_3D.curve`](bpy.types.LineStyleAlphaModifier_Curvature_3D.html#bpy.types.LineStyleAlphaModifier_Curvature_3D.curve "bpy.types.LineStyleAlphaModifier_Curvature_3D.curve")
  * [`LineStyleAlphaModifier_DistanceFromCamera.curve`](bpy.types.LineStyleAlphaModifier_DistanceFromCamera.html#bpy.types.LineStyleAlphaModifier_DistanceFromCamera.curve "bpy.types.LineStyleAlphaModifier_DistanceFromCamera.curve")
  * [`LineStyleAlphaModifier_DistanceFromObject.curve`](bpy.types.LineStyleAlphaModifier_DistanceFromObject.html#bpy.types.LineStyleAlphaModifier_DistanceFromObject.curve "bpy.types.LineStyleAlphaModifier_DistanceFromObject.curve")
  * [`LineStyleAlphaModifier_Material.curve`](bpy.types.LineStyleAlphaModifier_Material.html#bpy.types.LineStyleAlphaModifier_Material.curve "bpy.types.LineStyleAlphaModifier_Material.curve")
  * [`LineStyleAlphaModifier_Noise.curve`](bpy.types.LineStyleAlphaModifier_Noise.html#bpy.types.LineStyleAlphaModifier_Noise.curve "bpy.types.LineStyleAlphaModifier_Noise.curve")
  * [`LineStyleAlphaModifier_Tangent.curve`](bpy.types.LineStyleAlphaModifier_Tangent.html#bpy.types.LineStyleAlphaModifier_Tangent.curve "bpy.types.LineStyleAlphaModifier_Tangent.curve")
  * [`LineStyleThicknessModifier_AlongStroke.curve`](bpy.types.LineStyleThicknessModifier_AlongStroke.html#bpy.types.LineStyleThicknessModifier_AlongStroke.curve "bpy.types.LineStyleThicknessModifier_AlongStroke.curve")
  * [`LineStyleThicknessModifier_CreaseAngle.curve`](bpy.types.LineStyleThicknessModifier_CreaseAngle.html#bpy.types.LineStyleThicknessModifier_CreaseAngle.curve "bpy.types.LineStyleThicknessModifier_CreaseAngle.curve")
  * [`LineStyleThicknessModifier_Curvature_3D.curve`](bpy.types.LineStyleThicknessModifier_Curvature_3D.html#bpy.types.LineStyleThicknessModifier_Curvature_3D.curve "bpy.types.LineStyleThicknessModifier_Curvature_3D.curve")
  * [`LineStyleThicknessModifier_DistanceFromCamera.curve`](bpy.types.LineStyleThicknessModifier_DistanceFromCamera.html#bpy.types.LineStyleThicknessModifier_DistanceFromCamera.curve "bpy.types.LineStyleThicknessModifier_DistanceFromCamera.curve")
  * [`LineStyleThicknessModifier_DistanceFromObject.curve`](bpy.types.LineStyleThicknessModifier_DistanceFromObject.html#bpy.types.LineStyleThicknessModifier_DistanceFromObject.curve "bpy.types.LineStyleThicknessModifier_DistanceFromObject.curve")
  * [`LineStyleThicknessModifier_Material.curve`](bpy.types.LineStyleThicknessModifier_Material.html#bpy.types.LineStyleThicknessModifier_Material.curve "bpy.types.LineStyleThicknessModifier_Material.curve")
  * [`LineStyleThicknessModifier_Tangent.curve`](bpy.types.LineStyleThicknessModifier_Tangent.html#bpy.types.LineStyleThicknessModifier_Tangent.curve "bpy.types.LineStyleThicknessModifier_Tangent.curve")
  * [`Paint.cavity_curve`](bpy.types.Paint.html#bpy.types.Paint.cavity_curve "bpy.types.Paint.cavity_curve")
  * [`ParticleBrush.curve`](bpy.types.ParticleBrush.html#bpy.types.ParticleBrush.curve "bpy.types.ParticleBrush.curve")
  * [`ParticleSettings.clump_curve`](bpy.types.ParticleSettings.html#bpy.types.ParticleSettings.clump_curve "bpy.types.ParticleSettings.clump_curve")
  * [`ParticleSettings.roughness_curve`](bpy.types.ParticleSettings.html#bpy.types.ParticleSettings.roughness_curve "bpy.types.ParticleSettings.roughness_curve")
  * [`ParticleSettings.twist_curve`](bpy.types.ParticleSettings.html#bpy.types.ParticleSettings.twist_curve "bpy.types.ParticleSettings.twist_curve")
  * [`RenderSettings.motion_blur_shutter_curve`](bpy.types.RenderSettings.html#bpy.types.RenderSettings.motion_blur_shutter_curve "bpy.types.RenderSettings.motion_blur_shutter_curve")
  * [`Sculpt.automasking_cavity_curve`](bpy.types.Sculpt.html#bpy.types.Sculpt.automasking_cavity_curve "bpy.types.Sculpt.automasking_cavity_curve")
  * [`Sculpt.automasking_cavity_curve_op`](bpy.types.Sculpt.html#bpy.types.Sculpt.automasking_cavity_curve_op "bpy.types.Sculpt.automasking_cavity_curve_op")
  * [`ShaderNodeFloatCurve.mapping`](bpy.types.ShaderNodeFloatCurve.html#bpy.types.ShaderNodeFloatCurve.mapping "bpy.types.ShaderNodeFloatCurve.mapping")
  * [`ShaderNodeRGBCurve.mapping`](bpy.types.ShaderNodeRGBCurve.html#bpy.types.ShaderNodeRGBCurve.mapping "bpy.types.ShaderNodeRGBCurve.mapping")
  * [`ShaderNodeVectorCurve.mapping`](bpy.types.ShaderNodeVectorCurve.html#bpy.types.ShaderNodeVectorCurve.mapping "bpy.types.ShaderNodeVectorCurve.mapping")
  * [`TextureNodeCurveRGB.mapping`](bpy.types.TextureNodeCurveRGB.html#bpy.types.TextureNodeCurveRGB.mapping "bpy.types.TextureNodeCurveRGB.mapping")
  * [`TextureNodeCurveTime.curve`](bpy.types.TextureNodeCurveTime.html#bpy.types.TextureNodeCurveTime.curve "bpy.types.TextureNodeCurveTime.curve")
  * [`UvSculpt.strength_curve`](bpy.types.UvSculpt.html#bpy.types.UvSculpt.strength_curve "bpy.types.UvSculpt.strength_curve")
  * [`VertexWeightEditModifier.map_curve`](bpy.types.VertexWeightEditModifier.html#bpy.types.VertexWeightEditModifier.map_curve "bpy.types.VertexWeightEditModifier.map_curve")
  * [`VertexWeightProximityModifier.map_curve`](bpy.types.VertexWeightProximityModifier.html#bpy.types.VertexWeightProximityModifier.map_curve "bpy.types.VertexWeightProximityModifier.map_curve")
  * [`WarpModifier.falloff_curve`](bpy.types.WarpModifier.html#bpy.types.WarpModifier.falloff_curve "bpy.types.WarpModifier.falloff_curve")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

