---
url: https://freecad.github.io/SourceDoc/dd/dd4/classautomotive__design_1_1surface__curve.html
scraped_at: 2025-09-08T15:13:27.115512
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [surface_curve](../../dd/dd4/classautomotive__design_1_1surface__curve.html)

[List of all members](../../d3/d74/classautomotive__design_1_1surface__curve-members.html) | Public Member Functions | Public Attributes

automotive_design.surface_curve Class Reference

##  Public Member Functions  
  
---  
def | [associated_geometry](../../dd/dd4/classautomotive__design_1_1surface__curve.html#ae0abe865d39a860da7dcdbd4aee45d64) ()  
def | [basis_surface](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a4124fffa9d613bb72525c9f8ed586d85) ()  
def | [curve_3d](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a81690aed822536fb55166defbcd426b3) ()  
def | [master_representation](../../dd/dd4/classautomotive__design_1_1surface__curve.html#abc79bc01af5643e2337c080530c553f6) ()  
def | [wr1](../../dd/dd4/classautomotive__design_1_1surface__curve.html#ae4ee554add41003d19e419cc8f1a0a7c) (self)  
def | [wr2](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a666ba9430333277fdc71387682655a19) (self)  
def | [wr3](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a2b1b167aaad85df93f2693542797516b) (self)  
def | [wr4](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a6d4fa1fa4fc25313611a2beb48fef749) (self)  
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
[associated_geometry](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a0b784edb8e1c1c89cf424a0a84d7a15d)  
|
[curve_3d](../../dd/dd4/classautomotive__design_1_1surface__curve.html#ad32b76eee423e8aaad977eef8288fdd8)  
|
[dim](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a4fb59134e77c048d5659474dcef5f836)  
|
[master_representation](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a842c7f89f55c0669462a6eea7c17f9ca)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity surface_curve definition.
    
        :param curve_3d
        :type curve_3d:curve
    
        :param associated_geometry
        :type associated_geometry:LIST(1,2,'pcurve_or_surface', scope = schema_scope)
    
        :param master_representation
        :type master_representation:preferred_surface_curve_representation
    
        :param basis_surface
        :type basis_surface:SET(1,2,'surface', scope = schema_scope)

## Member Function Documentation

## ◆ associated_geometry()

def automotive_design.surface_curve.associated_geometry  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_curve._associated_geometry,
automotive_design.surface_curve._associated_geometry, and
config_control_design.surface_curve._associated_geometry.

Referenced by
[automotive_design.surface_curve.wr2()](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a666ba9430333277fdc71387682655a19),
[automotive_design.seam_edge.wr2()](../../d1/d38/classautomotive__design_1_1seam__edge.html#a3e9b6478fcf0b0635c010697146a0435),
[config_control_design.surface_curve.wr2()](../../db/d04/classconfig__control__design_1_1surface__curve.html#ac972c456bb3b774f17987a843b62ac1f),
[automotive_design.surface_curve.wr3()](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a2b1b167aaad85df93f2693542797516b),
and
[config_control_design.surface_curve.wr3()](../../db/d04/classconfig__control__design_1_1surface__curve.html#a82693e1b45e4ec57fe4baf615b283d12).

## ◆ basis_surface()

def automotive_design.surface_curve.basis_surface  | ( | | ) |   
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

## ◆ curve_3d()

def automotive_design.surface_curve.curve_3d  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_curve._curve_3d,
automotive_design.surface_curve._curve_3d, and
config_control_design.surface_curve._curve_3d.

Referenced by
[automotive_design.surface_curve.wr4()](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a6d4fa1fa4fc25313611a2beb48fef749),
and
[config_control_design.surface_curve.wr4()](../../db/d04/classconfig__control__design_1_1surface__curve.html#acc28c023fef6730e88621f524b51de15).

## ◆ master_representation()

def automotive_design.surface_curve.master_representation  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_curve._master_representation,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.trimmed_curve._master_representation,
automotive_design.surface_curve._master_representation,
automotive_design.trimmed_curve._master_representation,
config_control_design.surface_curve._master_representation, and
config_control_design.trimmed_curve._master_representation.

Referenced by
[automotive_design.surface_curve.wr2()](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a666ba9430333277fdc71387682655a19),
[config_control_design.surface_curve.wr2()](../../db/d04/classconfig__control__design_1_1surface__curve.html#ac972c456bb3b774f17987a843b62ac1f),
[automotive_design.surface_curve.wr3()](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a2b1b167aaad85df93f2693542797516b),
and
[config_control_design.surface_curve.wr3()](../../db/d04/classconfig__control__design_1_1surface__curve.html#a82693e1b45e4ec57fe4baf615b283d12).

## ◆ wr1()

def automotive_design.surface_curve.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.geometric_representation_item](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#a9677d2be5fc5c7c8ccb6819380198bbc).

Reimplemented in
[automotive_design.intersection_curve](../../de/d7a/classautomotive__design_1_1intersection__curve.html#a9f776070c2c732f2333688bb480bc02f),
[automotive_design.bounded_surface_curve](../../de/d6d/classautomotive__design_1_1bounded__surface__curve.html#a17d0323c0be110c9d944a1812231c013),
and
[automotive_design.seam_curve](../../da/d9c/classautomotive__design_1_1seam__curve.html#afc4d886ee6af527f72d9c9454a4b9e87).

## ◆ wr2()

def automotive_design.surface_curve.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented in
[automotive_design.intersection_curve](../../de/d7a/classautomotive__design_1_1intersection__curve.html#a26f1c89ec2150a0a1c3ce3b3e75bd852),
and
[automotive_design.seam_curve](../../da/d9c/classautomotive__design_1_1seam__curve.html#aca0b61e2182f795d94a40c40d47e18de).

References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_curve.associated_geometry,
[automotive_design.surface_curve.associated_geometry](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a0b784edb8e1c1c89cf424a0a84d7a15d),
[config_control_design.surface_curve.associated_geometry](../../db/d04/classconfig__control__design_1_1surface__curve.html#adc97ffd2c484d9b33e95ead595c77fd1),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_curve.master_representation,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.trimmed_curve.master_representation,
[automotive_design.surface_curve.master_representation](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a842c7f89f55c0669462a6eea7c17f9ca),
[automotive_design.trimmed_curve.master_representation](../../de/d2b/classautomotive__design_1_1trimmed__curve.html#a797c92353e1bdbf0490bdecc4bb923e8),
[config_control_design.surface_curve.master_representation](../../db/d04/classconfig__control__design_1_1surface__curve.html#a09408a914bf07aa243c315340cd45f28),
and
[config_control_design.trimmed_curve.master_representation](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#aee6252fd9df82fdbfd382ed861d09b61).

## ◆ wr3()

def automotive_design.surface_curve.wr3  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented in
[automotive_design.seam_curve](../../da/d9c/classautomotive__design_1_1seam__curve.html#a166996110e3f76450f7c8875bd12ad35).

References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_curve.associated_geometry,
[automotive_design.surface_curve.associated_geometry](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a0b784edb8e1c1c89cf424a0a84d7a15d),
[config_control_design.surface_curve.associated_geometry](../../db/d04/classconfig__control__design_1_1surface__curve.html#adc97ffd2c484d9b33e95ead595c77fd1),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_curve.master_representation,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.trimmed_curve.master_representation,
[automotive_design.surface_curve.master_representation](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a842c7f89f55c0669462a6eea7c17f9ca),
[automotive_design.trimmed_curve.master_representation](../../de/d2b/classautomotive__design_1_1trimmed__curve.html#a797c92353e1bdbf0490bdecc4bb923e8),
[config_control_design.surface_curve.master_representation](../../db/d04/classconfig__control__design_1_1surface__curve.html#a09408a914bf07aa243c315340cd45f28),
and
[config_control_design.trimmed_curve.master_representation](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#aee6252fd9df82fdbfd382ed861d09b61).

## ◆ wr4()

def automotive_design.surface_curve.wr4  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented in
[automotive_design.seam_curve](../../da/d9c/classautomotive__design_1_1seam__curve.html#a34ba8adb6c911bd5c4134c0221a10e9a).

References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_curve.curve_3d,
[automotive_design.surface_curve.curve_3d](../../dd/dd4/classautomotive__design_1_1surface__curve.html#ad32b76eee423e8aaad977eef8288fdd8),
and
[config_control_design.surface_curve.curve_3d](../../db/d04/classconfig__control__design_1_1surface__curve.html#a0cd961dd93cff214aa64e105c10282b2).

## Member Data Documentation

## ◆ associated_geometry

automotive_design.surface_curve.associated_geometry  
---  
  
Referenced by
[automotive_design.surface_curve.wr2()](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a666ba9430333277fdc71387682655a19),
[automotive_design.seam_edge.wr2()](../../d1/d38/classautomotive__design_1_1seam__edge.html#a3e9b6478fcf0b0635c010697146a0435),
[config_control_design.surface_curve.wr2()](../../db/d04/classconfig__control__design_1_1surface__curve.html#ac972c456bb3b774f17987a843b62ac1f),
[automotive_design.surface_curve.wr3()](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a2b1b167aaad85df93f2693542797516b),
and
[config_control_design.surface_curve.wr3()](../../db/d04/classconfig__control__design_1_1surface__curve.html#a82693e1b45e4ec57fe4baf615b283d12).

## ◆ curve_3d

automotive_design.surface_curve.curve_3d  
---  
  
Referenced by
[automotive_design.surface_curve.wr4()](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a6d4fa1fa4fc25313611a2beb48fef749),
and
[config_control_design.surface_curve.wr4()](../../db/d04/classconfig__control__design_1_1surface__curve.html#acc28c023fef6730e88621f524b51de15).

## ◆ dim

automotive_design.surface_curve.dim  
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

## ◆ master_representation

automotive_design.surface_curve.master_representation  
---  
  
Referenced by
[automotive_design.surface_curve.wr2()](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a666ba9430333277fdc71387682655a19),
[config_control_design.surface_curve.wr2()](../../db/d04/classconfig__control__design_1_1surface__curve.html#ac972c456bb3b774f17987a843b62ac1f),
[automotive_design.surface_curve.wr3()](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a2b1b167aaad85df93f2693542797516b),
and
[config_control_design.surface_curve.wr3()](../../db/d04/classconfig__control__design_1_1surface__curve.html#a82693e1b45e4ec57fe4baf615b283d12).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

