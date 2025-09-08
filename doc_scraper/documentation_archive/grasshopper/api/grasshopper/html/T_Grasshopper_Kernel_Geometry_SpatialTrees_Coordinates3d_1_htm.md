---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Geometry_SpatialTrees_Coordinates3d_1.htm
scraped_at: 2025-09-08T16:19:52.208106
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Geometry.SpatialTrees](../html/N_Grasshopper_Kernel_Geometry_SpatialTrees.htm
"Grasshopper.Kernel.Geometry.SpatialTrees")

[Coordinates3d(T)
Delegate](../html/T_Grasshopper_Kernel_Geometry_SpatialTrees_Coordinates3d_1.htm
"Coordinates3d\(T\) Delegate")

[Index3d(T)
Class](../html/T_Grasshopper_Kernel_Geometry_SpatialTrees_Index3d_1.htm
"Index3d\(T\) Class")

[Node3d(T)
Class](../html/T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm
"Node3d\(T\) Class")

[TreeDelegates
Class](../html/T_Grasshopper_Kernel_Geometry_SpatialTrees_TreeDelegates.htm
"TreeDelegates Class")

[Validation3d(T)
Delegate](../html/T_Grasshopper_Kernel_Geometry_SpatialTrees_Validation3d_1.htm
"Validation3d\(T\) Delegate")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# Coordinates3dT Delegate  
  
---  
  
Delegate for coordinate retrieval.

**Namespace:**
[Grasshopper.Kernel.Geometry.SpatialTrees](N_Grasshopper_Kernel_Geometry_SpatialTrees.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public delegate void Coordinates3d<T>(
    	T element,
    	out double x,
    	out double y,
    	out double z
    )
    
    
    
    Public Delegate Sub Coordinates3d(Of T) ( 
    	element As T,
    	<OutAttribute> ByRef x As Double,
    	<OutAttribute> ByRef y As Double,
    	<OutAttribute> ByRef z As Double
    )

#### Parameters

element

    Type: T  
Element to retrieve coordinates from.

x

    Type: [SystemDouble](https://docs.microsoft.com/dotnet/api/system.double)  
X coordinate of element.

y

    Type: [SystemDouble](https://docs.microsoft.com/dotnet/api/system.double)  
Y coordinate of element.

z

    Type: [SystemDouble](https://docs.microsoft.com/dotnet/api/system.double)  
Z coordinate of element.

#### Type Parameters

T

    Element type.

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Geometry.SpatialTrees
Namespace](N_Grasshopper_Kernel_Geometry_SpatialTrees.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

