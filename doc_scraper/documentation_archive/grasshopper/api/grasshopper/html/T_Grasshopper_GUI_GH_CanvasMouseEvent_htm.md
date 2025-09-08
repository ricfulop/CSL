---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_GH_CanvasMouseEvent.htm
scraped_at: 2025-09-08T16:12:16.196386
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH_CanvasMouseEvent Class](../html/T_Grasshopper_GUI_GH_CanvasMouseEvent.htm
"GH_CanvasMouseEvent Class")

[GH_CanvasMouseEvent Constructor
](../html/Overload_Grasshopper_GUI_GH_CanvasMouseEvent__ctor.htm
"GH_CanvasMouseEvent Constructor ")

[GH_CanvasMouseEvent
Properties](../html/Properties_T_Grasshopper_GUI_GH_CanvasMouseEvent.htm
"GH_CanvasMouseEvent Properties")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_CanvasMouseEvent Class  
  
---  
  
Class used in Canvas UI events.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[SystemEventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
Grasshopper.GUIGH_CanvasMouseEvent  

**Namespace:** [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_CanvasMouseEvent : EventArgs
    
    
    Public Class GH_CanvasMouseEvent
    	Inherits EventArgs

The GH_CanvasMouseEvent type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_CanvasMouseEvent](M_Grasshopper_GUI_GH_CanvasMouseEvent__ctor.htm)|  Blank
constructor.  
![Public method](../icons/pubmethod.gif)| [GH_CanvasMouseEvent(GH_Viewport,
MouseEventArgs)](M_Grasshopper_GUI_GH_CanvasMouseEvent__ctor_1.htm)|
Constructor.  
![Public method](../icons/pubmethod.gif)| [GH_CanvasMouseEvent(Point, PointF,
MouseButtons, Int32,
Int32)](M_Grasshopper_GUI_GH_CanvasMouseEvent__ctor_2.htm)|  Constructor.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Button](P_Grasshopper_GUI_GH_CanvasMouseEvent_Button.htm)|  Gets which mouse
button was pressed.  
![Public property](../icons/pubproperty.gif)|
[CanvasLocation](P_Grasshopper_GUI_GH_CanvasMouseEvent_CanvasLocation.htm)|
Gets the location of the cursor in canvas unit coordinates.  
![Public property](../icons/pubproperty.gif)|
[CanvasX](P_Grasshopper_GUI_GH_CanvasMouseEvent_CanvasX.htm)|  Gets the
x-coordinate of the cursor location in canvas unit coordinates.  
![Public property](../icons/pubproperty.gif)|
[CanvasY](P_Grasshopper_GUI_GH_CanvasMouseEvent_CanvasY.htm)|  Gets the
y-coordinate of the cursor location in canvas unit coordinates.  
![Public property](../icons/pubproperty.gif)|
[Clicks](P_Grasshopper_GUI_GH_CanvasMouseEvent_Clicks.htm)|  Gets the number
of times the mouse button was pressed and released.  
![Public property](../icons/pubproperty.gif)|
[ControlLocation](P_Grasshopper_GUI_GH_CanvasMouseEvent_ControlLocation.htm)|
Gets the location of the cursor in control pixel coordinates.  
![Public property](../icons/pubproperty.gif)|
[ControlX](P_Grasshopper_GUI_GH_CanvasMouseEvent_ControlX.htm)|  Gets the
x-coordinate of the cursor location in control pixel coordinates.  
![Public property](../icons/pubproperty.gif)|
[ControlY](P_Grasshopper_GUI_GH_CanvasMouseEvent_ControlY.htm)|  Gets the
y-coordinate of the cursor location in control pixel coordinates.  
![Public property](../icons/pubproperty.gif)|
[Delta](P_Grasshopper_GUI_GH_CanvasMouseEvent_Delta.htm)|  Gets a signed count
of the number of detents the mouse wheel has rotated. A detent is one notch of
the mouse wheel.  
![Public property](../icons/pubproperty.gif)|
[WinFormsEventArgs](P_Grasshopper_GUI_GH_CanvasMouseEvent_WinFormsEventArgs.htm)|
Downcast this data into a Windows.Forms.MouseEventArgs instance.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

