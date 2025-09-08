---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Undo_Actions_GH_PersistentDataAction_1.htm
scraped_at: 2025-09-08T16:22:19.813544
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Undo.Actions](../html/N_Grasshopper_Kernel_Undo_Actions.htm
"Grasshopper.Kernel.Undo.Actions")

[GH_PersistentDataAction(T)
Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_PersistentDataAction_1.htm
"GH_PersistentDataAction\(T\) Class")

[GH_PersistentDataAction(T) Constructor
](../html/M_Grasshopper_Kernel_Undo_Actions_GH_PersistentDataAction_1__ctor.htm
"GH_PersistentDataAction\(T\) Constructor ")

[GH_PersistentDataAction(T)
Properties](../html/Properties_T_Grasshopper_Kernel_Undo_Actions_GH_PersistentDataAction_1.htm
"GH_PersistentDataAction\(T\) Properties")

[GH_PersistentDataAction(T)
Methods](../html/Methods_T_Grasshopper_Kernel_Undo_Actions_GH_PersistentDataAction_1.htm
"GH_PersistentDataAction\(T\) Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_PersistentDataActionT Class  
  
---  
  
Records the changes in the persistent data of a parameter.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.Kernel.UndoGH_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm)  
[Grasshopper.Kernel.UndoGH_ObjectUndoAction](T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm)  
Grasshopper.Kernel.Undo.ActionsGH_PersistentDataActionT  

**Namespace:**
[Grasshopper.Kernel.Undo.Actions](N_Grasshopper_Kernel_Undo_Actions.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_PersistentDataAction<T> : GH_ObjectUndoAction
    where T : class, IGH_Goo
    
    
    
    Public Class GH_PersistentDataAction(Of T As {Class, IGH_Goo})
    	Inherits GH_ObjectUndoAction

#### Type Parameters

T

    

The GH_PersistentDataActionT type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_PersistentDataActionT](M_Grasshopper_Kernel_Undo_Actions_GH_PersistentDataAction_1__ctor.htm)|
Initializes a new instance of the GH_PersistentDataActionT class  
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
[ExpiresSolution](P_Grasshopper_Kernel_Undo_Actions_GH_PersistentDataAction_1_ExpiresSolution.htm)|
(Overrides
[GH_UndoActionExpiresSolution](P_Grasshopper_Kernel_Undo_GH_UndoAction_ExpiresSolution.htm).)  
![Public property](../icons/pubproperty.gif)|
[State](P_Grasshopper_Kernel_Undo_GH_UndoAction_State.htm)|  (Inherited from
[GH_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[Internal_Redo](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction_Internal_Redo.htm)|
(Inherited from
[GH_ObjectUndoAction](T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm).)  
![Protected method](../icons/protmethod.gif)|
[Internal_Undo](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction_Internal_Undo.htm)|
(Inherited from
[GH_ObjectUndoAction](T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm).)  
![Protected method](../icons/protmethod.gif)|
[Object_Redo](M_Grasshopper_Kernel_Undo_Actions_GH_PersistentDataAction_1_Object_Redo.htm)|
(Overrides [GH_ObjectUndoActionObject_Redo(GH_Document,
IGH_DocumentObject)](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction_Object_Redo.htm).)  
![Protected method](../icons/protmethod.gif)|
[Object_Undo](M_Grasshopper_Kernel_Undo_Actions_GH_PersistentDataAction_1_Object_Undo.htm)|
(Overrides [GH_ObjectUndoActionObject_Undo(GH_Document,
IGH_DocumentObject)](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction_Object_Undo.htm).)  
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

[Grasshopper.Kernel.Undo.Actions
Namespace](N_Grasshopper_Kernel_Undo_Actions.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

