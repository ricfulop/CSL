---
url: https://freecad.github.io/SourceDoc/df/dcb/classautomotive__design_1_1annotation__plane.html
scraped_at: 2025-09-08T14:59:38.676679
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [annotation_plane](../../df/dcb/classautomotive__design_1_1annotation__plane.html)

[List of all members](../../dc/da1/classautomotive__design_1_1annotation__plane-members.html) | Public Member Functions | Public Attributes

automotive_design.annotation_plane Class Reference

##  Public Member Functions  
  
---  
def | [elements](../../df/dcb/classautomotive__design_1_1annotation__plane.html#a6b3601b1e53af0685aea025b43b4d6d4) ()  
def | [styled_item_item](../../df/dcb/classautomotive__design_1_1annotation__plane.html#ad0d4079789ee15d19fe05a81bc021094) ()  
def | [wr1](../../df/dcb/classautomotive__design_1_1annotation__plane.html#ad19475f567f313205f1412f9e01e5c5f) (self)  
def | [wr2](../../df/dcb/classautomotive__design_1_1annotation__plane.html#ac0d719a768e40f09fe7b37a8181fd614) (self)  
def | [wr3](../../df/dcb/classautomotive__design_1_1annotation__plane.html#a8666f515b5da47a5476219736f39a010) (self)  
def | [wr4](../../df/dcb/classautomotive__design_1_1annotation__plane.html#a9c405c226390be9640e929de515a3e39) (self)  
def | [wr1](../../d1/d82/classautomotive__design_1_1annotation__occurrence.html#a1d53f8edfd0b54fd137032bdf5e7a508) (self)  
def | [wr2](../../d1/d82/classautomotive__design_1_1annotation__occurrence.html#af1afcd5eb3e329fd929a8a20c1bce00d) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.styled_item](../../dd/d39/classautomotive__design_1_1styled__item.html)  
def | [item](../../dd/d39/classautomotive__design_1_1styled__item.html#a1ca47f0662afee60e3d092187972d692) ()  
def | [styles](../../dd/d39/classautomotive__design_1_1styled__item.html#adddc1c1e338ae95a29f5e9525d5d24f7) ()  
def | [wr1](../../dd/d39/classautomotive__design_1_1styled__item.html#a150262e278f8248839d7cddb3ade3d26) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
def | [name](../../d3/d20/classautomotive__design_1_1representation__item.html#a33b5812d92aa0d107b4fd4274c17b9d9) ()  
def | [wr1](../../d3/d20/classautomotive__design_1_1representation__item.html#af350c19fc5e5763d4991494a99d979ed) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.geometric_representation_item](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html)  
def | [dim](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#aef245618450610e88788dcaea46ad742) ()  
def | [wr1](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#a9677d2be5fc5c7c8ccb6819380198bbc) (self)  
  
##  Public Attributes  
  
---  
|
[dim](../../df/dcb/classautomotive__design_1_1annotation__plane.html#ab82715944ac0274737cd9436043788ef)  
|
[elements](../../df/dcb/classautomotive__design_1_1annotation__plane.html#a73656954e26a599a5b6dd85b8557d59d)  
|
[styled_item_item](../../df/dcb/classautomotive__design_1_1annotation__plane.html#a88874961749c88cedd7bde8a216a4812)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.styled_item](../../dd/d39/classautomotive__design_1_1styled__item.html)  
|
[item](../../dd/d39/classautomotive__design_1_1styled__item.html#aad87aa33fdbad670cc9dfcfdbe866d79)  
|
[styles](../../dd/d39/classautomotive__design_1_1styled__item.html#a715f59d8d13c21ae1a5c704b0dbdbebb)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity annotation_plane definition.
    
        :param elements
        :type elements:SET(1,None,'annotation_plane_element', scope = schema_scope)
    
        :param styled_item_item
        :type styled_item_item:plane_or_planar_box

## Member Function Documentation

## ◆ elements()

def automotive_design.annotation_plane.elements  | ( | | ) |   
---|---|---|---|---  
  
References SMESH_ProxyMesh::SubMesh._elements, ElementBndBoxTree._elements,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.derived_unit._elements,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.data_environment._elements,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.procedural_representation_sequence._elements,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.annotation_plane._elements,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.geometric_set._elements,
automotive_design.data_environment._elements,
automotive_design.derived_unit._elements,
automotive_design.annotation_plane._elements,
automotive_design.geometric_set._elements,
config_control_design.geometric_set._elements,
ifc2x3.ifcgeometricset._elements, ifc2x3.ifcderivedunit._elements,
ifc4.ifcgeometricset._elements, and ifc4.ifcderivedunit._elements.

Referenced by
[ifc2x3.ifcgeometricset.dim()](../../dc/dab/classifc2x3_1_1ifcgeometricset.html#af569a780b93b69b4dce81b08ddd66f89),
[ifc4.ifcgeometricset.dim()](../../d1/d95/classifc4_1_1ifcgeometricset.html#a795b14ef2879e9acc0c066d66e122b9b),
[ifc2x3.ifcderivedunit.dimensions()](../../d1/d87/classifc2x3_1_1ifcderivedunit.html#abfb7d2614cbad7ba363d5b3c5eb5d470),
[ifc4.ifcderivedunit.dimensions()](../../d3/d76/classifc4_1_1ifcderivedunit.html#aa316302961670925c24a6da591f61b31),
[automotive_design.derived_unit.wr1()](../../dc/d0d/classautomotive__design_1_1derived__unit.html#a0f657919a22adecb60367513268f0487),
[ifc2x3.ifcderivedunit.wr1()](../../d1/d87/classifc2x3_1_1ifcderivedunit.html#a9187776e238d15570720320bf6875864),
and
[ifc4.ifcderivedunit.wr1()](../../d3/d76/classifc4_1_1ifcderivedunit.html#a3c29186705cf96c60831affaf117186e).

## ◆ styled_item_item()

def automotive_design.annotation_plane.styled_item_item  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.annotation_fill_area_occurrence._styled_item_item,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.annotation_symbol_occurrence._styled_item_item,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.annotation_curve_occurrence._styled_item_item,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.hidden_element_over_riding_styled_item._styled_item_item,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.annotation_plane._styled_item_item,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.annotation_text_occurrence._styled_item_item,
automotive_design.annotation_fill_area_occurrence._styled_item_item,
automotive_design.annotation_symbol_occurrence._styled_item_item,
automotive_design.annotation_curve_occurrence._styled_item_item,
automotive_design.annotation_plane._styled_item_item,
automotive_design.annotation_text_occurrence._styled_item_item, and
[automotive_design.plane_or_planar_box](../../d4/ddf/namespaceautomotive__design.html#ad9f5a27f1f752c6f234421cb24aafcdb).

## ◆ wr1()

def automotive_design.annotation_plane.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.annotation_occurrence](../../d1/d82/classautomotive__design_1_1annotation__occurrence.html#a1d53f8edfd0b54fd137032bdf5e7a508).

## ◆ wr2()

def automotive_design.annotation_plane.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.annotation_occurrence](../../d1/d82/classautomotive__design_1_1annotation__occurrence.html#af1afcd5eb3e329fd929a8a20c1bce00d).

References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## ◆ wr3()

def automotive_design.annotation_plane.wr3  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, Gui::Dialog::DownloadManager.self,
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.styles](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#a839aa1511527efa11396af742b9242b8),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.styled_item.styles,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.presentation_style_assignment.styles,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_side_style.styles,
[automotive_design.styled_item.styles](../../dd/d39/classautomotive__design_1_1styled__item.html#a715f59d8d13c21ae1a5c704b0dbdbebb),
[automotive_design.presentation_style_assignment.styles](../../de/def/classautomotive__design_1_1presentation__style__assignment.html#afeadbcbca8fe5c8bc8ad9964a77d6288),
[automotive_design.surface_side_style.styles](../../d6/d9d/classautomotive__design_1_1surface__side__style.html#ae2526492db4ab8a9fee66c3b0e6e286b),
[ifc2x3.ifcstyleditem.styles](../../d4/d21/classifc2x3_1_1ifcstyleditem.html#a92b1897ad683c2691b84a7527793f5f7),
[ifc2x3.ifcpresentationstyleassignment.styles](../../dc/d3e/classifc2x3_1_1ifcpresentationstyleassignment.html#a832304e6a91c9585dd3700eef29e70d0),
[ifc2x3.ifcsurfacestyle.styles](../../d0/d96/classifc2x3_1_1ifcsurfacestyle.html#a2a4f22d766a599ba4b4e95db7ced6154),
[ifc4.ifcpresentationstyleassignment.styles](../../d6/d8b/classifc4_1_1ifcpresentationstyleassignment.html#a8a096c963ffd6eabf177fc4497d10ff5),
[ifc4.ifcstyleditem.styles](../../da/db5/classifc4_1_1ifcstyleditem.html#aac77487fa26a4b30bfad1ce34bb93181),
and
[ifc4.ifcsurfacestyle.styles](../../d2/d7e/classifc4_1_1ifcsurfacestyle.html#a21f7510674db65c6379e6b118ca68cc3).

## ◆ wr4()

def automotive_design.annotation_plane.wr4  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, Gui::Dialog::DownloadManager.self,
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.styles](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#a839aa1511527efa11396af742b9242b8),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.styled_item.styles,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.presentation_style_assignment.styles,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_side_style.styles,
[automotive_design.styled_item.styles](../../dd/d39/classautomotive__design_1_1styled__item.html#a715f59d8d13c21ae1a5c704b0dbdbebb),
[automotive_design.presentation_style_assignment.styles](../../de/def/classautomotive__design_1_1presentation__style__assignment.html#afeadbcbca8fe5c8bc8ad9964a77d6288),
[automotive_design.surface_side_style.styles](../../d6/d9d/classautomotive__design_1_1surface__side__style.html#ae2526492db4ab8a9fee66c3b0e6e286b),
[ifc2x3.ifcstyleditem.styles](../../d4/d21/classifc2x3_1_1ifcstyleditem.html#a92b1897ad683c2691b84a7527793f5f7),
[ifc2x3.ifcpresentationstyleassignment.styles](../../dc/d3e/classifc2x3_1_1ifcpresentationstyleassignment.html#a832304e6a91c9585dd3700eef29e70d0),
[ifc2x3.ifcsurfacestyle.styles](../../d0/d96/classifc2x3_1_1ifcsurfacestyle.html#a2a4f22d766a599ba4b4e95db7ced6154),
[ifc4.ifcpresentationstyleassignment.styles](../../d6/d8b/classifc4_1_1ifcpresentationstyleassignment.html#a8a096c963ffd6eabf177fc4497d10ff5),
[ifc4.ifcstyleditem.styles](../../da/db5/classifc4_1_1ifcstyleditem.html#aac77487fa26a4b30bfad1ce34bb93181),
and
[ifc4.ifcsurfacestyle.styles](../../d2/d7e/classifc4_1_1ifcsurfacestyle.html#a21f7510674db65c6379e6b118ca68cc3).

## Member Data Documentation

## ◆ dim

automotive_design.annotation_plane.dim  
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

## ◆ elements

automotive_design.annotation_plane.elements  
---  
  
Referenced by
[ifc2x3.ifcgeometricset.dim()](../../dc/dab/classifc2x3_1_1ifcgeometricset.html#af569a780b93b69b4dce81b08ddd66f89),
[ifc4.ifcgeometricset.dim()](../../d1/d95/classifc4_1_1ifcgeometricset.html#a795b14ef2879e9acc0c066d66e122b9b),
[ifc2x3.ifcderivedunit.dimensions()](../../d1/d87/classifc2x3_1_1ifcderivedunit.html#abfb7d2614cbad7ba363d5b3c5eb5d470),
[ifc4.ifcderivedunit.dimensions()](../../d3/d76/classifc4_1_1ifcderivedunit.html#aa316302961670925c24a6da591f61b31),
[automotive_design.derived_unit.wr1()](../../dc/d0d/classautomotive__design_1_1derived__unit.html#a0f657919a22adecb60367513268f0487),
[ifc2x3.ifcderivedunit.wr1()](../../d1/d87/classifc2x3_1_1ifcderivedunit.html#a9187776e238d15570720320bf6875864),
and
[ifc4.ifcderivedunit.wr1()](../../d3/d76/classifc4_1_1ifcderivedunit.html#a3c29186705cf96c60831affaf117186e).

## ◆ styled_item_item

automotive_design.annotation_plane.styled_item_item  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

