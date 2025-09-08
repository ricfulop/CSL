---
url: https://freecad.github.io/SourceDoc/d3/d7e/classconfig__control__design_1_1toroidal__surface.html
scraped_at: 2025-09-08T15:24:18.857132
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [toroidal_surface](../../d3/d7e/classconfig__control__design_1_1toroidal__surface.html)

[List of all members](../../da/d6d/classconfig__control__design_1_1toroidal__surface-members.html) | Public Member Functions | Public Attributes

config_control_design.toroidal_surface Class Reference

##  Public Member Functions  
  
---  
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

    
    
    Entity toroidal_surface definition.
    
        :param major_radius
        :type major_radius:positive_length_measure
    
        :param minor_radius
        :type minor_radius:positive_length_measure

## Member Function Documentation

## ◆ major_radius()

def config_control_design.toroidal_surface.major_radius  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.toroidal_surface._major_radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.torus._major_radius,
automotive_design.toroidal_surface._major_radius,
automotive_design.torus._major_radius, and
config_control_design.toroidal_surface._major_radius.

Referenced by
[automotive_design.degenerate_toroidal_surface.wr1()](../../dc/d6e/classautomotive__design_1_1degenerate__toroidal__surface.html#ada91d37d93ce419c3d1e1cd1c372cef7),
[automotive_design.torus.wr1()](../../d1/dba/classautomotive__design_1_1torus.html#ae9a9ef7a7e5e4b865d2a9c3d1ed450bd),
and
[config_control_design.degenerate_toroidal_surface.wr1()](../../df/dad/classconfig__control__design_1_1degenerate__toroidal__surface.html#ace3808e03b5d62b58c8b281839737b57).

## ◆ minor_radius()

def config_control_design.toroidal_surface.minor_radius  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.toroidal_surface._minor_radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.torus._minor_radius,
automotive_design.toroidal_surface._minor_radius,
automotive_design.torus._minor_radius, and
config_control_design.toroidal_surface._minor_radius.

Referenced by
[automotive_design.degenerate_toroidal_surface.wr1()](../../dc/d6e/classautomotive__design_1_1degenerate__toroidal__surface.html#ada91d37d93ce419c3d1e1cd1c372cef7),
[automotive_design.torus.wr1()](../../d1/dba/classautomotive__design_1_1torus.html#ae9a9ef7a7e5e4b865d2a9c3d1ed450bd),
and
[config_control_design.degenerate_toroidal_surface.wr1()](../../df/dad/classconfig__control__design_1_1degenerate__toroidal__surface.html#ace3808e03b5d62b58c8b281839737b57).

## Member Data Documentation

## ◆ major_radius

config_control_design.toroidal_surface.major_radius  
---  
  
Referenced by
[automotive_design.degenerate_toroidal_surface.wr1()](../../dc/d6e/classautomotive__design_1_1degenerate__toroidal__surface.html#ada91d37d93ce419c3d1e1cd1c372cef7),
[automotive_design.torus.wr1()](../../d1/dba/classautomotive__design_1_1torus.html#ae9a9ef7a7e5e4b865d2a9c3d1ed450bd),
and
[config_control_design.degenerate_toroidal_surface.wr1()](../../df/dad/classconfig__control__design_1_1degenerate__toroidal__surface.html#ace3808e03b5d62b58c8b281839737b57).

## ◆ minor_radius

config_control_design.toroidal_surface.minor_radius  
---  
  
Referenced by
[automotive_design.degenerate_toroidal_surface.wr1()](../../dc/d6e/classautomotive__design_1_1degenerate__toroidal__surface.html#ada91d37d93ce419c3d1e1cd1c372cef7),
[automotive_design.torus.wr1()](../../d1/dba/classautomotive__design_1_1torus.html#ae9a9ef7a7e5e4b865d2a9c3d1ed450bd),
and
[config_control_design.degenerate_toroidal_surface.wr1()](../../df/dad/classconfig__control__design_1_1degenerate__toroidal__surface.html#ace3808e03b5d62b58c8b281839737b57).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

