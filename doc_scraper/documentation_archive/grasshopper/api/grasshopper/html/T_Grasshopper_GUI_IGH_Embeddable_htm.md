---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_IGH_Embeddable.htm
scraped_at: 2025-09-08T16:13:25.498571
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[IGH_Embeddable Interface](../html/T_Grasshopper_GUI_IGH_Embeddable.htm
"IGH_Embeddable Interface")

[IGH_Embeddable Methods](../html/Methods_T_Grasshopper_GUI_IGH_Embeddable.htm
"IGH_Embeddable Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_Embeddable Interface  
  
---  
  
Implement this interface in your custom control if you want to be called
before a menu commits or cancels.

**Namespace:** [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_Embeddable
    
    
    Public Interface IGH_Embeddable

The IGH_Embeddable type exposes the following members.

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[PrepareForCancel](M_Grasshopper_GUI_IGH_Embeddable_PrepareForCancel.htm)|
This will be called prior to a Cancel operation.  
![Public method](../icons/pubmethod.gif)|
[PrepareForCommit](M_Grasshopper_GUI_IGH_Embeddable_PrepareForCommit.htm)|
This will be called prior to a Commit operation.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

