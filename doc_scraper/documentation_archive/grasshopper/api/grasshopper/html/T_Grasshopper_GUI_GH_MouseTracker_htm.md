---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_GH_MouseTracker.htm
scraped_at: 2025-09-08T16:12:56.375028
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH_MouseTracker Class](../html/T_Grasshopper_GUI_GH_MouseTracker.htm
"GH_MouseTracker Class")

[GH_MouseTracker Constructor
](../html/Overload_Grasshopper_GUI_GH_MouseTracker__ctor.htm "GH_MouseTracker
Constructor ")

[GH_MouseTracker
Properties](../html/Properties_T_Grasshopper_GUI_GH_MouseTracker.htm
"GH_MouseTracker Properties")

[GH_MouseTracker
Methods](../html/Methods_T_Grasshopper_GUI_GH_MouseTracker.htm
"GH_MouseTracker Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_MouseTracker Class  
  
---  
  
Record mouse-movements over time.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.GUIGH_MouseTracker  

**Namespace:** [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_MouseTracker
    
    
    Public Class GH_MouseTracker

The GH_MouseTracker type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_MouseTracker](M_Grasshopper_GUI_GH_MouseTracker__ctor.htm)|  Create a new
mouse tracker.  
![Public method](../icons/pubmethod.gif)|
[GH_MouseTracker(Point)](M_Grasshopper_GUI_GH_MouseTracker__ctor_1.htm)|
Create a new mouse tracker.  
![Public method](../icons/pubmethod.gif)| [GH_MouseTracker(Point,
Object)](M_Grasshopper_GUI_GH_MouseTracker__ctor_2.htm)|  Create a new mouse
tracker.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Duration](P_Grasshopper_GUI_GH_MouseTracker_Duration.htm)|  Gets the timespan
that has passed between the oldest and youngest recorded frames. This is
**not** the same as the time that has passed since recording began.  
![Public property](../icons/pubproperty.gif)|
[Frame](P_Grasshopper_GUI_GH_MouseTracker_Frame.htm)|  Gets the position (in
control coordinates) of the frame at the given index.  
![Public property](../icons/pubproperty.gif)|
[FrameCount](P_Grasshopper_GUI_GH_MouseTracker_FrameCount.htm)|  Gets the
number of recorded frames.  
![Public property](../icons/pubproperty.gif)|
[MaximumDuration](P_Grasshopper_GUI_GH_MouseTracker_MaximumDuration.htm)|
Gets or sets the maximum allowed duration of the entire record. When new
frames are recorded, old frames that are more distant than MaximumDuration
will be dropped. The default duration is 10 seconds.  
![Public property](../icons/pubproperty.gif)|
[MaximumFrameCount](P_Grasshopper_GUI_GH_MouseTracker_MaximumFrameCount.htm)|
Gets or sets the maximum number of frames to keep in history. If more frames
are added, the oldest ones will be dropped. The default is 16,384 frames.  
![Public property](../icons/pubproperty.gif)|
[NewestFrame](P_Grasshopper_GUI_GH_MouseTracker_NewestFrame.htm)|  Gets the
most recent frame in recorded history.  
![Public property](../icons/pubproperty.gif)|
[OldestFrame](P_Grasshopper_GUI_GH_MouseTracker_OldestFrame.htm)|  Gets the
oldest frame in recorded history.  
![Public property](../icons/pubproperty.gif)|
[TemporalAccuracy](P_Grasshopper_GUI_GH_MouseTracker_TemporalAccuracy.htm)|
Gets or sets the maximum temporal accuracy. Frames that are closer together
than the accuracy will not be recorded. The default accuracy equals 5ms.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Deviation](M_Grasshopper_GUI_GH_MouseTracker_Deviation.htm)|  Gets the
maximum deviation of the recorded mouse path. The maximum deviation is the
furthest distance the mouse has been from the first point in the history
record.  
![Public method](../icons/pubmethod.gif)| [Deviation(DateTime,
DateTime)](M_Grasshopper_GUI_GH_MouseTracker_Deviation_1.htm)|  Gets the
maximum deviation of the recorded mouse path. The maximum deviation is the
furthest distance the mouse has been from the first point in the history span.
It does **not** measure the largest deviation between any two points in the
time span, only the first and any subsequent point.  
![Public method](../icons/pubmethod.gif)|
[DropFrames(DateTime)](M_Grasshopper_GUI_GH_MouseTracker_DropFrames.htm)|
Drop all frames older than a given limit.  
![Public method](../icons/pubmethod.gif)|
[DropFrames(Double)](M_Grasshopper_GUI_GH_MouseTracker_DropFrames_1.htm)|
Find the youngest frame that deviates too much from the current locus and drop
it and everything preceding it.  
![Public method](../icons/pubmethod.gif)| [DropFrames(Double,
Point)](M_Grasshopper_GUI_GH_MouseTracker_DropFrames_2.htm)|  Find the
youngest frame that deviates too much from the given locus and drop it and
everything preceding it.  
![Public method](../icons/pubmethod.gif)|
[LastFrameWithinDeviation](M_Grasshopper_GUI_GH_MouseTracker_LastFrameWithinDeviation.htm)|
Starting from the youngest frame, finds the oldest frame that is still within
a maximum deviation of the youngest frame.  
![Public method](../icons/pubmethod.gif)|
[Record(Point)](M_Grasshopper_GUI_GH_MouseTracker_Record.htm)|  Record a new
mouse event frame. If this frame is closer than [Accuracy]ms to the previously
recorded frame, it is not included.  
![Public method](../icons/pubmethod.gif)| [Record(Point,
Object)](M_Grasshopper_GUI_GH_MouseTracker_Record_1.htm)|  Record a new mouse
event frame. If this frame is closer than [Accuracy]ms to the previously
recorded frame, it is not included.  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_GUI_GH_MouseTracker_ToString.htm)|  (Overrides
[ObjectToString](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

