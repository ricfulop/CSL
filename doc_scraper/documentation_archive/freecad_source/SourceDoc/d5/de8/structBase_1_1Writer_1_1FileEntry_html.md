---
url: https://freecad.github.io/SourceDoc/d5/de8/structBase_1_1Writer_1_1FileEntry.html
scraped_at: 2025-09-08T15:18:15.309790
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [Writer](../../dd/d4d/classBase_1_1Writer.html)
  * [FileEntry](../../d5/de8/structBase_1_1Writer_1_1FileEntry.html)

[List of all members](../../dd/d22/structBase_1_1Writer_1_1FileEntry-members.html) | Public Attributes

Base::Writer::FileEntry Struct Reference

`#include <Writer.h>`

##  Public Attributes  
  
---  
std::string | [FileName](../../d5/de8/structBase_1_1Writer_1_1FileEntry.html#abd6c12817010758a25f9af39c2c3a70c)  
const [Base::Persistence](../../d9/d25/classBase_1_1Persistence.html) * | [Object](../../d5/de8/structBase_1_1Writer_1_1FileEntry.html#a15a35046c9bd5dad11dd5d97c18d675f)  
  
## Member Data Documentation

## ◆ FileName

std::string Base::Writer::FileEntry::FileName  
---  
  
Referenced by
[Base::Writer::addFile()](../../dd/d4d/classBase_1_1Writer.html#a253afcb774015eed79da264548ef4b55),
[Base::ZipWriter::writeFiles()](../../d9/df3/classBase_1_1ZipWriter.html#a473a5caab984aaff00f0b6dba44b6b0a),
[Base::FileWriter::writeFiles()](../../df/de4/classBase_1_1FileWriter.html#a617e36a2afd38f0317aa3b6789d48805),
[Gui::RecoveryWriter::writeFiles()](../../d9/d25/classGui_1_1RecoveryWriter.html#a943a1fe17a358266e1e6566c69c91e4c),
and
[Cloud::CloudWriter::writeFiles()](../../d0/d23/classCloud_1_1CloudWriter.html#ae10b7fa9f42a7c2b6cd73c6c9fb33b38).

## ◆ Object

const [Base::Persistence](../../d9/d25/classBase_1_1Persistence.html)*
Base::Writer::FileEntry::Object  
---  
  
Referenced by
[draftviewproviders.view_layer.ViewProviderLayer::activate()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#a100c49f5d1966d59f546943ce6685a08),
[ArchPanel.CommandPanelSheet::Activated()](../../d1/d94/classArchPanel_1_1CommandPanelSheet.html#abed1cd5ce53c5b156683ae24b81f75e4),
[ArchStructure.CommandStructuralSystem::Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[Base::Writer::addFile()](../../dd/d4d/classBase_1_1Writer.html#a253afcb774015eed79da264548ef4b55),
[OpenSCADFeatures.ViewProviderTree::attach()](../../df/dbf/classOpenSCADFeatures_1_1ViewProviderTree.html#a489f372b544fde950f6c94fe469ca039),
[ArchComponent.ViewProviderComponent::attach()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a35e80ee0b359823d7b9cecc23481b930),
[draftviewproviders.view_base.ViewProviderDraft::attach()](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#af35acb7285aa095bf670e82338c9462d),
[draftviewproviders.view_dimension.ViewProviderLinearDimension::attach()](../../dc/d15/classdraftviewproviders_1_1view__dimension_1_1ViewProviderLinearDimension.html#a6e8d37d9155778fc70b27e7d4e607f0b),
[draftviewproviders.view_dimension.ViewProviderAngularDimension::attach()](../../d5/d88/classdraftviewproviders_1_1view__dimension_1_1ViewProviderAngularDimension.html#a61b1ca60b7451140459dddaa2f2ff3db),
[draftviewproviders.view_draft_annotation.ViewProviderDraftAnnotation::attach()](../../d2/d24/classdraftviewproviders_1_1view__draft__annotation_1_1ViewProviderDraftAnnotation.html#a9d020c35cc375c2d2e91ab96c4563c8e),
[draftviewproviders.view_layer.ViewProviderLayer::attach()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#ab2a5fd20d4ab9b7d49e3a3e4d4ac8e78),
[draftviewproviders.view_layer.ViewProviderLayerContainer::attach()](../../d1/dec/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayerContainer.html#a5b25eb9ee95736d4049f5c11ea5977d0),
[PathScripts.PathArray.ViewProviderArray::attach()](../../dc/d4b/classPathScripts_1_1PathArray_1_1ViewProviderArray.html#abb70607468b63e690ee6dff23a4c3ef4),
[PathScripts.PathCopy.ViewProviderPathCopy::attach()](../../de/d45/classPathScripts_1_1PathCopy_1_1ViewProviderPathCopy.html#a7ba0a28dd4dac2a343da660cf7b8963c),
[PathScripts.PathDressupDragknife.ViewProviderDressup::attach()](../../dc/d40/classPathScripts_1_1PathDressupDragknife_1_1ViewProviderDressup.html#a302aaf7765dfd69f37d77c2e84dc0e91),
[PathScripts.PathHop.ViewProviderPathHop::attach()](../../da/dfa/classPathScripts_1_1PathHop_1_1ViewProviderPathHop.html#a28aaff1dcea04ba21c42974c68365ac3),
[PathScripts.PathOpGui.ViewProvider::attach()](../../db/df9/classPathScripts_1_1PathOpGui_1_1ViewProvider.html#a0840fdecdfbaaf3ffca3bcb866b39452),
[ArchSite.Compass::buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[ArchReference.ViewProviderArchReference::checkChanges()](../../d2/dfd/classArchReference_1_1ViewProviderArchReference.html#ab6a807091ea186d4252888a09f6b41ba),
[ArchComponent.ViewProviderComponent::claimChildren()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a05a3bbd9534c922df9943f971fd60bf2),
[draftviewproviders.view_base.ViewProviderDraft::claimChildren()](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#af0b551826340210d20874aa39175d3d5),
[draftviewproviders.view_draft_annotation.ViewProviderDraftAnnotation::claimChildren()](../../d2/d24/classdraftviewproviders_1_1view__draft__annotation_1_1ViewProviderDraftAnnotation.html#a588193f8dd5a57aae96a9571459b8e37),
[draftviewproviders.view_draftlink.ViewProviderDraftLink::claimChildren()](../../d1/d79/classdraftviewproviders_1_1view__draftlink_1_1ViewProviderDraftLink.html#a41b6cffae3663a58647a9227c4e1664a),
[draftviewproviders.view_layer.ViewProviderLayer::claimChildren()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#a8123f33a456b8fefa43a42fd11b82aa0),
[draftviewproviders.view_wire.ViewProviderWire::claimChildren()](../../da/dd2/classdraftviewproviders_1_1view__wire_1_1ViewProviderWire.html#a13e60e240bfcc6a291b5cf450367ad73),
[femviewprovider.view_mesh_gmsh.VPMeshGmsh::claimChildren()](../../df/dbc/classfemviewprovider_1_1view__mesh__gmsh_1_1VPMeshGmsh.html#a56cb33c198c8ed418656815f3d8c7abc),
[femviewprovider.view_result_mechanical.VPResultMechanical::claimChildren()](../../d7/d8f/classfemviewprovider_1_1view__result__mechanical_1_1VPResultMechanical.html#ab355e3a1025ce59b6797302f29c6d0c1),
[OpenSCADFeatures.ViewProviderTree::claimChildren()](../../df/dbf/classOpenSCADFeatures_1_1ViewProviderTree.html#aa51082a21dda8cd8ac4bfc75b8107936),
[BOPTools.JoinFeatures.ViewProviderConnect::claimChildren()](../../da/d91/classBOPTools_1_1JoinFeatures_1_1ViewProviderConnect.html#a2d75d1b98bfa1e05bbedc171ec608893),
[BOPTools.JoinFeatures.ViewProviderEmbed::claimChildren()](../../dc/d41/classBOPTools_1_1JoinFeatures_1_1ViewProviderEmbed.html#a468ee613f1d258009912c0f46dda8fdc),
[BOPTools.JoinFeatures.ViewProviderCutout::claimChildren()](../../d4/d85/classBOPTools_1_1JoinFeatures_1_1ViewProviderCutout.html#a4a0700249e2817cbe2f9c8b6e5b6f283),
[BOPTools.SplitFeatures.ViewProviderBooleanFragments::claimChildren()](../../d0/d5a/classBOPTools_1_1SplitFeatures_1_1ViewProviderBooleanFragments.html#a0905dfd15884082d80692f0923c87a93),
[BOPTools.SplitFeatures.ViewProviderSlice::claimChildren()](../../d5/d19/classBOPTools_1_1SplitFeatures_1_1ViewProviderSlice.html#a45243295181580dda3d489d0342026ed),
[BOPTools.SplitFeatures.ViewProviderXOR::claimChildren()](../../d9/de4/classBOPTools_1_1SplitFeatures_1_1ViewProviderXOR.html#a0895ad8a44b7eedf3d6a3fe62d74d13d),
[PathScripts.PathArray.ViewProviderArray::claimChildren()](../../dc/d4b/classPathScripts_1_1PathArray_1_1ViewProviderArray.html#a72d7ebded8be896fc0fa0bbb51a9bad2),
[PathScripts.PathDressupDragknife.ViewProviderDressup::claimChildren()](../../dc/d40/classPathScripts_1_1PathDressupDragknife_1_1ViewProviderDressup.html#a4f777850f1b59aca4952abde91a7ccc5),
[Spreadsheet_legacy.ViewProviderSpreadsheet::claimChildren()](../../d6/d84/classSpreadsheet__legacy_1_1ViewProviderSpreadsheet.html#a75aee00167480ff54cda421089caf2b3),
[PathScripts.PathOpGui.ViewProvider::clearTaskPanel()](../../db/df9/classPathScripts_1_1PathOpGui_1_1ViewProvider.html#a0f0a681075169c842b6ef664d12e299f),
[ArchBuildingPart.ViewProviderBuildingPart::cloneUp()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a6366b98cd7014623882d0445b0793949),
[ArchStructure.StructureTaskPanel::connectNodes()](../../df/d40/classArchStructure_1_1StructureTaskPanel.html#a7fc1254310c33bcf68f2809b5c827d64),
[ArchBuildingPart.ViewProviderBuildingPart::createGroup()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a0b72fbb5f93798cf75d6a232fb4b6a78),
[draftviewproviders.view_text.ViewProviderText::createObject()](../../db/dd9/classdraftviewproviders_1_1view__text_1_1ViewProviderText.html#a099b67b0359be25643d8abb175a6abfd),
[femviewprovider.view_mesh_gmsh.VPMeshGmsh::doubleClicked()](../../df/dbc/classfemviewprovider_1_1view__mesh__gmsh_1_1VPMeshGmsh.html#ab143d9b2417322495c5f98fa265ecacc),
[femviewprovider.view_mesh_gmsh.VPMeshGmsh::dragObject()](../../df/dbc/classfemviewprovider_1_1view__mesh__gmsh_1_1VPMeshGmsh.html#a41f4eeda1719d09e0db2a3b402cb5a56),
[BOPTools.JoinFeatures.ViewProviderConnect::dragObject()](../../da/d91/classBOPTools_1_1JoinFeatures_1_1ViewProviderConnect.html#a06e7f838195463e1b2d5e5eabc29d290),
[BOPTools.SplitFeatures.ViewProviderBooleanFragments::dragObject()](../../d0/d5a/classBOPTools_1_1SplitFeatures_1_1ViewProviderBooleanFragments.html#a32dd55908ef2535cad23580b9d8596be),
[BOPTools.SplitFeatures.ViewProviderXOR::dragObject()](../../d9/de4/classBOPTools_1_1SplitFeatures_1_1ViewProviderXOR.html#a09cd02ab0ba914e57cd2ece69fe77326),
[femviewprovider.view_mesh_gmsh.VPMeshGmsh::dropObject()](../../df/dbc/classfemviewprovider_1_1view__mesh__gmsh_1_1VPMeshGmsh.html#a29495e1ff56538caae1715408927c1b0),
[BOPTools.JoinFeatures.ViewProviderConnect::dropObject()](../../da/d91/classBOPTools_1_1JoinFeatures_1_1ViewProviderConnect.html#a3b5606e9058d9a40e2748a919c52e0d7),
[BOPTools.SplitFeatures.ViewProviderBooleanFragments::dropObject()](../../d0/d5a/classBOPTools_1_1SplitFeatures_1_1ViewProviderBooleanFragments.html#a233cc2803b0ee265b53c9925888e9de1),
[BOPTools.SplitFeatures.ViewProviderXOR::dropObject()](../../d9/de4/classBOPTools_1_1SplitFeatures_1_1ViewProviderXOR.html#a2a72acfa817cfd748982012c93fbd146),
[ArchStructure.StructureTaskPanel::extendNodes()](../../df/d40/classArchStructure_1_1StructureTaskPanel.html#a9ec5f0d27353c9cfed0826e541374f42),
[draftviewproviders.view_wire.ViewProviderWire::flatten()](../../da/dd2/classdraftviewproviders_1_1view__wire_1_1ViewProviderWire.html#a15505f930754af9e7bbff1aafe36249b),
[Mod.Show.Containers.Container::getCSChildren()](../../db/d52/classMod_1_1Show_1_1Containers_1_1Container.html#a3687b82f3a4172c04d80a17ef53b05b7),
[Mod.Show.Containers.Container::getDynamicChildren()](../../db/d52/classMod_1_1Show_1_1Containers_1_1Container.html#aecd0ce4fde06f71204eb5c611dd68840),
[ArchBuildingPart.ViewProviderBuildingPart::getIcon()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#ada13727d3aea660f86f34f5df06b0aea),
[ArchComponent.ViewProviderComponent::getIcon()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a82a5ba6de8551331198da2ba601e4bc2),
[draftviewproviders.view_array.ViewProviderDraftArray::getIcon()](../../dd/def/classdraftviewproviders_1_1view__array_1_1ViewProviderDraftArray.html#a2b7965750ecea6c17f44550bd2660a32),
[draftviewproviders.view_base.ViewProviderDraft::getIcon()](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#a200d7d3a9327ed8bbecf19cfac5c928e),
[draftviewproviders.view_dimension.ViewProviderDimensionBase::getIcon()](../../d6/d45/classdraftviewproviders_1_1view__dimension_1_1ViewProviderDimensionBase.html#acb3d1b672982c5750e2b4c7c4f0d063c),
[draftviewproviders.view_draftlink.ViewProviderDraftLink::getIcon()](../../d1/d79/classdraftviewproviders_1_1view__draftlink_1_1ViewProviderDraftLink.html#a30a8b44b0c675a7a300309e96417498e),
[femviewprovider.view_base_femobject.VPBaseFemObject::getIcon()](../../d0/d48/classfemviewprovider_1_1view__base__femobject_1_1VPBaseFemObject.html#af07b44b252f1be263ffd71892a8d9b20),
[femviewprovider.view_material_common.VPMaterialCommon::getIcon()](../../d8/df6/classfemviewprovider_1_1view__material__common_1_1VPMaterialCommon.html#aa19df62fbdb89b9ee863dce098d229da),
[OpenSCADFeatures.ViewProviderTree::getIcon()](../../df/dbf/classOpenSCADFeatures_1_1ViewProviderTree.html#ad8bf05f7bcbfef30282e646631acf36f),
[PathScripts.PathOpGui.ViewProvider::getIcon()](../../db/df9/classPathScripts_1_1PathOpGui_1_1ViewProvider.html#a6154aebd4655ece396c2ea0bacf6d415),
[Mod.Show.Containers.Container::getStaticChildren()](../../db/d52/classMod_1_1Show_1_1Containers_1_1Container.html#a083f7249986230ffb0069cb038095de7),
[Mod.Show.Containers.Container::getVisGroupChildren()](../../db/d52/classMod_1_1Show_1_1Containers_1_1Container.html#ad66cc3e90a04483f43e0455444e7c3e7),
[Mod.Show.Containers.Container::hasObjectRecursive()](../../db/d52/classMod_1_1Show_1_1Containers_1_1Container.html#a6eae499efb1d78a62ceae274d4a6c0f1),
[draftviewproviders.view_dimension.ViewProviderLinearDimension::is_linked_to_circle()](../../dc/d15/classdraftviewproviders_1_1view__dimension_1_1ViewProviderLinearDimension.html#aaae3dfca7794451c171ebd03b69af75f),
[Mod.Show.Containers.Container::isACS()](../../db/d52/classMod_1_1Show_1_1Containers_1_1Container.html#aec1b5743b2103cf4ee93d7d8e23a7780),
[ArchSchedule.CommandArchSchedule::IsActive()](../../d3/d2d/classArchSchedule_1_1CommandArchSchedule.html#aea4e379076ac7837ef44222df95fd97a),
[Mod.Show.Containers.Container::isAVisGroup()](../../db/d52/classMod_1_1Show_1_1Containers_1_1Container.html#a5e85a6f770a25900a637717dd3fd0885),
[Mod.Show.Containers.Container::isChildVisible()](../../db/d52/classMod_1_1Show_1_1Containers_1_1Container.html#ad46933cfaeeb44b002cb51bcf7c03e90),
[draftviewproviders.view_layer.ViewProviderLayerContainer::merge_by_name()](../../d1/dec/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayerContainer.html#a05e04faac4d4e363cc32bbc80e21a790),
[draftviewproviders.view_base.ViewProviderDraft::onChanged()](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#a97a75182f0c1f89d1140bfd91b0f72e2),
[BOPTools.JoinFeatures.ViewProviderEmbed::onDelete()](../../dc/d41/classBOPTools_1_1JoinFeatures_1_1ViewProviderEmbed.html#ae1df13f2bec676a45397e3a522246588),
[BOPTools.JoinFeatures.ViewProviderCutout::onDelete()](../../d4/d85/classBOPTools_1_1JoinFeatures_1_1ViewProviderCutout.html#a2665fc3bd0ffe461f9e3a8add08fe5fb),
[ArchReference.ViewProviderArchReference::onOpen()](../../d2/dfd/classArchReference_1_1ViewProviderArchReference.html#a61e3b48c424bfa0bf63e0a53f8c9ef2d),
[ArchReference.ViewProviderArchReference::onReload()](../../d2/dfd/classArchReference_1_1ViewProviderArchReference.html#ac1595166c3d83f9fca7d584a5cd0de82),
[ArchBuildingPart.ViewProviderBuildingPart::reorder()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a6c9e0e73fdbdc24fefd4b1a116028fae),
[ArchStructure.StructureTaskPanel::resetNodes()](../../df/d40/classArchStructure_1_1StructureTaskPanel.html#a80f7f79284c7da706d4383f122e02d2d),
[draftviewproviders.view_layer.ViewProviderLayer::select_contents()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#a68e11d79df17d156a11e517b2e4502a9),
[Mod.Show.Containers.Container::self_check()](../../db/d52/classMod_1_1Show_1_1Containers_1_1Container.html#a8d9f9bcbb3075bae260f27d662758dd7),
[ArchComponent.ViewProviderComponent::setDisplayMode()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#aa0542b1ecb134c494a26706a5f41d099),
[ArchComponent.ViewProviderComponent::setEdit()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#aead5dc101b4fb331c6905a022017846d),
[Mod.PartDesign.SprocketFeature.ViewProviderSprocket::setEdit()](../../da/d59/classMod_1_1PartDesign_1_1SprocketFeature_1_1ViewProviderSprocket.html#aa6d4cdd2dac11b7da5f1e3332a28c1fc),
[ArchStructure.StructureTaskPanel::setSelectionFromTool()](../../df/d40/classArchStructure_1_1StructureTaskPanel.html#ac80cd7068ded6e0fa2ceaa7c7fbfacf4),
[ArchStructure.StructureTaskPanel::setToolFromSelection()](../../df/d40/classArchStructure_1_1StructureTaskPanel.html#aaf6f1a737e2e9b8b1c685ffe4b88c489),
[PathScripts.PathOpGui.ViewProvider::setupTaskPanel()](../../db/df9/classPathScripts_1_1PathOpGui_1_1ViewProvider.html#a5ed23a9193fce9cd04149a0e0920ebd9),
[ArchBuildingPart.ViewProviderBuildingPart::setWorkingPlane()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#ace07507d5e9696c6fc3603cbbcf0fa09),
[femviewprovider.view_result_mechanical.VPResultMechanical::unsetEdit()](../../d7/d8f/classfemviewprovider_1_1view__result__mechanical_1_1VPResultMechanical.html#a16c06fb14a5a7d3e3a4063a218dc7a40),
[ArchBuildingPart.ViewProviderBuildingPart::writeCamera()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a3b1b1c7b54a861a46eab90dd1fdbc49c),
[draftviewproviders.view_wpproxy.ViewProviderWorkingPlaneProxy::writeCamera()](../../da/dbf/classdraftviewproviders_1_1view__wpproxy_1_1ViewProviderWorkingPlaneProxy.html#abd46fb66b0e0bd5d23dc238cf427f3a5),
[Base::ZipWriter::writeFiles()](../../d9/df3/classBase_1_1ZipWriter.html#a473a5caab984aaff00f0b6dba44b6b0a),
[Base::FileWriter::writeFiles()](../../df/de4/classBase_1_1FileWriter.html#a617e36a2afd38f0317aa3b6789d48805),
[Gui::RecoveryWriter::writeFiles()](../../d9/d25/classGui_1_1RecoveryWriter.html#a943a1fe17a358266e1e6566c69c91e4c),
[Cloud::CloudWriter::writeFiles()](../../d0/d23/classCloud_1_1CloudWriter.html#ae10b7fa9f42a7c2b6cd73c6c9fb33b38),
[ArchBuildingPart.ViewProviderBuildingPart::writeInventor()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#ae11999336601ac7fd9927d433b9f6884),
and
[draftviewproviders.view_wpproxy.ViewProviderWorkingPlaneProxy::writeState()](../../da/dbf/classdraftviewproviders_1_1view__wpproxy_1_1ViewProviderWorkingPlaneProxy.html#aa67186706faef974f14da09b45a94ca0).

* * *

The documentation for this struct was generated from the following file:

  * FreeCAD/src/Base/Writer.h

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

