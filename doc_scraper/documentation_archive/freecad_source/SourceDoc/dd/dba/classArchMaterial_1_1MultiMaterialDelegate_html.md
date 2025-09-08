---
url: https://freecad.github.io/SourceDoc/dd/dba/classArchMaterial_1_1MultiMaterialDelegate.html
scraped_at: 2025-09-08T14:57:57.274098
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ArchMaterial](../../dc/d52/namespaceArchMaterial.html)
  * [MultiMaterialDelegate](../../dd/dba/classArchMaterial_1_1MultiMaterialDelegate.html)

[List of all members](../../da/de1/classArchMaterial_1_1MultiMaterialDelegate-members.html) | Public Member Functions | Public Attributes

ArchMaterial.MultiMaterialDelegate Class Reference

##  Public Member Functions  
  
---  
def | [createEditor](../../dd/dba/classArchMaterial_1_1MultiMaterialDelegate.html#a74b9f239ff9a0c99e42192d19c9c5550) (self, parent, option, index)  
def | [setEditorData](../../dd/dba/classArchMaterial_1_1MultiMaterialDelegate.html#a75d5a15afd46efb694039ed6653ff181) (self, editor, index)  
def | [setModelData](../../dd/dba/classArchMaterial_1_1MultiMaterialDelegate.html#aa36ee69be80adc06480436ec7883804e) (self, editor, model, index)  
  
##  Public Attributes  
  
---  
|
[mats](../../dd/dba/classArchMaterial_1_1MultiMaterialDelegate.html#ae387a9a2f36ded662503190caa9f41b0)  
  
## Member Function Documentation

## ◆ createEditor()

def ArchMaterial.MultiMaterialDelegate.createEditor  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _parent_ ,   
|  |  | _option_ ,   
|  |  | _index_  
| ) | |   
  
## ◆ setEditorData()

def ArchMaterial.MultiMaterialDelegate.setEditorData  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _editor_ ,   
|  |  | _index_  
| ) | |   
  
References
[ArchMaterial.MultiMaterialDelegate.mats](../../dd/dba/classArchMaterial_1_1MultiMaterialDelegate.html#ae387a9a2f36ded662503190caa9f41b0).

## ◆ setModelData()

def ArchMaterial.MultiMaterialDelegate.setModelData  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _editor_ ,   
|  |  | _model_ ,   
|  |  | _index_  
| ) | |   
  
References ArchMaterial._ArchMultiMaterialTaskPanel.addLayer(),
ArchMaterial._ArchMultiMaterialTaskPanel.delLayer(),
ArchMaterial._ArchMultiMaterialTaskPanel.downLayer(),
ArchMaterial._ArchMaterialTaskPanel.existingmaterials,
ArchMaterial._ArchMultiMaterialTaskPanel.existingmaterials,
ArchMaterial._ArchMultiMaterialTaskPanel.fillData(),
ArchMaterial._ArchMaterialTaskPanel.fillExistingCombo(),
ArchMaterial._ArchMultiMaterialTaskPanel.fillExistingCombo(),
Gui::Dialog::PreferenceUiForm.form, ArchAxis._AxisTaskPanel.form,
[ArchAxisSystem.AxisSystemTaskPanel.form](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a2fa174aff9231042a55ce1040b332fe3),
[ArchCommands.SurveyTaskPanel.form](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a04804d6ea774adf44c626845ca1dcfb5),
[ArchComponent.ComponentTaskPanel.form](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#aaf2bc01991b6d99d8fecad2baaa7b159),
ArchCutPlane._CutPlaneTaskPanel.form,
[ArchGrid.ArchGridTaskPanel.form](../../d6/da7/classArchGrid_1_1ArchGridTaskPanel.html#a5bee5c5b381c514f05a7ec6eb74cc3c6),
[ArchIFCView.IfcContextUI.form](../../d6/d87/classArchIFCView_1_1IfcContextUI.html#ad108e6311176002bd116cffc0c985d97),
ArchMaterial._ArchMaterialTaskPanel.form,
ArchMaterial._ArchMultiMaterialTaskPanel.form,
[ArchPanel.SheetTaskPanel.form](../../dd/d0f/classArchPanel_1_1SheetTaskPanel.html#a8c30c1ad2d8a131e7ba3d4a6721dc304),
[ArchPanel.NestTaskPanel.form](../../da/d77/classArchPanel_1_1NestTaskPanel.html#ae3c3e5375b7c9c4420cb941a3f48c68c),
ArchPrecast._PrecastTaskPanel.form, ArchPrecast._DentsTaskPanel.form,
[ArchProfile.ProfileTaskPanel.form](../../dc/d9a/classArchProfile_1_1ProfileTaskPanel.html#a024dcb41ada370aae9c28813536b0310),
[ArchReference.ArchReferenceTaskPanel.form](../../d4/d73/classArchReference_1_1ArchReferenceTaskPanel.html#a16d9fea5b357215069bd9a862fb901b8),
ArchRoof._RoofTaskPanel.form,
[ArchSchedule.ArchScheduleTaskPanel.form](../../d5/da0/classArchSchedule_1_1ArchScheduleTaskPanel.html#a42c7a29edf2636798f1ddc5e2d5bdf48),
[ArchSectionPlane.SectionPlaneTaskPanel.form](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#ad93a0ec877dad72c4367f375b3397cee),
[ArchStructure.StructureTaskPanel.form](../../df/d40/classArchStructure_1_1StructureTaskPanel.html#a3932f7f746233bc68fee65f5931fc2d9),
ArchWindow._ArchWindowTaskPanel.form,
[DraftGui.DraftTaskPanel.form](../../db/db0/classDraftGui_1_1DraftTaskPanel.html#a8f3f3ea8dd157e9d6ab7481de227bf02),
[DraftGui.DraftToolBar.form](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a1837fdf360284245ed5dacc76f4dd080),
[DraftGui.FacebinderTaskPanel.form](../../d2/d61/classDraftGui_1_1FacebinderTaskPanel.html#a888254409780af1f13e607a0227ff0b4),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.form](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#a9d9805d63ef1ffc6a389e72eec26389d),
[draftguitools.gui_groups.Ui_AddNamedGroup.form](../../d3/df7/classdraftguitools_1_1gui__groups_1_1Ui__AddNamedGroup.html#abd5ef445cb6edc28f03d3b970b2a9945),
[draftguitools.gui_hatch.Draft_Hatch_TaskPanel.form](../../d1/d6e/classdraftguitools_1_1gui__hatch_1_1Draft__Hatch__TaskPanel.html#a43b9dcecc4c2eea539346d0b6c3423c1),
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel.form](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#a4a75028c11a01da1efbaffcacfacf641),
[drafttaskpanels.task_circulararray.TaskPanelCircularArray.form](../../dd/d3a/classdrafttaskpanels_1_1task__circulararray_1_1TaskPanelCircularArray.html#a51a1be96300f26aed459d1c3c4069824),
[drafttaskpanels.task_orthoarray.TaskPanelOrthoArray.form](../../d6/dfa/classdrafttaskpanels_1_1task__orthoarray_1_1TaskPanelOrthoArray.html#af5b3defb2165bc00010cf95b59f80db4),
[drafttaskpanels.task_polararray.TaskPanelPolarArray.form](../../d7/d8d/classdrafttaskpanels_1_1task__polararray_1_1TaskPanelPolarArray.html#a0d721f3610eb099f594a72856782544a),
[drafttaskpanels.task_scale.ScaleTaskPanel.form](../../df/d70/classdrafttaskpanels_1_1task__scale_1_1ScaleTaskPanel.html#a156aa13308e47762ae9158c36bfda49f),
[drafttaskpanels.task_selectplane.SelectPlaneTaskPanel.form](../../d5/ddd/classdrafttaskpanels_1_1task__selectplane_1_1SelectPlaneTaskPanel.html#a72277071479843fea2d90d17b2cee3dc),
[drafttaskpanels.task_shapestring.ShapeStringTaskPanel.form](../../d9/d1e/classdrafttaskpanels_1_1task__shapestring_1_1ShapeStringTaskPanel.html#a1b09fa4fb69fb3a575bfce69f554ce5d),
[feminout.importFenicsMesh.WriteXDMFTaskPanel.form](../../d4/d1a/classfeminout_1_1importFenicsMesh_1_1WriteXDMFTaskPanel.html#a94f5f6955928ff1a9fde5e9f1e1bc7e0),
femsolver.elmer.equations.equation._TaskPanel.form,
[femsolver.solver_taskpanel.ControlTaskPanel.form](../../de/d8f/classfemsolver_1_1solver__taskpanel_1_1ControlTaskPanel.html#aaff8cc3931907cc7fea0a6b2a3396853),
[femtaskpanels.task_constraint_centrif._TaskPanel.form](../../de/da6/classfemtaskpanels_1_1task__constraint__centrif_1_1__TaskPanel.html#a4654fd44978aa549cf11cd8cd6ed708a),
[femtaskpanels.task_constraint_electrostaticpotential._TaskPanel.form](../../d6/de9/classfemtaskpanels_1_1task__constraint__electrostaticpotential_1_1__TaskPanel.html#a35041f41bcb574d8316582ced4c9ecd5),
[femtaskpanels.task_constraint_flowvelocity._TaskPanel.form](../../d3/da8/classfemtaskpanels_1_1task__constraint__flowvelocity_1_1__TaskPanel.html#af01946386b72380d8c9a099d0c04a5ed),
[femtaskpanels.task_constraint_initialflowvelocity._TaskPanel.form](../../d5/d77/classfemtaskpanels_1_1task__constraint__initialflowvelocity_1_1__TaskPanel.html#af42299d7dbe4f7ebe223c9286f5f40ed),
[femtaskpanels.task_constraint_sectionprint._TaskPanel.form](../../da/d77/classfemtaskpanels_1_1task__constraint__sectionprint_1_1__TaskPanel.html#ad30e7ba003a5a5fcd0a4ee8b9a5e2426),
[femtaskpanels.task_constraint_tie._TaskPanel.form](../../d3/dcb/classfemtaskpanels_1_1task__constraint__tie_1_1__TaskPanel.html#a0926535d74e750d6d33343919fa78e3b),
[femtaskpanels.task_element_fluid1D._TaskPanel.form](../../d8/d3f/classfemtaskpanels_1_1task__element__fluid1D_1_1__TaskPanel.html#ab67b3e967eb86bbd97094f1355bf0002),
[femtaskpanels.task_element_geometry1D._TaskPanel.form](../../d8/d7d/classfemtaskpanels_1_1task__element__geometry1D_1_1__TaskPanel.html#aa19768a65ed0c450c1547a02948d7c0e),
[femtaskpanels.task_element_geometry2D._TaskPanel.form](../../de/df4/classfemtaskpanels_1_1task__element__geometry2D_1_1__TaskPanel.html#ae8d1905cf65cbf06f3e3cee6890591b3),
[femtaskpanels.task_element_rotation1D._TaskPanel.form](../../d4/d17/classfemtaskpanels_1_1task__element__rotation1D_1_1__TaskPanel.html#aae923308240fa4f6e1808748aa114996),
[femtaskpanels.task_material_common._TaskPanel.form](../../dd/db9/classfemtaskpanels_1_1task__material__common_1_1__TaskPanel.html#a1c4b1891fc4effb5bec3aa2a3d64080d),
[femtaskpanels.task_material_reinforced._TaskPanel.form](../../d3/d99/classfemtaskpanels_1_1task__material__reinforced_1_1__TaskPanel.html#abc07f48916e4c81a8f2d9fdb0736367c),
[femtaskpanels.task_mesh_boundarylayer._TaskPanel.form](../../d5/deb/classfemtaskpanels_1_1task__mesh__boundarylayer_1_1__TaskPanel.html#aab783a2b0217a40cae733fcb6d87c75d),
[femtaskpanels.task_mesh_gmsh._TaskPanel.form](../../d6/d90/classfemtaskpanels_1_1task__mesh__gmsh_1_1__TaskPanel.html#acfea9232b9fe18d065d3b2ac2d21b5b7),
[femtaskpanels.task_mesh_group._TaskPanel.form](../../da/d00/classfemtaskpanels_1_1task__mesh__group_1_1__TaskPanel.html#a9fafcda2a512632f818348b342bbe135),
[femtaskpanels.task_mesh_region._TaskPanel.form](../../d6/d04/classfemtaskpanels_1_1task__mesh__region_1_1__TaskPanel.html#a0437bf04c5f882fe370b69b355ef9fd6),
[femtaskpanels.task_result_mechanical._TaskPanel.form](../../d1/d11/classfemtaskpanels_1_1task__result__mechanical_1_1__TaskPanel.html#aecf085408c258bc90a830715202c86d2),
[femtaskpanels.task_solver_ccxtools._TaskPanel.form](../../da/df4/classfemtaskpanels_1_1task__solver__ccxtools_1_1__TaskPanel.html#a470b59d7f6c766544bcb092f1b6f6c01),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.tolerance_zone.form,
[automotive_design.tolerance_zone.form](../../d6/def/classautomotive__design_1_1tolerance__zone.html#adc83f5887897a2c991c4399647d39ad8),
[OpenSCADCommands.AddSCADTask.form](../../d5/d9d/classOpenSCADCommands_1_1AddSCADTask.html#a03c9bf4d8a83a90bba693a3aad1b7765),
[OpenSCADCommands.OpenSCADMeshBooleanTask.form](../../d7/d91/classOpenSCADCommands_1_1OpenSCADMeshBooleanTask.html#a9b9b2f3aaef8760502360d97e55c23b0),
[AttachmentEditor.TaskAttachmentEditor.AttachmentEditorTaskPanel.form](../../d8/d4c/classAttachmentEditor_1_1TaskAttachmentEditor_1_1AttachmentEditorTaskPanel.html#a2b3a8daa7cc6396433b8d9045ac5462f),
[BasicShapes.ViewProviderShapes.TaskTubeUI.form](../../db/dd6/classBasicShapes_1_1ViewProviderShapes_1_1TaskTubeUI.html#a54e00f1d6d94550bde572c73b4a577d9),
[Mod.PartDesign.FeatureHole.TaskHole.TaskHole.form](../../d1/d14/classMod_1_1PartDesign_1_1FeatureHole_1_1TaskHole_1_1TaskHole.html#afd4f06a4234d8cc056f45f0e1fe51b97),
Mod.PartDesign.InvoluteGearFeature._InvoluteGearTaskPanel.form,
[Mod.PartDesign.SprocketFeature.SprocketTaskPanel.form](../../db/d2b/classMod_1_1PartDesign_1_1SprocketFeature_1_1SprocketTaskPanel.html#ad454b75a40c683d61867e9dbb717d484),
[Mod.PartDesign.WizardShaft.WizardShaft.TaskWizardShaft.form](../../d9/dde/classMod_1_1PartDesign_1_1WizardShaft_1_1WizardShaft_1_1TaskWizardShaft.html#a156b5486d1a1951e7b04af9bcca24211),
[PathPythonGui.simple_edit_panel.SimpleEditPanel.form](../../d4/d29/classPathPythonGui_1_1simple__edit__panel_1_1SimpleEditPanel.html#ac9dab387e08a4adbbb051c49adf04245),
[PathScripts.PathCamoticsGui.CAMoticsUI.form](../../d2/df4/classPathScripts_1_1PathCamoticsGui_1_1CAMoticsUI.html#adb7ad0e649a66131a30d032830fb65a4),
[PathScripts.PathDressupAxisMap.TaskPanel.form](../../dd/de9/classPathScripts_1_1PathDressupAxisMap_1_1TaskPanel.html#ad6a929133568919c74cc1e57bad7a147),
[PathScripts.PathDressupDogbone.TaskPanel.form](../../df/d54/classPathScripts_1_1PathDressupDogbone_1_1TaskPanel.html#ab531d004fdf5b7f4b2d421e2a65b23ec),
[PathScripts.PathDressupDragknife.TaskPanel.form](../../d0/d93/classPathScripts_1_1PathDressupDragknife_1_1TaskPanel.html#a4b1c3b1ab157e75d00a3930cd0fbdd86),
[PathScripts.PathDressupPathBoundaryGui.TaskPanel.form](../../d4/d65/classPathScripts_1_1PathDressupPathBoundaryGui_1_1TaskPanel.html#a4bc82010533d01700d7cc676e355ba35),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.form](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#ab90eb693a1f730fb4a06885b4ff0c5ed),
[PathScripts.PathDressupTagPreferences.HoldingTagPreferences.form](../../d5/d35/classPathScripts_1_1PathDressupTagPreferences_1_1HoldingTagPreferences.html#a777b436370ff5b29653890343a101e58),
[PathScripts.PathDressupZCorrect.TaskPanel.form](../../d7/d25/classPathScripts_1_1PathDressupZCorrect_1_1TaskPanel.html#a361ceb1df718670e4c7d2dccbc6e1bd1),
[PathScripts.PathJobGui.StockEdit.form](../../d4/dbf/classPathScripts_1_1PathJobGui_1_1StockEdit.html#a51fe44feb100191b64b08ac811a42c84),
[PathScripts.PathJobGui.TaskPanel.form](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#a359e00422d40b8cd9d9b24faf82a52fe),
[PathScripts.PathOpGui.TaskPanelPage.form](../../d1/d18/classPathScripts_1_1PathOpGui_1_1TaskPanelPage.html#ad13a6ac11164bfd4f27e851aee69024e),
[PathScripts.PathOpGui.TaskPanel.form](../../da/d7e/classPathScripts_1_1PathOpGui_1_1TaskPanel.html#a79bf3f513955ef2d541c3c54450923f5),
[PathScripts.PathPreferencesAdvanced.AdvancedPreferencesPage.form](../../d5/d8b/classPathScripts_1_1PathPreferencesAdvanced_1_1AdvancedPreferencesPage.html#a6ca4e42a4bc484d463680b1c58e55570),
[PathScripts.PathPreferencesPathDressup.DressupPreferencesPage.form](../../db/d3d/classPathScripts_1_1PathPreferencesPathDressup_1_1DressupPreferencesPage.html#af177d36430b024980e0318d8409fe733),
[PathScripts.PathPreferencesPathJob.JobPreferencesPage.form](../../db/dec/classPathScripts_1_1PathPreferencesPathJob_1_1JobPreferencesPage.html#a5e6d4007077468d0c52f762da0c057cd),
[PathScripts.PathPropertyBagGui.PropertyCreate.form](../../dd/d6e/classPathScripts_1_1PathPropertyBagGui_1_1PropertyCreate.html#ae88e42e3c450e95a6860e0f5d6609d3d),
[PathScripts.PathPropertyBagGui.TaskPanel.form](../../d3/d93/classPathScripts_1_1PathPropertyBagGui_1_1TaskPanel.html#ae1ff342e003a7beb0757f4177194c400),
[PathScripts.PathSetupSheetGui.OpTaskPanel.form](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#a98a5843cff26e07a8dcf6f67441a94a7),
[PathScripts.PathSetupSheetGui.OpsDefaultEditor.form](../../d3/dcd/classPathScripts_1_1PathSetupSheetGui_1_1OpsDefaultEditor.html#a7bec49b69be355afcb30d257d0dfd590),
[PathScripts.PathSetupSheetGui.GlobalEditor.form](../../de/df9/classPathScripts_1_1PathSetupSheetGui_1_1GlobalEditor.html#a1dcb76e5675131c927b19332ede32aed),
[PathScripts.PathSetupSheetGui.TaskPanel.form](../../df/d2a/classPathScripts_1_1PathSetupSheetGui_1_1TaskPanel.html#afdefde1c95320c2180442b35f1967f89),
[PathScripts.PathSimulatorGui.CAMSimTaskUi.form](../../d9/ddf/classPathScripts_1_1PathSimulatorGui_1_1CAMSimTaskUi.html#a7134df13124c52c77813488c58c37f13),
[PathScripts.PathToolBitEdit.ToolBitEditor.form](../../d6/d36/classPathScripts_1_1PathToolBitEdit_1_1ToolBitEditor.html#afac465e3bbd80c55a6e2d8c9c43c8ab0),
[PathScripts.PathToolBitGui.TaskPanel.form](../../d4/dc9/classPathScripts_1_1PathToolBitGui_1_1TaskPanel.html#a4747e0d3c54f8c9b74e63609bc4b6939),
[PathScripts.PathToolBitLibraryGui.ToolBitSelector.form](../../d8/d6e/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitSelector.html#a32f1d3ac6e7f1b608cd36e1440bc3c4f),
[PathScripts.PathToolBitLibraryGui.ToolBitLibrary.form](../../dd/d3a/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitLibrary.html#a2cd857ed43442689be186dd9775c6a35),
[PathScripts.PathToolControllerGui.ToolControllerEditor.form](../../d2/db6/classPathScripts_1_1PathToolControllerGui_1_1ToolControllerEditor.html#a879d7dd6c6315d2faf0bb0775ce193c5),
[PathScripts.PathToolControllerGui.TaskPanel.form](../../dd/d4c/classPathScripts_1_1PathToolControllerGui_1_1TaskPanel.html#a91c9ee65a2170722ec8789350f99938c),
[PathScripts.PathToolEdit.ToolEditorDefault.form](../../db/db4/classPathScripts_1_1PathToolEdit_1_1ToolEditorDefault.html#aa770a3660e78695f696f6742c6ee017b),
[PathScripts.PathToolEdit.ToolEditorImage.form](../../dd/df1/classPathScripts_1_1PathToolEdit_1_1ToolEditorImage.html#ae8ee3319967836821bff939ec1369191),
[PathScripts.PathToolEdit.ToolEditor.form](../../d2/df8/classPathScripts_1_1PathToolEdit_1_1ToolEditor.html#a05ac115b416fbaf5ecc4da3dd11d3ccb),
[PathScripts.PathToolLibraryEditor.EditorPanel.form](../../d0/d92/classPathScripts_1_1PathToolLibraryEditor_1_1EditorPanel.html#ab947ef6f5639b4cb3e332a4b56e8611e),
SketcherGui::SketcherSettings.form,
[TechDrawTools.TaskMoveView.TaskMoveView.form](../../da/d16/classTechDrawTools_1_1TaskMoveView_1_1TaskMoveView.html#a30f1e99d118f7124e1ec5de9c1099fa3),
[TechDrawTools.TaskShareView.TaskShareView.form](../../d0/d64/classTechDrawTools_1_1TaskShareView_1_1TaskShareView.html#ac09cab300fc8823552c87d6757b20831),
[TaskPanel.TaskPanel.form](../../d3/da6/classTaskPanel_1_1TaskPanel.html#acb312cc9d738ff1274d7563b1614b736),
[TaskPanel.TaskCalendar.form](../../d7/de4/classTaskPanel_1_1TaskCalendar.html#a61b5bde6aa4d132d898b9be8d16f1197),
[TaskPanel.TaskManyTaskBoxes.form](../../dc/d41/classTaskPanel_1_1TaskManyTaskBoxes.html#ad5bcfb68a552a057a551ce410a793003),
ArchMaterial._ArchMaterialTaskPanel.fromExisting(),
ArchMaterial._ArchMultiMaterialTaskPanel.fromExisting(),
ArchMaterial._ArchMultiMaterialTaskPanel.invertLayer(),
[ArchMaterial.MultiMaterialDelegate.mats](../../dd/dba/classArchMaterial_1_1MultiMaterialDelegate.html#ae387a9a2f36ded662503190caa9f41b0),
Gui::VectorListEditor.model, ArchMaterial._ArchMultiMaterialTaskPanel.model,
PartGui::TaskCheckGeometryResults.model,
[PathScripts.PathFeatureExtensionsGui.TaskPanelExtensionPage.model](../../d0/de3/classPathScripts_1_1PathFeatureExtensionsGui_1_1TaskPanelExtensionPage.html#a042f0b1dc39d88617887b096746a8f43),
[PathScripts.PathJobDlg.JobCreate.model](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#a78b7fe869f083d6b1443602f5a9fe831),
[PathScripts.PathOp.ObjectOp.model](../../d0/dec/classPathScripts_1_1PathOp_1_1ObjectOp.html#a14a2d331acc36bce42c2ecaa3fbfef3e),
[PathScripts.PathPropertyBagGui.TaskPanel.model](../../d3/d93/classPathScripts_1_1PathPropertyBagGui_1_1TaskPanel.html#ac0b2482405795796de2e0c35194b0053),
[PathScripts.PathSetupSheetGui.OpTaskPanel.model](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#a82fccec7b21c095ca8fe5147431cb95f),
[PathScripts.PathToolBitEdit.ToolBitEditor.model](../../d6/d36/classPathScripts_1_1PathToolBitEdit_1_1ToolBitEditor.html#ac78901f82621cc7b91c880552b5e7fdb),
[SpreadsheetGui::SheetView.model](../../d0/d67/classSpreadsheetGui_1_1SheetView.html#a82aed23a1ce37b41866970b82bba2437),
ArchMaterial._ArchMultiMaterialTaskPanel.moveLayer(),
[UpdateLabelExpressionVisitor.obj](../../d3/d25/classUpdateLabelExpressionVisitor.html#a4f09629942c265910f22db0979c2076e),
App::Origin::OriginExtension.obj, Base::ObjectStatusLocker< Status, Object
>.obj, Gui::ActiveObjectList::ObjectInfo.obj,
[Info.obj](../../da/dd3/structInfo.html#a6ed67bc92bf2c8dd587a9f2304aa91e4),
[ExpressionCompleterModel::Info.obj](../../de/dc8/unionExpressionCompleterModel_1_1Info.html#ad98e6fee4858b5a5f0cfe4df44c87d8a),
[ItemInfo.obj](../../df/d38/structItemInfo.html#ae7a64403f10b96ad150fa909fc715a0a),
[ItemInfo2.obj](../../d0/dcc/structItemInfo2.html#ae11886d1835bfaf6a275f3f2a20beacd),
ArchAxis._AxisTaskPanel.obj,
[ArchAxisSystem.AxisSystemTaskPanel.obj](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#afe0e8deb023e870de138687223c543af),
[ArchComponent.ComponentTaskPanel.obj](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#a7c9c0c3b7e7450e5dbaa7eb482fa6a5a),
[ArchGrid.ArchGridTaskPanel.obj](../../d6/da7/classArchGrid_1_1ArchGridTaskPanel.html#a522c117afbe8df7d8db624b367b38aee),
ArchMaterial._ArchMaterialTaskPanel.obj,
ArchMaterial._ArchMultiMaterialTaskPanel.obj,
[ArchPanel.SheetTaskPanel.obj](../../dd/d0f/classArchPanel_1_1SheetTaskPanel.html#a7213fb4c596a7f86b52d01b61ef7ff3f),
[ArchProfile.ProfileTaskPanel.obj](../../dc/d9a/classArchProfile_1_1ProfileTaskPanel.html#af47df481a9173f0c6012467f1e0a723a),
[ArchReference.ArchReferenceTaskPanel.obj](../../d4/d73/classArchReference_1_1ArchReferenceTaskPanel.html#a07c7984a75033f2ec01e5833441758c3),
ArchRoof._RoofTaskPanel.obj,
[ArchSchedule.ArchScheduleTaskPanel.obj](../../d5/da0/classArchSchedule_1_1ArchScheduleTaskPanel.html#a59bbaafdc77eb65016ca5cc0b959a67e),
[ArchSectionPlane.SectionPlaneTaskPanel.obj](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#a0eb7e13b925a643924b1c3b89d335ba0),
ArchWindow._ArchWindowTaskPanel.obj,
[DraftGui.FacebinderTaskPanel.obj](../../d2/d61/classDraftGui_1_1FacebinderTaskPanel.html#a6dd2bb6b02fec5e1d3889b5498518f91),
[draftguitools.gui_base_original.DraftTool.obj](../../da/d09/classdraftguitools_1_1gui__base__original_1_1DraftTool.html#ab7436ce0f01eb939c13e24609fd8ba60),
[draftguitools.gui_edit.Edit.obj](../../d8/d68/classdraftguitools_1_1gui__edit_1_1Edit.html#aa8d3ebfbd130a35db4c75b1ba51803b3),
[draftguitools.gui_lines.Line.obj](../../da/d8f/classdraftguitools_1_1gui__lines_1_1Line.html#a99262a36880c92955289e18a4ac11c3c),
[draftguitools.gui_trimex.Trimex.obj](../../da/df7/classdraftguitools_1_1gui__trimex_1_1Trimex.html#aa55a7b7c6e9d738bdbae1ded50f1d56f),
[draftguitools.gui_wire2spline.WireToBSpline.obj](../../d4/dd5/classdraftguitools_1_1gui__wire2spline_1_1WireToBSpline.html#a9faba7181e99017273d68289627c7aed),
[femtaskpanels.task_constraint_centrif._TaskPanel.obj](../../de/da6/classfemtaskpanels_1_1task__constraint__centrif_1_1__TaskPanel.html#a7c775fa1762fde5f42a90d2a0239afc6),
[femtaskpanels.task_constraint_sectionprint._TaskPanel.obj](../../da/d77/classfemtaskpanels_1_1task__constraint__sectionprint_1_1__TaskPanel.html#aaa7b2ad8fb06796bf5d84e7c35ab647a),
[femtaskpanels.task_constraint_tie._TaskPanel.obj](../../d3/dcb/classfemtaskpanels_1_1task__constraint__tie_1_1__TaskPanel.html#a38fa3894658e392570f9337bc9a9c091),
[femtaskpanels.task_element_fluid1D._TaskPanel.obj](../../d8/d3f/classfemtaskpanels_1_1task__element__fluid1D_1_1__TaskPanel.html#a6b1074b6e8c5a51c0eaf6bf50fa29f82),
[femtaskpanels.task_element_geometry1D._TaskPanel.obj](../../d8/d7d/classfemtaskpanels_1_1task__element__geometry1D_1_1__TaskPanel.html#a1692ea078c03deb95848e6d25f8e2d87),
[femtaskpanels.task_element_geometry2D._TaskPanel.obj](../../de/df4/classfemtaskpanels_1_1task__element__geometry2D_1_1__TaskPanel.html#a812cb23a0144a61a7080a056c626dc73),
[femtaskpanels.task_element_rotation1D._TaskPanel.obj](../../d4/d17/classfemtaskpanels_1_1task__element__rotation1D_1_1__TaskPanel.html#a8d78ce582ce5492f114c21a4d672d272),
[femtaskpanels.task_material_common._TaskPanel.obj](../../dd/db9/classfemtaskpanels_1_1task__material__common_1_1__TaskPanel.html#afe2247c01f1c819235ee5ee0bd81baca),
[femtaskpanels.task_material_reinforced._TaskPanel.obj](../../d3/d99/classfemtaskpanels_1_1task__material__reinforced_1_1__TaskPanel.html#a40da4ebfceb93727eb81f21917152999),
[femtaskpanels.task_mesh_boundarylayer._TaskPanel.obj](../../d5/deb/classfemtaskpanels_1_1task__mesh__boundarylayer_1_1__TaskPanel.html#a54cae60fc88d1dac59f7a28909ba2dc6),
[femtaskpanels.task_mesh_group._TaskPanel.obj](../../da/d00/classfemtaskpanels_1_1task__mesh__group_1_1__TaskPanel.html#a72796377d8c08fd8c86a6e1813f53301),
[femtaskpanels.task_mesh_region._TaskPanel.obj](../../d6/d04/classfemtaskpanels_1_1task__mesh__region_1_1__TaskPanel.html#a6a18d75cacdb192835f605e3b63a46e3),
Import::ImportOCAF2::Info.obj,
[MaterialEditor.MaterialEditor.obj](../../d8/dbf/classMaterialEditor_1_1MaterialEditor.html#ada73666067450e97240e8182c65f6d9b),
[AttachmentEditor.TaskAttachmentEditor.AttachmentEditorTaskPanel.obj](../../d8/d4c/classAttachmentEditor_1_1TaskAttachmentEditor_1_1AttachmentEditorTaskPanel.html#aa424047116c81b898522afcaaa0d0d41),
[PartGui::DlgFilletEdges::Private::SelectionObjectCompare.obj](../../d8/db8/classPartGui_1_1DlgFilletEdges_1_1Private_1_1SelectionObjectCompare.html#a27ff7bdb4178561893a0726c1062394f),
[PartGui::FaceColors::Private.obj](../../d4/d4b/classFaceColors_1_1Private.html#a306ede71b7532576f87919c23fdcde58),
Mod.PartDesign.InvoluteGearFeature._InvoluteGearTaskPanel.obj,
[Mod.PartDesign.SprocketFeature.SprocketTaskPanel.obj](../../db/d2b/classMod_1_1PartDesign_1_1SprocketFeature_1_1SprocketTaskPanel.html#a011197f5361c0d748a8c46878226f930),
PathCommands._CommandSelectLoop.obj,
[PathPythonGui.simple_edit_panel.SimpleEditPanel.obj](../../d4/d29/classPathPythonGui_1_1simple__edit__panel_1_1SimpleEditPanel.html#a1b8bfee5c98ab82526cd0ab9a0d16d6a),
[PathScripts.PathDressupAxisMap.TaskPanel.obj](../../dd/de9/classPathScripts_1_1PathDressupAxisMap_1_1TaskPanel.html#ac57ff1080fb0ee5bb317335bea833c5c),
[PathScripts.PathDressupAxisMap.ViewProviderDressup.obj](../../d7/d13/classPathScripts_1_1PathDressupAxisMap_1_1ViewProviderDressup.html#a90fcd362243937d5bc27d562b30ac42e),
[PathScripts.PathDressupDogbone.Bone.obj](../../d6/d5c/classPathScripts_1_1PathDressupDogbone_1_1Bone.html#a1a8dbb8d22178123858a0f971bc11064),
[PathScripts.PathDressupDogbone.TaskPanel.obj](../../df/d54/classPathScripts_1_1PathDressupDogbone_1_1TaskPanel.html#a17c94b28fe95075964b2afb7d28de39a),
[PathScripts.PathDressupDogbone.ViewProviderDressup.obj](../../df/ddb/classPathScripts_1_1PathDressupDogbone_1_1ViewProviderDressup.html#a84a5aeeb00b5bd76932e81d9a97b708c),
[PathScripts.PathDressupDragknife.TaskPanel.obj](../../d0/d93/classPathScripts_1_1PathDressupDragknife_1_1TaskPanel.html#a5d735d8e5d238cc115209b657cb69550),
[PathScripts.PathDressupHoldingTags.PathData.obj](../../df/d95/classPathScripts_1_1PathDressupHoldingTags_1_1PathData.html#afd49ccec9b35ec10c2bf95637981b0ed),
[PathScripts.PathDressupHoldingTags.ObjectTagDressup.obj](../../de/dd2/classPathScripts_1_1PathDressupHoldingTags_1_1ObjectTagDressup.html#a31eb19991e7932da5690c65ed0b8433b),
[PathScripts.PathDressupLeadInOut.ObjectDressup.obj](../../de/dde/classPathScripts_1_1PathDressupLeadInOut_1_1ObjectDressup.html#aaa0a5c32d85a1a4576880a93d079c12e),
[PathScripts.PathDressupLeadInOut.ViewProviderDressup.obj](../../d7/d49/classPathScripts_1_1PathDressupLeadInOut_1_1ViewProviderDressup.html#a38cc17cbac5b8299b8373ead5584e0df),
[PathScripts.PathDressupPathBoundary.DressupPathBoundary.obj](../../d4/dc1/classPathScripts_1_1PathDressupPathBoundary_1_1DressupPathBoundary.html#add7b155f3cd5e5c7befad9d6f6cb0be1),
[PathScripts.PathDressupPathBoundaryGui.TaskPanel.obj](../../d4/d65/classPathScripts_1_1PathDressupPathBoundaryGui_1_1TaskPanel.html#ac5e4ca09097175ab1ca8a243addc0633),
[PathScripts.PathDressupPathBoundaryGui.DressupPathBoundaryViewProvider.obj](../../dc/d69/classPathScripts_1_1PathDressupPathBoundaryGui_1_1DressupPathBoundaryViewProvider.html#af62a8ee377f3b2442bd5d52eb4252b32),
[PathScripts.PathDressupRampEntry.ObjectDressup.obj](../../d4/d77/classPathScripts_1_1PathDressupRampEntry_1_1ObjectDressup.html#a582f3e90d46d59e66b944998f32b2da0),
[PathScripts.PathDressupRampEntry.ViewProviderDressup.obj](../../db/d82/classPathScripts_1_1PathDressupRampEntry_1_1ViewProviderDressup.html#abfc470a12f59764543d341fa2f7e47d7),
[PathScripts.PathDressupTag.ObjectDressup.obj](../../d9/dd0/classPathScripts_1_1PathDressupTag_1_1ObjectDressup.html#aef43708b6ac8e2f1f93c3f72d8d18871),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.obj](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#a0d18c292858e211002ed2b501d8a93eb),
[PathScripts.PathDressupTagGui.PathDressupTagViewProvider.obj](../../dc/d08/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagViewProvider.html#abb60176b837b2c5527671ffde04d29b0),
[PathScripts.PathDressupZCorrect.TaskPanel.obj](../../d7/d25/classPathScripts_1_1PathDressupZCorrect_1_1TaskPanel.html#a456004a13cca915810ce3ba91380c947),
[PathScripts.PathDressupZCorrect.ViewProviderDressup.obj](../../d1/df1/classPathScripts_1_1PathDressupZCorrect_1_1ViewProviderDressup.html#a20d3c8a8bc53aa6c86060d58c95a7c85),
[PathScripts.PathFeatureExtensions.Extension.obj](../../d7/d86/classPathScripts_1_1PathFeatureExtensions_1_1Extension.html#a31e68bd06177fc8655359cc24878e298),
PathScripts.PathFeatureExtensionsGui._Extension.obj,
[PathScripts.PathGetPoint.TaskPanel.obj](../../d8/d28/classPathScripts_1_1PathGetPoint_1_1TaskPanel.html#a38c51fe6f9ea3523715d04f018842f69),
[PathScripts.PathGui.QuantitySpinBox.obj](../../dc/de0/classPathScripts_1_1PathGui_1_1QuantitySpinBox.html#ac997c67c3aa6df182bc791f402cd02e0),
[PathScripts.PathIconViewProvider.ViewProvider.obj](../../d6/d55/classPathScripts_1_1PathIconViewProvider_1_1ViewProvider.html#abe9a5440c76a366b603e86d3ef07a812),
[PathScripts.PathJob.ObjectJob.obj](../../df/d08/classPathScripts_1_1PathJob_1_1ObjectJob.html#af27f9c05db9741873fccf1e67b2f7f69),
[PathScripts.PathJobGui.ViewProvider.obj](../../d3/d3e/classPathScripts_1_1PathJobGui_1_1ViewProvider.html#a6b51075bbeb4f6b364a9785d18313962),
[PathScripts.PathJobGui.StockEdit.obj](../../d4/dbf/classPathScripts_1_1PathJobGui_1_1StockEdit.html#a4e06464f3974a4f3096a2e6c0ad2e8ec),
[PathScripts.PathJobGui.TaskPanel.obj](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#a3623cc0a723dcde97d4eafef570fa536),
[PathScripts.PathOpGui.TaskPanelPage.obj](../../d1/d18/classPathScripts_1_1PathOpGui_1_1TaskPanelPage.html#af01d62483ff08cb8d1540324a8c27d19),
[PathScripts.PathOpGui.TaskPanel.obj](../../da/d7e/classPathScripts_1_1PathOpGui_1_1TaskPanel.html#a5d75b0eaa6ed4a4de43c6b1be7473617),
[PathScripts.PathPropertyBag.PropertyBag.obj](../../d8/dd1/classPathScripts_1_1PathPropertyBag_1_1PropertyBag.html#adc8a995796f80aad92fe0747f0240c02),
[PathScripts.PathPropertyBagGui.ViewProvider.obj](../../d5/d77/classPathScripts_1_1PathPropertyBagGui_1_1ViewProvider.html#a09da58a4977ab3854fb44e42ee760a82),
[PathScripts.PathPropertyBagGui.PropertyCreate.obj](../../dd/d6e/classPathScripts_1_1PathPropertyBagGui_1_1PropertyCreate.html#ac83d59135d7c86730b62ee7648ed8c8e),
[PathScripts.PathPropertyBagGui.TaskPanel.obj](../../d3/d93/classPathScripts_1_1PathPropertyBagGui_1_1TaskPanel.html#a688abd0f4bc19440a26f9f7b773c641f),
PathScripts.PathPropertyEditor._PropertyEditor.obj,
[PathScripts.PathSetupSheet.SetupSheet.obj](../../d9/dce/classPathScripts_1_1PathSetupSheet_1_1SetupSheet.html#af602e28b8af58f368abf8b9c38c04ca6),
[PathScripts.PathSetupSheetGui.ViewProvider.obj](../../dc/dc3/classPathScripts_1_1PathSetupSheetGui_1_1ViewProvider.html#a2bdc51a08cff4a635845b3b683c052c7),
[PathScripts.PathSetupSheetGui.OpTaskPanel.obj](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#a6214ae535c8596e5bcbc3014acaec1a0),
[PathScripts.PathSetupSheetGui.OpsDefaultEditor.obj](../../d3/dcd/classPathScripts_1_1PathSetupSheetGui_1_1OpsDefaultEditor.html#a3ed948b4abbcb4c00380b9e7667446a0),
[PathScripts.PathSetupSheetGui.GlobalEditor.obj](../../de/df9/classPathScripts_1_1PathSetupSheetGui_1_1GlobalEditor.html#ae8af16cf0707bfa9566a2623de7747f6),
[PathScripts.PathSetupSheetGui.TaskPanel.obj](../../df/d2a/classPathScripts_1_1PathSetupSheetGui_1_1TaskPanel.html#ab320f3654e32292a3f5fcecfa1188217),
[PathScripts.PathSurfaceSupport.PathGeometryGenerator.obj](../../d9/d46/classPathScripts_1_1PathSurfaceSupport_1_1PathGeometryGenerator.html#a60b07de04da82a9d0152af47a5fee947),
[PathScripts.PathSurfaceSupport.ProcessSelectedFaces.obj](../../d4/d8d/classPathScripts_1_1PathSurfaceSupport_1_1ProcessSelectedFaces.html#adeeb793df72885927a164bcf246c2e63),
[PathScripts.PathSurfaceSupport.OCL_Tool.obj](../../dd/da3/classPathScripts_1_1PathSurfaceSupport_1_1OCL__Tool.html#a065e783b847d9e6694c425234c7646a4),
[PathScripts.PathToolBit.ToolBit.obj](../../d3/d85/classPathScripts_1_1PathToolBit_1_1ToolBit.html#a4d61220c77906f30126dfc416eb469b1),
[PathScripts.PathToolBitGui.ViewProvider.obj](../../d0/d90/classPathScripts_1_1PathToolBitGui_1_1ViewProvider.html#a234eed19789386d6ae2ce79a55550597),
[PathScripts.PathToolBitGui.TaskPanel.obj](../../d4/dc9/classPathScripts_1_1PathToolBitGui_1_1TaskPanel.html#a74a359040e157c00224a223a9018050d),
[PathScripts.PathToolControllerGui.ToolControllerEditor.obj](../../d2/db6/classPathScripts_1_1PathToolControllerGui_1_1ToolControllerEditor.html#a29d6a019e0ab9a7b0251383c6858368f),
[PathScripts.PathToolControllerGui.TaskPanel.obj](../../dd/d4c/classPathScripts_1_1PathToolControllerGui_1_1TaskPanel.html#a63aca252d0366cef829a384d5e7a5685),
[PathScripts.PathToolControllerGui.DlgToolControllerEdit.obj](../../db/d49/classPathScripts_1_1PathToolControllerGui_1_1DlgToolControllerEdit.html#a2e660f70b1530a06714fa1c5500d6ad5),
[PathTests.TestPathDrillable.TestPathDrillable.obj](../../d4/d90/classPathTests_1_1TestPathDrillable_1_1TestPathDrillable.html#aab2f9325ad4469b8d399aedceee4d906),
[ReenGui::FitBSplineSurfaceWidget::Private.obj](../../d8/d89/classFitBSplineSurfaceWidget_1_1Private.html#a123d2f0a0b1f360ffd27abdcd2c2b63c),
[ReenGui::PoissonWidget::Private.obj](../../d7/d0a/classPoissonWidget_1_1Private.html#ae3d21aeac93bcea7e5ad54a882d1b201),
[Sandbox::CustomAddObjectEvent.obj](../../d0/d48/classSandbox_1_1CustomAddObjectEvent.html#a8e53e89ad1057ece113335351a50ef79),
[Sandbox::CustomPurgeEvent.obj](../../d1/d09/classSandbox_1_1CustomPurgeEvent.html#a94a0265ce60d78f30f737f80c89994be),
Sandbox::Callable< T, method >.obj, Sandbox::CallableWithArgs< T, Arg, method
>.obj, Sandbox::DocumentObjectProtector.obj,
[Texture.ViewProviderTexture.obj](../../d1/d29/classTexture_1_1ViewProviderTexture.html#a0618e1a1b918d420a331c2fb4848fe40),
Web::FirewallPython.obj,
[draftutils.translate.QT_TRANSLATE_NOOP](../../de/d75/group__draftutils.html#ga9e6796e4394a4a163501246d7390f3c4),
ArchMaterial._ArchMultiMaterialTaskPanel.recalcThickness(), and
ArchMaterial._ArchMultiMaterialTaskPanel.upLayer().

## Member Data Documentation

## ◆ mats

ArchMaterial.MultiMaterialDelegate.mats  
---  
  
Referenced by
[ArchMaterial.MultiMaterialDelegate.setEditorData()](../../dd/dba/classArchMaterial_1_1MultiMaterialDelegate.html#a75d5a15afd46efb694039ed6653ff181),
and
[ArchMaterial.MultiMaterialDelegate.setModelData()](../../dd/dba/classArchMaterial_1_1MultiMaterialDelegate.html#aa36ee69be80adc06480436ec7883804e).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Arch/ArchMaterial.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

