---
url: https://freecad.github.io/SourceDoc/d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html
scraped_at: 2025-09-08T15:18:34.401739
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [BOPTools](../../dc/dff/namespaceBOPTools.html)
  * [GeneralFuseResult](../../d3/d99/namespaceBOPTools_1_1GeneralFuseResult.html)
  * [GeneralFuseReturnBuilder](../../d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html)

[List of all members](../../d8/d87/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder-members.html) | Public Member Functions | Public Attributes

BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder Class Reference

##  Public Member Functions  
  
---  
def | [addPiece](../../d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html#a1b3d6ba361f3bab56ac793e4f5382d82) (self, piece_shape, source_shape_index_list)  
def | [getGFReturn](../../d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html#ae9a081f10819a3103dcb310095a59ac9) (self)  
def | [replacePiece](../../d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html#a47b1093b5ffe6b1ab94319db7802a466) (self, piece_index, new_shape)  
  
##  Public Attributes  
  
---  
|
[hasher_class](../../d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html#a070ec03d16bed83bb1d2310b41aba203)  
|
[pieces](../../d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html#a4d95a0628d2fff20e094a58f18f7b123)  
|
[source_shapes](../../d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html#a3627455ee63dda3fd65b838b4b62b237)  
  
## Member Function Documentation

## ◆ addPiece()

def BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder.addPiece  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _piece_shape_ ,   
|  |  | _source_shape_index_list_  
| ) | |   
      
    
    addPiece(piece_shape, source_shape_index_list): adds a piece. If the piece
    already exists, returns False, and only updates source<->piece map.

References BOPTools.GeneralFuseResult.GeneralFuseResult._piece_to_index,
BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder._piece_to_index,
BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder._pieces_from_source,
[BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder.hasher_class](../../d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html#a070ec03d16bed83bb1d2310b41aba203),
[BOPTools.GeneralFuseResult.GeneralFuseResult.pieces](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#aaecc3a8520fa477acb191ed609e06cee),
and
[BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder.pieces](../../d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html#a4d95a0628d2fff20e094a58f18f7b123).

## ◆ getGFReturn()

def BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder.getGFReturn  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder._pieces_from_source,
[BOPTools.GeneralFuseResult.GeneralFuseResult.pieces](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#aaecc3a8520fa477acb191ed609e06cee),
and
[BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder.pieces](../../d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html#a4d95a0628d2fff20e094a58f18f7b123).

## ◆ replacePiece()

def BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder.replacePiece  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _piece_index_ ,   
|  |  | _new_shape_  
| ) | |   
  
References
[BOPTools.GeneralFuseResult.GeneralFuseResult.pieces](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#aaecc3a8520fa477acb191ed609e06cee),
and
[BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder.pieces](../../d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html#a4d95a0628d2fff20e094a58f18f7b123).

## Member Data Documentation

## ◆ hasher_class

BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder.hasher_class  
---  
  
Referenced by
[BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder.addPiece()](../../d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html#a1b3d6ba361f3bab56ac793e4f5382d82).

## ◆ pieces

BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder.pieces  
---  
  
Referenced by
[BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder.addPiece()](../../d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html#a1b3d6ba361f3bab56ac793e4f5382d82),
[BOPTools.GeneralFuseResult.GeneralFuseResult.explodeCompounds()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#acaa64b16d29f0065ce1379f8dc572649),
[BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder.getGFReturn()](../../d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html#ae9a081f10819a3103dcb310095a59ac9),
[BOPTools.GeneralFuseResult.GeneralFuseResult.parse()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a6d96c514209cd870c0f4459827005fa2),
[BOPTools.GeneralFuseResult.GeneralFuseResult.parse_elements()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#ab6238c5203f5293c3d061a5c9c5ebdc6),
[BOPTools.GeneralFuseResult.GeneralFuseResult.piecesFromSource()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a9b0072ba2162c1527a0dca49069dde20),
[BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder.replacePiece()](../../d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html#a47b1093b5ffe6b1ab94319db7802a466),
and
[BOPTools.GeneralFuseResult.GeneralFuseResult.splitAggregates()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#ac2dd77595b00ad1c612310df00438702).

## ◆ source_shapes

BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder.source_shapes  
---  
  
Referenced by
[BOPTools.GeneralFuseResult.GeneralFuseResult.explodeCompounds()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#acaa64b16d29f0065ce1379f8dc572649),
[BOPTools.GeneralFuseResult.GeneralFuseResult.parse()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a6d96c514209cd870c0f4459827005fa2),
[BOPTools.GeneralFuseResult.GeneralFuseResult.sourcesOfPiece()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#aa5df8e412c4861d24573e4006b400fe6),
and
[BOPTools.GeneralFuseResult.GeneralFuseResult.splitAggregates()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#ac2dd77595b00ad1c612310df00438702).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Part/BOPTools/GeneralFuseResult.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

