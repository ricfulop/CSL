---
url: https://developer.rhino3d.com/api/grasshopper/html/N_Grasshopper_Kernel_Undo_Actions.htm#!
scraped_at: 2025-09-08T16:22:07.768006
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Undo.Actions](../html/N_Grasshopper_Kernel_Undo_Actions.htm
"Grasshopper.Kernel.Undo.Actions")

[GH_AddObjectAction
Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_AddObjectAction.htm
"GH_AddObjectAction Class")

[GH_AddStateAction
Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_AddStateAction.htm
"GH_AddStateAction Class")

[GH_DataMatchingAction
Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_DataMatchingAction.htm
"GH_DataMatchingAction Class")

[GH_DataModificationAction
Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_DataModificationAction.htm
"GH_DataModificationAction Class")

[GH_GenericObjectAction
Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_GenericObjectAction.htm
"GH_GenericObjectAction Class")

[GH_HiddenAction
Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_HiddenAction.htm
"GH_HiddenAction Class")

[GH_IconDisplayAction
Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_IconDisplayAction.htm
"GH_IconDisplayAction Class")

[GH_IconOverrideAction
Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_IconOverrideAction.htm
"GH_IconOverrideAction Class")

[GH_LayoutAction
Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_LayoutAction.htm
"GH_LayoutAction Class")

[GH_LockedAction
Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_LockedAction.htm
"GH_LockedAction Class")

[GH_NickNameAction
Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_NickNameAction.htm
"GH_NickNameAction Class")

[GH_PersistentDataAction(T)
Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_PersistentDataAction_1.htm
"GH_PersistentDataAction\(T\) Class")

[GH_PivotAction
Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_PivotAction.htm
"GH_PivotAction Class")

[GH_RemoveObjectAction
Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_RemoveObjectAction.htm
"GH_RemoveObjectAction Class")

[GH_RemoveStateAction
Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_RemoveStateAction.htm
"GH_RemoveStateAction Class")

[GH_WireAction
Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_WireAction.htm
"GH_WireAction Class")

[GH_WireDisplayAction
Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_WireDisplayAction.htm
"GH_WireDisplayAction Class")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# Grasshopper.Kernel.Undo.Actions Namespace  
  
---  
  
Contains a set of predefined undo/redo actions to make certain undo records
simpler.

![](../icons/SectionExpanded.png)Classes

| Class| Description  
---|---|---  
![Public class](../icons/pubclass.gif)|
[GH_AddObjectAction](T_Grasshopper_Kernel_Undo_Actions_GH_AddObjectAction.htm)|
Records a single object addition.  
![Public class](../icons/pubclass.gif)|
[GH_AddStateAction](T_Grasshopper_Kernel_Undo_Actions_GH_AddStateAction.htm)|
Record the addition of a single solution state to a document.  
![Public class](../icons/pubclass.gif)|
[GH_DataMatchingAction](T_Grasshopper_Kernel_Undo_Actions_GH_DataMatchingAction.htm)|
Records a single Component DataComparison event.  
![Public class](../icons/pubclass.gif)|
[GH_DataModificationAction](T_Grasshopper_Kernel_Undo_Actions_GH_DataModificationAction.htm)|
Records a single Parameter DataModification event.  
![Public class](../icons/pubclass.gif)|
[GH_GenericObjectAction](T_Grasshopper_Kernel_Undo_Actions_GH_GenericObjectAction.htm)|
Records a single object change. Object changes are undone/redone by
(de)serializing the objects. Object changes also keep track of all wires
feeding into and coming out of the object.  
![Public class](../icons/pubclass.gif)|
[GH_HiddenAction](T_Grasshopper_Kernel_Undo_Actions_GH_HiddenAction.htm)|
Records a single object Preview event.  
![Public class](../icons/pubclass.gif)|
[GH_IconDisplayAction](T_Grasshopper_Kernel_Undo_Actions_GH_IconDisplayAction.htm)|
Records a single icon display mode event.  
![Public class](../icons/pubclass.gif)|
[GH_IconOverrideAction](T_Grasshopper_Kernel_Undo_Actions_GH_IconOverrideAction.htm)|
Records a single icon override event.  
![Public class](../icons/pubclass.gif)|
[GH_LayoutAction](T_Grasshopper_Kernel_Undo_Actions_GH_LayoutAction.htm)|
Records a single object layout event. Useful for tracking object resizes.  
![Public class](../icons/pubclass.gif)|
[GH_LockedAction](T_Grasshopper_Kernel_Undo_Actions_GH_LockedAction.htm)|
Records a single object Enabled event.  
![Public class](../icons/pubclass.gif)|
[GH_NickNameAction](T_Grasshopper_Kernel_Undo_Actions_GH_NickNameAction.htm)|
Records a single object NickName and IconDisplayMode event.  
![Public class](../icons/pubclass.gif)|
[GH_PersistentDataActionT](T_Grasshopper_Kernel_Undo_Actions_GH_PersistentDataAction_1.htm)|
Records the changes in the persistent data of a parameter.  
![Public class](../icons/pubclass.gif)|
[GH_PivotAction](T_Grasshopper_Kernel_Undo_Actions_GH_PivotAction.htm)|
Records a single object pivot event. Useful for tracking object movement.  
![Public class](../icons/pubclass.gif)|
[GH_RemoveObjectAction](T_Grasshopper_Kernel_Undo_Actions_GH_RemoveObjectAction.htm)|
Records a single object removal.  
![Public class](../icons/pubclass.gif)|
[GH_RemoveStateAction](T_Grasshopper_Kernel_Undo_Actions_GH_RemoveStateAction.htm)|
Record the removal of a single solution state from a document.  
![Public class](../icons/pubclass.gif)|
[GH_WireAction](T_Grasshopper_Kernel_Undo_Actions_GH_WireAction.htm)|  Records
any change to the input wires of a given parameter.  
![Public class](../icons/pubclass.gif)|
[GH_WireDisplayAction](T_Grasshopper_Kernel_Undo_Actions_GH_WireDisplayAction.htm)|
Records a single wire display mode event.  
  
Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

