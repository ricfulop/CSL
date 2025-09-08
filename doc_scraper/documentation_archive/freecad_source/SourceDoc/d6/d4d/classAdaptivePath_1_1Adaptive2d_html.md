---
url: https://freecad.github.io/SourceDoc/d6/d4d/classAdaptivePath_1_1Adaptive2d.html
scraped_at: 2025-09-08T14:52:39.982411
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [AdaptivePath](../../d5/d7f/namespaceAdaptivePath.html)
  * [Adaptive2d](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html)

[List of all members](../../d9/d0b/classAdaptivePath_1_1Adaptive2d-members.html) | Public Member Functions | Public Attributes | Friends

AdaptivePath::Adaptive2d Class Reference

`#include <Adaptive.hpp>`

##  Public Member Functions  
  
---  
|
[Adaptive2d](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a70b8318ba5befa8d0ce061cbb5054724)
()  
std::list< [AdaptiveOutput](../../d4/de0/structAdaptivePath_1_1AdaptiveOutput.html) > | [Execute](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071) (const [DPaths](../../d5/d7f/namespaceAdaptivePath.html#a3e730733009ac85e2afe8df986221df6) &stockPaths, const [DPaths](../../d5/d7f/namespaceAdaptivePath.html#a3e730733009ac85e2afe8df986221df6) &paths, std::function< [bool](../../d9/db9/classbool.html)([TPaths](../../d5/d7f/namespaceAdaptivePath.html#a111e8ff22b4a96deb14103b0ca204475))> progressCallbackFn)  
  
##  Public Attributes  
  
---  
[bool](../../d9/db9/classbool.html) | [finishingProfile](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a78b4772cbc754d4013949f43d91b9039) = true  
[bool](../../d9/db9/classbool.html) | [forceInsideOut](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#ad9c5c41f527fbb706ac5755f1c4b4175) = true  
double | [helixRampDiameter](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#ae8f7cacc79144f4cfe72e5c0bd92acd6) = 0  
double | [keepToolDownDistRatio](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#aea4a0f808982d9fa101adac1871bd486) = 3.0  
[OperationType](../../d5/d7f/namespaceAdaptivePath.html#ae84b50235dbf1d89c136982756c1bb74) | [opType](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#ac758f66ae9c9d67f9ffc18310ca439b3) = OperationType::otClearingInside  
double | [stepOverFactor](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a7bea39e4b21bebffd3b12708ce756259) = 0.2  
double | [stockToLeave](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a76efc9527ec77f3c765b229f6fc89fbd) = 0  
double | [tolerance](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a214f3aed173dfb012c9be4ac363c24ca) = 0.1  
double | [toolDiameter](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#ae3c8aeddc4051f14b99c34170f58dcce) = 5  
  
##  Friends  
  
---  
class | [EngagePoint](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a8ccf9549c8622d97eba8ad4f5faf0697)  
  
## Constructor & Destructor Documentation

## ◆ Adaptive2d()

AdaptivePath::Adaptive2d::Adaptive2d  | ( | | ) |   
---|---|---|---|---  
  
## Member Function Documentation

## ◆ Execute()

std::list< [AdaptiveOutput](../../d4/de0/structAdaptivePath_1_1AdaptiveOutput.html) > AdaptivePath::Adaptive2d::Execute  | ( | const [DPaths](../../d5/d7f/namespaceAdaptivePath.html#a3e730733009ac85e2afe8df986221df6) & | _stockPaths_ ,   
---|---|---|---  
|  | const [DPaths](../../d5/d7f/namespaceAdaptivePath.html#a3e730733009ac85e2afe8df986221df6) & | _paths_ ,   
|  | std::function< [bool](../../d9/db9/classbool.html)([TPaths](../../d5/d7f/namespaceAdaptivePath.html#a111e8ff22b4a96deb14103b0ca204475))> | _progressCallbackFn_  
| ) | |   
  
tool bounds

offset back outwards - corner rounding

References
[ClipperLib::ClipperOffset::AddPath()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a0cd68e3690072f510924a5b25291043b),
[ClipperLib::ClipperBase::AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba),
[ClipperLib::ClipperOffset::AddPaths()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a18b35198f6370d76885af995ee2f16cb),
[ClipperLib::ClipperBase::AddPaths()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a2395967b47fb9f3f5846e2bf56c18f67),
[AdaptivePath::appendDirectChildPaths()](../../d5/d7f/namespaceAdaptivePath.html#ae4de2e0c14dadfa4dd7c25b581fdb8ea),
[AdaptivePath::CleanPath()](../../d5/d7f/namespaceAdaptivePath.html#aead96b0a2dabc04e6fc87c735b7158c4),
[ClipperLib::ClipperBase::Clear()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a5690952fe8c2cb047025566405827821),
[ClipperLib::ClipperOffset::Clear()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#ab444433587b6a3f6c89655938d889c7d),
[AdaptivePath::ConnectPaths()](../../d5/d7f/namespaceAdaptivePath.html#a26e83a95426b4f1c05b3eb98b4a04a17),
[AdaptivePath::DeduplicatePaths()](../../d5/d7f/namespaceAdaptivePath.html#a37e54774ebe2ecb52e17897441349d53),
[ClipperLib::Clipper::Execute()](../../d3/d1b/classClipperLib_1_1Clipper.html#a06da196a4b4151edd2e5426ed48744cf),
[ClipperLib::ClipperOffset::Execute()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#ac591b25e483a52c99c3190a256ad4589),
[finishingProfile](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a78b4772cbc754d4013949f43d91b9039),
[forceInsideOut](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#ad9c5c41f527fbb706ac5755f1c4b4175),
[AdaptivePath::getPathNestingLevel()](../../d5/d7f/namespaceAdaptivePath.html#afe6b9d42c4e97db975f5acf577006f18),
[helixRampDiameter](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#ae8f7cacc79144f4cfe72e5c0bd92acd6),
[draftfunctions.offset::offset()](../../d2/d57/group__draftfunctions.html#ga15bf04dc2feebf4fe453ff6b9a3a7492),
[opType](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#ac758f66ae9c9d67f9ffc18310ca439b3),
[ClipperLib::ReversePaths()](../../df/db2/namespaceClipperLib.html#ade103cad7caf2aa357b2d5410866ea62),
[ClipperLib::SimplifyPolygons()](../../df/db2/namespaceClipperLib.html#ac9ebbe437e4c08816bffeced6d001cf6),
[stepOverFactor](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a7bea39e4b21bebffd3b12708ce756259),
[stockToLeave](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a76efc9527ec77f3c765b229f6fc89fbd),
[tolerance](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a214f3aed173dfb012c9be4ac363c24ca),
[toolDiameter](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#ae3c8aeddc4051f14b99c34170f58dcce),
and
[ClipperLib::TranslatePath()](../../df/db2/namespaceClipperLib.html#a3c34a4a0ea91a10f729e5ceb6cc33714).

Referenced by
[PathScripts.PathJobCmd.CommandJobCreate::Activated()](../../db/d17/classPathScripts_1_1PathJobCmd_1_1CommandJobCreate.html#aac9d774ebbcda6c9840a1b776045fd2f),
and
[PathScripts.PathJobCmd.CommandJobTemplateExport::SaveDialog()](../../d7/d23/classPathScripts_1_1PathJobCmd_1_1CommandJobTemplateExport.html#a208b7ff58f9cc81651d8ae05fe9c44af).

## Friends And Related Function Documentation

## ◆ EngagePoint

| [friend](../../d7/d23/classfriend.html) class
[EngagePoint](../../de/d69/classAdaptivePath_1_1EngagePoint.html)  
---  
friend  
  
## Member Data Documentation

## ◆ finishingProfile

[bool](../../d9/db9/classbool.html) AdaptivePath::Adaptive2d::finishingProfile
= true  
---  
  
Referenced by
[Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071).

## ◆ forceInsideOut

[bool](../../d9/db9/classbool.html) AdaptivePath::Adaptive2d::forceInsideOut =
true  
---  
  
Referenced by
[Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071).

## ◆ helixRampDiameter

double AdaptivePath::Adaptive2d::helixRampDiameter = 0  
---  
  
Referenced by
[Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071).

## ◆ keepToolDownDistRatio

double AdaptivePath::Adaptive2d::keepToolDownDistRatio = 3.0  
---  
  
## ◆ opType

[OperationType](../../d5/d7f/namespaceAdaptivePath.html#ae84b50235dbf1d89c136982756c1bb74)
AdaptivePath::Adaptive2d::opType = OperationType::otClearingInside  
---  
  
Referenced by
[Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071).

## ◆ stepOverFactor

double AdaptivePath::Adaptive2d::stepOverFactor = 0.2  
---  
  
Referenced by
[Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071).

## ◆ stockToLeave

double AdaptivePath::Adaptive2d::stockToLeave = 0  
---  
  
Referenced by
[Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071).

## ◆ tolerance

double AdaptivePath::Adaptive2d::tolerance = 0.1  
---  
  
Referenced by
[femtaskpanels.task_constraint_tie._TaskPanel::accept()](../../d3/dcb/classfemtaskpanels_1_1task__constraint__tie_1_1__TaskPanel.html#a8e36b821a4bb2bd9c4d12117af84d1c9),
[Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071),
and
[femtaskpanels.task_constraint_tie._TaskPanel::tolerance_changed()](../../d3/dcb/classfemtaskpanels_1_1task__constraint__tie_1_1__TaskPanel.html#a043ed9d0943e66cbbd5f5ee727d5a9a2).

## ◆ toolDiameter

double AdaptivePath::Adaptive2d::toolDiameter = 5  
---  
  
Referenced by
[Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Mod/Path/libarea/Adaptive.hpp
  * FreeCAD/src/Mod/Path/libarea/Adaptive.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

