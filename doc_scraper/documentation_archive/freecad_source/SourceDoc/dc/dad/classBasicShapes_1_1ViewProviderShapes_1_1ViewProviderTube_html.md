---
url: https://freecad.github.io/SourceDoc/dc/dad/classBasicShapes_1_1ViewProviderShapes_1_1ViewProviderTube.html
scraped_at: 2025-09-08T15:18:30.374394
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [BasicShapes](../../de/d35/namespaceBasicShapes.html)
  * [ViewProviderShapes](../../db/d2d/namespaceBasicShapes_1_1ViewProviderShapes.html)
  * [ViewProviderTube](../../dc/dad/classBasicShapes_1_1ViewProviderShapes_1_1ViewProviderTube.html)

[List of all members](../../d7/dc8/classBasicShapes_1_1ViewProviderShapes_1_1ViewProviderTube-members.html) | Public Member Functions

BasicShapes.ViewProviderShapes.ViewProviderTube Class Reference

##  Public Member Functions  
  
---  
def | [attach](../../dc/dad/classBasicShapes_1_1ViewProviderShapes_1_1ViewProviderTube.html#a80e66be98d4db1973ffa8a5972e770ed) (self, obj)  
def | [getIcon](../../dc/dad/classBasicShapes_1_1ViewProviderShapes_1_1ViewProviderTube.html#ab484462b77962df3049eb511fa2b0285) (self)  
def | [setEdit](../../dc/dad/classBasicShapes_1_1ViewProviderShapes_1_1ViewProviderTube.html#a7457e7db7f6d3b56f283f0f8da2fdca3) (self, viewObject, mode)  
def | [setupContextMenu](../../dc/dad/classBasicShapes_1_1ViewProviderShapes_1_1ViewProviderTube.html#ac2ac3a9707a952797011121234376520) (self, viewObject, menu)  
def | [startDefaultEditMode](../../dc/dad/classBasicShapes_1_1ViewProviderShapes_1_1ViewProviderTube.html#a54a866ac46f008bd389ce4a272e4d2de) (self, viewObject)  
def | [unsetEdit](../../dc/dad/classBasicShapes_1_1ViewProviderShapes_1_1ViewProviderTube.html#ad42de523f01f9264b4522b6740ef7262) (self, viewObject, mode)  
  
## Member Function Documentation

## ◆ attach()

def BasicShapes.ViewProviderShapes.ViewProviderTube.attach  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_  
| ) | |   
      
    
     Setup the scene sub-graph of the view provider, this method is mandatory 

## ◆ getIcon()

def BasicShapes.ViewProviderShapes.ViewProviderTube.getIcon  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Referenced by
[ArchAxisSystem.AxisSystemTaskPanel.update()](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a376cbba2ccee6efd86c46d0f0a8e99e3),
[ArchComponent.ComponentTaskPanel.update()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#af95b36032a3837b4bf1b92fe7c6a47e0),
and
[ArchSectionPlane.SectionPlaneTaskPanel.update()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#aab4bcd7b08950b8e3b37d801381c5162).

## ◆ setEdit()

def BasicShapes.ViewProviderShapes.ViewProviderTube.setEdit  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _viewObject_ ,   
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

## ◆ setupContextMenu()

def BasicShapes.ViewProviderShapes.ViewProviderTube.setupContextMenu  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _viewObject_ ,   
|  |  | _menu_  
| ) | |   
  
## ◆ startDefaultEditMode()

def BasicShapes.ViewProviderShapes.ViewProviderTube.startDefaultEditMode  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _viewObject_  
| ) | |   
  
## ◆ unsetEdit()

def BasicShapes.ViewProviderShapes.ViewProviderTube.unsetEdit  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _viewObject_ ,   
|  |  | _mode_  
| ) | |   
  
Referenced by
[PathScripts.PathJobGui.ViewProvider.uneditObject()](../../d3/d3e/classPathScripts_1_1PathJobGui_1_1ViewProvider.html#aa663c276d96715669b3d07c7d2e34790).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Part/BasicShapes/ViewProviderShapes.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

