---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_ExternalFile.htm
scraped_at: 2025-09-08T16:16:40.323810
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_ExternalFile Class](../html/T_Grasshopper_Kernel_GH_ExternalFile.htm
"GH_ExternalFile Class")

[GH_ExternalFile Constructor
](../html/M_Grasshopper_Kernel_GH_ExternalFile__ctor.htm "GH_ExternalFile
Constructor ")

[GH_ExternalFile
Properties](../html/Properties_T_Grasshopper_Kernel_GH_ExternalFile.htm
"GH_ExternalFile Properties")

[GH_ExternalFile
Methods](../html/Methods_T_Grasshopper_Kernel_GH_ExternalFile.htm
"GH_ExternalFile Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_ExternalFile Class  
  
---  
  
Represents information about external files to be loaded.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_ExternalFile  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_ExternalFile
    
    
    Public Class GH_ExternalFile

The GH_ExternalFile type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_ExternalFile](M_Grasshopper_Kernel_GH_ExternalFile__ctor.htm)|  Create a
new instance of the file info class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[FileHash](P_Grasshopper_Kernel_GH_ExternalFile_FileHash.htm)|  Gets the file
hash.  
![Public property](../icons/pubproperty.gif)|
[FileName](P_Grasshopper_Kernel_GH_ExternalFile_FileName.htm)|  Gets the file
name (without the extension).  
![Public property](../icons/pubproperty.gif)|
[FilePath](P_Grasshopper_Kernel_GH_ExternalFile_FilePath.htm)|  Gets the file
path.  
![Public property](../icons/pubproperty.gif)|
[FileSize](P_Grasshopper_Kernel_GH_ExternalFile_FileSize.htm)|  Gets the file
size (in bytes).  
![Public property](../icons/pubproperty.gif)|
[FileType](P_Grasshopper_Kernel_GH_ExternalFile_FileType.htm)|  Gets the file
type as indicated by the extension.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[IsIdenticalTo](M_Grasshopper_Kernel_GH_ExternalFile_IsIdenticalTo.htm)|
Compares two files for content. If the size and the hash or the other file are
equal to this one, the files are considered identical.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

