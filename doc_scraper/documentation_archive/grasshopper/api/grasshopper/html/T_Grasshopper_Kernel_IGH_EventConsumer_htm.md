---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_IGH_EventConsumer.htm
scraped_at: 2025-09-08T16:18:31.856056
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH_EventConsumer
Interface](../html/T_Grasshopper_Kernel_IGH_EventConsumer.htm
"IGH_EventConsumer Interface")

[IGH_EventConsumer
Methods](../html/Methods_T_Grasshopper_Kernel_IGH_EventConsumer.htm
"IGH_EventConsumer Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_EventConsumer Interface  
  
---  
  
Implement this interface if you want to inter-operate with a GH_EventServer.

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_EventConsumer
    
    
    Public Interface IGH_EventConsumer

The IGH_EventConsumer type exposes the following members.

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[IsRelevantEvent](M_Grasshopper_Kernel_IGH_EventConsumer_IsRelevantEvent.htm)|
Whenever a new object event is handled, this function will be called to
determine whether it will cause an update.  
![Public method](../icons/pubmethod.gif)|
[PartialExpiration](M_Grasshopper_Kernel_IGH_EventConsumer_PartialExpiration.htm)|
This method will be called by the GH_CustomEventServer to indicate one or more
interesting object events can now be processed.  
![Public method](../icons/pubmethod.gif)|
[TotalExpiration](M_Grasshopper_Kernel_IGH_EventConsumer_TotalExpiration.htm)|
This method will be called by the GH_CustomEventServer to indicate all
interesting object events can now be processed.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

