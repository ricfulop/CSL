---
url: https://freecad.github.io/SourceDoc/de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html
scraped_at: 2025-09-08T14:55:43.728008
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html)
  * [ExpressionInfo](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html)

[List of all members](../../dc/daf/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo-members.html) | Public Member Functions | Public Attributes

App::PropertyExpressionEngine::ExpressionInfo Struct Reference

The
[ExpressionInfo](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html
"The ExpressionInfo struct encapsulates an expression.") struct encapsulates
an expression.
[More...](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html#details)

`#include <PropertyExpressionEngine.h>`

##  Public Member Functions  
  
---  
|
[ExpressionInfo](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html#a54b62db7b5b3bc1580b334b7409e1c29)
(const
[ExpressionInfo](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html)
&other)  
|
[ExpressionInfo](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html#ae01c292012c70f0b403f63324f52aa09)
(std::shared_ptr< [App::Expression](../../dc/d5c/classApp_1_1Expression.html)
>
[expression](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html#a075a8abc40defe9210a28b6699932fcd)=std::shared_ptr<
[App::Expression](../../dc/d5c/classApp_1_1Expression.html) >())  
[ExpressionInfo](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html) & | [operator=](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html#aa7fd1bdbeff0813403cbe9f99b45b838) (const [ExpressionInfo](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html) &other)  
  
##  Public Attributes  
  
---  
[bool](../../d9/db9/classbool.html) | [busy](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html#ac9f2ec699cfdfca1351c4f9ced6c0f96)  
std::shared_ptr< [App::Expression](../../dc/d5c/classApp_1_1Expression.html) > | [expression](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html#a075a8abc40defe9210a28b6699932fcd)  
| The actual expression tree.
[More...](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html#a075a8abc40defe9210a28b6699932fcd)  
  
  
## Detailed Description

The
[ExpressionInfo](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html
"The ExpressionInfo struct encapsulates an expression.") struct encapsulates
an expression.

## Constructor & Destructor Documentation

## ◆ ExpressionInfo() [1/2]

App::PropertyExpressionEngine::ExpressionInfo::ExpressionInfo  | ( | std::shared_ptr< [App::Expression](../../dc/d5c/classApp_1_1Expression.html) > | _expression_ = `std::shared_ptr<[App::Expression](../../dc/d5c/classApp_1_1Expression.html)>()`| ) |   
---|---|---|---|---|---  
  
## ◆ ExpressionInfo() [2/2]

App::PropertyExpressionEngine::ExpressionInfo::ExpressionInfo  | ( | const [ExpressionInfo](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html) & | _other_| ) |   
---|---|---|---|---|---  
  
References
[busy](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html#ac9f2ec699cfdfca1351c4f9ced6c0f96),
and
[expression](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html#a075a8abc40defe9210a28b6699932fcd).

## Member Function Documentation

## ◆ operator=()

[ExpressionInfo](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html) & App::PropertyExpressionEngine::ExpressionInfo::operator=  | ( | const [ExpressionInfo](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html) & | _other_| ) |   
---|---|---|---|---|---  
  
References
[busy](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html#ac9f2ec699cfdfca1351c4f9ced6c0f96),
and
[expression](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html#a075a8abc40defe9210a28b6699932fcd).

## Member Data Documentation

## ◆ busy

[bool](../../d9/db9/classbool.html)
App::PropertyExpressionEngine::ExpressionInfo::busy  
---  
  
Referenced by
[ExpressionInfo()](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html#a54b62db7b5b3bc1580b334b7409e1c29),
[operator=()](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html#aa7fd1bdbeff0813403cbe9f99b45b838),
[PathScripts.PathSimulatorGui.PathSimulation::PerformCutBoolean()](../../da/dfe/classPathScripts_1_1PathSimulatorGui_1_1PathSimulation.html#a7ff40dcd89340386443559a651d14b4e),
and
[PathScripts.PathSimulatorGui.PathSimulation::PerformCutVoxel()](../../da/dfe/classPathScripts_1_1PathSimulatorGui_1_1PathSimulation.html#a318c1a5a78add9f8c1af035b1913849f).

## ◆ expression

std::shared_ptr<[App::Expression](../../dc/d5c/classApp_1_1Expression.html)>
App::PropertyExpressionEngine::ExpressionInfo::expression  
---  
  
The actual expression tree.

Referenced by
[Sketcher::SketchObject::addCopyOfConstraints()](../../d9/dad/classSketcher_1_1SketchObject.html#ae855d43b68feffdb57a0489777e2b9ad),
[Sketcher::SketchObject::constraintHasExpression()](../../d9/dad/classSketcher_1_1SketchObject.html#a13d7d959fe45ea0b1f80b11a8337c492),
[ConstraintItem::data()](../../d3/d0f/classConstraintItem.html#a58e0ecc1824934b77e25bc0b319b6c51),
[ExpressionInfo()](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html#a54b62db7b5b3bc1580b334b7409e1c29),
[Gui::ExpressionBinding::getExpression()](../../dc/d5a/classGui_1_1ExpressionBinding.html#a2af16f7694ca1c7c0465a31eddf195d5),
[operator=()](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html#aa7fd1bdbeff0813403cbe9f99b45b838),
and
[ExpressionDelegate::paint()](../../d1/df5/classExpressionDelegate.html#ae8f09045fee240444d9d5383c8d23d0e).

* * *

The documentation for this struct was generated from the following file:

  * FreeCAD/src/App/PropertyExpressionEngine.h

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

