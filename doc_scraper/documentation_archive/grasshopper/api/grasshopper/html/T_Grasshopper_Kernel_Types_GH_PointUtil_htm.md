---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_GH_PointUtil.htm
scraped_at: 2025-09-08T16:21:23.577885
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[GH_PointUtil Class](../html/T_Grasshopper_Kernel_Types_GH_PointUtil.htm
"GH_PointUtil Class")

[GH_PointUtil
Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_PointUtil.htm
"GH_PointUtil Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_PointUtil Class  
  
---  
  
![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Kernel.TypesGH_PointUtil  

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class GH_PointUtil
    
    
    Public NotInheritable Class GH_PointUtil

The GH_PointUtil type exposes the following members.

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FitPlaneThroughPoints](M_Grasshopper_Kernel_Types_GH_PointUtil_FitPlaneThroughPoints.htm)|
Fit a least-squares plane through a collection of points.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ProjectPointsToPlane](M_Grasshopper_Kernel_Types_GH_PointUtil_ProjectPointsToPlane.htm)|
Project a list of points onto the plane. The result will be points in plane-uv
coordinates.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[PullPointsToPlane](M_Grasshopper_Kernel_Types_GH_PointUtil_PullPointsToPlane.htm)|
Pull a list of points onto the plane. The result will be points in 3D world
coordinates which are coincident with the given plane.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RemapPointsToPlane](M_Grasshopper_Kernel_Types_GH_PointUtil_RemapPointsToPlane.htm)|
Remap a list of points onto the plane. This operation equals a
ChangeBasisXForm for each point.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

