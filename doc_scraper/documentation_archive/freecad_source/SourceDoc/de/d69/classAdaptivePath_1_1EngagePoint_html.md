---
url: https://freecad.github.io/SourceDoc/de/d69/classAdaptivePath_1_1EngagePoint.html
scraped_at: 2025-09-08T14:52:44.021888
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [AdaptivePath](../../d5/d7f/namespaceAdaptivePath.html)
  * [EngagePoint](../../de/d69/classAdaptivePath_1_1EngagePoint.html)

[List of all members](../../d0/d77/classAdaptivePath_1_1EngagePoint-members.html) | Classes | Public Member Functions

AdaptivePath::EngagePoint Class Reference

##  Classes  
  
---  
struct | [EngageState](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html)  
  
##  Public Member Functions  
  
---  
|
[EngagePoint](../../de/d69/classAdaptivePath_1_1EngagePoint.html#afec128c665fb4145754c7c13abb13830)
(const
[Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe)
&p_toolBoundPaths)  
[DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) | [getCurrentDir](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a64238fcdbfa9f4bf6a2fc4f000405339) ()  
[IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | [getCurrentPoint](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a4a25dac76882d1527f13a9f4683024a2) ()  
[EngageState](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html) | [GetState](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a01d6adfac87d21f56374b968d109bf6b) ()  
[bool](../../d9/db9/classbool.html) | [moveForward](../../de/d69/classAdaptivePath_1_1EngagePoint.html#aff2059280bef1a583fca8a367e3df635) (double distance)  
void | [moveToClosestPoint](../../de/d69/classAdaptivePath_1_1EngagePoint.html#ab82d771a0d521b9b13fb15f6373df310) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt, double step)  
[bool](../../d9/db9/classbool.html) | [nextEngagePoint](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a853203bca004d7d69e68fed5a17e049f) ([Adaptive2d](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html) *parent, [ClearedArea](../../d8/d56/classAdaptivePath_1_1ClearedArea.html) &clearedArea, double step, double minCutArea, double maxCutArea, [int](../../d1/da0/classint.html) maxPases=2)  
[bool](../../d9/db9/classbool.html) | [nextPath](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a90133cef784e83a9b00801ecfa422d58) ()  
void | [ResetPasses](../../de/d69/classAdaptivePath_1_1EngagePoint.html#ad565edb37f2b1dc8c578328a599e0a1a) ()  
void | [SetPaths](../../de/d69/classAdaptivePath_1_1EngagePoint.html#ac21717234f26373f886055b60990717d) (const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &paths)  
void | [SetState](../../de/d69/classAdaptivePath_1_1EngagePoint.html#afdcef328ed326ee5f428c7f621735ca9) (const [EngageState](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html) &new_state)  
  
## Constructor & Destructor Documentation

## ◆ EngagePoint()

AdaptivePath::EngagePoint::EngagePoint  | ( | const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _p_toolBoundPaths_| ) |   
---|---|---|---|---|---  
  
References
[AdaptivePath::EngagePoint::EngageState::currentPathIndex](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#ab4cc9cf8cf2182c0562e1c57c757490b),
[AdaptivePath::EngagePoint::EngageState::currentSegmentIndex](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#aff954ac11fd189fb0a6c62a374d4eae3),
[AdaptivePath::EngagePoint::EngageState::segmentPos](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#a7df9f25695deaa7ac699e53393222e66),
[SetPaths()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#ac21717234f26373f886055b60990717d),
and
[AdaptivePath::EngagePoint::EngageState::totalDistance](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#a89d9791d4a09751734117ad9ad82e22a).

## Member Function Documentation

## ◆ getCurrentDir()

[DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) AdaptivePath::EngagePoint::getCurrentDir  | ( | | ) |   
---|---|---|---|---  
  
References
[AdaptivePath::EngagePoint::EngageState::currentPathIndex](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#ab4cc9cf8cf2182c0562e1c57c757490b),
[AdaptivePath::EngagePoint::EngageState::currentSegmentIndex](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#aff954ac11fd189fb0a6c62a374d4eae3),
[AdaptivePath::DistanceSqrd()](../../d5/d7f/namespaceAdaptivePath.html#a8ba2907627cf52f54a10caa7ffbe4ac1),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

## ◆ getCurrentPoint()

[IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) AdaptivePath::EngagePoint::getCurrentPoint  | ( | | ) |   
---|---|---|---|---  
  
References
[AdaptivePath::EngagePoint::EngageState::currentPathIndex](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#ab4cc9cf8cf2182c0562e1c57c757490b),
[AdaptivePath::EngagePoint::EngageState::currentSegmentIndex](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#aff954ac11fd189fb0a6c62a374d4eae3),
[AdaptivePath::DistanceSqrd()](../../d5/d7f/namespaceAdaptivePath.html#a8ba2907627cf52f54a10caa7ffbe4ac1),
[AdaptivePath::EngagePoint::EngageState::segmentPos](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#a7df9f25695deaa7ac699e53393222e66),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

Referenced by
[moveToClosestPoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#ab82d771a0d521b9b13fb15f6373df310),
and
[nextEngagePoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a853203bca004d7d69e68fed5a17e049f).

## ◆ GetState()

[EngageState](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html) AdaptivePath::EngagePoint::GetState  | ( | | ) |   
---|---|---|---|---  
  
## ◆ moveForward()

[bool](../../d9/db9/classbool.html) AdaptivePath::EngagePoint::moveForward  | ( | double  | _distance_| ) |   
---|---|---|---|---|---  
  
References
[AdaptivePath::EngagePoint::EngageState::currentPathIndex](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#ab4cc9cf8cf2182c0562e1c57c757490b),
[AdaptivePath::EngagePoint::EngageState::currentPathLength](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#afbe85d9f53105445d0c305dab4ca4064),
[AdaptivePath::EngagePoint::EngageState::currentSegmentIndex](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#aff954ac11fd189fb0a6c62a374d4eae3),
[AdaptivePath::EngagePoint::EngageState::segmentPos](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#a7df9f25695deaa7ac699e53393222e66),
and
[AdaptivePath::EngagePoint::EngageState::totalDistance](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#a89d9791d4a09751734117ad9ad82e22a).

Referenced by
[moveToClosestPoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#ab82d771a0d521b9b13fb15f6373df310),
and
[nextEngagePoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a853203bca004d7d69e68fed5a17e049f).

## ◆ moveToClosestPoint()

void AdaptivePath::EngagePoint::moveToClosestPoint  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt_ ,   
---|---|---|---  
|  | double  | _step_  
| ) | |   
  
References
[AdaptivePath::EngagePoint::EngageState::currentPathIndex](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#ab4cc9cf8cf2182c0562e1c57c757490b),
[AdaptivePath::EngagePoint::EngageState::currentSegmentIndex](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#aff954ac11fd189fb0a6c62a374d4eae3),
[AdaptivePath::DistanceSqrd()](../../d5/d7f/namespaceAdaptivePath.html#a8ba2907627cf52f54a10caa7ffbe4ac1),
[getCurrentPoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a4a25dac76882d1527f13a9f4683024a2),
[moveForward()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#aff2059280bef1a583fca8a367e3df635),
[nextPath()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a90133cef784e83a9b00801ecfa422d58),
[AdaptivePath::PopPathWithClosestPoint()](../../d5/d7f/namespaceAdaptivePath.html#a42481360e50af9d93ddfabe9d89bc66b),
[ResetPasses()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#ad565edb37f2b1dc8c578328a599e0a1a),
[AdaptivePath::EngagePoint::EngageState::segmentPos](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#a7df9f25695deaa7ac699e53393222e66),
and
[AdaptivePath::EngagePoint::EngageState::totalDistance](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#a89d9791d4a09751734117ad9ad82e22a).

## ◆ nextEngagePoint()

[bool](../../d9/db9/classbool.html) AdaptivePath::EngagePoint::nextEngagePoint  | ( | [Adaptive2d](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html) *  | _parent_ ,   
---|---|---|---  
|  | [ClearedArea](../../d8/d56/classAdaptivePath_1_1ClearedArea.html) & | _clearedArea_ ,   
|  | double  | _step_ ,   
|  | double  | _minCutArea_ ,   
|  | double  | _maxCutArea_ ,   
|  | [int](../../d1/da0/classint.html) | _maxPases_ = `2`  
| ) | |   
  
References
[getCurrentPoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a4a25dac76882d1527f13a9f4683024a2),
[moveForward()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#aff2059280bef1a583fca8a367e3df635),
[nextPath()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a90133cef784e83a9b00801ecfa422d58),
[AdaptivePath::EngagePoint::EngageState::passes](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#a66d85bedc41399fd958344ad3f6dbfa2),
[AdaptivePath::Perf_NextEngagePoint](../../d5/d7f/namespaceAdaptivePath.html#ada87d43aa4289654662208cf8a063726),
[AdaptivePath::PerfCounter::Start()](../../d2/d12/classAdaptivePath_1_1PerfCounter.html#a3020c4d3d1de9df1f3c201e39535978b),
and
[AdaptivePath::PerfCounter::Stop()](../../d2/d12/classAdaptivePath_1_1PerfCounter.html#ac161c5f0c9f2ff34315994274e151cf0).

## ◆ nextPath()

[bool](../../d9/db9/classbool.html) AdaptivePath::EngagePoint::nextPath  | ( | | ) |   
---|---|---|---|---  
  
References
[AdaptivePath::EngagePoint::EngageState::currentPathIndex](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#ab4cc9cf8cf2182c0562e1c57c757490b),
[AdaptivePath::EngagePoint::EngageState::currentSegmentIndex](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#aff954ac11fd189fb0a6c62a374d4eae3),
[AdaptivePath::EngagePoint::EngageState::segmentPos](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#a7df9f25695deaa7ac699e53393222e66),
and
[AdaptivePath::EngagePoint::EngageState::totalDistance](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#a89d9791d4a09751734117ad9ad82e22a).

Referenced by
[moveToClosestPoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#ab82d771a0d521b9b13fb15f6373df310),
and
[nextEngagePoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a853203bca004d7d69e68fed5a17e049f).

## ◆ ResetPasses()

void AdaptivePath::EngagePoint::ResetPasses  | ( | | ) |   
---|---|---|---|---  
  
References
[AdaptivePath::EngagePoint::EngageState::passes](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#a66d85bedc41399fd958344ad3f6dbfa2).

Referenced by
[moveToClosestPoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#ab82d771a0d521b9b13fb15f6373df310).

## ◆ SetPaths()

void AdaptivePath::EngagePoint::SetPaths  | ( | const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _paths_| ) |   
---|---|---|---|---|---  
  
References
[AdaptivePath::EngagePoint::EngageState::currentPathIndex](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#ab4cc9cf8cf2182c0562e1c57c757490b),
[AdaptivePath::EngagePoint::EngageState::currentSegmentIndex](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#aff954ac11fd189fb0a6c62a374d4eae3),
[AdaptivePath::EngagePoint::EngageState::passes](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#a66d85bedc41399fd958344ad3f6dbfa2),
[AdaptivePath::EngagePoint::EngageState::segmentPos](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#a7df9f25695deaa7ac699e53393222e66),
and
[AdaptivePath::EngagePoint::EngageState::totalDistance](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#a89d9791d4a09751734117ad9ad82e22a).

Referenced by
[EngagePoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#afec128c665fb4145754c7c13abb13830).

## ◆ SetState()

void AdaptivePath::EngagePoint::SetState  | ( | const [EngageState](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html) & | _new_state_| ) |   
---|---|---|---|---|---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Path/libarea/Adaptive.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

