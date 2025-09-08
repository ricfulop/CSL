---
url: https://developer.rhino3d.com/api/grasshopper/html/N_GH_IO_Serialization.htm#!
scraped_at: 2025-09-08T16:10:36.780714
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[GH_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH_Archive Class](../html/T_GH_IO_Serialization_GH_Archive.htm "GH_Archive
Class")

[GH_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH_Chunk.ChunkKeyedCollection
Class](../html/T_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection.htm
"GH_Chunk.ChunkKeyedCollection Class")

[GH_Compression Class](../html/T_GH_IO_Serialization_GH_Compression.htm
"GH_Compression Class")

[GH_IBinarySupport
Interface](../html/T_GH_IO_Serialization_GH_IBinarySupport.htm
"GH_IBinarySupport Interface")

[GH_IChunk Interface](../html/T_GH_IO_Serialization_GH_IChunk.htm "GH_IChunk
Interface")

[GH_IReader Interface](../html/T_GH_IO_Serialization_GH_IReader.htm
"GH_IReader Interface")

[GH_IWriter Interface](../html/T_GH_IO_Serialization_GH_IWriter.htm
"GH_IWriter Interface")

[GH_IXmlSupport Interface](../html/T_GH_IO_Serialization_GH_IXmlSupport.htm
"GH_IXmlSupport Interface")

[GH_LooseChunk Class](../html/T_GH_IO_Serialization_GH_LooseChunk.htm
"GH_LooseChunk Class")

[GH_Message Class](../html/T_GH_IO_Serialization_GH_Message.htm "GH_Message
Class")

[GH_Message_Type
Enumeration](../html/T_GH_IO_Serialization_GH_Message_Type.htm
"GH_Message_Type Enumeration")

[ID Structure](../html/T_GH_IO_Serialization_ID.htm "ID Structure")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_IO.Serialization Namespace  
  
---  
  
Namespace in GH_IO.dll that contains all the classes used during
(de)serialization.

![](../icons/SectionExpanded.png)Classes

| Class| Description  
---|---|---  
![Public class](../icons/pubclass.gif)|
[GH_Archive](T_GH_IO_Serialization_GH_Archive.htm)|  This is the base archive
class which takes care of all (de)serialization and messaging.  
![Public class](../icons/pubclass.gif)|
[GH_Chunk](T_GH_IO_Serialization_GH_Chunk.htm)|  Full implementation of
GH_IChunk, GH_IReader, GH_IWriter, GH_IBinarySupport and GH_IXmlSupport.
Instances of this class are usually disguised as one of the interfaces it
implements.  
![Public class](../icons/pubclass.gif)|
[GH_ChunkChunkKeyedCollection](T_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection.htm)|
Represents a collection of chunks with associated IDs  
![Public class](../icons/pubclass.gif)|
[GH_Compression](T_GH_IO_Serialization_GH_Compression.htm)|  Provides static
methods for compression of byte-arrays.  
![Public class](../icons/pubclass.gif)|
[GH_LooseChunk](T_GH_IO_Serialization_GH_LooseChunk.htm)|  A utility class for
creating partial archives.  
![Public class](../icons/pubclass.gif)|
[GH_Message](T_GH_IO_Serialization_GH_Message.htm)|  Represents an archive log
message. Messages are collected during read/write operations.  
  
![](../icons/SectionExpanded.png)Structures

| Structure| Description  
---|---|---  
![Public structure](../icons/pubstructure.gif)|
[ID](T_GH_IO_Serialization_ID.htm)|  An ID is used to uniquely identify a
specific item.  
  
![](../icons/SectionExpanded.png)Interfaces

| Interface| Description  
---|---|---  
![Public interface](../icons/pubinterface.gif)|
[GH_IBinarySupport](T_GH_IO_Serialization_GH_IBinarySupport.htm)|  Interface
which declares all methods required for objects that can be (de)serialized to
and from a binary archive.  
![Public interface](../icons/pubinterface.gif)|
[GH_IChunk](T_GH_IO_Serialization_GH_IChunk.htm)|  Base interface for all
Archive Chunks.  
![Public interface](../icons/pubinterface.gif)|
[GH_IReader](T_GH_IO_Serialization_GH_IReader.htm)|  Provides access to a
subset of GH_Chunk methods used for reading archives.  
![Public interface](../icons/pubinterface.gif)|
[GH_IWriter](T_GH_IO_Serialization_GH_IWriter.htm)|  Provides access to a
subset of GH_Chunk methods used for writing archives.  
![Public interface](../icons/pubinterface.gif)|
[GH_IXmlSupport](T_GH_IO_Serialization_GH_IXmlSupport.htm)|  Interface which
declares all methods required for objects that can be (de)serialized to and
from an Xml archive.  
  
![](../icons/SectionExpanded.png)Enumerations

| Enumeration| Description  
---|---|---  
![Public enumeration](../icons/pubenumeration.gif)|
[GH_Message_Type](T_GH_IO_Serialization_GH_Message_Type.htm)|  Message type
flag.  
  
Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

