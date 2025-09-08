---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm
scraped_at: 2025-09-08T16:22:00.743617
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Undo](../html/N_Grasshopper_Kernel_Undo.htm
"Grasshopper.Kernel.Undo")

[GH_ObjectUndoAction
Class](../html/T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm
"GH_ObjectUndoAction Class")

[GH_ObjectUndoAction Constructor
](../html/M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction__ctor.htm
"GH_ObjectUndoAction Constructor ")

[GH_ObjectUndoAction
Properties](../html/Properties_T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm
"GH_ObjectUndoAction Properties")

[GH_ObjectUndoAction
Methods](../html/Methods_T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm
"GH_ObjectUndoAction Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_ObjectUndoAction Class  
  
---  
  
Utility base class for undo actions that operate on a single
IGH_DocumentObject.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.Kernel.UndoGH_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm)  
Grasshopper.Kernel.UndoGH_ObjectUndoAction  
More...

**Namespace:** [Grasshopper.Kernel.Undo](N_Grasshopper_Kernel_Undo.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public abstract class GH_ObjectUndoAction : GH_UndoAction
    
    
    Public MustInherit Class GH_ObjectUndoAction
    	Inherits GH_UndoAction

The GH_ObjectUndoAction type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[GH_ObjectUndoAction](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction__ctor.htm)|
Initializes a new instance of the GH_ObjectUndoAction class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[ExpiresDisplay](P_Grasshopper_Kernel_Undo_GH_UndoAction_ExpiresDisplay.htm)|
Override this property if you want the Rhino viewport display to refresh upon
undo completion.  (Inherited from
[GH_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).)  
![Public property](../icons/pubproperty.gif)|
[ExpiresSolution](P_Grasshopper_Kernel_Undo_GH_UndoAction_ExpiresSolution.htm)|
Override this property if you want the Grasshopper solution to refresh upon
undo completion.  (Inherited from
[GH_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).)  
![Public property](../icons/pubproperty.gif)|
[State](P_Grasshopper_Kernel_Undo_GH_UndoAction_State.htm)|  (Inherited from
[GH_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[Internal_Redo](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction_Internal_Redo.htm)|
(Overrides
[GH_UndoActionInternal_Redo(GH_Document)](M_Grasshopper_Kernel_Undo_GH_UndoAction_Internal_Redo.htm).)  
![Protected method](../icons/protmethod.gif)|
[Internal_Undo](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction_Internal_Undo.htm)|
(Overrides
[GH_UndoActionInternal_Undo(GH_Document)](M_Grasshopper_Kernel_Undo_GH_UndoAction_Internal_Undo.htm).)  
![Protected method](../icons/protmethod.gif)|
[Object_Redo](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction_Object_Redo.htm)|  
![Protected method](../icons/protmethod.gif)|
[Object_Undo](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction_Object_Undo.htm)|  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_Undo_GH_UndoAction_Read.htm)|  (Inherited from
[GH_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).)  
![Public method](../icons/pubmethod.gif)|
[Redo](M_Grasshopper_Kernel_Undo_GH_UndoAction_Redo.htm)|  (Inherited from
[GH_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).)  
![Public method](../icons/pubmethod.gif)|
[Undo](M_Grasshopper_Kernel_Undo_GH_UndoAction_Undo.htm)|  (Inherited from
[GH_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).)  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_Undo_GH_UndoAction_Write.htm)|  (Inherited from
[GH_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Undo Namespace](N_Grasshopper_Kernel_Undo.htm)

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.Kernel.UndoGH_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm)  
Grasshopper.Kernel.UndoGH_ObjectUndoAction  
[Grasshopper.Kernel.Undo.ActionsGH_DataMatchingAction](T_Grasshopper_Kernel_Undo_Actions_GH_DataMatchingAction.htm)  
[Grasshopper.Kernel.Undo.ActionsGH_DataModificationAction](T_Grasshopper_Kernel_Undo_Actions_GH_DataModificationAction.htm)  
[Grasshopper.Kernel.Undo.ActionsGH_HiddenAction](T_Grasshopper_Kernel_Undo_Actions_GH_HiddenAction.htm)  
[Grasshopper.Kernel.Undo.ActionsGH_IconDisplayAction](T_Grasshopper_Kernel_Undo_Actions_GH_IconDisplayAction.htm)  
[Grasshopper.Kernel.Undo.ActionsGH_IconOverrideAction](T_Grasshopper_Kernel_Undo_Actions_GH_IconOverrideAction.htm)  
[Grasshopper.Kernel.Undo.ActionsGH_LayoutAction](T_Grasshopper_Kernel_Undo_Actions_GH_LayoutAction.htm)  
[Grasshopper.Kernel.Undo.ActionsGH_LockedAction](T_Grasshopper_Kernel_Undo_Actions_GH_LockedAction.htm)  
[Grasshopper.Kernel.Undo.ActionsGH_NickNameAction](T_Grasshopper_Kernel_Undo_Actions_GH_NickNameAction.htm)  
[Grasshopper.Kernel.Undo.ActionsGH_PersistentDataActionT](T_Grasshopper_Kernel_Undo_Actions_GH_PersistentDataAction_1.htm)  
[Grasshopper.Kernel.Undo.ActionsGH_PivotAction](T_Grasshopper_Kernel_Undo_Actions_GH_PivotAction.htm)  
[Grasshopper.Kernel.Undo.ActionsGH_WireDisplayAction](T_Grasshopper_Kernel_Undo_Actions_GH_WireDisplayAction.htm)  

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

