---
url: https://freecad.github.io/SourceDoc/d2/d7f/structClipperLib_1_1TEdge.html
scraped_at: 2025-09-08T15:19:21.612494
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ClipperLib](../../df/db2/namespaceClipperLib.html)
  * [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html)

[List of all members](../../d7/db5/structClipperLib_1_1TEdge-members.html) | Public Attributes

ClipperLib::TEdge Struct Reference

##  Public Attributes  
  
---  
[IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | [Bot](../../d2/d7f/structClipperLib_1_1TEdge.html#adddb6b117ed14437613d26cc456bb4bc) {0,0}  
[IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | [Curr](../../d2/d7f/structClipperLib_1_1TEdge.html#ad5932926d3d5d6ed6ae4bc991ed7bcec) {0,0}  
[IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | [Delta](../../d2/d7f/structClipperLib_1_1TEdge.html#afeb7324b818fe9f667199bd18701e23c) {0,0}  
double | [Dx](../../d2/d7f/structClipperLib_1_1TEdge.html#ace215b877c384f917d18f6c1da913959) = 0.0  
[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * | [Next](../../d2/d7f/structClipperLib_1_1TEdge.html#af63cea19f1590922691d1a3a90e4173d) = nullptr  
[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * | [NextInAEL](../../d2/d7f/structClipperLib_1_1TEdge.html#a7281f59250f53e96099c1f636350bbd5) = nullptr  
[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * | [NextInLML](../../d2/d7f/structClipperLib_1_1TEdge.html#a1d0ad253e18e6fc82ed025e3d69b33de) = nullptr  
[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * | [NextInSEL](../../d2/d7f/structClipperLib_1_1TEdge.html#a167cd4d991d27f344d875ad6fd43b862) = nullptr  
[int](../../d1/da0/classint.html) | [OutIdx](../../d2/d7f/structClipperLib_1_1TEdge.html#a85d226803a3c54dbc983668f430b7e28) = 0  
[PolyType](../../df/db2/namespaceClipperLib.html#a50d662440e5e100070014ed91281e960) | [PolyTyp](../../d2/d7f/structClipperLib_1_1TEdge.html#aedc0a4d8b17ae3e42555621b22af8296) = [ptSubject](../../df/db2/namespaceClipperLib.html#a50d662440e5e100070014ed91281e960a67607ff4c7ca5fca8302236ff9a575b6)  
[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * | [Prev](../../d2/d7f/structClipperLib_1_1TEdge.html#a2713de57bcc285aaee2b9e1f5023bebc) = nullptr  
[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * | [PrevInAEL](../../d2/d7f/structClipperLib_1_1TEdge.html#a69a6d91641e91d87bf8fb658ab5b80d1) = nullptr  
[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * | [PrevInSEL](../../d2/d7f/structClipperLib_1_1TEdge.html#aa38f572c772d0bae50323f7890334c5f) = nullptr  
[EdgeSide](../../df/db2/namespaceClipperLib.html#a0e8e5a1032917a06fbbf958f7a708f3f) | [Side](../../d2/d7f/structClipperLib_1_1TEdge.html#aa7840242535b7830744f4387aa53bdfa) = [esLeft](../../df/db2/namespaceClipperLib.html#a0e8e5a1032917a06fbbf958f7a708f3fae0e35c98eb9b5e1ea1fd643a474c2ab4)  
[IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | [Top](../../d2/d7f/structClipperLib_1_1TEdge.html#a9f09500b780f7492d8c4c511aabf1c96) {0,0}  
[int](../../d1/da0/classint.html) | [WindCnt](../../d2/d7f/structClipperLib_1_1TEdge.html#ad7df0e20b58e4c6bddcfc7faf0003d4c) = 0  
[int](../../d1/da0/classint.html) | [WindCnt2](../../d2/d7f/structClipperLib_1_1TEdge.html#a50ccbb54513e60a39132dfca7c9b40f4) = 0  
[int](../../d1/da0/classint.html) | [WindDelta](../../d2/d7f/structClipperLib_1_1TEdge.html#afd72e2c7b9f97706ead72907509f8bc1) = 0  
  
## Member Data Documentation

## ◆ Bot

[IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html)
ClipperLib::TEdge::Bot {0,0}  
---  
  
Referenced by
[ClipperLib::ClipperBase::AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba),
[ClipperLib::FindNextLocMin()](../../df/db2/namespaceClipperLib.html#a6c2a946a9f927bfd364c95b561d4191c),
[ClipperLib::GetHorzDirection()](../../df/db2/namespaceClipperLib.html#a3a6a98076d47afe4c2e033833ae89bf5),
[ClipperLib::IntersectPoint()](../../df/db2/namespaceClipperLib.html#acc907411a778b9ae34f8d852aaa7622a),
[ClipperLib::ClipperBase::ProcessBound()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a292655c74a7e70a8b8829337c632bdf0),
and
[ClipperLib::TopX()](../../df/db2/namespaceClipperLib.html#a63e0b77cf7232cbd4f9909b25bd300be).

## ◆ Curr

[IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html)
ClipperLib::TEdge::Curr {0,0}  
---  
  
Referenced by
[ClipperLib::ClipperBase::AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba),
[ClipperLib::E2InsertsBeforeE1()](../../df/db2/namespaceClipperLib.html#ae002e65db41b2e12c6a29b6c53d95e3d),
[ClipperLib::FindNextLocMin()](../../df/db2/namespaceClipperLib.html#a6c2a946a9f927bfd364c95b561d4191c),
and
[ClipperLib::IntersectPoint()](../../df/db2/namespaceClipperLib.html#acc907411a778b9ae34f8d852aaa7622a).

## ◆ Delta

[IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html)
ClipperLib::TEdge::Delta {0,0}  
---  
  
Referenced by
[ClipperLib::IntersectPoint()](../../df/db2/namespaceClipperLib.html#acc907411a778b9ae34f8d852aaa7622a),
and
[ClipperLib::SlopesEqual()](../../df/db2/namespaceClipperLib.html#a052da0ab7e1690b61e36e007769df9f8).

## ◆ Dx

double ClipperLib::TEdge::Dx = 0.0  
---  
  
Referenced by
[ClipperLib::ClipperBase::AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba),
[ClipperLib::IntersectPoint()](../../df/db2/namespaceClipperLib.html#acc907411a778b9ae34f8d852aaa7622a),
and
[ClipperLib::TopX()](../../df/db2/namespaceClipperLib.html#a63e0b77cf7232cbd4f9909b25bd300be).

## ◆ Next

[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html)* ClipperLib::TEdge::Next
= nullptr  
---  
  
Referenced by
[ClipperLib::ClipperBase::AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba),
[ClipperLib::FindNextLocMin()](../../df/db2/namespaceClipperLib.html#a6c2a946a9f927bfd364c95b561d4191c),
and
[ClipperLib::ClipperBase::ProcessBound()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a292655c74a7e70a8b8829337c632bdf0).

## ◆ NextInAEL

[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html)*
ClipperLib::TEdge::NextInAEL = nullptr  
---  
  
## ◆ NextInLML

[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html)*
ClipperLib::TEdge::NextInLML = nullptr  
---  
  
Referenced by
[ClipperLib::ClipperBase::AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba),
and
[ClipperLib::ClipperBase::ProcessBound()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a292655c74a7e70a8b8829337c632bdf0).

## ◆ NextInSEL

[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html)*
ClipperLib::TEdge::NextInSEL = nullptr  
---  
  
Referenced by
[ClipperLib::EdgesAdjacent()](../../df/db2/namespaceClipperLib.html#a178785f2e51a19d1e6bdb8848d14b924).

## ◆ OutIdx

[int](../../d1/da0/classint.html) ClipperLib::TEdge::OutIdx = 0  
---  
  
Referenced by
[ClipperLib::ClipperBase::AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba),
[ClipperLib::ClipperBase::ProcessBound()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a292655c74a7e70a8b8829337c632bdf0),
and
[ClipperLib::SwapPolyIndexes()](../../df/db2/namespaceClipperLib.html#a17c02161ee129cdb347b0a6a18a73849).

## ◆ PolyTyp

[PolyType](../../df/db2/namespaceClipperLib.html#a50d662440e5e100070014ed91281e960)
ClipperLib::TEdge::PolyTyp =
[ptSubject](../../df/db2/namespaceClipperLib.html#a50d662440e5e100070014ed91281e960a67607ff4c7ca5fca8302236ff9a575b6)  
---  
  
## ◆ Prev

[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html)* ClipperLib::TEdge::Prev
= nullptr  
---  
  
Referenced by
[ClipperLib::ClipperBase::AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba),
[ClipperLib::FindNextLocMin()](../../df/db2/namespaceClipperLib.html#a6c2a946a9f927bfd364c95b561d4191c),
and
[ClipperLib::ClipperBase::ProcessBound()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a292655c74a7e70a8b8829337c632bdf0).

## ◆ PrevInAEL

[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html)*
ClipperLib::TEdge::PrevInAEL = nullptr  
---  
  
## ◆ PrevInSEL

[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html)*
ClipperLib::TEdge::PrevInSEL = nullptr  
---  
  
Referenced by
[ClipperLib::EdgesAdjacent()](../../df/db2/namespaceClipperLib.html#a178785f2e51a19d1e6bdb8848d14b924).

## ◆ Side

[EdgeSide](../../df/db2/namespaceClipperLib.html#a0e8e5a1032917a06fbbf958f7a708f3f)
ClipperLib::TEdge::Side =
[esLeft](../../df/db2/namespaceClipperLib.html#a0e8e5a1032917a06fbbf958f7a708f3fae0e35c98eb9b5e1ea1fd643a474c2ab4)  
---  
  
Referenced by
[ClipperLib::ClipperBase::AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba),
and
[ClipperLib::SwapSides()](../../df/db2/namespaceClipperLib.html#a63ceaffceda5d8e57ef98a0d7317b342).

## ◆ Top

[IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html)
ClipperLib::TEdge::Top {0,0}  
---  
  
Referenced by
[ClipperLib::ClipperBase::AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba),
[ClipperLib::E2InsertsBeforeE1()](../../df/db2/namespaceClipperLib.html#ae002e65db41b2e12c6a29b6c53d95e3d),
[ClipperLib::FindNextLocMin()](../../df/db2/namespaceClipperLib.html#a6c2a946a9f927bfd364c95b561d4191c),
[ClipperLib::GetHorzDirection()](../../df/db2/namespaceClipperLib.html#a3a6a98076d47afe4c2e033833ae89bf5),
[ClipperLib::IntersectPoint()](../../df/db2/namespaceClipperLib.html#acc907411a778b9ae34f8d852aaa7622a),
[ClipperLib::ClipperBase::ProcessBound()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a292655c74a7e70a8b8829337c632bdf0),
and
[ClipperLib::TopX()](../../df/db2/namespaceClipperLib.html#a63e0b77cf7232cbd4f9909b25bd300be).

## ◆ WindCnt

[int](../../d1/da0/classint.html) ClipperLib::TEdge::WindCnt = 0  
---  
  
## ◆ WindCnt2

[int](../../d1/da0/classint.html) ClipperLib::TEdge::WindCnt2 = 0  
---  
  
## ◆ WindDelta

[int](../../d1/da0/classint.html) ClipperLib::TEdge::WindDelta = 0  
---  
  
Referenced by
[ClipperLib::ClipperBase::ProcessBound()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a292655c74a7e70a8b8829337c632bdf0).

* * *

The documentation for this struct was generated from the following file:

  * FreeCAD/src/Mod/Path/libarea/clipper.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

