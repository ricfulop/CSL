---
url: https://freecad.github.io/SourceDoc/da/d87/classClipperLib_1_1PolyNode.html
scraped_at: 2025-09-08T15:19:19.598341
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ClipperLib](../../df/db2/namespaceClipperLib.html)
  * [PolyNode](../../da/d87/classClipperLib_1_1PolyNode.html)

[List of all members](../../df/d96/classClipperLib_1_1PolyNode-members.html) | Public Member Functions | Public Attributes | Friends

ClipperLib::PolyNode Class Reference

`#include <clipper.hpp>`

##  Public Member Functions  
  
---  
[int](../../d1/da0/classint.html) | [ChildCount](../../da/d87/classClipperLib_1_1PolyNode.html#a19128db6fb2aca66555231edaffa7ade) () const  
[PolyNode](../../da/d87/classClipperLib_1_1PolyNode.html) * | [GetNext](../../da/d87/classClipperLib_1_1PolyNode.html#adbcb861001d8bfbd609c4ba4f4a19a58) () const  
[bool](../../d9/db9/classbool.html) | [IsHole](../../da/d87/classClipperLib_1_1PolyNode.html#a0467801cae1b28ad8a4917b96e551536) () const  
[bool](../../d9/db9/classbool.html) | [IsOpen](../../da/d87/classClipperLib_1_1PolyNode.html#ac9ade640af2515976d337b65e8e84776) () const  
|
[PolyNode](../../da/d87/classClipperLib_1_1PolyNode.html#a12b3350e7ab93fb0002b2b4d7dcf13ba)
()  
virtual | [~PolyNode](../../da/d87/classClipperLib_1_1PolyNode.html#abca566308c95d19c72dee88217b23064) ()  
  
##  Public Attributes  
  
---  
[PolyNodes](../../df/db2/namespaceClipperLib.html#ac9381bbff6b966df41b78667385b9c1e) | [Childs](../../da/d87/classClipperLib_1_1PolyNode.html#a7ac59aea508951a4c979bfca8913261d)  
[Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) | [Contour](../../da/d87/classClipperLib_1_1PolyNode.html#a1d08b8a9499ff8cb89d5d63a12f881ea)  
[PolyNode](../../da/d87/classClipperLib_1_1PolyNode.html) * | [Parent](../../da/d87/classClipperLib_1_1PolyNode.html#a9465bc02623316de2af3ab52c6f7041e)  
  
##  Friends  
  
---  
class | [Clipper](../../da/d87/classClipperLib_1_1PolyNode.html#a4d39a09ecdddeeb85930dd4554a54b3c)  
class | [ClipperOffset](../../da/d87/classClipperLib_1_1PolyNode.html#adadfb8ac9a17a5c8fb7b4f012075b975)  
  
## Constructor & Destructor Documentation

## ◆ PolyNode()

ClipperLib::PolyNode::PolyNode  | ( | | ) |   
---|---|---|---|---  
  
## ◆ ~PolyNode()

| virtual ClipperLib::PolyNode::~PolyNode  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ ChildCount()

[int](../../d1/da0/classint.html) ClipperLib::PolyNode::ChildCount  | ( | | ) |  const  
---|---|---|---|---  
  
References
[Childs](../../da/d87/classClipperLib_1_1PolyNode.html#a7ac59aea508951a4c979bfca8913261d).

Referenced by
[ClipperLib::ClipperOffset::AddPath()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a0cd68e3690072f510924a5b25291043b),
[ClipperLib::AddPolyNodeToPaths()](../../df/db2/namespaceClipperLib.html#a4644758856e780ca359c3e37065397a6),
[ClipperLib::ClipperOffset::Clear()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#ab444433587b6a3f6c89655938d889c7d),
[ClipperLib::ClipperOffset::Execute()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a3aaa9fcc20e503c967a23f1793536118),
and
[ClipperLib::OpenPathsFromPolyTree()](../../df/db2/namespaceClipperLib.html#aa8b0b36c4c1e8108f39b10e4fba81cc5).

## ◆ GetNext()

[PolyNode](../../da/d87/classClipperLib_1_1PolyNode.html) * ClipperLib::PolyNode::GetNext  | ( | | ) |  const  
---|---|---|---|---  
  
References
[Childs](../../da/d87/classClipperLib_1_1PolyNode.html#a7ac59aea508951a4c979bfca8913261d).

## ◆ IsHole()

[bool](../../d9/db9/classbool.html) ClipperLib::PolyNode::IsHole  | ( | | ) |  const  
---|---|---|---|---  
  
References
[Parent](../../da/d87/classClipperLib_1_1PolyNode.html#a9465bc02623316de2af3ab52c6f7041e).

## ◆ IsOpen()

[bool](../../d9/db9/classbool.html) ClipperLib::PolyNode::IsOpen  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[ClipperLib::AddPolyNodeToPaths()](../../df/db2/namespaceClipperLib.html#a4644758856e780ca359c3e37065397a6).

## Friends And Related Function Documentation

## ◆ Clipper

| [friend](../../d7/d23/classfriend.html) class
[Clipper](../../d3/d1b/classClipperLib_1_1Clipper.html)  
---  
friend  
  
## ◆ ClipperOffset

| [friend](../../d7/d23/classfriend.html) class
[ClipperOffset](../../d6/d79/classClipperLib_1_1ClipperOffset.html)  
---  
friend  
  
## Member Data Documentation

## ◆ Childs

[PolyNodes](../../df/db2/namespaceClipperLib.html#ac9381bbff6b966df41b78667385b9c1e)
ClipperLib::PolyNode::Childs  
---  
  
Referenced by
[ClipperLib::ClipperOffset::AddPath()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a0cd68e3690072f510924a5b25291043b),
[ClipperLib::AddPolyNodeToPaths()](../../df/db2/namespaceClipperLib.html#a4644758856e780ca359c3e37065397a6),
[ChildCount()](../../da/d87/classClipperLib_1_1PolyNode.html#a19128db6fb2aca66555231edaffa7ade),
[ClipperLib::PolyTree::Clear()](../../d3/d99/classClipperLib_1_1PolyTree.html#a8620ea631d478b3c43274ac084902ec4),
[ClipperLib::ClipperOffset::Clear()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#ab444433587b6a3f6c89655938d889c7d),
[ClipperLib::ClipperOffset::Execute()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a3aaa9fcc20e503c967a23f1793536118),
[ClipperLib::PolyTree::GetFirst()](../../d3/d99/classClipperLib_1_1PolyTree.html#a8b88b8d6225281ee7d536902b0d04e9e),
[GetNext()](../../da/d87/classClipperLib_1_1PolyNode.html#adbcb861001d8bfbd609c4ba4f4a19a58),
and
[ClipperLib::OpenPathsFromPolyTree()](../../df/db2/namespaceClipperLib.html#aa8b0b36c4c1e8108f39b10e4fba81cc5).

## ◆ Contour

[Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da)
ClipperLib::PolyNode::Contour  
---  
  
Referenced by
[ClipperLib::ClipperOffset::AddPath()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a0cd68e3690072f510924a5b25291043b),
and
[ClipperLib::AddPolyNodeToPaths()](../../df/db2/namespaceClipperLib.html#a4644758856e780ca359c3e37065397a6).

## ◆ Parent

[PolyNode](../../da/d87/classClipperLib_1_1PolyNode.html)*
ClipperLib::PolyNode::Parent  
---  
  
Referenced by
[IsHole()](../../da/d87/classClipperLib_1_1PolyNode.html#a0467801cae1b28ad8a4917b96e551536).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Mod/Path/libarea/clipper.hpp
  * FreeCAD/src/Mod/Path/libarea/clipper.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

