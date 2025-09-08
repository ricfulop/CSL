---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_GH_RotationalTuningData_1.htm
scraped_at: 2025-09-08T16:13:01.395148
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH_RotationalTuningData(T)
Class](../html/T_Grasshopper_GUI_GH_RotationalTuningData_1.htm
"GH_RotationalTuningData\(T\) Class")

[GH_RotationalTuningData(T) Constructor
](../html/Overload_Grasshopper_GUI_GH_RotationalTuningData_1__ctor.htm
"GH_RotationalTuningData\(T\) Constructor ")

[GH_RotationalTuningData(T)
Properties](../html/Properties_T_Grasshopper_GUI_GH_RotationalTuningData_1.htm
"GH_RotationalTuningData\(T\) Properties")

[GH_RotationalTuningData(T)
Methods](../html/Methods_T_Grasshopper_GUI_GH_RotationalTuningData_1.htm
"GH_RotationalTuningData\(T\) Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_RotationalTuningDataT Class  
  
---  
  
Utility class for keeping track of rotational mouse events.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.GUIGH_RotationalTuningDataT  

**Namespace:** [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_RotationalTuningData<T>
    
    
    
    Public Class GH_RotationalTuningData(Of T)

#### Type Parameters

T

    Basic type for initial conditions.

The GH_RotationalTuningDataT type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)| [GH_RotationalTuningDataT(T,
PointF)](M_Grasshopper_GUI_GH_RotationalTuningData_1__ctor.htm)|  Create a new
instance of the rotational tuning data.  
![Public method](../icons/pubmethod.gif)| [GH_RotationalTuningDataT(T, PointF,
PointF)](M_Grasshopper_GUI_GH_RotationalTuningData_1__ctor_1.htm)|  Create a
new instance of the rotational tuning data.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Frame](P_Grasshopper_GUI_GH_RotationalTuningData_1_Frame.htm)|  Gets the
frame at the given index.  
![Public property](../icons/pubproperty.gif)|
[FrameCount](P_Grasshopper_GUI_GH_RotationalTuningData_1_FrameCount.htm)|
Gets the total number of recorded frames.  
![Public property](../icons/pubproperty.gif)|
[InitialValue](P_Grasshopper_GUI_GH_RotationalTuningData_1_InitialValue.htm)|
Gets the initial value.  
![Public property](../icons/pubproperty.gif)|
[Pivot](P_Grasshopper_GUI_GH_RotationalTuningData_1_Pivot.htm)|  Gets or sets
the rotational pivot. You only need to set this if the pivot changes.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AddFrame](M_Grasshopper_GUI_GH_RotationalTuningData_1_AddFrame.htm)|  Grow
the tuning track by one point and compute the angle.  
![Public method](../icons/pubmethod.gif)|
[TotalAngle](M_Grasshopper_GUI_GH_RotationalTuningData_1_TotalAngle.htm)|
Compute the total angle from the first to the last frame.  
![Public method](../icons/pubmethod.gif)|
[TotalTurns](M_Grasshopper_GUI_GH_RotationalTuningData_1_TotalTurns.htm)|
Compute the total number of full turns from the first to the last frame.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

