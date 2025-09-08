---
url: https://freecad.github.io/SourceDoc/d8/d49/namespaceArchSectionPlane.html
scraped_at: 2025-09-08T14:58:26.372661
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

Classes | Functions | Variables

ArchSectionPlane Namespace Reference

[Workbenches](../../d2/df2/group__WORKBENCHES.html) » [Python
workbenches](../../d1/d82/group__PYTHONWORKBENCHES.html) »
[Arch](../../df/dce/group__ARCH.html)

The Section plane object and tools.
[More...](../../d8/d49/namespaceArchSectionPlane.html#details)

##  Classes  
  
---  
class | [SectionPlaneTaskPanel](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html)  
  
##  Functions  
  
---  
def | [closeViewer](../../d8/d49/namespaceArchSectionPlane.html#aa159e2389526d677138c754c18152c1c) (name)  
def | [getCameraData](../../d8/d49/namespaceArchSectionPlane.html#a36700e4f89839e2d6b562587564ca120) (floatlist)  
def | [getCoinSVG](../../d8/d49/namespaceArchSectionPlane.html#ad78e5453cf2b7d1746bf6520f9b9018a) (cutplane, objs, cameradata=None, linewidth=0.2, singleface=False, facecolor=None)  
def | [getCutShapes](../../d8/d49/namespaceArchSectionPlane.html#ad98fe70f703c12fd886e5d69fa88e200) (objs, cutplane, onlySolids, clip, joinArch, showHidden, groupSshapesByObject=False)  
def | [getDXF](../../d8/d49/namespaceArchSectionPlane.html#af9d861806c30dc30ac9a877e8ee67ef1) (obj)  
def | [getFillForObject](../../d8/d49/namespaceArchSectionPlane.html#ae1e7f165a6d0636b7eed5fa9e53a9cab) (o, defaultFill, source)  
def | [getSectionData](../../d8/d49/namespaceArchSectionPlane.html#aa958241dec0f9c12e300124765a4e2f9) (source)  
def | [getSVG](../../d8/d49/namespaceArchSectionPlane.html#ab394202bbb94a23f3248dc20ef00fdc6) (source, renderMode="Wireframe", allOn=False, showHidden=False, scale=1, rotation=0, linewidth=1, lineColor=(0.0, 0.0, 0.0), fontsize=1, showFill=False, fillColor=(1.0, 1.0, 1.0), techdraw=False, fillSpaces=False, cutlinewidth=0, joinArch=False)  
def | [isOriented](../../d8/d49/namespaceArchSectionPlane.html#ad465126d62005df3ae71a3783a392666) (obj, plane)  
def | [looksLikeDraft](../../d8/d49/namespaceArchSectionPlane.html#a7b9449d84e1241b75f1440b1207a81e0) (o)  
def | [makeSectionPlane](../../d8/d49/namespaceArchSectionPlane.html#a0248c326a0b2d6260f340369ac805ac7) (objectslist=None, name="Section")  
def | [makeSectionView](../../d8/d49/namespaceArchSectionPlane.html#a896474df2c7727bab6657b4233867ead) (section, name="View")  
def | [update_svg_cache](../../d8/d49/namespaceArchSectionPlane.html#a939ac133bc859539a698c2bbdf4060aa) (source, renderMode, showHidden, showFill, fillSpaces, joinArch, allOn, objs)  
  
##  Variables  
  
---  
[bool](../../d9/db9/classbool.html) | [ISRENDERING](../../d8/d49/namespaceArchSectionPlane.html#a1bd722300f0886564f6d4a031591487b) = False  
  
## Detailed Description

The Section plane object and tools.

This module provides tools to build Section plane objects. It also contains
functionality to produce SVG rendering of section planes, to be used in
[TechDraw](../../d7/d31/namespaceTechDraw.html "HatchLine - Classes related to
processing PAT files.") and [Drawing](../../d2/dba/namespaceDrawing.html)
modules

## Function Documentation

## ◆ closeViewer()

def ArchSectionPlane.closeViewer  | ( |  | _name_| ) |   
---|---|---|---|---|---  
      
    
    Close temporary viewers

References
[ArchCommands.getDefaultColor()](../../d4/d52/namespaceArchCommands.html#abfe83988dd63577babc96771bb3212a0),
[getSVG()](../../d8/d49/namespaceArchSectionPlane.html#ab394202bbb94a23f3248dc20ef00fdc6),
[DraftVecUtils.project()](../../dc/dc3/group__DRAFTVECUTILS.html#ga1bf889753387ffb78fb07cb90abed8bc),
and
[draftutils.translate.QT_TRANSLATE_NOOP](../../de/d75/group__draftutils.html#ga9e6796e4394a4a163501246d7390f3c4).

Referenced by
[getCoinSVG()](../../d8/d49/namespaceArchSectionPlane.html#ad78e5453cf2b7d1746bf6520f9b9018a).

## ◆ getCameraData()

def ArchSectionPlane.getCameraData  | ( |  | _floatlist_| ) |   
---|---|---|---|---|---  
      
    
    reconstructs a valid camera data string from stored values

## ◆ getCoinSVG()

def ArchSectionPlane.getCoinSVG  | ( |  | _cutplane_ ,   
---|---|---|---  
|  |  | _objs_ ,   
|  |  | _cameradata_ = `None`,   
|  |  | _linewidth_ = `0.2`,   
|  |  | _singleface_ = `False`,   
|  |  | _facecolor_ = `None`  
| ) | |   
      
    
    Returns an SVG fragment generated from a coin view

References
[closeViewer()](../../d8/d49/namespaceArchSectionPlane.html#aa159e2389526d677138c754c18152c1c),
[WorkingPlane.plane](../../d8/d4a/namespaceWorkingPlane.html#acd818647b5d80bd53b91ee7d60184f68),
and
[DraftVecUtils.project()](../../dc/dc3/group__DRAFTVECUTILS.html#ga1bf889753387ffb78fb07cb90abed8bc).

Referenced by
[getSVG()](../../d8/d49/namespaceArchSectionPlane.html#ab394202bbb94a23f3248dc20ef00fdc6).

## ◆ getCutShapes()

def ArchSectionPlane.getCutShapes  | ( |  | _objs_ ,   
---|---|---|---  
|  |  | _cutplane_ ,   
|  |  | _onlySolids_ ,   
|  |  | _clip_ ,   
|  |  | _joinArch_ ,   
|  |  | _showHidden_ ,   
|  |  | _groupSshapesByObject_ = `False`  
| ) | |   
      
    
    returns a list of shapes (visible, hidden, cut lines...)
    obtained from performing a series of booleans against the given cut plane
    

References
[ArchCommands.getCutVolume()](../../d4/d52/namespaceArchCommands.html#aa9bddbee3691ffd7b3cba2f35e55ce77).

Referenced by
[getDXF()](../../d8/d49/namespaceArchSectionPlane.html#af9d861806c30dc30ac9a877e8ee67ef1),
and
[getSVG()](../../d8/d49/namespaceArchSectionPlane.html#ab394202bbb94a23f3248dc20ef00fdc6).

## ◆ getDXF()

def ArchSectionPlane.getDXF  | ( |  | _obj_| ) |   
---|---|---|---|---|---  
      
    
    Return a DXF representation from a TechDraw/Drawing view.

References
[getCutShapes()](../../d8/d49/namespaceArchSectionPlane.html#ad98fe70f703c12fd886e5d69fa88e200),
and
[getSectionData()](../../d8/d49/namespaceArchSectionPlane.html#aa958241dec0f9c12e300124765a4e2f9).

Referenced by
[importDXF.getViewDXF()](../../d7/dbf/namespaceimportDXF.html#a781db18266868125c4d4a584c832cbfb).

## ◆ getFillForObject()

def ArchSectionPlane.getFillForObject  | ( |  | _o_ ,   
---|---|---|---  
|  |  | _defaultFill_ ,   
|  |  | _source_  
| ) | |   
      
    
    returns a color tuple from an object's material

Referenced by
[getSVG()](../../d8/d49/namespaceArchSectionPlane.html#ab394202bbb94a23f3248dc20ef00fdc6).

## ◆ getSectionData()

def ArchSectionPlane.getSectionData  | ( |  | _source_| ) |   
---|---|---|---|---|---  
      
    
    Returns some common data from section planes and building parts

Referenced by
[getDXF()](../../d8/d49/namespaceArchSectionPlane.html#af9d861806c30dc30ac9a877e8ee67ef1),
and
[getSVG()](../../d8/d49/namespaceArchSectionPlane.html#ab394202bbb94a23f3248dc20ef00fdc6).

## ◆ getSVG()

def ArchSectionPlane.getSVG  | ( |  | _source_ ,   
---|---|---|---  
|  |  | _renderMode_ = `"Wireframe"`,   
|  |  | _allOn_ = `False`,   
|  |  | _showHidden_ = `False`,   
|  |  | _scale_ = `1`,   
|  |  | _rotation_ = `0`,   
|  |  | _linewidth_ = `1`,   
|  |  | _lineColor_ = `(0.0, 0.0, 0.0)`,   
|  |  | _fontsize_ = `1`,   
|  |  | _showFill_ = `False`,   
|  |  | _fillColor_ = `(1.0, 1.0, 1.0)`,   
|  |  | _techdraw_ = `False`,   
|  |  | _fillSpaces_ = `False`,   
|  |  | _cutlinewidth_ = `0`,   
|  |  | _joinArch_ = `False`  
| ) | |   
      
    
    Return an SVG fragment from an Arch SectionPlane or BuildingPart.
    
    allOn
        If it is `True`, all cut objects are shown, regardless of if they are
        visible or not.
    
    renderMode
        Can be `'Wireframe'` (default) or `'Solid'` to use the Arch solid
        renderer.
    
    showHidden
        If it is `True`, the hidden geometry above the section plane
        is shown in dashed line.
    
    showFill
        If it is `True`, the cut areas get filled with a pattern.
    
    lineColor
        Color of lines for the `renderMode` is `'Wireframe'`.
    
    fillColor
        If `showFill` is `True` and `renderMode` is `'Wireframe'`,
        the cut areas are filled with `fillColor`.
    
    fillSpaces
        If `True`, shows space objects as filled surfaces.
    

References
[getCoinSVG()](../../d8/d49/namespaceArchSectionPlane.html#ad78e5453cf2b7d1746bf6520f9b9018a),
[getCutShapes()](../../d8/d49/namespaceArchSectionPlane.html#ad98fe70f703c12fd886e5d69fa88e200),
[getFillForObject()](../../d8/d49/namespaceArchSectionPlane.html#ae1e7f165a6d0636b7eed5fa9e53a9cab),
[getSectionData()](../../d8/d49/namespaceArchSectionPlane.html#aa958241dec0f9c12e300124765a4e2f9),
[isOriented()](../../d8/d49/namespaceArchSectionPlane.html#ad465126d62005df3ae71a3783a392666),
[looksLikeDraft()](../../d8/d49/namespaceArchSectionPlane.html#a7b9449d84e1241b75f1440b1207a81e0),
[WorkingPlane.plane](../../d8/d4a/namespaceWorkingPlane.html#acd818647b5d80bd53b91ee7d60184f68),
and
[update_svg_cache()](../../d8/d49/namespaceArchSectionPlane.html#a939ac133bc859539a698c2bbdf4060aa).

Referenced by
[closeViewer()](../../d8/d49/namespaceArchSectionPlane.html#aa159e2389526d677138c754c18152c1c).

## ◆ isOriented()

def ArchSectionPlane.isOriented  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _plane_  
| ) | |   
      
    
    determines if an annotation is facing the cutplane or not

Referenced by
[getSVG()](../../d8/d49/namespaceArchSectionPlane.html#ab394202bbb94a23f3248dc20ef00fdc6).

## ◆ looksLikeDraft()

def ArchSectionPlane.looksLikeDraft  | ( |  | _o_| ) |   
---|---|---|---|---|---  
      
    
    Does this object look like a Draft shape? (flat, no solid, etc)

Referenced by
[getSVG()](../../d8/d49/namespaceArchSectionPlane.html#ab394202bbb94a23f3248dc20ef00fdc6).

## ◆ makeSectionPlane()

def ArchSectionPlane.makeSectionPlane  | ( |  | _objectslist_ = `None`,   
---|---|---|---  
|  |  | _name_ = `"Section"`  
| ) | |   
      
    
    makeSectionPlane([objectslist]) : Creates a Section plane objects including the
    given objects. If no object is given, the whole document will be considered.

## ◆ makeSectionView()

def ArchSectionPlane.makeSectionView  | ( |  | _section_ ,   
---|---|---|---  
|  |  | _name_ = `"View"`  
| ) | |   
      
    
    OBSOLETE
    makeSectionView(section) : Creates a Drawing view of the given Section Plane
    in the active Page object (a new page will be created if none exists

References
[makeSectionView()](../../d8/d49/namespaceArchSectionPlane.html#a896474df2c7727bab6657b4233867ead).

Referenced by
[makeSectionView()](../../d8/d49/namespaceArchSectionPlane.html#a896474df2c7727bab6657b4233867ead).

## ◆ update_svg_cache()

def ArchSectionPlane.update_svg_cache  | ( |  | _source_ ,   
---|---|---|---  
|  |  | _renderMode_ ,   
|  |  | _showHidden_ ,   
|  |  | _showFill_ ,   
|  |  | _fillSpaces_ ,   
|  |  | _joinArch_ ,   
|  |  | _allOn_ ,   
|  |  | _objs_  
| ) | |   
      
    
    Returns None or cached SVG, clears shape cache if required
    

Referenced by
[getSVG()](../../d8/d49/namespaceArchSectionPlane.html#ab394202bbb94a23f3248dc20ef00fdc6).

## Variable Documentation

## ◆ ISRENDERING

[bool](../../d9/db9/classbool.html) ArchSectionPlane.ISRENDERING = False  
---  
  
* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

