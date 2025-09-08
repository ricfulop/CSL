---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_IGH_DocumentObject.htm
scraped_at: 2025-09-08T16:18:23.807940
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH_DocumentObject
Interface](../html/T_Grasshopper_Kernel_IGH_DocumentObject.htm
"IGH_DocumentObject Interface")

[IGH_DocumentObject
Properties](../html/Properties_T_Grasshopper_Kernel_IGH_DocumentObject.htm
"IGH_DocumentObject Properties")

[IGH_DocumentObject
Methods](../html/Methods_T_Grasshopper_Kernel_IGH_DocumentObject.htm
"IGH_DocumentObject Methods")

[IGH_DocumentObject
Events](../html/Events_T_Grasshopper_Kernel_IGH_DocumentObject.htm
"IGH_DocumentObject Events")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_DocumentObject Interface  
  
---  
  
Base interface for objects that want to play on the Canvas. Do not implement
this interface from scratch. Either inherit from GH_DocumentObject or one of
the other partially finished types such as GH_ActiveObject, GH_Param(Of T) or
GH_Component.

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_DocumentObject : IGH_InstanceDescription
    
    
    Public Interface IGH_DocumentObject
    	Inherits IGH_InstanceDescription

The IGH_DocumentObject type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Attributes](P_Grasshopper_Kernel_IGH_DocumentObject_Attributes.htm)|  Gets or
sets the attributes that are associated with this object. Only set custom
attributes if you know what you are doing.  
![Public property](../icons/pubproperty.gif)|
[Category](P_Grasshopper_Kernel_IGH_InstanceDescription_Category.htm)|  Gets
or sets the Category in which this object belongs. If HasCategory() returns
false, this field has no meaning.  (Inherited from
[IGH_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[ComponentGuid](P_Grasshopper_Kernel_IGH_DocumentObject_ComponentGuid.htm)|
Returns a consistent ID for this object type. Every object must supply a
unique and unchanging ID that is used to identify objects of the same type.  
![Public property](../icons/pubproperty.gif)|
[Description](P_Grasshopper_Kernel_IGH_InstanceDescription_Description.htm)|
Gets or sets the description of the object. This field typically remains fixed
during the lifetime of an object.  (Inherited from
[IGH_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[Exposure](P_Grasshopper_Kernel_IGH_DocumentObject_Exposure.htm)|  Gets the
exposure of this object in the Graphical User Interface.  
![Public property](../icons/pubproperty.gif)|
[HasCategory](P_Grasshopper_Kernel_IGH_InstanceDescription_HasCategory.htm)|
Gets whether or not the Category field has been set.  (Inherited from
[IGH_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[HasSubCategory](P_Grasshopper_Kernel_IGH_InstanceDescription_HasSubCategory.htm)|
Gets whether or not the SubCategory field has been set.  (Inherited from
[IGH_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[Icon_24x24](P_Grasshopper_Kernel_IGH_DocumentObject_Icon_24x24.htm)|  The
icon associated with this object.  
![Public property](../icons/pubproperty.gif)|
[Icon_24x24_Locked](P_Grasshopper_Kernel_IGH_DocumentObject_Icon_24x24_Locked.htm)|
The greyscale icon of this object.  
![Public property](../icons/pubproperty.gif)|
[IconDisplayMode](P_Grasshopper_Kernel_IGH_DocumentObject_IconDisplayMode.htm)|
Gets the current display mode of the object.  
![Public property](../icons/pubproperty.gif)|
[InstanceDescription](P_Grasshopper_Kernel_IGH_InstanceDescription_InstanceDescription.htm)|
Gets a description of the current state of the object. This field is usually
the same as the Description() field, but it might be variable when overridden.
(Inherited from
[IGH_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[InstanceGuid](P_Grasshopper_Kernel_IGH_InstanceDescription_InstanceGuid.htm)|
Gets the ID of this runtime instance.  (Inherited from
[IGH_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[Keywords](P_Grasshopper_Kernel_IGH_InstanceDescription_Keywords.htm)|  Gets a
list of additional keywords that describe the object. Typically this list is
empty but you can override this property to aid in object searches.
(Inherited from
[IGH_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[Name](P_Grasshopper_Kernel_IGH_InstanceDescription_Name.htm)|  Gets or sets
the name of the object. This field typically remains fixed during the lifetime
of an object.  (Inherited from
[IGH_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[NickName](P_Grasshopper_Kernel_IGH_InstanceDescription_NickName.htm)|  Gets
or sets the nickname of the object. This field can be changed by the user.
(Inherited from
[IGH_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[Obsolete](P_Grasshopper_Kernel_IGH_DocumentObject_Obsolete.htm)|  Gets
whether this object is Obsolete.  
![Public property](../icons/pubproperty.gif)|
[SubCategory](P_Grasshopper_Kernel_IGH_InstanceDescription_SubCategory.htm)|
Gets or sets the SubCategory in which this object belongs. If HasSubCategory()
returns false, this field has no meaning.  (Inherited from
[IGH_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AddedToDocument](M_Grasshopper_Kernel_IGH_DocumentObject_AddedToDocument.htm)|
This method will be called when an object is added to a document.  
![Public method](../icons/pubmethod.gif)|
[AppendMenuItems](M_Grasshopper_Kernel_IGH_DocumentObject_AppendMenuItems.htm)|
This function is called when a context menu is about to be displayed. Override
it to set custom items.  
![Public method](../icons/pubmethod.gif)|
[CreateAttributes](M_Grasshopper_Kernel_IGH_DocumentObject_CreateAttributes.htm)|
Create new default attributes for this object. You should only call this
function when the Attributes() field is null.  
![Public method](../icons/pubmethod.gif)|
[DocumentContextChanged](M_Grasshopper_Kernel_IGH_DocumentObject_DocumentContextChanged.htm)|
This method will be called when the document that owns this object moves into
a different context.  
![Public method](../icons/pubmethod.gif)|
[ExpirePreview](M_Grasshopper_Kernel_IGH_DocumentObject_ExpirePreview.htm)|
Call this function when you suspect that the preview has expired for this
object. This will cause the display cache to be eradicated.  
![Public method](../icons/pubmethod.gif)|
[ExpireSolution](M_Grasshopper_Kernel_IGH_DocumentObject_ExpireSolution.htm)|
Call this function whenever you do something which expires the current
solution. This will make sure all caches are erased, all downstream objects
are expired and that the event is raised. The default implementation merely
places a call to OnSolutionExpired(), override this function in derived
classes to make sure you clear local data caches and expire downstream
objects.  
![Public method](../icons/pubmethod.gif)|
[IsolateObject](M_Grasshopper_Kernel_IGH_DocumentObject_IsolateObject.htm)|
Destroy all connections to other objects.  
![Public method](../icons/pubmethod.gif)|
[MovedBetweenDocuments](M_Grasshopper_Kernel_IGH_DocumentObject_MovedBetweenDocuments.htm)|
This method will be called when an object is moved from one document to
another.  
![Public method](../icons/pubmethod.gif)|
[NewInstanceGuid](M_Grasshopper_Kernel_IGH_InstanceDescription_NewInstanceGuid.htm)|
Generate a new random instance GUID  (Inherited from
[IGH_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).)  
![Public method](../icons/pubmethod.gif)|
[NewInstanceGuid(Guid)](M_Grasshopper_Kernel_IGH_InstanceDescription_NewInstanceGuid_1.htm)|
Set the instance ID to be a specific GUID. This is very dangerous, only use
this function if you're 6"4' and called David.  (Inherited from
[IGH_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).)  
![Public method](../icons/pubmethod.gif)|
[OnAttributesChanged](M_Grasshopper_Kernel_IGH_DocumentObject_OnAttributesChanged.htm)|
Raises the AttributesChanged event on the toplevel object.  
![Public method](../icons/pubmethod.gif)|
[OnDisplayExpired](M_Grasshopper_Kernel_IGH_DocumentObject_OnDisplayExpired.htm)|
Raises the DisplayExpired event on the toplevel object.  
![Public method](../icons/pubmethod.gif)|
[OnObjectChanged(GH_ObjectChangedEventArgs)](M_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged.htm)|
Raises the ObjectChanged event on the current (!not the top level!) object.  
![Public method](../icons/pubmethod.gif)|
[OnObjectChanged(GH_ObjectEventType)](M_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged_1.htm)|
Raises the ObjectChanged event on the current (!not the top level!) object.  
![Public method](../icons/pubmethod.gif)|
[OnObjectChanged(String)](M_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged_3.htm)|
Raises the ObjectChanged event on the current (!not the top level!) object.  
![Public method](../icons/pubmethod.gif)| [OnObjectChanged(GH_ObjectEventType,
Object)](M_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged_2.htm)|
Raises the ObjectChanged event on the current (!not the top level!) object.  
![Public method](../icons/pubmethod.gif)| [OnObjectChanged(String,
Object)](M_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged_4.htm)|
Raises the ObjectChanged event on the current (!not the top level!) object.  
![Public method](../icons/pubmethod.gif)|
[OnPingDocument](M_Grasshopper_Kernel_IGH_DocumentObject_OnPingDocument.htm)|
Raise the PingDocument Event on the toplevel object and try to find the
document which owns this object.  
![Public method](../icons/pubmethod.gif)|
[OnPreviewExpired](M_Grasshopper_Kernel_IGH_DocumentObject_OnPreviewExpired.htm)|
Raises the PreviewExpired event on the toplevel object.  
![Public method](../icons/pubmethod.gif)|
[OnSolutionExpired](M_Grasshopper_Kernel_IGH_DocumentObject_OnSolutionExpired.htm)|
Raises the SolutionExpired event on the toplevel object.  
![Public method](../icons/pubmethod.gif)|
[RecordUndoEvent(GH_UndoRecord)](M_Grasshopper_Kernel_IGH_DocumentObject_RecordUndoEvent.htm)|
Record an entire undo record.  
![Public method](../icons/pubmethod.gif)|
[RecordUndoEvent(String)](M_Grasshopper_Kernel_IGH_DocumentObject_RecordUndoEvent_1.htm)|
Record a generic object change undo event.  
![Public method](../icons/pubmethod.gif)| [RecordUndoEvent(String,
IGH_UndoAction)](M_Grasshopper_Kernel_IGH_DocumentObject_RecordUndoEvent_2.htm)|
Record a specific object change undo event.  
![Public method](../icons/pubmethod.gif)|
[RemovedFromDocument](M_Grasshopper_Kernel_IGH_DocumentObject_RemovedFromDocument.htm)|
This method will be called when an object is removed from a document.  
![Public method](../icons/pubmethod.gif)|
[TriggerAutoSave](M_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave.htm)|
Triggers the AutoSave function on the owner document with the object_changed
flag.  
![Public method](../icons/pubmethod.gif)|
[TriggerAutoSave(GH_AutoSaveTrigger)](M_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave_1.htm)|
Triggers the AutoSave function on the owner document with a custom flag.  
![Public method](../icons/pubmethod.gif)|
[TriggerAutoSave(Guid)](M_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave_3.htm)|
Triggers the AutoSave function on the owner document with the object_changed
flag.  
![Public method](../icons/pubmethod.gif)| [TriggerAutoSave(GH_AutoSaveTrigger,
Guid)](M_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave_2.htm)|
Triggers the AutoSave function on the owner document with a custom flag.  
Top

![](../icons/SectionExpanded.png)Events

| Name| Description  
---|---|---  
![Public event](../icons/pubevent.gif)|
[AttributesChanged](E_Grasshopper_Kernel_IGH_DocumentObject_AttributesChanged.htm)|
Raised whenever the number or kind of attributes changes. This event is
handled by GH_Documents who subsequently wipe their attribute caches.  
![Public event](../icons/pubevent.gif)|
[DisplayExpired](E_Grasshopper_Kernel_IGH_DocumentObject_DisplayExpired.htm)|
Raised whenever the display (on the Canvas) of a certain object becomes
invalid.  
![Public event](../icons/pubevent.gif)|
[ObjectChanged](E_Grasshopper_Kernel_IGH_DocumentObject_ObjectChanged.htm)|
Raised whenever some property of the object changes that would affect remote
instances.  
![Public event](../icons/pubevent.gif)|
[PingDocument](E_Grasshopper_Kernel_IGH_DocumentObject_PingDocument.htm)|
Raised whenever an object needs to know which GH_Document it belongs to.  
![Public event](../icons/pubevent.gif)|
[PreviewExpired](E_Grasshopper_Kernel_IGH_DocumentObject_PreviewExpired.htm)|
Raised whenever the display (in the Rhino viewports) of a certain object
becomes invalid.  
![Public event](../icons/pubevent.gif)|
[SolutionExpired](E_Grasshopper_Kernel_IGH_DocumentObject_SolutionExpired.htm)|
Raised whenever the solution of a certain object becomes invalid.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

