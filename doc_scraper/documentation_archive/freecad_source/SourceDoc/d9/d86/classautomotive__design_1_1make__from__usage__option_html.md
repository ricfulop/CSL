---
url: https://freecad.github.io/SourceDoc/d9/d86/classautomotive__design_1_1make__from__usage__option.html
scraped_at: 2025-09-08T15:07:44.698951
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [make_from_usage_option](../../d9/d86/classautomotive__design_1_1make__from__usage__option.html)

[List of all members](../../d1/dad/classautomotive__design_1_1make__from__usage__option-members.html) | Public Member Functions | Public Attributes

automotive_design.make_from_usage_option Class Reference

##  Public Member Functions  
  
---  
def | [quantity](../../d9/d86/classautomotive__design_1_1make__from__usage__option.html#a5ef7f66c8bec5bb78a53398084184ba5) ()  
def | [ranking](../../d9/d86/classautomotive__design_1_1make__from__usage__option.html#ac9531cb5b49ce5b534c7ceecdcc4a6b5) ()  
def | [ranking_rationale](../../d9/d86/classautomotive__design_1_1make__from__usage__option.html#a6b4fac006fa47337b85b4b9edd01a511) ()  
def | [wr1](../../d9/d86/classautomotive__design_1_1make__from__usage__option.html#a32bfd0779e9f4db34925c1de0d9bf66a) (self)  
def | [wr1](../../d6/d51/classautomotive__design_1_1product__definition__usage.html#a1b9a87b051e6f8f5626be517305ba14a) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.product_definition_relationship](../../d4/d9d/classautomotive__design_1_1product__definition__relationship.html)  
def | [description](../../d4/d9d/classautomotive__design_1_1product__definition__relationship.html#a7fae75453fae00fcb7fbdbdeca822dcc) ()  
def | [id](../../d4/d9d/classautomotive__design_1_1product__definition__relationship.html#ae8e97311578df69cea700c0f53141a0e) ()  
def | [name](../../d4/d9d/classautomotive__design_1_1product__definition__relationship.html#aae1e9b63ca199974a2ff9baca1c1f50d) ()  
def | [related_product_definition](../../d4/d9d/classautomotive__design_1_1product__definition__relationship.html#abf01d576adfeb1f18496fe97886242f3) ()  
def | [relating_product_definition](../../d4/d9d/classautomotive__design_1_1product__definition__relationship.html#a0d4abc8f217bd29f233d6e9fe3d70e4b) ()  
  
##  Public Attributes  
  
---  
|
[quantity](../../d9/d86/classautomotive__design_1_1make__from__usage__option.html#a61d0c809c0ea261082a2ea623c73ec98)  
|
[ranking](../../d9/d86/classautomotive__design_1_1make__from__usage__option.html#a68640c1796a71762c49fc270d85d31b6)  
|
[ranking_rationale](../../d9/d86/classautomotive__design_1_1make__from__usage__option.html#a77f8ae36574669d4e69692f5361d7de3)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.product_definition_relationship](../../d4/d9d/classautomotive__design_1_1product__definition__relationship.html)  
|
[description](../../d4/d9d/classautomotive__design_1_1product__definition__relationship.html#a42164bd70dc59ddf47bda80a46cf035a)  
|
[id](../../d4/d9d/classautomotive__design_1_1product__definition__relationship.html#aded7c551700791620e185b73ac3dabaa)  
|
[name](../../d4/d9d/classautomotive__design_1_1product__definition__relationship.html#ae895328775ad0a6e909641acf70cfa35)  
|
[related_product_definition](../../d4/d9d/classautomotive__design_1_1product__definition__relationship.html#a68913ee57e66da588d2efc47a0eef813)  
|
[relating_product_definition](../../d4/d9d/classautomotive__design_1_1product__definition__relationship.html#a629db485b95eb8e6a39f2f0f2e164e2f)  
  
## Detailed Description

    
    
    Entity make_from_usage_option definition.
    
        :param ranking
        :type ranking:INTEGER
    
        :param ranking_rationale
        :type ranking_rationale:text
    
        :param quantity
        :type quantity:measure_with_unit

## Member Function Documentation

## ◆ quantity()

def automotive_design.make_from_usage_option.quantity  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.quantified_assembly_component_usage._quantity,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.make_from_usage_option._quantity,
automotive_design.quantified_assembly_component_usage._quantity,
automotive_design.make_from_usage_option._quantity, and
config_control_design.quantified_assembly_component_usage._quantity.

Referenced by
[automotive_design.quantified_assembly_component_usage.wr1()](../../d5/d9b/classautomotive__design_1_1quantified__assembly__component__usage.html#aed6cc3626acff4dc91ea150e4b3ddc3a),
and
[automotive_design.make_from_usage_option.wr1()](../../d9/d86/classautomotive__design_1_1make__from__usage__option.html#a32bfd0779e9f4db34925c1de0d9bf66a).

## ◆ ranking()

def automotive_design.make_from_usage_option.ranking  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.make_from_usage_option._ranking,
and automotive_design.make_from_usage_option._ranking.

## ◆ ranking_rationale()

def automotive_design.make_from_usage_option.ranking_rationale  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.make_from_usage_option._ranking_rationale,
and automotive_design.make_from_usage_option._ranking_rationale.

## ◆ wr1()

def automotive_design.make_from_usage_option.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.product_definition_usage](../../d6/d51/classautomotive__design_1_1product__definition__usage.html#a1b9a87b051e6f8f5626be517305ba14a).

References App::UnitExpression.quantity,
[App::ExpressionParser::semantic_type.quantity](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html#a7e78033f7fd4478c5b67f625c5fa9e4f),
[Gui::InputField.quantity](../../da/dfa/classGui_1_1InputField.html#a3e5b432e88f74cd8143c2d7f7c445dc6),
[Gui::QuantitySpinBoxPrivate.quantity](../../dd/d08/classGui_1_1QuantitySpinBoxPrivate.html#ac2ba4110d3210f9c2f7cb5cbe99fcf55),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.quantified_assembly_component_usage.quantity,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.make_from_usage_option.quantity,
[automotive_design.quantified_assembly_component_usage.quantity](../../d5/d9b/classautomotive__design_1_1quantified__assembly__component__usage.html#a3888b5d46915cb7456bdd5bfc0f82775),
[automotive_design.make_from_usage_option.quantity](../../d9/d86/classautomotive__design_1_1make__from__usage__option.html#a61d0c809c0ea261082a2ea623c73ec98),
[config_control_design.quantified_assembly_component_usage.quantity](../../db/d30/classconfig__control__design_1_1quantified__assembly__component__usage.html#aaac32fa5d91e4dc82f33b7f4abbfe777),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.measure_with_unit.value_component,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.value_representation_item.value_component,
[automotive_design.measure_with_unit.value_component](../../db/d66/classautomotive__design_1_1measure__with__unit.html#a6a36286bc2dcf141ac26006e93b8d59b),
[automotive_design.value_representation_item.value_component](../../d3/da7/classautomotive__design_1_1value__representation__item.html#af3ad8e6f86fac9a9bcca8f9c923ddfd7),
and
[config_control_design.measure_with_unit.value_component](../../d7/d6d/classconfig__control__design_1_1measure__with__unit.html#ab07ae804801ef56357725e86474a1666).

## Member Data Documentation

## ◆ quantity

automotive_design.make_from_usage_option.quantity  
---  
  
Referenced by
[automotive_design.quantified_assembly_component_usage.wr1()](../../d5/d9b/classautomotive__design_1_1quantified__assembly__component__usage.html#aed6cc3626acff4dc91ea150e4b3ddc3a),
and
[automotive_design.make_from_usage_option.wr1()](../../d9/d86/classautomotive__design_1_1make__from__usage__option.html#a32bfd0779e9f4db34925c1de0d9bf66a).

## ◆ ranking

automotive_design.make_from_usage_option.ranking  
---  
  
## ◆ ranking_rationale

automotive_design.make_from_usage_option.ranking_rationale  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

