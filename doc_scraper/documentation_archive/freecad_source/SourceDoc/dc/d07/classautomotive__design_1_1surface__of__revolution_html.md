---
url: https://freecad.github.io/SourceDoc/dc/d07/classautomotive__design_1_1surface__of__revolution.html
scraped_at: 2025-09-08T15:13:30.105160
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [surface_of_revolution](../../dc/d07/classautomotive__design_1_1surface__of__revolution.html)

[List of all members](../../d8/de1/classautomotive__design_1_1surface__of__revolution-members.html) | Public Member Functions | Public Attributes

automotive_design.surface_of_revolution Class Reference

##  Public Member Functions  
  
---  
def | [axis_line](../../dc/d07/classautomotive__design_1_1surface__of__revolution.html#ac11430bfca20d807bd7fbb1de4555324) ()  
def | [axis_position](../../dc/d07/classautomotive__design_1_1surface__of__revolution.html#a6a5fdc397bccc52b6f11f2f4d68fa0f7) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.swept_surface](../../d7/dd6/classautomotive__design_1_1swept__surface.html)  
def | [swept_curve](../../d7/dd6/classautomotive__design_1_1swept__surface.html#a992e26ca09101f97ff3015fb40481017) ()  
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
[axis_position](../../dc/d07/classautomotive__design_1_1surface__of__revolution.html#af7ca75ed1cc20033c054bcb1a029b247)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.swept_surface](../../d7/dd6/classautomotive__design_1_1swept__surface.html)  
|
[swept_curve](../../d7/dd6/classautomotive__design_1_1swept__surface.html#a0f7c575efa95ce9c43baa65024d7160f)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity surface_of_revolution definition.
    
        :param axis_position
        :type axis_position:axis1_placement
    
        :param axis_line
        :type axis_line:line

## Member Function Documentation

## ◆ axis_line()

def automotive_design.surface_of_revolution.axis_line  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_of_revolution.axis_position,
[automotive_design.surface_of_revolution.axis_position](../../dc/d07/classautomotive__design_1_1surface__of__revolution.html#af7ca75ed1cc20033c054bcb1a029b247),
[config_control_design.surface_of_revolution.axis_position](../../d3/dcc/classconfig__control__design_1_1surface__of__revolution.html#a6c9008fd4a87bf0308fc7bbbf897d8bf),
[App::Meta::Url.location](../../d7/de5/structApp_1_1Meta_1_1Url.html#aa40afabdf8d53cdd4f29dd5594effeda),
[draftguitools.gui_circulararray.CircularArray.location](../../dc/dd7/classdraftguitools_1_1gui__circulararray_1_1CircularArray.html#a0884f374b9ab70c333fafb73816b12e1),
[draftguitools.gui_polararray.PolarArray.location](../../dd/dc9/classdraftguitools_1_1gui__polararray_1_1PolarArray.html#a55e120c5eacdc1d6a9ffc2ee868b97a5),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.placement.location,
[automotive_design.placement.location](../../d8/d8c/classautomotive__design_1_1placement.html#aade15ec8d9163d4f50f6ebd55bf9e306),
[config_control_design.placement.location](../../da/d34/classconfig__control__design_1_1placement.html#a82d8e902f6a2bbfa6de928032d40bd1d),
[ifc2x3.ifcexternalreference.location](../../dd/dec/classifc2x3_1_1ifcexternalreference.html#a7a533b0d9fdb23c15223ab3ebc86d066),
[ifc2x3.ifcplacement.location](../../dd/dfd/classifc2x3_1_1ifcplacement.html#ab0f26a3cde0ba583e2d87ec02900e82c),
[ifc4.ifcexternalreference.location](../../d5/dd9/classifc4_1_1ifcexternalreference.html#a25390cf1c6b26090737c9d27429454f0),
[ifc4.ifcplacement.location](../../d4/da3/classifc4_1_1ifcplacement.html#ade56cca150b4b11e254d432caa231454),
[ifc4.ifcdocumentinformation.location](../../da/dbf/classifc4_1_1ifcdocumentinformation.html#af5b9773ffd2c248cbf06821180c75fce),
[ifc4.ifcclassification.location](../../db/d11/classifc4_1_1ifcclassification.html#a600169c34a2d9021964df0780fd070b4),
[ifc4.ifclibraryinformation.location](../../d9/d68/classifc4_1_1ifclibraryinformation.html#ab3c13281ded938f6115df119255d0005),
PartGui::TaskPrimitives.location, PartGui::TaskPrimitivesEdit.location,
[PathScripts.PathDressupDogbone.Bone.location()](../../d6/d5c/classPathScripts_1_1PathDressupDogbone_1_1Bone.html#a0810be25de1e0e54c88c3e39cc787d06),
[e57::Translation.z](../../de/d18/structe57_1_1Translation.html#a9445e1de70a2b4414fc5afdb8b5549d0),
[e57::Quaternion.z](../../d9/da9/structe57_1_1Quaternion.html#a0f203d24b9c9dfc9c2112daf41301ca3),
[R3.z](../../d4/d0e/classR3.html#afda83a4e3cf0442476aad4dc44a8eda2),
[Multitype.z](../../db/df2/unionMultitype.html#aa031f83e1db7e8f751458cebe7b9d897),
XYZ.z,
[Base::DualQuat.z](../../d4/d13/classBase_1_1DualQuat.html#a2299a66bb636cd1ec8f243e00ea97015),
[Base::Vector3< double
>.z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da),
[Base::Vector3< _Precision
>.z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da),
[Base::Vector3< float
>.z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da),
[Gui::PropertyEditor::PropertyVectorItem.z](../../dc/d86/classGui_1_1PropertyEditor_1_1PropertyVectorItem.html#ab8a9241764da877209aaa36696338a17),
[Gui::PropertyEditor::PropertyVectorDistanceItem.z](../../db/dd4/classGui_1_1PropertyEditor_1_1PropertyVectorDistanceItem.html#aef25ba0c263dc6ced80ebdadeaf6dab4),
[Gui::SelectionChanges.z](../../d5/d50/classGui_1_1SelectionChanges.html#a73c5fd0103bbbc388762557e06796a10),
[Gui::SelectionSingleton::SelObj.z](../../d3/ddf/structGui_1_1SelectionSingleton_1_1SelObj.html#a1b506759c2b744396c5e8c2fb33133b6),
Gui::SelectionSingleton::_SelObj.z, Gui::DockWnd::SelectionView.z,
[importSH3D.SH3DHandler.z](../../d8/de6/classimportSH3D_1_1SH3DHandler.html#aa31e8c79dbd7c6258a08a2c14fbeceba),
[DraftGui.DraftToolBar.z](../../d0/d91/classDraftGui_1_1DraftToolBar.html#ac76e8ed6c241bb3330b126dade09e950),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.axis1_placement.z(),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.right_angular_wedge.z,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.block.z,
[automotive_design.axis1_placement.z()](../../dd/d41/classautomotive__design_1_1axis1__placement.html#a0728a3baec495fbfb93954e7a8350658),
[automotive_design.right_angular_wedge.z](../../d4/df4/classautomotive__design_1_1right__angular__wedge.html#a5782b3772f1d57274d8ac89134b05378),
[automotive_design.block.z](../../d5/da2/classautomotive__design_1_1block.html#aa13f6909f4db29e3f4b558377285c2e2),
[config_control_design.axis1_placement.z()](../../d7/df7/classconfig__control__design_1_1axis1__placement.html#a2e286d9765dffb9a06686a29f273b3be),
[point3D.z](../../d4/d7b/structpoint3D.html#ae7370c9a05b6fb32d54c2b37a8b87d91),
[ifc2x3.ifcaxis1placement.z()](../../df/db1/classifc2x3_1_1ifcaxis1placement.html#a67f5cce20ad3eed02520d3db096a7cb2),
[ifc4.ifcaxis1placement.z()](../../dd/ddf/classifc4_1_1ifcaxis1placement.html#a11c43803bb9668bb02a978b8e2f60d22),
[MeshCore::MeshFastBuilder::Private::Vertex.z](../../de/d72/structMeshFastBuilder_1_1Private_1_1Vertex.html#afb7fbc6fc5ca843afdf5332b2ad89d6d),
MeshCore::MeshGridIterator::GridElement.z,
[MeshCore::NODE.z](../../d1/d49/structMeshCore_1_1NODE.html#aa20b952a1f25e07a738a00c48be97a7b),
[MeshPart::Vertex.z](../../db/d6a/structMeshPart_1_1Vertex.html#a36d6a2865faefc22aace974717ded766),
MeshPartGui::MeshCrossSection.z,
[Part::MeshVertex.z](../../d5/d5f/structPart_1_1MeshVertex.html#a4deafd4854178511879d10f2cb36f25d),
[PartGui::DimSelections::DimSelection.z](../../d1/d15/structPartGui_1_1DimSelections_1_1DimSelection.html#a394ea94b98840717954a922220ae9624),
[Mod.PartDesign.Scripts.FilletArc.Vector.z](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a78547896dd50c7a79dafebb62295468e),
[rotation_generator.refAxis.z](../../d6/d29/classrotation__generator_1_1refAxis.html#adf1630890e1b4e04a7d67c74b4fb18f1),
[geoff_geometry::Point3d.z](../../d0/ddc/classgeoff__geometry_1_1Point3d.html#ac5f155c60f62e1fe3ff64d0998e07ada),
[PathScripts.PathDressupHoldingTags.Tag.z](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#a080b6f3741f1771a227b810d05ca5be2),
[PathScripts.PathDressupTag.TagSolid.z](../../d2/dc0/classPathScripts_1_1PathDressupTag_1_1TagSolid.html#a344dfd1f36a6bd9100d819b6dbe02d47),
[Point3D.z](../../d5/d01/structPoint3D.html#a6e72b27633aeb7ed2e6f4b98da554b39),
Points::PointsGridIterator::GridElement.z, KDL::Vector.z(), and
[Param.z](../../da/da2/structParam.html#a5f25c71f9cbf36ac46357c743e1ca968).

## ◆ axis_position()

def automotive_design.surface_of_revolution.axis_position  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_of_revolution._axis_position,
automotive_design.surface_of_revolution._axis_position, and
config_control_design.surface_of_revolution._axis_position.

Referenced by
[automotive_design.surface_of_revolution.axis_line()](../../dc/d07/classautomotive__design_1_1surface__of__revolution.html#ac11430bfca20d807bd7fbb1de4555324).

## Member Data Documentation

## ◆ axis_position

automotive_design.surface_of_revolution.axis_position  
---  
  
Referenced by
[automotive_design.surface_of_revolution.axis_line()](../../dc/d07/classautomotive__design_1_1surface__of__revolution.html#ac11430bfca20d807bd7fbb1de4555324).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

