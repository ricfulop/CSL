---
url: https://freecad.github.io/SourceDoc/da/d1b/classautomotive__design_1_1tolerance__value.html
scraped_at: 2025-09-08T15:14:39.397842
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [tolerance_value](../../da/d1b/classautomotive__design_1_1tolerance__value.html)

[List of all members](../../de/d3f/classautomotive__design_1_1tolerance__value-members.html) | Public Member Functions | Public Attributes

automotive_design.tolerance_value Class Reference

##  Public Member Functions  
  
---  
def | [lower_bound](../../da/d1b/classautomotive__design_1_1tolerance__value.html#a36ab50cc2ca26faf062b009e16e7cca4) ()  
def | [upper_bound](../../da/d1b/classautomotive__design_1_1tolerance__value.html#a00d51d196ad6292b4d3c7cb2f3466c2f) ()  
def | [wr1](../../da/d1b/classautomotive__design_1_1tolerance__value.html#a2abfc5e79b83a1678fcb8d825ddbd462) (self)  
def | [wr2](../../da/d1b/classautomotive__design_1_1tolerance__value.html#a9c5ef6df15a5006251fc6e5e7372973f) (self)  
  
##  Public Attributes  
  
---  
|
[lower_bound](../../da/d1b/classautomotive__design_1_1tolerance__value.html#aa347fbaa84b3c586e97252d68481bf0b)  
|
[unit_component](../../da/d1b/classautomotive__design_1_1tolerance__value.html#ac7dcee6ace15304641c39e35dd73a709)  
|
[upper_bound](../../da/d1b/classautomotive__design_1_1tolerance__value.html#a76c7e8a9c5e9b045c94fb5ca2bd972ee)  
  
## Detailed Description

    
    
    Entity tolerance_value definition.
    
        :param lower_bound
        :type lower_bound:measure_with_unit
    
        :param upper_bound
        :type upper_bound:measure_with_unit

## Member Function Documentation

## ◆ lower_bound()

def automotive_design.tolerance_value.lower_bound  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.tolerance_value._lower_bound,
and automotive_design.tolerance_value._lower_bound.

Referenced by
[automotive_design.tolerance_value.wr1()](../../da/d1b/classautomotive__design_1_1tolerance__value.html#a2abfc5e79b83a1678fcb8d825ddbd462).

## ◆ upper_bound()

def automotive_design.tolerance_value.upper_bound  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.tolerance_value._upper_bound,
and automotive_design.tolerance_value._upper_bound.

Referenced by
[automotive_design.tolerance_value.wr1()](../../da/d1b/classautomotive__design_1_1tolerance__value.html#a2abfc5e79b83a1678fcb8d825ddbd462).

## ◆ wr1()

def automotive_design.tolerance_value.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.tolerance_value.lower_bound,
[automotive_design.tolerance_value.lower_bound](../../da/d1b/classautomotive__design_1_1tolerance__value.html#aa347fbaa84b3c586e97252d68481bf0b),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.tolerance_value.upper_bound,
[automotive_design.tolerance_value.upper_bound](../../da/d1b/classautomotive__design_1_1tolerance__value.html#a76c7e8a9c5e9b045c94fb5ca2bd972ee),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.measure_with_unit.value_component,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.value_representation_item.value_component,
[automotive_design.measure_with_unit.value_component](../../db/d66/classautomotive__design_1_1measure__with__unit.html#a6a36286bc2dcf141ac26006e93b8d59b),
[automotive_design.value_representation_item.value_component](../../d3/da7/classautomotive__design_1_1value__representation__item.html#af3ad8e6f86fac9a9bcca8f9c923ddfd7),
and
[config_control_design.measure_with_unit.value_component](../../d7/d6d/classconfig__control__design_1_1measure__with__unit.html#ab07ae804801ef56357725e86474a1666).

## ◆ wr2()

def automotive_design.tolerance_value.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
## Member Data Documentation

## ◆ lower_bound

automotive_design.tolerance_value.lower_bound  
---  
  
Referenced by
[automotive_design.tolerance_value.wr1()](../../da/d1b/classautomotive__design_1_1tolerance__value.html#a2abfc5e79b83a1678fcb8d825ddbd462).

## ◆ unit_component

automotive_design.tolerance_value.unit_component  
---  
  
Referenced by
[automotive_design.conversion_based_unit.named_unit_dimensions()](../../da/d8b/classautomotive__design_1_1conversion__based__unit.html#a051852ea2ab9f86eae67ce013076c373),
and
[automotive_design.projected_zone_definition.wr2()](../../d2/d04/classautomotive__design_1_1projected__zone__definition.html#a8b38d4f5b6eecd7742607255c261f40b).

## ◆ upper_bound

automotive_design.tolerance_value.upper_bound  
---  
  
Referenced by
[automotive_design.tolerance_value.wr1()](../../da/d1b/classautomotive__design_1_1tolerance__value.html#a2abfc5e79b83a1678fcb8d825ddbd462).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

