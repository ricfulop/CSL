---
url: https://freecad.github.io/SourceDoc/de/df8/classautomotive__design_1_1axis2__placement__2d.html
scraped_at: 2025-09-08T15:00:38.910097
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [axis2_placement_2d](../../de/df8/classautomotive__design_1_1axis2__placement__2d.html)

[List of all members](../../d3/dde/classautomotive__design_1_1axis2__placement__2d-members.html) | Public Member Functions | Public Attributes

automotive_design.axis2_placement_2d Class Reference

##  Public Member Functions  
  
---  
def | [p](../../de/df8/classautomotive__design_1_1axis2__placement__2d.html#a486597a463ad5c1866464ec6472bfb63) ()  
def | [ref_direction](../../de/df8/classautomotive__design_1_1axis2__placement__2d.html#aef7a8e041c625019e98ac54d0647b2b5) ()  
def | [wr1](../../de/df8/classautomotive__design_1_1axis2__placement__2d.html#ae04cefbf1df7f4cbc52a879293dc7337) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.placement](../../d8/d8c/classautomotive__design_1_1placement.html)  
def | [location](../../d8/d8c/classautomotive__design_1_1placement.html#ae557180edc9d5dd0ae9def8d6e23eb6d) ()  
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
[dim](../../de/df8/classautomotive__design_1_1axis2__placement__2d.html#a3bb2cbd4fe5edf0d606d247c937233ba)  
|
[ref_direction](../../de/df8/classautomotive__design_1_1axis2__placement__2d.html#a575c173d67a3efaf72776207a5f1e54d)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.placement](../../d8/d8c/classautomotive__design_1_1placement.html)  
|
[location](../../d8/d8c/classautomotive__design_1_1placement.html#aade15ec8d9163d4f50f6ebd55bf9e306)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity axis2_placement_2d definition.
    
        :param ref_direction
        :type ref_direction:direction
    
        :param p
        :type p:LIST(2,2,'direction', scope = schema_scope)

## Member Function Documentation

## ◆ p()

def automotive_design.axis2_placement_2d.p  | ( | | ) |   
---|---|---|---|---  
  
References
[automotive_design.build_2axes()](../../d4/ddf/namespaceautomotive__design.html#a46d83c94157f83c40bea5402729fbd56),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.axis2_placement_2d.ref_direction,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.offset_curve_3d.ref_direction,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.axis2_placement_3d.ref_direction,
[automotive_design.axis2_placement_2d.ref_direction](../../de/df8/classautomotive__design_1_1axis2__placement__2d.html#a575c173d67a3efaf72776207a5f1e54d),
[automotive_design.offset_curve_3d.ref_direction](../../d2/dfb/classautomotive__design_1_1offset__curve__3d.html#ab7d60a4d82b3fdc40c331c44801ed9b9),
[automotive_design.axis2_placement_3d.ref_direction](../../d8/d42/classautomotive__design_1_1axis2__placement__3d.html#a683adce22cd8480ddff77d4f1ba08ca1),
[config_control_design.axis2_placement_2d.ref_direction](../../dd/d34/classconfig__control__design_1_1axis2__placement__2d.html#a90c7545d54c888198f20c1e6af40bfc8),
[config_control_design.offset_curve_3d.ref_direction](../../dd/d91/classconfig__control__design_1_1offset__curve__3d.html#af6d2d7031258bcb13b3b12ff42f88441),
and
[config_control_design.axis2_placement_3d.ref_direction](../../dd/d2a/classconfig__control__design_1_1axis2__placement__3d.html#a851533113897f9d6ce767df525136ecf).

Referenced by
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel.accept()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#ae0e2ec6f40370c732beb919549a0111d),
and
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel.getPrefColor()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#aed0d2ca7140c357c09c3aae8f4bba159).

## ◆ ref_direction()

def automotive_design.axis2_placement_2d.ref_direction  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.axis2_placement_2d._ref_direction,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.offset_curve_3d._ref_direction,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.axis2_placement_3d._ref_direction,
automotive_design.axis2_placement_2d._ref_direction,
automotive_design.offset_curve_3d._ref_direction,
automotive_design.axis2_placement_3d._ref_direction,
config_control_design.axis2_placement_2d._ref_direction,
config_control_design.offset_curve_3d._ref_direction, and
config_control_design.axis2_placement_3d._ref_direction.

Referenced by
[automotive_design.axis2_placement_2d.p()](../../de/df8/classautomotive__design_1_1axis2__placement__2d.html#a486597a463ad5c1866464ec6472bfb63),
[automotive_design.axis2_placement_3d.p()](../../d8/d42/classautomotive__design_1_1axis2__placement__3d.html#aab66cdd3e3219a485a1d700a6bc8661f),
[config_control_design.axis2_placement_2d.p()](../../dd/d34/classconfig__control__design_1_1axis2__placement__2d.html#a7286aa583fd5c79398ac8521a937cb6b),
[config_control_design.axis2_placement_3d.p()](../../dd/d2a/classconfig__control__design_1_1axis2__placement__3d.html#ad2a448d4e07c9eb37ecd1abd490de827),
[automotive_design.axis2_placement_3d.wr3()](../../d8/d42/classautomotive__design_1_1axis2__placement__3d.html#aef9f7d5b239a07bf44a95014ce73b61d),
[config_control_design.axis2_placement_3d.wr3()](../../dd/d2a/classconfig__control__design_1_1axis2__placement__3d.html#aea36ab2e3de9512bb5d028dfeaea109b),
[automotive_design.axis2_placement_3d.wr4()](../../d8/d42/classautomotive__design_1_1axis2__placement__3d.html#a958dfcfe4ab4e5a077320cb4e34bbb4d),
and
[config_control_design.axis2_placement_3d.wr4()](../../dd/d2a/classconfig__control__design_1_1axis2__placement__3d.html#a8bec18bae8e6717f6914141ff0f73deb).

## ◆ wr1()

def automotive_design.axis2_placement_2d.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.geometric_representation_item](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#a9677d2be5fc5c7c8ccb6819380198bbc).

## Member Data Documentation

## ◆ dim

automotive_design.axis2_placement_2d.dim  
---  
  
Referenced by
[ifc4.ifccartesiantransformationoperator3d.axis3is3d()](../../d0/d2f/classifc4_1_1ifccartesiantransformationoperator3d.html#ad896e8cc3cd14db5cdcec81e4786eec1),
[ifc4.ifcaxis2placement3d.axisis3d()](../../d1/db1/classifc4_1_1ifcaxis2placement3d.html#ab2f3c3d035505e73f4c12cbceeeae151),
[ifc2x3.ifcsweptsurface.dim()](../../d6/df8/classifc2x3_1_1ifcsweptsurface.html#a5eb3187a1e204615771d1c71c0e05346),
[ifc2x3.ifcplacement.dim()](../../dd/dfd/classifc2x3_1_1ifcplacement.html#ac4dbcef9f43207432d3fa6d838dbdfb7),
[ifc2x3.ifccartesiantransformationoperator.dim()](../../d8/d5d/classifc2x3_1_1ifccartesiantransformationoperator.html#ad46e1f75ce8f2e0d1937c900059809bb),
[ifc2x3.ifccurveboundedplane.dim()](../../d2/dff/classifc2x3_1_1ifccurveboundedplane.html#a4b77cf901367c1cd92ffe6ef787c2f69),
[ifc2x3.ifccompositecurvesegment.dim()](../../dd/d6e/classifc2x3_1_1ifccompositecurvesegment.html#a6014167f48b54f55af87dec16702de32),
[ifc2x3.ifcgeometricset.dim()](../../dc/dab/classifc2x3_1_1ifcgeometricset.html#af569a780b93b69b4dce81b08ddd66f89),
[ifc2x3.ifcrectangulartrimmedsurface.dim()](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#a9864cd346a9caa1e4e8cf5a282192889),
[ifc2x3.ifcbooleanresult.dim()](../../dd/d21/classifc2x3_1_1ifcbooleanresult.html#aa2c029e00fa7348f4841b70fb651f921),
[ifc2x3.ifcelementarysurface.dim()](../../dc/d78/classifc2x3_1_1ifcelementarysurface.html#aa9fc1e4bb64357615bba0ad16fa6bc10),
[ifc2x3.ifcpointoncurve.dim()](../../d4/dfb/classifc2x3_1_1ifcpointoncurve.html#a97ff0b230b758d8c719d3dbe23a653a8),
[ifc2x3.ifcpointonsurface.dim()](../../d0/d83/classifc2x3_1_1ifcpointonsurface.html#a470f7e831cabe7ab72d99a5afbcb5906),
[ifc2x3.ifcvector.dim()](../../d3/d7f/classifc2x3_1_1ifcvector.html#acba206090ebaf1068c18b522050ab356),
[ifc4.ifccompositecurvesegment.dim()](../../da/d5c/classifc4_1_1ifccompositecurvesegment.html#af5316372982441eb627ec543094e86aa),
[ifc4.ifcplacement.dim()](../../d4/da3/classifc4_1_1ifcplacement.html#a4ff119d99b8ac53bebec7145128d0452),
[ifc4.ifccartesiantransformationoperator.dim()](../../d4/d39/classifc4_1_1ifccartesiantransformationoperator.html#a0a344ffdcb72a602de421822f59573dc),
[ifc4.ifcgeometricset.dim()](../../d1/d95/classifc4_1_1ifcgeometricset.html#a795b14ef2879e9acc0c066d66e122b9b),
[ifc4.ifcbooleanresult.dim()](../../d0/d2c/classifc4_1_1ifcbooleanresult.html#aa87cd3a0d4ac5e137c88d13ce336ba19),
[ifc4.ifcpointoncurve.dim()](../../d3/d46/classifc4_1_1ifcpointoncurve.html#ab0edcecba3e98c552d95d8ec2cbfd963),
[ifc4.ifcpointonsurface.dim()](../../d5/df4/classifc4_1_1ifcpointonsurface.html#a400416d6b069afa2e89e5d43ec6a37f1),
[ifc4.ifcvector.dim()](../../d0/d94/classifc4_1_1ifcvector.html#a472491a5b13134e67210054e2ac45890),
[ifc4.ifcaxis2placement3d.refdiris3d()](../../d1/db1/classifc4_1_1ifcaxis2placement3d.html#a2249e08fb14d97b33009f9638979ba10),
[ifc4.ifcfillareastylehatching.refhatchline2d()](../../d3/d40/classifc4_1_1ifcfillareastylehatching.html#a775eb971d46de59a558c12d4cbf073d2),
[automotive_design.axis2_placement_3d.wr2()](../../d8/d42/classautomotive__design_1_1axis2__placement__3d.html#a53e4146e50cdc12f6f425f5ae2a015e7),
[config_control_design.axis2_placement_3d.wr2()](../../dd/d2a/classconfig__control__design_1_1axis2__placement__3d.html#a8510a502b056a9261c4b9cf7323f51b4),
[ifc2x3.ifcaxis2placement3d.wr2()](../../d8/dbf/classifc2x3_1_1ifcaxis2placement3d.html#aab8fcc584ec7c8fa06ffd345c95b8663),
[ifc2x3.ifcfillareastylehatching.wr23()](../../da/d61/classifc2x3_1_1ifcfillareastylehatching.html#a8a321538b336a12f4d031b3c01cb3784),
[automotive_design.axis2_placement_3d.wr3()](../../d8/d42/classautomotive__design_1_1axis2__placement__3d.html#aef9f7d5b239a07bf44a95014ce73b61d),
[config_control_design.axis2_placement_3d.wr3()](../../dd/d2a/classconfig__control__design_1_1axis2__placement__3d.html#aea36ab2e3de9512bb5d028dfeaea109b),
[ifc2x3.ifcaxis2placement3d.wr3()](../../d8/dbf/classifc2x3_1_1ifcaxis2placement3d.html#a6df2d82e8ad19735331147ae1689c8be),
and
[ifc2x3.ifccartesiantransformationoperator3d.wr4()](../../de/d03/classifc2x3_1_1ifccartesiantransformationoperator3d.html#a68b1818b4a81ee6941337c29f3f4d8d7).

## ◆ ref_direction

automotive_design.axis2_placement_2d.ref_direction  
---  
  
Referenced by
[automotive_design.axis2_placement_2d.p()](../../de/df8/classautomotive__design_1_1axis2__placement__2d.html#a486597a463ad5c1866464ec6472bfb63),
[automotive_design.axis2_placement_3d.p()](../../d8/d42/classautomotive__design_1_1axis2__placement__3d.html#aab66cdd3e3219a485a1d700a6bc8661f),
[config_control_design.axis2_placement_2d.p()](../../dd/d34/classconfig__control__design_1_1axis2__placement__2d.html#a7286aa583fd5c79398ac8521a937cb6b),
[config_control_design.axis2_placement_3d.p()](../../dd/d2a/classconfig__control__design_1_1axis2__placement__3d.html#ad2a448d4e07c9eb37ecd1abd490de827),
[automotive_design.axis2_placement_3d.wr3()](../../d8/d42/classautomotive__design_1_1axis2__placement__3d.html#aef9f7d5b239a07bf44a95014ce73b61d),
[config_control_design.axis2_placement_3d.wr3()](../../dd/d2a/classconfig__control__design_1_1axis2__placement__3d.html#aea36ab2e3de9512bb5d028dfeaea109b),
[automotive_design.axis2_placement_3d.wr4()](../../d8/d42/classautomotive__design_1_1axis2__placement__3d.html#a958dfcfe4ab4e5a077320cb4e34bbb4d),
and
[config_control_design.axis2_placement_3d.wr4()](../../dd/d2a/classconfig__control__design_1_1axis2__placement__3d.html#a8bec18bae8e6717f6914141ff0f73deb).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

