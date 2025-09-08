---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Gradient_GH_GradientChangedEventArgs.htm
scraped_at: 2025-09-08T16:15:03.924295
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Gradient](../html/N_Grasshopper_GUI_Gradient.htm
"Grasshopper.GUI.Gradient")

[GH_GradientChangedEventArgs
Class](../html/T_Grasshopper_GUI_Gradient_GH_GradientChangedEventArgs.htm
"GH_GradientChangedEventArgs Class")

[GH_GradientChangedEventArgs Constructor
](../html/M_Grasshopper_GUI_Gradient_GH_GradientChangedEventArgs__ctor.htm
"GH_GradientChangedEventArgs Constructor ")

[GH_GradientChangedEventArgs
Properties](../html/Properties_T_Grasshopper_GUI_Gradient_GH_GradientChangedEventArgs.htm
"GH_GradientChangedEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_GradientChangedEventArgs Class  
  
---  
  
Arguments for te GradientChanged event.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[SystemEventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
Grasshopper.GUI.GradientGH_GradientChangedEventArgs  

**Namespace:** [Grasshopper.GUI.Gradient](N_Grasshopper_GUI_Gradient.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_GradientChangedEventArgs : EventArgs
    
    
    Public Class GH_GradientChangedEventArgs
    	Inherits EventArgs

The GH_GradientChangedEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_GradientChangedEventArgs](M_Grasshopper_GUI_Gradient_GH_GradientChangedEventArgs__ctor.htm)|
Initializes a new instance of the GH_GradientChangedEventArgs class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Gradient](P_Grasshopper_GUI_Gradient_GH_GradientChangedEventArgs_Gradient.htm)|
Gets the gradient that raised this event.  
![Public property](../icons/pubproperty.gif)|
[Intermediate](P_Grasshopper_GUI_Gradient_GH_GradientChangedEventArgs_Intermediate.htm)|
Gets whether this event is intermediate. I.e. whether it will be followed by
another, similar event.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Gradient Namespace](N_Grasshopper_GUI_Gradient.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

