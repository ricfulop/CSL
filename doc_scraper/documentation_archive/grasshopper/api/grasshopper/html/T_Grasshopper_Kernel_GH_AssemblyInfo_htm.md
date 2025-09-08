---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_AssemblyInfo.htm
scraped_at: 2025-09-08T16:15:21.061267
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_AssemblyInfo Class](../html/T_Grasshopper_Kernel_GH_AssemblyInfo.htm
"GH_AssemblyInfo Class")

[GH_AssemblyInfo Constructor
](../html/M_Grasshopper_Kernel_GH_AssemblyInfo__ctor.htm "GH_AssemblyInfo
Constructor ")

[GH_AssemblyInfo
Properties](../html/Properties_T_Grasshopper_Kernel_GH_AssemblyInfo.htm
"GH_AssemblyInfo Properties")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_AssemblyInfo Class  
  
---  
  
Implement this interface once (and once only) in a GHA project if you wish to
add additional information about your library to Grasshopper. Note you must
supply an empty constructor.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_AssemblyInfo  
[Grasshopper.KernelGH_AssemblyInfoStub](T_Grasshopper_Kernel_GH_AssemblyInfoStub.htm)  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public abstract class GH_AssemblyInfo
    
    
    Public MustInherit Class GH_AssemblyInfo

The GH_AssemblyInfo type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[GH_AssemblyInfo](M_Grasshopper_Kernel_GH_AssemblyInfo__ctor.htm)| Initializes
a new instance of the GH_AssemblyInfo class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Assembly](P_Grasshopper_Kernel_GH_AssemblyInfo_Assembly.htm)|  Gets the
actual assembly that this info object describes.  
![Public property](../icons/pubproperty.gif)|
[AuthorContact](P_Grasshopper_Kernel_GH_AssemblyInfo_AuthorContact.htm)|  Gets
the contact information for the author. This can be email, phone, fax, address
or all of the above. Return null if you do not wish to associate contact
details with this assembly.  
![Public property](../icons/pubproperty.gif)|
[AuthorName](P_Grasshopper_Kernel_GH_AssemblyInfo_AuthorName.htm)|  Gets the
name of the individual/company/organisation that is responsible for this
assembly. Return null if you do not wish to associate an author with this
assembly.  
![Public property](../icons/pubproperty.gif)|
[Description](P_Grasshopper_Kernel_GH_AssemblyInfo_Description.htm)|  Gets the
human readable description of this assembly. Return null if you do not wish to
associate a description with this assembly.  
![Public property](../icons/pubproperty.gif)|
[Icon](P_Grasshopper_Kernel_GH_AssemblyInfo_Icon.htm)|  Gets a 24x24 icon that
represents this assembly. Return null if you do not wish to associate an icon
with this assembly.  
![Public property](../icons/pubproperty.gif)|
[Id](P_Grasshopper_Kernel_GH_AssemblyInfo_Id.htm)|  Gets the Id of this
assembly. By default the Id is a hash of the name.  
![Public property](../icons/pubproperty.gif)|
[IsCoreLibrary](P_Grasshopper_Kernel_GH_AssemblyInfo_IsCoreLibrary.htm)|  Gets
whether this library is a Grasshopper core library. Core libraries are
installed along with Grasshopper and thus should always be available anywhere.  
![Public property](../icons/pubproperty.gif)|
[License](P_Grasshopper_Kernel_GH_AssemblyInfo_License.htm)|  Gets the license
type for this assembly.  
![Public property](../icons/pubproperty.gif)|
[LoadingMechanism](P_Grasshopper_Kernel_GH_AssemblyInfo_LoadingMechanism.htm)|
Gets the mechanism used to load this assembly.  
![Public property](../icons/pubproperty.gif)|
[Location](P_Grasshopper_Kernel_GH_AssemblyInfo_Location.htm)|  Gets the
location this assembly was loaded from.  
![Public property](../icons/pubproperty.gif)|
[Name](P_Grasshopper_Kernel_GH_AssemblyInfo_Name.htm)|  Gets the human
readable name of this assembly. Return null if you do not wish to associate a
name with this assembly.  
![Public property](../icons/pubproperty.gif)|
[Version](P_Grasshopper_Kernel_GH_AssemblyInfo_Version.htm)|  Gets the version
code for this assembly.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

