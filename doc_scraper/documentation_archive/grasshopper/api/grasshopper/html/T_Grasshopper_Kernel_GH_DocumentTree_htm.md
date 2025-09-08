---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_DocumentTree.htm
scraped_at: 2025-09-08T16:16:36.319462
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_DocumentTree Class](../html/T_Grasshopper_Kernel_GH_DocumentTree.htm
"GH_DocumentTree Class")

[GH_DocumentTree Constructor
](../html/M_Grasshopper_Kernel_GH_DocumentTree__ctor.htm "GH_DocumentTree
Constructor ")

[GH_DocumentTree
Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocumentTree.htm
"GH_DocumentTree Properties")

[GH_DocumentTree
Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentTree.htm
"GH_DocumentTree Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_DocumentTree Class  
  
---  
  
Represents a hierarchical tree of documents that are subsidiary to one
another.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_DocumentTree  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_DocumentTree : IGH_DebugDescription
    
    
    Public Class GH_DocumentTree
    	Implements IGH_DebugDescription

The GH_DocumentTree type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_DocumentTree](M_Grasshopper_Kernel_GH_DocumentTree__ctor.htm)|  Create a
new document tree.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[FlatCollection](P_Grasshopper_Kernel_GH_DocumentTree_FlatCollection.htm)|
Gets a flat collection of all documents. The most subsidiary documents are at
the start of the collection.  
![Public property](../icons/pubproperty.gif)|
[Root](P_Grasshopper_Kernel_GH_DocumentTree_Root.htm)|  Gets the root node for
this document.  
![Public property](../icons/pubproperty.gif)|
[RootDocument](P_Grasshopper_Kernel_GH_DocumentTree_RootDocument.htm)|  Gets
the document inside the root node of this tree.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AppendToDebugLog](M_Grasshopper_Kernel_GH_DocumentTree_AppendToDebugLog.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

