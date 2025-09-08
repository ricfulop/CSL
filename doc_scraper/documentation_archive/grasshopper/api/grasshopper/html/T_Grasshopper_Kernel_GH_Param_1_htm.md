---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_Param_1.htm
scraped_at: 2025-09-08T16:17:15.573802
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_Param(T) Class](../html/T_Grasshopper_Kernel_GH_Param_1.htm "GH_Param\(T\)
Class")

[GH_Param(T) Constructor
](../html/Overload_Grasshopper_Kernel_GH_Param_1__ctor.htm "GH_Param\(T\)
Constructor ")

[GH_Param(T)
Properties](../html/Properties_T_Grasshopper_Kernel_GH_Param_1.htm
"GH_Param\(T\) Properties")

[GH_Param(T) Methods](../html/Methods_T_Grasshopper_Kernel_GH_Param_1.htm
"GH_Param\(T\) Methods")

[GH_Param(T) Events](../html/Events_T_Grasshopper_Kernel_GH_Param_1.htm
"GH_Param\(T\) Events")

[GH_Param(T) Fields](../html/Fields_T_Grasshopper_Kernel_GH_Param_1.htm
"GH_Param\(T\) Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_ParamT Class  
  
---  
  
Base implementation of IGH_Param. Derive from this class rather than
implementing IGH_Param from scratch. If your parameter can store persistent
data, derive from GH_PersistentParam(Of T) instead.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.KernelGH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm)  
[Grasshopper.KernelGH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm)  
[Grasshopper.KernelGH_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm)  
Grasshopper.KernelGH_ParamT  
[Grasshopper.KernelGH_PersistentParamT](T_Grasshopper_Kernel_GH_PersistentParam_1.htm)  
[Grasshopper.Kernel.ParametersParam_Predicate](T_Grasshopper_Kernel_Parameters_Param_Predicate.htm)  
[Grasshopper.Rhinoceros.ParamsModelDataParamT](T_Grasshopper_Rhinoceros_Params_ModelDataParam_1.htm)  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public abstract class GH_Param<T> : GH_ActiveObject, 
    	IGH_Param
    where T : class, IGH_Goo
    
    
    
    Public MustInherit Class GH_Param(Of T As {Class, IGH_Goo})
    	Inherits GH_ActiveObject
    	Implements IGH_Param

#### Type Parameters

T

    Data type for this parameter.

The GH_ParamT type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[GH_ParamT(IGH_InstanceDescription)](M_Grasshopper_Kernel_GH_Param_1__ctor.htm)|
Initializes a new instance of the GH_ParamT class  
![Protected method](../icons/protmethod.gif)|
[GH_ParamT(IGH_InstanceDescription,
GH_ParamAccess)](M_Grasshopper_Kernel_GH_Param_1__ctor_1.htm)| Initializes a
new instance of the GH_ParamT class  
![Protected method](../icons/protmethod.gif)| [GH_ParamT(String, String,
String, String, String,
GH_ParamAccess)](M_Grasshopper_Kernel_GH_Param_1__ctor_2.htm)| Initializes a
new instance of the GH_ParamT class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Access](P_Grasshopper_Kernel_GH_Param_1_Access.htm)|  Gets or sets the Access
level for this parameter.  
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
[ComponentGuid](P_Grasshopper_Kernel_GH_DocumentObject_ComponentGuid.htm)|
Returns a consistent ID for this object type. Every object must supply a
unique and unchanging ID that is used to identify objects of the same type.
(Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[DataMapping](P_Grasshopper_Kernel_GH_Param_1_DataMapping.htm)|  Gets or sets
the data mapping of this Parameter.  
![Public property](../icons/pubproperty.gif)|
[DataType](P_Grasshopper_Kernel_GH_Param_1_DataType.htm)|  Type is either Void
if there are no sources or Remote. Derived classes should expand on this.  
![Public property](../icons/pubproperty.gif)|
[Description](P_Grasshopper_Kernel_GH_InstanceDescription_Description.htm)|
Gets or sets the description of the object. This field typically remains fixed
during the lifetime of an object.  (Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[Exposure](P_Grasshopper_Kernel_GH_DocumentObject_Exposure.htm)|  Gets the
exposure of this object in the Graphical User Interface. The default is to
expose everywhere.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[HasCategory](P_Grasshopper_Kernel_GH_InstanceDescription_HasCategory.htm)|
Gets whether or not the Category field has been set.  (Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[HasProxySources](P_Grasshopper_Kernel_GH_Param_1_HasProxySources.htm)|  Gets
a value indicating whether or not this parameter maintains proxy sources.
Proxy sources are used during file IO, when actual sources might not be
available yet. Once an IO operation has been completed there should be no more
proxy sources.  
![Public property](../icons/pubproperty.gif)|
[HasSubCategory](P_Grasshopper_Kernel_GH_InstanceDescription_HasSubCategory.htm)|
Gets whether or not the SubCategory field has been set.  (Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Protected property](../icons/protproperty.gif)|
[Icon](P_Grasshopper_Kernel_GH_DocumentObject_Icon.htm)|  Override this
function to supply a custom icon (24x24 pixels). The result of this property
is cached, so don't worry if icon retrieval is not very fast.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
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
amount and source of the local values.  (Overrides
[GH_InstanceDescriptionInstanceDescription](P_Grasshopper_Kernel_GH_InstanceDescription_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[InstanceGuid](P_Grasshopper_Kernel_GH_InstanceDescription_InstanceGuid.htm)|
Gets the ID of this runtime instance.  (Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsDataProvider](P_Grasshopper_Kernel_GH_Param_1_IsDataProvider.htm)|
(Overrides
[GH_ActiveObjectIsDataProvider](P_Grasshopper_Kernel_GH_ActiveObject_IsDataProvider.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsPrincipal](P_Grasshopper_Kernel_GH_Param_1_IsPrincipal.htm)|  Gets whether
this parameter is a principal parameter. Principal parameters are maintained
by components and are not part of the IGH_Param interface.  
![Public property](../icons/pubproperty.gif)|
[Keywords](P_Grasshopper_Kernel_GH_InstanceDescription_Keywords.htm)|  Gets a
list of additional keywords that describe the object. Typically this list is
empty but you can override this property to aid in object searches.
(Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[Kind](P_Grasshopper_Kernel_GH_Param_1_Kind.htm)|  Gets the parameter kind.
The kind is evaluated lazily and cached.  
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
![Public property](../icons/pubproperty.gif)|
[Phase](P_Grasshopper_Kernel_GH_ActiveObject_Phase.htm)|  Gets or sets the
solution phase this object is currenly in.  (Inherited from
[GH_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).)  
![Public property](../icons/pubproperty.gif)|
[ProcessorTime](P_Grasshopper_Kernel_GH_Param_1_ProcessorTime.htm)|
(Overrides
[GH_ActiveObjectProcessorTime](P_Grasshopper_Kernel_GH_ActiveObject_ProcessorTime.htm).)  
![Public property](../icons/pubproperty.gif)|
[ProxySourceCount](P_Grasshopper_Kernel_GH_Param_1_ProxySourceCount.htm)|
Gets the number of proxy sources for this parameter. Proxy sources are used
during file IO, when actual sources might not be available yet. Once an IO
operation has been completed there should be no more proxy sources.  
![Public property](../icons/pubproperty.gif)|
[Recipients](P_Grasshopper_Kernel_GH_Param_1_Recipients.htm)|  Gets a list of
all the recipients of this parameter. I.e. a recipient has this parameter as
one of the sources. The Recipient list is maintained by the parameter, do not
modify it yourself.  
![Public property](../icons/pubproperty.gif)|
[Reverse](P_Grasshopper_Kernel_GH_Param_1_Reverse.htm)|  Gets or sets the data
reverse modifier of this parameter.  
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
simplify modifier for this parameter.  
![Public property](../icons/pubproperty.gif)|
[SourceCount](P_Grasshopper_Kernel_GH_Param_1_SourceCount.htm)|  Gets the
number of sources for this parameter.  
![Public property](../icons/pubproperty.gif)|
[Sources](P_Grasshopper_Kernel_GH_Param_1_Sources.htm)|  Gets a list of source
parameters. Do not modify this list, if you wish to add or remove sources, use
dedicated functions like AddSource() and RemoveSource() instead.  
![Public property](../icons/pubproperty.gif)|
[StateTags](P_Grasshopper_Kernel_GH_Param_1_StateTags.htm)|  Gets all the
StateTags that are associated with this parameter. A state tag is a visual
feedback icon that represents specific internal settings.  
![Public property](../icons/pubproperty.gif)|
[SubCategory](P_Grasshopper_Kernel_GH_InstanceDescription_SubCategory.htm)|
Gets or sets the SubCategory in which this object belongs. If HasSubCategory()
returns false, this field has no meaning.  (Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[Type](P_Grasshopper_Kernel_GH_Param_1_Type.htm)|  Gets the Framework Type
descriptor for the stored Data.  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_GH_Param_1_TypeName.htm)|  Calls TypeName() on
the first instance of T it can find. This is either an item in the volatile
list, or a newly constructed instance.  
![Public property](../icons/pubproperty.gif)|
[VolatileData](P_Grasshopper_Kernel_GH_Param_1_VolatileData.htm)|  
![Public property](../icons/pubproperty.gif)|
[VolatileDataCount](P_Grasshopper_Kernel_GH_Param_1_VolatileDataCount.htm)|  
![Public property](../icons/pubproperty.gif)|
[WireDisplay](P_Grasshopper_Kernel_GH_Param_1_WireDisplay.htm)|  Gets or sets
the wire display style for this parameter. Wire display only affects the wires
connected to the parameter input.  
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
parameter with data at runtime.  
![Public method](../icons/pubmethod.gif)| [AddSource(IGH_Param,
Int32)](M_Grasshopper_Kernel_GH_Param_1_AddSource_1.htm)|  Insert a new Source
parameter into the Sources list. Sources provide this parameter with data at
runtime.  
![Public method](../icons/pubmethod.gif)| [AddVolatileData(GH_Path, Int32,
T)](M_Grasshopper_Kernel_GH_Param_1_AddVolatileData_1.htm)|  
![Public method](../icons/pubmethod.gif)| [AddVolatileData(GH_Path, Int32,
Object)](M_Grasshopper_Kernel_GH_Param_1_AddVolatileData.htm)|  Inserts an
item of volatile data into the data structure.  
![Public method](../icons/pubmethod.gif)| [AddVolatileDataList(GH_Path,
ListT)](M_Grasshopper_Kernel_GH_Param_1_AddVolatileDataList.htm)|  
![Public method](../icons/pubmethod.gif)| [AddVolatileDataList(GH_Path,
IEnumerable)](M_Grasshopper_Kernel_GH_Param_1_AddVolatileDataList_1.htm)|  
![Public method](../icons/pubmethod.gif)|
[AddVolatileDataTree(GH_StructureT)](M_Grasshopper_Kernel_GH_Param_1_AddVolatileDataTree.htm)|  
![Public method](../icons/pubmethod.gif)|
[AddVolatileDataTree(IGH_Structure)](M_Grasshopper_Kernel_GH_Param_1_AddVolatileDataTree_1.htm)|  
![Public method](../icons/pubmethod.gif)|
[AppendAdditionalMenuItems](M_Grasshopper_Kernel_GH_Param_1_AppendAdditionalMenuItems.htm)|
Override this function if you want to add specific items to the object context
menu Default items already included in the menu toolstrip are: 1\. Name 2\.
Preview 3\. Warnings 4\. Errors  (Overrides
[GH_ActiveObjectAppendAdditionalMenuItems(ToolStripDropDown)](M_Grasshopper_Kernel_GH_ActiveObject_AppendAdditionalMenuItems.htm).)  
![Public method](../icons/pubmethod.gif)|
[AppendMenuItems](M_Grasshopper_Kernel_GH_ActiveObject_AppendMenuItems.htm)|
This function is called when a context menu is about to be displayed. Override
it to set custom items. GH_ActiveObject will already populate the menu with
default items, if you merely wish to insert object-specific menu item,
consider overriding AppendAdditionalMenuItems instead.  (Inherited from
[GH_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).)  
![Protected method](../icons/protmethod.gif)|
[Cast_Object](M_Grasshopper_Kernel_GH_Param_1_Cast_Object.htm)|  Attempts to
convert the Object reference into an instance of T. This method will perform a
direct cast if possible or it will call Casting functions on T or Data if they
exist. Data will not be duplicated unless a type conversion is required.  
![Public method](../icons/pubmethod.gif)|
[ClearData](M_Grasshopper_Kernel_GH_Param_1_ClearData.htm)|  (Overrides
[GH_ActiveObjectClearData](M_Grasshopper_Kernel_GH_ActiveObject_ClearData.htm).)  
![Public method](../icons/pubmethod.gif)|
[ClearProxySources](M_Grasshopper_Kernel_GH_Param_1_ClearProxySources.htm)|
Remove all proxy sources without attempting to relink them.  
![Public method](../icons/pubmethod.gif)|
[ClearRuntimeMessages](M_Grasshopper_Kernel_GH_ActiveObject_ClearRuntimeMessages.htm)|
Destroy all warning and error lists  (Inherited from
[GH_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[CollectData](M_Grasshopper_Kernel_GH_Param_1_CollectData.htm)|  (Overrides
[GH_ActiveObjectCollectData](M_Grasshopper_Kernel_GH_ActiveObject_CollectData.htm).)  
![Protected method](../icons/protmethod.gif)|
[CollectVolatileData_Custom](M_Grasshopper_Kernel_GH_Param_1_CollectVolatileData_Custom.htm)|
If a parameter has no sources, the CollectVolatileData_Custom() method is
called. The basic implementation does nothing, but you can override this
method to provide special data instantiation logic.  
![Protected method](../icons/protmethod.gif)|
[CollectVolatileData_FromSources](M_Grasshopper_Kernel_GH_Param_1_CollectVolatileData_FromSources.htm)|
This method collects volatile data from all the source parameters.  
![Public method](../icons/pubmethod.gif)|
[ComputeData](M_Grasshopper_Kernel_GH_Param_1_ComputeData.htm)|  (Overrides
[GH_ActiveObjectComputeData](M_Grasshopper_Kernel_GH_ActiveObject_ComputeData.htm).)  
![Protected method](../icons/protmethod.gif)|
[ConversionCallback](M_Grasshopper_Kernel_GH_Param_1_ConversionCallback.htm)|
This method is called whenever a successful conversion takes place from some
source data into local target data. Override it if you wish to keep tabs on
conversions.  
![Public method](../icons/pubmethod.gif)|
[CopyFrom](M_Grasshopper_Kernel_GH_InstanceDescription_CopyFrom.htm)|  Copy
all fields (except the instance ID) from another instance description.
(Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public method](../icons/pubmethod.gif)|
[CreateAttributes](M_Grasshopper_Kernel_GH_Param_1_CreateAttributes.htm)|
(Overrides
[GH_DocumentObjectCreateAttributes](M_Grasshopper_Kernel_GH_DocumentObject_CreateAttributes.htm).)  
![Public method](../icons/pubmethod.gif)|
[CreateProxySources](M_Grasshopper_Kernel_GH_Param_1_CreateProxySources.htm)|
Convert all proper source parameters into proxy sources.  
![Public method](../icons/pubmethod.gif)|
[DependsOn](M_Grasshopper_Kernel_GH_Param_1_DependsOn.htm)|  (Overrides
[GH_ActiveObjectDependsOn(IGH_ActiveObject)](M_Grasshopper_Kernel_GH_ActiveObject_DependsOn.htm).)  
![Protected method](../icons/protmethod.gif)|
[DestroyIconCache](M_Grasshopper_Kernel_GH_DocumentObject_DestroyIconCache.htm)|
Call this method to erase the existing icon cache. You must call this if you
want to change the display icon of an object.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[DocumentContextChanged](M_Grasshopper_Kernel_GH_DocumentObject_DocumentContextChanged.htm)|
This method will be called when the document that owns this object moves into
a different context.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Protected method](../icons/protmethod.gif)|
[ExpireDownStreamObjects](M_Grasshopper_Kernel_GH_Param_1_ExpireDownStreamObjects.htm)|
(Overrides
[GH_ActiveObjectExpireDownStreamObjects](M_Grasshopper_Kernel_GH_ActiveObject_ExpireDownStreamObjects.htm).)  
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
Invoke the Expiresolution(bool) method on the toplevel object.  
![Protected method](../icons/protmethod.gif)|
[Format](M_Grasshopper_Kernel_GH_Param_1_Format.htm)|  Returns "Null" if the
data is a null reference, otherwise calls ToString() on the Data instance.  
![Protected method](../icons/protmethod.gif)| [GetValue(String,
Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue.htm)|  Get a boolean
value from the component value table.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Protected method](../icons/protmethod.gif)| [GetValue(String,
Double)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue_1.htm)|  Get a double
value from the component value table.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Protected method](../icons/protmethod.gif)| [GetValue(String,
Color)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue_2.htm)|  Get a color
value from the component value table.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Protected method](../icons/protmethod.gif)| [GetValue(String,
Int32)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue_3.htm)|  Get an
integer value from the component value table.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Protected method](../icons/protmethod.gif)| [GetValue(String,
String)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue_4.htm)|  Get a string
value from the component value table.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Protected method](../icons/protmethod.gif)|
[HtmlHelp_Source](M_Grasshopper_Kernel_GH_DocumentObject_HtmlHelp_Source.htm)|
Return a String which contains HTML formatted source for the help topic. If
you want to pass a URL that points to a remote page, then prefix the URL with
a GOTO: tag, like so: GOTO:http://www.YourWebAddressHere.com  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Protected method](../icons/protmethod.gif)|
[InstantiateT](M_Grasshopper_Kernel_GH_Param_1_InstantiateT.htm)|  Attempts to
instantiate a new instance of T.  
![Public method](../icons/pubmethod.gif)|
[IsolateObject](M_Grasshopper_Kernel_GH_Param_1_IsolateObject.htm)|
(Overrides
[GH_DocumentObjectIsolateObject](M_Grasshopper_Kernel_GH_DocumentObject_IsolateObject.htm).)  
![Protected method](../icons/protmethod.gif)|
[Menu_AppendBakeItem](M_Grasshopper_Kernel_GH_ActiveObject_Menu_AppendBakeItem.htm)|
Append the default Bake menu item.  (Inherited from
[GH_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).)  
![Protected method](../icons/protmethod.gif)|
[Menu_AppendDisconnectWires](M_Grasshopper_Kernel_GH_Param_1_Menu_AppendDisconnectWires.htm)|  
![Protected method](../icons/protmethod.gif)|
[Menu_AppendEnableItem](M_Grasshopper_Kernel_GH_ActiveObject_Menu_AppendEnableItem.htm)|
Append the default Enable/Disable menu item.  (Inherited from
[GH_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).)  
![Protected method](../icons/protmethod.gif)|
[Menu_AppendFlattenParameter](M_Grasshopper_Kernel_GH_Param_1_Menu_AppendFlattenParameter.htm)|  
![Protected method](../icons/protmethod.gif)|
[Menu_AppendGraftParameter](M_Grasshopper_Kernel_GH_Param_1_Menu_AppendGraftParameter.htm)|  
![Protected method](../icons/protmethod.gif)|
[Menu_AppendObjectHelp](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendObjectHelp.htm)|
Appends the default object Help menu item.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Protected method](../icons/protmethod.gif)|
[Menu_AppendObjectName](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendObjectName.htm)|
Appends the old-fashioned object name menu item. If you also want the Display
mode toggle then use Menu_AppendObjectNameEx()  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Protected method](../icons/protmethod.gif)|
[Menu_AppendObjectNameEx](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendObjectNameEx.htm)|
Appends the default object name + display mode menu item.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Protected method](../icons/protmethod.gif)|
[Menu_AppendPreviewItem](M_Grasshopper_Kernel_GH_ActiveObject_Menu_AppendPreviewItem.htm)|
Append the default Show/Hide preview menu item.  (Inherited from
[GH_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).)  
![Protected method](../icons/protmethod.gif)|
[Menu_AppendPrincipalParameter](M_Grasshopper_Kernel_GH_Param_1_Menu_AppendPrincipalParameter.htm)|  
![Protected method](../icons/protmethod.gif)|
[Menu_AppendPublish](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendPublish.htm)|
Appends the default item for publishing to RCP. This menu will only appear if
the current class implement IRcpAwareObject  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Protected method](../icons/protmethod.gif)|
[Menu_AppendReverseParameter](M_Grasshopper_Kernel_GH_Param_1_Menu_AppendReverseParameter.htm)|  
![Protected method](../icons/protmethod.gif)|
[Menu_AppendRuntimeMessages](M_Grasshopper_Kernel_GH_ActiveObject_Menu_AppendRuntimeMessages.htm)|
Append the default warnings and errors menu items.  (Inherited from
[GH_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).)  
![Protected method](../icons/protmethod.gif)|
[Menu_AppendSimplifyParameter](M_Grasshopper_Kernel_GH_Param_1_Menu_AppendSimplifyParameter.htm)|  
![Protected method](../icons/protmethod.gif)|
[Menu_AppendWireDisplay](M_Grasshopper_Kernel_GH_Param_1_Menu_AppendWireDisplay.htm)|  
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
![Protected method](../icons/protmethod.gif)|
[OnVolatileDataCollected](M_Grasshopper_Kernel_GH_Param_1_OnVolatileDataCollected.htm)|
Once volatile data has been collected this method will be calles. The basic
implementation does nothing, but you can add code here to post-process or
analyze the volatile data.  
![Protected method](../icons/protmethod.gif)|
[PreferredCast](M_Grasshopper_Kernel_GH_Param_1_PreferredCast.htm)|  Implement
this function if you're certain that you'll be confronted with very common
casts. For example, GH_Point has a preferred cast from Rhino.Geometry.Point3d
and GH_Number has a preferred cast from System.Double.  
![Protected method](../icons/protmethod.gif)|
[Preview_ComputeClippingBox](M_Grasshopper_Kernel_GH_Param_1_Preview_ComputeClippingBox.htm)|
This function can be used to iterate over all items in the Volatile data tree
and collect the union clipping box of all non-null items that implement
Preview.IGH_PreviewData. This function requires a lot of TypeOf and
DirectCasting, so if you're worried about performance you should consider
doing this yourself.  
![Protected method](../icons/protmethod.gif)|
[Preview_DrawMeshes](M_Grasshopper_Kernel_GH_Param_1_Preview_DrawMeshes.htm)|
This function can be used to iterate over all items in the Volatile data tree
and call DrawViewportWires on each item that implements
Preview.IGH_PreviewData. This function requires a lot of TypeOf and
DirectCasting, so if you're worried about performance you should consider
doing this yourself.  
![Protected method](../icons/protmethod.gif)|
[Preview_DrawWires](M_Grasshopper_Kernel_GH_Param_1_Preview_DrawWires.htm)|
This function can be used to iterate over all items in the Volatile data tree
and call DrawViewportWires on each item that implements
Preview.IGH_PreviewData. This function requires a lot of TypeOf and
DirectCasting, so if you're worried about performance you should consider
doing this yourself.  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_GH_Param_1_Read.htm)|  (Overrides
[GH_ActiveObjectRead(GH_IReader)](M_Grasshopper_Kernel_GH_ActiveObject_Read.htm).)  
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
[RegisterRemoteIDs](M_Grasshopper_Kernel_GH_ActiveObject_RegisterRemoteIDs.htm)|
Override this function if you want object changes in the Rhino document to
trigger a new solution.  (Inherited from
[GH_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).)  
![Protected method](../icons/protmethod.gif)|
[RegisterRemoteIDsUtil](M_Grasshopper_Kernel_GH_Param_1_RegisterRemoteIDsUtil.htm)|
Utility function which treats all data in the Volatile cache as
IGH_GeometricGoo and registers all referenced objects. Call this function from
within RegisterRemoteIDs() if you are absolutely sure that all the items in
volatiledata implement IGH_GeometricGoo.  
![Public method](../icons/pubmethod.gif)|
[RelinkProxySources](M_Grasshopper_Kernel_GH_Param_1_RelinkProxySources.htm)|
Attempt to replace all proxy sources with real sources. Proxy sources are used
during file IO, when actual sources might not be available yet. Once an IO
operation has been completed there should be no more proxy sources.  
![Public method](../icons/pubmethod.gif)|
[RemoveAllSources](M_Grasshopper_Kernel_GH_Param_1_RemoveAllSources.htm)|
Remove all sources from this parameter.  
![Public method](../icons/pubmethod.gif)|
[RemovedFromDocument](M_Grasshopper_Kernel_GH_DocumentObject_RemovedFromDocument.htm)|
This method will be called when an object is removed from a document. Override
this method if you want to handle such events.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[RemoveEffects](M_Grasshopper_Kernel_GH_Param_1_RemoveEffects.htm)|  Remove
all post-process effects. Note to implementors, you _must_ call the base
method if you override this function.  
![Public method](../icons/pubmethod.gif)|
[RemoveSource(Guid)](M_Grasshopper_Kernel_GH_Param_1_RemoveSource_1.htm)|
Remove the specified source from this parameter.  
![Public method](../icons/pubmethod.gif)|
[RemoveSource(IGH_Param)](M_Grasshopper_Kernel_GH_Param_1_RemoveSource.htm)|
Remove the specified source from this parameter.  
![Protected method](../icons/protmethod.gif)|
[Render_AppendGeometry](M_Grasshopper_Kernel_GH_Param_1_Render_AppendGeometry.htm)|
**Obsolete.** This function has been emptied because it is Obsolete.  
![Public method](../icons/pubmethod.gif)| [ReplaceSource(Guid,
IGH_Param)](M_Grasshopper_Kernel_GH_Param_1_ReplaceSource_1.htm)|  Replace an
existing source with a new one. If the old_source does not exist in this
parameter, nothing happens.  
![Public method](../icons/pubmethod.gif)| [ReplaceSource(IGH_Param,
IGH_Param)](M_Grasshopper_Kernel_GH_Param_1_ReplaceSource.htm)|  Replace an
existing source with a new one. If the old_source does not exist in this
parameter, nothing happens.  
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
[SetPrincipal](M_Grasshopper_Kernel_GH_Param_1_SetPrincipal.htm)|  Set the
principal parameter state.  
![Protected method](../icons/protmethod.gif)| [SetValue(String,
Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue.htm)|  Set a named
value. This value will be serialized with the component.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Protected method](../icons/protmethod.gif)| [SetValue(String,
Double)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue_1.htm)|  Set a named
value. This value will be serialized with the component.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Protected method](../icons/protmethod.gif)| [SetValue(String,
Color)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue_2.htm)|  Set a named
value. This value will be serialized with the component.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Protected method](../icons/protmethod.gif)| [SetValue(String,
Int32)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue_3.htm)|  Set a named
value. This value will be serialized with the component.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Protected method](../icons/protmethod.gif)| [SetValue(String,
String)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue_4.htm)|  Set a named
value. This value will be serialized with the component.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
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
![Protected method](../icons/protmethod.gif)|
[ValuesChanged](M_Grasshopper_Kernel_GH_DocumentObject_ValuesChanged.htm)|
Override this method if you want to respond to changes to the value table. The
base implementation is empty, so you don't have to call it.  (Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Protected method](../icons/protmethod.gif)|
[VolatileDataDescription](M_Grasshopper_Kernel_GH_Param_1_VolatileDataDescription.htm)|
This method is called to populate the Tooltip data description field.  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_GH_Param_1_Write.htm)|  (Overrides
[GH_ActiveObjectWrite(GH_IWriter)](M_Grasshopper_Kernel_GH_ActiveObject_Write.htm).)  
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

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Protected field](../icons/protfield.gif)|
[m_attributes](F_Grasshopper_Kernel_GH_DocumentObject_m_attributes.htm)|
(Inherited from
[GH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).)  
![Protected field](../icons/protfield.gif)|
[m_data](F_Grasshopper_Kernel_GH_Param_1_m_data.htm)|  Contains the runtime
data for this parameter, also known as "Volatile" data.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

