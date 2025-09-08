---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_StateTag.htm
scraped_at: 2025-09-08T16:18:00.741631
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_StateTag Class](../html/T_Grasshopper_Kernel_GH_StateTag.htm "GH_StateTag
Class")

[GH_StateTag Constructor ](../html/M_Grasshopper_Kernel_GH_StateTag__ctor.htm
"GH_StateTag Constructor ")

[GH_StateTag
Properties](../html/Properties_T_Grasshopper_Kernel_GH_StateTag.htm
"GH_StateTag Properties")

[GH_StateTag Methods](../html/Methods_T_Grasshopper_Kernel_GH_StateTag.htm
"GH_StateTag Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_StateTag Class  
  
---  
  
Abstract implementation of the IGH_StateTag interface. Derive from this class
rather than implementing IGH_StateTag.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_StateTag  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public abstract class GH_StateTag : IGH_StateTag
    
    
    Public MustInherit Class GH_StateTag
    	Implements IGH_StateTag

The GH_StateTag type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[GH_StateTag](M_Grasshopper_Kernel_GH_StateTag__ctor.htm)| Initializes a new
instance of the GH_StateTag class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Description](P_Grasshopper_Kernel_GH_StateTag_Description.htm)|  
![Public property](../icons/pubproperty.gif)|
[Icon](P_Grasshopper_Kernel_GH_StateTag_Icon.htm)|  
![Public property](../icons/pubproperty.gif)|
[Name](P_Grasshopper_Kernel_GH_StateTag_Name.htm)|  
![Public property](../icons/pubproperty.gif)|
[Stage](P_Grasshopper_Kernel_GH_StateTag_Stage.htm)|  Gets or sets the stage
rectangle for this tag.  
![Public property](../icons/pubproperty.gif)|
[StateDescription](P_Grasshopper_Kernel_GH_StateTag_StateDescription.htm)|
Gets or sets the state description for this tag.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Render](M_Grasshopper_Kernel_GH_StateTag_Render.htm)|  
![Protected method](../icons/protmethod.gif)|
[RenderFreeformIcon](M_Grasshopper_Kernel_GH_StateTag_RenderFreeformIcon.htm)|
Render a filled path with default shading.  
![Protected method](../icons/protmethod.gif)|
[RenderTagBlankIcon(Graphics)](M_Grasshopper_Kernel_GH_StateTag_RenderTagBlankIcon.htm)|
Render a blank rectangle icon.  
![Protected method](../icons/protmethod.gif)| [RenderTagBlankIcon(Graphics,
GH_StateTagDrawCallback)](M_Grasshopper_Kernel_GH_StateTag_RenderTagBlankIcon_1.htm)|
Render a blank rectangle icon.  
![Protected method](../icons/protmethod.gif)|
[RenderTagPolygonIcon](M_Grasshopper_Kernel_GH_StateTag_RenderTagPolygonIcon.htm)|
Render a filled polygon with default shading.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

