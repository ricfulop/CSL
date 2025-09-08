---
url: https://freecad.github.io/SourceDoc/d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html
scraped_at: 2025-09-08T14:58:12.343716
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ArchPanel](../../df/d76/namespaceArchPanel.html)
  * [ViewProviderPanelSheet](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html)

[List of all members](../../dd/db8/classArchPanel_1_1ViewProviderPanelSheet-members.html) | Public Member Functions | Public Attributes

ArchPanel.ViewProviderPanelSheet Class Reference

##  Public Member Functions  
  
---  
def | [attach](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#aaff17755bc54fc5a1963a96d48076aaf) (self, vobj)  
def | [getIcon](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#ae6de4f56583c621e68eb8c91affbfc02) (self)  
def | [onChanged](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a23b7c16b9daf13fbb1d9de061e3949a2) (self, vobj, prop)  
def | [onDocumentRestored](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a4b5aa2a21de0a9ebd24cb59e54e54994) (self, vobj)  
def | [setEdit](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#ae867e3595c276c8e66b8650c8d1a9344) (self, vobj, mode)  
def | [setProperties](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a36bba4eebef09728a582d6a4b3b71150) (self, vobj)  
def | [unsetEdit](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#aba0b478f7a14110ab8e07958b5718403) (self, vobj, mode)  
def | [updateData](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a916cdf8131f60494dabf61e971d1a093) (self, obj, prop)  
  
##  Public Attributes  
  
---  
|
[color](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#ac46be3e74ce0d8359488e1e75e609c1b)  
|
[coords](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#af88fc245ebd7ab92fc9a10ab6cb107bf)  
|
[lineset](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#ae88ef1f0e96d75b1c86a0a78e2f4fcf8)  
|
[switch](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a98ef246fd06fced33ed8bb5bef82700f)  
  
## Member Function Documentation

## ◆ attach()

def ArchPanel.ViewProviderPanelSheet.attach  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _vobj_  
| ) | |   
  
## ◆ getIcon()

def ArchPanel.ViewProviderPanelSheet.getIcon  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Referenced by
[ArchAxisSystem.AxisSystemTaskPanel.update()](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a376cbba2ccee6efd86c46d0f0a8e99e3),
[ArchComponent.ComponentTaskPanel.update()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#af95b36032a3837b4bf1b92fe7c6a47e0),
and
[ArchSectionPlane.SectionPlaneTaskPanel.update()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#aab4bcd7b08950b8e3b37d801381c5162).

## ◆ onChanged()

def ArchPanel.ViewProviderPanelSheet.onChanged  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _vobj_ ,   
|  |  | _prop_  
| ) | |   
  
References
[UNV2411::TRecord.color](../../d5/d1a/structUNV2411_1_1TRecord.html#ad28d017ae9371805fe3db5f2668aea11),
[UNV2412::TRecord.color](../../d0/d32/structUNV2412_1_1TRecord.html#ac939d2d4a45328543767025847528c26),
[Gui::SoRegPoint.color](../../d8/da6/classGui_1_1SoRegPoint.html#a0905179151ce2dc70da75fc4290cc50d),
[Gui::RDragger.color](../../d2/d5d/classGui_1_1RDragger.html#a6be44fe335f8ad3ec01e55e36be64542),
[Gui::SyntaxHighlighter.color()](../../d7/d17/classGui_1_1SyntaxHighlighter.html#a6e917532f6c6d3a402d3b625a0922f60),
[Gui::ColorButton.color](../../dc/d1c/classGui_1_1ColorButton.html#a41d31286e472b112f3f3713559b76031),
[ArchPanel.ViewProviderPanelCut.color](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a0cab9384f41ebb3d65d614b0fc3822ec),
[ArchPanel.ViewProviderPanelSheet.color](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#ac46be3e74ce0d8359488e1e75e609c1b),
ArchSite._ViewProviderSite.color, ArchSpace._ViewProviderSpace.color,
[DraftGui.DraftToolBar.color](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a6ef9459f80edd8f2184747902fb9dc43),
[draftguitools.gui_trackers.Tracker.color](../../d2/d99/classdraftguitools_1_1gui__trackers_1_1Tracker.html#a716abcadfc78fb0d37929527c939c9b4),
[draftguitools.gui_trackers.editTracker.color](../../d3/dce/classdraftguitools_1_1gui__trackers_1_1editTracker.html#a78de0b69185b2268e97eccd54ed03bc3),
[draftguitools.gui_trimex.Trimex.color](../../da/df7/classdraftguitools_1_1gui__trimex_1_1Trimex.html#ae0f8916da3350c2fa6cc050b9af891a2),
[draftviewproviders.view_dimension.ViewProviderLinearDimension.color](../../dc/d15/classdraftviewproviders_1_1view__dimension_1_1ViewProviderLinearDimension.html#a40c9732d877b5c6bae3859899441fc29),
[draftviewproviders.view_dimension.ViewProviderAngularDimension.color](../../d5/d88/classdraftviewproviders_1_1view__dimension_1_1ViewProviderAngularDimension.html#a5dea45c63ec6b3fd28fe45d7ab8bc4d7),
[importSVG.svgHandler.color](../../dc/d45/classimportSVG_1_1svgHandler.html#a56888666ef9ee10f0f459ecb8eacbe9f),
[ColorPickerItem.color()](../../d5/d00/classColorPickerItem.html#a774de0e3bae031514e42412215efbc33),
[ColorPickerPopup.color()](../../d2/da2/classColorPickerPopup.html#a921eda867036b1d3c65f1420b9205918),
[QtColorPicker.color()](../../dc/d28/classQtColorPicker.html#a5482070f028e1a4b4c5a4bbddbb7a2d7),
[PathScripts.PathDressupDogbone.Marker.color()](../../d9/dd1/classPathScripts_1_1PathDressupDogbone_1_1Marker.html#aa6559a825c993d35fc860af9866776e7),
[PathScripts.PathDressupTagGui.HoldingTagMarker.color](../../d1/df1/classPathScripts_1_1PathDressupTagGui_1_1HoldingTagMarker.html#a2266f8413e4668718623f3853c3a9d6f),
[TechDraw::CosmeticVertex.color](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#a43dc51729b750cd27636f984286a553f),
TechDrawGui::lineAttributes.color,
[FeaturePython.ViewProviderOctahedron.color](../../dc/d32/classFeaturePython_1_1ViewProviderOctahedron.html#aa15c2b97e68435c067784a4b5d418349),
[Mod.Test.unittestgui.ProgressBar.color](../../d6/dca/classMod_1_1Test_1_1unittestgui_1_1ProgressBar.html#aa731df03071422cb8d7253f05269153c),
Gui::SoFCColorGradient.coords, Gui::SoFCColorLegend.coords,
ArchEquipment._ViewProviderEquipment.coords,
[ArchPanel.ViewProviderPanelCut.coords](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a5be6bf887998ed4600f11232fd4b21e3),
[ArchPanel.ViewProviderPanelSheet.coords](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#af88fc245ebd7ab92fc9a10ab6cb107bf),
ArchSite._ViewProviderSite.coords, ArchSpace._ViewProviderSpace.coords,
ArchStructure._ViewProviderStructure.coords,
[draftguitools.gui_trackers.snapTracker.coords](../../d9/d7e/classdraftguitools_1_1gui__trackers_1_1snapTracker.html#acd6c2abe38d24b02a8acbeac9ab42ce8),
[draftguitools.gui_trackers.lineTracker.coords](../../da/db8/classdraftguitools_1_1gui__trackers_1_1lineTracker.html#a84149aa895c2decf5d542357db04634d),
[draftguitools.gui_trackers.rectangleTracker.coords](../../d7/d8d/classdraftguitools_1_1gui__trackers_1_1rectangleTracker.html#a9f28029d9fd3a484be59bcd618f4addc),
[draftguitools.gui_trackers.dimTracker.coords](../../d2/d2f/classdraftguitools_1_1gui__trackers_1_1dimTracker.html#ab0b64cc9f072ce50f3e95802a567f4b0),
[draftguitools.gui_trackers.ghostTracker.coords](../../d9/dc6/classdraftguitools_1_1gui__trackers_1_1ghostTracker.html#ab633c8ee9b9b06fd9d919e688ca592ab),
[draftguitools.gui_trackers.editTracker.coords](../../d3/dce/classdraftguitools_1_1gui__trackers_1_1editTracker.html#a2d97c26b55a2fe001250f9f48d3785f6),
[draftguitools.gui_trackers.wireTracker.coords](../../dc/dfc/classdraftguitools_1_1gui__trackers_1_1wireTracker.html#a1adc7471f2154760060cb43da8bf316d),
[draftviewproviders.view_dimension.ViewProviderLinearDimension.coords](../../dc/d15/classdraftviewproviders_1_1view__dimension_1_1ViewProviderLinearDimension.html#aabc67055b60334bf7826c71bf1138667),
[draftviewproviders.view_dimension.ViewProviderAngularDimension.coords](../../d5/d88/classdraftviewproviders_1_1view__dimension_1_1ViewProviderAngularDimension.html#ab42693ddd4ff8ec2120485ee16ecf851),
[draftviewproviders.view_wire.ViewProviderWire.coords](../../da/dd2/classdraftviewproviders_1_1view__wire_1_1ViewProviderWire.html#ad81dd0a4dc7fb6c066b93b000cd93ef0),
MeshPartGui::ViewProviderCrossSections.coords,
PartGui::ViewProviderCrossSections.coords,
[PartGui::ViewProviderPartExt.coords](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#ac770b2513129e2d0771db6ee71fdbacf),
ObjectObserver.coords,
[FeaturePython.ViewProviderCircleSet.coords](../../df/d71/classFeaturePython_1_1ViewProviderCircleSet.html#afa8a04b13421228c73a2df2b835dba57),
ArchAxis._ViewProviderAxis.lineset,
[ArchPanel.ViewProviderPanelCut.lineset](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#ace4cbf26906e9032bae9bb671174c477),
[ArchPanel.ViewProviderPanelSheet.lineset](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#ae88ef1f0e96d75b1c86a0a78e2f4fcf8),
ArchStructure._ViewProviderStructure.lineset,
[PartGui::ViewProviderPartExt.lineset](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a4a92bc1352416f86059b9a32c0328e37),
[ArchPanel.ViewProviderPanelCut.switch](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#af0af46dafeea92faddbab8c76fe5953d),
[ArchPanel.ViewProviderPanelSheet.switch](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a98ef246fd06fced33ed8bb5bef82700f),
[draftguitools.gui_trackers.Tracker.switch](../../d2/d99/classdraftguitools_1_1gui__trackers_1_1Tracker.html#a4869e436be9c89bec96e6ef6cbe114ed),
[PathScripts.PathDressupDogbone.ViewProviderDressup.switch](../../df/ddb/classPathScripts_1_1PathDressupDogbone_1_1ViewProviderDressup.html#ad3aae6644a0e8aed31ad5837957595b9),
[PathScripts.PathDressupTagGui.PathDressupTagViewProvider.switch](../../dc/d08/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagViewProvider.html#ac8859f47a525d7fa4366532fb613d076),
PathScripts.PathFeatureExtensionsGui._Extension.switch,
[PathScripts.PathFeatureExtensionsGui.TaskPanelExtensionPage.switch](../../d0/de3/classPathScripts_1_1PathFeatureExtensionsGui_1_1TaskPanelExtensionPage.html#aeed5343ed8c44b35e2e8f9ddf34d7ab6),
and
[PathScripts.PathJobGui.ViewProvider.switch](../../d3/d3e/classPathScripts_1_1PathJobGui_1_1ViewProvider.html#a00558435f401b527dfcf2a67438ceae5).

Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftviewproviders.view_base.ViewProviderDraft.attach()](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#af35acb7285aa095bf670e82338c9462d),
[ArchSite.Compass.buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[draftobjects.wire.Wire.execute()](../../d4/d14/classdraftobjects_1_1wire_1_1Wire.html#ad931a4e79d7d0516803bf1a8a33e7655),
[ArchBuildingPart.ViewProviderBuildingPart.updateData()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a12d40383666b8987a3277ea26454995d),
[ArchPanel.ViewProviderPanelCut.updateData()](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a970ed7e44ebec3c959dcb48bf60b2d31),
[ArchPanel.ViewProviderPanelSheet.updateData()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a916cdf8131f60494dabf61e971d1a093),
[draftviewproviders.view_label.ViewProviderLabel.updateData()](../../d1/d88/classdraftviewproviders_1_1view__label_1_1ViewProviderLabel.html#aab195af09dd4fbe60e1bb38d362385ba),
[draftviewproviders.view_layer.ViewProviderLayer.updateData()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#a9c641727fd15eaa141c8a58837e14248),
and
[draftviewproviders.view_wpproxy.ViewProviderWorkingPlaneProxy.updateData()](../../da/dbf/classdraftviewproviders_1_1view__wpproxy_1_1ViewProviderWorkingPlaneProxy.html#ad58eb6ce87860ff0389b3498143d11c7).

## ◆ onDocumentRestored()

def ArchPanel.ViewProviderPanelSheet.onDocumentRestored  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _vobj_  
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

## ◆ setEdit()

def ArchPanel.ViewProviderPanelSheet.setEdit  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _vobj_ ,   
|  |  | _mode_  
| ) | |   
  
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

def ArchPanel.ViewProviderPanelSheet.setProperties  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _vobj_  
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

## ◆ unsetEdit()

def ArchPanel.ViewProviderPanelSheet.unsetEdit  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _vobj_ ,   
|  |  | _mode_  
| ) | |   
  
Referenced by
[PathScripts.PathJobGui.ViewProvider.uneditObject()](../../d3/d3e/classPathScripts_1_1PathJobGui_1_1ViewProvider.html#aa663c276d96715669b3d07c7d2e34790).

## ◆ updateData()

def ArchPanel.ViewProviderPanelSheet.updateData  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_ ,   
|  |  | _prop_  
| ) | |   
  
References
[App::VRMLObject.onChanged()](../../df/df6/classApp_1_1VRMLObject.html#a80cc75727e9f349bafe5037842c6fbcf),
[FemGui::ViewProviderFemPostPlaneFunction.onChanged()](../../d8/ddd/classFemGui_1_1ViewProviderFemPostPlaneFunction.html#aff4da6a421671244ed9f106adbaee37a),
[Part::Circle.onChanged()](../../de/de4/classPart_1_1Circle.html#aac82db0865d1e2eb55342a84cf91872e),
[Part::Vertex.onChanged()](../../de/d96/classPart_1_1Vertex.html#a9421cb9911928eae246b23f3590bc3ee),
[Part::Line.onChanged()](../../d3/dfe/classPart_1_1Line.html#ab63d1eeff0a1ad1773c06cca1d731017),
[Part::Ellipse.onChanged()](../../d6/d22/classPart_1_1Ellipse.html#aebecb9c21eca867973512232a720cc63),
[PartDesignGui::ViewProviderDatumCoordinateSystem.onChanged()](../../d7/d4d/classPartDesignGui_1_1ViewProviderDatumCoordinateSystem.html#a48324f18ce89cf9a307a32d54e3cfcc3),
[Surface::GeomFillSurface.onChanged()](../../d7/d0d/classSurface_1_1GeomFillSurface.html#a3bfc3e08b782ee0cb3ccb98f8dd1600f),
[PartDesign::Chamfer.onChanged()](../../da/d6f/classPartDesign_1_1Chamfer.html#a778fc5826d5950fba6fb6e5a2d2208dd),
[Sketcher::SketchObject.onChanged()](../../d9/dad/classSketcher_1_1SketchObject.html#a838e11f3f3d9b47452ece92f8057bff1),
[TechDrawGui::ViewProviderBalloon.onChanged()](../../d2/dd9/classTechDrawGui_1_1ViewProviderBalloon.html#abbbfdc1b1e66ea1ea4ba8a483794161d),
[TechDrawGui::ViewProviderDimension.onChanged()](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#aa4c52719f57d011b0a4f3bef4c68a016),
[TechDrawGui::ViewProviderLeader.onChanged()](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#a74a77269f6962a4a975229ac51c582c7),
[TechDrawGui::ViewProviderRichAnno.onChanged()](../../d2/d72/classTechDrawGui_1_1ViewProviderRichAnno.html#a338b45f77e146a3a179b2f7922de8d8d),
[TechDrawGui::ViewProviderWeld.onChanged()](../../dc/dbe/classTechDrawGui_1_1ViewProviderWeld.html#acad7ad25b7e30c03fc13738bce5db1de),
[Gui::ViewProvider.onChanged()](../../d3/db3/classGui_1_1ViewProvider.html#a825924c3bb8e3aaed03215ef12867392),
[Gui::ViewProviderAnnotation.onChanged()](../../d3/d71/classGui_1_1ViewProviderAnnotation.html#a789aabe3e009284175581640dec663c3),
[Gui::ViewProviderAnnotationLabel.onChanged()](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#a53d7de6d67521a3dadb7ae43c96869bc),
[Gui::ViewProviderGeometryObject.onChanged()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#ac9e49ff9d0f734482071f412b15b934c),
[Gui::ViewProviderMeasureDistance.onChanged()](../../dd/d89/classGui_1_1ViewProviderMeasureDistance.html#a55ba8a09c4ee671752b6e88c3561d9e1),
[Gui::ViewProviderOrigin.onChanged()](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#acba30fffb482dd3f286e36fff1dfee5c),
[Gui::ViewProviderOriginFeature.onChanged()](../../d9/d6a/classGui_1_1ViewProviderOriginFeature.html#a86520630c898707677753ccc3877eced),
[Gui::ViewProviderPythonFeatureImp.onChanged()](../../de/dbe/classGui_1_1ViewProviderPythonFeatureImp.html#a3084d0bbb14eacb2dfe624cd7c58a283),
[Gui::ViewProviderTextDocument.onChanged()](../../dc/d65/classGui_1_1ViewProviderTextDocument.html#a8d87ca622183dd3077563ad3d45c479b),
[Drawing::FeatureClip.onChanged()](../../d5/d4a/classDrawing_1_1FeatureClip.html#a2f703cc6f8d0f4d9e953a80ec936b8f0),
[Drawing::FeaturePage.onChanged()](../../db/d0f/classDrawing_1_1FeaturePage.html#a9c6b6897f29ff589163044d51b7e5c04),
[Drawing::FeatureViewSymbol.onChanged()](../../da/d14/classDrawing_1_1FeatureViewSymbol.html#aaf6475415e3e3e4e35ad6d1cd034f7fc),
[Fem::Constraint.onChanged()](../../d0/d11/classFem_1_1Constraint.html#aec25bc397a1a87056079e3cd5a59d778),
[Fem::ConstraintBearing.onChanged()](../../df/d0a/classFem_1_1ConstraintBearing.html#ae81d9fda05994bd43bf81faf3acae5d6),
[Fem::ConstraintContact.onChanged()](../../db/d7c/classFem_1_1ConstraintContact.html#a2470d9364e84ea3c15f5873073f26539),
[Fem::ConstraintDisplacement.onChanged()](../../d5/d1c/classFem_1_1ConstraintDisplacement.html#a8525892f2c7183b75c1d8f2052f82401),
[Fem::ConstraintFixed.onChanged()](../../d1/d43/classFem_1_1ConstraintFixed.html#a2b9b87e9151f1571ab9cff619ec5547c),
[Fem::ConstraintFluidBoundary.onChanged()](../../d6/dbc/classFem_1_1ConstraintFluidBoundary.html#acee1bd2b1d9f5b712253eaf827c00110),
[Fem::ConstraintForce.onChanged()](../../d6/d63/classFem_1_1ConstraintForce.html#aa19098735f62c480439948314f6532b3),
[Fem::ConstraintGear.onChanged()](../../d8/d55/classFem_1_1ConstraintGear.html#a971506b4ca246c3378e2755160ed4772),
[Fem::ConstraintHeatflux.onChanged()](../../de/dce/classFem_1_1ConstraintHeatflux.html#a0caeab069cf3e2fc8246aa163735d1e9),
[Fem::ConstraintInitialTemperature.onChanged()](../../da/d91/classFem_1_1ConstraintInitialTemperature.html#aa21e4c9c6cc31312e5147bbe1f8fcf05),
[Fem::ConstraintPlaneRotation.onChanged()](../../d7/d08/classFem_1_1ConstraintPlaneRotation.html#a668aafd16c5cf0565dde1072dd55a34a),
[Fem::ConstraintPressure.onChanged()](../../dd/d5e/classFem_1_1ConstraintPressure.html#a05ca046143c094c241c12702f7b820f7),
[Fem::ConstraintPulley.onChanged()](../../d3/dec/classFem_1_1ConstraintPulley.html#a6c23af9b8ba29b03f25163da9b75a41f),
[Fem::ConstraintSpring.onChanged()](../../dc/d42/classFem_1_1ConstraintSpring.html#ae67112c14de2dc75f749842b6591fcf8),
[Fem::ConstraintTemperature.onChanged()](../../d7/dff/classFem_1_1ConstraintTemperature.html#a74f2f9e94a2d9011490c09caab3c0da9),
[Fem::ConstraintTransform.onChanged()](../../d8/d3c/classFem_1_1ConstraintTransform.html#a38b893dee34272ad6bf0c6126aad561f),
[Fem::FemMeshObject.onChanged()](../../d5/d68/classFem_1_1FemMeshObject.html#aeea4f2e58af23fcd160a31ccea76cc6e),
[Fem::FemPostClipFilter.onChanged()](../../dc/d06/classFem_1_1FemPostClipFilter.html#a696285744236a6bf6e8c14f735034705),
[Fem::FemPostDataAlongLineFilter.onChanged()](../../da/d26/classFem_1_1FemPostDataAlongLineFilter.html#ae418afcb8e18abba84d16c2a645a434e),
[Fem::FemPostDataAtPointFilter.onChanged()](../../d1/d7a/classFem_1_1FemPostDataAtPointFilter.html#ae4bb2f96ee214db7c2bcb5a0afe0fdc4),
[Fem::FemPostScalarClipFilter.onChanged()](../../d9/da9/classFem_1_1FemPostScalarClipFilter.html#a6c5243b230b4dac2cde71f28d04dcd53),
[Fem::FemPostWarpVectorFilter.onChanged()](../../db/d33/classFem_1_1FemPostWarpVectorFilter.html#a64c913cbc86feb708504b94b931f1085),
[Fem::FemPostCutFilter.onChanged()](../../da/d89/classFem_1_1FemPostCutFilter.html#a682758b8e3c1c8cf8b272d2244321913),
[Fem::FemPostFunctionProvider.onChanged()](../../dd/d47/classFem_1_1FemPostFunctionProvider.html#a5d57b8e7aadfb627843050d88d933911),
[Fem::FemPostPlaneFunction.onChanged()](../../dd/d76/classFem_1_1FemPostPlaneFunction.html#ab73b39b74f480820feda8b3f5bcad117),
[Fem::FemPostSphereFunction.onChanged()](../../d5/dcb/classFem_1_1FemPostSphereFunction.html#abffccabdacd9cbbe6e61e799c8385c59),
[Fem::FemPostPipeline.onChanged()](../../d5/d4b/classFem_1_1FemPostPipeline.html#a333b47057bc9b7691cc0c9db9b0c79ba),
[FemGui::ViewProviderFemConstraint.onChanged()](../../d7/dc7/classFemGui_1_1ViewProviderFemConstraint.html#a3d33c13c95f3a907325ad1c399dc5a14),
[FemGui::ViewProviderFemMesh.onChanged()](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#ab319d4e3659d8c99309bd397af321308),
[FemGui::ViewProviderFemPostFunctionProvider.onChanged()](../../df/d22/classFemGui_1_1ViewProviderFemPostFunctionProvider.html#a13a3a3015d78a539b51f342fa516670c),
[FemGui::ViewProviderFemPostFunction.onChanged()](../../d5/d14/classFemGui_1_1ViewProviderFemPostFunction.html#ae95be84201f7f51ce6162468c514e33e),
[FemGui::ViewProviderFemPostObject.onChanged()](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#a5d27aeff234b60ec0214c939556b26c5),
[InspectionGui::ViewProviderInspection.onChanged()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a75537f17b213bb2c7ea45b374ed65375),
[Mesh::Feature.onChanged()](../../dd/dce/classMesh_1_1Feature.html#a136a80fff5bcb707ecb5c4d308e42c56),
[MeshGui::ViewProviderMesh.onChanged()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ae9ec71d871b59be4a532fb2be2cb8d52),
[MeshGui::ViewProviderMeshCurvature.onChanged()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#acd7c344f3f6180e42b53db82ddc998a6),
[MeshGui::ViewProviderMeshDefects.onChanged()](../../da/d50/classMeshGui_1_1ViewProviderMeshDefects.html#a0d494009344982737533a865b26ce7d4),
[MeshGui::ViewProviderMeshNode.onChanged()](../../dc/d89/classMeshGui_1_1ViewProviderMeshNode.html#a6f37857950fa14e1e1978c56706d0797),
[Part::Mirroring.onChanged()](../../dc/dac/classPart_1_1Mirroring.html#aa4148eb536fa6f15fb2fc21f3fe839b4),
[Part::Box.onChanged()](../../dc/d80/classPart_1_1Box.html#a29bcbc46ec0749e4035fffc5117e1723),
[Part::RuledSurface.onChanged()](../../d1/d41/classPart_1_1RuledSurface.html#a143afeec2aafb3207cd29e9ef6fc5934),
[Part::Loft.onChanged()](../../d3/d52/classPart_1_1Loft.html#acc65fe857c50b113cb06e0d092c83fd5),
[Part::Sweep.onChanged()](../../df/dc6/classPart_1_1Sweep.html#a67f346ffecb66556a70c38c9184cdd56),
[Part::Helix.onChanged()](../../df/d49/classPart_1_1Helix.html#a8f7d2c5809cd60f90231a0350ea5c444),
[Part::Spiral.onChanged()](../../d2/d3f/classPart_1_1Spiral.html#a2f38f985d7c148ee3acec62a8358b4b7),
[Part::Wedge.onChanged()](../../d5/dc5/classPart_1_1Wedge.html#a609125d1bc02031accfc330fc2e79d08),
[PartGui::ViewProvider2DObjectGrid.onChanged()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a04a16b5ac49a2b5df31304da0a4318ee),
[PartGui::ViewProviderCustom.onChanged()](../../d5/d45/classPartGui_1_1ViewProviderCustom.html#a326f53617a41a940cb743b45853c0780),
[PartGui::ViewProviderPartReference.onChanged()](../../d8/df3/classPartGui_1_1ViewProviderPartReference.html#a8af0748ed20158c08efa16db288d3f81),
[PartDesign::Line.onChanged()](../../d0/d2a/classPartDesign_1_1Line.html#a9da12fed7c1a5cfa4af5c06af23c6fff),
[PartDesign::Plane.onChanged()](../../df/df0/classPartDesign_1_1Plane.html#a82dfdf47875b49263a5275ab1ff3c686),
[PartDesign::FeatureBase.onChanged()](../../d2/d7c/classPartDesign_1_1FeatureBase.html#a628a37fc8716ca08f0c67bb727ac3b76),
[PartDesign::DressUp.onChanged()](../../df/de5/classPartDesign_1_1DressUp.html#a7f7a173d69576711009fb17aeb08f6bc),
[PartDesign::Helix.onChanged()](../../d3/d78/classPartDesign_1_1Helix.html#a8f7d2c5809cd60f90231a0350ea5c444),
[PartDesign::Hole.onChanged()](../../dd/dd0/classPartDesign_1_1Hole.html#a2d2bbe8a83eafdedc73ae1cfa9360758),
[PartDesign::ProfileBased.onChanged()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a36fd19fd597799ebeccd8eddd104bdf4),
[PartDesignGui::ViewProviderDatumPoint.onChanged()](../../dc/d9d/classPartDesignGui_1_1ViewProviderDatumPoint.html#ada6d519997cb6ca57d88957962fc1377),
[Path::Feature.onChanged()](../../d5/dd9/classPath_1_1Feature.html#a136a80fff5bcb707ecb5c4d308e42c56),
[PathGui::ViewProviderPath.onChanged()](../../db/d31/classPathGui_1_1ViewProviderPath.html#ac6bc90e9c178290fc1ecf742e31ac167),
[Points::Feature.onChanged()](../../d8/de3/classPoints_1_1Feature.html#a136a80fff5bcb707ecb5c4d308e42c56),
[PointsGui::ViewProviderPoints.onChanged()](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#ad91786e290cd4be69ef99a41c85faa32),
[Robot::Edge2TracObject.onChanged()](../../d8/df5/classRobot_1_1Edge2TracObject.html#a3e8b60d7dcc4abe17a0e640a0e0ef5e9),
[Robot::RobotObject.onChanged()](../../db/d51/classRobot_1_1RobotObject.html#abebfe59d5888146a96594cb7d31ffce8),
[Robot::TrajectoryDressUpObject.onChanged()](../../d6/d95/classRobot_1_1TrajectoryDressUpObject.html#a58ad4466b7239a951a9b9b4d30b7f1d3),
[Robot::TrajectoryObject.onChanged()](../../d7/db5/classRobot_1_1TrajectoryObject.html#aded21cc1ebf027aa6b39e81759687ea3),
[RobotGui::ViewProviderRobotObject.onChanged()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a41cfa5ba4f24dacf46491cc903e5a715),
[Sandbox::SandboxObject.onChanged()](../../da/dd9/classSandbox_1_1SandboxObject.html#ae3e3d04a08a28cb8060a72df914f3685),
[SketcherGui::ViewProviderCustom.onChanged()](../../d9/d6b/classSketcherGui_1_1ViewProviderCustom.html#a326f53617a41a940cb743b45853c0780),
[Spreadsheet::Sheet.onChanged()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a50d56147d2f6d3cf3329413baef6e66d),
[TechDraw::DrawParametricTemplate.onChanged()](../../d5/d13/classTechDraw_1_1DrawParametricTemplate.html#a98d6a8c0896aca4d3fa549700b8a4eb6),
[TechDraw::DrawRichAnno.onChanged()](../../da/d5f/classTechDraw_1_1DrawRichAnno.html#aca7c4594d99963f20955aaaea06f9fbc),
[TechDraw::DrawSVGTemplate.onChanged()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#afa43ef4d1bf529675b75c5d31fff582b),
[TechDraw::DrawTemplate.onChanged()](../../d8/d95/classTechDraw_1_1DrawTemplate.html#a6d7ffefeb992220357cf4dab59576919),
[TechDraw::DrawTile.onChanged()](../../da/d56/classTechDraw_1_1DrawTile.html#a0a7ecfbee9fbaf70d3d69acfd16c62e7),
[TechDraw::DrawTileWeld.onChanged()](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a4241390f45c70002f410b5c78a4d0452),
[TechDraw::DrawViewAnnotation.onChanged()](../../d5/d65/classTechDraw_1_1DrawViewAnnotation.html#a6566da76a48d680dc1cc90db63e0c60a),
[TechDraw::DrawViewClip.onChanged()](../../dd/de8/classTechDraw_1_1DrawViewClip.html#afb0fdb6bcca35df389d3cd1632191706),
[TechDraw::DrawViewCollection.onChanged()](../../df/d2f/classTechDraw_1_1DrawViewCollection.html#a5897d64ff7b47d70c7f4bddce6ac17ce),
[TechDraw::DrawViewDimExtent.onChanged()](../../d9/d77/classTechDraw_1_1DrawViewDimExtent.html#a33e7b8c64f2983f2b81608bd1ebfc494),
[TechDraw::DrawViewSpreadsheet.onChanged()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#ab3c3a1352fddadb8dea1ef9ec40acd91),
[TechDraw::DrawWeldSymbol.onChanged()](../../dd/d15/classTechDraw_1_1DrawWeldSymbol.html#ad0b71b97ee45320fc8e8634e98b935cb),
[TechDrawGui::ViewProviderImage.onChanged()](../../d3/d5b/classTechDrawGui_1_1ViewProviderImage.html#ad13417ef59c1aeb04fbc4fbcc6aa57d2),
[TechDrawGui::ViewProviderProjGroup.onChanged()](../../d6/dc7/classTechDrawGui_1_1ViewProviderProjGroup.html#a23482323e8ec6da0cb3dd93b00203e73),
[TechDrawGui::ViewProviderViewPart.onChanged()](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#a86b7b59890bb041b58c8e5564383e631),
[TechDrawGui::ViewProviderViewSection.onChanged()](../../d2/df0/classTechDrawGui_1_1ViewProviderViewSection.html#a0387c427509686ba2dff332930fb5efe),
[Gui::ViewProviderDocumentObject.onChanged()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ac7163501426771c94bb2026224ec94d8),
[Gui::ViewProviderLink.onChanged()](../../d6/d59/classGui_1_1ViewProviderLink.html#a07a0d46d41cc066a8b7da7cab6d0e1a1),
[Gui::ViewProviderPart.onChanged()](../../d9/d6c/classGui_1_1ViewProviderPart.html#a5e76f3437483472cd66247d0eb98aa1a),
[Gui::ViewProviderPlacement.onChanged()](../../da/d5e/classGui_1_1ViewProviderPlacement.html#a471b5fcc496e5d153b398a0675e2c93e),
[Gui::ViewProviderPythonFeatureT< ViewProviderT
>.onChanged()](../../dc/d41/classGui_1_1ViewProviderPythonFeatureT.html#a64d55596d48786e66dd8a1086ae6ba8b),
[Part::BodyBase.onChanged()](../../da/dc8/classPart_1_1BodyBase.html#aad727053c5bb43ee6f065f3d0b458f16),
[Part::Revolution.onChanged()](../../d3/d17/classPart_1_1Revolution.html#a9940a58886c8d7d0b4b009082d81f14c),
[Part::Feature.onChanged()](../../d7/d7e/classPart_1_1Feature.html#a17178c5bf097534e84b20380ad13563b),
[Part::Primitive.onChanged()](../../d2/d31/classPart_1_1Primitive.html#ac5544f9b57ebf2a1b626450200a4bec0),
[PartGui::ViewProviderPartExt.onChanged()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a52ae16d5a0dbe879343e3dad26d9e30b),
[PartDesign::Body.onChanged()](../../dd/db8/classPartDesign_1_1Body.html#aef216a77e951705ba9b124bfb88ae533),
[PartDesign::Point.onChanged()](../../da/d0d/classPartDesign_1_1Point.html#a559cef769b27bcf8efeef552583f9aa4),
[PartDesign::Boolean.onChanged()](../../d2/d81/classPartDesign_1_1Boolean.html#a41c675a8b7f2f6e73b95946b99245f12),
[PartDesign::FeaturePrimitive.onChanged()](../../da/d0d/classPartDesign_1_1FeaturePrimitive.html#a86c00f82005801a22585584fb378e4e5),
[PartDesign::ShapeBinder.onChanged()](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#a984513ae894c80494f6a0c3b0725f48f),
[PartDesign::SubShapeBinder.onChanged()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a525834748579d35e2e8ecbf9cd18bf3d),
[PartDesignGui::ViewProvider.onChanged()](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#a257ca77e2256cbd8df847cedc5892289),
[PartDesignGui::ViewProviderBody.onChanged()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#adf615077f77d932ed33b637b2e87e922),
[PartDesignGui::ViewProviderBoolean.onChanged()](../../d7/d09/classPartDesignGui_1_1ViewProviderBoolean.html#ab446d9f6494af864bd745136c7e20439),
[PartDesignGui::ViewProviderSubShapeBinder.onChanged()](../../d1/da6/classPartDesignGui_1_1ViewProviderSubShapeBinder.html#acfc66960894369715fed17de459c679d),
[SketcherGui::ViewProviderSketch.onChanged()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#ae317a35c18a1f9b333a14655c35eb8dc),
[Surface::Extend.onChanged()](../../d1/d22/classSurface_1_1Extend.html#ac33fb0ebd31edae770d009cc24c58df9),
[TechDraw::DrawGeomHatch.onChanged()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a9942ef5dd5ecef6dba83a1245a0840ca),
[TechDraw::DrawHatch.onChanged()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a655588bfe5d6ff663e4aefc40c118a58),
[TechDraw::DrawLeaderLine.onChanged()](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#a289014293fbb3c42b8c46416e261530a),
[TechDraw::DrawPage.onChanged()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a883373ce2f6c8d3335c3074c1f7866ed),
[TechDraw::DrawProjGroup.onChanged()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#afe9cc0a3218a4c8037a9a6b67642d450),
[TechDraw::DrawProjGroupItem.onChanged()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#aea5cc872256320be7112396d84b3fee5),
[TechDraw::DrawView.onChanged()](../../d6/d1c/classTechDraw_1_1DrawView.html#a2980fbae4ce0a12aae609193764465cf),
[TechDraw::DrawViewBalloon.onChanged()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#aed3817b8e495aca5729e5bed436cca6c),
[TechDraw::DrawViewDetail.onChanged()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad6ccb9e626c3e77b1228188eb2fab34c),
[TechDraw::DrawViewDimension.onChanged()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f650d374435ed4a7ee16ed101674296),
[TechDraw::DrawViewImage.onChanged()](../../d0/d87/classTechDraw_1_1DrawViewImage.html#a42774ac4ebd8f4fc4819cf4833e779aa),
[TechDraw::DrawViewMulti.onChanged()](../../d1/d80/classTechDraw_1_1DrawViewMulti.html#aa73d9e1a0934d049da29a63f2c5ddddd),
[TechDraw::DrawViewPart.onChanged()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a6a340bbf67a96de757e412b21d7a5491),
[TechDraw::DrawViewSection.onChanged()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a9ddcd143279f82644cdcc124c6a71419),
[TechDraw::DrawViewSymbol.onChanged()](../../d3/d02/classTechDraw_1_1DrawViewSymbol.html#adb3364984aac5da2ff804a43845ceee4),
[TechDraw::LandmarkDimension.onChanged()](../../d8/d4f/classTechDraw_1_1LandmarkDimension.html#a9c8e7f17abdc4acecdc7e6670328f7a6),
[TechDrawGui::ViewProviderDrawingView.onChanged()](../../db/d6f/classTechDrawGui_1_1ViewProviderDrawingView.html#af947ca7438432b3448358f4ebcf6bbc1),
[TechDrawGui::ViewProviderGeomHatch.onChanged()](../../db/dbe/classTechDrawGui_1_1ViewProviderGeomHatch.html#a1a42e7ea4d5eb17c7e1f536cad241cc3),
[TechDrawGui::ViewProviderHatch.onChanged()](../../de/d1a/classTechDrawGui_1_1ViewProviderHatch.html#aada265457fade9ade61cbade5aee4f2b),
[TechDrawGui::ViewProviderPage.onChanged()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#a498b66c6f2b5af184c95c4a07bc6f98e),
[TechDrawGui::ViewProviderTemplate.onChanged()](../../dc/d9b/classTechDrawGui_1_1ViewProviderTemplate.html#a7b5d5197907bbf4cc9c65c1004a1da83),
[App::PropertyContainer.onChanged()](../../d5/d48/classApp_1_1PropertyContainer.html#ab9705aa8b662b534f1a3a6c7b77f1a34),
[App::ExtensionContainer.onChanged()](../../d6/d76/classApp_1_1ExtensionContainer.html#ad571ff1df010fb7f617689f0e4ff360d),
[App::FeatureCustomT< FeatureT
>.onChanged()](../../d7/d3f/classApp_1_1FeatureCustomT.html#a1dd739f646e30108053da973728b4545),
[App::FeaturePythonImp.onChanged()](../../de/d49/classApp_1_1FeaturePythonImp.html#a31e2aa2e633c8db8d05057f71dc42a17),
[App::MeasureDistance.onChanged()](../../d7/d61/classApp_1_1MeasureDistance.html#abbccf44662823af983d2786da162cc43),
[App::TextDocument.onChanged()](../../d9/de9/classApp_1_1TextDocument.html#affdf6c8a48df5cea53213040c487e5f8),
[App::Document.onChanged()](../../d8/d3e/classApp_1_1Document.html#ab0259fb189ab0c44b820d72b2d9fe17a),
[App::DocumentObject.onChanged()](../../d2/de4/classApp_1_1DocumentObject.html#aa9fcfd8db6b2ffdf46274b18b45811cf),
[App::FeaturePythonT< FeatureT
>.onChanged()](../../d2/d2f/classApp_1_1FeaturePythonT.html#aefbf8694218d25f4b90d8ffe7fe796ee),
[draftobjects.bezcurve.BezCurve.onChanged()](../../dd/de3/classdraftobjects_1_1bezcurve_1_1BezCurve.html#aeba2787e2957549355c437defa1580d3),
[draftobjects.bspline.BSpline.onChanged()](../../d5/dee/classdraftobjects_1_1bspline_1_1BSpline.html#a8255cb2abe8eee3861e45c826f8dd124),
[OpenSCADFeatures.Resize.onChanged()](../../d0/d16/classOpenSCADFeatures_1_1Resize.html#a74342799b04e05685c9b9e7f0dc3237a),
[OpenSCADFeatures.MatrixTransform.onChanged()](../../d0/d13/classOpenSCADFeatures_1_1MatrixTransform.html#aa08a1c34a236e7178e37dbc0cdf3a9db),
[OpenSCADFeatures.ImportObject.onChanged()](../../d4/db2/classOpenSCADFeatures_1_1ImportObject.html#adb0c7c95dd6233cca67091782d5b09c9),
[OpenSCADFeatures.RefineShape.onChanged()](../../d4/ded/classOpenSCADFeatures_1_1RefineShape.html#a1822b311e09a7d66c696b42cb664be88),
[OpenSCADFeatures.IncreaseTolerance.onChanged()](../../d7/d14/classOpenSCADFeatures_1_1IncreaseTolerance.html#a67cdfc41a889e463abfc43930021378b),
[OpenSCADFeatures.GetWire.onChanged()](../../da/dd5/classOpenSCADFeatures_1_1GetWire.html#a30db2a18571331bb247d7ad5d79a82c8),
[OpenSCADFeatures.Frustum.onChanged()](../../d5/d20/classOpenSCADFeatures_1_1Frustum.html#a9b8d083a9077c14821e3ef57d7a6d1d9),
[OpenSCADFeatures.Twist.onChanged()](../../d0/d1e/classOpenSCADFeatures_1_1Twist.html#a6f2c167bd82f4d6d45659bd913fa1280),
[OpenSCADFeatures.PrismaticToroid.onChanged()](../../d9/d5e/classOpenSCADFeatures_1_1PrismaticToroid.html#a266694864f4a21a233ca2c92db824960),
[OpenSCADFeatures.OffsetShape.onChanged()](../../d7/dc8/classOpenSCADFeatures_1_1OffsetShape.html#ad6441bf902e24e312b696e0a6ec8a594),
[Mod.PartDesign.FeatureHole.FeatureHole.Hole.onChanged()](../../de/dba/classMod_1_1PartDesign_1_1FeatureHole_1_1FeatureHole_1_1Hole.html#ab9080f897b9cbfe7eea9ab0fb12f6d69),
[Mod.PartDesign.Scripts.DistanceBolt.DistanceBolt.onChanged()](../../d8/d9d/classMod_1_1PartDesign_1_1Scripts_1_1DistanceBolt_1_1DistanceBolt.html#a5899c4fe94fa654ae168588d09ec3674),
[Mod.PartDesign.Scripts.Epitrochoid.Epitrochoid.onChanged()](../../da/d92/classMod_1_1PartDesign_1_1Scripts_1_1Epitrochoid_1_1Epitrochoid.html#a666d03d55a3758fd5b580ecdf83ff046),
[Mod.PartDesign.Scripts.Parallelepiped.Parallelepiped.onChanged()](../../da/db1/classMod_1_1PartDesign_1_1Scripts_1_1Parallelepiped_1_1Parallelepiped.html#a7d58a665dbdb613ccf9830254b6b3a28),
[Mod.PartDesign.Scripts.Parallelepiped.BoxCylinder.onChanged()](../../dc/dc9/classMod_1_1PartDesign_1_1Scripts_1_1Parallelepiped_1_1BoxCylinder.html#a32f2314f8a81f2034ba5fb8902079e75),
[Mod.PartDesign.Scripts.Spring.MySpring.onChanged()](../../d3/d4c/classMod_1_1PartDesign_1_1Scripts_1_1Spring_1_1MySpring.html#a45b49877108608c2473da154cbf7980d),
[PathScripts.PathDressupZCorrect.ObjectDressup.onChanged()](../../d2/de1/classPathScripts_1_1PathDressupZCorrect_1_1ObjectDressup.html#a22412dd4c157681fcf2710caeb4e1e35),
[FeaturePython.Box.onChanged()](../../de/d80/classFeaturePython_1_1Box.html#a8d01210266fbc404533bc702a231bd9d),
[FeaturePython.PointFeature.onChanged()](../../d5/dbf/classFeaturePython_1_1PointFeature.html#af26f94d430cacbce6997ea83b2e1a6f8),
[FeaturePython.MeshFeature.onChanged()](../../da/d2f/classFeaturePython_1_1MeshFeature.html#a0da703e72283a19176461491ed158e54),
[FeaturePython.DistanceBolt.onChanged()](../../d9/d7d/classFeaturePython_1_1DistanceBolt.html#a644c14797e2ed9043537de3c86f7fdf1),
[Texture.Texture.onChanged()](../../d7/d39/classTexture_1_1Texture.html#a6a2d1589fd96d0e717fb4928543a9ce0),
ArchAxis._Axis.onChanged(), ArchAxisSystem._AxisSystem.onChanged(),
[ArchBuildingPart.BuildingPart.onChanged()](../../d2/def/classArchBuildingPart_1_1BuildingPart.html#af29a6f8f0bd35ef5779a12f9bfc3c26e),
[ArchComponent.Component.onChanged()](../../de/d87/classArchComponent_1_1Component.html#ac10328dd9515bdac2dd7e11861c4609e),
[ArchCurtainWall.CurtainWall.onChanged()](../../d3/ddd/classArchCurtainWall_1_1CurtainWall.html#acbae8cc86609f0e9ef6cfe9a7078901f),
ArchEquipment._Equipment.onChanged(), ArchFloor._Floor.onChanged(),
[ArchIFC.IfcRoot.onChanged()](../../d4/da7/classArchIFC_1_1IfcRoot.html#abde72ec687dc6401837824722d16d9ea),
ArchMaterial._ArchMaterial.onChanged(),
[ArchPanel.PanelView.onChanged()](../../dd/da0/classArchPanel_1_1PanelView.html#a27851fa2cc842781c0f11dd6c4c8c76e),
ArchRebar._Rebar.onChanged(),
[ArchReference.ArchReference.onChanged()](../../d3/d06/classArchReference_1_1ArchReference.html#adda72d69a29b48f2145aec91a530556f),
ArchSchedule._ArchSchedule.onChanged(),
ArchSectionPlane._SectionPlane.onChanged(), ArchSite._Site.onChanged(),
ArchSpace._Space.onChanged(), ArchStructure._Structure.onChanged(),
[ArchTruss.Truss.onChanged()](../../d9/d6f/classArchTruss_1_1Truss.html#ad5bacb59d6610e87c0aad5a4dc7f8987),
ArchWall._Wall.onChanged(), ArchWindow._Window.onChanged(),
[draftobjects.array.Array.onChanged()](../../d7/d7e/classdraftobjects_1_1array_1_1Array.html#a0e270c9f742df2a9745701e990d473fd),
[draftobjects.base.DraftObject.onChanged()](../../d1/d64/classdraftobjects_1_1base_1_1DraftObject.html#a0240a9d9d6164a6bbb7d61fc9dad089c),
[draftobjects.dimension.LinearDimension.onChanged()](../../dd/d6f/classdraftobjects_1_1dimension_1_1LinearDimension.html#a73a053cdb053995498b61c141c25fd2e),
[draftobjects.dimension.AngularDimension.onChanged()](../../d9/df3/classdraftobjects_1_1dimension_1_1AngularDimension.html#ae74ad664eeaa745188f98c9c4b427685),
[draftobjects.draft_annotation.DraftAnnotation.onChanged()](../../d4/dca/classdraftobjects_1_1draft__annotation_1_1DraftAnnotation.html#aba399378981bb8862d151c295ab42834),
[draftobjects.draftlink.DraftLink.onChanged()](../../d6/d1d/classdraftobjects_1_1draftlink_1_1DraftLink.html#abf631b6e29c488b5f5efba5d54c682d4),
[draftobjects.fillet.Fillet.onChanged()](../../dc/de0/classdraftobjects_1_1fillet_1_1Fillet.html#ad376b23c5d8bfcabe96f45963f3c9042),
[draftobjects.label.Label.onChanged()](../../d8/db6/classdraftobjects_1_1label_1_1Label.html#adf0439fe4b2d0bbe7eb60ce14f1e5a9d),
[draftobjects.patharray.PathArray.onChanged()](../../de/dbe/classdraftobjects_1_1patharray_1_1PathArray.html#a43dc8ba99121be6523d40cc4c4a582e2),
[draftobjects.pathtwistedarray.PathTwistedArray.onChanged()](../../da/d1a/classdraftobjects_1_1pathtwistedarray_1_1PathTwistedArray.html#aec963f49d8449cf7d45c1cc033008a78),
[draftobjects.wire.Wire.onChanged()](../../d4/d14/classdraftobjects_1_1wire_1_1Wire.html#a2832beac9526a31b90bc4da2dec506ce),
[draftobjects.wpproxy.WorkingPlaneProxy.onChanged()](../../d1/d19/classdraftobjects_1_1wpproxy_1_1WorkingPlaneProxy.html#a1792829e9ead47991aaf04cbe82e35ae),
[PathScripts.PathArray.ObjectArray.onChanged()](../../d1/dbb/classPathScripts_1_1PathArray_1_1ObjectArray.html#aaaaffe03bab46bdd481c1b94eb935403),
[PathScripts.PathComment.Comment.onChanged()](../../de/d58/classPathScripts_1_1PathComment_1_1Comment.html#a467c2b9b68d19724c816bc4a6553824f),
[PathScripts.PathDressupAxisMap.ObjectDressup.onChanged()](../../d3/d2b/classPathScripts_1_1PathDressupAxisMap_1_1ObjectDressup.html#a207af4143464f45758c7713b57a02790),
[PathScripts.PathDressupRampEntry.ObjectDressup.onChanged()](../../d4/d77/classPathScripts_1_1PathDressupRampEntry_1_1ObjectDressup.html#ad54af2fdb3f158558c48f5fc203cf871),
[PathScripts.PathJob.ObjectJob.onChanged()](../../df/d08/classPathScripts_1_1PathJob_1_1ObjectJob.html#a9e841a1353500cf44f9b1513731108de),
[PathScripts.PathOp.ObjectOp.onChanged()](../../d0/dec/classPathScripts_1_1PathOp_1_1ObjectOp.html#adbe35988fdbd8ac71572c26df7128c40),
[PathScripts.PathSlot.ObjectSlot.onChanged()](../../d6/dca/classPathScripts_1_1PathSlot_1_1ObjectSlot.html#a098281739b56491660fdc2cb18aa46be),
[PathScripts.PathStock.StockFromBase.onChanged()](../../d1/d74/classPathScripts_1_1PathStock_1_1StockFromBase.html#a2c3dfa73d2881d73e95ac79cb572e9b9),
[PathScripts.PathStock.StockCreateBox.onChanged()](../../d9/dd6/classPathScripts_1_1PathStock_1_1StockCreateBox.html#ae190342a16a7a1c726c7748b85bc36d7),
[PathScripts.PathStock.StockCreateCylinder.onChanged()](../../da/de2/classPathScripts_1_1PathStock_1_1StockCreateCylinder.html#aaee43a8f62bd342d2b16ff4268dd33c9),
[PathScripts.PathStop.Stop.onChanged()](../../de/d01/classPathScripts_1_1PathStop_1_1Stop.html#ab9c8a325fb08df3d7ecf81bac65c819e),
[PathScripts.PathSurface.ObjectSurface.onChanged()](../../dd/d92/classPathScripts_1_1PathSurface_1_1ObjectSurface.html#a3dacd3615f547bd8de9e3b893b71ea17),
[PathScripts.PathToolBit.ToolBit.onChanged()](../../d3/d85/classPathScripts_1_1PathToolBit_1_1ToolBit.html#ab54ce26cb3074d72bf750c121efdf895),
[PathScripts.PathWaterline.ObjectWaterline.onChanged()](../../db/dcc/classPathScripts_1_1PathWaterline_1_1ObjectWaterline.html#ae81879b1fc3163ad6ee573245c0dab08),
[Spreadsheet_legacy.SpreadsheetController.onChanged()](../../d1/d38/classSpreadsheet__legacy_1_1SpreadsheetController.html#af6a869e9f6792f82c3bc64c67db566f5),
[Spreadsheet_legacy.SpreadsheetPropertyController.onChanged()](../../d5/d01/classSpreadsheet__legacy_1_1SpreadsheetPropertyController.html#ae07315f73931ed9751807df36f43fc91),
[Texture.ViewProviderTexture.onChanged()](../../d1/d29/classTexture_1_1ViewProviderTexture.html#ab3aa3ad8d0fdf5c18f82fb92bd2581c0),
[DocumentObject.DocumentObject.onChanged()](../../d7/dae/classDocumentObject_1_1DocumentObject.html#a3ddd3f88d14a83a2e41491680fb9b882),
ArchAxis._ViewProviderAxis.onChanged(),
ArchAxisSystem._ViewProviderAxisSystem.onChanged(),
[ArchBuildingPart.ViewProviderBuildingPart.onChanged()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#ab521b855d25a75f28c70a1cc42889546),
[ArchComponent.ViewProviderComponent.onChanged()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a14303b12cf40f4c4393c5d86c08820bf),
[ArchCurtainWall.ViewProviderCurtainWall.onChanged()](../../d7/d61/classArchCurtainWall_1_1ViewProviderCurtainWall.html#add541f453903121b6540cd9361af9bc7),
ArchFence._ViewProviderFence.onChanged(),
ArchMaterial._ViewProviderArchMaterial.onChanged(),
[ArchPanel.ViewProviderPanelCut.onChanged()](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a095d6d5009cc3ac370c0f85785c16e4b),
[ArchPanel.ViewProviderPanelSheet.onChanged()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a23b7c16b9daf13fbb1d9de061e3949a2),
ArchRebar._ViewProviderRebar.onChanged(),
[ArchReference.ViewProviderArchReference.onChanged()](../../d2/dfd/classArchReference_1_1ViewProviderArchReference.html#adc47944d5c97e98c2cc354697a305538),
ArchSectionPlane._ViewProviderSectionPlane.onChanged(),
ArchSite._ViewProviderSite.onChanged(),
ArchSpace._ViewProviderSpace.onChanged(),
ArchStructure._ViewProviderStructure.onChanged(),
ArchWindow._ViewProviderWindow.onChanged(),
[draftviewproviders.view_base.ViewProviderDraft.onChanged()](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#a97a75182f0c1f89d1140bfd91b0f72e2),
[draftviewproviders.view_dimension.ViewProviderDimensionBase.onChanged()](../../d6/d45/classdraftviewproviders_1_1view__dimension_1_1ViewProviderDimensionBase.html#a3dd696bb72ae710c1e41c778364a754f),
[draftviewproviders.view_dimension.ViewProviderLinearDimension.onChanged()](../../dc/d15/classdraftviewproviders_1_1view__dimension_1_1ViewProviderLinearDimension.html#a811de5a9bc446762fba4a970fa19139e),
[draftviewproviders.view_dimension.ViewProviderAngularDimension.onChanged()](../../d5/d88/classdraftviewproviders_1_1view__dimension_1_1ViewProviderAngularDimension.html#a087daa2336d84802959135e0da541289),
[draftviewproviders.view_draft_annotation.ViewProviderDraftAnnotation.onChanged()](../../d2/d24/classdraftviewproviders_1_1view__draft__annotation_1_1ViewProviderDraftAnnotation.html#a85727241b9b93b467a5563c22b92a95e),
[draftviewproviders.view_label.ViewProviderLabel.onChanged()](../../d1/d88/classdraftviewproviders_1_1view__label_1_1ViewProviderLabel.html#a0c2d2d99716b94c14f16529079f8d06c),
[draftviewproviders.view_layer.ViewProviderLayer.onChanged()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#a3dbd47c9cbb1ed1f262be822a3c7a317),
[draftviewproviders.view_point.ViewProviderPoint.onChanged()](../../da/d93/classdraftviewproviders_1_1view__point_1_1ViewProviderPoint.html#aaa650c6fc36c006546c509cbf0603513),
[draftviewproviders.view_text.ViewProviderText.onChanged()](../../db/dd9/classdraftviewproviders_1_1view__text_1_1ViewProviderText.html#a798abb26aface6f3a7c06d0da2e6d15f),
[draftviewproviders.view_wire.ViewProviderWire.onChanged()](../../da/dd2/classdraftviewproviders_1_1view__wire_1_1ViewProviderWire.html#a45511b113b62eba083c491b40c7fe3e8),
[draftviewproviders.view_wpproxy.ViewProviderWorkingPlaneProxy.onChanged()](../../da/dbf/classdraftviewproviders_1_1view__wpproxy_1_1ViewProviderWorkingPlaneProxy.html#a9ca0b8694e8cb26ad7a712b4165240f6),
[femviewprovider.view_mesh_gmsh.VPMeshGmsh.onChanged()](../../df/dbc/classfemviewprovider_1_1view__mesh__gmsh_1_1VPMeshGmsh.html#a42887e52114ba070a5a3284e7eadc3a1),
PathScripts.PathComment._ViewProviderComment.onChanged(),
PathScripts.PathFixture._ViewProviderFixture.onChanged(),
PathScripts.PathPlane._ViewProviderPlane.onChanged(),
PathScripts.PathStop._ViewProviderStop.onChanged(),
[PathScripts.PathToolControllerGui.ViewProvider.onChanged()](../../db/db5/classPathScripts_1_1PathToolControllerGui_1_1ViewProvider.html#af521ed5966fb0c28d1a5d93d181f0e3a),
[OpenSCADFeatures.ViewProviderTree.onChanged()](../../df/dbf/classOpenSCADFeatures_1_1ViewProviderTree.html#a17837c823e4a2ff9a3d9d4fc1c2c460c),
[Mod.PartDesign.FeatureHole.ViewProviderHole.ViewProviderHole.onChanged()](../../de/d6b/classMod_1_1PartDesign_1_1FeatureHole_1_1ViewProviderHole_1_1ViewProviderHole.html#a179d1b3518fc399f85b49d7e7c09cf0c),
[FeaturePython.ViewProviderBox.onChanged()](../../d1/d1a/classFeaturePython_1_1ViewProviderBox.html#ac9ce1397db214fa0c5a73128f38e3149),
[FeaturePython.ViewProviderOctahedron.onChanged()](../../dc/d32/classFeaturePython_1_1ViewProviderOctahedron.html#a84c7717127fca122029d6e566c0a8538),
[FeaturePython.ViewProviderPoints.onChanged()](../../d5/dc2/classFeaturePython_1_1ViewProviderPoints.html#afab81f83ef30df441c0056cafbf4a9ac),
[DraftVecUtils.rotate()](../../dc/dc3/group__DRAFTVECUTILS.html#ga2e3351cd7a33a0d82d1da1d378e13db1),
[draftviewproviders.view_base.ViewProviderDraft.texcoords](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#a4431f0b97bd11405e6f70a2c9d17edd2),
and
[ifc4.ifcindexedtexturemap.texcoords](../../d9/d5d/classifc4_1_1ifcindexedtexturemap.html#a441ab58c9575be27584f7375e6a46db1).

Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[PathScripts.PathJobDlg.JobCreate.exec_()](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#a3949bbe83170d8e065b74724bcde9e2a),
[draftviewproviders.view_dimension.ViewProviderLinearDimension.onChanged()](../../dc/d15/classdraftviewproviders_1_1view__dimension_1_1ViewProviderLinearDimension.html#a811de5a9bc446762fba4a970fa19139e),
[draftviewproviders.view_dimension.ViewProviderAngularDimension.onChanged()](../../d5/d88/classdraftviewproviders_1_1view__dimension_1_1ViewProviderAngularDimension.html#a087daa2336d84802959135e0da541289),
[draftviewproviders.view_wire.ViewProviderWire.onChanged()](../../da/dd2/classdraftviewproviders_1_1view__wire_1_1ViewProviderWire.html#a45511b113b62eba083c491b40c7fe3e8),
[PathScripts.PathOpGui.TaskPanelPage.pageUpdateData()](../../d1/d18/classPathScripts_1_1PathOpGui_1_1TaskPanelPage.html#ac7aeda3cf19b74fa6d6a620db8140a66),
[PathScripts.PathPropertyBagGui.TaskPanel.setupUi()](../../d3/d93/classPathScripts_1_1PathPropertyBagGui_1_1TaskPanel.html#a0e7d9c2f42ae50ec45505059011deba5),
and
[PathScripts.PathSetupSheetGui.OpTaskPanel.setupUi()](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#a03e427ec6574bd249d859f5bd2496576).

## Member Data Documentation

## ◆ color

ArchPanel.ViewProviderPanelSheet.color  
---  
  
Referenced by
[ArchSite.Compass.buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[draftviewproviders.view_dimension.ViewProviderLinearDimension.draw_dim_arrows()](../../dc/d15/classdraftviewproviders_1_1view__dimension_1_1ViewProviderLinearDimension.html#a00c28fd7958623750a3ff11c07e5a200),
[draftviewproviders.view_dimension.ViewProviderAngularDimension.draw_dim_arrows()](../../d5/d88/classdraftviewproviders_1_1view__dimension_1_1ViewProviderAngularDimension.html#a9da4e18f559915f439560905218c9c3e),
[draftviewproviders.view_dimension.ViewProviderLinearDimension.draw_dim_overshoot()](../../dc/d15/classdraftviewproviders_1_1view__dimension_1_1ViewProviderLinearDimension.html#ac1a078fd77c430a4531902fc88944999),
[draftviewproviders.view_dimension.ViewProviderLinearDimension.draw_ext_overshoot()](../../dc/d15/classdraftviewproviders_1_1view__dimension_1_1ViewProviderLinearDimension.html#a64c02f9dac7c37e0063776af61e57300),
[draftguitools.gui_trimex.Trimex.finish()](../../da/df7/classdraftguitools_1_1gui__trimex_1_1Trimex.html#ad394c0738be99c19146ee3555d4d016d),
[importSVG.svgHandler.format()](../../dc/d45/classimportSVG_1_1svgHandler.html#ab2003c4e0f60dfaa63ac993c337d8120),
[DraftGui.DraftToolBar.getcol()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a698f6464005ac98a52c32f4ecba73240),
[DraftGui.DraftToolBar.getDefaultColor()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a82a983d4674e378821777284345d0ae9),
[PathScripts.PathDressupDogbone.Marker.highlight()](../../d9/dd1/classPathScripts_1_1PathDressupDogbone_1_1Marker.html#a82ec0dc11eef4149a8cd4937cf802886),
[PathScripts.PathDressupDogbone.Marker.lowlight()](../../d9/dd1/classPathScripts_1_1PathDressupDogbone_1_1Marker.html#adf6ff98093410464a7170c41e6495471),
[ArchPanel.ViewProviderPanelCut.onChanged()](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a095d6d5009cc3ac370c0f85785c16e4b),
[ArchPanel.ViewProviderPanelSheet.onChanged()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a23b7c16b9daf13fbb1d9de061e3949a2),
[draftviewproviders.view_dimension.ViewProviderLinearDimension.onChanged()](../../dc/d15/classdraftviewproviders_1_1view__dimension_1_1ViewProviderLinearDimension.html#a811de5a9bc446762fba4a970fa19139e),
[draftviewproviders.view_dimension.ViewProviderAngularDimension.onChanged()](../../d5/d88/classdraftviewproviders_1_1view__dimension_1_1ViewProviderAngularDimension.html#a087daa2336d84802959135e0da541289),
[FeaturePython.ViewProviderOctahedron.onChanged()](../../dc/d32/classFeaturePython_1_1ViewProviderOctahedron.html#a84c7717127fca122029d6e566c0a8538),
[Mod.Test.unittestgui.ProgressBar.paint()](../../d6/dca/classMod_1_1Test_1_1unittestgui_1_1ProgressBar.html#a631bc2906cc2b3f124b575fadda34efb),
[draftguitools.gui_trackers.editTracker.setColor()](../../d3/dce/classdraftguitools_1_1gui__trackers_1_1editTracker.html#ae7513d3ac071c59358abb830ee1d2802),
[PathScripts.PathDressupTagGui.HoldingTagMarker.setEnabled()](../../d1/df1/classPathScripts_1_1PathDressupTagGui_1_1HoldingTagMarker.html#a943a09c269cbaaf1837e72bc498abfff),
and
[DraftGui.DraftToolBar.setStyleButton()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a9e78aed9caa690cdbbb7b1306b479584).

## ◆ coords

ArchPanel.ViewProviderPanelSheet.coords  
---  
  
Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftguitools.gui_trackers.snapTracker.addCoords()](../../d9/d7e/classdraftguitools_1_1gui__trackers_1_1snapTracker.html#a7787270d3ed8d8094955650930601bc4),
[ArchSite.Compass.buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[draftguitools.gui_trackers.dimTracker.calc()](../../d2/d2f/classdraftguitools_1_1gui__trackers_1_1dimTracker.html#a55b0af8e2e595d3cdf7d7129b8f3b7c0),
[draftguitools.gui_trackers.snapTracker.clear()](../../d9/d7e/classdraftguitools_1_1gui__trackers_1_1snapTracker.html#a31835a905b876918501dbf62cc098c71),
[draftguitools.gui_trackers.editTracker.get()](../../d3/dce/classdraftguitools_1_1gui__trackers_1_1editTracker.html#a6ae705bd3c995cf5e1dc9e22392059bd),
[draftguitools.gui_trackers.lineTracker.getLength()](../../da/db8/classdraftguitools_1_1gui__trackers_1_1lineTracker.html#a6aa4dd8271753ebfb1f594484b80a41c),
[draftguitools.gui_trackers.rectangleTracker.getSize()](../../d7/d8d/classdraftguitools_1_1gui__trackers_1_1rectangleTracker.html#afc397a50b7aff2b85bd34fec4f3577f3),
[ArchPanel.ViewProviderPanelCut.onChanged()](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a095d6d5009cc3ac370c0f85785c16e4b),
[ArchPanel.ViewProviderPanelSheet.onChanged()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a23b7c16b9daf13fbb1d9de061e3949a2),
[draftviewproviders.view_wire.ViewProviderWire.onChanged()](../../da/dd2/classdraftviewproviders_1_1view__wire_1_1ViewProviderWire.html#a45511b113b62eba083c491b40c7fe3e8),
[draftguitools.gui_trackers.lineTracker.p1()](../../da/db8/classdraftguitools_1_1gui__trackers_1_1lineTracker.html#a0d46757a24c602477dd638f8a8fc95f6),
[draftguitools.gui_trackers.rectangleTracker.p1()](../../d7/d8d/classdraftguitools_1_1gui__trackers_1_1rectangleTracker.html#a21320b7fd29d9cf3b885d234c0bf9955),
[draftguitools.gui_trackers.rectangleTracker.p2()](../../d7/d8d/classdraftguitools_1_1gui__trackers_1_1rectangleTracker.html#af4166c16b90e631ab5283680e1828dbd),
[draftguitools.gui_trackers.lineTracker.p2()](../../da/db8/classdraftguitools_1_1gui__trackers_1_1lineTracker.html#a032c57e5421167d0d776249f77f573fa),
[draftguitools.gui_trackers.rectangleTracker.p3()](../../d7/d8d/classdraftguitools_1_1gui__trackers_1_1rectangleTracker.html#a1bf47cdde1ea165a58946f1a5fdc6c8e),
[draftguitools.gui_trackers.rectangleTracker.p4()](../../d7/d8d/classdraftguitools_1_1gui__trackers_1_1rectangleTracker.html#a5972b233131fc2906260135b27c45b15),
[draftguitools.gui_trackers.editTracker.set()](../../d3/dce/classdraftguitools_1_1gui__trackers_1_1editTracker.html#a8e45024e164c51236c07525d2f718b98),
[draftguitools.gui_trackers.snapTracker.setCoords()](../../d9/d7e/classdraftguitools_1_1gui__trackers_1_1snapTracker.html#ab0b32c50324a34e91aebf241621dd7fd),
[draftguitools.gui_trackers.rectangleTracker.setorigin()](../../d7/d8d/classdraftguitools_1_1gui__trackers_1_1rectangleTracker.html#ae479b57eba5124cc3051bf736a1f7269),
[draftguitools.gui_trackers.rectangleTracker.update()](../../d7/d8d/classdraftguitools_1_1gui__trackers_1_1rectangleTracker.html#acedcfce459af33f633a1aa7e57501a7f),
[draftguitools.gui_trackers.wireTracker.update()](../../dc/dfc/classdraftguitools_1_1gui__trackers_1_1wireTracker.html#a06640e7b526a420f36ef66f5e2c516fb),
[FeaturePython.ViewProviderCircleSet.updateData()](../../df/d71/classFeaturePython_1_1ViewProviderCircleSet.html#a89b54d62a988a8edc51ac4060b6c090f),
[draftviewproviders.view_wire.ViewProviderWire.updateData()](../../da/dd2/classdraftviewproviders_1_1view__wire_1_1ViewProviderWire.html#a593b4fb5aed224be64e186060dc0b79a),
and
[draftguitools.gui_trackers.wireTracker.updateFromPointlist()](../../dc/dfc/classdraftguitools_1_1gui__trackers_1_1wireTracker.html#a8af4fba9e0805c2a2362f49cf5c1aea8).

## ◆ lineset

ArchPanel.ViewProviderPanelSheet.lineset  
---  
  
Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[ArchPanel.ViewProviderPanelCut.onChanged()](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a095d6d5009cc3ac370c0f85785c16e4b),
and
[ArchPanel.ViewProviderPanelSheet.onChanged()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a23b7c16b9daf13fbb1d9de061e3949a2).

## ◆ switch

ArchPanel.ViewProviderPanelSheet.switch  
---  
  
Referenced by
[PathScripts.PathDressupTagGui.PathDressupTagViewProvider.attach()](../../dc/d08/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagViewProvider.html#a5ab69e8211c75c07d8729a776e2a47ab),
[PathScripts.PathJobGui.ViewProvider.attach()](../../d3/d3e/classPathScripts_1_1PathJobGui_1_1ViewProvider.html#a4b0b81cbeece9ca1e1972c52b970306a),
[PathScripts.PathFeatureExtensionsGui.TaskPanelExtensionPage.cleanupPage()](../../d0/de3/classPathScripts_1_1PathFeatureExtensionsGui_1_1TaskPanelExtensionPage.html#a9d7f24acedc35558022fad962ec1a329),
[PathScripts.PathFeatureExtensionsGui.TaskPanelExtensionPage.createItemForBaseModel()](../../d0/de3/classPathScripts_1_1PathFeatureExtensionsGui_1_1TaskPanelExtensionPage.html#ab5d487f9cf952c3a83c17d2e82dcec80),
[draftguitools.gui_trackers.Tracker.finalize()](../../d2/d99/classdraftguitools_1_1gui__trackers_1_1Tracker.html#ade5d7b8965fb7b5d824ecffce1c7ddf1),
[draftguitools.gui_trackers.Tracker.lowerTracker()](../../d2/d99/classdraftguitools_1_1gui__trackers_1_1Tracker.html#ad4e2306691fe67a64f71f39c9f7ad4b7),
[draftguitools.gui_trackers.Tracker.off()](../../d2/d99/classdraftguitools_1_1gui__trackers_1_1Tracker.html#a1f1fb8ed1ab4ccaf50e1e6bd08d5e393),
[draftguitools.gui_trackers.Tracker.on()](../../d2/d99/classdraftguitools_1_1gui__trackers_1_1Tracker.html#a32813b48effec28b3bbf87a4ec2104e4),
[ArchPanel.ViewProviderPanelCut.onChanged()](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a095d6d5009cc3ac370c0f85785c16e4b),
[ArchPanel.ViewProviderPanelSheet.onChanged()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a23b7c16b9daf13fbb1d9de061e3949a2),
[draftguitools.gui_trackers.Tracker.raiseTracker()](../../d2/d99/classdraftguitools_1_1gui__trackers_1_1Tracker.html#a9d42a38e2e327e9f6a5597bb88bb36ed),
[draftguitools.gui_trackers.ghostTracker.remove()](../../d9/dc6/classdraftguitools_1_1gui__trackers_1_1ghostTracker.html#a6d3d5ac2b343751035f7e31d41c87d87),
[PathScripts.PathFeatureExtensionsGui.TaskPanelExtensionPage.setExtensions()](../../d0/de3/classPathScripts_1_1PathFeatureExtensionsGui_1_1TaskPanelExtensionPage.html#a856caaf6e79ccf88242d279f1f7dd122),
[PathScripts.PathDressupDogbone.ViewProviderDressup.showMarkers()](../../df/ddb/classPathScripts_1_1PathDressupDogbone_1_1ViewProviderDressup.html#a7e76814361ac10fc76685ec77206161c),
[PathScripts.PathJobGui.ViewProvider.showOriginAxis()](../../d3/d3e/classPathScripts_1_1PathJobGui_1_1ViewProvider.html#a673fe185d276bcce7835dcce82485d9c),
[PathScripts.PathDressupTagGui.PathDressupTagViewProvider.turnMarkerDisplayOn()](../../dc/d08/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagViewProvider.html#a4e4ef3c08d6508579ba5fbe2e92a2d13),
and
[PathScripts.PathDressupTagGui.PathDressupTagViewProvider.updatePositions()](../../dc/d08/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagViewProvider.html#a9491908ddf472db45f01229e5e36ff57).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Arch/ArchPanel.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

