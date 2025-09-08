---
url: https://freecad.github.io/SourceDoc/dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html
scraped_at: 2025-09-08T15:18:33.397879
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [BOPTools](../../dc/dff/namespaceBOPTools.html)
  * [GeneralFuseResult](../../d3/d99/namespaceBOPTools_1_1GeneralFuseResult.html)
  * [GeneralFuseResult](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html)

[List of all members](../../d9/d64/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult-members.html) | Public Member Functions | Public Attributes

BOPTools.GeneralFuseResult.GeneralFuseResult Class Reference

##  Public Member Functions  
  
---  
def | [explodeCompounds](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#acaa64b16d29f0065ce1379f8dc572649) (self)  
def | [indexOfPiece](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#ab96a1c112570277c178b8e0e2428ff65) (self, piece_shape)  
def | [indexOfSource](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a1f9d0fa4ebd7d6814c1d2b4dc5beddde) (self, source_shape)  
def | [largestOverlapCount](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a02f7d83b9ede574e09816b6f33411113) (self)  
def | [makeSplitPieces](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a9226c1237c30defa9ee2ba39afa07ef5) (self, shape)  
def | [parse](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a6d96c514209cd870c0f4459827005fa2) (self)  
def | [parse_elements](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#ab6238c5203f5293c3d061a5c9c5ebdc6) (self)  
def | [piecesFromSource](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a9b0072ba2162c1527a0dca49069dde20) (self, source_shape)  
def | [sourcesOfPiece](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#aa5df8e412c4861d24573e4006b400fe6) (self, piece_shape)  
def | [splitAggregates](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#ac2dd77595b00ad1c612310df00438702) (self, pieces_to_split=None)  
  
##  Public Attributes  
  
---  
|
[gfa_return](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a8e632041c40cbe05682b058fa00fc8c6)  
|
[pieces](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#aaecc3a8520fa477acb191ed609e06cee)  
|
[source_shapes](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a02715e73b744bb771db682a7509e8ce4)  
  
## Detailed Description

    
    
    class GeneralFuseResult: helper object for obtaining info from results of
    Part.Shape.generalFuse() method.
    
    Usage:
    def myCustomFusionRoutine(list_of_shapes):
    generalFuse_return = list_of_shapes[0].generalFuse(list_of_shapes[1:])
    ao = GeneralFuseResult(list_of_shapes, generalFuse_return)
    ... (use attributes and methods of ao) ...

## Member Function Documentation

## ◆ explodeCompounds()

def BOPTools.GeneralFuseResult.GeneralFuseResult.explodeCompounds  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    explodeCompounds(): if any of self.pieces is a compound, the compound is exploded.
    After running this, 'self' is filled with new data, where pieces are updated to
    contain the stuff extracted from compounds.

References BOPTools.GeneralFuseResult.GeneralFuseResult._sources_of_piece,
[BOPTools.GeneralFuseResult.GeneralFuseResult.gfa_return](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a8e632041c40cbe05682b058fa00fc8c6),
[App::ObjectIdentifier.parse()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a067a142eca99580ead933730b95a075b),
[App::Expression.parse()](../../dc/d5c/classApp_1_1Expression.html#a377c20925f92aab0265eb9e3e0b35c97),
[nlohmann::detail::parser< BasicJsonType, InputAdapterType
>.parse()](../../df/d6b/classnlohmann_1_1detail_1_1parser.html#a75fb9145ea85f1ad9cc14f61981e1111),
[Base::Quantity.parse()](../../d8/d18/classBase_1_1Quantity.html#ae1fd875bacec268fcb40771b60c6386a),
[e57::E57XmlParser.parse()](../../d0/d25/classe57_1_1E57XmlParser.html#a0f50a872eaa374894d2effe51d8bfb01),
[nlohmann::basic_json< ObjectType, ArrayType, StringType, BooleanType,
NumberIntegerType, NumberUnsignedType, NumberFloatType, AllocatorType,
JSONSerializer, BinaryType
>.parse()](../../d9/dcc/classnlohmann_1_1basic__json.html#a15018ade392a844ea32d5188d1a0b9c6),
[BOPTools.GeneralFuseResult.GeneralFuseResult.parse()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a6d96c514209cd870c0f4459827005fa2),
[Gui::SelectionFilter.parse()](../../d3/de7/classGui_1_1SelectionFilter.html#abb7651ba2344bccc48ff5bd00cf30db4),
[BOPTools.GeneralFuseResult.GeneralFuseResult.pieces](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#aaecc3a8520fa477acb191ed609e06cee),
[BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder.pieces](../../d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html#a4d95a0628d2fff20e094a58f18f7b123),
[BOPTools.GeneralFuseResult.GeneralFuseResult.source_shapes](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a02715e73b744bb771db682a7509e8ce4),
and
[BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder.source_shapes](../../d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html#a3627455ee63dda3fd65b838b4b62b237).

## ◆ indexOfPiece()

def BOPTools.GeneralFuseResult.GeneralFuseResult.indexOfPiece  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _piece_shape_  
| ) | |   
  
References BOPTools.GeneralFuseResult.GeneralFuseResult._piece_to_index, and
BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder._piece_to_index.

Referenced by
[BOPTools.GeneralFuseResult.GeneralFuseResult.parse()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a6d96c514209cd870c0f4459827005fa2),
and
[BOPTools.GeneralFuseResult.GeneralFuseResult.sourcesOfPiece()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#aa5df8e412c4861d24573e4006b400fe6).

## ◆ indexOfSource()

def BOPTools.GeneralFuseResult.GeneralFuseResult.indexOfSource  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _source_shape_  
| ) | |   
  
References BOPTools.GeneralFuseResult.GeneralFuseResult._source_to_index.

Referenced by
[BOPTools.GeneralFuseResult.GeneralFuseResult.parse()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a6d96c514209cd870c0f4459827005fa2),
and
[BOPTools.GeneralFuseResult.GeneralFuseResult.piecesFromSource()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a9b0072ba2162c1527a0dca49069dde20).

## ◆ largestOverlapCount()

def BOPTools.GeneralFuseResult.GeneralFuseResult.largestOverlapCount  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    largestOverlapCount(self): returns the largest overlap count. For example, if three
    spheres intersect and have some volume common to all three, largestOverlapCount
    returns 3.
    
    Note: the return value may be incorrect if some of the pieces are wires/shells/
    compsolids/compounds. Please use explodeCompounds and splitAggregates before using this function.

References BOPTools.GeneralFuseResult.GeneralFuseResult._sources_of_piece.

## ◆ makeSplitPieces()

def BOPTools.GeneralFuseResult.GeneralFuseResult.makeSplitPieces  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _shape_  
| ) | |   
      
    
    makeSplitPieces(self, shape): splits a shell, wire or compsolid into pieces where
    it intersects with other shapes.
    
    Returns list of split pieces. If no splits were done, returns list containing the
    original shape.

References BOPTools.GeneralFuseResult.GeneralFuseResult._element_to_source,
and
[BOPTools.GeneralFuseResult.GeneralFuseResult.gfa_return](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a8e632041c40cbe05682b058fa00fc8c6).

Referenced by
[BOPTools.GeneralFuseResult.GeneralFuseResult.splitAggregates()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#ac2dd77595b00ad1c612310df00438702).

## ◆ parse()

def BOPTools.GeneralFuseResult.GeneralFuseResult.parse  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    Parses the result of generalFuse recorded into self.gfa_return. Recovers missing
    information. Fills in data structures.
    
    It is called automatically by class constructor.

References
AttachmentEditor.TaskAttachmentEditor.AttachmentEditorTaskPanel.__define_attributes(),
BOPTools.GeneralFuseResult.GeneralFuseResult.__define_attributes(),
BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder.__define_attributes(),
BOPTools.GeneralFuseResult.GeneralFuseResult._piece_to_index,
BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder._piece_to_index,
BOPTools.GeneralFuseResult.GeneralFuseResult._pieces_of_source,
BOPTools.GeneralFuseResult.GeneralFuseResult._source_to_index,
BOPTools.GeneralFuseResult.GeneralFuseResult._sources_of_piece,
[BOPTools.GeneralFuseResult.GeneralFuseResult.gfa_return](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a8e632041c40cbe05682b058fa00fc8c6),
[BOPTools.GeneralFuseResult.GeneralFuseResult.indexOfPiece()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#ab96a1c112570277c178b8e0e2428ff65),
[BOPTools.GeneralFuseResult.GeneralFuseResult.indexOfSource()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a1f9d0fa4ebd7d6814c1d2b4dc5beddde),
[BOPTools.GeneralFuseResult.GeneralFuseResult.pieces](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#aaecc3a8520fa477acb191ed609e06cee),
[BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder.pieces](../../d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html#a4d95a0628d2fff20e094a58f18f7b123),
[BOPTools.GeneralFuseResult.GeneralFuseResult.source_shapes](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a02715e73b744bb771db682a7509e8ce4),
and
[BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder.source_shapes](../../d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html#a3627455ee63dda3fd65b838b4b62b237).

Referenced by
[BOPTools.GeneralFuseResult.GeneralFuseResult.explodeCompounds()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#acaa64b16d29f0065ce1379f8dc572649),
and
[BOPTools.GeneralFuseResult.GeneralFuseResult.splitAggregates()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#ac2dd77595b00ad1c612310df00438702).

## ◆ parse_elements()

def BOPTools.GeneralFuseResult.GeneralFuseResult.parse_elements  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    Fills element-to-source map. Potentially slow, so separated from general parse.
    Needed for splitAggregates; called automatically from splitAggregates.

References BOPTools.GeneralFuseResult.GeneralFuseResult._element_to_source,
BOPTools.GeneralFuseResult.GeneralFuseResult._sources_of_piece,
[BOPTools.GeneralFuseResult.GeneralFuseResult.pieces](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#aaecc3a8520fa477acb191ed609e06cee),
and
[BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder.pieces](../../d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html#a4d95a0628d2fff20e094a58f18f7b123).

Referenced by
[BOPTools.GeneralFuseResult.GeneralFuseResult.splitAggregates()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#ac2dd77595b00ad1c612310df00438702).

## ◆ piecesFromSource()

def BOPTools.GeneralFuseResult.GeneralFuseResult.piecesFromSource  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _source_shape_  
| ) | |   
      
    
    piecesFromSource(source_shape): returns list of pieces (shapes) that came from
    given source shape.
    
    Note: aggregate pieces (e.g. wire, shell, compound) always have only one source - the
    shape they came directly from. Only after executing splitAggregates and
    explodeCompounds the source lists become completely populated.

References BOPTools.GeneralFuseResult.GeneralFuseResult._pieces_of_source,
[BOPTools.GeneralFuseResult.GeneralFuseResult.indexOfSource()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a1f9d0fa4ebd7d6814c1d2b4dc5beddde),
[BOPTools.GeneralFuseResult.GeneralFuseResult.pieces](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#aaecc3a8520fa477acb191ed609e06cee),
and
[BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder.pieces](../../d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html#a4d95a0628d2fff20e094a58f18f7b123).

## ◆ sourcesOfPiece()

def BOPTools.GeneralFuseResult.GeneralFuseResult.sourcesOfPiece  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _piece_shape_  
| ) | |   
      
    
    sourcesOfPiece(piece_shape): returns list of source shapes given piece came from.
    
    Note: aggregate pieces (e.g. wire, shell, compound) always have only one source - the
    shape they came directly from. Only after executing splitAggregates and
    explodeCompounds the source lists become completely populated.

References BOPTools.GeneralFuseResult.GeneralFuseResult._sources_of_piece,
[BOPTools.GeneralFuseResult.GeneralFuseResult.indexOfPiece()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#ab96a1c112570277c178b8e0e2428ff65),
[BOPTools.GeneralFuseResult.GeneralFuseResult.source_shapes](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a02715e73b744bb771db682a7509e8ce4),
and
[BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder.source_shapes](../../d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html#a3627455ee63dda3fd65b838b4b62b237).

## ◆ splitAggregates()

def BOPTools.GeneralFuseResult.GeneralFuseResult.splitAggregates  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _pieces_to_split_ = `None`  
| ) | |   
      
    
    splitAggregates(pieces_to_split = None): splits aggregate shapes (wires, shells,
    compsolids) in pieces of GF result as cut by intersections. Also splits aggregates
    inside compounds. After running this, 'self' is replaced with new data, where the
    pieces_to_split are split.
    
    'pieces_to_split': list of shapes (from self.pieces), that are to be processed. If
    None, all pieces will be split if possible.
    
    Notes:
    * this routine is very important to functioning of Connect on shells and wires.
    * Warning: convoluted and slow.

References BOPTools.GeneralFuseResult.GeneralFuseResult._sources_of_piece,
BOPTools.GeneralFuseResult.GeneralFuseResult._splitInCompound(),
[BOPTools.GeneralFuseResult.GeneralFuseResult.gfa_return](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a8e632041c40cbe05682b058fa00fc8c6),
[BOPTools.GeneralFuseResult.GeneralFuseResult.makeSplitPieces()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a9226c1237c30defa9ee2ba39afa07ef5),
[App::ObjectIdentifier.parse()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a067a142eca99580ead933730b95a075b),
[App::Expression.parse()](../../dc/d5c/classApp_1_1Expression.html#a377c20925f92aab0265eb9e3e0b35c97),
[nlohmann::detail::parser< BasicJsonType, InputAdapterType
>.parse()](../../df/d6b/classnlohmann_1_1detail_1_1parser.html#a75fb9145ea85f1ad9cc14f61981e1111),
[Base::Quantity.parse()](../../d8/d18/classBase_1_1Quantity.html#ae1fd875bacec268fcb40771b60c6386a),
[e57::E57XmlParser.parse()](../../d0/d25/classe57_1_1E57XmlParser.html#a0f50a872eaa374894d2effe51d8bfb01),
[nlohmann::basic_json< ObjectType, ArrayType, StringType, BooleanType,
NumberIntegerType, NumberUnsignedType, NumberFloatType, AllocatorType,
JSONSerializer, BinaryType
>.parse()](../../d9/dcc/classnlohmann_1_1basic__json.html#a15018ade392a844ea32d5188d1a0b9c6),
[BOPTools.GeneralFuseResult.GeneralFuseResult.parse()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a6d96c514209cd870c0f4459827005fa2),
[Gui::SelectionFilter.parse()](../../d3/de7/classGui_1_1SelectionFilter.html#abb7651ba2344bccc48ff5bd00cf30db4),
[BOPTools.GeneralFuseResult.GeneralFuseResult.parse_elements()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#ab6238c5203f5293c3d061a5c9c5ebdc6),
[BOPTools.GeneralFuseResult.GeneralFuseResult.pieces](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#aaecc3a8520fa477acb191ed609e06cee),
[BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder.pieces](../../d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html#a4d95a0628d2fff20e094a58f18f7b123),
[BOPTools.GeneralFuseResult.GeneralFuseResult.source_shapes](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a02715e73b744bb771db682a7509e8ce4),
and
[BOPTools.GeneralFuseResult.GeneralFuseReturnBuilder.source_shapes](../../d9/db2/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseReturnBuilder.html#a3627455ee63dda3fd65b838b4b62b237).

## Member Data Documentation

## ◆ gfa_return

BOPTools.GeneralFuseResult.GeneralFuseResult.gfa_return  
---  
  
Referenced by
[BOPTools.GeneralFuseResult.GeneralFuseResult.explodeCompounds()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#acaa64b16d29f0065ce1379f8dc572649),
[BOPTools.GeneralFuseResult.GeneralFuseResult.makeSplitPieces()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a9226c1237c30defa9ee2ba39afa07ef5),
[BOPTools.GeneralFuseResult.GeneralFuseResult.parse()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#a6d96c514209cd870c0f4459827005fa2),
and
[BOPTools.GeneralFuseResult.GeneralFuseResult.splitAggregates()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#ac2dd77595b00ad1c612310df00438702).

## ◆ pieces

BOPTools.GeneralFuseResult.GeneralFuseResult.pieces  
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

BOPTools.GeneralFuseResult.GeneralFuseResult.source_shapes  
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

