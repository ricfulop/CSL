---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Gradient_GH_Grip.htm
scraped_at: 2025-09-08T16:15:04.944174
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Gradient](../html/N_Grasshopper_GUI_Gradient.htm
"Grasshopper.GUI.Gradient")

[GH_Grip Class](../html/T_Grasshopper_GUI_Gradient_GH_Grip.htm "GH_Grip
Class")

[GH_Grip Constructor
](../html/Overload_Grasshopper_GUI_Gradient_GH_Grip__ctor.htm "GH_Grip
Constructor ")

[GH_Grip Properties](../html/Properties_T_Grasshopper_GUI_Gradient_GH_Grip.htm
"GH_Grip Properties")

[GH_Grip Methods](../html/Methods_T_Grasshopper_GUI_Gradient_GH_Grip.htm
"GH_Grip Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Grip Class  
  
---  
  
Represents a grip in a gradient. A grip defines both where and how the colour
of a gradient changes.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.GUI.GradientGH_Grip  

**Namespace:** [Grasshopper.GUI.Gradient](N_Grasshopper_GUI_Gradient.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Grip : IComparable<GH_Grip>, 
    	GH_ISerializable
    
    
    Public Class GH_Grip
    	Implements IComparable(Of GH_Grip), GH_ISerializable

The GH_Grip type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_Grip](M_Grasshopper_GUI_Gradient_GH_Grip__ctor.htm)| Initializes a new
instance of the GH_Grip class  
![Public method](../icons/pubmethod.gif)|
[GH_Grip(GH_Grip)](M_Grasshopper_GUI_Gradient_GH_Grip__ctor_1.htm)|
Initializes a new instance of the GH_Grip class  
![Public method](../icons/pubmethod.gif)| [GH_Grip(Double,
Color)](M_Grasshopper_GUI_Gradient_GH_Grip__ctor_2.htm)| Initializes a new
instance of the GH_Grip class  
![Public method](../icons/pubmethod.gif)| [GH_Grip(Double, Color,
Color)](M_Grasshopper_GUI_Gradient_GH_Grip__ctor_3.htm)| Initializes a new
instance of the GH_Grip class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[ColourLeft](P_Grasshopper_GUI_Gradient_GH_Grip_ColourLeft.htm)|  Gets the
colour to the left of this grip.  
![Public property](../icons/pubproperty.gif)|
[ColourRight](P_Grasshopper_GUI_Gradient_GH_Grip_ColourRight.htm)|  Gets the
colour to the right of this grip.  
![Public property](../icons/pubproperty.gif)|
[GripId](P_Grasshopper_GUI_Gradient_GH_Grip_GripId.htm)|  Gets the Grip ID.  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_GUI_Gradient_GH_Grip_IsValid.htm)|  Gets whether this
grip is valid. A valid grip must have a non-empty Id and a non-NaN parameter.  
![Public property](../icons/pubproperty.gif)|
[Parameter](P_Grasshopper_GUI_Gradient_GH_Grip_Parameter.htm)|  Gets or sets
the numeric parameter of the grip.  
![Public property](../icons/pubproperty.gif)|
[Selected](P_Grasshopper_GUI_Gradient_GH_Grip_Selected.htm)|  Gets or sets
whether this grip is selected. Selection state is not (de)serialized.  
![Public property](../icons/pubproperty.gif)|
[Type](P_Grasshopper_GUI_Gradient_GH_Grip_Type.htm)|  Gets whether the colour
across this grip is smooth.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Blend](M_Grasshopper_GUI_Gradient_GH_Grip_Blend.htm)|  
![Public method](../icons/pubmethod.gif)|
[CompareTo](M_Grasshopper_GUI_Gradient_GH_Grip_CompareTo.htm)|  
![Public method](../icons/pubmethod.gif)|
[MutateId](M_Grasshopper_GUI_Gradient_GH_Grip_MutateId.htm)|  Create a new
grip ID.  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_GUI_Gradient_GH_Grip_Read.htm)|  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_GUI_Gradient_GH_Grip_Write.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Gradient Namespace](N_Grasshopper_GUI_Gradient.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

