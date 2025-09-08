---
url: https://freecad.github.io/SourceDoc/de/dfd/classautomotive__design_1_1curve__bounded__surface.html
scraped_at: 2025-09-08T15:02:55.484380
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [curve_bounded_surface](../../de/dfd/classautomotive__design_1_1curve__bounded__surface.html)

[List of all members](../../db/de4/classautomotive__design_1_1curve__bounded__surface-members.html) | Public Member Functions | Public Attributes

automotive_design.curve_bounded_surface Class Reference

##  Public Member Functions  
  
---  
def | [basis_surface](../../de/dfd/classautomotive__design_1_1curve__bounded__surface.html#a102d0573d7b4dc2c6ce2bb60f9ba3f5c) ()  
def | [boundaries](../../de/dfd/classautomotive__design_1_1curve__bounded__surface.html#a5a7e29f3f1bddf61248d99458c8c38ee) ()  
def | [implicit_outer](../../de/dfd/classautomotive__design_1_1curve__bounded__surface.html#a884ccea96e2e4b16fcee0ee5f1a5d2b7) ()  
def | [wr1](../../de/dfd/classautomotive__design_1_1curve__bounded__surface.html#a5b2c2edd7fead378a35133cd39a99513) (self)  
def | [wr2](../../de/dfd/classautomotive__design_1_1curve__bounded__surface.html#aee9bebad9973fccb90b85a3418fe6259) (self)  
def | [wr3](../../de/dfd/classautomotive__design_1_1curve__bounded__surface.html#aa95841eb848d5809d185b79c26709b63) (self)  
def | [wr4](../../de/dfd/classautomotive__design_1_1curve__bounded__surface.html#a83bdd4774372ebd41135a1d0a169437b) (self)  
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
[basis_surface](../../de/dfd/classautomotive__design_1_1curve__bounded__surface.html#a398fae2bacfa1b9854cddf04a8cef43a)  
|
[boundaries](../../de/dfd/classautomotive__design_1_1curve__bounded__surface.html#a5edc45e9b6f6470730d92f3eb67676d5)  
|
[implicit_outer](../../de/dfd/classautomotive__design_1_1curve__bounded__surface.html#a9f675f00cf5645fa37d5ff6af76eea3b)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity curve_bounded_surface definition.
    
        :param basis_surface
        :type basis_surface:surface
    
        :param boundaries
        :type boundaries:SET(1,None,'boundary_curve', scope = schema_scope)
    
        :param implicit_outer
        :type implicit_outer:BOOLEAN

## Member Function Documentation

## ◆ basis_surface()

def automotive_design.curve_bounded_surface.basis_surface  | ( | | ) |   
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

## ◆ boundaries()

def automotive_design.curve_bounded_surface.boundaries  | ( | | ) |   
---|---|---|---|---  
  
References femsolver.elmer.sifio.Builder._boundaries,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.tolerance_zone_definition._boundaries,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.annotation_fill_area._boundaries,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.curve_bounded_surface._boundaries,
automotive_design.tolerance_zone_definition._boundaries,
automotive_design.annotation_fill_area._boundaries,
automotive_design.curve_bounded_surface._boundaries,
config_control_design.curve_bounded_surface._boundaries, and
ifc4.ifccurveboundedsurface._boundaries.

Referenced by
[Mod.PartDesign.WizardShaft.SegmentFunction.TranslationFunction.evaluate()](../../dd/de9/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1TranslationFunction.html#ab0735814eeb7905e8a476d0d53a32b55),
and
[config_control_design.curve_bounded_surface.wr1()](../../dc/d61/classconfig__control__design_1_1curve__bounded__surface.html#a2ec204f7adf74d242473768dff1f8e54).

## ◆ implicit_outer()

def automotive_design.curve_bounded_surface.implicit_outer  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.curve_bounded_surface._implicit_outer,
automotive_design.curve_bounded_surface._implicit_outer, and
config_control_design.curve_bounded_surface._implicit_outer.

Referenced by
[automotive_design.curve_bounded_surface.wr1()](../../de/dfd/classautomotive__design_1_1curve__bounded__surface.html#a5b2c2edd7fead378a35133cd39a99513),
[config_control_design.curve_bounded_surface.wr1()](../../dc/d61/classconfig__control__design_1_1curve__bounded__surface.html#a2ec204f7adf74d242473768dff1f8e54),
[automotive_design.curve_bounded_surface.wr2()](../../de/dfd/classautomotive__design_1_1curve__bounded__surface.html#aee9bebad9973fccb90b85a3418fe6259),
and
[config_control_design.curve_bounded_surface.wr2()](../../dc/d61/classconfig__control__design_1_1curve__bounded__surface.html#a6c40b7a7eaace49a3aabfe3fa47d2a35).

## ◆ wr1()

def automotive_design.curve_bounded_surface.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.geometric_representation_item](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#a9677d2be5fc5c7c8ccb6819380198bbc).

References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.curve_bounded_surface.implicit_outer,
[automotive_design.curve_bounded_surface.implicit_outer](../../de/dfd/classautomotive__design_1_1curve__bounded__surface.html#a9f675f00cf5645fa37d5ff6af76eea3b),
and
[config_control_design.curve_bounded_surface.implicit_outer](../../dc/d61/classconfig__control__design_1_1curve__bounded__surface.html#a8c9dd79b440e1373d534cdb3259a32db).

## ◆ wr2()

def automotive_design.curve_bounded_surface.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
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
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.curve_bounded_surface.implicit_outer,
[automotive_design.curve_bounded_surface.implicit_outer](../../de/dfd/classautomotive__design_1_1curve__bounded__surface.html#a9f675f00cf5645fa37d5ff6af76eea3b),
and
[config_control_design.curve_bounded_surface.implicit_outer](../../dc/d61/classconfig__control__design_1_1curve__bounded__surface.html#a8c9dd79b440e1373d534cdb3259a32db).

## ◆ wr3()

def automotive_design.curve_bounded_surface.wr3  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
## ◆ wr4()

def automotive_design.curve_bounded_surface.wr4  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
## Member Data Documentation

## ◆ basis_surface

automotive_design.curve_bounded_surface.basis_surface  
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

## ◆ boundaries

automotive_design.curve_bounded_surface.boundaries  
---  
  
Referenced by
[Mod.PartDesign.WizardShaft.SegmentFunction.TranslationFunction.evaluate()](../../dd/de9/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1TranslationFunction.html#ab0735814eeb7905e8a476d0d53a32b55),
and
[config_control_design.curve_bounded_surface.wr1()](../../dc/d61/classconfig__control__design_1_1curve__bounded__surface.html#a2ec204f7adf74d242473768dff1f8e54).

## ◆ implicit_outer

automotive_design.curve_bounded_surface.implicit_outer  
---  
  
Referenced by
[automotive_design.curve_bounded_surface.wr1()](../../de/dfd/classautomotive__design_1_1curve__bounded__surface.html#a5b2c2edd7fead378a35133cd39a99513),
[config_control_design.curve_bounded_surface.wr1()](../../dc/d61/classconfig__control__design_1_1curve__bounded__surface.html#a2ec204f7adf74d242473768dff1f8e54),
[automotive_design.curve_bounded_surface.wr2()](../../de/dfd/classautomotive__design_1_1curve__bounded__surface.html#aee9bebad9973fccb90b85a3418fe6259),
and
[config_control_design.curve_bounded_surface.wr2()](../../dc/d61/classconfig__control__design_1_1curve__bounded__surface.html#a6c40b7a7eaace49a3aabfe3fa47d2a35).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

