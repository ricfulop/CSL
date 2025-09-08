---
url: https://freecad.github.io/SourceDoc/dd/d1b/classArchComponent_1_1ViewProviderComponent.html
scraped_at: 2025-09-08T14:57:38.223360
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ArchComponent](../../da/d62/namespaceArchComponent.html)
  * [ViewProviderComponent](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html)

[List of all members](../../d2/d1c/classArchComponent_1_1ViewProviderComponent-members.html) | Public Member Functions | Public Attributes

ArchComponent.ViewProviderComponent Class Reference

##  Public Member Functions  
  
---  
def | [areDifferentColors](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#abef0fbecf4fb23a8a2e956782435dbc8) (self, a, b)  
def | [attach](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a35e80ee0b359823d7b9cecc23481b930) (self, vobj)  
def | [claimChildren](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a05a3bbd9534c922df9943f971fd60bf2) (self)  
def | [colorize](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#ac78064634eb8dcc79b78058091f9e93f) (self, obj, force=False)  
def | [getDisplayModes](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a0d8c5720e1a9f11604ad7e354b87c513) (self, vobj)  
def | [getIcon](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a82a5ba6de8551331198da2ba601e4bc2) (self)  
def | [onChanged](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a14303b12cf40f4c4393c5d86c08820bf) (self, vobj, prop)  
def | [setDisplayMode](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#aa0542b1ecb134c494a26706a5f41d099) (self, mode)  
def | [setEdit](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#aead5dc101b4fb331c6905a022017846d) (self, vobj, mode)  
def | [setProperties](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#abbd3e374ae515673bada8f848fbc98af) (self, vobj)  
def | [setupContextMenu](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a9cb06662d675ab2a3f956c0b7672a64c) (self, vobj, menu)  
def | [toggleSubcomponents](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#afdd01b4893303b90769e0870a675b7b9) (self)  
def | [unsetEdit](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#aee3ff9b804a7bb9866152879ca13b5e3) (self, vobj, mode)  
def | [updateData](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#ad521883fec55dd63135b0dbb597dabdb) (self, obj, prop)  
  
##  Public Attributes  
  
---  
|
[hiresgroup](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#adb5745944ae9b415394ada099f13d717)  
|
[meshcolor](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#ab82023aa98281fdd4fdb9aee6eb05466)  
|
[meshnode](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#acb568729ce3429c521c62c72135e221a)  
|
[Object](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a597cb57c8f3b67265e32073313fc7140)  
  
## Detailed Description

    
    
    A default View Provider for Component objects.
    
    Acts as a base for all other Arch view providers. It's properties and
    behaviours are common to all Arch view providers.
    
    Parameters
    ----------
    vobj: <Gui.ViewProviderDocumentObject>
        The view provider to turn into a component view provider.
    

## Member Function Documentation

## ◆ areDifferentColors()

def ArchComponent.ViewProviderComponent.areDifferentColors  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _a_ ,   
|  |  | _b_  
| ) | |   
      
    
    Check if two diffuse colors are almost the same.
    
    Parameters
    ----------
    a: tuple
        The first DiffuseColor value to compare.
    a: tuple
        The second DiffuseColor value to compare.
    
    Returns
    -------
    bool:
        True if colors are different, false if they are similar.
    

Referenced by
[ArchComponent.ViewProviderComponent.colorize()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#ac78064634eb8dcc79b78058091f9e93f),
and
[ArchCurtainWall.ViewProviderCurtainWall.colorize()](../../d7/d61/classArchCurtainWall_1_1ViewProviderCurtainWall.html#a2c7de1b2acf70db3bdb71a48c67cbd94).

## ◆ attach()

def ArchComponent.ViewProviderComponent.attach  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _vobj_  
| ) | |   
      
    
    Add display modes' data to the coin scenegraph.
    
    Add each display mode as a coin node, whose parent is this view
    provider.
    
    Each display mode's node includes the data needed to display the object
    in that mode. This might include colors of faces, or the draw style of
    lines. This data is stored as additional coin nodes which are children
    of the display mode node.
    
    Add the HiRes display mode.
    
    Parameters
    ----------
    vobj: <Gui.ViewProviderDocumentObject>
        The component's view provider object.
    

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
[ArchWall.areSameWallTypes()](../../d2/d8e/namespaceArchWall.html#a289f6e980eba7dd10b74dcfb84dd0c92),
[ArchRebar.makeRebar()](../../dd/de9/namespaceArchRebar.html#a4f9bf27bce35bf45fc8f02cfd5a8078d),
and
[ArchSpace.removeSpaceBoundaries()](../../d8/d6a/namespaceArchSpace.html#aca020b8800ac48fabbf4fce2a0f16cee).

## ◆ claimChildren()

def ArchComponent.ViewProviderComponent.claimChildren  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    Define which objects will appear as children in the tree view.
    
    Set the host object's Base object as a child, and set any additions or
    subtractions as children.
    
    Parameters
    ----------
    vobj: <Gui.ViewProviderDocumentObject>
        The component's view provider object.
    
    Returns
    -------
    list of <App::DocumentObject>s:
        The objects claimed as children.
    

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
[ArchFrame.makeFrame()](../../d8/db6/namespaceArchFrame.html#a43a080855e00e52afc61334b48c48290),
[femviewprovider.view_mesh_gmsh.VPMeshGmsh.onDelete()](../../df/dbc/classfemviewprovider_1_1view__mesh__gmsh_1_1VPMeshGmsh.html#ae4c9ca343356d3acf252b0566b3ff01c),
[femviewprovider.view_result_mechanical.VPResultMechanical.onDelete()](../../d7/d8f/classfemviewprovider_1_1view__result__mechanical_1_1VPResultMechanical.html#a6bde7f2d215b4399295a2d2b426d6f4f),
[BOPTools.JoinFeatures.ViewProviderConnect.onDelete()](../../da/d91/classBOPTools_1_1JoinFeatures_1_1ViewProviderConnect.html#a7578eaa093ec056d3080b03f20244ca8),
[BOPTools.SplitFeatures.ViewProviderBooleanFragments.onDelete()](../../d0/d5a/classBOPTools_1_1SplitFeatures_1_1ViewProviderBooleanFragments.html#a1a561237cd3f10b60c442c5b6e63b794),
[BOPTools.SplitFeatures.ViewProviderSlice.onDelete()](../../d5/d19/classBOPTools_1_1SplitFeatures_1_1ViewProviderSlice.html#a20a3b8fa1e0921831683ebaae84baa98),
and
[BOPTools.SplitFeatures.ViewProviderXOR.onDelete()](../../d9/de4/classBOPTools_1_1SplitFeatures_1_1ViewProviderXOR.html#a199d8da22e104fa58c6b88685ffdfec1).

## ◆ colorize()

def ArchComponent.ViewProviderComponent.colorize  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_ ,   
|  |  | _force_ = `False`  
| ) | |   
      
    
    If an object is a clone, set it to copy the color of its parent.
    
    Only change the color of the clone if the clone and its parent have
    colors that are distinguishably different from each other.
    
    Parameters
    ----------
    obj: <Part::Feature>
        The object to change the color of.
    force: bool
        If true, forces the colourisation even if the two objects have very
        similar colors.
    

Reimplemented in
[ArchCurtainWall.ViewProviderCurtainWall](../../d7/d61/classArchCurtainWall_1_1ViewProviderCurtainWall.html#a2c7de1b2acf70db3bdb71a48c67cbd94).

References
[ArchComponent.ViewProviderComponent.areDifferentColors()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#abef0fbecf4fb23a8a2e956782435dbc8).

Referenced by
[ArchCurtainWall.ViewProviderCurtainWall.onChanged()](../../d7/d61/classArchCurtainWall_1_1ViewProviderCurtainWall.html#add541f453903121b6540cd9361af9bc7),
and
[ArchCurtainWall.ViewProviderCurtainWall.updateData()](../../d7/d61/classArchCurtainWall_1_1ViewProviderCurtainWall.html#a1c40a49ffebf36d0c5153dade5d6c8e0).

## ◆ getDisplayModes()

def ArchComponent.ViewProviderComponent.getDisplayModes  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _vobj_  
| ) | |   
      
    
    Define the display modes unique to the Arch Component.
    
    Define mode HiRes, which displays the component as a mesh, intended as
    a more visually appealing version of the component.
    
    Parameters
    ----------
    vobj: <Gui.ViewProviderDocumentObject>
        The component's view provider object.
    
    Returns
    -------
    list of str
        List containing the names of the new display modes.
    

Referenced by
[ArchWall.areSameWallTypes()](../../d2/d8e/namespaceArchWall.html#a289f6e980eba7dd10b74dcfb84dd0c92),
[ArchRebar.makeRebar()](../../dd/de9/namespaceArchRebar.html#a4f9bf27bce35bf45fc8f02cfd5a8078d),
and
[ArchSpace.removeSpaceBoundaries()](../../d8/d6a/namespaceArchSpace.html#aca020b8800ac48fabbf4fce2a0f16cee).

## ◆ getIcon()

def ArchComponent.ViewProviderComponent.getIcon  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    Return the path to the appropriate icon.
    
    If a clone, return the cloned component icon path. Otherwise return the
    Arch Component icon.
    
    Returns
    -------
    str
        Path to the appropriate icon .svg file.
    

Reimplemented in
[ArchCurtainWall.ViewProviderCurtainWall](../../d7/d61/classArchCurtainWall_1_1ViewProviderCurtainWall.html#a07883fa28b0d7ec4534bb6628cd419e2),
and
[ArchTruss.ViewProviderTruss](../../db/d3f/classArchTruss_1_1ViewProviderTruss.html#a820cb1de7e37e6a37f6e8f4f84d4054b).

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
[ArchAxisSystem.AxisSystemTaskPanel.update()](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a376cbba2ccee6efd86c46d0f0a8e99e3),
[ArchComponent.ComponentTaskPanel.update()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#af95b36032a3837b4bf1b92fe7c6a47e0),
and
[ArchSectionPlane.SectionPlaneTaskPanel.update()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#aab4bcd7b08950b8e3b37d801381c5162).

## ◆ onChanged()

def ArchComponent.ViewProviderComponent.onChanged  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _vobj_ ,   
|  |  | _prop_  
| ) | |   
      
    
    Method called when the view provider has a property changed.
    
    If DiffuseColor changes, change DiffuseColor to copy the host object's
    clone, if it exists.
    
    If ShapeColor changes, overwrite it with DiffuseColor.
    
    If Visibility changes, propagate the change to all view objects that
    are also hosted by this view object's host.
    
    Parameters
    ----------
    vobj: <Gui.ViewProviderDocumentObject>
        The component's view provider object.
    prop: string
        The name of the property that has changed.
    

Reimplemented in
[ArchCurtainWall.ViewProviderCurtainWall](../../d7/d61/classArchCurtainWall_1_1ViewProviderCurtainWall.html#add541f453903121b6540cd9361af9bc7).

Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftviewproviders.view_base.ViewProviderDraft.attach()](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#af35acb7285aa095bf670e82338c9462d),
[ArchSite.Compass.buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[draftobjects.wire.Wire.execute()](../../d4/d14/classdraftobjects_1_1wire_1_1Wire.html#ad931a4e79d7d0516803bf1a8a33e7655),
[ArchRebar.makeRebar()](../../dd/de9/namespaceArchRebar.html#a4f9bf27bce35bf45fc8f02cfd5a8078d),
[ArchCurtainWall.ViewProviderCurtainWall.onChanged()](../../d7/d61/classArchCurtainWall_1_1ViewProviderCurtainWall.html#add541f453903121b6540cd9361af9bc7),
[ArchBuildingPart.ViewProviderBuildingPart.updateData()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a12d40383666b8987a3277ea26454995d),
[ArchPanel.ViewProviderPanelCut.updateData()](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a970ed7e44ebec3c959dcb48bf60b2d31),
[ArchPanel.ViewProviderPanelSheet.updateData()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a916cdf8131f60494dabf61e971d1a093),
[draftviewproviders.view_label.ViewProviderLabel.updateData()](../../d1/d88/classdraftviewproviders_1_1view__label_1_1ViewProviderLabel.html#aab195af09dd4fbe60e1bb38d362385ba),
[draftviewproviders.view_layer.ViewProviderLayer.updateData()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#a9c641727fd15eaa141c8a58837e14248),
and
[draftviewproviders.view_wpproxy.ViewProviderWorkingPlaneProxy.updateData()](../../da/dbf/classdraftviewproviders_1_1view__wpproxy_1_1ViewProviderWorkingPlaneProxy.html#ad58eb6ce87860ff0389b3498143d11c7).

## ◆ setDisplayMode()

def ArchComponent.ViewProviderComponent.setDisplayMode  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _mode_  
| ) | |   
      
    
    Method called when the display mode changes.
    
    Called when the display mode changes, this method can be used to set
    data that wasn't available when .attach() was called.
    
    When HiRes is set as display mode, display the component as a copy of
    the mesh associated as the HiRes property of the host object. See
    ArchComponent.Component's properties.
    
    If no shape is set in the HiRes property, just display the object as
    the Flat Lines display mode.
    
    Parameters
    ----------
    vobj: <Gui.ViewProviderDocumentObject>
        The component's view provider object.
    mode: str
        The name of the display mode the view provider has switched to.
    
    Returns
    -------
    str:
        The name of the display mode the view provider has switched to.
    

References
[ArchComponent.ViewProviderComponent.hiresgroup](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#adb5745944ae9b415394ada099f13d717),
[ArchComponent.ViewProviderComponent.meshnode](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#acb568729ce3429c521c62c72135e221a),
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
[ArchWall.areSameWallTypes()](../../d2/d8e/namespaceArchWall.html#a289f6e980eba7dd10b74dcfb84dd0c92),
and
[ArchSpace.removeSpaceBoundaries()](../../d8/d6a/namespaceArchSpace.html#aca020b8800ac48fabbf4fce2a0f16cee).

## ◆ setEdit()

def ArchComponent.ViewProviderComponent.setEdit  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _vobj_ ,   
|  |  | _mode_  
| ) | |   
      
    
    Method called when the document requests the object to enter edit mode.
    
    Edit mode is entered when a user double clicks on an object in the tree
    view, or when they use the menu option [Edit -> Toggle Edit Mode].
    
    Parameters
    ----------
    vobj: <Gui.ViewProviderDocumentObject>
        The component's view provider object.
    mode: int or str
        The edit mode the document has requested. Set to 0 when requested via
        a double click or [Edit -> Toggle Edit Mode].
    
    Returns
    -------
    bool
        If edit mode was entered.
    

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
[ArchGrid.ViewProviderArchGrid.doubleClicked()](../../d4/dbf/classArchGrid_1_1ViewProviderArchGrid.html#a35948c50ff2dccdada47d584d8bf32bd),
[ArchReference.ViewProviderArchReference.doubleClicked()](../../d2/dfd/classArchReference_1_1ViewProviderArchReference.html#a921a71a757c5853c3331216eefb23703),
[draftviewproviders.view_dimension.ViewProviderDimensionBase.doubleClicked()](../../d6/d45/classdraftviewproviders_1_1view__dimension_1_1ViewProviderDimensionBase.html#a164ae40613358c396be3f6b9fae3937d),
[draftviewproviders.view_hatch.ViewProviderDraftHatch.doubleClicked()](../../dd/d75/classdraftviewproviders_1_1view__hatch_1_1ViewProviderDraftHatch.html#a9274ff72268d6c1a4337118b5db8bcc4),
[draftviewproviders.view_text.ViewProviderText.doubleClicked()](../../db/dd9/classdraftviewproviders_1_1view__text_1_1ViewProviderText.html#adc22c64d135df407787ca53f9029c3a0),
[PathScripts.PathPropertyBagGui.ViewProvider.doubleClicked()](../../d5/d77/classPathScripts_1_1PathPropertyBagGui_1_1ViewProvider.html#a915f858e0483981f8124bdf4df7e02d4),
[PathScripts.PathSetupSheetGui.ViewProvider.doubleClicked()](../../dc/dc3/classPathScripts_1_1PathSetupSheetGui_1_1ViewProvider.html#a9b1b82571f01e8e740eadabfec88b9f3),
[PathScripts.PathToolBitGui.ViewProvider.doubleClicked()](../../d0/d90/classPathScripts_1_1PathToolBitGui_1_1ViewProvider.html#a7265835d9e6286fa1e48f47a0f2b82f0),
[Spreadsheet_legacy.ViewProviderSpreadsheet.doubleClicked()](../../d6/d84/classSpreadsheet__legacy_1_1ViewProviderSpreadsheet.html#aa89fcb2be2b67b2f1d210bd06ea9e55a),
[ArchSchedule.CommandArchSchedule.IsActive()](../../d3/d2d/classArchSchedule_1_1CommandArchSchedule.html#aea4e379076ac7837ef44222df95fd97a),
[PathScripts.PathIconViewProvider.ViewProvider.setupContextMenu()](../../d6/d55/classPathScripts_1_1PathIconViewProvider_1_1ViewProvider.html#a9a8ca3029fe2523b0d7736c1d4e611a7),
[PathScripts.PathJobGui.ViewProvider.setupContextMenu()](../../d3/d3e/classPathScripts_1_1PathJobGui_1_1ViewProvider.html#ab8dd16390af82dadddf816c3a85cae0b),
[PathScripts.PathOpGui.ViewProvider.setupContextMenu()](../../db/df9/classPathScripts_1_1PathOpGui_1_1ViewProvider.html#a79f8f54d1d96c0a29b00b0775e5231ac),
and
[PathScripts.PathToolControllerGui.ViewProvider.setupContextMenu()](../../db/db5/classPathScripts_1_1PathToolControllerGui_1_1ViewProvider.html#a2f21a1b07712507aedc89ac30d8379c5).

## ◆ setProperties()

def ArchComponent.ViewProviderComponent.setProperties  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _vobj_  
| ) | |   
      
    
    Give the component view provider its component view provider specific properties.
    
    You can learn more about properties here:
    https://wiki.freecadweb.org/property
    

References
[draftutils.translate.QT_TRANSLATE_NOOP](../../de/d75/group__draftutils.html#ga9e6796e4394a4a163501246d7390f3c4).

Referenced by
[ArchPanel.CommandPanelSheet.Activated()](../../d1/d94/classArchPanel_1_1CommandPanelSheet.html#abed1cd5ce53c5b156683ae24b81f75e4),
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[ArchSite.Compass.buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[ArchSchedule.CommandArchSchedule.IsActive()](../../d3/d2d/classArchSchedule_1_1CommandArchSchedule.html#aea4e379076ac7837ef44222df95fd97a),
[ArchBuildingPart.BuildingPart.onDocumentRestored()](../../d2/def/classArchBuildingPart_1_1BuildingPart.html#a8029b4336a228315b03abd4cbe009001),
[ArchCurtainWall.CurtainWall.onDocumentRestored()](../../d3/ddd/classArchCurtainWall_1_1CurtainWall.html#a95c6772213f7a083a0dd81eef6163150),
[ArchGrid.ArchGrid.onDocumentRestored()](../../d7/d52/classArchGrid_1_1ArchGrid.html#af3945be9606a8a88bdfdeb840068ca5d),
[ArchPanel.PanelView.onDocumentRestored()](../../dd/da0/classArchPanel_1_1PanelView.html#a6e956704109979457399259409b3c12e),
[ArchPanel.PanelCut.onDocumentRestored()](../../d6/dbd/classArchPanel_1_1PanelCut.html#a81bcbc2154418c01c75c606932184aee),
[ArchPanel.PanelSheet.onDocumentRestored()](../../dc/d22/classArchPanel_1_1PanelSheet.html#afb1ed907e00ab4c552d73f932a3beb6e),
[ArchTruss.Truss.onDocumentRestored()](../../d9/d6f/classArchTruss_1_1Truss.html#abf7290b67c66f8b38f2f24c3a913eb7d),
[draftobjects.hatch.Hatch.onDocumentRestored()](../../db/d7f/classdraftobjects_1_1hatch_1_1Hatch.html#a5f4a52b199d98d8ef1bf681170a39214),
[draftobjects.shape2dview.Shape2DView.onDocumentRestored()](../../dc/d42/classdraftobjects_1_1shape2dview_1_1Shape2DView.html#aeb419e3492426690e6df5043bdd8fbf3),
[ArchBuildingPart.ViewProviderBuildingPart.onDocumentRestored()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a77d1c4103e062b3ee3d06a348b25310f),
[ArchPanel.ViewProviderPanelCut.onDocumentRestored()](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a97810dc3b020c64a4352d53c96ee8500),
and
[ArchPanel.ViewProviderPanelSheet.onDocumentRestored()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a4b5aa2a21de0a9ebd24cb59e54e54994).

## ◆ setupContextMenu()

def ArchComponent.ViewProviderComponent.setupContextMenu  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _vobj_ ,   
|  |  | _menu_  
| ) | |   
      
    
    Add the component specific options to the context menu.
    
    The context menu is the drop down menu that opens when the user right
    clicks on the component in the tree view.
    
    Add a menu choice to call the Arch_ToggleSubs Gui command. See
    ArchCommands._ToggleSubs
    
    Parameters
    ----------
    vobj: <Gui.ViewProviderDocumentObject>
        The component's view provider object.
    menu: <PySide2.QtWidgets.QMenu>
        The context menu already assembled prior to this method being
        called.
    

References
[ArchComponent.ViewProviderComponent.toggleSubcomponents()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#afdd01b4893303b90769e0870a675b7b9).

## ◆ toggleSubcomponents()

def ArchComponent.ViewProviderComponent.toggleSubcomponents  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    Simple wrapper to call Arch_ToggleSubs when the relevant context
    menu choice is selected.

Referenced by
[ArchComponent.ViewProviderComponent.setupContextMenu()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a9cb06662d675ab2a3f956c0b7672a64c).

## ◆ unsetEdit()

def ArchComponent.ViewProviderComponent.unsetEdit  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _vobj_ ,   
|  |  | _mode_  
| ) | |   
      
    
    Method called when the document requests the object exit edit mode.
    
    Returns
    -------
    False
    

Referenced by
[PathScripts.PathJobGui.ViewProvider.uneditObject()](../../d3/d3e/classPathScripts_1_1PathJobGui_1_1ViewProvider.html#aa663c276d96715669b3d07c7d2e34790).

## ◆ updateData()

def ArchComponent.ViewProviderComponent.updateData  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_ ,   
|  |  | _prop_  
| ) | |   
      
    
    Method called when the host object has a property changed.
    
    If the object has a Material associated with it, match the view
    object's ShapeColor and Transparency to match the Material.
    
    If the object is now cloned, or is part of a compound, have the view
    object inherit the DiffuseColor.
    
    Parameters
    ----------
    obj: <App::FeaturePython>
        The host object that has changed.
    prop: string
        The name of the property that has changed.
    

Reimplemented in
[ArchCurtainWall.ViewProviderCurtainWall](../../d7/d61/classArchCurtainWall_1_1ViewProviderCurtainWall.html#a1c40a49ffebf36d0c5153dade5d6c8e0).

Referenced by
[ArchPanel.CommandPanelSheet.Activated()](../../d1/d94/classArchPanel_1_1CommandPanelSheet.html#abed1cd5ce53c5b156683ae24b81f75e4),
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[ArchWall.areSameWallTypes()](../../d2/d8e/namespaceArchWall.html#a289f6e980eba7dd10b74dcfb84dd0c92),
[PathScripts.PathJobDlg.JobCreate.exec_()](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#a3949bbe83170d8e065b74724bcde9e2a),
[ArchRebar.makeRebar()](../../dd/de9/namespaceArchRebar.html#a4f9bf27bce35bf45fc8f02cfd5a8078d),
[draftviewproviders.view_dimension.ViewProviderLinearDimension.onChanged()](../../dc/d15/classdraftviewproviders_1_1view__dimension_1_1ViewProviderLinearDimension.html#a811de5a9bc446762fba4a970fa19139e),
[draftviewproviders.view_dimension.ViewProviderAngularDimension.onChanged()](../../d5/d88/classdraftviewproviders_1_1view__dimension_1_1ViewProviderAngularDimension.html#a087daa2336d84802959135e0da541289),
[draftviewproviders.view_wire.ViewProviderWire.onChanged()](../../da/dd2/classdraftviewproviders_1_1view__wire_1_1ViewProviderWire.html#a45511b113b62eba083c491b40c7fe3e8),
[PathScripts.PathOpGui.TaskPanelPage.pageUpdateData()](../../d1/d18/classPathScripts_1_1PathOpGui_1_1TaskPanelPage.html#ac7aeda3cf19b74fa6d6a620db8140a66),
[PathScripts.PathPropertyBagGui.TaskPanel.setupUi()](../../d3/d93/classPathScripts_1_1PathPropertyBagGui_1_1TaskPanel.html#a0e7d9c2f42ae50ec45505059011deba5),
and
[PathScripts.PathSetupSheetGui.OpTaskPanel.setupUi()](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#a03e427ec6574bd249d859f5bd2496576).

## Member Data Documentation

## ◆ hiresgroup

ArchComponent.ViewProviderComponent.hiresgroup  
---  
  
Referenced by
[ArchComponent.ViewProviderComponent.setDisplayMode()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#aa0542b1ecb134c494a26706a5f41d099).

## ◆ meshcolor

ArchComponent.ViewProviderComponent.meshcolor  
---  
  
## ◆ meshnode

ArchComponent.ViewProviderComponent.meshnode  
---  
  
Referenced by
[ArchComponent.ViewProviderComponent.setDisplayMode()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#aa0542b1ecb134c494a26706a5f41d099).

## ◆ Object

ArchComponent.ViewProviderComponent.Object  
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

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Arch/ArchComponent.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

