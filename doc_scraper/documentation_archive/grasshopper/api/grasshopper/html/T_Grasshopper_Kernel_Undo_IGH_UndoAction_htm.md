---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Undo_IGH_UndoAction.htm
scraped_at: 2025-09-08T16:22:06.760352
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Undo](../html/N_Grasshopper_Kernel_Undo.htm
"Grasshopper.Kernel.Undo")

[IGH_UndoAction
Interface](../html/T_Grasshopper_Kernel_Undo_IGH_UndoAction.htm
"IGH_UndoAction Interface")

[IGH_UndoAction
Properties](../html/Properties_T_Grasshopper_Kernel_Undo_IGH_UndoAction.htm
"IGH_UndoAction Properties")

[IGH_UndoAction
Methods](../html/Methods_T_Grasshopper_Kernel_Undo_IGH_UndoAction.htm
"IGH_UndoAction Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_UndoAction Interface  
  
---  
  
Base interface for all undo/redo actions

**Namespace:** [Grasshopper.Kernel.Undo](N_Grasshopper_Kernel_Undo.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_UndoAction : GH_ISerializable
    
    
    Public Interface IGH_UndoAction
    	Inherits GH_ISerializable

The IGH_UndoAction type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[ExpiresDisplay](P_Grasshopper_Kernel_Undo_IGH_UndoAction_ExpiresDisplay.htm)|
Gets the display expiration flag for this event. If True, the Rhino viewports
will be redrawn once the entire undo record has been completed. If
ExpiresSolution is set to true, ExpriresDisplay is implied.  
![Public property](../icons/pubproperty.gif)|
[ExpiresSolution](P_Grasshopper_Kernel_Undo_IGH_UndoAction_ExpiresSolution.htm)|
Gets the solution expiration flag for this event. If True, the solution needs
to be recalculated once the entire undo record has been completed.  
![Public property](../icons/pubproperty.gif)|
[State](P_Grasshopper_Kernel_Undo_IGH_UndoAction_State.htm)|  Gets the current
state of the undo action.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Read](M_GH_IO_GH_ISerializable_Read.htm)|  This method is called whenever the
instance is required to deserialize itself.  (Inherited from
[GH_ISerializable](T_GH_IO_GH_ISerializable.htm).)  
![Public method](../icons/pubmethod.gif)|
[Redo](M_Grasshopper_Kernel_Undo_IGH_UndoAction_Redo.htm)|  Redo the action
stored in this record.  
![Public method](../icons/pubmethod.gif)|
[Undo](M_Grasshopper_Kernel_Undo_IGH_UndoAction_Undo.htm)|  Undo the action
stored in this record.  
![Public method](../icons/pubmethod.gif)|
[Write](M_GH_IO_GH_ISerializable_Write.htm)|  This method is called whenever
the instance is required to serialize itself.  (Inherited from
[GH_ISerializable](T_GH_IO_GH_ISerializable.htm).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Undo Namespace](N_Grasshopper_Kernel_Undo.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

