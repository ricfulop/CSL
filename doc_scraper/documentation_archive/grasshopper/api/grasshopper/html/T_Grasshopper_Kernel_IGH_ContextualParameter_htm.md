---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_IGH_ContextualParameter.htm
scraped_at: 2025-09-08T16:18:19.776675
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH_ContextualParameter
Interface](../html/T_Grasshopper_Kernel_IGH_ContextualParameter.htm
"IGH_ContextualParameter Interface")

[IGH_ContextualParameter
Properties](../html/Properties_T_Grasshopper_Kernel_IGH_ContextualParameter.htm
"IGH_ContextualParameter Properties")

[IGH_ContextualParameter
Methods](../html/Methods_T_Grasshopper_Kernel_IGH_ContextualParameter.htm
"IGH_ContextualParameter Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_ContextualParameter Interface  
  
---  
  
Base interface for contextual parameters. This makes accessing non-strongly-
typed functionality easier.

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_ContextualParameter
    
    
    Public Interface IGH_ContextualParameter

The IGH_ContextualParameter type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[AtLeast](P_Grasshopper_Kernel_IGH_ContextualParameter_AtLeast.htm)|  Minimum
number of inputs to request  
![Public property](../icons/pubproperty.gif)|
[AtMost](P_Grasshopper_Kernel_IGH_ContextualParameter_AtMost.htm)|  Maximum
number of inputs to request.  
![Public property](../icons/pubproperty.gif)|
[ContextualData](P_Grasshopper_Kernel_IGH_ContextualParameter_ContextualData.htm)|
Iterate over all specified contextual values.  
![Public property](../icons/pubproperty.gif)|
[Immediate](P_Grasshopper_Kernel_IGH_ContextualParameter_Immediate.htm)|  Gets
whether this parameter triggers immediate updates from inside its getter.
Immediacy is important for a smooth experience, but it maybe disabled if the
expected recalculation time becomes excessive.  
![Public property](../icons/pubproperty.gif)|
[Prompt](P_Grasshopper_Kernel_IGH_ContextualParameter_Prompt.htm)|  Gets the
prompt to be displayed while asking the user to enter data. The prompt string
may contain '{0}' fields which will be populated with the amount of values
picked so far.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AssignContextualData](M_Grasshopper_Kernel_IGH_ContextualParameter_AssignContextualData.htm)|
Assign a collection of values as contextual data.  
![Public method](../icons/pubmethod.gif)|
[AutoAssignContextualData](M_Grasshopper_Kernel_IGH_ContextualParameter_AutoAssignContextualData.htm)|
Use the in-build getter UI to assign data to the parameter.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

