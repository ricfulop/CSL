---
url: https://freecad.github.io/SourceDoc/d8/d56/classAdaptivePath_1_1ClearedArea.html
scraped_at: 2025-09-08T14:52:42.966060
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [AdaptivePath](../../d5/d7f/namespaceAdaptivePath.html)
  * [ClearedArea](../../d8/d56/classAdaptivePath_1_1ClearedArea.html)

[List of all members](../../d7/df4/classAdaptivePath_1_1ClearedArea-members.html) | Public Member Functions

AdaptivePath::ClearedArea Class Reference

##  Public Member Functions  
  
---  
|
[ClearedArea](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#ad3516887d709c56b2b5346f5d5af5367)
([ClipperLib::cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa)
p_toolRadiusScaled)  
void | [ExpandCleared](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a880cf981ced9aa6c2021bee6d35fc58b) (const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) toClearToolPath)  
[Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | [GetBoundedClearedAreaClipped](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a396af78fc129b33fe0c3730caadc9503) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &toolPos)  
[Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | [GetBoundedClearedPaths](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a68e1a211be4683c860dba6ec244abc36) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &toolPos)  
[Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | [GetCleared](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a55ba28ab385ec21a770918a7456b6c7c) ()  
void | [SetClearedPaths](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a29ac020e07bb8d1907fd015b287ff774) (const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &paths)  
  
## Constructor & Destructor Documentation

## ◆ ClearedArea()

AdaptivePath::ClearedArea::ClearedArea  | ( | [ClipperLib::cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) | _p_toolRadiusScaled_| ) |   
---|---|---|---|---|---  
  
## Member Function Documentation

## ◆ ExpandCleared()

void AdaptivePath::ClearedArea::ExpandCleared  | ( | const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) | _toClearToolPath_| ) |   
---|---|---|---|---|---  
  
References
[ClipperLib::ClipperOffset::AddPath()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a0cd68e3690072f510924a5b25291043b),
[ClipperLib::ClipperBase::AddPaths()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a2395967b47fb9f3f5846e2bf56c18f67),
[ClipperLib::CleanPolygons()](../../df/db2/namespaceClipperLib.html#a770cbc6ce4f16d02b8fe27c5abf6159c),
[ClipperLib::ClipperBase::Clear()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a5690952fe8c2cb047025566405827821),
[ClipperLib::ClipperOffset::Clear()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#ab444433587b6a3f6c89655938d889c7d),
[ClipperLib::Clipper::Execute()](../../d3/d1b/classClipperLib_1_1Clipper.html#a06da196a4b4151edd2e5426ed48744cf),
[ClipperLib::ClipperOffset::Execute()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#ac591b25e483a52c99c3190a256ad4589),
[AdaptivePath::Perf_ExpandCleared](../../d5/d7f/namespaceAdaptivePath.html#a50017e1cb8671a90d2a954c13b84aa49),
[AdaptivePath::PerfCounter::Start()](../../d2/d12/classAdaptivePath_1_1PerfCounter.html#a3020c4d3d1de9df1f3c201e39535978b),
and
[AdaptivePath::PerfCounter::Stop()](../../d2/d12/classAdaptivePath_1_1PerfCounter.html#ac161c5f0c9f2ff34315994274e151cf0).

## ◆ GetBoundedClearedAreaClipped()

[Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & AdaptivePath::ClearedArea::GetBoundedClearedAreaClipped  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _toolPos_| ) |   
---|---|---|---|---|---  
  
References
[ClipperLib::ClipperBase::AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba),
[ClipperLib::ClipperBase::AddPaths()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a2395967b47fb9f3f5846e2bf56c18f67),
[AdaptivePath::BoundBox::AddPoint()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a47b23bb75413d049f127728ad178ea76),
[ClipperLib::ClipperBase::Clear()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a5690952fe8c2cb047025566405827821),
[AdaptivePath::BoundBox::Contains()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#af72c43f46ec868065be57cebd1bc1f85),
[ClipperLib::Clipper::Execute()](../../d3/d1b/classClipperLib_1_1Clipper.html#a06da196a4b4151edd2e5426ed48744cf),
[AdaptivePath::BoundBox::SetFirstPoint()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a33a37a0cdf8b16dbd473f595ba0984eb),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

## ◆ GetBoundedClearedPaths()

[Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & AdaptivePath::ClearedArea::GetBoundedClearedPaths  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _toolPos_| ) |   
---|---|---|---|---|---  
  
References
[AdaptivePath::BoundBox::AddPoint()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a47b23bb75413d049f127728ad178ea76),
[AdaptivePath::BoundBox::CollidesWith()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a2bbbd18bf8af744a2b9fd7a8f67409ea),
[AdaptivePath::BoundBox::Contains()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#af72c43f46ec868065be57cebd1bc1f85),
[AdaptivePath::BoundBox::SetFirstPoint()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a33a37a0cdf8b16dbd473f595ba0984eb),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

## ◆ GetCleared()

[Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & AdaptivePath::ClearedArea::GetCleared  | ( | | ) |   
---|---|---|---|---  
  
## ◆ SetClearedPaths()

void AdaptivePath::ClearedArea::SetClearedPaths  | ( | const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _paths_| ) |   
---|---|---|---|---|---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Path/libarea/Adaptive.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

