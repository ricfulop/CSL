---
url: https://freecad.github.io/SourceDoc/de/d9d/classconfig__control__design_1_1point__on__surface.html
scraped_at: 2025-09-08T15:23:02.546497
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [point_on_surface](../../de/d9d/classconfig__control__design_1_1point__on__surface.html)

[List of all members](../../db/dce/classconfig__control__design_1_1point__on__surface-members.html) | Public Member Functions | Public Attributes

config_control_design.point_on_surface Class Reference

##  Public Member Functions  
  
---  
def | [basis_surface](../../de/d9d/classconfig__control__design_1_1point__on__surface.html#ad91dfe91df73bf3e9ffc53156233c52d) ()  
def | [point_parameter_u](../../de/d9d/classconfig__control__design_1_1point__on__surface.html#a7f7fdd1670c3d79586c6ed3f945b3057) ()  
def | [point_parameter_v](../../de/d9d/classconfig__control__design_1_1point__on__surface.html#a22fe32681a888be98f19a59cee179e31) ()  
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
[basis_surface](../../de/d9d/classconfig__control__design_1_1point__on__surface.html#ad76843c75f55e71afc83016a05fbf691)  
|
[point_parameter_u](../../de/d9d/classconfig__control__design_1_1point__on__surface.html#a130f2ad3ddc88703e866c55d144335c9)  
|
[point_parameter_v](../../de/d9d/classconfig__control__design_1_1point__on__surface.html#a84ea79a0c4bb6902a2408f036a85708a)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
|
[name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a0e8be677f8410825a46422f3c0e1c128)  
  
## Detailed Description

    
    
    Entity point_on_surface definition.
    
        :param basis_surface
        :type basis_surface:surface
    
        :param point_parameter_u
        :type point_parameter_u:parameter_value
    
        :param point_parameter_v
        :type point_parameter_v:parameter_value

## Member Function Documentation

## ◆ basis_surface()

def config_control_design.point_on_surface.basis_surface  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.offset_surface._basis_surface,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.point_on_surface._basis_surface,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.pcurve._basis_surface,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rectangular_trimmed_surface._basis_surface,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.degenerate_pcurve._basis_surface,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.curve_bounded_surface._basis_surface,
automotive_design.offset_surface._basis_surface,
automotive_design.point_on_surface._basis_surface,
automotive_design.pcurve._basis_surface,
automotive_design.rectangular_trimmed_surface._basis_surface,
automotive_design.degenerate_pcurve._basis_surface,
automotive_design.curve_bounded_surface._basis_surface,
config_control_design.offset_surface._basis_surface,
config_control_design.point_on_surface._basis_surface,
config_control_design.pcurve._basis_surface,
config_control_design.rectangular_trimmed_surface._basis_surface,
config_control_design.degenerate_pcurve._basis_surface, and
config_control_design.curve_bounded_surface._basis_surface.

Referenced by
[automotive_design.swept_area_solid.wr1()](../../d9/d56/classautomotive__design_1_1swept__area__solid.html#af06ba2d89fb93f3538bd0cfb3899ca7d),
[automotive_design.surface_curve_swept_area_solid.wr1()](../../dc/db7/classautomotive__design_1_1surface__curve__swept__area__solid.html#a9c3872eaf0dbc9d98d40429cc3dbf773),
[automotive_design.composite_curve_on_surface.wr1()](../../d9/d62/classautomotive__design_1_1composite__curve__on__surface.html#aa4c4c80418d0ac5f7c0d8c14865f4126),
[config_control_design.composite_curve_on_surface.wr1()](../../da/d0c/classconfig__control__design_1_1composite__curve__on__surface.html#af1248e63f087994050d924b1f03ce2a7),
[automotive_design.curve_bounded_surface.wr2()](../../de/dfd/classautomotive__design_1_1curve__bounded__surface.html#aee9bebad9973fccb90b85a3418fe6259),
[config_control_design.curve_bounded_surface.wr2()](../../dc/d61/classconfig__control__design_1_1curve__bounded__surface.html#a6c40b7a7eaace49a3aabfe3fa47d2a35),
[automotive_design.rectangular_trimmed_surface.wr3()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a4c4fa09bc28e0979821dcb919bc70801),
[config_control_design.rectangular_trimmed_surface.wr3()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#af917d1182a7d07aa13d556e19e3be76a),
[automotive_design.rectangular_trimmed_surface.wr4()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#afc4757205d91cd02edfd30794d089939),
and
[config_control_design.rectangular_trimmed_surface.wr4()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a58eb9b75ab01c968f17742257c5de3e2).

## ◆ point_parameter_u()

def config_control_design.point_on_surface.point_parameter_u  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.point_on_surface._point_parameter_u,
automotive_design.point_on_surface._point_parameter_u, and
config_control_design.point_on_surface._point_parameter_u.

## ◆ point_parameter_v()

def config_control_design.point_on_surface.point_parameter_v  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.point_on_surface._point_parameter_v,
automotive_design.point_on_surface._point_parameter_v, and
config_control_design.point_on_surface._point_parameter_v.

## Member Data Documentation

## ◆ basis_surface

config_control_design.point_on_surface.basis_surface  
---  
  
Referenced by
[automotive_design.swept_area_solid.wr1()](../../d9/d56/classautomotive__design_1_1swept__area__solid.html#af06ba2d89fb93f3538bd0cfb3899ca7d),
[automotive_design.surface_curve_swept_area_solid.wr1()](../../dc/db7/classautomotive__design_1_1surface__curve__swept__area__solid.html#a9c3872eaf0dbc9d98d40429cc3dbf773),
[automotive_design.composite_curve_on_surface.wr1()](../../d9/d62/classautomotive__design_1_1composite__curve__on__surface.html#aa4c4c80418d0ac5f7c0d8c14865f4126),
[config_control_design.composite_curve_on_surface.wr1()](../../da/d0c/classconfig__control__design_1_1composite__curve__on__surface.html#af1248e63f087994050d924b1f03ce2a7),
[automotive_design.curve_bounded_surface.wr2()](../../de/dfd/classautomotive__design_1_1curve__bounded__surface.html#aee9bebad9973fccb90b85a3418fe6259),
[config_control_design.curve_bounded_surface.wr2()](../../dc/d61/classconfig__control__design_1_1curve__bounded__surface.html#a6c40b7a7eaace49a3aabfe3fa47d2a35),
[automotive_design.rectangular_trimmed_surface.wr3()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a4c4fa09bc28e0979821dcb919bc70801),
[config_control_design.rectangular_trimmed_surface.wr3()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#af917d1182a7d07aa13d556e19e3be76a),
[automotive_design.rectangular_trimmed_surface.wr4()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#afc4757205d91cd02edfd30794d089939),
and
[config_control_design.rectangular_trimmed_surface.wr4()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a58eb9b75ab01c968f17742257c5de3e2).

## ◆ point_parameter_u

config_control_design.point_on_surface.point_parameter_u  
---  
  
## ◆ point_parameter_v

config_control_design.point_on_surface.point_parameter_v  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

