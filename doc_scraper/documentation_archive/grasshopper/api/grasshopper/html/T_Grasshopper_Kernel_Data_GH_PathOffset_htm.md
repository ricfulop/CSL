---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Data_GH_PathOffset.htm
scraped_at: 2025-09-08T16:19:08.008128
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm
"Grasshopper.Kernel.Data")

[GH_PathOffset Class](../html/T_Grasshopper_Kernel_Data_GH_PathOffset.htm
"GH_PathOffset Class")

[GH_PathOffset Constructor
](../html/Overload_Grasshopper_Kernel_Data_GH_PathOffset__ctor.htm
"GH_PathOffset Constructor ")

[GH_PathOffset
Properties](../html/Properties_T_Grasshopper_Kernel_Data_GH_PathOffset.htm
"GH_PathOffset Properties")

[GH_PathOffset
Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_PathOffset.htm
"GH_PathOffset Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_PathOffset Class  
  
---  
  
Represents a relative offset within a data structure.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Kernel.DataGH_PathOffset  

**Namespace:** [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_PathOffset
    
    
    Public Class GH_PathOffset

The GH_PathOffset type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_PathOffset](M_Grasshopper_Kernel_Data_GH_PathOffset__ctor.htm)|
Initializes a new instance of the GH_PathOffset class  
![Public method](../icons/pubmethod.gif)|
[GH_PathOffset(IEnumerableInt32)](M_Grasshopper_Kernel_Data_GH_PathOffset__ctor_1.htm)|
Initializes a new instance of the GH_PathOffset class  
![Public method](../icons/pubmethod.gif)| [GH_PathOffset(IEnumerableInt32,
Int32)](M_Grasshopper_Kernel_Data_GH_PathOffset__ctor_2.htm)| Initializes a
new instance of the GH_PathOffset class  
![Public method](../icons/pubmethod.gif)| [GH_PathOffset(IEnumerableInt32,
Int32, Boolean,
Boolean)](M_Grasshopper_Kernel_Data_GH_PathOffset__ctor_3.htm)| Initializes a
new instance of the GH_PathOffset class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[ItemOffset](P_Grasshopper_Kernel_Data_GH_PathOffset_ItemOffset.htm)|  Gets or
sets the relative offset for branch items.  
![Public property](../icons/pubproperty.gif)|
[ItemWrap](P_Grasshopper_Kernel_Data_GH_PathOffset_ItemWrap.htm)|  Gets or
sets the ItemWrap flag.  
![Public property](../icons/pubproperty.gif)|
[PathOffset](P_Grasshopper_Kernel_Data_GH_PathOffset_PathOffset.htm)|  Gets
access to the relative offsets for path indices.  
![Public property](../icons/pubproperty.gif)|
[PathWrap](P_Grasshopper_Kernel_Data_GH_PathOffset_PathWrap.htm)|  Gets or
sets the PathWrap flag.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)| [OffsetPath(GH_Path, Int32, GH_Path,
Int32)](M_Grasshopper_Kernel_Data_GH_PathOffset_OffsetPath.htm)|  Offset a
path + index value without wrapping.  
![Public method](../icons/pubmethod.gif)| [OffsetPath(GH_Path, Int32,
IGH_Structure, GH_Path,
Int32)](M_Grasshopper_Kernel_Data_GH_PathOffset_OffsetPath_1.htm)|  Offset a
path + index value with wrapping and bounds checking.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ParseString](M_Grasshopper_Kernel_Data_GH_PathOffset_ParseString.htm)|  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Data_GH_PathOffset_ToString.htm)|  Format the
Path Offset.  (Overrides
[ObjectToString](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

