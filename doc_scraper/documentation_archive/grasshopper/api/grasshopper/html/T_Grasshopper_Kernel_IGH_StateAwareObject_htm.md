---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_IGH_StateAwareObject.htm
scraped_at: 2025-09-08T16:18:42.881326
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH_StateAwareObject
Interface](../html/T_Grasshopper_Kernel_IGH_StateAwareObject.htm
"IGH_StateAwareObject Interface")

[IGH_StateAwareObject
Methods](../html/Methods_T_Grasshopper_Kernel_IGH_StateAwareObject.htm
"IGH_StateAwareObject Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_StateAwareObject Interface  
  
---  
  
Implement this interface if you want to be included in state saving/loading.

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_StateAwareObject
    
    
    Public Interface IGH_StateAwareObject

The IGH_StateAwareObject type exposes the following members.

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[LoadState](M_Grasshopper_Kernel_IGH_StateAwareObject_LoadState.htm)|
Override this function to load your state data. DO NOT START A NEW SOLUTION.
This will be handled by the state manager.  
![Public method](../icons/pubmethod.gif)|
[SaveState](M_Grasshopper_Kernel_IGH_StateAwareObject_SaveState.htm)|
Override this function to store your state data. You have to return a
deserializable string.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

