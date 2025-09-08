---
url: https://freecad.github.io/SourceDoc/d8/d1c/classArchCommands_1_1SurveyTaskPanel.html
scraped_at: 2025-09-08T14:57:31.307508
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ArchCommands](../../d4/d52/namespaceArchCommands.html)
  * [SurveyTaskPanel](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html)

[List of all members](../../db/d70/classArchCommands_1_1SurveyTaskPanel-members.html) | Public Member Functions | Public Attributes

ArchCommands.SurveyTaskPanel Class Reference

##  Public Member Functions  
  
---  
def | [clear](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a3d71740ba5dd0df4a7336c16ee953059) (self)  
def | [clipArea](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a1b8288364a10a547a60fd6f31f1a905b) (self)  
def | [clipLength](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a92d5adcd70e03694fd7b1372c451c523) (self)  
def | [exportCSV](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#af92d233658c91140db86272c111fc760) (self)  
def | [getStandardButtons](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#abc60ff137082157b02d74beecd109faf) (self)  
def | [isAllowedAlterSelection](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#aa6e602740be52677db7c626532b03c94) (self)  
def | [isAllowedAlterView](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a2b88a4911d0480320d0d3d24714fb074) (self)  
def | [newline](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a57d6b27250bfa8a1a2e74be167af7bda) (self, length=0, area=0)  
def | [reject](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a89fa5b20fd9f70a1ae2623cc24aa2b40) (self)  
def | [retranslateUi](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a80aefc6bf17d60c63cd66e8984616d4b) (self, dlg)  
def | [setDescr](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a50b3c7eab9fe04cc2dac1cff7ded7e3a) (self, item, col)  
def | [setText](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#ad3c7a67dea06fdb170bb7e6d76224b1e) (self)  
def | [update](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a77685c35ce185891696d5ac525070003) (self, column, txt)  
  
##  Public Attributes  
  
---  
|
[addButton](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a0a6a52090b3e7f8e3f93b9cc4e9c01a8)  
|
[clearButton](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a476d6e01eadb9c172cf059d0481a8ebe)  
|
[copyArea](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a4bf4f54edb7dae185229cd580c8b9b2f)  
|
[copyLength](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#aa67013cbf8d7b4f4b1d6fa48c937856f)  
|
[descr](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#afd9964216a25519a3a80c49426ae6d0e)  
|
[export](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#ae882a1934ee25e38683b82cd4f27c79f)  
|
[form](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a04804d6ea774adf44c626845ca1dcfb5)  
|
[tree](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a00907b1a9c07d5f90fa3a99f3111fc79)  
  
## Member Function Documentation

## ◆ clear()

def ArchCommands.SurveyTaskPanel.clear  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
## ◆ clipArea()

def ArchCommands.SurveyTaskPanel.clipArea  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[ArchCommands.SurveyTaskPanel.setText()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#ad3c7a67dea06fdb170bb7e6d76224b1e),
and
[ArchCommands.string_replace()](../../d4/d52/namespaceArchCommands.html#af256192f97a16dc89632e0e9fd0c804b).

## ◆ clipLength()

def ArchCommands.SurveyTaskPanel.clipLength  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[ArchCommands.SurveyTaskPanel.setText()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#ad3c7a67dea06fdb170bb7e6d76224b1e).

## ◆ exportCSV()

def ArchCommands.SurveyTaskPanel.exportCSV  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References Gui::DockWnd::ComboView.tree, ArchAxis._AxisTaskPanel.tree,
[ArchAxisSystem.AxisSystemTaskPanel.tree](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a0c3edb65b15bb3281318dfdda901a2e3),
[ArchCommands.SurveyTaskPanel.tree](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a00907b1a9c07d5f90fa3a99f3111fc79),
[ArchComponent.ComponentTaskPanel.tree](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#a8bf67d0d3fc4b9dc7afa38bc9bdf0f75),
ArchRoof._RoofTaskPanel.tree,
[ArchSectionPlane.SectionPlaneTaskPanel.tree](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#ae2f456774b3f7209b1ce8407a72cfc98),
ArchWindow._ArchWindowTaskPanel.tree,
[DraftGui.FacebinderTaskPanel.tree](../../d2/d61/classDraftGui_1_1FacebinderTaskPanel.html#a0fd43fd796a2b9b32cb311f4f596ab63),
KDL::TreeFkSolverPos_recursive.tree, KDL::TreeIkSolverPos_NR_JL.tree,
KDL::TreeIkSolverVel_wdls.tree, and KDL::TreeJntToJacSolver.tree.

Referenced by
[ArchSchedule.ArchScheduleTaskPanel.export()](../../d5/da0/classArchSchedule_1_1ArchScheduleTaskPanel.html#afc8e0139c98920da44de6e077aba8138).

## ◆ getStandardButtons()

def ArchCommands.SurveyTaskPanel.getStandardButtons  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
## ◆ isAllowedAlterSelection()

def ArchCommands.SurveyTaskPanel.isAllowedAlterSelection  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
## ◆ isAllowedAlterView()

def ArchCommands.SurveyTaskPanel.isAllowedAlterView  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
## ◆ newline()

def ArchCommands.SurveyTaskPanel.newline  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _length_ = `0`,   
|  |  | _area_ = `0`  
| ) | |   
  
References
[ArchCommands.SurveyTaskPanel.descr](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#afd9964216a25519a3a80c49426ae6d0e),
[ArchCommands.SurveyTaskPanel.setText()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#ad3c7a67dea06fdb170bb7e6d76224b1e),
Gui::DockWnd::ComboView.tree, ArchAxis._AxisTaskPanel.tree,
[ArchAxisSystem.AxisSystemTaskPanel.tree](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a0c3edb65b15bb3281318dfdda901a2e3),
[ArchCommands.SurveyTaskPanel.tree](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a00907b1a9c07d5f90fa3a99f3111fc79),
[ArchComponent.ComponentTaskPanel.tree](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#a8bf67d0d3fc4b9dc7afa38bc9bdf0f75),
ArchRoof._RoofTaskPanel.tree,
[ArchSectionPlane.SectionPlaneTaskPanel.tree](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#ae2f456774b3f7209b1ce8407a72cfc98),
ArchWindow._ArchWindowTaskPanel.tree,
[DraftGui.FacebinderTaskPanel.tree](../../d2/d61/classDraftGui_1_1FacebinderTaskPanel.html#a0fd43fd796a2b9b32cb311f4f596ab63),
KDL::TreeFkSolverPos_recursive.tree, KDL::TreeIkSolverPos_NR_JL.tree,
KDL::TreeIkSolverVel_wdls.tree, and KDL::TreeJntToJacSolver.tree.

## ◆ reject()

def ArchCommands.SurveyTaskPanel.reject  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Referenced by
[draftguitools.gui_hatch.Draft_Hatch_TaskPanel.accept()](../../d1/d6e/classdraftguitools_1_1gui__hatch_1_1Draft__Hatch__TaskPanel.html#a233bb1c01579f1e00acc06984efec11a),
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel.accept()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#ae0e2ec6f40370c732beb919549a0111d),
[drafttaskpanels.task_shapestring.ShapeStringTaskPanelCmd.accept()](../../df/d8e/classdrafttaskpanels_1_1task__shapestring_1_1ShapeStringTaskPanelCmd.html#ac1562e837c0659251e16a2a5b7796cf2),
[drafttaskpanels.task_shapestring.ShapeStringTaskPanelEdit.accept()](../../d7/da9/classdrafttaskpanels_1_1task__shapestring_1_1ShapeStringTaskPanelEdit.html#a9201c29e738ab0b73095e222421cdfc3),
[drafttaskpanels.task_shapestring.ShapeStringTaskPanel.action()](../../d9/d1e/classdrafttaskpanels_1_1task__shapestring_1_1ShapeStringTaskPanel.html#aff179367fdb60160feb642c72ea17465),
[femexamples.examplesgui.FemExamples.clicked()](../../d2/db9/classfemexamples_1_1examplesgui_1_1FemExamples.html#ad3b96de3e075bb69e51539a3c99dfd14),
and
[PathScripts.PathToolBitLibraryGui.ToolBitLibrary.toolEdit()](../../dd/d3a/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitLibrary.html#ac20855be381c22621c17d3df63458595).

## ◆ retranslateUi()

def ArchCommands.SurveyTaskPanel.retranslateUi  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _dlg_  
| ) | |   
  
References
[Gui::Dialog::Ui_DlgChooseIcon.addButton](../../d2/d80/classGui_1_1Dialog_1_1Ui__DlgChooseIcon.html#aca6108c2d4476d6a470423b8ed38b7ab),
Gui::Dialog::IconFolders.addButton, Gui::ActionSelector.addButton,
ArchAxis._AxisTaskPanel.addButton,
[ArchAxisSystem.AxisSystemTaskPanel.addButton](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#aa8b0f409fb40c4895564912e95ed1495),
[ArchCommands.SurveyTaskPanel.addButton](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a0a6a52090b3e7f8e3f93b9cc4e9c01a8),
[ArchComponent.ComponentTaskPanel.addButton](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#ae54b414f55b1921e460d0d363b7a8129),
[ArchSectionPlane.SectionPlaneTaskPanel.addButton](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#a143989373655901f4df66126c77cb703),
ArchWindow._ArchWindowTaskPanel.addButton,
[DraftGui.FacebinderTaskPanel.addButton](../../d2/d61/classDraftGui_1_1FacebinderTaskPanel.html#a06b93330622fcc3c81444170f66782f2),
[MeshGui::Ui_RemeshGmsh.clearButton](../../df/deb/classMeshGui_1_1Ui__RemeshGmsh.html#aa36569ab3584e05ae08e2283a98ad551),
Gui::Dialog::DlgCustomizeSpaceball.clearButton,
[ArchCommands.SurveyTaskPanel.clearButton](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a476d6e01eadb9c172cf059d0481a8ebe),
[ArchCommands.SurveyTaskPanel.copyArea](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a4bf4f54edb7dae185229cd580c8b9b2f),
[ArchCommands.SurveyTaskPanel.copyLength](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#aa67013cbf8d7b4f4b1d6fa48c937856f),
[ArchCommands.SurveyTaskPanel.export](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#ae882a1934ee25e38683b82cd4f27c79f),
[ArchSchedule.ArchScheduleTaskPanel.export()](../../d5/da0/classArchSchedule_1_1ArchScheduleTaskPanel.html#afc8e0139c98920da44de6e077aba8138),
[PathScripts.PathPostProcessor.PostProcessor.export()](../../d2/d58/classPathScripts_1_1PathPostProcessor_1_1PostProcessor.html#a95038d6e936f32f44317ed7cded4f569),
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
[ArchCommands.SurveyTaskPanel.setText()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#ad3c7a67dea06fdb170bb7e6d76224b1e),
Gui::DockWnd::ComboView.tree, ArchAxis._AxisTaskPanel.tree,
[ArchAxisSystem.AxisSystemTaskPanel.tree](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a0c3edb65b15bb3281318dfdda901a2e3),
[ArchCommands.SurveyTaskPanel.tree](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a00907b1a9c07d5f90fa3a99f3111fc79),
[ArchComponent.ComponentTaskPanel.tree](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#a8bf67d0d3fc4b9dc7afa38bc9bdf0f75),
ArchRoof._RoofTaskPanel.tree,
[ArchSectionPlane.SectionPlaneTaskPanel.tree](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#ae2f456774b3f7209b1ce8407a72cfc98),
ArchWindow._ArchWindowTaskPanel.tree,
[DraftGui.FacebinderTaskPanel.tree](../../d2/d61/classDraftGui_1_1FacebinderTaskPanel.html#a0fd43fd796a2b9b32cb311f4f596ab63),
KDL::TreeFkSolverPos_recursive.tree, KDL::TreeIkSolverPos_NR_JL.tree,
KDL::TreeIkSolverVel_wdls.tree, and KDL::TreeJntToJacSolver.tree.

Referenced by
[ArchGrid.ArchGridTaskPanel.addColumn()](../../d6/da7/classArchGrid_1_1ArchGridTaskPanel.html#a3bd6a2518fda6a52f2f15a46e8d1fefb),
[ArchGrid.ArchGridTaskPanel.addRow()](../../d6/da7/classArchGrid_1_1ArchGridTaskPanel.html#ac8b2ccdd8b7d2673eb1e8eb6f7299609),
[ArchGrid.ArchGridTaskPanel.delColumn()](../../d6/da7/classArchGrid_1_1ArchGridTaskPanel.html#a858f41da98bab48d6b4bb6c0e976767b),
[ArchGrid.ArchGridTaskPanel.delRow()](../../d6/da7/classArchGrid_1_1ArchGridTaskPanel.html#a4f33342adae96fc721fbaefe33665fd4),
[DraftGui.DraftToolBar.taskUi()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a4193c3e4772bfcf1ed7ac11daeffa9fa),
[ArchAxisSystem.AxisSystemTaskPanel.update()](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a376cbba2ccee6efd86c46d0f0a8e99e3),
[ArchComponent.ComponentTaskPanel.update()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#af95b36032a3837b4bf1b92fe7c6a47e0),
[ArchSectionPlane.SectionPlaneTaskPanel.update()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#aab4bcd7b08950b8e3b37d801381c5162),
and
[DraftGui.FacebinderTaskPanel.update()](../../d2/d61/classDraftGui_1_1FacebinderTaskPanel.html#a191f43aa777ae22c42a00d118688bafe).

## ◆ setDescr()

def ArchCommands.SurveyTaskPanel.setDescr  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _item_ ,   
|  |  | _col_  
| ) | |   
  
References
[ArchCommands.SurveyTaskPanel.descr](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#afd9964216a25519a3a80c49426ae6d0e),
and
[ArchCommands.SurveyTaskPanel.setText()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#ad3c7a67dea06fdb170bb7e6d76224b1e).

## ◆ setText()

def ArchCommands.SurveyTaskPanel.setText  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[ArchCommands.SurveyTaskPanel.descr](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#afd9964216a25519a3a80c49426ae6d0e),
[ArchCommands.SurveyTaskPanel.setText()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#ad3c7a67dea06fdb170bb7e6d76224b1e),
Gui::DockWnd::ComboView.tree, ArchAxis._AxisTaskPanel.tree,
[ArchAxisSystem.AxisSystemTaskPanel.tree](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a0c3edb65b15bb3281318dfdda901a2e3),
[ArchCommands.SurveyTaskPanel.tree](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a00907b1a9c07d5f90fa3a99f3111fc79),
[ArchComponent.ComponentTaskPanel.tree](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#a8bf67d0d3fc4b9dc7afa38bc9bdf0f75),
ArchRoof._RoofTaskPanel.tree,
[ArchSectionPlane.SectionPlaneTaskPanel.tree](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#ae2f456774b3f7209b1ce8407a72cfc98),
ArchWindow._ArchWindowTaskPanel.tree,
[DraftGui.FacebinderTaskPanel.tree](../../d2/d61/classDraftGui_1_1FacebinderTaskPanel.html#a0fd43fd796a2b9b32cb311f4f596ab63),
KDL::TreeFkSolverPos_recursive.tree, KDL::TreeIkSolverPos_NR_JL.tree,
KDL::TreeIkSolverVel_wdls.tree, and KDL::TreeJntToJacSolver.tree.

Referenced by
[ArchCommands.SurveyTaskPanel.clipArea()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a1b8288364a10a547a60fd6f31f1a905b),
[ArchCommands.SurveyTaskPanel.clipLength()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a92d5adcd70e03694fd7b1372c451c523),
[ArchCommands.SurveyTaskPanel.newline()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a57d6b27250bfa8a1a2e74be167af7bda),
[ArchCommands.SurveyTaskPanel.retranslateUi()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a80aefc6bf17d60c63cd66e8984616d4b),
[ArchCommands.SurveyTaskPanel.setDescr()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a50b3c7eab9fe04cc2dac1cff7ded7e3a),
and
[ArchCommands.SurveyTaskPanel.setText()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#ad3c7a67dea06fdb170bb7e6d76224b1e).

## ◆ update()

def ArchCommands.SurveyTaskPanel.update  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _column_ ,   
|  |  | _txt_  
| ) | |   
  
References Gui::DockWnd::ComboView.tree, ArchAxis._AxisTaskPanel.tree,
[ArchAxisSystem.AxisSystemTaskPanel.tree](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a0c3edb65b15bb3281318dfdda901a2e3),
[ArchCommands.SurveyTaskPanel.tree](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a00907b1a9c07d5f90fa3a99f3111fc79),
[ArchComponent.ComponentTaskPanel.tree](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#a8bf67d0d3fc4b9dc7afa38bc9bdf0f75),
ArchRoof._RoofTaskPanel.tree,
[ArchSectionPlane.SectionPlaneTaskPanel.tree](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#ae2f456774b3f7209b1ce8407a72cfc98),
ArchWindow._ArchWindowTaskPanel.tree,
[DraftGui.FacebinderTaskPanel.tree](../../d2/d61/classDraftGui_1_1FacebinderTaskPanel.html#a0fd43fd796a2b9b32cb311f4f596ab63),
KDL::TreeFkSolverPos_recursive.tree, KDL::TreeIkSolverPos_NR_JL.tree,
KDL::TreeIkSolverVel_wdls.tree, KDL::TreeJntToJacSolver.tree, and
[draftutils.utils.utf8_decode()](../../de/d75/group__draftutils.html#ga65481f0e89b6495a5ea0c7a428fc7cb7).

Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[ArchAxisSystem.AxisSystemTaskPanel.addElement()](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a68544065aac91fa78a8bddb3e6ed5a99),
[ArchComponent.ComponentTaskPanel.addElement()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#a21a385085defc9e8ccca8b2261a57314),
[ArchSectionPlane.SectionPlaneTaskPanel.addElement()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#a6317c0ca7eb0c28e60b863f96ddeb81f),
[DraftGui.FacebinderTaskPanel.addElement()](../../d2/d61/classDraftGui_1_1FacebinderTaskPanel.html#a7642fdc6d6fa90afec25930af3b0a66e),
[femtaskpanels.task_result_mechanical._TaskPanel.calculate()](../../d1/d11/classfemtaskpanels_1_1task__result__mechanical_1_1__TaskPanel.html#aa2b98b5a9e12d62038ea9cc00366ecb6),
[Spreadsheet_legacy.SpreadsheetView.changeCell()](../../d7/d03/classSpreadsheet__legacy_1_1SpreadsheetView.html#a897cda21a4a4f34431c371a31579706e),
[draftguitools.gui_edit.Edit.endEditing()](../../d8/d68/classdraftguitools_1_1gui__edit_1_1Edit.html#ab9797631ba43c7855016e2552c21834f),
[draftguitools.gui_trackers.boxTracker.height()](../../d5/dca/classdraftguitools_1_1gui__trackers_1_1boxTracker.html#a25f7d7bbd56b5ff5ef5da124e515dd00),
[draftguitools.gui_trackers.rectangleTracker.p3()](../../d7/d8d/classdraftguitools_1_1gui__trackers_1_1rectangleTracker.html#a1bf47cdde1ea165a58946f1a5fdc6c8e),
[Plot.Plot.plot()](../../d3/d54/classPlot_1_1Plot.html#a8b670f38324a7fae1c7128e117cba688),
[Spreadsheet_legacy.SpreadsheetView.recompute()](../../d7/d03/classSpreadsheet__legacy_1_1SpreadsheetView.html#a1d8b8256ad183347aedaf40a269c2d3a),
[ArchAxisSystem.AxisSystemTaskPanel.removeElement()](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a27e3fe8ffbc52acfd92f2d333626a76d),
[ArchComponent.ComponentTaskPanel.removeElement()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#ad9d18ffd3ef7556affab6b62a6acceb5),
[ArchSectionPlane.SectionPlaneTaskPanel.removeElement()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#a544dbf3def03e06b86e6f32c390fd46a),
[DraftGui.FacebinderTaskPanel.removeElement()](../../d2/d61/classDraftGui_1_1FacebinderTaskPanel.html#a8ce5c644e81d1fbb3907e351e2050a0a),
[draftguitools.gui_trackers.gridTracker.reset()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#a2c6f7e1d0a817adacef8297962691a9c),
[ArchNesting.Nester.run()](../../d0/df4/classArchNesting_1_1Nester.html#af4bd331488aca3d29d5ade158e30b102),
[draftguitools.gui_trackers.gridTracker.setMainlines()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#ac1c96a4a6282724211bc61a37ffa5a05),
[draftguitools.gui_trackers.gridTracker.setSize()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#a6bb2d86a97781159c083a23a30f9fb9a),
[draftguitools.gui_trackers.gridTracker.setSpacing()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#a67fe5637d9f2b95d4c6c6a717f41e6e4),
and
[draftguitools.gui_edit_arch_objects.ArchWallGuiTools.update_object_from_edit_points()](../../d1/d46/classdraftguitools_1_1gui__edit__arch__objects_1_1ArchWallGuiTools.html#a1340bdc87e40eb0a04ba856255ae0f93).

## Member Data Documentation

## ◆ addButton

ArchCommands.SurveyTaskPanel.addButton  
---  
  
Referenced by
[ArchComponent.ComponentTaskPanel.check()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#a42457d57c57858913a567235656a6792),
[ArchCommands.SurveyTaskPanel.retranslateUi()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a80aefc6bf17d60c63cd66e8984616d4b),
[ArchAxisSystem.AxisSystemTaskPanel.retranslateUi()](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a2df79c4ca31ab9fadfa023c68f37fac2),
[ArchComponent.ComponentTaskPanel.retranslateUi()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#ab850764046f470d1a25650ab9c22c05a),
[ArchSectionPlane.SectionPlaneTaskPanel.retranslateUi()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#a6df215e0eb75725cf271449452684c20),
and
[DraftGui.FacebinderTaskPanel.retranslateUi()](../../d2/d61/classDraftGui_1_1FacebinderTaskPanel.html#a55e80e032ef5765677d4c987c3fdb301).

## ◆ clearButton

ArchCommands.SurveyTaskPanel.clearButton  
---  
  
Referenced by
[ArchCommands.SurveyTaskPanel.retranslateUi()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a80aefc6bf17d60c63cd66e8984616d4b).

## ◆ copyArea

ArchCommands.SurveyTaskPanel.copyArea  
---  
  
Referenced by
[ArchCommands.SurveyTaskPanel.retranslateUi()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a80aefc6bf17d60c63cd66e8984616d4b).

## ◆ copyLength

ArchCommands.SurveyTaskPanel.copyLength  
---  
  
Referenced by
[ArchCommands.SurveyTaskPanel.retranslateUi()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a80aefc6bf17d60c63cd66e8984616d4b).

## ◆ descr

ArchCommands.SurveyTaskPanel.descr  
---  
  
Referenced by
[ArchCommands.SurveyTaskPanel.newline()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a57d6b27250bfa8a1a2e74be167af7bda),
[ArchCommands.SurveyTaskPanel.setDescr()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a50b3c7eab9fe04cc2dac1cff7ded7e3a),
and
[ArchCommands.SurveyTaskPanel.setText()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#ad3c7a67dea06fdb170bb7e6d76224b1e).

## ◆ export

ArchCommands.SurveyTaskPanel.export  
---  
  
Referenced by
[ArchCommands.SurveyTaskPanel.retranslateUi()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a80aefc6bf17d60c63cd66e8984616d4b).

## ◆ form

ArchCommands.SurveyTaskPanel.form  
---  
  
Referenced by
[ArchSchedule.ArchScheduleTaskPanel.accept()](../../d5/da0/classArchSchedule_1_1ArchScheduleTaskPanel.html#a047247bc36058abe94435197f9599c86),
[draftguitools.gui_hatch.Draft_Hatch_TaskPanel.accept()](../../d1/d6e/classdraftguitools_1_1gui__hatch_1_1Draft__Hatch__TaskPanel.html#a233bb1c01579f1e00acc06984efec11a),
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel.accept()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#ae0e2ec6f40370c732beb919549a0111d),
[drafttaskpanels.task_shapestring.ShapeStringTaskPanelEdit.accept()](../../d7/da9/classdrafttaskpanels_1_1task__shapestring_1_1ShapeStringTaskPanelEdit.html#a9201c29e738ab0b73095e222421cdfc3),
[Mod.PartDesign.WizardShaft.WizardShaft.TaskWizardShaft.accept()](../../d9/dde/classMod_1_1PartDesign_1_1WizardShaft_1_1WizardShaft_1_1TaskWizardShaft.html#a1c59e848f832a1827818047a21546702),
[PathScripts.PathJobGui.StockEdit.activate()](../../d4/dbf/classPathScripts_1_1PathJobGui_1_1StockEdit.html#a08560f4efb13bfcc18690474049d0dec),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.Activated()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#ac7fe745faef8d402397cb0641e130965),
[ArchSchedule.ArchScheduleTaskPanel.add()](../../d5/da0/classArchSchedule_1_1ArchScheduleTaskPanel.html#adedc500f9bb32916e7edc8f6fec0cacb),
[OpenSCADCommands.AddSCADTask.addelement()](../../d5/d9d/classOpenSCADCommands_1_1AddSCADTask.html#a4df377bda136cbd7a53692b1e208d03b),
[TaskPanel.TaskPanel.addElement()](../../d3/da6/classTaskPanel_1_1TaskPanel.html#aebbaaf9f220f5dad762235f82b68ebf8),
[AttachmentEditor.TaskAttachmentEditor.AttachmentEditorTaskPanel.addSelection()](../../d8/d4c/classAttachmentEditor_1_1TaskAttachmentEditor_1_1AttachmentEditorTaskPanel.html#aaa42ce1862ba2b811d8b78e5f90c6baf),
[AttachmentEditor.TaskAttachmentEditor.AttachmentEditorTaskPanel.attachmentOffsetChanged()](../../d8/d4c/classAttachmentEditor_1_1TaskAttachmentEditor_1_1AttachmentEditorTaskPanel.html#a8fff02fcd77197d71d886c9e3e4992a1),
[PathScripts.PathPreferencesPathJob.JobPreferencesPage.bestGuessForFilePath()](../../db/dec/classPathScripts_1_1PathPreferencesPathJob_1_1JobPreferencesPage.html#a356e7f3c0943c051aba50eb54669810a),
[PathScripts.PathPreferencesPathJob.JobPreferencesPage.browseDefaultFilePath()](../../db/dec/classPathScripts_1_1PathPreferencesPathJob_1_1JobPreferencesPage.html#a8bb6c5d4083fdc1f628295c5b86eee32),
[PathScripts.PathPreferencesPathJob.JobPreferencesPage.browseDefaultJobTemplate()](../../db/dec/classPathScripts_1_1PathPreferencesPathJob_1_1JobPreferencesPage.html#a8f452361b39656c0c61bcb3ed26f3cbb),
[PathScripts.PathPreferencesPathJob.JobPreferencesPage.browseOutputFile()](../../db/dec/classPathScripts_1_1PathPreferencesPathJob_1_1JobPreferencesPage.html#a90a000381844dc708d578dc1ad22abf5),
[PathScripts.PathCamoticsGui.CAMoticsUI.calculating()](../../d2/df4/classPathScripts_1_1PathCamoticsGui_1_1CAMoticsUI.html#aeb66d2c521cf46490c052ae71a4a5a85),
[femtaskpanels.task_solver_ccxtools._TaskPanel.calculixFinished()](../../da/df4/classfemtaskpanels_1_1task__solver__ccxtools_1_1__TaskPanel.html#a6e21e27d9dc2fef551c5382b141ec5e4),
[femtaskpanels.task_solver_ccxtools._TaskPanel.calculixStarted()](../../da/df4/classfemtaskpanels_1_1task__solver__ccxtools_1_1__TaskPanel.html#a19a89a73ffa2ad3700d93ce879a670e3),
[femtaskpanels.task_solver_ccxtools._TaskPanel.check_prerequisites_helper()](../../da/df4/classfemtaskpanels_1_1task__solver__ccxtools_1_1__TaskPanel.html#a4be4ead63889a74287fde974266b5dbb),
[AttachmentEditor.TaskAttachmentEditor.AttachmentEditorTaskPanel.checkBoxFlipClicked()](../../d8/d4c/classAttachmentEditor_1_1TaskAttachmentEditor_1_1AttachmentEditorTaskPanel.html#afe4883fe024eb935894215113cd38b05),
[Mod.PartDesign.FeatureHole.TaskHole.TaskHole.checkCustom()](../../d1/d14/classMod_1_1PartDesign_1_1FeatureHole_1_1TaskHole_1_1TaskHole.html#a81a114cc07123782bf4ecc160627ab06),
[Mod.PartDesign.FeatureHole.TaskHole.TaskHole.checkCustomThreadLength()](../../d1/d14/classMod_1_1PartDesign_1_1FeatureHole_1_1TaskHole_1_1TaskHole.html#a61e14ae8f0e64ce2c7c065481992f228),
[PathScripts.PathCircularHoleBaseGui.TaskPanelHoleGeometryPage.checkedChanged()](../../d3/dfd/classPathScripts_1_1PathCircularHoleBaseGui_1_1TaskPanelHoleGeometryPage.html#ac538e1717e10b8ace7b0c353cc843ad9),
[PathScripts.PathJobGui.StockFromBaseBoundBoxEdit.checkXpos()](../../d6/df2/classPathScripts_1_1PathJobGui_1_1StockFromBaseBoundBoxEdit.html#a4ad434484564e9929de29562dc322aab),
[PathScripts.PathJobGui.StockFromBaseBoundBoxEdit.checkYpos()](../../d6/df2/classPathScripts_1_1PathJobGui_1_1StockFromBaseBoundBoxEdit.html#a9a88e428c7b0903c864727f94cc5d090),
[PathScripts.PathJobGui.StockFromBaseBoundBoxEdit.checkZpos()](../../d6/df2/classPathScripts_1_1PathJobGui_1_1StockFromBaseBoundBoxEdit.html#aafddd934154ef1ed7d745068d0e8d747),
[femtaskpanels.task_mesh_gmsh._TaskPanel.choose_dimension()](../../d6/d90/classfemtaskpanels_1_1task__mesh__gmsh_1_1__TaskPanel.html#a38fd2105dcbfe9ea0ed33aa09e7423f4),
[femtaskpanels.task_mesh_gmsh._TaskPanel.choose_order()](../../d6/d90/classfemtaskpanels_1_1task__mesh__gmsh_1_1__TaskPanel.html#a1675090caa83cf98146c3ebcf59f482d),
[femtaskpanels.task_solver_ccxtools._TaskPanel.choose_working_dir()](../../da/df4/classfemtaskpanels_1_1task__solver__ccxtools_1_1__TaskPanel.html#a2cebc14b77d64b9658641ebcc7c0b43e),
[ArchReference.ArchReferenceTaskPanel.chooseFile()](../../d4/d73/classArchReference_1_1ArchReferenceTaskPanel.html#adf36d52dcd143c0e0bd4fb23c77d5672),
[PathScripts.PathToolBitLibraryGui.ToolBitLibrary.cleanupDocument()](../../dd/d3a/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitLibrary.html#a16dfbcd6d2fd6beb762bb5af51276b86),
[ArchSchedule.ArchScheduleTaskPanel.clear()](../../d5/da0/classArchSchedule_1_1ArchScheduleTaskPanel.html#a91a81c217aab4441e4b426dc51948a6b),
[Mod.PartDesign.FeatureHole.TaskHole.TaskHole.comboFinishNorm()](../../d1/d14/classMod_1_1PartDesign_1_1FeatureHole_1_1TaskHole_1_1TaskHole.html#a06d12223f063ced1404b564f6a8a3b7b),
[Mod.PartDesign.FeatureHole.TaskHole.TaskHole.comboNorm()](../../d1/d14/classMod_1_1PartDesign_1_1FeatureHole_1_1TaskHole_1_1TaskHole.html#a18b3cb88a3060c69cecfc7c31dd593d3),
[Mod.PartDesign.FeatureHole.TaskHole.TaskHole.comboNormBoltWasher()](../../d1/d14/classMod_1_1PartDesign_1_1FeatureHole_1_1TaskHole_1_1TaskHole.html#a2f98bca83aaa1964323b148cf0f5d851),
[Mod.PartDesign.FeatureHole.TaskHole.TaskHole.comboNormDia()](../../d1/d14/classMod_1_1PartDesign_1_1FeatureHole_1_1TaskHole_1_1TaskHole.html#ada30eefb8187aa37ce44cbf64dea6773),
[Mod.PartDesign.FeatureHole.TaskHole.TaskHole.comboThreadDia()](../../d1/d14/classMod_1_1PartDesign_1_1FeatureHole_1_1TaskHole_1_1TaskHole.html#aabe36f9adf58f06f8af2337e7f159899),
[Mod.PartDesign.FeatureHole.TaskHole.TaskHole.comboThreadNorm()](../../d1/d14/classMod_1_1PartDesign_1_1FeatureHole_1_1TaskHole_1_1TaskHole.html#a63af946d20d85079ee5279d31e1ececc),
[Mod.PartDesign.FeatureHole.TaskHole.TaskHole.comboTolerance()](../../d1/d14/classMod_1_1PartDesign_1_1FeatureHole_1_1TaskHole_1_1TaskHole.html#a6c5c3e54c1ba89d065ef8e2454785213),
[PathPythonGui.simple_edit_panel.SimpleEditPanel.connectWidget()](../../d4/d29/classPathPythonGui_1_1simple__edit__panel_1_1SimpleEditPanel.html#a76b0a015d9b1936a00f2ab12a442910e),
[femtaskpanels.task_mesh_gmsh._TaskPanel.console_log()](../../d6/d90/classfemtaskpanels_1_1task__mesh__gmsh_1_1__TaskPanel.html#a26161f4dcc802a29e4ce408765295f96),
[feminout.importFenicsMesh.WriteXDMFTaskPanel.convert_fem_mesh_obj_to_table()](../../d4/d1a/classfeminout_1_1importFenicsMesh_1_1WriteXDMFTaskPanel.html#ae1664b9cca1d848b36613a2910d9b20b),
[feminout.importFenicsMesh.WriteXDMFTaskPanel.convert_table_to_group_dict()](../../d4/d1a/classfeminout_1_1importFenicsMesh_1_1WriteXDMFTaskPanel.html#a6bbd8d26f0fad57aa577b65a4c7f8044),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.copyNewTags()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#a4f58c524d66aeb0d056034443152b8a7),
[PathScripts.PathToolLibraryEditor.EditorPanel.copyTools()](../../d0/d92/classPathScripts_1_1PathToolLibraryEditor_1_1EditorPanel.html#a7a220589b29f57010e038397eed16a6e),
[PathScripts.PathPropertyBagGui.PropertyCreate.createAnother()](../../dd/d6e/classPathScripts_1_1PathPropertyBagGui_1_1PropertyCreate.html#ac37f777cc672d5af32d2e3c533183c9c),
[PathScripts.PathFeatureExtensionsGui.TaskPanelExtensionPage.createItemForBaseModel()](../../d0/de3/classPathScripts_1_1PathFeatureExtensionsGui_1_1TaskPanelExtensionPage.html#ab5d487f9cf952c3a83c17d2e82dcec80),
[drafttaskpanels.task_shapestring.ShapeStringTaskPanelCmd.createObject()](../../df/d8e/classdrafttaskpanels_1_1task__shapestring_1_1ShapeStringTaskPanelCmd.html#a2bf73c981ede5444c97bd0d33af8eace),
[PathScripts.PathFeatureExtensionsGui.TaskPanelExtensionPage.currentExtensions()](../../d0/de3/classPathScripts_1_1PathFeatureExtensionsGui_1_1TaskPanelExtensionPage.html#a4b6043e18d5e47c50c9f00458b5237c3),
[PathScripts.PathSlotGui.TaskPanelOpPage.customizeReference_1()](../../d2/da9/classPathScripts_1_1PathSlotGui_1_1TaskPanelOpPage.html#a044524cdce8fd5b4f33e581bcdefbe2d),
[PathScripts.PathSlotGui.TaskPanelOpPage.customizeReference_2()](../../d2/da9/classPathScripts_1_1PathSlotGui_1_1TaskPanelOpPage.html#acbdbb4ab2d39f15281f294795f79d9e3),
[PathScripts.PathToolLibraryEditor.EditorPanel.delete()](../../d0/d92/classPathScripts_1_1PathToolLibraryEditor_1_1EditorPanel.html#a407eba847af9dbe2892951952ae597d6),
[PathScripts.PathCircularHoleBaseGui.TaskPanelHoleGeometryPage.deleteBase()](../../d3/dfd/classPathScripts_1_1PathCircularHoleBaseGui_1_1TaskPanelHoleGeometryPage.html#afc7852e3360116cbd33d2c3addfa1242),
[PathScripts.PathOpGui.TaskPanelBaseGeometryPage.deleteBase()](../../d4/dfc/classPathScripts_1_1PathOpGui_1_1TaskPanelBaseGeometryPage.html#a6ecdbbc084e5ffd89c64cf71f71ab968),
[drafttaskpanels.task_circulararray.TaskPanelCircularArray.display_point()](../../dd/d3a/classdrafttaskpanels_1_1task__circulararray_1_1TaskPanelCircularArray.html#ada109ed8aee6922b7c210f499b153837),
[drafttaskpanels.task_polararray.TaskPanelPolarArray.display_point()](../../d7/d8d/classdrafttaskpanels_1_1task__polararray_1_1TaskPanelPolarArray.html#af2f2f783903669fbd4719485a1a80d86),
[OpenSCADCommands.OpenSCADMeshBooleanTask.doboolean()](../../d7/d91/classOpenSCADCommands_1_1OpenSCADMeshBooleanTask.html#a1e2670e38c9769c9b186364e8da0ba75),
[PathScripts.PathToolLibraryEditor.EditorPanel.duplicate()](../../d0/d92/classPathScripts_1_1PathToolLibraryEditor_1_1EditorPanel.html#ae248f0ce6ee8ed5cf36687b54ecb697f),
[PathScripts.PathJobGui.StockFromBaseBoundBoxEdit.editorFrame()](../../d6/df2/classPathScripts_1_1PathJobGui_1_1StockFromBaseBoundBoxEdit.html#ac8be7f749f7654f160db84ba1d0285c3),
[PathScripts.PathJobGui.StockCreateBoxEdit.editorFrame()](../../db/dde/classPathScripts_1_1PathJobGui_1_1StockCreateBoxEdit.html#afcae9ab74f60f46bbdceed0e6871c5a8),
[PathScripts.PathJobGui.StockCreateCylinderEdit.editorFrame()](../../d8/dc0/classPathScripts_1_1PathJobGui_1_1StockCreateCylinderEdit.html#a6e221c640393205020f7b76b376a23d3),
[PathScripts.PathJobGui.StockFromExistingEdit.editorFrame()](../../d8/d19/classPathScripts_1_1PathJobGui_1_1StockFromExistingEdit.html#aace20f771f722b129664270319aef573),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.editSelectedTag()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#aeb54b2a05ef9484b7cbcbe96eff52c85),
[PathScripts.PathToolLibraryEditor.EditorPanel.editTool()](../../d0/d92/classPathScripts_1_1PathToolLibraryEditor_1_1EditorPanel.html#ad6de8dfedd9c77a1d0dc9a8dc75637cc),
[PathScripts.PathToolBitLibraryGui.ToolBitSelector.enableButtons()](../../d8/d6e/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitSelector.html#a15b93af7861b14dee9954a63b58eabd1),
[PathScripts.PathPropertyBagGui.PropertyCreate.exec_()](../../dd/d6e/classPathScripts_1_1PathPropertyBagGui_1_1PropertyCreate.html#a30fb811b4868844918ab3a84651e84ce),
[PathScripts.PathToolLibraryEditor.EditorPanel.exportFile()](../../d0/d92/classPathScripts_1_1PathToolLibraryEditor_1_1EditorPanel.html#a32e590d955cb1eb38ebf1ded5b5cbc84),
[femtaskpanels.task_solver_ccxtools._TaskPanel.femConsoleMessage()](../../da/df4/classfemtaskpanels_1_1task__solver__ccxtools_1_1__TaskPanel.html#a47f08070e23d7fb33fb97b96a82bafac),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.fill_editor()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#a82c7c22dfe901c7297d64f3a715ffc11),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.generateNewTags()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#a4ee0905fd28a840812ab0d24ae677fb5),
[drafttaskpanels.task_circulararray.TaskPanelCircularArray.get_center()](../../dd/d3a/classdrafttaskpanels_1_1task__circulararray_1_1TaskPanelCircularArray.html#a7f5bd5afe9ee9d74e6af1a132175df6e),
[drafttaskpanels.task_polararray.TaskPanelPolarArray.get_center()](../../d7/d8d/classdrafttaskpanels_1_1task__polararray_1_1TaskPanelPolarArray.html#ac2ac44d835d817df65583cd0c2299f18),
[drafttaskpanels.task_circulararray.TaskPanelCircularArray.get_distances()](../../dd/d3a/classdrafttaskpanels_1_1task__circulararray_1_1TaskPanelCircularArray.html#a0dc7fc31e7071f384cf9fd95c241e8b1),
[drafttaskpanels.task_orthoarray.TaskPanelOrthoArray.get_intervals()](../../d6/dfa/classdrafttaskpanels_1_1task__orthoarray_1_1TaskPanelOrthoArray.html#a2b1e4eaa4150bb43b3bb757c80ec17d5),
[drafttaskpanels.task_polararray.TaskPanelPolarArray.get_number_angle()](../../d7/d8d/classdrafttaskpanels_1_1task__polararray_1_1TaskPanelPolarArray.html#adad1a7861811744eb74cb21c0683378b),
[drafttaskpanels.task_circulararray.TaskPanelCircularArray.get_number_symmetry()](../../dd/d3a/classdrafttaskpanels_1_1task__circulararray_1_1TaskPanelCircularArray.html#a2e8e7b4b817baae5af36d43d55982457),
[drafttaskpanels.task_orthoarray.TaskPanelOrthoArray.get_numbers()](../../d6/dfa/classdrafttaskpanels_1_1task__orthoarray_1_1TaskPanelOrthoArray.html#a6d7fe01e6a0ff4120447f833468cc2fd),
[ArchPanel.NestTaskPanel.getContainer()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#ad25ef9b5aade32a390de4a8bd34bafda),
[AttachmentEditor.TaskAttachmentEditor.AttachmentEditorTaskPanel.getCurrentMode()](../../d8/d4c/classAttachmentEditor_1_1TaskAttachmentEditor_1_1AttachmentEditorTaskPanel.html#a788dd3228ade4660e643733187513c04),
[PathScripts.PathDressupAxisMap.TaskPanel.getFields()](../../dd/de9/classPathScripts_1_1PathDressupAxisMap_1_1TaskPanel.html#a546edd51390be5e9a80243290709c8e2),
[PathScripts.PathDressupDogbone.TaskPanel.getFields()](../../df/d54/classPathScripts_1_1PathDressupDogbone_1_1TaskPanel.html#a885be1f42121c7194d93e970ec9fd5b8),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.getFields()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#aa8cc9a19c1ad1adb9e40aef3d1237458),
[PathScripts.PathJobGui.TaskPanel.getFields()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#a8269022e9a5e2c7fa16cbce8e4d0b874),
[PathScripts.PathSetupSheetGui.GlobalEditor.getFields()](../../de/df9/classPathScripts_1_1PathSetupSheetGui_1_1GlobalEditor.html#addbaf5a8db41a40121a6e2e085d56e96),
[PathScripts.PathAdaptiveGui.TaskPanelOpPage.getFields()](../../d4/d86/classPathScripts_1_1PathAdaptiveGui_1_1TaskPanelOpPage.html#a1f2d7f6c09e4f3855635fd42e3d1756e),
[PathScripts.PathCustomGui.TaskPanelOpPage.getFields()](../../de/d5c/classPathScripts_1_1PathCustomGui_1_1TaskPanelOpPage.html#a2273981faf16504dc3b180b2696daa10),
[PathScripts.PathDeburrGui.TaskPanelOpPage.getFields()](../../d8/d57/classPathScripts_1_1PathDeburrGui_1_1TaskPanelOpPage.html#a8d43eec4fa54a1e3f6549b4b16ced1b6),
[PathScripts.PathDrillingGui.TaskPanelOpPage.getFields()](../../d6/df8/classPathScripts_1_1PathDrillingGui_1_1TaskPanelOpPage.html#a0b4ddc2bed6d260368d47351aea6ec5c),
[PathScripts.PathEngraveGui.TaskPanelOpPage.getFields()](../../d9/de5/classPathScripts_1_1PathEngraveGui_1_1TaskPanelOpPage.html#acc6b835699f3d430d7cfcff18724cf4b),
[PathScripts.PathFeatureExtensionsGui.TaskPanelExtensionPage.getFields()](../../d0/de3/classPathScripts_1_1PathFeatureExtensionsGui_1_1TaskPanelExtensionPage.html#acd2e5e148212f4872e6067b388889f19),
[PathScripts.PathHelixGui.TaskPanelOpPage.getFields()](../../d5/d26/classPathScripts_1_1PathHelixGui_1_1TaskPanelOpPage.html#ac631c0bdd8677655c8b364fff0472827),
[PathScripts.PathJobGui.StockFromExistingEdit.getFields()](../../d8/d19/classPathScripts_1_1PathJobGui_1_1StockFromExistingEdit.html#a9c4820c09ef72435be5d9cfe98cc2b3b),
[PathScripts.PathPocketBaseGui.TaskPanelOpPage.getFields()](../../d1/d25/classPathScripts_1_1PathPocketBaseGui_1_1TaskPanelOpPage.html#a8fa2ca03de1c393f0cecf128f3b3a278),
[PathScripts.PathProbeGui.TaskPanelOpPage.getFields()](../../db/de4/classPathScripts_1_1PathProbeGui_1_1TaskPanelOpPage.html#a7975c6b06693c8d1047a979fe3dc9c4b),
[PathScripts.PathProfileGui.TaskPanelOpPage.getFields()](../../db/d54/classPathScripts_1_1PathProfileGui_1_1TaskPanelOpPage.html#a466cd8d259dd1262150e8ed976b756dc),
[PathScripts.PathSlotGui.TaskPanelOpPage.getFields()](../../d2/da9/classPathScripts_1_1PathSlotGui_1_1TaskPanelOpPage.html#ae59925bab6448e0662f90aca387f41a8),
[PathScripts.PathSurfaceGui.TaskPanelOpPage.getFields()](../../d7/d7a/classPathScripts_1_1PathSurfaceGui_1_1TaskPanelOpPage.html#ab4e4cc1ab44bf7668c4719036be87b60),
[PathScripts.PathThreadMillingGui.TaskPanelOpPage.getFields()](../../df/d59/classPathScripts_1_1PathThreadMillingGui_1_1TaskPanelOpPage.html#a15f1fd1b14c164dd424dc7750972b656),
[PathScripts.PathVcarveGui.TaskPanelOpPage.getFields()](../../d8/dc5/classPathScripts_1_1PathVcarveGui_1_1TaskPanelOpPage.html#a7f3ee7556a816440e35fa903699320ab),
[PathScripts.PathWaterlineGui.TaskPanelOpPage.getFields()](../../d3/dcf/classPathScripts_1_1PathWaterlineGui_1_1TaskPanelOpPage.html#adfea0b3d18cadda3985137e8498185fb),
[PathScripts.PathJobGui.StockCreateBoxEdit.getFields()](../../db/dde/classPathScripts_1_1PathJobGui_1_1StockCreateBoxEdit.html#a1943d75d9101cb076b9326156072d830),
[PathScripts.PathJobGui.StockCreateCylinderEdit.getFields()](../../d8/dc0/classPathScripts_1_1PathJobGui_1_1StockCreateCylinderEdit.html#a5e8c08202b607d06c589ab9efeded5ff),
[PathScripts.PathJobGui.StockFromBaseBoundBoxEdit.getFieldsStock()](../../d6/df2/classPathScripts_1_1PathJobGui_1_1StockFromBaseBoundBoxEdit.html#a4178daad6508f9f497cb6915838aa8f4),
[ArchPanel.NestTaskPanel.getShapes()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#a52edae24a9d124678d48b157749b5f04),
[PathScripts.PathAdaptiveGui.TaskPanelOpPage.getSignalsForUpdate()](../../d4/d86/classPathScripts_1_1PathAdaptiveGui_1_1TaskPanelOpPage.html#afe7b173d71f54bba63d6b954986550f6),
[PathScripts.PathCustomGui.TaskPanelOpPage.getSignalsForUpdate()](../../de/d5c/classPathScripts_1_1PathCustomGui_1_1TaskPanelOpPage.html#a6dd64b575f3834be9a57c691ad9338de),
[PathScripts.PathDeburrGui.TaskPanelOpPage.getSignalsForUpdate()](../../d8/d57/classPathScripts_1_1PathDeburrGui_1_1TaskPanelOpPage.html#aa600241c333b2bb1993a0c56daeae0cf),
[PathScripts.PathDrillingGui.TaskPanelOpPage.getSignalsForUpdate()](../../d6/df8/classPathScripts_1_1PathDrillingGui_1_1TaskPanelOpPage.html#a911f9db9adbd92d636f45b15168c36be),
[PathScripts.PathEngraveGui.TaskPanelOpPage.getSignalsForUpdate()](../../d9/de5/classPathScripts_1_1PathEngraveGui_1_1TaskPanelOpPage.html#a30c8525149a8d50dc6991c163a0e492b),
[PathScripts.PathFeatureExtensionsGui.TaskPanelExtensionPage.getSignalsForUpdate()](../../d0/de3/classPathScripts_1_1PathFeatureExtensionsGui_1_1TaskPanelExtensionPage.html#a4e7c8ff5f7981d5a2f75a6085a61cb2f),
[PathScripts.PathHelixGui.TaskPanelOpPage.getSignalsForUpdate()](../../d5/d26/classPathScripts_1_1PathHelixGui_1_1TaskPanelOpPage.html#ab33b85e746810df23b7ca5a5ce95fe74),
[PathScripts.PathOpGui.TaskPanelHeightsPage.getSignalsForUpdate()](../../d0/d65/classPathScripts_1_1PathOpGui_1_1TaskPanelHeightsPage.html#af6c4ba836fcb15a59281a602ad34d7a1),
[PathScripts.PathOpGui.TaskPanelDepthsPage.getSignalsForUpdate()](../../da/d1a/classPathScripts_1_1PathOpGui_1_1TaskPanelDepthsPage.html#aea712f685f9c9525487c8d9136302b6e),
[PathScripts.PathOpGui.TaskPanelDiametersPage.getSignalsForUpdate()](../../d1/d2e/classPathScripts_1_1PathOpGui_1_1TaskPanelDiametersPage.html#a8d33a18e087b09d3d545bcccecaa4e14),
[PathScripts.PathPocketBaseGui.TaskPanelOpPage.getSignalsForUpdate()](../../d1/d25/classPathScripts_1_1PathPocketBaseGui_1_1TaskPanelOpPage.html#a7ecd517ef4459158dafa92e67ab2fa15),
[PathScripts.PathProbeGui.TaskPanelOpPage.getSignalsForUpdate()](../../db/de4/classPathScripts_1_1PathProbeGui_1_1TaskPanelOpPage.html#ad9178e08e7e6d467fe21fe271c932b76),
[PathScripts.PathProfileGui.TaskPanelOpPage.getSignalsForUpdate()](../../db/d54/classPathScripts_1_1PathProfileGui_1_1TaskPanelOpPage.html#af911863ccbb3b1225ed76f2eaaab401d),
[PathScripts.PathSlotGui.TaskPanelOpPage.getSignalsForUpdate()](../../d2/da9/classPathScripts_1_1PathSlotGui_1_1TaskPanelOpPage.html#a41354b4d522ee1ac1541372e0d26c31c),
[PathScripts.PathSurfaceGui.TaskPanelOpPage.getSignalsForUpdate()](../../d7/d7a/classPathScripts_1_1PathSurfaceGui_1_1TaskPanelOpPage.html#a4df73d6d650ad78e1871731d5d02385f),
[PathScripts.PathThreadMillingGui.TaskPanelOpPage.getSignalsForUpdate()](../../df/d59/classPathScripts_1_1PathThreadMillingGui_1_1TaskPanelOpPage.html#ad06361feac8973d64db1919e01206f19),
[PathScripts.PathVcarveGui.TaskPanelOpPage.getSignalsForUpdate()](../../d8/dc5/classPathScripts_1_1PathVcarveGui_1_1TaskPanelOpPage.html#a4a623bcc88a9dd21eaea0fe9e5ab192a),
[PathScripts.PathWaterlineGui.TaskPanelOpPage.getSignalsForUpdate()](../../d3/dcf/classPathScripts_1_1PathWaterlineGui_1_1TaskPanelOpPage.html#a5dc089c5fd0ff2af4fe221b8eaf04a26),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.getTags()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#a07fef4c2e1cb107e60bc1338c0e49958),
[femsolver.elmer.equations.equation.ViewProxy.getTaskWidget()](../../d7/d0b/classfemsolver_1_1elmer_1_1equations_1_1equation_1_1ViewProxy.html#a767f86f8b9f344118769a0327f927767),
[PathScripts.PathToolLibraryEditor.EditorPanel.getToolTableByName()](../../d0/d92/classPathScripts_1_1PathToolLibraryEditor_1_1EditorPanel.html#a19824f6c29b51b857093c8ae0bd87be6),
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel.getValues()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#a00d7014f14cb4fd507c4951c2bd95f71),
[PathScripts.PathOpGui.TaskPanelBaseGeometryPage.importBaseGeometry()](../../d4/dfc/classPathScripts_1_1PathOpGui_1_1TaskPanelBaseGeometryPage.html#aa8d6373628f812b0726d74e561190062),
[ArchSchedule.ArchScheduleTaskPanel.importCSV()](../../d5/da0/classArchSchedule_1_1ArchScheduleTaskPanel.html#a8d97c69e4bdeda804455d4ca50b33482),
[PathScripts.PathToolLibraryEditor.EditorPanel.importFile()](../../d0/d92/classPathScripts_1_1PathToolLibraryEditor_1_1EditorPanel.html#abce1219a9e6838ec313209c6c9ee0794),
[PathScripts.PathCamoticsGui.CAMoticsUI.initializeUI()](../../d2/df4/classPathScripts_1_1PathCamoticsGui_1_1CAMoticsUI.html#aa810dda101898a0181888826455ed638),
[PathScripts.PathOpGui.TaskPanelHeightsPage.initPage()](../../d0/d65/classPathScripts_1_1PathOpGui_1_1TaskPanelHeightsPage.html#a29e2912f0af6e942ac6902c7843b61e7),
[PathScripts.PathOpGui.TaskPanelDepthsPage.initPage()](../../da/d1a/classPathScripts_1_1PathOpGui_1_1TaskPanelDepthsPage.html#a12a9620b0ca81ee94f8e516f5ceeae7c),
[PathScripts.PathCircularHoleBaseGui.TaskPanelHoleGeometryPage.itemActivated()](../../d3/dfd/classPathScripts_1_1PathCircularHoleBaseGui_1_1TaskPanelHoleGeometryPage.html#a60065a69d5a311b11d45faf3cc091570),
[PathScripts.PathOpGui.TaskPanelBaseGeometryPage.itemActivated()](../../d4/dfc/classPathScripts_1_1PathOpGui_1_1TaskPanelBaseGeometryPage.html#a63802742f547f29e7d68fe08edc33d5c),
[PathScripts.PathOpGui.TaskPanelBaseLocationPage.itemActivated()](../../d6/d50/classPathScripts_1_1PathOpGui_1_1TaskPanelBaseLocationPage.html#ab85baee40c48beff8a0fb8e5aefc991d),
[PathScripts.PathToolBitLibraryGui.ToolBitLibrary.libraryNew()](../../dd/d3a/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitLibrary.html#a8a99aba635052cf51fdb38fe878eb507),
[PathScripts.PathToolBitLibraryGui.ToolBitLibrary.libraryOk()](../../dd/d3a/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitLibrary.html#ae13a9fc57890abbf715f51501c531c04),
[PathScripts.PathToolBitLibraryGui.ToolBitLibrary.libraryPath()](../../dd/d3a/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitLibrary.html#ab68f9ce4e617283c8d6838f72def510b),
[PathScripts.PathToolBitLibraryGui.ToolBitLibrary.librarySaveAs()](../../dd/d3a/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitLibrary.html#aacc6b835c3257775d5683ff5c4494b27),
[PathScripts.PathToolBitLibraryGui.ToolBitSelector.loadData()](../../d8/d6e/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitSelector.html#a07483c07d79c32172ffccac7470cb325),
[PathScripts.PathToolBitLibraryGui.ToolBitLibrary.loadData()](../../dd/d3a/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitLibrary.html#ae2616669ba6b30e1833ff2d498cc2d6a),
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel.loadDefaults()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#a891f1e17c68d3e761fb4eb7839772ad7),
[OpenSCADCommands.AddSCADTask.loadelement()](../../d5/d9d/classOpenSCADCommands_1_1AddSCADTask.html#a2a34f64411bd2b0aa92b513fc66565b9),
[PathScripts.PathDressupTagPreferences.HoldingTagPreferences.loadSettings()](../../d5/d35/classPathScripts_1_1PathDressupTagPreferences_1_1HoldingTagPreferences.html#af650851943cefac1b52364bde65c879e),
[PathScripts.PathPreferencesAdvanced.AdvancedPreferencesPage.loadSettings()](../../d5/d8b/classPathScripts_1_1PathPreferencesAdvanced_1_1AdvancedPreferencesPage.html#a75555477ea0f4d35c9cead6a058c48b2),
[PathScripts.PathPreferencesPathJob.JobPreferencesPage.loadSettings()](../../db/dec/classPathScripts_1_1PathPreferencesPathJob_1_1JobPreferencesPage.html#a8313cfc6b3f83b9a3c5f74156960f35e),
[PathScripts.PathPreferencesPathJob.JobPreferencesPage.loadStockSettings()](../../db/dec/classPathScripts_1_1PathPreferencesPathJob_1_1JobPreferencesPage.html#ab1a409f821cfe2e0ca85dfd79d51bbb9),
[PathScripts.PathToolLibraryEditor.EditorPanel.loadTable()](../../d0/d92/classPathScripts_1_1PathToolLibraryEditor_1_1EditorPanel.html#ad41512d35c0f48ce3c29655e060a8d6c),
[PathScripts.PathPreferencesPathJob.JobPreferencesPage.loadToolSettings()](../../db/dec/classPathScripts_1_1PathPreferencesPathJob_1_1JobPreferencesPage.html#a7c37b86291fffea3848dcfaa477e363d),
[PathScripts.PathToolLibraryEditor.EditorPanel.loadToolTables()](../../d0/d92/classPathScripts_1_1PathToolLibraryEditor_1_1EditorPanel.html#a0d85a8790702ed8c7b77a7b86577d3a5),
[PathScripts.PathToolBitLibraryGui.ToolBitLibrary.lockoff()](../../dd/d3a/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitLibrary.html#aa6e420e437ba98bcc3e0fe5d9466b901),
[PathScripts.PathToolBitLibraryGui.ToolBitLibrary.lockon()](../../dd/d3a/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitLibrary.html#af30e1641da76646421aebc4cdb9cb46d),
[PathScripts.PathCamoticsGui.CAMoticsUI.makeCamoticsFile()](../../d2/df4/classPathScripts_1_1PathCamoticsGui_1_1CAMoticsUI.html#a4721d9739af5bb9f812462dd9401df7a),
[DraftGui.DraftToolBar.makeDumbTask()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a33b02e68ac7011178cfc4c2dfd7100be),
[PathScripts.PathJobGui.TaskPanel.modelMove()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#ac16e4825b674fa89cb71f88940ecd008),
[PathScripts.PathJobGui.TaskPanel.modelRotate()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#a89cf389f4c45cd1b8e789d0d3ba7b15e),
[PathScripts.PathJobGui.TaskPanel.modelSet0()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#af12c3534a832b3ed0aac6b8df15349e0),
[PathScripts.PathToolLibraryEditor.EditorPanel.moveDown()](../../d0/d92/classPathScripts_1_1PathToolLibraryEditor_1_1EditorPanel.html#a98cda7aa8007adde4f5fa5f9c60ef124),
[PathScripts.PathToolLibraryEditor.EditorPanel.moveUp()](../../d0/d92/classPathScripts_1_1PathToolLibraryEditor_1_1EditorPanel.html#a2befce37f25939918d3bb65436fed2cf),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.on_delete()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#af3669f24c57e597f1625c82f67d0cdb2),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.on_import()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#aa4ea57c767b4f551ad3f7ba88fee61b8),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.on_rename()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#a1c19fb58b4db3cb77344af3217075ea4),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.on_style_changed()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#ac5183cb3d37565f9de75e2aa006e48e6),
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel.onApplyDim()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#a5cee62097661ae9105c06d4f2a51fd96),
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel.onApplyStyle()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#af2ec3f7c30de28de9884af7557b56e12),
[draftguitools.gui_hatch.Draft_Hatch_TaskPanel.onFileChanged()](../../d1/d6e/classdraftguitools_1_1gui__hatch_1_1Draft__Hatch__TaskPanel.html#a422c165eda9997bf36907a97e56c64f8),
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel.onLoadStyle()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#a1ba62c7eca1bc9f408549242e3def48b),
[PathScripts.PathJobGui.TaskPanel.open()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#ad0968b75b7c8fe7e00afe3fea9fce497),
[PathScripts.PathToolBitLibraryGui.ToolBitLibrary.open()](../../dd/d3a/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitLibrary.html#aaa8f14ccf8f8a25d826102c1b7d663ed),
[PathScripts.PathToolBitLibraryGui.ToolBitSelector.open()](../../d8/d6e/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitSelector.html#a37ea7defe21afc116a13fee1a24bbdbb),
[PathScripts.PathJobGui.TaskPanel.operationDelete()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#acb8fd8604f2e7f710935ccca3d4408a0),
[PathScripts.PathJobGui.TaskPanel.operationMoveDown()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#aa338789029d355cfb68bdb3bf21c9564),
[PathScripts.PathJobGui.TaskPanel.operationMoveUp()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#a2c90efcc52c43f734dbe48ffafd8397c),
[PathScripts.PathJobGui.TaskPanel.operationSelect()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#abd187f3b5062cc4f88ce722e615f9487),
[TechDrawTools.TaskMoveView.TaskMoveView.pickFromPage()](../../da/d16/classTechDrawTools_1_1TaskMoveView_1_1TaskMoveView.html#a6315fd5a894efeaac64d8a3bf4c0420c),
[TechDrawTools.TaskShareView.TaskShareView.pickFromPage()](../../d0/d64/classTechDrawTools_1_1TaskShareView_1_1TaskShareView.html#afe2a46265f27152125c899865945c706),
[TechDrawTools.TaskMoveView.TaskMoveView.pickToPage()](../../da/d16/classTechDrawTools_1_1TaskMoveView_1_1TaskMoveView.html#a8603fbbe2bbd698e77d8313c70d67580),
[TechDrawTools.TaskShareView.TaskShareView.pickToPage()](../../d0/d64/classTechDrawTools_1_1TaskShareView_1_1TaskShareView.html#acedbfda483a1d58ac4745eeb34dac5b1),
[TechDrawTools.TaskMoveView.TaskMoveView.pickView()](../../da/d16/classTechDrawTools_1_1TaskMoveView_1_1TaskMoveView.html#a86e4e71d2ef6da50142d097b77c08731),
[TechDrawTools.TaskShareView.TaskShareView.pickView()](../../d0/d64/classTechDrawTools_1_1TaskShareView_1_1TaskShareView.html#afe19c1a1a0c84244e474e3b8faadf80f),
[PathScripts.PathPropertyBagGui.TaskPanel.propertyAdd()](../../d3/d93/classPathScripts_1_1PathPropertyBagGui_1_1TaskPanel.html#af151274cd14cf9e25a684f82e9c2287a),
[PathScripts.PathPropertyBagGui.PropertyCreate.propertyEnumerations()](../../dd/d6e/classPathScripts_1_1PathPropertyBagGui_1_1PropertyCreate.html#a4fc2dd4c1261bb1340858cb511781b6d),
[PathScripts.PathPropertyBagGui.PropertyCreate.propertyGroup()](../../dd/d6e/classPathScripts_1_1PathPropertyBagGui_1_1PropertyCreate.html#af1bc9bd3c33dea1b8480dc87bd8a247b),
[PathScripts.PathPropertyBagGui.PropertyCreate.propertyInfo()](../../dd/d6e/classPathScripts_1_1PathPropertyBagGui_1_1PropertyCreate.html#ac7f39ce59cf6eebb99a41154033bbd8a),
[PathScripts.PathPropertyBagGui.TaskPanel.propertyModify()](../../d3/d93/classPathScripts_1_1PathPropertyBagGui_1_1TaskPanel.html#a34edfc260429400595cdf1c4a9338e6b),
[PathScripts.PathPropertyBagGui.PropertyCreate.propertyName()](../../dd/d6e/classPathScripts_1_1PathPropertyBagGui_1_1PropertyCreate.html#a132de9df94d283e68977e0e39cda54c5),
[PathScripts.PathPropertyBagGui.TaskPanel.propertyRemove()](../../d3/d93/classPathScripts_1_1PathPropertyBagGui_1_1TaskPanel.html#ad2290190d7ad9b07e95242d26931231e),
[PathScripts.PathPropertyBagGui.TaskPanel.propertySelected()](../../d3/d93/classPathScripts_1_1PathPropertyBagGui_1_1TaskPanel.html#a36bace35f0d3c794dfd724404c4d2b68),
[PathScripts.PathPropertyBagGui.PropertyCreate.propertyType()](../../dd/d6e/classPathScripts_1_1PathPropertyBagGui_1_1PropertyCreate.html#a6e7479711cbbff48db959a5d33848ee9),
[PathScripts.PathToolEdit.ToolEditorImage.quantityCuttingEdgeAngle()](../../dd/df1/classPathScripts_1_1PathToolEdit_1_1ToolEditorImage.html#aac7efa4c4845693d90dc1ce67329bfef),
[PathScripts.PathToolEdit.ToolEditorDrill.quantityCuttingEdgeAngle()](../../d3/d1e/classPathScripts_1_1PathToolEdit_1_1ToolEditorDrill.html#ab3fef0c9bff3eac2cbb5fe58427a6004),
[PathScripts.PathToolEdit.ToolEditorImage.quantityCuttingEdgeHeight()](../../dd/df1/classPathScripts_1_1PathToolEdit_1_1ToolEditorImage.html#a79712563bb3659cd358dad344c779abd),
[PathScripts.PathToolEdit.ToolEditorImage.quantityDiameter()](../../dd/df1/classPathScripts_1_1PathToolEdit_1_1ToolEditorImage.html#a91d1a0785a81d154ee17a6614f516388),
[PathScripts.PathToolEdit.ToolEditorImage.quantityFlatRadius()](../../dd/df1/classPathScripts_1_1PathToolEdit_1_1ToolEditorImage.html#a07b28c9fa8d24dac0f401d7ab2783f00),
[AttachmentEditor.TaskAttachmentEditor.AttachmentEditorTaskPanel.readParameters()](../../d8/d4c/classAttachmentEditor_1_1TaskAttachmentEditor_1_1AttachmentEditorTaskPanel.html#a2f3caaa8ebf937b917953fc718d0f6bc),
[PathScripts.PathToolBitEdit.ToolBitEditor.refresh()](../../d6/d36/classPathScripts_1_1PathToolBitEdit_1_1ToolBitEditor.html#a0141161438ab8f8381c2871d715c669b),
[PathScripts.PathToolControllerGui.ToolControllerEditor.refresh()](../../d2/db6/classPathScripts_1_1PathToolControllerGui_1_1ToolControllerEditor.html#a64ba4dfdf3d4ac7390f17e90ce12c749),
[PathScripts.PathToolEdit.ToolEditor.refresh()](../../d2/df8/classPathScripts_1_1PathToolEdit_1_1ToolEditor.html#ad9beb036bd18fef6f816ac808e393d41),
[OpenSCADCommands.AddSCADTask.refreshelement()](../../d5/d9d/classOpenSCADCommands_1_1AddSCADTask.html#a27e2a75e11a2e139586d8a79492bbc3d),
[PathScripts.PathJobGui.TaskPanel.refreshStock()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#ad739d5e38b5826f086a9f22644da5907),
[PathScripts.PathCircularHoleBaseGui.TaskPanelHoleGeometryPage.registerSignalHandlers()](../../d3/dfd/classPathScripts_1_1PathCircularHoleBaseGui_1_1TaskPanelHoleGeometryPage.html#a3086d9c6fc9dd75e3db74ad018c3b041),
[PathScripts.PathDeburrGui.TaskPanelOpPage.registerSignalHandlers()](../../d8/d57/classPathScripts_1_1PathDeburrGui_1_1TaskPanelOpPage.html#a903edcf338b7d1e9cf2431cafc2ae8ed),
[PathScripts.PathDrillingGui.TaskPanelOpPage.registerSignalHandlers()](../../d6/df8/classPathScripts_1_1PathDrillingGui_1_1TaskPanelOpPage.html#a24620d388f520c3cb0a97088a23b0016),
[PathScripts.PathFeatureExtensionsGui.TaskPanelExtensionPage.registerSignalHandlers()](../../d0/de3/classPathScripts_1_1PathFeatureExtensionsGui_1_1TaskPanelExtensionPage.html#a7250839195cb0e87b88ed86cc6a21fe6),
[PathScripts.PathOpGui.TaskPanelBaseGeometryPage.registerSignalHandlers()](../../d4/dfc/classPathScripts_1_1PathOpGui_1_1TaskPanelBaseGeometryPage.html#a95e3654240ee52abfd7b11b615f4abd5),
[PathScripts.PathOpGui.TaskPanelBaseLocationPage.registerSignalHandlers()](../../d6/d50/classPathScripts_1_1PathOpGui_1_1TaskPanelBaseLocationPage.html#a016607d7204403f157f206fa28cfd35d),
[PathScripts.PathOpGui.TaskPanelDepthsPage.registerSignalHandlers()](../../da/d1a/classPathScripts_1_1PathOpGui_1_1TaskPanelDepthsPage.html#afd6f12b10d16a649bed4abc8afb61fc0),
[PathScripts.PathProfileGui.TaskPanelOpPage.registerSignalHandlers()](../../db/d54/classPathScripts_1_1PathProfileGui_1_1TaskPanelOpPage.html#a3b352b7278f774e521310fb8ee5ff9d3),
[PathScripts.PathSurfaceGui.TaskPanelOpPage.registerSignalHandlers()](../../d7/d7a/classPathScripts_1_1PathSurfaceGui_1_1TaskPanelOpPage.html#a373098ebbd90aa7d51e6196abceb5d2a),
[PathScripts.PathThreadMillingGui.TaskPanelOpPage.registerSignalHandlers()](../../df/d59/classPathScripts_1_1PathThreadMillingGui_1_1TaskPanelOpPage.html#aa5d6418c4ffe7d290dcb0049f03eb008),
[PathScripts.PathWaterlineGui.TaskPanelOpPage.registerSignalHandlers()](../../d3/dcf/classPathScripts_1_1PathWaterlineGui_1_1TaskPanelOpPage.html#a1b28ed435c424455e72001276306d65d),
[ArchSchedule.ArchScheduleTaskPanel.reject()](../../d5/da0/classArchSchedule_1_1ArchScheduleTaskPanel.html#acf02b2833e0fac4dccd6663350d9efcd),
[ArchSchedule.ArchScheduleTaskPanel.remove()](../../d5/da0/classArchSchedule_1_1ArchScheduleTaskPanel.html#a3dc0065e9e2a6e11031187452da6dfaf),
[ArchPanel.NestTaskPanel.removeShapes()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#a14b88173115d5a126ac1d5a0bc973395),
[PathScripts.PathToolLibraryEditor.EditorPanel.renameTable()](../../d0/d92/classPathScripts_1_1PathToolLibraryEditor_1_1EditorPanel.html#a8ee6a7789d6ce8bcb6b3ce2460a3a1be),
[drafttaskpanels.task_circulararray.TaskPanelCircularArray.reset_point()](../../dd/d3a/classdrafttaskpanels_1_1task__circulararray_1_1TaskPanelCircularArray.html#aa62cedfe83055f3d98616fbb2bc46b98),
[drafttaskpanels.task_polararray.TaskPanelPolarArray.reset_point()](../../d7/d8d/classdrafttaskpanels_1_1task__polararray_1_1TaskPanelPolarArray.html#a58abe0235a2b97d0fa6e4ae3de9644aa),
[drafttaskpanels.task_orthoarray.TaskPanelOrthoArray.reset_v()](../../d6/dfa/classdrafttaskpanels_1_1task__orthoarray_1_1TaskPanelOrthoArray.html#a4f5165c6a7af1c3ae3b432f1662a7ff7),
[PathScripts.PathOpGui.TaskPanelPage.resetToolController()](../../d1/d18/classPathScripts_1_1PathOpGui_1_1TaskPanelPage.html#a24f3077779ab32608edaa092dbd4d44b),
[PathScripts.PathOpGui.TaskPanelBaseGeometryPage.resizeBaseList()](../../d4/dfc/classPathScripts_1_1PathOpGui_1_1TaskPanelBaseGeometryPage.html#aab7a1f24d0ee5e70730be3bf08a48b4e),
[PathScripts.PathFeatureExtensionsGui.TaskPanelExtensionPage.restoreSelection()](../../d0/de3/classPathScripts_1_1PathFeatureExtensionsGui_1_1TaskPanelExtensionPage.html#a178e8a65a2b495e3c44b7d62958e1dd4),
[ArchCommands.SurveyTaskPanel.retranslateUi()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a80aefc6bf17d60c63cd66e8984616d4b),
[ArchProfile.ProfileTaskPanel.retranslateUi()](../../dc/d9a/classArchProfile_1_1ProfileTaskPanel.html#a8b6ffa229d56acdd0aabe8fb92de728b),
[ArchGrid.ArchGridTaskPanel.retranslateUi()](../../d6/da7/classArchGrid_1_1ArchGridTaskPanel.html#a6297fd61506e67f6be9ba5d86bdcfc10),
[drafttaskpanels.task_scale.ScaleTaskPanel.retranslateUi()](../../df/d70/classdrafttaskpanels_1_1task__scale_1_1ScaleTaskPanel.html#ab5cdf6b149fea39e027f877ea7b5a12c),
[OpenSCADCommands.AddSCADTask.saveelement()](../../d5/d9d/classOpenSCADCommands_1_1AddSCADTask.html#a309e55ea365827eb92c89f776f44c211),
[PathScripts.PathDressupTagPreferences.HoldingTagPreferences.saveSettings()](../../d5/d35/classPathScripts_1_1PathDressupTagPreferences_1_1HoldingTagPreferences.html#a22b23c2790193ef3918a0a4eec057461),
[PathScripts.PathPreferencesAdvanced.AdvancedPreferencesPage.saveSettings()](../../d5/d8b/classPathScripts_1_1PathPreferencesAdvanced_1_1AdvancedPreferencesPage.html#a4a2be89c496ef71ca7d885b9fd89595b),
[PathScripts.PathPreferencesPathJob.JobPreferencesPage.saveSettings()](../../db/dec/classPathScripts_1_1PathPreferencesPathJob_1_1JobPreferencesPage.html#a6a99007201877c5e63a6c8b7b487782b),
[PathScripts.PathPreferencesPathJob.JobPreferencesPage.saveStockSettings()](../../db/dec/classPathScripts_1_1PathPreferencesPathJob_1_1JobPreferencesPage.html#ae18eae6affa59ac96ef853e7343065d6),
[PathScripts.PathPreferencesPathJob.JobPreferencesPage.saveToolsSettings()](../../db/dec/classPathScripts_1_1PathPreferencesPathJob_1_1JobPreferencesPage.html#a692419d66a629d797b75bd6d7b9fc4e7),
[ArchSchedule.ArchScheduleTaskPanel.select()](../../d5/da0/classArchSchedule_1_1ArchScheduleTaskPanel.html#a5f453c8731c737210fcd85da53865be6),
[femtaskpanels.task_solver_ccxtools._TaskPanel.select_analysis_type()](../../da/df4/classfemtaskpanels_1_1task__solver__ccxtools_1_1__TaskPanel.html#a73c0a9cc0bb32d0e59f5df14829b60f1),
[PathScripts.PathToolBitLibraryGui.ToolBitSelector.selectedOrAllTools()](../../d8/d6e/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitSelector.html#a96d4cd54a4633268061ab179d624fb29),
[PathScripts.PathToolBitEdit.ToolBitEditor.selectShape()](../../d6/d36/classPathScripts_1_1PathToolBitEdit_1_1ToolBitEditor.html#aabd78f2e5bb4b7ab46db1be4117c450e),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.selectTagWithId()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#a18bb926e8c948262c2541661f0f697a0),
[drafttaskpanels.task_circulararray.TaskPanelCircularArray.set_focus()](../../dd/d3a/classdrafttaskpanels_1_1task__circulararray_1_1TaskPanelCircularArray.html#a6abb1efc8018e9d27ce587419ea41daf),
[drafttaskpanels.task_polararray.TaskPanelPolarArray.set_focus()](../../d7/d8d/classdrafttaskpanels_1_1task__polararray_1_1TaskPanelPolarArray.html#a4a0e1e12f2a624c2f36e2aeef6abc488),
[drafttaskpanels.task_circulararray.TaskPanelCircularArray.set_fuse()](../../dd/d3a/classdrafttaskpanels_1_1task__circulararray_1_1TaskPanelCircularArray.html#abcdebbd4c3b43deba4f0561fd37e6dae),
[drafttaskpanels.task_orthoarray.TaskPanelOrthoArray.set_fuse()](../../d6/dfa/classdrafttaskpanels_1_1task__orthoarray_1_1TaskPanelOrthoArray.html#acb8ceb2cc713c7fc16cbf2a54516ed99),
[drafttaskpanels.task_polararray.TaskPanelPolarArray.set_fuse()](../../d7/d8d/classdrafttaskpanels_1_1task__polararray_1_1TaskPanelPolarArray.html#a2a45c82ea93f52f74996cc38570da3ed),
[drafttaskpanels.task_circulararray.TaskPanelCircularArray.set_link()](../../dd/d3a/classdrafttaskpanels_1_1task__circulararray_1_1TaskPanelCircularArray.html#a54b834c7d9a9f9f5f1d8d41c2b35c795),
[drafttaskpanels.task_orthoarray.TaskPanelOrthoArray.set_link()](../../d6/dfa/classdrafttaskpanels_1_1task__orthoarray_1_1TaskPanelOrthoArray.html#ac4363660790efa873ef0621d6b744c38),
[drafttaskpanels.task_polararray.TaskPanelPolarArray.set_link()](../../d7/d8d/classdrafttaskpanels_1_1task__polararray_1_1TaskPanelPolarArray.html#a1d680be69a189357fbe021cb401cddd0),
[drafttaskpanels.task_circulararray.TaskPanelCircularArray.set_widget_callbacks()](../../dd/d3a/classdrafttaskpanels_1_1task__circulararray_1_1TaskPanelCircularArray.html#ae9ec46914fbaee1f3813f5883642e495),
[drafttaskpanels.task_orthoarray.TaskPanelOrthoArray.set_widget_callbacks()](../../d6/dfa/classdrafttaskpanels_1_1task__orthoarray_1_1TaskPanelOrthoArray.html#ac974cd63bb8543c0b37452af1f4909d3),
[drafttaskpanels.task_polararray.TaskPanelPolarArray.set_widget_callbacks()](../../d7/d8d/classdrafttaskpanels_1_1task__polararray_1_1TaskPanelPolarArray.html#a1ed0ba6eb56004688d79b06092a5c33d),
[ArchPanel.NestTaskPanel.setCounter()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#ac7c67ca72068f6667c2fd40430960757),
[PathScripts.PathToolLibraryEditor.EditorPanel.setCurrentToolTableByName()](../../d0/d92/classPathScripts_1_1PathToolLibraryEditor_1_1EditorPanel.html#af423729346d2ead46fad0c831496eaa9),
[PathScripts.PathFeatureExtensionsGui.TaskPanelExtensionPage.setExtensions()](../../d0/de3/classPathScripts_1_1PathFeatureExtensionsGui_1_1TaskPanelExtensionPage.html#a856caaf6e79ccf88242d279f1f7dd122),
[PathScripts.PathDressupDogbone.TaskPanel.setFields()](../../df/d54/classPathScripts_1_1PathDressupDogbone_1_1TaskPanel.html#a5e37bf09b5ccd50a3576f1f33000f2df),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.setFields()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#a9a16b583913d19a3e8259c6bdef77588),
[PathScripts.PathDressupZCorrect.TaskPanel.setFields()](../../d7/d25/classPathScripts_1_1PathDressupZCorrect_1_1TaskPanel.html#aa7e3e307a8ee37cb99e8437df0ffe1f8),
[PathScripts.PathJobGui.TaskPanel.setFields()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#ad6c0540aaf5341104d44606f1cdb559a),
[PathScripts.PathAdaptiveGui.TaskPanelOpPage.setFields()](../../d4/d86/classPathScripts_1_1PathAdaptiveGui_1_1TaskPanelOpPage.html#a81500326949447cb057152f86bd9b475),
[PathScripts.PathCircularHoleBaseGui.TaskPanelHoleGeometryPage.setFields()](../../d3/dfd/classPathScripts_1_1PathCircularHoleBaseGui_1_1TaskPanelHoleGeometryPage.html#a3f2bf69ec30e9a5dbb28b2426c6c5352),
[PathScripts.PathCustomGui.TaskPanelOpPage.setFields()](../../de/d5c/classPathScripts_1_1PathCustomGui_1_1TaskPanelOpPage.html#a56a5b53146f8a36da1db1eb3d482e9e7),
[PathScripts.PathDeburrGui.TaskPanelOpPage.setFields()](../../d8/d57/classPathScripts_1_1PathDeburrGui_1_1TaskPanelOpPage.html#a8384dc38cba6c1c8648d0e2b4f00273e),
[PathScripts.PathDrillingGui.TaskPanelOpPage.setFields()](../../d6/df8/classPathScripts_1_1PathDrillingGui_1_1TaskPanelOpPage.html#a454182832dd739c20de85df9bfc32596),
[PathScripts.PathEngraveGui.TaskPanelBaseGeometryPage.setFields()](../../d0/d2e/classPathScripts_1_1PathEngraveGui_1_1TaskPanelBaseGeometryPage.html#abe353d1b197f1f413749f7f7939919ae),
[PathScripts.PathEngraveGui.TaskPanelOpPage.setFields()](../../d9/de5/classPathScripts_1_1PathEngraveGui_1_1TaskPanelOpPage.html#abafe637cd9c28209fa5fdca92ee2ad9d),
[PathScripts.PathFeatureExtensionsGui.TaskPanelExtensionPage.setFields()](../../d0/de3/classPathScripts_1_1PathFeatureExtensionsGui_1_1TaskPanelExtensionPage.html#a5fd660d439ad67e0fafff022ae92cd30),
[PathScripts.PathHelixGui.TaskPanelOpPage.setFields()](../../d5/d26/classPathScripts_1_1PathHelixGui_1_1TaskPanelOpPage.html#aecf9a43da4725b2def5f369a1c17a1db),
[PathScripts.PathJobGui.StockFromExistingEdit.setFields()](../../d8/d19/classPathScripts_1_1PathJobGui_1_1StockFromExistingEdit.html#a67378232547c025dc42538d70e233973),
[PathScripts.PathPocketBaseGui.TaskPanelOpPage.setFields()](../../d1/d25/classPathScripts_1_1PathPocketBaseGui_1_1TaskPanelOpPage.html#ac78b2120480789d1cb66f6d7726d62fd),
[PathScripts.PathProbeGui.TaskPanelOpPage.setFields()](../../db/de4/classPathScripts_1_1PathProbeGui_1_1TaskPanelOpPage.html#a11b4ea70b2615c0b58f0609df89e4d86),
[PathScripts.PathProfileGui.TaskPanelOpPage.setFields()](../../db/d54/classPathScripts_1_1PathProfileGui_1_1TaskPanelOpPage.html#aeda3c2cdbf188d3ce5b3c2677c2ef8f9),
[PathScripts.PathSlotGui.TaskPanelOpPage.setFields()](../../d2/da9/classPathScripts_1_1PathSlotGui_1_1TaskPanelOpPage.html#a724ecf6fb54f44af517b3141891ce579),
[PathScripts.PathSurfaceGui.TaskPanelOpPage.setFields()](../../d7/d7a/classPathScripts_1_1PathSurfaceGui_1_1TaskPanelOpPage.html#ae15e187a14a5026b093e46bb40bd4575),
[PathScripts.PathThreadMillingGui.TaskPanelOpPage.setFields()](../../df/d59/classPathScripts_1_1PathThreadMillingGui_1_1TaskPanelOpPage.html#a0546b64219e91a87f17a4474bc465c52),
[PathScripts.PathVcarveGui.TaskPanelBaseGeometryPage.setFields()](../../dc/d9b/classPathScripts_1_1PathVcarveGui_1_1TaskPanelBaseGeometryPage.html#a041e95d6b71ba789ee550eb24ee910e2),
[PathScripts.PathVcarveGui.TaskPanelOpPage.setFields()](../../d8/dc5/classPathScripts_1_1PathVcarveGui_1_1TaskPanelOpPage.html#a514ad381e7aef69f102ccface2cc35ed),
[PathScripts.PathWaterlineGui.TaskPanelOpPage.setFields()](../../d3/dcf/classPathScripts_1_1PathWaterlineGui_1_1TaskPanelOpPage.html#a9aaae151b9694864b7d984e58b3712af),
[PathScripts.PathCustomGui.TaskPanelOpPage.setGCode()](../../de/d5c/classPathScripts_1_1PathCustomGui_1_1TaskPanelOpPage.html#acc62ac3c9667944807beca9d39b35510),
[ArchMaterial.MultiMaterialDelegate.setModelData()](../../dd/dba/classArchMaterial_1_1MultiMaterialDelegate.html#aa36ee69be80adc06480436ec7883804e),
[PathScripts.PathProbeGui.TaskPanelOpPage.SetOutputFileName()](../../db/de4/classPathScripts_1_1PathProbeGui_1_1TaskPanelOpPage.html#ae218dea328c419ddec9304d8719d0a32),
[drafttaskpanels.task_shapestring.ShapeStringTaskPanel.setPoint()](../../d9/d1e/classdrafttaskpanels_1_1task__shapestring_1_1ShapeStringTaskPanel.html#a99c68878ca6fbb83fba91af41b71a76f),
[PathScripts.PathJobGui.TaskPanel.setPostProcessorOutputFile()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#a128c925148744a3cb9ca7fdf4467e952),
[PathScripts.PathDressupZCorrect.TaskPanel.SetProbePointFileName()](../../d7/d25/classPathScripts_1_1PathDressupZCorrect_1_1TaskPanel.html#a80a8548159e07949717dcd2e66c21c92),
[PathScripts.PathPreferencesPathJob.JobPreferencesPage.setProcessorListTooltip()](../../db/dec/classPathScripts_1_1PathPreferencesPathJob_1_1JobPreferencesPage.html#a5de35b33a3587342e0ac56eb7594f43b),
[PathScripts.PathCamoticsGui.CAMoticsUI.setRunTime()](../../d2/df4/classPathScripts_1_1PathCamoticsGui_1_1CAMoticsUI.html#a0b501bc22a3e258902a4298592d988fc),
[PathScripts.PathPreferencesPathJob.JobPreferencesPage.setupStock()](../../db/dec/classPathScripts_1_1PathPreferencesPathJob_1_1JobPreferencesPage.html#a3875f3d247d5be30f62bf3f37b9cd74c),
[PathScripts.PathToolBitEdit.ToolBitEditor.setupTool()](../../d6/d36/classPathScripts_1_1PathToolBitEdit_1_1ToolBitEditor.html#a4dcfc3c9a2967c78e73919f4b85abf6f),
[Mod.PartDesign.FeatureHole.TaskHole.TaskHole.setupUi()](../../d1/d14/classMod_1_1PartDesign_1_1FeatureHole_1_1TaskHole_1_1TaskHole.html#a1ea2ec8e78187e6ef3f6dfbb718ab320),
[PathScripts.PathDressupDogbone.TaskPanel.setupUi()](../../df/d54/classPathScripts_1_1PathDressupDogbone_1_1TaskPanel.html#a550fcfcb691482a72d02a7a1bde819e6),
[PathScripts.PathDressupLeadInOut.TaskDressupLeadInOut.setupUi()](../../de/de7/classPathScripts_1_1PathDressupLeadInOut_1_1TaskDressupLeadInOut.html#a0975e82d9423f69fb6b39b4bfac2b7cd),
[PathScripts.PathDressupPathBoundaryGui.TaskPanel.setupUi()](../../d4/d65/classPathScripts_1_1PathDressupPathBoundaryGui_1_1TaskPanel.html#ac8a189618a3ad5a052ca9a56649682e1),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.setupUi()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#acf37f2ac6986c8a488e72583704023af),
[PathScripts.PathPropertyBagGui.TaskPanel.setupUi()](../../d3/d93/classPathScripts_1_1PathPropertyBagGui_1_1TaskPanel.html#a0e7d9c2f42ae50ec45505059011deba5),
[PathScripts.PathSetupSheetGui.OpTaskPanel.setupUi()](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#a03e427ec6574bd249d859f5bd2496576),
[PathScripts.PathSetupSheetGui.OpsDefaultEditor.setupUi()](../../d3/dcd/classPathScripts_1_1PathSetupSheetGui_1_1OpsDefaultEditor.html#aa801d1240606920fb9c6a5e77ac6ed41),
[PathScripts.PathSetupSheetGui.GlobalEditor.setupUi()](../../de/df9/classPathScripts_1_1PathSetupSheetGui_1_1GlobalEditor.html#ad7f1aaae1d7c9082666c4d873dea7e05),
[PathScripts.PathToolBitEdit.ToolBitEditor.setupUI()](../../d6/d36/classPathScripts_1_1PathToolBitEdit_1_1ToolBitEditor.html#ac6ca422dac09ad140db418319c2c05e2),
[PathScripts.PathToolBitLibraryGui.ToolBitSelector.setupUI()](../../d8/d6e/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitSelector.html#a25fe2ac75d6f8f5fdef379968d896ee9),
[PathScripts.PathToolBitLibraryGui.ToolBitLibrary.setupUI()](../../dd/d3a/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitLibrary.html#ab113bd2de3c3f7618638b0a30fbcca16),
[PathScripts.PathToolControllerGui.ToolControllerEditor.setupUi()](../../d2/db6/classPathScripts_1_1PathToolControllerGui_1_1ToolControllerEditor.html#ac65d1c5c0d0e29af0184084c6b0924e7),
[PathScripts.PathToolEdit.ToolEditorDefault.setupUI()](../../db/db4/classPathScripts_1_1PathToolEdit_1_1ToolEditorDefault.html#a15b5c3aa264b9e267e2e38e0f6c3ae7b),
[PathScripts.PathToolEdit.ToolEditorImage.setupUI()](../../dd/df1/classPathScripts_1_1PathToolEdit_1_1ToolEditorImage.html#a084ad5441e84f4bab1e2ab96bb45e09f),
[PathScripts.PathToolEdit.ToolEditor.setupUI()](../../d2/df8/classPathScripts_1_1PathToolEdit_1_1ToolEditor.html#a1f8ad48742a24a6b9a1d1b0ce191252f),
[PathScripts.PathToolLibraryEditor.EditorPanel.setupUi()](../../d0/d92/classPathScripts_1_1PathToolLibraryEditor_1_1EditorPanel.html#a6a2464b91987b1eda339705daeaa3bc3),
[PathScripts.PathJobGui.TaskPanel.setupUi()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#aeec0e3144421da5b88dc6e0a9573d488),
[PathScripts.PathJobGui.StockFromBaseBoundBoxEdit.setupUi()](../../d6/df2/classPathScripts_1_1PathJobGui_1_1StockFromBaseBoundBoxEdit.html#a71b2dc314bc75bb2b0c52e3125ea5ebb),
[PathScripts.PathJobGui.StockCreateBoxEdit.setupUi()](../../db/dde/classPathScripts_1_1PathJobGui_1_1StockCreateBoxEdit.html#aba81ea27c94300c89bd4b927b9a90680),
[PathScripts.PathJobGui.StockCreateCylinderEdit.setupUi()](../../d8/dc0/classPathScripts_1_1PathJobGui_1_1StockCreateCylinderEdit.html#aefd4db946331c1060b745582916b5f24),
[PathScripts.PathJobGui.StockFromExistingEdit.setupUi()](../../d8/d19/classPathScripts_1_1PathJobGui_1_1StockFromExistingEdit.html#ae60488383a94b2c7b8ffc6ad1f0b47fe),
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel.setValues()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#aeae62102b8bdfc483bfee73586df265d),
[TechDrawTools.TaskMoveView.TaskMoveView.setValues()](../../da/d16/classTechDrawTools_1_1TaskMoveView_1_1TaskMoveView.html#a38ab8c950cb582708106e2b7a4b213b0),
[TechDrawTools.TaskShareView.TaskShareView.setValues()](../../d0/d64/classTechDrawTools_1_1TaskShareView_1_1TaskShareView.html#a3247ce86755b967959d168e14197bed9),
[PathScripts.PathFeatureExtensionsGui.TaskPanelExtensionPage.showHideExtension()](../../d0/de3/classPathScripts_1_1PathFeatureExtensionsGui_1_1TaskPanelExtensionPage.html#a8636bb77eea09ed27adf0d0a09503714),
[Mod.PartDesign.SprocketFeature.SprocketTaskPanel.sprocketReferenceChanged()](../../db/d2b/classMod_1_1PartDesign_1_1SprocketFeature_1_1SprocketTaskPanel.html#a2f46648dfb523b2fad1e05e91c3c21d3),
[ArchPanel.NestTaskPanel.start()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#ae94d1620245089dea3da24cffad8f785),
[ArchPanel.NestTaskPanel.stop()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#a95c60f3ed8efc1dce43fd0d96c110a6a),
[PathScripts.PathToolLibraryEditor.EditorPanel.tableSelected()](../../d0/d92/classPathScripts_1_1PathToolLibraryEditor_1_1EditorPanel.html#ac0c5cd0d24c66d34d0686cf98af3aa1a),
[PathScripts.PathJobGui.TaskPanel.toolControllerDelete()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#a33eb29824a2d7617cd4b2fb249466612),
[PathScripts.PathJobGui.TaskPanel.toolControllerEdit()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#a4d5b502b782198cfa9cafb2f82a9a500),
[PathScripts.PathJobGui.TaskPanel.toolControllerSelect()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#a5d37c33f9e4e7d86afd804292b6e68cc),
[PathScripts.PathToolBitLibraryGui.ToolBitLibrary.toolEdit()](../../dd/d3a/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitLibrary.html#ac20855be381c22621c17d3df63458595),
[PathScripts.PathToolBitLibraryGui.ToolBitLibrary.toolSelect()](../../dd/d3a/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitLibrary.html#a40b79889da8627bfb5048fd7413e8b87),
[PathScripts.PathToolLibraryEditor.EditorPanel.toolSelectionChanged()](../../d0/d92/classPathScripts_1_1PathToolLibraryEditor_1_1EditorPanel.html#a3924b8d98caeeefd7def88d5a1d80418),
[Mod.PartDesign.SprocketFeature.SprocketTaskPanel.transferFrom()](../../db/d2b/classMod_1_1PartDesign_1_1SprocketFeature_1_1SprocketTaskPanel.html#ada50146f8f419202b8499a08ec900363),
[Mod.PartDesign.SprocketFeature.SprocketTaskPanel.transferTo()](../../db/d2b/classMod_1_1PartDesign_1_1SprocketFeature_1_1SprocketTaskPanel.html#a5a70f0ef0e602ac72c333fcc2d7a426d),
[ArchAxisSystem.AxisSystemTaskPanel.update()](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a376cbba2ccee6efd86c46d0f0a8e99e3),
[ArchSectionPlane.SectionPlaneTaskPanel.update()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#aab4bcd7b08950b8e3b37d801381c5162),
[DraftGui.FacebinderTaskPanel.update()](../../d2/d61/classDraftGui_1_1FacebinderTaskPanel.html#a191f43aa777ae22c42a00d118688bafe),
[femtaskpanels.task_mesh_gmsh._TaskPanel.update()](../../d6/d90/classfemtaskpanels_1_1task__mesh__gmsh_1_1__TaskPanel.html#a684d236263b413e2d04839f3ce9cacb7),
[femtaskpanels.task_solver_ccxtools._TaskPanel.update()](../../da/df4/classfemtaskpanels_1_1task__solver__ccxtools_1_1__TaskPanel.html#ab71f275d8aa529999c628cf0435e9874),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.update_style()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#a498ea0c29ad69561734096f882857154),
[femtaskpanels.task_mesh_gmsh._TaskPanel.update_timer_text()](../../d6/d90/classfemtaskpanels_1_1task__mesh__gmsh_1_1__TaskPanel.html#a146532382b72ed3e7d70305b8c94271d),
[PathScripts.PathCircularHoleBaseGui.TaskPanelHoleGeometryPage.updateBase()](../../d3/dfd/classPathScripts_1_1PathCircularHoleBaseGui_1_1TaskPanelHoleGeometryPage.html#a052033eb156bea939788a85b4a2bbda7),
[PathScripts.PathEngraveGui.TaskPanelBaseGeometryPage.updateBase()](../../d0/d2e/classPathScripts_1_1PathEngraveGui_1_1TaskPanelBaseGeometryPage.html#a559dae7011efe851a54fc791750dcb50),
[PathScripts.PathOpGui.TaskPanelBaseGeometryPage.updateBase()](../../d4/dfc/classPathScripts_1_1PathOpGui_1_1TaskPanelBaseGeometryPage.html#acdc9a3f064f2f375c61869fa9aca10ac),
[PathScripts.PathVcarveGui.TaskPanelBaseGeometryPage.updateBase()](../../dc/d9b/classPathScripts_1_1PathVcarveGui_1_1TaskPanelBaseGeometryPage.html#ad3de941bd2524f1a9b69f6166254f717),
[PathScripts.PathDressupDogbone.TaskPanel.updateBoneList()](../../df/d54/classPathScripts_1_1PathDressupDogbone_1_1TaskPanel.html#afe3ba1f00b8d5c11cbc9da683fbcf0b0),
[PathScripts.PathFeatureExtensionsGui.TaskPanelExtensionPage.updateData()](../../d0/de3/classPathScripts_1_1PathFeatureExtensionsGui_1_1TaskPanelExtensionPage.html#ae9bf67c1be6b22bac31dbd2b64111264),
[PathScripts.PathPreferencesPathJob.JobPreferencesPage.updateDefaultPostProcessorToolTip()](../../db/dec/classPathScripts_1_1PathPreferencesPathJob_1_1JobPreferencesPage.html#aa7500314cc69071905c4ddd9bf564d86),
[PathScripts.PathDressupPathBoundaryGui.TaskPanel.updateDressup()](../../d4/d65/classPathScripts_1_1PathDressupPathBoundaryGui_1_1TaskPanel.html#a87025a0b1df9b78081247f9ca93b8448),
[PathScripts.PathDeburrGui.TaskPanelOpPage.updateExtraDepth()](../../d8/d57/classPathScripts_1_1PathDeburrGui_1_1TaskPanelOpPage.html#a9e9c6d5dcf90ac19d7bd7e63257fc2fb),
[AttachmentEditor.TaskAttachmentEditor.AttachmentEditorTaskPanel.updateListOfModes()](../../d8/d4c/classAttachmentEditor_1_1TaskAttachmentEditor_1_1AttachmentEditorTaskPanel.html#a875ee9614a4419f0359579deb222952b),
[femsolver.solver_taskpanel.ControlTaskPanel.updateMachine()](../../de/d8f/classfemsolver_1_1solver__taskpanel_1_1ControlTaskPanel.html#a0db57d6c44058ef3b34f6a2bf564b950),
[PathScripts.PathDressupDogbone.TaskPanel.updateMarkers()](../../df/d54/classPathScripts_1_1PathDressupDogbone_1_1TaskPanel.html#a523d964e27dbab843da6ca1f17eb9ef3),
[PathScripts.PathPocketBaseGui.TaskPanelOpPage.updateMinTravel()](../../d1/d25/classPathScripts_1_1PathPocketBaseGui_1_1TaskPanelOpPage.html#ae4b46dcbd3fba8cb4dbcb8778152e854),
[AttachmentEditor.TaskAttachmentEditor.AttachmentEditorTaskPanel.updatePreview()](../../d8/d4c/classAttachmentEditor_1_1TaskAttachmentEditor_1_1AttachmentEditorTaskPanel.html#ac9346cec8bcab000c5423d7449239e27),
[PathScripts.PathJobGui.TaskPanel.updateSelection()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#a6610036c947788e4b0bcb624bb9dd2c3),
[PathScripts.PathToolLibraryEditor.EditorPanel.updateSelection()](../../d0/d92/classPathScripts_1_1PathToolLibraryEditor_1_1EditorPanel.html#a31cf8384a83993f6f6e9ef2390338522),
[PathScripts.PathOpGui.TaskPanelBaseGeometryPage.updateSelection()](../../d4/dfc/classPathScripts_1_1PathOpGui_1_1TaskPanelBaseGeometryPage.html#a25560d3b1dfad3ba1f52555bd545098c),
[PathScripts.PathOpGui.TaskPanelDepthsPage.updateSelection()](../../da/d1a/classPathScripts_1_1PathOpGui_1_1TaskPanelDepthsPage.html#ad1444c55b041f8640e9074369f5d541a),
[PathScripts.PathPreferencesAdvanced.AdvancedPreferencesPage.updateSelection()](../../d5/d8b/classPathScripts_1_1PathPreferencesAdvanced_1_1AdvancedPreferencesPage.html#a84b9e8be6386c464b834fe84edddac66),
[PathScripts.PathToolBitEdit.ToolBitEditor.updateShape()](../../d6/d36/classPathScripts_1_1PathToolBitEdit_1_1ToolBitEditor.html#a2feff2bec16a74dd0908d20c6af9f2e2),
[PathScripts.PathCamoticsGui.CAMoticsUI.updateStatus()](../../d2/df4/classPathScripts_1_1PathCamoticsGui_1_1CAMoticsUI.html#a5e2dab257aa89c52d589774d9863b25a),
[PathScripts.PathDressupPathBoundaryGui.TaskPanel.updateStockEditor()](../../d4/d65/classPathScripts_1_1PathDressupPathBoundaryGui_1_1TaskPanel.html#a8be840649114568ffef2a95a70d93845),
[PathScripts.PathJobGui.TaskPanel.updateStockEditor()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#aa6c4e98158932bc79e6cedd462dcad48),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.updateTagsView()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#a400a8a81dde688fa51cfe40025e2220c),
[femtaskpanels.task_solver_ccxtools._TaskPanel.UpdateText()](../../da/df4/classfemtaskpanels_1_1task__solver__ccxtools_1_1__TaskPanel.html#ae02498c26a4a9315f58067aad516b221),
[PathScripts.PathToolBitEdit.ToolBitEditor.updateTool()](../../d6/d36/classPathScripts_1_1PathToolBitEdit_1_1ToolBitEditor.html#a4249a61897135e91f7687050142890f2),
[PathScripts.PathToolEdit.ToolEditorDefault.updateTool()](../../db/db4/classPathScripts_1_1PathToolEdit_1_1ToolEditorDefault.html#a6a2b24178b8115630bc688bf2055f751),
[PathScripts.PathToolEdit.ToolEditor.updateTool()](../../d2/df8/classPathScripts_1_1PathToolEdit_1_1ToolEditor.html#ac3e0bcb605d1d151d8d37925474cb8d2),
[PathScripts.PathJobGui.TaskPanel.updateToolController()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#abcc56d915abcc5fb3ac188ff13c6e6f5),
[PathScripts.PathToolControllerGui.ToolControllerEditor.updateToolController()](../../d2/db6/classPathScripts_1_1PathToolControllerGui_1_1ToolControllerEditor.html#a516c379e960635e9944622f3e8015b77),
[PathScripts.PathJobGui.TaskPanel.updateTooltips()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#a1879049d870232643010638da10a9491),
[PathScripts.PathToolEdit.ToolEditor.updateToolType()](../../d2/df8/classPathScripts_1_1PathToolEdit_1_1ToolEditor.html#a2ab9dc5c3f1a484ce30b642df4879fa3),
[Mod.PartDesign.FeatureHole.TaskHole.TaskHole.updateUI()](../../d1/d14/classMod_1_1PartDesign_1_1FeatureHole_1_1TaskHole_1_1TaskHole.html#aa58e6f5fe55c099a87f9e419c8edcd38),
[PathScripts.PathDressupAxisMap.TaskPanel.updateUI()](../../dd/de9/classPathScripts_1_1PathDressupAxisMap_1_1TaskPanel.html#a7abdbeead552f7fe20880fb9a3ca7504),
[PathScripts.PathDressupDogbone.TaskPanel.updateUI()](../../df/d54/classPathScripts_1_1PathDressupDogbone_1_1TaskPanel.html#a9a59e317716123fc7fa15fe7b2ec6326),
[PathScripts.PathPropertyBagGui.PropertyCreate.updateUI()](../../dd/d6e/classPathScripts_1_1PathPropertyBagGui_1_1PropertyCreate.html#ae6ce297311061270653b0e6ad855acf9),
[PathScripts.PathSetupSheetGui.GlobalEditor.updateUI()](../../de/df9/classPathScripts_1_1PathSetupSheetGui_1_1GlobalEditor.html#aa8b6f2a0dba387f2f70ee416b92863ee),
[PathScripts.PathToolBitEdit.ToolBitEditor.updateUI()](../../d6/d36/classPathScripts_1_1PathToolBitEdit_1_1ToolBitEditor.html#acb7bf247d1ebdbf54b964f52a44780cb),
[PathScripts.PathToolControllerGui.ToolControllerEditor.updateUi()](../../d2/db6/classPathScripts_1_1PathToolControllerGui_1_1ToolControllerEditor.html#a51eb9159a6f14fcc99cc648e433ddae3),
[PathScripts.PathToolEdit.ToolEditorDefault.updateUI()](../../db/db4/classPathScripts_1_1PathToolEdit_1_1ToolEditorDefault.html#aaea594e9685c5e1855482fd61ab3c096),
[PathScripts.PathToolEdit.ToolEditorImage.updateUI()](../../dd/df1/classPathScripts_1_1PathToolEdit_1_1ToolEditorImage.html#ab56beaabebfb14024f704898182930ad),
[PathScripts.PathToolEdit.ToolEditor.updateUI()](../../d2/df8/classPathScripts_1_1PathToolEdit_1_1ToolEditor.html#a901452eb82081a083d2b5d97ab8fe306),
[PathScripts.PathProfileGui.TaskPanelOpPage.updateVisibility()](../../db/d54/classPathScripts_1_1PathProfileGui_1_1TaskPanelOpPage.html#a893ae907fc53c0b26cd1ca4a21bbf7c1),
[PathScripts.PathSlotGui.TaskPanelOpPage.updateVisibility()](../../d2/da9/classPathScripts_1_1PathSlotGui_1_1TaskPanelOpPage.html#a3f51d9989ffe6b9c8ee9c0e41bb2fd82),
[PathScripts.PathSurfaceGui.TaskPanelOpPage.updateVisibility()](../../d7/d7a/classPathScripts_1_1PathSurfaceGui_1_1TaskPanelOpPage.html#a11bf2ea6faceb9fe83b2e80565934224),
[PathScripts.PathWaterlineGui.TaskPanelOpPage.updateVisibility()](../../d3/dcf/classPathScripts_1_1PathWaterlineGui_1_1TaskPanelOpPage.html#a172d89389727d8c517fac62dd381fcb1),
[femsolver.solver_taskpanel.ControlTaskPanel.updateWidget()](../../de/d8f/classfemsolver_1_1solver__taskpanel_1_1ControlTaskPanel.html#a4175c733f50ef814a06da2f8272017ac),
[PathScripts.PathDeburrGui.TaskPanelOpPage.updateWidth()](../../d8/d57/classPathScripts_1_1PathDeburrGui_1_1TaskPanelOpPage.html#a74b7201075fa6cc5fbb814b79a28ce96),
[PathScripts.PathJobGui.StockFromBaseBoundBoxEdit.updateXpos()](../../d6/df2/classPathScripts_1_1PathJobGui_1_1StockFromBaseBoundBoxEdit.html#a9e40222fe4273798e083323d6ae32fae),
[PathScripts.PathJobGui.StockFromBaseBoundBoxEdit.updateYpos()](../../d6/df2/classPathScripts_1_1PathJobGui_1_1StockFromBaseBoundBoxEdit.html#aad5ef42222d45e20a5db043025419cc5),
[PathScripts.PathPocketBaseGui.TaskPanelOpPage.updateZigZagAngle()](../../d1/d25/classPathScripts_1_1PathPocketBaseGui_1_1TaskPanelOpPage.html#ace4e9b0ed481ecee35bb1089234c73d1),
[PathScripts.PathJobGui.StockFromBaseBoundBoxEdit.updateZpos()](../../d6/df2/classPathScripts_1_1PathJobGui_1_1StockFromBaseBoundBoxEdit.html#a0cf326020295a91d670006c8202e4e75),
[drafttaskpanels.task_polararray.TaskPanelPolarArray.validate_input()](../../d7/d8d/classdrafttaskpanels_1_1task__polararray_1_1TaskPanelPolarArray.html#ac504fbf48bb8962308c66cb053e3e89a),
[drafttaskpanels.task_circulararray.TaskPanelCircularArray.validate_input()](../../dd/d3a/classdrafttaskpanels_1_1task__circulararray_1_1TaskPanelCircularArray.html#aab61622e012c46ef94520c65b9f4b25d),
[drafttaskpanels.task_orthoarray.TaskPanelOrthoArray.validate_input()](../../d6/dfa/classdrafttaskpanels_1_1task__orthoarray_1_1TaskPanelOrthoArray.html#a896ef86c9cf2324d5486dec9e6956f04),
[PathScripts.PathPreferencesPathJob.JobPreferencesPage.verifyAndUpdateDefaultPostProcessor()](../../db/dec/classPathScripts_1_1PathPreferencesPathJob_1_1JobPreferencesPage.html#a02565c1fa325ea633363b21106fd06c1),
[PathScripts.PathPreferencesPathJob.JobPreferencesPage.verifyAndUpdateDefaultPostProcessorWith()](../../db/dec/classPathScripts_1_1PathPreferencesPathJob_1_1JobPreferencesPage.html#a9396905d7094d47bb4a763defa7681d0),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.whenCountChanged()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#ad829e36c267f75e8feffd7dcd2ac41ce),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.whenTagSelectionChanged()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#a44283c1e06bcb62ab9da42df382c6d51),
and
[ArchSchedule.ArchScheduleTaskPanel.writeValues()](../../d5/da0/classArchSchedule_1_1ArchScheduleTaskPanel.html#a00a93e3bae2d14c6ffb5df4d5da1293d).

## ◆ tree

ArchCommands.SurveyTaskPanel.tree  
---  
  
Referenced by
[ArchComponent.ComponentTaskPanel.addElement()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#a21a385085defc9e8ccca8b2261a57314),
[ArchCommands.SurveyTaskPanel.exportCSV()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#af92d233658c91140db86272c111fc760),
[ArchCommands.SurveyTaskPanel.newline()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a57d6b27250bfa8a1a2e74be167af7bda),
[ArchSectionPlane.SectionPlaneTaskPanel.onTreeClick()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#ad1f64605e0e57561bb159696f4788fb0),
[ArchAxisSystem.AxisSystemTaskPanel.removeElement()](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a27e3fe8ffbc52acfd92f2d333626a76d),
[ArchComponent.ComponentTaskPanel.removeElement()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#ad9d18ffd3ef7556affab6b62a6acceb5),
[ArchSectionPlane.SectionPlaneTaskPanel.removeElement()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#a544dbf3def03e06b86e6f32c390fd46a),
[DraftGui.FacebinderTaskPanel.removeElement()](../../d2/d61/classDraftGui_1_1FacebinderTaskPanel.html#a8ce5c644e81d1fbb3907e351e2050a0a),
[ArchCommands.SurveyTaskPanel.retranslateUi()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a80aefc6bf17d60c63cd66e8984616d4b),
[ArchCommands.SurveyTaskPanel.setText()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#ad3c7a67dea06fdb170bb7e6d76224b1e),
[ArchAxisSystem.AxisSystemTaskPanel.update()](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a376cbba2ccee6efd86c46d0f0a8e99e3),
[ArchComponent.ComponentTaskPanel.update()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#af95b36032a3837b4bf1b92fe7c6a47e0),
[ArchSectionPlane.SectionPlaneTaskPanel.update()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#aab4bcd7b08950b8e3b37d801381c5162),
[DraftGui.FacebinderTaskPanel.update()](../../d2/d61/classDraftGui_1_1FacebinderTaskPanel.html#a191f43aa777ae22c42a00d118688bafe),
and
[ArchCommands.SurveyTaskPanel.update()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a77685c35ce185891696d5ac525070003).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Arch/ArchCommands.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

