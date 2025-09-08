---
url: https://freecad.github.io/SourceDoc/d2/d04/classautomotive__design_1_1projected__zone__definition.html
scraped_at: 2025-09-08T15:11:10.505737
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [projected_zone_definition](../../d2/d04/classautomotive__design_1_1projected__zone__definition.html)

[List of all members](../../d3/d66/classautomotive__design_1_1projected__zone__definition-members.html) | Public Member Functions | Public Attributes

automotive_design.projected_zone_definition Class Reference

##  Public Member Functions  
  
---  
def | [projected_length](../../d2/d04/classautomotive__design_1_1projected__zone__definition.html#a78664599b1c99ad2194f92f53326f7c4) ()  
def | [projection_end](../../d2/d04/classautomotive__design_1_1projected__zone__definition.html#af1f173e20e2b814bd2d96625e2157ce4) ()  
def | [wr1](../../d2/d04/classautomotive__design_1_1projected__zone__definition.html#ad18477cba8cf3247f93407ee8869089c) (self)  
def | [wr2](../../d2/d04/classautomotive__design_1_1projected__zone__definition.html#a8b38d4f5b6eecd7742607255c261f40b) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.tolerance_zone_definition](../../d8/d9d/classautomotive__design_1_1tolerance__zone__definition.html)  
def | [boundaries](../../d8/d9d/classautomotive__design_1_1tolerance__zone__definition.html#ad1ce85a92ac2e8eaded59dade3ba9498) ()  
def | [zone](../../d8/d9d/classautomotive__design_1_1tolerance__zone__definition.html#a12115a713b73549cf16de4666fb87b2e) ()  
  
##  Public Attributes  
  
---  
|
[projected_length](../../d2/d04/classautomotive__design_1_1projected__zone__definition.html#a31331628953d137450642702b5413b08)  
|
[projection_end](../../d2/d04/classautomotive__design_1_1projected__zone__definition.html#a03146d5f392d592f0697d3ad1b585633)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.tolerance_zone_definition](../../d8/d9d/classautomotive__design_1_1tolerance__zone__definition.html)  
|
[boundaries](../../d8/d9d/classautomotive__design_1_1tolerance__zone__definition.html#a157006997500cd225328ae5e191ff94a)  
|
[zone](../../d8/d9d/classautomotive__design_1_1tolerance__zone__definition.html#acad199ab29b7272af33a565806ce32c9)  
  
## Detailed Description

    
    
    Entity projected_zone_definition definition.
    
        :param projection_end
        :type projection_end:shape_aspect
    
        :param projected_length
        :type projected_length:measure_with_unit

## Member Function Documentation

## ◆ projected_length()

def automotive_design.projected_zone_definition.projected_length  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.projected_zone_definition._projected_length,
and automotive_design.projected_zone_definition._projected_length.

Referenced by
[automotive_design.projected_zone_definition.wr1()](../../d2/d04/classautomotive__design_1_1projected__zone__definition.html#ad18477cba8cf3247f93407ee8869089c),
and
[automotive_design.projected_zone_definition.wr2()](../../d2/d04/classautomotive__design_1_1projected__zone__definition.html#a8b38d4f5b6eecd7742607255c261f40b).

## ◆ projection_end()

def automotive_design.projected_zone_definition.projection_end  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.projected_zone_definition._projection_end,
and automotive_design.projected_zone_definition._projection_end.

## ◆ wr1()

def automotive_design.projected_zone_definition.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.projected_zone_definition.projected_length,
[automotive_design.projected_zone_definition.projected_length](../../d2/d04/classautomotive__design_1_1projected__zone__definition.html#a31331628953d137450642702b5413b08),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.measure_with_unit.value_component,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.value_representation_item.value_component,
[automotive_design.measure_with_unit.value_component](../../db/d66/classautomotive__design_1_1measure__with__unit.html#a6a36286bc2dcf141ac26006e93b8d59b),
[automotive_design.value_representation_item.value_component](../../d3/da7/classautomotive__design_1_1value__representation__item.html#af3ad8e6f86fac9a9bcca8f9c923ddfd7),
and
[config_control_design.measure_with_unit.value_component](../../d7/d6d/classconfig__control__design_1_1measure__with__unit.html#ab07ae804801ef56357725e86474a1666).

## ◆ wr2()

def automotive_design.projected_zone_definition.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[automotive_design.derive_dimensional_exponents()](../../d4/ddf/namespaceautomotive__design.html#a930358cc90d7890ebfbf59511431901c),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.projected_zone_definition.projected_length,
[automotive_design.projected_zone_definition.projected_length](../../d2/d04/classautomotive__design_1_1projected__zone__definition.html#a31331628953d137450642702b5413b08),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.measure_with_unit.unit_component,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.tolerance_value.unit_component,
[automotive_design.measure_with_unit.unit_component](../../db/d66/classautomotive__design_1_1measure__with__unit.html#a30da8ff5991b14c1513623a8a78df360),
[automotive_design.tolerance_value.unit_component](../../da/d1b/classautomotive__design_1_1tolerance__value.html#ac7dcee6ace15304641c39e35dd73a709),
and
[config_control_design.measure_with_unit.unit_component](../../d7/d6d/classconfig__control__design_1_1measure__with__unit.html#a0c21fd85303ecb5bba70cc8b85f5fbb3).

## Member Data Documentation

## ◆ projected_length

automotive_design.projected_zone_definition.projected_length  
---  
  
Referenced by
[automotive_design.projected_zone_definition.wr1()](../../d2/d04/classautomotive__design_1_1projected__zone__definition.html#ad18477cba8cf3247f93407ee8869089c),
and
[automotive_design.projected_zone_definition.wr2()](../../d2/d04/classautomotive__design_1_1projected__zone__definition.html#a8b38d4f5b6eecd7742607255c261f40b).

## ◆ projection_end

automotive_design.projected_zone_definition.projection_end  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

