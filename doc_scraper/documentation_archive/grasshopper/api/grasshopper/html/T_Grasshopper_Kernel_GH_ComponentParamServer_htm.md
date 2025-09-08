---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_ComponentParamServer.htm
scraped_at: 2025-09-08T16:15:45.113030
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_ComponentParamServer
Class](../html/T_Grasshopper_Kernel_GH_ComponentParamServer.htm
"GH_ComponentParamServer Class")

[GH_ComponentParamServer
Properties](../html/Properties_T_Grasshopper_Kernel_GH_ComponentParamServer.htm
"GH_ComponentParamServer Properties")

[GH_ComponentParamServer
Methods](../html/Methods_T_Grasshopper_Kernel_GH_ComponentParamServer.htm
"GH_ComponentParamServer Methods")

[GH_ComponentParamServer
Events](../html/Events_T_Grasshopper_Kernel_GH_ComponentParamServer.htm
"GH_ComponentParamServer Events")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_ComponentParamServer Class  
  
---  
  
Wraps all members and functions needed for GH_Component to manage its input
and output parameters.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_ComponentParamServer  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_ComponentParamServer : GH_ISerializable, 
    	IEnumerable<IGH_Param>
    
    
    Public Class GH_ComponentParamServer
    	Implements GH_ISerializable, IEnumerable(Of IGH_Param)

