---
url: https://developer.rhino3d.com/api/grasshopper/html/N_Grasshopper_Kernel_Undo.htm#!
scraped_at: 2025-09-08T16:21:58.716190
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Undo](../html/N_Grasshopper_Kernel_Undo.htm
"Grasshopper.Kernel.Undo")

[GH_ArchivedUndoAction
Class](../html/T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm
"GH_ArchivedUndoAction Class")

[GH_ObjectUndoAction
Class](../html/T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm
"GH_ObjectUndoAction Class")

[GH_UndoAction Class](../html/T_Grasshopper_Kernel_Undo_GH_UndoAction.htm
"GH_UndoAction Class")

[GH_UndoException
Class](../html/T_Grasshopper_Kernel_Undo_GH_UndoException.htm
"GH_UndoException Class")

[GH_UndoRecord Class](../html/T_Grasshopper_Kernel_Undo_GH_UndoRecord.htm
"GH_UndoRecord Class")

[GH_UndoServer Class](../html/T_Grasshopper_Kernel_Undo_GH_UndoServer.htm
"GH_UndoServer Class")

[GH_UndoState Enumeration](../html/T_Grasshopper_Kernel_Undo_GH_UndoState.htm
"GH_UndoState Enumeration")

[IGH_UndoAction
Interface](../html/T_Grasshopper_Kernel_Undo_IGH_UndoAction.htm
"IGH_UndoAction Interface")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# Grasshopper.Kernel.Undo Namespace  
  
---  
  
Namespace that contains all the types and methods to do with the recording and
re-instating GHX undo/redo data.

![](../icons/SectionExpanded.png)Classes

| Class| Description  
---|---|---  
![Public class](../icons/pubclass.gif)|
[GH_ArchivedUndoAction](T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm)|
Base class implementation for undo actions that require (de)serialization of
data.  
![Public class](../icons/pubclass.gif)|
[GH_ObjectUndoAction](T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm)|
Utility base class for undo actions that operate on a single
IGH_DocumentObject.  
![Public class](../icons/pubclass.gif)|
[GH_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm)|  Base class
implementation for undo actions.  
![Public class](../icons/pubclass.gif)|
[GH_UndoException](T_Grasshopper_Kernel_Undo_GH_UndoException.htm)|  Exception
associated with undo events  
![Public class](../icons/pubclass.gif)|
[GH_UndoRecord](T_Grasshopper_Kernel_Undo_GH_UndoRecord.htm)|  Represents a
single undo/redo record. A single record may contain any number of undo
actions.  
![Public class](../icons/pubclass.gif)|
[GH_UndoServer](T_Grasshopper_Kernel_Undo_GH_UndoServer.htm)|  Provides access
to a documents undo data.  
  
![](../icons/SectionExpanded.png)Interfaces

| Interface| Description  
---|---|---  
![Public interface](../icons/pubinterface.gif)|
[IGH_UndoAction](T_Grasshopper_Kernel_Undo_IGH_UndoAction.htm)|  Base
interface for all undo/redo actions  
  
![](../icons/SectionExpanded.png)Enumerations

| Enumeration| Description  
---|---|---  
![Public enumeration](../icons/pubenumeration.gif)|
[GH_UndoState](T_Grasshopper_Kernel_Undo_GH_UndoState.htm)|  State enumeration
for undo records.  
  
Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

