---
url: https://freecad.github.io/SourceDoc/df/d0d/classArchComponent_1_1ArchSelectionObserver.html
scraped_at: 2025-09-08T14:57:33.174319
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ArchComponent](../../da/d62/namespaceArchComponent.html)
  * [ArchSelectionObserver](../../df/d0d/classArchComponent_1_1ArchSelectionObserver.html)

[List of all members](../../de/d20/classArchComponent_1_1ArchSelectionObserver-members.html) | Public Member Functions | Public Attributes

ArchComponent.ArchSelectionObserver Class Reference

##  Public Member Functions  
  
---  
def | [addSelection](../../df/d0d/classArchComponent_1_1ArchSelectionObserver.html#abd6b916e9a66ac26700ad6f4d0c2d30c) (self, document, [object](../../dc/dd8/classobject.html), element, position)  
  
##  Public Attributes  
  
---  
|
[hide](../../df/d0d/classArchComponent_1_1ArchSelectionObserver.html#a929f37fedcef6c02783c338c093888c9)  
|
[nextCommand](../../df/d0d/classArchComponent_1_1ArchSelectionObserver.html#a76c1412f5c28233dbb899932e91280e9)  
|
[origin](../../df/d0d/classArchComponent_1_1ArchSelectionObserver.html#a97b15efb3e81236a06c2fc734901d9cc)  
|
[watched](../../df/d0d/classArchComponent_1_1ArchSelectionObserver.html#a37e4e3078a1df7c3968ec6e764ffa210)  
  
## Detailed Description

    
    
    Selection observer used throughout the Arch module.
    
    When a nextCommand is specified, the observer fires a Gui command when
    anything is selected.
    
    When a watched object is specified, the observer will only fire when this
    watched object is selected.
    
    TODO: This could probably use a rework. Most of the functionality isn't
    used. It does not work correctly to reset the appearance of parent object
    in ComponentTaskPanel.editObject(), for example.
    
    Parameters
    ----------
    watched: <App::DocumentObject>, optional
        If no watched value is provided, functionality relating to origin
        and hide parameters will not occur. Only the nextCommand will fire.
    
        When a watched value is provided, the selection observer will only
        fire when the watched object has been selected.
    hide: bool
        Sets if the watched object should be hidden.
    origin: <App::DocumentObject, optional
        If provided, and hide is True, will make the origin object
        selectable, and opaque (set transparency to 0).
    nextCommand: str
        Name of Gui command to run when the watched object is selected, (if
        one is specified), or when anything is selected (if no watched
        object is specified).
    

## Member Function Documentation

## ◆ addSelection()

def ArchComponent.ArchSelectionObserver.addSelection  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _document_ ,   
|  |  | _object_ ,   
|  |  | _element_ ,   
|  |  | _position_  
| ) | |   
      
    
    Method called when a selection is made on the Gui.
    
    When a nextCommand is specified, fire a Gui command when anything is
    selected.
    
    When a watched object is specified, only fire when this watched object
    is selected.
    
    Parameters
    ----------
    document: str
        The document's Name.
    object: str
        The selected object's Name.
    element: str
        The element on the object that was selected, such as an edge or
        face.
    position:
        The location in XYZ space the selection was made.
    

References
[MeshGui::ViewProviderMeshCurvature.hide()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#ad83ab0bef7709bfdb7bd2ff4471d8ada),
[ArchSite.Compass.hide()](../../d9/d61/classArchSite_1_1Compass.html#af26d6b8d3ac61782438dfd0817dafb7a),
[DraftGui.DraftToolBar.hide()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#af33cb7298cd84bb944eb8a3727ec3dc8),
[draftguitools.gui_snapper.Snapper.hide()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#ac0a6c1298a2da5be5a42addc39cd2c49),
PathScripts.PathFeatureExtensionsGui._Extension.hide(),
[DocumentObject.ViewProvider.hide()](../../d8/dd7/classDocumentObject_1_1ViewProvider.html#a1a7e05fd45656f48d26c1c7e6bb973ba),
[Mod.Show.mTempoVis.TempoVis.hide()](../../d7/d98/classMod_1_1Show_1_1mTempoVis_1_1TempoVis.html#ac07ddaf03ecea19a49968f95a6f85c9f),
[Gui::ViewProvider.hide()](../../d3/db3/classGui_1_1ViewProvider.html#a6ebeb34c881fe262bfa6660683b52319),
[DrawingGui::ViewProviderDrawingPage.hide()](../../d7/d4d/classDrawingGui_1_1ViewProviderDrawingPage.html#a1a835fe20339fa1ff3a825c6481296e9),
[DrawingGui::ViewProviderDrawingView.hide()](../../d2/dce/classDrawingGui_1_1ViewProviderDrawingView.html#af1f9e27cb4717b1eab17df64def3a5a3),
[DrawingGui::ViewProviderDrawingClip.hide()](../../d3/d00/classDrawingGui_1_1ViewProviderDrawingClip.html#ae328b7a7c463a0cfe21fb19adb6a8cab),
[FemGui::ViewProviderFemAnalysis.hide()](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#a4850a42a90d0220afedd7226c2cb95d5),
[FemGui::ViewProviderFemPostObject.hide()](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#ad194bdde945ec44c617d1974ec5351f9),
[InspectionGui::ViewProviderInspection.hide()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a2c2b1c3a15d359f94134528eea3c370a),
[TechDrawGui::ViewProviderViewClip.hide()](../../d1/dc2/classTechDrawGui_1_1ViewProviderViewClip.html#a0dad53d8ccb241aa1ffaa1ca6cd0e85b),
[Gui::ViewProviderDocumentObject.hide()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#af961215142d52e0e355a89df19610333),
[ArchComponent.ArchSelectionObserver.hide](../../df/d0d/classArchComponent_1_1ArchSelectionObserver.html#a929f37fedcef6c02783c338c093888c9),
[FemFace.hide](../../d0/d1f/structFemFace.html#a1d133f593252d4d08846d63445b79036),
[PathScripts.PathToolEdit.ToolEditorImage.hide](../../dd/df1/classPathScripts_1_1PathToolEdit_1_1ToolEditorImage.html#aecc8459b98350f4e1e7c6a8c64219fd1),
[TechDrawGui::ViewProviderDrawingView.hide()](../../db/d6f/classTechDrawGui_1_1ViewProviderDrawingView.html#a76b2851b249a59575433a30cc5776432),
[TechDrawGui::ViewProviderPage.hide()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#afd1cfb51b69db6ac5816cf42df10eb2d),
[TechDrawGui::ViewProviderTemplate.hide()](../../dc/d9b/classTechDrawGui_1_1ViewProviderTemplate.html#add04ca12b8bd9d195f0d691688ae3e7a),
[ArchComponent.ArchSelectionObserver.nextCommand](../../df/d0d/classArchComponent_1_1ArchSelectionObserver.html#a76c1412f5c28233dbb899932e91280e9),
[ArchComponent.ArchSelectionObserver.origin](../../df/d0d/classArchComponent_1_1ArchSelectionObserver.html#a97b15efb3e81236a06c2fc734901d9cc),
[draftguitools.gui_trackers.rectangleTracker.origin](../../d7/d8d/classdraftguitools_1_1gui__trackers_1_1rectangleTracker.html#a2e34ede99ecb73ab65eece9dca0fb6bd),
[PartGui::DimensionLinear.origin](../../d7/d39/classPartGui_1_1DimensionLinear.html#a5a389d34212672dcfa9a6d85d04e8572),
PartGui::VectorAdapter.origin,
[PathScripts.PathStock.StockFromBase.origin](../../d1/d74/classPathScripts_1_1PathStock_1_1StockFromBase.html#aa6eb74047b63b1b84262a5eb2fae29b5),
KDL::Joint.origin,
[TechDraw::DrawViewBalloon.origin](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a7af17936c4a3201383e1527301444fd1),
and
[ArchComponent.ArchSelectionObserver.watched](../../df/d0d/classArchComponent_1_1ArchSelectionObserver.html#a37e4e3078a1df7c3968ec6e764ffa210).

## Member Data Documentation

## ◆ hide

ArchComponent.ArchSelectionObserver.hide  
---  
  
Referenced by
[ArchComponent.ArchSelectionObserver.addSelection()](../../df/d0d/classArchComponent_1_1ArchSelectionObserver.html#abd6b916e9a66ac26700ad6f4d0c2d30c),
[Mod.Show.mTempoVis.TempoVis.hide_all_dependencies()](../../d7/d98/classMod_1_1Show_1_1mTempoVis_1_1TempoVis.html#a3e3225ff34a80f32b99dd564b4eb3657),
[Mod.Show.mTempoVis.TempoVis.hide_all_dependent()](../../d7/d98/classMod_1_1Show_1_1mTempoVis_1_1TempoVis.html#a5092d1f6ba718c2056c4de9d0df34f61),
[PathScripts.PathToolEdit.ToolEditorImage.setupUI()](../../dd/df1/classPathScripts_1_1PathToolEdit_1_1ToolEditorImage.html#a084ad5441e84f4bab1e2ab96bb45e09f),
and
[PathScripts.PathToolEdit.ToolEditorImage.updateTool()](../../dd/df1/classPathScripts_1_1PathToolEdit_1_1ToolEditorImage.html#acc3d4c7e3670300bb09c552d68664e00).

## ◆ nextCommand

ArchComponent.ArchSelectionObserver.nextCommand  
---  
  
Referenced by
[ArchComponent.ArchSelectionObserver.addSelection()](../../df/d0d/classArchComponent_1_1ArchSelectionObserver.html#abd6b916e9a66ac26700ad6f4d0c2d30c).

## ◆ origin

ArchComponent.ArchSelectionObserver.origin  
---  
  
Referenced by
[ArchComponent.ArchSelectionObserver.addSelection()](../../df/d0d/classArchComponent_1_1ArchSelectionObserver.html#abd6b916e9a66ac26700ad6f4d0c2d30c),
[PathScripts.PathStock.StockFromBase.execute()](../../d1/d74/classPathScripts_1_1PathStock_1_1StockFromBase.html#a9fa59e6edf99801ba45c953b49561ae2),
[draftguitools.gui_trackers.rectangleTracker.setorigin()](../../d7/d8d/classdraftguitools_1_1gui__trackers_1_1rectangleTracker.html#ae479b57eba5124cc3051bf736a1f7269),
and
[draftguitools.gui_trackers.rectangleTracker.update()](../../d7/d8d/classdraftguitools_1_1gui__trackers_1_1rectangleTracker.html#acedcfce459af33f633a1aa7e57501a7f).

## ◆ watched

ArchComponent.ArchSelectionObserver.watched  
---  
  
Referenced by
[ArchComponent.ArchSelectionObserver.addSelection()](../../df/d0d/classArchComponent_1_1ArchSelectionObserver.html#abd6b916e9a66ac26700ad6f4d0c2d30c).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Arch/ArchComponent.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

