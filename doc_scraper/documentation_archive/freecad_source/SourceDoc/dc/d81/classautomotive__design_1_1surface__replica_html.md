---
url: https://freecad.github.io/SourceDoc/dc/d81/classautomotive__design_1_1surface__replica.html
scraped_at: 2025-09-08T15:13:36.138045
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [surface_replica](../../dc/d81/classautomotive__design_1_1surface__replica.html)

[List of all members](../../d4/dbc/classautomotive__design_1_1surface__replica-members.html) | Public Member Functions | Public Attributes

automotive_design.surface_replica Class Reference

##  Public Member Functions  
  
---  
def | [parent_surface](../../dc/d81/classautomotive__design_1_1surface__replica.html#a612ba50f8a3cc856c91c5c3e80fee535) ()  
def | [transformation](../../dc/d81/classautomotive__design_1_1surface__replica.html#aabedd62d16ba8afe06ddc3de4e5157ff) ()  
def | [wr1](../../dc/d81/classautomotive__design_1_1surface__replica.html#a812129187669585b95025f0018804056) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.geometric_representation_item](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html)  
def | [dim](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#aef245618450610e88788dcaea46ad742) ()  
def | [wr1](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#a9677d2be5fc5c7c8ccb6819380198bbc) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
def | [name](../../d3/d20/classautomotive__design_1_1representation__item.html#a33b5812d92aa0d107b4fd4274c17b9d9) ()  
def | [wr1](../../d3/d20/classautomotive__design_1_1representation__item.html#af350c19fc5e5763d4991494a99d979ed) (self)  
  
##  Public Attributes  
  
---  
|
[parent_surface](../../dc/d81/classautomotive__design_1_1surface__replica.html#a500c51ae7ee373a8013b71e82d46dad2)  
|
[transformation](../../dc/d81/classautomotive__design_1_1surface__replica.html#abe9d8500a49ca6f28ae192ac5fba23ed)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity surface_replica definition.
    
        :param parent_surface
        :type parent_surface:surface
    
        :param transformation
        :type transformation:cartesian_transformation_operator_3d

## Member Function Documentation

## ◆ parent_surface()

def automotive_design.surface_replica.parent_surface  | ( | | ) |   
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

def automotive_design.surface_replica.transformation  | ( | | ) |   
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

def automotive_design.surface_replica.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.geometric_representation_item](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#a9677d2be5fc5c7c8ccb6819380198bbc).

References
[automotive_design.acyclic_surface_replica()](../../d4/ddf/namespaceautomotive__design.html#ac69fefac2b054edd55e2aa93d0389f42),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_patch.parent_surface,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_replica.parent_surface,
[automotive_design.surface_patch.parent_surface](../../d6/d5c/classautomotive__design_1_1surface__patch.html#a7a7f65381c66ea5826129479e9c07f01),
[automotive_design.surface_replica.parent_surface](../../dc/d81/classautomotive__design_1_1surface__replica.html#a500c51ae7ee373a8013b71e82d46dad2),
[config_control_design.surface_patch.parent_surface](../../d6/d69/classconfig__control__design_1_1surface__patch.html#aefbf09b851a0ea38fb9dc80344003f6f),
and
[config_control_design.surface_replica.parent_surface](../../d5/d47/classconfig__control__design_1_1surface__replica.html#af73c8cb56c14ddd318a6e2794c40bf0f).

## Member Data Documentation

## ◆ parent_surface

automotive_design.surface_replica.parent_surface  
---  
  
Referenced by
[automotive_design.surface_patch.wr1()](../../d6/d5c/classautomotive__design_1_1surface__patch.html#a92d8eabe436aad643e3e71cff32af6da),
[automotive_design.surface_replica.wr1()](../../dc/d81/classautomotive__design_1_1surface__replica.html#a812129187669585b95025f0018804056),
[config_control_design.surface_patch.wr1()](../../d6/d69/classconfig__control__design_1_1surface__patch.html#a8a73245fa60e5740cf5d29f26dcf8c4d),
and
[config_control_design.surface_replica.wr1()](../../d5/d47/classconfig__control__design_1_1surface__replica.html#a1f82b4551b739b2e449d70bf30032d9b).

## ◆ transformation

automotive_design.surface_replica.transformation  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

