---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_IGH_DocumentOwner.htm
scraped_at: 2025-09-08T16:18:30.837197
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH_DocumentOwner
Interface](../html/T_Grasshopper_Kernel_IGH_DocumentOwner.htm
"IGH_DocumentOwner Interface")

[IGH_DocumentOwner
Methods](../html/Methods_T_Grasshopper_Kernel_IGH_DocumentOwner.htm
"IGH_DocumentOwner Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_DocumentOwner Interface  
  
---  
  
Implement this interface if you want to be the owner assigned to a document in
the Grasshopper documentserver.

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_DocumentOwner
    
    
    Public Interface IGH_DocumentOwner

The IGH_DocumentOwner type exposes the following members.

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[DocumentClosed](M_Grasshopper_Kernel_IGH_DocumentOwner_DocumentClosed.htm)|
This method will be called whenever the owner document was closed.  
![Public method](../icons/pubmethod.gif)|
[DocumentModified](M_Grasshopper_Kernel_IGH_DocumentOwner_DocumentModified.htm)|
This method will be called whenever the owned document is modified.  
![Public method](../icons/pubmethod.gif)|
[OwnerDocument](M_Grasshopper_Kernel_IGH_DocumentOwner_OwnerDocument.htm)|  If
the IGH_DocumentOwner is part of a GH_Document of its own, this function will
return that document.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

