---
url: https://freecad.github.io/SourceDoc/d1/d03/classautomotive__design_1_1point__on__surface.html
scraped_at: 2025-09-08T15:09:51.177037
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [point_on_surface](../../d1/d03/classautomotive__design_1_1point__on__surface.html)

[List of all members](../../d1/d0e/classautomotive__design_1_1point__on__surface-members.html) | Public Member Functions | Public Attributes

automotive_design.point_on_surface Class Reference

##  Public Member Functions  
  
---  
def | [basis_surface](../../d1/d03/classautomotive__design_1_1point__on__surface.html#ad832d5f0a711f6991a5d9bb06c9e88b2) ()  
def | [point_parameter_u](../../d1/d03/classautomotive__design_1_1point__on__surface.html#a929e608b0cdb56e5d66bdb17600ccb53) ()  
def | [point_parameter_v](../../d1/d03/classautomotive__design_1_1point__on__surface.html#aa0842715c211a905cc2b041a8dfcd2aa) ()  
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
[basis_surface](../../d1/d03/classautomotive__design_1_1point__on__surface.html#a3ec7b3f54324d01811620d9f0e920391)  
|
[point_parameter_u](../../d1/d03/classautomotive__design_1_1point__on__surface.html#ac6cd8af72977ab79d1c0164872e642ec)  
|
[point_parameter_v](../../d1/d03/classautomotive__design_1_1point__on__surface.html#a3a30eae1023c3c30fe42d62bfcd88f9e)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
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

def automotive_design.point_on_surface.basis_surface  | ( | | ) |   
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

def automotive_design.point_on_surface.point_parameter_u  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.point_on_surface._point_parameter_u,
automotive_design.point_on_surface._point_parameter_u, and
config_control_design.point_on_surface._point_parameter_u.

## ◆ point_parameter_v()

def automotive_design.point_on_surface.point_parameter_v  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.point_on_surface._point_parameter_v,
automotive_design.point_on_surface._point_parameter_v, and
config_control_design.point_on_surface._point_parameter_v.

## Member Data Documentation

## ◆ basis_surface

automotive_design.point_on_surface.basis_surface  
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

automotive_design.point_on_surface.point_parameter_u  
---  
  
## ◆ point_parameter_v

automotive_design.point_on_surface.point_parameter_v  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

