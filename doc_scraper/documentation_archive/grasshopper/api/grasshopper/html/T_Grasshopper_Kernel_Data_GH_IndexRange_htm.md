---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Data_GH_IndexRange.htm
scraped_at: 2025-09-08T16:19:00.970198
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm
"Grasshopper.Kernel.Data")

[GH_IndexRange Structure](../html/T_Grasshopper_Kernel_Data_GH_IndexRange.htm
"GH_IndexRange Structure")

[GH_IndexRange Constructor
](../html/Overload_Grasshopper_Kernel_Data_GH_IndexRange__ctor.htm
"GH_IndexRange Constructor ")

[GH_IndexRange
Properties](../html/Properties_T_Grasshopper_Kernel_Data_GH_IndexRange.htm
"GH_IndexRange Properties")

[GH_IndexRange
Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_IndexRange.htm
"GH_IndexRange Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_IndexRange Structure  
  
---  
  
Represents a range of indices.

**Namespace:** [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public struct GH_IndexRange : GH_ISerializable
    
    
    Public Structure GH_IndexRange
    	Implements GH_ISerializable

The GH_IndexRange type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_IndexRange(Int32)](M_Grasshopper_Kernel_Data_GH_IndexRange__ctor.htm)|
Create a new singular range.  
![Public method](../icons/pubmethod.gif)| [GH_IndexRange(Int32,
Int32)](M_Grasshopper_Kernel_Data_GH_IndexRange__ctor_1.htm)|  Create a new
range.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Index0](P_Grasshopper_Kernel_Data_GH_IndexRange_Index0.htm)|  Gets the first
index in the range.  
![Public property](../icons/pubproperty.gif)|
[Index1](P_Grasshopper_Kernel_Data_GH_IndexRange_Index1.htm)|  Gets the last
index in the range.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[InvalidRange](P_Grasshopper_Kernel_Data_GH_IndexRange_InvalidRange.htm)|
Gets the predefined invalid range.  
![Public property](../icons/pubproperty.gif)|
[IsSingular](P_Grasshopper_Kernel_Data_GH_IndexRange_IsSingular.htm)|  Gets
whether the range has zero length.  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Kernel_Data_GH_IndexRange_IsValid.htm)|  Gets whether
this range is valid.  
![Public property](../icons/pubproperty.gif)|
[Length](P_Grasshopper_Kernel_Data_GH_IndexRange_Length.htm)|  Gets the length
of the range.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[MaxValue](P_Grasshopper_Kernel_Data_GH_IndexRange_MaxValue.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AdjacentTo](M_Grasshopper_Kernel_Data_GH_IndexRange_AdjacentTo.htm)|  Tests
whether this range is adjacent to another.  
![Public method](../icons/pubmethod.gif)|
[Contains(GH_IndexRange)](M_Grasshopper_Kernel_Data_GH_IndexRange_Contains.htm)|
Tests whether a specified range is entirely contained within this range.  
![Public method](../icons/pubmethod.gif)|
[Contains(Int32)](M_Grasshopper_Kernel_Data_GH_IndexRange_Contains_1.htm)|
Tests whether a specified index is defined by this range.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Intersection](M_Grasshopper_Kernel_Data_GH_IndexRange_Intersection.htm)|
Create the intersection between two ranges.  
![Public method](../icons/pubmethod.gif)|
[IntersectsWith](M_Grasshopper_Kernel_Data_GH_IndexRange_IntersectsWith.htm)|
Tests whether certain indices are described by both this and another range.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Split](M_Grasshopper_Kernel_Data_GH_IndexRange_Split.htm)|  Split a range
into two using an integer index.  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Data_GH_IndexRange_ToString.htm)|  (Overrides
[ValueTypeToString](https://docs.microsoft.com/dotnet/api/system.valuetype.tostring#system-
valuetype-tostring).)  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Union](M_Grasshopper_Kernel_Data_GH_IndexRange_Union.htm)|  Create a range
which contains both input ranges.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

