---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_IGH_StateTag.htm
scraped_at: 2025-09-08T16:18:43.876467
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH_StateTag Interface](../html/T_Grasshopper_Kernel_IGH_StateTag.htm
"IGH_StateTag Interface")

[IGH_StateTag
Properties](../html/Properties_T_Grasshopper_Kernel_IGH_StateTag.htm
"IGH_StateTag Properties")

[IGH_StateTag Methods](../html/Methods_T_Grasshopper_Kernel_IGH_StateTag.htm
"IGH_StateTag Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_StateTag Interface  
  
---  
  
A StateTag is a visual feedback mechanism that reflects a certain local
setting of an Object.

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_StateTag
    
    
    Public Interface IGH_StateTag

The IGH_StateTag type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Description](P_Grasshopper_Kernel_IGH_StateTag_Description.htm)|  Gets the
description of this state tag.  
![Public property](../icons/pubproperty.gif)|
[Icon](P_Grasshopper_Kernel_IGH_StateTag_Icon.htm)|  Gets the 16 by 16 pixel
icon associated with this state tag.  
![Public property](../icons/pubproperty.gif)|
[Name](P_Grasshopper_Kernel_IGH_StateTag_Name.htm)|  Gets the name field of
this state tag.  
![Public property](../icons/pubproperty.gif)|
[Stage](P_Grasshopper_Kernel_IGH_StateTag_Stage.htm)|  Gets or sets the Stage
rectangle for this state tag. Stages are assigned during Attribute Layout
operations by owner objects.  
![Public property](../icons/pubproperty.gif)|
[StateDescription](P_Grasshopper_Kernel_IGH_StateTag_StateDescription.htm)|
Gets or sets the state description of this tag. The state description appears
in the Tooltip info field.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Render](M_Grasshopper_Kernel_IGH_StateTag_Render.htm)|  Render this tag into
a graphics surface.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

