---
url: https://developer.rhino3d.com/api/grasshopper/html/T_GH_IO_Serialization_ID.htm
scraped_at: 2025-09-08T16:10:49.861867
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[GH_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[ID Structure](../html/T_GH_IO_Serialization_ID.htm "ID Structure")

[ID Constructor ](../html/Overload_GH_IO_Serialization_ID__ctor.htm "ID
Constructor ")

[ID Properties](../html/Properties_T_GH_IO_Serialization_ID.htm "ID
Properties")

[ID Methods](../html/Methods_T_GH_IO_Serialization_ID.htm "ID Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ID Structure  
  
---  
  
An ID is used to uniquely identify a specific item.

**Namespace:** [GH_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:** GH_IO (in GH_IO.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public struct ID : IComparable<ID>, IEquatable<ID>
    
    
    Public Structure ID
    	Implements IComparable(Of ID), IEquatable(Of ID)

The ID type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ID(String)](M_GH_IO_Serialization_ID__ctor.htm)|  Constuctor for IDs.  
![Public method](../icons/pubmethod.gif)| [ID(String,
Int32)](M_GH_IO_Serialization_ID__ctor_1.htm)|  Constructor for IDs.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Hash](P_GH_IO_Serialization_ID_Hash.htm)|  Gets the hash code.  
![Public property](../icons/pubproperty.gif)|
[HasIndex](P_GH_IO_Serialization_ID_HasIndex.htm)|  Gets whether the index has
been set.  
![Public property](../icons/pubproperty.gif)|
[HasName](P_GH_IO_Serialization_ID_HasName.htm)|  Gets whether the name has
been set. Every valid ID must have a name.  
![Public property](../icons/pubproperty.gif)|
[Index](P_GH_IO_Serialization_ID_Index.htm)|  Gets the index of this ID, if
there is no valid index then -1 is returned.  
![Public property](../icons/pubproperty.gif)|
[Name](P_GH_IO_Serialization_ID_Name.htm)|  Gets the name of this ID.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CompareTo](M_GH_IO_Serialization_ID_CompareTo.htm)|  Compares this ID to
another ID.  
![Public method](../icons/pubmethod.gif)|
[Equals](M_GH_IO_Serialization_ID_Equals.htm)|  Determines if two IDs are
equal.  
![Public method](../icons/pubmethod.gif)|
[GetHashCode](M_GH_IO_Serialization_ID_GetHashCode.htm)|  Gets the hash code.
(Overrides
[ValueTypeGetHashCode](https://docs.microsoft.com/dotnet/api/system.valuetype.gethashcode#system-
valuetype-gethashcode).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_GH_IO_Serialization_ID_ToString.htm)|  Gets a string
representation for this ID.  (Overrides
[ValueTypeToString](https://docs.microsoft.com/dotnet/api/system.valuetype.tostring#system-
valuetype-tostring).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

