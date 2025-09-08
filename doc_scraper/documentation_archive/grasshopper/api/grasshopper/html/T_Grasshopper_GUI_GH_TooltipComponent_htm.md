---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_GH_TooltipComponent.htm
scraped_at: 2025-09-08T16:13:12.451528
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH_TooltipComponent Class](../html/T_Grasshopper_GUI_GH_TooltipComponent.htm
"GH_TooltipComponent Class")

[GH_TooltipComponent Constructor
](../html/M_Grasshopper_GUI_GH_TooltipComponent__ctor.htm "GH_TooltipComponent
Constructor ")

[GH_TooltipComponent
Properties](../html/Properties_T_Grasshopper_GUI_GH_TooltipComponent.htm
"GH_TooltipComponent Properties")

[GH_TooltipComponent
Methods](../html/Methods_T_Grasshopper_GUI_GH_TooltipComponent.htm
"GH_TooltipComponent Methods")

[GH_TooltipComponent
Events](../html/Events_T_Grasshopper_GUI_GH_TooltipComponent.htm
"GH_TooltipComponent Events")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_TooltipComponent Class  
  
---  
  
This component provides Grasshopper tooltip functionality through a winforms
Component.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[SystemMarshalByRefObject](https://docs.microsoft.com/dotnet/api/system.marshalbyrefobject)  
[System.ComponentModelComponent](https://docs.microsoft.com/dotnet/api/system.componentmodel.component)  
Grasshopper.GUIGH_TooltipComponent  

**Namespace:** [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class GH_TooltipComponent : Component
    
    
    Public NotInheritable Class GH_TooltipComponent
    	Inherits Component

The GH_TooltipComponent type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_TooltipComponent](M_Grasshopper_GUI_GH_TooltipComponent__ctor.htm)|
Initializes a new instance of the GH_TooltipComponent class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Delay](P_Grasshopper_GUI_GH_TooltipComponent_Delay.htm)|  Gets or sets the
delay (in milliseconds) for this tooltip to appear.  
![Public property](../icons/pubproperty.gif)|
[Enabled](P_Grasshopper_GUI_GH_TooltipComponent_Enabled.htm)|  Gets or sets
the Enabled flag.  
![Public property](../icons/pubproperty.gif)|
[Tag](P_Grasshopper_GUI_GH_TooltipComponent_Tag.htm)|  Provides an easy way to
store information on this Tooltip.  
![Public property](../icons/pubproperty.gif)|
[Target](P_Grasshopper_GUI_GH_TooltipComponent_Target.htm)|  Gets or sets the
control this tooltip is tied to.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Hide](M_Grasshopper_GUI_GH_TooltipComponent_Hide.htm)|  
![Public method](../icons/pubmethod.gif)|
[IsTag](M_Grasshopper_GUI_GH_TooltipComponent_IsTag.htm)|  Test whether the
current Tooltip tag matches the object.  
Top

![](../icons/SectionExpanded.png)Events

| Name| Description  
---|---|---  
![Public event](../icons/pubevent.gif)|
[PopulateTooltip](E_Grasshopper_GUI_GH_TooltipComponent_PopulateTooltip.htm)|
This event is raised just prior to the tooltip display.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

