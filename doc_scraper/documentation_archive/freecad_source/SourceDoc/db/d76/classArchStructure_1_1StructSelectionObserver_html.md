---
url: https://freecad.github.io/SourceDoc/db/d76/classArchStructure_1_1StructSelectionObserver.html
scraped_at: 2025-09-08T14:58:34.383231
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ArchStructure](../../d3/d32/namespaceArchStructure.html)
  * [StructSelectionObserver](../../db/d76/classArchStructure_1_1StructSelectionObserver.html)

[List of all members](../../de/dfa/classArchStructure_1_1StructSelectionObserver-members.html) | Public Member Functions | Public Attributes

ArchStructure.StructSelectionObserver Class Reference

##  Public Member Functions  
  
---  
def | [addSelection](../../db/d76/classArchStructure_1_1StructSelectionObserver.html#ac984e4631db3078ffee1dc0fee52df74) (self, docName, objName, sub, pos)  
  
##  Public Attributes  
  
---  
|
[callback](../../db/d76/classArchStructure_1_1StructSelectionObserver.html#a9b2773b0a110d80258f1dc5e44e22f4d)  
  
## Member Function Documentation

## ◆ addSelection()

def ArchStructure.StructSelectionObserver.addSelection  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _docName_ ,   
|  |  | _objName_ ,   
|  |  | _sub_ ,   
|  |  | _pos_  
| ) | |   
  
References
[DraftGui.DraftToolBar.callback](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a296c06bdaa66d1e471304f191856ac59),
[PathScripts.PathCamoticsGui.CamoticsSimulation.callback()](../../d0/db0/classPathScripts_1_1PathCamoticsGui_1_1CamoticsSimulation.html#ae061d4f73c3228dfe79c6ed5d3d08df0),
[SmSwitchboard.callback()](../../df/d81/classSmSwitchboard.html#ad1634974cc1d88137f6020d394dbc0bd),
[Gui::SoAutoZoomTranslation.callback()](../../d6/d91/classGui_1_1SoAutoZoomTranslation.html#a737cb8e49ebcc0f3d18b900cd77224ec),
[Gui::SoFCSelectionRoot.callback()](../../d8/d65/classGui_1_1SoFCSelectionRoot.html#a31b401c40836a1fad31ad3aef664e72a),
ArchCommands._SurveyObserver.callback,
[ArchStructure.StructSelectionObserver.callback](../../db/d76/classArchStructure_1_1StructSelectionObserver.html#a9b2773b0a110d80258f1dc5e44e22f4d),
[MeshGui::SoFCMeshFacet.callback()](../../de/d0f/classMeshGui_1_1SoFCMeshFacet.html#aced9b523837dff716de6421b145a9a7b),
[MeshGui::SoFCMeshObjectNode.callback()](../../d8/d3e/classMeshGui_1_1SoFCMeshObjectNode.html#a0a4bc6f047475afcf3c401b9cc987191),
[MeshGui::SoFCMeshVertex.callback()](../../d8/dc3/classMeshGui_1_1SoFCMeshVertex.html#a4ca1c7bc993588d72f145ae87e0a6c7c),
nlohmann::detail::json_sax_dom_callback_parser< BasicJsonType >.callback,
nlohmann::detail::parser< BasicJsonType, InputAdapterType >.callback,
[SketcherGui::SoZoomTranslation.callback()](../../d2/d20/classSketcherGui_1_1SoZoomTranslation.html#a81ddb6e4b428e25164c335ee39110dda),
[qtunittest.GUITestResult.callback](../../d1/d00/classqtunittest_1_1GUITestResult.html#a7c96077b64c6e5b9f35865b43bf5eb6d),
[Mod.Test.unittestgui.GUITestResult.callback](../../d1/d18/classMod_1_1Test_1_1unittestgui_1_1GUITestResult.html#aa60628ae85de2e35d091dad2cf2803aa),
ArchStructure._StructuralSystem.getAxisPlacement(),
ArchStructure._StructuralSystem.getAxisPoints(),
[ArchComponent.Component.processSubShapes()](../../de/d87/classArchComponent_1_1Component.html#a34cd7509406ea5e01a1d72b41e900742),
[draftutils.translate.QT_TRANSLATE_NOOP](../../de/d75/group__draftutils.html#ga9e6796e4394a4a163501246d7390f3c4),
[App::FeaturePythonPyT< FeaturePyT
>.Type](../../d5/df9/classApp_1_1FeaturePythonPyT.html#a30564b7cd97268ab1c5ec82087341bb3),
[App::Part.Type](../../da/d8d/classApp_1_1Part.html#a0a40cb4c87c3b600ff21bbc2073a9b58),
[App::PropertyData::PropertySpec.Type](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html#a6244b48b04beb90601c0eab74414ac4f),
[Base::PyObjectBase.Type](../../d0/d61/classBase_1_1PyObjectBase.html#aa40cc61e3f6a68dd6fb81745b5fc20de),
[Base::Type.Type()](../../dc/dee/classBase_1_1Type.html#a26ce658f5055f20610491addb5983ad6),
Py::Type.Type(),
[Gui::SelectionChanges.Type](../../d5/d50/classGui_1_1SelectionChanges.html#a14bc5c24e02146dec9aadcbde50d3651),
ArchAxis._Axis.Type, ArchAxisSystem._AxisSystem.Type,
ArchBuilding._Building.Type,
[ArchBuildingPart.BuildingPart.Type](../../d2/def/classArchBuildingPart_1_1BuildingPart.html#acaa6f58401fab574a68e9a88c7a18e75),
[ArchComponent.Component.Type](../../de/d87/classArchComponent_1_1Component.html#a4a5c3bb5d5f50162eca9c62b01ec1e32),
ArchEquipment._Equipment.Type, ArchFence._Fence.Type, ArchFloor._Floor.Type,
ArchFrame._Frame.Type,
[ArchGrid.ArchGrid.Type](../../d7/d52/classArchGrid_1_1ArchGrid.html#a2b579984d85ef9ff4d312b9f7a311fef),
ArchMaterial._ArchMaterialContainer.Type, ArchMaterial._ArchMaterial.Type,
ArchMaterial._ArchMultiMaterial.Type, ArchPanel._Panel.Type,
[ArchPanel.PanelView.Type](../../dd/da0/classArchPanel_1_1PanelView.html#ac870d9fd722704e5618157a816ba2e03),
[ArchPanel.PanelCut.Type](../../d6/dbd/classArchPanel_1_1PanelCut.html#a0a2977f3f7ff28a9200a96c93e3903ee),
[ArchPanel.PanelSheet.Type](../../dc/d22/classArchPanel_1_1PanelSheet.html#a029f7be79c7aecc3314076236b5105d7),
ArchPipe._ArchPipe.Type, ArchPipe._ArchPipeConnector.Type,
ArchPrecast._Precast.Type, ArchProject._Project.Type, ArchRebar._Rebar.Type,
[ArchReference.ArchReference.Type](../../d3/d06/classArchReference_1_1ArchReference.html#a02e4ee0ba8acff45b12557cdf006e337),
ArchRoof._Roof.Type, ArchSchedule._ArchSchedule.Type,
ArchSectionPlane._SectionPlane.Type, ArchSectionPlane._ArchDrawingView.Type,
ArchSite._Site.Type, ArchSpace._Space.Type, ArchStairs._Stairs.Type,
ArchStructure._Structure.Type, ArchStructure._StructuralSystem.Type,
[ArchTruss.Truss.Type](../../d9/d6f/classArchTruss_1_1Truss.html#a1660bf4d5d226841974b618b2eec7c95),
ArchWall._Wall.Type, ArchWindow._Window.Type,
[draftobjects.base.DraftObject.Type](../../d1/d64/classdraftobjects_1_1base_1_1DraftObject.html#a5ea27fe2e4a784618bb15cce5fed29da),
[draftobjects.draft_annotation.DraftAnnotation.Type](../../d4/dca/classdraftobjects_1_1draft__annotation_1_1DraftAnnotation.html#aa4ff69b2beeff361d3fc7cbbb5525877),
[draftobjects.hatch.Hatch.Type](../../db/d7f/classdraftobjects_1_1hatch_1_1Hatch.html#a475adff5eebedba71f542ec42a2b2613),
[draftobjects.layer.Layer.Type](../../d0/ddc/classdraftobjects_1_1layer_1_1Layer.html#a87de9038f1943ab0652620c09f76999f),
[draftobjects.layer.LayerContainer.Type](../../de/d4d/classdraftobjects_1_1layer_1_1LayerContainer.html#a64993d18819511ef6653e8818afb886d),
[draftobjects.wpproxy.WorkingPlaneProxy.Type](../../d1/d19/classdraftobjects_1_1wpproxy_1_1WorkingPlaneProxy.html#a2084c6e0721cfd8e5f050fbdc3540141),
[femobjects.constant_vacuumpermittivity.ConstantVacuumPermittivity.Type](../../d6/db6/classfemobjects_1_1constant__vacuumpermittivity_1_1ConstantVacuumPermittivity.html#a003dafc798992d429951717bf69a479c),
[femobjects.constraint_bodyheatsource.ConstraintBodyHeatSource.Type](../../d7/d28/classfemobjects_1_1constraint__bodyheatsource_1_1ConstraintBodyHeatSource.html#ab94186d5a2fa03dc2b09e454661dd6c5),
[femobjects.constraint_centrif.ConstraintCentrif.Type](../../d8/dc4/classfemobjects_1_1constraint__centrif_1_1ConstraintCentrif.html#a8a65cc6e8fdc11a99e7e0dbfd9480a51),
[femobjects.constraint_electrostaticpotential.ConstraintElectrostaticPotential.Type](../../d9/db9/classfemobjects_1_1constraint__electrostaticpotential_1_1ConstraintElectrostaticPotential.html#ae442a4db8cf082a04c42a0e4fed213fd),
[femobjects.constraint_flowvelocity.ConstraintFlowVelocity.Type](../../d5/dc9/classfemobjects_1_1constraint__flowvelocity_1_1ConstraintFlowVelocity.html#af7e4d0e2423972ba96660cde7425c481),
[femobjects.constraint_initialflowvelocity.ConstraintInitialFlowVelocity.Type](../../de/d2d/classfemobjects_1_1constraint__initialflowvelocity_1_1ConstraintInitialFlowVelocity.html#aeecfd1ce5578c520a890f3c02f3be48d),
[femobjects.constraint_sectionprint.ConstraintSectionPrint.Type](../../de/d31/classfemobjects_1_1constraint__sectionprint_1_1ConstraintSectionPrint.html#abf70ff34ebe0f11df556c2d8e39de37a),
[femobjects.constraint_selfweight.ConstraintSelfWeight.Type](../../d1/d49/classfemobjects_1_1constraint__selfweight_1_1ConstraintSelfWeight.html#ad4f9e756e3f3ed3684882549f2e998fd),
[femobjects.constraint_tie.ConstraintTie.Type](../../d8/df5/classfemobjects_1_1constraint__tie_1_1ConstraintTie.html#ac695ceed59e47822e7b489af984705ca),
[femobjects.element_fluid1D.ElementFluid1D.Type](../../df/d16/classfemobjects_1_1element__fluid1D_1_1ElementFluid1D.html#a6a1f92e36bfaa2fede1c04a65d173112),
[femobjects.element_geometry1D.ElementGeometry1D.Type](../../d0/d4f/classfemobjects_1_1element__geometry1D_1_1ElementGeometry1D.html#aa49316cb0d3742daf112a4319bafe3fe),
[femobjects.element_geometry2D.ElementGeometry2D.Type](../../d1/d6f/classfemobjects_1_1element__geometry2D_1_1ElementGeometry2D.html#aec4e8219d3c239d7967d8e58fa79b1ad),
[femobjects.element_rotation1D.ElementRotation1D.Type](../../d8/d0c/classfemobjects_1_1element__rotation1D_1_1ElementRotation1D.html#a31e57a2998752501d0e5b59510a3f4d3),
[femobjects.material_common.MaterialCommon.Type](../../db/dfc/classfemobjects_1_1material__common_1_1MaterialCommon.html#a6a59fa9434a44b1c8c7c3c8d970a58c8),
[femobjects.material_mechanicalnonlinear.MaterialMechanicalNonlinear.Type](../../dd/de0/classfemobjects_1_1material__mechanicalnonlinear_1_1MaterialMechanicalNonlinear.html#a1081a3956f0b3f397de6b094762f8c9d),
[femobjects.material_reinforced.MaterialReinforced.Type](../../da/de9/classfemobjects_1_1material__reinforced_1_1MaterialReinforced.html#a5435f0ba45bb61fa825c29fd6aaeb043),
[femobjects.mesh_boundarylayer.MeshBoundaryLayer.Type](../../de/d8e/classfemobjects_1_1mesh__boundarylayer_1_1MeshBoundaryLayer.html#a44c98ddcafd39b00595a179ce79c919d),
[femobjects.mesh_gmsh.MeshGmsh.Type](../../d0/d6a/classfemobjects_1_1mesh__gmsh_1_1MeshGmsh.html#accca355b99808987e89a50dc0a7a8abb),
[femobjects.mesh_group.MeshGroup.Type](../../db/d27/classfemobjects_1_1mesh__group_1_1MeshGroup.html#a4205607b5781b420c1cf795bfc18ae1e),
[femobjects.mesh_region.MeshRegion.Type](../../d9/d54/classfemobjects_1_1mesh__region_1_1MeshRegion.html#acd98c4198b934d280996601aacf4f698),
[femobjects.mesh_result.MeshResult.Type](../../d3/dc5/classfemobjects_1_1mesh__result_1_1MeshResult.html#a5e0ad65a89b84fc7c666d52dcad8c26a),
[femobjects.result_mechanical.ResultMechanical.Type](../../df/d8e/classfemobjects_1_1result__mechanical_1_1ResultMechanical.html#ae31e12f1d2e8388b73c421c5b4fa5a75),
[femobjects.solver_ccxtools.SolverCcxTools.Type](../../d6/d04/classfemobjects_1_1solver__ccxtools_1_1SolverCcxTools.html#afc7312b45245fcfb8b13fce99bc42883),
[femsolver.calculix.solver.Proxy.Type](../../d1/d64/classfemsolver_1_1calculix_1_1solver_1_1Proxy.html#a0dda3e478bc2f2e7a7c213757b477c94),
[femsolver.elmer.equations.elasticity.Proxy.Type](../../d1/d26/classfemsolver_1_1elmer_1_1equations_1_1elasticity_1_1Proxy.html#a827374b372394f6a55715d8000d91a11),
[femsolver.elmer.equations.electricforce.Proxy.Type](../../df/d18/classfemsolver_1_1elmer_1_1equations_1_1electricforce_1_1Proxy.html#a424b9d54098cca5b041b985285d846ea),
[femsolver.elmer.equations.electrostatic.Proxy.Type](../../d6/de7/classfemsolver_1_1elmer_1_1equations_1_1electrostatic_1_1Proxy.html#a7abadb440f9efb90383a3bce2bf40bd9),
[femsolver.elmer.equations.flow.Proxy.Type](../../d7/df7/classfemsolver_1_1elmer_1_1equations_1_1flow_1_1Proxy.html#a17792067859e79de47ee42476bdca7af),
[femsolver.elmer.equations.flux.Proxy.Type](../../d7/d6e/classfemsolver_1_1elmer_1_1equations_1_1flux_1_1Proxy.html#ade7473658051685426681928fc8573f6),
[femsolver.elmer.equations.heat.Proxy.Type](../../d6/d2e/classfemsolver_1_1elmer_1_1equations_1_1heat_1_1Proxy.html#a8fe59b519933d43683f8778dad3de91b),
[femsolver.elmer.solver.Proxy.Type](../../d1/d12/classfemsolver_1_1elmer_1_1solver_1_1Proxy.html#a29077c596586ad78d325b35980a32a82),
[femsolver.mystran.solver.Proxy.Type](../../d5/d4c/classfemsolver_1_1mystran_1_1solver_1_1Proxy.html#abdcd60e96f9af34af791155ec54f2f6f),
[femsolver.z88.solver.Proxy.Type](../../da/df7/classfemsolver_1_1z88_1_1solver_1_1Proxy.html#adadcfae624495e13f9216a7bec1937b5),
[FemGui::FemSelectionGate.Type](../../dd/de5/classFemGui_1_1FemSelectionGate.html#a73acc6174efc0f8d14d733b9b2fdc775),
[Import::FeatureImportIges.Type()](../../d7/dac/classImport_1_1FeatureImportIges.html#ae6b12eca169b5640871542c5749285a4),
[Import::FeatureImportStep.Type()](../../da/dde/classImport_1_1FeatureImportStep.html#ad67e186d8b9e9429b29b2c399214d1f0),
[BOPTools.JoinFeatures.FeatureConnect.Type](../../d0/d85/classBOPTools_1_1JoinFeatures_1_1FeatureConnect.html#a085878c3a06ffcc56f72411ea7b999b6),
[BOPTools.JoinFeatures.FeatureEmbed.Type](../../d7/d55/classBOPTools_1_1JoinFeatures_1_1FeatureEmbed.html#a1a5451e074efffe4a5b3fbd7e13b3211),
[BOPTools.JoinFeatures.FeatureCutout.Type](../../da/d9a/classBOPTools_1_1JoinFeatures_1_1FeatureCutout.html#a0f6002e45db975e0c036d9091841017a),
[BOPTools.SplitFeatures.FeatureBooleanFragments.Type](../../dc/d6e/classBOPTools_1_1SplitFeatures_1_1FeatureBooleanFragments.html#ac69fc844a4b5e6fb9c42b39b5b768ad8),
[BOPTools.SplitFeatures.FeatureSlice.Type](../../d1/d28/classBOPTools_1_1SplitFeatures_1_1FeatureSlice.html#a233fc62ef4b1c01e2b8f35fd8184ae2c),
[BOPTools.SplitFeatures.FeatureXOR.Type](../../da/dc0/classBOPTools_1_1SplitFeatures_1_1FeatureXOR.html#ae6a2dd3e1299c54cf3f63a779e19f740),
CompoundTools.CompoundFilter._CompoundFilter.Type,
JoinFeatures._PartJoinFeature.Type,
[PartDesign::Boolean.Type](../../d2/d81/classPartDesign_1_1Boolean.html#abaa8fc572b875da05542f6cdcfb43b87),
[PartDesign::FeatureExtrude.Type](../../da/d12/classPartDesign_1_1FeatureExtrude.html#ab2d0f58f67fe1b39c32a8ba2a195d66c),
Mod.PartDesign.InvoluteGearFeature._InvoluteGear.Type,
[Mod.PartDesign.SprocketFeature.Sprocket.Type](../../d6/df0/classMod_1_1PartDesign_1_1SprocketFeature_1_1Sprocket.html#af1b6d3a276a2e1a68b0343018f61d490),
[Path::Tool.Type](../../dd/dfe/classPath_1_1Tool.html#a1a5c4a64ea8594cbc421bad861f7a55c),
[Robot::Waypoint.Type](../../d1/dc7/classRobot_1_1Waypoint.html#ad99104e4ef2eb005f6f1569be5339591),
[Sketcher::ConstraintIds.Type](../../d0/d44/structSketcher_1_1ConstraintIds.html#a53ec9e04ffffd30aba48f6594e78b612),
[Sketcher::Constraint.Type](../../d6/def/classSketcher_1_1Constraint.html#a9190f836a1069a4d68d7d06fa51bf8f1),
[SketcherGui::AutoConstraint.Type](../../d3/db2/structSketcherGui_1_1AutoConstraint.html#aeab32f95e6eabfc8d7350fab4f2637db),
[Spreadsheet_legacy.Spreadsheet.Type](../../d2/d6d/classSpreadsheet__legacy_1_1Spreadsheet.html#af352de8d6ea6ae08c1a29bae9f20e2e5),
[Spreadsheet_legacy.SpreadsheetController.Type](../../d1/d38/classSpreadsheet__legacy_1_1SpreadsheetController.html#a3b6ea54bbf3ed2ea79305e7d66679b6d),
[Spreadsheet_legacy.SpreadsheetPropertyController.Type](../../d5/d01/classSpreadsheet__legacy_1_1SpreadsheetPropertyController.html#a2a485827317092e4c630f20a69466c1a),
[TechDraw::DrawProjGroupItem.Type](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a952de556951509da8740b0bf924fdf8e),
[TechDraw::DrawViewDimension.Type](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#aae98f71f065fb355c0e9145f363c4b3d),
[TechDrawGui::QGCustomBorder.Type](../../d5/d7b/classTechDrawGui_1_1QGCustomBorder.html#a34a214b82406103046843f78a562a163a599ae99463247ae65be81a5fa7f34aa4),
[TechDrawGui::QGCustomClip.Type](../../db/d33/classTechDrawGui_1_1QGCustomClip.html#ac734f647650f53acc8a42125c8a0bb70a6c691532e5cd18fef6598b7084cbec4d),
[TechDrawGui::QGCustomImage.Type](../../d5/d80/classTechDrawGui_1_1QGCustomImage.html#ab1970a1e546a68598947d99573a86352a0cb5d62da4ef545552b6c316ca2fef12),
[TechDrawGui::QGCustomLabel.Type](../../d4/dec/classTechDrawGui_1_1QGCustomLabel.html#a12fc2c36c627d584a8c907ad71623d0ea9d2484267356f0519f2bac2b8b5e58fb),
[TechDrawGui::QGCustomRect.Type](../../d9/d78/classTechDrawGui_1_1QGCustomRect.html#aec720a2da3d8cec0f8c9a2823782bef0ac701148347fcabef101d37476fe60018),
[TechDrawGui::QGCustomSvg.Type](../../d4/d3c/classTechDrawGui_1_1QGCustomSvg.html#a906be3c8ad0886baf69b9286d4c1af4eae43649273dcd5ae22e012ef67af4b748),
[TechDrawGui::QGCustomText.Type](../../d8/d42/classTechDrawGui_1_1QGCustomText.html#a5e6e8209f3bfb21d1e06e21f0544bdacab31562c88940d9d5b974a32d039ed948),
[TechDrawGui::QGDisplayArea.Type](../../d4/da6/classTechDrawGui_1_1QGDisplayArea.html#a77aadc72052fa76e7621af0c504e1a86a9e04344dc341a437bd4df79fd7ff135f),
[TechDrawGui::QGMarker.Type](../../d8/de2/classTechDrawGui_1_1QGMarker.html#a9dee446914eeaae77b5d1a2dd4bf3e94a77ce0f76e7105fdb2e3ab4ac7a9c8b73),
[TechDrawGui::QGEPath.Type](../../d9/da7/classTechDrawGui_1_1QGEPath.html#a5d2bb9a49bf6c87130c3754de1b25356a9f81c65b47e399fb60c1cbfcfee11226),
[TechDrawGui::QGIArrow.Type](../../d4/d60/classTechDrawGui_1_1QGIArrow.html#a8472ba969a65f8f973cc6ea9c9ce59a8ab799fe719ee151f8b9e3158ff3c57981),
[TechDrawGui::QGICaption.Type](../../d2/d68/classTechDrawGui_1_1QGICaption.html#a71703f39a9ad603870b6d8a5428ecb78aea045d6a58a1631e10a5df93401319cf),
[TechDrawGui::QGICenterLine.Type](../../d5/d69/classTechDrawGui_1_1QGICenterLine.html#a7322222d95ff78d312cece7a55be3f25ae857eca9df729ff51b256590a2dd8291),
[TechDrawGui::QGICMark.Type](../../d0/de9/classTechDrawGui_1_1QGICMark.html#aed3d772f8585ca030aec5aa4a46344bda96268001ffdbc0977f1387a74af61da2),
[TechDrawGui::QGIDecoration.Type](../../d7/dcd/classTechDrawGui_1_1QGIDecoration.html#acb742c749b524dfcb7f6e20ec60eb032a97ac081e4c8a90800b45458fc6f6dc00),
[TechDrawGui::QGIDimLines.Type](../../d2/d30/classTechDrawGui_1_1QGIDimLines.html#a9576de78ac8decae7b7a64fe80a739c2a4bcf5bff761700ebcc64de8a18fede05),
[TechDrawGui::QGIDrawingTemplate.Type](../../d3/d23/classTechDrawGui_1_1QGIDrawingTemplate.html#a73c70815ccc1451ccfb0ca443dc2dcb0a2b107fff323f9d9bb924730331593d22),
[TechDrawGui::QGIEdge.Type](../../dd/d6c/classTechDrawGui_1_1QGIEdge.html#aed397ffd157f476375472bf2bda49711a543d53e7ac49ec5c6b369a2a2c550d34),
[TechDrawGui::QGIFace.Type](../../d9/d59/classTechDrawGui_1_1QGIFace.html#ae21480fdaab7b3295cf9988c30e4cfeba530da8179c89e6929a2a9c1438d18afe),
[TechDrawGui::QGIGhostHighlight.Type](../../d1/d6a/classTechDrawGui_1_1QGIGhostHighlight.html#ac2315f6f8da71e123de6a808202c7460a659fe1f1eb97f2e7268812826a1ae6f9),
[TechDrawGui::QGIHighlight.Type](../../df/dee/classTechDrawGui_1_1QGIHighlight.html#a12a75f3803b101bd7a11d84c38aa9cdda1faaa60152d143c1abfefb423a81a664),
[TechDrawGui::QGILeaderLine.Type](../../db/d57/classTechDrawGui_1_1QGILeaderLine.html#ab6a8a830c63d6958b68e6ccf90202876a91233b24fd3b76a8b7b01a4231dc8216),
[TechDrawGui::QGIMatting.Type](../../d2/d0e/classTechDrawGui_1_1QGIMatting.html#af7c3fa816a92bf1317a318e587b9540fa003d89c4fddf536c33ffdd7c6813ed54),
[TechDrawGui::QGIPrimPath.Type](../../dd/dc6/classTechDrawGui_1_1QGIPrimPath.html#a1edb8eca4ab12c4d7bda827df9e5f26ba0c2976410ae0147267f5ff0e700ed82a),
[TechDrawGui::QGIProjGroup.Type](../../db/d20/classTechDrawGui_1_1QGIProjGroup.html#ab7031a8b6f56d526d52a958eb074a6fba69c179233f383c04a24ab1062f50455c),
[TechDrawGui::QGIRichAnno.Type](../../d0/d89/classTechDrawGui_1_1QGIRichAnno.html#aefe95fc9b872ebf9260cf93418aee72bab3d0618783c6370f020d006aa3d35c65),
[TechDrawGui::QGISectionLine.Type](../../dd/db1/classTechDrawGui_1_1QGISectionLine.html#ab646fb03b45180b28ca8086338baa676a4624d0454c209045d7a6dd399da6eaa7),
[TechDrawGui::QGISVGTemplate.Type](../../d4/d36/classTechDrawGui_1_1QGISVGTemplate.html#a1766596c75248c888c21476b9b0fab5ea57eca51f45938727163020df6c28f08a),
[TechDrawGui::QGITemplate.Type](../../d5/d8e/classTechDrawGui_1_1QGITemplate.html#a636a084d979e88901c8e73799e718799a92a78b30aacebea31bf40b89471a7658),
[TechDrawGui::QGITile.Type](../../d6/d9b/classTechDrawGui_1_1QGITile.html#a0288420d7caf083efd206b026de96b86aa98b6d33f579d065156cb5ee2f6d9338),
[TechDrawGui::QGIVertex.Type](../../d0/d7d/classTechDrawGui_1_1QGIVertex.html#a7806bd155e1bf9713ad3061fae7e7ea9ac2b29cff0f277dc429c686c39b52e78b),
[TechDrawGui::QGIView.Type](../../d1/d99/classTechDrawGui_1_1QGIView.html#a95a4fdb35cd4b584aadbcaab7992b1f2aaef695b1dc11c7fa20ad2a3aaaf03fdd),
[TechDrawGui::QGIViewAnnotation.Type](../../d4/d5b/classTechDrawGui_1_1QGIViewAnnotation.html#ade42c83a994c527913805923c14afa16a34117b672c1e35526efcd04fe332b097),
[TechDrawGui::QGIBalloonLabel.Type](../../dc/d5c/classTechDrawGui_1_1QGIBalloonLabel.html#ac20842d970d6918ab9bd53c2616c493aa156b22e7be0aefbfda1d59449bec70bf),
[TechDrawGui::QGIViewBalloon.Type](../../d0/d29/classTechDrawGui_1_1QGIViewBalloon.html#a14cd65d5c6968300e021fde990578185a075fc86b328acc99fa015675e9539193),
[TechDrawGui::QGIViewClip.Type](../../d4/dcc/classTechDrawGui_1_1QGIViewClip.html#ad1b0ac4caaa861b7fe05debaccc627efa12f85250d7cea3d542e8d1d5a2ce1666),
[TechDrawGui::QGIViewCollection.Type](../../d0/dd1/classTechDrawGui_1_1QGIViewCollection.html#a31e27d058688ebd167e49555c5fddc75a9cb796498477560f3da6ca2e0ce91783),
[TechDrawGui::QGIDatumLabel.Type](../../d7/d0c/classTechDrawGui_1_1QGIDatumLabel.html#a7d7a967a9868b24cbd063acaad009306a93aceb84dc2cff89c264c7fa48671aa0),
[TechDrawGui::QGIViewDimension.Type](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#ad0b101d699bb7c6238fe11c663339bc5a46d1e488a429a0b726abb7b75fb6117e),
[TechDrawGui::QGIViewImage.Type](../../d9/ddb/classTechDrawGui_1_1QGIViewImage.html#ae55d41b24d6e2374786b75849aa938d1a4f92ffa9b6de2576b27f896245e24477),
[TechDrawGui::QGIViewPart.Type](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#a9205a836ddc11b3738074507eb8d2bb8aa55000633f8c330ae41fbc73f25e3f51),
[TechDrawGui::QGIViewSection.Type](../../d7/d73/classTechDrawGui_1_1QGIViewSection.html#a6f792c7a034bdd41f7fe5d84a3339a8fa82967530b4c864bbb426e508dc1eff9a),
[TechDrawGui::QGIViewSpreadsheet.Type](../../d5/d05/classTechDrawGui_1_1QGIViewSpreadsheet.html#a3fd77e4b77ec1fea324573c3ed528aa7a9b2902c31348ed5f1ef7d26b3568956b),
[TechDrawGui::QGIViewSymbol.Type](../../d1/da0/classTechDrawGui_1_1QGIViewSymbol.html#a4e1c28ebfa04186445e971f034f7e9f9ad8b091fc538b2964070ef3aa8baad53b),
[TechDrawGui::QGIWeldSymbol.Type](../../da/dcd/classTechDrawGui_1_1QGIWeldSymbol.html#a9bbb2171e64f2adde7f10221cdfffd80af334738f577ec2a4c6f30b8a1a39c1a6),
[TechDrawGui::QGMText.Type](../../d4/d28/classTechDrawGui_1_1QGMText.html#a2aa57280a268eecc5ce2105cf895afbea3070b7ecb7b2442b979c2effcd34eb89),
[TechDrawGui::QGTracker.Type](../../da/d66/classTechDrawGui_1_1QGTracker.html#ab082bbe3fddfe49c01ed28dc1f2cae68a6aaeeb54f94dce879a2fabe9423802ec),
[TechDrawGui::TemplateTextField.Type](../../d9/d4e/classTechDrawGui_1_1TemplateTextField.html#a936b5453c53b94a9ce7e73cd69eff97cadc2d7f6db209109574d318866c11f6ab),
[DocumentObject.DocumentObject.Type()](../../d7/dae/classDocumentObject_1_1DocumentObject.html#adf8fab4998d6834dcde65aa6adcb188f),
and
[DocumentObject.ViewProvider.Type()](../../d8/dd7/classDocumentObject_1_1ViewProvider.html#a0dae9452ad6b57ed3616a5b113eea97a).

## Member Data Documentation

## ◆ callback

ArchStructure.StructSelectionObserver.callback  
---  
  
Referenced by
[qtunittest.GUITestResult.addError()](../../d1/d00/classqtunittest_1_1GUITestResult.html#ae48860c1b471550b79d21258aecc7efb),
[Mod.Test.unittestgui.GUITestResult.addError()](../../d1/d18/classMod_1_1Test_1_1unittestgui_1_1GUITestResult.html#a9344b1ab5e86e91088bd9d62396f7814),
[qtunittest.GUITestResult.addFailure()](../../d1/d00/classqtunittest_1_1GUITestResult.html#ac560ab52550d22b3b22fd3498d375a98),
[Mod.Test.unittestgui.GUITestResult.addFailure()](../../d1/d18/classMod_1_1Test_1_1unittestgui_1_1GUITestResult.html#ae8a66d91a1c99d0753cf2f35d70d73d9),
[ArchStructure.StructSelectionObserver.addSelection()](../../db/d76/classArchStructure_1_1StructSelectionObserver.html#ac984e4631db3078ffee1dc0fee52df74),
[PathScripts.PathCamoticsGui.CamoticsSimulation.execute()](../../d0/db0/classPathScripts_1_1PathCamoticsGui_1_1CamoticsSimulation.html#a2814905f08041fc7111270671b13096d),
[qtunittest.GUITestResult.startTest()](../../d1/d00/classqtunittest_1_1GUITestResult.html#a5c304ec542f1f451bf1ec1def6b2b7d8),
[Mod.Test.unittestgui.GUITestResult.startTest()](../../d1/d18/classMod_1_1Test_1_1unittestgui_1_1GUITestResult.html#a05d6b60e93ded48f3da839251d074bf6),
[qtunittest.GUITestResult.stopTest()](../../d1/d00/classqtunittest_1_1GUITestResult.html#a9a7eb4e88e892399ae22ed06a45f957c),
and
[Mod.Test.unittestgui.GUITestResult.stopTest()](../../d1/d18/classMod_1_1Test_1_1unittestgui_1_1GUITestResult.html#a65c5312dc3d260644f9404d2ab05c86a).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Arch/ArchStructure.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

