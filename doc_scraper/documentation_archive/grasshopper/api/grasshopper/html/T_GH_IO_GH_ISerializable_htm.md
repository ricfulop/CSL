---
url: https://developer.rhino3d.com/api/grasshopper/html/T_GH_IO_GH_ISerializable.htm
scraped_at: 2025-09-08T16:10:33.786086
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[GH_IO](../html/N_GH_IO.htm "GH_IO")

[GH_ISerializable Interface](../html/T_GH_IO_GH_ISerializable.htm
"GH_ISerializable Interface")

[GH_ISerializable Methods](../html/Methods_T_GH_IO_GH_ISerializable.htm
"GH_ISerializable Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_ISerializable Interface  
  
---  
  
Every object which needs to (de)serialize itself using GH_IO methodology must
implement this interface.

**Namespace:** [GH_IO](N_GH_IO.htm)  
**Assembly:** GH_IO (in GH_IO.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface GH_ISerializable
    
    
    Public Interface GH_ISerializable

The GH_ISerializable type exposes the following members.

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Read](M_GH_IO_GH_ISerializable_Read.htm)|  This method is called whenever the
instance is required to deserialize itself.  
![Public method](../icons/pubmethod.gif)|
[Write](M_GH_IO_GH_ISerializable_Write.htm)|  This method is called whenever
the instance is required to serialize itself.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH_IO Namespace](N_GH_IO.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

