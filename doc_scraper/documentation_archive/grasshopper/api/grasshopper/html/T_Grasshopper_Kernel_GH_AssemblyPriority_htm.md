---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_AssemblyPriority.htm
scraped_at: 2025-09-08T16:15:23.022598
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_AssemblyPriority
Class](../html/T_Grasshopper_Kernel_GH_AssemblyPriority.htm
"GH_AssemblyPriority Class")

[GH_AssemblyPriority Constructor
](../html/M_Grasshopper_Kernel_GH_AssemblyPriority__ctor.htm
"GH_AssemblyPriority Constructor ")

[GH_AssemblyPriority
Methods](../html/Methods_T_Grasshopper_Kernel_GH_AssemblyPriority.htm
"GH_AssemblyPriority Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_AssemblyPriority Class  
  
---  
  
Derive from this class if you wish to perform additional steps before any of
your components are loaded. Any class in your project which inherits from
GH_AssemblyPriority and which has an empty constructor will be instantiated
prior to any GH_Component or IGH_DocumentObject classes.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_AssemblyPriority  
[Grasshopper.RhinocerosModelContentEnablerLoader](T_Grasshopper_Rhinoceros_ModelContentEnablerLoader.htm)  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public abstract class GH_AssemblyPriority
    
    
    Public MustInherit Class GH_AssemblyPriority

The GH_AssemblyPriority type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[GH_AssemblyPriority](M_Grasshopper_Kernel_GH_AssemblyPriority__ctor.htm)|
Initializes a new instance of the GH_AssemblyPriority class  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[PriorityLoad](M_Grasshopper_Kernel_GH_AssemblyPriority_PriorityLoad.htm)|
This method will be called exactly once before any of the Components in your
project are loaded.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

