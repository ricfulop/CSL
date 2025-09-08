---
url: https://freecad.github.io/SourceDoc/d5/dfd/classArchVRM_1_1Renderer.html
scraped_at: 2025-09-08T14:58:41.465335
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ArchVRM](../../df/d1d/namespaceArchVRM.html)
  * [Renderer](../../d5/dfd/classArchVRM_1_1Renderer.html)

[List of all members](../../d7/d00/classArchVRM_1_1Renderer-members.html) | Public Member Functions | Public Attributes

ArchVRM.Renderer Class Reference

##  Public Member Functions  
  
---  
def | [addFaces](../../d5/dfd/classArchVRM_1_1Renderer.html#a5398694c47561828347cdb21b9a8783f) (self, [faces](../../d5/dfd/classArchVRM_1_1Renderer.html#ab052dd41cffa61d6098339313232df71), color=(0.9, 0.9, 0.9, 1.0))  
def | [addLabels](../../d5/dfd/classArchVRM_1_1Renderer.html#a154c8a7fb7273e3ecc7242a6f048f659) (self)  
def | [addObjects](../../d5/dfd/classArchVRM_1_1Renderer.html#ae9d5501f6f159004a5735e337c03ef1e) (self, objs)  
def | [addShapes](../../d5/dfd/classArchVRM_1_1Renderer.html#aec9719059fd4a06e2cd43792827a985c) (self, [shapes](../../d5/dfd/classArchVRM_1_1Renderer.html#aa8cca10507837180c0cfea82a1d67f9e), color=(0.9, 0.9, 0.9, 1.0))  
def | [buildDummy](../../d5/dfd/classArchVRM_1_1Renderer.html#a3aa0cbbf0fed468267430ecc693fa19d) (self)  
def | [compare](../../d5/dfd/classArchVRM_1_1Renderer.html#a78f4e0b92707209bcfeb72db372e044a) (self, face1, face2)  
def | [cut](../../d5/dfd/classArchVRM_1_1Renderer.html#a42a08e8de6110aefc78bdfd483206b10) (self, cutplane, hidden=False)  
def | [findPosition](../../d5/dfd/classArchVRM_1_1Renderer.html#a97f368ace00f62ba6fcd7754d27658b8) (self, f1, [faces](../../d5/dfd/classArchVRM_1_1Renderer.html#ab052dd41cffa61d6098339313232df71))  
def | [flattenFace](../../d5/dfd/classArchVRM_1_1Renderer.html#ac8bb14fcc9629050daa0513fc71e9247) (self, face)  
def | [getFill](../../d5/dfd/classArchVRM_1_1Renderer.html#a5f1d662bdcbb1effe6b34546d6ba5c49) (self, fill)  
def | [getHiddenSVG](../../d5/dfd/classArchVRM_1_1Renderer.html#a260a5d749414eb9baecb3d78587e371c) (self, linewidth=0.02)  
def | [getPathData](../../d5/dfd/classArchVRM_1_1Renderer.html#aa3913ebcc8242d58d7bad0d885cbca09) (self, w)  
def | [getSectionSVG](../../d5/dfd/classArchVRM_1_1Renderer.html#ae6f1fdf02312ca7e2d0ec5788b3aadcd) (self, linewidth=0.02, fillpattern=None)  
def | [getViewSVG](../../d5/dfd/classArchVRM_1_1Renderer.html#a93d12556de6816282a9c7f85c8b0970a) (self, linewidth=0.01)  
def | [info](../../d5/dfd/classArchVRM_1_1Renderer.html#a0beedb32288b016f4a4739b78803562e) (self)  
def | [isInside](../../d5/dfd/classArchVRM_1_1Renderer.html#ae3b9d221eef5caf5fb883fcd5894521d) (self, vert, face)  
def | [isVisible](../../d5/dfd/classArchVRM_1_1Renderer.html#a87a6c89b1891db19398235a1d7142c5f) (self, face)  
def | [join](../../d5/dfd/classArchVRM_1_1Renderer.html#a21a14885523bc7995975c677b7077575) (self, otype)  
def | [projectEdge](../../d5/dfd/classArchVRM_1_1Renderer.html#a0022e29552adab1c6f7f91710c0d1880) (self, edge)  
def | [projectFace](../../d5/dfd/classArchVRM_1_1Renderer.html#a2476b5baba8beebf01fcfddcbe1b7ede) (self, face)  
def | [removeHidden](../../d5/dfd/classArchVRM_1_1Renderer.html#a61819c30358d66516bdad27291128881) (self)  
def | [reorient](../../d5/dfd/classArchVRM_1_1Renderer.html#acfbe4d1ea07b8ae822f94499f6aebce9) (self)  
def | [reset](../../d5/dfd/classArchVRM_1_1Renderer.html#a6e527fa83621dff1499db482f43068aa) (self)  
def | [resetFlags](../../d5/dfd/classArchVRM_1_1Renderer.html#aa5509ca92ea13d23101b7b0913cb67ae) (self)  
def | [setWorkingPlane](../../d5/dfd/classArchVRM_1_1Renderer.html#aa8a752e2d04b66cbe66a500efb36565b) (self, [wp](../../d5/dfd/classArchVRM_1_1Renderer.html#ad8c2f0a1df6d4130ba9fedaab295ba4f))  
def | [sort](../../d5/dfd/classArchVRM_1_1Renderer.html#abd10a8841e997a0eae5ffcf357b306a3) (self)  
def | [zOverlaps](../../d5/dfd/classArchVRM_1_1Renderer.html#a3fc2563f2f8d910e302c5debf4487f51) (self, face1, face2)  
  
##  Public Attributes  
  
---  
|
[faces](../../d5/dfd/classArchVRM_1_1Renderer.html#ab052dd41cffa61d6098339313232df71)  
|
[hiddenEdges](../../d5/dfd/classArchVRM_1_1Renderer.html#a690bfb6e2612b2ed5cd036ebc59a9bd2)  
|
[iscut](../../d5/dfd/classArchVRM_1_1Renderer.html#a86904afdadeae10808183a2a4f23bfb3)  
|
[joined](../../d5/dfd/classArchVRM_1_1Renderer.html#af8214ddbfda12ef694396b64afec6e34)  
|
[objects](../../d5/dfd/classArchVRM_1_1Renderer.html#acb7fcee04d6acbec95828793cc7735fa)  
|
[oriented](../../d5/dfd/classArchVRM_1_1Renderer.html#a85f1b15d38f64a32e82ba6d95ec9d8f6)  
|
[sections](../../d5/dfd/classArchVRM_1_1Renderer.html#a20afa3ae5cb037a7146233dfefece571)  
|
[shapes](../../d5/dfd/classArchVRM_1_1Renderer.html#aa8cca10507837180c0cfea82a1d67f9e)  
|
[sorted](../../d5/dfd/classArchVRM_1_1Renderer.html#acab84a683a9350dbf161eb29fad4198e)  
|
[trimmed](../../d5/dfd/classArchVRM_1_1Renderer.html#ad6af9e05d7f5b200d66767bfc71541be)  
|
[wp](../../d5/dfd/classArchVRM_1_1Renderer.html#ad8c2f0a1df6d4130ba9fedaab295ba4f)  
  
## Member Function Documentation

## ◆ addFaces()

def ArchVRM.Renderer.addFaces  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _faces_ ,   
|  |  | _color_ = `(0.9,0.9,0.9,1.0)`  
| ) | |   
  
References
[ArchVRM.Renderer.faces](../../d5/dfd/classArchVRM_1_1Renderer.html#ab052dd41cffa61d6098339313232df71),
[draftguitools.gui_offset.Offset.faces](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#a9cb4390dbf6279c95d4bda5174608ce6),
and
[ArchVRM.Renderer.resetFlags()](../../d5/dfd/classArchVRM_1_1Renderer.html#aa5509ca92ea13d23101b7b0913cb67ae).

## ◆ addLabels()

def ArchVRM.Renderer.addLabels  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[ArchVRM.Renderer.faces](../../d5/dfd/classArchVRM_1_1Renderer.html#ab052dd41cffa61d6098339313232df71),
and
[draftguitools.gui_offset.Offset.faces](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#a9cb4390dbf6279c95d4bda5174608ce6).

## ◆ addObjects()

def ArchVRM.Renderer.addObjects  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _objs_  
| ) | |   
  
References
[ArchVRM.Renderer.faces](../../d5/dfd/classArchVRM_1_1Renderer.html#ab052dd41cffa61d6098339313232df71),
[draftguitools.gui_offset.Offset.faces](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#a9cb4390dbf6279c95d4bda5174608ce6),
App::MergeDocuments.objects, Gui::MergeDocuments.objects,
[ArchNesting.Nester.objects](../../d0/df4/classArchNesting_1_1Nester.html#a71fb6b461a18039fbefc657cfda2628e),
[ArchVRM.Renderer.objects](../../d5/dfd/classArchVRM_1_1Renderer.html#acb7fcee04d6acbec95828793cc7735fa),
[exportIFCHelper.ContextCreator.objects](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#affe82dba355ac1fcde6142df2dbc88fb),
[importIFCHelper.ProjectImporter.objects](../../d0/d2c/classimportIFCHelper_1_1ProjectImporter.html#ad45d68ab09fc5ee8f99e06cd423d58f8),
[ArchVRM.Renderer.resetFlags()](../../d5/dfd/classArchVRM_1_1Renderer.html#aa5509ca92ea13d23101b7b0913cb67ae),
[PartGui::Ui_Mirroring.shapes](../../d7/d25/classPartGui_1_1Ui__Mirroring.html#a14237f21c9d1b595b129bb6d1152a2ef),
[ArchNesting.Nester.shapes](../../d0/df4/classArchNesting_1_1Nester.html#aed7787ad1f42e7e27147330762081bfb),
[ArchPanel.NestTaskPanel.shapes](../../da/d77/classArchPanel_1_1NestTaskPanel.html#aea539396a62cf1e98ae5e20bf671c070),
[ArchVRM.Renderer.shapes](../../d5/dfd/classArchVRM_1_1Renderer.html#aa8cca10507837180c0cfea82a1d67f9e),
[MeshPartGui::Mesh2ShapeGmsh::Private.shapes](../../db/dff/classMesh2ShapeGmsh_1_1Private.html#aa141e7e29a8bff58da6a9c0d93e1e071),
and
[PathScripts.PathDressupDogbone.ObjectDressup.shapes](../../d5/dfa/classPathScripts_1_1PathDressupDogbone_1_1ObjectDressup.html#a46bb0b891c7ada9669ed3ff732084a80).

## ◆ addShapes()

def ArchVRM.Renderer.addShapes  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _shapes_ ,   
|  |  | _color_ = `(0.9,0.9,0.9,1.0)`  
| ) | |   
  
References
[ArchVRM.Renderer.faces](../../d5/dfd/classArchVRM_1_1Renderer.html#ab052dd41cffa61d6098339313232df71),
[draftguitools.gui_offset.Offset.faces](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#a9cb4390dbf6279c95d4bda5174608ce6),
[ArchVRM.Renderer.resetFlags()](../../d5/dfd/classArchVRM_1_1Renderer.html#aa5509ca92ea13d23101b7b0913cb67ae),
[PartGui::Ui_Mirroring.shapes](../../d7/d25/classPartGui_1_1Ui__Mirroring.html#a14237f21c9d1b595b129bb6d1152a2ef),
[ArchNesting.Nester.shapes](../../d0/df4/classArchNesting_1_1Nester.html#aed7787ad1f42e7e27147330762081bfb),
[ArchPanel.NestTaskPanel.shapes](../../da/d77/classArchPanel_1_1NestTaskPanel.html#aea539396a62cf1e98ae5e20bf671c070),
[ArchVRM.Renderer.shapes](../../d5/dfd/classArchVRM_1_1Renderer.html#aa8cca10507837180c0cfea82a1d67f9e),
[MeshPartGui::Mesh2ShapeGmsh::Private.shapes](../../db/dff/classMesh2ShapeGmsh_1_1Private.html#aa141e7e29a8bff58da6a9c0d93e1e071),
and
[PathScripts.PathDressupDogbone.ObjectDressup.shapes](../../d5/dfa/classPathScripts_1_1PathDressupDogbone_1_1ObjectDressup.html#a46bb0b891c7ada9669ed3ff732084a80).

## ◆ buildDummy()

def ArchVRM.Renderer.buildDummy  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[ArchVRM.Renderer.faces](../../d5/dfd/classArchVRM_1_1Renderer.html#ab052dd41cffa61d6098339313232df71),
[draftguitools.gui_offset.Offset.faces](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#a9cb4390dbf6279c95d4bda5174608ce6),
[ArchVRM.Renderer.flattenFace()](../../d5/dfd/classArchVRM_1_1Renderer.html#ac8bb14fcc9629050daa0513fc71e9247),
Py::List.sort(),
[ArchVRM.Renderer.sort()](../../d5/dfd/classArchVRM_1_1Renderer.html#abd10a8841e997a0eae5ffcf357b306a3),
[ifc4.ifcclassificationreference.sort](../../db/d62/classifc4_1_1ifcclassificationreference.html#aef08296abd43d4ed2a7926fac1335377),
and
[ArchVRM.Renderer.sorted](../../d5/dfd/classArchVRM_1_1Renderer.html#acab84a683a9350dbf161eb29fad4198e).

## ◆ compare()

def ArchVRM.Renderer.compare  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _face1_ ,   
|  |  | _face2_  
| ) | |   
  
References
[DraftVecUtils.isNull()](../../dc/dc3/group__DRAFTVECUTILS.html#gaaccdee2ed1226b010ac7b3e04c42a687),
[DraftVecUtils.project()](../../dc/dc3/group__DRAFTVECUTILS.html#ga1bf889753387ffb78fb07cb90abed8bc),
and
[ArchVRM.Renderer.zOverlaps()](../../d5/dfd/classArchVRM_1_1Renderer.html#a3fc2563f2f8d910e302c5debf4487f51).

Referenced by
[ArchVRM.Renderer.findPosition()](../../d5/dfd/classArchVRM_1_1Renderer.html#a97f368ace00f62ba6fcd7754d27658b8),
and
[ArchVRM.Renderer.sort()](../../d5/dfd/classArchVRM_1_1Renderer.html#abd10a8841e997a0eae5ffcf357b306a3).

## ◆ cut()

def ArchVRM.Renderer.cut  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _cutplane_ ,   
|  |  | _hidden_ = `False`  
| ) | |   
  
References
[ArchVRM.Renderer.faces](../../d5/dfd/classArchVRM_1_1Renderer.html#ab052dd41cffa61d6098339313232df71),
[draftguitools.gui_offset.Offset.faces](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#a9cb4390dbf6279c95d4bda5174608ce6),
[ArchCommands.getCutVolume()](../../d4/d52/namespaceArchCommands.html#aa9bddbee3691ffd7b3cba2f35e55ce77),
[ArchVRM.Renderer.hiddenEdges](../../d5/dfd/classArchVRM_1_1Renderer.html#a690bfb6e2612b2ed5cd036ebc59a9bd2),
[ArchVRM.Renderer.iscut](../../d5/dfd/classArchVRM_1_1Renderer.html#a86904afdadeae10808183a2a4f23bfb3),
[ArchVRM.Renderer.joined](../../d5/dfd/classArchVRM_1_1Renderer.html#af8214ddbfda12ef694396b64afec6e34),
[ArchVRM.Renderer.oriented](../../d5/dfd/classArchVRM_1_1Renderer.html#a85f1b15d38f64a32e82ba6d95ec9d8f6),
[ArchVRM.Renderer.sections](../../d5/dfd/classArchVRM_1_1Renderer.html#a20afa3ae5cb037a7146233dfefece571),
[femsolver.elmer.sifio.Sif.sections](../../d5/dce/classfemsolver_1_1elmer_1_1sifio_1_1Sif.html#ab0b6be5bc8fa2c689aa135d091bbe654),
[PartGui::Ui_Mirroring.shapes](../../d7/d25/classPartGui_1_1Ui__Mirroring.html#a14237f21c9d1b595b129bb6d1152a2ef),
[ArchNesting.Nester.shapes](../../d0/df4/classArchNesting_1_1Nester.html#aed7787ad1f42e7e27147330762081bfb),
[ArchPanel.NestTaskPanel.shapes](../../da/d77/classArchPanel_1_1NestTaskPanel.html#aea539396a62cf1e98ae5e20bf671c070),
[ArchVRM.Renderer.shapes](../../d5/dfd/classArchVRM_1_1Renderer.html#aa8cca10507837180c0cfea82a1d67f9e),
[MeshPartGui::Mesh2ShapeGmsh::Private.shapes](../../db/dff/classMesh2ShapeGmsh_1_1Private.html#aa141e7e29a8bff58da6a9c0d93e1e071),
[PathScripts.PathDressupDogbone.ObjectDressup.shapes](../../d5/dfa/classPathScripts_1_1PathDressupDogbone_1_1ObjectDressup.html#a46bb0b891c7ada9669ed3ff732084a80),
[ArchVRM.Renderer.sorted](../../d5/dfd/classArchVRM_1_1Renderer.html#acab84a683a9350dbf161eb29fad4198e),
and
[ArchVRM.Renderer.trimmed](../../d5/dfd/classArchVRM_1_1Renderer.html#ad6af9e05d7f5b200d66767bfc71541be).

## ◆ findPosition()

def ArchVRM.Renderer.findPosition  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _f1_ ,   
|  |  | _faces_  
| ) | |   
  
References Py::PythonExtensionBase.compare(),
[ArchVRM.Renderer.compare()](../../d5/dfd/classArchVRM_1_1Renderer.html#a78f4e0b92707209bcfeb72db372e044a),
[ArchVRM.Renderer.faces](../../d5/dfd/classArchVRM_1_1Renderer.html#ab052dd41cffa61d6098339313232df71),
and
[draftguitools.gui_offset.Offset.faces](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#a9cb4390dbf6279c95d4bda5174608ce6).

Referenced by
[ArchVRM.Renderer.sort()](../../d5/dfd/classArchVRM_1_1Renderer.html#abd10a8841e997a0eae5ffcf357b306a3).

## ◆ flattenFace()

def ArchVRM.Renderer.flattenFace  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _face_  
| ) | |   
  
Referenced by
[ArchVRM.Renderer.buildDummy()](../../d5/dfd/classArchVRM_1_1Renderer.html#a3aa0cbbf0fed468267430ecc693fa19d),
and
[ArchVRM.Renderer.zOverlaps()](../../d5/dfd/classArchVRM_1_1Renderer.html#a3fc2563f2f8d910e302c5debf4487f51).

## ◆ getFill()

def ArchVRM.Renderer.getFill  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _fill_  
| ) | |   
  
Referenced by
[ArchVRM.Renderer.getViewSVG()](../../d5/dfd/classArchVRM_1_1Renderer.html#a93d12556de6816282a9c7f85c8b0970a),
and
[ArchVRM.Renderer.info()](../../d5/dfd/classArchVRM_1_1Renderer.html#a0beedb32288b016f4a4739b78803562e).

## ◆ getHiddenSVG()

def ArchVRM.Renderer.getHiddenSVG  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _linewidth_ = `0.02`  
| ) | |   
  
References
[ArchVRM.Renderer.getPathData()](../../d5/dfd/classArchVRM_1_1Renderer.html#aa3913ebcc8242d58d7bad0d885cbca09),
[ArchVRM.Renderer.hiddenEdges](../../d5/dfd/classArchVRM_1_1Renderer.html#a690bfb6e2612b2ed5cd036ebc59a9bd2),
[ArchVRM.Renderer.oriented](../../d5/dfd/classArchVRM_1_1Renderer.html#a85f1b15d38f64a32e82ba6d95ec9d8f6),
[ArchVRM.Renderer.reorient()](../../d5/dfd/classArchVRM_1_1Renderer.html#acfbe4d1ea07b8ae822f94499f6aebce9),
[ArchVRM.Renderer.sections](../../d5/dfd/classArchVRM_1_1Renderer.html#a20afa3ae5cb037a7146233dfefece571),
and
[femsolver.elmer.sifio.Sif.sections](../../d5/dce/classfemsolver_1_1elmer_1_1sifio_1_1Sif.html#ab0b6be5bc8fa2c689aa135d091bbe654).

## ◆ getPathData()

def ArchVRM.Renderer.getPathData  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _w_  
| ) | |   
  
References
[DraftVecUtils.precision()](../../dc/dc3/group__DRAFTVECUTILS.html#ga1dde8544b2fa3998691eb2adb39a100d).

Referenced by
[ArchVRM.Renderer.getHiddenSVG()](../../d5/dfd/classArchVRM_1_1Renderer.html#a260a5d749414eb9baecb3d78587e371c),
[ArchVRM.Renderer.getSectionSVG()](../../d5/dfd/classArchVRM_1_1Renderer.html#ae6f1fdf02312ca7e2d0ec5788b3aadcd),
and
[ArchVRM.Renderer.getViewSVG()](../../d5/dfd/classArchVRM_1_1Renderer.html#a93d12556de6816282a9c7f85c8b0970a).

## ◆ getSectionSVG()

def ArchVRM.Renderer.getSectionSVG  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _linewidth_ = `0.02`,   
|  |  | _fillpattern_ = `None`  
| ) | |   
  
References
[ArchVRM.Renderer.getPathData()](../../d5/dfd/classArchVRM_1_1Renderer.html#aa3913ebcc8242d58d7bad0d885cbca09),
[ArchVRM.Renderer.oriented](../../d5/dfd/classArchVRM_1_1Renderer.html#a85f1b15d38f64a32e82ba6d95ec9d8f6),
[ArchVRM.Renderer.reorient()](../../d5/dfd/classArchVRM_1_1Renderer.html#acfbe4d1ea07b8ae822f94499f6aebce9),
[ArchVRM.Renderer.sections](../../d5/dfd/classArchVRM_1_1Renderer.html#a20afa3ae5cb037a7146233dfefece571),
and
[femsolver.elmer.sifio.Sif.sections](../../d5/dce/classfemsolver_1_1elmer_1_1sifio_1_1Sif.html#ab0b6be5bc8fa2c689aa135d091bbe654).

## ◆ getViewSVG()

def ArchVRM.Renderer.getViewSVG  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _linewidth_ = `0.01`  
| ) | |   
  
References
[ArchVRM.Renderer.faces](../../d5/dfd/classArchVRM_1_1Renderer.html#ab052dd41cffa61d6098339313232df71),
[draftguitools.gui_offset.Offset.faces](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#a9cb4390dbf6279c95d4bda5174608ce6),
[ArchVRM.Renderer.getFill()](../../d5/dfd/classArchVRM_1_1Renderer.html#a5f1d662bdcbb1effe6b34546d6ba5c49),
[ArchVRM.Renderer.getPathData()](../../d5/dfd/classArchVRM_1_1Renderer.html#aa3913ebcc8242d58d7bad0d885cbca09),
Py::List.sort(),
[ArchVRM.Renderer.sort()](../../d5/dfd/classArchVRM_1_1Renderer.html#abd10a8841e997a0eae5ffcf357b306a3),
[ifc4.ifcclassificationreference.sort](../../db/d62/classifc4_1_1ifcclassificationreference.html#aef08296abd43d4ed2a7926fac1335377),
and
[ArchVRM.Renderer.sorted](../../d5/dfd/classArchVRM_1_1Renderer.html#acab84a683a9350dbf161eb29fad4198e).

## ◆ info()

def ArchVRM.Renderer.info  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[ArchVRM.Renderer.faces](../../d5/dfd/classArchVRM_1_1Renderer.html#ab052dd41cffa61d6098339313232df71),
[draftguitools.gui_offset.Offset.faces](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#a9cb4390dbf6279c95d4bda5174608ce6),
[ArchVRM.Renderer.getFill()](../../d5/dfd/classArchVRM_1_1Renderer.html#a5f1d662bdcbb1effe6b34546d6ba5c49),
[ArchVRM.Renderer.oriented](../../d5/dfd/classArchVRM_1_1Renderer.html#a85f1b15d38f64a32e82ba6d95ec9d8f6),
[ArchVRM.Renderer.sorted](../../d5/dfd/classArchVRM_1_1Renderer.html#acab84a683a9350dbf161eb29fad4198e),
and
[ArchVRM.Renderer.trimmed](../../d5/dfd/classArchVRM_1_1Renderer.html#ad6af9e05d7f5b200d66767bfc71541be).

Referenced by
[draftguitools.gui_dimensions.Dimension.action()](../../d5/d6a/classdraftguitools_1_1gui__dimensions_1_1Dimension.html#a96494d2774d1c1c9b0973c27fa7e37d2),
[PathScripts.PathProperty.Property.setupProperty()](../../d3/ddd/classPathScripts_1_1PathProperty_1_1Property.html#a5a5e131e96ff2fe47560b350c5936e2e),
and
[PathScripts.PathSetupSheetOpPrototype.Property.setupProperty()](../../d2/d60/classPathScripts_1_1PathSetupSheetOpPrototype_1_1Property.html#a113176886a5350831cd5a943afb10b2e).

## ◆ isInside()

def ArchVRM.Renderer.isInside  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _vert_ ,   
|  |  | _face_  
| ) | |   
  
References
[ArchVRM.Renderer.wp](../../d5/dfd/classArchVRM_1_1Renderer.html#ad8c2f0a1df6d4130ba9fedaab295ba4f).

Referenced by
[ArchVRM.Renderer.zOverlaps()](../../d5/dfd/classArchVRM_1_1Renderer.html#a3fc2563f2f8d910e302c5debf4487f51).

## ◆ isVisible()

def ArchVRM.Renderer.isVisible  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _face_  
| ) | |   
  
References
[ArchVRM.Renderer.wp](../../d5/dfd/classArchVRM_1_1Renderer.html#ad8c2f0a1df6d4130ba9fedaab295ba4f).

Referenced by
[ArchVRM.Renderer.removeHidden()](../../d5/dfd/classArchVRM_1_1Renderer.html#a61819c30358d66516bdad27291128881).

## ◆ join()

def ArchVRM.Renderer.join  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _otype_  
| ) | |   
  
Referenced by
[draftobjects.clone.Clone.execute()](../../df/d9d/classdraftobjects_1_1clone_1_1Clone.html#a989a485bf24e2e5e5faa1d70fc906646).

## ◆ projectEdge()

def ArchVRM.Renderer.projectEdge  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _edge_  
| ) | |   
  
References
[ArchVRM.Renderer.wp](../../d5/dfd/classArchVRM_1_1Renderer.html#ad8c2f0a1df6d4130ba9fedaab295ba4f).

Referenced by
[ArchVRM.Renderer.reorient()](../../d5/dfd/classArchVRM_1_1Renderer.html#acfbe4d1ea07b8ae822f94499f6aebce9).

## ◆ projectFace()

def ArchVRM.Renderer.projectFace  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _face_  
| ) | |   
  
References
[ArchCommands.makeFace()](../../d4/d52/namespaceArchCommands.html#a98c94780af071056a7971a4ba882832e),
and
[ArchVRM.Renderer.wp](../../d5/dfd/classArchVRM_1_1Renderer.html#ad8c2f0a1df6d4130ba9fedaab295ba4f).

Referenced by
[ArchVRM.Renderer.reorient()](../../d5/dfd/classArchVRM_1_1Renderer.html#acfbe4d1ea07b8ae822f94499f6aebce9).

## ◆ removeHidden()

def ArchVRM.Renderer.removeHidden  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[ArchVRM.Renderer.faces](../../d5/dfd/classArchVRM_1_1Renderer.html#ab052dd41cffa61d6098339313232df71),
[draftguitools.gui_offset.Offset.faces](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#a9cb4390dbf6279c95d4bda5174608ce6),
SketcherGui::EditModeInformationOverlayCoinConverter.isVisible(),
[Gui::SoBoxSelectionRenderAction.isVisible()](../../d2/d08/classGui_1_1SoBoxSelectionRenderAction.html#a4788f4a833642076cd4fc31894996253),
[Gui::ViewProvider.isVisible()](../../d3/db3/classGui_1_1ViewProvider.html#a3df346ae0a318f1abe550f869e3c058b),
[Gui::LinkInfo.isVisible()](../../d4/da4/classGui_1_1LinkInfo.html#a27debfdfa1eb441c621fd5d77d206e65),
[TechDrawGui::QGIView.isVisible()](../../d1/d99/classTechDrawGui_1_1QGIView.html#a6fea8197de9d4bc71a04aa2bd1880c48),
[Gui::PreferencePackManager.isVisible()](../../d9/d11/classGui_1_1PreferencePackManager.html#a376d5716cb006d990ab52034998d2a56),
[Gui::SoFCColorBar.isVisible()](../../d0/dc7/classGui_1_1SoFCColorBar.html#a839044389befed45fafe5dd5a160f5f7),
[Gui::SoFCColorGradient.isVisible()](../../d0/de7/classGui_1_1SoFCColorGradient.html#a884bf4343ccfcaf957879cc3b96e5e35),
[Gui::SoFCColorBarBase.isVisible()](../../db/d6a/classGui_1_1SoFCColorBarBase.html#a8f4428f1c2ab435a7d412ae30618fa9c),
[Gui::SoFCColorLegend.isVisible()](../../dd/dd5/classGui_1_1SoFCColorLegend.html#a9f776db0196715da9d594385dc1b3124),
[DocumentObject.ViewProvider.isVisible()](../../d8/dd7/classDocumentObject_1_1ViewProvider.html#a8f25d53bb792b603a013f9b49cad0e44),
[ArchVRM.Renderer.isVisible()](../../d5/dfd/classArchVRM_1_1Renderer.html#a87a6c89b1891db19398235a1d7142c5f),
and
[ArchVRM.Renderer.trimmed](../../d5/dfd/classArchVRM_1_1Renderer.html#ad6af9e05d7f5b200d66767bfc71541be).

Referenced by
[ArchVRM.Renderer.sort()](../../d5/dfd/classArchVRM_1_1Renderer.html#abd10a8841e997a0eae5ffcf357b306a3).

## ◆ reorient()

def ArchVRM.Renderer.reorient  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[ArchVRM.Renderer.faces](../../d5/dfd/classArchVRM_1_1Renderer.html#ab052dd41cffa61d6098339313232df71),
[draftguitools.gui_offset.Offset.faces](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#a9cb4390dbf6279c95d4bda5174608ce6),
[ArchVRM.Renderer.hiddenEdges](../../d5/dfd/classArchVRM_1_1Renderer.html#a690bfb6e2612b2ed5cd036ebc59a9bd2),
[ArchVRM.Renderer.oriented](../../d5/dfd/classArchVRM_1_1Renderer.html#a85f1b15d38f64a32e82ba6d95ec9d8f6),
[TechDraw::DrawViewPart.projectEdge()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#ac9a4b6e79ebdc71df945792bc01b0f32),
[ArchVRM.Renderer.projectEdge()](../../d5/dfd/classArchVRM_1_1Renderer.html#a0022e29552adab1c6f7f91710c0d1880),
[TechDraw::GeometryObject.projectFace()](../../dc/dbe/classTechDraw_1_1GeometryObject.html#aa7288dd3cff425824b8176f882d28990),
[ArchVRM.Renderer.projectFace()](../../d5/dfd/classArchVRM_1_1Renderer.html#a2476b5baba8beebf01fcfddcbe1b7ede),
[ArchVRM.Renderer.sections](../../d5/dfd/classArchVRM_1_1Renderer.html#a20afa3ae5cb037a7146233dfefece571),
and
[femsolver.elmer.sifio.Sif.sections](../../d5/dce/classfemsolver_1_1elmer_1_1sifio_1_1Sif.html#ab0b6be5bc8fa2c689aa135d091bbe654).

Referenced by
[ArchVRM.Renderer.getHiddenSVG()](../../d5/dfd/classArchVRM_1_1Renderer.html#a260a5d749414eb9baecb3d78587e371c),
[ArchVRM.Renderer.getSectionSVG()](../../d5/dfd/classArchVRM_1_1Renderer.html#ae6f1fdf02312ca7e2d0ec5788b3aadcd),
and
[ArchVRM.Renderer.sort()](../../d5/dfd/classArchVRM_1_1Renderer.html#abd10a8841e997a0eae5ffcf357b306a3).

## ◆ reset()

def ArchVRM.Renderer.reset  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Referenced by
[draftguitools.gui_trackers.gridTracker.set()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#a1499cdcfd43fe110d46cd9c72c52b356).

## ◆ resetFlags()

def ArchVRM.Renderer.resetFlags  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Referenced by
[ArchVRM.Renderer.addFaces()](../../d5/dfd/classArchVRM_1_1Renderer.html#a5398694c47561828347cdb21b9a8783f),
[ArchVRM.Renderer.addObjects()](../../d5/dfd/classArchVRM_1_1Renderer.html#ae9d5501f6f159004a5735e337c03ef1e),
and
[ArchVRM.Renderer.addShapes()](../../d5/dfd/classArchVRM_1_1Renderer.html#aec9719059fd4a06e2cd43792827a985c).

## ◆ setWorkingPlane()

def ArchVRM.Renderer.setWorkingPlane  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _wp_  
| ) | |   
  
References
[ArchVRM.Renderer.wp](../../d5/dfd/classArchVRM_1_1Renderer.html#ad8c2f0a1df6d4130ba9fedaab295ba4f).

Referenced by
[ArchBuildingPart.ViewProviderBuildingPart.activate()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a3d54c550a81d6a8e3ed69e264eea1e9f),
and
[ArchBuildingPart.ViewProviderBuildingPart.setupContextMenu()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#af4a9ef0aacacccf376553d8aa6f85bcf).

## ◆ sort()

def ArchVRM.Renderer.sort  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References Py::PythonExtensionBase.compare(),
[ArchVRM.Renderer.compare()](../../d5/dfd/classArchVRM_1_1Renderer.html#a78f4e0b92707209bcfeb72db372e044a),
[ArchVRM.Renderer.faces](../../d5/dfd/classArchVRM_1_1Renderer.html#ab052dd41cffa61d6098339313232df71),
[draftguitools.gui_offset.Offset.faces](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#a9cb4390dbf6279c95d4bda5174608ce6),
[ArchVRM.Renderer.findPosition()](../../d5/dfd/classArchVRM_1_1Renderer.html#a97f368ace00f62ba6fcd7754d27658b8),
[ArchVRM.Renderer.oriented](../../d5/dfd/classArchVRM_1_1Renderer.html#a85f1b15d38f64a32e82ba6d95ec9d8f6),
[ArchVRM.Renderer.removeHidden()](../../d5/dfd/classArchVRM_1_1Renderer.html#a61819c30358d66516bdad27291128881),
[ArchVRM.Renderer.reorient()](../../d5/dfd/classArchVRM_1_1Renderer.html#acfbe4d1ea07b8ae822f94499f6aebce9),
[ArchVRM.Renderer.sorted](../../d5/dfd/classArchVRM_1_1Renderer.html#acab84a683a9350dbf161eb29fad4198e),
and
[ArchVRM.Renderer.trimmed](../../d5/dfd/classArchVRM_1_1Renderer.html#ad6af9e05d7f5b200d66767bfc71541be).

Referenced by
[ArchVRM.Renderer.buildDummy()](../../d5/dfd/classArchVRM_1_1Renderer.html#a3aa0cbbf0fed468267430ecc693fa19d),
and
[ArchVRM.Renderer.getViewSVG()](../../d5/dfd/classArchVRM_1_1Renderer.html#a93d12556de6816282a9c7f85c8b0970a).

## ◆ zOverlaps()

def ArchVRM.Renderer.zOverlaps  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _face1_ ,   
|  |  | _face2_  
| ) | |   
  
References
[ArchVRM.Renderer.flattenFace()](../../d5/dfd/classArchVRM_1_1Renderer.html#ac8bb14fcc9629050daa0513fc71e9247),
[SMESH_OctreeNode.isInside()](../../dd/d88/classSMESH__OctreeNode.html#a3e4bcb5c1bcfd4b2ce8899addd7062bb),
[cSimTool.isInside()](../../d3/d31/classcSimTool.html#ad2e9adbe06388f51b1ba05025d6021a3),
[Part::FaceMakerCheese.isInside()](../../d0/d37/classPart_1_1FaceMakerCheese.html#a445164d40df7124477122cc54f7e3daa),
[draftguitools.gui_trackers.rectangleTracker.isInside()](../../d7/d8d/classdraftguitools_1_1gui__trackers_1_1rectangleTracker.html#a228a5fce20903baa872be30d7d392a6e),
and
[ArchVRM.Renderer.isInside()](../../d5/dfd/classArchVRM_1_1Renderer.html#ae3b9d221eef5caf5fb883fcd5894521d).

Referenced by
[ArchVRM.Renderer.compare()](../../d5/dfd/classArchVRM_1_1Renderer.html#a78f4e0b92707209bcfeb72db372e044a).

## Member Data Documentation

## ◆ faces

ArchVRM.Renderer.faces  
---  
  
Referenced by
[ArchVRM.Renderer.addFaces()](../../d5/dfd/classArchVRM_1_1Renderer.html#a5398694c47561828347cdb21b9a8783f),
[ArchVRM.Renderer.addLabels()](../../d5/dfd/classArchVRM_1_1Renderer.html#a154c8a7fb7273e3ecc7242a6f048f659),
[ArchVRM.Renderer.addObjects()](../../d5/dfd/classArchVRM_1_1Renderer.html#ae9d5501f6f159004a5735e337c03ef1e),
[ArchVRM.Renderer.addShapes()](../../d5/dfd/classArchVRM_1_1Renderer.html#aec9719059fd4a06e2cd43792827a985c),
[ArchVRM.Renderer.buildDummy()](../../d5/dfd/classArchVRM_1_1Renderer.html#a3aa0cbbf0fed468267430ecc693fa19d),
[ArchVRM.Renderer.cut()](../../d5/dfd/classArchVRM_1_1Renderer.html#a42a08e8de6110aefc78bdfd483206b10),
[ArchVRM.Renderer.findPosition()](../../d5/dfd/classArchVRM_1_1Renderer.html#a97f368ace00f62ba6fcd7754d27658b8),
[ArchVRM.Renderer.getViewSVG()](../../d5/dfd/classArchVRM_1_1Renderer.html#a93d12556de6816282a9c7f85c8b0970a),
[ArchVRM.Renderer.info()](../../d5/dfd/classArchVRM_1_1Renderer.html#a0beedb32288b016f4a4739b78803562e),
[ArchVRM.Renderer.removeHidden()](../../d5/dfd/classArchVRM_1_1Renderer.html#a61819c30358d66516bdad27291128881),
[ArchVRM.Renderer.reorient()](../../d5/dfd/classArchVRM_1_1Renderer.html#acfbe4d1ea07b8ae822f94499f6aebce9),
and
[ArchVRM.Renderer.sort()](../../d5/dfd/classArchVRM_1_1Renderer.html#abd10a8841e997a0eae5ffcf357b306a3).

## ◆ hiddenEdges

ArchVRM.Renderer.hiddenEdges  
---  
  
Referenced by
[ArchVRM.Renderer.cut()](../../d5/dfd/classArchVRM_1_1Renderer.html#a42a08e8de6110aefc78bdfd483206b10),
[ArchVRM.Renderer.getHiddenSVG()](../../d5/dfd/classArchVRM_1_1Renderer.html#a260a5d749414eb9baecb3d78587e371c),
and
[ArchVRM.Renderer.reorient()](../../d5/dfd/classArchVRM_1_1Renderer.html#acfbe4d1ea07b8ae822f94499f6aebce9).

## ◆ iscut

ArchVRM.Renderer.iscut  
---  
  
Referenced by
[ArchVRM.Renderer.cut()](../../d5/dfd/classArchVRM_1_1Renderer.html#a42a08e8de6110aefc78bdfd483206b10).

## ◆ joined

ArchVRM.Renderer.joined  
---  
  
Referenced by
[ArchVRM.Renderer.cut()](../../d5/dfd/classArchVRM_1_1Renderer.html#a42a08e8de6110aefc78bdfd483206b10).

## ◆ objects

ArchVRM.Renderer.objects  
---  
  
Referenced by
[ArchNesting.Nester.addObjects()](../../d0/df4/classArchNesting_1_1Nester.html#a1f946b09a59e8cbfa07786ad9efd1c1e),
[ArchVRM.Renderer.addObjects()](../../d5/dfd/classArchVRM_1_1Renderer.html#ae9d5501f6f159004a5735e337c03ef1e),
[ArchNesting.Nester.apply()](../../d0/df4/classArchNesting_1_1Nester.html#a5a54761a94bf3b3a500582014b33a8bc),
[ArchNesting.Nester.clear()](../../d0/df4/classArchNesting_1_1Nester.html#a5a000afd19e4cceaa9b0cea8be980f92),
and
[exportIFCHelper.ContextCreator.getProjectObject()](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#aa3ac63346b1513523c069e16745f66c1).

## ◆ oriented

ArchVRM.Renderer.oriented  
---  
  
Referenced by
[ArchVRM.Renderer.cut()](../../d5/dfd/classArchVRM_1_1Renderer.html#a42a08e8de6110aefc78bdfd483206b10),
[ArchVRM.Renderer.getHiddenSVG()](../../d5/dfd/classArchVRM_1_1Renderer.html#a260a5d749414eb9baecb3d78587e371c),
[ArchVRM.Renderer.getSectionSVG()](../../d5/dfd/classArchVRM_1_1Renderer.html#ae6f1fdf02312ca7e2d0ec5788b3aadcd),
[ArchVRM.Renderer.info()](../../d5/dfd/classArchVRM_1_1Renderer.html#a0beedb32288b016f4a4739b78803562e),
[ArchVRM.Renderer.reorient()](../../d5/dfd/classArchVRM_1_1Renderer.html#acfbe4d1ea07b8ae822f94499f6aebce9),
and
[ArchVRM.Renderer.sort()](../../d5/dfd/classArchVRM_1_1Renderer.html#abd10a8841e997a0eae5ffcf357b306a3).

## ◆ sections

ArchVRM.Renderer.sections  
---  
  
Referenced by
[ArchVRM.Renderer.cut()](../../d5/dfd/classArchVRM_1_1Renderer.html#a42a08e8de6110aefc78bdfd483206b10),
[ArchVRM.Renderer.getHiddenSVG()](../../d5/dfd/classArchVRM_1_1Renderer.html#a260a5d749414eb9baecb3d78587e371c),
[ArchVRM.Renderer.getSectionSVG()](../../d5/dfd/classArchVRM_1_1Renderer.html#ae6f1fdf02312ca7e2d0ec5788b3aadcd),
[ArchVRM.Renderer.reorient()](../../d5/dfd/classArchVRM_1_1Renderer.html#acfbe4d1ea07b8ae822f94499f6aebce9),
and
[femsolver.elmer.sifio.Sif.write()](../../d5/dce/classfemsolver_1_1elmer_1_1sifio_1_1Sif.html#a9c0d6bec705c701aa99ba64b5f5ee574).

## ◆ shapes

ArchVRM.Renderer.shapes  
---  
  
Referenced by
[ArchNesting.Nester.addObjects()](../../d0/df4/classArchNesting_1_1Nester.html#a1f946b09a59e8cbfa07786ad9efd1c1e),
[ArchVRM.Renderer.addObjects()](../../d5/dfd/classArchVRM_1_1Renderer.html#ae9d5501f6f159004a5735e337c03ef1e),
[ArchVRM.Renderer.addShapes()](../../d5/dfd/classArchVRM_1_1Renderer.html#aec9719059fd4a06e2cd43792827a985c),
[ArchNesting.Nester.clear()](../../d0/df4/classArchNesting_1_1Nester.html#a5a000afd19e4cceaa9b0cea8be980f92),
[ArchVRM.Renderer.cut()](../../d5/dfd/classArchVRM_1_1Renderer.html#a42a08e8de6110aefc78bdfd483206b10),
[ArchPanel.NestTaskPanel.getContainer()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#ad25ef9b5aade32a390de4a8bd34bafda),
[ArchPanel.NestTaskPanel.getShapes()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#a52edae24a9d124678d48b157749b5f04),
[PathScripts.PathDressupDogbone.ObjectDressup.insertBone()](../../d5/dfa/classPathScripts_1_1PathDressupDogbone_1_1ObjectDressup.html#a5d52eb985f34b6eb0d161bc6e25de874),
[ArchPanel.NestTaskPanel.removeShapes()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#a14b88173115d5a126ac1d5a0bc973395),
[ArchNesting.Nester.run()](../../d0/df4/classArchNesting_1_1Nester.html#af4bd331488aca3d29d5ade158e30b102),
[PathScripts.PathDressupDogbone.ObjectDressup.setup()](../../d5/dfa/classPathScripts_1_1PathDressupDogbone_1_1ObjectDressup.html#a810152e1fbb2f48646297c091e52d6a1),
and
[ArchPanel.NestTaskPanel.start()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#ae94d1620245089dea3da24cffad8f785).

## ◆ sorted

ArchVRM.Renderer.sorted  
---  
  
Referenced by
[ArchVRM.Renderer.buildDummy()](../../d5/dfd/classArchVRM_1_1Renderer.html#a3aa0cbbf0fed468267430ecc693fa19d),
[ArchVRM.Renderer.cut()](../../d5/dfd/classArchVRM_1_1Renderer.html#a42a08e8de6110aefc78bdfd483206b10),
[ArchVRM.Renderer.getViewSVG()](../../d5/dfd/classArchVRM_1_1Renderer.html#a93d12556de6816282a9c7f85c8b0970a),
[ArchVRM.Renderer.info()](../../d5/dfd/classArchVRM_1_1Renderer.html#a0beedb32288b016f4a4739b78803562e),
and
[ArchVRM.Renderer.sort()](../../d5/dfd/classArchVRM_1_1Renderer.html#abd10a8841e997a0eae5ffcf357b306a3).

## ◆ trimmed

ArchVRM.Renderer.trimmed  
---  
  
Referenced by
[ArchVRM.Renderer.cut()](../../d5/dfd/classArchVRM_1_1Renderer.html#a42a08e8de6110aefc78bdfd483206b10),
[ArchVRM.Renderer.info()](../../d5/dfd/classArchVRM_1_1Renderer.html#a0beedb32288b016f4a4739b78803562e),
[ArchVRM.Renderer.removeHidden()](../../d5/dfd/classArchVRM_1_1Renderer.html#a61819c30358d66516bdad27291128881),
and
[ArchVRM.Renderer.sort()](../../d5/dfd/classArchVRM_1_1Renderer.html#abd10a8841e997a0eae5ffcf357b306a3).

## ◆ wp

ArchVRM.Renderer.wp  
---  
  
Referenced by
[ArchVRM.Renderer.isInside()](../../d5/dfd/classArchVRM_1_1Renderer.html#ae3b9d221eef5caf5fb883fcd5894521d),
[ArchVRM.Renderer.isVisible()](../../d5/dfd/classArchVRM_1_1Renderer.html#a87a6c89b1891db19398235a1d7142c5f),
[ArchVRM.Renderer.projectEdge()](../../d5/dfd/classArchVRM_1_1Renderer.html#a0022e29552adab1c6f7f91710c0d1880),
[ArchVRM.Renderer.projectFace()](../../d5/dfd/classArchVRM_1_1Renderer.html#a2476b5baba8beebf01fcfddcbe1b7ede),
and
[ArchVRM.Renderer.setWorkingPlane()](../../d5/dfd/classArchVRM_1_1Renderer.html#aa8a752e2d04b66cbe66a500efb36565b).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Arch/ArchVRM.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

