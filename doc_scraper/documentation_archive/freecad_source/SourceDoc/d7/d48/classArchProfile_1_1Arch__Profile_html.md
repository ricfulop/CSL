---
url: https://freecad.github.io/SourceDoc/d7/d48/classArchProfile_1_1Arch__Profile.html
scraped_at: 2025-09-08T14:58:15.319420
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ArchProfile](../../df/dee/namespaceArchProfile.html)
  * [Arch_Profile](../../d7/d48/classArchProfile_1_1Arch__Profile.html)

[List of all members](../../d7/d13/classArchProfile_1_1Arch__Profile-members.html) | Public Member Functions | Public Attributes

ArchProfile.Arch_Profile Class Reference

##  Public Member Functions  
  
---  
def | [Activated](../../d7/d48/classArchProfile_1_1Arch__Profile.html#a763cf4009bc9139fb9ee7cf65d0cc65b) (self)  
def | [getPoint](../../d7/d48/classArchProfile_1_1Arch__Profile.html#adba04e55c6f0800f15566d4246397582) (self, point=None, obj=None)  
def | [GetResources](../../d7/d48/classArchProfile_1_1Arch__Profile.html#a10b6bc033bdd90fc7b3549acf3de6aae) (self)  
def | [IsActive](../../d7/d48/classArchProfile_1_1Arch__Profile.html#a8c9bf0c7e228a662cd1433af65954eb1) (self)  
def | [setCategory](../../d7/d48/classArchProfile_1_1Arch__Profile.html#aeb374a3c40d75b04d7c3f37eba51ed31) (self, i)  
def | [setPreset](../../d7/d48/classArchProfile_1_1Arch__Profile.html#ae128806d02925f8e8a82559c8dee3f8f) (self, i)  
def | [taskbox](../../d7/d48/classArchProfile_1_1Arch__Profile.html#adb2ad6553bb71bab23e1d2ad3de1034f) (self)  
  
##  Public Attributes  
  
---  
|
[Categories](../../d7/d48/classArchProfile_1_1Arch__Profile.html#a2d84fb4ba820e0172a0de7891d89deae)  
|
[Presets](../../d7/d48/classArchProfile_1_1Arch__Profile.html#a7190d3fad0b453a2ac7fcaed8d3f18a5)  
|
[Profile](../../d7/d48/classArchProfile_1_1Arch__Profile.html#a4810f8511de0e13f8ecd5d955c19c644)  
|
[pSelect](../../d7/d48/classArchProfile_1_1Arch__Profile.html#a23ea2b071dfde958a0040ab6002ba904)  
|
[vCategory](../../d7/d48/classArchProfile_1_1Arch__Profile.html#abf39669fb8387a7a288b07331f1d6cea)  
|
[vPresets](../../d7/d48/classArchProfile_1_1Arch__Profile.html#a97f0198a583266e1b11ba3ae01102819)  
  
## Detailed Description

    
    
    The FreeCAD Arch_Profile command definition

## Member Function Documentation

## ◆ Activated()

def ArchProfile.Arch_Profile.Activated  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftguitools.gui_arcs.Arc.finish()](../../da/d4f/classdraftguitools_1_1gui__arcs_1_1Arc.html#a2262d966a879bfa9b71d9c699e6929b2),
[draftguitools.gui_beziers.BezCurve.finish()](../../d2/dce/classdraftguitools_1_1gui__beziers_1_1BezCurve.html#a6b4598d09cb7c1f0b06fe1b96cc9096f),
[draftguitools.gui_beziers.CubicBezCurve.finish()](../../de/d5e/classdraftguitools_1_1gui__beziers_1_1CubicBezCurve.html#abadcbdae43b1e54d516d249c71fc0991),
[draftguitools.gui_ellipses.Ellipse.finish()](../../db/d98/classdraftguitools_1_1gui__ellipses_1_1Ellipse.html#aa534628f13f8ad6effacb1fcbd76bb2a),
[draftguitools.gui_lines.Line.finish()](../../da/d8f/classdraftguitools_1_1gui__lines_1_1Line.html#a622af4e1166f892f860b86d3d1e3f053),
[draftguitools.gui_mirror.Mirror.finish()](../../d8/dbd/classdraftguitools_1_1gui__mirror_1_1Mirror.html#a73d8f0dba4d186590485bf972fa8e25d),
[draftguitools.gui_move.Move.finish()](../../d2/df5/classdraftguitools_1_1gui__move_1_1Move.html#aa2c8c371106351f316c238f67bf7accf),
[draftguitools.gui_polygons.Polygon.finish()](../../df/d3d/classdraftguitools_1_1gui__polygons_1_1Polygon.html#a06317245940b6d99d62b0823d657dcb2),
[draftguitools.gui_rectangles.Rectangle.finish()](../../dd/d46/classdraftguitools_1_1gui__rectangles_1_1Rectangle.html#a7ba174f4093affb5af55e58c804a527d),
[draftguitools.gui_rotate.Rotate.finish()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#ad60faae5b86f1d2c74f045c2291ae6dd),
[draftguitools.gui_splines.BSpline.finish()](../../d1/d3f/classdraftguitools_1_1gui__splines_1_1BSpline.html#ab00ba1111a2b9d2afcee43a0396a4cd5),
[draftguitools.gui_texts.Text.finish()](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a3fe64be64c77319af1f265609dd8e985),
[draftguitools.gui_points.Point.finish()](../../d7/dc7/classdraftguitools_1_1gui__points_1_1Point.html#ac55499c15db7b01680f41b3f3dd32477),
[draftguitools.gui_shapestrings.ShapeString.finish()](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#af7a14bf7135177bc521cfa7a9123b2bf),
[draftguitools.gui_arcs.Arc_3Points.getPoint()](../../d4/d32/classdraftguitools_1_1gui__arcs_1_1Arc__3Points.html#addd65326b504c7bf765526ef2db14321),
and
[ArchPanel.CommandPanel.getPoint()](../../d9/d86/classArchPanel_1_1CommandPanel.html#ad968284b7adc2bee10d76a20c1a4c7fb).

## ◆ getPoint()

def ArchProfile.Arch_Profile.getPoint  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _point_ = `None`,   
|  |  | _obj_ = `None`  
| ) | |   
  
References
[ArchPanel.CommandPanel.Profile](../../d9/d86/classArchPanel_1_1CommandPanel.html#ae6853ed51f834120710e01c60464f3f3),
[ArchProfile.Arch_Profile.Profile](../../d7/d48/classArchProfile_1_1Arch__Profile.html#a4810f8511de0e13f8ecd5d955c19c644),
ArchProfile._Profile.Profile,
[ArchProfile.ProfileTaskPanel.Profile](../../dc/d9a/classArchProfile_1_1ProfileTaskPanel.html#a00eb3f90d2c95c384614b65cc9dde08b),
ArchStructure._CommandStructure.Profile,
[PartDesign::ProfileBased.Profile](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a43d980d965c8eb1f6e0cb6c1ce7be7dd),
[PartDesignGui::ViewProviderLoft.Profile](../../d9/d6e/classPartDesignGui_1_1ViewProviderLoft.html#a967511bbda23b602ebc9e2df52372a3ea3a40eaf32c21ad73474836cff86b8b68),
and
[PartDesignGui::ViewProviderPipe.Profile](../../d8/dc8/classPartDesignGui_1_1ViewProviderPipe.html#a33e876ddcc94e710a86a041b38a407a5a451e0dea3c048d27a9ecf0294c99f141).

Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[PathScripts.PathOpGui.TaskPanelBaseLocationPage.addLocation()](../../d6/d50/classPathScripts_1_1PathOpGui_1_1TaskPanelBaseLocationPage.html#ab5f56b9ada560aab1c7ec52da82887e2),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.addNewTag()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#ad5c4ec1bd21c22bd83a9ef4c2cf7b2a8),
[PathScripts.PathOpGui.TaskPanelBaseLocationPage.editLocation()](../../d6/d50/classPathScripts_1_1PathOpGui_1_1TaskPanelBaseLocationPage.html#a6eaff94ff9e615e8dacac7241fb3229d),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.editTag()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#a66963fb0f8fbff5f5b1f0de6d92aa468),
[draftguitools.gui_arcs.Arc_3Points.getPoint()](../../d4/d32/classdraftguitools_1_1gui__arcs_1_1Arc__3Points.html#addd65326b504c7bf765526ef2db14321),
[ArchCurtainWall.CommandArchCurtainWall.getPoint()](../../d3/d55/classArchCurtainWall_1_1CommandArchCurtainWall.html#ae21c6277cadac9992ad426960f203392),
[ArchTruss.CommandArchTruss.getPoint()](../../dc/d2c/classArchTruss_1_1CommandArchTruss.html#aee560d06232a65dbd5f410bcac5c0318),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.modifyStandardButtons()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#a7e92a13bef37b0a1ba80f6ee14501147),
and
[PathScripts.PathOpGui.TaskPanelBaseLocationPage.modifyStandardButtons()](../../d6/d50/classPathScripts_1_1PathOpGui_1_1TaskPanelBaseLocationPage.html#aac091052db42e260ae961d00e55aa4a0).

## ◆ GetResources()

def ArchProfile.Arch_Profile.GetResources  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[draftutils.translate.QT_TRANSLATE_NOOP](../../de/d75/group__draftutils.html#ga9e6796e4394a4a163501246d7390f3c4).

## ◆ IsActive()

def ArchProfile.Arch_Profile.IsActive  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
## ◆ setCategory()

def ArchProfile.Arch_Profile.setCategory  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _i_  
| ) | |   
  
References
[ArchProfile.Arch_Profile.Categories](../../d7/d48/classArchProfile_1_1Arch__Profile.html#a2d84fb4ba820e0172a0de7891d89deae),
[ArchProfile.Arch_Profile.Presets](../../d7/d48/classArchProfile_1_1Arch__Profile.html#a7190d3fad0b453a2ac7fcaed8d3f18a5),
[ArchProfile.Arch_Profile.pSelect](../../d7/d48/classArchProfile_1_1Arch__Profile.html#a23ea2b071dfde958a0040ab6002ba904),
ArchStructure._CommandStructure.pSelect,
[ArchPanel.CommandPanel.setPreset()](../../d9/d86/classArchPanel_1_1CommandPanel.html#a8ee939633a1994367e81aaac4b9d1103),
[ArchProfile.Arch_Profile.setPreset()](../../d7/d48/classArchProfile_1_1Arch__Profile.html#ae128806d02925f8e8a82559c8dee3f8f),
ArchStructure._CommandStructure.setPreset(),
ArchWindow._CommandWindow.setPreset(),
ArchPrecast._PrecastTaskPanel.setPreset(),
[ArchProfile.Arch_Profile.vPresets](../../d7/d48/classArchProfile_1_1Arch__Profile.html#a97f0198a583266e1b11ba3ae01102819),
and ArchStructure._CommandStructure.vPresets.

Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c).

## ◆ setPreset()

def ArchProfile.Arch_Profile.setPreset  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _i_  
| ) | |   
  
References
[ArchProfile.Arch_Profile.Presets](../../d7/d48/classArchProfile_1_1Arch__Profile.html#a7190d3fad0b453a2ac7fcaed8d3f18a5),
[ArchPanel.CommandPanel.Profile](../../d9/d86/classArchPanel_1_1CommandPanel.html#ae6853ed51f834120710e01c60464f3f3),
[ArchProfile.Arch_Profile.Profile](../../d7/d48/classArchProfile_1_1Arch__Profile.html#a4810f8511de0e13f8ecd5d955c19c644),
ArchProfile._Profile.Profile,
[ArchProfile.ProfileTaskPanel.Profile](../../dc/d9a/classArchProfile_1_1ProfileTaskPanel.html#a00eb3f90d2c95c384614b65cc9dde08b),
ArchStructure._CommandStructure.Profile,
[PartDesign::ProfileBased.Profile](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a43d980d965c8eb1f6e0cb6c1ce7be7dd),
[PartDesignGui::ViewProviderLoft.Profile](../../d9/d6e/classPartDesignGui_1_1ViewProviderLoft.html#a967511bbda23b602ebc9e2df52372a3ea3a40eaf32c21ad73474836cff86b8b68),
[PartDesignGui::ViewProviderPipe.Profile](../../d8/dc8/classPartDesignGui_1_1ViewProviderPipe.html#a33e876ddcc94e710a86a041b38a407a5a451e0dea3c048d27a9ecf0294c99f141),
[ArchProfile.Arch_Profile.pSelect](../../d7/d48/classArchProfile_1_1Arch__Profile.html#a23ea2b071dfde958a0040ab6002ba904),
ArchStructure._CommandStructure.pSelect, and
[draftutils.translate.QT_TRANSLATE_NOOP](../../de/d75/group__draftutils.html#ga9e6796e4394a4a163501246d7390f3c4).

Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
and
[ArchProfile.Arch_Profile.setCategory()](../../d7/d48/classArchProfile_1_1Arch__Profile.html#aeb374a3c40d75b04d7c3f37eba51ed31).

## ◆ taskbox()

def ArchProfile.Arch_Profile.taskbox  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c).

## Member Data Documentation

## ◆ Categories

ArchProfile.Arch_Profile.Categories  
---  
  
Referenced by
[ArchProfile.Arch_Profile.setCategory()](../../d7/d48/classArchProfile_1_1Arch__Profile.html#aeb374a3c40d75b04d7c3f37eba51ed31).

## ◆ Presets

ArchProfile.Arch_Profile.Presets  
---  
  
Referenced by
[ArchProfile.Arch_Profile.setCategory()](../../d7/d48/classArchProfile_1_1Arch__Profile.html#aeb374a3c40d75b04d7c3f37eba51ed31),
and
[ArchProfile.Arch_Profile.setPreset()](../../d7/d48/classArchProfile_1_1Arch__Profile.html#ae128806d02925f8e8a82559c8dee3f8f).

## ◆ Profile

ArchProfile.Arch_Profile.Profile  
---  
  
Referenced by
[ArchProfile.ProfileTaskPanel.accept()](../../dc/d9a/classArchProfile_1_1ProfileTaskPanel.html#a2506d93eee0ae9e8570d71e066425999),
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[ArchProfile.ProfileTaskPanel.changeProfile()](../../dc/d9a/classArchProfile_1_1ProfileTaskPanel.html#a440683bf0e41eba72709320a7bd4c49b),
[ArchPanel.CommandPanel.getPoint()](../../d9/d86/classArchPanel_1_1CommandPanel.html#ad968284b7adc2bee10d76a20c1a4c7fb),
[ArchProfile.Arch_Profile.getPoint()](../../d7/d48/classArchProfile_1_1Arch__Profile.html#adba04e55c6f0800f15566d4246397582),
and
[ArchProfile.Arch_Profile.setPreset()](../../d7/d48/classArchProfile_1_1Arch__Profile.html#ae128806d02925f8e8a82559c8dee3f8f).

## ◆ pSelect

ArchProfile.Arch_Profile.pSelect  
---  
  
Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[ArchProfile.Arch_Profile.setCategory()](../../d7/d48/classArchProfile_1_1Arch__Profile.html#aeb374a3c40d75b04d7c3f37eba51ed31),
and
[ArchProfile.Arch_Profile.setPreset()](../../d7/d48/classArchProfile_1_1Arch__Profile.html#ae128806d02925f8e8a82559c8dee3f8f).

## ◆ vCategory

ArchProfile.Arch_Profile.vCategory  
---  
  
## ◆ vPresets

ArchProfile.Arch_Profile.vPresets  
---  
  
Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
and
[ArchProfile.Arch_Profile.setCategory()](../../d7/d48/classArchProfile_1_1Arch__Profile.html#aeb374a3c40d75b04d7c3f37eba51ed31).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Arch/ArchProfile.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

