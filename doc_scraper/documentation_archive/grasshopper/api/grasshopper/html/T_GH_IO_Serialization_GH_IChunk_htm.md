---
url: https://developer.rhino3d.com/api/grasshopper/html/T_GH_IO_Serialization_GH_IChunk.htm
scraped_at: 2025-09-08T16:10:42.829713
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[GH_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH_IChunk Interface](../html/T_GH_IO_Serialization_GH_IChunk.htm "GH_IChunk
Interface")

[GH_IChunk Properties](../html/Properties_T_GH_IO_Serialization_GH_IChunk.htm
"GH_IChunk Properties")

[GH_IChunk Methods](../html/Methods_T_GH_IO_Serialization_GH_IChunk.htm
"GH_IChunk Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_IChunk Interface  
  
---  
  
Base interface for all Archive Chunks.

**Namespace:** [GH_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:** GH_IO (in GH_IO.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface GH_IChunk : GH_IBinarySupport, 
    	GH_IXmlSupport
    
    
    Public Interface GH_IChunk
    	Inherits GH_IBinarySupport, GH_IXmlSupport

The GH_IChunk type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Archive](P_GH_IO_Serialization_GH_IChunk_Archive.htm)|  Gets a pointer to the
archive that owns the Root of the tree this chunk belongs to.  
![Public property](../icons/pubproperty.gif)|
[ArchiveLocation](P_GH_IO_Serialization_GH_IChunk_ArchiveLocation.htm)|  Gets
a string representing the URI with which the archive is associated. The
location may be a null string.  
![Public property](../icons/pubproperty.gif)|
[ChunkCount](P_GH_IO_Serialization_GH_IChunk_ChunkCount.htm)|  Gets the number
of child chunks contained in this chunk. The set of all child chunks is
referred to as a 'litter'.  
![Public property](../icons/pubproperty.gif)|
[Chunks](P_GH_IO_Serialization_GH_IChunk_Chunks.htm)|  Gets a pointer to the
internal list of child chunks. Do not access this list unless you know what
you are doing.  
![Public property](../icons/pubproperty.gif)|
[Index](P_GH_IO_Serialization_GH_IChunk_Index.htm)|  Gets the index of this
chunk. The index is set by the owner of this chunk. Indices smaller than zero
imply no index has been set. The combination of name+index is always unique
among a set of chunks in the same litter.  
![Public property](../icons/pubproperty.gif)|
[ItemCount](P_GH_IO_Serialization_GH_IChunk_ItemCount.htm)|  Gets the number
of items contained in this chunk.  
![Public property](../icons/pubproperty.gif)|
[Items](P_GH_IO_Serialization_GH_IChunk_Items.htm)|  Gets a pointer to the
internal list of items. Do not access this list unless you know what you are
doing.  
![Public property](../icons/pubproperty.gif)|
[Name](P_GH_IO_Serialization_GH_IChunk_Name.htm)|  Gets the name of this
chunk. The name is set by the owner of this chunk. Names must be at least 1
character long. The combination of name+index is always unique among a set of
chunks in a single litter.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AddMessage](M_GH_IO_Serialization_GH_IChunk_AddMessage.htm)|  Log a new
message with the top-level archive. Messages are collected during read/write
operations, and can be displayed to the user upon completion using
GH_Archive.ShowMessageLog().  
![Public method](../icons/pubmethod.gif)|
[Read(BinaryReader)](M_GH_IO_Serialization_GH_IBinarySupport_Read.htm)|
Called when an object is required to deserialize itself.  (Inherited from
[GH_IBinarySupport](T_GH_IO_Serialization_GH_IBinarySupport.htm).)  
![Public method](../icons/pubmethod.gif)|
[Read(XmlNode)](M_GH_IO_Serialization_GH_IXmlSupport_Read.htm)|  Called when
an object is required to deserialize itself.  (Inherited from
[GH_IXmlSupport](T_GH_IO_Serialization_GH_IXmlSupport.htm).)  
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

