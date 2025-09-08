---
url: https://freecad.github.io/SourceDoc/d9/d62/classautomotive__design_1_1composite__curve__on__surface.html
scraped_at: 2025-09-08T15:02:07.292432
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [composite_curve_on_surface](../../d9/d62/classautomotive__design_1_1composite__curve__on__surface.html)

[List of all members](../../d6/dfa/classautomotive__design_1_1composite__curve__on__surface-members.html) | Public Member Functions

automotive_design.composite_curve_on_surface Class Reference

##  Public Member Functions  
  
---  
def | [basis_surface](../../d9/d62/classautomotive__design_1_1composite__curve__on__surface.html#a0cc000cde500f2c0eb2286391e0c1f37) ()  
def | [wr1](../../d9/d62/classautomotive__design_1_1composite__curve__on__surface.html#aa4c4c80418d0ac5f7c0d8c14865f4126) (self)  
def | [wr2](../../d9/d62/classautomotive__design_1_1composite__curve__on__surface.html#ac91070e2975055b6bd7b4856e947ac9d) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.composite_curve](../../de/d2c/classautomotive__design_1_1composite__curve.html)  
def | [closed_curve](../../de/d2c/classautomotive__design_1_1composite__curve.html#a6b988086709b2d29b533fa3145010e1d) ()  
def | [n_segments](../../de/d2c/classautomotive__design_1_1composite__curve.html#ad537919a3fcbf060a73068a13add3be9) ()  
def | [segments](../../de/d2c/classautomotive__design_1_1composite__curve.html#ae958961a1c98d4887b1982ca20655a89) ()  
def | [self_intersect](../../de/d2c/classautomotive__design_1_1composite__curve.html#a5b236a39add33e2eec9aa7a4692b7509) ()  
def | [wr1](../../de/d2c/classautomotive__design_1_1composite__curve.html#a6c06ad45cd7346e7624b280655556968) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.geometric_representation_item](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html)  
def | [dim](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#aef245618450610e88788dcaea46ad742) ()  
def | [wr1](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#a9677d2be5fc5c7c8ccb6819380198bbc) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
def | [name](../../d3/d20/classautomotive__design_1_1representation__item.html#a33b5812d92aa0d107b4fd4274c17b9d9) ()  
def | [wr1](../../d3/d20/classautomotive__design_1_1representation__item.html#af350c19fc5e5763d4991494a99d979ed) (self)  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.composite_curve](../../de/d2c/classautomotive__design_1_1composite__curve.html)  
|
[segments](../../de/d2c/classautomotive__design_1_1composite__curve.html#a568c2816d1f69a0584b0e631b61b6384)  
|
[self_intersect](../../de/d2c/classautomotive__design_1_1composite__curve.html#abc77b0dbfceac592cd5c570043f24d4c)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity composite_curve_on_surface definition.
    
        :param basis_surface
        :type basis_surface:SET(0,2,'surface', scope = schema_scope)

## Member Function Documentation

## ◆ basis_surface()

def automotive_design.composite_curve_on_surface.basis_surface  | ( | | ) |   
---|---|---|---|---  
  
References
[automotive_design.get_basis_surface()](../../d4/ddf/namespaceautomotive__design.html#a676b4e09ef5efab0b358fc57506f71b2).

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

## ◆ wr1()

def automotive_design.composite_curve_on_surface.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.composite_curve](../../de/d2c/classautomotive__design_1_1composite__curve.html#a6c06ad45cd7346e7624b280655556968).

Reimplemented in
[automotive_design.boundary_curve](../../d6/db8/classautomotive__design_1_1boundary__curve.html#a4c0ae421a9284e0352b0abe776092fec).

References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.offset_surface.basis_surface,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.point_on_surface.basis_surface,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.composite_curve_on_surface.basis_surface(),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_curve.basis_surface(),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.pcurve.basis_surface,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rectangular_trimmed_surface.basis_surface,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.degenerate_pcurve.basis_surface,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.curve_bounded_surface.basis_surface,
[automotive_design.offset_surface.basis_surface](../../df/d73/classautomotive__design_1_1offset__surface.html#aa72ec368edcce7f74718dc18a9d3be7d),
[automotive_design.point_on_surface.basis_surface](../../d1/d03/classautomotive__design_1_1point__on__surface.html#a3ec7b3f54324d01811620d9f0e920391),
[automotive_design.composite_curve_on_surface.basis_surface()](../../d9/d62/classautomotive__design_1_1composite__curve__on__surface.html#a0cc000cde500f2c0eb2286391e0c1f37),
[automotive_design.surface_curve.basis_surface()](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a4124fffa9d613bb72525c9f8ed586d85),
[automotive_design.pcurve.basis_surface](../../d4/d4b/classautomotive__design_1_1pcurve.html#a0448d2b4e9bea68fa8ef372c62736f24),
[automotive_design.rectangular_trimmed_surface.basis_surface](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#aed9764c3a03e2191bba3317e28371b00),
[automotive_design.degenerate_pcurve.basis_surface](../../de/d21/classautomotive__design_1_1degenerate__pcurve.html#a42e73f451fd2ed80e05db5b64c59fc70),
[automotive_design.curve_bounded_surface.basis_surface](../../de/dfd/classautomotive__design_1_1curve__bounded__surface.html#a398fae2bacfa1b9854cddf04a8cef43a),
[config_control_design.offset_surface.basis_surface](../../de/d83/classconfig__control__design_1_1offset__surface.html#aa6314357180ffcf0ac76e5c30a32e562),
[config_control_design.point_on_surface.basis_surface](../../de/d9d/classconfig__control__design_1_1point__on__surface.html#ad76843c75f55e71afc83016a05fbf691),
[config_control_design.composite_curve_on_surface.basis_surface()](../../da/d0c/classconfig__control__design_1_1composite__curve__on__surface.html#ac2894f2e56864a54058ce357445f8914),
[config_control_design.surface_curve.basis_surface()](../../db/d04/classconfig__control__design_1_1surface__curve.html#abfa790ac414a75af3b6ed8c093208a5a),
[config_control_design.pcurve.basis_surface](../../d8/d67/classconfig__control__design_1_1pcurve.html#a5fd85c1443902391b7d328216cece85b),
[config_control_design.rectangular_trimmed_surface.basis_surface](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a2cc8169c38c15fa8b3097b45f5bab005),
[config_control_design.degenerate_pcurve.basis_surface](../../d3/d07/classconfig__control__design_1_1degenerate__pcurve.html#acb5d040c5ad86be353cd2c8de85bb0ce),
and
[config_control_design.curve_bounded_surface.basis_surface](../../dc/d61/classconfig__control__design_1_1curve__bounded__surface.html#a41f3f9de2d93a5bbb4cd209533394602).

## ◆ wr2()

def automotive_design.composite_curve_on_surface.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[automotive_design.constraints_composite_curve_on_surface()](../../d4/ddf/namespaceautomotive__design.html#aa927e1901fc784d7f9cdcb72876a1d64).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

