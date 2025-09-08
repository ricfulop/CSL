---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Data_GH_TreeFilter.htm
scraped_at: 2025-09-08T16:19:22.077582
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm
"Grasshopper.Kernel.Data")

[GH_TreeFilter Class](../html/T_Grasshopper_Kernel_Data_GH_TreeFilter.htm
"GH_TreeFilter Class")

[GH_TreeFilter Constructor
](../html/M_Grasshopper_Kernel_Data_GH_TreeFilter__ctor.htm "GH_TreeFilter
Constructor ")

[GH_TreeFilter
Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_TreeFilter.htm
"GH_TreeFilter Methods")

[GH_TreeFilter
Fields](../html/Fields_T_Grasshopper_Kernel_Data_GH_TreeFilter.htm
"GH_TreeFilter Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_TreeFilter Class  
  
---  
  
Represents a collection of rules for validating DataTree paths and indices.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Kernel.DataGH_TreeFilter  

**Namespace:** [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_TreeFilter
    
    
    Public Class GH_TreeFilter

The GH_TreeFilter type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_TreeFilter](M_Grasshopper_Kernel_Data_GH_TreeFilter__ctor.htm)|
Initializes a new instance of the GH_TreeFilter class  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FindItemBrackets](M_Grasshopper_Kernel_Data_GH_TreeFilter_FindItemBrackets.htm)|
Locate the two parenthesis that delineate the index segment of an Index Rule
set.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FindNextLevelChar](M_Grasshopper_Kernel_Data_GH_TreeFilter_FindNextLevelChar.htm)|
Find the next occurance of a char in a string that is level with the search
start index.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FindPathBrackets](M_Grasshopper_Kernel_Data_GH_TreeFilter_FindPathBrackets.htm)|
Locate the two curly brackets that delineate the path segment of an Index Rule
set.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FindPrevLevelChar](M_Grasshopper_Kernel_Data_GH_TreeFilter_FindPrevLevelChar.htm)|
Find the previous occurance of a char in a string that is level with the
search start index.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ParsePattern](M_Grasshopper_Kernel_Data_GH_TreeFilter_ParsePattern.htm)|
Parses a textual filter and returns an instance of the GH_TreeFilter. If the
filter cannot be parsed an exception will be thrown.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[SplitStringWithExpressions](M_Grasshopper_Kernel_Data_GH_TreeFilter_SplitStringWithExpressions.htm)|
Split a string into segments using level-aware split. This method throws
exceptions if the input string is not correctly formatted.  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[ItemClose](F_Grasshopper_Kernel_Data_GH_TreeFilter_ItemClose.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[ItemOpen](F_Grasshopper_Kernel_Data_GH_TreeFilter_ItemOpen.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[PathClose](F_Grasshopper_Kernel_Data_GH_TreeFilter_PathClose.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[PathOpen](F_Grasshopper_Kernel_Data_GH_TreeFilter_PathOpen.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[PathSeparator](F_Grasshopper_Kernel_Data_GH_TreeFilter_PathSeparator.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[SegmentSeparator](F_Grasshopper_Kernel_Data_GH_TreeFilter_SegmentSeparator.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[StringDelimeter](F_Grasshopper_Kernel_Data_GH_TreeFilter_StringDelimeter.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

