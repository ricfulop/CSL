---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_IGH_TaskCapableComponent.htm
scraped_at: 2025-09-08T16:18:44.895864
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH_TaskCapableComponent
Interface](../html/T_Grasshopper_Kernel_IGH_TaskCapableComponent.htm
"IGH_TaskCapableComponent Interface")

[IGH_TaskCapableComponent
Properties](../html/Properties_T_Grasshopper_Kernel_IGH_TaskCapableComponent.htm
"IGH_TaskCapableComponent Properties")

[IGH_TaskCapableComponent
Methods](../html/Methods_T_Grasshopper_Kernel_IGH_TaskCapableComponent.htm
"IGH_TaskCapableComponent Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_TaskCapableComponent Interface  
  
---  
  
GH_Component that can choose to support the use of Tasks to compute solutions
When UseTasks returns true, the component has it's SolveInstance enumeration
called twice. The first pass (InPreSolve=True) is intended solely for
collecting data and starting calculation tasks. The second pass
(InPreSolve=False) takes results or the tasks and sets the output.

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_TaskCapableComponent : IGH_Component
    
    
    Public Interface IGH_TaskCapableComponent
    	Inherits IGH_Component

The IGH_TaskCapableComponent type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[InConstructor](P_Grasshopper_Kernel_IGH_Component_InConstructor.htm)|  Gets
the constructor flag for this instance. If InConstructor = True, it means the
component is still registering parameters and the layout is not yet complete.
(Inherited from [IGH_Component](T_Grasshopper_Kernel_IGH_Component.htm).)  
![Public property](../icons/pubproperty.gif)|
[InPreSolve](P_Grasshopper_Kernel_IGH_TaskCapableComponent_InPreSolve.htm)|
Is set to True by the framework right before a "use tasks" pass is made on
SolveIntance calls. When True, SolveInstance should be using Tasks to start
calculations on input data. When False, SolveInstance should be setting the
output data by either using the result of a task or directly computing the
results.  
![Public property](../icons/pubproperty.gif)|
[IsValidMasterParameterIndex](P_Grasshopper_Kernel_IGH_Component_IsValidMasterParameterIndex.htm)|
Gets whether the MasterParameterIndex property identifies a valid parameter.
(Inherited from [IGH_Component](T_Grasshopper_Kernel_IGH_Component.htm).)  
![Public property](../icons/pubproperty.gif)|
[MasterParameterIndex](P_Grasshopper_Kernel_IGH_Component_MasterParameterIndex.htm)|
Gets or sets the master parameter index override. Negative indices or indices
larger than or equal to the input parameter count will be ignored and regular
master parameter detection will kick in.  (Inherited from
[IGH_Component](T_Grasshopper_Kernel_IGH_Component.htm).)  
![Public property](../icons/pubproperty.gif)|
[Message](P_Grasshopper_Kernel_IGH_Component_Message.htm)|  Gets or sets a
custom message to be displayed underneath the component.  (Inherited from
[IGH_Component](T_Grasshopper_Kernel_IGH_Component.htm).)  
![Public property](../icons/pubproperty.gif)|
[Params](P_Grasshopper_Kernel_IGH_Component_Params.htm)|  Gets the Params
object that managed input and output parameters.  (Inherited from
[IGH_Component](T_Grasshopper_Kernel_IGH_Component.htm).)  
![Public property](../icons/pubproperty.gif)|
[RunCount](P_Grasshopper_Kernel_IGH_Component_RunCount.htm)|  Gets a value
indicating how many times the SolveInstance method was called on this
component during the last solution. This property will return -1 if no valid
runcount is available.  (Inherited from
[IGH_Component](T_Grasshopper_Kernel_IGH_Component.htm).)  
![Public property](../icons/pubproperty.gif)|
[UseTasks](P_Grasshopper_Kernel_IGH_TaskCapableComponent_UseTasks.htm)|
Returns True if the component is set to support tasks. Components can have
this feature turned on/off. Note that even if UseTasks returns True, there is
a chance that a multipass task based solution may not be invoked depending on
if multiple calls need to be made during enumeration. You must pay attention
to the value of InPreSolve during SolveInstance. The set version of this
property can be called by the framework if we want to provide a technique to
globally turn on/off task support for all components in a definition.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[RequestTaskCancellation](M_Grasshopper_Kernel_IGH_TaskCapableComponent_RequestTaskCancellation.htm)|
Called by the framework when solving has been interrupted and tasks do not
need to complete.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

