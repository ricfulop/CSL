---
url: https://freecad.github.io/SourceDoc/d0/dfa/classBase_1_1Polygon2d.html
scraped_at: 2025-09-08T15:16:52.965494
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [Polygon2d](../../d0/dfa/classBase_1_1Polygon2d.html)

[List of all members](../../d8/d08/classBase_1_1Polygon2d-members.html) | Public Member Functions

Base::Polygon2d Class Reference

[Polygon2d](../../d0/dfa/classBase_1_1Polygon2d.html "Polygon2d.").
[More...](../../d0/dfa/classBase_1_1Polygon2d.html#details)

`#include <Tools2D.h>`

##  Public Member Functions  
  
---  
[bool](../../d9/db9/classbool.html) | [Add](../../d0/dfa/classBase_1_1Polygon2d.html#a654c75e15581223ea9643a42be8538cd) (const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &rclVct)  
[Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | [At](../../d0/dfa/classBase_1_1Polygon2d.html#a97f1729046db44c709f5fa01ab8e647c) (size_t ulNdx)  
const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | [At](../../d0/dfa/classBase_1_1Polygon2d.html#aeb03dd7e1819a7105ad87ca9579214da) (size_t ulNdx) const  
[BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html) | [CalcBoundBox](../../d0/dfa/classBase_1_1Polygon2d.html#a28a51cc5d29213d6e4b9305d658fbd24) () const  
| POLYGON2d.
[More...](../../d0/dfa/classBase_1_1Polygon2d.html#a28a51cc5d29213d6e4b9305d658fbd24)  
  
[bool](../../d9/db9/classbool.html) | [Contains](../../d0/dfa/classBase_1_1Polygon2d.html#ae1505348f7365e85a8a9d724dd2a7475) (const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &rclV) const  
[bool](../../d9/db9/classbool.html) | [Delete](../../d0/dfa/classBase_1_1Polygon2d.html#a5c86e5706bff96a62485b04971dc5c2e) (size_t ulNdx)  
void | [DeleteAll](../../d0/dfa/classBase_1_1Polygon2d.html#a36a100c6bffc3ae8f0d71a18fb52ab46) ()  
size_t | [GetCtVectors](../../d0/dfa/classBase_1_1Polygon2d.html#ae3d3b22f23505533cd9379ce3b00e3eb) () const  
[bool](../../d9/db9/classbool.html) | [Intersect](../../d0/dfa/classBase_1_1Polygon2d.html#a83fd4dc646471725efaf0607521516c5) (const [Polygon2d](../../d0/dfa/classBase_1_1Polygon2d.html) &rclPolygon) const  
void | [Intersect](../../d0/dfa/classBase_1_1Polygon2d.html#aac2ae89f2f12433cbd3666ba40f5a4ce) (const [Polygon2d](../../d0/dfa/classBase_1_1Polygon2d.html) &rclPolygon, std::list< [Polygon2d](../../d0/dfa/classBase_1_1Polygon2d.html) > &rclResultPolygonList) const  
[bool](../../d9/db9/classbool.html) | [Intersect](../../d0/dfa/classBase_1_1Polygon2d.html#a68973131a51999a2ea47eaeebdc23932) (const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &rclV, double eps) const  
[Polygon2d](../../d0/dfa/classBase_1_1Polygon2d.html) & | [operator=](../../d0/dfa/classBase_1_1Polygon2d.html#a3b795ee94b6aa1ca05b20402f23ea64f) (const [Polygon2d](../../d0/dfa/classBase_1_1Polygon2d.html) &rclP)  
[Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | [operator[]](../../d0/dfa/classBase_1_1Polygon2d.html#a848bfb665a4f6b6ed07f76debcceb561) (size_t ulNdx)  
const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | [operator[]](../../d0/dfa/classBase_1_1Polygon2d.html#aafae6290b6863a802367ec88b35aebe2) (size_t ulNdx) const  
|
[Polygon2d](../../d0/dfa/classBase_1_1Polygon2d.html#ad94c3c7e8aadc63fce986dfdf851f460)
()  
|
[Polygon2d](../../d0/dfa/classBase_1_1Polygon2d.html#a0e76c77dda35c6788fb50c4864cfad7b)
(const [Polygon2d](../../d0/dfa/classBase_1_1Polygon2d.html) &rclPoly)  
virtual | [~Polygon2d](../../d0/dfa/classBase_1_1Polygon2d.html#a4d355b4b21032eb1da8f92dbadc304ae) ()  
  
## Detailed Description

[Polygon2d](../../d0/dfa/classBase_1_1Polygon2d.html "Polygon2d.").

2D polygon class.

## Constructor & Destructor Documentation

## ◆ Polygon2d() [1/2]

Base::Polygon2d::Polygon2d  | ( | | ) |   
---|---|---|---|---  
  
## ◆ Polygon2d() [2/2]

Base::Polygon2d::Polygon2d  | ( | const [Polygon2d](../../d0/dfa/classBase_1_1Polygon2d.html) & | _rclPoly_| ) |   
---|---|---|---|---|---  
  
## ◆ ~Polygon2d()

| virtual Base::Polygon2d::~Polygon2d  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ Add()

[bool](../../d9/db9/classbool.html) Base::Polygon2d::Add  | ( | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _rclVct_| ) |   
---|---|---|---|---|---  
  
Referenced by
[PointsGui::ViewProviderScattered::cut()](../../df/dca/classPointsGui_1_1ViewProviderScattered.html#a6e93ecaa9bbca01c9cd9c294ba22f38c),
[PointsGui::ViewProviderStructured::cut()](../../d4/d20/classPointsGui_1_1ViewProviderStructured.html#a808184849a3543a6d70c263099506c98),
[Intersect()](../../d0/dfa/classBase_1_1Polygon2d.html#aac2ae89f2f12433cbd3666ba40f5a4ce),
and
[MeshGui::ViewProviderMesh::trimMesh()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a265b2a1e25e284315a52153b8b6c4d71).

## ◆ At() [1/2]

[Vector2d](../../db/da7/classBase_1_1Vector2d.html) & Base::Polygon2d::At  | ( | size_t  | _ulNdx_| ) |   
---|---|---|---|---|---  
  
## ◆ At() [2/2]

const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & Base::Polygon2d::At  | ( | size_t  | _ulNdx_| ) |  const  
---|---|---|---|---|---  
  
Referenced by
[Intersect()](../../d0/dfa/classBase_1_1Polygon2d.html#aac2ae89f2f12433cbd3666ba40f5a4ce).

## ◆ CalcBoundBox()

[BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html) Polygon2d::CalcBoundBox  | ( | | ) |  const  
---|---|---|---|---  
  
POLYGON2d.

References
[Base::BoundBox2d::MaxX](../../de/db4/classBase_1_1BoundBox2d.html#a945cf6dbf19794fadf57611c743d4af1),
[Base::BoundBox2d::MaxY](../../de/db4/classBase_1_1BoundBox2d.html#a16e40b1b2005f47d75fba6802dcd8f80),
[Base::BoundBox2d::MinX](../../de/db4/classBase_1_1BoundBox2d.html#a463231b777b4ac6a329167866d054d36),
and
[Base::BoundBox2d::MinY](../../de/db4/classBase_1_1BoundBox2d.html#acd6ec6a1cc10a691503379e335a24133).

Referenced by
[MeshCore::MeshAlgorithm::CheckFacets()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#ac8032a5a0a06cee43035edcb9253b731),
and
[MeshCore::MeshTrimming::CheckFacets()](../../d3/da1/classMeshCore_1_1MeshTrimming.html#a94a5bf3ea3f16d468c08906a5dcbb472).

## ◆ Contains()

[bool](../../d9/db9/classbool.html) Polygon2d::Contains  | ( | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _rclV_| ) |  const  
---|---|---|---|---|---  
  
References
[GetCtVectors()](../../d0/dfa/classBase_1_1Polygon2d.html#ae3d3b22f23505533cd9379ce3b00e3eb),
[Base::Vector2d::x](../../db/da7/classBase_1_1Vector2d.html#a3315b37d53044b7356de30337675eb59),
and
[Base::Vector2d::y](../../db/da7/classBase_1_1Vector2d.html#a939f494d2b0c0395a9003e30d4c07887).

Referenced by
[MeshCore::MeshAlgorithm::CheckFacets()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#ac8032a5a0a06cee43035edcb9253b731),
[PointsGui::ViewProviderScattered::cut()](../../df/dca/classPointsGui_1_1ViewProviderScattered.html#a6e93ecaa9bbca01c9cd9c294ba22f38c),
[PointsGui::ViewProviderStructured::cut()](../../d4/d20/classPointsGui_1_1ViewProviderStructured.html#a808184849a3543a6d70c263099506c98),
[Base::BoundBox2d::Intersect()](../../de/db4/classBase_1_1BoundBox2d.html#a06385687a9da411a4fa8863de43c2926),
and
[Intersect()](../../d0/dfa/classBase_1_1Polygon2d.html#aac2ae89f2f12433cbd3666ba40f5a4ce).

## ◆ Delete()

[bool](../../d9/db9/classbool.html) Base::Polygon2d::Delete  | ( | size_t  | _ulNdx_| ) |   
---|---|---|---|---|---  
  
## ◆ DeleteAll()

void Base::Polygon2d::DeleteAll  | ( | | ) |   
---|---|---|---|---  
  
Referenced by
[Intersect()](../../d0/dfa/classBase_1_1Polygon2d.html#aac2ae89f2f12433cbd3666ba40f5a4ce).

## ◆ GetCtVectors()

size_t Base::Polygon2d::GetCtVectors  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[Contains()](../../d0/dfa/classBase_1_1Polygon2d.html#ae1505348f7365e85a8a9d724dd2a7475),
[Base::BoundBox2d::Intersect()](../../de/db4/classBase_1_1BoundBox2d.html#a06385687a9da411a4fa8863de43c2926),
and
[Intersect()](../../d0/dfa/classBase_1_1Polygon2d.html#aac2ae89f2f12433cbd3666ba40f5a4ce).

## ◆ Intersect() [1/3]

[bool](../../d9/db9/classbool.html) Polygon2d::Intersect  | ( | const [Polygon2d](../../d0/dfa/classBase_1_1Polygon2d.html) & | _rclPolygon_| ) |  const  
---|---|---|---|---|---  
  
References
[At()](../../d0/dfa/classBase_1_1Polygon2d.html#aeb03dd7e1819a7105ad87ca9579214da),
[Contains()](../../d0/dfa/classBase_1_1Polygon2d.html#ae1505348f7365e85a8a9d724dd2a7475),
[GetCtVectors()](../../d0/dfa/classBase_1_1Polygon2d.html#ae3d3b22f23505533cd9379ce3b00e3eb),
and
[Base::Line2d::IntersectAndContain()](../../d1/d69/classBase_1_1Line2d.html#afd22687bb810c2f174f65d1f96361bda).

## ◆ Intersect() [2/3]

void Polygon2d::Intersect  | ( | const [Polygon2d](../../d0/dfa/classBase_1_1Polygon2d.html) & | _rclPolygon_ ,   
---|---|---|---  
|  | std::list< [Polygon2d](../../d0/dfa/classBase_1_1Polygon2d.html) > & | _rclResultPolygonList_  
| ) | |  const  
  
References
[Add()](../../d0/dfa/classBase_1_1Polygon2d.html#a654c75e15581223ea9643a42be8538cd),
[At()](../../d0/dfa/classBase_1_1Polygon2d.html#aeb03dd7e1819a7105ad87ca9579214da),
[Contains()](../../d0/dfa/classBase_1_1Polygon2d.html#ae1505348f7365e85a8a9d724dd2a7475),
[DeleteAll()](../../d0/dfa/classBase_1_1Polygon2d.html#a36a100c6bffc3ae8f0d71a18fb52ab46),
[Base::Line2d::FromPos()](../../d1/d69/classBase_1_1Line2d.html#a6a9d25de5ddb351d022bc8c4baf4da94),
[GetCtVectors()](../../d0/dfa/classBase_1_1Polygon2d.html#ae3d3b22f23505533cd9379ce3b00e3eb),
and
[Base::Line2d::IntersectAndContain()](../../d1/d69/classBase_1_1Line2d.html#afd22687bb810c2f174f65d1f96361bda).

## ◆ Intersect() [3/3]

[bool](../../d9/db9/classbool.html) Polygon2d::Intersect  | ( | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _rclV_ ,   
---|---|---|---  
|  | double  | _eps_  
| ) | |  const  
  
References
[GetCtVectors()](../../d0/dfa/classBase_1_1Polygon2d.html#ae3d3b22f23505533cd9379ce3b00e3eb).

## ◆ operator=()

[Polygon2d](../../d0/dfa/classBase_1_1Polygon2d.html) & Base::Polygon2d::operator=  | ( | const [Polygon2d](../../d0/dfa/classBase_1_1Polygon2d.html) & | _rclP_| ) |   
---|---|---|---|---|---  
  
## ◆ operator[]() [1/2]

[Vector2d](../../db/da7/classBase_1_1Vector2d.html) & Base::Polygon2d::operator[]  | ( | size_t  | _ulNdx_| ) |   
---|---|---|---|---|---  
  
## ◆ operator[]() [2/2]

const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & Base::Polygon2d::operator[]  | ( | size_t  | _ulNdx_| ) |  const  
---|---|---|---|---|---  
  
* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Tools2D.h
  * FreeCAD/src/Base/Tools2D.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

