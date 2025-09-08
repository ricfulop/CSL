---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Undo_GH_UndoRecord.htm
scraped_at: 2025-09-08T16:22:03.737655
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Undo](../html/N_Grasshopper_Kernel_Undo.htm
"Grasshopper.Kernel.Undo")

[GH_UndoRecord Class](../html/T_Grasshopper_Kernel_Undo_GH_UndoRecord.htm
"GH_UndoRecord Class")

[GH_UndoRecord Constructor
](../html/Overload_Grasshopper_Kernel_Undo_GH_UndoRecord__ctor.htm
"GH_UndoRecord Constructor ")

[GH_UndoRecord
Properties](../html/Properties_T_Grasshopper_Kernel_Undo_GH_UndoRecord.htm
"GH_UndoRecord Properties")

[GH_UndoRecord
Methods](../html/Methods_T_Grasshopper_Kernel_Undo_GH_UndoRecord.htm
"GH_UndoRecord Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_UndoRecord Class  
  
---  
  
Represents a single undo/redo record. A single record may contain any number
of undo actions.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Kernel.UndoGH_UndoRecord  

**Namespace:** [Grasshopper.Kernel.Undo](N_Grasshopper_Kernel_Undo.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_UndoRecord
    
    
    Public Class GH_UndoRecord

The GH_UndoRecord type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_UndoRecord](M_Grasshopper_Kernel_Undo_GH_UndoRecord__ctor.htm)|
Initializes a new instance of the GH_UndoRecord class  
![Public method](../icons/pubmethod.gif)|
[GH_UndoRecord(String)](M_Grasshopper_Kernel_Undo_GH_UndoRecord__ctor_1.htm)|
Initializes a new instance of the GH_UndoRecord class  
![Public method](../icons/pubmethod.gif)| [GH_UndoRecord(String,
IGH_UndoAction)](M_Grasshopper_Kernel_Undo_GH_UndoRecord__ctor_2.htm)|
Initializes a new instance of the GH_UndoRecord class  
![Public method](../icons/pubmethod.gif)| [GH_UndoRecord(String,
IGH_UndoAction)](M_Grasshopper_Kernel_Undo_GH_UndoRecord__ctor_3.htm)|
Initializes a new instance of the GH_UndoRecord class  
![Public method](../icons/pubmethod.gif)| [GH_UndoRecord(String,
IEnumerableIGH_UndoAction)](M_Grasshopper_Kernel_Undo_GH_UndoRecord__ctor_4.htm)|
Initializes a new instance of the GH_UndoRecord class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[ActionCount](P_Grasshopper_Kernel_Undo_GH_UndoRecord_ActionCount.htm)|  Gets
the number of actions stored in this record.  
![Public property](../icons/pubproperty.gif)|
[Actions](P_Grasshopper_Kernel_Undo_GH_UndoRecord_Actions.htm)|  Gets or sets
the actions inside this record.  
![Public property](../icons/pubproperty.gif)|
[ExpiresDisplay](P_Grasshopper_Kernel_Undo_GH_UndoRecord_ExpiresDisplay.htm)|
Gets the display expiration flag for this event. If True, the Rhino viewports
will be redrawn once the entire undo record has been completed. If
ExpiresSolution is set to true, ExpriresDisplay is implied.  
![Public property](../icons/pubproperty.gif)|
[ExpiresSolution](P_Grasshopper_Kernel_Undo_GH_UndoRecord_ExpiresSolution.htm)|
Gets the solution expiration flag for this event. If True, the solution needs
to be recalculated once the entire undo record has been completed.  
![Public property](../icons/pubproperty.gif)|
[Guid](P_Grasshopper_Kernel_Undo_GH_UndoRecord_Guid.htm)|  Gets the ID of this
undo item. Every undo record has a unique ID.  
![Public property](../icons/pubproperty.gif)|
[Name](P_Grasshopper_Kernel_Undo_GH_UndoRecord_Name.htm)|  Gets or sets the
name of the undo record (as displayed in the menu)  
![Public property](../icons/pubproperty.gif)|
[State](P_Grasshopper_Kernel_Undo_GH_UndoRecord_State.htm)|  Gets the undo
state of this record. The state dictates which action are legal.  
![Public property](../icons/pubproperty.gif)|
[Time](P_Grasshopper_Kernel_Undo_GH_UndoRecord_Time.htm)|  Gets the time at
which this record was created.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AddAction](M_Grasshopper_Kernel_Undo_GH_UndoRecord_AddAction.htm)|  Append an
undo action to this record. You should only do this prior to calling undo for
the first time.  
![Public method](../icons/pubmethod.gif)|
[Redo](M_Grasshopper_Kernel_Undo_GH_UndoRecord_Redo.htm)|  
![Public method](../icons/pubmethod.gif)|
[Undo](M_Grasshopper_Kernel_Undo_GH_UndoRecord_Undo.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Undo Namespace](N_Grasshopper_Kernel_Undo.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

