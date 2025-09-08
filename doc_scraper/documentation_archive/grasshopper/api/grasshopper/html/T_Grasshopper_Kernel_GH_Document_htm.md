---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_Document.htm
scraped_at: 2025-09-08T16:16:09.272322
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_Document Class](../html/T_Grasshopper_Kernel_GH_Document.htm "GH_Document
Class")

[GH_Document Constructor ](../html/M_Grasshopper_Kernel_GH_Document__ctor.htm
"GH_Document Constructor ")

[GH_Document
Properties](../html/Properties_T_Grasshopper_Kernel_GH_Document.htm
"GH_Document Properties")

[GH_Document Methods](../html/Methods_T_Grasshopper_Kernel_GH_Document.htm
"GH_Document Methods")

[GH_Document Events](../html/Events_T_Grasshopper_Kernel_GH_Document.htm
"GH_Document Events")

[GH_Document Fields](../html/Fields_T_Grasshopper_Kernel_GH_Document.htm
"GH_Document Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Document Class  
  
---  
  
Represents a single Grasshopper document.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_Document  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class GH_Document : GH_ISerializable, 
    	IDisposable, IComparable<GH_Document>, IGH_DebugDescription
    
    
    Public NotInheritable Class GH_Document
    	Implements GH_ISerializable, IDisposable, IComparable(Of GH_Document), 
    	IGH_DebugDescription

The GH_Document type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_Document](M_Grasshopper_Kernel_GH_Document__ctor.htm)|  Constructor for
GH_Document. Makes sure all important members are initialized.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[AbortRequested](P_Grasshopper_Kernel_GH_Document_AbortRequested.htm)|  Gets
the abortrequested flag state.  
![Public property](../icons/pubproperty.gif)|
[ActiveDoc](P_Grasshopper_Kernel_GH_Document_ActiveDoc.htm)|  Gets or sets a
value indicating that this document was last active in a multi-doc aware
Rhino.  
![Public property](../icons/pubproperty.gif)|
[AttributeCount](P_Grasshopper_Kernel_GH_Document_AttributeCount.htm)|
Returns the total number of attributes in the document. Both Normal and Hidden
ones  
![Public property](../icons/pubproperty.gif)|
[Attributes](P_Grasshopper_Kernel_GH_Document_Attributes.htm)|  Returns a list
of all the attributes in this document. This includes attributes for nested
objects such as input or output parameters.  
![Public property](../icons/pubproperty.gif)|
[Author](P_Grasshopper_Kernel_GH_Document_Author.htm)|  Gets the author
details associated with this document.  
![Public property](../icons/pubproperty.gif)|
[ConstantServer](P_Grasshopper_Kernel_GH_Document_ConstantServer.htm)|  Gets
the dictionary of constants defined in this document.  
![Public property](../icons/pubproperty.gif)|
[Context](P_Grasshopper_Kernel_GH_Document_Context.htm)|  Gets or sets the
context for this document. Note that the context is not a state so much as an
action. Therefore it is not particularly useful to read the context after the
fact, rather, context is mostly intended to be a setter, not a getter. When
you set the context, all top-level document objects will be informed and the
ContextChanged event will be raised.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[DefaultPreviewColour](P_Grasshopper_Kernel_GH_Document_DefaultPreviewColour.htm)|
Gets or sets the default preview colour for normal objects.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[DefaultSelectedPreviewColour](P_Grasshopper_Kernel_GH_Document_DefaultSelectedPreviewColour.htm)|
Gets or sets the default preview colour for normal objects.  
![Public property](../icons/pubproperty.gif)|
[DisplayName](P_Grasshopper_Kernel_GH_Document_DisplayName.htm)|  Gets the
display name for this document. The display name is highly context sensitive
and is only supposed to give the user a good idea of which document this is
and whether it has been modified.  
![Public property](../icons/pubproperty.gif)|
[DocumentID](P_Grasshopper_Kernel_GH_Document_DocumentID.htm)|  Gets the
document Id. The Id is assigned at construction and never changed. Note:
clusters may choose to modify the Id of their internal documents.  
![Public property](../icons/pubproperty.gif)|
[Enabled](P_Grasshopper_Kernel_GH_Document_Enabled.htm)|  Gets or sets the
enabled state for this document. Enabled documents respond to events and
display their previews in the Rhino viewport.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[EnableSolutions](P_Grasshopper_Kernel_GH_Document_EnableSolutions.htm)|  Gets
or sets a global variable that indicates whether solutions are allowed to be
recomputed. When this flag is off, the solver will be disabled and the event
watchers should be silent.  
![Public property](../icons/pubproperty.gif)|
[EventServer](P_Grasshopper_Kernel_GH_Document_EventServer.htm)|  Gets the
event server that belongs to this document. The Event server may be in an
inactive state, but it is never null.  
![Public property](../icons/pubproperty.gif)|
[FilePath](P_Grasshopper_Kernel_GH_Document_FilePath.htm)|  Gets or sets the
file path of this document. If the file path is not set Nothing is returned.  
![Public property](../icons/pubproperty.gif)|
[IgnoredCount](P_Grasshopper_Kernel_GH_Document_IgnoredCount.htm)|  Returns
the total numbers of components currently in the Object Exception Ignore List.  
![Public property](../icons/pubproperty.gif)|
[IsFilePathDefined](P_Grasshopper_Kernel_GH_Document_IsFilePathDefined.htm)|
Returns True if the filename flag of this document has been set  
![Public property](../icons/pubproperty.gif)|
[IsModified](P_Grasshopper_Kernel_GH_Document_IsModified.htm)|  Gets or sets
the modified flag. If the new value differs from the old value, the
ModifiedChanged() event is raised.  
![Public property](../icons/pubproperty.gif)|
[ModifiedSubsidiaries](P_Grasshopper_Kernel_GH_Document_ModifiedSubsidiaries.htm)|
Gets the number of modified subsidiary documents.  
![Public property](../icons/pubproperty.gif)|
[Nested](P_Grasshopper_Kernel_GH_Document_Nested.htm)|  Gets or sets whether
this document is nested. A nested document is always part of some other
document and is therefore unknown to the DocumentServer and the Canvas.  
![Public property](../icons/pubproperty.gif)|
[ObjectCount](P_Grasshopper_Kernel_GH_Document_ObjectCount.htm)|  Returns the
total number of top-level objects in the document.  
![Public property](../icons/pubproperty.gif)|
[Objects](P_Grasshopper_Kernel_GH_Document_Objects.htm)|  Returns a list of
all normal, top-level objects.  
![Public property](../icons/pubproperty.gif)|
[ObjectSpan](P_Grasshopper_Kernel_GH_Document_ObjectSpan.htm)|  Gets the total
timespan for all objects.  
![Public property](../icons/pubproperty.gif)|
[Owner](P_Grasshopper_Kernel_GH_Document_Owner.htm)|  Gets or sets the owner
of this document. A document is typically owned when it is subsidiary to some
object, such as a cluster.  
![Public property](../icons/pubproperty.gif)|
[PreviewBoundary](P_Grasshopper_Kernel_GH_Document_PreviewBoundary.htm)|  Gets
or sets the preview boundary applied to this document. If a boundary has been
set, only those objects which are inside the boundary will be previewed.  
![Public property](../icons/pubproperty.gif)|
[PreviewBoundingBox](P_Grasshopper_Kernel_GH_Document_PreviewBoundingBox.htm)|
Gets the boundingbox used for previews.  
![Public property](../icons/pubproperty.gif)|
[PreviewColour](P_Grasshopper_Kernel_GH_Document_PreviewColour.htm)|  Gets or
sets the colour of unselected preview geometry.  
![Public property](../icons/pubproperty.gif)|
[PreviewColourSelected](P_Grasshopper_Kernel_GH_Document_PreviewColourSelected.htm)|
Gets or sets the colour of selected preview geometry.  
![Public property](../icons/pubproperty.gif)|
[PreviewCustomMeshParameters](P_Grasshopper_Kernel_GH_Document_PreviewCustomMeshParameters.htm)|
Gets or sets the Custom Meshing Parameters for this document, these are only
used when PreviewMeshType = GH_PreviewMesh.Custom  
![Public property](../icons/pubproperty.gif)|
[PreviewFilter](P_Grasshopper_Kernel_GH_Document_PreviewFilter.htm)|  Gets or
set the preview filter.  
![Public property](../icons/pubproperty.gif)|
[PreviewMeshType](P_Grasshopper_Kernel_GH_Document_PreviewMeshType.htm)|  Gets
or sets the preview mesh type for this document.  
![Public property](../icons/pubproperty.gif)|
[PreviewMode](P_Grasshopper_Kernel_GH_Document_PreviewMode.htm)|  Gets or sets
the preview display mode and makes sure the conduit instance of this class is
set to match.  
![Public property](../icons/pubproperty.gif)|
[Profiler](P_Grasshopper_Kernel_GH_Document_Profiler.htm)|  Gets or sets the
profiler mode used in this document.  
![Public property](../icons/pubproperty.gif)|
[Properties](P_Grasshopper_Kernel_GH_Document_Properties.htm)|  The properties
of this document  
![Public property](../icons/pubproperty.gif)|
[RaiseEvents](P_Grasshopper_Kernel_GH_Document_RaiseEvents.htm)|  If
RaiseEvents is set to false, all the On....() methods of this document will
stop raising events.  
![Public property](../icons/pubproperty.gif)|
[RemotePanelLayout](P_Grasshopper_Kernel_GH_Document_RemotePanelLayout.htm)|
Gets the Remote Control Panel layout for this document.  
![Public property](../icons/pubproperty.gif)|
[RhinoDocument](P_Grasshopper_Kernel_GH_Document_RhinoDocument.htm)|  
![Public property](../icons/pubproperty.gif)|
[RuntimeID](P_Grasshopper_Kernel_GH_Document_RuntimeID.htm)|  Gets the runtime
ID of this document. RuntimeID is assigned once and never changed. It is also
not deserialized so every document will always have a unique ID when loaded.  
![Public property](../icons/pubproperty.gif)|
[ScheduleDelay](P_Grasshopper_Kernel_GH_Document_ScheduleDelay.htm)|  Gets the
delay for the next scheduled solution. If there is no solution scheduled the
delay will be negative.  
![Public property](../icons/pubproperty.gif)|
[SelectedCount](P_Grasshopper_Kernel_GH_Document_SelectedCount.htm)|  Gets the
number of selected objects  
![Public property](../icons/pubproperty.gif)|
[SelectionTopology](P_Grasshopper_Kernel_GH_Document_SelectionTopology.htm)|
Gets the selection topology of the document.  
![Public property](../icons/pubproperty.gif)|
[SolutionDepth](P_Grasshopper_Kernel_GH_Document_SolutionDepth.htm)|  Gets the
number of nested solutions currently running. If no solutions are running, the
depth should be zero. If one solution is runnnig, the depth should be one.
Higher depths are only possible if a new solution was scheduled from within an
existing solution with delay=0ms.  
![Public property](../icons/pubproperty.gif)|
[SolutionHistory](P_Grasshopper_Kernel_GH_Document_SolutionHistory.htm)|  Gets
a list of the last 1000 solution timespans, from oldest to youngest.  
![Public property](../icons/pubproperty.gif)|
[SolutionSpan](P_Grasshopper_Kernel_GH_Document_SolutionSpan.htm)|  Gets the
timespan for the most recent solution.  
![Public property](../icons/pubproperty.gif)|
[SolutionState](P_Grasshopper_Kernel_GH_Document_SolutionState.htm)|  Gets the
state of this document.  
![Public property](../icons/pubproperty.gif)|
[StateServer](P_Grasshopper_Kernel_GH_Document_StateServer.htm)|  Gets the
list of stored states in this document  
![Public property](../icons/pubproperty.gif)|
[Thumbnail](P_Grasshopper_Kernel_GH_Document_Thumbnail.htm)|  Gets or sets the
thumbnail bitmap for this document.  
![Public property](../icons/pubproperty.gif)|
[UndoServer](P_Grasshopper_Kernel_GH_Document_UndoServer.htm)|  Gets the
UndoServer instance that belongs to this document.  
![Public property](../icons/pubproperty.gif)|
[UndoUtil](P_Grasshopper_Kernel_GH_Document_UndoUtil.htm)|  Gets a temporary
undo utility instance that allows you to easily create standard undo events.  
![Public property](../icons/pubproperty.gif)|
[ValueTable](P_Grasshopper_Kernel_GH_Document_ValueTable.htm)|  Gets the value
table associated with this document.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ActiveObjects](M_Grasshopper_Kernel_GH_Document_ActiveObjects.htm)|  Returns
all normal objects in the document that implement the IGH_ActiveObject
interface  
![Public method](../icons/pubmethod.gif)|
[AddObject](M_Grasshopper_Kernel_GH_Document_AddObject.htm)|  Add a new object
to the document. If the object is already contained, nothing will happen  
![Public method](../icons/pubmethod.gif)| [AlignObjects(GH_Align,
GH_Distribute)](M_Grasshopper_Kernel_GH_Document_AlignObjects.htm)|  Perform
alignment and distribution logic on all selected objects.  
![Public method](../icons/pubmethod.gif)| [AlignObjects(GH_Align,
GH_Distribute,
ListIGH_DocumentObject)](M_Grasshopper_Kernel_GH_Document_AlignObjects_1.htm)|
Perform alignment and distribution logic on a set of objects.  
![Public method](../icons/pubmethod.gif)|
[AppendToDebugLog](M_Grasshopper_Kernel_GH_Document_AppendToDebugLog.htm)|
Useful for creating textual representations of this document for debugging
purposes.  
![Public method](../icons/pubmethod.gif)|
[ArrangeObject](M_Grasshopper_Kernel_GH_Document_ArrangeObject.htm)|
Rearrange the stack order of the object.  
![Public method](../icons/pubmethod.gif)|
[ArrangeObjects](M_Grasshopper_Kernel_GH_Document_ArrangeObjects.htm)|
Rearrange the stack order of a collection of objects.  
![Public method](../icons/pubmethod.gif)|
[AssociateWithRhinoDocument](M_Grasshopper_Kernel_GH_Document_AssociateWithRhinoDocument.htm)|
Associate this GH_Document with the currently active Rhino document. This only
works if both the 3dm and the ghx file have been saved at least once.  
![Public method](../icons/pubmethod.gif)|
[AutoLayoutComponents](M_Grasshopper_Kernel_GH_Document_AutoLayoutComponents.htm)|
Perform automatic layout on this document.  
![Public method](../icons/pubmethod.gif)|
[AutoSave(GH_AutoSaveTrigger)](M_Grasshopper_Kernel_GH_Document_AutoSave.htm)|
Creates a new autosave file on the disk. The previous autosave file (assuming
it exists) will be temporarily renamed and eventually deleted entirely. Note:
AutoSave is only possible on Documents that have TopLevel Rank and a valid
FilePath.  
![Public method](../icons/pubmethod.gif)| [AutoSave(GH_AutoSaveTrigger,
Guid)](M_Grasshopper_Kernel_GH_Document_AutoSave_1.htm)|  Creates a new
autosave file on the disk. The previous autosave file (assuming it exists)
will be temporarily renamed and eventually deleted entirely. Note: AutoSave is
only possible on Documents that have TopLevel Rank and a valid FilePath.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[AutoSaveFileName](M_Grasshopper_Kernel_GH_Document_AutoSaveFileName.htm)|
Computes the autosave filename for a full grasshopper filepath.  
![Public method](../icons/pubmethod.gif)|
[BoundingBox](M_Grasshopper_Kernel_GH_Document_BoundingBox.htm)|  Returns the
boundingbox of all the normal attributes. If the document contains no normal
attributes an Empty RectangleF structure is returned.  
![Public method](../icons/pubmethod.gif)|
[BringSelectionToTop](M_Grasshopper_Kernel_GH_Document_BringSelectionToTop.htm)|
Move the selection set to the top of the visible stack  
![Public method](../icons/pubmethod.gif)|
[ClearIgnoreList](M_Grasshopper_Kernel_GH_Document_ClearIgnoreList.htm)|
Clears the Object Exception Ignore List.  
![Public method](../icons/pubmethod.gif)|
[ClearReferenceTable](M_Grasshopper_Kernel_GH_Document_ClearReferenceTable.htm)|
Destroys the Referenced object table in the Rhino event watcher. You must call
this function if you either add or remove a reference to a Rhino object.  
![Public method](../icons/pubmethod.gif)|
[CloseAllSubsidiaries](M_Grasshopper_Kernel_GH_Document_CloseAllSubsidiaries.htm)|
Iterate over all subsidiary documents and close them all without saving.  
![Public method](../icons/pubmethod.gif)|
[ClusterInputHooks](M_Grasshopper_Kernel_GH_Document_ClusterInputHooks.htm)|
Gets a sorted list of all the cluster input hooks.  
![Public method](../icons/pubmethod.gif)|
[ClusterInstanceCount](M_Grasshopper_Kernel_GH_Document_ClusterInstanceCount.htm)|
Counts the number of instances of a specific cluster document ID.  
![Public method](../icons/pubmethod.gif)|
[ClusterOutputHooks](M_Grasshopper_Kernel_GH_Document_ClusterOutputHooks.htm)|
Gets a sorted list of all the cluster output hooks.  
![Public method](../icons/pubmethod.gif)|
[CompareTo](M_Grasshopper_Kernel_GH_Document_CompareTo.htm)|  Compare two
documents. This function _does not_ compare document content.  
![Public method](../icons/pubmethod.gif)|
[ConstructDocumentTree](M_Grasshopper_Kernel_GH_Document_ConstructDocumentTree.htm)|
Create a hierarchical document tree of ownership with this document as the
root.  
![Public method](../icons/pubmethod.gif)|
[ContainsClusterHooks](M_Grasshopper_Kernel_GH_Document_ContainsClusterHooks.htm)|
Tests whether this document contains at least one cluster hook.  
![Public method](../icons/pubmethod.gif)|
[ConvertFullNamesToNickNames](M_Grasshopper_Kernel_GH_Document_ConvertFullNamesToNickNames.htm)|
Convert all nicknames to original nicknames if they are equal to the default
full name. There will be no undo record associated with this operation.  
![Public method](../icons/pubmethod.gif)|
[ConvertNickNamesToFullNames](M_Grasshopper_Kernel_GH_Document_ConvertNickNamesToFullNames.htm)|
Convert all nicknames to full names, if they are equal to the default
nickname. There will be no undo record associated with this operation.  
![Public method](../icons/pubmethod.gif)|
[CreateAutomaticClusterHooks](M_Grasshopper_Kernel_GH_Document_CreateAutomaticClusterHooks.htm)|
Add an input hook for every non-optional input parameter with no persistent
data and no sources. Then add an output hook for every floating parameter
without recipients, and for every first component output parameter where the
parent component has no recipients.  
![Public method](../icons/pubmethod.gif)|
[CreateConnectivityDiagram](M_Grasshopper_Kernel_GH_Document_CreateConnectivityDiagram.htm)|
Gets the connectivity diagram for the current state of this document.  
![Public method](../icons/pubmethod.gif)|
[CreateExpressionParser](M_Grasshopper_Kernel_GH_Document_CreateExpressionParser.htm)|
Create a new Expression Solver preloaded with the constants defined in this
document.  
![Public method](../icons/pubmethod.gif)|
[DefineConstant](M_Grasshopper_Kernel_GH_Document_DefineConstant.htm)|  Add a
new constant to the document. Constants are not case-sensitive, when you
define a constant with an existing name, the old one will be replaced. Note:
constants are as of yet unused. Eventually they are supposed to become
accessible to all expressions running inside a document.  
![Public method](../icons/pubmethod.gif)|
[DeselectAll](M_Grasshopper_Kernel_GH_Document_DeselectAll.htm)|  Deselect all
top-level attributes.  
![Public method](../icons/pubmethod.gif)|
[DestroyAttributeCache](M_Grasshopper_Kernel_GH_Document_DestroyAttributeCache.htm)|
Destroys the Attribute cache. Call this function whenever you do something
which might affect attributes.  
![Public method](../icons/pubmethod.gif)|
[DestroyAutoSaveFiles](M_Grasshopper_Kernel_GH_Document_DestroyAutoSaveFiles.htm)|
Destroys all autosave files and backup files that are associated with this
document. Only call this function when you are certain that the document has
been properly saved and no changes have occured since.  
![Public method](../icons/pubmethod.gif)|
[DestroyObjectTable](M_Grasshopper_Kernel_GH_Document_DestroyObjectTable.htm)|
Erase the Object fast lookup table. You _must_ call this whenever you add or
remove objects to or from the document while circumventing the regular
channels.  
![Public method](../icons/pubmethod.gif)|
[DestroyPreviewCaches](M_Grasshopper_Kernel_GH_Document_DestroyPreviewCaches.htm)|
Wipe all caches for Viewport Preview logic.  
![Public method](../icons/pubmethod.gif)|
[DestroyPreviewMeshes](M_Grasshopper_Kernel_GH_Document_DestroyPreviewMeshes.htm)|
Attempts to destroy all the preview meshes in this document. It might not work
for all objects, but this is still your best bet.  
![Public method](../icons/pubmethod.gif)|
[DestroyProxySources](M_Grasshopper_Kernel_GH_Document_DestroyProxySources.htm)|
Remove all remaining proxy sources from the document.  
![Public method](../icons/pubmethod.gif)|
[DisabledObjects](M_Grasshopper_Kernel_GH_Document_DisabledObjects.htm)|
Returns all disabled objects in the document  
![Public method](../icons/pubmethod.gif)|
[Dispose](M_Grasshopper_Kernel_GH_Document_Dispose.htm)|  When you discard
documents you must call Dispose or the Viewport Display event handlers will
not be disconnected.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[DuplicateDocument](M_Grasshopper_Kernel_GH_Document_DuplicateDocument.htm)|
Attempt to duplicate a document.  
![Public method](../icons/pubmethod.gif)|
[EnabledObjects](M_Grasshopper_Kernel_GH_Document_EnabledObjects.htm)|
Returns all enabled objects in the document  
![Public method](../icons/pubmethod.gif)|
[ExpandSelection](M_Grasshopper_Kernel_GH_Document_ExpandSelection.htm)|  Grow
or shift the selection set based on source and recipient links  
![Public method](../icons/pubmethod.gif)|
[ExpirePreview](M_Grasshopper_Kernel_GH_Document_ExpirePreview.htm)|  Expires
the preview caches of the conduit.  
![Public method](../icons/pubmethod.gif)|
[ExpireSolution](M_Grasshopper_Kernel_GH_Document_ExpireSolution.htm)|  Expire
the entire solution. This will blank all objects.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FilterActive](M_Grasshopper_Kernel_GH_Document_FilterActive.htm)|  Filter a
list of objects.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FilterDisabled](M_Grasshopper_Kernel_GH_Document_FilterDisabled.htm)|  Filter
a list of objects.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FilterEnabled](M_Grasshopper_Kernel_GH_Document_FilterEnabled.htm)|  Filter a
list of objects.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FilterInactive](M_Grasshopper_Kernel_GH_Document_FilterInactive.htm)|  Filter
a list of objects.  
![Public method](../icons/pubmethod.gif)| [FilterObjects(GH_Filter, GH_Filter,
GH_Filter)](M_Grasshopper_Kernel_GH_Document_FilterObjects.htm)|  Returns all
objects in the document that pass the filter specification  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FilterObjects(ListIGH_DocumentObject, GH_Filter, GH_Filter,
GH_Filter)](M_Grasshopper_Kernel_GH_Document_FilterObjects_1.htm)|  Filter a
list of objects using several filters at once  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FilterSelected](M_Grasshopper_Kernel_GH_Document_FilterSelected.htm)|  Filter
a list of objects.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FilterUnselected](M_Grasshopper_Kernel_GH_Document_FilterUnselected.htm)|
Filter a list of objects.  
![Public method](../icons/pubmethod.gif)|
[FindAllDownstreamObjects(IGH_ActiveObject)](M_Grasshopper_Kernel_GH_Document_FindAllDownstreamObjects.htm)|
Find all objects that depend in some way on the Source.  
![Public method](../icons/pubmethod.gif)|
[FindAllDownstreamObjects(ListIGH_ActiveObject)](M_Grasshopper_Kernel_GH_Document_FindAllDownstreamObjects_2.htm)|
Find all objects that depend in some way on the Source collection  
![Public method](../icons/pubmethod.gif)|
[FindAllDownstreamObjects(IGH_ActiveObject,
GH_DocumentGH_ActiveObjectFilter)](M_Grasshopper_Kernel_GH_Document_FindAllDownstreamObjects_1.htm)|
Find all objects that depend in some way on the Source.  
![Public method](../icons/pubmethod.gif)|
[FindAllDownstreamObjects(ListIGH_ActiveObject,
GH_DocumentGH_ActiveObjectFilter)](M_Grasshopper_Kernel_GH_Document_FindAllDownstreamObjects_3.htm)|
Find all objects that depend in some way on the Source collection  
![Public method](../icons/pubmethod.gif)|
[FindAttribute(Guid)](M_Grasshopper_Kernel_GH_Document_FindAttribute_1.htm)|
Find the object that matches the ID  
![Public method](../icons/pubmethod.gif)| [FindAttribute(PointF,
Boolean)](M_Grasshopper_Kernel_GH_Document_FindAttribute.htm)|  Search for
attributes that contain a certain point.  
![Public method](../icons/pubmethod.gif)| [FindAttributeByGrip(PointF,
Boolean, Int32)](M_Grasshopper_Kernel_GH_Document_FindAttributeByGrip_1.htm)|
Search for attributes that contain grips near the search locus  
![Public method](../icons/pubmethod.gif)| [FindAttributeByGrip(PointF,
Boolean, Boolean, Boolean,
Int32)](M_Grasshopper_Kernel_GH_Document_FindAttributeByGrip.htm)|  Search for
attributes that contain grips near the search locus  
![Public method](../icons/pubmethod.gif)|
[FindClusters(Guid)](M_Grasshopper_Kernel_GH_Document_FindClusters.htm)|  Find
all the clusters that have a matching ID.  
![Public method](../icons/pubmethod.gif)|
[FindClusters(String)](M_Grasshopper_Kernel_GH_Document_FindClusters_1.htm)|
Find all the clusters that have a matching filepath.  
![Public method](../icons/pubmethod.gif)|
[FindComponent(Guid)](M_Grasshopper_Kernel_GH_Document_FindComponent_1.htm)|
Search for components using an ID filter  
![Public method](../icons/pubmethod.gif)|
[FindComponent(Point)](M_Grasshopper_Kernel_GH_Document_FindComponent.htm)|
Search for components that contain the locus  
![Public method](../icons/pubmethod.gif)|
[FindFloatingParameter](M_Grasshopper_Kernel_GH_Document_FindFloatingParameter.htm)|
Search for floating parameters that contain the locus  
![Public method](../icons/pubmethod.gif)|
[FindInputParameter](M_Grasshopper_Kernel_GH_Document_FindInputParameter.htm)|
Search for input (upstream) parameters that contain the locus  
![Public method](../icons/pubmethod.gif)| [FindObject(Guid,
Boolean)](M_Grasshopper_Kernel_GH_Document_FindObject_1.htm)|  Find the object
that matches the ID.  
![Public method](../icons/pubmethod.gif)| [FindObject(PointF,
Single)](M_Grasshopper_Kernel_GH_Document_FindObject.htm)|  Find the topmost
object that is closest to the point  
![Public method](../icons/pubmethod.gif)| [FindObjectT(Guid,
Boolean)](M_Grasshopper_Kernel_GH_Document_FindObject__1.htm)|  Find the
object that matches the ID.  
![Public method](../icons/pubmethod.gif)|
[FindObjects](M_Grasshopper_Kernel_GH_Document_FindObjects.htm)|  Find the
objects in the document that match the search term. Top level object names and
nicknames are searched, as well as descriptions. Some objects are special
cased to allow for more targeted searches. Data descriptions are not searched.  
![Public method](../icons/pubmethod.gif)|
[FindOutputParameter](M_Grasshopper_Kernel_GH_Document_FindOutputParameter.htm)|
Search for output (downstream) parameters that contain the locus  
![Public method](../icons/pubmethod.gif)|
[FindParameter](M_Grasshopper_Kernel_GH_Document_FindParameter.htm)|  Search
for parameters using an ID filter  
![Public method](../icons/pubmethod.gif)|
[FindWireAt](M_Grasshopper_Kernel_GH_Document_FindWireAt.htm)|  Find the wire
at or near the given coordinate.  
![Public method](../icons/pubmethod.gif)|
[ForcePreview](M_Grasshopper_Kernel_GH_Document_ForcePreview.htm)|  If true,
the document will draw viewport previews regardless of other conditions.
Typically a document only previews if it is loaded in the canvas or when it
has an RCP.  
![Public method](../icons/pubmethod.gif)|
[GetAllInstanceIDs](M_Grasshopper_Kernel_GH_Document_GetAllInstanceIDs.htm)|
Get a sorted list of all the IGH_DocumentObject instance IDs in this document.  
![Public method](../icons/pubmethod.gif)|
[InactiveObjects](M_Grasshopper_Kernel_GH_Document_InactiveObjects.htm)|
Returns all objects in the document that don't implement the IGH_ActiveObject
interface  
![Public method](../icons/pubmethod.gif)|
[InvertSelection](M_Grasshopper_Kernel_GH_Document_InvertSelection.htm)|
Invert the selected state of all top-level attributes.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[IsEscapeKeyDown](M_Grasshopper_Kernel_GH_Document_IsEscapeKeyDown.htm)|  Gets
whether the escape key was pressed since the last time this function was
called. Though in reality the actual escape state is checked no more than once
every 50 milliseconds or so, which should be sufficient for a smooth user
experience.  
![Public method](../icons/pubmethod.gif)|
[IsRenderMeshPipelineViewport](M_Grasshopper_Kernel_GH_Document_IsRenderMeshPipelineViewport.htm)|
Test to see whether a pipeline should have custom render meshes vs. previews.  
![Public method](../icons/pubmethod.gif)|
[MergeDocument(GH_Document)](M_Grasshopper_Kernel_GH_Document_MergeDocument.htm)|
Hoist all objects from another document into this one.  
![Public method](../icons/pubmethod.gif)| [MergeDocument(GH_Document,
Boolean)](M_Grasshopper_Kernel_GH_Document_MergeDocument_1.htm)|  Hoist all
objects from another document into this one.  
![Public method](../icons/pubmethod.gif)| [MergeDocument(GH_Document, Boolean,
Boolean)](M_Grasshopper_Kernel_GH_Document_MergeDocument_2.htm)|  Hoist all
objects from another document into this one.  
![Public method](../icons/pubmethod.gif)|
[Modified](M_Grasshopper_Kernel_GH_Document_Modified.htm)|  Sets the modified
flag of this document.  
![Public method](../icons/pubmethod.gif)|
[MutateAllIds](M_Grasshopper_Kernel_GH_Document_MutateAllIds.htm)|  Change all
the instance UUIDs of all objects in the document. Be sure to resolve all
proxy sources before mutating IDs. This function will ensure all groups are
updated appropriately.  
![Public method](../icons/pubmethod.gif)|
[NewSolution(Boolean)](M_Grasshopper_Kernel_GH_Document_NewSolution.htm)|
Start a new solution.  
![Public method](../icons/pubmethod.gif)| [NewSolution(Boolean,
GH_SolutionMode)](M_Grasshopper_Kernel_GH_Document_NewSolution_1.htm)|  Start
a new solution.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[NonBlankFilter](M_Grasshopper_Kernel_GH_Document_NonBlankFilter.htm)|  This
delegate can be used in the FindAllDownstreamObjects(...) methods. Only
includes objects that are non-blank and non-failed.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[NullFilter](M_Grasshopper_Kernel_GH_Document_NullFilter.htm)|  This delegate
can be used in the FindAllDownstreamObjects(...) methods. Includes all
objects.  
![Public method](../icons/pubmethod.gif)|
[OnContextChanged](M_Grasshopper_Kernel_GH_Document_OnContextChanged.htm)|
Raise the ContextChanged event.  
![Public method](../icons/pubmethod.gif)|
[OnEnabledChanged](M_Grasshopper_Kernel_GH_Document_OnEnabledChanged.htm)|
Raise the EnabledChanged event.  
![Public method](../icons/pubmethod.gif)|
[OnFilePathChanged](M_Grasshopper_Kernel_GH_Document_OnFilePathChanged.htm)|
Raise the FilePathChanged event.  
![Public method](../icons/pubmethod.gif)|
[OnModifiedChanged](M_Grasshopper_Kernel_GH_Document_OnModifiedChanged.htm)|
Raise the ModifiedChanged event  
![Public method](../icons/pubmethod.gif)|
[OnObjectAdded](M_Grasshopper_Kernel_GH_Document_OnObjectAdded.htm)|  Raise
the ObjectsAdded event.  
![Public method](../icons/pubmethod.gif)|
[OnObjectDeleted](M_Grasshopper_Kernel_GH_Document_OnObjectDeleted.htm)|
Raise the ObjectsDeleted event.  
![Public method](../icons/pubmethod.gif)|
[OnObjectsAdded](M_Grasshopper_Kernel_GH_Document_OnObjectsAdded.htm)|  Raise
the ObjectsAdded event.  
![Public method](../icons/pubmethod.gif)|
[OnObjectsDeleted](M_Grasshopper_Kernel_GH_Document_OnObjectsDeleted.htm)|
Raise the ObjectsDeleted event.  
![Public method](../icons/pubmethod.gif)|
[OnSettingsChanged](M_Grasshopper_Kernel_GH_Document_OnSettingsChanged.htm)|
Raise the SettingsChanged event.  
![Public method](../icons/pubmethod.gif)|
[OnUndoStateChanged](M_Grasshopper_Kernel_GH_Document_OnUndoStateChanged.htm)|
Raise the UndoStateChanged event.  
![Public method](../icons/pubmethod.gif)|
[PreviewCurrentMeshParameters](M_Grasshopper_Kernel_GH_Document_PreviewCurrentMeshParameters.htm)|
Gets the currently relevant meshing parameters (do not modify the instance as
it may be shared).  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_GH_Document_Read.htm)|  Standard archiving
function. Will deserialize the entire document.  
![Public method](../icons/pubmethod.gif)|
[Redo](M_Grasshopper_Kernel_GH_Document_Redo.htm)|  Perform the first redo
event.  
![Public method](../icons/pubmethod.gif)|
[RelevantObjectAtPoint(PointF)](M_Grasshopper_Kernel_GH_Document_RelevantObjectAtPoint.htm)|
Find the most relevant object at a given canvas location. The most relevant
object might be a regular Object (Component or Parameter), it might be an
attribute grip, an attribute balloon, a wire or a group.  
![Public method](../icons/pubmethod.gif)| [RelevantObjectAtPoint(PointF,
GH_RelevantObjectFilter)](M_Grasshopper_Kernel_GH_Document_RelevantObjectAtPoint_1.htm)|
Find the most relevant object at a given canvas location. The most relevant
object might be a regular Object (Component or Parameter), it might be an
attribute grip, an attribute balloon, a wire or a group.  
![Public method](../icons/pubmethod.gif)| [RemoveObject(IGH_Attributes,
Boolean)](M_Grasshopper_Kernel_GH_Document_RemoveObject.htm)|  Remove the top-
level object in the attribute tree from the document. This method does not add
an Undo event, that is the responsibility of the caller.  
![Public method](../icons/pubmethod.gif)| [RemoveObject(IGH_DocumentObject,
Boolean)](M_Grasshopper_Kernel_GH_Document_RemoveObject_1.htm)|  Remove the
object from the document. This removal is the precursor to object deletion. Do
not call this function if you intend to transfer the object to another
GH_Document. This method does not add an Undo event, that is the
responsibility of the caller.  
![Public method](../icons/pubmethod.gif)|
[RemoveObjects](M_Grasshopper_Kernel_GH_Document_RemoveObjects.htm)|  Remove
the specified objects from the document. This removal is the precursor to
object deletion. Do not call this function if you intend to transfer the
objects to another GH_Document. This method does not add an Undo event, that
is the responsibility of the caller.  
![Public method](../icons/pubmethod.gif)|
[RemoveSelection](M_Grasshopper_Kernel_GH_Document_RemoveSelection.htm)|
Delete all the objects in the selection set. This method does not record an
Undo event, that is the responsibility of the caller.  
![Public method](../icons/pubmethod.gif)|
[RepairProxySources](M_Grasshopper_Kernel_GH_Document_RepairProxySources.htm)|
Attempts to resolve all proxy sources in the document.  
![Public method](../icons/pubmethod.gif)|
[ReplaceProxySources](M_Grasshopper_Kernel_GH_Document_ReplaceProxySources.htm)|
Replace all remaining proxy sources in the document with UnresolvedProxy
Objects.  
![Public method](../icons/pubmethod.gif)|
[RequestAbortSolution](M_Grasshopper_Kernel_GH_Document_RequestAbortSolution.htm)|
Set the requestabort flag. The solution will be aborted whenever the current
active object is completed. It is also possible that active objects themselves
implement an abortion mechanism, in which case abortion might occur even
sooner.  
![Public method](../icons/pubmethod.gif)|
[RunningAsCommand](M_Grasshopper_Kernel_GH_Document_RunningAsCommand.htm)|
When the document is being solved inside the context of an executing Rhino
command, this function will return the command instance. Under normal
operation of Grasshopper in the traditional sense, this function will return
null. The document executes as a command when inside of the grasshopper player
or as a compiled grasshopper player based command. The way to run a
GH_Document as a command is to call the GH_RhinoScriptInterface.RunAsCommand
function  
![Public method](../icons/pubmethod.gif)|
[ScheduleSolution(Int32)](M_Grasshopper_Kernel_GH_Document_ScheduleSolution.htm)|
Schedule a new solution after a specified time interval. The schedule is
erased if another solution is triggered before the schedule is executed. Tight
schedules override loose schedules. If this method is called _during_ a
solution, the schedule will be started after the current solution completes.  
![Public method](../icons/pubmethod.gif)| [ScheduleSolution(Int32,
GH_DocumentGH_ScheduleDelegate)](M_Grasshopper_Kernel_GH_Document_ScheduleSolution_1.htm)|
Schedule a new solution after a specified time interval. The schedule is
erased if another solution is triggered before the schedule is executed. Tight
schedules override loose schedules. If this method is called _during_ a
solution, the schedule will be started after the current solution completes.  
![Public method](../icons/pubmethod.gif)|
[Select(GH_RelevantObjectData)](M_Grasshopper_Kernel_GH_Document_Select.htm)|
Default pick selection behaviour. (looks at current Shift + Control modifier
states to determine addition/removal)  
![Public method](../icons/pubmethod.gif)| [Select(GH_RelevantObjectData,
Boolean, Boolean)](M_Grasshopper_Kernel_GH_Document_Select_1.htm)|  Default
pick selection behaviour  
![Public method](../icons/pubmethod.gif)|
[SelectAll](M_Grasshopper_Kernel_GH_Document_SelectAll.htm)|  Select all top-
level attributes.  
![Public method](../icons/pubmethod.gif)|
[SelectedObjects](M_Grasshopper_Kernel_GH_Document_SelectedObjects.htm)|
Returns all selected objects in the document  
![Public method](../icons/pubmethod.gif)|
[SetEnabledFlags(Boolean)](M_Grasshopper_Kernel_GH_Document_SetEnabledFlags.htm)|
Set the enabled flags of all selected objects to true or false  
![Public method](../icons/pubmethod.gif)|
[SetEnabledFlags(ListIGH_DocumentObject,
Boolean)](M_Grasshopper_Kernel_GH_Document_SetEnabledFlags_1.htm)|  Set the
enabled flags of all specified objects to true or false  
![Public method](../icons/pubmethod.gif)|
[SetPreviewFlags(Boolean)](M_Grasshopper_Kernel_GH_Document_SetPreviewFlags.htm)|
Set the preview flags of all selected objects to true or false  
![Public method](../icons/pubmethod.gif)|
[SetPreviewFlags(ListIGH_DocumentObject,
Boolean)](M_Grasshopper_Kernel_GH_Document_SetPreviewFlags_1.htm)|  Set the
preview flags of all specified objects to true or false  
![Public method](../icons/pubmethod.gif)|
[SetStatusBarEventHelper](M_Grasshopper_Kernel_GH_Document_SetStatusBarEventHelper.htm)|  
![Public method](../icons/pubmethod.gif)|
[ShowPreviewSettings](M_Grasshopper_Kernel_GH_Document_ShowPreviewSettings.htm)|
Display the Preview settings dialog.  
![Public method](../icons/pubmethod.gif)|
[SolutionProgress](M_Grasshopper_Kernel_GH_Document_SolutionProgress.htm)|
Returns the progress of the current solution.  
![Public method](../icons/pubmethod.gif)|
[ToggleEnabledFlags](M_Grasshopper_Kernel_GH_Document_ToggleEnabledFlags.htm)|
Toggle the enabled flags of all selected objects  
![Public method](../icons/pubmethod.gif)|
[ToggleEnabledFlags(ListIGH_DocumentObject)](M_Grasshopper_Kernel_GH_Document_ToggleEnabledFlags_1.htm)|
Toggle the enabled flags of all specified objects  
![Public method](../icons/pubmethod.gif)|
[TogglePreviewFlags](M_Grasshopper_Kernel_GH_Document_TogglePreviewFlags.htm)|
Toggle the preview flags of all selected objects  
![Public method](../icons/pubmethod.gif)|
[TogglePreviewFlags(ListIGH_DocumentObject)](M_Grasshopper_Kernel_GH_Document_TogglePreviewFlags_1.htm)|
Toggle the preview flags of all specified objects  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_GH_Document_ToString.htm)|  A document
serializes itself using the filename of the current path. This is useful for
sorting purposes and ListBoxes.  (Overrides
[ObjectToString](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring).)  
![Public method](../icons/pubmethod.gif)|
[TranslateObjects](M_Grasshopper_Kernel_GH_Document_TranslateObjects.htm)|
Offset objects by a certain distance in X and Y  
![Public method](../icons/pubmethod.gif)|
[Undo](M_Grasshopper_Kernel_GH_Document_Undo.htm)|  Perform the first undo
event.  
![Public method](../icons/pubmethod.gif)|
[UnselectedObjects](M_Grasshopper_Kernel_GH_Document_UnselectedObjects.htm)|
Returns all unselected objects in the document  
![Public method](../icons/pubmethod.gif)|
[UpdateAllSubsidiaries](M_Grasshopper_Kernel_GH_Document_UpdateAllSubsidiaries.htm)|
Iterate over all subsidiary documents and update them with their respective
owners. If a subsidiary hasn't been modified, it will not be updated and it
will not be counted.  
![Public method](../icons/pubmethod.gif)|
[Write(GH_IWriter)](M_Grasshopper_Kernel_GH_Document_Write.htm)|  Standard
archiving function. Will serialize the entire document.  
![Public method](../icons/pubmethod.gif)| [Write(GH_IWriter,
IListIGH_DocumentObject)](M_Grasshopper_Kernel_GH_Document_Write_1.htm)|
Special function that allows writing of a custom object list. This function is
used when partial documents need to be serialized such as when exporting or
during clipboard operations.  
Top

