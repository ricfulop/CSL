---
url: https://developer.rhino3d.com/api/grasshopper/html/T_GH_IO_Serialization_GH_IReader.htm
scraped_at: 2025-09-08T16:10:43.869541
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[GH_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH_IReader Interface](../html/T_GH_IO_Serialization_GH_IReader.htm
"GH_IReader Interface")

[GH_IReader
Properties](../html/Properties_T_GH_IO_Serialization_GH_IReader.htm
"GH_IReader Properties")

[GH_IReader Methods](../html/Methods_T_GH_IO_Serialization_GH_IReader.htm
"GH_IReader Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_IReader Interface  
  
---  
  
Provides access to a subset of GH_Chunk methods used for reading archives.

**Namespace:** [GH_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:** GH_IO (in GH_IO.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface GH_IReader : GH_IChunk, 
    	GH_IBinarySupport, GH_IXmlSupport
    
    
    Public Interface GH_IReader
    	Inherits GH_IChunk, GH_IBinarySupport, GH_IXmlSupport

The GH_IReader type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Archive](P_GH_IO_Serialization_GH_IChunk_Archive.htm)|  Gets a pointer to the
archive that owns the Root of the tree this chunk belongs to.  (Inherited from
[GH_IChunk](T_GH_IO_Serialization_GH_IChunk.htm).)  
![Public property](../icons/pubproperty.gif)|
[ArchiveLocation](P_GH_IO_Serialization_GH_IChunk_ArchiveLocation.htm)|  Gets
a string representing the URI with which the archive is associated. The
location may be a null string.  (Inherited from
[GH_IChunk](T_GH_IO_Serialization_GH_IChunk.htm).)  
![Public property](../icons/pubproperty.gif)|
[ChunkCount](P_GH_IO_Serialization_GH_IChunk_ChunkCount.htm)|  Gets the number
of child chunks contained in this chunk. The set of all child chunks is
referred to as a 'litter'.  (Inherited from
[GH_IChunk](T_GH_IO_Serialization_GH_IChunk.htm).)  
![Public property](../icons/pubproperty.gif)|
[Chunks](P_GH_IO_Serialization_GH_IChunk_Chunks.htm)|  Gets a pointer to the
internal list of child chunks. Do not access this list unless you know what
you are doing.  (Inherited from
[GH_IChunk](T_GH_IO_Serialization_GH_IChunk.htm).)  
![Public property](../icons/pubproperty.gif)|
[Index](P_GH_IO_Serialization_GH_IChunk_Index.htm)|  Gets the index of this
chunk. The index is set by the owner of this chunk. Indices smaller than zero
imply no index has been set. The combination of name+index is always unique
among a set of chunks in the same litter.  (Inherited from
[GH_IChunk](T_GH_IO_Serialization_GH_IChunk.htm).)  
![Public property](../icons/pubproperty.gif)|
[ItemCount](P_GH_IO_Serialization_GH_IChunk_ItemCount.htm)|  Gets the number
of items contained in this chunk.  (Inherited from
[GH_IChunk](T_GH_IO_Serialization_GH_IChunk.htm).)  
![Public property](../icons/pubproperty.gif)|
[Items](P_GH_IO_Serialization_GH_IChunk_Items.htm)|  Gets a pointer to the
internal list of items. Do not access this list unless you know what you are
doing.  (Inherited from [GH_IChunk](T_GH_IO_Serialization_GH_IChunk.htm).)  
![Public property](../icons/pubproperty.gif)|
[Name](P_GH_IO_Serialization_GH_IChunk_Name.htm)|  Gets the name of this
chunk. The name is set by the owner of this chunk. Names must be at least 1
character long. The combination of name+index is always unique among a set of
chunks in a single litter.  (Inherited from
[GH_IChunk](T_GH_IO_Serialization_GH_IChunk.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AddMessage](M_GH_IO_Serialization_GH_IChunk_AddMessage.htm)|  Log a new
message with the top-level archive. Messages are collected during read/write
operations, and can be displayed to the user upon completion using
GH_Archive.ShowMessageLog().  (Inherited from
[GH_IChunk](T_GH_IO_Serialization_GH_IChunk.htm).)  
![Public method](../icons/pubmethod.gif)|
[ChunkExists(String)](M_GH_IO_Serialization_GH_IReader_ChunkExists.htm)|
Checks whether a chunk with the specified name exists in the litter. Only
chunks without index qualifiers are considered. Name comparisons are not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [ChunkExists(String,
Int32)](M_GH_IO_Serialization_GH_IReader_ChunkExists_1.htm)|  Checks whether a
chunk with the specified name and index exists in the litter. Only chunks with
index qualifiers are considered. Name comparisons are not case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[FindChunk(String)](M_GH_IO_Serialization_GH_IReader_FindChunk.htm)|  Finds
the first chunk in the litter that matches the given name. Only chunks without
index qualifiers are considered.  
![Public method](../icons/pubmethod.gif)| [FindChunk(String,
Int32)](M_GH_IO_Serialization_GH_IReader_FindChunk_1.htm)|  Finds the first
chunk in the list that matches the given name and index. Only chunks with
index qualifiers are considered.  
![Public method](../icons/pubmethod.gif)|
[FindItem(String)](M_GH_IO_Serialization_GH_IReader_FindItem.htm)|  Finds the
first item that matches the given name. Only items without index qualifiers
are considered. Name comparisons are not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [FindItem(String,
Int32)](M_GH_IO_Serialization_GH_IReader_FindItem_1.htm)|  Finds the first
item that matches the given name and index. Only items with index qualifiers
are considered. Name comparisons are not case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetBoolean(String)](M_GH_IO_Serialization_GH_IReader_GetBoolean.htm)|  Gets
the value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetBoolean(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetBoolean_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetBoundingBox(String)](M_GH_IO_Serialization_GH_IReader_GetBoundingBox.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetBoundingBox(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetBoundingBox_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetByte(String)](M_GH_IO_Serialization_GH_IReader_GetByte.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetByte(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetByte_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetByteArray(String)](M_GH_IO_Serialization_GH_IReader_GetByteArray.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetByteArray(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetByteArray_1.htm)|  Gets the value
of the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetDate(String)](M_GH_IO_Serialization_GH_IReader_GetDate.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetDate(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetDate_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetDecimal(String)](M_GH_IO_Serialization_GH_IReader_GetDecimal.htm)|  Gets
the value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetDecimal(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetDecimal_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetDouble(String)](M_GH_IO_Serialization_GH_IReader_GetDouble.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetDouble(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetDouble_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetDoubleArray(String)](M_GH_IO_Serialization_GH_IReader_GetDoubleArray.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetDoubleArray(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetDoubleArray_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetDrawingBitmap(String)](M_GH_IO_Serialization_GH_IReader_GetDrawingBitmap.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetDrawingBitmap(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetDrawingBitmap_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetDrawingColor(String)](M_GH_IO_Serialization_GH_IReader_GetDrawingColor.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetDrawingColor(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetDrawingColor_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetDrawingPoint(String)](M_GH_IO_Serialization_GH_IReader_GetDrawingPoint.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetDrawingPoint(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetDrawingPoint_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetDrawingPointF(String)](M_GH_IO_Serialization_GH_IReader_GetDrawingPointF.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetDrawingPointF(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetDrawingPointF_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetDrawingRectangle(String)](M_GH_IO_Serialization_GH_IReader_GetDrawingRectangle.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetDrawingRectangle(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetDrawingRectangle_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetDrawingRectangleF(String)](M_GH_IO_Serialization_GH_IReader_GetDrawingRectangleF.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetDrawingRectangleF(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetDrawingRectangleF_1.htm)|  Gets
the value of the item with the specified name and index. Name comparison is
not case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetDrawingSize(String)](M_GH_IO_Serialization_GH_IReader_GetDrawingSize.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetDrawingSize(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetDrawingSize_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetDrawingSizeF(String)](M_GH_IO_Serialization_GH_IReader_GetDrawingSizeF.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetDrawingSizeF(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetDrawingSizeF_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetGuid(String)](M_GH_IO_Serialization_GH_IReader_GetGuid.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetGuid(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetGuid_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetInt32(String)](M_GH_IO_Serialization_GH_IReader_GetInt32.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetInt32(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetInt32_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetInt64(String)](M_GH_IO_Serialization_GH_IReader_GetInt64.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetInt64(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetInt64_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetInterval1D(String)](M_GH_IO_Serialization_GH_IReader_GetInterval1D.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetInterval1D(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetInterval1D_1.htm)|  Gets the value
of the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetInterval2D(String)](M_GH_IO_Serialization_GH_IReader_GetInterval2D.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetInterval2D(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetInterval2D_1.htm)|  Gets the value
of the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetLine(String)](M_GH_IO_Serialization_GH_IReader_GetLine.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetLine(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetLine_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetPath(String,
String)](M_GH_IO_Serialization_GH_IReader_GetPath_1.htm)|  Gets the value of
the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [GetPath(String, Int32,
String)](M_GH_IO_Serialization_GH_IReader_GetPath.htm)|  Gets the value of the
item with the specified name and index. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetPlane(String)](M_GH_IO_Serialization_GH_IReader_GetPlane.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetPlane(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetPlane_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetPoint2D(String)](M_GH_IO_Serialization_GH_IReader_GetPoint2D.htm)|  Gets
the value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetPoint2D(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetPoint2D_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetPoint3D(String)](M_GH_IO_Serialization_GH_IReader_GetPoint3D.htm)|  Gets
the value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetPoint3D(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetPoint3D_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetPoint4D(String)](M_GH_IO_Serialization_GH_IReader_GetPoint4D.htm)|  Gets
the value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetPoint4D(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetPoint4D_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetSingle(String)](M_GH_IO_Serialization_GH_IReader_GetSingle.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetSingle(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetSingle_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetString(String)](M_GH_IO_Serialization_GH_IReader_GetString.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetString(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetString_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[GetVersion(String)](M_GH_IO_Serialization_GH_IReader_GetVersion.htm)|  Gets
the value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [GetVersion(String,
Int32)](M_GH_IO_Serialization_GH_IReader_GetVersion_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)|
[ItemExists(String)](M_GH_IO_Serialization_GH_IReader_ItemExists.htm)|  Checks
whether an item with the specified name exists. Only items without index
qualifiers are considered. Name comparisons are not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [ItemExists(String,
Int32)](M_GH_IO_Serialization_GH_IReader_ItemExists_1.htm)|  Checks whether an
item with the specified name and index exists. Only items with index
qualifiers are considered. Name comparisons are not case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[Read(BinaryReader)](M_GH_IO_Serialization_GH_IBinarySupport_Read.htm)|
Called when an object is required to deserialize itself.  (Inherited from
[GH_IBinarySupport](T_GH_IO_Serialization_GH_IBinarySupport.htm).)  
![Public method](../icons/pubmethod.gif)|
[Read(XmlNode)](M_GH_IO_Serialization_GH_IXmlSupport_Read.htm)|  Called when
an object is required to deserialize itself.  (Inherited from
[GH_IXmlSupport](T_GH_IO_Serialization_GH_IXmlSupport.htm).)  
![Public method](../icons/pubmethod.gif)| [TryGetBoolean(String,
Boolean)](M_GH_IO_Serialization_GH_IReader_TryGetBoolean.htm)|  Gets the value
of the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetBoolean(String, Int32,
Boolean)](M_GH_IO_Serialization_GH_IReader_TryGetBoolean_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetBoundingBox(String,
GH_BoundingBox)](M_GH_IO_Serialization_GH_IReader_TryGetBoundingBox.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetBoundingBox(String, Int32,
GH_BoundingBox)](M_GH_IO_Serialization_GH_IReader_TryGetBoundingBox_1.htm)|
Gets the value of the item with the specified name and index. Name comparison
is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetByte(String,
Byte)](M_GH_IO_Serialization_GH_IReader_TryGetByte.htm)|  Gets the value of
the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetByte(String, Int32,
Byte)](M_GH_IO_Serialization_GH_IReader_TryGetByte_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDate(String,
DateTime)](M_GH_IO_Serialization_GH_IReader_TryGetDate.htm)|  Gets the value
of the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDate(String, Int32,
DateTime)](M_GH_IO_Serialization_GH_IReader_TryGetDate_1.htm)|  Gets the value
of the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDecimal(String,
Decimal)](M_GH_IO_Serialization_GH_IReader_TryGetDecimal.htm)|  Gets the value
of the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDecimal(String, Int32,
Decimal)](M_GH_IO_Serialization_GH_IReader_TryGetDecimal_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDouble(String,
Double)](M_GH_IO_Serialization_GH_IReader_TryGetDouble.htm)|  Gets the value
of the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDouble(String, Int32,
Double)](M_GH_IO_Serialization_GH_IReader_TryGetDouble_1.htm)|  Gets the value
of the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingColor(String,
Color)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingColor.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingColor(String, Int32,
Color)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingColor_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingPoint(String,
Point)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingPoint.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingPoint(String, Int32,
Point)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingPoint_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingPointF(String,
PointF)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingPointF.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingPointF(String, Int32,
PointF)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingPointF_1.htm)|  Gets
the value of the item with the specified name and index. Name comparison is
not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingRectangle(String,
Rectangle)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingRectangle.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingRectangle(String,
Int32,
Rectangle)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingRectangle_1.htm)|
Gets the value of the item with the specified name and index. Name comparison
is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingRectangleF(String,
RectangleF)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingRectangleF.htm)|
Gets the value of the item with the specified name. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingRectangleF(String,
Int32,
RectangleF)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingRectangleF_1.htm)|
Gets the value of the item with the specified name and index. Name comparison
is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingSize(String,
Size)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingSize.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingSize(String, Int32,
Size)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingSize_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingSizeF(String,
SizeF)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingSizeF.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetDrawingSizeF(String, Int32,
SizeF)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingSizeF_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetGuid(String,
Guid)](M_GH_IO_Serialization_GH_IReader_TryGetGuid.htm)|  Gets the value of
the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetGuid(String, Int32,
Guid)](M_GH_IO_Serialization_GH_IReader_TryGetGuid_1.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetInt32(String,
Int32)](M_GH_IO_Serialization_GH_IReader_TryGetInt32_1.htm)|  Gets the value
of the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetInt32(String, Int32,
Int32)](M_GH_IO_Serialization_GH_IReader_TryGetInt32.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetInt64(String,
Int64)](M_GH_IO_Serialization_GH_IReader_TryGetInt64_1.htm)|  Gets the value
of the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetInt64(String, Int32,
Int64)](M_GH_IO_Serialization_GH_IReader_TryGetInt64.htm)|  Gets the value of
the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetInterval1D(String,
GH_Interval1D)](M_GH_IO_Serialization_GH_IReader_TryGetInterval1D.htm)|  Gets
the value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetInterval1D(String, Int32,
GH_Interval1D)](M_GH_IO_Serialization_GH_IReader_TryGetInterval1D_1.htm)|
Gets the value of the item with the specified name and index. Name comparison
is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetInterval2D(String,
GH_Interval2D)](M_GH_IO_Serialization_GH_IReader_TryGetInterval2D.htm)|  Gets
the value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetInterval2D(String, Int32,
GH_Interval2D)](M_GH_IO_Serialization_GH_IReader_TryGetInterval2D_1.htm)|
Gets the value of the item with the specified name and index. Name comparison
is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetLine(String,
GH_Line)](M_GH_IO_Serialization_GH_IReader_TryGetLine.htm)|  Gets the value of
the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetLine(String, Int32,
GH_Line)](M_GH_IO_Serialization_GH_IReader_TryGetLine_1.htm)|  Gets the value
of the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetPlane(String,
GH_Plane)](M_GH_IO_Serialization_GH_IReader_TryGetPlane.htm)|  Gets the value
of the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetPlane(String, Int32,
GH_Plane)](M_GH_IO_Serialization_GH_IReader_TryGetPlane_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetPoint2D(String,
GH_Point2D)](M_GH_IO_Serialization_GH_IReader_TryGetPoint2D.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetPoint2D(String, Int32,
GH_Point2D)](M_GH_IO_Serialization_GH_IReader_TryGetPoint2D_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetPoint3D(String,
GH_Point3D)](M_GH_IO_Serialization_GH_IReader_TryGetPoint3D.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetPoint3D(String, Int32,
GH_Point3D)](M_GH_IO_Serialization_GH_IReader_TryGetPoint3D_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetPoint4D(String,
GH_Point4D)](M_GH_IO_Serialization_GH_IReader_TryGetPoint4D.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetPoint4D(String, Int32,
GH_Point4D)](M_GH_IO_Serialization_GH_IReader_TryGetPoint4D_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetSingle(String,
Single)](M_GH_IO_Serialization_GH_IReader_TryGetSingle_1.htm)|  Gets the value
of the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetSingle(String, Int32,
Single)](M_GH_IO_Serialization_GH_IReader_TryGetSingle.htm)|  Gets the value
of the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetString(String,
String)](M_GH_IO_Serialization_GH_IReader_TryGetString_1.htm)|  Gets the value
of the item with the specified name. Name comparison is not case-sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetString(String, Int32,
String)](M_GH_IO_Serialization_GH_IReader_TryGetString.htm)|  Gets the value
of the item with the specified name and index. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetVersion(String,
GH_Version)](M_GH_IO_Serialization_GH_IReader_TryGetVersion.htm)|  Gets the
value of the item with the specified name. Name comparison is not case-
sensitive.  
![Public method](../icons/pubmethod.gif)| [TryGetVersion(String, Int32,
GH_Version)](M_GH_IO_Serialization_GH_IReader_TryGetVersion_1.htm)|  Gets the
value of the item with the specified name and index. Name comparison is not
case-sensitive.  
![Public method](../icons/pubmethod.gif)|
[Write(BinaryWriter)](M_GH_IO_Serialization_GH_IBinarySupport_Write.htm)|
Called when an object is required to serialize itself.  (Inherited from
[GH_IBinarySupport](T_GH_IO_Serialization_GH_IBinarySupport.htm).)  
![Public method](../icons/pubmethod.gif)|
[Write(XmlWriter)](M_GH_IO_Serialization_GH_IXmlSupport_Write.htm)|  Called
when an object is required to serialize itself.  (Inherited from
[GH_IXmlSupport](T_GH_IO_Serialization_GH_IXmlSupport.htm).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

