---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_GH_Animator_1.htm
scraped_at: 2025-09-08T16:12:11.190256
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH_Animator(T) Class](../html/T_Grasshopper_GUI_GH_Animator_1.htm
"GH_Animator\(T\) Class")

[GH_Animator(T) Constructor
](../html/Overload_Grasshopper_GUI_GH_Animator_1__ctor.htm "GH_Animator\(T\)
Constructor ")

[GH_Animator(T)
Properties](../html/Properties_T_Grasshopper_GUI_GH_Animator_1.htm
"GH_Animator\(T\) Properties")

[GH_Animator(T) Methods](../html/Methods_T_Grasshopper_GUI_GH_Animator_1.htm
"GH_Animator\(T\) Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_AnimatorT Class  
  
---  
  
Provides methods for animating values.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.GUIGH_AnimatorT  

**Namespace:** [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Animator<T>
    
    
    
    Public Class GH_Animator(Of T)

#### Type Parameters

T

    Data type to animate.

The GH_AnimatorT type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)| [GH_AnimatorT(T, T, TimeSpan,
GH_AnimatorTInterpolate)](M_Grasshopper_GUI_GH_Animator_1__ctor_1.htm)|
Create a new instance of the generic animator.  
![Public method](../icons/pubmethod.gif)| [GH_AnimatorT(T, T, DateTime,
DateTime,
GH_AnimatorTInterpolate)](M_Grasshopper_GUI_GH_Animator_1__ctor.htm)|  Create
a new instance of the generic animator.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Interpolation](P_Grasshopper_GUI_GH_Animator_1_Interpolation.htm)|  Gets or
sets the interpolation mode. Changing the mode during an animation will result
in discontinuous motion.  
![Public property](../icons/pubproperty.gif)|
[Phase](P_Grasshopper_GUI_GH_Animator_1_Phase.htm)|  Gets the current
animation phase.  
![Public property](../icons/pubproperty.gif)|
[ValueA](P_Grasshopper_GUI_GH_Animator_1_ValueA.htm)|  Gets or sets the start
value of the animation. This value is set from within the constructor though
you can change it at any time.  
![Public property](../icons/pubproperty.gif)|
[ValueB](P_Grasshopper_GUI_GH_Animator_1_ValueB.htm)|  Gets or sets the end
value of the animation. This value is set from within the constructor though
you can change it at any time.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AdjustAnimation(T)](M_Grasshopper_GUI_GH_Animator_1_AdjustAnimation.htm)|
Adjust the animation.  
![Public method](../icons/pubmethod.gif)| [AdjustAnimation(T,
Int32)](M_Grasshopper_GUI_GH_Animator_1_AdjustAnimation_2.htm)|  Adjust the
animation.  
![Public method](../icons/pubmethod.gif)| [AdjustAnimation(T, DateTime,
DateTime)](M_Grasshopper_GUI_GH_Animator_1_AdjustAnimation_1.htm)|  Adjust the
animation.  
![Public method](../icons/pubmethod.gif)|
[CurrentValue](M_Grasshopper_GUI_GH_Animator_1_CurrentValue.htm)|  Gets the
current animated value.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

