---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_DocumentObject.htm
scraped_at: 2025-09-08T16:16:29.322546
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_DocumentObject Class](../html/T_Grasshopper_Kernel_GH_DocumentObject.htm
"GH_DocumentObject Class")

[GH_DocumentObject Constructor
](../html/Overload_Grasshopper_Kernel_GH_DocumentObject__ctor.htm
"GH_DocumentObject Constructor ")

[GH_DocumentObject
Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocumentObject.htm
"GH_DocumentObject Properties")

[GH_DocumentObject
Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentObject.htm
"GH_DocumentObject Methods")

[GH_DocumentObject
Events](../html/Events_T_Grasshopper_Kernel_GH_DocumentObject.htm
"GH_DocumentObject Events")

[GH_DocumentObject
Fields](../html/Fields_T_Grasshopper_Kernel_GH_DocumentObject.htm
"GH_DocumentObject Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_DocumentObject Class  
  
---  
  
Standard implementation of IGH_DocumentObject.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.KernelGH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm)  
Grasshopper.KernelGH_DocumentObject  
[Grasshopper.KernelGH_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm)  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public abstract class GH_DocumentObject : GH_InstanceDescription, 
    	IGH_DocumentObject
    
    
    Public MustInherit Class GH_DocumentObject
    	Inherits GH_InstanceDescription
    	Implements IGH_DocumentObject

