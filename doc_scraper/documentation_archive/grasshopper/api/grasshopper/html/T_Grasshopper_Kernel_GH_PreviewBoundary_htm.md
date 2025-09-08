---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_PreviewBoundary.htm
scraped_at: 2025-09-08T16:17:33.582012
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_PreviewBoundary Class](../html/T_Grasshopper_Kernel_GH_PreviewBoundary.htm
"GH_PreviewBoundary Class")

[GH_PreviewBoundary Constructor
](../html/M_Grasshopper_Kernel_GH_PreviewBoundary__ctor.htm
"GH_PreviewBoundary Constructor ")

[GH_PreviewBoundary
Properties](../html/Properties_T_Grasshopper_Kernel_GH_PreviewBoundary.htm
"GH_PreviewBoundary Properties")

[GH_PreviewBoundary
Methods](../html/Methods_T_Grasshopper_Kernel_GH_PreviewBoundary.htm
"GH_PreviewBoundary Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_PreviewBoundary Class  
  
---  
  
A closed boundary for filtering previewed objects.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_PreviewBoundary  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_PreviewBoundary : GH_ISerializable
    
    
    Public Class GH_PreviewBoundary
    	Implements GH_ISerializable

The GH_PreviewBoundary type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_PreviewBoundary](M_Grasshopper_Kernel_GH_PreviewBoundary__ctor.htm)|
Create a new preview boundary.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Boundary](P_Grasshopper_Kernel_GH_PreviewBoundary_Boundary.htm)|  Gets the
boundary region.  
![Public property](../icons/pubproperty.gif)|
[Limits](P_Grasshopper_Kernel_GH_PreviewBoundary_Limits.htm)|  Gets the limits
of the boundary.  
![Public property](../icons/pubproperty.gif)|
[Points](P_Grasshopper_Kernel_GH_PreviewBoundary_Points.htm)|  Gets the array
of points this boundary was made from.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[IsVisible](M_Grasshopper_Kernel_GH_PreviewBoundary_IsVisible.htm)|  Gets
whether a specific object is visible within this boundary.  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_GH_PreviewBoundary_Read.htm)|  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_GH_PreviewBoundary_Write.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

