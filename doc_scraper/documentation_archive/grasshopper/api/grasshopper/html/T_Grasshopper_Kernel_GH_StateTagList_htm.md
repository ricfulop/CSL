---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_StateTagList.htm
scraped_at: 2025-09-08T16:18:03.707195
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_StateTagList Class](../html/T_Grasshopper_Kernel_GH_StateTagList.htm
"GH_StateTagList Class")

[GH_StateTagList Constructor
](../html/M_Grasshopper_Kernel_GH_StateTagList__ctor.htm "GH_StateTagList
Constructor ")

[GH_StateTagList
Properties](../html/Properties_T_Grasshopper_Kernel_GH_StateTagList.htm
"GH_StateTagList Properties")

[GH_StateTagList
Methods](../html/Methods_T_Grasshopper_Kernel_GH_StateTagList.htm
"GH_StateTagList Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_StateTagList Class  
  
---  
  
Maintains a collection of IGH_StateTag objects.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[System.Collections.GenericList](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)[IGH_StateTag](T_Grasshopper_Kernel_IGH_StateTag.htm)  
Grasshopper.KernelGH_StateTagList  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_StateTagList : List<IGH_StateTag>, 
    	IGH_TooltipAwareObject
    
    
    Public Class GH_StateTagList
    	Inherits List(Of IGH_StateTag)
    	Implements IGH_TooltipAwareObject

The GH_StateTagList type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_StateTagList](M_Grasshopper_Kernel_GH_StateTagList__ctor.htm)| Initializes
a new instance of the GH_StateTagList class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[BoundingBox](P_Grasshopper_Kernel_GH_StateTagList_BoundingBox.htm)|  Gets the
boundingbox of all StateTags.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Layout](M_Grasshopper_Kernel_GH_StateTagList_Layout.htm)|  Layout the
StateTags.  
![Public method](../icons/pubmethod.gif)|
[RenderStateTags](M_Grasshopper_Kernel_GH_StateTagList_RenderStateTags.htm)|
Render all StateTags in this list to the designated Graphics surface.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

