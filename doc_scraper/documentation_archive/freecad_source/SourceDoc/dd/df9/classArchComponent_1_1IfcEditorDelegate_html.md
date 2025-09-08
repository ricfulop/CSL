---
url: https://freecad.github.io/SourceDoc/dd/df9/classArchComponent_1_1IfcEditorDelegate.html
scraped_at: 2025-09-08T14:57:36.203172
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ArchComponent](../../da/d62/namespaceArchComponent.html)
  * [IfcEditorDelegate](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html)

[List of all members](../../d6/db1/classArchComponent_1_1IfcEditorDelegate-members.html) | Public Member Functions | Public Attributes

ArchComponent.IfcEditorDelegate Class Reference

##  Public Member Functions  
  
---  
def | [createEditor](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#a7b151b586b40ed6dce1516b3050e0b8c) (self, parent, option, index)  
def | [setEditorData](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#a2cfb48de6dc71c6b79fa899ec26df952) (self, editor, index)  
def | [setModelData](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#a1650f566d64beed8bdab63018e9da05e) (self, editor, model, index)  
  
##  Public Attributes  
  
---  
|
[dialog](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#adbc52010133bf10d5364aa3876413d3b)  
|
[plabels](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#a756c3ed29e5353e19de067dba1a6bc31)  
|
[ptypes](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#a855b775a6481b1e3a327a15714452b67)  
  
## Detailed Description

    
    
    This class manages the editing of the individual table cells in the IFC editor.
    
    Parameters
    ----------
    parent: <PySide2.QtWidgets.QWidget>
        Unclear.
    dialog: <ArchComponent.ComponentTaskPanel>
        The dialog box this delegate was created in.
    ptypes: list of str
        A list of the names of IFC property types.
    plables: list of str
        A list of the human readable names of IFC property types.
    

## Member Function Documentation

## ◆ createEditor()

def ArchComponent.IfcEditorDelegate.createEditor  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _parent_ ,   
|  |  | _option_ ,   
|  |  | _index_  
| ) | |   
      
    
    Return the widget used to change data.
    
    Return a text line editor if editing the property name.  Return a
    dropdown to change property type if editing property type.  If
    editing the property's value, return an appropriate widget
    depending on the datatype of the value.
    
    Parameters
    ----------
    parent: <pyside2.qtwidgets.qwidget>
        The table cell that is being edited.
    option:
        Unused?
    index: <PySide2.QtCore.QModelIndex>
        The index object of the table of the IFC editor.
    
    Returns
    -------
    <pyside2.qtwidgets.qwidget>
        The editor widget this method has created.
    

## ◆ setEditorData()

def ArchComponent.IfcEditorDelegate.setEditorData  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _editor_ ,   
|  |  | _index_  
| ) | |   
      
    
    Give data to the edit widget.
    
    Extract the data already present in the table, and write it to the
    editor. This means the user starts the editor with their previous
    data already present, instead of a blank slate.
    
    Parameters
    ----------
    editor: <pyside2.qtwidgets.qwidget>
        The editor widget.
    index: <PySide2.QtCore.QModelIndex>
        The index object of the table, of the IFC editor
    

References
[ArchComponent.ComponentTaskPanel.plabels](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#a19aabf74bdad400825cc225f7919327e),
and
[ArchComponent.IfcEditorDelegate.plabels](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#a756c3ed29e5353e19de067dba1a6bc31).

## ◆ setModelData()

def ArchComponent.IfcEditorDelegate.setModelData  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _editor_ ,   
|  |  | _model_ ,   
|  |  | _index_  
| ) | |   
      
    
    Write the data in the editor to the IFC editor's table.
    
    Parameters
    ----------
    editor: <pyside2.qtwidgets.qwidget>
        The editor widget.
    model:
        The table object of the IFC editor.
    index: <PySide2.QtCore.QModelIndex>
        The index object of the table, of the IFC editor
    

References Gui::Dialog::DlgParameterFind.dialog,
[RemoteDebugger.RemoteDebugger.dialog](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a36d8e434a10fb9e7d1aae9e2bc635c71),
Gui::Dialog::TaskTextureMapping.dialog, Gui::Dialog::TaskTransform.dialog,
[AddonManager.CommandAddonManager.dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab6a31ca97dab5476ffeccb0e8b5bd071),
[ArchComponent.IfcEditorDelegate.dialog](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#adbc52010133bf10d5364aa3876413d3b),
[draftguitools.gui_shapestrings.ShapeString.dialog](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#a4d72dff4351e71a8639459fbc9a1b353),
[draftguitools.gui_texts.Text.dialog](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a66c664551f3a6e28ada5fb99f8051ea0),
[PathScripts.PathJobDlg.JobCreate.dialog](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#af69757ca6b013ee2b5ad64272f26d74f),
[PathScripts.PathJobDlg.JobTemplateExport.dialog](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abbe5f7d6383f5e8a5bc27619fd557cc8),
[PathScripts.PathPost.DlgSelectPostProcessor.dialog](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a35ed78937500551699c74f44a7ca92e3),
[ArchComponent.ComponentTaskPanel.plabels](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#a19aabf74bdad400825cc225f7919327e),
and
[ArchComponent.IfcEditorDelegate.plabels](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#a756c3ed29e5353e19de067dba1a6bc31).

## Member Data Documentation

## ◆ dialog

ArchComponent.IfcEditorDelegate.dialog  
---  
  
Referenced by
[RemoteDebugger.RemoteDebugger.accept()](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#ae2ed6ffa5958b758f58b061ab5ab5aa7),
[PathScripts.PathJobDlg.JobTemplateExport.checkUncheckTools()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#a11c5eb6fce8ecee3c9352aa50ed686ac),
[AddonManager.CommandAddonManager.dependency_installation_failure()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa52493ff30557ea04b4000c33243abac),
[AddonManager.CommandAddonManager.do_next_startup_phase()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#afc0b4e496960a62e610043b953ec028b),
[AddonManager.CommandAddonManager.enable_updates()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#afbe900e4d7a33a684336a1e4ba2910f9),
[RemoteDebugger.RemoteDebugger.exec_()](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a97a015d8cfdfae14723535c0b848a9aa),
[PathScripts.PathJobDlg.JobCreate.exec_()](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#a3949bbe83170d8e065b74724bcde9e2a),
[PathScripts.PathJobDlg.JobTemplateExport.exec_()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#a0e1d5958964dcb0592e9e1582a2b02ec),
[PathScripts.PathPost.DlgSelectPostProcessor.exec_()](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a08d96f772033302b5f80db42c9ba3ae7),
[AddonManager.CommandAddonManager.executemacro()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa9a71a1815f63568b938dd0ec14dc2be),
[PathScripts.PathJobDlg.JobTemplateExport.exportButton()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#a3bea8dbb69e7ff35e1b282948568c1d3),
[draftguitools.gui_texts.Text.finish()](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a3fe64be64c77319af1f265609dd8e985),
[AddonManager.CommandAddonManager.force_check_updates()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a59ef1319a65cb46f3dab02bb23a7158d),
[PathScripts.PathJobDlg.JobCreate.getTemplate()](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#aff1aa651e747f139e2857baa3ac098cd),
[AddonManager.CommandAddonManager.handle_disallowed_python()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a98d4404b8f0a7b16cff129ea4e65c8f4),
[AddonManager.CommandAddonManager.hide_progress_widgets()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab5aa671118056f1c4e1b25468c63a02e),
[PathScripts.PathJobDlg.JobTemplateExport.includePostProcessing()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#a5c0ae3a25dd31d7852c33ba61a077463),
[PathScripts.PathJobDlg.JobTemplateExport.includeSettingCoolant()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abd2430ce061573743a362f761e0edf43),
[PathScripts.PathJobDlg.JobTemplateExport.includeSettingOperationDepths()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#a13a21bb42ed7f99ad2b0adae828162af),
[PathScripts.PathJobDlg.JobTemplateExport.includeSettingOperationHeights()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#ac27ee58071125bf488a3dec81cbcccfd),
[PathScripts.PathJobDlg.JobTemplateExport.includeSettingOpsSettings()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#a29e5c0c9eee24a216ba723ab92ad49ca),
[PathScripts.PathJobDlg.JobTemplateExport.includeSettings()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#a2d9abd88c9a00cf383c0c5f0521c22ee),
[PathScripts.PathJobDlg.JobTemplateExport.includeSettingToolRapid()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#a533790f9f6f5d30189750c73c3bc5920),
[PathScripts.PathJobDlg.JobTemplateExport.includeStock()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#a27be0d3af9b7a30e228c80e7841fbb78),
[PathScripts.PathJobDlg.JobTemplateExport.includeStockExtent()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#ae3e2784d39e0002d29ed7849e7644abc),
[PathScripts.PathJobDlg.JobTemplateExport.includeStockPlacement()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abc0e5c85e8c1e1abdaf83b287b1f255d),
[PathScripts.PathJobDlg.JobTemplateExport.includeToolControllers()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#a95880615cff4e1fdf5a478d87ae0aa89),
[AddonManager.CommandAddonManager.no_pip()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#abe9fbe57e535559f53434676040a0f80),
[AddonManager.CommandAddonManager.no_python_exe()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a02ecc07f773ae69b309435ae5df313f7),
[AddonManager.CommandAddonManager.on_buttonUpdateCache_clicked()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa49366f509bb5b61e1d518f286f05adf),
[AddonManager.CommandAddonManager.on_installation_failed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ac8cf465e055e3880d958923bcf98f094),
[AddonManager.CommandAddonManager.on_package_installed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#abf1dbc5ed9bc3918e6f96dda28954770),
[AddonManager.CommandAddonManager.on_update_all_completed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a1fa2c3ccb5f70dcb1d20df00bbb40982),
[RemoteDebugger.RemoteDebugger.reject()](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a04c50a1b4f01889e599a863e1cede497),
[AddonManager.CommandAddonManager.reject()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aef345e1dbcc980bf3d435f6c365905ca),
[AddonManager.CommandAddonManager.remove()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aae7cdf308d96b87d195e7be2de765a00),
[AddonManager.CommandAddonManager.report_missing_workbenches()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a90d0c6b99bc0b3a71e3f98d69c6dc3b2),
[ArchComponent.IfcEditorDelegate.setModelData()](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#a1650f566d64beed8bdab63018e9da05e),
[PathScripts.PathJobDlg.JobCreate.setupModel()](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#af073d7eb130a89da63d46c0b5365ebd6),
[PathScripts.PathJobDlg.JobCreate.setupTemplate()](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#a80e4cb8c0244d4087827496e639a0047),
[PathScripts.PathJobDlg.JobCreate.setupTitle()](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#afb9f2a2deb2c8b0d282c4381f178b314),
[AddonManager.CommandAddonManager.show_information()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa2f17e60211c4a2e322e8801da6ff052),
[AddonManager.CommandAddonManager.show_progress_widgets()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#af9df8398a3a7418385e7368fe10f6fe0),
[AddonManager.CommandAddonManager.stop_update()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a625e178c0cc51da55bfb3c7b93595000),
[AddonManager.CommandAddonManager.update_check_complete()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad6f86c6ddb56f3acd0d7b6985c49e936),
[AddonManager.CommandAddonManager.update_progress_bar()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a552bbbcaaddfd7c7a3b3c15b1c3235b3),
[PathScripts.PathPost.DlgSelectPostProcessor.updateTooltip()](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a7d0bd03437af3799d01917c0f65a8586),
and
[PathScripts.PathJobDlg.JobTemplateExport.updateUI()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#add858b24fbcff0183f70f02aacb541f0).

## ◆ plabels

ArchComponent.IfcEditorDelegate.plabels  
---  
  
Referenced by
[ArchComponent.ComponentTaskPanel.acceptIfcProperties()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#ab460d4a3baa8a41b6778461a2a2958b1),
[ArchComponent.ComponentTaskPanel.addIfcProperty()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#a41a48be97bdb4db134e5b083e143c4f7),
[ArchComponent.IfcEditorDelegate.setEditorData()](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#a2cfb48de6dc71c6b79fa899ec26df952),
and
[ArchComponent.IfcEditorDelegate.setModelData()](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#a1650f566d64beed8bdab63018e9da05e).

## ◆ ptypes

ArchComponent.IfcEditorDelegate.ptypes  
---  
  
Referenced by
[ArchComponent.ComponentTaskPanel.acceptIfcProperties()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#ab460d4a3baa8a41b6778461a2a2958b1),
and
[ArchComponent.ComponentTaskPanel.addIfcProperty()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#a41a48be97bdb4db134e5b083e143c4f7).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Arch/ArchComponent.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