The GH_DocumentObject type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[GH_DocumentObject(IGH_InstanceDescription)](M_Grasshopper_Kernel_GH_DocumentObject__ctor.htm)|
Initializes a new instance of the GH_DocumentObject class  
![Protected method](../icons/protmethod.gif)| [GH_DocumentObject(String,
String, String, String,
String)](M_Grasshopper_Kernel_GH_DocumentObject__ctor_1.htm)| Initializes a
new instance of the GH_DocumentObject class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Attributes](P_Grasshopper_Kernel_GH_DocumentObject_Attributes.htm)|  Gets or
sets the attributes that are associated with this object. Only set custom
attributes if you know what you are doing.  
![Public property](../icons/pubproperty.gif)|
[Category](P_Grasshopper_Kernel_GH_InstanceDescription_Category.htm)|  Gets or
sets the Category in which this object belongs. If HasCategory() returns
false, this field has no meaning.  (Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[ComponentGuid](P_Grasshopper_Kernel_GH_DocumentObject_ComponentGuid.htm)|
Returns a consistent ID for this object type. Every object must supply a
unique and unchanging ID that is used to identify objects of the same type.  
![Public property](../icons/pubproperty.gif)|
[Description](P_Grasshopper_Kernel_GH_InstanceDescription_Description.htm)|
Gets or sets the description of the object. This field typically remains fixed
during the lifetime of an object.  (Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[Exposure](P_Grasshopper_Kernel_GH_DocumentObject_Exposure.htm)|  Gets the
exposure of this object in the Graphical User Interface. The default is to
expose everywhere.  
![Public property](../icons/pubproperty.gif)|
[HasCategory](P_Grasshopper_Kernel_GH_InstanceDescription_HasCategory.htm)|
Gets whether or not the Category field has been set.  (Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[HasSubCategory](P_Grasshopper_Kernel_GH_InstanceDescription_HasSubCategory.htm)|
Gets whether or not the SubCategory field has been set.  (Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Protected property](../icons/protproperty.gif)|
[Icon](P_Grasshopper_Kernel_GH_DocumentObject_Icon.htm)|  Override this
function to supply a custom icon (24x24 pixels). The result of this property
is cached, so don't worry if icon retrieval is not very fast.  
![Public property](../icons/pubproperty.gif)|
[Icon_24x24](P_Grasshopper_Kernel_GH_DocumentObject_Icon_24x24.htm)|  The icon
associated with this object.  
![Public property](../icons/pubproperty.gif)|
[Icon_24x24_Locked](P_Grasshopper_Kernel_GH_DocumentObject_Icon_24x24_Locked.htm)|
The greyscale icon of this object.  
![Public property](../icons/pubproperty.gif)|
[IconDisplayMode](P_Grasshopper_Kernel_GH_DocumentObject_IconDisplayMode.htm)|
Gets the current display mode of the object.  
![Public property](../icons/pubproperty.gif)|
[InstanceDescription](P_Grasshopper_Kernel_GH_InstanceDescription_InstanceDescription.htm)|
Gets a description of the current state of the object. This field is usually
the same as the Description() field, but it might be variable when overridden.
(Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[InstanceGuid](P_Grasshopper_Kernel_GH_InstanceDescription_InstanceGuid.htm)|
Gets the ID of this runtime instance.  (Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[Keywords](P_Grasshopper_Kernel_GH_InstanceDescription_Keywords.htm)|  Gets a
list of additional keywords that describe the object. Typically this list is
empty but you can override this property to aid in object searches.
(Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
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
adding the ObsoleteAttribute instead.  
![Public property](../icons/pubproperty.gif)|
[SubCategory](P_Grasshopper_Kernel_GH_InstanceDescription_SubCategory.htm)|
Gets or sets the SubCategory in which this object belongs. If HasSubCategory()
returns false, this field has no meaning.  (Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AddedToDocument](M_Grasshopper_Kernel_GH_DocumentObject_AddedToDocument.htm)|
This method will be called when an object is added to a document. Override
this method if you want to handle such events.  
![Public method](../icons/pubmethod.gif)|
[AppendMenuItems](M_Grasshopper_Kernel_GH_DocumentObject_AppendMenuItems.htm)|
This function is called when a context menu is about to be displayed. Override
it to set custom items.  
![Public method](../icons/pubmethod.gif)|
[CopyFrom](M_Grasshopper_Kernel_GH_InstanceDescription_CopyFrom.htm)|  Copy
all fields (except the instance ID) from another instance description.
(Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public method](../icons/pubmethod.gif)|
[CreateAttributes](M_Grasshopper_Kernel_GH_DocumentObject_CreateAttributes.htm)|
This function creates the stand-alone attributes for this object. If you wish
to supply your own Attributes, you must override this function.  
![Protected method](../icons/protmethod.gif)|
[DestroyIconCache](M_Grasshopper_Kernel_GH_DocumentObject_DestroyIconCache.htm)|
Call this method to erase the existing icon cache. You must call this if you
want to change the display icon of an object.  
![Public method](../icons/pubmethod.gif)|
[DocumentContextChanged](M_Grasshopper_Kernel_GH_DocumentObject_DocumentContextChanged.htm)|
This method will be called when the document that owns this object moves into
a different context.  
![Public method](../icons/pubmethod.gif)|
[ExpirePreview](M_Grasshopper_Kernel_GH_DocumentObject_ExpirePreview.htm)|
Call this function when you suspect that the preview has expired for this
object. This will cause the display cache to be eradicated.  
![Public method](../icons/pubmethod.gif)|
[ExpireSolution](M_Grasshopper_Kernel_GH_DocumentObject_ExpireSolution.htm)|
Call this function whenever you do something which expires the current
solution. This will make sure all caches are erased, all downstream objects
are expired and that the event is raised. The default implementation merely
places a call to OnSolutionExpired(), override this function in derived
classes to make sure you clear local data caches and expire downstream
objects.  
![Protected method](../icons/protmethod.gif)| [GetValue(String,
Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue.htm)|  Get a boolean
value from the component value table.  
![Protected method](../icons/protmethod.gif)| [GetValue(String,
Double)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue_1.htm)|  Get a double
value from the component value table.  
![Protected method](../icons/protmethod.gif)| [GetValue(String,
Color)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue_2.htm)|  Get a color
value from the component value table.  
![Protected method](../icons/protmethod.gif)| [GetValue(String,
Int32)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue_3.htm)|  Get an
integer value from the component value table.  
![Protected method](../icons/protmethod.gif)| [GetValue(String,
String)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue_4.htm)|  Get a string
value from the component value table.  
![Protected method](../icons/protmethod.gif)|
[HtmlHelp_Source](M_Grasshopper_Kernel_GH_DocumentObject_HtmlHelp_Source.htm)|
Return a String which contains HTML formatted source for the help topic. If
you want to pass a URL that points to a remote page, then prefix the URL with
a GOTO: tag, like so: GOTO:http://www.YourWebAddressHere.com  
![Public method](../icons/pubmethod.gif)|
[IsolateObject](M_Grasshopper_Kernel_GH_DocumentObject_IsolateObject.htm)|
Destroy all connections to other objects.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Menu_AppendColourPicker](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendColourPicker.htm)|
Add a colour picker to a menu.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Menu_AppendCustomItem(ToolStripDropDown,
Control)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendCustomItem.htm)|
Utility function for inserting exotic controls into dropdown menus.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Menu_AppendCustomItem(ToolStripDropDown, Control,
KeyDownEventHandler)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendCustomItem_1.htm)|
Utility function for inserting exotic controls into dropdown menus.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Menu_AppendCustomItem(ToolStripDropDown, Control, KeyDownEventHandler,
Boolean, Int32,
Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendCustomItem_2.htm)|
Utility function for inserting exotic controls into dropdown menus.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Menu_AppendDigitScrollerItem](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendDigitScrollerItem.htm)|
Utility function for inserting a digit scroller into menus.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Menu_AppendItem(ToolStrip,
String)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem.htm)|  Utility
function for appending generic menu items.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Menu_AppendItem(ToolStrip, String,
EventHandler)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem_1.htm)|
Utility function for appending generic menu items.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Menu_AppendItem(ToolStrip, String, EventHandler,
Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem_2.htm)|
Utility function for appending generic menu items.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Menu_AppendItem(ToolStrip, String, EventHandler,
Image)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem_4.htm)|
Utility function for appending generic menu items.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Menu_AppendItem(ToolStrip, String, EventHandler, Boolean,
Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem_3.htm)|
Utility function for appending generic menu items.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Menu_AppendItem(ToolStrip, String, EventHandler, Image,
Object)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem_6.htm)|
Utility function for appending generic menu items.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Menu_AppendItem(ToolStrip, String, EventHandler, Image, Boolean,
Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem_5.htm)|
Utility function for appending generic menu items.  
![Protected method](../icons/protmethod.gif)|
[Menu_AppendObjectHelp](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendObjectHelp.htm)|
Appends the default object Help menu item.  
![Protected method](../icons/protmethod.gif)|
[Menu_AppendObjectName](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendObjectName.htm)|
Appends the old-fashioned object name menu item. If you also want the Display
mode toggle then use Menu_AppendObjectNameEx()  
![Protected method](../icons/protmethod.gif)|
[Menu_AppendObjectNameEx](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendObjectNameEx.htm)|
Appends the default object name + display mode menu item.  
![Protected method](../icons/protmethod.gif)|
[Menu_AppendPublish](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendPublish.htm)|
Appends the default item for publishing to RCP. This menu will only appear if
the current class implement IRcpAwareObject  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Menu_AppendSeparator](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendSeparator.htm)|
Utility function for appending separators to a menu dropdown. If the dropdown
is empty or if it already has a separator at the bottom, nothing will happen.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Menu_AppendTextItem(ToolStripDropDown, String,
GH_MenuTextBoxKeyDownEventHandler, GH_MenuTextBoxTextChangedEventHandler,
Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendTextItem.htm)|
Utility function for inserting text boxes into menus.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Menu_AppendTextItem(ToolStripDropDown, String,
GH_MenuTextBoxKeyDownEventHandler, GH_MenuTextBoxTextChangedEventHandler,
Boolean, Int32,
Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendTextItem_1.htm)|
Utility function for inserting text boxes into menus.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Menu_MoveItem(ToolStripItem,
String)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_MoveItem_1.htm)|  Utility
function for moving menu items.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Menu_MoveItem(ToolStripItem, Boolean,
String)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_MoveItem.htm)|  Utility
function for moving menu items.  
![Public method](../icons/pubmethod.gif)|
[MovedBetweenDocuments](M_Grasshopper_Kernel_GH_DocumentObject_MovedBetweenDocuments.htm)|
This method will be called when an object is moved from one document to
another. Override this method if you want to handle such events.  
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
Raises the AttributesChanged event on the toplevel object.  
![Public method](../icons/pubmethod.gif)|
[OnDisplayExpired](M_Grasshopper_Kernel_GH_DocumentObject_OnDisplayExpired.htm)|
Raises the DisplayExpired event on the toplevel object.  
![Public method](../icons/pubmethod.gif)|
[OnObjectChanged(GH_ObjectChangedEventArgs)](M_Grasshopper_Kernel_GH_DocumentObject_OnObjectChanged.htm)|  
![Public method](../icons/pubmethod.gif)|
[OnObjectChanged(GH_ObjectEventType)](M_Grasshopper_Kernel_GH_DocumentObject_OnObjectChanged_1.htm)|  
![Public method](../icons/pubmethod.gif)|
[OnObjectChanged(String)](M_Grasshopper_Kernel_GH_DocumentObject_OnObjectChanged_3.htm)|  
![Public method](../icons/pubmethod.gif)| [OnObjectChanged(GH_ObjectEventType,
Object)](M_Grasshopper_Kernel_GH_DocumentObject_OnObjectChanged_2.htm)|  
![Public method](../icons/pubmethod.gif)| [OnObjectChanged(String,
Object)](M_Grasshopper_Kernel_GH_DocumentObject_OnObjectChanged_4.htm)|  
![Public method](../icons/pubmethod.gif)|
[OnPingDocument](M_Grasshopper_Kernel_GH_DocumentObject_OnPingDocument.htm)|
Raise the PingDocument Event on the toplevel object and try to find the
document which owns this object.  
![Public method](../icons/pubmethod.gif)|
[OnPreviewExpired](M_Grasshopper_Kernel_GH_DocumentObject_OnPreviewExpired.htm)|
Raises the PreviewExpired event on the toplevel object.  
![Public method](../icons/pubmethod.gif)|
[OnSolutionExpired](M_Grasshopper_Kernel_GH_DocumentObject_OnSolutionExpired.htm)|
Raises the SolutionExpired event on the toplevel object. You probably want to
call ExpireSolution() instead of this method directly.  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_GH_DocumentObject_Read.htm)|  (Overrides
[GH_InstanceDescriptionRead(GH_IReader)](M_Grasshopper_Kernel_GH_InstanceDescription_Read.htm).)  
![Public method](../icons/pubmethod.gif)|
[ReadFull](M_Grasshopper_Kernel_GH_InstanceDescription_ReadFull.htm)|
GH_InstanceDescription does not by default serialize all fields. Use this
function to read _all_ fields from the archive. This method is compatible with
the default Write()/Read() operations.  (Inherited from
[GH_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).)  
![Public method](../icons/pubmethod.gif)|
[RecordUndoEvent(GH_UndoRecord)](M_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent.htm)|
Record an entire undo record.  
![Public method](../icons/pubmethod.gif)|
[RecordUndoEvent(String)](M_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent_1.htm)|
Record a generic object change undo event.  
![Public method](../icons/pubmethod.gif)| [RecordUndoEvent(String,
IGH_UndoAction)](M_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent_2.htm)|
Record a specific object change undo event.  
![Public method](../icons/pubmethod.gif)|
[RemovedFromDocument](M_Grasshopper_Kernel_GH_DocumentObject_RemovedFromDocument.htm)|
This method will be called when an object is removed from a document. Override
this method if you want to handle such events.  
![Public method](../icons/pubmethod.gif)|
[SetIconOverride](M_Grasshopper_Kernel_GH_DocumentObject_SetIconOverride.htm)|
Set a new custom icon override for this object.  
![Protected method](../icons/protmethod.gif)| [SetValue(String,
Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue.htm)|  Set a named
value. This value will be serialized with the component.  
![Protected method](../icons/protmethod.gif)| [SetValue(String,
Double)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue_1.htm)|  Set a named
value. This value will be serialized with the component.  
![Protected method](../icons/protmethod.gif)| [SetValue(String,
Color)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue_2.htm)|  Set a named
value. This value will be serialized with the component.  
![Protected method](../icons/protmethod.gif)| [SetValue(String,
Int32)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue_3.htm)|  Set a named
value. This value will be serialized with the component.  
![Protected method](../icons/protmethod.gif)| [SetValue(String,
String)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue_4.htm)|  Set a named
value. This value will be serialized with the component.  
![Public method](../icons/pubmethod.gif)|
[TriggerAutoSave](M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave.htm)|
Triggers the AutoSave function on the owner document with the object_changed
flag.  
![Public method](../icons/pubmethod.gif)|
[TriggerAutoSave(GH_AutoSaveTrigger)](M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave_1.htm)|
Triggers the AutoSave function on the owner document with a custom flag.  
![Public method](../icons/pubmethod.gif)|
[TriggerAutoSave(Guid)](M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave_3.htm)|
Triggers the AutoSave function on the owner document with the object_changed
flag.  
![Public method](../icons/pubmethod.gif)| [TriggerAutoSave(GH_AutoSaveTrigger,
Guid)](M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave_2.htm)|
Triggers the AutoSave function on the owner document with a custom flag.  
![Protected method](../icons/protmethod.gif)|
[ValuesChanged](M_Grasshopper_Kernel_GH_DocumentObject_ValuesChanged.htm)|
Override this method if you want to respond to changes to the value table. The
base implementation is empty, so you don't have to call it.  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_GH_DocumentObject_Write.htm)|  (Overrides
[GH_InstanceDescriptionWrite(GH_IWriter)](M_Grasshopper_Kernel_GH_InstanceDescription_Write.htm).)  
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
![Public event](../icons/pubevent.gif)|
[DisplayExpired](E_Grasshopper_Kernel_GH_DocumentObject_DisplayExpired.htm)|
Raised whenever the display (on the Canvas) of a certain object becomes
invalid.  
![Public event](../icons/pubevent.gif)|
[ObjectChanged](E_Grasshopper_Kernel_GH_DocumentObject_ObjectChanged.htm)|  
![Public event](../icons/pubevent.gif)|
[PingDocument](E_Grasshopper_Kernel_GH_DocumentObject_PingDocument.htm)|
Raised whenever an object needs to know which GH_Document it belongs to.  
![Public event](../icons/pubevent.gif)|
[PreviewExpired](E_Grasshopper_Kernel_GH_DocumentObject_PreviewExpired.htm)|
Raised whenever the display (in the Rhino viewports) of a certain object
becomes invalid.  
![Public event](../icons/pubevent.gif)|
[SolutionExpired](E_Grasshopper_Kernel_GH_DocumentObject_SolutionExpired.htm)|
Raised whenever the solution of a certain object becomes invalid.  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Protected field](../icons/protfield.gif)|
[m_attributes](F_Grasshopper_Kernel_GH_DocumentObject_m_attributes.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

