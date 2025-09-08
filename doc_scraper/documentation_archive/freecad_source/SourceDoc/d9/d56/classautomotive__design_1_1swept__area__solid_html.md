---
url: https://freecad.github.io/SourceDoc/d9/d56/classautomotive__design_1_1swept__area__solid.html
scraped_at: 2025-09-08T15:13:55.204832
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [swept_area_solid](../../d9/d56/classautomotive__design_1_1swept__area__solid.html)

[List of all members](../../dd/d2b/classautomotive__design_1_1swept__area__solid-members.html) | Public Member Functions | Public Attributes

automotive_design.swept_area_solid Class Reference

##  Public Member Functions  
  
---  
def | [swept_area](../../d9/d56/classautomotive__design_1_1swept__area__solid.html#a34733853b458d9d5121fac66b63dce35) ()  
def | [wr1](../../d9/d56/classautomotive__design_1_1swept__area__solid.html#af06ba2d89fb93f3538bd0cfb3899ca7d) (self)  
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
[swept_area](../../d9/d56/classautomotive__design_1_1swept__area__solid.html#a88b9dee12a1622f6dcae61055453a815)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity swept_area_solid definition.
    
        :param swept_area
        :type swept_area:curve_bounded_surface

## Member Function Documentation

## ◆ swept_area()

def automotive_design.swept_area_solid.swept_area  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.swept_area_solid._swept_area,
and automotive_design.swept_area_solid._swept_area.

Referenced by
[automotive_design.swept_area_solid.wr1()](../../d9/d56/classautomotive__design_1_1swept__area__solid.html#af06ba2d89fb93f3538bd0cfb3899ca7d).

## ◆ wr1()

def automotive_design.swept_area_solid.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.geometric_representation_item](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#a9677d2be5fc5c7c8ccb6819380198bbc).

Reimplemented in
[automotive_design.surface_curve_swept_area_solid](../../dc/db7/classautomotive__design_1_1surface__curve__swept__area__solid.html#a9c3872eaf0dbc9d98d40429cc3dbf773),
[automotive_design.extruded_area_solid](../../db/d70/classautomotive__design_1_1extruded__area__solid.html#a1d3bf9a15a698b5deb63e5889b37f152),
and
[automotive_design.ruled_surface_swept_area_solid](../../da/dd8/classautomotive__design_1_1ruled__surface__swept__area__solid.html#a7146ef05ee5c0d08da8d6d3916b66510).

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
[config_control_design.curve_bounded_surface.basis_surface](../../dc/d61/classconfig__control__design_1_1curve__bounded__surface.html#a41f3f9de2d93a5bbb4cd209533394602),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.swept_area_solid.swept_area,
and
[automotive_design.swept_area_solid.swept_area](../../d9/d56/classautomotive__design_1_1swept__area__solid.html#a88b9dee12a1622f6dcae61055453a815).

## Member Data Documentation

## ◆ swept_area

automotive_design.swept_area_solid.swept_area  
---  
  
Referenced by
[automotive_design.swept_area_solid.wr1()](../../d9/d56/classautomotive__design_1_1swept__area__solid.html#af06ba2d89fb93f3538bd0cfb3899ca7d).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

