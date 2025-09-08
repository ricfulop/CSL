---
url: https://freecad.github.io/SourceDoc/d7/d61/classArchCurtainWall_1_1ViewProviderCurtainWall.html
scraped_at: 2025-09-08T14:57:42.207842
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ArchCurtainWall](../../d7/dd3/namespaceArchCurtainWall.html)
  * [ViewProviderCurtainWall](../../d7/d61/classArchCurtainWall_1_1ViewProviderCurtainWall.html)

[List of all members](../../d7/d91/classArchCurtainWall_1_1ViewProviderCurtainWall-members.html) | Public Member Functions

ArchCurtainWall.ViewProviderCurtainWall Class Reference

##  Public Member Functions  
  
---  
def | [colorize](../../d7/d61/classArchCurtainWall_1_1ViewProviderCurtainWall.html#a2c7de1b2acf70db3bdb71a48c67cbd94) (self, obj, force=False)  
def | [getIcon](../../d7/d61/classArchCurtainWall_1_1ViewProviderCurtainWall.html#a07883fa28b0d7ec4534bb6628cd419e2) (self)  
def | [onChanged](../../d7/d61/classArchCurtainWall_1_1ViewProviderCurtainWall.html#add541f453903121b6540cd9361af9bc7) (self, vobj, prop)  
def | [updateData](../../d7/d61/classArchCurtainWall_1_1ViewProviderCurtainWall.html#a1c40a49ffebf36d0c5153dade5d6c8e0) (self, obj, prop)  
![-](../../closed.png) Public Member Functions inherited from
[ArchComponent.ViewProviderComponent](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html)  
def | [areDifferentColors](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#abef0fbecf4fb23a8a2e956782435dbc8) (self, a, b)  
def | [attach](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a35e80ee0b359823d7b9cecc23481b930) (self, vobj)  
def | [claimChildren](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a05a3bbd9534c922df9943f971fd60bf2) (self)  
def | [colorize](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#ac78064634eb8dcc79b78058091f9e93f) (self, obj, force=False)  
def | [getDisplayModes](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a0d8c5720e1a9f11604ad7e354b87c513) (self, vobj)  
def | [getIcon](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a82a5ba6de8551331198da2ba601e4bc2) (self)  
def | [onChanged](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a14303b12cf40f4c4393c5d86c08820bf) (self, vobj, prop)  
def | [setDisplayMode](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#aa0542b1ecb134c494a26706a5f41d099) (self, mode)  
def | [setEdit](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#aead5dc101b4fb331c6905a022017846d) (self, vobj, mode)  
def | [setProperties](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#abbd3e374ae515673bada8f848fbc98af) (self, vobj)  
def | [setupContextMenu](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a9cb06662d675ab2a3f956c0b7672a64c) (self, vobj, menu)  
def | [toggleSubcomponents](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#afdd01b4893303b90769e0870a675b7b9) (self)  
def | [unsetEdit](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#aee3ff9b804a7bb9866152879ca13b5e3) (self, vobj, mode)  
def | [updateData](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#ad521883fec55dd63135b0dbb597dabdb) (self, obj, prop)  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Public Attributes inherited from
[ArchComponent.ViewProviderComponent](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html)  
|
[hiresgroup](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#adb5745944ae9b415394ada099f13d717)  
|
[meshcolor](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#ab82023aa98281fdd4fdb9aee6eb05466)  
|
[meshnode](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#acb568729ce3429c521c62c72135e221a)  
|
[Object](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a597cb57c8f3b67265e32073313fc7140)  
  
## Member Function Documentation

## ◆ colorize()

def ArchCurtainWall.ViewProviderCurtainWall.colorize  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_ ,   
|  |  | _force_ = `False`  
| ) | |   
      
    
    If an object is a clone, set it to copy the color of its parent.
    
    Only change the color of the clone if the clone and its parent have
    colors that are distinguishably different from each other.
    
    Parameters
    ----------
    obj: <Part::Feature>
        The object to change the color of.
    force: bool
        If true, forces the colourisation even if the two objects have very
        similar colors.
    

Reimplemented from
[ArchComponent.ViewProviderComponent](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#ac78064634eb8dcc79b78058091f9e93f).

References
[ArchComponent.ViewProviderComponent.areDifferentColors()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#abef0fbecf4fb23a8a2e956782435dbc8),
and
[ArchCommands.getDefaultColor()](../../d4/d52/namespaceArchCommands.html#abfe83988dd63577babc96771bb3212a0).

Referenced by
[ArchCurtainWall.ViewProviderCurtainWall.onChanged()](../../d7/d61/classArchCurtainWall_1_1ViewProviderCurtainWall.html#add541f453903121b6540cd9361af9bc7),
and
[ArchCurtainWall.ViewProviderCurtainWall.updateData()](../../d7/d61/classArchCurtainWall_1_1ViewProviderCurtainWall.html#a1c40a49ffebf36d0c5153dade5d6c8e0).

## ◆ getIcon()

def ArchCurtainWall.ViewProviderCurtainWall.getIcon  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    Return the path to the appropriate icon.
    
    If a clone, return the cloned component icon path. Otherwise return the
    Arch Component icon.
    
    Returns
    -------
    str
        Path to the appropriate icon .svg file.
    

Reimplemented from
[ArchComponent.ViewProviderComponent](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a82a5ba6de8551331198da2ba601e4bc2).

Referenced by
[ArchAxisSystem.AxisSystemTaskPanel.update()](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a376cbba2ccee6efd86c46d0f0a8e99e3),
[ArchComponent.ComponentTaskPanel.update()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#af95b36032a3837b4bf1b92fe7c6a47e0),
and
[ArchSectionPlane.SectionPlaneTaskPanel.update()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#aab4bcd7b08950b8e3b37d801381c5162).

## ◆ onChanged()

def ArchCurtainWall.ViewProviderCurtainWall.onChanged  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _vobj_ ,   
|  |  | _prop_  
| ) | |   
      
    
    Method called when the view provider has a property changed.
    
    If DiffuseColor changes, change DiffuseColor to copy the host object's
    clone, if it exists.
    
    If ShapeColor changes, overwrite it with DiffuseColor.
    
    If Visibility changes, propagate the change to all view objects that
    are also hosted by this view object's host.
    
    Parameters
    ----------
    vobj: <Gui.ViewProviderDocumentObject>
        The component's view provider object.
    prop: string
        The name of the property that has changed.
    

Reimplemented from
[ArchComponent.ViewProviderComponent](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a14303b12cf40f4c4393c5d86c08820bf).

References
[ArchComponent.ViewProviderComponent.colorize()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#ac78064634eb8dcc79b78058091f9e93f),
[ArchCurtainWall.ViewProviderCurtainWall.colorize()](../../d7/d61/classArchCurtainWall_1_1ViewProviderCurtainWall.html#a2c7de1b2acf70db3bdb71a48c67cbd94),
ArchWindow._ViewProviderWindow.colorize(), and
[ArchComponent.ViewProviderComponent.onChanged()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#a14303b12cf40f4c4393c5d86c08820bf).

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

## ◆ updateData()

def ArchCurtainWall.ViewProviderCurtainWall.updateData  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_ ,   
|  |  | _prop_  
| ) | |   
      
    
    Method called when the host object has a property changed.
    
    If the object has a Material associated with it, match the view
    object's ShapeColor and Transparency to match the Material.
    
    If the object is now cloned, or is part of a compound, have the view
    object inherit the DiffuseColor.
    
    Parameters
    ----------
    obj: <App::FeaturePython>
        The host object that has changed.
    prop: string
        The name of the property that has changed.
    

Reimplemented from
[ArchComponent.ViewProviderComponent](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#ad521883fec55dd63135b0dbb597dabdb).

References
[ArchComponent.ViewProviderComponent.colorize()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#ac78064634eb8dcc79b78058091f9e93f),
[ArchCurtainWall.ViewProviderCurtainWall.colorize()](../../d7/d61/classArchCurtainWall_1_1ViewProviderCurtainWall.html#a2c7de1b2acf70db3bdb71a48c67cbd94),
and ArchWindow._ViewProviderWindow.colorize().

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

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Arch/ArchCurtainWall.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

