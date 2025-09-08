---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_Render_Params_Param_ModelRenderMaterial.htm
scraped_at: 2025-09-08T16:24:53.502885
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros.Render.Params](../html/N_Grasshopper_Rhinoceros_Render_Params.htm
"Grasshopper.Rhinoceros.Render.Params")

[Param_ModelRenderMaterial
Class](../html/T_Grasshopper_Rhinoceros_Render_Params_Param_ModelRenderMaterial.htm
"Param_ModelRenderMaterial Class")

[Param_ModelRenderMaterial Constructor
](../html/M_Grasshopper_Rhinoceros_Render_Params_Param_ModelRenderMaterial__ctor.htm
"Param_ModelRenderMaterial Constructor ")

[Param_ModelRenderMaterial
Properties](../html/Properties_T_Grasshopper_Rhinoceros_Render_Params_Param_ModelRenderMaterial.htm
"Param_ModelRenderMaterial Properties")

[Param_ModelRenderMaterial
Methods](../html/Methods_T_Grasshopper_Rhinoceros_Render_Params_Param_ModelRenderMaterial.htm
"Param_ModelRenderMaterial Methods")

[Param_ModelRenderMaterial
Events](../html/Events_T_Grasshopper_Rhinoceros_Render_Params_Param_ModelRenderMaterial.htm
"Param_ModelRenderMaterial Events")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# Param_ModelRenderMaterial Class  
  
---  
  
![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.KernelGH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm)  
[Grasshopper.KernelGH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm)  
[Grasshopper.KernelGH_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm)  
[Grasshopper.KernelGH_Param](T_Grasshopper_Kernel_GH_Param_1.htm)[ModelRenderMaterial](T_Grasshopper_Rhinoceros_Render_ModelRenderMaterial.htm)  
[Grasshopper.KernelGH_PersistentParam](T_Grasshopper_Kernel_GH_PersistentParam_1.htm)[ModelRenderMaterial](T_Grasshopper_Rhinoceros_Render_ModelRenderMaterial.htm)  
[Grasshopper.KernelGH_PersistentReferenceParam](T_Grasshopper_Kernel_GH_PersistentReferenceParam_1.htm)[ModelRenderMaterial](T_Grasshopper_Rhinoceros_Render_ModelRenderMaterial.htm)  
[Grasshopper.Rhinoceros.ParamsModelContentParam](T_Grasshopper_Rhinoceros_Params_ModelContentParam_1.htm)[ModelRenderMaterial](T_Grasshopper_Rhinoceros_Render_ModelRenderMaterial.htm)  
Grasshopper.Rhinoceros.Render.ParamsParam_ModelRenderMaterial  

