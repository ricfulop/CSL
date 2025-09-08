---
url: https://freecad.github.io/SourceDoc/d4/d2e/classconfig__control__design_1_1face__surface.html
scraped_at: 2025-09-08T15:21:52.237627
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [face_surface](../../d4/d2e/classconfig__control__design_1_1face__surface.html)

[List of all members](../../d7/dd1/classconfig__control__design_1_1face__surface-members.html) | Public Member Functions | Public Attributes

config_control_design.face_surface Class Reference

##  Public Member Functions  
  
---  
def | [face_geometry](../../d4/d2e/classconfig__control__design_1_1face__surface.html#aecfd84870bf3d5f6dab88c9dcd00f915) ()  
def | [same_sense](../../d4/d2e/classconfig__control__design_1_1face__surface.html#a7c7e22b79c38ac91e64e9b72c5a53eab) ()  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.face](../../d3/d78/classconfig__control__design_1_1face.html)  
def | [bounds](../../d3/d78/classconfig__control__design_1_1face.html#a313840aa2d165b012db67959d15aa6d2) ()  
def | [wr1](../../d3/d78/classconfig__control__design_1_1face.html#a047aab57b192ef6ce0bb7924eafc9bd4) (self)  
def | [wr2](../../d3/d78/classconfig__control__design_1_1face.html#ac882f231c3972a4f8938f97eecbf0774) (self)  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
def | [name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a5ea878073c85170f328deff23a9c5732) ()  
def | [wr1](../../d9/d69/classconfig__control__design_1_1representation__item.html#a4cdc1db49341dedc8f271ec89801c713) (self)  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.geometric_representation_item](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html)  
def | [dim](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html#aac385fb99d009b699d0d77f10ebdc5f1) ()  
def | [wr1](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html#a779ebde9495ea4132b585e06aa418f13) (self)  
  
##  Public Attributes  
  
---  
|
[face_geometry](../../d4/d2e/classconfig__control__design_1_1face__surface.html#a04ace46f8dc2e22c7f4a28d267531f6a)  
|
[same_sense](../../d4/d2e/classconfig__control__design_1_1face__surface.html#ac371a30a18be473ae9e3ad7b320f7c24)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.face](../../d3/d78/classconfig__control__design_1_1face.html)  
|
[bounds](../../d3/d78/classconfig__control__design_1_1face.html#acd48bf7a8d0eb03155bb61c39a19cbc8)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
|
[name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a0e8be677f8410825a46422f3c0e1c128)  
  
## Detailed Description

    
    
    Entity face_surface definition.
    
        :param face_geometry
        :type face_geometry:surface
    
        :param same_sense
        :type same_sense:BOOLEAN

## Member Function Documentation

## ◆ face_geometry()

def config_control_design.face_surface.face_geometry  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.face_surface._face_geometry,
automotive_design.face_surface._face_geometry, and
config_control_design.face_surface._face_geometry.

Referenced by
[automotive_design.swept_face_solid.wr1()](../../d1/d64/classautomotive__design_1_1swept__face__solid.html#a6ba90dcc401b0d407dd0ba8128a71e4f),
[automotive_design.face_surface.wr1()](../../df/d6b/classautomotive__design_1_1face__surface.html#ad6c02b269122e6cfaea7b325a76fe6da),
[automotive_design.advanced_face.wr1()](../../d1/d62/classautomotive__design_1_1advanced__face.html#a909cfe9dc6dce7295fc8b058d98be155),
[config_control_design.advanced_face.wr1()](../../db/d65/classconfig__control__design_1_1advanced__face.html#a479a609264b1ca2e70775476f690681e),
[automotive_design.advanced_face.wr10()](../../d1/d62/classautomotive__design_1_1advanced__face.html#aa08adf112660acfb17f4847e837bdf6d),
[config_control_design.advanced_face.wr10()](../../db/d65/classconfig__control__design_1_1advanced__face.html#a0118e22d47858317fa0dff7407854d05),
[automotive_design.advanced_face.wr6()](../../d1/d62/classautomotive__design_1_1advanced__face.html#ac086e0ff8446e94665dadf33064d24c8),
and
[config_control_design.advanced_face.wr6()](../../db/d65/classconfig__control__design_1_1advanced__face.html#a915743fb20126f8a0b1adccf202a429d).

## ◆ same_sense()

def config_control_design.face_surface.same_sense  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.composite_curve_segment._same_sense,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.face_surface._same_sense,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.edge_curve._same_sense,
automotive_design.composite_curve_segment._same_sense,
automotive_design.face_surface._same_sense,
automotive_design.edge_curve._same_sense,
config_control_design.composite_curve_segment._same_sense,
config_control_design.face_surface._same_sense, and
config_control_design.edge_curve._same_sense.

## Member Data Documentation

## ◆ face_geometry

config_control_design.face_surface.face_geometry  
---  
  
Referenced by
[automotive_design.swept_face_solid.wr1()](../../d1/d64/classautomotive__design_1_1swept__face__solid.html#a6ba90dcc401b0d407dd0ba8128a71e4f),
[automotive_design.face_surface.wr1()](../../df/d6b/classautomotive__design_1_1face__surface.html#ad6c02b269122e6cfaea7b325a76fe6da),
[automotive_design.advanced_face.wr1()](../../d1/d62/classautomotive__design_1_1advanced__face.html#a909cfe9dc6dce7295fc8b058d98be155),
[config_control_design.advanced_face.wr1()](../../db/d65/classconfig__control__design_1_1advanced__face.html#a479a609264b1ca2e70775476f690681e),
[automotive_design.advanced_face.wr10()](../../d1/d62/classautomotive__design_1_1advanced__face.html#aa08adf112660acfb17f4847e837bdf6d),
[config_control_design.advanced_face.wr10()](../../db/d65/classconfig__control__design_1_1advanced__face.html#a0118e22d47858317fa0dff7407854d05),
[automotive_design.advanced_face.wr6()](../../d1/d62/classautomotive__design_1_1advanced__face.html#ac086e0ff8446e94665dadf33064d24c8),
and
[config_control_design.advanced_face.wr6()](../../db/d65/classconfig__control__design_1_1advanced__face.html#a915743fb20126f8a0b1adccf202a429d).

## ◆ same_sense

config_control_design.face_surface.same_sense  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

