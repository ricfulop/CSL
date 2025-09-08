---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Canvas_GH_Canvas.htm
scraped_at: 2025-09-08T16:13:59.708779
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm
"Grasshopper.GUI.Canvas")

[GH_Canvas Class](../html/T_Grasshopper_GUI_Canvas_GH_Canvas.htm "GH_Canvas
Class")

[GH_Canvas Constructor ](../html/M_Grasshopper_GUI_Canvas_GH_Canvas__ctor.htm
"GH_Canvas Constructor ")

[GH_Canvas
Properties](../html/Properties_T_Grasshopper_GUI_Canvas_GH_Canvas.htm
"GH_Canvas Properties")

[GH_Canvas Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_Canvas.htm
"GH_Canvas Methods")

[GH_Canvas Events](../html/Events_T_Grasshopper_GUI_Canvas_GH_Canvas.htm
"GH_Canvas Events")

[GH_Canvas Fields](../html/Fields_T_Grasshopper_GUI_Canvas_GH_Canvas.htm
"GH_Canvas Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Canvas Class  
  
---  
  
The GH_Canvas is the control that handles all mouse and paint events for a
single loaded document.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[SystemMarshalByRefObject](https://docs.microsoft.com/dotnet/api/system.marshalbyrefobject)  
[System.ComponentModelComponent](https://docs.microsoft.com/dotnet/api/system.componentmodel.component)  
[System.Windows.FormsControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.control)  
Grasshopper.GUI.CanvasGH_Canvas  

**Namespace:** [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Canvas : Control
    
    
    Public Class GH_Canvas
    	Inherits Control

The GH_Canvas type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_Canvas](M_Grasshopper_GUI_Canvas_GH_Canvas__ctor.htm)| Initializes a new
instance of the GH_Canvas class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[ActiveInteraction](P_Grasshopper_GUI_Canvas_GH_Canvas_ActiveInteraction.htm)|
Gets or sets the currently active interaction object.  
![Public property](../icons/pubproperty.gif)|
[ActiveObject](P_Grasshopper_GUI_Canvas_GH_Canvas_ActiveObject.htm)|  Gets or
sets the currently active object.  
![Public property](../icons/pubproperty.gif)|
[ActiveWidget](P_Grasshopper_GUI_Canvas_GH_Canvas_ActiveWidget.htm)|  Gets or
sets the currently active widget.  
![Public property](../icons/pubproperty.gif)|
[CursorCanvasPosition](P_Grasshopper_GUI_Canvas_GH_Canvas_CursorCanvasPosition.htm)|
Gets the location of the cursor in Canvas coordinates.  
![Public property](../icons/pubproperty.gif)|
[CursorControlPosition](P_Grasshopper_GUI_Canvas_GH_Canvas_CursorControlPosition.htm)|
Gets the location of the cursor in Control coordinates.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[DisplayVoronoiWarning](P_Grasshopper_GUI_Canvas_GH_Canvas_DisplayVoronoiWarning.htm)|
Gets or sets whether the Voronoi Over-dose warning message is displayed. This
property is set once at Grasshopper startup to True.  
![Public property](../icons/pubproperty.gif)|
[Document](P_Grasshopper_GUI_Canvas_GH_Canvas_Document.htm)|  Gets or sets the
document currently loaded in this canvas.  
![Public property](../icons/pubproperty.gif)|
[DrawingMode](P_Grasshopper_GUI_Canvas_GH_Canvas_DrawingMode.htm)|  Gets the
current drawing mode for this canvas.  
![Public property](../icons/pubproperty.gif)|
[HasControlWithFocus](P_Grasshopper_GUI_Canvas_GH_Canvas_HasControlWithFocus.htm)|
Gets whether or not this canvas has a child control on it with focus.  
![Public property](../icons/pubproperty.gif)|
[IsActiveInteraction](P_Grasshopper_GUI_Canvas_GH_Canvas_IsActiveInteraction.htm)|
Gets a value indicating whether or not there is an interaction object loaded
in this canvas.  
![Public property](../icons/pubproperty.gif)|
[IsActiveObject](P_Grasshopper_GUI_Canvas_GH_Canvas_IsActiveObject.htm)|  Gets
a value indicating whether or not an object is currently activated.  
![Public property](../icons/pubproperty.gif)|
[IsActiveWidget](P_Grasshopper_GUI_Canvas_GH_Canvas_IsActiveWidget.htm)|  Gets
a value indicating whether or not a widget is currently activated.  
![Public property](../icons/pubproperty.gif)|
[IsDocument](P_Grasshopper_GUI_Canvas_GH_Canvas_IsDocument.htm)|  Gets a value
indicating whether or not a document is currently loaded in this canvas.  
![Public property](../icons/pubproperty.gif)|
[MarkovSuggestions](P_Grasshopper_GUI_Canvas_GH_Canvas_MarkovSuggestions.htm)|  
![Public property](../icons/pubproperty.gif)|
[ModifiersEnabled](P_Grasshopper_GUI_Canvas_GH_Canvas_ModifiersEnabled.htm)|
Gets or sets the modifiers enabled flag. When modifiers are disabled, only
zooming and panning is still allowed.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[NavigationPanDown](P_Grasshopper_GUI_Canvas_GH_Canvas_NavigationPanDown.htm)|
Gets or sets the special key for panning down.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[NavigationPanLeft](P_Grasshopper_GUI_Canvas_GH_Canvas_NavigationPanLeft.htm)|
Gets or sets the special key for panning left.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[NavigationPanPixels](P_Grasshopper_GUI_Canvas_GH_Canvas_NavigationPanPixels.htm)|
Gets or sets the number of pixels for each pan operation.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[NavigationPanRight](P_Grasshopper_GUI_Canvas_GH_Canvas_NavigationPanRight.htm)|
Gets or sets the special key for panning right.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[NavigationPanUp](P_Grasshopper_GUI_Canvas_GH_Canvas_NavigationPanUp.htm)|
Gets or sets the special key for panning up.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[NavigationZoomFactor](P_Grasshopper_GUI_Canvas_GH_Canvas_NavigationZoomFactor.htm)|
Gets or sets the zoom factor for navigation zoom operations.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[NavigationZoomIn](P_Grasshopper_GUI_Canvas_GH_Canvas_NavigationZoomIn.htm)|
Gets or sets the special key for zooming in.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[NavigationZoomOut](P_Grasshopper_GUI_Canvas_GH_Canvas_NavigationZoomOut.htm)|
Gets or sets the special key for zooming in.  
![Public property](../icons/pubproperty.gif)|
[Painter](P_Grasshopper_GUI_Canvas_GH_Canvas_Painter.htm)|  Gets the painter
object that handles most of the drawing logic for this canvas.  
![Public property](../icons/pubproperty.gif)|
[Painting](P_Grasshopper_GUI_Canvas_GH_Canvas_Painting.htm)|  Gets whether
this canvas is currently busy painting itself.  
![Public property](../icons/pubproperty.gif)|
[RecordPreviewBoundary](P_Grasshopper_GUI_Canvas_GH_Canvas_RecordPreviewBoundary.htm)|  
![Public property](../icons/pubproperty.gif)|
[TagArtistIDs](P_Grasshopper_GUI_Canvas_GH_Canvas_TagArtistIDs.htm)|  Gets all
the TagArtist IDs in this Canvas.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[ThumbnailSize](P_Grasshopper_GUI_Canvas_GH_Canvas_ThumbnailSize.htm)|  Gets
the thumbnail size for documents.  
![Public property](../icons/pubproperty.gif)|
[TooltipDelay](P_Grasshopper_GUI_Canvas_GH_Canvas_TooltipDelay.htm)|  Gets the
delay (in milliseconds) required for a tooltip popup. This delay is a user
setting stored under the Canvas:TooltipDelay field of the core settings.  
![Public property](../icons/pubproperty.gif)|
[Validator](P_Grasshopper_GUI_Canvas_GH_Canvas_Validator.htm)|  Provides
access to all the validators associated with this canvas.  
![Public property](../icons/pubproperty.gif)|
[Viewport](P_Grasshopper_GUI_Canvas_GH_Canvas_Viewport.htm)|  Gets the
viewport that determines the panning and zooming for this canvas.  
![Public property](../icons/pubproperty.gif)|
[Widgets](P_Grasshopper_GUI_Canvas_GH_Canvas_Widgets.htm)|  Gets a list of all
the widgets on this canvas.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[ZoomFadeHigh](P_Grasshopper_GUI_Canvas_GH_Canvas_ZoomFadeHigh.htm)|  Gets the
ZUI fade alpha value for the high zoom level threshold. This static field gets
set on every Canvas paint start. The high threshold is typically used for ZUI
elements that only appear when zoomed in.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[ZoomFadeLow](P_Grasshopper_GUI_Canvas_GH_Canvas_ZoomFadeLow.htm)|  Gets the
ZUI fade alpha value for the low zoom level threshold. This static field gets
set on every Canvas paint start. The low threshold is typically used for
fading of icons and object names.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[ZoomFadeMedium](P_Grasshopper_GUI_Canvas_GH_Canvas_ZoomFadeMedium.htm)|  Gets
the ZUI fade alpha value for the medium zoom level threshold. This static
field gets set on every Canvas paint start. The medium threshold is typically
used for non-informative UI elements such as highlights.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AddTagArtist](M_Grasshopper_GUI_Canvas_GH_Canvas_AddTagArtist.htm)|  Add a
Tag Artist instance to this canvas.  
![Public method](../icons/pubmethod.gif)|
[AddValidator](M_Grasshopper_GUI_Canvas_GH_Canvas_AddValidator.htm)|  Add a
new drop validator to the canvas.  
![Public method](../icons/pubmethod.gif)|
[AutoSaveDocument](M_Grasshopper_GUI_Canvas_GH_Canvas_AutoSaveDocument.htm)|  
![Public method](../icons/pubmethod.gif)|
[CanvasOldSchoolMenu](M_Grasshopper_GUI_Canvas_GH_Canvas_CanvasOldSchoolMenu.htm)|  
![Public method](../icons/pubmethod.gif)|
[CreateMRUPanels](M_Grasshopper_GUI_Canvas_GH_Canvas_CreateMRUPanels.htm)|
Create new MRU panels. This function only does something if there is no
document loaded in the canvas.  
![Public method](../icons/pubmethod.gif)|
[CreatePreview](M_Grasshopper_GUI_Canvas_GH_Canvas_CreatePreview.htm)|  Render
this canvas to a thumbnail preview.  
![Public method](../icons/pubmethod.gif)|
[DestroyMRUPanels](M_Grasshopper_GUI_Canvas_GH_Canvas_DestroyMRUPanels.htm)|
Destroy any MRU panels that might be in existence.  
![Protected method](../icons/protmethod.gif)|
[Dispose](M_Grasshopper_GUI_Canvas_GH_Canvas_Dispose.htm)| Releases the
unmanaged resources used by the GH_Canvas and optionally releases the managed
resources (Overrides
[ControlDispose(Boolean)](https://docs.microsoft.com/dotnet/api/system.windows.forms.control.dispose#system-
windows-forms-control-dispose\(system-boolean\)).)  
![Public method](../icons/pubmethod.gif)|
[GenerateHiResImage](M_Grasshopper_GUI_Canvas_GH_Canvas_GenerateHiResImage.htm)|
Generate a collection of hi-res images of the document.  
![Public method](../icons/pubmethod.gif)|
[GenerateHiResImageTile](M_Grasshopper_GUI_Canvas_GH_Canvas_GenerateHiResImageTile.htm)|
Generate a single tile in a Hi-Res image export.  
![Public method](../icons/pubmethod.gif)|
[GetCanvasScreenBuffer](M_Grasshopper_GUI_Canvas_GH_Canvas_GetCanvasScreenBuffer.htm)|
Get a bitmap that resembles the current state of the canvas.  
![Public method](../icons/pubmethod.gif)|
[GetGraphicsObject](M_Grasshopper_GUI_Canvas_GH_Canvas_GetGraphicsObject.htm)|
Gets a graphics object for this control. You are not allowed to draw with this
object, use it only for visibility testing and such. If you're inside a canvas
update, use the Graphics() property instead. You must dispose of the Graphics
object returned by this method or resources will be leaked.  
![Public method](../icons/pubmethod.gif)|
[HideMRUPanels](M_Grasshopper_GUI_Canvas_GH_Canvas_HideMRUPanels.htm)|  Hide
all existing MRU panels by sliding them out of view.  
![Public method](../icons/pubmethod.gif)| [InstantiateNewObject(Guid, PointF,
Boolean)](M_Grasshopper_GUI_Canvas_GH_Canvas_InstantiateNewObject.htm)|  
![Public method](../icons/pubmethod.gif)| [InstantiateNewObject(Guid, String,
PointF,
Boolean)](M_Grasshopper_GUI_Canvas_GH_Canvas_InstantiateNewObject_1.htm)|  
![Public method](../icons/pubmethod.gif)|
[Navigate](M_Grasshopper_GUI_Canvas_GH_Canvas_Navigate.htm)|  Perform a single
navigation step.  
![Protected method](../icons/protmethod.gif)|
[OnPaint](M_Grasshopper_GUI_Canvas_GH_Canvas_OnPaint.htm)|  (Overrides
[ControlOnPaint(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.control.onpaint#system-
windows-forms-control-onpaint\(system-windows-forms-painteventargs\)).)  
![Protected method](../icons/protmethod.gif)|
[OnPaintBackground](M_Grasshopper_GUI_Canvas_GH_Canvas_OnPaintBackground.htm)|
(Overrides
[ControlOnPaintBackground(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.control.onpaintbackground#system-
windows-forms-control-onpaintbackground\(system-windows-forms-
painteventargs\)).)  
![Public method](../icons/pubmethod.gif)|
[OnViewportChanged](M_Grasshopper_GUI_Canvas_GH_Canvas_OnViewportChanged.htm)|
Ensure the canvas and document viewport data are synchronised and raises the
ViewportChanged event.  
![Public method](../icons/pubmethod.gif)|
[ReevaluateMarkovSuggestions](M_Grasshopper_GUI_Canvas_GH_Canvas_ReevaluateMarkovSuggestions.htm)|  
![Public method](../icons/pubmethod.gif)|
[RemoveAllTagArtists](M_Grasshopper_GUI_Canvas_GH_Canvas_RemoveAllTagArtists.htm)|
Remove all IGH_TagArtists from this canvas. Do not use this method unless you
want to screw over everyone else.  
![Public method](../icons/pubmethod.gif)|
[RemoveTagArtist(Guid)](M_Grasshopper_GUI_Canvas_GH_Canvas_RemoveTagArtist_1.htm)|
Remove all IGH_TagArtists from this canvas that match a certain ID.  
![Public method](../icons/pubmethod.gif)|
[RemoveTagArtist(IGH_TagArtist)](M_Grasshopper_GUI_Canvas_GH_Canvas_RemoveTagArtist.htm)|
Remove a specific tag artist from this canvas. If the instance occurs multiple
times in the TagArtist list, all instances will be removed.  
![Public method](../icons/pubmethod.gif)|
[RemoveValidator](M_Grasshopper_GUI_Canvas_GH_Canvas_RemoveValidator.htm)|
Remove a drop validator from the canvas.  
![Public method](../icons/pubmethod.gif)|
[ScheduleRegen](M_Grasshopper_GUI_Canvas_GH_Canvas_ScheduleRegen.htm)|
Schedule a regen to occur after the specified number of milliseconds have
elapsed. If a Regen is called in this time frame, the schedule will be
cleared. Only a single schedule can be active at any time, so any call to
ScheduleRegen will clear existing schedules.  
![Public method](../icons/pubmethod.gif)|
[SetSmartTextRenderingHint](M_Grasshopper_GUI_Canvas_GH_Canvas_SetSmartTextRenderingHint.htm)|
When this method is called during a redraw, the TextRenderingHint of the
associated graphics object will be set to either GH_CrispText or GH_SmoothText
depending on zoom level.  
![Public method](../icons/pubmethod.gif)|
[ShowComponentSearchBox](M_Grasshopper_GUI_Canvas_GH_Canvas_ShowComponentSearchBox.htm)|
Display the component Search dialog at the current mouse location. The dialog
cannot be shown if ModifiersEnabled=False.  
![Public method](../icons/pubmethod.gif)|
[ShowComponentSearchBox(Point)](M_Grasshopper_GUI_Canvas_GH_Canvas_ShowComponentSearchBox_1.htm)|
Display the component Search dialog at the given coordinate. The dialog cannot
be shown if ModifiersEnabled=False.  
![Public method](../icons/pubmethod.gif)|
[ShowMRUPanels](M_Grasshopper_GUI_Canvas_GH_Canvas_ShowMRUPanels.htm)|  Show
any hidden MRU panels by sliding them back into view.  
![Public method](../icons/pubmethod.gif)|
[ShowNavigationPane](M_Grasshopper_GUI_Canvas_GH_Canvas_ShowNavigationPane.htm)|
Displays the quick-navigation popup pane at the cursor.  
![Public method](../icons/pubmethod.gif)|
[ShowSearchDialog](M_Grasshopper_GUI_Canvas_GH_Canvas_ShowSearchDialog.htm)|
Display the Find dialog. If a Find dialog is already active for this canvas,
nothing will happen.  
![Public method](../icons/pubmethod.gif)|
[StartAutoPan](M_Grasshopper_GUI_Canvas_GH_Canvas_StartAutoPan.htm)|  Start
the auto-panning timer.  
![Public method](../icons/pubmethod.gif)|
[StopAutoPan](M_Grasshopper_GUI_Canvas_GH_Canvas_StopAutoPan.htm)|  Stop the
auto-panning timer.  
![Public method](../icons/pubmethod.gif)|
[UpdateDocumentPreview](M_Grasshopper_GUI_Canvas_GH_Canvas_UpdateDocumentPreview.htm)|
Call this method to update the preview thumbnail for the currently loaded
document. If no document is currently loaded, nothing will happen.  
Top

![](../icons/SectionExpanded.png)Events

| Name| Description  
---|---|---  
![Public event](../icons/pubevent.gif)|
[CanvasPaintBackground](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPaintBackground.htm)|
Raised after the background has been drawn.  
![Public event](../icons/pubevent.gif)|
[CanvasPaintBegin](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPaintBegin.htm)|
Raised before a new paint operation starts. This event is always raised, even
if the Canvas isn't visible.  
![Public event](../icons/pubevent.gif)|
[CanvasPaintEnd](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPaintEnd.htm)|
Raised after a paint operation completes. This event is always raised, even if
the Canvas isn't visible.  
![Public event](../icons/pubevent.gif)|
[CanvasPostPaintGroups](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPostPaintGroups.htm)|
Raised after group drawing completes.  
![Public event](../icons/pubevent.gif)|
[CanvasPostPaintObjects](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPostPaintObjects.htm)|
Raised after object drawing completes.  
![Public event](../icons/pubevent.gif)|
[CanvasPostPaintOverlay](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPostPaintOverlay.htm)|
Raised after object overlay drawing completes.  
![Public event](../icons/pubevent.gif)|
[CanvasPostPaintWidgets](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPostPaintWidgets.htm)|
Raised after widgets are drawn. This is the final event in the Drawing
pipeline.  
![Public event](../icons/pubevent.gif)|
[CanvasPostPaintWires](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPostPaintWires.htm)|
Raised after wire drawing completes.  
![Public event](../icons/pubevent.gif)|
[CanvasPrePaintGroups](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPrePaintGroups.htm)|
Raised before group drawing starts.  
![Public event](../icons/pubevent.gif)|
[CanvasPrePaintObjects](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPrePaintObjects.htm)|
Raised before object drawing starts.  
![Public event](../icons/pubevent.gif)|
[CanvasPrePaintOverlay](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPrePaintOverlay.htm)|
Raised before object overlay drawing starts.  
![Public event](../icons/pubevent.gif)|
[CanvasPrePaintWidgets](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPrePaintWidgets.htm)|
Raised before Widgets are drawn.  
![Public event](../icons/pubevent.gif)|
[CanvasPrePaintWires](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPrePaintWires.htm)|
Raised before wire drawing starts.  
![Public event](../icons/pubevent.gif)|
[Document_ModifiedChanged](E_Grasshopper_GUI_Canvas_GH_Canvas_Document_ModifiedChanged.htm)|  
![Public event](../icons/pubevent.gif)|
[Document_ObjectsAdded](E_Grasshopper_GUI_Canvas_GH_Canvas_Document_ObjectsAdded.htm)|  
![Public event](../icons/pubevent.gif)|
[Document_ObjectsDeleted](E_Grasshopper_GUI_Canvas_GH_Canvas_Document_ObjectsDeleted.htm)|  
![Public event](../icons/pubevent.gif)|
[Document_SettingsChanged](E_Grasshopper_GUI_Canvas_GH_Canvas_Document_SettingsChanged.htm)|  
![Public event](../icons/pubevent.gif)|
[DocumentChanged](E_Grasshopper_GUI_Canvas_GH_Canvas_DocumentChanged.htm)|
This event is raised whenever a different document is loaded into this canvas.  
![Public event](../icons/pubevent.gif)|
[DocumentObjectMouseDown](E_Grasshopper_GUI_Canvas_GH_Canvas_DocumentObjectMouseDown.htm)|
This event is raised whenever the left mouse button is pressed while over a
Document object.  
![Public event](../icons/pubevent.gif)|
[ModifiersChanged](E_Grasshopper_GUI_Canvas_GH_Canvas_ModifiersChanged.htm)|
This event is raised whenever the ModifiersEnabled property changes.  
![Public event](../icons/pubevent.gif)![Static member](../icons/static.gif)|
[NavigationSettingsChanged](E_Grasshopper_GUI_Canvas_GH_Canvas_NavigationSettingsChanged.htm)|
Raised whenever any of the shared navigation properties changed.  
![Public event](../icons/pubevent.gif)|
[ViewportChanged](E_Grasshopper_GUI_Canvas_GH_Canvas_ViewportChanged.htm)|
This event is raised whenever the viewport properties are modified, for
example when the pan or zoom values are affected.  
![Public event](../icons/pubevent.gif)![Static member](../icons/static.gif)|
[WidgetListCreated](E_Grasshopper_GUI_Canvas_GH_Canvas_WidgetListCreated.htm)|
This event is raised once for every GH_Canvas object that is created anew. The
event is Shared (static) because it is raised inside the constructor of a
GH_Canvas object and therefor cannot be registered on an instance.  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[ScheduleInactive](F_Grasshopper_GUI_Canvas_GH_Canvas_ScheduleInactive.htm)|
Defines the delay used to indicate the absence of a schedule.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[ThumbnailHeight](F_Grasshopper_GUI_Canvas_GH_Canvas_ThumbnailHeight.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[ThumbnailWidth](F_Grasshopper_GUI_Canvas_GH_Canvas_ThumbnailWidth.htm)|  
Top

![](../icons/SectionExpanded.png)Extension Methods

| Name| Description  
---|---|---  
![Public Extension Method](../icons/pubextension.gif)|
[ToEto](M_Grasshopper_EtoExtensions_ToEto_7.htm)|  (Defined by
[EtoExtensions](T_Grasshopper_EtoExtensions.htm).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

