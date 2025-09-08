---
url: https://freecad.github.io/SourceDoc/df/d6b/classautomotive__design_1_1face__surface.html
scraped_at: 2025-09-08T15:05:29.104448
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [face_surface](../../df/d6b/classautomotive__design_1_1face__surface.html)

[List of all members](../../d7/d8d/classautomotive__design_1_1face__surface-members.html) | Public Member Functions | Public Attributes

automotive_design.face_surface Class Reference

##  Public Member Functions  
  
---  
def | [face_geometry](../../df/d6b/classautomotive__design_1_1face__surface.html#ac2cd2019e37534c34c7c85b63acf6ef8) ()  
def | [same_sense](../../df/d6b/classautomotive__design_1_1face__surface.html#a65405e863469479e97c181e56eada7b0) ()  
def | [wr1](../../df/d6b/classautomotive__design_1_1face__surface.html#ad6c02b269122e6cfaea7b325a76fe6da) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.face](../../d4/d1b/classautomotive__design_1_1face.html)  
def | [bounds](../../d4/d1b/classautomotive__design_1_1face.html#af679fe2caae48769302c5f02959487bc) ()  
def | [wr1](../../d4/d1b/classautomotive__design_1_1face.html#a130adf47ee7912741b284ac0aa3f2208) (self)  
def | [wr2](../../d4/d1b/classautomotive__design_1_1face.html#a476bf9885f52fbbd7d6c683a16b44335) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
def | [name](../../d3/d20/classautomotive__design_1_1representation__item.html#a33b5812d92aa0d107b4fd4274c17b9d9) ()  
def | [wr1](../../d3/d20/classautomotive__design_1_1representation__item.html#af350c19fc5e5763d4991494a99d979ed) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.geometric_representation_item](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html)  
def | [dim](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#aef245618450610e88788dcaea46ad742) ()  
def | [wr1](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#a9677d2be5fc5c7c8ccb6819380198bbc) (self)  
  
##  Public Attributes  
  
---  
|
[face_geometry](../../df/d6b/classautomotive__design_1_1face__surface.html#a6627d755c4d2148c31c803c83f733d5e)  
|
[same_sense](../../df/d6b/classautomotive__design_1_1face__surface.html#abba5e90730d25517b863993e0870e7c0)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.face](../../d4/d1b/classautomotive__design_1_1face.html)  
|
[bounds](../../d4/d1b/classautomotive__design_1_1face.html#a78bfe1fdfc9d39b9e740428b5a355b4c)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity face_surface definition.
    
        :param face_geometry
        :type face_geometry:surface
    
        :param same_sense
        :type same_sense:BOOLEAN

## Member Function Documentation

## ◆ face_geometry()

def automotive_design.face_surface.face_geometry  | ( | | ) |   
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

def automotive_design.face_surface.same_sense  | ( | | ) |   
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

## ◆ wr1()

def automotive_design.face_surface.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.geometric_representation_item](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#a9677d2be5fc5c7c8ccb6819380198bbc).

Reimplemented in
[automotive_design.advanced_face](../../d1/d62/classautomotive__design_1_1advanced__face.html#a909cfe9dc6dce7295fc8b058d98be155).

References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.face_surface.face_geometry,
[automotive_design.face_surface.face_geometry](../../df/d6b/classautomotive__design_1_1face__surface.html#a6627d755c4d2148c31c803c83f733d5e),
and
[config_control_design.face_surface.face_geometry](../../d4/d2e/classconfig__control__design_1_1face__surface.html#a04ace46f8dc2e22c7f4a28d267531f6a).

## Member Data Documentation

## ◆ face_geometry

automotive_design.face_surface.face_geometry  
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

automotive_design.face_surface.same_sense  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

