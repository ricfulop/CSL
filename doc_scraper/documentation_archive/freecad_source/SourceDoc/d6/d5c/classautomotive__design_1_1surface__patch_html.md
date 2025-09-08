---
url: https://freecad.github.io/SourceDoc/d6/d5c/classautomotive__design_1_1surface__patch.html
scraped_at: 2025-09-08T15:13:33.132635
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [surface_patch](../../d6/d5c/classautomotive__design_1_1surface__patch.html)

[List of all members](../../d8/dda/classautomotive__design_1_1surface__patch-members.html) | Public Member Functions | Public Attributes

automotive_design.surface_patch Class Reference

##  Public Member Functions  
  
---  
def | [parent_surface](../../d6/d5c/classautomotive__design_1_1surface__patch.html#a013bec3556c75aea906f86715d210081) ()  
def | [u_sense](../../d6/d5c/classautomotive__design_1_1surface__patch.html#a60aeceebfcc4c01e87bc29b886c6f8ec) ()  
def | [u_transition](../../d6/d5c/classautomotive__design_1_1surface__patch.html#a3b49c5b72dd821f8629e743e0313ea80) ()  
def | [using_surfaces](../../d6/d5c/classautomotive__design_1_1surface__patch.html#a3a9dc3097c6b1b1d32665a3ab3a2a6dc) ()  
def | [v_sense](../../d6/d5c/classautomotive__design_1_1surface__patch.html#a6a413a4ba90a88a8fd638a3ab79a0df8) ()  
def | [v_transition](../../d6/d5c/classautomotive__design_1_1surface__patch.html#a5908f745c9c57aeec0bc374c6590c7d3) ()  
def | [wr1](../../d6/d5c/classautomotive__design_1_1surface__patch.html#a92d8eabe436aad643e3e71cff32af6da) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.founded_item](../../d4/d12/classautomotive__design_1_1founded__item.html)  
def | [users](../../d4/d12/classautomotive__design_1_1founded__item.html#a0299c3fccdb8223cc8c9f590f7cee9a5) ()  
def | [wr1](../../d4/d12/classautomotive__design_1_1founded__item.html#a0668b2127d1c208daa93b2d435855a7f) (self)  
def | [wr2](../../d4/d12/classautomotive__design_1_1founded__item.html#a1ef4a4f4c94d46b616c25ec02609838f) (self)  
  
##  Public Attributes  
  
---  
|
[parent_surface](../../d6/d5c/classautomotive__design_1_1surface__patch.html#a7a7f65381c66ea5826129479e9c07f01)  
|
[u_sense](../../d6/d5c/classautomotive__design_1_1surface__patch.html#a7c106b4df3768efc7329fc4b59b896fe)  
|
[u_transition](../../d6/d5c/classautomotive__design_1_1surface__patch.html#a711bf46cf785d602c9a46ac4c8ce148b)  
|
[v_sense](../../d6/d5c/classautomotive__design_1_1surface__patch.html#a25b4148150c67b3994411b96a3d1ddad)  
|
[v_transition](../../d6/d5c/classautomotive__design_1_1surface__patch.html#ae39af6064c113b86f1dd673a0ebba34c)  
  
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

def automotive_design.surface_patch.parent_surface  | ( | | ) |   
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

def automotive_design.surface_patch.u_sense  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_patch._u_sense,
automotive_design.surface_patch._u_sense, and
config_control_design.surface_patch._u_sense.

## ◆ u_transition()

def automotive_design.surface_patch.u_transition  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_patch._u_transition,
automotive_design.surface_patch._u_transition, and
config_control_design.surface_patch._u_transition.

## ◆ using_surfaces()

def automotive_design.surface_patch.using_surfaces  | ( | | ) |   
---|---|---|---|---  
  
## ◆ v_sense()

def automotive_design.surface_patch.v_sense  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_patch._v_sense,
automotive_design.surface_patch._v_sense, and
config_control_design.surface_patch._v_sense.

## ◆ v_transition()

def automotive_design.surface_patch.v_transition  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_patch._v_transition,
automotive_design.surface_patch._v_transition, and
config_control_design.surface_patch._v_transition.

## ◆ wr1()

def automotive_design.surface_patch.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.founded_item](../../d4/d12/classautomotive__design_1_1founded__item.html#a0668b2127d1c208daa93b2d435855a7f).

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

automotive_design.surface_patch.parent_surface  
---  
  
Referenced by
[automotive_design.surface_patch.wr1()](../../d6/d5c/classautomotive__design_1_1surface__patch.html#a92d8eabe436aad643e3e71cff32af6da),
[automotive_design.surface_replica.wr1()](../../dc/d81/classautomotive__design_1_1surface__replica.html#a812129187669585b95025f0018804056),
[config_control_design.surface_patch.wr1()](../../d6/d69/classconfig__control__design_1_1surface__patch.html#a8a73245fa60e5740cf5d29f26dcf8c4d),
and
[config_control_design.surface_replica.wr1()](../../d5/d47/classconfig__control__design_1_1surface__replica.html#a1f82b4551b739b2e449d70bf30032d9b).

## ◆ u_sense

automotive_design.surface_patch.u_sense  
---  
  
## ◆ u_transition

automotive_design.surface_patch.u_transition  
---  
  
## ◆ v_sense

automotive_design.surface_patch.v_sense  
---  
  
## ◆ v_transition

automotive_design.surface_patch.v_transition  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

