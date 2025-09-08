---
url: https://freecad.github.io/SourceDoc/d5/d19/classBOPTools_1_1SplitFeatures_1_1ViewProviderSlice.html
scraped_at: 2025-09-08T15:18:54.505145
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [BOPTools](../../dc/dff/namespaceBOPTools.html)
  * [SplitFeatures](../../d7/de4/namespaceBOPTools_1_1SplitFeatures.html)
  * [ViewProviderSlice](../../d5/d19/classBOPTools_1_1SplitFeatures_1_1ViewProviderSlice.html)

[List of all members](../../d1/d77/classBOPTools_1_1SplitFeatures_1_1ViewProviderSlice-members.html) | Public Member Functions | Public Attributes

BOPTools.SplitFeatures.ViewProviderSlice Class Reference

##  Public Member Functions  
  
---  
def | [attach](../../d5/d19/classBOPTools_1_1SplitFeatures_1_1ViewProviderSlice.html#ae4929c60cb75ad5ca3742f8caf18be4d) (self, vobj)  
def | [claimChildren](../../d5/d19/classBOPTools_1_1SplitFeatures_1_1ViewProviderSlice.html#a45243295181580dda3d489d0342026ed) (self)  
def | [getIcon](../../d5/d19/classBOPTools_1_1SplitFeatures_1_1ViewProviderSlice.html#af38f34dc51a1d7ad35d7254a0bb74f5b) (self)  
def | [onDelete](../../d5/d19/classBOPTools_1_1SplitFeatures_1_1ViewProviderSlice.html#a20a3b8fa1e0921831683ebaae84baa98) (self, feature, subelements)  
  
##  Public Attributes  
  
---  
|
[Object](../../d5/d19/classBOPTools_1_1SplitFeatures_1_1ViewProviderSlice.html#a15ecfb5f1a6f53bcb0265653db346a47)  
|
[ViewObject](../../d5/d19/classBOPTools_1_1SplitFeatures_1_1ViewProviderSlice.html#a2a3a0100420aa9d0fddc30b70b554dbc)  
  
## Detailed Description

    
    
    A View Provider for the Part Slice feature.

## Member Function Documentation

## ◆ attach()

def BOPTools.SplitFeatures.ViewProviderSlice.attach  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _vobj_  
| ) | |   
  
## ◆ claimChildren()

def BOPTools.SplitFeatures.ViewProviderSlice.claimChildren  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[Base::XMLReader::FileEntry.Object](../../d4/d0e/structBase_1_1XMLReader_1_1FileEntry.html#a810a31633177de69f84d2b9749940dc9),
[Base::Writer::FileEntry.Object](../../d5/de8/structBase_1_1Writer_1_1FileEntry.html#a15a35046c9bd5dad11dd5d97c18d675f),
Py::Object.Object(),
[Gui::SelectionChanges.Object](../../d5/d50/classGui_1_1SelectionChanges.html#a9a19f506b1a84b6e75fb8740bcd3a575),
[ArchBuildingPart.ViewProviderBuildingPart.Object](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a80074ab1c13b73be0cfb1b8d70fc140c),
[ArchComponent.ViewProviderComponent.Object](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a597cb57c8f3b67265e32073313fc7140),
ArchEquipment._ViewProviderEquipment.Object, ArchFloor._Floor.Object,
ArchFloor._ViewProviderFloor.Object,
ArchMaterial._ViewProviderArchMaterialContainer.Object,
ArchMaterial._ViewProviderArchMaterial.Object,
[ArchReference.ViewProviderArchReference.Object](../../d2/dfd/classArchReference_1_1ViewProviderArchReference.html#a7ff834265c54ac7fb2656b1743c6beca),
ArchRoof._ViewProviderRoof.Object,
ArchSchedule._ViewProviderArchSchedule.Object,
ArchSectionPlane._ViewProviderSectionPlane.Object,
ArchSite._ViewProviderSite.Object, ArchSpace._ViewProviderSpace.Object,
[ArchStructure.StructureTaskPanel.Object](../../df/d40/classArchStructure_1_1StructureTaskPanel.html#a2a7f5afe1095df43467d870bd66015b2),
ArchWall._ViewProviderWall.Object,
[draftobjects.layer.Layer.Object](../../d0/ddc/classdraftobjects_1_1layer_1_1Layer.html#acb6706be7ad1a79dc3ab403ccbacb591),
[draftviewproviders.view_base.ViewProviderDraft.Object](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#af3e3740115122efcc10bff5b2dbffcf4),
[draftviewproviders.view_dimension.ViewProviderDimensionBase.Object](../../d6/d45/classdraftviewproviders_1_1view__dimension_1_1ViewProviderDimensionBase.html#a2cc0e04e6a50a9e3be070d3fb4c32c7e),
[draftviewproviders.view_dimension.ViewProviderLinearDimension.Object](../../dc/d15/classdraftviewproviders_1_1view__dimension_1_1ViewProviderLinearDimension.html#af5589835e2e8dce93afafa9a246b7ccd),
[draftviewproviders.view_dimension.ViewProviderAngularDimension.Object](../../d5/d88/classdraftviewproviders_1_1view__dimension_1_1ViewProviderAngularDimension.html#a3aaa8f2262ee754f43a500d5f1939053),
[draftviewproviders.view_draft_annotation.ViewProviderDraftAnnotation.Object](../../d2/d24/classdraftviewproviders_1_1view__draft__annotation_1_1ViewProviderDraftAnnotation.html#a20ade5bec2ae3eb3ea7ae695937c2c58),
[draftviewproviders.view_label.ViewProviderLabel.Object](../../d1/d88/classdraftviewproviders_1_1view__label_1_1ViewProviderLabel.html#ac983249a6e5f94ed59af459cebebe749),
[draftviewproviders.view_layer.ViewProviderLayer.Object](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#a8c9a3925420b39835429fd957332f320),
[draftviewproviders.view_layer.ViewProviderLayerContainer.Object](../../d1/dec/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayerContainer.html#ab0dc98dc58ff9b0853c822599e24e0c9),
[draftviewproviders.view_text.ViewProviderText.Object](../../db/dd9/classdraftviewproviders_1_1view__text_1_1ViewProviderText.html#a05f7b6bee1b34cf5eafd22fef0ba76a2),
[draftviewproviders.view_wire.ViewProviderWire.Object](../../da/dd2/classdraftviewproviders_1_1view__wire_1_1ViewProviderWire.html#a61ba75eda07d4458cb2ffa6b076ff96c),
[draftviewproviders.view_wpproxy.ViewProviderWorkingPlaneProxy.Object](../../da/dbf/classdraftviewproviders_1_1view__wpproxy_1_1ViewProviderWorkingPlaneProxy.html#aa0d5af582a27cee2917faef98c706b59),
[femviewprovider.view_base_femconstraint.VPBaseFemConstraint.Object](../../d8/d92/classfemviewprovider_1_1view__base__femconstraint_1_1VPBaseFemConstraint.html#a3f3218d9519118642a24bb2e8ad4a91b),
[femviewprovider.view_base_femobject.VPBaseFemObject.Object](../../d0/d48/classfemviewprovider_1_1view__base__femobject_1_1VPBaseFemObject.html#af205146496732cbe6c506294db4d0fda),
[femviewprovider.view_mesh_gmsh.VPMeshGmsh.Object](../../df/dbc/classfemviewprovider_1_1view__mesh__gmsh_1_1VPMeshGmsh.html#a3483ee45886ec851784fa9f60cda8626),
[OpenSCADFeatures.ViewProviderTree.Object](../../df/dbf/classOpenSCADFeatures_1_1ViewProviderTree.html#a551bca6e05e09056eed10a7ccfdce9f3),
[BOPTools.JoinFeatures.ViewProviderConnect.Object](../../da/d91/classBOPTools_1_1JoinFeatures_1_1ViewProviderConnect.html#a90cca2c770c6b0798ec2b46bf73dfbf3),
[BOPTools.JoinFeatures.ViewProviderEmbed.Object](../../dc/d41/classBOPTools_1_1JoinFeatures_1_1ViewProviderEmbed.html#a80a4f7be937dfa7d6b917c7eb69098ab),
[BOPTools.JoinFeatures.ViewProviderCutout.Object](../../d4/d85/classBOPTools_1_1JoinFeatures_1_1ViewProviderCutout.html#aeec0c48b42056af82c259e57e6d5b79f),
[BOPTools.SplitFeatures.ViewProviderBooleanFragments.Object](../../d0/d5a/classBOPTools_1_1SplitFeatures_1_1ViewProviderBooleanFragments.html#a0c77eb31d1b9d66157606764a007ca73),
[BOPTools.SplitFeatures.ViewProviderSlice.Object](../../d5/d19/classBOPTools_1_1SplitFeatures_1_1ViewProviderSlice.html#a15ecfb5f1a6f53bcb0265653db346a47),
[BOPTools.SplitFeatures.ViewProviderXOR.Object](../../d9/de4/classBOPTools_1_1SplitFeatures_1_1ViewProviderXOR.html#ac18bbcf4db8fc26d78356a427108c7d5),
CompoundTools.CompoundFilter._ViewProviderCompoundFilter.Object,
JoinFeatures._ViewProviderPartJoinFeature.Object,
[Mod.PartDesign.FeatureHole.ViewProviderHole.ViewProviderHole.Object](../../de/d6b/classMod_1_1PartDesign_1_1FeatureHole_1_1ViewProviderHole_1_1ViewProviderHole.html#a075a0d66e3cee7d0130660504a5840c7),
Mod.PartDesign.InvoluteGearFeature._ViewProviderInvoluteGear.Object,
[Mod.PartDesign.SprocketFeature.ViewProviderSprocket.Object](../../da/d59/classMod_1_1PartDesign_1_1SprocketFeature_1_1ViewProviderSprocket.html#ada8c7660ebbbf71305fadf6186ee8a05),
[PathScripts.PathArray.ViewProviderArray.Object](../../dc/d4b/classPathScripts_1_1PathArray_1_1ViewProviderArray.html#acc715b58fbeb757403ca188707eb83b7),
PathScripts.PathCollision._ViewProviderCollisionSim.Object,
[PathScripts.PathCopy.ViewProviderPathCopy.Object](../../de/d45/classPathScripts_1_1PathCopy_1_1ViewProviderPathCopy.html#a9bbdf33af7f09d7ccdafdc5f8cc0b4cb),
[PathScripts.PathDressupDragknife.ViewProviderDressup.Object](../../dc/d40/classPathScripts_1_1PathDressupDragknife_1_1ViewProviderDressup.html#ad6d7bd90a0a701c68bfeb55c314ed5fa),
[PathScripts.PathHop.ViewProviderPathHop.Object](../../da/dfa/classPathScripts_1_1PathHop_1_1ViewProviderPathHop.html#a3ec9b9210e599809ddec0a1e711106fa),
[PathScripts.PathOpGui.ViewProvider.Object](../../db/df9/classPathScripts_1_1PathOpGui_1_1ViewProvider.html#af6241ad8210a6060fb55d797e6d082ff),
[Mod.Show.Containers.Container.Object](../../db/d52/classMod_1_1Show_1_1Containers_1_1Container.html#aea8c76ed8a0f879a33e1abe68df4a960),
[Spreadsheet_legacy.Spreadsheet.Object](../../d2/d6d/classSpreadsheet__legacy_1_1Spreadsheet.html#a4e65495069891285020965e854149600),
[Spreadsheet_legacy.ViewProviderSpreadsheet.Object](../../d6/d84/classSpreadsheet__legacy_1_1ViewProviderSpreadsheet.html#ab3bd99499693b288462fbdbd5399fc53),
[DocumentObject.ViewProvider.Object()](../../d8/dd7/classDocumentObject_1_1ViewProvider.html#a04e829dec435fa70e442b47989269388),
and
[Mod.Test.Document.DocumentBasicCases.Object](../../dd/dbe/classMod_1_1Test_1_1Document_1_1DocumentBasicCases.html#aabbc092c15e784e33f697508ae5ecbac).

Referenced by
[femviewprovider.view_mesh_gmsh.VPMeshGmsh.onDelete()](../../df/dbc/classfemviewprovider_1_1view__mesh__gmsh_1_1VPMeshGmsh.html#ae4c9ca343356d3acf252b0566b3ff01c),
[femviewprovider.view_result_mechanical.VPResultMechanical.onDelete()](../../d7/d8f/classfemviewprovider_1_1view__result__mechanical_1_1VPResultMechanical.html#a6bde7f2d215b4399295a2d2b426d6f4f),
[BOPTools.JoinFeatures.ViewProviderConnect.onDelete()](../../da/d91/classBOPTools_1_1JoinFeatures_1_1ViewProviderConnect.html#a7578eaa093ec056d3080b03f20244ca8),
[BOPTools.SplitFeatures.ViewProviderBooleanFragments.onDelete()](../../d0/d5a/classBOPTools_1_1SplitFeatures_1_1ViewProviderBooleanFragments.html#a1a561237cd3f10b60c442c5b6e63b794),
[BOPTools.SplitFeatures.ViewProviderSlice.onDelete()](../../d5/d19/classBOPTools_1_1SplitFeatures_1_1ViewProviderSlice.html#a20a3b8fa1e0921831683ebaae84baa98),
and
[BOPTools.SplitFeatures.ViewProviderXOR.onDelete()](../../d9/de4/classBOPTools_1_1SplitFeatures_1_1ViewProviderXOR.html#a199d8da22e104fa58c6b88685ffdfec1).

## ◆ getIcon()

def BOPTools.SplitFeatures.ViewProviderSlice.getIcon  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[BOPTools.SplitFeatures.getIconPath()](../../d7/de4/namespaceBOPTools_1_1SplitFeatures.html#a8414fc6d96bf4b7e5b6d9524b002ae03).

Referenced by
[ArchAxisSystem.AxisSystemTaskPanel.update()](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a376cbba2ccee6efd86c46d0f0a8e99e3),
[ArchComponent.ComponentTaskPanel.update()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#af95b36032a3837b4bf1b92fe7c6a47e0),
and
[ArchSectionPlane.SectionPlaneTaskPanel.update()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#aab4bcd7b08950b8e3b37d801381c5162).

## ◆ onDelete()

def BOPTools.SplitFeatures.ViewProviderSlice.onDelete  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _feature_ ,   
|  |  | _subelements_  
| ) | |   
  
References
[PartGui::ViewProviderCompound.claimChildren()](../../d1/d39/classPartGui_1_1ViewProviderCompound.html#a8e5d16c05e27ff22d077c79d43520f2b),
[PartGui::ViewProviderMirror.claimChildren()](../../d2/d29/classPartGui_1_1ViewProviderMirror.html#a2d89dd0a0fc37e95b48e979b8b81408a),
[PartGui::ViewProviderFillet.claimChildren()](../../de/dd4/classPartGui_1_1ViewProviderFillet.html#a6d3129fc39ba787229812c61d8b751a9),
[PartGui::ViewProviderChamfer.claimChildren()](../../db/d6b/classPartGui_1_1ViewProviderChamfer.html#a7d796ef8d2a8cd022982342ce798ee98),
[PartGui::ViewProviderRuledSurface.claimChildren()](../../d3/d74/classPartGui_1_1ViewProviderRuledSurface.html#a8f7d6bf9c5c95fc9c085581c4589b645),
[Gui::ViewProviderPythonFeatureT< ViewProviderT
>.claimChildren()](../../dc/d41/classGui_1_1ViewProviderPythonFeatureT.html#a687e762307eb21b2402d181c4dd4b2b6),
Gui::DocumentModel.claimChildren(),
ArchAxis._ViewProviderAxis.claimChildren(),
ArchAxisSystem._ViewProviderAxisSystem.claimChildren(),
[ArchComponent.ViewProviderComponent.claimChildren()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a05a3bbd9534c922df9943f971fd60bf2),
ArchFence._ViewProviderFence.claimChildren(),
ArchFloor._ViewProviderFloor.claimChildren(),
ArchFrame._ViewProviderFrame.claimChildren(),
ArchMaterial._ViewProviderArchMaterial.claimChildren(),
ArchSchedule._ViewProviderArchSchedule.claimChildren(),
ArchSectionPlane._ViewProviderSectionPlane.claimChildren(),
ArchSite._ViewProviderSite.claimChildren(),
[draftviewproviders.view_base.ViewProviderDraft.claimChildren()](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#af0b551826340210d20874aa39175d3d5),
[draftviewproviders.view_base.ViewProviderDraftAlt.claimChildren()](../../dd/d2f/classdraftviewproviders_1_1view__base_1_1ViewProviderDraftAlt.html#a65a0634b3319dec99689429b0338379c),
[draftviewproviders.view_draft_annotation.ViewProviderDraftAnnotation.claimChildren()](../../d2/d24/classdraftviewproviders_1_1view__draft__annotation_1_1ViewProviderDraftAnnotation.html#a588193f8dd5a57aae96a9571459b8e37),
[draftviewproviders.view_draftlink.ViewProviderDraftLink.claimChildren()](../../d1/d79/classdraftviewproviders_1_1view__draftlink_1_1ViewProviderDraftLink.html#a41b6cffae3663a58647a9227c4e1664a),
[draftviewproviders.view_label.ViewProviderLabel.claimChildren()](../../d1/d88/classdraftviewproviders_1_1view__label_1_1ViewProviderLabel.html#a1dde857646d7409d23296afcedd4c39d),
[draftviewproviders.view_layer.ViewProviderLayer.claimChildren()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#a8123f33a456b8fefa43a42fd11b82aa0),
[draftviewproviders.view_text.ViewProviderText.claimChildren()](../../db/dd9/classdraftviewproviders_1_1view__text_1_1ViewProviderText.html#a92051d52c03d890762ae743205b5e4ec),
[draftviewproviders.view_wire.ViewProviderWire.claimChildren()](../../da/dd2/classdraftviewproviders_1_1view__wire_1_1ViewProviderWire.html#a13e60e240bfcc6a291b5cf450367ad73),
[draftviewproviders.view_wpproxy.ViewProviderWorkingPlaneProxy.claimChildren()](../../da/dbf/classdraftviewproviders_1_1view__wpproxy_1_1ViewProviderWorkingPlaneProxy.html#ac3774745afb201786a53010448d41ae3),
[femviewprovider.view_mesh_gmsh.VPMeshGmsh.claimChildren()](../../df/dbc/classfemviewprovider_1_1view__mesh__gmsh_1_1VPMeshGmsh.html#a56cb33c198c8ed418656815f3d8c7abc),
[femviewprovider.view_result_mechanical.VPResultMechanical.claimChildren()](../../d7/d8f/classfemviewprovider_1_1view__result__mechanical_1_1VPResultMechanical.html#ab355e3a1025ce59b6797302f29c6d0c1),
[OpenSCADFeatures.ViewProviderTree.claimChildren()](../../df/dbf/classOpenSCADFeatures_1_1ViewProviderTree.html#aa51082a21dda8cd8ac4bfc75b8107936),
[BOPTools.JoinFeatures.ViewProviderConnect.claimChildren()](../../da/d91/classBOPTools_1_1JoinFeatures_1_1ViewProviderConnect.html#a2d75d1b98bfa1e05bbedc171ec608893),
[BOPTools.JoinFeatures.ViewProviderEmbed.claimChildren()](../../dc/d41/classBOPTools_1_1JoinFeatures_1_1ViewProviderEmbed.html#a468ee613f1d258009912c0f46dda8fdc),
[BOPTools.JoinFeatures.ViewProviderCutout.claimChildren()](../../d4/d85/classBOPTools_1_1JoinFeatures_1_1ViewProviderCutout.html#a4a0700249e2817cbe2f9c8b6e5b6f283),
[BOPTools.SplitFeatures.ViewProviderBooleanFragments.claimChildren()](../../d0/d5a/classBOPTools_1_1SplitFeatures_1_1ViewProviderBooleanFragments.html#a0905dfd15884082d80692f0923c87a93),
[BOPTools.SplitFeatures.ViewProviderSlice.claimChildren()](../../d5/d19/classBOPTools_1_1SplitFeatures_1_1ViewProviderSlice.html#a45243295181580dda3d489d0342026ed),
[BOPTools.SplitFeatures.ViewProviderXOR.claimChildren()](../../d9/de4/classBOPTools_1_1SplitFeatures_1_1ViewProviderXOR.html#a0895ad8a44b7eedf3d6a3fe62d74d13d),
CompoundTools.CompoundFilter._ViewProviderCompoundFilter.claimChildren(),
JoinFeatures._ViewProviderPartJoinFeature.claimChildren(),
[Mod.PartDesign.FeatureHole.ViewProviderHole.ViewProviderHole.claimChildren()](../../de/d6b/classMod_1_1PartDesign_1_1FeatureHole_1_1ViewProviderHole_1_1ViewProviderHole.html#a448ef4f8ef14d3cf55a92eff7250bb90),
[PathScripts.PathArray.ViewProviderArray.claimChildren()](../../dc/d4b/classPathScripts_1_1PathArray_1_1ViewProviderArray.html#a72d7ebded8be896fc0fa0bbb51a9bad2),
[PathScripts.PathDressupAxisMap.ViewProviderDressup.claimChildren()](../../d7/d13/classPathScripts_1_1PathDressupAxisMap_1_1ViewProviderDressup.html#a1a492fb4b8dafa57646f5896e41dd3fc),
[PathScripts.PathDressupDogbone.ViewProviderDressup.claimChildren()](../../df/ddb/classPathScripts_1_1PathDressupDogbone_1_1ViewProviderDressup.html#ad5dfe7e7575dee94a6ae8efd74e4f670),
[PathScripts.PathDressupDragknife.ViewProviderDressup.claimChildren()](../../dc/d40/classPathScripts_1_1PathDressupDragknife_1_1ViewProviderDressup.html#a4f777850f1b59aca4952abde91a7ccc5),
[PathScripts.PathDressupLeadInOut.ViewProviderDressup.claimChildren()](../../d7/d49/classPathScripts_1_1PathDressupLeadInOut_1_1ViewProviderDressup.html#a6f95ceed7760b7546e70b32519053d9b),
[PathScripts.PathDressupPathBoundaryGui.DressupPathBoundaryViewProvider.claimChildren()](../../dc/d69/classPathScripts_1_1PathDressupPathBoundaryGui_1_1DressupPathBoundaryViewProvider.html#a748ed9eba9af86272b464fd0b3d4d673),
[PathScripts.PathDressupRampEntry.ViewProviderDressup.claimChildren()](../../db/d82/classPathScripts_1_1PathDressupRampEntry_1_1ViewProviderDressup.html#ae3bd7afb166d203eb4ebfc83b0e496ce),
[PathScripts.PathDressupTagGui.PathDressupTagViewProvider.claimChildren()](../../dc/d08/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagViewProvider.html#a727d17080103323622874ed30de09970),
[PathScripts.PathDressupZCorrect.ViewProviderDressup.claimChildren()](../../d1/df1/classPathScripts_1_1PathDressupZCorrect_1_1ViewProviderDressup.html#a38637b5c32f5f1cf78463bf5d817336a),
[PathScripts.PathJobGui.ViewProvider.claimChildren()](../../d3/d3e/classPathScripts_1_1PathJobGui_1_1ViewProvider.html#a38386ef952c7be3ef968d3e3fcc3c88a),
[PathScripts.PathPropertyBagGui.ViewProvider.claimChildren()](../../d5/d77/classPathScripts_1_1PathPropertyBagGui_1_1ViewProvider.html#aa904df13a84919ba5498218e4b03de8e),
[PathScripts.PathSetupSheetGui.ViewProvider.claimChildren()](../../dc/dc3/classPathScripts_1_1PathSetupSheetGui_1_1ViewProvider.html#a65995951e72d8f5bdf1ca386314ed447),
[PathScripts.PathToolBitGui.ViewProvider.claimChildren()](../../d0/d90/classPathScripts_1_1PathToolBitGui_1_1ViewProvider.html#acef07b8be08153ef8fce6aabe7d25c53),
[PathScripts.PathToolControllerGui.ViewProvider.claimChildren()](../../db/db5/classPathScripts_1_1PathToolControllerGui_1_1ViewProvider.html#acf2d47a31c7fc520038a4bd53a07c290),
[Spreadsheet_legacy.ViewProviderSpreadsheet.claimChildren()](../../d6/d84/classSpreadsheet__legacy_1_1ViewProviderSpreadsheet.html#a75aee00167480ff54cda421089caf2b3),
[Texture.ViewProviderTexture.claimChildren()](../../d1/d29/classTexture_1_1ViewProviderTexture.html#ada894ebdfb390c525a432bf26b2f5242),
[Gui::ViewProviderPythonFeatureImp.claimChildren()](../../de/dbe/classGui_1_1ViewProviderPythonFeatureImp.html#a613cc470becfc76d29969a6f4d4bcd0a),
[Gui::ViewProvider.claimChildren()](../../d3/db3/classGui_1_1ViewProvider.html#af51254c2d4352f0c36f75c6e909ef1df),
[Gui::ViewProviderOrigin.claimChildren()](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#afd2e9b23fb332226846d2b13edf9e6ba),
[FemGui::ViewProviderFemAnalysis.claimChildren()](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#a37458e3a42b6d8e7a53bc0b07f720c02),
[FemGui::ViewProviderFemConstraint.claimChildren()](../../d7/dc7/classFemGui_1_1ViewProviderFemConstraint.html#a45b2f43632cae53dfefcce10f30ae398),
[FemGui::ViewProviderFemPostFunctionProvider.claimChildren()](../../df/d22/classFemGui_1_1ViewProviderFemPostFunctionProvider.html#a93fdb079614b29a6658a4596881405fb),
[FemGui::ViewProviderFemPostPipeline.claimChildren()](../../df/d95/classFemGui_1_1ViewProviderFemPostPipeline.html#ac5626a9e2850eeb26ecff5a70bf2d941),
[PartGui::ViewProviderBoolean.claimChildren()](../../df/dcc/classPartGui_1_1ViewProviderBoolean.html#a2ddf6a6611da27e24b5c177fa82179e9),
[PartGui::ViewProviderMultiFuse.claimChildren()](../../db/d93/classPartGui_1_1ViewProviderMultiFuse.html#a0045707f443193b046cb01b7c139b652),
[PartGui::ViewProviderMultiCommon.claimChildren()](../../db/daf/classPartGui_1_1ViewProviderMultiCommon.html#ab7e6ca8e32fb15358223c7eb8dc97b49),
[PartGui::ViewProviderExtrusion.claimChildren()](../../d7/dc8/classPartGui_1_1ViewProviderExtrusion.html#ae591beb9bf81e182debee47b7a0ca814),
[PartGui::ViewProviderRevolution.claimChildren()](../../dc/d27/classPartGui_1_1ViewProviderRevolution.html#a6a7ba941a61a447fb9a6e4e5246c4cee),
[PartGui::ViewProviderLoft.claimChildren()](../../d5/d42/classPartGui_1_1ViewProviderLoft.html#ac368f091664f727043f69262f84d3d3a),
[PartGui::ViewProviderSweep.claimChildren()](../../d7/d5f/classPartGui_1_1ViewProviderSweep.html#a91b5fe397c600d5fe79e69c62c3ac22e),
[PartGui::ViewProviderOffset.claimChildren()](../../df/ded/classPartGui_1_1ViewProviderOffset.html#a16ecb9054d6817296a620fdf43b90154),
[PartGui::ViewProviderThickness.claimChildren()](../../d1/d8f/classPartGui_1_1ViewProviderThickness.html#a8de30390b0f529bf7aa199a226628bc7),
[PartGui::ViewProviderFace.claimChildren()](../../d9/dba/classPartGui_1_1ViewProviderFace.html#a2455deb85cf98bb710dd4322ad07854c),
[PartDesignGui::ViewProviderHelix.claimChildren()](../../da/d62/classPartDesignGui_1_1ViewProviderHelix.html#a27d75e659da5ae824301907d1f95fe4d),
[PartDesignGui::ViewProviderHole.claimChildren()](../../df/dda/classPartDesignGui_1_1ViewProviderHole.html#abee71c6672e4a1f8a5b6d6bfe1423371),
[PartDesignGui::ViewProviderLoft.claimChildren()](../../d9/d6e/classPartDesignGui_1_1ViewProviderLoft.html#ac368f091664f727043f69262f84d3d3a),
[PartDesignGui::ViewProviderMainPart.claimChildren()](../../d4/d87/classPartDesignGui_1_1ViewProviderMainPart.html#ab287f6031d8457881ed450ff0028298e),
[PartDesignGui::ViewProviderMultiTransform.claimChildren()](../../d6/d05/classPartDesignGui_1_1ViewProviderMultiTransform.html#af5e53bee082a9a57e0e69dd5e6070035),
[PartDesignGui::ViewProviderPipe.claimChildren()](../../d8/dc8/classPartDesignGui_1_1ViewProviderPipe.html#a4c581523b2a518090737db2569d91dfa),
[PartDesignGui::ViewProviderSketchBased.claimChildren()](../../d3/d7d/classPartDesignGui_1_1ViewProviderSketchBased.html#a4552ed8301193054b5f18e6d1b445b89),
[PathGui::ViewProviderArea.claimChildren()](../../d3/d66/classPathGui_1_1ViewProviderArea.html#a3ee6f619b68b35b3ec246a7873fa6653),
[PathGui::ViewProviderAreaView.claimChildren()](../../dc/d0c/classPathGui_1_1ViewProviderAreaView.html#af7f604bd9905d7b5488f874185e867d9),
[PathGui::ViewProviderPathCompound.claimChildren()](../../db/d9a/classPathGui_1_1ViewProviderPathCompound.html#ad25e77d61c55b396d049d51301d0cfc7),
[PathGui::ViewProviderPathShape.claimChildren()](../../d9/d9e/classPathGui_1_1ViewProviderPathShape.html#a07694ec29ec000ec830fc3988076fab1),
[RobotGui::ViewProviderTrajectoryCompound.claimChildren()](../../d7/d47/classRobotGui_1_1ViewProviderTrajectoryCompound.html#ae747a93e2570dde9f2d60ba618be32d2),
[RobotGui::ViewProviderTrajectoryDressUp.claimChildren()](../../da/dff/classRobotGui_1_1ViewProviderTrajectoryDressUp.html#a7bc4e3cb415db601995399924a6d5435),
[TechDrawGui::ViewProviderLeader.claimChildren()](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#ab90cf47c766f83da23d7f960ded3ccdd),
[TechDrawGui::ViewProviderProjGroup.claimChildren()](../../d6/dc7/classTechDrawGui_1_1ViewProviderProjGroup.html#a702e5f00c38dcb77490c48b4018d093e),
[TechDrawGui::ViewProviderViewClip.claimChildren()](../../d1/dc2/classTechDrawGui_1_1ViewProviderViewClip.html#ab19cf412f22ca45bce0de2d22f88b7bb),
[TechDrawGui::ViewProviderViewPart.claimChildren()](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#aba1c9f4a2a6681b4ea6666ba487847c1),
[TechDrawGui::ViewProviderViewSection.claimChildren()](../../d2/df0/classTechDrawGui_1_1ViewProviderViewSection.html#a476e979878e83b84e952c2949d3d007a),
[TechDrawGui::ViewProviderWeld.claimChildren()](../../dc/dbe/classTechDrawGui_1_1ViewProviderWeld.html#a4e8d25b0066202499ac3da63f664db36),
[Gui::ViewProviderLink.claimChildren()](../../d6/d59/classGui_1_1ViewProviderLink.html#a3cba171d1aa19a5462fa22825dcc2047),
[PartDesignGui::ViewProviderSubShapeBinder.claimChildren()](../../d1/da6/classPartDesignGui_1_1ViewProviderSubShapeBinder.html#ac4ec5b8a1cc9767dcf24f5b49a2d7522),
and
[TechDrawGui::ViewProviderPage.claimChildren()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#abaf1943763d885917f20c4a78a8e2ef5).

## Member Data Documentation

## ◆ Object

BOPTools.SplitFeatures.ViewProviderSlice.Object  
---  
  
Referenced by
[draftviewproviders.view_layer.ViewProviderLayer.activate()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#a100c49f5d1966d59f546943ce6685a08),
[ArchPanel.CommandPanelSheet.Activated()](../../d1/d94/classArchPanel_1_1CommandPanelSheet.html#abed1cd5ce53c5b156683ae24b81f75e4),
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[OpenSCADFeatures.ViewProviderTree.attach()](../../df/dbf/classOpenSCADFeatures_1_1ViewProviderTree.html#a489f372b544fde950f6c94fe469ca039),
[ArchComponent.ViewProviderComponent.attach()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a35e80ee0b359823d7b9cecc23481b930),
[draftviewproviders.view_base.ViewProviderDraft.attach()](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#af35acb7285aa095bf670e82338c9462d),
[draftviewproviders.view_dimension.ViewProviderLinearDimension.attach()](../../dc/d15/classdraftviewproviders_1_1view__dimension_1_1ViewProviderLinearDimension.html#a6e8d37d9155778fc70b27e7d4e607f0b),
[draftviewproviders.view_dimension.ViewProviderAngularDimension.attach()](../../d5/d88/classdraftviewproviders_1_1view__dimension_1_1ViewProviderAngularDimension.html#a61b1ca60b7451140459dddaa2f2ff3db),
[draftviewproviders.view_draft_annotation.ViewProviderDraftAnnotation.attach()](../../d2/d24/classdraftviewproviders_1_1view__draft__annotation_1_1ViewProviderDraftAnnotation.html#a9d020c35cc375c2d2e91ab96c4563c8e),
[draftviewproviders.view_layer.ViewProviderLayer.attach()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#ab2a5fd20d4ab9b7d49e3a3e4d4ac8e78),
[draftviewproviders.view_layer.ViewProviderLayerContainer.attach()](../../d1/dec/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayerContainer.html#a5b25eb9ee95736d4049f5c11ea5977d0),
[PathScripts.PathArray.ViewProviderArray.attach()](../../dc/d4b/classPathScripts_1_1PathArray_1_1ViewProviderArray.html#abb70607468b63e690ee6dff23a4c3ef4),
[PathScripts.PathCopy.ViewProviderPathCopy.attach()](../../de/d45/classPathScripts_1_1PathCopy_1_1ViewProviderPathCopy.html#a7ba0a28dd4dac2a343da660cf7b8963c),
[PathScripts.PathDressupDragknife.ViewProviderDressup.attach()](../../dc/d40/classPathScripts_1_1PathDressupDragknife_1_1ViewProviderDressup.html#a302aaf7765dfd69f37d77c2e84dc0e91),
[PathScripts.PathHop.ViewProviderPathHop.attach()](../../da/dfa/classPathScripts_1_1PathHop_1_1ViewProviderPathHop.html#a28aaff1dcea04ba21c42974c68365ac3),
[PathScripts.PathOpGui.ViewProvider.attach()](../../db/df9/classPathScripts_1_1PathOpGui_1_1ViewProvider.html#a0840fdecdfbaaf3ffca3bcb866b39452),
[ArchSite.Compass.buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[ArchReference.ViewProviderArchReference.checkChanges()](../../d2/dfd/classArchReference_1_1ViewProviderArchReference.html#ab6a807091ea186d4252888a09f6b41ba),
[ArchComponent.ViewProviderComponent.claimChildren()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a05a3bbd9534c922df9943f971fd60bf2),
[draftviewproviders.view_base.ViewProviderDraft.claimChildren()](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#af0b551826340210d20874aa39175d3d5),
[draftviewproviders.view_draft_annotation.ViewProviderDraftAnnotation.claimChildren()](../../d2/d24/classdraftviewproviders_1_1view__draft__annotation_1_1ViewProviderDraftAnnotation.html#a588193f8dd5a57aae96a9571459b8e37),
[draftviewproviders.view_draftlink.ViewProviderDraftLink.claimChildren()](../../d1/d79/classdraftviewproviders_1_1view__draftlink_1_1ViewProviderDraftLink.html#a41b6cffae3663a58647a9227c4e1664a),
[draftviewproviders.view_layer.ViewProviderLayer.claimChildren()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#a8123f33a456b8fefa43a42fd11b82aa0),
[draftviewproviders.view_wire.ViewProviderWire.claimChildren()](../../da/dd2/classdraftviewproviders_1_1view__wire_1_1ViewProviderWire.html#a13e60e240bfcc6a291b5cf450367ad73),
[femviewprovider.view_mesh_gmsh.VPMeshGmsh.claimChildren()](../../df/dbc/classfemviewprovider_1_1view__mesh__gmsh_1_1VPMeshGmsh.html#a56cb33c198c8ed418656815f3d8c7abc),
[femviewprovider.view_result_mechanical.VPResultMechanical.claimChildren()](../../d7/d8f/classfemviewprovider_1_1view__result__mechanical_1_1VPResultMechanical.html#ab355e3a1025ce59b6797302f29c6d0c1),
[OpenSCADFeatures.ViewProviderTree.claimChildren()](../../df/dbf/classOpenSCADFeatures_1_1ViewProviderTree.html#aa51082a21dda8cd8ac4bfc75b8107936),
[BOPTools.JoinFeatures.ViewProviderConnect.claimChildren()](../../da/d91/classBOPTools_1_1JoinFeatures_1_1ViewProviderConnect.html#a2d75d1b98bfa1e05bbedc171ec608893),
[BOPTools.JoinFeatures.ViewProviderEmbed.claimChildren()](../../dc/d41/classBOPTools_1_1JoinFeatures_1_1ViewProviderEmbed.html#a468ee613f1d258009912c0f46dda8fdc),
[BOPTools.JoinFeatures.ViewProviderCutout.claimChildren()](../../d4/d85/classBOPTools_1_1JoinFeatures_1_1ViewProviderCutout.html#a4a0700249e2817cbe2f9c8b6e5b6f283),
[BOPTools.SplitFeatures.ViewProviderBooleanFragments.claimChildren()](../../d0/d5a/classBOPTools_1_1SplitFeatures_1_1ViewProviderBooleanFragments.html#a0905dfd15884082d80692f0923c87a93),
[BOPTools.SplitFeatures.ViewProviderSlice.claimChildren()](../../d5/d19/classBOPTools_1_1SplitFeatures_1_1ViewProviderSlice.html#a45243295181580dda3d489d0342026ed),
[BOPTools.SplitFeatures.ViewProviderXOR.claimChildren()](../../d9/de4/classBOPTools_1_1SplitFeatures_1_1ViewProviderXOR.html#a0895ad8a44b7eedf3d6a3fe62d74d13d),
[PathScripts.PathArray.ViewProviderArray.claimChildren()](../../dc/d4b/classPathScripts_1_1PathArray_1_1ViewProviderArray.html#a72d7ebded8be896fc0fa0bbb51a9bad2),
[PathScripts.PathDressupDragknife.ViewProviderDressup.claimChildren()](../../dc/d40/classPathScripts_1_1PathDressupDragknife_1_1ViewProviderDressup.html#a4f777850f1b59aca4952abde91a7ccc5),
[Spreadsheet_legacy.ViewProviderSpreadsheet.claimChildren()](../../d6/d84/classSpreadsheet__legacy_1_1ViewProviderSpreadsheet.html#a75aee00167480ff54cda421089caf2b3),
[PathScripts.PathOpGui.ViewProvider.clearTaskPanel()](../../db/df9/classPathScripts_1_1PathOpGui_1_1ViewProvider.html#a0f0a681075169c842b6ef664d12e299f),
[ArchBuildingPart.ViewProviderBuildingPart.cloneUp()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a6366b98cd7014623882d0445b0793949),
[ArchStructure.StructureTaskPanel.connectNodes()](../../df/d40/classArchStructure_1_1StructureTaskPanel.html#a7fc1254310c33bcf68f2809b5c827d64),
[ArchBuildingPart.ViewProviderBuildingPart.createGroup()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a0b72fbb5f93798cf75d6a232fb4b6a78),
[draftviewproviders.view_text.ViewProviderText.createObject()](../../db/dd9/classdraftviewproviders_1_1view__text_1_1ViewProviderText.html#a099b67b0359be25643d8abb175a6abfd),
[femviewprovider.view_mesh_gmsh.VPMeshGmsh.doubleClicked()](../../df/dbc/classfemviewprovider_1_1view__mesh__gmsh_1_1VPMeshGmsh.html#ab143d9b2417322495c5f98fa265ecacc),
[femviewprovider.view_mesh_gmsh.VPMeshGmsh.dragObject()](../../df/dbc/classfemviewprovider_1_1view__mesh__gmsh_1_1VPMeshGmsh.html#a41f4eeda1719d09e0db2a3b402cb5a56),
[BOPTools.JoinFeatures.ViewProviderConnect.dragObject()](../../da/d91/classBOPTools_1_1JoinFeatures_1_1ViewProviderConnect.html#a06e7f838195463e1b2d5e5eabc29d290),
[BOPTools.SplitFeatures.ViewProviderBooleanFragments.dragObject()](../../d0/d5a/classBOPTools_1_1SplitFeatures_1_1ViewProviderBooleanFragments.html#a32dd55908ef2535cad23580b9d8596be),
[BOPTools.SplitFeatures.ViewProviderXOR.dragObject()](../../d9/de4/classBOPTools_1_1SplitFeatures_1_1ViewProviderXOR.html#a09cd02ab0ba914e57cd2ece69fe77326),
[femviewprovider.view_mesh_gmsh.VPMeshGmsh.dropObject()](../../df/dbc/classfemviewprovider_1_1view__mesh__gmsh_1_1VPMeshGmsh.html#a29495e1ff56538caae1715408927c1b0),
[BOPTools.JoinFeatures.ViewProviderConnect.dropObject()](../../da/d91/classBOPTools_1_1JoinFeatures_1_1ViewProviderConnect.html#a3b5606e9058d9a40e2748a919c52e0d7),
[BOPTools.SplitFeatures.ViewProviderBooleanFragments.dropObject()](../../d0/d5a/classBOPTools_1_1SplitFeatures_1_1ViewProviderBooleanFragments.html#a233cc2803b0ee265b53c9925888e9de1),
[BOPTools.SplitFeatures.ViewProviderXOR.dropObject()](../../d9/de4/classBOPTools_1_1SplitFeatures_1_1ViewProviderXOR.html#a2a72acfa817cfd748982012c93fbd146),
[ArchStructure.StructureTaskPanel.extendNodes()](../../df/d40/classArchStructure_1_1StructureTaskPanel.html#a9ec5f0d27353c9cfed0826e541374f42),
[draftviewproviders.view_wire.ViewProviderWire.flatten()](../../da/dd2/classdraftviewproviders_1_1view__wire_1_1ViewProviderWire.html#a15505f930754af9e7bbff1aafe36249b),
[Mod.Show.Containers.Container.getCSChildren()](../../db/d52/classMod_1_1Show_1_1Containers_1_1Container.html#a3687b82f3a4172c04d80a17ef53b05b7),
[Mod.Show.Containers.Container.getDynamicChildren()](../../db/d52/classMod_1_1Show_1_1Containers_1_1Container.html#aecd0ce4fde06f71204eb5c611dd68840),
[ArchBuildingPart.ViewProviderBuildingPart.getIcon()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#ada13727d3aea660f86f34f5df06b0aea),
[ArchComponent.ViewProviderComponent.getIcon()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a82a5ba6de8551331198da2ba601e4bc2),
[draftviewproviders.view_array.ViewProviderDraftArray.getIcon()](../../dd/def/classdraftviewproviders_1_1view__array_1_1ViewProviderDraftArray.html#a2b7965750ecea6c17f44550bd2660a32),
[draftviewproviders.view_base.ViewProviderDraft.getIcon()](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#a200d7d3a9327ed8bbecf19cfac5c928e),
[draftviewproviders.view_dimension.ViewProviderDimensionBase.getIcon()](../../d6/d45/classdraftviewproviders_1_1view__dimension_1_1ViewProviderDimensionBase.html#acb3d1b672982c5750e2b4c7c4f0d063c),
[draftviewproviders.view_draftlink.ViewProviderDraftLink.getIcon()](../../d1/d79/classdraftviewproviders_1_1view__draftlink_1_1ViewProviderDraftLink.html#a30a8b44b0c675a7a300309e96417498e),
[femviewprovider.view_base_femobject.VPBaseFemObject.getIcon()](../../d0/d48/classfemviewprovider_1_1view__base__femobject_1_1VPBaseFemObject.html#af07b44b252f1be263ffd71892a8d9b20),
[femviewprovider.view_material_common.VPMaterialCommon.getIcon()](../../d8/df6/classfemviewprovider_1_1view__material__common_1_1VPMaterialCommon.html#aa19df62fbdb89b9ee863dce098d229da),
[OpenSCADFeatures.ViewProviderTree.getIcon()](../../df/dbf/classOpenSCADFeatures_1_1ViewProviderTree.html#ad8bf05f7bcbfef30282e646631acf36f),
[PathScripts.PathOpGui.ViewProvider.getIcon()](../../db/df9/classPathScripts_1_1PathOpGui_1_1ViewProvider.html#a6154aebd4655ece396c2ea0bacf6d415),
[Mod.Show.Containers.Container.getStaticChildren()](../../db/d52/classMod_1_1Show_1_1Containers_1_1Container.html#a083f7249986230ffb0069cb038095de7),
[Mod.Show.Containers.Container.getVisGroupChildren()](../../db/d52/classMod_1_1Show_1_1Containers_1_1Container.html#ad66cc3e90a04483f43e0455444e7c3e7),
[Mod.Show.Containers.Container.hasObjectRecursive()](../../db/d52/classMod_1_1Show_1_1Containers_1_1Container.html#a6eae499efb1d78a62ceae274d4a6c0f1),
[draftviewproviders.view_dimension.ViewProviderLinearDimension.is_linked_to_circle()](../../dc/d15/classdraftviewproviders_1_1view__dimension_1_1ViewProviderLinearDimension.html#aaae3dfca7794451c171ebd03b69af75f),
[Mod.Show.Containers.Container.isACS()](../../db/d52/classMod_1_1Show_1_1Containers_1_1Container.html#aec1b5743b2103cf4ee93d7d8e23a7780),
[ArchSchedule.CommandArchSchedule.IsActive()](../../d3/d2d/classArchSchedule_1_1CommandArchSchedule.html#aea4e379076ac7837ef44222df95fd97a),
[Mod.Show.Containers.Container.isAVisGroup()](../../db/d52/classMod_1_1Show_1_1Containers_1_1Container.html#a5e85a6f770a25900a637717dd3fd0885),
[Mod.Show.Containers.Container.isChildVisible()](../../db/d52/classMod_1_1Show_1_1Containers_1_1Container.html#ad46933cfaeeb44b002cb51bcf7c03e90),
[draftviewproviders.view_layer.ViewProviderLayerContainer.merge_by_name()](../../d1/dec/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayerContainer.html#a05e04faac4d4e363cc32bbc80e21a790),
[draftviewproviders.view_base.ViewProviderDraft.onChanged()](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#a97a75182f0c1f89d1140bfd91b0f72e2),
[BOPTools.JoinFeatures.ViewProviderEmbed.onDelete()](../../dc/d41/classBOPTools_1_1JoinFeatures_1_1ViewProviderEmbed.html#ae1df13f2bec676a45397e3a522246588),
[BOPTools.JoinFeatures.ViewProviderCutout.onDelete()](../../d4/d85/classBOPTools_1_1JoinFeatures_1_1ViewProviderCutout.html#a2665fc3bd0ffe461f9e3a8add08fe5fb),
[ArchReference.ViewProviderArchReference.onOpen()](../../d2/dfd/classArchReference_1_1ViewProviderArchReference.html#a61e3b48c424bfa0bf63e0a53f8c9ef2d),
[ArchReference.ViewProviderArchReference.onReload()](../../d2/dfd/classArchReference_1_1ViewProviderArchReference.html#ac1595166c3d83f9fca7d584a5cd0de82),
[ArchBuildingPart.ViewProviderBuildingPart.reorder()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a6c9e0e73fdbdc24fefd4b1a116028fae),
[ArchStructure.StructureTaskPanel.resetNodes()](../../df/d40/classArchStructure_1_1StructureTaskPanel.html#a80f7f79284c7da706d4383f122e02d2d),
[draftviewproviders.view_layer.ViewProviderLayer.select_contents()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#a68e11d79df17d156a11e517b2e4502a9),
[Mod.Show.Containers.Container.self_check()](../../db/d52/classMod_1_1Show_1_1Containers_1_1Container.html#a8d9f9bcbb3075bae260f27d662758dd7),
[ArchComponent.ViewProviderComponent.setDisplayMode()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#aa0542b1ecb134c494a26706a5f41d099),
[ArchComponent.ViewProviderComponent.setEdit()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#aead5dc101b4fb331c6905a022017846d),
[Mod.PartDesign.SprocketFeature.ViewProviderSprocket.setEdit()](../../da/d59/classMod_1_1PartDesign_1_1SprocketFeature_1_1ViewProviderSprocket.html#aa6d4cdd2dac11b7da5f1e3332a28c1fc),
[ArchStructure.StructureTaskPanel.setSelectionFromTool()](../../df/d40/classArchStructure_1_1StructureTaskPanel.html#ac80cd7068ded6e0fa2ceaa7c7fbfacf4),
[ArchStructure.StructureTaskPanel.setToolFromSelection()](../../df/d40/classArchStructure_1_1StructureTaskPanel.html#aaf6f1a737e2e9b8b1c685ffe4b88c489),
[PathScripts.PathOpGui.ViewProvider.setupTaskPanel()](../../db/df9/classPathScripts_1_1PathOpGui_1_1ViewProvider.html#a5ed23a9193fce9cd04149a0e0920ebd9),
[ArchBuildingPart.ViewProviderBuildingPart.setWorkingPlane()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#ace07507d5e9696c6fc3603cbbcf0fa09),
[femviewprovider.view_result_mechanical.VPResultMechanical.unsetEdit()](../../d7/d8f/classfemviewprovider_1_1view__result__mechanical_1_1VPResultMechanical.html#a16c06fb14a5a7d3e3a4063a218dc7a40),
[ArchBuildingPart.ViewProviderBuildingPart.writeCamera()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a3b1b1c7b54a861a46eab90dd1fdbc49c),
[draftviewproviders.view_wpproxy.ViewProviderWorkingPlaneProxy.writeCamera()](../../da/dbf/classdraftviewproviders_1_1view__wpproxy_1_1ViewProviderWorkingPlaneProxy.html#abd46fb66b0e0bd5d23dc238cf427f3a5),
[ArchBuildingPart.ViewProviderBuildingPart.writeInventor()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#ae11999336601ac7fd9927d433b9f6884),
and
[draftviewproviders.view_wpproxy.ViewProviderWorkingPlaneProxy.writeState()](../../da/dbf/classdraftviewproviders_1_1view__wpproxy_1_1ViewProviderWorkingPlaneProxy.html#aa67186706faef974f14da09b45a94ca0).

## ◆ ViewObject

BOPTools.SplitFeatures.ViewProviderSlice.ViewObject  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Part/BOPTools/SplitFeatures.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

