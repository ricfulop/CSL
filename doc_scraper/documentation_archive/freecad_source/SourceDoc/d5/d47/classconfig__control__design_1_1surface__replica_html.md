---
url: https://freecad.github.io/SourceDoc/d5/d47/classconfig__control__design_1_1surface__replica.html
scraped_at: 2025-09-08T15:24:14.856061
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [surface_replica](../../d5/d47/classconfig__control__design_1_1surface__replica.html)

[List of all members](../../df/dbe/classconfig__control__design_1_1surface__replica-members.html) | Public Member Functions | Public Attributes

config_control_design.surface_replica Class Reference

##  Public Member Functions  
  
---  
def | [parent_surface](../../d5/d47/classconfig__control__design_1_1surface__replica.html#a5838d9d1e4b8ef0a8b42c4e01a099aee) ()  
def | [transformation](../../d5/d47/classconfig__control__design_1_1surface__replica.html#abf3b087aa4ad023943b04119cfda6147) ()  
def | [wr1](../../d5/d47/classconfig__control__design_1_1surface__replica.html#a1f82b4551b739b2e449d70bf30032d9b) (self)  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.geometric_representation_item](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html)  
def | [dim](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html#aac385fb99d009b699d0d77f10ebdc5f1) ()  
def | [wr1](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html#a779ebde9495ea4132b585e06aa418f13) (self)  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
def | [name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a5ea878073c85170f328deff23a9c5732) ()  
def | [wr1](../../d9/d69/classconfig__control__design_1_1representation__item.html#a4cdc1db49341dedc8f271ec89801c713) (self)  
  
##  Public Attributes  
  
---  
|
[parent_surface](../../d5/d47/classconfig__control__design_1_1surface__replica.html#af73c8cb56c14ddd318a6e2794c40bf0f)  
|
[transformation](../../d5/d47/classconfig__control__design_1_1surface__replica.html#ab8862df758fcbce7a5a68e95c461cf75)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
|
[name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a0e8be677f8410825a46422f3c0e1c128)  
  
## Detailed Description

    
    
    Entity surface_replica definition.
    
        :param parent_surface
        :type parent_surface:surface
    
        :param transformation
        :type transformation:cartesian_transformation_operator_3d

## Member Function Documentation

## ◆ parent_surface()

def config_control_design.surface_replica.parent_surface  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_patch._parent_surface,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_replica._parent_surface,
automotive_design.surface_patch._parent_surface,
automotive_design.surface_replica._parent_surface,
config_control_design.surface_patch._parent_surface, and
config_control_design.surface_replica._parent_surface.

Referenced by
[automotive_design.surface_patch.wr1()](../../d6/d5c/classautomotive__design_1_1surface__patch.html#a92d8eabe436aad643e3e71cff32af6da),
[automotive_design.surface_replica.wr1()](../../dc/d81/classautomotive__design_1_1surface__replica.html#a812129187669585b95025f0018804056),
[config_control_design.surface_patch.wr1()](../../d6/d69/classconfig__control__design_1_1surface__patch.html#a8a73245fa60e5740cf5d29f26dcf8c4d),
and
[config_control_design.surface_replica.wr1()](../../d5/d47/classconfig__control__design_1_1surface__replica.html#a1f82b4551b739b2e449d70bf30032d9b).

## ◆ transformation()

def config_control_design.surface_replica.transformation  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.curve_replica._transformation,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.point_replica._transformation,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_replica._transformation,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.solid_replica._transformation,
automotive_design.curve_replica._transformation,
automotive_design.point_replica._transformation,
automotive_design.surface_replica._transformation,
automotive_design.solid_replica._transformation,
config_control_design.curve_replica._transformation,
config_control_design.point_replica._transformation, and
config_control_design.surface_replica._transformation.

## ◆ wr1()

def config_control_design.surface_replica.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[config_control_design.geometric_representation_item](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html#a779ebde9495ea4132b585e06aa418f13).

References
[config_control_design.acyclic_surface_replica()](../../d4/d07/namespaceconfig__control__design.html#a49283f0fb899d5f714375ac8e272a0e5),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_patch.parent_surface,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_replica.parent_surface,
[automotive_design.surface_patch.parent_surface](../../d6/d5c/classautomotive__design_1_1surface__patch.html#a7a7f65381c66ea5826129479e9c07f01),
[automotive_design.surface_replica.parent_surface](../../dc/d81/classautomotive__design_1_1surface__replica.html#a500c51ae7ee373a8013b71e82d46dad2),
[config_control_design.surface_patch.parent_surface](../../d6/d69/classconfig__control__design_1_1surface__patch.html#aefbf09b851a0ea38fb9dc80344003f6f),
and
[config_control_design.surface_replica.parent_surface](../../d5/d47/classconfig__control__design_1_1surface__replica.html#af73c8cb56c14ddd318a6e2794c40bf0f).

## Member Data Documentation

## ◆ parent_surface

config_control_design.surface_replica.parent_surface  
---  
  
Referenced by
[automotive_design.surface_patch.wr1()](../../d6/d5c/classautomotive__design_1_1surface__patch.html#a92d8eabe436aad643e3e71cff32af6da),
[automotive_design.surface_replica.wr1()](../../dc/d81/classautomotive__design_1_1surface__replica.html#a812129187669585b95025f0018804056),
[config_control_design.surface_patch.wr1()](../../d6/d69/classconfig__control__design_1_1surface__patch.html#a8a73245fa60e5740cf5d29f26dcf8c4d),
and
[config_control_design.surface_replica.wr1()](../../d5/d47/classconfig__control__design_1_1surface__replica.html#a1f82b4551b739b2e449d70bf30032d9b).

## ◆ transformation

config_control_design.surface_replica.transformation  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