**Namespace:**
[Grasshopper.Rhinoceros.Render.Params](N_Grasshopper_Rhinoceros_Render_Params.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class Param_ModelRenderMaterial : ModelContentParam<ModelRenderMaterial>
    
    
    Public NotInheritable Class Param_ModelRenderMaterial
    	Inherits ModelContentParam(Of ModelRenderMaterial)

The Param_ModelRenderMaterial type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Param_ModelRenderMaterial](M_Grasshopper_Rhinoceros_Render_Params_Param_ModelRenderMaterial__ctor.htm)|
Initializes a new instance of the Param_ModelRenderMaterial class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Access](P_Grasshopper_Kernel_GH_Param_1_Access.htm)|  Gets or sets the Access
level for this parameter.  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[Attributes](P_Grasshopper_Kernel_GH_DocumentObject_Attributes.htm)|  Gets or
sets the attributes that are associated with this object. Only set custom
attributes if you know what you are doing.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[Category](P_Grasshopper_Kernel_GH_InstanceDescription_Category.htm)|  Gets or
sets the Category in which this object belongs. If HasCategory() returns
false, this field has no meaning.  (Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[ComponentGuid](P_Grasshopper_Rhinoceros_Render_Params_Param_ModelRenderMaterial_ComponentGuid.htm)|
(Overrides
[GH_DocumentObjectComponentGuid](P_Grasshopper_Kernel_GH_DocumentObject_ComponentGuid.htm).)  
![Public property](../icons/pubproperty.gif)|
[DataMapping](P_Grasshopper_Kernel_GH_Param_1_DataMapping.htm)|  Gets or sets
the data mapping of this Parameter.  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[DataType](P_Grasshopper_Kernel_GH_PersistentParam_1_DataType.htm)|  Gets the
type of data stored in this parameter.  (Inherited from
[GH_PersistentParamT](T_Grasshopper_Kernel_GH_PersistentParam_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[Description](P_Grasshopper_Kernel_GH_InstanceDescription_Description.htm)|
Gets or sets the description of the object. This field typically remains fixed
during the lifetime of an object.  (Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[Exposure](P_Grasshopper_Rhinoceros_Render_Params_Param_ModelRenderMaterial_Exposure.htm)|
(Overrides
[GH_DocumentObjectExposure](P_Grasshopper_Kernel_GH_DocumentObject_Exposure.htm).)  
![Public property](../icons/pubproperty.gif)|
[HasCategory](P_Grasshopper_Kernel_GH_InstanceDescription_HasCategory.htm)|
Gets whether or not the Category field has been set.  (Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[HasProxySources](P_Grasshopper_Kernel_GH_Param_1_HasProxySources.htm)|  Gets
a value indicating whether or not this parameter maintains proxy sources.
Proxy sources are used during file IO, when actual sources might not be
available yet. Once an IO operation has been completed there should be no more
proxy sources.  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[HasSubCategory](P_Grasshopper_Kernel_GH_InstanceDescription_HasSubCategory.htm)|
Gets whether or not the SubCategory field has been set.  (Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[Icon_24x24](P_Grasshopper_Kernel_GH_DocumentObject_Icon_24x24.htm)|  The icon
associated with this object.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[Icon_24x24_Locked](P_Grasshopper_Kernel_GH_DocumentObject_Icon_24x24_Locked.htm)|
The greyscale icon of this object.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[IconCapableUI](P_Grasshopper_Kernel_GH_ActiveObject_IconCapableUI.htm)|  By
default the NickName menu item supports the Icon Mode override toggle. If your
UI is not capable of displaying icons, then override this property and return
False.  (Inherited from
[GH_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[IconDisplayMode](P_Grasshopper_Kernel_GH_DocumentObject_IconDisplayMode.htm)|
Gets the current display mode of the object.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[InstanceDescription](P_Grasshopper_Kernel_GH_Param_1_InstanceDescription.htm)|
Gets the description of this instance. The default description is about the
amount and source of the local values.  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[InstanceGuid](P_Grasshopper_Kernel_GH_InstanceDescription_InstanceGuid.htm)|
Gets the ID of this runtime instance.  (Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsBakeCapable](P_Grasshopper_Rhinoceros_Params_ModelContentParam_1_IsBakeCapable.htm)|
(Inherited from
[ModelContentParamT](T_Grasshopper_Rhinoceros_Params_ModelContentParam_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsDataProvider](P_Grasshopper_Kernel_GH_Param_1_IsDataProvider.htm)|
(Inherited from [GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsPrincipal](P_Grasshopper_Kernel_GH_Param_1_IsPrincipal.htm)|  Gets whether
this parameter is a principal parameter. Principal parameters are maintained
by components and are not part of the IGH_Param interface.  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[Keywords](P_Grasshopper_Kernel_GH_InstanceDescription_Keywords.htm)|  Gets a
list of additional keywords that describe the object. Typically this list is
empty but you can override this property to aid in object searches.
(Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[Kind](P_Grasshopper_Kernel_GH_Param_1_Kind.htm)|  Gets the parameter kind.
The kind is evaluated lazily and cached.  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[Locked](P_Grasshopper_Kernel_GH_ActiveObject_Locked.htm)|  Gets or sets the
enabled flag of this object. Disabled objects are ignored during solutions.
(Inherited from [GH_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[MutableNickName](P_Grasshopper_Kernel_GH_ActiveObject_MutableNickName.htm)|
Gets or sets a value that enables Nick name changes through the menu. The
default is TRUE.  (Inherited from
[GH_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[Name](P_Grasshopper_Kernel_GH_InstanceDescription_Name.htm)|  Gets or sets
the name of the object. This field typically remains fixed during the lifetime
of an object.  (Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[NickName](P_Grasshopper_Kernel_GH_InstanceDescription_NickName.htm)|  Gets or
sets the nickname of the object. This field can be changed by the user.
(Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[Obsolete](P_Grasshopper_Kernel_GH_DocumentObject_Obsolete.htm)|  Gets whether
this object is obsolete. Default implementation returns true if the class name
contains the string "OBSOLETE" or if this class has been decorated with the
ObsoleteAttribute. You are free to override this if you want, but I suggest
adding the ObsoleteAttribute instead.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[Optional](P_Grasshopper_Kernel_GH_Param_1_Optional.htm)|  Gets or sets
whether or not this parameter is considered optional by the owner component.
Empty, non-optional parameters prevent the component from being solved.
(Inherited from [GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[PersistentData](P_Grasshopper_Kernel_GH_PersistentParam_1_PersistentData.htm)|
Gets the persistent data stored in this parameter. If you modify the
persistent data, be sure to call the:
OnObjectChanged(GH_ObjectEventType.PersistentData) event.  (Inherited from
[GH_PersistentParamT](T_Grasshopper_Kernel_GH_PersistentParam_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[PersistentDataCount](P_Grasshopper_Kernel_GH_PersistentParam_1_PersistentDataCount.htm)|
Gets the number of persistent data items stored in this parameter.  (Inherited
from [GH_PersistentParamT](T_Grasshopper_Kernel_GH_PersistentParam_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[Phase](P_Grasshopper_Kernel_GH_ActiveObject_Phase.htm)|  Gets or sets the
solution phase this object is currenly in.  (Inherited from
[GH_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[ProcessorTime](P_Grasshopper_Kernel_GH_Param_1_ProcessorTime.htm)|
(Inherited from [GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[ProxySourceCount](P_Grasshopper_Kernel_GH_Param_1_ProxySourceCount.htm)|
Gets the number of proxy sources for this parameter. Proxy sources are used
during file IO, when actual sources might not be available yet. Once an IO
operation has been completed there should be no more proxy sources.
(Inherited from [GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[Recipients](P_Grasshopper_Kernel_GH_Param_1_Recipients.htm)|  Gets a list of
all the recipients of this parameter. I.e. a recipient has this parameter as
one of the sources. The Recipient list is maintained by the parameter, do not
modify it yourself.  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[Reverse](P_Grasshopper_Kernel_GH_Param_1_Reverse.htm)|  Gets or sets the data
reverse modifier of this parameter.  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[RuntimeMessageLevel](P_Grasshopper_Kernel_GH_ActiveObject_RuntimeMessageLevel.htm)|
Returns the worst case flag for the current object If the object contains at
least 1 error, the result is Error.If the object contains at least 1 warning,
the result is Warning.If the object contains at least 1 message, the result is
Remark.If the object contains no errors, no warnings and no messages, the
result is Blank. (Inherited from
[GH_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[Simplify](P_Grasshopper_Kernel_GH_Param_1_Simplify.htm)|  Gets or sets the
simplify modifier for this parameter.  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[SourceCount](P_Grasshopper_Kernel_GH_Param_1_SourceCount.htm)|  Gets the
number of sources for this parameter.  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[Sources](P_Grasshopper_Kernel_GH_Param_1_Sources.htm)|  Gets a list of source
parameters. Do not modify this list, if you wish to add or remove sources, use
dedicated functions like AddSource() and RemoveSource() instead.  (Inherited
from [GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[StateTags](P_Grasshopper_Kernel_GH_Param_1_StateTags.htm)|  Gets all the
StateTags that are associated with this parameter. A state tag is a visual
feedback icon that represents specific internal settings.  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[SubCategory](P_Grasshopper_Kernel_GH_InstanceDescription_SubCategory.htm)|
Gets or sets the SubCategory in which this object belongs. If HasSubCategory()
returns false, this field has no meaning.  (Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[Type](P_Grasshopper_Kernel_GH_Param_1_Type.htm)|  Gets the Framework Type
descriptor for the stored Data.  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_GH_PersistentReferenceParam_1_TypeName.htm)|
(Inherited from
[GH_PersistentReferenceParamT](T_Grasshopper_Kernel_GH_PersistentReferenceParam_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[VolatileData](P_Grasshopper_Kernel_GH_Param_1_VolatileData.htm)|  (Inherited
from [GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[VolatileDataCount](P_Grasshopper_Kernel_GH_Param_1_VolatileDataCount.htm)|
(Inherited from [GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[WireDisplay](P_Grasshopper_Kernel_GH_Param_1_WireDisplay.htm)|  Gets or sets
the wire display style for this parameter. Wire display only affects the wires
connected to the parameter input.  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AddedToDocument](M_Grasshopper_Kernel_GH_DocumentObject_AddedToDocument.htm)|
This method will be called when an object is added to a document. Override
this method if you want to handle such events.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[AddRuntimeMessage](M_Grasshopper_Kernel_GH_ActiveObject_AddRuntimeMessage.htm)|
Add a new message to this object. Valid message type flags are Warning and
Error. If the Message string is empty or zero-length no message is added.
(Inherited from [GH_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[AddSource(IGH_Param)](M_Grasshopper_Kernel_GH_Param_1_AddSource.htm)|  Append
a new Source parameter to the end of the Sources list. Sources provide this
parameter with data at runtime.  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public method](../icons/pubmethod.gif)| [AddSource(IGH_Param,
Int32)](M_Grasshopper_Kernel_GH_Param_1_AddSource_1.htm)|  Insert a new Source
parameter into the Sources list. Sources provide this parameter with data at
runtime.  (Inherited from [GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public method](../icons/pubmethod.gif)| [AddVolatileData(GH_Path, Int32,
T)](M_Grasshopper_Kernel_GH_Param_1_AddVolatileData_1.htm)|  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public method](../icons/pubmethod.gif)| [AddVolatileData(GH_Path, Int32,
Object)](M_Grasshopper_Kernel_GH_Param_1_AddVolatileData.htm)|  Inserts an
item of volatile data into the data structure.  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public method](../icons/pubmethod.gif)| [AddVolatileDataList(GH_Path,
ListT)](M_Grasshopper_Kernel_GH_Param_1_AddVolatileDataList.htm)|  (Inherited
from [GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public method](../icons/pubmethod.gif)| [AddVolatileDataList(GH_Path,
IEnumerable)](M_Grasshopper_Kernel_GH_Param_1_AddVolatileDataList_1.htm)|
(Inherited from [GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[AddVolatileDataTree(GH_StructureT)](M_Grasshopper_Kernel_GH_Param_1_AddVolatileDataTree.htm)|
(Inherited from [GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[AddVolatileDataTree(IGH_Structure)](M_Grasshopper_Kernel_GH_Param_1_AddVolatileDataTree_1.htm)|
(Inherited from [GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[AppendAdditionalMenuItems](M_Grasshopper_Kernel_GH_PersistentParam_1_AppendAdditionalMenuItems.htm)|
(Inherited from
[GH_PersistentParamT](T_Grasshopper_Kernel_GH_PersistentParam_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[AppendMenuItems](M_Grasshopper_Kernel_GH_ActiveObject_AppendMenuItems.htm)|
This function is called when a context menu is about to be displayed. Override
it to set custom items. GH_ActiveObject will already populate the menu with
default items, if you merely wish to insert object-specific menu item,
consider overriding AppendAdditionalMenuItems instead.  (Inherited from
[GH_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).)  
![Public method](../icons/pubmethod.gif)| [BakeGeometry(RhinoDoc,
ListGuid)](M_Grasshopper_Rhinoceros_Params_ModelContentParam_1_BakeGeometry_1.htm)|
(Inherited from
[ModelContentParamT](T_Grasshopper_Rhinoceros_Params_ModelContentParam_1.htm).)  
![Public method](../icons/pubmethod.gif)| [BakeGeometry(RhinoDoc,
ObjectAttributes,
ListGuid)](M_Grasshopper_Rhinoceros_Params_ModelContentParam_1_BakeGeometry.htm)|
(Inherited from
[ModelContentParamT](T_Grasshopper_Rhinoceros_Params_ModelContentParam_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[ClearData](M_Grasshopper_Kernel_GH_PersistentReferenceParam_1_ClearData.htm)|
(Inherited from
[GH_PersistentReferenceParamT](T_Grasshopper_Kernel_GH_PersistentReferenceParam_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[ClearProxySources](M_Grasshopper_Kernel_GH_Param_1_ClearProxySources.htm)|
Remove all proxy sources without attempting to relink them.  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[ClearRuntimeMessages](M_Grasshopper_Kernel_GH_ActiveObject_ClearRuntimeMessages.htm)|
Destroy all warning and error lists  (Inherited from
[GH_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[CollectData](M_Grasshopper_Kernel_GH_Param_1_CollectData.htm)|  (Inherited
from [GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[ComputeData](M_Grasshopper_Kernel_GH_Param_1_ComputeData.htm)|  (Inherited
from [GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[CopyFrom](M_Grasshopper_Kernel_GH_InstanceDescription_CopyFrom.htm)|  Copy
all fields (except the instance ID) from another instance description.
(Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public method](../icons/pubmethod.gif)|
[CreateAttributes](M_Grasshopper_Kernel_GH_Param_1_CreateAttributes.htm)|
(Inherited from [GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[CreateProxySources](M_Grasshopper_Kernel_GH_Param_1_CreateProxySources.htm)|
Convert all proper source parameters into proxy sources.  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[DependsOn](M_Grasshopper_Kernel_GH_Param_1_DependsOn.htm)|  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[DocumentContextChanged](M_Grasshopper_Kernel_GH_DocumentObject_DocumentContextChanged.htm)|
This method will be called when the document that owns this object moves into
a different context.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[ExpirePreview](M_Grasshopper_Kernel_GH_DocumentObject_ExpirePreview.htm)|
Call this function when you suspect that the preview has expired for this
object. This will cause the display cache to be eradicated.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[ExpireSolution](M_Grasshopper_Kernel_GH_ActiveObject_ExpireSolution.htm)|
Informs the document that owns this object that the solution has expired. The
current object will be set to BLANK as a result. This method is recursive, it
will also expire any and all objects which depend on this object. If you want
a less destructive expiration, consider using ClearData(). If this object is
already Blank, you should consider not expiring it.  (Inherited from
[GH_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[ExpireSolutionTopLevel](M_Grasshopper_Kernel_GH_Param_1_ExpireSolutionTopLevel.htm)|
Invoke the Expiresolution(bool) method on the toplevel object.  (Inherited
from [GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[IsolateObject](M_Grasshopper_Kernel_GH_Param_1_IsolateObject.htm)|
(Inherited from [GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[MovedBetweenDocuments](M_Grasshopper_Kernel_GH_DocumentObject_MovedBetweenDocuments.htm)|
This method will be called when an object is moved from one document to
another. Override this method if you want to handle such events.  (Inherited
from [GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[NewInstanceGuid](M_Grasshopper_Kernel_GH_InstanceDescription_NewInstanceGuid.htm)|
Generate a new random instance GUID  (Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public method](../icons/pubmethod.gif)|
[NewInstanceGuid(Guid)](M_Grasshopper_Kernel_GH_InstanceDescription_NewInstanceGuid_1.htm)|
Set the instance ID to be a specific GUID. This is very dangerous, only use
this function if you're 6"4' and your first name is David.  (Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public method](../icons/pubmethod.gif)|
[OnAttributesChanged](M_Grasshopper_Kernel_GH_DocumentObject_OnAttributesChanged.htm)|
Raises the AttributesChanged event on the toplevel object.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[OnDisplayExpired](M_Grasshopper_Kernel_GH_DocumentObject_OnDisplayExpired.htm)|
Raises the DisplayExpired event on the toplevel object.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[OnObjectChanged(GH_ObjectChangedEventArgs)](M_Grasshopper_Kernel_GH_DocumentObject_OnObjectChanged.htm)|
(Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[OnObjectChanged(GH_ObjectEventType)](M_Grasshopper_Kernel_GH_DocumentObject_OnObjectChanged_1.htm)|
(Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[OnObjectChanged(String)](M_Grasshopper_Kernel_GH_DocumentObject_OnObjectChanged_3.htm)|
(Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)| [OnObjectChanged(GH_ObjectEventType,
Object)](M_Grasshopper_Kernel_GH_DocumentObject_OnObjectChanged_2.htm)|
(Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)| [OnObjectChanged(String,
Object)](M_Grasshopper_Kernel_GH_DocumentObject_OnObjectChanged_4.htm)|
(Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[OnPingDocument](M_Grasshopper_Kernel_GH_DocumentObject_OnPingDocument.htm)|
Raise the PingDocument Event on the toplevel object and try to find the
document which owns this object.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[OnPreviewExpired](M_Grasshopper_Kernel_GH_DocumentObject_OnPreviewExpired.htm)|
Raises the PreviewExpired event on the toplevel object.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[OnSolutionExpired](M_Grasshopper_Kernel_GH_DocumentObject_OnSolutionExpired.htm)|
Raises the SolutionExpired event on the toplevel object. You probably want to
call ExpireSolution() instead of this method directly.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_GH_PersistentParam_1_Read.htm)|  (Inherited from
[GH_PersistentParamT](T_Grasshopper_Kernel_GH_PersistentParam_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[ReadFull](M_Grasshopper_Kernel_GH_InstanceDescription_ReadFull.htm)|
GH_InstanceDescription does not by default serialize all fields. Use this
function to read _all_ fields from the archive. This method is compatible with
the default Write()/Read() operations.  (Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public method](../icons/pubmethod.gif)|
[RecordUndoEvent(GH_UndoRecord)](M_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent.htm)|
Record an entire undo record.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[RecordUndoEvent(String)](M_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent_1.htm)|
Record a generic object change undo event.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)| [RecordUndoEvent(String,
IGH_UndoAction)](M_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent_2.htm)|
Record a specific object change undo event.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[RegisterRemoteIDs](M_Grasshopper_Rhinoceros_Params_ModelContentParam_1_RegisterRemoteIDs.htm)|
(Inherited from
[ModelContentParamT](T_Grasshopper_Rhinoceros_Params_ModelContentParam_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[RelinkProxySources](M_Grasshopper_Kernel_GH_Param_1_RelinkProxySources.htm)|
Attempt to replace all proxy sources with real sources. Proxy sources are used
during file IO, when actual sources might not be available yet. Once an IO
operation has been completed there should be no more proxy sources.
(Inherited from [GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[RemoveAllSources](M_Grasshopper_Kernel_GH_Param_1_RemoveAllSources.htm)|
Remove all sources from this parameter.  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[RemovedFromDocument](M_Grasshopper_Kernel_GH_DocumentObject_RemovedFromDocument.htm)|
This method will be called when an object is removed from a document. Override
this method if you want to handle such events.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[RemoveEffects](M_Grasshopper_Kernel_GH_Param_1_RemoveEffects.htm)|  Remove
all post-process effects. Note to implementors, you _must_ call the base
method if you override this function.  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[RemoveSource(Guid)](M_Grasshopper_Kernel_GH_Param_1_RemoveSource_1.htm)|
Remove the specified source from this parameter.  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[RemoveSource(IGH_Param)](M_Grasshopper_Kernel_GH_Param_1_RemoveSource.htm)|
Remove the specified source from this parameter.  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public method](../icons/pubmethod.gif)| [ReplaceSource(Guid,
IGH_Param)](M_Grasshopper_Kernel_GH_Param_1_ReplaceSource_1.htm)|  Replace an
existing source with a new one. If the old_source does not exist in this
parameter, nothing happens.  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public method](../icons/pubmethod.gif)| [ReplaceSource(IGH_Param,
IGH_Param)](M_Grasshopper_Kernel_GH_Param_1_ReplaceSource.htm)|  Replace an
existing source with a new one. If the old_source does not exist in this
parameter, nothing happens.  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[RuntimeMessages](M_Grasshopper_Kernel_GH_ActiveObject_RuntimeMessages.htm)|
Gets the list of cached runtime messages that were recorded during solver-time
processes.  (Inherited from
[GH_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[SDKCompliancy](M_Grasshopper_Kernel_GH_ActiveObject_SDKCompliancy.htm)|  Test
whether this object is compliant with a given Rhino version.  (Inherited from
[GH_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[SetIconOverride](M_Grasshopper_Kernel_GH_DocumentObject_SetIconOverride.htm)|
Set a new custom icon override for this object.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[SetPersistentData(T)](M_Grasshopper_Kernel_GH_PersistentParam_1_SetPersistentData_3.htm)|
Add a single item to the persistent data. This method will record an undo
event, raise the OnObjectChanged event for PersistentData flags and place a
call to ExpireSolution(False). If you want to add more than one piece of data,
you should use the appropriate overload for this method.  (Inherited from
[GH_PersistentParamT](T_Grasshopper_Kernel_GH_PersistentParam_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[SetPersistentData(GH_StructureT)](M_Grasshopper_Kernel_GH_PersistentParam_1_SetPersistentData.htm)|
Assign a tree of items to the persistent data. This method will erase any
existing data, record an undo event, raise the OnObjectChanged event for
PersistentData flags and place a call to ExpireSolution(False). If you want to
add a tree of data, you should use the appropriate overload for this method.
(Inherited from
[GH_PersistentParamT](T_Grasshopper_Kernel_GH_PersistentParam_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[SetPersistentData(IEnumerableT)](M_Grasshopper_Kernel_GH_PersistentParam_1_SetPersistentData_1.htm)|
Assign a list of items to the persistent data. This method will erase any
existing data, record an undo event, raise the OnObjectChanged event for
PersistentData flags and place a call to ExpireSolution(False). If you want to
add a tree of data, you should use the appropriate overload for this method.
(Inherited from
[GH_PersistentParamT](T_Grasshopper_Kernel_GH_PersistentParam_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[SetPersistentData(Object)](M_Grasshopper_Kernel_GH_PersistentParam_1_SetPersistentData_2.htm)|
Add a collection of values to the persistent data.  (Inherited from
[GH_PersistentParamT](T_Grasshopper_Kernel_GH_PersistentParam_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[SetPrincipal](M_Grasshopper_Kernel_GH_Param_1_SetPrincipal.htm)|  Set the
principal parameter state.  (Inherited from
[GH_ParamT](T_Grasshopper_Kernel_GH_Param_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[TriggerAutoSave](M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave.htm)|
Triggers the AutoSave function on the owner document with the object_changed
flag.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[TriggerAutoSave(GH_AutoSaveTrigger)](M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave_1.htm)|
Triggers the AutoSave function on the owner document with a custom flag.
(Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[TriggerAutoSave(Guid)](M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave_3.htm)|
Triggers the AutoSave function on the owner document with the object_changed
flag.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)| [TriggerAutoSave(GH_AutoSaveTrigger,
Guid)](M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave_2.htm)|
Triggers the AutoSave function on the owner document with a custom flag.
(Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_GH_PersistentParam_1_Write.htm)|  (Inherited from
[GH_PersistentParamT](T_Grasshopper_Kernel_GH_PersistentParam_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[WriteFull](M_Grasshopper_Kernel_GH_InstanceDescription_WriteFull.htm)|
GH_InstanceDescription does not by default serialize all fields. Use this
function to write _all_ fields to the archive. This method is compatible with
the default Write()/Read() operations.  (Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
Top

![](../icons/SectionExpanded.png)Events

| Name| Description  
---|---|---  
![Public event](../icons/pubevent.gif)|
[AttributesChanged](E_Grasshopper_Kernel_GH_DocumentObject_AttributesChanged.htm)|
Raised whenever the number or kind of attributes changes. This event is
handled by GH_Documents who subsequently wipe their attribute caches.
(Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public event](../icons/pubevent.gif)|
[DisplayExpired](E_Grasshopper_Kernel_GH_DocumentObject_DisplayExpired.htm)|
Raised whenever the display (on the Canvas) of a certain object becomes
invalid.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public event](../icons/pubevent.gif)|
[ObjectChanged](E_Grasshopper_Kernel_GH_DocumentObject_ObjectChanged.htm)|
(Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public event](../icons/pubevent.gif)|
[PingDocument](E_Grasshopper_Kernel_GH_DocumentObject_PingDocument.htm)|
Raised whenever an object needs to know which GH_Document it belongs to.
(Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public event](../icons/pubevent.gif)|
[PreviewExpired](E_Grasshopper_Kernel_GH_DocumentObject_PreviewExpired.htm)|
Raised whenever the display (in the Rhino viewports) of a certain object
becomes invalid.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public event](../icons/pubevent.gif)|
[SolutionExpired](E_Grasshopper_Kernel_GH_DocumentObject_SolutionExpired.htm)|
Raised whenever the solution of a certain object becomes invalid.  (Inherited
from [GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Render.Params
Namespace](N_Grasshopper_Rhinoceros_Render_Params.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

