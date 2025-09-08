---
url: https://freecad.github.io/SourceDoc/db/d66/classautomotive__design_1_1measure__with__unit.html
scraped_at: 2025-09-08T15:08:00.719882
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [measure_with_unit](../../db/d66/classautomotive__design_1_1measure__with__unit.html)

[List of all members](../../dc/dc4/classautomotive__design_1_1measure__with__unit-members.html) | Public Member Functions | Public Attributes

automotive_design.measure_with_unit Class Reference

##  Public Member Functions  
  
---  
def | [unit_component](../../db/d66/classautomotive__design_1_1measure__with__unit.html#accf524e37fd3e05e483c04da33ec25a9) ()  
def | [value_component](../../db/d66/classautomotive__design_1_1measure__with__unit.html#ac8f78eb072238eb05d09fc2350d71fe6) ()  
def | [wr1](../../db/d66/classautomotive__design_1_1measure__with__unit.html#a10d2c432c94d0063fedaecff3483b0d6) (self)  
  
##  Public Attributes  
  
---  
|
[unit_component](../../db/d66/classautomotive__design_1_1measure__with__unit.html#a30da8ff5991b14c1513623a8a78df360)  
|
[value_component](../../db/d66/classautomotive__design_1_1measure__with__unit.html#a6a36286bc2dcf141ac26006e93b8d59b)  
  
## Detailed Description

    
    
    Entity measure_with_unit definition.
    
        :param value_component
        :type value_component:measure_value
    
        :param unit_component
        :type unit_component:unit

## Member Function Documentation

## ◆ unit_component()

def automotive_design.measure_with_unit.unit_component  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.measure_with_unit._unit_component,
automotive_design.measure_with_unit._unit_component,
config_control_design.measure_with_unit._unit_component, and
[automotive_design.unit](../../d4/ddf/namespaceautomotive__design.html#ac54ab7af888f820d36b123946d8f0881).

Referenced by
[automotive_design.conversion_based_unit.named_unit_dimensions()](../../da/d8b/classautomotive__design_1_1conversion__based__unit.html#a051852ea2ab9f86eae67ce013076c373),
and
[automotive_design.projected_zone_definition.wr2()](../../d2/d04/classautomotive__design_1_1projected__zone__definition.html#a8b38d4f5b6eecd7742607255c261f40b).

## ◆ value_component()

def automotive_design.measure_with_unit.value_component  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.measure_with_unit._value_component,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.value_representation_item._value_component,
automotive_design.measure_with_unit._value_component,
automotive_design.value_representation_item._value_component,
config_control_design.measure_with_unit._value_component, and
[automotive_design.measure_value](../../d4/ddf/namespaceautomotive__design.html#a71871f84663120ab636d78f18836c2cd).

Referenced by
[automotive_design.geometric_tolerance.wr1()](../../d9/d7e/classautomotive__design_1_1geometric__tolerance.html#a2fce32370e842edeb4692d15bba8963e),
[automotive_design.quantified_assembly_component_usage.wr1()](../../d5/d9b/classautomotive__design_1_1quantified__assembly__component__usage.html#aed6cc3626acff4dc91ea150e4b3ddc3a),
[automotive_design.tolerance_value.wr1()](../../da/d1b/classautomotive__design_1_1tolerance__value.html#a2abfc5e79b83a1678fcb8d825ddbd462),
[automotive_design.projected_zone_definition.wr1()](../../d2/d04/classautomotive__design_1_1projected__zone__definition.html#ad18477cba8cf3247f93407ee8869089c),
[automotive_design.geometric_tolerance_with_defined_unit.wr1()](../../d7/d30/classautomotive__design_1_1geometric__tolerance__with__defined__unit.html#aef61f246198fab1a4aafeeea187c25a6),
and
[automotive_design.make_from_usage_option.wr1()](../../d9/d86/classautomotive__design_1_1make__from__usage__option.html#a32bfd0779e9f4db34925c1de0d9bf66a).

## ◆ wr1()

def automotive_design.measure_with_unit.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented in
[automotive_design.area_measure_with_unit](../../d9/da7/classautomotive__design_1_1area__measure__with__unit.html#a14bf9f06dea6d1d65df1294bf240ff5a),
[automotive_design.length_measure_with_unit](../../db/d82/classautomotive__design_1_1length__measure__with__unit.html#af5681a08c90395a137e333db11fda14d),
[automotive_design.celsius_temperature_measure_with_unit](../../d5/d02/classautomotive__design_1_1celsius__temperature__measure__with__unit.html#a5149e805292cf25bc8b88a5b008526c4),
[automotive_design.amount_of_substance_measure_with_unit](../../d5/d1f/classautomotive__design_1_1amount__of__substance__measure__with__unit.html#a4e1721c073efaac12aecf76b5a7da2da),
[automotive_design.uncertainty_measure_with_unit](../../d3/df7/classautomotive__design_1_1uncertainty__measure__with__unit.html#af8dc616469f37ac2be152af07ef01235),
[automotive_design.luminous_intensity_measure_with_unit](../../d2/d5a/classautomotive__design_1_1luminous__intensity__measure__with__unit.html#ab1ff31aaf06bec46c971bee1f8f9b58e),
[automotive_design.plane_angle_measure_with_unit](../../df/d14/classautomotive__design_1_1plane__angle__measure__with__unit.html#a3e82376248c798cbb8e4c586e57dd3a8),
[automotive_design.mass_measure_with_unit](../../dd/d8a/classautomotive__design_1_1mass__measure__with__unit.html#a7f2f08cb3059fbe7cf1ac26931fcd277),
[automotive_design.electric_current_measure_with_unit](../../d4/d8d/classautomotive__design_1_1electric__current__measure__with__unit.html#a3c30d73aeca3c268505e4d5294d1547f),
[automotive_design.solid_angle_measure_with_unit](../../da/d7c/classautomotive__design_1_1solid__angle__measure__with__unit.html#a26e56a0dbbd4a199bd6b975655897c82),
[automotive_design.volume_measure_with_unit](../../db/d5d/classautomotive__design_1_1volume__measure__with__unit.html#a5fcb814747e5188662a41a467e41e2af),
[automotive_design.thermodynamic_temperature_measure_with_unit](../../d6/da1/classautomotive__design_1_1thermodynamic__temperature__measure__with__unit.html#a33ede593a2ae3fce1f97610d4113fde9),
[automotive_design.ratio_measure_with_unit](../../d1/d54/classautomotive__design_1_1ratio__measure__with__unit.html#a6bafea5266c6083f59739aac324f5415),
and
[automotive_design.time_measure_with_unit](../../db/d65/classautomotive__design_1_1time__measure__with__unit.html#a591f4d49cced6d657520f7f819c41181).

References
[automotive_design.valid_units()](../../d4/ddf/namespaceautomotive__design.html#af37503fcc9fc0b8808f47620886eae34).

## Member Data Documentation

## ◆ unit_component

automotive_design.measure_with_unit.unit_component  
---  
  
Referenced by
[automotive_design.conversion_based_unit.named_unit_dimensions()](../../da/d8b/classautomotive__design_1_1conversion__based__unit.html#a051852ea2ab9f86eae67ce013076c373),
and
[automotive_design.projected_zone_definition.wr2()](../../d2/d04/classautomotive__design_1_1projected__zone__definition.html#a8b38d4f5b6eecd7742607255c261f40b).

## ◆ value_component

automotive_design.measure_with_unit.value_component  
---  
  
Referenced by
[automotive_design.geometric_tolerance.wr1()](../../d9/d7e/classautomotive__design_1_1geometric__tolerance.html#a2fce32370e842edeb4692d15bba8963e),
[automotive_design.quantified_assembly_component_usage.wr1()](../../d5/d9b/classautomotive__design_1_1quantified__assembly__component__usage.html#aed6cc3626acff4dc91ea150e4b3ddc3a),
[automotive_design.tolerance_value.wr1()](../../da/d1b/classautomotive__design_1_1tolerance__value.html#a2abfc5e79b83a1678fcb8d825ddbd462),
[automotive_design.projected_zone_definition.wr1()](../../d2/d04/classautomotive__design_1_1projected__zone__definition.html#ad18477cba8cf3247f93407ee8869089c),
[automotive_design.geometric_tolerance_with_defined_unit.wr1()](../../d7/d30/classautomotive__design_1_1geometric__tolerance__with__defined__unit.html#aef61f246198fab1a4aafeeea187c25a6),
and
[automotive_design.make_from_usage_option.wr1()](../../d9/d86/classautomotive__design_1_1make__from__usage__option.html#a32bfd0779e9f4db34925c1de0d9bf66a).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

