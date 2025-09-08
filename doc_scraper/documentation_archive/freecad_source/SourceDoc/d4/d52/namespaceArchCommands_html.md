---
url: https://freecad.github.io/SourceDoc/d4/d52/namespaceArchCommands.html
scraped_at: 2025-09-08T14:57:29.302219
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

Classes | Functions

ArchCommands Namespace Reference

[Workbenches](../../d2/df2/group__WORKBENCHES.html) » [Python
workbenches](../../d1/d82/group__PYTHONWORKBENCHES.html) »
[Arch](../../df/dce/group__ARCH.html)

Utility functions for the [Arch](../../df/dc6/namespaceArch.html)
[Workbench](../../da/d26/classWorkbench.html).
[More...](../../d4/d52/namespaceArchCommands.html#details)

##  Classes  
  
---  
class | [SurveyTaskPanel](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html)  
  
##  Functions  
  
---  
def | [addComponents](../../d4/d52/namespaceArchCommands.html#a8287616509ce8d3b41bf7628abbd331c) (objectsList, host)  
def | [check](../../d4/d52/namespaceArchCommands.html#a711cf551f0bed73105abcd328ec2e527) (objectslist, includehidden=False)  
def | [cleanArchSplitter](../../d4/d52/namespaceArchCommands.html#a6b92687884b8c04ca9c52e7df9ae99b5) (objects=None)  
def | [cloneComponent](../../d4/d52/namespaceArchCommands.html#a43c20fa7529b3f7afc858e65966d268e) (obj)  
def | [closeHole](../../d4/d52/namespaceArchCommands.html#aa465eac40edecce3e75c8fa38576a80a) (shape)  
def | [copyProperties](../../d4/d52/namespaceArchCommands.html#afa3427cb1ac2cb051a2424ae9236eba0) (obj1, obj2)  
def | [download](../../d4/d52/namespaceArchCommands.html#a3f0173b5c487667a4ebcb8531b3b9863) (url, force=False)  
def | [getAllChildren](../../d4/d52/namespaceArchCommands.html#aa4ea8ff7a1f01ab48b4c429db173c986) (objectlist)  
def | [getCutVolume](../../d4/d52/namespaceArchCommands.html#aa9bddbee3691ffd7b3cba2f35e55ce77) (cutplane, shapes, clip=False, depth=None)  
def | [getDefaultColor](../../d4/d52/namespaceArchCommands.html#abfe83988dd63577babc96771bb3212a0) (objectType)  
def | [getExtrusionData](../../d4/d52/namespaceArchCommands.html#ab65511367c7ab694de78f77c4da6453a) (shape, sortmethod="area")  
def | [getHost](../../d4/d52/namespaceArchCommands.html#a0f3cb7055a7b61252475246478e1430d) (obj, strict=True)  
def | [getShapeFromMesh](../../d4/d52/namespaceArchCommands.html#a37db9c820a988faeb31d27d7dbb00dbe) (mesh, fast=True, tolerance=0.001, flat=False, cut=True)  
def | [getStringList](../../d4/d52/namespaceArchCommands.html#a4519a770295e841921618e6a43744bb2) (objects)  
def | [makeComponent](../../d4/d52/namespaceArchCommands.html#a5e52b2724d4491e3e30c0875a2f0d845) (baseobj=None, name="Component", delete=False)  
def | [makeCompoundFromSelected](../../d4/d52/namespaceArchCommands.html#afde12c414c0e63408b385bf2fcf92e72) (objects=None)  
def | [makeFace](../../d4/d52/namespaceArchCommands.html#a98c94780af071056a7971a4ba882832e) (wires, method=2, cleanup=False)  
def | [makeIfcSpreadsheet](../../d4/d52/namespaceArchCommands.html#af3c876fb829d2ff5051e65e5a0eaa7c6) (archobj=None)  
def | [mergeCells](../../d4/d52/namespaceArchCommands.html#ac37be91f5b34674f97c6dc9c7889c54d) (objectslist)  
def | [meshToShape](../../d4/d52/namespaceArchCommands.html#a212eee2155be7c16f8a4817ca33d1057) (obj, mark=True, fast=True, tol=0.001, flat=False, cut=True)  
def | [printMessage](../../d4/d52/namespaceArchCommands.html#a7cf139de3565c96081296b4ab4b15421) (message)  
def | [printWarning](../../d4/d52/namespaceArchCommands.html#aa246a606bc319851e58c55f66d7693e6) (message)  
def | [projectToVector](../../d4/d52/namespaceArchCommands.html#a0f73f9076e0b2e2d1d651348d008522a) (shape, vector)  
def | [pruneIncluded](../../d4/d52/namespaceArchCommands.html#a1d99424f677b8bd1ea21df527c0a8f0f) (objectslist, strict=False)  
def | [rebuildArchShape](../../d4/d52/namespaceArchCommands.html#ab5e241befaf6e37b4788b6efc6042bae) (objects=None)  
def | [removeComponents](../../d4/d52/namespaceArchCommands.html#a42827993f20cf7bca87c7a9d1fbbaaac) (objectsList, host=None)  
def | [removeCurves](../../d4/d52/namespaceArchCommands.html#ab1a7fc05792ac9dfa9a7f861338ec713) (shape, dae=False, tolerance=5)  
def | [removeShape](../../d4/d52/namespaceArchCommands.html#af251273d7e60f828f0cafd22e4a881b1) (objs, mark=True)  
def | [setAsSubcomponent](../../d4/d52/namespaceArchCommands.html#ab6ea06dd24271c406f4e1f9a9e555c6a) (obj)  
def | [splitMesh](../../d4/d52/namespaceArchCommands.html#a3e09c50fc5b3a4a23b00cc702097d119) (obj, mark=True)  
def | [string_replace](../../d4/d52/namespaceArchCommands.html#af256192f97a16dc89632e0e9fd0c804b) (text, pattern, replacement)  
def | [survey](../../d4/d52/namespaceArchCommands.html#a2a97d8ae69e51460196b4d3e0d6859f1) (callback=False)  
def | [toggleIfcBrepFlag](../../d4/d52/namespaceArchCommands.html#afef50dee48c82402a2215afb55cd95f1) (obj)  
  
## Detailed Description

Utility functions for the [Arch](../../df/dc6/namespaceArch.html)
[Workbench](../../da/d26/classWorkbench.html).

This module provides general functions used by
[Arch](../../df/dc6/namespaceArch.html) tools and utility commands

## Function Documentation

## ◆ addComponents()

def ArchCommands.addComponents  | ( |  | _objectsList_ ,   
---|---|---|---  
|  |  | _host_  
| ) | |   
      
    
    addComponents(objectsList,hostObject): adds the given object or the objects
    from the given list as components to the given host Object. Use this for
    example to add windows to a wall, or to add walls to a cell or floor.

Referenced by
[importIFClegacy.read()](../../db/d15/namespaceimportIFClegacy.html#a8d7878f0b7576afcda6b95e88c5776e4).

## ◆ check()

def ArchCommands.check  | ( |  | _objectslist_ ,   
---|---|---|---  
|  |  | _includehidden_ = `False`  
| ) | |   
      
    
    check(objectslist,includehidden=False): checks if the given objects contain only solids

Referenced by
[printWarning()](../../d4/d52/namespaceArchCommands.html#aa246a606bc319851e58c55f66d7693e6).

## ◆ cleanArchSplitter()

def ArchCommands.cleanArchSplitter  | ( |  | _objects_ = `None`| ) |   
---|---|---|---|---|---  
      
    
    cleanArchSplitter([objects]): removes the splitters from the base shapes
    of the given Arch objects or selected Arch objects if objects is None

## ◆ cloneComponent()

def ArchCommands.cloneComponent  | ( |  | _obj_| ) |   
---|---|---|---|---|---  
      
    
    cloneComponent(obj): Creates a clone of an object as an undefined component

References
[makeComponent()](../../d4/d52/namespaceArchCommands.html#a5e52b2724d4491e3e30c0875a2f0d845).

## ◆ closeHole()

def ArchCommands.closeHole  | ( |  | _shape_| ) |   
---|---|---|---|---|---  
      
    
    closeHole(shape): closes a hole in an open shape

Referenced by
[printWarning()](../../d4/d52/namespaceArchCommands.html#aa246a606bc319851e58c55f66d7693e6).

## ◆ copyProperties()

def ArchCommands.copyProperties  | ( |  | _obj1_ ,   
---|---|---|---  
|  |  | _obj2_  
| ) | |   
      
    
    copyProperties(obj1,obj2): Copies properties values from obj1 to obj2,
    when that property exists in both objects

## ◆ download()

def ArchCommands.download  | ( |  | _url_ ,   
---|---|---|---  
|  |  | _force_ = `False`  
| ) | |   
      
    
    download(url,force=False): downloads a file from the given URL and saves it in the
    macro path. Returns the path to the saved file. If force is True, the file will be
    downloaded again evn if it already exists.

Referenced by
[importDXF.errorDXFLib()](../../d7/dbf/namespaceimportDXF.html#afe38bedfa6c04e0f9ae5e9495cfeb0bf),
and
[importIFClegacy.getSchema()](../../db/d15/namespaceimportIFClegacy.html#aae935448893346c21c75de97edc418d3).

## ◆ getAllChildren()

def ArchCommands.getAllChildren  | ( |  | _objectlist_| ) |   
---|---|---|---|---|---  
  
References
[getAllChildren()](../../d4/d52/namespaceArchCommands.html#aa4ea8ff7a1f01ab48b4c429db173c986).

Referenced by
[getAllChildren()](../../d4/d52/namespaceArchCommands.html#aa4ea8ff7a1f01ab48b4c429db173c986).

## ◆ getCutVolume()

def ArchCommands.getCutVolume  | ( |  | _cutplane_ ,   
---|---|---|---  
|  |  | _shapes_ ,   
|  |  | _clip_ = `False`,   
|  |  | _depth_ = `None`  
| ) | |   
      
    
    getCutVolume(cutplane,shapes,[clip,depth]): returns a cut face and a cut volume
    from the given shapes and the given cutting plane. If clip is True, the cutvolume will
    also cut off everything outside the cutplane projection. If depth is non-zero, geometry
    further than this distance will be clipped off

References
[DraftVecUtils.project()](../../dc/dc3/group__DRAFTVECUTILS.html#ga1bf889753387ffb78fb07cb90abed8bc),
and
[DraftVecUtils.scaleTo()](../../dc/dc3/group__DRAFTVECUTILS.html#ga6b1b9879299d28cb689cbee684e9d5f3).

Referenced by
[ArchVRM.Renderer.cut()](../../d5/dfd/classArchVRM_1_1Renderer.html#a42a08e8de6110aefc78bdfd483206b10),
[ArchCutPlane.cutComponentwithPlane()](../../d5/da7/namespaceArchCutPlane.html#aa1ff7471ad5f704a5ff1c96224450a23),
[ArchSectionPlane.getCutShapes()](../../d8/d49/namespaceArchSectionPlane.html#ad98fe70f703c12fd886e5d69fa88e200),
[ArchPipe.makePipeConnector()](../../de/d7d/namespaceArchPipe.html#ad0045d91c1268a704a446908729aaa5f),
and
[ArchSpace.removeSpaceBoundaries()](../../d8/d6a/namespaceArchSpace.html#aca020b8800ac48fabbf4fce2a0f16cee).

## ◆ getDefaultColor()

def ArchCommands.getDefaultColor  | ( |  | _objectType_| ) |   
---|---|---|---|---|---  
      
    
    getDefaultColor(string): returns a color value for the given object
    type (Wall, Structure, Window, WindowGlass)

Referenced by
[ArchPanel.CommandPanelSheet.Activated()](../../d1/d94/classArchPanel_1_1CommandPanelSheet.html#abed1cd5ce53c5b156683ae24b81f75e4),
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[ArchWall.areSameWallTypes()](../../d2/d8e/namespaceArchWall.html#a289f6e980eba7dd10b74dcfb84dd0c92),
[ArchSectionPlane.closeViewer()](../../d8/d49/namespaceArchSectionPlane.html#aa159e2389526d677138c754c18152c1c),
[ArchCurtainWall.ViewProviderCurtainWall.colorize()](../../d7/d61/classArchCurtainWall_1_1ViewProviderCurtainWall.html#a2c7de1b2acf70db3bdb71a48c67cbd94),
[ArchAxis.makeAxis()](../../db/d0d/namespaceArchAxis.html#a70adcb27c65b4028ce6335ed7a491edc),
[ArchRebar.makeRebar()](../../dd/de9/namespaceArchRebar.html#a4f9bf27bce35bf45fc8f02cfd5a8078d),
[ArchSpace.removeSpaceBoundaries()](../../d8/d6a/namespaceArchSpace.html#aca020b8800ac48fabbf4fce2a0f16cee),
and
[setAsSubcomponent()](../../d4/d52/namespaceArchCommands.html#ab6ea06dd24271c406f4e1f9a9e555c6a).

## ◆ getExtrusionData()

def ArchCommands.getExtrusionData  | ( |  | _shape_ ,   
---|---|---|---  
|  |  | _sortmethod_ = `"area"`  
| ) | |   
      
    
    If a shape has been extruded, returns the base face, and extrusion vector.
    
    Determines if a shape appears to have been extruded from some base face, and
    extruded at the normal from that base face. IE: it looks like a cuboid.
    https://en.wikipedia.org/wiki/Cuboid#Rectangular_cuboid
    
    If this is the case, returns what appears to be the base face, and the vector
    used to make that extrusion.
    
    The base face is determined based on the sortmethod parameter, which can either
    be:
    
    "area" = Of the faces with the smallest area, the one with the lowest z coordinate.
    "z" = The face with the lowest z coordinate.
    a 3D vector = the face which center is closest to the given 3D point
    
    Parameters
    ----------
    shape: <Part.Shape>
        Shape to examine.
    sortmethod: {"area", "z"}
        Which sorting algorithm to use to determine the base face.
    
    Returns
    -------
    Extrusion data: list
        Two item list containing the base face, and the vector used to create the
        extrusion. In that order.
    Failure: None
        Returns None if the object does not appear to be an extrusion.
    

Referenced by
[ArchComponent.Component.getExtrusionData()](../../de/d87/classArchComponent_1_1Component.html#abe6b1db0166c4b8edb14db2440ab4919).

## ◆ getHost()

def ArchCommands.getHost  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _strict_ = `True`  
| ) | |   
      
    
    getHost(obj,[strict]): returns the host of the current object. If strict is true (default),
    the host can only be an object of a higher level than the given one, or in other words, if a wall
    is contained in another wall which is part of a floor, the floor is returned instead of the parent wall

References
[getHost()](../../d4/d52/namespaceArchCommands.html#a0f3cb7055a7b61252475246478e1430d).

Referenced by
[getHost()](../../d4/d52/namespaceArchCommands.html#a0f3cb7055a7b61252475246478e1430d).

## ◆ getShapeFromMesh()

def ArchCommands.getShapeFromMesh  | ( |  | _mesh_ ,   
---|---|---|---  
|  |  | _fast_ = `True`,   
|  |  | _tolerance_ = `0.001`,   
|  |  | _flat_ = `False`,   
|  |  | _cut_ = `True`  
| ) | |   
  
References
[makeFace()](../../d4/d52/namespaceArchCommands.html#a98c94780af071056a7971a4ba882832e).

Referenced by
[ArchPanel.CommandPanelSheet.Activated()](../../d1/d94/classArchPanel_1_1CommandPanelSheet.html#abed1cd5ce53c5b156683ae24b81f75e4),
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[ArchWall.areSameWallTypes()](../../d2/d8e/namespaceArchWall.html#a289f6e980eba7dd10b74dcfb84dd0c92),
[meshToShape()](../../d4/d52/namespaceArchCommands.html#a212eee2155be7c16f8a4817ca33d1057),
and
[removeCurves()](../../d4/d52/namespaceArchCommands.html#ab1a7fc05792ac9dfa9a7f861338ec713).

## ◆ getStringList()

def ArchCommands.getStringList  | ( |  | _objects_| ) |   
---|---|---|---|---|---  
      
    
    getStringList(objects): returns a string defining a list
    of objects

Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c).

## ◆ makeComponent()

def ArchCommands.makeComponent  | ( |  | _baseobj_ = `None`,   
---|---|---|---  
|  |  | _name_ = `"Component"`,   
|  |  | _delete_ = `False`  
| ) | |   
      
    
    makeComponent([baseobj]): creates an undefined, non-parametric Arch
    component from the given base object

Referenced by
[cloneComponent()](../../d4/d52/namespaceArchCommands.html#a43c20fa7529b3f7afc858e65966d268e).

## ◆ makeCompoundFromSelected()

def ArchCommands.makeCompoundFromSelected  | ( |  | _objects_ = `None`| ) |   
---|---|---|---|---|---  
      
    
    makeCompoundFromSelected([objects]): Creates a new compound object from the given
    subobjects (faces, edges) or from the selection if objects is None

## ◆ makeFace()

def ArchCommands.makeFace  | ( |  | _wires_ ,   
---|---|---|---  
|  |  | _method_ = `2`,   
|  |  | _cleanup_ = `False`  
| ) | |   
      
    
    makeFace(wires): makes a face from a list of wires, finding which ones are holes

Referenced by
[ArchPanel.CommandPanelSheet.Activated()](../../d1/d94/classArchPanel_1_1CommandPanelSheet.html#abed1cd5ce53c5b156683ae24b81f75e4),
[getShapeFromMesh()](../../d4/d52/namespaceArchCommands.html#a37db9c820a988faeb31d27d7dbb00dbe),
and
[ArchVRM.Renderer.projectFace()](../../d5/dfd/classArchVRM_1_1Renderer.html#a2476b5baba8beebf01fcfddcbe1b7ede).

## ◆ makeIfcSpreadsheet()

def ArchCommands.makeIfcSpreadsheet  | ( |  | _archobj_ = `None`| ) |   
---|---|---|---|---|---  
  
## ◆ mergeCells()

def ArchCommands.mergeCells  | ( |  | _objectslist_| ) |   
---|---|---|---|---|---  
      
    
    mergeCells(objectslist): merges the objects in the given list
    into one. All objects must be of the same type and based on the Cell
    object (cells, floors, buildings, or sites).

Referenced by
[printWarning()](../../d4/d52/namespaceArchCommands.html#aa246a606bc319851e58c55f66d7693e6).

## ◆ meshToShape()

def ArchCommands.meshToShape  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _mark_ = `True`,   
|  |  | _fast_ = `True`,   
|  |  | _tol_ = `0.001`,   
|  |  | _flat_ = `False`,   
|  |  | _cut_ = `True`  
| ) | |   
      
    
    meshToShape(object,[mark,fast,tol,flat,cut]): turns a mesh into a shape, joining coplanar facets. If
    mark is True (default), non-solid objects will be marked in red. Fast uses a faster algorithm by
    building a shell from the facets then removing splitter, tol is the tolerance used when converting
    mesh segments to wires, flat will force the wires to be perfectly planar, to be sure they can be
    turned into faces, but this might leave gaps in the final shell. If cut is true, holes in faces are
    made by subtraction (default)

References
[getShapeFromMesh()](../../d4/d52/namespaceArchCommands.html#a37db9c820a988faeb31d27d7dbb00dbe).

Referenced by
[printWarning()](../../d4/d52/namespaceArchCommands.html#aa246a606bc319851e58c55f66d7693e6).

## ◆ printMessage()

def ArchCommands.printMessage  | ( |  | _message_| ) |   
---|---|---|---|---|---  
  
Referenced by
[ArchSite.Compass.buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[ArchBuilding.makeBuilding()](../../d8/def/namespaceArchBuilding.html#a9ff5afad344ac96642ffeef4ce271afe),
and
[ArchFloor.makeFloor()](../../df/d16/namespaceArchFloor.html#a6c27d8dc5a92ad8079677e720e783191).

## ◆ printWarning()

def ArchCommands.printWarning  | ( |  | _message_| ) |   
---|---|---|---|---|---  
  
References
[check()](../../d4/d52/namespaceArchCommands.html#a711cf551f0bed73105abcd328ec2e527),
[closeHole()](../../d4/d52/namespaceArchCommands.html#aa465eac40edecce3e75c8fa38576a80a),
[mergeCells()](../../d4/d52/namespaceArchCommands.html#ac37be91f5b34674f97c6dc9c7889c54d),
[meshToShape()](../../d4/d52/namespaceArchCommands.html#a212eee2155be7c16f8a4817ca33d1057),
[removeShape()](../../d4/d52/namespaceArchCommands.html#af251273d7e60f828f0cafd22e4a881b1),
[splitMesh()](../../d4/d52/namespaceArchCommands.html#a3e09c50fc5b3a4a23b00cc702097d119),
[toggleIfcBrepFlag()](../../d4/d52/namespaceArchCommands.html#afef50dee48c82402a2215afb55cd95f1),
and
[draftutils.utils.utf8_decode()](../../de/d75/group__draftutils.html#ga65481f0e89b6495a5ea0c7a428fc7cb7).

## ◆ projectToVector()

def ArchCommands.projectToVector  | ( |  | _shape_ ,   
---|---|---|---  
|  |  | _vector_  
| ) | |   
      
    
    projectToVector(shape,vector): projects the given shape on the given
    vector

References
[DraftVecUtils.project()](../../dc/dc3/group__DRAFTVECUTILS.html#ga1bf889753387ffb78fb07cb90abed8bc),
and
[DraftVecUtils.scaleTo()](../../dc/dc3/group__DRAFTVECUTILS.html#ga6b1b9879299d28cb689cbee684e9d5f3).

Referenced by
[ArchRebar.makeRebar()](../../dd/de9/namespaceArchRebar.html#a4f9bf27bce35bf45fc8f02cfd5a8078d).

## ◆ pruneIncluded()

def ArchCommands.pruneIncluded  | ( |  | _objectslist_ ,   
---|---|---|---  
|  |  | _strict_ = `False`  
| ) | |   
      
    
    pruneIncluded(objectslist,[strict]): removes from a list of Arch objects, those that are subcomponents of
    another shape-based object, leaving only the top-level shapes. If strict is True, the object
    is removed only if the parent is also part of the selection.

## ◆ rebuildArchShape()

def ArchCommands.rebuildArchShape  | ( |  | _objects_ = `None`| ) |   
---|---|---|---|---|---  
      
    
    rebuildArchShape([objects]): takes the faces from the base shape of the given (or selected
    if objects is None) Arch objects, and tries to rebuild a valid solid from them.

## ◆ removeComponents()

def ArchCommands.removeComponents  | ( |  | _objectsList_ ,   
---|---|---|---  
|  |  | _host_ = `None`  
| ) | |   
      
    
    removeComponents(objectsList,[hostObject]): removes the given component or
    the components from the given list from their parents. If a host object is
    specified, this function will try adding the components as holes to the host
    object instead.

References
[setAsSubcomponent()](../../d4/d52/namespaceArchCommands.html#ab6ea06dd24271c406f4e1f9a9e555c6a).

Referenced by
[ArchCutPlane.cutComponentwithPlane()](../../d5/da7/namespaceArchCutPlane.html#aa1ff7471ad5f704a5ff1c96224450a23),
and
[importIFClegacy.read()](../../db/d15/namespaceimportIFClegacy.html#a8d7878f0b7576afcda6b95e88c5776e4).

## ◆ removeCurves()

def ArchCommands.removeCurves  | ( |  | _shape_ ,   
---|---|---|---  
|  |  | _dae_ = `False`,   
|  |  | _tolerance_ = `5`  
| ) | |   
      
    
    removeCurves(shape,dae,tolerance=5): replaces curved faces in a shape
    with faceted segments. If dae is True, DAE triangulation options are used

References
[getShapeFromMesh()](../../d4/d52/namespaceArchCommands.html#a37db9c820a988faeb31d27d7dbb00dbe),
and
[importDAE.triangulate()](../../dd/d88/namespaceimportDAE.html#a6c4020daa4b3b4e9233e377e30c136ed).

## ◆ removeShape()

def ArchCommands.removeShape  | ( |  | _objs_ ,   
---|---|---|---  
|  |  | _mark_ = `True`  
| ) | |   
      
    
    removeShape(objs,mark=True): takes an arch object (wall or structure) built on a cubic shape, and removes
    the inner shape, keeping its length, width and height as parameters. If mark is True, objects that cannot
    be processed by this function will become red.

References
[ArchStructure.makeStructure()](../../d3/d32/namespaceArchStructure.html#ac13ef58c486502672b4ccfe9f359b529),
and
[ArchWall.makeWall()](../../d2/d8e/namespaceArchWall.html#aefaababeff5a24ab8c28585efb0406c6).

Referenced by
[printWarning()](../../d4/d52/namespaceArchCommands.html#aa246a606bc319851e58c55f66d7693e6).

## ◆ setAsSubcomponent()

def ArchCommands.setAsSubcomponent  | ( |  | _obj_| ) |   
---|---|---|---|---|---  
      
    
    Sets the given object properly to become a subcomponent (addition, subtraction)
    of an Arch component

References
[getDefaultColor()](../../d4/d52/namespaceArchCommands.html#abfe83988dd63577babc96771bb3212a0).

Referenced by
[removeComponents()](../../d4/d52/namespaceArchCommands.html#a42827993f20cf7bca87c7a9d1fbbaaac),
and
[ArchComponent.removeFromComponent()](../../da/d62/namespaceArchComponent.html#a17514796122b97b14647e550056e419a).

## ◆ splitMesh()

def ArchCommands.splitMesh  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _mark_ = `True`  
| ) | |   
      
    
    splitMesh(object,[mark]): splits the given mesh object into separated components.
    If mark is False, nothing else is done. If True (default), non-manifold components
    will be painted in red.

Referenced by
[printWarning()](../../d4/d52/namespaceArchCommands.html#aa246a606bc319851e58c55f66d7693e6).

## ◆ string_replace()

def ArchCommands.string_replace  | ( |  | _text_ ,   
---|---|---|---  
|  |  | _pattern_ ,   
|  |  | _replacement_  
| ) | |   
      
    
    if py2 isn't supported anymore calls to this function
    should be replaced with:
    `text.replace(pattern, replacement)`
    for python2 the encoding must be done, as unicode replacement leads to something like this:
    ```
    >>> a = u'abc mm ^3'
    >>> a.replace(u"^3", u"³")
    u'abc mm \xc2\xb3'
    ```
    

Referenced by
[ArchCommands.SurveyTaskPanel.clipArea()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a1b8288364a10a547a60fd6f31f1a905b),
and
[survey()](../../d4/d52/namespaceArchCommands.html#a2a97d8ae69e51460196b4d3e0d6859f1).

## ◆ survey()

def ArchCommands.survey  | ( |  | _callback_ = `False`| ) |   
---|---|---|---|---|---  
      
    
    survey(): starts survey mode, where you can click edges and faces to get their lengths or area.
    Clicking on no object (on an empty area) resets the count.

References
[string_replace()](../../d4/d52/namespaceArchCommands.html#af256192f97a16dc89632e0e9fd0c804b),
and
[draftutils.utils.utf8_decode()](../../de/d75/group__draftutils.html#ga65481f0e89b6495a5ea0c7a428fc7cb7).

## ◆ toggleIfcBrepFlag()

def ArchCommands.toggleIfcBrepFlag  | ( |  | _obj_| ) |   
---|---|---|---|---|---  
      
    
    toggleIfcBrepFlag(obj): toggles the IFC brep flag of the given object, forcing it
    to be exported as brep geometry or not.

Referenced by
[printWarning()](../../d4/d52/namespaceArchCommands.html#aa246a606bc319851e58c55f66d7693e6).

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

