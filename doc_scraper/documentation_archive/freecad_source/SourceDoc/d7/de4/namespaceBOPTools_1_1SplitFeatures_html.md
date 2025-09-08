---
url: https://freecad.github.io/SourceDoc/d7/de4/namespaceBOPTools_1_1SplitFeatures.html
scraped_at: 2025-09-08T15:18:45.459419
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [BOPTools](../../dc/dff/namespaceBOPTools.html)
  * [SplitFeatures](../../d7/de4/namespaceBOPTools_1_1SplitFeatures.html)

Classes | Functions | Variables

BOPTools.SplitFeatures Namespace Reference

##  Classes  
  
---  
class | [CommandBooleanFragments](../../d3/d93/classBOPTools_1_1SplitFeatures_1_1CommandBooleanFragments.html)  
class | [CommandSlice](../../d5/d56/classBOPTools_1_1SplitFeatures_1_1CommandSlice.html)  
class | [CommandSliceApart](../../d2/db2/classBOPTools_1_1SplitFeatures_1_1CommandSliceApart.html)  
class | [CommandXOR](../../d1/d26/classBOPTools_1_1SplitFeatures_1_1CommandXOR.html)  
class | [FeatureBooleanFragments](../../dc/d6e/classBOPTools_1_1SplitFeatures_1_1FeatureBooleanFragments.html)  
class | [FeatureSlice](../../d1/d28/classBOPTools_1_1SplitFeatures_1_1FeatureSlice.html)  
class | [FeatureXOR](../../da/dc0/classBOPTools_1_1SplitFeatures_1_1FeatureXOR.html)  
class | [ViewProviderBooleanFragments](../../d0/d5a/classBOPTools_1_1SplitFeatures_1_1ViewProviderBooleanFragments.html)  
class | [ViewProviderSlice](../../d5/d19/classBOPTools_1_1SplitFeatures_1_1ViewProviderSlice.html)  
class | [ViewProviderXOR](../../d9/de4/classBOPTools_1_1SplitFeatures_1_1ViewProviderXOR.html)  
  
##  Functions  
  
