---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_IGH_VariableParameterComponent.htm
scraped_at: 2025-09-08T16:18:48.920759
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH_VariableParameterComponent
Interface](../html/T_Grasshopper_Kernel_IGH_VariableParameterComponent.htm
"IGH_VariableParameterComponent Interface")

[IGH_VariableParameterComponent
Methods](../html/Methods_T_Grasshopper_Kernel_IGH_VariableParameterComponent.htm
"IGH_VariableParameterComponent Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_VariableParameterComponent Interface  
  
---  
  
Implement this interface in your component if you want to enable variable
parameter UI.

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_VariableParameterComponent
    
    
    Public Interface IGH_VariableParameterComponent

The IGH_VariableParameterComponent type exposes the following members.

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CanInsertParameter](M_Grasshopper_Kernel_IGH_VariableParameterComponent_CanInsertParameter.htm)|
This function will get called before an attempt is made to insert a parameter.
Since this method is potentially called on Canvas redraws, it must be _fast_.  
![Public method](../icons/pubmethod.gif)|
[CanRemoveParameter](M_Grasshopper_Kernel_IGH_VariableParameterComponent_CanRemoveParameter.htm)|
This function will get called before an attempt is made to remove a parameter.
Since this method is potentially called on Canvas redraws, it must be _fast_.  
![Public method](../icons/pubmethod.gif)|
[CreateParameter](M_Grasshopper_Kernel_IGH_VariableParameterComponent_CreateParameter.htm)|
This function will be called when a new parameter is about to be inserted. You
_must_ provide a valid parameter or insertion will be skipped. You do not,
repeat _not_ , need to insert the parameter yourself.  
![Public method](../icons/pubmethod.gif)|
[DestroyParameter](M_Grasshopper_Kernel_IGH_VariableParameterComponent_DestroyParameter.htm)|
This function will be called when a parameter is about to be removed. You do
not need to do anything, but this would be a good time to remove any event
handlers that might be attached to the parameter in question.  
![Public method](../icons/pubmethod.gif)|
[VariableParameterMaintenance](M_Grasshopper_Kernel_IGH_VariableParameterComponent_VariableParameterMaintenance.htm)|
This method will be called when a closely related set of variable parameter
operations completes. This would be a good time to ensure all Nicknames and
parameter properties are correct. This method will also be called upon IO
operations such as Open, Paste, Undo and Redo.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

