---
url: https://docs.blender.org/api/current/bpy.types.ColorRamp.html
scraped_at: 2025-09-08T14:22:07.420274
title: ColorRamp(bpy_struct)¶
---

# ColorRamp(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.ColorRamp(_bpy_struct_)¶

    

Color ramp mapping a scalar value to a color

color_mode¶

    

Set color mode to use for interpolation

Type:

    

enum in [`RGB`, `HSV`, `HSL`], default `RGB`

elements¶

    

Type:

    

[`ColorRampElements`](bpy.types.ColorRampElements.html#bpy.types.ColorRampElements
"bpy.types.ColorRampElements")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`ColorRampElement`](bpy.types.ColorRampElement.html#bpy.types.ColorRampElement
"bpy.types.ColorRampElement"), (readonly)

hue_interpolation¶

    

Set color interpolation

Type:

    

enum in [`NEAR`, `FAR`, `CW`, `CCW`], default `NEAR`

interpolation¶

    

Set interpolation between color stops

Type:

    

enum in [`EASE`, `CARDINAL`, `LINEAR`, `B_SPLINE`, `CONSTANT`], default
`LINEAR`

evaluate(_position_)¶

    

Evaluate Color Ramp

Parameters:

    

**position** (_float in_ _[__0_ _,__1_ _]_) – Position, Evaluate Color Ramp at
position

Returns:

    

Color, Color at given position

Return type:

    

float array of 4 items in [-inf, inf]

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

  * [`Brush.gradient`](bpy.types.Brush.html#bpy.types.Brush.gradient "bpy.types.Brush.gradient")
  * [`ColorMapping.color_ramp`](bpy.types.ColorMapping.html#bpy.types.ColorMapping.color_ramp "bpy.types.ColorMapping.color_ramp")
  * [`CompositorNodeValToRGB.color_ramp`](bpy.types.CompositorNodeValToRGB.html#bpy.types.CompositorNodeValToRGB.color_ramp "bpy.types.CompositorNodeValToRGB.color_ramp")
  * [`DynamicPaintBrushSettings.paint_ramp`](bpy.types.DynamicPaintBrushSettings.html#bpy.types.DynamicPaintBrushSettings.paint_ramp "bpy.types.DynamicPaintBrushSettings.paint_ramp")
  * [`DynamicPaintBrushSettings.velocity_ramp`](bpy.types.DynamicPaintBrushSettings.html#bpy.types.DynamicPaintBrushSettings.velocity_ramp "bpy.types.DynamicPaintBrushSettings.velocity_ramp")
  * [`FluidDomainSettings.color_ramp`](bpy.types.FluidDomainSettings.html#bpy.types.FluidDomainSettings.color_ramp "bpy.types.FluidDomainSettings.color_ramp")
  * [`GreasePencilTintModifier.color_ramp`](bpy.types.GreasePencilTintModifier.html#bpy.types.GreasePencilTintModifier.color_ramp "bpy.types.GreasePencilTintModifier.color_ramp")
  * [`LineStyleColorModifier_AlongStroke.color_ramp`](bpy.types.LineStyleColorModifier_AlongStroke.html#bpy.types.LineStyleColorModifier_AlongStroke.color_ramp "bpy.types.LineStyleColorModifier_AlongStroke.color_ramp")
  * [`LineStyleColorModifier_CreaseAngle.color_ramp`](bpy.types.LineStyleColorModifier_CreaseAngle.html#bpy.types.LineStyleColorModifier_CreaseAngle.color_ramp "bpy.types.LineStyleColorModifier_CreaseAngle.color_ramp")
  * [`LineStyleColorModifier_Curvature_3D.color_ramp`](bpy.types.LineStyleColorModifier_Curvature_3D.html#bpy.types.LineStyleColorModifier_Curvature_3D.color_ramp "bpy.types.LineStyleColorModifier_Curvature_3D.color_ramp")

|

  * [`LineStyleColorModifier_DistanceFromCamera.color_ramp`](bpy.types.LineStyleColorModifier_DistanceFromCamera.html#bpy.types.LineStyleColorModifier_DistanceFromCamera.color_ramp "bpy.types.LineStyleColorModifier_DistanceFromCamera.color_ramp")
  * [`LineStyleColorModifier_DistanceFromObject.color_ramp`](bpy.types.LineStyleColorModifier_DistanceFromObject.html#bpy.types.LineStyleColorModifier_DistanceFromObject.color_ramp "bpy.types.LineStyleColorModifier_DistanceFromObject.color_ramp")
  * [`LineStyleColorModifier_Material.color_ramp`](bpy.types.LineStyleColorModifier_Material.html#bpy.types.LineStyleColorModifier_Material.color_ramp "bpy.types.LineStyleColorModifier_Material.color_ramp")
  * [`LineStyleColorModifier_Noise.color_ramp`](bpy.types.LineStyleColorModifier_Noise.html#bpy.types.LineStyleColorModifier_Noise.color_ramp "bpy.types.LineStyleColorModifier_Noise.color_ramp")
  * [`LineStyleColorModifier_Tangent.color_ramp`](bpy.types.LineStyleColorModifier_Tangent.html#bpy.types.LineStyleColorModifier_Tangent.color_ramp "bpy.types.LineStyleColorModifier_Tangent.color_ramp")
  * [`PreferencesView.weight_color_range`](bpy.types.PreferencesView.html#bpy.types.PreferencesView.weight_color_range "bpy.types.PreferencesView.weight_color_range")
  * [`ShaderNodeValToRGB.color_ramp`](bpy.types.ShaderNodeValToRGB.html#bpy.types.ShaderNodeValToRGB.color_ramp "bpy.types.ShaderNodeValToRGB.color_ramp")
  * [`Texture.color_ramp`](bpy.types.Texture.html#bpy.types.Texture.color_ramp "bpy.types.Texture.color_ramp")
  * [`TextureNodeValToRGB.color_ramp`](bpy.types.TextureNodeValToRGB.html#bpy.types.TextureNodeValToRGB.color_ramp "bpy.types.TextureNodeValToRGB.color_ramp")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

