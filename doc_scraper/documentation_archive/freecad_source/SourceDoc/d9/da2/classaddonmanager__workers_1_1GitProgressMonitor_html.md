---
url: https://freecad.github.io/SourceDoc/d9/da2/classaddonmanager__workers_1_1GitProgressMonitor.html
scraped_at: 2025-09-08T14:53:07.078576
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [addonmanager_workers](../../d7/da4/namespaceaddonmanager__workers.html)
  * [GitProgressMonitor](../../d9/da2/classaddonmanager__workers_1_1GitProgressMonitor.html)

[List of all members](../../d6/d72/classaddonmanager__workers_1_1GitProgressMonitor-members.html) | Public Member Functions | Public Attributes

addonmanager_workers.GitProgressMonitor Class Reference

##  Public Member Functions  
  
---  
None | [update](../../d9/da2/classaddonmanager__workers_1_1GitProgressMonitor.html#a792da2433df991c6af7f84aa5d557918) (self, [int](../../d1/da0/classint.html) _, Union[[str](../../d9/d36/classstr.html), float] cur_count, Union[[str](../../d9/d36/classstr.html), float, None] max_count=None, [str](../../d9/d36/classstr.html) [message](../../d9/da2/classaddonmanager__workers_1_1GitProgressMonitor.html#a0c1dd2af12bffdd3ac3bd0df7d4effbc)="")  
  
##  Public Attributes  
  
---  
|
[current](../../d9/da2/classaddonmanager__workers_1_1GitProgressMonitor.html#aab2c7fabf27ca92b7b5216c92ac2689b)  
|
[message](../../d9/da2/classaddonmanager__workers_1_1GitProgressMonitor.html#a0c1dd2af12bffdd3ac3bd0df7d4effbc)  
|
[total](../../d9/da2/classaddonmanager__workers_1_1GitProgressMonitor.html#ac6d60830373933891713b487182fc66f)  
  
## Detailed Description

    
    
    An object that receives git progress updates and stores them for later display

## Member Function Documentation

## ◆ update()

None addonmanager_workers.GitProgressMonitor.update  | ( |  | _self_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | ___ ,   
|  | Union[[str](../../d9/d36/classstr.html), float]  | _cur_count_ ,   
|  | Union[[str](../../d9/d36/classstr.html), float, None]  | _max_count_ = `None`,   
|  | [str](../../d9/d36/classstr.html) | _message_ = `""`  
| ) | |   
  
References Base::FutureWatcherProgress.current,
[addonmanager_workers.GitProgressMonitor.current](../../d9/da2/classaddonmanager__workers_1_1GitProgressMonitor.html#aab2c7fabf27ca92b7b5216c92ac2689b),
[OfflineRenderingUtils.FreeCADGuiHandler.current](../../d6/dc4/classOfflineRenderingUtils_1_1FreeCADGuiHandler.html#a16036283bca22f1015323c93ad3ecd03),
nlohmann::detail::iterator_input_adapter< IteratorType >.current,
nlohmann::detail::lexer< BasicJsonType, InputAdapterType >.current,
nlohmann::detail::binary_reader< BasicJsonType, InputAdapterType, SAX
>.current,
[PartGui::Ui_TaskAttacher.message](../../d8/d60/classPartGui_1_1Ui__TaskAttacher.html#ad9ea0e3510ac0198fd292bfcb4a960a9),
[Gui::CustomMessageEvent.message()](../../d3/d7e/classGui_1_1CustomMessageEvent.html#ae9fea9c1ac5a502c8456e01bce875d9f),
[CustomReportEvent.message()](../../d4/d96/classCustomReportEvent.html#aa076091c0543ae883c525d32b7476c8c),
[Gui::MDIView.message()](../../df/d23/classGui_1_1MDIView.html#af9b79fc9fabec5dbf0558a94fbd2c14c),
[addonmanager_workers.GitProgressMonitor.message](../../d9/da2/classaddonmanager__workers_1_1GitProgressMonitor.html#a0c1dd2af12bffdd3ac3bd0df7d4effbc),
[Attacher::SuggestResult.message](../../d6/d4f/structAttacher_1_1SuggestResult.html#ab2b1b860a530404df8eec712ff873ce9),
[AttachmentEditor.TaskAttachmentEditor.CancelError.message](../../d8/d25/classAttachmentEditor_1_1TaskAttachmentEditor_1_1CancelError.html#accb27ad8a7e2d68e7a7eef01878037dd),
PartGui::TaskCheckGeometryResults.message,
[PartDesignGui::TaskDlgTransformedParameters.message](../../d3/d69/classPartDesignGui_1_1TaskDlgTransformedParameters.html#a553098dc2a185351f69812b710a51112),
and
[addonmanager_workers.GitProgressMonitor.total](../../d9/da2/classaddonmanager__workers_1_1GitProgressMonitor.html#ac6d60830373933891713b487182fc66f).

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

## ◆ current

addonmanager_workers.GitProgressMonitor.current  
---  
  
Referenced by
[OfflineRenderingUtils.FreeCADGuiHandler.endElement()](../../d6/dc4/classOfflineRenderingUtils_1_1FreeCADGuiHandler.html#a5af207d468e4861e0996effc1f9bc188),
[OfflineRenderingUtils.FreeCADGuiHandler.startElement()](../../d6/dc4/classOfflineRenderingUtils_1_1FreeCADGuiHandler.html#aa519a0e1bcaa939bb44302fadf47f069),
and
[addonmanager_workers.GitProgressMonitor.update()](../../d9/da2/classaddonmanager__workers_1_1GitProgressMonitor.html#a792da2433df991c6af7f84aa5d557918).

## ◆ message

addonmanager_workers.GitProgressMonitor.message  
---  
  
Referenced by
[addonmanager_workers.GitProgressMonitor.update()](../../d9/da2/classaddonmanager__workers_1_1GitProgressMonitor.html#a792da2433df991c6af7f84aa5d557918).

## ◆ total

addonmanager_workers.GitProgressMonitor.total  
---  
  
Referenced by
[addonmanager_workers.GitProgressMonitor.update()](../../d9/da2/classaddonmanager__workers_1_1GitProgressMonitor.html#a792da2433df991c6af7f84aa5d557918).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/AddonManager/addonmanager_workers.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

