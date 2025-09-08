---
url: https://freecad.github.io/SourceDoc/d3/d18/classconfig__control__design_1_1geometric__representation__item.html
scraped_at: 2025-09-08T15:21:59.275655
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [geometric_representation_item](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html)

[List of all members](../../d7/d26/classconfig__control__design_1_1geometric__representation__item-members.html) | Public Member Functions

config_control_design.geometric_representation_item Class Reference

##  Public Member Functions  
  
---  
def | [dim](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html#aac385fb99d009b699d0d77f10ebdc5f1) ()  
def | [wr1](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html#a779ebde9495ea4132b585e06aa418f13) (self)  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
def | [name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a5ea878073c85170f328deff23a9c5732) ()  
def | [wr1](../../d9/d69/classconfig__control__design_1_1representation__item.html#a4cdc1db49341dedc8f271ec89801c713) (self)  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
|
[name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a0e8be677f8410825a46422f3c0e1c128)  
  
## Detailed Description

    
    
    Entity geometric_representation_item definition.
    
        :param dim
        :type dim:dimension_count

## Member Function Documentation

## ◆ dim()

def config_control_design.geometric_representation_item.dim  | ( | | ) |   
---|---|---|---|---  
  
References
[config_control_design.dimension_of()](../../d4/d07/namespaceconfig__control__design.html#aa7236ac2cdbbb5059f5e542e1dbdf94d).

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

## ◆ wr1()

def config_control_design.geometric_representation_item.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html#a4cdc1db49341dedc8f271ec89801c713).

Reimplemented in
[config_control_design.cartesian_transformation_operator](../../d5/de5/classconfig__control__design_1_1cartesian__transformation__operator.html#a06437e2bc2271b9f251dae4e14d9519a),
[config_control_design.cartesian_transformation_operator_3d](../../dc/d92/classconfig__control__design_1_1cartesian__transformation__operator__3d.html#afd21097debcae9ba535fbee796734773),
[config_control_design.axis2_placement_2d](../../dd/d34/classconfig__control__design_1_1axis2__placement__2d.html#a7dd500bbf8d664b900aa90b7e10b0926),
[config_control_design.b_spline_surface](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a7b8fa4169157c5e5b779fdc1bfbbeb97),
[config_control_design.axis1_placement](../../d7/df7/classconfig__control__design_1_1axis1__placement.html#a2b3bad17a685bd44d94f254992a1a550),
[config_control_design.b_spline_curve](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#a398f92dc8b064539c2a505afbeb470de),
[config_control_design.rational_b_spline_curve](../../d2/d28/classconfig__control__design_1_1rational__b__spline__curve.html#ad450bf462f3eef07955850c3c609d71e),
[config_control_design.direction](../../da/d18/classconfig__control__design_1_1direction.html#a45700758912614fe3500bab0b19f8605),
[config_control_design.offset_curve_3d](../../dd/d91/classconfig__control__design_1_1offset__curve__3d.html#a5ccb88f0704f55ee73895137c7972ef2),
[config_control_design.composite_curve](../../d9/d22/classconfig__control__design_1_1composite__curve.html#a7adb0598ad5498f569df00d0632714ec),
[config_control_design.composite_curve_on_surface](../../da/d0c/classconfig__control__design_1_1composite__curve__on__surface.html#af1248e63f087994050d924b1f03ce2a7),
[config_control_design.boundary_curve](../../d4/d2f/classconfig__control__design_1_1boundary__curve.html#afe5e4e7932ec2ddaf7af41d9cacffcb6),
[config_control_design.curve_replica](../../db/d4a/classconfig__control__design_1_1curve__replica.html#ab244c22fdebf9081049a991c17f447d3),
[config_control_design.surface_curve](../../db/d04/classconfig__control__design_1_1surface__curve.html#a8c14cc35e33593ad00bb6b6d4d561cf9),
[config_control_design.parabola](../../d8/dcc/classconfig__control__design_1_1parabola.html#a23d0a36c703b93d69edf39a1bab8d238),
[config_control_design.rectangular_composite_surface](../../df/d23/classconfig__control__design_1_1rectangular__composite__surface.html#ac31aeab4af00b3f915b8d9d8efa69acb),
[config_control_design.shell_based_surface_model](../../dd/d19/classconfig__control__design_1_1shell__based__surface__model.html#af0fbce04fb6437b9d9ca476a5125ee73),
[config_control_design.vector](../../dc/d96/classconfig__control__design_1_1vector.html#a3afca0b28ec6498757c78eeca7c67b63),
[config_control_design.pcurve](../../d8/d67/classconfig__control__design_1_1pcurve.html#a081b5cdb8f8e42e856b54ca97fe9ba05),
[config_control_design.bounded_pcurve](../../db/dc7/classconfig__control__design_1_1bounded__pcurve.html#a4a82e5a675f172f3dc9b69cfa1c63bcb),
[config_control_design.intersection_curve](../../df/dd2/classconfig__control__design_1_1intersection__curve.html#a458c1aeb30e18e9d134998999b91248a),
[config_control_design.trimmed_curve](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#a2b4039eecdc53fc8dcb5cf94498f84dc),
[config_control_design.bounded_surface_curve](../../df/d5b/classconfig__control__design_1_1bounded__surface__curve.html#a5e85388765ed34c1e72173fc6e784624),
[config_control_design.shell_based_wireframe_model](../../dc/d93/classconfig__control__design_1_1shell__based__wireframe__model.html#ab7558c4c1f67f3e961b75968c0346c35),
[config_control_design.degenerate_toroidal_surface](../../df/dad/classconfig__control__design_1_1degenerate__toroidal__surface.html#ace3808e03b5d62b58c8b281839737b57),
[config_control_design.point_replica](../../d1/d7b/classconfig__control__design_1_1point__replica.html#ad2a02dc48666cf2068acff14ba8f5a70),
[config_control_design.rectangular_trimmed_surface](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a44a102b137d46fed49015ee7810a342b),
[config_control_design.line](../../d6/def/classconfig__control__design_1_1line.html#a3970abe56dda491e515ceeb4200b6a4c),
[config_control_design.geometric_curve_set](../../db/df5/classconfig__control__design_1_1geometric__curve__set.html#a064055181be36e349c6f269043e9db61),
[config_control_design.degenerate_pcurve](../../d3/d07/classconfig__control__design_1_1degenerate__pcurve.html#aae1772a95d3ed412ea932efd74ac2697),
[config_control_design.curve_bounded_surface](../../dc/d61/classconfig__control__design_1_1curve__bounded__surface.html#a2ec204f7adf74d242473768dff1f8e54),
[config_control_design.b_spline_curve_with_knots](../../d2/dc3/classconfig__control__design_1_1b__spline__curve__with__knots.html#a670e34aa43e8c3d276bf8a7df99f1d94),
[config_control_design.seam_curve](../../d7/d68/classconfig__control__design_1_1seam__curve.html#a84a4020f6d803bfad517b36cdd1558bb),
[config_control_design.axis2_placement_3d](../../dd/d2a/classconfig__control__design_1_1axis2__placement__3d.html#aefbd820c543c76fbbec4bcf974bb46aa),
[config_control_design.rational_b_spline_surface](../../df/da0/classconfig__control__design_1_1rational__b__spline__surface.html#a21c1bb1a384a79e5ef50126d0c2cb71c),
[config_control_design.b_spline_surface_with_knots](../../d9/d81/classconfig__control__design_1_1b__spline__surface__with__knots.html#abe07d58f15c35095876483703b505fa9),
[config_control_design.advanced_face](../../db/d65/classconfig__control__design_1_1advanced__face.html#a479a609264b1ca2e70775476f690681e),
[config_control_design.surface_replica](../../d5/d47/classconfig__control__design_1_1surface__replica.html#a1f82b4551b739b2e449d70bf30032d9b),
and
[config_control_design.conical_surface](../../de/d42/classconfig__control__design_1_1conical__surface.html#a92e0d1af17bf8d262fe664d42024cc3e).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

