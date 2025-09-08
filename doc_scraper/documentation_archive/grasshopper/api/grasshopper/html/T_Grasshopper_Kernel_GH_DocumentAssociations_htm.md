---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_DocumentAssociations.htm
scraped_at: 2025-09-08T16:16:25.335891
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_DocumentAssociations
Class](../html/T_Grasshopper_Kernel_GH_DocumentAssociations.htm
"GH_DocumentAssociations Class")

[GH_DocumentAssociations Constructor
](../html/M_Grasshopper_Kernel_GH_DocumentAssociations__ctor.htm
"GH_DocumentAssociations Constructor ")

[GH_DocumentAssociations
Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentAssociations.htm
"GH_DocumentAssociations Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_DocumentAssociations Class  
  
---  
  
![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_DocumentAssociations  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_DocumentAssociations
    
    
    Public Class GH_DocumentAssociations

The GH_DocumentAssociations type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_DocumentAssociations](M_Grasshopper_Kernel_GH_DocumentAssociations__ctor.htm)|
Initializes a new instance of the GH_DocumentAssociations class  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Associate](M_Grasshopper_Kernel_GH_DocumentAssociations_Associate.htm)|  Add
an association between a Rhino and a Grasshopper file. If a similar
association already exists, it will be overwritten. This function reads and
writes to the disk, it is SLOW. Only call it when you KNOW something changed.  
![Public method](../icons/pubmethod.gif)|
[GetGrasshopperAssociations](M_Grasshopper_Kernel_GH_DocumentAssociations_GetGrasshopperAssociations.htm)|
Find all the Grasshopper ghx files that have been associated with a given
Rhino file.  
![Public method](../icons/pubmethod.gif)|
[GetRhinoAssociations](M_Grasshopper_Kernel_GH_DocumentAssociations_GetRhinoAssociations.htm)|
Find all the Rhino 3dm files that have been associated with a given
Grasshopper file.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

