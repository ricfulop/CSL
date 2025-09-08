---
url: https://freecad.github.io/SourceDoc/df/dc3/classautomotive__design_1_1mechanism.html
scraped_at: 2025-09-08T15:08:03.742346
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [mechanism](../../df/dc3/classautomotive__design_1_1mechanism.html)

[List of all members](../../d2/dcb/classautomotive__design_1_1mechanism-members.html) | Public Member Functions | Public Attributes

automotive_design.mechanism Class Reference

##  Public Member Functions  
  
---  
def | [base](../../df/dc3/classautomotive__design_1_1mechanism.html#aa10127a1c07f9d09cb1f8383ec0e1685) ()  
def | [containing_property](../../df/dc3/classautomotive__design_1_1mechanism.html#a7bc3427730c79cfc2f20b3dadb5c1621) ()  
def | [structure_definition](../../df/dc3/classautomotive__design_1_1mechanism.html#a8d048d6d6751525a256f7106e49bf5c8) ()  
def | [wr1](../../df/dc3/classautomotive__design_1_1mechanism.html#addb0fe8f5c9c6f7efbf75f8c43574511) (self)  
  
##  Public Attributes  
  
---  
|
[base](../../df/dc3/classautomotive__design_1_1mechanism.html#a2f05a4ada5c1fc1f6a76e576d5216671)  
|
[containing_property](../../df/dc3/classautomotive__design_1_1mechanism.html#af4bd4ae102d7422d145502996221f41c)  
|
[structure_definition](../../df/dc3/classautomotive__design_1_1mechanism.html#ac659a8ee7fa443b24ec0c11857800975)  
  
## Detailed Description

    
    
    Entity mechanism definition.
    
        :param structure_definition
        :type structure_definition:kinematic_structure
    
        :param base
        :type base:kinematic_link
    
        :param containing_property
        :type containing_property:kinematic_property_definition

## Member Function Documentation

## ◆ base()

def automotive_design.mechanism.base  | ( | | ) |   
---|---|---|---|---  
  
References Base::Axis._base,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.alternate_product_relationship._base,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.assembly_component_usage_substitute._base,
automotive_design.mechanism._base,
automotive_design.alternate_product_relationship._base,
automotive_design.assembly_component_usage_substitute._base,
config_control_design.alternate_product_relationship._base, and
config_control_design.assembly_component_usage_substitute._base.

Referenced by
[automotive_design.mechanism_base_placement.representation_relationship_rep_2()](../../db/d8b/classautomotive__design_1_1mechanism__base__placement.html#a2036d6b183b15bb056bf017cb9d261f5),
[PathTests.TestPathStock.TestPathStock.test12()](../../da/d6d/classPathTests_1_1TestPathStock_1_1TestPathStock.html#a1fb40516a78ced11589f0fc264bffa84),
[automotive_design.alternate_product_relationship.wr1()](../../d4/ddc/classautomotive__design_1_1alternate__product__relationship.html#a71ebb08637be198fba68bbe6cd511779),
[config_control_design.alternate_product_relationship.wr1()](../../db/d4c/classconfig__control__design_1_1alternate__product__relationship.html#a80679d1c15b83eeefd706b42bdaca71a),
[automotive_design.assembly_component_usage_substitute.wr2()](../../d3/d66/classautomotive__design_1_1assembly__component__usage__substitute.html#af760fb12cbfb0bad117a1b394ec77d4e),
and
[config_control_design.assembly_component_usage_substitute.wr2()](../../d7/d37/classconfig__control__design_1_1assembly__component__usage__substitute.html#afeed759c1e59ecb42b4d564eff3e614c).

## ◆ containing_property()

def automotive_design.mechanism.containing_property  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.mechanism._containing_property.

## ◆ structure_definition()

def automotive_design.mechanism.structure_definition  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.mechanism._structure_definition.

## ◆ wr1()

def automotive_design.mechanism.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
## Member Data Documentation

## ◆ base

automotive_design.mechanism.base  
---  
  
Referenced by
[automotive_design.mechanism_base_placement.representation_relationship_rep_2()](../../db/d8b/classautomotive__design_1_1mechanism__base__placement.html#a2036d6b183b15bb056bf017cb9d261f5),
[PathTests.TestPathStock.TestPathStock.test12()](../../da/d6d/classPathTests_1_1TestPathStock_1_1TestPathStock.html#a1fb40516a78ced11589f0fc264bffa84),
[automotive_design.alternate_product_relationship.wr1()](../../d4/ddc/classautomotive__design_1_1alternate__product__relationship.html#a71ebb08637be198fba68bbe6cd511779),
[config_control_design.alternate_product_relationship.wr1()](../../db/d4c/classconfig__control__design_1_1alternate__product__relationship.html#a80679d1c15b83eeefd706b42bdaca71a),
[automotive_design.assembly_component_usage_substitute.wr2()](../../d3/d66/classautomotive__design_1_1assembly__component__usage__substitute.html#af760fb12cbfb0bad117a1b394ec77d4e),
and
[config_control_design.assembly_component_usage_substitute.wr2()](../../d7/d37/classconfig__control__design_1_1assembly__component__usage__substitute.html#afeed759c1e59ecb42b4d564eff3e614c).

## ◆ containing_property

automotive_design.mechanism.containing_property  
---  
  
## ◆ structure_definition

automotive_design.mechanism.structure_definition  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

