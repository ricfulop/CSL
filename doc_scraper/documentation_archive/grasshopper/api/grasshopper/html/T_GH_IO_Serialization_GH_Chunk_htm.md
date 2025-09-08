---
url: https://developer.rhino3d.com/api/grasshopper/html/T_GH_IO_Serialization_GH_Chunk.htm
scraped_at: 2025-09-08T16:10:38.879439
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[GH_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH_Chunk Constructor
](../html/Overload_GH_IO_Serialization_GH_Chunk__ctor.htm "GH_Chunk
Constructor ")

[GH_Chunk Properties](../html/Properties_T_GH_IO_Serialization_GH_Chunk.htm
"GH_Chunk Properties")

[GH_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm
"GH_Chunk Methods")

[GH_Chunk Fields](../html/Fields_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk
Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Chunk Class  
  
---  
  
Full implementation of GH_IChunk, GH_IReader, GH_IWriter, GH_IBinarySupport
and GH_IXmlSupport. Instances of this class are usually disguised as one of
the interfaces it implements.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
GH_IO.SerializationGH_Chunk  
[GH_IO.SerializationGH_LooseChunk](T_GH_IO_Serialization_GH_LooseChunk.htm)  

**Namespace:** [GH_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:** GH_IO (in GH_IO.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Chunk : GH_IWriter, GH_IChunk, 
    	GH_IBinarySupport, GH_IXmlSupport, GH_IReader
    
    
    Public Class GH_Chunk
    	Implements GH_IWriter, GH_IChunk, GH_IBinarySupport, GH_IXmlSupport, 
    	GH_IReader

The GH_Chunk type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[GH_Chunk](M_GH_IO_Serialization_GH_Chunk__ctor.htm)|  Blank constructor. You
typically do not need to create your own Chunks. The GH_Archive class will
create top-level chunks and existing chunks can create child chunks.  
![Protected method](../icons/protmethod.gif)|
[GH_Chunk(GH_Archive)](M_GH_IO_Serialization_GH_Chunk__ctor_1.htm)|
Constructor. You typically do not need to create your own Chunks. The
GH_Archive class will create top-level chunks and existing chunks can create
child chunks.  
![Protected method](../icons/protmethod.gif)| [GH_Chunk(GH_Archive,
String)](M_GH_IO_Serialization_GH_Chunk__ctor_2.htm)|  Constructor. You
typically do not need to create your own Chunks. The GH_Archive class will
create top-level chunks and existing chunks can create child chunks.  
![Protected method](../icons/protmethod.gif)| [GH_Chunk(GH_Archive, String,
Int32)](M_GH_IO_Serialization_GH_Chunk__ctor_3.htm)|  Constructor. You
typically do not need to create your own Chunks. The GH_Archive class will
create top-level chunks and existing chunks can create child chunks.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Archive](P_GH_IO_Serialization_GH_Chunk_Archive.htm)|  Gets a pointer to the
archive that owns the Root of the tree this chunk belongs to.  
![Public property](../icons/pubproperty.gif)|
[ArchiveLocation](P_GH_IO_Serialization_GH_Chunk_ArchiveLocation.htm)|  Gets a
string representing the URI with which the archive is associated. The location
may be a null string.  
![Public property](../icons/pubproperty.gif)|
[ChunkCount](P_GH_IO_Serialization_GH_Chunk_ChunkCount.htm)|  Gets the number
of child chunks contained in this chunk. The set of all child chunks is
referred to as a 'litter'.  
![Public property](../icons/pubproperty.gif)|
[Chunks](P_GH_IO_Serialization_GH_Chunk_Chunks.htm)|  Gets a pointer to the
internal list of child chunks. Do not access this list unless you know what
you are doing.  
![Public property](../icons/pubproperty.gif)|
[HasComments](P_GH_IO_Serialization_GH_Chunk_HasComments.htm)|  Gets a value
that indicates whether or not comments have been stored in this chunk.  
![Public property](../icons/pubproperty.gif)|
[HasIndex](P_GH_IO_Serialization_GH_Chunk_HasIndex.htm)|  Gets the index
existence implication. The item is considered to have an index qualifier if
the index value is larger than or equal to zero.  
![Public property](../icons/pubproperty.gif)|
[HasName](P_GH_IO_Serialization_GH_Chunk_HasName.htm)|  Gets the name validity
of this item. The item is considered to have an invalid name if
string.IsNullOrEmpty(name)  
![Public property](../icons/pubproperty.gif)|
[Index](P_GH_IO_Serialization_GH_Chunk_Index.htm)|  Gets the index of this
chunk. The index is set by the owner of this chunk. Indices smaller than zero
imply no index has been set. The combination of name+index is always unique
among a set of chunks in the same litter.  
![Public property](../icons/pubproperty.gif)|
[ItemCount](P_GH_IO_Serialization_GH_Chunk_ItemCount.htm)|  Gets the number of
items contained in this chunk.  
![Public property](../icons/pubproperty.gif)|
[Items](P_GH_IO_Serialization_GH_Chunk_Items.htm)|  Gets a pointer to the
internal list of items. Do not access this list unless you know what you are
doing.  
![Public property](../icons/pubproperty.gif)|
[Name](P_GH_IO_Serialization_GH_Chunk_Name.htm)|  Gets the name of this chunk.
The name is set by the owner of this chunk. Names must be at least 1 character
long. The combination of name+index is always unique among a set of chunks in
a single litter.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AddComment](M_GH_IO_Serialization_GH_Chunk_AddComment.htm)|  Adds a text
comment to this chunk. Comments are serialized only if the output flavour is a
human readable format. Comments are never deserialized, they are purely for
the benefit of the humans reading the file data.  
![Public method](../icons/pubmethod.gif)|
[AddMessage](M_GH_IO_Serialization_GH_Chunk_AddMessage.htm)|  Log a new
message with the top-level archive. Messages are collected during read/write
operations, and can be displayed to the user upon completion using
GH_Archive.ShowMessageLog().  
![Public method](../icons/pubmethod.gif)|
[ChunkExists(String)](M_GH_IO_Serialization_GH_Chunk_ChunkExists.htm)|  Checks
whether a chunk with the specified name exists in the litter. Only chunks
without index qualifiers are considered. Name comparisons are not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [ChunkExists(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_ChunkExists_1.htm)|  Checks whether a
chunk with the specified name and index exists in the litter. Only chunks with
index qualifiers are considered. Name comparisons are not case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[CopyValuesFromChunk](M_GH_IO_Serialization_GH_Chunk_CopyValuesFromChunk.htm)|
Copy all values and sub-chunks from another chunk.  
![Public method](../icons/pubmethod.gif)|
[CopyValuesToChunk](M_GH_IO_Serialization_GH_Chunk_CopyValuesToChunk.htm)|
Copy all values and sub-chunks in this chunk to another chunk which does not
point to the same archive.  
![Public method](../icons/pubmethod.gif)|
[CreateChunk(String)](M_GH_IO_Serialization_GH_Chunk_CreateChunk.htm)|  Create
a new child chunk with the specified name and without an index qualifier. If
another chunk already exists with similar properties, an exception will be
thrown.  
![Public method](../icons/pubmethod.gif)| [CreateChunk(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_CreateChunk_1.htm)|  Create a new child
chunk with the specified name and index qualifier. If another chunk already
exists with similar properties, an exception will be thrown.  
![Public method](../icons/pubmethod.gif)|
[FindChunk(String)](M_GH_IO_Serialization_GH_Chunk_FindChunk.htm)|  Finds the
first chunk in the litter that matches the given name. Only chunks without
index qualifiers are considered.  
![Public method](../icons/pubmethod.gif)| [FindChunk(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_FindChunk_1.htm)|  Finds the first
chunk in the list that matches the given name and index. Only chunks with
index qualifiers are considered.  
![Public method](../icons/pubmethod.gif)|
[FindItem(String)](M_GH_IO_Serialization_GH_Chunk_FindItem.htm)|  Finds the
first item that matches the given name. Only items without index qualifiers
are considered. Name comparisons are not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [FindItem(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_FindItem_1.htm)|  Finds the first item
that matches the given name and index. Only items with index qualifiers are
considered. Name comparisons are not case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetBoolean(String)](M_GH_IO_Serialization_GH_Chunk_GetBoolean.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetBoolean(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetBoolean_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetBoundingBox(String)](M_GH_IO_Serialization_GH_Chunk_GetBoundingBox.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetBoundingBox(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetBoundingBox_1.htm)|  Gets the value
of the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetByte(String)](M_GH_IO_Serialization_GH_Chunk_GetByte.htm)|  Gets the value
of the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetByte(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetByte_1.htm)|  Gets the value of the
item with the specified name and index. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetByteArray(String)](M_GH_IO_Serialization_GH_Chunk_GetByteArray.htm)|  Gets
the value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetByteArray(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetByteArray_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetDate(String)](M_GH_IO_Serialization_GH_Chunk_GetDate.htm)|  Gets the value
of the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetDate(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetDate_1.htm)|  Gets the value of the
item with the specified name and index. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetDecimal(String)](M_GH_IO_Serialization_GH_Chunk_GetDecimal.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetDecimal(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetDecimal_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetDouble(String)](M_GH_IO_Serialization_GH_Chunk_GetDouble.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetDouble(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetDouble_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetDoubleArray(String)](M_GH_IO_Serialization_GH_Chunk_GetDoubleArray.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetDoubleArray(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetDoubleArray_1.htm)|  Gets the value
of the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetDrawingBitmap(String)](M_GH_IO_Serialization_GH_Chunk_GetDrawingBitmap.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetDrawingBitmap(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetDrawingBitmap_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetDrawingColor(String)](M_GH_IO_Serialization_GH_Chunk_GetDrawingColor.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetDrawingColor(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetDrawingColor_1.htm)|  Gets the value
of the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetDrawingPoint(String)](M_GH_IO_Serialization_GH_Chunk_GetDrawingPoint.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetDrawingPoint(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetDrawingPoint_1.htm)|  Gets the value
of the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetDrawingPointF(String)](M_GH_IO_Serialization_GH_Chunk_GetDrawingPointF.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetDrawingPointF(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetDrawingPointF_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetDrawingRectangle(String)](M_GH_IO_Serialization_GH_Chunk_GetDrawingRectangle.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetDrawingRectangle(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetDrawingRectangle_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetDrawingRectangleF(String)](M_GH_IO_Serialization_GH_Chunk_GetDrawingRectangleF.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetDrawingRectangleF(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetDrawingRectangleF_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetDrawingSize(String)](M_GH_IO_Serialization_GH_Chunk_GetDrawingSize.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetDrawingSize(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetDrawingSize_1.htm)|  Gets the value
of the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetDrawingSizeF(String)](M_GH_IO_Serialization_GH_Chunk_GetDrawingSizeF.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetDrawingSizeF(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetDrawingSizeF_1.htm)|  Gets the value
of the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetGuid(String)](M_GH_IO_Serialization_GH_Chunk_GetGuid.htm)|  Gets the value
of the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetGuid(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetGuid_1.htm)|  Gets the value of the
item with the specified name and index. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetInt32(String)](M_GH_IO_Serialization_GH_Chunk_GetInt32.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetInt32(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetInt32_1.htm)|  Gets the value of the
item with the specified name and index. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetInt64(String)](M_GH_IO_Serialization_GH_Chunk_GetInt64.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetInt64(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetInt64_1.htm)|  Gets the value of the
item with the specified name and index. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetInterval1D(String)](M_GH_IO_Serialization_GH_Chunk_GetInterval1D.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetInterval1D(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetInterval1D_1.htm)|  Gets the value
of the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetInterval2D(String)](M_GH_IO_Serialization_GH_Chunk_GetInterval2D.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetInterval2D(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetInterval2D_1.htm)|  Gets the value
of the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetLine(String)](M_GH_IO_Serialization_GH_Chunk_GetLine.htm)|  Gets the value
of the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetLine(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetLine_1.htm)|  Gets the value of the
item with the specified name and index. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetPath(String,
String)](M_GH_IO_Serialization_GH_Chunk_GetPath_1.htm)|  Gets the value of the
item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetPath(String, Int32,
String)](M_GH_IO_Serialization_GH_Chunk_GetPath.htm)|  Gets the value of the
item with the specified name and index. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetPlane(String)](M_GH_IO_Serialization_GH_Chunk_GetPlane.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetPlane(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetPlane_1.htm)|  Gets the value of the
item with the specified name and index. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetPoint2D(String)](M_GH_IO_Serialization_GH_Chunk_GetPoint2D.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetPoint2D(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetPoint2D_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetPoint3D(String)](M_GH_IO_Serialization_GH_Chunk_GetPoint3D.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetPoint3D(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetPoint3D_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetPoint4D(String)](M_GH_IO_Serialization_GH_Chunk_GetPoint4D.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetPoint4D(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetPoint4D_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetSingle(String)](M_GH_IO_Serialization_GH_Chunk_GetSingle.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetSingle(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetSingle_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetString(String)](M_GH_IO_Serialization_GH_Chunk_GetString.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetString(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetString_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetVersion(String)](M_GH_IO_Serialization_GH_Chunk_GetVersion.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetVersion(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_GetVersion_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[InstantiateRoot](M_GH_IO_Serialization_GH_Chunk_InstantiateRoot.htm)|
Construct a new instance of GH_Chunk which acts as a Root node. If you
**must** create a chunk from scratch, use this static method to create one.  
![Public method](../icons/pubmethod.gif)|
[ItemExists(String)](M_GH_IO_Serialization_GH_Chunk_ItemExists.htm)|  Gets the
occupancy for a specific item name. Only items without index qualifiers are
considered.  
![Public method](../icons/pubmethod.gif)| [ItemExists(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_ItemExists_1.htm)|  Checks whether an
item with the specified name and index exists. Only items with index
qualifiers are considered. Name comparisons are not case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[Read(BinaryReader)](M_GH_IO_Serialization_GH_Chunk_Read.htm)|  Read this
chunk and all child chunks from a binary stream.  
![Public method](../icons/pubmethod.gif)|
[Read(XmlNode)](M_GH_IO_Serialization_GH_Chunk_Read_1.htm)|  Read this chunk
and all child chunks from an Xml node.  
![Public method](../icons/pubmethod.gif)|
[RemoveChunk(GH_IChunk)](M_GH_IO_Serialization_GH_Chunk_RemoveChunk.htm)|
Remove the specified chunk from the litter.  
![Public method](../icons/pubmethod.gif)|
[RemoveChunk(String)](M_GH_IO_Serialization_GH_Chunk_RemoveChunk_1.htm)|
Remove the first chunk with a matching name. Only chunks without index
qualifiers are considered. Name comparisons are not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [RemoveChunk(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_RemoveChunk_2.htm)|  Remove the first
chunk with a matching name and index. Only chunks with index qualifiers are
considered. Name comparisons are not case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[RemoveItem(String)](M_GH_IO_Serialization_GH_Chunk_RemoveItem.htm)|  Remove
an unindexed item from this chunk.  
![Public method](../icons/pubmethod.gif)| [RemoveItem(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_RemoveItem_1.htm)|  Remove an indexed
item from this chunk.  
![Public method](../icons/pubmethod.gif)| [SetBoolean(String,
Boolean)](M_GH_IO_Serialization_GH_Chunk_SetBoolean.htm)|  Add a new data item
to this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetBoolean(String, Int32,
Boolean)](M_GH_IO_Serialization_GH_Chunk_SetBoolean_1.htm)|  Add a new data
item to this chunk. The combination of name and index must be unique or an
exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetBoundingBox(String,
GH_BoundingBox)](M_GH_IO_Serialization_GH_Chunk_SetBoundingBox.htm)|  Add a
new data item to this chunk. The name must be unique or an exception will be
thrown.  
![Public method](../icons/pubmethod.gif)| [SetBoundingBox(String, Int32,
GH_BoundingBox)](M_GH_IO_Serialization_GH_Chunk_SetBoundingBox_1.htm)|  Add a
new data item to this chunk. The combination of name and index must be unique
or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetByte(String,
Byte)](M_GH_IO_Serialization_GH_Chunk_SetByte.htm)|  Add a new data item to
this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetByte(String, Int32,
Byte)](M_GH_IO_Serialization_GH_Chunk_SetByte_1.htm)|  Add a new data item to
this chunk. The combination of name and index must be unique or an exception
will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetByteArray(String,
Byte)](M_GH_IO_Serialization_GH_Chunk_SetByteArray.htm)|  Add a new data item
to this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetByteArray(String, Int32,
Byte)](M_GH_IO_Serialization_GH_Chunk_SetByteArray_1.htm)|  Add a new data
item to this chunk. The combination of name and index must be unique or an
exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetDate(String,
DateTime)](M_GH_IO_Serialization_GH_Chunk_SetDate.htm)|  Add a new data item
to this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetDate(String, Int32,
DateTime)](M_GH_IO_Serialization_GH_Chunk_SetDate_1.htm)|  Add a new data item
to this chunk. The combination of name and index must be unique or an
exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetDecimal(String,
Decimal)](M_GH_IO_Serialization_GH_Chunk_SetDecimal.htm)|  Add a new data item
to this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetDecimal(String, Int32,
Decimal)](M_GH_IO_Serialization_GH_Chunk_SetDecimal_1.htm)|  Add a new data
item to this chunk. The combination of name and index must be unique or an
exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetDouble(String,
Double)](M_GH_IO_Serialization_GH_Chunk_SetDouble.htm)|  Add a new data item
to this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetDouble(String, Int32,
Double)](M_GH_IO_Serialization_GH_Chunk_SetDouble_1.htm)|  Add a new data item
to this chunk. The combination of name and index must be unique or an
exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetDoubleArray(String,
Double)](M_GH_IO_Serialization_GH_Chunk_SetDoubleArray.htm)|  Add a new data
item to this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetDoubleArray(String, Int32,
Double)](M_GH_IO_Serialization_GH_Chunk_SetDoubleArray_1.htm)|  Add a new data
item to this chunk. The combination of name and index must be unique or an
exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetDrawingBitmap(String,
Bitmap)](M_GH_IO_Serialization_GH_Chunk_SetDrawingBitmap.htm)|  Add a new data
item to this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetDrawingBitmap(String, Int32,
Bitmap)](M_GH_IO_Serialization_GH_Chunk_SetDrawingBitmap_1.htm)|  Add a new
data item to this chunk. The name must be unique or an exception will be
thrown.  
![Public method](../icons/pubmethod.gif)| [SetDrawingColor(String,
Color)](M_GH_IO_Serialization_GH_Chunk_SetDrawingColor.htm)|  Add a new data
item to this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetDrawingColor(String, Int32,
Color)](M_GH_IO_Serialization_GH_Chunk_SetDrawingColor_1.htm)|  Add a new data
item to this chunk. The combination of name and index must be unique or an
exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetDrawingPoint(String,
Point)](M_GH_IO_Serialization_GH_Chunk_SetDrawingPoint.htm)|  Add a new data
item to this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetDrawingPoint(String, Int32,
Point)](M_GH_IO_Serialization_GH_Chunk_SetDrawingPoint_1.htm)|  Add a new data
item to this chunk. The combination of name and index must be unique or an
exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetDrawingPointF(String,
PointF)](M_GH_IO_Serialization_GH_Chunk_SetDrawingPointF.htm)|  Add a new data
item to this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetDrawingPointF(String, Int32,
PointF)](M_GH_IO_Serialization_GH_Chunk_SetDrawingPointF_1.htm)|  Add a new
data item to this chunk. The combination of name and index must be unique or
an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetDrawingRectangle(String,
Rectangle)](M_GH_IO_Serialization_GH_Chunk_SetDrawingRectangle.htm)|  Add a
new data item to this chunk. The name must be unique or an exception will be
thrown.  
![Public method](../icons/pubmethod.gif)| [SetDrawingRectangle(String, Int32,
Rectangle)](M_GH_IO_Serialization_GH_Chunk_SetDrawingRectangle_1.htm)|  Add a
new data item to this chunk. The combination of name and index must be unique
or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetDrawingRectangleF(String,
RectangleF)](M_GH_IO_Serialization_GH_Chunk_SetDrawingRectangleF.htm)|  Add a
new data item to this chunk. The name must be unique or an exception will be
thrown.  
![Public method](../icons/pubmethod.gif)| [SetDrawingRectangleF(String, Int32,
RectangleF)](M_GH_IO_Serialization_GH_Chunk_SetDrawingRectangleF_1.htm)|  Add
a new data item to this chunk. The combination of name and index must be
unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetDrawingSize(String,
Size)](M_GH_IO_Serialization_GH_Chunk_SetDrawingSize.htm)|  Add a new data
item to this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetDrawingSize(String, Int32,
Size)](M_GH_IO_Serialization_GH_Chunk_SetDrawingSize_1.htm)|  Add a new data
item to this chunk. The combination of name and index must be unique or an
exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetDrawingSizeF(String,
SizeF)](M_GH_IO_Serialization_GH_Chunk_SetDrawingSizeF.htm)|  Add a new data
item to this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetDrawingSizeF(String, Int32,
SizeF)](M_GH_IO_Serialization_GH_Chunk_SetDrawingSizeF_1.htm)|  Add a new data
item to this chunk. The combination of name and index must be unique or an
exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetGuid(String,
Guid)](M_GH_IO_Serialization_GH_Chunk_SetGuid.htm)|  Add a new data item to
this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetGuid(String, Int32,
Guid)](M_GH_IO_Serialization_GH_Chunk_SetGuid_1.htm)|  Add a new data item to
this chunk. The combination of name and index must be unique or an exception
will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetInt32(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_SetInt32.htm)|  Add a new data item to
this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetInt32(String, Int32,
Int32)](M_GH_IO_Serialization_GH_Chunk_SetInt32_1.htm)|  Add a new data item
to this chunk. The combination of name and index must be unique or an
exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetInt64(String,
Int64)](M_GH_IO_Serialization_GH_Chunk_SetInt64_1.htm)|  Add a new data item
to this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetInt64(String, Int32,
Int64)](M_GH_IO_Serialization_GH_Chunk_SetInt64.htm)|  Add a new data item to
this chunk. The combination of name and index must be unique or an exception
will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetInterval1D(String,
GH_Interval1D)](M_GH_IO_Serialization_GH_Chunk_SetInterval1D.htm)|  Add a new
data item to this chunk. The name must be unique or an exception will be
thrown.  
![Public method](../icons/pubmethod.gif)| [SetInterval1D(String, Int32,
GH_Interval1D)](M_GH_IO_Serialization_GH_Chunk_SetInterval1D_1.htm)|  Add a
new data item to this chunk. The combination of name and index must be unique
or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetInterval2D(String,
GH_Interval2D)](M_GH_IO_Serialization_GH_Chunk_SetInterval2D.htm)|  Add a new
data item to this chunk. The name must be unique or an exception will be
thrown.  
![Public method](../icons/pubmethod.gif)| [SetInterval2D(String, Int32,
GH_Interval2D)](M_GH_IO_Serialization_GH_Chunk_SetInterval2D_1.htm)|  Add a
new data item to this chunk. The combination of name and index must be unique
or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetLine(String,
GH_Line)](M_GH_IO_Serialization_GH_Chunk_SetLine.htm)|  Add a new data item to
this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetLine(String, Int32,
GH_Line)](M_GH_IO_Serialization_GH_Chunk_SetLine_1.htm)|  Add a new data item
to this chunk. The combination of name and index must be unique or an
exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetPath(String, String,
String)](M_GH_IO_Serialization_GH_Chunk_SetPath_1.htm)|  Add a new data item
to this chunk. The combination of name and index must be unique or an
exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetPath(String, Int32, String,
String)](M_GH_IO_Serialization_GH_Chunk_SetPath.htm)|  Add a new data item to
this chunk. The combination of name and index must be unique or an exception
will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetPlane(String,
GH_Plane)](M_GH_IO_Serialization_GH_Chunk_SetPlane.htm)|  Add a new data item
to this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetPlane(String, Int32,
GH_Plane)](M_GH_IO_Serialization_GH_Chunk_SetPlane_1.htm)|  Add a new data
item to this chunk. The combination of name and index must be unique or an
exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetPoint2D(String,
GH_Point2D)](M_GH_IO_Serialization_GH_Chunk_SetPoint2D.htm)|  Add a new data
item to this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetPoint2D(String, Int32,
GH_Point2D)](M_GH_IO_Serialization_GH_Chunk_SetPoint2D_1.htm)|  Add a new data
item to this chunk. The combination of name and index must be unique or an
exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetPoint3D(String,
GH_Point3D)](M_GH_IO_Serialization_GH_Chunk_SetPoint3D.htm)|  Add a new data
item to this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetPoint3D(String, Int32,
GH_Point3D)](M_GH_IO_Serialization_GH_Chunk_SetPoint3D_1.htm)|  Add a new data
item to this chunk. The combination of name and index must be unique or an
exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetPoint4D(String,
GH_Point4D)](M_GH_IO_Serialization_GH_Chunk_SetPoint4D.htm)|  Add a new data
item to this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetPoint4D(String, Int32,
GH_Point4D)](M_GH_IO_Serialization_GH_Chunk_SetPoint4D_1.htm)|  Add a new data
item to this chunk. The combination of name and index must be unique or an
exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetSingle(String,
Single)](M_GH_IO_Serialization_GH_Chunk_SetSingle_1.htm)|  Add a new data item
to this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetSingle(String, Int32,
Single)](M_GH_IO_Serialization_GH_Chunk_SetSingle.htm)|  Add a new data item
to this chunk. The combination of name and index must be unique or an
exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetString(String,
String)](M_GH_IO_Serialization_GH_Chunk_SetString_1.htm)|  Add a new data item
to this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetString(String, Int32,
String)](M_GH_IO_Serialization_GH_Chunk_SetString.htm)|  Add a new data item
to this chunk. The combination of name and index must be unique or an
exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetVersion(String,
GH_Version)](M_GH_IO_Serialization_GH_Chunk_SetVersion.htm)|  Add a new data
item to this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetVersion(String, Int32,
GH_Version)](M_GH_IO_Serialization_GH_Chunk_SetVersion_1.htm)|  Add a new data
item to this chunk. The combination of name and index must be unique or an
exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetVersion(String, Int32, Int32,
Int32)](M_GH_IO_Serialization_GH_Chunk_SetVersion_2.htm)|  Add a new data item
to this chunk. The name must be unique or an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [SetVersion(String, Int32, Int32,
Int32, Int32)](M_GH_IO_Serialization_GH_Chunk_SetVersion_3.htm)|  Add a new
data item to this chunk. The combination of name and index must be unique or
an exception will be thrown.  
![Public method](../icons/pubmethod.gif)| [TryGetBoolean(String,
Boolean)](M_GH_IO_Serialization_GH_Chunk_TryGetBoolean.htm)|  Gets the value
of the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetBoolean(String, Int32,
Boolean)](M_GH_IO_Serialization_GH_Chunk_TryGetBoolean_1.htm)|  Gets the value
of the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetBoundingBox(String,
GH_BoundingBox)](M_GH_IO_Serialization_GH_Chunk_TryGetBoundingBox.htm)|  Gets
the value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetBoundingBox(String, Int32,
GH_BoundingBox)](M_GH_IO_Serialization_GH_Chunk_TryGetBoundingBox_1.htm)|
Gets the value of the item with the specified name and index. Name comparison
is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetByte(String,
Byte)](M_GH_IO_Serialization_GH_Chunk_TryGetByte.htm)|  Gets the value of the
item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetByte(String, Int32,
Byte)](M_GH_IO_Serialization_GH_Chunk_TryGetByte_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDate(String,
DateTime)](M_GH_IO_Serialization_GH_Chunk_TryGetDate.htm)|  Gets the value of
the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDate(String, Int32,
DateTime)](M_GH_IO_Serialization_GH_Chunk_TryGetDate_1.htm)|  Gets the value
of the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDecimal(String,
Decimal)](M_GH_IO_Serialization_GH_Chunk_TryGetDecimal.htm)|  Gets the value
of the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDecimal(String, Int32,
Decimal)](M_GH_IO_Serialization_GH_Chunk_TryGetDecimal_1.htm)|  Gets the value
of the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDouble(String,
Double)](M_GH_IO_Serialization_GH_Chunk_TryGetDouble.htm)|  Gets the value of
the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDouble(String, Int32,
Double)](M_GH_IO_Serialization_GH_Chunk_TryGetDouble_1.htm)|  Gets the value
of the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingColor(String,
Color)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingColor.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingColor(String, Int32,
Color)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingColor_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingPoint(String,
Point)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingPoint.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingPoint(String, Int32,
Point)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingPoint_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingPointF(String,
PointF)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingPointF.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingPointF(String, Int32,
PointF)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingPointF_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingRectangle(String,
Rectangle)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingRectangle.htm)|  Gets
the value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingRectangle(String,
Int32,
Rectangle)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingRectangle_1.htm)|
Gets the value of the item with the specified name and index. Name comparison
is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingRectangleF(String,
RectangleF)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingRectangleF.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingRectangleF(String,
Int32,
RectangleF)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingRectangleF_1.htm)|
Gets the value of the item with the specified name and index. Name comparison
is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingSize(String,
Size)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingSize.htm)|  Gets the value
of the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingSize(String, Int32,
Size)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingSize_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingSizeF(String,
SizeF)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingSizeF.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingSizeF(String, Int32,
SizeF)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingSizeF_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetGuid(String,
Guid)](M_GH_IO_Serialization_GH_Chunk_TryGetGuid.htm)|  Gets the value of the
item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetGuid(String, Int32,
Guid)](M_GH_IO_Serialization_GH_Chunk_TryGetGuid_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetInt32(String,
Int32)](M_GH_IO_Serialization_GH_Chunk_TryGetInt32_1.htm)|  Gets the value of
the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetInt32(String, Int32,
Int32)](M_GH_IO_Serialization_GH_Chunk_TryGetInt32.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetInt64(String,
Int64)](M_GH_IO_Serialization_GH_Chunk_TryGetInt64_1.htm)|  Gets the value of
the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetInt64(String, Int32,
Int64)](M_GH_IO_Serialization_GH_Chunk_TryGetInt64.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetInterval1D(String,
GH_Interval1D)](M_GH_IO_Serialization_GH_Chunk_TryGetInterval1D.htm)|  Gets
the value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetInterval1D(String, Int32,
GH_Interval1D)](M_GH_IO_Serialization_GH_Chunk_TryGetInterval1D_1.htm)|  Gets
the value of the item with the specified name and index. Name comparison is
not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetInterval2D(String,
GH_Interval2D)](M_GH_IO_Serialization_GH_Chunk_TryGetInterval2D.htm)|  Gets
the value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetInterval2D(String, Int32,
GH_Interval2D)](M_GH_IO_Serialization_GH_Chunk_TryGetInterval2D_1.htm)|  Gets
the value of the item with the specified name and index. Name comparison is
not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetLine(String,
GH_Line)](M_GH_IO_Serialization_GH_Chunk_TryGetLine.htm)|  Gets the value of
the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetLine(String, Int32,
GH_Line)](M_GH_IO_Serialization_GH_Chunk_TryGetLine_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetPlane(String,
GH_Plane)](M_GH_IO_Serialization_GH_Chunk_TryGetPlane.htm)|  Gets the value of
the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetPlane(String, Int32,
GH_Plane)](M_GH_IO_Serialization_GH_Chunk_TryGetPlane_1.htm)|  Gets the value
of the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetPoint2D(String,
GH_Point2D)](M_GH_IO_Serialization_GH_Chunk_TryGetPoint2D.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetPoint2D(String, Int32,
GH_Point2D)](M_GH_IO_Serialization_GH_Chunk_TryGetPoint2D_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetPoint3D(String,
GH_Point3D)](M_GH_IO_Serialization_GH_Chunk_TryGetPoint3D.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetPoint3D(String, Int32,
GH_Point3D)](M_GH_IO_Serialization_GH_Chunk_TryGetPoint3D_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetPoint4D(String,
GH_Point4D)](M_GH_IO_Serialization_GH_Chunk_TryGetPoint4D.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetPoint4D(String, Int32,
GH_Point4D)](M_GH_IO_Serialization_GH_Chunk_TryGetPoint4D_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetSingle(String,
Single)](M_GH_IO_Serialization_GH_Chunk_TryGetSingle_1.htm)|  Gets the value
of the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetSingle(String, Int32,
Single)](M_GH_IO_Serialization_GH_Chunk_TryGetSingle.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetString(String,
String)](M_GH_IO_Serialization_GH_Chunk_TryGetString_1.htm)|  Gets the value
of the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetString(String, Int32,
String)](M_GH_IO_Serialization_GH_Chunk_TryGetString.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetVersion(String,
GH_Version)](M_GH_IO_Serialization_GH_Chunk_TryGetVersion.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetVersion(String, Int32,
GH_Version)](M_GH_IO_Serialization_GH_Chunk_TryGetVersion_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[Write(BinaryWriter)](M_GH_IO_Serialization_GH_Chunk_Write.htm)|  Write this
chunk and all child chunks to a binary stream.  
![Public method](../icons/pubmethod.gif)|
[Write(XmlWriter)](M_GH_IO_Serialization_GH_Chunk_Write_1.htm)|  Serialize
this chunk into an Xml stream.  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Protected field](../icons/protfield.gif)|
[m_archive](F_GH_IO_Serialization_GH_Chunk_m_archive.htm)|  Pointer to the
archive that owns the Root of the tree this chunk belongs to.  
![Protected field](../icons/protfield.gif)|
[m_chunks](F_GH_IO_Serialization_GH_Chunk_m_chunks.htm)|  Dictionary of sub-
chunks contained within this chunk.  
![Protected field](../icons/protfield.gif)|
[m_comments](F_GH_IO_Serialization_GH_Chunk_m_comments.htm)|  List of text
comments. This list is automatically instantiated once the first comment is
added.  
![Protected field](../icons/protfield.gif)|
[m_index](F_GH_IO_Serialization_GH_Chunk_m_index.htm)|  Index of this chunk.
This field is set only once, during construction. A negative index indicates
no index qualifier has been set.  
![Protected field](../icons/protfield.gif)|
[m_items](F_GH_IO_Serialization_GH_Chunk_m_items.htm)|  The list of nodes
contained within this chunk.  
![Protected field](../icons/protfield.gif)|
[m_name](F_GH_IO_Serialization_GH_Chunk_m_name.htm)|  Name of this chunk. This
field is set only once, during construction.  
![Protected field](../icons/protfield.gif)![Static
member](../icons/static.gif)|
[name_comp](F_GH_IO_Serialization_GH_Chunk_name_comp.htm)|  Comparison flag to
use when comparing names.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

