---
url: https://freecad.github.io/SourceDoc/d8/d45/classconfig__control__design_1_1person.html
scraped_at: 2025-09-08T15:22:50.527637
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [person](../../d8/d45/classconfig__control__design_1_1person.html)

[List of all members](../../d3/d94/classconfig__control__design_1_1person-members.html) | Public Member Functions | Public Attributes

config_control_design.person Class Reference

##  Public Member Functions  
  
---  
def | [first_name](../../d8/d45/classconfig__control__design_1_1person.html#ac593d47d852cc8d4812ef0646335c448) ()  
def | [id](../../d8/d45/classconfig__control__design_1_1person.html#ac308c5e75567cd86d2a1acdc8d6c2493) ()  
def | [last_name](../../d8/d45/classconfig__control__design_1_1person.html#afa981e96745e47062c2852fb7f4d4ca2) ()  
def | [middle_names](../../d8/d45/classconfig__control__design_1_1person.html#a181e37b2bfe69b6c210cfef79bfe33b3) ()  
def | [prefix_titles](../../d8/d45/classconfig__control__design_1_1person.html#af5b82b4b7cf7dd3fb6c3dfe101fe777b) ()  
def | [suffix_titles](../../d8/d45/classconfig__control__design_1_1person.html#abc2001163710469ad156af035c1becfc) ()  
def | [wr1](../../d8/d45/classconfig__control__design_1_1person.html#a55f69c65f23a84c2eef68a55f0e7a4dd) (self)  
  
##  Public Attributes  
  
---  
|
[first_name](../../d8/d45/classconfig__control__design_1_1person.html#ad7b52514d2ae1f338fbc7a7092637355)  
|
[id](../../d8/d45/classconfig__control__design_1_1person.html#aebfdc7e24e8e1017eafb0e83ff6ee594)  
|
[last_name](../../d8/d45/classconfig__control__design_1_1person.html#a5863b1c03cdce3eb877695c47034c639)  
|
[middle_names](../../d8/d45/classconfig__control__design_1_1person.html#a8106336c436a7fce1e874bc01f80f5d6)  
|
[prefix_titles](../../d8/d45/classconfig__control__design_1_1person.html#a9bc13f1e24288994e2acf5da7ead0e75)  
|
[suffix_titles](../../d8/d45/classconfig__control__design_1_1person.html#aef5f7ec62819c9147096c8305dd85e05)  
  
## Detailed Description

    
    
    Entity person definition.
    
        :param id
        :type id:identifier
    
        :param last_name
        :type last_name:label
    
        :param first_name
        :type first_name:label
    
        :param middle_names
        :type middle_names:LIST(1,None,'STRING', scope = schema_scope)
    
        :param prefix_titles
        :type prefix_titles:LIST(1,None,'STRING', scope = schema_scope)
    
        :param suffix_titles
        :type suffix_titles:LIST(1,None,'STRING', scope = schema_scope)

## Member Function Documentation

## ◆ first_name()

def config_control_design.person.first_name  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.person._first_name,
automotive_design.person._first_name, and
config_control_design.person._first_name.

Referenced by
[automotive_design.person.wr1()](../../db/d97/classautomotive__design_1_1person.html#a55b680f57ef89bfd3875c4cabbd9f679),
and
[config_control_design.person.wr1()](../../d8/d45/classconfig__control__design_1_1person.html#a55f69c65f23a84c2eef68a55f0e7a4dd).

## ◆ id()

def config_control_design.person.id  | ( | | ) |   
---|---|---|---|---  
  
References SMESH_Mesh._id, App::Property._id,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.versioned_action_request._id,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.general_property._id,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.product_definition_relationship._id,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.time_interval._id,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.effectivity._id,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.product_definition._id,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.product_concept._id,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.product_definition_formation_relationship._id,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.person._id,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.product_definition_formation._id,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.event_occurrence._id,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.configuration_item._id,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.contract_relationship._id,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.product_concept_feature._id,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.text_font_family._id,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.document._id,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.text_font._id,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.product._id,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.organization._id,
automotive_design.versioned_action_request._id,
automotive_design.product_definition_relationship._id,
automotive_design.product_definition._id, automotive_design.time_interval._id,
automotive_design.effectivity._id, automotive_design.general_property._id,
automotive_design.product_concept._id,
automotive_design.product_definition_formation_relationship._id,
automotive_design.person._id,
automotive_design.product_definition_formation._id,
automotive_design.event_occurrence._id,
automotive_design.configuration_item._id,
automotive_design.product_concept_feature._id, automotive_design.document._id,
automotive_design.versioned_action_request_relationship._id,
automotive_design.product._id, automotive_design.organization._id,
config_control_design.versioned_action_request._id,
config_control_design.product_definition_relationship._id,
config_control_design.effectivity._id, config_control_design.person._id,
config_control_design.document._id,
config_control_design.product_definition_formation._id,
config_control_design.configuration_item._id,
config_control_design.product._id, config_control_design.product_concept._id,
config_control_design.product_definition._id,
config_control_design.organization._id, ifc2x3.ifcorganization._id,
ifc2x3.ifcperson._id, ifc2x3.ifccostschedule._id, and
ifc2x3.ifcprojectorder._id.

## ◆ last_name()

def config_control_design.person.last_name  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.person._last_name,
automotive_design.person._last_name, and
config_control_design.person._last_name.

Referenced by
[automotive_design.person.wr1()](../../db/d97/classautomotive__design_1_1person.html#a55b680f57ef89bfd3875c4cabbd9f679),
and
[config_control_design.person.wr1()](../../d8/d45/classconfig__control__design_1_1person.html#a55f69c65f23a84c2eef68a55f0e7a4dd).

## ◆ middle_names()

def config_control_design.person.middle_names  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.person._middle_names,
automotive_design.person._middle_names, and
config_control_design.person._middle_names.

## ◆ prefix_titles()

def config_control_design.person.prefix_titles  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.person._prefix_titles,
automotive_design.person._prefix_titles, and
config_control_design.person._prefix_titles.

## ◆ suffix_titles()

def config_control_design.person.suffix_titles  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.person._suffix_titles,
automotive_design.person._suffix_titles, and
config_control_design.person._suffix_titles.

## ◆ wr1()

def config_control_design.person.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.person.first_name,
[automotive_design.person.first_name](../../db/d97/classautomotive__design_1_1person.html#ab7666ebda9f8aace40090c443659cd68),
[config_control_design.person.first_name](../../d8/d45/classconfig__control__design_1_1person.html#ad7b52514d2ae1f338fbc7a7092637355),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.person.last_name,
[automotive_design.person.last_name](../../db/d97/classautomotive__design_1_1person.html#ab1e80f16228b5eb735b75f42975e762d),
and
[config_control_design.person.last_name](../../d8/d45/classconfig__control__design_1_1person.html#a5863b1c03cdce3eb877695c47034c639).

## Member Data Documentation

## ◆ first_name

config_control_design.person.first_name  
---  
  
Referenced by
[automotive_design.person.wr1()](../../db/d97/classautomotive__design_1_1person.html#a55b680f57ef89bfd3875c4cabbd9f679),
and
[config_control_design.person.wr1()](../../d8/d45/classconfig__control__design_1_1person.html#a55f69c65f23a84c2eef68a55f0e7a4dd).

## ◆ id

config_control_design.person.id  
---  
  
## ◆ last_name

config_control_design.person.last_name  
---  
  
Referenced by
[automotive_design.person.wr1()](../../db/d97/classautomotive__design_1_1person.html#a55b680f57ef89bfd3875c4cabbd9f679),
and
[config_control_design.person.wr1()](../../d8/d45/classconfig__control__design_1_1person.html#a55f69c65f23a84c2eef68a55f0e7a4dd).

## ◆ middle_names

config_control_design.person.middle_names  
---  
  
## ◆ prefix_titles

config_control_design.person.prefix_titles  
---  
  
## ◆ suffix_titles

config_control_design.person.suffix_titles  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

