---
url: https://freecad.github.io/SourceDoc/dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html
scraped_at: 2025-09-08T14:52:44.977671
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [AdaptivePath](../../d5/d7f/namespaceAdaptivePath.html)
  * [EngagePoint](../../de/d69/classAdaptivePath_1_1EngagePoint.html)
  * [EngageState](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html)

[List of all members](../../d6/df1/structAdaptivePath_1_1EngagePoint_1_1EngageState-members.html) | Public Member Functions | Public Attributes

AdaptivePath::EngagePoint::EngageState Struct Reference

##  Public Member Functions  
  
---  
[bool](../../d9/db9/classbool.html) | [operator<](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#a9ffda9ec00684115c9656e4cce8afac3) (const [EngageState](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html) &other) const  
  
##  Public Attributes  
  
---  
size_t | [currentPathIndex](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#ab4cc9cf8cf2182c0562e1c57c757490b) = 0  
double | [currentPathLength](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#afbe85d9f53105445d0c305dab4ca4064) = 0  
size_t | [currentSegmentIndex](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#aff954ac11fd189fb0a6c62a374d4eae3) = 0  
double | [metric](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#aee59f507717fb0648214a061aee5d084) = 0  
[int](../../d1/da0/classint.html) | [passes](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#a66d85bedc41399fd958344ad3f6dbfa2) = 0  
double | [segmentPos](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#a7df9f25695deaa7ac699e53393222e66) = 0  
double | [totalDistance](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#a89d9791d4a09751734117ad9ad82e22a) = 0  
  
## Member Function Documentation

## ◆ operator<()

[bool](../../d9/db9/classbool.html) AdaptivePath::EngagePoint::EngageState::operator< | ( | const [EngageState](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
References
[metric](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#aee59f507717fb0648214a061aee5d084).

## Member Data Documentation

## ◆ currentPathIndex

size_t AdaptivePath::EngagePoint::EngageState::currentPathIndex = 0  
---  
  
Referenced by
[AdaptivePath::EngagePoint::EngagePoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#afec128c665fb4145754c7c13abb13830),
[AdaptivePath::EngagePoint::getCurrentDir()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a64238fcdbfa9f4bf6a2fc4f000405339),
[AdaptivePath::EngagePoint::getCurrentPoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a4a25dac76882d1527f13a9f4683024a2),
[AdaptivePath::EngagePoint::moveForward()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#aff2059280bef1a583fca8a367e3df635),
[AdaptivePath::EngagePoint::moveToClosestPoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#ab82d771a0d521b9b13fb15f6373df310),
[AdaptivePath::EngagePoint::nextPath()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a90133cef784e83a9b00801ecfa422d58),
and
[AdaptivePath::EngagePoint::SetPaths()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#ac21717234f26373f886055b60990717d).

## ◆ currentPathLength

double AdaptivePath::EngagePoint::EngageState::currentPathLength = 0  
---  
  
Referenced by
[AdaptivePath::EngagePoint::moveForward()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#aff2059280bef1a583fca8a367e3df635).

## ◆ currentSegmentIndex

size_t AdaptivePath::EngagePoint::EngageState::currentSegmentIndex = 0  
---  
  
Referenced by
[AdaptivePath::EngagePoint::EngagePoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#afec128c665fb4145754c7c13abb13830),
[AdaptivePath::EngagePoint::getCurrentDir()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a64238fcdbfa9f4bf6a2fc4f000405339),
[AdaptivePath::EngagePoint::getCurrentPoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a4a25dac76882d1527f13a9f4683024a2),
[AdaptivePath::EngagePoint::moveForward()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#aff2059280bef1a583fca8a367e3df635),
[AdaptivePath::EngagePoint::moveToClosestPoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#ab82d771a0d521b9b13fb15f6373df310),
[AdaptivePath::EngagePoint::nextPath()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a90133cef784e83a9b00801ecfa422d58),
and
[AdaptivePath::EngagePoint::SetPaths()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#ac21717234f26373f886055b60990717d).

## ◆ metric

double AdaptivePath::EngagePoint::EngageState::metric = 0  
---  
  
Referenced by
[operator<()](../../dd/d57/structAdaptivePath_1_1EngagePoint_1_1EngageState.html#a9ffda9ec00684115c9656e4cce8afac3).

## ◆ passes

[int](../../d1/da0/classint.html)
AdaptivePath::EngagePoint::EngageState::passes = 0  
---  
  
Referenced by
[AdaptivePath::EngagePoint::nextEngagePoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a853203bca004d7d69e68fed5a17e049f),
[AdaptivePath::EngagePoint::ResetPasses()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#ad565edb37f2b1dc8c578328a599e0a1a),
and
[AdaptivePath::EngagePoint::SetPaths()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#ac21717234f26373f886055b60990717d).

## ◆ segmentPos

double AdaptivePath::EngagePoint::EngageState::segmentPos = 0  
---  
  
Referenced by
[AdaptivePath::EngagePoint::EngagePoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#afec128c665fb4145754c7c13abb13830),
[AdaptivePath::EngagePoint::getCurrentPoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a4a25dac76882d1527f13a9f4683024a2),
[AdaptivePath::EngagePoint::moveForward()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#aff2059280bef1a583fca8a367e3df635),
[AdaptivePath::EngagePoint::moveToClosestPoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#ab82d771a0d521b9b13fb15f6373df310),
[AdaptivePath::EngagePoint::nextPath()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a90133cef784e83a9b00801ecfa422d58),
and
[AdaptivePath::EngagePoint::SetPaths()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#ac21717234f26373f886055b60990717d).

## ◆ totalDistance

double AdaptivePath::EngagePoint::EngageState::totalDistance = 0  
---  
  
Referenced by
[AdaptivePath::EngagePoint::EngagePoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#afec128c665fb4145754c7c13abb13830),
[AdaptivePath::EngagePoint::moveForward()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#aff2059280bef1a583fca8a367e3df635),
[AdaptivePath::EngagePoint::moveToClosestPoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#ab82d771a0d521b9b13fb15f6373df310),
[AdaptivePath::EngagePoint::nextPath()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a90133cef784e83a9b00801ecfa422d58),
and
[AdaptivePath::EngagePoint::SetPaths()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#ac21717234f26373f886055b60990717d).

* * *

The documentation for this struct was generated from the following file:

  * FreeCAD/src/Mod/Path/libarea/Adaptive.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

