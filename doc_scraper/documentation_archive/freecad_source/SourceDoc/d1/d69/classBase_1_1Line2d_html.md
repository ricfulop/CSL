---
url: https://freecad.github.io/SourceDoc/d1/d69/classBase_1_1Line2d.html
scraped_at: 2025-09-08T15:16:34.907565
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [Line2d](../../d1/d69/classBase_1_1Line2d.html)

[List of all members](../../df/daf/classBase_1_1Line2d-members.html) | Public Member Functions | Public Attributes

Base::Line2d Class Reference

[Line2d](../../d1/d69/classBase_1_1Line2d.html "Line2d.").
[More...](../../d1/d69/classBase_1_1Line2d.html#details)

`#include <Tools2D.h>`

##  Public Member Functions  
  
---  
[BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html) | [CalcBoundBox](../../d1/d69/classBase_1_1Line2d.html#ac67a75e9c6476cbebed194d8e66c8516) () const  
| LINE2D.
[More...](../../d1/d69/classBase_1_1Line2d.html#ac67a75e9c6476cbebed194d8e66c8516)  
  
[bool](../../d9/db9/classbool.html) | [Contains](../../d1/d69/classBase_1_1Line2d.html#a6327c8680eb946c971868a31229cb959) (const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &rclV) const  
[Vector2d](../../db/da7/classBase_1_1Vector2d.html) | [FromPos](../../d1/d69/classBase_1_1Line2d.html#a6a9d25de5ddb351d022bc8c4baf4da94) (double fDistance) const  
[bool](../../d9/db9/classbool.html) | [Intersect](../../d1/d69/classBase_1_1Line2d.html#a6387b9d36d8bb717c7d643792e8fe3e7) (const [Line2d](../../d1/d69/classBase_1_1Line2d.html) &rclLine, [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &rclV) const  
[bool](../../d9/db9/classbool.html) | [Intersect](../../d1/d69/classBase_1_1Line2d.html#a3f96fbfbd16be8fd36ad955a39bb22b7) (const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &rclV, double eps) const  
[bool](../../d9/db9/classbool.html) | [IntersectAndContain](../../d1/d69/classBase_1_1Line2d.html#afd22687bb810c2f174f65d1f96361bda) (const [Line2d](../../d1/d69/classBase_1_1Line2d.html) &rclLine, [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &rclV) const  
double | [Length](../../d1/d69/classBase_1_1Line2d.html#a05f118183e69c67107e28cb3c1cf2d32) () const  
|
[Line2d](../../d1/d69/classBase_1_1Line2d.html#ae8e8dfa321874a11721fb4c5b30d6c0e)
()  
|
[Line2d](../../d1/d69/classBase_1_1Line2d.html#aea454401f5f915970077b569a06a72bb)
(const [Line2d](../../d1/d69/classBase_1_1Line2d.html) &rclLine)  
|
[Line2d](../../d1/d69/classBase_1_1Line2d.html#a14beefbeb2e34e2a45dc7f7b04dfd5a1)
(const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &rclV1, const
[Vector2d](../../db/da7/classBase_1_1Vector2d.html) &rclV2)  
[Line2d](../../d1/d69/classBase_1_1Line2d.html) & | [operator=](../../d1/d69/classBase_1_1Line2d.html#afa8d881f3da0bdba2018bf5c9a90141a) (const [Line2d](../../d1/d69/classBase_1_1Line2d.html) &rclLine)  
[bool](../../d9/db9/classbool.html) | [operator==](../../d1/d69/classBase_1_1Line2d.html#ada100bf87ca5ee882fb48219e886246d) (const [Line2d](../../d1/d69/classBase_1_1Line2d.html) &rclLine) const  
  
##  Public Attributes  
  
---  
[Vector2d](../../db/da7/classBase_1_1Vector2d.html) | [clV1](../../d1/d69/classBase_1_1Line2d.html#a10884a03dec4bc93c74ab8ad7c2b3d60)  
[Vector2d](../../db/da7/classBase_1_1Vector2d.html) | [clV2](../../d1/d69/classBase_1_1Line2d.html#ae368828e435ebf6acc77c1cf10cd09ce)  
  
## Detailed Description

[Line2d](../../d1/d69/classBase_1_1Line2d.html "Line2d.").

2D line class.

## Constructor & Destructor Documentation

## ◆ Line2d() [1/3]

Base::Line2d::Line2d  | ( | | ) |   
---|---|---|---|---  
  
## ◆ Line2d() [2/3]

Base::Line2d::Line2d  | ( | const [Line2d](../../d1/d69/classBase_1_1Line2d.html) & | _rclLine_| ) |   
---|---|---|---|---|---  
  
## ◆ Line2d() [3/3]

Base::Line2d::Line2d  | ( | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _rclV1_ ,   
---|---|---|---  
|  | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _rclV2_  
| ) | |   
  
## Member Function Documentation

## ◆ CalcBoundBox()

[BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html) Line2d::CalcBoundBox  | ( | | ) |  const  
---|---|---|---|---  
  
LINE2D.

References
[clV1](../../d1/d69/classBase_1_1Line2d.html#a10884a03dec4bc93c74ab8ad7c2b3d60),
[clV2](../../d1/d69/classBase_1_1Line2d.html#ae368828e435ebf6acc77c1cf10cd09ce),
[Base::BoundBox2d::MaxX](../../de/db4/classBase_1_1BoundBox2d.html#a945cf6dbf19794fadf57611c743d4af1),
[Base::BoundBox2d::MaxY](../../de/db4/classBase_1_1BoundBox2d.html#a16e40b1b2005f47d75fba6802dcd8f80),
[Base::BoundBox2d::MinX](../../de/db4/classBase_1_1BoundBox2d.html#a463231b777b4ac6a329167866d054d36),
[Base::BoundBox2d::MinY](../../de/db4/classBase_1_1BoundBox2d.html#acd6ec6a1cc10a691503379e335a24133),
[Base::Vector2d::x](../../db/da7/classBase_1_1Vector2d.html#a3315b37d53044b7356de30337675eb59),
and
[Base::Vector2d::y](../../db/da7/classBase_1_1Vector2d.html#a939f494d2b0c0395a9003e30d4c07887).

Referenced by
[Contains()](../../d1/d69/classBase_1_1Line2d.html#a6327c8680eb946c971868a31229cb959).

## ◆ Contains()

[bool](../../d9/db9/classbool.html) Base::Line2d::Contains  | ( | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _rclV_| ) |  const  
---|---|---|---|---|---  
  
References
[CalcBoundBox()](../../d1/d69/classBase_1_1Line2d.html#ac67a75e9c6476cbebed194d8e66c8516),
and
[Base::BoundBox2d::Contains()](../../de/db4/classBase_1_1BoundBox2d.html#afb5c026976e2e965c7dbd4ef4e95c5b9).

Referenced by
[IntersectAndContain()](../../d1/d69/classBase_1_1Line2d.html#afd22687bb810c2f174f65d1f96361bda).

## ◆ FromPos()

[Vector2d](../../db/da7/classBase_1_1Vector2d.html) Line2d::FromPos  | ( | double  | _fDistance_| ) |  const  
---|---|---|---|---|---  
  
References
[clV1](../../d1/d69/classBase_1_1Line2d.html#a10884a03dec4bc93c74ab8ad7c2b3d60),
[clV2](../../d1/d69/classBase_1_1Line2d.html#ae368828e435ebf6acc77c1cf10cd09ce),
[Base::Vector2d::Normalize()](../../db/da7/classBase_1_1Vector2d.html#ad86e1f342407f62d1eb78bfd5b112ec6),
[Base::Vector2d::x](../../db/da7/classBase_1_1Vector2d.html#a3315b37d53044b7356de30337675eb59),
and
[Base::Vector2d::y](../../db/da7/classBase_1_1Vector2d.html#a939f494d2b0c0395a9003e30d4c07887).

Referenced by
[Base::Polygon2d::Intersect()](../../d0/dfa/classBase_1_1Polygon2d.html#aac2ae89f2f12433cbd3666ba40f5a4ce).

## ◆ Intersect() [1/2]

[bool](../../d9/db9/classbool.html) Line2d::Intersect  | ( | const [Line2d](../../d1/d69/classBase_1_1Line2d.html) & | _rclLine_ ,   
---|---|---|---  
|  | [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _rclV_  
| ) | |  const  
  
References
[clV1](../../d1/d69/classBase_1_1Line2d.html#a10884a03dec4bc93c74ab8ad7c2b3d60),
[clV2](../../d1/d69/classBase_1_1Line2d.html#ae368828e435ebf6acc77c1cf10cd09ce),
[Base::Vector2d::x](../../db/da7/classBase_1_1Vector2d.html#a3315b37d53044b7356de30337675eb59),
and
[Base::Vector2d::y](../../db/da7/classBase_1_1Vector2d.html#a939f494d2b0c0395a9003e30d4c07887).

Referenced by
[CmdSketcherConstrainAngle::activated()](../../dc/dd6/classCmdSketcherConstrainAngle.html#a0d48a74c0960a5a240c1a39137f070a3),
[CmdSketcherConstrainAngle::applyConstraint()](../../dc/dd6/classCmdSketcherConstrainAngle.html#a5602881a59f6c0a0a83a30641560aeb7),
and
[IntersectAndContain()](../../d1/d69/classBase_1_1Line2d.html#afd22687bb810c2f174f65d1f96361bda).

## ◆ Intersect() [2/2]

[bool](../../d9/db9/classbool.html) Line2d::Intersect  | ( | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _rclV_ ,   
---|---|---|---  
|  | double  | _eps_  
| ) | |  const  
  
References
[clV1](../../d1/d69/classBase_1_1Line2d.html#a10884a03dec4bc93c74ab8ad7c2b3d60),
[clV2](../../d1/d69/classBase_1_1Line2d.html#ae368828e435ebf6acc77c1cf10cd09ce),
[Base::Vector2d::x](../../db/da7/classBase_1_1Vector2d.html#a3315b37d53044b7356de30337675eb59),
and
[Base::Vector2d::y](../../db/da7/classBase_1_1Vector2d.html#a939f494d2b0c0395a9003e30d4c07887).

## ◆ IntersectAndContain()

[bool](../../d9/db9/classbool.html) Line2d::IntersectAndContain  | ( | const [Line2d](../../d1/d69/classBase_1_1Line2d.html) & | _rclLine_ ,   
---|---|---|---  
|  | [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _rclV_  
| ) | |  const  
  
References
[Contains()](../../d1/d69/classBase_1_1Line2d.html#a6327c8680eb946c971868a31229cb959),
and
[Intersect()](../../d1/d69/classBase_1_1Line2d.html#a6387b9d36d8bb717c7d643792e8fe3e7).

Referenced by
[Base::BoundBox2d::Intersect()](../../de/db4/classBase_1_1BoundBox2d.html#a2bdb07ef91c340dc5fd1f4371f1e1329),
and
[Base::Polygon2d::Intersect()](../../d0/dfa/classBase_1_1Polygon2d.html#aac2ae89f2f12433cbd3666ba40f5a4ce).

## ◆ Length()

double Base::Line2d::Length  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
References
[clV1](../../d1/d69/classBase_1_1Line2d.html#a10884a03dec4bc93c74ab8ad7c2b3d60),
and
[clV2](../../d1/d69/classBase_1_1Line2d.html#ae368828e435ebf6acc77c1cf10cd09ce).

Referenced by
[ArchStructure.CommandStructuralSystem::Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[ArchPanel.CommandPanel::getPoint()](../../d9/d86/classArchPanel_1_1CommandPanel.html#ad968284b7adc2bee10d76a20c1a4c7fb),
[ArchPanel.CommandPanel::setLength()](../../d9/d86/classArchPanel_1_1CommandPanel.html#a324c9bdbfec0dd8eacfb7d0cea302998),
and
[ArchPanel.CommandPanel::update()](../../d9/d86/classArchPanel_1_1CommandPanel.html#a2e34ede3be08f250ec800823ef76df1c).

## ◆ operator=()

[Line2d](../../d1/d69/classBase_1_1Line2d.html) & Base::Line2d::operator=  | ( | const [Line2d](../../d1/d69/classBase_1_1Line2d.html) & | _rclLine_| ) |   
---|---|---|---|---|---  
  
References
[clV1](../../d1/d69/classBase_1_1Line2d.html#a10884a03dec4bc93c74ab8ad7c2b3d60),
and
[clV2](../../d1/d69/classBase_1_1Line2d.html#ae368828e435ebf6acc77c1cf10cd09ce).

## ◆ operator==()

[bool](../../d9/db9/classbool.html) Base::Line2d::operator==  | ( | const [Line2d](../../d1/d69/classBase_1_1Line2d.html) & | _rclLine_| ) |  const  
---|---|---|---|---|---  
  
References
[clV1](../../d1/d69/classBase_1_1Line2d.html#a10884a03dec4bc93c74ab8ad7c2b3d60),
and
[clV2](../../d1/d69/classBase_1_1Line2d.html#ae368828e435ebf6acc77c1cf10cd09ce).

## Member Data Documentation

## ◆ clV1

[Vector2d](../../db/da7/classBase_1_1Vector2d.html) Base::Line2d::clV1  
---  
  
Referenced by
[CalcBoundBox()](../../d1/d69/classBase_1_1Line2d.html#ac67a75e9c6476cbebed194d8e66c8516),
[FromPos()](../../d1/d69/classBase_1_1Line2d.html#a6a9d25de5ddb351d022bc8c4baf4da94),
[Base::BoundBox2d::Intersect()](../../de/db4/classBase_1_1BoundBox2d.html#a2bdb07ef91c340dc5fd1f4371f1e1329),
[Intersect()](../../d1/d69/classBase_1_1Line2d.html#a6387b9d36d8bb717c7d643792e8fe3e7),
[Length()](../../d1/d69/classBase_1_1Line2d.html#a05f118183e69c67107e28cb3c1cf2d32),
[operator=()](../../d1/d69/classBase_1_1Line2d.html#afa8d881f3da0bdba2018bf5c9a90141a),
and
[operator==()](../../d1/d69/classBase_1_1Line2d.html#ada100bf87ca5ee882fb48219e886246d).

## ◆ clV2

[Vector2d](../../db/da7/classBase_1_1Vector2d.html) Base::Line2d::clV2  
---  
  
Referenced by
[CalcBoundBox()](../../d1/d69/classBase_1_1Line2d.html#ac67a75e9c6476cbebed194d8e66c8516),
[FromPos()](../../d1/d69/classBase_1_1Line2d.html#a6a9d25de5ddb351d022bc8c4baf4da94),
[Base::BoundBox2d::Intersect()](../../de/db4/classBase_1_1BoundBox2d.html#a2bdb07ef91c340dc5fd1f4371f1e1329),
[Intersect()](../../d1/d69/classBase_1_1Line2d.html#a6387b9d36d8bb717c7d643792e8fe3e7),
[Length()](../../d1/d69/classBase_1_1Line2d.html#a05f118183e69c67107e28cb3c1cf2d32),
[operator=()](../../d1/d69/classBase_1_1Line2d.html#afa8d881f3da0bdba2018bf5c9a90141a),
and
[operator==()](../../d1/d69/classBase_1_1Line2d.html#ada100bf87ca5ee882fb48219e886246d).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Tools2D.h
  * FreeCAD/src/Base/Tools2D.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

