---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Geometry_SpatialTrees_Index3d_1.htm
scraped_at: 2025-09-08T16:19:53.206143
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Geometry.SpatialTrees](../html/N_Grasshopper_Kernel_Geometry_SpatialTrees.htm
"Grasshopper.Kernel.Geometry.SpatialTrees")

[Index3d(T)
Class](../html/T_Grasshopper_Kernel_Geometry_SpatialTrees_Index3d_1.htm
"Index3d\(T\) Class")

[Index3d(T) Constructor
](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Index3d_1__ctor.htm
"Index3d\(T\) Constructor ")

[Index3d(T)
Properties](../html/Properties_T_Grasshopper_Kernel_Geometry_SpatialTrees_Index3d_1.htm
"Index3d\(T\) Properties")

[Index3d(T)
Methods](../html/Methods_T_Grasshopper_Kernel_Geometry_SpatialTrees_Index3d_1.htm
"Index3d\(T\) Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# Index3dT Class  
  
---  
  
Represents an element index within a Tree3d instance.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Kernel.Geometry.SpatialTreesIndex3dT  

**Namespace:**
[Grasshopper.Kernel.Geometry.SpatialTrees](N_Grasshopper_Kernel_Geometry_SpatialTrees.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class Index3d<T> : IComparable<Index3d<T>>
    
    
    
    Public Class Index3d(Of T)
    	Implements IComparable(Of Index3d(Of T))

#### Type Parameters

T

    

The Index3dT type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Index3dT](M_Grasshopper_Kernel_Geometry_SpatialTrees_Index3d_1__ctor.htm)|
Initializes a new instance of the Index3dT class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[GlobalIndex](P_Grasshopper_Kernel_Geometry_SpatialTrees_Index3d_1_GlobalIndex.htm)|
Gets the item index within the tree global list.  
![Public property](../icons/pubproperty.gif)|
[Item](P_Grasshopper_Kernel_Geometry_SpatialTrees_Index3d_1_Item.htm)|  Gets
the actual item.  
![Public property](../icons/pubproperty.gif)|
[LocalIndex](P_Grasshopper_Kernel_Geometry_SpatialTrees_Index3d_1_LocalIndex.htm)|
Gets the index within the node index list.  
![Public property](../icons/pubproperty.gif)|
[Node](P_Grasshopper_Kernel_Geometry_SpatialTrees_Index3d_1_Node.htm)|  Gets
the node of the tree in which this element is stored.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CompareTo](M_Grasshopper_Kernel_Geometry_SpatialTrees_Index3d_1_CompareTo.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Geometry.SpatialTrees
Namespace](N_Grasshopper_Kernel_Geometry_SpatialTrees.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

