---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_GH_FadeAnimation.htm
scraped_at: 2025-09-08T16:12:33.283643
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH_FadeAnimation Class](../html/T_Grasshopper_GUI_GH_FadeAnimation.htm
"GH_FadeAnimation Class")

[GH_FadeAnimation Constructor
](../html/Overload_Grasshopper_GUI_GH_FadeAnimation__ctor.htm
"GH_FadeAnimation Constructor ")

[GH_FadeAnimation
Properties](../html/Properties_T_Grasshopper_GUI_GH_FadeAnimation.htm
"GH_FadeAnimation Properties")

[GH_FadeAnimation
Methods](../html/Methods_T_Grasshopper_GUI_GH_FadeAnimation.htm
"GH_FadeAnimation Methods")

[GH_FadeAnimation
Fields](../html/Fields_T_Grasshopper_GUI_GH_FadeAnimation.htm
"GH_FadeAnimation Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_FadeAnimation Class  
  
---  
  
Utility class for animating fade ZUI events on the canvas.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.GUIGH_FadeAnimation  

**Namespace:** [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_FadeAnimation
    
    
    Public Class GH_FadeAnimation

The GH_FadeAnimation type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_FadeAnimation](M_Grasshopper_GUI_GH_FadeAnimation__ctor.htm)|  Creates a
new instance of the Animator class with default settings.  
![Public method](../icons/pubmethod.gif)|
[GH_FadeAnimation(Single)](M_Grasshopper_GUI_GH_FadeAnimation__ctor_1.htm)|
Create a new instance of the Animator class with custom values for zoom
threshold.  
![Public method](../icons/pubmethod.gif)| [GH_FadeAnimation(Single,
Int32)](M_Grasshopper_GUI_GH_FadeAnimation__ctor_2.htm)|  Create a new
instance of the Animator class with custom values for zoom threshold and
duration.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Duration](P_Grasshopper_GUI_GH_FadeAnimation_Duration.htm)|  Gets or sets the
duration (in milliseconds) for ZUI animations. Negative durations are not
allowed. The default is 350 milliseconds.  
![Public property](../icons/pubproperty.gif)|
[FadeAlpha](P_Grasshopper_GUI_GH_FadeAnimation_FadeAlpha.htm)|  Gets the blend
alpha byte for the current state. 0 means fully hidden, 255 means fully shown.  
![Public property](../icons/pubproperty.gif)|
[FadeFactor](P_Grasshopper_GUI_GH_FadeAnimation_FadeFactor.htm)|  Gets the
blend factor for the current state. 0.0 means fully hidden, 1.0 means fully
shown.  
![Public property](../icons/pubproperty.gif)|
[IsFinished](P_Grasshopper_GUI_GH_FadeAnimation_IsFinished.htm)|  Gets a value
indicating whether this animator has finished animating.  
![Public property](../icons/pubproperty.gif)|
[Phase](P_Grasshopper_GUI_GH_FadeAnimation_Phase.htm)|  Gets the current
animation phase.  
![Public property](../icons/pubproperty.gif)|
[Threshold](P_Grasshopper_GUI_GH_FadeAnimation_Threshold.htm)|  Gets or sets
the threshold value for the fade animation trigger.  
![Public property](../icons/pubproperty.gif)|
[TriggerUpdate](P_Grasshopper_GUI_GH_FadeAnimation_TriggerUpdate.htm)|  Gets
or sets whether this animator triggers canvas updates.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Evaluate(GH_Canvas)](M_Grasshopper_GUI_GH_FadeAnimation_Evaluate.htm)|
Reevaluate the fade animation parameters. You should call this method from
within the Render method of your attributes. If an animation is currently in
progress a redraw of the canvas will be scheduled, whether or not the
attributes are actually visible on the canvas. You should therefore only call
this method if your attributes are already drawing themselves.  
![Public method](../icons/pubmethod.gif)| [Evaluate(GH_Canvas,
Boolean)](M_Grasshopper_GUI_GH_FadeAnimation_Evaluate_1.htm)|  Reevaluate the
fade animation parameters. You should call this method from within the Render
method of your attributes. If an animation is currently in progress a redraw
of the canvas will be scheduled, whether or not the attributes are actually
visible on the canvas. You should therefore only call this method if your
attributes are already drawing themselves.  
![Public method](../icons/pubmethod.gif)| [Evaluate(GH_Canvas,
Single)](M_Grasshopper_GUI_GH_FadeAnimation_Evaluate_2.htm)|  Reevaluate the
fade animation parameters. You should call this method from within the Render
method of your attributes. If an animation is currently in progress a redraw
of the canvas will be scheduled, whether or not the attributes are actually
visible on the canvas. You should therefore only call this method if your
attributes are already drawing themselves.  
![Public method](../icons/pubmethod.gif)| [Evaluate(GH_Canvas, Single,
Boolean)](M_Grasshopper_GUI_GH_FadeAnimation_Evaluate_3.htm)|  Reevaluate the
fade animation parameters. You should call this method from within the Render
method of your attributes. If an animation is currently in progress a redraw
of the canvas will be scheduled, whether or not the attributes are actually
visible on the canvas. You should therefore only call this method if your
attributes are already drawing themselves.  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[Delay](F_Grasshopper_GUI_GH_FadeAnimation_Delay.htm)|  Gets the number of
milliseconds between redraws (25 milliseconds, resulting in ~40 fps)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

