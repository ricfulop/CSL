---
url: https://freecad.github.io/SourceDoc/d6/dc3/classAdaptivePath_1_1BoundBox.html
scraped_at: 2025-09-08T14:52:41.977875
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [AdaptivePath](../../d5/d7f/namespaceAdaptivePath.html)
  * [BoundBox](../../d6/dc3/classAdaptivePath_1_1BoundBox.html)

[List of all members](../../d0/dab/classAdaptivePath_1_1BoundBox-members.html) | Public Member Functions | Public Attributes

AdaptivePath::BoundBox Class Reference

##  Public Member Functions  
  
---  
void | [AddPoint](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a47b23bb75413d049f127728ad178ea76) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt)  
|
[BoundBox](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a3a9a43a16ea3b218bd72c904ef7f193a)
()  
|
[BoundBox](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a44f2f9ec24434c7b4c664a749c44d04d)
(const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &center,
long radius)  
|
[BoundBox](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#abe92c0b8410f953628b1e2a3010af556)
(const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &p1)  
|
[BoundBox](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a2701ab64d616348483ca133da0a9b004)
(const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &p1, const
[IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &p2)  
[bool](../../d9/db9/classbool.html) | [CollidesWith](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a2bbbd18bf8af744a2b9fd7a8f67409ea) (const [BoundBox](../../d6/dc3/classAdaptivePath_1_1BoundBox.html) &bb2)  
[bool](../../d9/db9/classbool.html) | [Contains](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#af72c43f46ec868065be57cebd1bc1f85) (const [BoundBox](../../d6/dc3/classAdaptivePath_1_1BoundBox.html) &bb2)  
void | [SetFirstPoint](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a33a37a0cdf8b16dbd473f595ba0984eb) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &p1)  
  
##  Public Attributes  
  
---  
[ClipperLib::cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) | [maxX](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a057b8aa1332e9fc72afb68101840e217)  
[ClipperLib::cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) | [maxY](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#ab0d502e908de607e815b49559832a98d)  
[ClipperLib::cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) | [minX](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#ac6dbba07f108c126a884f2fca89f1f84)  
[ClipperLib::cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) | [minY](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a2fbe02b197a1dd03001fcc3974ce8bde)  
  
## Constructor & Destructor Documentation

## ◆ BoundBox() [1/4]

AdaptivePath::BoundBox::BoundBox  | ( | | ) |   
---|---|---|---|---  
  
References
[minX](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#ac6dbba07f108c126a884f2fca89f1f84).

## ◆ BoundBox() [2/4]

AdaptivePath::BoundBox::BoundBox  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _p1_| ) |   
---|---|---|---|---|---  
  
References
[minX](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#ac6dbba07f108c126a884f2fca89f1f84),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

## ◆ BoundBox() [3/4]

AdaptivePath::BoundBox::BoundBox  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _p1_ ,   
---|---|---|---  
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _p2_  
| ) | |   
  
References
[minX](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#ac6dbba07f108c126a884f2fca89f1f84),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

## ◆ BoundBox() [4/4]

AdaptivePath::BoundBox::BoundBox  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _center_ ,   
---|---|---|---  
|  | long  | _radius_  
| ) | |   
  
References
[minX](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#ac6dbba07f108c126a884f2fca89f1f84).

## Member Function Documentation

## ◆ AddPoint()

void AdaptivePath::BoundBox::AddPoint  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt_| ) |   
---|---|---|---|---|---  
  
References
[minX](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#ac6dbba07f108c126a884f2fca89f1f84),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

Referenced by
[AdaptivePath::ClearedArea::GetBoundedClearedAreaClipped()](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a396af78fc129b33fe0c3730caadc9503),
[AdaptivePath::ClearedArea::GetBoundedClearedPaths()](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a68e1a211be4683c860dba6ec244abc36),
and
[AdaptivePath::IntersectionPoint()](../../d5/d7f/namespaceAdaptivePath.html#a393af31a1bf0ed6ef6428832dd4a596b).

## ◆ CollidesWith()

[bool](../../d9/db9/classbool.html) AdaptivePath::BoundBox::CollidesWith  | ( | const [BoundBox](../../d6/dc3/classAdaptivePath_1_1BoundBox.html) & | _bb2_| ) |   
---|---|---|---|---|---  
  
References
[maxX](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a057b8aa1332e9fc72afb68101840e217),
[maxY](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#ab0d502e908de607e815b49559832a98d),
[minX](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#ac6dbba07f108c126a884f2fca89f1f84),
and
[minY](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a2fbe02b197a1dd03001fcc3974ce8bde).

Referenced by
[AdaptivePath::ClearedArea::GetBoundedClearedPaths()](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a68e1a211be4683c860dba6ec244abc36),
[AdaptivePath::IntersectionPoint()](../../d5/d7f/namespaceAdaptivePath.html#a393af31a1bf0ed6ef6428832dd4a596b),
and
[AdaptivePath::Line2CircleIntersect()](../../d5/d7f/namespaceAdaptivePath.html#a162b44dbc1289576521d7d3e3084562f).

## ◆ Contains()

[bool](../../d9/db9/classbool.html) AdaptivePath::BoundBox::Contains  | ( | const [BoundBox](../../d6/dc3/classAdaptivePath_1_1BoundBox.html) & | _bb2_| ) |   
---|---|---|---|---|---  
  
References
[maxX](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a057b8aa1332e9fc72afb68101840e217),
[maxY](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#ab0d502e908de607e815b49559832a98d),
[minX](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#ac6dbba07f108c126a884f2fca89f1f84),
and
[minY](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a2fbe02b197a1dd03001fcc3974ce8bde).

Referenced by
[AdaptivePath::ClearedArea::GetBoundedClearedAreaClipped()](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a396af78fc129b33fe0c3730caadc9503),
and
[AdaptivePath::ClearedArea::GetBoundedClearedPaths()](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a68e1a211be4683c860dba6ec244abc36).

## ◆ SetFirstPoint()

void AdaptivePath::BoundBox::SetFirstPoint  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _p1_| ) |   
---|---|---|---|---|---  
  
References
[minX](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#ac6dbba07f108c126a884f2fca89f1f84),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

Referenced by
[AdaptivePath::ClearedArea::GetBoundedClearedAreaClipped()](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a396af78fc129b33fe0c3730caadc9503),
and
[AdaptivePath::ClearedArea::GetBoundedClearedPaths()](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a68e1a211be4683c860dba6ec244abc36).

## Member Data Documentation

## ◆ maxX

[ClipperLib::cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa)
AdaptivePath::BoundBox::maxX  
---  
  
Referenced by
[CollidesWith()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a2bbbd18bf8af744a2b9fd7a8f67409ea),
and
[Contains()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#af72c43f46ec868065be57cebd1bc1f85).

## ◆ maxY

[ClipperLib::cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa)
AdaptivePath::BoundBox::maxY  
---  
  
Referenced by
[CollidesWith()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a2bbbd18bf8af744a2b9fd7a8f67409ea),
and
[Contains()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#af72c43f46ec868065be57cebd1bc1f85).

## ◆ minX

[ClipperLib::cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa)
AdaptivePath::BoundBox::minX  
---  
  
Referenced by
[AddPoint()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a47b23bb75413d049f127728ad178ea76),
[BoundBox()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a3a9a43a16ea3b218bd72c904ef7f193a),
[CollidesWith()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a2bbbd18bf8af744a2b9fd7a8f67409ea),
[Contains()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#af72c43f46ec868065be57cebd1bc1f85),
and
[SetFirstPoint()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a33a37a0cdf8b16dbd473f595ba0984eb).

## ◆ minY

[ClipperLib::cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa)
AdaptivePath::BoundBox::minY  
---  
  
Referenced by
[CollidesWith()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a2bbbd18bf8af744a2b9fd7a8f67409ea),
and
[Contains()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#af72c43f46ec868065be57cebd1bc1f85).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Path/libarea/Adaptive.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

