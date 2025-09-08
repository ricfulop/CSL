---
url: https://developer.rhino3d.com/api/grasshopper/html/T_GH_IO_Serialization_GH_Message_Type.htm
scraped_at: 2025-09-08T16:10:48.848477
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

# GH_Message_Type Enumeration  
  
---  
  
Message type flag.

**Namespace:** [GH_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:** GH_IO (in GH_IO.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public enum GH_Message_Type
    
    
    Public Enumeration GH_Message_Type

![](../icons/SectionExpanded.png)Members

| Member name| Value| Description  
---|---|---|---  
| info| 0|  Indicates a message represents information.  
| warning| 1|  Indicates the message represents a warning. Warnings are not
severe enough to be regarded as IO errors.  
| error| 2|  Indicates the message represents an error. Errors mean
(de)serialization failed (partially).  
  
![](../icons/SectionExpanded.png)See Also

#### Reference

[GH_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

