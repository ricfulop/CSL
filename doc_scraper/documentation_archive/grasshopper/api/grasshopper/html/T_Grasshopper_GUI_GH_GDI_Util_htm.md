---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_GH_GDI_Util.htm
scraped_at: 2025-09-08T16:12:41.326583
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH_GDI_Util Class](../html/T_Grasshopper_GUI_GH_GDI_Util.htm "GH_GDI_Util
Class")

[GH_GDI_Util Methods](../html/Methods_T_Grasshopper_GUI_GH_GDI_Util.htm
"GH_GDI_Util Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_GDI_Util Class  
  
---  
  
Contains some global function for filleting corners of GDI objects.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.GUIGH_GDI_Util  

**Namespace:** [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class GH_GDI_Util
    
    
    Public NotInheritable Class GH_GDI_Util

The GH_GDI_Util type exposes the following members.

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[BoxUnion](M_Grasshopper_GUI_GH_GDI_Util_BoxUnion.htm)|  Create the outline of
a set of boxes.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FilletBoxOutline](M_Grasshopper_GUI_GH_GDI_Util_FilletBoxOutline.htm)|
Fillet all the corners of the combined outline of a set of rectangles.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FilletPolyline(Point,
Int32)](M_Grasshopper_GUI_GH_GDI_Util_FilletPolyline.htm)|  Fillet all the
corners of a freeform outline.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FilletPolyline(PointF,
Single)](M_Grasshopper_GUI_GH_GDI_Util_FilletPolyline_1.htm)|  Fillet all the
corners of a freeform outline.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FilletRectangle](M_Grasshopper_GUI_GH_GDI_Util_FilletRectangle.htm)|  Create
a rectangle with filleted corners.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Freeform_Blob(IEnumerableRectangleF, Int32,
Double)](M_Grasshopper_GUI_GH_GDI_Util_Freeform_Blob.htm)|  Create a meta-ball
outline for a set of rectangles.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Freeform_Blob(IEnumerableRectangleF, Int32, Double, FieldSolver,
Double)](M_Grasshopper_GUI_GH_GDI_Util_Freeform_Blob_1.htm)|  Create a meta-
ball outline for a set of rectangles.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[SimplifyBoxes](M_Grasshopper_GUI_GH_GDI_Util_SimplifyBoxes.htm)|  Create a
simplified collection of Rectangles that describe the same union space as the
supplied rectangles.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

