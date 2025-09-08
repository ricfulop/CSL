---
url: https://freecad.github.io/SourceDoc/d9/da0/classClipperLib_1_1ClipperBase.html
scraped_at: 2025-09-08T15:19:06.572092
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ClipperLib](../../df/db2/namespaceClipperLib.html)
  * [ClipperBase](../../d9/da0/classClipperLib_1_1ClipperBase.html)

[List of all members](../../d8/dfc/classClipperLib_1_1ClipperBase-members.html) | Public Member Functions | Protected Types | Protected Member Functions | Protected Attributes

ClipperLib::ClipperBase Class Reference

`#include <clipper.hpp>`

##  Public Member Functions  
  
---  
[bool](../../d9/db9/classbool.html) | [AddPath](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba) (const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &pg, [PolyType](../../df/db2/namespaceClipperLib.html#a50d662440e5e100070014ed91281e960) PolyTyp, [bool](../../d9/db9/classbool.html) Closed)  
[bool](../../d9/db9/classbool.html) | [AddPaths](../../d9/da0/classClipperLib_1_1ClipperBase.html#a2395967b47fb9f3f5846e2bf56c18f67) (const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &ppg, [PolyType](../../df/db2/namespaceClipperLib.html#a50d662440e5e100070014ed91281e960) PolyTyp, [bool](../../d9/db9/classbool.html) Closed)  
virtual void | [Clear](../../d9/da0/classClipperLib_1_1ClipperBase.html#a5690952fe8c2cb047025566405827821) ()  
|
[ClipperBase](../../d9/da0/classClipperLib_1_1ClipperBase.html#ab7144fc592427238c55ae81061e895a2)
()  
[IntRect](../../d7/d16/structClipperLib_1_1IntRect.html) | [GetBounds](../../d9/da0/classClipperLib_1_1ClipperBase.html#a5590a5454248ac3f6beeba7f9690f62e) ()  
[bool](../../d9/db9/classbool.html) | [PreserveCollinear](../../d9/da0/classClipperLib_1_1ClipperBase.html#a95c47199aeb139b13059968bc6056f44) ()  
void | [PreserveCollinear](../../d9/da0/classClipperLib_1_1ClipperBase.html#aa827cfffd9be40dba7d503a3da708b91) ([bool](../../d9/db9/classbool.html) value)  
virtual | [~ClipperBase](../../d9/da0/classClipperLib_1_1ClipperBase.html#ae73a6a12fb3e7e62b59d1ff38135b27c) ()  
  
##  Protected Types  
  
---  
typedef std::vector< [LocalMinimum](../../d0/d4a/structClipperLib_1_1LocalMinimum.html) > | [MinimaList](../../d9/da0/classClipperLib_1_1ClipperBase.html#addb22572066d3983dcd5797c542df00b)  
  
##  Protected Member Functions  
  
---  
[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * | [AddBoundsToLML](../../d9/da0/classClipperLib_1_1ClipperBase.html#a66f47d6317d1266200363ea06a457663) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *e, [bool](../../d9/db9/classbool.html) IsClosed)  
void | [AscendToMax](../../d9/da0/classClipperLib_1_1ClipperBase.html#afafbf0dafffb5ad6f5a5c30dbed6378f) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *&E, [bool](../../d9/db9/classbool.html) Appending, [bool](../../d9/db9/classbool.html) IsClosed)  
[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * | [DescendToMin](../../d9/da0/classClipperLib_1_1ClipperBase.html#aff108948d9216d9621ac6904cd880cf3) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *&E)  
void | [DisposeLocalMinimaList](../../d9/da0/classClipperLib_1_1ClipperBase.html#a311dbbec1454ab7965e363a0359f5ee4) ()  
void | [DoMinimaLML](../../d9/da0/classClipperLib_1_1ClipperBase.html#ae57efb542cfbbc42d000815e8a2e2877) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *E1, [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *E2, [bool](../../d9/db9/classbool.html) IsClosed)  
void | [PopLocalMinima](../../d9/da0/classClipperLib_1_1ClipperBase.html#a9554e9f2273c39e0f5f07d3cd73533e6) ()  
[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * | [ProcessBound](../../d9/da0/classClipperLib_1_1ClipperBase.html#a292655c74a7e70a8b8829337c632bdf0) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *E, [bool](../../d9/db9/classbool.html) IsClockwise)  
virtual void | [Reset](../../d9/da0/classClipperLib_1_1ClipperBase.html#a125febb065f23fc55dafffe8d185b642) ()  
  
##  Protected Attributes  
  
---  
MinimaList::iterator | [m_CurrentLM](../../d9/da0/classClipperLib_1_1ClipperBase.html#ab6ed40f62810c0f894878c79d74afb36)  
[EdgeList](../../df/db2/namespaceClipperLib.html#a86ece3ad074061d6b3d18819b1fa4ed7) | [m_edges](../../d9/da0/classClipperLib_1_1ClipperBase.html#a8bfc007c0c0afd4e9d252dac0ef5daa0)  
[bool](../../d9/db9/classbool.html) | [m_HasOpenPaths](../../d9/da0/classClipperLib_1_1ClipperBase.html#aa2508f5b2a599294c359271506441fbd)  
[MinimaList](../../d9/da0/classClipperLib_1_1ClipperBase.html#addb22572066d3983dcd5797c542df00b) | [m_MinimaList](../../d9/da0/classClipperLib_1_1ClipperBase.html#a970749dc12a20e980c932af040f8a8c5)  
[bool](../../d9/db9/classbool.html) | [m_PreserveCollinear](../../d9/da0/classClipperLib_1_1ClipperBase.html#aad4ca0f2a16a6fb466036b36cc5ff638)  
[bool](../../d9/db9/classbool.html) | [m_UseFullRange](../../d9/da0/classClipperLib_1_1ClipperBase.html#aea11d183617adc12d7ba2b84533f7f45)  
  
## Member Typedef Documentation

## ◆ MinimaList

| typedef
std::vector<[LocalMinimum](../../d0/d4a/structClipperLib_1_1LocalMinimum.html)>
[ClipperLib::ClipperBase::MinimaList](../../d9/da0/classClipperLib_1_1ClipperBase.html#addb22572066d3983dcd5797c542df00b)  
---  
protected  
  
## Constructor & Destructor Documentation

## ◆ ClipperBase()

ClipperLib::ClipperBase::ClipperBase  | ( | | ) |   
---|---|---|---|---  
  
References
[m_CurrentLM](../../d9/da0/classClipperLib_1_1ClipperBase.html#ab6ed40f62810c0f894878c79d74afb36),
[m_HasOpenPaths](../../d9/da0/classClipperLib_1_1ClipperBase.html#aa2508f5b2a599294c359271506441fbd),
[m_MinimaList](../../d9/da0/classClipperLib_1_1ClipperBase.html#a970749dc12a20e980c932af040f8a8c5),
[m_PreserveCollinear](../../d9/da0/classClipperLib_1_1ClipperBase.html#aad4ca0f2a16a6fb466036b36cc5ff638),
and
[m_UseFullRange](../../d9/da0/classClipperLib_1_1ClipperBase.html#aea11d183617adc12d7ba2b84533f7f45).

## ◆ ~ClipperBase()

| ClipperLib::ClipperBase::~ClipperBase  | ( | | ) |   
---|---|---|---|---  
virtual  
  
References
[Clear()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a5690952fe8c2cb047025566405827821).

## Member Function Documentation

## ◆ AddBoundsToLML()

| [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * ClipperLib::ClipperBase::AddBoundsToLML  | ( | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *  | _e_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _IsClosed_  
| ) | |   
protected  
  
## ◆ AddPath()

[bool](../../d9/db9/classbool.html) ClipperLib::ClipperBase::AddPath  | ( | const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _pg_ ,   
---|---|---|---  
|  | [PolyType](../../df/db2/namespaceClipperLib.html#a50d662440e5e100070014ed91281e960) | _PolyTyp_ ,   
|  | [bool](../../d9/db9/classbool.html) | _Closed_  
| ) | |   
  
References
[ClipperLib::TEdge::Bot](../../d2/d7f/structClipperLib_1_1TEdge.html#adddb6b117ed14437613d26cc456bb4bc),
[ClipperLib::TEdge::Curr](../../d2/d7f/structClipperLib_1_1TEdge.html#ad5932926d3d5d6ed6ae4bc991ed7bcec),
[ClipperLib::TEdge::Dx](../../d2/d7f/structClipperLib_1_1TEdge.html#ace215b877c384f917d18f6c1da913959),
[ClipperLib::esLeft](../../df/db2/namespaceClipperLib.html#a0e8e5a1032917a06fbbf958f7a708f3fae0e35c98eb9b5e1ea1fd643a474c2ab4),
[ClipperLib::esRight](../../df/db2/namespaceClipperLib.html#a0e8e5a1032917a06fbbf958f7a708f3fae755211893cad1da40ec2f0d2dbd9c32),
[ClipperLib::FindNextLocMin()](../../df/db2/namespaceClipperLib.html#a6c2a946a9f927bfd364c95b561d4191c),
[ClipperLib::InitEdge()](../../df/db2/namespaceClipperLib.html#a1b822f020efce65b1e0c4fcdb264fd35),
[ClipperLib::InitEdge2()](../../df/db2/namespaceClipperLib.html#ae5ad4a2545fa1528f81bd2a89d9cddcb),
[m_edges](../../d9/da0/classClipperLib_1_1ClipperBase.html#a8bfc007c0c0afd4e9d252dac0ef5daa0),
[m_HasOpenPaths](../../d9/da0/classClipperLib_1_1ClipperBase.html#aa2508f5b2a599294c359271506441fbd),
[m_MinimaList](../../d9/da0/classClipperLib_1_1ClipperBase.html#a970749dc12a20e980c932af040f8a8c5),
[m_PreserveCollinear](../../d9/da0/classClipperLib_1_1ClipperBase.html#aad4ca0f2a16a6fb466036b36cc5ff638),
[m_UseFullRange](../../d9/da0/classClipperLib_1_1ClipperBase.html#aea11d183617adc12d7ba2b84533f7f45),
[ClipperLib::TEdge::Next](../../d2/d7f/structClipperLib_1_1TEdge.html#af63cea19f1590922691d1a3a90e4173d),
[ClipperLib::TEdge::NextInLML](../../d2/d7f/structClipperLib_1_1TEdge.html#a1d0ad253e18e6fc82ed025e3d69b33de),
[ClipperLib::TEdge::OutIdx](../../d2/d7f/structClipperLib_1_1TEdge.html#a85d226803a3c54dbc983668f430b7e28),
[ClipperLib::TEdge::Prev](../../d2/d7f/structClipperLib_1_1TEdge.html#a2713de57bcc285aaee2b9e1f5023bebc),
[ProcessBound()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a292655c74a7e70a8b8829337c632bdf0),
[ClipperLib::Pt2IsBetweenPt1AndPt3()](../../df/db2/namespaceClipperLib.html#a0a448254ee6419dfde0a539080502d88),
[ClipperLib::ptClip](../../df/db2/namespaceClipperLib.html#a50d662440e5e100070014ed91281e960a33152b07d096815ff64f4aeab67f0335),
[ClipperLib::RangeTest()](../../df/db2/namespaceClipperLib.html#add09a980dfa1da81e1693a55cd912908),
[ClipperLib::RemoveEdge()](../../df/db2/namespaceClipperLib.html#a618e13d6a0fc1230b030ac02d70a2e0a),
[ClipperLib::ReverseHorizontal()](../../df/db2/namespaceClipperLib.html#a308e107fa8e429684f57440687d77adc),
[ClipperLib::TEdge::Side](../../d2/d7f/structClipperLib_1_1TEdge.html#aa7840242535b7830744f4387aa53bdfa),
[ClipperLib::Skip](../../df/db2/namespaceClipperLib.html#a6e9f2a3266e14dced8a5fee78224c1bf),
[ClipperLib::SlopesEqual()](../../df/db2/namespaceClipperLib.html#a052da0ab7e1690b61e36e007769df9f8),
[ClipperLib::TEdge::Top](../../d2/d7f/structClipperLib_1_1TEdge.html#a9f09500b780f7492d8c4c511aabf1c96),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

Referenced by
[AddPaths()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a2395967b47fb9f3f5846e2bf56c18f67),
[AdaptivePath::Adaptive2d::Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071),
[ClipperLib::ClipperOffset::Execute()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#ac591b25e483a52c99c3190a256ad4589),
and
[AdaptivePath::ClearedArea::GetBoundedClearedAreaClipped()](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a396af78fc129b33fe0c3730caadc9503).

## ◆ AddPaths()

[bool](../../d9/db9/classbool.html) ClipperLib::ClipperBase::AddPaths  | ( | const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _ppg_ ,   
---|---|---|---  
|  | [PolyType](../../df/db2/namespaceClipperLib.html#a50d662440e5e100070014ed91281e960) | _PolyTyp_ ,   
|  | [bool](../../d9/db9/classbool.html) | _Closed_  
| ) | |   
  
References
[AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba).

Referenced by
[AdaptivePath::Adaptive2d::Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071),
[ClipperLib::ClipperOffset::Execute()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#ac591b25e483a52c99c3190a256ad4589),
[AdaptivePath::ClearedArea::ExpandCleared()](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a880cf981ced9aa6c2021bee6d35fc58b),
[AdaptivePath::ClearedArea::GetBoundedClearedAreaClipped()](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a396af78fc129b33fe0c3730caadc9503),
[ClipperLib::MinkowskiDiff()](../../df/db2/namespaceClipperLib.html#a76dac24102863220c7bc13be222a1dda),
and
[ClipperLib::MinkowskiSum()](../../df/db2/namespaceClipperLib.html#ad12b5697c25579dce65d369a2e3cf608).

## ◆ AscendToMax()

| void ClipperLib::ClipperBase::AscendToMax  | ( | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *& | _E_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _Appending_ ,   
|  | [bool](../../d9/db9/classbool.html) | _IsClosed_  
| ) | |   
protected  
  
## ◆ Clear()

| void ClipperLib::ClipperBase::Clear  | ( | void  | | ) |   
---|---|---|---|---|---  
virtual  
  
References
[DisposeLocalMinimaList()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a311dbbec1454ab7965e363a0359f5ee4),
[m_edges](../../d9/da0/classClipperLib_1_1ClipperBase.html#a8bfc007c0c0afd4e9d252dac0ef5daa0),
[m_HasOpenPaths](../../d9/da0/classClipperLib_1_1ClipperBase.html#aa2508f5b2a599294c359271506441fbd),
and
[m_UseFullRange](../../d9/da0/classClipperLib_1_1ClipperBase.html#aea11d183617adc12d7ba2b84533f7f45).

Referenced by
[AdaptivePath::Adaptive2d::Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071),
[AdaptivePath::ClearedArea::ExpandCleared()](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a880cf981ced9aa6c2021bee6d35fc58b),
[AdaptivePath::ClearedArea::GetBoundedClearedAreaClipped()](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a396af78fc129b33fe0c3730caadc9503),
[ClipperLib::Clipper::~Clipper()](../../d3/d1b/classClipperLib_1_1Clipper.html#af7e75828307cef83465fd72285346563),
and
[~ClipperBase()](../../d9/da0/classClipperLib_1_1ClipperBase.html#ae73a6a12fb3e7e62b59d1ff38135b27c).

## ◆ DescendToMin()

| [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * ClipperLib::ClipperBase::DescendToMin  | ( | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *& | _E_| ) |   
---|---|---|---|---|---  
protected  
  
## ◆ DisposeLocalMinimaList()

| void ClipperLib::ClipperBase::DisposeLocalMinimaList  | ( | | ) |   
---|---|---|---|---  
protected  
  
References
[m_CurrentLM](../../d9/da0/classClipperLib_1_1ClipperBase.html#ab6ed40f62810c0f894878c79d74afb36),
and
[m_MinimaList](../../d9/da0/classClipperLib_1_1ClipperBase.html#a970749dc12a20e980c932af040f8a8c5).

Referenced by
[Clear()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a5690952fe8c2cb047025566405827821).

## ◆ DoMinimaLML()

| void ClipperLib::ClipperBase::DoMinimaLML  | ( | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *  | _E1_ ,   
---|---|---|---  
|  | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *  | _E2_ ,   
|  | [bool](../../d9/db9/classbool.html) | _IsClosed_  
| ) | |   
protected  
  
## ◆ GetBounds()

[IntRect](../../d7/d16/structClipperLib_1_1IntRect.html) ClipperLib::ClipperBase::GetBounds  | ( | | ) |   
---|---|---|---|---  
  
References
[m_MinimaList](../../d9/da0/classClipperLib_1_1ClipperBase.html#a970749dc12a20e980c932af040f8a8c5).

Referenced by
[ClipperLib::ClipperOffset::Execute()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#ac591b25e483a52c99c3190a256ad4589).

## ◆ PopLocalMinima()

| void ClipperLib::ClipperBase::PopLocalMinima  | ( | | ) |   
---|---|---|---|---  
protected  
  
References
[m_CurrentLM](../../d9/da0/classClipperLib_1_1ClipperBase.html#ab6ed40f62810c0f894878c79d74afb36),
and
[m_MinimaList](../../d9/da0/classClipperLib_1_1ClipperBase.html#a970749dc12a20e980c932af040f8a8c5).

## ◆ PreserveCollinear() [1/2]

[bool](../../d9/db9/classbool.html) ClipperLib::ClipperBase::PreserveCollinear  | ( | | ) |   
---|---|---|---|---  
  
References
[m_PreserveCollinear](../../d9/da0/classClipperLib_1_1ClipperBase.html#aad4ca0f2a16a6fb466036b36cc5ff638).

## ◆ PreserveCollinear() [2/2]

void ClipperLib::ClipperBase::PreserveCollinear  | ( | [bool](../../d9/db9/classbool.html) | _value_| ) |   
---|---|---|---|---|---  
  
References
[m_PreserveCollinear](../../d9/da0/classClipperLib_1_1ClipperBase.html#aad4ca0f2a16a6fb466036b36cc5ff638).

## ◆ ProcessBound()

| [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * ClipperLib::ClipperBase::ProcessBound  | ( | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *  | _E_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _IsClockwise_  
| ) | |   
protected  
  
References
[ClipperLib::TEdge::Bot](../../d2/d7f/structClipperLib_1_1TEdge.html#adddb6b117ed14437613d26cc456bb4bc),
[ClipperLib::IsHorizontal()](../../df/db2/namespaceClipperLib.html#af9afcf65d7038ec26bf32b7d0c312c37),
[m_MinimaList](../../d9/da0/classClipperLib_1_1ClipperBase.html#a970749dc12a20e980c932af040f8a8c5),
[ClipperLib::TEdge::Next](../../d2/d7f/structClipperLib_1_1TEdge.html#af63cea19f1590922691d1a3a90e4173d),
[ClipperLib::TEdge::NextInLML](../../d2/d7f/structClipperLib_1_1TEdge.html#a1d0ad253e18e6fc82ed025e3d69b33de),
[ClipperLib::TEdge::OutIdx](../../d2/d7f/structClipperLib_1_1TEdge.html#a85d226803a3c54dbc983668f430b7e28),
[ClipperLib::TEdge::Prev](../../d2/d7f/structClipperLib_1_1TEdge.html#a2713de57bcc285aaee2b9e1f5023bebc),
[ProcessBound()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a292655c74a7e70a8b8829337c632bdf0),
[ClipperLib::ReverseHorizontal()](../../df/db2/namespaceClipperLib.html#a308e107fa8e429684f57440687d77adc),
[ClipperLib::Skip](../../df/db2/namespaceClipperLib.html#a6e9f2a3266e14dced8a5fee78224c1bf),
[ClipperLib::TEdge::Top](../../d2/d7f/structClipperLib_1_1TEdge.html#a9f09500b780f7492d8c4c511aabf1c96),
[ClipperLib::TEdge::WindDelta](../../d2/d7f/structClipperLib_1_1TEdge.html#afd72e2c7b9f97706ead72907509f8bc1),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

Referenced by
[AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba),
and
[ProcessBound()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a292655c74a7e70a8b8829337c632bdf0).

## ◆ Reset()

| void ClipperLib::ClipperBase::Reset  | ( | | ) |   
---|---|---|---|---  
protectedvirtual  
  
Reimplemented in
[ClipperLib::Clipper](../../d3/d1b/classClipperLib_1_1Clipper.html#a14c704b062e8a079e34a8ce40838861e).

References
[ClipperLib::esLeft](../../df/db2/namespaceClipperLib.html#a0e8e5a1032917a06fbbf958f7a708f3fae0e35c98eb9b5e1ea1fd643a474c2ab4),
[ClipperLib::esRight](../../df/db2/namespaceClipperLib.html#a0e8e5a1032917a06fbbf958f7a708f3fae755211893cad1da40ec2f0d2dbd9c32),
[m_CurrentLM](../../d9/da0/classClipperLib_1_1ClipperBase.html#ab6ed40f62810c0f894878c79d74afb36),
[m_MinimaList](../../d9/da0/classClipperLib_1_1ClipperBase.html#a970749dc12a20e980c932af040f8a8c5),
and
[ClipperLib::Unassigned](../../df/db2/namespaceClipperLib.html#ae8c8149f9414a1459f7691ecd2f94669).

Referenced by
[ClipperLib::Clipper::Reset()](../../d3/d1b/classClipperLib_1_1Clipper.html#a14c704b062e8a079e34a8ce40838861e).

## Member Data Documentation

## ◆ m_CurrentLM

| MinimaList::iterator ClipperLib::ClipperBase::m_CurrentLM  
---  
protected  
  
Referenced by
[ClipperBase()](../../d9/da0/classClipperLib_1_1ClipperBase.html#ab7144fc592427238c55ae81061e895a2),
[DisposeLocalMinimaList()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a311dbbec1454ab7965e363a0359f5ee4),
[ClipperLib::Clipper::ExecuteInternal()](../../d3/d1b/classClipperLib_1_1Clipper.html#a3e8757e5f8a6ffcb7fd0f9630fde02d3),
[PopLocalMinima()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a9554e9f2273c39e0f5f07d3cd73533e6),
and
[Reset()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a125febb065f23fc55dafffe8d185b642).

## ◆ m_edges

|
[EdgeList](../../df/db2/namespaceClipperLib.html#a86ece3ad074061d6b3d18819b1fa4ed7)
ClipperLib::ClipperBase::m_edges  
---  
protected  
  
Referenced by
[AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba),
and
[Clear()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a5690952fe8c2cb047025566405827821).

## ◆ m_HasOpenPaths

| [bool](../../d9/db9/classbool.html) ClipperLib::ClipperBase::m_HasOpenPaths  
---  
protected  
  
Referenced by
[AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba),
[Clear()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a5690952fe8c2cb047025566405827821),
[ClipperLib::Clipper::Clipper()](../../d3/d1b/classClipperLib_1_1Clipper.html#adceb8536f6a80e8f115213dba9208427),
[ClipperBase()](../../d9/da0/classClipperLib_1_1ClipperBase.html#ab7144fc592427238c55ae81061e895a2),
and
[ClipperLib::Clipper::Execute()](../../d3/d1b/classClipperLib_1_1Clipper.html#a06da196a4b4151edd2e5426ed48744cf).

## ◆ m_MinimaList

|
[MinimaList](../../d9/da0/classClipperLib_1_1ClipperBase.html#addb22572066d3983dcd5797c542df00b)
ClipperLib::ClipperBase::m_MinimaList  
---  
protected  
  
Referenced by
[AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba),
[ClipperBase()](../../d9/da0/classClipperLib_1_1ClipperBase.html#ab7144fc592427238c55ae81061e895a2),
[DisposeLocalMinimaList()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a311dbbec1454ab7965e363a0359f5ee4),
[ClipperLib::Clipper::ExecuteInternal()](../../d3/d1b/classClipperLib_1_1Clipper.html#a3e8757e5f8a6ffcb7fd0f9630fde02d3),
[GetBounds()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a5590a5454248ac3f6beeba7f9690f62e),
[PopLocalMinima()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a9554e9f2273c39e0f5f07d3cd73533e6),
[ProcessBound()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a292655c74a7e70a8b8829337c632bdf0),
[Reset()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a125febb065f23fc55dafffe8d185b642),
and
[ClipperLib::Clipper::Reset()](../../d3/d1b/classClipperLib_1_1Clipper.html#a14c704b062e8a079e34a8ce40838861e).

## ◆ m_PreserveCollinear

| [bool](../../d9/db9/classbool.html)
ClipperLib::ClipperBase::m_PreserveCollinear  
---  
protected  
  
Referenced by
[AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba),
[ClipperLib::Clipper::Clipper()](../../d3/d1b/classClipperLib_1_1Clipper.html#adceb8536f6a80e8f115213dba9208427),
[ClipperBase()](../../d9/da0/classClipperLib_1_1ClipperBase.html#ab7144fc592427238c55ae81061e895a2),
and
[PreserveCollinear()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a95c47199aeb139b13059968bc6056f44).

## ◆ m_UseFullRange

| [bool](../../d9/db9/classbool.html) ClipperLib::ClipperBase::m_UseFullRange  
---  
protected  
  
Referenced by
[AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba),
[Clear()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a5690952fe8c2cb047025566405827821),
[ClipperLib::Clipper::Clipper()](../../d3/d1b/classClipperLib_1_1Clipper.html#adceb8536f6a80e8f115213dba9208427),
and
[ClipperBase()](../../d9/da0/classClipperLib_1_1ClipperBase.html#ab7144fc592427238c55ae81061e895a2).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Mod/Path/libarea/clipper.hpp
  * FreeCAD/src/Mod/Path/libarea/clipper.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

