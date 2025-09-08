---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_IGH_Component.htm
scraped_at: 2025-09-08T16:18:17.774660
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH_Component Interface](../html/T_Grasshopper_Kernel_IGH_Component.htm
"IGH_Component Interface")

[IGH_Component
Properties](../html/Properties_T_Grasshopper_Kernel_IGH_Component.htm
"IGH_Component Properties")

[IGH_Component Methods](../html/Methods_T_Grasshopper_Kernel_IGH_Component.htm
"IGH_Component Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_Component Interface  
  
---  
  
Base interface for all GH_Component types. Do not implement this interface
from scratch, inherit from GH_Component instead.

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_Component : IGH_ActiveObject, 
    	IGH_PreviewObject, IGH_BakeAwareObject
    
    
    Public Interface IGH_Component
    	Inherits IGH_ActiveObject, IGH_PreviewObject, IGH_BakeAwareObject

The IGH_Component type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[ClippingBox](P_Grasshopper_Kernel_IGH_PreviewObject_ClippingBox.htm)|  Gets
the clipping box for this object. The clipping box is typically the union of
the boundingboxes of all the geometry that is drawn by this object.
(Inherited from
[IGH_PreviewObject](T_Grasshopper_Kernel_IGH_PreviewObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[Hidden](P_Grasshopper_Kernel_IGH_PreviewObject_Hidden.htm)|  Gets or sets a
value indicating whether or not this object is currently drawing preview
flags.  (Inherited from
[IGH_PreviewObject](T_Grasshopper_Kernel_IGH_PreviewObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[InConstructor](P_Grasshopper_Kernel_IGH_Component_InConstructor.htm)|  Gets
the constructor flag for this instance. If InConstructor = True, it means the
component is still registering parameters and the layout is not yet complete.  
![Public property](../icons/pubproperty.gif)|
[IsBakeCapable](P_Grasshopper_Kernel_IGH_BakeAwareObject_IsBakeCapable.htm)|
Gets a value indicating whether or not the object can potentially Bake data in
its current state.  (Inherited from
[IGH_BakeAwareObject](T_Grasshopper_Kernel_IGH_BakeAwareObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsDataProvider](P_Grasshopper_Kernel_IGH_ActiveObject_IsDataProvider.htm)|
Gets whether or not this object is capable of emitting data.  (Inherited from
[IGH_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsPreviewCapable](P_Grasshopper_Kernel_IGH_PreviewObject_IsPreviewCapable.htm)|
Gets a value indicating whether or not this object (in its current state) can
draw geometric previews at all.  (Inherited from
[IGH_PreviewObject](T_Grasshopper_Kernel_IGH_PreviewObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValidMasterParameterIndex](P_Grasshopper_Kernel_IGH_Component_IsValidMasterParameterIndex.htm)|
Gets whether the MasterParameterIndex property identifies a valid parameter.  
![Public property](../icons/pubproperty.gif)|
[Locked](P_Grasshopper_Kernel_IGH_ActiveObject_Locked.htm)|  Gets or sets the
locked flag of this object. Locked objects are ignored during solutions.
(Inherited from
[IGH_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[MasterParameterIndex](P_Grasshopper_Kernel_IGH_Component_MasterParameterIndex.htm)|
Gets or sets the master parameter index override. Negative indices or indices
larger than or equal to the input parameter count will be ignored and regular
master parameter detection will kick in.  
![Public property](../icons/pubproperty.gif)|
[Message](P_Grasshopper_Kernel_IGH_Component_Message.htm)|  Gets or sets a
custom message to be displayed underneath the component.  
![Public property](../icons/pubproperty.gif)|
[MutableNickName](P_Grasshopper_Kernel_IGH_ActiveObject_MutableNickName.htm)|
Gets or sets a value that enables Nick name changes through the menu. The
default is TRUE.  (Inherited from
[IGH_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[Params](P_Grasshopper_Kernel_IGH_Component_Params.htm)|  Gets the Params
object that managed input and output parameters.  
![Public property](../icons/pubproperty.gif)|
[Phase](P_Grasshopper_Kernel_IGH_ActiveObject_Phase.htm)|  Gets the solution
phase in which this object is currently stuck.  (Inherited from
[IGH_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[ProcessorTime](P_Grasshopper_Kernel_IGH_ActiveObject_ProcessorTime.htm)|
Gets the most recent measured processor time.  (Inherited from
[IGH_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[RunCount](P_Grasshopper_Kernel_IGH_Component_RunCount.htm)|  Gets a value
indicating how many times the SolveInstance method was called on this
component during the last solution. This property will return -1 if no valid
runcount is available.  
![Public property](../icons/pubproperty.gif)|
[RuntimeMessageLevel](P_Grasshopper_Kernel_IGH_ActiveObject_RuntimeMessageLevel.htm)|
Gets the worst-case level of all messages. I.e. if only warnings have been
recorded, the level will be ::warning. If even a single error exists, the
level will be ::error.  (Inherited from
[IGH_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).)  
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
![Public method](../icons/pubmethod.gif)| [BakeGeometry(RhinoDoc,
ListGuid)](M_Grasshopper_Kernel_IGH_BakeAwareObject_BakeGeometry_1.htm)|  Bake
all the goemetry in this object in the given Rhino document.  (Inherited from
[IGH_BakeAwareObject](T_Grasshopper_Kernel_IGH_BakeAwareObject.htm).)  
![Public method](../icons/pubmethod.gif)| [BakeGeometry(RhinoDoc,
ObjectAttributes,
ListGuid)](M_Grasshopper_Kernel_IGH_BakeAwareObject_BakeGeometry.htm)|  Bake
all the goemetry in this object in the given Rhino document.  (Inherited from
[IGH_BakeAwareObject](T_Grasshopper_Kernel_IGH_BakeAwareObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[ClearData](M_Grasshopper_Kernel_IGH_ActiveObject_ClearData.htm)|  This
function is called whenever the object needs to clear all solution data. This
usually amounts to wiping volatile caches and messages. This function will not
affect any other objects, but it will set the Phase flag to Blank  (Inherited
from [IGH_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).)  
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
[DependsOn](M_Grasshopper_Kernel_IGH_ActiveObject_DependsOn.htm)|  Solve the
inheritance relationship between this object and a potential parental object.
(Inherited from
[IGH_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[DrawViewportMeshes](M_Grasshopper_Kernel_IGH_PreviewObject_DrawViewportMeshes.htm)|
Implement this function to draw all shaded meshes. If the viewport does not
support shading, this function will not be called.  (Inherited from
[IGH_PreviewObject](T_Grasshopper_Kernel_IGH_PreviewObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[DrawViewportWires](M_Grasshopper_Kernel_IGH_PreviewObject_DrawViewportWires.htm)|
Implement this function to draw all wire and point geometry previews.
(Inherited from
[IGH_PreviewObject](T_Grasshopper_Kernel_IGH_PreviewObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[RegisterRemoteIDs](M_Grasshopper_Kernel_IGH_ActiveObject_RegisterRemoteIDs.htm)|
If this object depends on Rhino Objects, you must register the UUIDs of those
objects. Failure to do so will result in faulty event handling.  (Inherited
from [IGH_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).)  
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

