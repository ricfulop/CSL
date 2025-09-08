---
url: https://freecad.github.io/SourceDoc/df/d73/classautomotive__design_1_1offset__surface.html
scraped_at: 2025-09-08T15:08:39.893386
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [offset_surface](../../df/d73/classautomotive__design_1_1offset__surface.html)

[List of all members](../../d7/de9/classautomotive__design_1_1offset__surface-members.html) | Public Member Functions | Public Attributes

automotive_design.offset_surface Class Reference

##  Public Member Functions  
  
---  
def | [basis_surface](../../df/d73/classautomotive__design_1_1offset__surface.html#a507c012cb74ed7496a155cc8fcb60cad) ()  
def | [distance](../../df/d73/classautomotive__design_1_1offset__surface.html#ac111528948334d9b8baa3a4742978d81) ()  
def | [self_intersect](../../df/d73/classautomotive__design_1_1offset__surface.html#a2df30eec12d2df40c40265f34b8be07b) ()  
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
[basis_surface](../../df/d73/classautomotive__design_1_1offset__surface.html#aa72ec368edcce7f74718dc18a9d3be7d)  
|
[distance](../../df/d73/classautomotive__design_1_1offset__surface.html#a0d0f611b03179a8743dda860d211399e)  
|
[self_intersect](../../df/d73/classautomotive__design_1_1offset__surface.html#a4e0ffedcca1c15d34f6cf0cc22cb276d)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity offset_surface definition.
    
        :param basis_surface
        :type basis_surface:surface
    
        :param distance
        :type distance:length_measure
    
        :param self_intersect
        :type self_intersect:LOGICAL

## Member Function Documentation

## ◆ basis_surface()

def automotive_design.offset_surface.basis_surface  | ( | | ) |   
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

## ◆ distance()

def automotive_design.offset_surface.distance  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.offset_surface._distance,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.offset_curve_3d._distance,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.offset_curve_2d._distance,
automotive_design.offset_surface._distance,
automotive_design.offset_curve_3d._distance,
automotive_design.offset_curve_2d._distance,
config_control_design.offset_surface._distance,
config_control_design.offset_curve_3d._distance,
ifc2x3.ifcoffsetcurve2d._distance, ifc2x3.ifcoffsetcurve3d._distance,
ifc4.ifcoffsetcurve2d._distance, and ifc4.ifcoffsetcurve3d._distance.

Referenced by
[PathScripts.PathDressupDogbone.Bone.adaptiveLength()](../../d6/d5c/classPathScripts_1_1PathDressupDogbone_1_1Bone.html#adde010e67251dab408b4c9737e25f0f8),
and
[PathScripts.PathDressupDogbone.Bone.corner()](../../d6/d5c/classPathScripts_1_1PathDressupDogbone_1_1Bone.html#a3020aa4704bbeca155e81158067a80d2).

## ◆ self_intersect()

def automotive_design.offset_surface.self_intersect  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.offset_surface._self_intersect,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_surface._self_intersect,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_curve._self_intersect,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.offset_curve_3d._self_intersect,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.composite_curve._self_intersect,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.offset_curve_2d._self_intersect,
automotive_design.offset_surface._self_intersect,
automotive_design.b_spline_surface._self_intersect,
automotive_design.b_spline_curve._self_intersect,
automotive_design.offset_curve_3d._self_intersect,
automotive_design.composite_curve._self_intersect,
automotive_design.offset_curve_2d._self_intersect,
config_control_design.offset_surface._self_intersect,
config_control_design.b_spline_surface._self_intersect,
config_control_design.b_spline_curve._self_intersect,
config_control_design.offset_curve_3d._self_intersect, and
config_control_design.composite_curve._self_intersect.

## Member Data Documentation

## ◆ basis_surface

automotive_design.offset_surface.basis_surface  
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

## ◆ distance

automotive_design.offset_surface.distance  
---  
  
Referenced by
[PathScripts.PathDressupDogbone.Bone.adaptiveLength()](../../d6/d5c/classPathScripts_1_1PathDressupDogbone_1_1Bone.html#adde010e67251dab408b4c9737e25f0f8),
and
[PathScripts.PathDressupDogbone.Bone.corner()](../../d6/d5c/classPathScripts_1_1PathDressupDogbone_1_1Bone.html#a3020aa4704bbeca155e81158067a80d2).

## ◆ self_intersect

automotive_design.offset_surface.self_intersect  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

