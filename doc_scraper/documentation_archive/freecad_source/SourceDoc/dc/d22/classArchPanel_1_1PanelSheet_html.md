---
url: https://freecad.github.io/SourceDoc/dc/d22/classArchPanel_1_1PanelSheet.html
scraped_at: 2025-09-08T14:58:08.310283
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ArchPanel](../../df/d76/namespaceArchPanel.html)
  * [PanelSheet](../../dc/d22/classArchPanel_1_1PanelSheet.html)

[List of all members](../../de/d29/classArchPanel_1_1PanelSheet-members.html) | Public Member Functions | Public Attributes

ArchPanel.PanelSheet Class Reference

##  Public Member Functions  
  
---  
def | [execute](../../dc/d22/classArchPanel_1_1PanelSheet.html#a9d4f849f31d9c3c7ac1ff1972d5bf0e6) (self, obj)  
def | [getHoles](../../dc/d22/classArchPanel_1_1PanelSheet.html#a96780dd784e032149f96c945ade6c8ca) (self, obj, transform=False)  
def | [getOutlines](../../dc/d22/classArchPanel_1_1PanelSheet.html#ac0ec5e21e9a5fd86d4e11760a1b5a46b) (self, obj, transform=False)  
def | [getTags](../../dc/d22/classArchPanel_1_1PanelSheet.html#a9c9843d366714ae5384918ebe629882d) (self, obj, transform=False)  
def | [onDocumentRestored](../../dc/d22/classArchPanel_1_1PanelSheet.html#afb1ed907e00ab4c552d73f932a3beb6e) (self, obj)  
def | [setProperties](../../dc/d22/classArchPanel_1_1PanelSheet.html#a6f1bddeabda97604ae78d870456ce30c) (self, obj)  
  
##  Public Attributes  
  
---  
|
[sheetborder](../../dc/d22/classArchPanel_1_1PanelSheet.html#a4f6517d4d82795d5eabe39fbced1c80a)  
|
[sheettag](../../dc/d22/classArchPanel_1_1PanelSheet.html#a9dfbe90d626d5bc759172d0afcc5b7f9)  
|
[Type](../../dc/d22/classArchPanel_1_1PanelSheet.html#a029f7be79c7aecc3314076236b5105d7)  
  
## Member Function Documentation

## ◆ execute()

def ArchPanel.PanelSheet.execute  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_  
| ) | |   
  
Referenced by
[draftobjects.facebinder.Facebinder.addSubobjects()](../../d9/d57/classdraftobjects_1_1facebinder_1_1Facebinder.html#a50c77c202a034ce7109bb93322ff6e4e),
[PathScripts.PathDressupDogbone.ObjectDressup.boneStateList()](../../d5/dfa/classPathScripts_1_1PathDressupDogbone_1_1ObjectDressup.html#af7788dd97e3ca711047ebc4472cf9f21),
[ArchSite.Compass.buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[PathScripts.PathDressupHoldingTags.ObjectTagDressup.generateTags()](../../de/dd2/classPathScripts_1_1PathDressupHoldingTags_1_1ObjectTagDressup.html#a0937c170df6457d4d7aa799c876584ae),
[ArchPanel.PanelCut.getWires()](../../d6/dbd/classArchPanel_1_1PanelCut.html#a61534af5c2a0125dde05e08a22025195),
[ArchSchedule.CommandArchSchedule.IsActive()](../../d3/d2d/classArchSchedule_1_1CommandArchSchedule.html#aea4e379076ac7837ef44222df95fd97a),
[Mod.PartDesign.Scripts.DistanceBolt.DistanceBolt.onChanged()](../../d8/d9d/classMod_1_1PartDesign_1_1Scripts_1_1DistanceBolt_1_1DistanceBolt.html#a5899c4fe94fa654ae168588d09ec3674),
[Mod.PartDesign.Scripts.Epitrochoid.Epitrochoid.onChanged()](../../da/d92/classMod_1_1PartDesign_1_1Scripts_1_1Epitrochoid_1_1Epitrochoid.html#a666d03d55a3758fd5b580ecdf83ff046),
[Mod.PartDesign.Scripts.Parallelepiped.Parallelepiped.onChanged()](../../da/db1/classMod_1_1PartDesign_1_1Scripts_1_1Parallelepiped_1_1Parallelepiped.html#a7d58a665dbdb613ccf9830254b6b3a28),
[Mod.PartDesign.Scripts.Parallelepiped.BoxCylinder.onChanged()](../../dc/dc9/classMod_1_1PartDesign_1_1Scripts_1_1Parallelepiped_1_1BoxCylinder.html#a32f2314f8a81f2034ba5fb8902079e75),
[Mod.PartDesign.Scripts.Spring.MySpring.onChanged()](../../d3/d4c/classMod_1_1PartDesign_1_1Scripts_1_1Spring_1_1MySpring.html#a45b49877108608c2473da154cbf7980d),
[FeaturePython.DistanceBolt.onChanged()](../../d9/d7d/classFeaturePython_1_1DistanceBolt.html#a644c14797e2ed9043537de3c86f7fdf1),
[PathScripts.PathStock.StockFromBase.onChanged()](../../d1/d74/classPathScripts_1_1PathStock_1_1StockFromBase.html#a2c3dfa73d2881d73e95ac79cb572e9b9),
[PathScripts.PathStock.StockCreateBox.onChanged()](../../d9/dd6/classPathScripts_1_1PathStock_1_1StockCreateBox.html#ae190342a16a7a1c726c7748b85bc36d7),
[PathScripts.PathStock.StockCreateCylinder.onChanged()](../../da/de2/classPathScripts_1_1PathStock_1_1StockCreateCylinder.html#aaee43a8f62bd342d2b16ff4268dd33c9),
[draftobjects.draftlink.DraftLink.onDocumentRestored()](../../d6/d1d/classdraftobjects_1_1draftlink_1_1DraftLink.html#ac93069a613e26475296ba7eba274a783),
[draftobjects.patharray.PathArray.onDocumentRestored()](../../de/dbe/classdraftobjects_1_1patharray_1_1PathArray.html#a6a3f3b5a3444a8e2bc12d61152100fd5),
and
[draftobjects.pathtwistedarray.PathTwistedArray.onDocumentRestored()](../../da/d1a/classdraftobjects_1_1pathtwistedarray_1_1PathTwistedArray.html#a780c1e365112f239b177875caa78103b).

## ◆ getHoles()

def ArchPanel.PanelSheet.getHoles  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_ ,   
|  |  | _transform_ = `False`  
| ) | |   
      
    
    getHoles(obj,transform=False): returns a list of compound whose wires define the
    holes contained in the panels in this sheet. If transform is True, the placement of
    the sheet will be added to each wire

## ◆ getOutlines()

def ArchPanel.PanelSheet.getOutlines  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_ ,   
|  |  | _transform_ = `False`  
| ) | |   
      
    
    getOutlines(obj,transform=False): returns a list of compounds whose wires define the
    outlines of the panels in this sheet. If transform is True, the placement of
    the sheet will be added to each wire

## ◆ getTags()

def ArchPanel.PanelSheet.getTags  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_ ,   
|  |  | _transform_ = `False`  
| ) | |   
      
    
    getTags(obj,transform=False): returns a list of compounds whose wires define the
    tags (engravings) contained in the panels in this sheet and the sheet intself.
    If transform is True, the placement of the sheet will be added to each wire.
    Warning, the wires returned by this function may not be closed,
    depending on the font

References
[ArchPanel.PanelSheet.sheettag](../../dc/d22/classArchPanel_1_1PanelSheet.html#a9dfbe90d626d5bc759172d0afcc5b7f9).

Referenced by
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.addNewTag()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#ad5c4ec1bd21c22bd83a9ef4c2cf7b2a8),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.deleteSelectedTag()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#ac2b73344d112083703e070277b7f7643),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.editTag()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#a66963fb0f8fbff5f5b1f0de6d92aa468),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.getFields()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#aa8cc9a19c1ad1adb9e40aef3d1237458),
and
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.whenTagsViewChanged()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#a0dc5e07f2f70e3714e5016f8ce84511b).

## ◆ onDocumentRestored()

def ArchPanel.PanelSheet.onDocumentRestored  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_  
| ) | |   
  
References ArchAxis._Axis.setProperties(),
ArchAxisSystem._AxisSystem.setProperties(),
ArchBuilding._Building.setProperties(),
[ArchBuildingPart.BuildingPart.setProperties()](../../d2/def/classArchBuildingPart_1_1BuildingPart.html#a01e29cb1d764fda7df9055fe009dbf35),
[ArchComponent.Component.setProperties()](../../de/d87/classArchComponent_1_1Component.html#a83f183119924946069f3b00947ec9793),
[ArchCurtainWall.CurtainWall.setProperties()](../../d3/ddd/classArchCurtainWall_1_1CurtainWall.html#a1c7351250cd02e8b790e5ed84ebe7553),
ArchEquipment._Equipment.setProperties(), ArchFence._Fence.setProperties(),
ArchFloor._Floor.setProperties(), ArchFrame._Frame.setProperties(),
[ArchGrid.ArchGrid.setProperties()](../../d7/d52/classArchGrid_1_1ArchGrid.html#a229519e55602df9a0561e406eccbcd43),
[ArchIFC.IfcRoot.setProperties()](../../d4/da7/classArchIFC_1_1IfcRoot.html#a085b21fd2e99fa8a5ac287d97fbe7fa2),
ArchMaterial._ArchMaterial.setProperties(), ArchPanel._Panel.setProperties(),
[ArchPanel.PanelView.setProperties()](../../dd/da0/classArchPanel_1_1PanelView.html#a4d88fc678e1545b9d6758274b79ff6de),
[ArchPanel.PanelCut.setProperties()](../../d6/dbd/classArchPanel_1_1PanelCut.html#ab647ec1cd91fa4c50475f46c709f2283),
[ArchPanel.PanelSheet.setProperties()](../../dc/d22/classArchPanel_1_1PanelSheet.html#a6f1bddeabda97604ae78d870456ce30c),
ArchPipe._ArchPipe.setProperties(),
ArchPipe._ArchPipeConnector.setProperties(),
ArchPrecast._Precast.setProperties(),
ArchPrecast._PrecastBeam.setProperties(),
ArchPrecast._PrecastIbeam.setProperties(),
ArchPrecast._PrecastPillar.setProperties(),
ArchPrecast._PrecastPanel.setProperties(),
ArchPrecast._PrecastSlab.setProperties(),
ArchPrecast._PrecastStairs.setProperties(),
ArchProject._Project.setProperties(), ArchRebar._Rebar.setProperties(),
[ArchReference.ArchReference.setProperties()](../../d3/d06/classArchReference_1_1ArchReference.html#a41a26333eb23a48bdb3271bed98296e5),
ArchRoof._Roof.setProperties(), ArchSchedule._ArchSchedule.setProperties(),
ArchSectionPlane._SectionPlane.setProperties(),
ArchSectionPlane._ArchDrawingView.setProperties(),
ArchSite._Site.setProperties(), ArchSpace._Space.setProperties(),
ArchStairs._Stairs.setProperties(), ArchStructure._Structure.setProperties(),
[ArchTruss.Truss.setProperties()](../../d9/d6f/classArchTruss_1_1Truss.html#a90f32bb2105867d75078e021f1ba771c),
ArchWall._Wall.setProperties(), ArchWindow._Window.setProperties(),
[draftobjects.hatch.Hatch.setProperties()](../../db/d7f/classdraftobjects_1_1hatch_1_1Hatch.html#a48c378dffc98e6b9f7ecac53074128da),
[draftobjects.shape2dview.Shape2DView.setProperties()](../../dc/d42/classdraftobjects_1_1shape2dview_1_1Shape2DView.html#aa3d3c084e10c9697c432ccf1ddee8928),
ArchAxis._ViewProviderAxis.setProperties(),
[ArchBuildingPart.ViewProviderBuildingPart.setProperties()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a16972577fb2b2bebf116c298b7f0f9da),
[ArchComponent.ViewProviderComponent.setProperties()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#abbd3e374ae515673bada8f848fbc98af),
ArchFence._ViewProviderFence.setProperties(),
[ArchPanel.ViewProviderPanelCut.setProperties()](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a728ad185d4b895a95966a464948c1027),
[ArchPanel.ViewProviderPanelSheet.setProperties()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a36bba4eebef09728a582d6a4b3b71150),
ArchRebar._ViewProviderRebar.setProperties(),
[ArchReference.ViewProviderArchReference.setProperties()](../../d2/dfd/classArchReference_1_1ViewProviderArchReference.html#a7f9d1dadc048dd8e345d54d9b06629c9),
ArchSectionPlane._ViewProviderSectionPlane.setProperties(),
ArchSite._ViewProviderSite.setProperties(),
ArchSpace._ViewProviderSpace.setProperties(), and
ArchStructure._ViewProviderStructure.setProperties().

## ◆ setProperties()

def ArchPanel.PanelSheet.setProperties  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_  
| ) | |   
  
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

## Member Data Documentation

## ◆ sheetborder

ArchPanel.PanelSheet.sheetborder  
---  
  
## ◆ sheettag

ArchPanel.PanelSheet.sheettag  
---  
  
Referenced by
[ArchPanel.PanelSheet.getTags()](../../dc/d22/classArchPanel_1_1PanelSheet.html#a9c9843d366714ae5384918ebe629882d).

## ◆ Type

ArchPanel.PanelSheet.Type  
---  
  
Referenced by
[ArchPanel.CommandPanelSheet.Activated()](../../d1/d94/classArchPanel_1_1CommandPanelSheet.html#abed1cd5ce53c5b156683ae24b81f75e4),
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftobjects.draft_annotation.DraftAnnotation.add_missing_properties_0v19()](../../d4/dca/classdraftobjects_1_1draft__annotation_1_1DraftAnnotation.html#a345b51b0cfae010e7e5574f0a84dd2f3),
[ArchStructure.StructSelectionObserver.addSelection()](../../db/d76/classArchStructure_1_1StructSelectionObserver.html#ac984e4631db3078ffee1dc0fee52df74),
[ArchSite.Compass.buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[ArchComponent.Component.execute()](../../de/d87/classArchComponent_1_1Component.html#a2ab328b6ab53b7bc9017eef25870cdf0),
[draftobjects.layer.LayerContainer.execute()](../../de/d4d/classdraftobjects_1_1layer_1_1LayerContainer.html#a960d8cd7f03fe7426f8cac669671b513),
[ArchSchedule.CommandArchSchedule.IsActive()](../../d3/d2d/classArchSchedule_1_1CommandArchSchedule.html#aea4e379076ac7837ef44222df95fd97a),
[draftobjects.layer.Layer.set_properties()](../../d0/ddc/classdraftobjects_1_1layer_1_1Layer.html#aa6a95fe93a36b884d61ef2c668de002e),
and
[ArchReference.ArchReference.setProperties()](../../d3/d06/classArchReference_1_1ArchReference.html#a41a26333eb23a48bdb3271bed98296e5).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Arch/ArchPanel.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

