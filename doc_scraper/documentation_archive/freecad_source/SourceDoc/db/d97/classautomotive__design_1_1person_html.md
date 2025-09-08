---
url: https://freecad.github.io/SourceDoc/db/d97/classautomotive__design_1_1person.html
scraped_at: 2025-09-08T15:09:20.065549
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [person](../../db/d97/classautomotive__design_1_1person.html)

[List of all members](../../d6/d0e/classautomotive__design_1_1person-members.html) | Public Member Functions | Public Attributes

automotive_design.person Class Reference

##  Public Member Functions  
  
---  
def | [first_name](../../db/d97/classautomotive__design_1_1person.html#a7772fb4e5121d0f0b4545ec6d0abd167) ()  
def | [id](../../db/d97/classautomotive__design_1_1person.html#a52ae71bc105f8588d647f74a27bdd19d) ()  
def | [last_name](../../db/d97/classautomotive__design_1_1person.html#aca6533c845b44977dda37c6242aacbb0) ()  
def | [middle_names](../../db/d97/classautomotive__design_1_1person.html#a80c008f102fcaccaf43858d574a89ff7) ()  
def | [prefix_titles](../../db/d97/classautomotive__design_1_1person.html#a6f05cfe046f063d568cbd76970b1ce3c) ()  
def | [suffix_titles](../../db/d97/classautomotive__design_1_1person.html#abf123b7b122d20e13b600ddd166ca48d) ()  
def | [wr1](../../db/d97/classautomotive__design_1_1person.html#a55b680f57ef89bfd3875c4cabbd9f679) (self)  
  
##  Public Attributes  
  
---  
|
[first_name](../../db/d97/classautomotive__design_1_1person.html#ab7666ebda9f8aace40090c443659cd68)  
|
[id](../../db/d97/classautomotive__design_1_1person.html#a75e9684d11fd202c1384a617d120b041)  
|
[last_name](../../db/d97/classautomotive__design_1_1person.html#ab1e80f16228b5eb735b75f42975e762d)  
|
[middle_names](../../db/d97/classautomotive__design_1_1person.html#a2a16076184e1b53d13d01bb30b800bfd)  
|
[prefix_titles](../../db/d97/classautomotive__design_1_1person.html#aabec09d3e8257b0deadb1c8c2a33b543)  
|
[suffix_titles](../../db/d97/classautomotive__design_1_1person.html#a619f00e48b1a606deb133b4d7c5195fd)  
  
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

def automotive_design.person.first_name  | ( | | ) |   
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

def automotive_design.person.id  | ( | | ) |   
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

def automotive_design.person.last_name  | ( | | ) |   
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

def automotive_design.person.middle_names  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.person._middle_names,
automotive_design.person._middle_names, and
config_control_design.person._middle_names.

## ◆ prefix_titles()

def automotive_design.person.prefix_titles  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.person._prefix_titles,
automotive_design.person._prefix_titles, and
config_control_design.person._prefix_titles.

## ◆ suffix_titles()

def automotive_design.person.suffix_titles  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.person._suffix_titles,
automotive_design.person._suffix_titles, and
config_control_design.person._suffix_titles.

## ◆ wr1()

def automotive_design.person.wr1  | ( |  | _self_| ) |   
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

automotive_design.person.first_name  
---  
  
Referenced by
[automotive_design.person.wr1()](../../db/d97/classautomotive__design_1_1person.html#a55b680f57ef89bfd3875c4cabbd9f679),
and
[config_control_design.person.wr1()](../../d8/d45/classconfig__control__design_1_1person.html#a55f69c65f23a84c2eef68a55f0e7a4dd).

## ◆ id

automotive_design.person.id  
---  
  
## ◆ last_name

automotive_design.person.last_name  
---  
  
Referenced by
[automotive_design.person.wr1()](../../db/d97/classautomotive__design_1_1person.html#a55b680f57ef89bfd3875c4cabbd9f679),
and
[config_control_design.person.wr1()](../../d8/d45/classconfig__control__design_1_1person.html#a55f69c65f23a84c2eef68a55f0e7a4dd).

## ◆ middle_names

automotive_design.person.middle_names  
---  
  
## ◆ prefix_titles

automotive_design.person.prefix_titles  
---  
  
## ◆ suffix_titles

automotive_design.person.suffix_titles  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

