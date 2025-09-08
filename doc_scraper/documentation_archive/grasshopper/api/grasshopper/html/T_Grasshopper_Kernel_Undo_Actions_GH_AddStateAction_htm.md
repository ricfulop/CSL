---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Undo_Actions_GH_AddStateAction.htm
scraped_at: 2025-09-08T16:22:09.777790
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Undo.Actions](../html/N_Grasshopper_Kernel_Undo_Actions.htm
"Grasshopper.Kernel.Undo.Actions")

[GH_AddStateAction
Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_AddStateAction.htm
"GH_AddStateAction Class")

[GH_AddStateAction Constructor
](../html/M_Grasshopper_Kernel_Undo_Actions_GH_AddStateAction__ctor.htm
"GH_AddStateAction Constructor ")

[GH_AddStateAction
Properties](../html/Properties_T_Grasshopper_Kernel_Undo_Actions_GH_AddStateAction.htm
"GH_AddStateAction Properties")

[GH_AddStateAction
Methods](../html/Methods_T_Grasshopper_Kernel_Undo_Actions_GH_AddStateAction.htm
"GH_AddStateAction Methods")

[GH_AddStateAction
Fields](../html/Fields_T_Grasshopper_Kernel_Undo_Actions_GH_AddStateAction.htm
"GH_AddStateAction Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_AddStateAction Class  
  
---  
  
Record the addition of a single solution state to a document.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.Kernel.UndoGH_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm)  
[Grasshopper.Kernel.UndoGH_ArchivedUndoAction](T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm)  
Grasshopper.Kernel.Undo.ActionsGH_AddStateAction  

**Namespace:**
[Grasshopper.Kernel.Undo.Actions](N_Grasshopper_Kernel_Undo_Actions.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_AddStateAction : GH_ArchivedUndoAction
    
    
    Public Class GH_AddStateAction
    	Inherits GH_ArchivedUndoAction

The GH_AddStateAction type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_AddStateAction](M_Grasshopper_Kernel_Undo_Actions_GH_AddStateAction__ctor.htm)|
Initializes a new instance of the GH_AddStateAction class  
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
[Deserialize](M_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction_Deserialize.htm)|
Deserializes the obj from the local archive.  (Inherited from
[GH_ArchivedUndoAction](T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm).)  
![Protected method](../icons/protmethod.gif)|
[Internal_Redo](M_Grasshopper_Kernel_Undo_Actions_GH_AddStateAction_Internal_Redo.htm)|
(Overrides
[GH_UndoActionInternal_Redo(GH_Document)](M_Grasshopper_Kernel_Undo_GH_UndoAction_Internal_Redo.htm).)  
![Protected method](../icons/protmethod.gif)|
[Internal_Undo](M_Grasshopper_Kernel_Undo_Actions_GH_AddStateAction_Internal_Undo.htm)|
(Overrides
[GH_UndoActionInternal_Undo(GH_Document)](M_Grasshopper_Kernel_Undo_GH_UndoAction_Internal_Undo.htm).)  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_Undo_Actions_GH_AddStateAction_Read.htm)|
(Overrides
[GH_ArchivedUndoActionRead(GH_IReader)](M_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction_Read.htm).)  
![Public method](../icons/pubmethod.gif)|
[Redo](M_Grasshopper_Kernel_Undo_GH_UndoAction_Redo.htm)|  (Inherited from
[GH_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).)  
![Protected method](../icons/protmethod.gif)|
[Serialize](M_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction_Serialize.htm)|
Serializes the obj into the local archive.  (Inherited from
[GH_ArchivedUndoAction](T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm).)  
![Protected method](../icons/protmethod.gif)|
[SerializeToByteArray](M_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction_SerializeToByteArray.htm)|
Serializes the obj into the local archive.  (Inherited from
[GH_ArchivedUndoAction](T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm).)  
![Public method](../icons/pubmethod.gif)|
[Undo](M_Grasshopper_Kernel_Undo_GH_UndoAction_Undo.htm)|  (Inherited from
[GH_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).)  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_Undo_Actions_GH_AddStateAction_Write.htm)|
(Overrides
[GH_ArchivedUndoActionWrite(GH_IWriter)](M_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction_Write.htm).)  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Protected field](../icons/protfield.gif)|
[m_data](F_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction_m_data.htm)|
Internal data storage for serialized archives.  (Inherited from
[GH_ArchivedUndoAction](T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Undo.Actions
Namespace](N_Grasshopper_Kernel_Undo_Actions.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

