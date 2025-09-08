---
url: https://docs.blender.org/api/current/bpy.types.FloatProperty.html
scraped_at: 2025-09-08T14:25:29.184088
title: FloatProperty(Property)¶
---

# FloatProperty(Property)¶  
  
base classes — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct"),
[`Property`](bpy.types.Property.html#bpy.types.Property "bpy.types.Property")

_class _bpy.types.FloatProperty(_Property_)¶

    

RNA floating-point number (single precision) property definition

array_dimensions¶

    

Length of each dimension of the array

Type:

    

int array of 3 items in [0, inf], default (0, 0, 0), (readonly)

array_length¶

    

Maximum length of the array, 0 means unlimited

Type:

    

int in [0, inf], default 0, (readonly)

default¶

    

Default value for this number

Type:

    

float in [-inf, inf], default 0.0, (readonly)

default_array¶

    

Default value for this array

Type:

    

float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

hard_max¶

    

Maximum value used by buttons

Type:

    

float in [-inf, inf], default 0.0, (readonly)

hard_min¶

    

Minimum value used by buttons

Type:

    

float in [-inf, inf], default 0.0, (readonly)

is_array¶

    

Type:

    

boolean, default False, (readonly)

precision¶

    

Number of digits after the dot used by buttons. Fraction is automatically
hidden for exact integer values of fields with unit ‘NONE’ or ‘TIME’ (frame
count) and step divisible by 100.

Type:

    

int in [0, inf], default 0, (readonly)

soft_max¶

    

Maximum value used by buttons

Type:

    

float in [-inf, inf], default 0.0, (readonly)

soft_min¶

    

Minimum value used by buttons

Type:

    

float in [-inf, inf], default 0.0, (readonly)

step¶

    

Step size used by number buttons, for floats 1/100th of the step size

Type:

    

float in [0, inf], default 0.0, (readonly)

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
  * [`Property.name`](bpy.types.Property.html#bpy.types.Property.name "bpy.types.Property.name")
  * [`Property.identifier`](bpy.types.Property.html#bpy.types.Property.identifier "bpy.types.Property.identifier")
  * [`Property.description`](bpy.types.Property.html#bpy.types.Property.description "bpy.types.Property.description")
  * [`Property.translation_context`](bpy.types.Property.html#bpy.types.Property.translation_context "bpy.types.Property.translation_context")
  * [`Property.type`](bpy.types.Property.html#bpy.types.Property.type "bpy.types.Property.type")
  * [`Property.subtype`](bpy.types.Property.html#bpy.types.Property.subtype "bpy.types.Property.subtype")
  * [`Property.srna`](bpy.types.Property.html#bpy.types.Property.srna "bpy.types.Property.srna")
  * [`Property.unit`](bpy.types.Property.html#bpy.types.Property.unit "bpy.types.Property.unit")
  * [`Property.icon`](bpy.types.Property.html#bpy.types.Property.icon "bpy.types.Property.icon")
  * [`Property.is_readonly`](bpy.types.Property.html#bpy.types.Property.is_readonly "bpy.types.Property.is_readonly")
  * [`Property.is_animatable`](bpy.types.Property.html#bpy.types.Property.is_animatable "bpy.types.Property.is_animatable")
  * [`Property.is_overridable`](bpy.types.Property.html#bpy.types.Property.is_overridable "bpy.types.Property.is_overridable")
  * [`Property.is_required`](bpy.types.Property.html#bpy.types.Property.is_required "bpy.types.Property.is_required")
  * [`Property.is_argument_optional`](bpy.types.Property.html#bpy.types.Property.is_argument_optional "bpy.types.Property.is_argument_optional")

|

  * [`Property.is_never_none`](bpy.types.Property.html#bpy.types.Property.is_never_none "bpy.types.Property.is_never_none")
  * [`Property.is_hidden`](bpy.types.Property.html#bpy.types.Property.is_hidden "bpy.types.Property.is_hidden")
  * [`Property.is_skip_save`](bpy.types.Property.html#bpy.types.Property.is_skip_save "bpy.types.Property.is_skip_save")
  * [`Property.is_skip_preset`](bpy.types.Property.html#bpy.types.Property.is_skip_preset "bpy.types.Property.is_skip_preset")
  * [`Property.is_output`](bpy.types.Property.html#bpy.types.Property.is_output "bpy.types.Property.is_output")
  * [`Property.is_registered`](bpy.types.Property.html#bpy.types.Property.is_registered "bpy.types.Property.is_registered")
  * [`Property.is_registered_optional`](bpy.types.Property.html#bpy.types.Property.is_registered_optional "bpy.types.Property.is_registered_optional")
  * [`Property.is_runtime`](bpy.types.Property.html#bpy.types.Property.is_runtime "bpy.types.Property.is_runtime")
  * [`Property.is_enum_flag`](bpy.types.Property.html#bpy.types.Property.is_enum_flag "bpy.types.Property.is_enum_flag")
  * [`Property.is_library_editable`](bpy.types.Property.html#bpy.types.Property.is_library_editable "bpy.types.Property.is_library_editable")
  * [`Property.is_path_output`](bpy.types.Property.html#bpy.types.Property.is_path_output "bpy.types.Property.is_path_output")
  * [`Property.is_path_supports_blend_relative`](bpy.types.Property.html#bpy.types.Property.is_path_supports_blend_relative "bpy.types.Property.is_path_supports_blend_relative")
  * [`Property.is_path_supports_templates`](bpy.types.Property.html#bpy.types.Property.is_path_supports_templates "bpy.types.Property.is_path_supports_templates")
  * [`Property.tags`](bpy.types.Property.html#bpy.types.Property.tags "bpy.types.Property.tags")

  
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

|

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
  * [`Property.bl_rna_get_subclass`](bpy.types.Property.html#bpy.types.Property.bl_rna_get_subclass "bpy.types.Property.bl_rna_get_subclass")
  * [`Property.bl_rna_get_subclass_py`](bpy.types.Property.html#bpy.types.Property.bl_rna_get_subclass_py "bpy.types.Property.bl_rna_get_subclass_py")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

