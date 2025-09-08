---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_GH_DragInfo.htm
scraped_at: 2025-09-08T16:12:30.295540
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH_DragInfo Class](../html/T_Grasshopper_GUI_GH_DragInfo.htm "GH_DragInfo
Class")

[GH_DragInfo Constructor ](../html/M_Grasshopper_GUI_GH_DragInfo__ctor.htm
"GH_DragInfo Constructor ")

[GH_DragInfo Properties](../html/Properties_T_Grasshopper_GUI_GH_DragInfo.htm
"GH_DragInfo Properties")

[GH_DragInfo Methods](../html/Methods_T_Grasshopper_GUI_GH_DragInfo.htm
"GH_DragInfo Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_DragInfo Class  
  
---  
  
Contains data used for UI drag operations.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.GUIGH_DragInfo  

**Namespace:** [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_DragInfo
    
    
    Public Class GH_DragInfo

The GH_DragInfo type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_DragInfo](M_Grasshopper_GUI_GH_DragInfo__ctor.htm)|  Create a new DragInfo
instance.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Box_Drag](P_Grasshopper_GUI_GH_DragInfo_Box_Drag.htm)|  Gets the dimensions
of the box as a result of the dragging op.  
![Public property](../icons/pubproperty.gif)|
[Box_Start](P_Grasshopper_GUI_GH_DragInfo_Box_Start.htm)|  Gets the dimensions
of the drag box prior to dragging.  
![Public property](../icons/pubproperty.gif)|
[Constraint](P_Grasshopper_GUI_GH_DragInfo_Constraint.htm)|  Gets or sets the
directional constraint for the drag operation.  
![Public property](../icons/pubproperty.gif)|
[Point_Drag](P_Grasshopper_GUI_GH_DragInfo_Point_Drag.htm)|  Gets the cursor
location at the current moment.  
![Public property](../icons/pubproperty.gif)|
[Point_Start](P_Grasshopper_GUI_GH_DragInfo_Point_Start.htm)|  Gets the cursor
location at the start of the drag.  
![Public property](../icons/pubproperty.gif)|
[Region](P_Grasshopper_GUI_GH_DragInfo_Region.htm)|  Gets or sets the drag
limits. If the region is Rectangle.Empty then the region is ignored. For valid
results the Region should be larger than the dimensions of the drag box.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Drag](M_Grasshopper_GUI_GH_DragInfo_Drag.htm)|  Call this method to adjust
the drag data. Results will be automatically constrained and limited.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

