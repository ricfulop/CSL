---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_IGH_InstanceGuidDependent.htm
scraped_at: 2025-09-08T16:18:34.829713
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH_InstanceGuidDependent
Interface](../html/T_Grasshopper_Kernel_IGH_InstanceGuidDependent.htm
"IGH_InstanceGuidDependent Interface")

[IGH_InstanceGuidDependent
Methods](../html/Methods_T_Grasshopper_Kernel_IGH_InstanceGuidDependent.htm
"IGH_InstanceGuidDependent Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_InstanceGuidDependent Interface  
  
---  
  
Implement this interface in your IGH_DocumentObject class if you want to be
informed when the InstanceGuids of objects in the document are mutated.

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_InstanceGuidDependent
    
    
    Public Interface IGH_InstanceGuidDependent

The IGH_InstanceGuidDependent type exposes the following members.

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[InstanceGuidsChanged](M_Grasshopper_Kernel_IGH_InstanceGuidDependent_InstanceGuidsChanged.htm)|
This method will be called by the GH_Document that owns this object after it
mutates some or all of it's object InstanceIds.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

