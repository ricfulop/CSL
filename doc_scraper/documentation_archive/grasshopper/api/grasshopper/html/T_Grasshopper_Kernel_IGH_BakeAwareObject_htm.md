---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_IGH_BakeAwareObject.htm
scraped_at: 2025-09-08T16:18:16.752740
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH_BakeAwareObject
Interface](../html/T_Grasshopper_Kernel_IGH_BakeAwareObject.htm
"IGH_BakeAwareObject Interface")

[IGH_BakeAwareObject
Properties](../html/Properties_T_Grasshopper_Kernel_IGH_BakeAwareObject.htm
"IGH_BakeAwareObject Properties")

[IGH_BakeAwareObject
Methods](../html/Methods_T_Grasshopper_Kernel_IGH_BakeAwareObject.htm
"IGH_BakeAwareObject Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_BakeAwareObject Interface  
  
---  
  
Implement this interface on your IGH_ActiveObject if you want to participate
in the Bake GUI.

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_BakeAwareObject
    
    
    Public Interface IGH_BakeAwareObject

The IGH_BakeAwareObject type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[IsBakeCapable](P_Grasshopper_Kernel_IGH_BakeAwareObject_IsBakeCapable.htm)|
Gets a value indicating whether or not the object can potentially Bake data in
its current state.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)| [BakeGeometry(RhinoDoc,
ListGuid)](M_Grasshopper_Kernel_IGH_BakeAwareObject_BakeGeometry_1.htm)|  Bake
all the goemetry in this object in the given Rhino document.  
![Public method](../icons/pubmethod.gif)| [BakeGeometry(RhinoDoc,
ObjectAttributes,
ListGuid)](M_Grasshopper_Kernel_IGH_BakeAwareObject_BakeGeometry.htm)|  Bake
all the goemetry in this object in the given Rhino document.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