The GH_ComponentParamServer type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Input](P_Grasshopper_Kernel_GH_ComponentParamServer_Input.htm)|  Gets or sets
the input list of parameters. Do not insert or remove parameters from this
list, use the dedicated functions instead.  
![Public property](../icons/pubproperty.gif)|
[InputWidth](P_Grasshopper_Kernel_GH_ComponentParamServer_InputWidth.htm)|
Gets the width of the largest input parameter.  
![Public property](../icons/pubproperty.gif)|
[OnlyTreeAndListParameters](P_Grasshopper_Kernel_GH_ComponentParamServer_OnlyTreeAndListParameters.htm)|
Returns True if every input parameter is either a list or a tree parameter.  
![Public property](../icons/pubproperty.gif)|
[OnlyTreeParameters](P_Grasshopper_Kernel_GH_ComponentParamServer_OnlyTreeParameters.htm)|
Returns True if every input parameter is a tree parameter.  
![Public property](../icons/pubproperty.gif)|
[Output](P_Grasshopper_Kernel_GH_ComponentParamServer_Output.htm)|  Gets or
sets the output list of parameters. Do not insert or remove parameters from
this list, use the dedicated functions instead.  
![Public property](../icons/pubproperty.gif)|
[OutputWidth](P_Grasshopper_Kernel_GH_ComponentParamServer_OutputWidth.htm)|
Gets the width of the largest output parameter.  
![Public property](../icons/pubproperty.gif)|
[Owner](P_Grasshopper_Kernel_GH_ComponentParamServer_Owner.htm)|  Gets the
owner component of this instance  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AccessCount](M_Grasshopper_Kernel_GH_ComponentParamServer_AccessCount.htm)|
Returns the total number of input parameters that match the access mask.  
![Public method](../icons/pubmethod.gif)|
[Clear](M_Grasshopper_Kernel_GH_ComponentParamServer_Clear.htm)|  Removes all
input and output parameters.  
![Public method](../icons/pubmethod.gif)|
[Clear(Boolean)](M_Grasshopper_Kernel_GH_ComponentParamServer_Clear_1.htm)|
Removes all input and output parameters.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateDuplicate](M_Grasshopper_Kernel_GH_ComponentParamServer_CreateDuplicate.htm)|
Attempts to duplicate a parameter. Attributes will be ignored. Warning! The
duplicate will have the same ID as the original!  
![Public method](../icons/pubmethod.gif)|
[EmitSyncObject](M_Grasshopper_Kernel_GH_ComponentParamServer_EmitSyncObject.htm)|
Create a synch object that stores a shallow representation of this server.
Cache this object if you're planning to make sweeping changes to this param-
server. Then, once you are finished call the Sync() function to perform
cleanup of removed parameters. This is a utility function and you can choose
to perform cleanup yourself.  
![Public method](../icons/pubmethod.gif)|
[Find](M_Grasshopper_Kernel_GH_ComponentParamServer_Find.htm)|  Find the
parameter that has the given InstanceGuid.  
![Public method](../icons/pubmethod.gif)|
[GetEnumerator](M_Grasshopper_Kernel_GH_ComponentParamServer_GetEnumerator.htm)|
Gets a customized enumerator which iterates over all (both input and output)
parameters.  
![Public method](../icons/pubmethod.gif)|
[GetHashCode](M_Grasshopper_Kernel_GH_ComponentParamServer_GetHashCode.htm)|
(Overrides
[ObjectGetHashCode](https://docs.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode).)  
![Public method](../icons/pubmethod.gif)|
[GetHashCode(GH_ParamHashFields)](M_Grasshopper_Kernel_GH_ComponentParamServer_GetHashCode_1.htm)|
Creates a SHA1 hash from the parameter data.  
![Public method](../icons/pubmethod.gif)|
[IndexOfInputParam(Guid)](M_Grasshopper_Kernel_GH_ComponentParamServer_IndexOfInputParam.htm)|
Finds the index of the input parameter that matches the specified search mask.  
![Public method](../icons/pubmethod.gif)|
[IndexOfInputParam(String)](M_Grasshopper_Kernel_GH_ComponentParamServer_IndexOfInputParam_1.htm)|
Finds the index of the input parameter that matches the specified search mask.  
![Public method](../icons/pubmethod.gif)|
[IndexOfOutputParam(Guid)](M_Grasshopper_Kernel_GH_ComponentParamServer_IndexOfOutputParam.htm)|
Finds the index of the output parameter that matches the specified search
mask.  
![Public method](../icons/pubmethod.gif)|
[IndexOfOutputParam(String)](M_Grasshopper_Kernel_GH_ComponentParamServer_IndexOfOutputParam_1.htm)|
Finds the index of the output parameter that matches the specified search
mask.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[InventUniqueNickname(String,
IEnumerableIGH_Param)](M_Grasshopper_Kernel_GH_ComponentParamServer_InventUniqueNickname.htm)|
Create a new, unique parameter nickname.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[InventUniqueNickname(String,
IEnumerableString)](M_Grasshopper_Kernel_GH_ComponentParamServer_InventUniqueNickname_1.htm)|
Create a new, unique parameter nickname.  
![Public method](../icons/pubmethod.gif)|
[IsInputParam](M_Grasshopper_Kernel_GH_ComponentParamServer_IsInputParam.htm)|
Returns True if this parameter is an input child of the component  
![Public method](../icons/pubmethod.gif)|
[IsOutputParam](M_Grasshopper_Kernel_GH_ComponentParamServer_IsOutputParam.htm)|
Returns True if this parameter is an output child of the component  
![Public method](../icons/pubmethod.gif)|
[IsParam](M_Grasshopper_Kernel_GH_ComponentParamServer_IsParam.htm)|  Returns
True if this parameter is a child of the component  
![Public method](../icons/pubmethod.gif)|
[OnParametersChanged](M_Grasshopper_Kernel_GH_ComponentParamServer_OnParametersChanged.htm)|
Call this function when you change input/output parameter lists or types. This
function will wipe all caches that are potentially invalid. PerformLayout on
the component attributes will be called.  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_GH_ComponentParamServer_Read.htm)|  Read all
parameter data from an IO archive.  
![Public method](../icons/pubmethod.gif)|
[RegisterInputParam(IGH_Param)](M_Grasshopper_Kernel_GH_ComponentParamServer_RegisterInputParam.htm)|
Add a parameter to the end of the input list.  
![Public method](../icons/pubmethod.gif)| [RegisterInputParam(IGH_Param,
Int32)](M_Grasshopper_Kernel_GH_ComponentParamServer_RegisterInputParam_1.htm)|
Add a parameter at the specific index of the input list.  
![Public method](../icons/pubmethod.gif)|
[RegisterOutputParam(IGH_Param)](M_Grasshopper_Kernel_GH_ComponentParamServer_RegisterOutputParam.htm)|
Add a parameter to the end of the output list.  
![Public method](../icons/pubmethod.gif)| [RegisterOutputParam(IGH_Param,
Int32)](M_Grasshopper_Kernel_GH_ComponentParamServer_RegisterOutputParam_1.htm)|
Add a parameter at the specific index of the output list.  
![Public method](../icons/pubmethod.gif)|
[RepairParamAssociations](M_Grasshopper_Kernel_GH_ComponentParamServer_RepairParamAssociations.htm)|
Makes sure all parameter attributes are a-ok. If you stick to regular
functions, you shouldn't have to call this.  
![Public method](../icons/pubmethod.gif)|
[RepairProxyParams](M_Grasshopper_Kernel_GH_ComponentParamServer_RepairProxyParams.htm)|
Attempt to fix all proxy params. Returns false if a single one fails.  
![Public method](../icons/pubmethod.gif)|
[SortInput(Double)](M_Grasshopper_Kernel_GH_ComponentParamServer_SortInput.htm)|
Sort the input parameter order based on a numeric key array.  
![Public method](../icons/pubmethod.gif)|
[SortInput(Int32)](M_Grasshopper_Kernel_GH_ComponentParamServer_SortInput_1.htm)|
Sort the input parameter order based on a numeric key array.  
![Public method](../icons/pubmethod.gif)|
[SortInput(Single)](M_Grasshopper_Kernel_GH_ComponentParamServer_SortInput_2.htm)|
Sort the input parameter order based on a numeric key array.  
![Public method](../icons/pubmethod.gif)|
[SortOutput(Double)](M_Grasshopper_Kernel_GH_ComponentParamServer_SortOutput.htm)|
Sort the input parameter order based on a numeric key array.  
![Public method](../icons/pubmethod.gif)|
[SortOutput(Int32)](M_Grasshopper_Kernel_GH_ComponentParamServer_SortOutput_1.htm)|
Sort the output parameter order based on a numeric key array.  
![Public method](../icons/pubmethod.gif)|
[SortOutput(Single)](M_Grasshopper_Kernel_GH_ComponentParamServer_SortOutput_2.htm)|
Sort the output parameter order based on a numeric key array.  
![Public method](../icons/pubmethod.gif)|
[Sync(GH_ComponentParamServerIGH_SyncObject)](M_Grasshopper_Kernel_GH_ComponentParamServer_Sync.htm)|
Sync changes from a prerecorded state. All param references in the sync object
which are no longer present in the current server will be properly deleted.
The sync object will be reset in the process, so you can only call this
function with a specific Sync object once.  
![Public method](../icons/pubmethod.gif)|
[Sync(Object)](M_Grasshopper_Kernel_GH_ComponentParamServer_Sync_2.htm)|  Sync
changes from a prerecorded state. All param references in the sync object
which are no longer present in the current server will be properly deleted.
The sync object will be reset in the process, so you can only call this
function with a specific Sync object once.  
![Public method](../icons/pubmethod.gif)|
[Sync(GH_ComponentParamServerIGH_SyncObject,
Int32)](M_Grasshopper_Kernel_GH_ComponentParamServer_Sync_1.htm)|  Sync
changes from a prerecorded state. All param references in the sync object
which are no longer present in the current server will be properly deleted.
The sync object will be reset in the process, so you can only call this
function with a specific Sync object once.  
![Public method](../icons/pubmethod.gif)|
[UnregisterInputParameter(IGH_Param)](M_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterInputParameter.htm)|
Removes the specified parameter from this component.  
![Public method](../icons/pubmethod.gif)| [UnregisterInputParameter(IGH_Param,
Boolean)](M_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterInputParameter_1.htm)|
Removes the specified parameter from this component.  
![Public method](../icons/pubmethod.gif)|
[UnregisterOutputParameter(IGH_Param)](M_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterOutputParameter.htm)|
Removes the specified parameter from this component.  
![Public method](../icons/pubmethod.gif)|
[UnregisterOutputParameter(IGH_Param,
Boolean)](M_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterOutputParameter_1.htm)|
Removes the specified parameter from this component.  
![Public method](../icons/pubmethod.gif)|
[UnregisterParameter(IGH_Param)](M_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterParameter.htm)|
Removes the specified parameter from this component.  
![Public method](../icons/pubmethod.gif)| [UnregisterParameter(IGH_Param,
Boolean)](M_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterParameter_1.htm)|
Removes the specified parameter from this component.  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_GH_ComponentParamServer_Write.htm)|  Write all
parameter data to an IO archive.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[WriteParamHashData](M_Grasshopper_Kernel_GH_ComponentParamServer_WriteParamHashData.htm)|
Write parameter data to a binary writer.  
Top

![](../icons/SectionExpanded.png)Events

| Name| Description  
---|---|---  
![Public event](../icons/pubevent.gif)|
[ParameterChanged](E_Grasshopper_Kernel_GH_ComponentParamServer_ParameterChanged.htm)|
Raised whenever there is a change to any parameter. If you only care about
NickName or Source changes, handle the ParameterNickNameChanged or
ParameterSourcesChanged events instead.  
![Public event](../icons/pubevent.gif)|
[ParameterNickNameChanged](E_Grasshopper_Kernel_GH_ComponentParamServer_ParameterNickNameChanged.htm)|
Raised whenever a parameter nickname change is accepted.  
![Public event](../icons/pubevent.gif)|
[ParameterSourcesChanged](E_Grasshopper_Kernel_GH_ComponentParamServer_ParameterSourcesChanged.htm)|
Raised whenever the source list of an input parameter is changed.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

