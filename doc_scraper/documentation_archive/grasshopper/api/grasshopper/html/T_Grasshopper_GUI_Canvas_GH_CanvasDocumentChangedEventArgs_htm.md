---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Canvas_GH_CanvasDocumentChangedEventArgs.htm
scraped_at: 2025-09-08T16:14:26.820533
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm
"Grasshopper.GUI.Canvas")

[GH_CanvasDocumentChangedEventArgs
Class](../html/T_Grasshopper_GUI_Canvas_GH_CanvasDocumentChangedEventArgs.htm
"GH_CanvasDocumentChangedEventArgs Class")

[GH_CanvasDocumentChangedEventArgs Constructor
](../html/M_Grasshopper_GUI_Canvas_GH_CanvasDocumentChangedEventArgs__ctor.htm
"GH_CanvasDocumentChangedEventArgs Constructor ")

[GH_CanvasDocumentChangedEventArgs
Properties](../html/Properties_T_Grasshopper_GUI_Canvas_GH_CanvasDocumentChangedEventArgs.htm
"GH_CanvasDocumentChangedEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_CanvasDocumentChangedEventArgs Class  
  
---  
  
These arguments are used in the DocumentChanged event on GH_Canvas.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[SystemEventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
Grasshopper.GUI.CanvasGH_CanvasDocumentChangedEventArgs  

**Namespace:** [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_CanvasDocumentChangedEventArgs : EventArgs
    
    
    Public Class GH_CanvasDocumentChangedEventArgs
    	Inherits EventArgs

The GH_CanvasDocumentChangedEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_CanvasDocumentChangedEventArgs](M_Grasshopper_GUI_Canvas_GH_CanvasDocumentChangedEventArgs__ctor.htm)|
Initializes a new instance of the GH_CanvasDocumentChangedEventArgs class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[NewDocument](P_Grasshopper_GUI_Canvas_GH_CanvasDocumentChangedEventArgs_NewDocument.htm)|
Gets the document which has just been loaded into the canvas.  
![Public property](../icons/pubproperty.gif)|
[OldDocument](P_Grasshopper_GUI_Canvas_GH_CanvasDocumentChangedEventArgs_OldDocument.htm)|
Gets the document which was previously loaded into the canvas.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

