---
url: https://freecad.github.io/SourceDoc/d6/d69/classconfig__control__design_1_1surface__patch.html
scraped_at: 2025-09-08T15:24:13.907507
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [surface_patch](../../d6/d69/classconfig__control__design_1_1surface__patch.html)

[List of all members](../../d3/d78/classconfig__control__design_1_1surface__patch-members.html) | Public Member Functions | Public Attributes

config_control_design.surface_patch Class Reference

##  Public Member Functions  
  
---  
def | [parent_surface](../../d6/d69/classconfig__control__design_1_1surface__patch.html#a575d98295efe7031b246b91eb99859a8) ()  
def | [u_sense](../../d6/d69/classconfig__control__design_1_1surface__patch.html#a3bbde14a16bca1bbef6ffe266cbc1609) ()  
def | [u_transition](../../d6/d69/classconfig__control__design_1_1surface__patch.html#a94534a4f06822188b0551ba20b03d6c1) ()  
def | [using_surfaces](../../d6/d69/classconfig__control__design_1_1surface__patch.html#a07eae0a4b8a2db66b77cd1ce744447ad) ()  
def | [v_sense](../../d6/d69/classconfig__control__design_1_1surface__patch.html#ad3cfc89a47ffc2ed6ecc33a91e2821b0) ()  
def | [v_transition](../../d6/d69/classconfig__control__design_1_1surface__patch.html#a9a0756a2fdb1d15f61b4e1f1cd302fdf) ()  
def | [wr1](../../d6/d69/classconfig__control__design_1_1surface__patch.html#a8a73245fa60e5740cf5d29f26dcf8c4d) (self)  
  
##  Public Attributes  
  
---  
|
[parent_surface](../../d6/d69/classconfig__control__design_1_1surface__patch.html#aefbf09b851a0ea38fb9dc80344003f6f)  
|
[u_sense](../../d6/d69/classconfig__control__design_1_1surface__patch.html#a46ba3d7b4a24e6d2b4ca0725ef0a62a3)  
|
[u_transition](../../d6/d69/classconfig__control__design_1_1surface__patch.html#a51b952c6f099448b495eef3fa7aa6acd)  
|
[v_sense](../../d6/d69/classconfig__control__design_1_1surface__patch.html#a742744fae3b8cdff30525008d28f9760)  
|
[v_transition](../../d6/d69/classconfig__control__design_1_1surface__patch.html#a4bf674db7b687d3972a1aef6311b4611)  
  
## Detailed Description

    
    
    Entity surface_patch definition.
    
        :param parent_surface
        :type parent_surface:bounded_surface
    
        :param u_transition
        :type u_transition:transition_code
    
        :param v_transition
        :type v_transition:transition_code
    
        :param u_sense
        :type u_sense:BOOLEAN
    
        :param v_sense
        :type v_sense:BOOLEAN
    
        :param using_surfaces
        :type using_surfaces:BAG(1,None,'rectangular_composite_surface', scope = schema_scope)

## Member Function Documentation

## ◆ parent_surface()

def config_control_design.surface_patch.parent_surface  | ( | | ) |   
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

## ◆ u_sense()

def config_control_design.surface_patch.u_sense  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_patch._u_sense,
automotive_design.surface_patch._u_sense, and
config_control_design.surface_patch._u_sense.

## ◆ u_transition()

def config_control_design.surface_patch.u_transition  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_patch._u_transition,
automotive_design.surface_patch._u_transition, and
config_control_design.surface_patch._u_transition.

## ◆ using_surfaces()

def config_control_design.surface_patch.using_surfaces  | ( | | ) |   
---|---|---|---|---  
  
## ◆ v_sense()

def config_control_design.surface_patch.v_sense  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_patch._v_sense,
automotive_design.surface_patch._v_sense, and
config_control_design.surface_patch._v_sense.

## ◆ v_transition()

def config_control_design.surface_patch.v_transition  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_patch._v_transition,
automotive_design.surface_patch._v_transition, and
config_control_design.surface_patch._v_transition.

## ◆ wr1()

def config_control_design.surface_patch.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_patch.parent_surface,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_replica.parent_surface,
[automotive_design.surface_patch.parent_surface](../../d6/d5c/classautomotive__design_1_1surface__patch.html#a7a7f65381c66ea5826129479e9c07f01),
[automotive_design.surface_replica.parent_surface](../../dc/d81/classautomotive__design_1_1surface__replica.html#a500c51ae7ee373a8013b71e82d46dad2),
[config_control_design.surface_patch.parent_surface](../../d6/d69/classconfig__control__design_1_1surface__patch.html#aefbf09b851a0ea38fb9dc80344003f6f),
and
[config_control_design.surface_replica.parent_surface](../../d5/d47/classconfig__control__design_1_1surface__replica.html#af73c8cb56c14ddd318a6e2794c40bf0f).

## Member Data Documentation

## ◆ parent_surface

config_control_design.surface_patch.parent_surface  
---  
  
Referenced by
[automotive_design.surface_patch.wr1()](../../d6/d5c/classautomotive__design_1_1surface__patch.html#a92d8eabe436aad643e3e71cff32af6da),
[automotive_design.surface_replica.wr1()](../../dc/d81/classautomotive__design_1_1surface__replica.html#a812129187669585b95025f0018804056),
[config_control_design.surface_patch.wr1()](../../d6/d69/classconfig__control__design_1_1surface__patch.html#a8a73245fa60e5740cf5d29f26dcf8c4d),
and
[config_control_design.surface_replica.wr1()](../../d5/d47/classconfig__control__design_1_1surface__replica.html#a1f82b4551b739b2e449d70bf30032d9b).

## ◆ u_sense

config_control_design.surface_patch.u_sense  
---  
  
## ◆ u_transition

config_control_design.surface_patch.u_transition  
---  
  
## ◆ v_sense

config_control_design.surface_patch.v_sense  
---  
  
## ◆ v_transition

config_control_design.surface_patch.v_transition  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

