---
url: https://freecad.github.io/SourceDoc/d7/d6d/classconfig__control__design_1_1measure__with__unit.html
scraped_at: 2025-09-08T15:22:25.383350
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [measure_with_unit](../../d7/d6d/classconfig__control__design_1_1measure__with__unit.html)

[List of all members](../../db/dc8/classconfig__control__design_1_1measure__with__unit-members.html) | Public Member Functions | Public Attributes

config_control_design.measure_with_unit Class Reference

##  Public Member Functions  
  
---  
def | [unit_component](../../d7/d6d/classconfig__control__design_1_1measure__with__unit.html#ac6c509bee9eb59277f072627bf7dbc93) ()  
def | [value_component](../../d7/d6d/classconfig__control__design_1_1measure__with__unit.html#aa1721ca3248d99403996decb22a2c74b) ()  
def | [wr1](../../d7/d6d/classconfig__control__design_1_1measure__with__unit.html#a550125905995e524550f5fe916ed9405) (self)  
  
##  Public Attributes  
  
---  
|
[unit_component](../../d7/d6d/classconfig__control__design_1_1measure__with__unit.html#a0c21fd85303ecb5bba70cc8b85f5fbb3)  
|
[value_component](../../d7/d6d/classconfig__control__design_1_1measure__with__unit.html#ab07ae804801ef56357725e86474a1666)  
  
## Detailed Description

    
    
    Entity measure_with_unit definition.
    
        :param value_component
        :type value_component:measure_value
    
        :param unit_component
        :type unit_component:unit

## Member Function Documentation

## ◆ unit_component()

def config_control_design.measure_with_unit.unit_component  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.measure_with_unit._unit_component,
automotive_design.measure_with_unit._unit_component,
config_control_design.measure_with_unit._unit_component, and
[config_control_design.unit](../../d4/d07/namespaceconfig__control__design.html#a49f5715f0a78eaa317c6fdae63201cd9).

Referenced by
[automotive_design.conversion_based_unit.named_unit_dimensions()](../../da/d8b/classautomotive__design_1_1conversion__based__unit.html#a051852ea2ab9f86eae67ce013076c373),
and
[automotive_design.projected_zone_definition.wr2()](../../d2/d04/classautomotive__design_1_1projected__zone__definition.html#a8b38d4f5b6eecd7742607255c261f40b).

## ◆ value_component()

def config_control_design.measure_with_unit.value_component  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.measure_with_unit._value_component,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.value_representation_item._value_component,
automotive_design.measure_with_unit._value_component,
automotive_design.value_representation_item._value_component,
config_control_design.measure_with_unit._value_component, and
[config_control_design.measure_value](../../d4/d07/namespaceconfig__control__design.html#a40dc9d1718da257283e9686e60beec06).

Referenced by
[automotive_design.geometric_tolerance.wr1()](../../d9/d7e/classautomotive__design_1_1geometric__tolerance.html#a2fce32370e842edeb4692d15bba8963e),
[automotive_design.quantified_assembly_component_usage.wr1()](../../d5/d9b/classautomotive__design_1_1quantified__assembly__component__usage.html#aed6cc3626acff4dc91ea150e4b3ddc3a),
[automotive_design.tolerance_value.wr1()](../../da/d1b/classautomotive__design_1_1tolerance__value.html#a2abfc5e79b83a1678fcb8d825ddbd462),
[automotive_design.projected_zone_definition.wr1()](../../d2/d04/classautomotive__design_1_1projected__zone__definition.html#ad18477cba8cf3247f93407ee8869089c),
[automotive_design.geometric_tolerance_with_defined_unit.wr1()](../../d7/d30/classautomotive__design_1_1geometric__tolerance__with__defined__unit.html#aef61f246198fab1a4aafeeea187c25a6),
and
[automotive_design.make_from_usage_option.wr1()](../../d9/d86/classautomotive__design_1_1make__from__usage__option.html#a32bfd0779e9f4db34925c1de0d9bf66a).

## ◆ wr1()

def config_control_design.measure_with_unit.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented in
[config_control_design.area_measure_with_unit](../../d4/dee/classconfig__control__design_1_1area__measure__with__unit.html#a8ddc6ddb26a2d15305a14239f6877fd0),
[config_control_design.length_measure_with_unit](../../da/d40/classconfig__control__design_1_1length__measure__with__unit.html#a963a4a0c21f9905bf05fb13e0f2857e7),
[config_control_design.uncertainty_measure_with_unit](../../d1/d92/classconfig__control__design_1_1uncertainty__measure__with__unit.html#aff81c105d101d33f9283b5bbd562f7f8),
[config_control_design.plane_angle_measure_with_unit](../../df/d0a/classconfig__control__design_1_1plane__angle__measure__with__unit.html#aa66cbbf88660d7e6c23d9550fc1404c3),
[config_control_design.mass_measure_with_unit](../../d0/d6a/classconfig__control__design_1_1mass__measure__with__unit.html#a38a63ff16810ab2496254c38a8bdf123),
[config_control_design.solid_angle_measure_with_unit](../../d9/d2f/classconfig__control__design_1_1solid__angle__measure__with__unit.html#a590ef7c91642b7a52a763f7b8477df0f),
and
[config_control_design.volume_measure_with_unit](../../dc/d26/classconfig__control__design_1_1volume__measure__with__unit.html#ab326bf6fee194782a0a50a85e7f85e0a).

References
[config_control_design.valid_units()](../../d4/d07/namespaceconfig__control__design.html#ae455ab47eb524ffdb62758cd0158e58b).

## Member Data Documentation

## ◆ unit_component

config_control_design.measure_with_unit.unit_component  
---  
  
Referenced by
[automotive_design.conversion_based_unit.named_unit_dimensions()](../../da/d8b/classautomotive__design_1_1conversion__based__unit.html#a051852ea2ab9f86eae67ce013076c373),
and
[automotive_design.projected_zone_definition.wr2()](../../d2/d04/classautomotive__design_1_1projected__zone__definition.html#a8b38d4f5b6eecd7742607255c261f40b).

## ◆ value_component

config_control_design.measure_with_unit.value_component  
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

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

