---
url: https://freecad.github.io/SourceDoc/d0/d13/namespaceBOPTools_1_1JoinFeatures.html
scraped_at: 2025-09-08T15:18:35.404167
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [BOPTools](../../dc/dff/namespaceBOPTools.html)
  * [JoinFeatures](../../d0/d13/namespaceBOPTools_1_1JoinFeatures.html)

Classes | Functions | Variables

BOPTools.JoinFeatures Namespace Reference

##  Classes  
  
---  
class | [CommandConnect](../../d7/d5c/classBOPTools_1_1JoinFeatures_1_1CommandConnect.html)  
class | [CommandCutout](../../d9/d9e/classBOPTools_1_1JoinFeatures_1_1CommandCutout.html)  
class | [CommandEmbed](../../d2/d0c/classBOPTools_1_1JoinFeatures_1_1CommandEmbed.html)  
class | [FeatureConnect](../../d0/d85/classBOPTools_1_1JoinFeatures_1_1FeatureConnect.html)  
class | [FeatureCutout](../../da/d9a/classBOPTools_1_1JoinFeatures_1_1FeatureCutout.html)  
class | [FeatureEmbed](../../d7/d55/classBOPTools_1_1JoinFeatures_1_1FeatureEmbed.html)  
class | [ViewProviderConnect](../../da/d91/classBOPTools_1_1JoinFeatures_1_1ViewProviderConnect.html)  
class | [ViewProviderCutout](../../d4/d85/classBOPTools_1_1JoinFeatures_1_1ViewProviderCutout.html)  
class | [ViewProviderEmbed](../../dc/d41/classBOPTools_1_1JoinFeatures_1_1ViewProviderEmbed.html)  
  
##  Functions  
  
---  
def | [addCommands](../../d0/d13/namespaceBOPTools_1_1JoinFeatures.html#a8ffc48857227d6e07cbde82fea3d815b) ()  
def | [cmdCreateJoinFeature](../../d0/d13/namespaceBOPTools_1_1JoinFeatures.html#a08937c6e37282c0fc7df9da9b6496bab) (name, mode)  
def | [getIconPath](../../d0/d13/namespaceBOPTools_1_1JoinFeatures.html#a5629f5ef8376a3b2aad2d385f35b73b0) (icon_dot_svg)  
def | [getParamRefine](../../d0/d13/namespaceBOPTools_1_1JoinFeatures.html#a4fe268a983e5076eb67d2434d3063675) ()  
def | [makeConnect](../../d0/d13/namespaceBOPTools_1_1JoinFeatures.html#a25256a04d5f449ec6bd02d9003d7c21e) (name)  
def | [makeCutout](../../d0/d13/namespaceBOPTools_1_1JoinFeatures.html#ac23bff264ca587a80a4cfb7b321173ee) (name)  
def | [makeEmbed](../../d0/d13/namespaceBOPTools_1_1JoinFeatures.html#ac9be69f02fbaa714587216ff8468fee3) (name)  
  
##  Variables  
  
---  
|
[translate](../../d0/d13/namespaceBOPTools_1_1JoinFeatures.html#a5384e702df6e1d8e058a739d0748b35c)
= FreeCAD.Qt.translate  
  
## Function Documentation

## ◆ addCommands()

def BOPTools.JoinFeatures.addCommands  | ( | | ) |   
---|---|---|---|---  
  
## ◆ cmdCreateJoinFeature()

def BOPTools.JoinFeatures.cmdCreateJoinFeature  | ( |  | _name_ ,   
---|---|---|---  
|  |  | _mode_  
| ) | |   
      
    
    cmdCreateJoinFeature(name, mode): generalized implementation of GUI commands.

Referenced by
[BOPTools.JoinFeatures.CommandConnect.Activated()](../../d7/d5c/classBOPTools_1_1JoinFeatures_1_1CommandConnect.html#a3f7cda1bd19bf036f0fbcb99ed9a4c5b),
[BOPTools.JoinFeatures.CommandEmbed.Activated()](../../d2/d0c/classBOPTools_1_1JoinFeatures_1_1CommandEmbed.html#a8aeb75010c460d69f39512df8f88e5d8),
and
[BOPTools.JoinFeatures.CommandCutout.Activated()](../../d9/d9e/classBOPTools_1_1JoinFeatures_1_1CommandCutout.html#aea70bc7aa6ac82465e976f3dafbbc8f6).

## ◆ getIconPath()

def BOPTools.JoinFeatures.getIconPath  | ( |  | _icon_dot_svg_| ) |   
---|---|---|---|---|---  
  
Referenced by
[BOPTools.JoinFeatures.ViewProviderConnect.getIcon()](../../da/d91/classBOPTools_1_1JoinFeatures_1_1ViewProviderConnect.html#a52cbaa5908235b8edd5ccb358148912b),
[BOPTools.JoinFeatures.ViewProviderEmbed.getIcon()](../../dc/d41/classBOPTools_1_1JoinFeatures_1_1ViewProviderEmbed.html#a60fabba8b73fb37ec9bafd232ac4481a),
[BOPTools.JoinFeatures.ViewProviderCutout.getIcon()](../../d4/d85/classBOPTools_1_1JoinFeatures_1_1ViewProviderCutout.html#a38d62fe72d500807e304d93430afda80),
[BOPTools.JoinFeatures.CommandConnect.GetResources()](../../d7/d5c/classBOPTools_1_1JoinFeatures_1_1CommandConnect.html#ac3cc820d3b77973a45022f9283213a73),
[BOPTools.JoinFeatures.CommandEmbed.GetResources()](../../d2/d0c/classBOPTools_1_1JoinFeatures_1_1CommandEmbed.html#a61c70fbf424cb5d8c8ea3147d32a5ee1),
and
[BOPTools.JoinFeatures.CommandCutout.GetResources()](../../d9/d9e/classBOPTools_1_1JoinFeatures_1_1CommandCutout.html#a0090302f07d8a72ccabb13b618e91f65).

## ◆ getParamRefine()

def BOPTools.JoinFeatures.getParamRefine  | ( | | ) |   
---|---|---|---|---  
  
## ◆ makeConnect()

def BOPTools.JoinFeatures.makeConnect  | ( |  | _name_| ) |   
---|---|---|---|---|---  
      
    
    makeConnect(name): makes an Connect object.

## ◆ makeCutout()

def BOPTools.JoinFeatures.makeCutout  | ( |  | _name_| ) |   
---|---|---|---|---|---  
      
    
    makeCutout(name): makes an Cutout object.

## ◆ makeEmbed()

def BOPTools.JoinFeatures.makeEmbed  | ( |  | _name_| ) |   
---|---|---|---|---|---  
      
    
    makeEmbed(name): makes an Embed object.

## Variable Documentation

## ◆ translate

BOPTools.JoinFeatures.translate = FreeCAD.Qt.translate  
---  
  
* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

