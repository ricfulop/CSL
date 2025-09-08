---
url: https://freecad.github.io/SourceDoc/db/d8b/classautomotive__design_1_1mechanism__base__placement.html
scraped_at: 2025-09-08T15:08:04.756073
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [mechanism_base_placement](../../db/d8b/classautomotive__design_1_1mechanism__base__placement.html)

[List of all members](../../d6/d7d/classautomotive__design_1_1mechanism__base__placement-members.html) | Public Member Functions | Public Attributes

automotive_design.mechanism_base_placement Class Reference

##  Public Member Functions  
  
---  
def | [base_of_mechanism](../../db/d8b/classautomotive__design_1_1mechanism__base__placement.html#ab7c22439703e97e13c0b2e9e96644a6f) ()  
def | [representation_relationship_rep_2](../../db/d8b/classautomotive__design_1_1mechanism__base__placement.html#a2036d6b183b15bb056bf017cb9d261f5) ()  
def | [representation_relationship_with_transformation_transformation_operator](../../db/d8b/classautomotive__design_1_1mechanism__base__placement.html#adedd9b66bacdcc6082c6562c3f9b90cb) ()  
def | [wr1](../../db/d8b/classautomotive__design_1_1mechanism__base__placement.html#aee3cf56f03a8e71b05e0c9621935f58e) (self)  
def | [wr2](../../db/d8b/classautomotive__design_1_1mechanism__base__placement.html#a571f98d6de05c9b7dfc26865582594a3) (self)  
def | [wr3](../../db/d8b/classautomotive__design_1_1mechanism__base__placement.html#a9387659fc5262c115087e9847db175e8) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.representation_relationship_with_transformation](../../d2/dcc/classautomotive__design_1_1representation__relationship__with__transformation.html)  
def | [transformation_operator](../../d2/dcc/classautomotive__design_1_1representation__relationship__with__transformation.html#a17e60743711d8a427cbeab15f66e7f02) ()  
def | [wr1](../../d2/dcc/classautomotive__design_1_1representation__relationship__with__transformation.html#aaec18b1f2c9eeb21d8f6f927e3cd2e49) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.representation_relationship](../../d3/d47/classautomotive__design_1_1representation__relationship.html)  
def | [description](../../d3/d47/classautomotive__design_1_1representation__relationship.html#ad19763c0b195fdb86036c42f815fc0ec) ()  
def | [name](../../d3/d47/classautomotive__design_1_1representation__relationship.html#a0848115085605d8443d2871fc116dbd3) ()  
def | [rep_1](../../d3/d47/classautomotive__design_1_1representation__relationship.html#a3402a69089802fc9240c57346490ec4c) ()  
def | [rep_2](../../d3/d47/classautomotive__design_1_1representation__relationship.html#a7e0c4a8b1b3ed0b4a18dc04121eec47c) ()  
  
##  Public Attributes  
  
---  
|
[base_of_mechanism](../../db/d8b/classautomotive__design_1_1mechanism__base__placement.html#a08410fa2d5559b1609585e4d76819534)  
|
[representation_relationship_with_transformation_transformation_operator](../../db/d8b/classautomotive__design_1_1mechanism__base__placement.html#a5febc3a7e6daf58ad16e6d3c9a3258eb)  
|
[transformation_operator](../../db/d8b/classautomotive__design_1_1mechanism__base__placement.html#aef1aa818eff88c0fb8d7c75da4252afb)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_relationship_with_transformation](../../d2/dcc/classautomotive__design_1_1representation__relationship__with__transformation.html)  
|
[transformation_operator](../../d2/dcc/classautomotive__design_1_1representation__relationship__with__transformation.html#a9d0ffe7d2084616d4c57dd90afa55959)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_relationship](../../d3/d47/classautomotive__design_1_1representation__relationship.html)  
|
[description](../../d3/d47/classautomotive__design_1_1representation__relationship.html#a06f918f5bc436973cf2d5bb094436599)  
|
[name](../../d3/d47/classautomotive__design_1_1representation__relationship.html#ad596c73def5a04e3f9c16b475a61e3d9)  
|
[rep_1](../../d3/d47/classautomotive__design_1_1representation__relationship.html#a48aeeda7c357a7c5d27dfd5c728a4cc6)  
|
[rep_2](../../d3/d47/classautomotive__design_1_1representation__relationship.html#af36f53abfdcf74f240b09c7eef35d6ec)  
  
## Detailed Description

    
    
    Entity mechanism_base_placement definition.
    
        :param base_of_mechanism
        :type base_of_mechanism:mechanism
    
        :param representation_relationship_with_transformation_transformation_operator
        :type representation_relationship_with_transformation_transformation_operator:cartesian_transformation_operator_3d
    
        :param representation_relationship_rep_2
        :type representation_relationship_rep_2:kinematic_link_representation

## Member Function Documentation

## ◆ base_of_mechanism()

def automotive_design.mechanism_base_placement.base_of_mechanism  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.mechanism_base_placement._base_of_mechanism.

Referenced by
[automotive_design.mechanism_base_placement.representation_relationship_rep_2()](../../db/d8b/classautomotive__design_1_1mechanism__base__placement.html#a2036d6b183b15bb056bf017cb9d261f5),
and
[automotive_design.mechanism_base_placement.wr2()](../../db/d8b/classautomotive__design_1_1mechanism__base__placement.html#a571f98d6de05c9b7dfc26865582594a3).

## ◆ representation_relationship_rep_2()

def automotive_design.mechanism_base_placement.representation_relationship_rep_2  | ( | | ) |   
---|---|---|---|---  
  
References
[e57::SourceDestBufferImpl.base()](../../d2/dcb/classe57_1_1SourceDestBufferImpl.html#a2a058a75579867c9b75a785161ca48d3),
KDTree::_Alloc_base< _Tp, _Alloc >::NoLeakAlloc.base,
[Gui::SoRegPoint.base](../../d8/da6/classGui_1_1SoRegPoint.html#a377248fec41d9ab80ec0c0b15495e19b),
Gui::AbstractSplitViewPy.base, Gui::View3DInventorPy.base,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.alternate_product_relationship.base,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.assembly_component_usage_substitute.base,
[automotive_design.mechanism.base](../../df/dc3/classautomotive__design_1_1mechanism.html#a2f05a4ada5c1fc1f6a76e576d5216671),
[automotive_design.alternate_product_relationship.base](../../d4/ddc/classautomotive__design_1_1alternate__product__relationship.html#a454b8602c9ded9ddc790f16072b07e0e),
[automotive_design.assembly_component_usage_substitute.base](../../d3/d66/classautomotive__design_1_1assembly__component__usage__substitute.html#a374f7957be24a0fc391de1a9020b9c63),
[config_control_design.alternate_product_relationship.base](../../db/d4c/classconfig__control__design_1_1alternate__product__relationship.html#a9129f2eacd3b05f798966ca1ba6e69e8),
[config_control_design.assembly_component_usage_substitute.base](../../d7/d37/classconfig__control__design_1_1assembly__component__usage__substitute.html#a844dee21b25544012e3b0b0caaa9d48d),
MeshCore::MeshNearestIndexToPlane< T >.base,
PathScripts.PathFeatureExtensionsGui._Extension.base,
[PathScripts.PathSlot.ObjectSlot.base](../../d6/dca/classPathScripts_1_1PathSlot_1_1ObjectSlot.html#aabb7ace34d073fc723abe5ff0046e7f2),
[PathTests.TestPathStock.TestPathStock.base](../../da/d6d/classPathTests_1_1TestPathStock_1_1TestPathStock.html#aee676d92bccb21e4035bd6beb4104f03),
[SpreadsheetGui::SheetViewPy.base](../../d7/d63/classSpreadsheetGui_1_1SheetViewPy.html#adfa3bb119141e1856d7f5b26f106a6f1),
[TechDrawGui::MDIViewPagePy.base](../../d8/dbc/classTechDrawGui_1_1MDIViewPagePy.html#a9e478fa37babcc60a92df4a6c978599e),
WebGui::BrowserViewPy.base,
[automotive_design.mechanism_base_placement.base_of_mechanism](../../db/d8b/classautomotive__design_1_1mechanism__base__placement.html#a08410fa2d5559b1609585e4d76819534),
and
[automotive_design.representation_of_link()](../../d4/ddf/namespaceautomotive__design.html#a87a9006f262676089fa69db9e075f03b).

## ◆ representation_relationship_with_transformation_transformation_operator()

def automotive_design.mechanism_base_placement.representation_relationship_with_transformation_transformation_operator  | ( | | ) |   
---|---|---|---|---  
  
References
automotive_design.mechanism_base_placement._representation_relationship_with_transformation_transformation_operator,
and
automotive_design.kinematic_frame_background_representation_association._representation_relationship_with_transformation_transformation_operator.

## ◆ wr1()

def automotive_design.mechanism_base_placement.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.representation_relationship_with_transformation](../../d2/dcc/classautomotive__design_1_1representation__relationship__with__transformation.html#aaec18b1f2c9eeb21d8f6f927e3cd2e49).

References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## ◆ wr2()

def automotive_design.mechanism_base_placement.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[automotive_design.mechanism_base_placement.base_of_mechanism](../../db/d8b/classautomotive__design_1_1mechanism__base__placement.html#a08410fa2d5559b1609585e4d76819534),
and
[automotive_design.suitably_based_mechanism()](../../d4/ddf/namespaceautomotive__design.html#a0d516839be364f87f60d1e7f82796e77).

## ◆ wr3()

def automotive_design.mechanism_base_placement.wr3  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
## Member Data Documentation

## ◆ base_of_mechanism

automotive_design.mechanism_base_placement.base_of_mechanism  
---  
  
Referenced by
[automotive_design.mechanism_base_placement.representation_relationship_rep_2()](../../db/d8b/classautomotive__design_1_1mechanism__base__placement.html#a2036d6b183b15bb056bf017cb9d261f5),
and
[automotive_design.mechanism_base_placement.wr2()](../../db/d8b/classautomotive__design_1_1mechanism__base__placement.html#a571f98d6de05c9b7dfc26865582594a3).

## ◆ representation_relationship_with_transformation_transformation_operator

automotive_design.mechanism_base_placement.representation_relationship_with_transformation_transformation_operator  
---  
  
## ◆ transformation_operator

automotive_design.mechanism_base_placement.transformation_operator  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

