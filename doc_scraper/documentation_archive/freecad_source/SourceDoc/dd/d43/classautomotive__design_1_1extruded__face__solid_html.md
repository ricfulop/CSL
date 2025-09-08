---
url: https://freecad.github.io/SourceDoc/dd/d43/classautomotive__design_1_1extruded__face__solid.html
scraped_at: 2025-09-08T15:05:23.089773
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [extruded_face_solid](../../dd/d43/classautomotive__design_1_1extruded__face__solid.html)

[List of all members](../../db/d91/classautomotive__design_1_1extruded__face__solid-members.html) | Public Member Functions | Public Attributes

automotive_design.extruded_face_solid Class Reference

##  Public Member Functions  
  
---  
def | [depth](../../dd/d43/classautomotive__design_1_1extruded__face__solid.html#ad5f88b9b05a01672a156daedf840c8ed) ()  
def | [extruded_direction](../../dd/d43/classautomotive__design_1_1extruded__face__solid.html#a2d5a2cd1f45e5337703720305dc9dc93) ()  
def | [wr1](../../dd/d43/classautomotive__design_1_1extruded__face__solid.html#a2fcf5f4e98797a0fddb17a49ae0b5591) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.swept_face_solid](../../d1/d64/classautomotive__design_1_1swept__face__solid.html)  
def | [swept_face](../../d1/d64/classautomotive__design_1_1swept__face__solid.html#aa66713ac491c44290176d613289d2872) ()  
def | [wr1](../../d1/d64/classautomotive__design_1_1swept__face__solid.html#a6ba90dcc401b0d407dd0ba8128a71e4f) (self)  
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
[depth](../../dd/d43/classautomotive__design_1_1extruded__face__solid.html#abe73b14cf36fa66cec4cb512d4364c24)  
|
[extruded_direction](../../dd/d43/classautomotive__design_1_1extruded__face__solid.html#a1a1cf34e45d40e52cd99d5883b809db1)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.swept_face_solid](../../d1/d64/classautomotive__design_1_1swept__face__solid.html)  
|
[swept_face](../../d1/d64/classautomotive__design_1_1swept__face__solid.html#ae3ab19b94fa38ab7330d319128a88152)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity extruded_face_solid definition.
    
        :param extruded_direction
        :type extruded_direction:direction
    
        :param depth
        :type depth:positive_length_measure

## Member Function Documentation

## ◆ depth()

def automotive_design.extruded_face_solid.depth  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.solid_with_depression._depth,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.extruded_face_solid._depth,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.extruded_area_solid._depth,
automotive_design.extruded_face_solid._depth,
automotive_design.extruded_area_solid._depth,
ifc2x3.ifczshapeprofiledef._depth, ifc2x3.ifcushapeprofiledef._depth,
ifc2x3.ifctshapeprofiledef._depth, ifc2x3.ifcsurfaceoflinearextrusion._depth,
ifc2x3.ifcextrudedareasolid._depth, ifc2x3.ifccshapeprofiledef._depth,
ifc2x3.ifclshapeprofiledef._depth, ifc4.ifczshapeprofiledef._depth,
ifc4.ifcushapeprofiledef._depth, ifc4.ifctshapeprofiledef._depth,
ifc4.ifcsurfaceoflinearextrusion._depth, ifc4.ifcextrudedareasolid._depth,
ifc4.ifccshapeprofiledef._depth, and ifc4.ifclshapeprofiledef._depth.

Referenced by
[ifc4.ifcsurfaceoflinearextrusion.depthgreaterzero()](../../d5/d08/classifc4_1_1ifcsurfaceoflinearextrusion.html#a7231ce58b4b294ea71815d6de2313ac0),
[ifc2x3.ifcsurfaceoflinearextrusion.extrusionaxis()](../../de/d03/classifc2x3_1_1ifcsurfaceoflinearextrusion.html#a53e1943c83dc089f88243732dbafd31f),
[ifc4.ifcsurfaceoflinearextrusion.extrusionaxis()](../../d5/d08/classifc4_1_1ifcsurfaceoflinearextrusion.html#a0838104d3debceababb835373da34aa6),
[ifc4.ifczshapeprofiledef.validflangethickness()](../../d7/d0a/classifc4_1_1ifczshapeprofiledef.html#a240bf3917a4fbcd9b7e7870ca5778224),
[ifc4.ifcushapeprofiledef.validflangethickness()](../../dd/d5b/classifc4_1_1ifcushapeprofiledef.html#a08506a07249eca41be91b0dbf95308b7),
[ifc4.ifctshapeprofiledef.validflangethickness()](../../d5/db9/classifc4_1_1ifctshapeprofiledef.html#a2c806b36c6f8681dc3e2987278be48df),
[ifc4.ifccshapeprofiledef.validgirth()](../../de/d67/classifc4_1_1ifccshapeprofiledef.html#ad9b540de93b41012c5c0e9b4891df830),
[ifc4.ifccshapeprofiledef.validinternalfilletradius()](../../de/d67/classifc4_1_1ifccshapeprofiledef.html#a47a971a97096964be416735e4f5a23c1),
[ifc4.ifclshapeprofiledef.validthickness()](../../d9/da2/classifc4_1_1ifclshapeprofiledef.html#a1050493838fdcc2d82f333bc6c1ee2e5),
[ifc4.ifccshapeprofiledef.validwallthickness()](../../de/d67/classifc4_1_1ifccshapeprofiledef.html#a2d860c3545893249fd0329005265d22c),
[ifc2x3.ifctshapeprofiledef.wr1()](../../d4/dd9/classifc2x3_1_1ifctshapeprofiledef.html#ad7e07acb622115f1abd5cc5c11214511),
[ifc2x3.ifccshapeprofiledef.wr1()](../../d3/d77/classifc2x3_1_1ifccshapeprofiledef.html#a5b75b6e6b93b6c3e1c93d9e85a856c86),
[ifc2x3.ifccshapeprofiledef.wr2()](../../d3/d77/classifc2x3_1_1ifccshapeprofiledef.html#a47e987af28a25df6cb441cd6ffb2d322),
[ifc2x3.ifczshapeprofiledef.wr21()](../../df/dad/classifc2x3_1_1ifczshapeprofiledef.html#aad3af74d6aa9f937294b3f7df6905216),
[ifc2x3.ifcushapeprofiledef.wr21()](../../d8/d7f/classifc2x3_1_1ifcushapeprofiledef.html#a5380b8a148febcd6cc1801a2b1be7f30),
[ifc2x3.ifclshapeprofiledef.wr21()](../../dc/da1/classifc2x3_1_1ifclshapeprofiledef.html#a4bd745dfc32fd6bc52fd97a41a19d8e1),
[ifc2x3.ifccshapeprofiledef.wr3()](../../d3/d77/classifc2x3_1_1ifccshapeprofiledef.html#aebc8c91c25b4c261345e2fea631a88e7),
and
[ifc2x3.ifcsurfaceoflinearextrusion.wr41()](../../de/d03/classifc2x3_1_1ifcsurfaceoflinearextrusion.html#ab305102fbded6830f159564385bfccac).

## ◆ extruded_direction()

def automotive_design.extruded_face_solid.extruded_direction  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.extruded_face_solid._extruded_direction,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.extruded_area_solid._extruded_direction,
automotive_design.extruded_face_solid._extruded_direction, and
automotive_design.extruded_area_solid._extruded_direction.

Referenced by
[automotive_design.extruded_face_solid.wr1()](../../dd/d43/classautomotive__design_1_1extruded__face__solid.html#a2fcf5f4e98797a0fddb17a49ae0b5591),
and
[automotive_design.extruded_area_solid.wr1()](../../db/d70/classautomotive__design_1_1extruded__area__solid.html#a1d3bf9a15a698b5deb63e5889b37f152).

## ◆ wr1()

def automotive_design.extruded_face_solid.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.swept_face_solid](../../d1/d64/classautomotive__design_1_1swept__face__solid.html#a6ba90dcc401b0d407dd0ba8128a71e4f).

References
[automotive_design.dot_product()](../../d4/ddf/namespaceautomotive__design.html#a1042c326649d6596a3d7b8a1c2d32121),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.extruded_face_solid.extruded_direction,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.extruded_area_solid.extruded_direction,
[automotive_design.extruded_face_solid.extruded_direction](../../dd/d43/classautomotive__design_1_1extruded__face__solid.html#a1a1cf34e45d40e52cd99d5883b809db1),
[automotive_design.extruded_area_solid.extruded_direction](../../db/d70/classautomotive__design_1_1extruded__area__solid.html#a7a61c2a85979a1b02a938b85763d1d5f),
App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## Member Data Documentation

## ◆ depth

automotive_design.extruded_face_solid.depth  
---  
  
Referenced by
[ifc4.ifcsurfaceoflinearextrusion.depthgreaterzero()](../../d5/d08/classifc4_1_1ifcsurfaceoflinearextrusion.html#a7231ce58b4b294ea71815d6de2313ac0),
[ifc2x3.ifcsurfaceoflinearextrusion.extrusionaxis()](../../de/d03/classifc2x3_1_1ifcsurfaceoflinearextrusion.html#a53e1943c83dc089f88243732dbafd31f),
[ifc4.ifcsurfaceoflinearextrusion.extrusionaxis()](../../d5/d08/classifc4_1_1ifcsurfaceoflinearextrusion.html#a0838104d3debceababb835373da34aa6),
[ifc4.ifczshapeprofiledef.validflangethickness()](../../d7/d0a/classifc4_1_1ifczshapeprofiledef.html#a240bf3917a4fbcd9b7e7870ca5778224),
[ifc4.ifcushapeprofiledef.validflangethickness()](../../dd/d5b/classifc4_1_1ifcushapeprofiledef.html#a08506a07249eca41be91b0dbf95308b7),
[ifc4.ifctshapeprofiledef.validflangethickness()](../../d5/db9/classifc4_1_1ifctshapeprofiledef.html#a2c806b36c6f8681dc3e2987278be48df),
[ifc4.ifccshapeprofiledef.validgirth()](../../de/d67/classifc4_1_1ifccshapeprofiledef.html#ad9b540de93b41012c5c0e9b4891df830),
[ifc4.ifccshapeprofiledef.validinternalfilletradius()](../../de/d67/classifc4_1_1ifccshapeprofiledef.html#a47a971a97096964be416735e4f5a23c1),
[ifc4.ifclshapeprofiledef.validthickness()](../../d9/da2/classifc4_1_1ifclshapeprofiledef.html#a1050493838fdcc2d82f333bc6c1ee2e5),
[ifc4.ifccshapeprofiledef.validwallthickness()](../../de/d67/classifc4_1_1ifccshapeprofiledef.html#a2d860c3545893249fd0329005265d22c),
[ifc2x3.ifctshapeprofiledef.wr1()](../../d4/dd9/classifc2x3_1_1ifctshapeprofiledef.html#ad7e07acb622115f1abd5cc5c11214511),
[ifc2x3.ifccshapeprofiledef.wr1()](../../d3/d77/classifc2x3_1_1ifccshapeprofiledef.html#a5b75b6e6b93b6c3e1c93d9e85a856c86),
[ifc2x3.ifccshapeprofiledef.wr2()](../../d3/d77/classifc2x3_1_1ifccshapeprofiledef.html#a47e987af28a25df6cb441cd6ffb2d322),
[ifc2x3.ifczshapeprofiledef.wr21()](../../df/dad/classifc2x3_1_1ifczshapeprofiledef.html#aad3af74d6aa9f937294b3f7df6905216),
[ifc2x3.ifcushapeprofiledef.wr21()](../../d8/d7f/classifc2x3_1_1ifcushapeprofiledef.html#a5380b8a148febcd6cc1801a2b1be7f30),
[ifc2x3.ifclshapeprofiledef.wr21()](../../dc/da1/classifc2x3_1_1ifclshapeprofiledef.html#a4bd745dfc32fd6bc52fd97a41a19d8e1),
[ifc2x3.ifccshapeprofiledef.wr3()](../../d3/d77/classifc2x3_1_1ifccshapeprofiledef.html#aebc8c91c25b4c261345e2fea631a88e7),
and
[ifc2x3.ifcsurfaceoflinearextrusion.wr41()](../../de/d03/classifc2x3_1_1ifcsurfaceoflinearextrusion.html#ab305102fbded6830f159564385bfccac).

## ◆ extruded_direction

automotive_design.extruded_face_solid.extruded_direction  
---  
  
Referenced by
[automotive_design.extruded_face_solid.wr1()](../../dd/d43/classautomotive__design_1_1extruded__face__solid.html#a2fcf5f4e98797a0fddb17a49ae0b5591),
and
[automotive_design.extruded_area_solid.wr1()](../../db/d70/classautomotive__design_1_1extruded__area__solid.html#a1d3bf9a15a698b5deb63e5889b37f152).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

