---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_GH_SamplingSphere.htm
scraped_at: 2025-09-08T16:13:02.399592
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH_SamplingSphere Class](../html/T_Grasshopper_GUI_GH_SamplingSphere.htm
"GH_SamplingSphere Class")

[GH_SamplingSphere Constructor
](../html/M_Grasshopper_GUI_GH_SamplingSphere__ctor.htm "GH_SamplingSphere
Constructor ")

[GH_SamplingSphere
Properties](../html/Properties_T_Grasshopper_GUI_GH_SamplingSphere.htm
"GH_SamplingSphere Properties")

[GH_SamplingSphere
Methods](../html/Methods_T_Grasshopper_GUI_GH_SamplingSphere.htm
"GH_SamplingSphere Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_SamplingSphere Class  
  
---  
  
Represents a coloured sphere that can be sampled at various rotations.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.GUIGH_SamplingSphere  

**Namespace:** [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_SamplingSphere
    
    
    Public Class GH_SamplingSphere

The GH_SamplingSphere type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_SamplingSphere](M_Grasshopper_GUI_GH_SamplingSphere__ctor.htm)|
Initializes a new instance of the GH_SamplingSphere class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[SampleCount](P_Grasshopper_GUI_GH_SamplingSphere_SampleCount.htm)|  Gets the
total number of samples contained in this sampling grid.  
![Public property](../icons/pubproperty.gif)|
[Size](P_Grasshopper_GUI_GH_SamplingSphere_Size.htm)|  Gets the size of this
sample grid.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[SampleSphere(Sphere)](M_Grasshopper_GUI_GH_SamplingSphere_SampleSphere.htm)|
Sample the UV locations of a sphere. The sphere should be centered on the
world origin.  
![Public method](../icons/pubmethod.gif)| [SampleSphere(Sphere,
GH_MemoryBitmap)](M_Grasshopper_GUI_GH_SamplingSphere_SampleSphere_1.htm)|
Sample a sphere with a UV texture and return a bitmap of sampled values.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

