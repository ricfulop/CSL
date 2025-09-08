---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_GH_TrackerFrame.htm
scraped_at: 2025-09-08T16:13:15.462602
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH_TrackerFrame Structure](../html/T_Grasshopper_GUI_GH_TrackerFrame.htm
"GH_TrackerFrame Structure")

[GH_TrackerFrame Constructor
](../html/M_Grasshopper_GUI_GH_TrackerFrame__ctor.htm "GH_TrackerFrame
Constructor ")

[GH_TrackerFrame Fields](../html/Fields_T_Grasshopper_GUI_GH_TrackerFrame.htm
"GH_TrackerFrame Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_TrackerFrame Structure  
  
---  
  
Represents a single frame in a mouse-tracker history. A frame represents all
relevant mouse and keyboard data at a given time.

**Namespace:** [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public struct GH_TrackerFrame
    
    
    Public Structure GH_TrackerFrame

The GH_TrackerFrame type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_TrackerFrame](M_Grasshopper_GUI_GH_TrackerFrame__ctor.htm)| Initializes a
new instance of the GH_TrackerFrame class  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Public field](../icons/pubfield.gif)|
[Buttons](F_Grasshopper_GUI_GH_TrackerFrame_Buttons.htm)|  The state of the
mouse buttons of the frame.  
![Public field](../icons/pubfield.gif)|
[Keys](F_Grasshopper_GUI_GH_TrackerFrame_Keys.htm)|  The state of the modifier
keys (Contro, Shift and Alt) of the frame.  
![Public field](../icons/pubfield.gif)|
[PositionControl](F_Grasshopper_GUI_GH_TrackerFrame_PositionControl.htm)|  The
position (in control coordinates) of the frame.  
![Public field](../icons/pubfield.gif)|
[PositionScreen](F_Grasshopper_GUI_GH_TrackerFrame_PositionScreen.htm)|  The
position (in screen coordinates) of the frame.  
![Public field](../icons/pubfield.gif)|
[Tag](F_Grasshopper_GUI_GH_TrackerFrame_Tag.htm)|  Optional Tag object (to be
supplied by user).  
![Public field](../icons/pubfield.gif)|
[Time](F_Grasshopper_GUI_GH_TrackerFrame_Time.htm)|  The time at which this
frame was recorded.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

