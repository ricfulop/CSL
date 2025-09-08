---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Undo_GH_UndoAction.htm
scraped_at: 2025-09-08T16:22:01.727646
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Undo](../html/N_Grasshopper_Kernel_Undo.htm
"Grasshopper.Kernel.Undo")

[GH_UndoAction Class](../html/T_Grasshopper_Kernel_Undo_GH_UndoAction.htm
"GH_UndoAction Class")

[GH_UndoAction Constructor
](../html/M_Grasshopper_Kernel_Undo_GH_UndoAction__ctor.htm "GH_UndoAction
Constructor ")

[GH_UndoAction
Properties](../html/Properties_T_Grasshopper_Kernel_Undo_GH_UndoAction.htm
"GH_UndoAction Properties")

[GH_UndoAction
Methods](../html/Methods_T_Grasshopper_Kernel_Undo_GH_UndoAction.htm
"GH_UndoAction Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_UndoAction Class  
  
---  
  
Base class implementation for undo actions.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Kernel.UndoGH_UndoAction  
[Grasshopper.Kernel.Undo.ActionsGH_AddObjectAction](T_Grasshopper_Kernel_Undo_Actions_GH_AddObjectAction.htm)  
[Grasshopper.Kernel.Undo.ActionsGH_WireAction](T_Grasshopper_Kernel_Undo_Actions_GH_WireAction.htm)  
[Grasshopper.Kernel.UndoGH_ArchivedUndoAction](T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm)  
[Grasshopper.Kernel.UndoGH_ObjectUndoAction](T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm)  

**Namespace:** [Grasshopper.Kernel.Undo](N_Grasshopper_Kernel_Undo.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public abstract class GH_UndoAction : IGH_UndoAction
    
    
    Public MustInherit Class GH_UndoAction
    	Implements IGH_UndoAction

The GH_UndoAction type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[GH_UndoAction](M_Grasshopper_Kernel_Undo_GH_UndoAction__ctor.htm)|
Initializes a new instance of the GH_UndoAction class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[ExpiresDisplay](P_Grasshopper_Kernel_Undo_GH_UndoAction_ExpiresDisplay.htm)|
Override this property if you want the Rhino viewport display to refresh upon
undo completion.  
![Public property](../icons/pubproperty.gif)|
[ExpiresSolution](P_Grasshopper_Kernel_Undo_GH_UndoAction_ExpiresSolution.htm)|
Override this property if you want the Grasshopper solution to refresh upon
undo completion.  
![Public property](../icons/pubproperty.gif)|
[State](P_Grasshopper_Kernel_Undo_GH_UndoAction_State.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[Internal_Redo](M_Grasshopper_Kernel_Undo_GH_UndoAction_Internal_Redo.htm)|  
![Protected method](../icons/protmethod.gif)|
[Internal_Undo](M_Grasshopper_Kernel_Undo_GH_UndoAction_Internal_Undo.htm)|  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_Undo_GH_UndoAction_Read.htm)|  
![Public method](../icons/pubmethod.gif)|
[Redo](M_Grasshopper_Kernel_Undo_GH_UndoAction_Redo.htm)|  
![Public method](../icons/pubmethod.gif)|
[Undo](M_Grasshopper_Kernel_Undo_GH_UndoAction_Undo.htm)|  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_Undo_GH_UndoAction_Write.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Undo Namespace](N_Grasshopper_Kernel_Undo.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