![](../icons/SectionExpanded.png)Events

| Name| Description  
---|---|---  
![Public event](../icons/pubevent.gif)|
[ContextChanged](E_Grasshopper_Kernel_GH_Document_ContextChanged.htm)|  The
context for this document was changed.  
![Public event](../icons/pubevent.gif)![Static member](../icons/static.gif)|
[DefaultPreviewColourChanged](E_Grasshopper_Kernel_GH_Document_DefaultPreviewColourChanged.htm)|
This even is raised whenever the global default for Normal preview colour is
changed.  
![Public event](../icons/pubevent.gif)![Static member](../icons/static.gif)|
[DefaultSelectedPreviewColourChanged](E_Grasshopper_Kernel_GH_Document_DefaultSelectedPreviewColourChanged.htm)|
This even is raised whenever the global default for Selected preview colour is
changed.  
![Public event](../icons/pubevent.gif)|
[EnabledChanged](E_Grasshopper_Kernel_GH_Document_EnabledChanged.htm)|  The
Enabled state was changed on this document.  
![Public event](../icons/pubevent.gif)![Static member](../icons/static.gif)|
[EnableSolutionsChanged](E_Grasshopper_Kernel_GH_Document_EnableSolutionsChanged.htm)|
Raised whenever the Shared EnabledSolutions property is changed.  
![Public event](../icons/pubevent.gif)|
[FilePathChanged](E_Grasshopper_Kernel_GH_Document_FilePathChanged.htm)|
Raised whenever the FilePath of the document is modified.  
![Public event](../icons/pubevent.gif)|
[ModifiedChanged](E_Grasshopper_Kernel_GH_Document_ModifiedChanged.htm)|  The
modified flag on the document was changed.  
![Public event](../icons/pubevent.gif)|
[ObjectsAdded](E_Grasshopper_Kernel_GH_Document_ObjectsAdded.htm)|  Raised
after a collection of objects was added to the document.  
![Public event](../icons/pubevent.gif)|
[ObjectsDeleted](E_Grasshopper_Kernel_GH_Document_ObjectsDeleted.htm)|  Raised
after a collection of objects was removed from the document. At this point,
the objects still exist, but they no longer belong to this document.  
![Public event](../icons/pubevent.gif)|
[SettingsChanged](E_Grasshopper_Kernel_GH_Document_SettingsChanged.htm)|  Some
settings of the document were changed.  
![Public event](../icons/pubevent.gif)|
[SolutionEnd](E_Grasshopper_Kernel_GH_Document_SolutionEnd.htm)|  This event
is raised whenever a new solution request has been handled. Even if the
document is locked.  
![Public event](../icons/pubevent.gif)|
[SolutionStart](E_Grasshopper_Kernel_GH_Document_SolutionStart.htm)|  This
event is raised whenever a new solution is requested. Even if the document is
locked.  
![Public event](../icons/pubevent.gif)|
[UndoStateChanged](E_Grasshopper_Kernel_GH_Document_UndoStateChanged.htm)|
Raised whenever there is a change to the document undo/redo stack.  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[IgnoredUnknowns](F_Grasshopper_Kernel_GH_Document_IgnoredUnknowns.htm)|  A
collection of missing component IDs to ignore during file load operations.
Erase this cache to re-enable all the load warnings.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[ScheduleInactive](F_Grasshopper_Kernel_GH_Document_ScheduleInactive.htm)|
Defined the delay used to indicate the absence of a schedule.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[ScheduleRecursive](F_Grasshopper_Kernel_GH_Document_ScheduleRecursive.htm)|
Defines the delay used to indicate the schedule should be immedate and
recursive.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