---  
def | [addCommands](../../d7/de4/namespaceBOPTools_1_1SplitFeatures.html#a7776b4ee5cbe0094a4c5738ae51bdd58) ()  
def | [cmdCreateBooleanFragmentsFeature](../../d7/de4/namespaceBOPTools_1_1SplitFeatures.html#ad8eb904015883fee20ff5ff0f4d1b8a3) (name, mode)  
def | [cmdCreateSliceFeature](../../d7/de4/namespaceBOPTools_1_1SplitFeatures.html#adcc81c011af1fa7bdbbbafc9c4ce3e47) (name, mode, transaction=True)  
def | [cmdCreateXORFeature](../../d7/de4/namespaceBOPTools_1_1SplitFeatures.html#a8dcec98a9235fefb05db9a09b58627e9) (name)  
def | [cmdSliceApart](../../d7/de4/namespaceBOPTools_1_1SplitFeatures.html#ac38ef321c49e5a920daf20b6614cdf7a) ()  
def | [getIconPath](../../d7/de4/namespaceBOPTools_1_1SplitFeatures.html#a8414fc6d96bf4b7e5b6d9524b002ae03) (icon_dot_svg)  
def | [makeBooleanFragments](../../d7/de4/namespaceBOPTools_1_1SplitFeatures.html#af9ed6877092255f3e541654472a6f0b3) (name)  
def | [makeSlice](../../d7/de4/namespaceBOPTools_1_1SplitFeatures.html#a1854ddd59d07b87e5fccdebd2bd05991) (name)  
def | [makeXOR](../../d7/de4/namespaceBOPTools_1_1SplitFeatures.html#a337717b0203812b3d7d9bd0e4f7751f7) (name)  
  
##  Variables  
  
---  
|
[translate](../../d7/de4/namespaceBOPTools_1_1SplitFeatures.html#a7f2babde11f2a036cc0ce5fcf4039b6b)
= FreeCAD.Qt.translate  
  
## Function Documentation

## ◆ addCommands()

def BOPTools.SplitFeatures.addCommands  | ( | | ) |   
---|---|---|---|---  
  
## ◆ cmdCreateBooleanFragmentsFeature()

def BOPTools.SplitFeatures.cmdCreateBooleanFragmentsFeature  | ( |  | _name_ ,   
---|---|---|---  
|  |  | _mode_  
| ) | |   
      
    
    cmdCreateBooleanFragmentsFeature(name, mode): implementation of GUI command to create
    BooleanFragments feature (GFA). Mode can be "Standard", "Split", or "CompSolid".

Referenced by
[BOPTools.SplitFeatures.CommandBooleanFragments.Activated()](../../d3/d93/classBOPTools_1_1SplitFeatures_1_1CommandBooleanFragments.html#a7b9e5d1014ca80db52c61ec1d7b566fe).

## ◆ cmdCreateSliceFeature()

def BOPTools.SplitFeatures.cmdCreateSliceFeature  | ( |  | _name_ ,   
---|---|---|---  
|  |  | _mode_ ,   
|  |  | _transaction_ = `True`  
| ) | |   
      
    
    cmdCreateSliceFeature(name, mode): implementation of GUI command to create
    Slice feature. Mode can be "Standard", "Split", or "CompSolid".

Referenced by
[BOPTools.SplitFeatures.CommandSlice.Activated()](../../d5/d56/classBOPTools_1_1SplitFeatures_1_1CommandSlice.html#ac38f0353cffad07b63ce820b45db249a),
and
[BOPTools.SplitFeatures.cmdSliceApart()](../../d7/de4/namespaceBOPTools_1_1SplitFeatures.html#ac38ef321c49e5a920daf20b6614cdf7a).

## ◆ cmdCreateXORFeature()

def BOPTools.SplitFeatures.cmdCreateXORFeature  | ( |  | _name_| ) |   
---|---|---|---|---|---  
      
    
    cmdCreateXORFeature(name): implementation of GUI command to create
    XOR feature (GFA). Mode can be "Standard", "Split", or "CompSolid".

Referenced by
[BOPTools.SplitFeatures.CommandXOR.Activated()](../../d1/d26/classBOPTools_1_1SplitFeatures_1_1CommandXOR.html#a20490f5a8071e5d3a140a6bc5f9c265e).

## ◆ cmdSliceApart()

def BOPTools.SplitFeatures.cmdSliceApart  | ( | | ) |   
---|---|---|---|---  
  
References
[BOPTools.SplitFeatures.cmdCreateSliceFeature()](../../d7/de4/namespaceBOPTools_1_1SplitFeatures.html#adcc81c011af1fa7bdbbbafc9c4ce3e47).

Referenced by
[BOPTools.SplitFeatures.CommandSliceApart.Activated()](../../d2/db2/classBOPTools_1_1SplitFeatures_1_1CommandSliceApart.html#a9fdd049797563a8aebd3a940b3d8f968).

## ◆ getIconPath()

def BOPTools.SplitFeatures.getIconPath  | ( |  | _icon_dot_svg_| ) |   
---|---|---|---|---|---  
  
Referenced by
[BOPTools.SplitFeatures.ViewProviderBooleanFragments.getIcon()](../../d0/d5a/classBOPTools_1_1SplitFeatures_1_1ViewProviderBooleanFragments.html#a6d64e19af6e69559355702c85693901a),
[BOPTools.SplitFeatures.ViewProviderSlice.getIcon()](../../d5/d19/classBOPTools_1_1SplitFeatures_1_1ViewProviderSlice.html#af38f34dc51a1d7ad35d7254a0bb74f5b),
[BOPTools.SplitFeatures.ViewProviderXOR.getIcon()](../../d9/de4/classBOPTools_1_1SplitFeatures_1_1ViewProviderXOR.html#a702f5dd1df55d22685d0b81f289516be),
[BOPTools.SplitFeatures.CommandBooleanFragments.GetResources()](../../d3/d93/classBOPTools_1_1SplitFeatures_1_1CommandBooleanFragments.html#a5c80cd30b4fcaaf5495950f7bb8c148b),
[BOPTools.SplitFeatures.CommandSlice.GetResources()](../../d5/d56/classBOPTools_1_1SplitFeatures_1_1CommandSlice.html#af40cf3948a1be7b70fefe5c0188c7fa3),
[BOPTools.SplitFeatures.CommandSliceApart.GetResources()](../../d2/db2/classBOPTools_1_1SplitFeatures_1_1CommandSliceApart.html#a938e8fe82ab851281db1b021d428970a),
and
[BOPTools.SplitFeatures.CommandXOR.GetResources()](../../d1/d26/classBOPTools_1_1SplitFeatures_1_1CommandXOR.html#a968e17ef20eec48954455ce5611b94aa).

## ◆ makeBooleanFragments()

def BOPTools.SplitFeatures.makeBooleanFragments  | ( |  | _name_| ) |   
---|---|---|---|---|---  
      
    
    makeBooleanFragments(name): makes an BooleanFragments object.

Referenced by
[femexamples.material_multiple_bendingbeam_fiveboxes.setup()](../../d6/d5c/namespacefemexamples_1_1material__multiple__bendingbeam__fiveboxes.html#a15478012e500a6a2f78cb4ec336e406e).

## ◆ makeSlice()

def BOPTools.SplitFeatures.makeSlice  | ( |  | _name_| ) |   
---|---|---|---|---|---  
      
    
    makeSlice(name): makes an Slice object.

## ◆ makeXOR()

def BOPTools.SplitFeatures.makeXOR  | ( |  | _name_| ) |   
---|---|---|---|---|---  
      
    
    makeXOR(name): makes an XOR object.

## Variable Documentation

## ◆ translate

BOPTools.SplitFeatures.translate = FreeCAD.Qt.translate  
---  
  
* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

