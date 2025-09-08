---
url: https://developer.rhino3d.com/api/grasshopper/html/T_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection.htm
scraped_at: 2025-09-08T16:10:39.813115
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[GH_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH_Chunk.ChunkKeyedCollection
Class](../html/T_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection.htm
"GH_Chunk.ChunkKeyedCollection Class")

[GH_Chunk.ChunkKeyedCollection Constructor
](../html/M_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection__ctor.htm
"GH_Chunk.ChunkKeyedCollection Constructor ")

[ChunkKeyedCollection
Properties](../html/Properties_T_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection.htm
"ChunkKeyedCollection Properties")

[ChunkKeyedCollection
Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection.htm
"ChunkKeyedCollection Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_ChunkChunkKeyedCollection Class  
  
---  
  
Represents a collection of chunks with associated IDs

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
GH_IO.SerializationGH_ChunkChunkKeyedCollection  

**Namespace:** [GH_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:** GH_IO (in GH_IO.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class ChunkKeyedCollection : IEnumerable<GH_Chunk>, 
    	IEnumerable
    
    
    Public Class ChunkKeyedCollection
    	Implements IEnumerable(Of GH_Chunk), IEnumerable

The GH_ChunkChunkKeyedCollection type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_ChunkChunkKeyedCollection](M_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection__ctor.htm)|
Create a new collection.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Count](P_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection_Count.htm)|
Returns the amount in the collection.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Add](M_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection_Add.htm)|  Adds a
new chunk.  
![Public method](../icons/pubmethod.gif)|
[Clear](M_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection_Clear.htm)|
Removes all chunks from the collection.  
![Public method](../icons/pubmethod.gif)|
[GetEnumerator](M_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection_GetEnumerator.htm)|
Gets an enumerator that iterates over all chunks in the collection.  
![Public method](../icons/pubmethod.gif)|
[Remove(GH_Chunk)](M_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection_Remove.htm)|
Removes a chunk.  
![Public method](../icons/pubmethod.gif)|
[Remove(ID)](M_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection_Remove_1.htm)|
Removes an ID.  
![Public method](../icons/pubmethod.gif)|
[TryGetValue](M_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection_TryGetValue.htm)|
Try and find the chunk that belongs to a given ID.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

