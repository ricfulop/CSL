---
url: https://freecad.github.io/SourceDoc/d6/d79/classClipperLib_1_1ClipperOffset.html
scraped_at: 2025-09-08T15:19:08.543944
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ClipperLib](../../df/db2/namespaceClipperLib.html)
  * [ClipperOffset](../../d6/d79/classClipperLib_1_1ClipperOffset.html)

[List of all members](../../d9/d58/classClipperLib_1_1ClipperOffset-members.html) | Public Member Functions | Public Attributes

ClipperLib::ClipperOffset Class Reference

`#include <clipper.hpp>`

##  Public Member Functions  
  
---  
void | [AddPath](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a0cd68e3690072f510924a5b25291043b) (const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &path, [JoinType](../../df/db2/namespaceClipperLib.html#ab3880a3ca1b45df3ce93ac315a74c06e) joinType, [EndType](../../df/db2/namespaceClipperLib.html#abee78a365e96a6edf45e15f885568079) endType)  
void | [AddPaths](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a18b35198f6370d76885af995ee2f16cb) (const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &paths, [JoinType](../../df/db2/namespaceClipperLib.html#ab3880a3ca1b45df3ce93ac315a74c06e) joinType, [EndType](../../df/db2/namespaceClipperLib.html#abee78a365e96a6edf45e15f885568079) endType)  
void | [Clear](../../d6/d79/classClipperLib_1_1ClipperOffset.html#ab444433587b6a3f6c89655938d889c7d) ()  
|
[ClipperOffset](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a45b4750989901db0c3865c374abdfcdc)
(double miterLimit=2.0, double roundPrecision=0.25)  
void | [Execute](../../d6/d79/classClipperLib_1_1ClipperOffset.html#ac591b25e483a52c99c3190a256ad4589) ([Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &solution, double delta)  
void | [Execute](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a3aaa9fcc20e503c967a23f1793536118) ([PolyTree](../../d3/d99/classClipperLib_1_1PolyTree.html) &solution, double delta)  
|
[~ClipperOffset](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a05b2d8d13e1148db74b681203a6ea76d)
()  
  
##  Public Attributes  
  
---  
double | [ArcTolerance](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a6c1735720b06e6b92dc25891014b2a92)  
double | [MiterLimit](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a36b3bf4571e5b831edd584cbcb179246)  
  
## Constructor & Destructor Documentation

## ◆ ClipperOffset()

ClipperLib::ClipperOffset::ClipperOffset  | ( | double  | _miterLimit_ = `2.0`,   
---|---|---|---  
|  | double  | _roundPrecision_ = `0.25`  
| ) | |   
  
References
[ArcTolerance](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a6c1735720b06e6b92dc25891014b2a92),
[MiterLimit](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a36b3bf4571e5b831edd584cbcb179246),
and
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6).

## ◆ ~ClipperOffset()

ClipperLib::ClipperOffset::~ClipperOffset  | ( | | ) |   
---|---|---|---|---  
  
References
[Clear()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#ab444433587b6a3f6c89655938d889c7d).

## Member Function Documentation

## ◆ AddPath()

void ClipperLib::ClipperOffset::AddPath  | ( | const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _path_ ,   
---|---|---|---  
|  | [JoinType](../../df/db2/namespaceClipperLib.html#ab3880a3ca1b45df3ce93ac315a74c06e) | _joinType_ ,   
|  | [EndType](../../df/db2/namespaceClipperLib.html#abee78a365e96a6edf45e15f885568079) | _endType_  
| ) | |   
  
References
[ClipperLib::PolyNode::ChildCount()](../../da/d87/classClipperLib_1_1PolyNode.html#a19128db6fb2aca66555231edaffa7ade),
[ClipperLib::PolyNode::Childs](../../da/d87/classClipperLib_1_1PolyNode.html#a7ac59aea508951a4c979bfca8913261d),
[ClipperLib::PolyNode::Contour](../../da/d87/classClipperLib_1_1PolyNode.html#a1d08b8a9499ff8cb89d5d63a12f881ea),
[ClipperLib::etClosedLine](../../df/db2/namespaceClipperLib.html#abee78a365e96a6edf45e15f885568079aa4b6951fbc935423f51f3acee30a4c5e),
[ClipperLib::etClosedPolygon](../../df/db2/namespaceClipperLib.html#abee78a365e96a6edf45e15f885568079abe139ce126eefdd24f9d947bd494404b),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

Referenced by
[AddPaths()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a18b35198f6370d76885af995ee2f16cb),
[AdaptivePath::Adaptive2d::Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071),
[AdaptivePath::ClearedArea::ExpandCleared()](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a880cf981ced9aa6c2021bee6d35fc58b),
and
[CArea::OffsetWithClipper()](../../d3/d52/classCArea.html#aa3bdef3b6eb55a436a1673479da035fb).

## ◆ AddPaths()

void ClipperLib::ClipperOffset::AddPaths  | ( | const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _paths_ ,   
---|---|---|---  
|  | [JoinType](../../df/db2/namespaceClipperLib.html#ab3880a3ca1b45df3ce93ac315a74c06e) | _joinType_ ,   
|  | [EndType](../../df/db2/namespaceClipperLib.html#abee78a365e96a6edf45e15f885568079) | _endType_  
| ) | |   
  
References
[AddPath()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a0cd68e3690072f510924a5b25291043b).

Referenced by
[AdaptivePath::Adaptive2d::Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071).

## ◆ Clear()

void ClipperLib::ClipperOffset::Clear  | ( | void  | | ) |   
---|---|---|---|---|---  
  
References
[ClipperLib::PolyNode::ChildCount()](../../da/d87/classClipperLib_1_1PolyNode.html#a19128db6fb2aca66555231edaffa7ade),
[ClipperLib::PolyNode::Childs](../../da/d87/classClipperLib_1_1PolyNode.html#a7ac59aea508951a4c979bfca8913261d),
and
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6).

Referenced by
[AdaptivePath::Adaptive2d::Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071),
[AdaptivePath::ClearedArea::ExpandCleared()](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a880cf981ced9aa6c2021bee6d35fc58b),
and
[~ClipperOffset()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a05b2d8d13e1148db74b681203a6ea76d).

## ◆ Execute() [1/2]

void ClipperLib::ClipperOffset::Execute  | ( | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _solution_ ,   
---|---|---|---  
|  | double  | _delta_  
| ) | |   
  
References
[ClipperLib::ClipperBase::AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba),
[ClipperLib::ClipperBase::AddPaths()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a2395967b47fb9f3f5846e2bf56c18f67),
[ClipperLib::ctUnion](../../df/db2/namespaceClipperLib.html#a3db4fddd50b81ba657107505821d7f46abb57d8284f7bf1cd7b902eae5b93c310),
[ClipperLib::Clipper::Execute()](../../d3/d1b/classClipperLib_1_1Clipper.html#a06da196a4b4151edd2e5426ed48744cf),
[ClipperLib::ClipperBase::GetBounds()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a5590a5454248ac3f6beeba7f9690f62e),
[ClipperLib::pftNegative](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7a02692db143e5586a360eb686c5d1b7c2),
[ClipperLib::pftPositive](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7a681ce5d4d05aff1ae01842b970fe7fe8),
[ClipperLib::ptSubject](../../df/db2/namespaceClipperLib.html#a50d662440e5e100070014ed91281e960a67607ff4c7ca5fca8302236ff9a575b6),
and
[ClipperLib::Clipper::ReverseSolution()](../../d3/d1b/classClipperLib_1_1Clipper.html#ad556ba9961f498de02d55dc95bc5a889).

Referenced by
[PathScripts.PathJobCmd.CommandJobCreate::Activated()](../../db/d17/classPathScripts_1_1PathJobCmd_1_1CommandJobCreate.html#aac9d774ebbcda6c9840a1b776045fd2f),
[AdaptivePath::Adaptive2d::Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071),
[AdaptivePath::ClearedArea::ExpandCleared()](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a880cf981ced9aa6c2021bee6d35fc58b),
[CArea::OffsetWithClipper()](../../d3/d52/classCArea.html#aa3bdef3b6eb55a436a1673479da035fb),
and
[PathScripts.PathJobCmd.CommandJobTemplateExport::SaveDialog()](../../d7/d23/classPathScripts_1_1PathJobCmd_1_1CommandJobTemplateExport.html#a208b7ff58f9cc81651d8ae05fe9c44af).

## ◆ Execute() [2/2]

void ClipperLib::ClipperOffset::Execute  | ( | [PolyTree](../../d3/d99/classClipperLib_1_1PolyTree.html) & | _solution_ ,   
---|---|---|---  
|  | double  | _delta_  
| ) | |   
  
References
[ClipperLib::ClipperBase::AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba),
[ClipperLib::ClipperBase::AddPaths()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a2395967b47fb9f3f5846e2bf56c18f67),
[ClipperLib::PolyNode::ChildCount()](../../da/d87/classClipperLib_1_1PolyNode.html#a19128db6fb2aca66555231edaffa7ade),
[ClipperLib::PolyNode::Childs](../../da/d87/classClipperLib_1_1PolyNode.html#a7ac59aea508951a4c979bfca8913261d),
[ClipperLib::PolyTree::Clear()](../../d3/d99/classClipperLib_1_1PolyTree.html#a8620ea631d478b3c43274ac084902ec4),
[ClipperLib::ctUnion](../../df/db2/namespaceClipperLib.html#a3db4fddd50b81ba657107505821d7f46abb57d8284f7bf1cd7b902eae5b93c310),
[ClipperLib::Clipper::Execute()](../../d3/d1b/classClipperLib_1_1Clipper.html#a06da196a4b4151edd2e5426ed48744cf),
[ClipperLib::ClipperBase::GetBounds()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a5590a5454248ac3f6beeba7f9690f62e),
[ClipperLib::pftNegative](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7a02692db143e5586a360eb686c5d1b7c2),
[ClipperLib::pftPositive](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7a681ce5d4d05aff1ae01842b970fe7fe8),
[ClipperLib::ptSubject](../../df/db2/namespaceClipperLib.html#a50d662440e5e100070014ed91281e960a67607ff4c7ca5fca8302236ff9a575b6),
and
[ClipperLib::Clipper::ReverseSolution()](../../d3/d1b/classClipperLib_1_1Clipper.html#ad556ba9961f498de02d55dc95bc5a889).

Referenced by
[PathScripts.PathJobCmd.CommandJobCreate::Activated()](../../db/d17/classPathScripts_1_1PathJobCmd_1_1CommandJobCreate.html#aac9d774ebbcda6c9840a1b776045fd2f),
and
[PathScripts.PathJobCmd.CommandJobTemplateExport::SaveDialog()](../../d7/d23/classPathScripts_1_1PathJobCmd_1_1CommandJobTemplateExport.html#a208b7ff58f9cc81651d8ae05fe9c44af).

## Member Data Documentation

## ◆ ArcTolerance

double ClipperLib::ClipperOffset::ArcTolerance  
---  
  
Referenced by
[ClipperOffset()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a45b4750989901db0c3865c374abdfcdc).

## ◆ MiterLimit

double ClipperLib::ClipperOffset::MiterLimit  
---  
  
Referenced by
[ClipperOffset()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a45b4750989901db0c3865c374abdfcdc).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Mod/Path/libarea/clipper.hpp
  * FreeCAD/src/Mod/Path/libarea/clipper.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

