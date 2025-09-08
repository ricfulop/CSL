---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Gradient_GH_Gradient.htm
scraped_at: 2025-09-08T16:15:00.920756
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Gradient](../html/N_Grasshopper_GUI_Gradient.htm
"Grasshopper.GUI.Gradient")

[GH_Gradient Class](../html/T_Grasshopper_GUI_Gradient_GH_Gradient.htm
"GH_Gradient Class")

[GH_Gradient Constructor
](../html/Overload_Grasshopper_GUI_Gradient_GH_Gradient__ctor.htm "GH_Gradient
Constructor ")

[GH_Gradient
Properties](../html/Properties_T_Grasshopper_GUI_Gradient_GH_Gradient.htm
"GH_Gradient Properties")

[GH_Gradient
Methods](../html/Methods_T_Grasshopper_GUI_Gradient_GH_Gradient.htm
"GH_Gradient Methods")

[GH_Gradient Events](../html/Events_T_Grasshopper_GUI_Gradient_GH_Gradient.htm
"GH_Gradient Events")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Gradient Class  
  
---  
  
Represents a colour gradient defined by a succession of grips.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.GUI.GradientGH_Gradient  

**Namespace:** [Grasshopper.GUI.Gradient](N_Grasshopper_GUI_Gradient.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Gradient : GH_ISerializable, 
    	IGradient
    
    
    Public Class GH_Gradient
    	Implements GH_ISerializable, IGradient

The GH_Gradient type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_Gradient](M_Grasshopper_GUI_Gradient_GH_Gradient__ctor.htm)| Initializes a
new instance of the GH_Gradient class  
![Public method](../icons/pubmethod.gif)|
[GH_Gradient(GH_Gradient)](M_Grasshopper_GUI_Gradient_GH_Gradient__ctor_1.htm)|
Create a duplicate of another gradient.  
![Public method](../icons/pubmethod.gif)| [GH_Gradient(IEnumerableDouble,
IEnumerableColor)](M_Grasshopper_GUI_Gradient_GH_Gradient__ctor_2.htm)|
Create a new gradient from grips and colours.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Grip](P_Grasshopper_GUI_Gradient_GH_Gradient_Grip.htm)|  Gets or sets the
grip at the given index.  
![Public property](../icons/pubproperty.gif)|
[GripCount](P_Grasshopper_GUI_Gradient_GH_Gradient_GripCount.htm)|  Gets the
number of grips in this gradient.  
![Public property](../icons/pubproperty.gif)|
[Linear](P_Grasshopper_GUI_Gradient_GH_Gradient_Linear.htm)|  Gets or sets
whether the colours are interpolated linearly between grips.  
![Public property](../icons/pubproperty.gif)|
[Locked](P_Grasshopper_GUI_Gradient_GH_Gradient_Locked.htm)|  Gets or sets
whether this gradient is locked. A locked gradient cannot be modified by the
user.  
![Public property](../icons/pubproperty.gif)|
[SelectedGrip](P_Grasshopper_GUI_Gradient_GH_Gradient_SelectedGrip.htm)|  Gets
or sets the selected grip.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AddGrip(Double)](M_Grasshopper_GUI_Gradient_GH_Gradient_AddGrip_1.htm)|  Add
a new grip to the gradient. The colour of the grip will be picked so that
there is no difference to the gradient, though this is not actually possible
when the interpolation mode is not linear.  
![Public method](../icons/pubmethod.gif)|
[AddGrip(GH_Grip)](M_Grasshopper_GUI_Gradient_GH_Gradient_AddGrip.htm)|  Add a
new grip to the gradient. This method does not raise the GradientChanged
event, so you need to do that yourself by calling OnGradientChanged().  
![Public method](../icons/pubmethod.gif)| [AddGrip(Double,
Color)](M_Grasshopper_GUI_Gradient_GH_Gradient_AddGrip_2.htm)|  Add a new
single-colour grip.  
![Public method](../icons/pubmethod.gif)| [AddGrip(Double, Color,
Color)](M_Grasshopper_GUI_Gradient_GH_Gradient_AddGrip_3.htm)|  Add a new bi-
colour grip.  
![Public method](../icons/pubmethod.gif)|
[ColourAt](M_Grasshopper_GUI_Gradient_GH_Gradient_ColourAt.htm)|  Evaluate the
colour at a specific parameter.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[DeleteGripRegion](M_Grasshopper_GUI_Gradient_GH_Gradient_DeleteGripRegion.htm)|
Gets the Delete Grip region rectangle based on a gradient destination
rectangle.  
![Public method](../icons/pubmethod.gif)|
[DisplayGradientEditor](M_Grasshopper_GUI_Gradient_GH_Gradient_DisplayGradientEditor.htm)|  
![Public method](../icons/pubmethod.gif)|
[DisplayGripColourPicker](M_Grasshopper_GUI_Gradient_GH_Gradient_DisplayGripColourPicker.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[EarthlyBrown](M_Grasshopper_GUI_Gradient_GH_Gradient_EarthlyBrown.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Forest](M_Grasshopper_GUI_Gradient_GH_Gradient_Forest.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[GreyScale](M_Grasshopper_GUI_Gradient_GH_Gradient_GreyScale.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Heat](M_Grasshopper_GUI_Gradient_GH_Gradient_Heat.htm)|  
![Public method](../icons/pubmethod.gif)|
[MouseDown](M_Grasshopper_GUI_Gradient_GH_Gradient_MouseDown.htm)|  Begin grip
drag operation.  
![Public method](../icons/pubmethod.gif)|
[MouseDragAbort](M_Grasshopper_GUI_Gradient_GH_Gradient_MouseDragAbort.htm)|
Abort grip drag.  
![Public method](../icons/pubmethod.gif)|
[MouseMove](M_Grasshopper_GUI_Gradient_GH_Gradient_MouseMove.htm)|  Continue
grip dragging operation.  
![Public method](../icons/pubmethod.gif)|
[MouseUp](M_Grasshopper_GUI_Gradient_GH_Gradient_MouseUp.htm)|  Terminate grip
drag.  
![Public method](../icons/pubmethod.gif)|
[NearestGrip(Double)](M_Grasshopper_GUI_Gradient_GH_Gradient_NearestGrip.htm)|
Find the nearest grip to a parameter.  
![Public method](../icons/pubmethod.gif)| [NearestGrip(Double,
GH_GripSide)](M_Grasshopper_GUI_Gradient_GH_Gradient_NearestGrip_1.htm)|  Find
the nearest grip to a parameter.  
![Public method](../icons/pubmethod.gif)| [NearestGrip(RectangleF, PointF,
Double)](M_Grasshopper_GUI_Gradient_GH_Gradient_NearestGrip_2.htm)|  Find the
nearest grip in screen coordinates.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[NewGripRegion](M_Grasshopper_GUI_Gradient_GH_Gradient_NewGripRegion.htm)|
Gets the new Grip region rectangle based on a gradient destination rectangle.  
![Public method](../icons/pubmethod.gif)|
[NormalizeGrips](M_Grasshopper_GUI_Gradient_GH_Gradient_NormalizeGrips.htm)|
Normalize all grips. This will scale all grip parameters so that the full
gradient extend equals 0~1.  
![Public method](../icons/pubmethod.gif)|
[OnGradientChanged](M_Grasshopper_GUI_Gradient_GH_Gradient_OnGradientChanged.htm)|
Raise the GradientChanged event.  
![Public method](../icons/pubmethod.gif)|
[OnGradientChangedIntermediate](M_Grasshopper_GUI_Gradient_GH_Gradient_OnGradientChangedIntermediate.htm)|
Raise the GradientChanged event.  
![Public method](../icons/pubmethod.gif)|
[OnSelectionChanged](M_Grasshopper_GUI_Gradient_GH_Gradient_OnSelectionChanged.htm)|
Raise the SelectionChanged event.  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_GUI_Gradient_GH_Gradient_Read.htm)|  
![Public method](../icons/pubmethod.gif)|
[RemoveGrip(GH_Grip)](M_Grasshopper_GUI_Gradient_GH_Gradient_RemoveGrip.htm)|
Remove the specified grip.  
![Public method](../icons/pubmethod.gif)|
[RemoveGrip(Int32)](M_Grasshopper_GUI_Gradient_GH_Gradient_RemoveGrip_1.htm)|
Remove the grip at the specified index.  
![Public method](../icons/pubmethod.gif)|
[Render_Background](M_Grasshopper_GUI_Gradient_GH_Gradient_Render_Background.htm)|  
![Public method](../icons/pubmethod.gif)|
[Render_Gradient](M_Grasshopper_GUI_Gradient_GH_Gradient_Render_Gradient.htm)|  
![Public method](../icons/pubmethod.gif)|
[Render_Grips](M_Grasshopper_GUI_Gradient_GH_Gradient_Render_Grips.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[SoGay](M_Grasshopper_GUI_Gradient_GH_Gradient_SoGay.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Spectrum](M_Grasshopper_GUI_Gradient_GH_Gradient_Spectrum.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Traffic](M_Grasshopper_GUI_Gradient_GH_Gradient_Traffic.htm)|  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_GUI_Gradient_GH_Gradient_Write.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Zebra](M_Grasshopper_GUI_Gradient_GH_Gradient_Zebra.htm)|  
Top

![](../icons/SectionExpanded.png)Events

| Name| Description  
---|---|---  
![Public event](../icons/pubevent.gif)|
[GradientChanged](E_Grasshopper_GUI_Gradient_GH_Gradient_GradientChanged.htm)|  
![Public event](../icons/pubevent.gif)|
[SelectionChanged](E_Grasshopper_GUI_Gradient_GH_Gradient_SelectionChanged.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Gradient Namespace](N_Grasshopper_GUI_Gradient.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

