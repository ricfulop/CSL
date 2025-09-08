---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_GH_DocumentEditor.htm
scraped_at: 2025-09-08T16:12:26.256925
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH_DocumentEditor Class](../html/T_Grasshopper_GUI_GH_DocumentEditor.htm
"GH_DocumentEditor Class")

[GH_DocumentEditor Constructor
](../html/M_Grasshopper_GUI_GH_DocumentEditor__ctor.htm "GH_DocumentEditor
Constructor ")

[GH_DocumentEditor
Properties](../html/Properties_T_Grasshopper_GUI_GH_DocumentEditor.htm
"GH_DocumentEditor Properties")

[GH_DocumentEditor
Methods](../html/Methods_T_Grasshopper_GUI_GH_DocumentEditor.htm
"GH_DocumentEditor Methods")

[GH_DocumentEditor
Events](../html/Events_T_Grasshopper_GUI_GH_DocumentEditor.htm
"GH_DocumentEditor Events")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_DocumentEditor Class  
  
---  
  
The Grasshopper main window.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[SystemMarshalByRefObject](https://docs.microsoft.com/dotnet/api/system.marshalbyrefobject)  
[System.ComponentModelComponent](https://docs.microsoft.com/dotnet/api/system.componentmodel.component)  
[System.Windows.FormsControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.control)  
[System.Windows.FormsScrollableControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol)  
[System.Windows.FormsContainerControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.containercontrol)  
[System.Windows.FormsForm](https://docs.microsoft.com/dotnet/api/system.windows.forms.form)  
Grasshopper.GUIGH_DocumentEditor  

**Namespace:** [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_DocumentEditor : Form
    
    
    Public Class GH_DocumentEditor
    	Inherits Form

The GH_DocumentEditor type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_DocumentEditor](M_Grasshopper_GUI_GH_DocumentEditor__ctor.htm)|
Initializes a new instance of the GH_DocumentEditor class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Collapsed](P_Grasshopper_GUI_GH_DocumentEditor_Collapsed.htm)|  Gets a value
indicating whether or not the form is currently collapsed.  
![Protected property](../icons/protproperty.gif)|
[CreateParams](P_Grasshopper_GUI_GH_DocumentEditor_CreateParams.htm)|
(Overrides
[FormCreateParams](https://docs.microsoft.com/dotnet/api/system.windows.forms.form.createparams#system-
windows-forms-form-createparams).)  
![Public property](../icons/pubproperty.gif)|
[FormShepard](P_Grasshopper_GUI_GH_DocumentEditor_FormShepard.htm)|  Gets the
form shepard for this window. Register your modeless dialogs with this shepard
if you want to be popular.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ClearStatusBar](M_Grasshopper_GUI_GH_DocumentEditor_ClearStatusBar.htm)|
Clear the Grasshopper status-bar.  
![Public method](../icons/pubmethod.gif)|
[CloseForReal](M_Grasshopper_GUI_GH_DocumentEditor_CloseForReal.htm)|  Really,
_really_ close the window.  
![Public method](../icons/pubmethod.gif)|
[CollapseForm](M_Grasshopper_GUI_GH_DocumentEditor_CollapseForm.htm)|
Collapses the form into the title bar area.  
![Public method](../icons/pubmethod.gif)|
[DisableUI](M_Grasshopper_GUI_GH_DocumentEditor_DisableUI.htm)|  Disable all
modifier UI.  
![Protected method](../icons/protmethod.gif)|
[Dispose](M_Grasshopper_GUI_GH_DocumentEditor_Dispose.htm)| Releases the
unmanaged resources used by the GH_DocumentEditor and optionally releases the
managed resources (Overrides
[FormDispose(Boolean)](https://docs.microsoft.com/dotnet/api/system.windows.forms.form.dispose#system-
windows-forms-form-dispose\(system-boolean\)).)  
![Public method](../icons/pubmethod.gif)|
[EnableUI](M_Grasshopper_GUI_GH_DocumentEditor_EnableUI.htm)|  Enable all
modifier UI.  
![Public method](../icons/pubmethod.gif)|
[ExpandForm](M_Grasshopper_GUI_GH_DocumentEditor_ExpandForm.htm)|  Expands the
form if it is currenly collapsed.  
![Public method](../icons/pubmethod.gif)|
[FadeIn](M_Grasshopper_GUI_GH_DocumentEditor_FadeIn.htm)|  Call this method if
the prompt switches back to Grasshopper.  
![Public method](../icons/pubmethod.gif)|
[FadeOut](M_Grasshopper_GUI_GH_DocumentEditor_FadeOut.htm)|  Call this method
if the prompt switches to Rhino.  
![Public method](../icons/pubmethod.gif)|
[FixCanvasToolbarState](M_Grasshopper_GUI_GH_DocumentEditor_FixCanvasToolbarState.htm)|
Enabled/Disables the appropriate buttons depending on whether there is a
document loaded on the canvas.  
![Public method](../icons/pubmethod.gif)|
[ScriptAccess_CloseAllDocuments](M_Grasshopper_GUI_GH_DocumentEditor_ScriptAccess_CloseAllDocuments.htm)|
Closes all documents in the Document Queue.  
![Public method](../icons/pubmethod.gif)|
[ScriptAccess_CloseDocument](M_Grasshopper_GUI_GH_DocumentEditor_ScriptAccess_CloseDocument.htm)|
Closes the currently active document and loads the next available document
into the canvas. Changes will not be saved.  
![Public method](../icons/pubmethod.gif)|
[ScriptAccess_IsDocument](M_Grasshopper_GUI_GH_DocumentEditor_ScriptAccess_IsDocument.htm)|
Returns true if there is an active document.  
![Public method](../icons/pubmethod.gif)|
[ScriptAccess_IsDocumentModified](M_Grasshopper_GUI_GH_DocumentEditor_ScriptAccess_IsDocumentModified.htm)|
Gets the modified flag of the currently loaded document.  
![Public method](../icons/pubmethod.gif)|
[ScriptAccess_NewDocument](M_Grasshopper_GUI_GH_DocumentEditor_ScriptAccess_NewDocument.htm)|
Creates a new document and loads it into the Canvas.  
![Public method](../icons/pubmethod.gif)|
[ScriptAccess_OpenDocument](M_Grasshopper_GUI_GH_DocumentEditor_ScriptAccess_OpenDocument.htm)|
Displays a command line interface for File Open... then loads that file into
the Canvas.  
![Public method](../icons/pubmethod.gif)|
[ScriptAccess_OpenDocument(String)](M_Grasshopper_GUI_GH_DocumentEditor_ScriptAccess_OpenDocument_1.htm)|
Loads a specific file off the hard disk into the Canvas.  
![Public method](../icons/pubmethod.gif)|
[ScriptAccess_SaveDocument](M_Grasshopper_GUI_GH_DocumentEditor_ScriptAccess_SaveDocument.htm)|
Saves the document currently loaded in the Canvas. If the document hasn't been
saved before then a Save... dialog box will be shown.  
![Public method](../icons/pubmethod.gif)|
[ScriptAccess_SaveDocumentAs](M_Grasshopper_GUI_GH_DocumentEditor_ScriptAccess_SaveDocumentAs.htm)|
Saves the currently active document to disk.  
![Public method](../icons/pubmethod.gif)|
[ScriptAccess_SaveDocumentAs(String)](M_Grasshopper_GUI_GH_DocumentEditor_ScriptAccess_SaveDocumentAs_1.htm)|
Saves the currently active document to disk.  
![Public method](../icons/pubmethod.gif)|
[SetStatusBarEvent](M_Grasshopper_GUI_GH_DocumentEditor_SetStatusBarEvent.htm)|
Set a new message on the Grasshopper status bar.  
![Public method](../icons/pubmethod.gif)|
[ToggleForm](M_Grasshopper_GUI_GH_DocumentEditor_ToggleForm.htm)|  Collapses
the form if it's currently expanded or expands the form if it's currently
collapsed.  
![Protected method](../icons/protmethod.gif)|
[WndProc](M_Grasshopper_GUI_GH_DocumentEditor_WndProc.htm)|  WndProc is
overridden in order to allow for title-bar double-click (un)folding.
(Overrides
[FormWndProc(Message)](https://docs.microsoft.com/dotnet/api/system.windows.forms.form.wndproc#system-
windows-forms-form-wndproc\(system-windows-forms-message@\)).)  
Top

![](../icons/SectionExpanded.png)Events

| Name| Description  
---|---|---  
![Public event](../icons/pubevent.gif)![Static member](../icons/static.gif)|
[AggregateShortcutMenuItems](E_Grasshopper_GUI_GH_DocumentEditor_AggregateShortcutMenuItems.htm)|
This event is raised whenever a GH_DocumentEditor collects all shortcuttable
menu items. If you added items to the menu and you want to be able to have
custom shortcuts on these items, you must handle this event and insert your
own items.  
![Public event](../icons/pubevent.gif)|
[EditorFoldStateChanged](E_Grasshopper_GUI_GH_DocumentEditor_EditorFoldStateChanged.htm)|
This event is raised whenever the main windows folds or unfolds.  
Top

![](../icons/SectionExpanded.png)Extension Methods

| Name| Description  
---|---|---  
![Public Extension Method](../icons/pubextension.gif)|
[ToEto](M_Grasshopper_EtoExtensions_ToEto_8.htm)| Overloaded. (Defined by
[EtoExtensions](T_Grasshopper_EtoExtensions.htm).)  
![Public Extension Method](../icons/pubextension.gif)|
[ToEto](M_Grasshopper_EtoExtensions_ToEto_7.htm)| Overloaded. (Defined by
[EtoExtensions](T_Grasshopper_EtoExtensions.htm).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

