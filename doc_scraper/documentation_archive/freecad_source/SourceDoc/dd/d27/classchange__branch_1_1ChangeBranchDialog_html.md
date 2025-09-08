---
url: https://freecad.github.io/SourceDoc/dd/d27/classchange__branch_1_1ChangeBranchDialog.html
scraped_at: 2025-09-08T15:19:01.529138
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [change_branch](../../dc/d9f/namespacechange__branch.html)
  * [ChangeBranchDialog](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html)

[List of all members](../../d1/d57/classchange__branch_1_1ChangeBranchDialog-members.html) | Public Member Functions | Public Attributes | Static Public Attributes

change_branch.ChangeBranchDialog Class Reference

##  Public Member Functions  
  
---  
def | [exec](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a6c58ac15929c71fac630a9462df2004c) (self)  
  
##  Public Attributes  
  
---  
|
[item_filter](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#af0ce02d3d7dc91300fea3d0e94ea3aab)  
|
[item_model](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a2973e58066cedd227e8e9dc4b2f7407e)  
|
[ui](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#aa36b394e7540f2fe906ceba455163f0d)  
  
##  Static Public Attributes  
  
---  
|
[branch_changed](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a58c681743b684a5d792abf9bb24fd021)
= QtCore.Signal([str](../../d9/d36/classstr.html))  
  
## Member Function Documentation

## ◆ exec()

def change_branch.ChangeBranchDialog.exec  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[change_branch.ChangeBranchDialog.branch_changed](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a58c681743b684a5d792abf9bb24fd021),
[package_details.PackageDetails.branch_changed()](../../d1/df5/classpackage__details_1_1PackageDetails.html#a15328dbccbc762df726cf1fe9264cb5c),
[change_branch.ChangeBranchDialog.exec()](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a6c58ac15929c71fac630a9462df2004c),
[change_branch.ChangeBranchDialog.item_filter](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#af0ce02d3d7dc91300fea3d0e94ea3aab),
[package_list.PackageList.item_filter](../../d8/d41/classpackage__list_1_1PackageList.html#aae2a686bb4ae31740cd78c666faddeba),
[AddonManager.CommandAddonManager.item_model](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a935f56116ff654bd2adcf2049021fd71),
[change_branch.ChangeBranchDialog.item_model](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a2973e58066cedd227e8e9dc4b2f7407e),
[package_list.PackageList.item_model](../../d8/d41/classpackage__list_1_1PackageList.html#a2ef980f40752a0fe3bf98a23880921c4),
[Gui::Dialog::Clipping::Private.ui](../../d0/d7b/classClipping_1_1Private.html#ada68196c0dcc40cea30015612a70afa9),
Gui::Dialog::DemoMode.ui, Gui::Dialog::DlgCustomActionsImp.ui,
Gui::Dialog::IconDialog.ui, Gui::Dialog::DlgActivateWindowImp.ui,
Gui::Dialog::DlgAddProperty.ui,
[Gui::Dialog::DlgCheckableMessageBoxPrivate.ui](../../d6/d3e/structGui_1_1Dialog_1_1DlgCheckableMessageBoxPrivate.html#ac3a2fe31c9149d4f75a527340ad75c67),
Gui::Dialog::DlgCustomCommandsImp.ui,
Gui::Dialog::DlgCreateNewPreferencePackImp.ui,
Gui::Dialog::DlgCustomizeSpNavSettings.ui,
[Gui::Dialog::DlgDisplayPropertiesImp::Private.ui](../../de/d2a/classDlgDisplayPropertiesImp_1_1Private.html#ae7cb2e98b9279f2e6789423b46b28a2d),
Gui::Dialog::DlgSettingsEditorImp.ui, Gui::Dialog::DlgExpressionInput.ui,
Gui::Dialog::DlgGeneralImp.ui, Gui::Dialog::DlgInputDialogImp.ui,
Gui::Dialog::DlgCustomKeyboardImp.ui, Gui::Dialog::DlgMacroExecuteImp.ui,
Gui::Dialog::DlgMacroRecordImp.ui, Gui::Dialog::DlgMaterialPropertiesImp.ui,
Gui::DlgObjectSelection.ui, Gui::Dialog::DlgOnlineHelpImp.ui,
Gui::Dialog::DlgParameterFind.ui,
[Gui::Dialog::DlgParameterImp.ui](../../d7/de1/classGui_1_1Dialog_1_1DlgParameterImp.html#a3539e26e136c618bccae689e0fab652d),
Gui::Dialog::DlgPreferencePackManagementImp.ui,
Gui::Dialog::DlgPreferencesImp.ui, Gui::Dialog::DlgProjectInformationImp.ui,
[Gui::Dialog::DlgProjectUtility.ui](../../d8/d0f/classGui_1_1Dialog_1_1DlgProjectUtility.html#aa6604c30af0f734bba10c9af9801c06c),
Gui::Dialog::DlgPropertyLink.ui, Gui::Dialog::DlgReportViewImp.ui,
Gui::Dialog::DlgRevertToBackupConfigImp.ui, Gui::Dialog::DlgRunExternal.ui,
Gui::Dialog::DlgSettings3DViewImp.ui,
Gui::Dialog::DlgSettingsCacheDirectory.ui,
Gui::Dialog::DlgSettingsColorGradientImp.ui,
Gui::Dialog::DlgSettingsDocumentImp.ui, Gui::Dialog::DlgSettingsImageImp.ui,
Gui::Dialog::DlgSettingsLazyLoadedImp.ui, Gui::Dialog::DlgSettingsMacroImp.ui,
Gui::Dialog::DlgSettingsNavigation.ui,
Gui::Dialog::DlgSettingsPythonConsole.ui,
Gui::Dialog::DlgSettingsSelection.ui, Gui::Dialog::DlgSettingsUnitsImp.ui,
Gui::Dialog::DlgSettingsViewColor.ui,
[Gui::Dialog::DlgCustomToolbars.ui](../../db/d86/classGui_1_1Dialog_1_1DlgCustomToolbars.html#a6b1173d785bdf914cc03aebc1597d97e),
Gui::Dialog::DlgUnitsCalculator.ui, Gui::Dialog::DlgWorkbenchesImp.ui,
[Gui::Dialog::DocumentRecoveryPrivate.ui](../../db/dab/classGui_1_1Dialog_1_1DocumentRecoveryPrivate.html#a9c765a51c0ecd40bca0ef7b0a6da7039),
Gui::Dialog::DownloadManager.ui, [Gui::LocationDialogImp< Ui
>.ui](../../d7/dd6/classGui_1_1LocationDialogImp.html#a0819857384aac6e2d435f453671fcbb6),
Gui::LocationImpUi< Ui >.ui,
[Gui::LocationDialogUiImp.ui](../../de/dbb/classGui_1_1LocationDialogUiImp.html#a93592cb4cbb48a5e0fd9d56927b50154),
Gui::Dialog::Placement.ui, Gui::Dialog::DlgInspector.ui,
Gui::Dialog::AboutDialog.ui, Gui::TaskBoxPosition.ui, Gui::TaskBoxAngle.ui,
[Gui::ElementColors::Private.ui](../../d8/dc9/classElementColors_1_1Private.html#a3118f1f4a1a2bb3152e8811902133079),
Gui::TaskView::TaskAppearance.ui, Gui::TaskView::TaskSelectLinkProperty.ui,
Gui::Dialog::TextureMapping.ui, Gui::Dialog::Transform.ui,
Gui::VectorListEditor.ui, Gui::CheckListDialog.ui,
[change_branch.ChangeBranchDialog.ui](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#aa36b394e7540f2fe906ceba455163f0d),
[package_details.PackageDetails.ui](../../d1/df5/classpackage__details_1_1PackageDetails.html#a129317b36b5956a9e5036c014dd42754),
[package_list.PackageList.ui](../../d8/d41/classpackage__list_1_1PackageList.html#accb1f1065a05157923cd9e58039311d9),
[package_list.CompactView.ui](../../dc/dd0/classpackage__list_1_1CompactView.html#a8ea5e3715de4ca7a4f8a1fd0cb061a70),
[package_list.ExpandedView.ui](../../d0/d92/classpackage__list_1_1ExpandedView.html#a3e744bcade5f1d03210ba7025608bff8),
[draftguitools.gui_base_original.DraftTool.ui](../../da/d09/classdraftguitools_1_1gui__base__original_1_1DraftTool.html#ae5e63515f585e8aa35f8bae25986570c),
[draftguitools.gui_circulararray.CircularArray.ui](../../dc/dd7/classdraftguitools_1_1gui__circulararray_1_1CircularArray.html#a85eb0b9576d4a8fef489647c4c0c6b1b),
[draftguitools.gui_edit.Edit.ui](../../d8/d68/classdraftguitools_1_1gui__edit_1_1Edit.html#a02573b7334c371a07df8f1b47c1700ec),
[draftguitools.gui_groups.AddToGroup.ui](../../d8/d83/classdraftguitools_1_1gui__groups_1_1AddToGroup.html#a083ed71714513503b4712a83e078ce8d),
[draftguitools.gui_groups.SetAutoGroup.ui](../../d4/df8/classdraftguitools_1_1gui__groups_1_1SetAutoGroup.html#aceb9215a3dcd99a0097b94dd494c31a0),
[draftguitools.gui_orthoarray.OrthoArray.ui](../../dc/d0f/classdraftguitools_1_1gui__orthoarray_1_1OrthoArray.html#af8d6c063ca5b8274bcebd732c0b81fe0),
[draftguitools.gui_polararray.PolarArray.ui](../../dd/dc9/classdraftguitools_1_1gui__polararray_1_1PolarArray.html#a51b488802c082d7bc9522012681d1edf),
[draftguitools.gui_snapper.Snapper.ui](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#aded2b237069d4d260aed0ba92a1dc64a),
DrawingGui::TaskOrthoViews.ui, FemGui::DlgSettingsFemCcxImp.ui,
FemGui::DlgSettingsFemElmerImp.ui, FemGui::DlgSettingsFemExportAbaqusImp.ui,
FemGui::DlgSettingsFemGeneralImp.ui, FemGui::DlgSettingsFemGmshImp.ui,
FemGui::DlgSettingsFemInOutVtkImp.ui, FemGui::DlgSettingsFemMaterialImp.ui,
FemGui::DlgSettingsFemMystranImp.ui, FemGui::DlgSettingsFemZ88Imp.ui,
FemGui::TaskAnalysisInfo.ui, FemGui::TaskCreateNodeSet.ui,
FemGui::TaskDriver.ui,
[FemGui::TaskFemConstraintBearing.ui](../../d5/d79/classFemGui_1_1TaskFemConstraintBearing.html#adae96ac828c3a76138a4a2f0c3ff80b2),
FemGui::TaskFemConstraintContact.ui, FemGui::TaskFemConstraintDisplacement.ui,
FemGui::TaskFemConstraintFixed.ui, FemGui::TaskFemConstraintFluidBoundary.ui,
FemGui::TaskFemConstraintForce.ui, FemGui::TaskFemConstraintHeatflux.ui,
FemGui::TaskFemConstraintInitialTemperature.ui,
FemGui::TaskFemConstraintPlaneRotation.ui,
FemGui::TaskFemConstraintPressure.ui, FemGui::TaskFemConstraintSpring.ui,
FemGui::TaskFemConstraintTemperature.ui,
FemGui::TaskFemConstraintTransform.ui, FemGui::TaskObjectName.ui,
FemGui::TaskPostDisplay.ui, FemGui::TaskPostClip.ui,
FemGui::TaskPostDataAlongLine.ui, FemGui::TaskPostDataAtPoint.ui,
FemGui::TaskPostScalarClip.ui, FemGui::TaskPostWarpVector.ui,
FemGui::TaskPostCut.ui, FemGui::TaskTetParameter.ui, FemGui::PlaneWidget.ui,
FemGui::SphereWidget.ui, ImageGui::ImageOrientationDialog.ui,
InspectionGui::VisualInspection.ui, MeshGui::DlgDecimating.ui,
[MeshGui::DlgEvaluateMeshImp::Private.ui](../../dc/da0/classDlgEvaluateMeshImp_1_1Private.html#a44a216a6919acbbf15ad923f5c94359e),
MeshGui::DlgEvaluateSettings.ui, MeshGui::DlgRegularSolidImp.ui,
MeshGui::DlgSettingsImportExport.ui, MeshGui::DlgSettingsMeshView.ui,
MeshGui::DlgSmoothing.ui,
[MeshGui::GmshWidget::Private.ui](../../d7/d2a/classGmshWidget_1_1Private.html#a142b7908a5cf7b91469986fff997de23),
MeshGui::RemoveComponents.ui, MeshGui::Segmentation.ui,
MeshGui::SegmentationBestFit.ui, MeshGui::Selection.ui,
MeshPartGui::CrossSections.ui, MeshPartGui::CurveOnMeshWidget.ui,
MeshPartGui::Tessellation.ui, PartGui::CrossSections.ui,
PartGui::DlgBooleanOperation.ui, PartGui::DlgExtrusion.ui,
PartGui::DlgFilletEdges.ui, PartGui::DlgPartImportIgesImp.ui,
PartGui::DlgPartImportStepImp.ui, PartGui::DlgPrimitives.ui,
PartGui::Location.ui, PartGui::DlgProjectionOnSurface.ui,
PartGui::DlgRevolution.ui, PartGui::DlgSettings3DViewPart.ui,
PartGui::DlgSettingsGeneral.ui, PartGui::DlgImportExportIges.ui,
PartGui::DlgImportExportStep.ui, PartGui::DlgSettingsObjectColor.ui,
PartGui::Mirroring.ui, PartGui::SectionCut.ui, PartGui::ShapeFromMesh.ui,
PartGui::TaskAttacher.ui,
[PartGui::FaceColors::Private.ui](../../d4/d4b/classFaceColors_1_1Private.html#ac08c52779414847e0dd8d33e0cecf1a3),
[PartGui::LoftWidget::Private.ui](../../d5/d93/classLoftWidget_1_1Private.html#a984500a34561da970a7c6ae533f15983),
[PartGui::OffsetWidget::Private.ui](../../d9/d3e/classOffsetWidget_1_1Private.html#ae5634287ffaf785216b4a477bc42b3fd),
[PartGui::ShapeBuilderWidget::Private.ui](../../dc/d12/classShapeBuilderWidget_1_1Private.html#abf505ed1100a0e6ef95b0216703783f0),
[PartGui::SweepWidget::Private.ui](../../d9/daf/classSweepWidget_1_1Private.html#a1ca05e95511937d69d6e4785f7176563),
[PartGui::ThicknessWidget::Private.ui](../../df/df6/classThicknessWidget_1_1Private.html#a1dc25fc758b2a28e0fd21cd1fa52bd0d),
[Mod.PartDesign.FeatureHole.TaskHole.TaskHole.ui](../../d1/d14/classMod_1_1PartDesign_1_1FeatureHole_1_1TaskHole_1_1TaskHole.html#a4200e3a04a2eb08703c8be5f03169c49),
PartDesignGui::DlgActiveBody.ui, PartDesignGui::TaskBooleanParameters.ui,
PartDesignGui::TaskChamferParameters.ui,
PartDesignGui::TaskDraftParameters.ui,
[PartDesignGui::TaskExtrudeParameters.ui](../../d7/d0a/classPartDesignGui_1_1TaskExtrudeParameters.html#a78cccdb902e3484740bcf341a592927a),
PartDesignGui::TaskFeaturePick.ui, PartDesignGui::TaskFilletParameters.ui,
PartDesignGui::TaskHelixParameters.ui, PartDesignGui::TaskHoleParameters.ui,
PartDesignGui::TaskLinearPatternParameters.ui,
PartDesignGui::TaskLoftParameters.ui,
PartDesignGui::TaskMirroredParameters.ui,
PartDesignGui::TaskMultiTransformParameters.ui,
PartDesignGui::TaskPipeParameters.ui, PartDesignGui::TaskPipeOrientation.ui,
PartDesignGui::TaskPipeScaling.ui,
PartDesignGui::TaskPolarPatternParameters.ui,
PartDesignGui::TaskBoxPrimitives.ui,
PartDesignGui::TaskRevolutionParameters.ui,
PartDesignGui::TaskScaledParameters.ui, PartDesignGui::TaskShapeBinder.ui,
PartDesignGui::TaskThicknessParameters.ui,
PartDesignGui::TaskTransformedMessages.ui, PathGui::DlgProcessorChooser.ui,
PathGui::DlgSettingsPathColor.ui, PathGui::TaskWidgetPathCompound.ui,
PointsGui::DlgPointsReadImp.ui, RaytracingGui::DlgSettingsRayImp.ui,
[ReenGui::FitBSplineSurfaceWidget::Private.ui](../../d8/d89/classFitBSplineSurfaceWidget_1_1Private.html#ac4b138eb3a67fbf8beb3320eb6086a71),
[ReenGui::PoissonWidget::Private.ui](../../d7/d0a/classPoissonWidget_1_1Private.html#a8b694ce06544bd6e6ccfb6ddaba4915e),
ReverseEngineeringGui::Segmentation.ui,
ReverseEngineeringGui::SegmentationManual.ui,
RobotGui::TaskEdge2TracParameter.ui, RobotGui::TaskRobot6Axis.ui,
RobotGui::TaskRobotControl.ui, RobotGui::TaskRobotMessages.ui,
RobotGui::TaskTrajectory.ui, RobotGui::TaskTrajectoryDressUpParameter.ui,
RobotGui::TrajectorySimulate.ui, SketcherGui::ConstraintMultiFilterDialog.ui,
SketcherGui::ConstraintSettingsDialog.ui,
SketcherGui::SketcherRegularPolygonDialog.ui,
SketcherGui::SketcherSettings.ui, SketcherGui::SketcherSettingsDisplay.ui,
SketcherGui::SketcherSettingsColors.ui, SketcherGui::SketchMirrorDialog.ui,
SketcherGui::SketchOrientationDialog.ui,
SketcherGui::SketchRectangularArrayDialog.ui,
SketcherGui::TaskSketcherConstraints.ui, SketcherGui::TaskSketcherElements.ui,
SketcherGui::SketcherGeneralWidget.ui, SketcherGui::TaskSketcherMessages.ui,
SketcherGui::TaskSketcherSolverAdvanced.ui,
SketcherGui::SketcherValidation.ui, SpreadsheetGui::DlgBindSheet.ui,
SpreadsheetGui::DlgSettingsImp.ui, SpreadsheetGui::DlgSheetConf.ui,
SpreadsheetGui::PropertiesDialog.ui,
[SpreadsheetGui::SheetView.ui](../../d0/d67/classSpreadsheetGui_1_1SheetView.html#aab1581966f4675481db605bd0ea9f3c6),
StartGui::DlgStartPreferencesImp.ui, SurfaceGui::FillingPanel.ui,
SurfaceGui::FillingEdgePanel.ui, SurfaceGui::FillingVertexPanel.ui,
SurfaceGui::GeomFillSurface.ui, SurfaceGui::SectionsPanel.ui,
TechDrawGui::DlgPageChooser.ui, TechDrawGui::DlgPrefsTechDrawAdvancedImp.ui,
TechDrawGui::DlgPrefsTechDrawAnnotationImp.ui,
TechDrawGui::DlgPrefsTechDrawColorsImp.ui,
TechDrawGui::DlgPrefsTechDrawDimensionsImp.ui,
TechDrawGui::DlgPrefsTechDrawGeneralImp.ui,
TechDrawGui::DlgPrefsTechDrawHLRImp.ui,
TechDrawGui::DlgPrefsTechDrawScaleImp.ui, TechDrawGui::DlgTemplateField.ui,
TechDrawGui::SymbolChooser.ui, TechDrawGui::TaskActiveView.ui,
TechDrawGui::TaskAlignViews.ui, TechDrawGui::TaskBalloon.ui,
TechDrawGui::TaskCenterLine.ui, TechDrawGui::TaskCosmeticLine.ui,
TechDrawGui::TaskCosVertex.ui, TechDrawGui::TaskCustomizeFormat.ui,
TechDrawGui::TaskDetail.ui, TechDrawGui::TaskDimension.ui,
TechDrawGui::TaskGeomHatch.ui, TechDrawGui::TaskHatch.ui,
TechDrawGui::TaskLeaderLine.ui, TechDrawGui::TaskLineDecor.ui,
TechDrawGui::TaskRestoreLines.ui, TechDrawGui::TaskLinkDim.ui,
TechDrawGui::TaskProjection.ui, TechDrawGui::TaskProjGroup.ui,
TechDrawGui::TaskRichAnno.ui, TechDrawGui::TaskSectionView.ui,
TechDrawGui::TaskSelectLineAttributes.ui, TechDrawGui::TaskWeldingSymbol.ui,
[TechDrawTools.CommandMoveView.CommandMoveView.ui](../../dd/d52/classTechDrawTools_1_1CommandMoveView_1_1CommandMoveView.html#a18b58c0d4883fadfe5fc6ad7dbb517d5),
[TechDrawTools.CommandShareView.CommandShareView.ui](../../de/d84/classTechDrawTools_1_1CommandShareView_1_1CommandShareView.html#a2f406250966c67b1018c4c176c061af7),
[TaskPanel.TaskPanel.ui](../../d3/da6/classTaskPanel_1_1TaskPanel.html#a282ea65bcb4dc553d7ec0cb8b116f328),
and TestGui::UnitTestDialog.ui.

Referenced by
[change_branch.ChangeBranchDialog.exec()](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a6c58ac15929c71fac630a9462df2004c).

## Member Data Documentation

## ◆ branch_changed

| change_branch.ChangeBranchDialog.branch_changed =
QtCore.Signal([str](../../d9/d36/classstr.html))  
---  
static  
  
Referenced by
[package_details.PackageDetails.change_branch_clicked()](../../d1/df5/classpackage__details_1_1PackageDetails.html#afd7c8de0e903b89492fae61e6b22d418),
and
[change_branch.ChangeBranchDialog.exec()](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a6c58ac15929c71fac630a9462df2004c).

## ◆ item_filter

change_branch.ChangeBranchDialog.item_filter  
---  
  
Referenced by
[change_branch.ChangeBranchDialog.exec()](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a6c58ac15929c71fac630a9462df2004c),
[package_list.PackageList.on_listPackages_clicked()](../../d8/d41/classpackage__list_1_1PackageList.html#a54fa96e2d947c6aea2e6ec176cca7fc9),
[package_list.PackageList.update_status_filter()](../../d8/d41/classpackage__list_1_1PackageList.html#a167a6f1df99102afb965bab4ad885705),
[package_list.PackageList.update_text_filter()](../../d8/d41/classpackage__list_1_1PackageList.html#a4355d30f250ee94174c95a51bbffe8cc),
and
[package_list.PackageList.update_type_filter()](../../d8/d41/classpackage__list_1_1PackageList.html#a3fde795d3e7e6375ccd5568e94c32b39).

## ◆ item_model

change_branch.ChangeBranchDialog.item_model  
---  
  
Referenced by
[AddonManager.CommandAddonManager.add_addon_repo()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a0128d399282eb71e55417bf8ef4ec946),
[AddonManager.CommandAddonManager.append_to_repos_list()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a34106546e723a43de9e286223474904e),
[AddonManager.CommandAddonManager.dependency_dialog_yes_clicked()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a24130c49cbb70c64796e0327923b9396),
[change_branch.ChangeBranchDialog.exec()](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a6c58ac15929c71fac630a9462df2004c),
[AddonManager.CommandAddonManager.mark_repo_update_available()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a670656464d505dcab469a2f1bd7de259),
[package_list.PackageList.on_listPackages_clicked()](../../d8/d41/classpackage__list_1_1PackageList.html#a54fa96e2d947c6aea2e6ec176cca7fc9),
[AddonManager.CommandAddonManager.on_package_installed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#abf1dbc5ed9bc3918e6f96dda28954770),
[AddonManager.CommandAddonManager.on_package_updated()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ae31bf139686923b617a182aeb1588425),
[AddonManager.CommandAddonManager.on_update_all_completed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a1fa2c3ccb5f70dcb1d20df00bbb40982),
[AddonManager.CommandAddonManager.populate_packages_table()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#adcc9afd53c106b8a724792bf17943fe3),
[AddonManager.CommandAddonManager.reject()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aef345e1dbcc980bf3d435f6c365905ca),
[AddonManager.CommandAddonManager.remove()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aae7cdf308d96b87d195e7be2de765a00),
[AddonManager.CommandAddonManager.resolve_dependencies()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a61c2eb1ed8627176ccd7b098754dbb18),
[AddonManager.CommandAddonManager.select_addon()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa632e875b2d90517423d4e47fa60a263),
[package_list.PackageList.set_view_style()](../../d8/d41/classpackage__list_1_1PackageList.html#ac8e3ffc5c454dd0f8df710ed32866696),
[AddonManager.CommandAddonManager.status_updated()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a34e713179c4b82c43c5228dcc3a5edab),
and
[AddonManager.CommandAddonManager.validate()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a3b5bdb4d937ff0f22e82fa180bb5ed2e).

## ◆ ui

change_branch.ChangeBranchDialog.ui  
---  
  
Referenced by
[draftguitools.gui_beziers.BezCurve.action()](../../d2/dce/classdraftguitools_1_1gui__beziers_1_1BezCurve.html#ae90c7f6298d0843cb57ac2f622639277),
[draftguitools.gui_dimensions.Dimension.action()](../../d5/d6a/classdraftguitools_1_1gui__dimensions_1_1Dimension.html#a96494d2774d1c1c9b0973c27fa7e37d2),
[draftguitools.gui_ellipses.Ellipse.action()](../../db/d98/classdraftguitools_1_1gui__ellipses_1_1Ellipse.html#ae469c3dfd4f33dbd563751a8d988ca2c),
[draftguitools.gui_labels.Label.action()](../../d4/d3a/classdraftguitools_1_1gui__labels_1_1Label.html#a31d95b9c0428e8e5e2fc2c0e5ba1f9cf),
[draftguitools.gui_lines.Line.action()](../../da/d8f/classdraftguitools_1_1gui__lines_1_1Line.html#a94d8909150460a1530cac08b2c731cac),
[draftguitools.gui_mirror.Mirror.action()](../../d8/dbd/classdraftguitools_1_1gui__mirror_1_1Mirror.html#a0477abe6224797c04d876c422f644e88),
[draftguitools.gui_offset.Offset.action()](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#af6fe1d529ed82fe117bb430a75844ec5),
[draftguitools.gui_rectangles.Rectangle.action()](../../dd/d46/classdraftguitools_1_1gui__rectangles_1_1Rectangle.html#ab25370f0a95da297c1262044828da6a6),
[draftguitools.gui_shapestrings.ShapeString.action()](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#ae360211d72d5b65f4af72aea37cc4250),
[draftguitools.gui_splines.BSpline.action()](../../d1/d3f/classdraftguitools_1_1gui__splines_1_1BSpline.html#adca6c9978608bdf13b653cfa58ea2eab),
[draftguitools.gui_texts.Text.action()](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a26b33ab0c572145b63b6666e2016ff18),
[draftguitools.gui_arcs.Arc.Activated()](../../da/d4f/classdraftguitools_1_1gui__arcs_1_1Arc.html#ab7c70926ad95129a06d6aa52bcc34309),
[draftguitools.gui_circulararray.CircularArray.Activated()](../../dc/dd7/classdraftguitools_1_1gui__circulararray_1_1CircularArray.html#add24faedacfd2c2ad7f159032c044931),
[draftguitools.gui_clone.Clone.Activated()](../../df/d67/classdraftguitools_1_1gui__clone_1_1Clone.html#addc877a683b0c3c3861ff0793a3d973b),
[draftguitools.gui_downgrade.Downgrade.Activated()](../../de/d8b/classdraftguitools_1_1gui__downgrade_1_1Downgrade.html#a724c3827c15d821dde302e9bdf2fba25),
[draftguitools.gui_draft2sketch.Draft2Sketch.Activated()](../../dd/d7c/classdraftguitools_1_1gui__draft2sketch_1_1Draft2Sketch.html#a5c70d486873c26b45a12bd6adf296b1a),
[draftguitools.gui_ellipses.Ellipse.Activated()](../../db/d98/classdraftguitools_1_1gui__ellipses_1_1Ellipse.html#aa9bbf52c8fbe9080ab25f4db93d0a8db),
[draftguitools.gui_facebinders.Facebinder.Activated()](../../da/dc9/classdraftguitools_1_1gui__facebinders_1_1Facebinder.html#a40b08b9d18731931aac3f121c9c140b8),
[draftguitools.gui_join.Join.Activated()](../../d4/d50/classdraftguitools_1_1gui__join_1_1Join.html#a232ea198987b6ed19b57255408f2e9d4),
[draftguitools.gui_move.Move.Activated()](../../d2/df5/classdraftguitools_1_1gui__move_1_1Move.html#a8a8ca9b914e02c71f4a9530b6f82f8c0),
[draftguitools.gui_orthoarray.OrthoArray.Activated()](../../dc/d0f/classdraftguitools_1_1gui__orthoarray_1_1OrthoArray.html#a2c082714ec66ef3b1f8195c1ac964846),
[draftguitools.gui_polararray.PolarArray.Activated()](../../dd/dc9/classdraftguitools_1_1gui__polararray_1_1PolarArray.html#acc402dde8d5c1b007e3ac33f06340df6),
[draftguitools.gui_polygons.Polygon.Activated()](../../df/d3d/classdraftguitools_1_1gui__polygons_1_1Polygon.html#a0a265363effba04f7d57678d77ead1c5),
[draftguitools.gui_rectangles.Rectangle.Activated()](../../dd/d46/classdraftguitools_1_1gui__rectangles_1_1Rectangle.html#a33116d563b8e2e63b9611de7b5978f80),
[draftguitools.gui_rotate.Rotate.Activated()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#a05285f7eb37a8609cf45b8a0a571b0f3),
[draftguitools.gui_scale.Scale.Activated()](../../d5/d4f/classdraftguitools_1_1gui__scale_1_1Scale.html#a4ef892d2aa173b239100693df6da2402),
[draftguitools.gui_shape2dview.Shape2DView.Activated()](../../d5/d96/classdraftguitools_1_1gui__shape2dview_1_1Shape2DView.html#acbdcbafc208af6c024f899c90239b79a),
[draftguitools.gui_shapestrings.ShapeString.Activated()](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#a4431a6731cbd4339eed1b96c017d6c9a),
[draftguitools.gui_split.Split.Activated()](../../db/d21/classdraftguitools_1_1gui__split_1_1Split.html#a7872ad5cd9031bb89498067eaa10321c),
[draftguitools.gui_styles.ApplyStyle.Activated()](../../d6/d90/classdraftguitools_1_1gui__styles_1_1ApplyStyle.html#a4203bafacf18db241693dc4d3bb1885c),
[draftguitools.gui_texts.Text.Activated()](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a3b5036e41120c03e82e1cc1a1de16a1d),
[draftguitools.gui_upgrade.Upgrade.Activated()](../../d2/dd7/classdraftguitools_1_1gui__upgrade_1_1Upgrade.html#a22679466e33d9185873405db23107116),
[draftguitools.gui_array_simple.Array.Activated()](../../da/d0e/classdraftguitools_1_1gui__array__simple_1_1Array.html#a0d39a890eaccfb43bae967e3d3a80eda),
[draftguitools.gui_fillets.Fillet.Activated()](../../da/d40/classdraftguitools_1_1gui__fillets_1_1Fillet.html#af67b23b90312ec91aff8c0429f57f0f0),
[draftguitools.gui_stretch.Stretch.addPoint()](../../df/d6e/classdraftguitools_1_1gui__stretch_1_1Stretch.html#ab36c5bf4469339485cbc9b87007a7b52),
[draftguitools.gui_ellipses.Ellipse.appendPoint()](../../db/d98/classdraftguitools_1_1gui__ellipses_1_1Ellipse.html#a1f25a3825200b9e455c77599c7038c45),
[draftguitools.gui_rectangles.Rectangle.appendPoint()](../../dd/d46/classdraftguitools_1_1gui__rectangles_1_1Rectangle.html#a08cfba15893201d2bc537f22332969ed),
[package_details.PackageDetails.branch_changed()](../../d1/df5/classpackage__details_1_1PackageDetails.html#a15328dbccbc762df726cf1fe9264cb5c),
[DraftGui.DraftToolBar.changeEvent()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a37e1c36c517d5d189cce0a13e3005851),
[draftguitools.gui_circulararray.CircularArray.click()](../../dc/dd7/classdraftguitools_1_1gui__circulararray_1_1CircularArray.html#acb60db675f996c559548328a691ac458),
[draftguitools.gui_orthoarray.OrthoArray.click()](../../dc/d0f/classdraftguitools_1_1gui__orthoarray_1_1OrthoArray.html#a3a77bfd8c7066e96b5d5d6719b8f4757),
[draftguitools.gui_polararray.PolarArray.click()](../../dd/dc9/classdraftguitools_1_1gui__polararray_1_1PolarArray.html#a9da378b54e97a057039765e7e1f9c152),
[draftguitools.gui_dimensions.Dimension.createObject()](../../d5/d6a/classdraftguitools_1_1gui__dimensions_1_1Dimension.html#af10155d140aeeaa88c232b874c86c07f),
[package_details.PackageDetails.disable_clicked()](../../d1/df5/classpackage__details_1_1PackageDetails.html#a0b127e8433a9db40523d10257c612dd3),
[package_details.PackageDetails.display_repo_status()](../../d1/df5/classpackage__details_1_1PackageDetails.html#abafff14948ac22d38fe00e5cf8110900),
[draftguitools.gui_polygons.Polygon.drawPolygon()](../../df/d3d/classdraftguitools_1_1gui__polygons_1_1Polygon.html#a8f4ddb1f0ebe6e684173a9b6c60c700c),
[package_details.PackageDetails.enable_clicked()](../../d1/df5/classpackage__details_1_1PackageDetails.html#a9633078163d737ff02767885299c4b13),
[draftguitools.gui_edit.Edit.endEditing()](../../d8/d68/classdraftguitools_1_1gui__edit_1_1Edit.html#ab9797631ba43c7855016e2552c21834f),
[change_branch.ChangeBranchDialog.exec()](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a6c58ac15929c71fac630a9462df2004c),
[draftguitools.gui_base_original.DraftTool.finish()](../../da/d09/classdraftguitools_1_1gui__base__original_1_1DraftTool.html#a4da73a24591b23ecab869d41bef6de95),
[draftguitools.gui_fillets.Fillet.finish()](../../da/d40/classdraftguitools_1_1gui__fillets_1_1Fillet.html#a6b8e06e5a26d68509b050c212ec0685f),
[draftguitools.gui_dimensions.Dimension.finish()](../../d5/d6a/classdraftguitools_1_1gui__dimensions_1_1Dimension.html#a45a9678355d3608296dc03d7d993c0a2),
[draftguitools.gui_edit.Edit.finish()](../../d8/d68/classdraftguitools_1_1gui__edit_1_1Edit.html#a8d8bc8079f6beae1158a282fe64a9f02),
[draftguitools.gui_trimex.Trimex.finish()](../../da/df7/classdraftguitools_1_1gui__trimex_1_1Trimex.html#ad394c0738be99c19146ee3555d4d016d),
[draftguitools.gui_arcs.Arc.finish()](../../da/d4f/classdraftguitools_1_1gui__arcs_1_1Arc.html#a2262d966a879bfa9b71d9c699e6929b2),
[draftguitools.gui_beziers.BezCurve.finish()](../../d2/dce/classdraftguitools_1_1gui__beziers_1_1BezCurve.html#a6b4598d09cb7c1f0b06fe1b96cc9096f),
[draftguitools.gui_beziers.CubicBezCurve.finish()](../../de/d5e/classdraftguitools_1_1gui__beziers_1_1CubicBezCurve.html#abadcbdae43b1e54d516d249c71fc0991),
[draftguitools.gui_ellipses.Ellipse.finish()](../../db/d98/classdraftguitools_1_1gui__ellipses_1_1Ellipse.html#aa534628f13f8ad6effacb1fcbd76bb2a),
[draftguitools.gui_lines.Line.finish()](../../da/d8f/classdraftguitools_1_1gui__lines_1_1Line.html#a622af4e1166f892f860b86d3d1e3f053),
[draftguitools.gui_mirror.Mirror.finish()](../../d8/dbd/classdraftguitools_1_1gui__mirror_1_1Mirror.html#a73d8f0dba4d186590485bf972fa8e25d),
[draftguitools.gui_move.Move.finish()](../../d2/df5/classdraftguitools_1_1gui__move_1_1Move.html#aa2c8c371106351f316c238f67bf7accf),
[draftguitools.gui_polygons.Polygon.finish()](../../df/d3d/classdraftguitools_1_1gui__polygons_1_1Polygon.html#a06317245940b6d99d62b0823d657dcb2),
[draftguitools.gui_rectangles.Rectangle.finish()](../../dd/d46/classdraftguitools_1_1gui__rectangles_1_1Rectangle.html#a7ba174f4093affb5af55e58c804a527d),
[draftguitools.gui_rotate.Rotate.finish()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#ad60faae5b86f1d2c74f045c2291ae6dd),
[draftguitools.gui_splines.BSpline.finish()](../../d1/d3f/classdraftguitools_1_1gui__splines_1_1BSpline.html#ab00ba1111a2b9d2afcee43a0396a4cd5),
[draftguitools.gui_texts.Text.finish()](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a3fe64be64c77319af1f265609dd8e985),
[draftguitools.gui_points.Point.finish()](../../d7/dc7/classdraftguitools_1_1gui__points_1_1Point.html#ac55499c15db7b01680f41b3f3dd32477),
[draftguitools.gui_shapestrings.ShapeString.finish()](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#af7a14bf7135177bc521cfa7a9123b2bf),
[draftguitools.gui_move.Move.get_object_selection()](../../d2/df5/classdraftguitools_1_1gui__move_1_1Move.html#aaa0ddbc10aa3d9357af8e20f25f1680c),
[draftguitools.gui_rotate.Rotate.get_object_selection()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#a425b0a53b493b1349a5adc9bdbc31b26),
[draftguitools.gui_scale.Scale.get_object_selection()](../../d5/d4f/classdraftguitools_1_1gui__scale_1_1Scale.html#a984cbcfe94c35486ceb0cc809ff80d36),
[draftguitools.gui_subelements.SubelementHighlight.get_selection()](../../d4/db2/classdraftguitools_1_1gui__subelements_1_1SubelementHighlight.html#a46717a3c64adaecee289a36c9373b5a6),
[draftguitools.gui_base_original.DraftTool.getStrings()](../../da/d09/classdraftguitools_1_1gui__base__original_1_1DraftTool.html#a940881c2458a5ec52c3e7eda58a7296d),
[draftguitools.gui_move.Move.handle_mouse_click_event()](../../d2/df5/classdraftguitools_1_1gui__move_1_1Move.html#a8b258f5688f4f8c4e8d2123de6613f3c),
[package_details.PackageDetails.load_finished()](../../d1/df5/classpackage__details_1_1PackageDetails.html#a43e55b5608760e77db97297548034965),
[package_details.PackageDetails.load_progress()](../../d1/df5/classpackage__details_1_1PackageDetails.html#ae6d0af778d39f8e1b117ea0db66b74ea),
[package_details.PackageDetails.load_started()](../../d1/df5/classpackage__details_1_1PackageDetails.html#a79bd0070ebec9ff3c1b872b9d43abe42),
[package_details.PackageDetails.long_load_running()](../../d1/df5/classpackage__details_1_1PackageDetails.html#a3980a45e74b723ae671e379d41557230),
[package_details.PackageDetails.macro_readme_updated()](../../d1/df5/classpackage__details_1_1PackageDetails.html#adaec13a0b56c829e2f4fd5018d49dc5e),
[draftguitools.gui_circulararray.CircularArray.move()](../../dc/dd7/classdraftguitools_1_1gui__circulararray_1_1CircularArray.html#a3bd54671d6a7a903ce9c014d25c16b0f),
[draftguitools.gui_points.Point.move()](../../d7/dc7/classdraftguitools_1_1gui__points_1_1Point.html#a7f79ff750e8f51f9e886e5a7cdc968b0),
[draftguitools.gui_polararray.PolarArray.move()](../../dd/dc9/classdraftguitools_1_1gui__polararray_1_1PolarArray.html#a25cc4c7e5764e70d07adb146880bdb6d),
[draftguitools.gui_move.Move.move()](../../d2/df5/classdraftguitools_1_1gui__move_1_1Move.html#af3e504a851692b629dc3af82f8b1dba9),
[draftguitools.gui_arcs.Arc.numericInput()](../../da/d4f/classdraftguitools_1_1gui__arcs_1_1Arc.html#ad04454872b35387d6865f50512d4c188),
[draftguitools.gui_polygons.Polygon.numericInput()](../../df/d3d/classdraftguitools_1_1gui__polygons_1_1Polygon.html#a62df321b9b6cb28a53ccf047a4157f6c),
[draftguitools.gui_rotate.Rotate.numericInput()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#a203b15586f8f247ed4ca23937528781c),
[draftguitools.gui_shapestrings.ShapeString.numericInput()](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#aa7ace5ed4fbd7e74568ed62da36a517f),
[draftguitools.gui_arcs.Arc.numericRadius()](../../da/d4f/classdraftguitools_1_1gui__arcs_1_1Arc.html#a3a55830e1e08f60be95ed81d73759e52),
[draftguitools.gui_offset.Offset.numericRadius()](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#ae08617dcd80297f9e33139b0cfb5589f),
[draftguitools.gui_rotate.Rotate.numericRadius()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#a9233be8153158528af33797d19c7dffd),
[draftguitools.gui_edit.Edit.proceed()](../../d8/d68/classdraftguitools_1_1gui__edit_1_1Edit.html#acbed8eb20e1258f73052eaf88b5fdc65),
[draftguitools.gui_groups.AddToGroup.proceed()](../../d8/d83/classdraftguitools_1_1gui__groups_1_1AddToGroup.html#a593a469720294390952479a7fed88727),
[draftguitools.gui_groups.SetAutoGroup.proceed()](../../d4/df8/classdraftguitools_1_1gui__groups_1_1SetAutoGroup.html#a9387cd4530b72b25f12a2da87e619bdb),
[draftguitools.gui_rotate.Rotate.rotate()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#a1a517fdbb53236b19c394e7007230f24),
[package_details.PackageDetails.run_javascript()](../../d1/df5/classpackage__details_1_1PackageDetails.html#a8d9e49bc7a738114e7552003f1ac2434),
[draftguitools.gui_fillets.Fillet.set_chamfer()](../../da/d40/classdraftguitools_1_1gui__fillets_1_1Fillet.html#acd0cca7ffd604780d42294f890db69b5),
[package_details.PackageDetails.set_change_branch_button_state()](../../d1/df5/classpackage__details_1_1PackageDetails.html#aef7177bce5cd10a353851f12a8eedb45),
[draftguitools.gui_fillets.Fillet.set_delete()](../../da/d40/classdraftguitools_1_1gui__fillets_1_1Fillet.html#ab51feb62bde0663c96b48fd72273511c),
[package_details.PackageDetails.set_disable_button_state()](../../d1/df5/classpackage__details_1_1PackageDetails.html#a3bbe5faf55f51f98c78ce43e0501cf02),
[draftguitools.gui_move.Move.set_ghosts()](../../d2/df5/classdraftguitools_1_1gui__move_1_1Move.html#a66c83007e6ed8445314b8cff528c2c4c),
[draftguitools.gui_rotate.Rotate.set_ghosts()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#a5a1e208298860f47ec960ff1096d6e89),
[draftguitools.gui_rotate.Rotate.set_start_point()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#af7f9d3d7f68c7488e0ca108234d0cf45),
[package_list.PackageList.set_view_style()](../../d8/d41/classpackage__list_1_1PackageList.html#ac8e3ffc5c454dd0f8df710ed32866696),
[package_details.PackageDetails.show_error_for()](../../d1/df5/classpackage__details_1_1PackageDetails.html#a45df925f5fdc2d0a49e12d402e167fdf),
[package_details.PackageDetails.show_package()](../../d1/df5/classpackage__details_1_1PackageDetails.html#a23a2e237f2ae2733d8016598b07e8a89),
[package_details.PackageDetails.show_repo()](../../d1/df5/classpackage__details_1_1PackageDetails.html#aae7b13ab2d26ff73d55732b868b71edf),
[package_details.PackageDetails.show_workbench()](../../d1/df5/classpackage__details_1_1PackageDetails.html#a570cb029dbcf3738c91d98dce9e10e4e),
[draftguitools.gui_edit.Edit.startEditing()](../../d8/d68/classdraftguitools_1_1gui__edit_1_1Edit.html#a995694cb17bcc6deed985956c2e96429),
[package_list.PackageList.update_text_filter()](../../d8/d41/classpackage__list_1_1PackageList.html#a4355d30f250ee94174c95a51bbffe8cc),
and
[draftguitools.gui_edit.Edit.updateTrackerAndGhost()](../../d8/d68/classdraftguitools_1_1gui__edit_1_1Edit.html#a665078311363dae81f241e1cb5a16021).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/AddonManager/change_branch.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

