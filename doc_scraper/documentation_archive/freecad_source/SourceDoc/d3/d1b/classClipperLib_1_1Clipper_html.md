---
url: https://freecad.github.io/SourceDoc/d3/d1b/classClipperLib_1_1Clipper.html
scraped_at: 2025-09-08T15:19:05.560367
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ClipperLib](../../df/db2/namespaceClipperLib.html)
  * [Clipper](../../d3/d1b/classClipperLib_1_1Clipper.html)

[List of all members](../../de/df1/classClipperLib_1_1Clipper-members.html) | Public Member Functions | Protected Member Functions

ClipperLib::Clipper Class Reference

`#include <clipper.hpp>`

##  Public Member Functions  
  
---  
|
[Clipper](../../d3/d1b/classClipperLib_1_1Clipper.html#adceb8536f6a80e8f115213dba9208427)
([int](../../d1/da0/classint.html) initOptions=0)  
[bool](../../d9/db9/classbool.html) | [Execute](../../d3/d1b/classClipperLib_1_1Clipper.html#a06da196a4b4151edd2e5426ed48744cf) ([ClipType](../../df/db2/namespaceClipperLib.html#a3db4fddd50b81ba657107505821d7f46) clipType, [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &solution, [PolyFillType](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7) subjFillType=[pftEvenOdd](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7acede4475518a377720537448c7b2df73), [PolyFillType](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7) clipFillType=[pftEvenOdd](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7acede4475518a377720537448c7b2df73))  
[bool](../../d9/db9/classbool.html) | [Execute](../../d3/d1b/classClipperLib_1_1Clipper.html#aceb19a1e5a5c9e31067f4d1177793403) ([ClipType](../../df/db2/namespaceClipperLib.html#a3db4fddd50b81ba657107505821d7f46) clipType, [PolyTree](../../d3/d99/classClipperLib_1_1PolyTree.html) &polytree, [PolyFillType](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7) subjFillType=[pftEvenOdd](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7acede4475518a377720537448c7b2df73), [PolyFillType](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7) clipFillType=[pftEvenOdd](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7acede4475518a377720537448c7b2df73))  
[bool](../../d9/db9/classbool.html) | [ReverseSolution](../../d3/d1b/classClipperLib_1_1Clipper.html#ad556ba9961f498de02d55dc95bc5a889) ()  
void | [ReverseSolution](../../d3/d1b/classClipperLib_1_1Clipper.html#a44afc0c82a1d2607829b5fd21f7644ef) ([bool](../../d9/db9/classbool.html) value)  
[bool](../../d9/db9/classbool.html) | [StrictlySimple](../../d3/d1b/classClipperLib_1_1Clipper.html#a50eb4c514466ed37fd365769e0bcf67b) ()  
void | [StrictlySimple](../../d3/d1b/classClipperLib_1_1Clipper.html#a85aa82d75e0d7d1f380d2e96231d6aa3) ([bool](../../d9/db9/classbool.html) value)  
|
[~Clipper](../../d3/d1b/classClipperLib_1_1Clipper.html#af7e75828307cef83465fd72285346563)
()  
![-](../../closed.png) Public Member Functions inherited from
[ClipperLib::ClipperBase](../../d9/da0/classClipperLib_1_1ClipperBase.html)  
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
  
##  Protected Member Functions  
  
---  
virtual [bool](../../d9/db9/classbool.html) | [ExecuteInternal](../../d3/d1b/classClipperLib_1_1Clipper.html#a3e8757e5f8a6ffcb7fd0f9630fde02d3) ()  
void | [Reset](../../d3/d1b/classClipperLib_1_1Clipper.html#a14c704b062e8a079e34a8ce40838861e) ()  
![-](../../closed.png) Protected Member Functions inherited from
[ClipperLib::ClipperBase](../../d9/da0/classClipperLib_1_1ClipperBase.html)  
[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * | [AddBoundsToLML](../../d9/da0/classClipperLib_1_1ClipperBase.html#a66f47d6317d1266200363ea06a457663) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *e, [bool](../../d9/db9/classbool.html) IsClosed)  
void | [AscendToMax](../../d9/da0/classClipperLib_1_1ClipperBase.html#afafbf0dafffb5ad6f5a5c30dbed6378f) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *&E, [bool](../../d9/db9/classbool.html) Appending, [bool](../../d9/db9/classbool.html) IsClosed)  
[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * | [DescendToMin](../../d9/da0/classClipperLib_1_1ClipperBase.html#aff108948d9216d9621ac6904cd880cf3) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *&E)  
void | [DisposeLocalMinimaList](../../d9/da0/classClipperLib_1_1ClipperBase.html#a311dbbec1454ab7965e363a0359f5ee4) ()  
void | [DoMinimaLML](../../d9/da0/classClipperLib_1_1ClipperBase.html#ae57efb542cfbbc42d000815e8a2e2877) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *E1, [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *E2, [bool](../../d9/db9/classbool.html) IsClosed)  
void | [PopLocalMinima](../../d9/da0/classClipperLib_1_1ClipperBase.html#a9554e9f2273c39e0f5f07d3cd73533e6) ()  
[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * | [ProcessBound](../../d9/da0/classClipperLib_1_1ClipperBase.html#a292655c74a7e70a8b8829337c632bdf0) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *E, [bool](../../d9/db9/classbool.html) IsClockwise)  
virtual void | [Reset](../../d9/da0/classClipperLib_1_1ClipperBase.html#a125febb065f23fc55dafffe8d185b642) ()  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Protected Types inherited from
[ClipperLib::ClipperBase](../../d9/da0/classClipperLib_1_1ClipperBase.html)  
typedef std::vector< [LocalMinimum](../../d0/d4a/structClipperLib_1_1LocalMinimum.html) > | [MinimaList](../../d9/da0/classClipperLib_1_1ClipperBase.html#addb22572066d3983dcd5797c542df00b)  
![-](../../closed.png) Protected Attributes inherited from
[ClipperLib::ClipperBase](../../d9/da0/classClipperLib_1_1ClipperBase.html)  
MinimaList::iterator | [m_CurrentLM](../../d9/da0/classClipperLib_1_1ClipperBase.html#ab6ed40f62810c0f894878c79d74afb36)  
[EdgeList](../../df/db2/namespaceClipperLib.html#a86ece3ad074061d6b3d18819b1fa4ed7) | [m_edges](../../d9/da0/classClipperLib_1_1ClipperBase.html#a8bfc007c0c0afd4e9d252dac0ef5daa0)  
[bool](../../d9/db9/classbool.html) | [m_HasOpenPaths](../../d9/da0/classClipperLib_1_1ClipperBase.html#aa2508f5b2a599294c359271506441fbd)  
[MinimaList](../../d9/da0/classClipperLib_1_1ClipperBase.html#addb22572066d3983dcd5797c542df00b) | [m_MinimaList](../../d9/da0/classClipperLib_1_1ClipperBase.html#a970749dc12a20e980c932af040f8a8c5)  
[bool](../../d9/db9/classbool.html) | [m_PreserveCollinear](../../d9/da0/classClipperLib_1_1ClipperBase.html#aad4ca0f2a16a6fb466036b36cc5ff638)  
[bool](../../d9/db9/classbool.html) | [m_UseFullRange](../../d9/da0/classClipperLib_1_1ClipperBase.html#aea11d183617adc12d7ba2b84533f7f45)  
  
## Constructor & Destructor Documentation

## ◆ Clipper()

ClipperLib::Clipper::Clipper  | ( | [int](../../d1/da0/classint.html) | _initOptions_ = `0`| ) |   
---|---|---|---|---|---  
  
References
[ClipperLib::ctIntersection](../../df/db2/namespaceClipperLib.html#a3db4fddd50b81ba657107505821d7f46a7ab04c0263f5c01a93330dc199a1ca42),
[ClipperLib::ioPreserveCollinear](../../df/db2/namespaceClipperLib.html#a322ee4b6e4480f648dad8c65c58b2804a5ee1ca93ff35691b7b27ce0f1bc4a898),
[ClipperLib::ioReverseSolution](../../df/db2/namespaceClipperLib.html#a322ee4b6e4480f648dad8c65c58b2804a019c42b227a89408692e98e9312baa77),
[ClipperLib::ioStrictlySimple](../../df/db2/namespaceClipperLib.html#a322ee4b6e4480f648dad8c65c58b2804ad2ab367f64cd3abcf737e04acb32b9f2),
[ClipperLib::ClipperBase::m_HasOpenPaths](../../d9/da0/classClipperLib_1_1ClipperBase.html#aa2508f5b2a599294c359271506441fbd),
[ClipperLib::ClipperBase::m_PreserveCollinear](../../d9/da0/classClipperLib_1_1ClipperBase.html#aad4ca0f2a16a6fb466036b36cc5ff638),
[ClipperLib::ClipperBase::m_UseFullRange](../../d9/da0/classClipperLib_1_1ClipperBase.html#aea11d183617adc12d7ba2b84533f7f45),
and
[ClipperLib::pftEvenOdd](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7acede4475518a377720537448c7b2df73).

## ◆ ~Clipper()

ClipperLib::Clipper::~Clipper  | ( | | ) |   
---|---|---|---|---  
  
References
[ClipperLib::ClipperBase::Clear()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a5690952fe8c2cb047025566405827821).

## Member Function Documentation

## ◆ Execute() [1/2]

[bool](../../d9/db9/classbool.html) ClipperLib::Clipper::Execute  | ( | [ClipType](../../df/db2/namespaceClipperLib.html#a3db4fddd50b81ba657107505821d7f46) | _clipType_ ,   
---|---|---|---  
|  | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _solution_ ,   
|  | [PolyFillType](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7) | _subjFillType_ = `[pftEvenOdd](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7acede4475518a377720537448c7b2df73)`,   
|  | [PolyFillType](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7) | _clipFillType_ = `[pftEvenOdd](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7acede4475518a377720537448c7b2df73)`  
| ) | |   
  
References
[ExecuteInternal()](../../d3/d1b/classClipperLib_1_1Clipper.html#a3e8757e5f8a6ffcb7fd0f9630fde02d3),
and
[ClipperLib::ClipperBase::m_HasOpenPaths](../../d9/da0/classClipperLib_1_1ClipperBase.html#aa2508f5b2a599294c359271506441fbd).

Referenced by
[PathScripts.PathJobCmd.CommandJobCreate::Activated()](../../db/d17/classPathScripts_1_1PathJobCmd_1_1CommandJobCreate.html#aac9d774ebbcda6c9840a1b776045fd2f),
[AdaptivePath::Adaptive2d::Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071),
[ClipperLib::ClipperOffset::Execute()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#ac591b25e483a52c99c3190a256ad4589),
[AdaptivePath::ClearedArea::ExpandCleared()](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a880cf981ced9aa6c2021bee6d35fc58b),
[AdaptivePath::ClearedArea::GetBoundedClearedAreaClipped()](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a396af78fc129b33fe0c3730caadc9503),
and
[PathScripts.PathJobCmd.CommandJobTemplateExport::SaveDialog()](../../d7/d23/classPathScripts_1_1PathJobCmd_1_1CommandJobTemplateExport.html#a208b7ff58f9cc81651d8ae05fe9c44af).

## ◆ Execute() [2/2]

[bool](../../d9/db9/classbool.html) ClipperLib::Clipper::Execute  | ( | [ClipType](../../df/db2/namespaceClipperLib.html#a3db4fddd50b81ba657107505821d7f46) | _clipType_ ,   
---|---|---|---  
|  | [PolyTree](../../d3/d99/classClipperLib_1_1PolyTree.html) & | _polytree_ ,   
|  | [PolyFillType](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7) | _subjFillType_ = `[pftEvenOdd](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7acede4475518a377720537448c7b2df73)`,   
|  | [PolyFillType](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7) | _clipFillType_ = `[pftEvenOdd](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7acede4475518a377720537448c7b2df73)`  
| ) | |   
  
References
[ExecuteInternal()](../../d3/d1b/classClipperLib_1_1Clipper.html#a3e8757e5f8a6ffcb7fd0f9630fde02d3).

Referenced by
[PathScripts.PathJobCmd.CommandJobCreate::Activated()](../../db/d17/classPathScripts_1_1PathJobCmd_1_1CommandJobCreate.html#aac9d774ebbcda6c9840a1b776045fd2f),
and
[PathScripts.PathJobCmd.CommandJobTemplateExport::SaveDialog()](../../d7/d23/classPathScripts_1_1PathJobCmd_1_1CommandJobTemplateExport.html#a208b7ff58f9cc81651d8ae05fe9c44af).

## ◆ ExecuteInternal()

| [bool](../../d9/db9/classbool.html) ClipperLib::Clipper::ExecuteInternal  | ( | | ) |   
---|---|---|---|---  
protectedvirtual  
  
References
[ClipperLib::Area()](../../df/db2/namespaceClipperLib.html#a4a96cc48117e1dba6cf51bbc2d91fe97),
[ClipperLib::OutRec::IsHole](../../d1/d21/structClipperLib_1_1OutRec.html#a18b2b534b717139528047ba10a1c805c),
[ClipperLib::OutRec::IsOpen](../../d1/d21/structClipperLib_1_1OutRec.html#a065731c084453a818939c219868a2fcc),
[ClipperLib::ClipperBase::m_CurrentLM](../../d9/da0/classClipperLib_1_1ClipperBase.html#ab6ed40f62810c0f894878c79d74afb36),
[ClipperLib::ClipperBase::m_MinimaList](../../d9/da0/classClipperLib_1_1ClipperBase.html#a970749dc12a20e980c932af040f8a8c5),
[ClipperLib::OutRec::Pts](../../d1/d21/structClipperLib_1_1OutRec.html#a82e9cba88d46d0d60db0b0365c6bd02e),
[Reset()](../../d3/d1b/classClipperLib_1_1Clipper.html#a14c704b062e8a079e34a8ce40838861e),
and
[ClipperLib::ReversePolyPtLinks()](../../df/db2/namespaceClipperLib.html#a5148d4f90b324e0e4a13d1b13055661f).

Referenced by
[Execute()](../../d3/d1b/classClipperLib_1_1Clipper.html#a06da196a4b4151edd2e5426ed48744cf).

## ◆ Reset()

| void ClipperLib::Clipper::Reset  | ( | | ) |   
---|---|---|---|---  
protectedvirtual  
  
Reimplemented from
[ClipperLib::ClipperBase](../../d9/da0/classClipperLib_1_1ClipperBase.html#a125febb065f23fc55dafffe8d185b642).

References
[ClipperLib::ClipperBase::m_MinimaList](../../d9/da0/classClipperLib_1_1ClipperBase.html#a970749dc12a20e980c932af040f8a8c5),
and
[ClipperLib::ClipperBase::Reset()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a125febb065f23fc55dafffe8d185b642).

Referenced by
[ExecuteInternal()](../../d3/d1b/classClipperLib_1_1Clipper.html#a3e8757e5f8a6ffcb7fd0f9630fde02d3).

## ◆ ReverseSolution() [1/2]

[bool](../../d9/db9/classbool.html) ClipperLib::Clipper::ReverseSolution  | ( | | ) |   
---|---|---|---|---  
  
Referenced by
[ClipperLib::ClipperOffset::Execute()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#ac591b25e483a52c99c3190a256ad4589).

## ◆ ReverseSolution() [2/2]

void ClipperLib::Clipper::ReverseSolution  | ( | [bool](../../d9/db9/classbool.html) | _value_| ) |   
---|---|---|---|---|---  
  
## ◆ StrictlySimple() [1/2]

[bool](../../d9/db9/classbool.html) ClipperLib::Clipper::StrictlySimple  | ( | | ) |   
---|---|---|---|---  
  
Referenced by
[CArea::Clip()](../../d3/d52/classCArea.html#aa4cab52e8f430196b3bfec652fb633e5),
[CArea::Intersect()](../../d3/d52/classCArea.html#aa3b91e3f3334bb09958debb072c63f7e),
[ClipperLib::SimplifyPolygon()](../../df/db2/namespaceClipperLib.html#af374cea59a991e49f36c3530efc45feb),
[ClipperLib::SimplifyPolygons()](../../df/db2/namespaceClipperLib.html#ac9ebbe437e4c08816bffeced6d001cf6),
[CArea::Subtract()](../../d3/d52/classCArea.html#a5a8ffb513a52d57bc8a8290eb003465b),
[CArea::Union()](../../d3/d52/classCArea.html#ad8edc8f34c4ccf3ea5dffe6245ba18ab),
[CArea::UniteCurves()](../../d3/d52/classCArea.html#aee75fc41d894490882ba64c7d3d2c25e),
and
[CArea::Xor()](../../d3/d52/classCArea.html#ad38c9c69a999398d749233a258b4365f).

## ◆ StrictlySimple() [2/2]

void ClipperLib::Clipper::StrictlySimple  | ( | [bool](../../d9/db9/classbool.html) | _value_| ) |   
---|---|---|---|---|---  
  
* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Mod/Path/libarea/clipper.hpp
  * FreeCAD/src/Mod/Path/libarea/clipper.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

