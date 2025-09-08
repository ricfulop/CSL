---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_ConnectivityDisparity.htm
scraped_at: 2025-09-08T16:15:54.154761
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_ConnectivityDisparity
Class](../html/T_Grasshopper_Kernel_GH_ConnectivityDisparity.htm
"GH_ConnectivityDisparity Class")

[GH_ConnectivityDisparity Constructor
](../html/M_Grasshopper_Kernel_GH_ConnectivityDisparity__ctor.htm
"GH_ConnectivityDisparity Constructor ")

[GH_ConnectivityDisparity
Properties](../html/Properties_T_Grasshopper_Kernel_GH_ConnectivityDisparity.htm
"GH_ConnectivityDisparity Properties")

[GH_ConnectivityDisparity
Methods](../html/Methods_T_Grasshopper_Kernel_GH_ConnectivityDisparity.htm
"GH_ConnectivityDisparity Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_ConnectivityDisparity Class  
  
---  
  
Maintains two connectivity diagrams, one of which is a subset of the other.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_ConnectivityDisparity  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_ConnectivityDisparity
    
    
    Public Class GH_ConnectivityDisparity

The GH_ConnectivityDisparity type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_ConnectivityDisparity](M_Grasshopper_Kernel_GH_ConnectivityDisparity__ctor.htm)|
Create a new instance of the Connectivity Disparity utility class.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[SubNodes](P_Grasshopper_Kernel_GH_ConnectivityDisparity_SubNodes.htm)|  Gets
a proxy for all the Nodes in the Subset diagram.  
![Public property](../icons/pubproperty.gif)|
[SubSet](P_Grasshopper_Kernel_GH_ConnectivityDisparity_SubSet.htm)|  Gets a
pointer to the subset diagram stored in this disparity class.  
![Public property](../icons/pubproperty.gif)|
[TopNodes](P_Grasshopper_Kernel_GH_ConnectivityDisparity_TopNodes.htm)|  Gets
a proxy for all the Nodes in the Top Level diagram.  
![Public property](../icons/pubproperty.gif)|
[TopSet](P_Grasshopper_Kernel_GH_ConnectivityDisparity_TopSet.htm)|  Gets a
pointer to the complete diagram stored in this disparity class.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ExternalInputs](M_Grasshopper_Kernel_GH_ConnectivityDisparity_ExternalInputs.htm)|
Find all external sources for a given id in the subset.  
![Public method](../icons/pubmethod.gif)|
[ExternalOutputs](M_Grasshopper_Kernel_GH_ConnectivityDisparity_ExternalOutputs.htm)|
Find all external recipients for a given id in the subset.  
![Public method](../icons/pubmethod.gif)|
[InternalInputs](M_Grasshopper_Kernel_GH_ConnectivityDisparity_InternalInputs.htm)|
Find all internal sources for a given id in the subset.  
![Public method](../icons/pubmethod.gif)|
[InternalOutputs](M_Grasshopper_Kernel_GH_ConnectivityDisparity_InternalOutputs.htm)|
Find all external recipients for a given id in the subset.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

