---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_DocumentIO.htm
scraped_at: 2025-09-08T16:16:28.295772
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_DocumentIO Class](../html/T_Grasshopper_Kernel_GH_DocumentIO.htm
"GH_DocumentIO Class")

[GH_DocumentIO Constructor
](../html/Overload_Grasshopper_Kernel_GH_DocumentIO__ctor.htm "GH_DocumentIO
Constructor ")

[GH_DocumentIO
Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocumentIO.htm
"GH_DocumentIO Properties")

[GH_DocumentIO Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentIO.htm
"GH_DocumentIO Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_DocumentIO Class  
  
---  
  
Provides basic IO operations for GH_Documents.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_DocumentIO  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class GH_DocumentIO
    
    
    Public NotInheritable Class GH_DocumentIO

The GH_DocumentIO type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_DocumentIO](M_Grasshopper_Kernel_GH_DocumentIO__ctor.htm)|  Create a new
instance of GH_DocumentIO without an internal document.  
![Public method](../icons/pubmethod.gif)|
[GH_DocumentIO(GH_Document)](M_Grasshopper_Kernel_GH_DocumentIO__ctor_1.htm)|
Create a new instance of GH_DocumentIO with an internal document.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[DisableOverwriteProtection](P_Grasshopper_Kernel_GH_DocumentIO_DisableOverwriteProtection.htm)|
Gets or sets whether the file overwrite protection dialog ought to be shown
during risky saves.  
![Public property](../icons/pubproperty.gif)|
[Document](P_Grasshopper_Kernel_GH_DocumentIO_Document.htm)|  Gets or sets the
internal document.  
![Public property](../icons/pubproperty.gif)|
[IsDocument](P_Grasshopper_Kernel_GH_DocumentIO_IsDocument.htm)|  Gets a value
indicating whether or not this instance of GH_DocumentIO contains an internal
document.  
![Public property](../icons/pubproperty.gif)|
[LocalClipboardContent](P_Grasshopper_Kernel_GH_DocumentIO_LocalClipboardContent.htm)|
Gets the contents of the local clipboard.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ClearClipboard](M_Grasshopper_Kernel_GH_DocumentIO_ClearClipboard.htm)|
Clear the Clipboard Text content. This function wipes both the Text and
UnicodeText clipboard fields.  
![Public method](../icons/pubmethod.gif)|
[Copy(GH_ClipboardType)](M_Grasshopper_Kernel_GH_DocumentIO_Copy.htm)|  Copy
the internal document into the clipboard.  
![Public method](../icons/pubmethod.gif)| [Copy(GH_ClipboardType,
Boolean)](M_Grasshopper_Kernel_GH_DocumentIO_Copy_1.htm)|  Copy the internal
document into the clipboard.  
![Public method](../icons/pubmethod.gif)| [Copy(GH_ClipboardType,
IEnumerableGuid)](M_Grasshopper_Kernel_GH_DocumentIO_Copy_2.htm)|  Copy the
specified objects in the internal document into the clipboard.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[GetDocumentIcon](M_Grasshopper_Kernel_GH_DocumentIO_GetDocumentIcon.htm)|
Try and extract the icon image of a document. Not all gh/ghx files contain an
icon so this function may return null. The document itself is not loaded and
rendered, so the icon really has to be part of the file already.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[GetDocumentThumbnail](M_Grasshopper_Kernel_GH_DocumentIO_GetDocumentThumbnail.htm)|
Try and extract the preview image of a document. Not all gh/ghx files contain
a thumbnail so this function may return null. The document itself is not
loaded and rendered, so the thumbnail really has to be part of the file
already.  
![Public method](../icons/pubmethod.gif)|
[Open](M_Grasshopper_Kernel_GH_DocumentIO_Open.htm)|  Perform a default Open
operation and store the result as the internal document.  
![Public method](../icons/pubmethod.gif)|
[Open(String)](M_Grasshopper_Kernel_GH_DocumentIO_Open_1.htm)|  Open the file
at the given location.  
![Public method](../icons/pubmethod.gif)|
[OpenDocumentDialog](M_Grasshopper_Kernel_GH_DocumentIO_OpenDocumentDialog.htm)|
Display the Open GH/GHX dialog.  
![Public method](../icons/pubmethod.gif)|
[Paste](M_Grasshopper_Kernel_GH_DocumentIO_Paste.htm)|  Deserialize a
Grasshopper document from the clipboard. On success, the internal document of
this GH_DocumentIO instance will be set.  
![Public method](../icons/pubmethod.gif)|
[Save](M_Grasshopper_Kernel_GH_DocumentIO_Save.htm)|  Perform a default Save
operation on the internal document.  
![Public method](../icons/pubmethod.gif)|
[SaveAs](M_Grasshopper_Kernel_GH_DocumentIO_SaveAs.htm)|  Perform a default
Save As operation on the internal document.  
![Public method](../icons/pubmethod.gif)|
[SaveAsCopyDocumentDialog](M_Grasshopper_Kernel_GH_DocumentIO_SaveAsCopyDocumentDialog.htm)|
Display the Save As Copy GH/GHX dialog.  
![Public method](../icons/pubmethod.gif)|
[SaveAsDocumentDialog](M_Grasshopper_Kernel_GH_DocumentIO_SaveAsDocumentDialog.htm)|
Display the Save As GH/GHX dialog.  
![Public method](../icons/pubmethod.gif)|
[SaveBackup](M_Grasshopper_Kernel_GH_DocumentIO_SaveBackup.htm)|  Save a time-
stamped copy of the current file.  
![Public method](../icons/pubmethod.gif)|
[SaveDocumentDialog](M_Grasshopper_Kernel_GH_DocumentIO_SaveDocumentDialog.htm)|
Display the Save GH/GHX dialog.  
![Public method](../icons/pubmethod.gif)|
[SaveQuiet](M_Grasshopper_Kernel_GH_DocumentIO_SaveQuiet.htm)|  Quietly save a
file to a given location.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ShowOverwriteDialog(String)](M_Grasshopper_Kernel_GH_DocumentIO_ShowOverwriteDialog.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ShowOverwriteDialog(String, DateTime,
DateTime)](M_Grasshopper_Kernel_GH_DocumentIO_ShowOverwriteDialog_1.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[SubsidiaryDocumentSavePrompt(GH_Document)](M_Grasshopper_Kernel_GH_DocumentIO_SubsidiaryDocumentSavePrompt.htm)|
Display a 'stuff has changed do you want to save' message box with
Yes/No/Cancel options.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[SubsidiaryDocumentSavePrompt(String, Boolean,
Int32)](M_Grasshopper_Kernel_GH_DocumentIO_SubsidiaryDocumentSavePrompt_1.htm)|
Display a 'stuff has changed do you want to save' message box with
Yes/No/Cancel options.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

