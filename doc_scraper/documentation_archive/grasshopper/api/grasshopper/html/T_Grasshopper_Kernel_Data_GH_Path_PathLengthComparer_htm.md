---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Data_GH_Path_PathLengthComparer.htm
scraped_at: 2025-09-08T16:19:06.991577
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm
"Grasshopper.Kernel.Data")

[GH_Path.PathLengthComparer
Class](../html/T_Grasshopper_Kernel_Data_GH_Path_PathLengthComparer.htm
"GH_Path.PathLengthComparer Class")

[GH_Path.PathLengthComparer Constructor
](../html/M_Grasshopper_Kernel_Data_GH_Path_PathLengthComparer__ctor.htm
"GH_Path.PathLengthComparer Constructor ")

[PathLengthComparer
Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_Path_PathLengthComparer.htm
"PathLengthComparer Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_PathPathLengthComparer Class  
  
---  
  
Use this comparer to sort lists of paths using a topological approach. Shorter
paths are favoured over longer paths. Equal length paths use the default
comparer.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Kernel.DataGH_PathPathLengthComparer  

**Namespace:** [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class PathLengthComparer : IComparer<GH_Path>
    
    
    Public Class PathLengthComparer
    	Implements IComparer(Of GH_Path)

The GH_PathPathLengthComparer type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_PathPathLengthComparer](M_Grasshopper_Kernel_Data_GH_Path_PathLengthComparer__ctor.htm)|
Initializes a new instance of the GH_PathPathLengthComparer class  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Compare](M_Grasshopper_Kernel_Data_GH_Path_PathLengthComparer_Compare.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

