---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Instances.htm
scraped_at: 2025-09-08T16:11:46.100128
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper](../html/N_Grasshopper.htm "Grasshopper")

[Instances Class](../html/T_Grasshopper_Instances.htm "Instances Class")

[Instances Properties](../html/Properties_T_Grasshopper_Instances.htm
"Instances Properties")

[Instances Methods](../html/Methods_T_Grasshopper_Instances.htm "Instances
Methods")

[Instances Events](../html/Events_T_Grasshopper_Instances.htm "Instances
Events")

[Instances Fields](../html/Fields_T_Grasshopper_Instances.htm "Instances
Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# Instances Class  
  
---  
  
Provides access to a bunch of global instances and variables.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
GrasshopperInstances  

**Namespace:** [Grasshopper](N_Grasshopper.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class Instances
    
    
    Public NotInheritable Class Instances

The Instances type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[ActiveCanvas](P_Grasshopper_Instances_ActiveCanvas.htm)|  Gets the currently
active Grasshopper canvas (if any)  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[ActiveDocument](P_Grasshopper_Instances_ActiveDocument.htm)|  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[ActiveRhinoDoc](P_Grasshopper_Instances_ActiveRhinoDoc.htm)|  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[AutoHideBanner](P_Grasshopper_Instances_AutoHideBanner.htm)|  Gets or sets a
value indicating whether the banner ought to be hidden automatically when
loading completes.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[AutoShowBanner](P_Grasshopper_Instances_AutoShowBanner.htm)|  Gets or sets a
value indicating whether or not the banner will be displayed during the
ComponentServer Loading process.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[ComponentServer](P_Grasshopper_Instances_ComponentServer.htm)|  Gets the
ComponentServer instance cached by the Instance Server. The ComponentServer
will be instantiated the first time this property accessed. This is a rather
involved process during which the Grasshopper Banner will be displayed.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[CursorServer](P_Grasshopper_Instances_CursorServer.htm)|  Gets the
CursorServer instance cached by the Instance Server. The CursorServer will be
instantiated the first time this property is accessed.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[DocumentAssociationServer](P_Grasshopper_Instances_DocumentAssociationServer.htm)|
Gets the Document Association Server instance cached by the Instance Server.
The Document Association Server will be instantiated the first time this
property accessed.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[DocumentEditor](P_Grasshopper_Instances_DocumentEditor.htm)|  Gets the
DocumentEditor of Grasshopper.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[DocumentServer](P_Grasshopper_Instances_DocumentServer.htm)|  Gets the
DocumentServer instance cached by the Instance Server. The DocumentServer will
be instantiated the first time this property accessed.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[EtoDocumentEditor](P_Grasshopper_Instances_EtoDocumentEditor.htm)|  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[GrasshopperPluginId](P_Grasshopper_Instances_GrasshopperPluginId.htm)|  Gets
the ID of the Grasshopper Plugin.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[IsComponentServer](P_Grasshopper_Instances_IsComponentServer.htm)|  Gets
whether the Component server has been set.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[IsCursorServer](P_Grasshopper_Instances_IsCursorServer.htm)|  Gets whether
the Cursor server has been set.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[IsDocumentAssociationServer](P_Grasshopper_Instances_IsDocumentAssociationServer.htm)|
Gets whether the Document Association server has been set.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[IsDocumentEditor](P_Grasshopper_Instances_IsDocumentEditor.htm)|  Gets
whether the Document Editor has been set.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[IsDocumentEditorOnTopOfViewports](P_Grasshopper_Instances_IsDocumentEditorOnTopOfViewports.htm)|
Gets whether the Grasshopper document editor (or any of its child forms) is
obscuring a significant part of the Rhino viewports.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[IsDocumentServer](P_Grasshopper_Instances_IsDocumentServer.htm)|  Gets
whether the Document server has been set.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[IsMarkovChain](P_Grasshopper_Instances_IsMarkovChain.htm)|  Gets a value
indicating whether or not the MarkovChain has already been initialized.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[IsMruServer](P_Grasshopper_Instances_IsMruServer.htm)|  Gets a value
indicating whether or not the MRU server has been initialized.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[IsRemotePanelVisible](P_Grasshopper_Instances_IsRemotePanelVisible.htm)|
Gets whether the Remote Control Panel is currently visible.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[MarkovChain](P_Grasshopper_Instances_MarkovChain.htm)|  Gets the MarkovChain
instance cached by the Instance Server. The Markov chain will be instantiated
if it hasn't been already.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[MruServer](P_Grasshopper_Instances_MruServer.htm)|  Gets the MRU_Server
instance cached by the Instance Server. The MRU_Server will be instantiated
the first time this property accessed.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[RcpPanel](P_Grasshopper_Instances_RcpPanel.htm)|  Gets the app-domain wide
RCP panel instance. If it doesn't exist yet it will be created.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[RunningHeadless](P_Grasshopper_Instances_RunningHeadless.htm)|  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[Settings](P_Grasshopper_Instances_Settings.htm)|  Represents the default
settings database. Feel free to add your own settings to this database.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[DocumentEditorFadeIn](M_Grasshopper_Instances_DocumentEditorFadeIn.htm)|
Calls the FadeIn() method on the DocumentEditor if it exists.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[DocumentEditorFadeOut](M_Grasshopper_Instances_DocumentEditorFadeOut.htm)|
Calls the FadeOut() method on the DocumentEditor if it exists.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[EnforceInvariantCulture](M_Grasshopper_Instances_EnforceInvariantCulture.htm)|
If the Setting "EnforceInvariantCulture" is set to False, this function does
nothing  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[HideRemotePanel](M_Grasshopper_Instances_HideRemotePanel.htm)|  Hides the
remote control panel.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Interop](M_Grasshopper_Instances_Interop.htm)|  Gets the Grasshopper 1.0
interop object, i.e. an instance of GrasshopperPlugin.GrasshopperInterop as
exposed via the GetInteropObject() method on the Grasshopper 1.0 plugin
object.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[InvalidateCanvas](M_Grasshopper_Instances_InvalidateCanvas.htm)|  Invalidates
the currently active Grasshopper Canvas, causing a redraw sometime in the
foreseeable future.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RedrawAll](M_Grasshopper_Instances_RedrawAll.htm)|  Forces a redraw of both
the active canvas and the Rhino viewports on the active document.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RedrawCanvas](M_Grasshopper_Instances_RedrawCanvas.htm)|  Forces a redraw of
the currently active Grasshopper Canvas.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ReloadMemoryAssemblies](M_Grasshopper_Instances_ReloadMemoryAssemblies.htm)|
Unload and attempt to reload all plugin assemblies that were loaded via the
COFF pipeline.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ShowRemotePanel](M_Grasshopper_Instances_ShowRemotePanel.htm)|  Shows the
remote control panel.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[UnloadAllObjects](M_Grasshopper_Instances_UnloadAllObjects.htm)|  Clears and
unloads all cached objects. This function is called by the
_GrasshopperUnloadPlugin command. Please don't use it.  
Top

![](../icons/SectionExpanded.png)Events

| Name| Description  
---|---|---  
![Public event](../icons/pubevent.gif)![Static member](../icons/static.gif)|
[CanvasCreated](E_Grasshopper_Instances_CanvasCreated.htm)|  Raised when the
main canvas is created.  
![Public event](../icons/pubevent.gif)![Static member](../icons/static.gif)|
[CanvasDestroyed](E_Grasshopper_Instances_CanvasDestroyed.htm)|  Raised when
the main canvas is destroyed.  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[LoadOneByOne](F_Grasshopper_Instances_LoadOneByOne.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper Namespace](N_Grasshopper.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

