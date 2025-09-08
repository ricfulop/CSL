---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_IGH_Param.htm
scraped_at: 2025-09-08T16:18:36.865421
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH_Param Interface](../html/T_Grasshopper_Kernel_IGH_Param.htm "IGH_Param
Interface")

[IGH_Param Properties](../html/Properties_T_Grasshopper_Kernel_IGH_Param.htm
"IGH_Param Properties")

[IGH_Param Methods](../html/Methods_T_Grasshopper_Kernel_IGH_Param.htm
"IGH_Param Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_Param Interface  
  
---  
  
Base interface for all Parameter types in Grasshopper. Do not implement this
interface from scratch, derive from GH_Param or GH_PersistentParam instead.

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_Param : IGH_ActiveObject
    
    
    Public Interface IGH_Param
    	Inherits IGH_ActiveObject

The IGH_Param type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Access](P_Grasshopper_Kernel_IGH_Param_Access.htm)|  Gets or sets the Access
level for this parameter.  
![Public property](../icons/pubproperty.gif)|
[DataMapping](P_Grasshopper_Kernel_IGH_Param_DataMapping.htm)|  Gets or sets
the data mapping of this Parameter.  
![Public property](../icons/pubproperty.gif)|
[DataType](P_Grasshopper_Kernel_IGH_Param_DataType.htm)|  Gets the type of the
current data state.  
![Public property](../icons/pubproperty.gif)|
[HasProxySources](P_Grasshopper_Kernel_IGH_Param_HasProxySources.htm)|  Gets a
value indicating whether or not this parameter maintains proxy sources. Proxy
sources are used during file IO, when actual sources might not be available
yet. Once an IO operation has been completed there should be no more proxy
sources.  
![Public property](../icons/pubproperty.gif)|
[IsDataProvider](P_Grasshopper_Kernel_IGH_ActiveObject_IsDataProvider.htm)|
Gets whether or not this object is capable of emitting data.  (Inherited from
[IGH_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[Kind](P_Grasshopper_Kernel_IGH_Param_Kind.htm)|  Gets the parameter kind. The
kind is evaluated lazily and cached.  
![Public property](../icons/pubproperty.gif)|
[Locked](P_Grasshopper_Kernel_IGH_ActiveObject_Locked.htm)|  Gets or sets the
locked flag of this object. Locked objects are ignored during solutions.
(Inherited from
[IGH_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[MutableNickName](P_Grasshopper_Kernel_IGH_ActiveObject_MutableNickName.htm)|
Gets or sets a value that enables Nick name changes through the menu. The
default is TRUE.  (Inherited from
[IGH_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[Optional](P_Grasshopper_Kernel_IGH_Param_Optional.htm)|  Gets or sets whether
or not this parameter is considered optional by the owner component. Empty,
non-optional parameters prevent the component from being solved.  
![Public property](../icons/pubproperty.gif)|
[Phase](P_Grasshopper_Kernel_IGH_ActiveObject_Phase.htm)|  Gets the solution
phase in which this object is currently stuck.  (Inherited from
[IGH_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[ProcessorTime](P_Grasshopper_Kernel_IGH_ActiveObject_ProcessorTime.htm)|
Gets the most recent measured processor time.  (Inherited from
[IGH_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[ProxySourceCount](P_Grasshopper_Kernel_IGH_Param_ProxySourceCount.htm)|  Gets
the number of proxy sources for this parameter. Proxy sources are used during
file IO, when actual sources might not be available yet. Once an IO operation
has been completed there should be no more proxy sources.  
![Public property](../icons/pubproperty.gif)|
[Recipients](P_Grasshopper_Kernel_IGH_Param_Recipients.htm)|  Gets a list of
all the recipients of this parameter. I.e. a recipient has this parameter as
one of the sources. The Recipient list is maintained by the parameter, do not
modify it yourself.  
![Public property](../icons/pubproperty.gif)|
[Reverse](P_Grasshopper_Kernel_IGH_Param_Reverse.htm)|  Gets or sets the data
reverse modifier of this parameter.  
![Public property](../icons/pubproperty.gif)|
[RuntimeMessageLevel](P_Grasshopper_Kernel_IGH_ActiveObject_RuntimeMessageLevel.htm)|
Gets the worst-case level of all messages. I.e. if only warnings have been
recorded, the level will be ::warning. If even a single error exists, the
level will be ::error.  (Inherited from
[IGH_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[Simplify](P_Grasshopper_Kernel_IGH_Param_Simplify.htm)|  Gets or sets the
simplify modifier for this parameter.  
![Public property](../icons/pubproperty.gif)|
[SourceCount](P_Grasshopper_Kernel_IGH_Param_SourceCount.htm)|  Gets the
number of sources for this parameter.  
![Public property](../icons/pubproperty.gif)|
[Sources](P_Grasshopper_Kernel_IGH_Param_Sources.htm)|  Gets a list of source
parameters. Do not modify this list, if you wish to add or remove sources, use
dedicated functions like AddSource() and RemoveSource instead.  
![Public property](../icons/pubproperty.gif)|
[StateTags](P_Grasshopper_Kernel_IGH_Param_StateTags.htm)|  Gets all the
StateTags that are associated with this parameter. A state tag is a visual
feedback icon that represents specific internal settings.  
![Public property](../icons/pubproperty.gif)|
[Type](P_Grasshopper_Kernel_IGH_Param_Type.htm)|  Gets the Framework Type
descriptor for the stored Data.  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_IGH_Param_TypeName.htm)|  Gets a human
readable description of the data stored in this parameter.  
![Public property](../icons/pubproperty.gif)|
[VolatileData](P_Grasshopper_Kernel_IGH_Param_VolatileData.htm)|  Gets the
instance of the volatile data tree stored in this parameter.  
![Public property](../icons/pubproperty.gif)|
[VolatileDataCount](P_Grasshopper_Kernel_IGH_Param_VolatileDataCount.htm)|
Gets the total number of volatile data items stored in this parameter.  
![Public property](../icons/pubproperty.gif)|
[WireDisplay](P_Grasshopper_Kernel_IGH_Param_WireDisplay.htm)|  Gets or sets
the wire display style for this parameter. Wire display only affects the wires
connected to the parameter input.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AddRuntimeMessage](M_Grasshopper_Kernel_IGH_ActiveObject_AddRuntimeMessage.htm)|
Add a new message to this object. Valid message type flags are Warning and
Error. If the Message string is empty or zero-length no message is added.
(Inherited from
[IGH_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[AddSource(IGH_Param)](M_Grasshopper_Kernel_IGH_Param_AddSource.htm)|  Append
a new Source parameter to the end of the Sources list. Sources provide this
parameter with data at runtime.  
![Public method](../icons/pubmethod.gif)| [AddSource(IGH_Param,
Int32)](M_Grasshopper_Kernel_IGH_Param_AddSource_1.htm)|  Insert a new Source
parameter into the Sources list. Sources provide this parameter with data at
runtime.  
![Public method](../icons/pubmethod.gif)|
[AddVolatileData](M_Grasshopper_Kernel_IGH_Param_AddVolatileData.htm)|
Inserts an item of volatile data into the data structure.  
![Public method](../icons/pubmethod.gif)|
[AddVolatileDataList](M_Grasshopper_Kernel_IGH_Param_AddVolatileDataList.htm)|
Inserts a list of items into the data structure.  
![Public method](../icons/pubmethod.gif)|
[AddVolatileDataTree](M_Grasshopper_Kernel_IGH_Param_AddVolatileDataTree.htm)|
Insert an entire data tree into this parameter.  
![Public method](../icons/pubmethod.gif)|
[ClearData](M_Grasshopper_Kernel_IGH_ActiveObject_ClearData.htm)|  This
function is called whenever the object needs to clear all solution data. This
usually amounts to wiping volatile caches and messages. This function will not
affect any other objects, but it will set the Phase flag to Blank  (Inherited
from [IGH_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[ClearProxySources](M_Grasshopper_Kernel_IGH_Param_ClearProxySources.htm)|
Remove all proxy sources without attempting to relink them.  
![Public method](../icons/pubmethod.gif)|
[ClearRuntimeMessages](M_Grasshopper_Kernel_IGH_ActiveObject_ClearRuntimeMessages.htm)|
Clear all message lists.  (Inherited from
[IGH_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[CollectData](M_Grasshopper_Kernel_IGH_ActiveObject_CollectData.htm)|  This
function is called whenever the object is required to collect all data. Either
from Persistent records, from source params or whatever. This step is only
performed if the phase flag is Blank or Failed. Upon completion, the phase
flag will be set to Collected  (Inherited from
[IGH_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[ComputeData](M_Grasshopper_Kernel_IGH_ActiveObject_ComputeData.htm)|  This
function is called whenever the object is required to generate new data. This
step is only performed by some objects and only when the Phase flag is
Collected. Upon completion, the Phase will be Computed. If this object throws
exceptions, it is the responsibility of the caller to set the Phase flag to
Failed.  (Inherited from
[IGH_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[CreateProxySources](M_Grasshopper_Kernel_IGH_Param_CreateProxySources.htm)|
Convert all proper source parameters into proxy sources.  
![Public method](../icons/pubmethod.gif)|
[DependsOn](M_Grasshopper_Kernel_IGH_ActiveObject_DependsOn.htm)|  Solve the
inheritance relationship between this object and a potential parental object.
(Inherited from
[IGH_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[RegisterRemoteIDs](M_Grasshopper_Kernel_IGH_ActiveObject_RegisterRemoteIDs.htm)|
If this object depends on Rhino Objects, you must register the UUIDs of those
objects. Failure to do so will result in faulty event handling.  (Inherited
from [IGH_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[RelinkProxySources](M_Grasshopper_Kernel_IGH_Param_RelinkProxySources.htm)|
Attempt to replace all proxy sources with real sources. Proxy sources are used
during file IO, when actual sources might not be available yet. Once an IO
operation has been completed there should be no more proxy sources.  
![Public method](../icons/pubmethod.gif)|
[RemoveAllSources](M_Grasshopper_Kernel_IGH_Param_RemoveAllSources.htm)|
Remove all sources from this parameter.  
![Public method](../icons/pubmethod.gif)|
[RemoveEffects](M_Grasshopper_Kernel_IGH_Param_RemoveEffects.htm)|  Remove all
post-process effects.  
![Public method](../icons/pubmethod.gif)|
[RemoveSource(Guid)](M_Grasshopper_Kernel_IGH_Param_RemoveSource_1.htm)|
Remove the specified source from this parameter.  
![Public method](../icons/pubmethod.gif)|
[RemoveSource(IGH_Param)](M_Grasshopper_Kernel_IGH_Param_RemoveSource.htm)|
Remove the specified source from this parameter.  
![Public method](../icons/pubmethod.gif)| [ReplaceSource(Guid,
IGH_Param)](M_Grasshopper_Kernel_IGH_Param_ReplaceSource_1.htm)|  Replace an
existing source with a new one. If the old_source does not exist in this
parameter, nothing happens.  
![Public method](../icons/pubmethod.gif)| [ReplaceSource(IGH_Param,
IGH_Param)](M_Grasshopper_Kernel_IGH_Param_ReplaceSource.htm)|  Replace an
existing source with a new one. If the old_source does not exist in this
parameter, nothing happens.  
![Public method](../icons/pubmethod.gif)|
[RuntimeMessages](M_Grasshopper_Kernel_IGH_ActiveObject_RuntimeMessages.htm)|
Gets the list of cached runtime messages that were recorded during solver-time
processes.  (Inherited from
[IGH_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[SDKCompliancy](M_Grasshopper_Kernel_IGH_ActiveObject_SDKCompliancy.htm)|
Test whether this object is compliant with a given Rhino version.  (Inherited
from [IGH_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

