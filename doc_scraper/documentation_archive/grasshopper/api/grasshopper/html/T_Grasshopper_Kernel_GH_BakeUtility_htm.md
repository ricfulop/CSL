---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_BakeUtility.htm
scraped_at: 2025-09-08T16:15:37.091271
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_BakeUtility Class](../html/T_Grasshopper_Kernel_GH_BakeUtility.htm
"GH_BakeUtility Class")

[GH_BakeUtility Constructor
](../html/M_Grasshopper_Kernel_GH_BakeUtility__ctor.htm "GH_BakeUtility
Constructor ")

[GH_BakeUtility
Properties](../html/Properties_T_Grasshopper_Kernel_GH_BakeUtility.htm
"GH_BakeUtility Properties")

[GH_BakeUtility
Methods](../html/Methods_T_Grasshopper_Kernel_GH_BakeUtility.htm
"GH_BakeUtility Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_BakeUtility Class  
  
---  
  
A utility class for baking. We heavily recommend you use this for any baking,
as it handles invalid objects correctly.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_BakeUtility  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_BakeUtility
    
    
    Public Class GH_BakeUtility

The GH_BakeUtility type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_BakeUtility](M_Grasshopper_Kernel_GH_BakeUtility__ctor.htm)|  Create a new
baker.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[BakedCount](P_Grasshopper_Kernel_GH_BakeUtility_BakedCount.htm)|  Gets the
number of successful baking operations.  
![Public property](../icons/pubproperty.gif)|
[BakedIds](P_Grasshopper_Kernel_GH_BakeUtility_BakedIds.htm)|  Gets all
collected object ids.  
![Public property](../icons/pubproperty.gif)|
[InvalidCount](P_Grasshopper_Kernel_GH_BakeUtility_InvalidCount.htm)|  Gets
the number of invalid objects encountered.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[BakeObject](M_Grasshopper_Kernel_GH_BakeUtility_BakeObject.htm)|  Try and
bake a single object.  
![Public method](../icons/pubmethod.gif)|
[BakeObjects](M_Grasshopper_Kernel_GH_BakeUtility_BakeObjects.htm)|  Bake a
bunch of objects.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

