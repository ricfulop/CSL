---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_DocumentServer.htm
scraped_at: 2025-09-08T16:16:32.315988
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_DocumentServer Class](../html/T_Grasshopper_Kernel_GH_DocumentServer.htm
"GH_DocumentServer Class")

[GH_DocumentServer Constructor
](../html/M_Grasshopper_Kernel_GH_DocumentServer__ctor.htm "GH_DocumentServer
Constructor ")

[GH_DocumentServer
Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocumentServer.htm
"GH_DocumentServer Properties")

[GH_DocumentServer
Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentServer.htm
"GH_DocumentServer Methods")

[GH_DocumentServer
Events](../html/Events_T_Grasshopper_Kernel_GH_DocumentServer.htm
"GH_DocumentServer Events")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_DocumentServer Class  
  
---  
  
Manages and maintains a collection of GH_Documents.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_DocumentServer  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class GH_DocumentServer : IEnumerable<GH_Document>
    
    
    Public NotInheritable Class GH_DocumentServer
    	Implements IEnumerable(Of GH_Document)

The GH_DocumentServer type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_DocumentServer](M_Grasshopper_Kernel_GH_DocumentServer__ctor.htm)|
Initializes a new instance of the GH_DocumentServer class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Document](P_Grasshopper_Kernel_GH_DocumentServer_Document.htm)|  Gets the
document at the given index.  
![Public property](../icons/pubproperty.gif)|
[DocumentCount](P_Grasshopper_Kernel_GH_DocumentServer_DocumentCount.htm)|
Gets the number of documents stored in the global list.  
![Public property](../icons/pubproperty.gif)|
[DocumentNames](P_Grasshopper_Kernel_GH_DocumentServer_DocumentNames.htm)|
Gets a string collection containing all the names of the documents in the
global list.  
![Public property](../icons/pubproperty.gif)|
[ModifiedDocumentCount](P_Grasshopper_Kernel_GH_DocumentServer_ModifiedDocumentCount.htm)|
Gets the total number of modified (unsaved) documents.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AddDocument(GH_Document)](M_Grasshopper_Kernel_GH_DocumentServer_AddDocument.htm)|
Add a new document to the global list. If the document is already registered
nothing will happen. This also applies to a different document which points to
the same file path  
![Public method](../icons/pubmethod.gif)| [AddDocument(GH_Document,
Boolean)](M_Grasshopper_Kernel_GH_DocumentServer_AddDocument_1.htm)|  Add a
new document to the global list. If the document is already registered nothing
will happen. This also applies to a different document which points to the
same file path  
![Public method](../icons/pubmethod.gif)| [AddDocument(String,
Boolean)](M_Grasshopper_Kernel_GH_DocumentServer_AddDocument_2.htm)|  Add a
new document to the global list. If there already is a document with the given
path, it will be made active.  
![Public method](../icons/pubmethod.gif)|
[AddNewDocument](M_Grasshopper_Kernel_GH_DocumentServer_AddNewDocument.htm)|
Adds a new document to the global list. If a template file has been set, this
document will be based on the template.  
![Public method](../icons/pubmethod.gif)|
[Contains](M_Grasshopper_Kernel_GH_DocumentServer_Contains.htm)|  Gets a value
indicating whether or not the given document is inside the list.  
![Public method](../icons/pubmethod.gif)|
[GetEnumerator](M_Grasshopper_Kernel_GH_DocumentServer_GetEnumerator.htm)|  
![Public method](../icons/pubmethod.gif)|
[GetEnumerator_Generic](M_Grasshopper_Kernel_GH_DocumentServer_GetEnumerator_Generic.htm)|  
![Public method](../icons/pubmethod.gif)|
[IndexOf(GH_Document)](M_Grasshopper_Kernel_GH_DocumentServer_IndexOf.htm)|
Gets the index of the given document.  
![Public method](../icons/pubmethod.gif)|
[IndexOf(String)](M_Grasshopper_Kernel_GH_DocumentServer_IndexOf_1.htm)|  Gets
the index of the document that matches the filepath.  
![Public method](../icons/pubmethod.gif)|
[IndexOfAutoSave](M_Grasshopper_Kernel_GH_DocumentServer_IndexOfAutoSave.htm)|
Gets the document index that is associated with the specified autosave
location.  
![Public method](../icons/pubmethod.gif)|
[NextAvailableDocument](M_Grasshopper_Kernel_GH_DocumentServer_NextAvailableDocument.htm)|
Gets the most important, non-active document.  
![Public method](../icons/pubmethod.gif)|
[PromoteDocument](M_Grasshopper_Kernel_GH_DocumentServer_PromoteDocument.htm)|
Push a document to the top of the list, meaning it will be first in line when
a new default document needs to be selected.  
![Public method](../icons/pubmethod.gif)|
[RemoveAllDocuments](M_Grasshopper_Kernel_GH_DocumentServer_RemoveAllDocuments.htm)|
Remove all documents in the global list.  
![Public method](../icons/pubmethod.gif)|
[RemoveDocument](M_Grasshopper_Kernel_GH_DocumentServer_RemoveDocument.htm)|
Removes a specific document from the global list. If the document isn't
registered nothing will happen. If the document is owned by an
IGH_DocumentOwner, the owner will be informed of the removal.  
![Public method](../icons/pubmethod.gif)|
[SafeRemoveDocument](M_Grasshopper_Kernel_GH_DocumentServer_SafeRemoveDocument.htm)|
Remove a document correctly from the server. This method shows user-interface
prompts if there is unsaved data and will also save if needed.  
Top

![](../icons/SectionExpanded.png)Events

| Name| Description  
---|---|---  
![Public event](../icons/pubevent.gif)|
[DocumentAdded](E_Grasshopper_Kernel_GH_DocumentServer_DocumentAdded.htm)|  
![Public event](../icons/pubevent.gif)|
[DocumentRemoved](E_Grasshopper_Kernel_GH_DocumentServer_DocumentRemoved.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

