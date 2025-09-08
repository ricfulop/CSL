---
url: https://freecad.github.io/SourceDoc/df/dad/classconfig__control__design_1_1degenerate__toroidal__surface.html
scraped_at: 2025-09-08T15:21:25.114849
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [degenerate_toroidal_surface](../../df/dad/classconfig__control__design_1_1degenerate__toroidal__surface.html)

[List of all members](../../d4/d39/classconfig__control__design_1_1degenerate__toroidal__surface-members.html) | Public Member Functions | Public Attributes

config_control_design.degenerate_toroidal_surface Class Reference

##  Public Member Functions  
  
---  
def | [select_outer](../../df/dad/classconfig__control__design_1_1degenerate__toroidal__surface.html#a9ba069bc04a89e1cf0d2bbb28902b3ed) ()  
def | [wr1](../../df/dad/classconfig__control__design_1_1degenerate__toroidal__surface.html#ace3808e03b5d62b58c8b281839737b57) (self)  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.toroidal_surface](../../d3/d7e/classconfig__control__design_1_1toroidal__surface.html)  
def | [major_radius](../../d3/d7e/classconfig__control__design_1_1toroidal__surface.html#a1c9d054409e75866e28af5c8d7982e57) ()  
def | [minor_radius](../../d3/d7e/classconfig__control__design_1_1toroidal__surface.html#add516d029d141383054a334a41420790) ()  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.elementary_surface](../../d1/d48/classconfig__control__design_1_1elementary__surface.html)  
def | [position](../../d1/d48/classconfig__control__design_1_1elementary__surface.html#a9c3e462ddcea690d63e805d417fe1adc) ()  
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
[select_outer](../../df/dad/classconfig__control__design_1_1degenerate__toroidal__surface.html#aff66397ae465b8576c255081fead6036)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.toroidal_surface](../../d3/d7e/classconfig__control__design_1_1toroidal__surface.html)  
|
[major_radius](../../d3/d7e/classconfig__control__design_1_1toroidal__surface.html#a78b546623eb8a989a8ae636b6c09a9e9)  
|
[minor_radius](../../d3/d7e/classconfig__control__design_1_1toroidal__surface.html#aaab59ff146369decf339d46680d2e8ab)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.elementary_surface](../../d1/d48/classconfig__control__design_1_1elementary__surface.html)  
|
[position](../../d1/d48/classconfig__control__design_1_1elementary__surface.html#a6c61fb6f8f3e65f2afad3b47ad97afd9)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
|
[name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a0e8be677f8410825a46422f3c0e1c128)  
  
## Detailed Description

    
    
    Entity degenerate_toroidal_surface definition.
    
        :param select_outer
        :type select_outer:BOOLEAN

## Member Function Documentation

## ◆ select_outer()

def config_control_design.degenerate_toroidal_surface.select_outer  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.degenerate_toroidal_surface._select_outer,
automotive_design.degenerate_toroidal_surface._select_outer, and
config_control_design.degenerate_toroidal_surface._select_outer.

## ◆ wr1()

def config_control_design.degenerate_toroidal_surface.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[config_control_design.geometric_representation_item](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html#a779ebde9495ea4132b585e06aa418f13).

References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.toroidal_surface.major_radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.torus.major_radius,
[automotive_design.toroidal_surface.major_radius](../../dd/daf/classautomotive__design_1_1toroidal__surface.html#a49c468b596d4042fc69d35d3da9a26e0),
[automotive_design.torus.major_radius](../../d1/dba/classautomotive__design_1_1torus.html#a5907f2a419aea80d1863ee1fa5d26ed8),
[config_control_design.toroidal_surface.major_radius](../../d3/d7e/classconfig__control__design_1_1toroidal__surface.html#a78b546623eb8a989a8ae636b6c09a9e9),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.toroidal_surface.minor_radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.torus.minor_radius,
[automotive_design.toroidal_surface.minor_radius](../../dd/daf/classautomotive__design_1_1toroidal__surface.html#a867d306837362228ad9f822d18fb448d),
[automotive_design.torus.minor_radius](../../d1/dba/classautomotive__design_1_1torus.html#a967d95189338f94dc03c429f307013fd),
and
[config_control_design.toroidal_surface.minor_radius](../../d3/d7e/classconfig__control__design_1_1toroidal__surface.html#aaab59ff146369decf339d46680d2e8ab).

## Member Data Documentation

## ◆ select_outer

config_control_design.degenerate_toroidal_surface.select_outer  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

