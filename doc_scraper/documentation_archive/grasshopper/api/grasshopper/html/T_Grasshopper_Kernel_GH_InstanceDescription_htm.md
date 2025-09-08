---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_InstanceDescription.htm
scraped_at: 2025-09-08T16:16:59.444870
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_InstanceDescription
Class](../html/T_Grasshopper_Kernel_GH_InstanceDescription.htm
"GH_InstanceDescription Class")

[GH_InstanceDescription
Properties](../html/Properties_T_Grasshopper_Kernel_GH_InstanceDescription.htm
"GH_InstanceDescription Properties")

[GH_InstanceDescription
Methods](../html/Methods_T_Grasshopper_Kernel_GH_InstanceDescription.htm
"GH_InstanceDescription Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_InstanceDescription Class  
  
---  
  
Base implementation of IGH_InstanceDescription. Consider deriving from this
class rather than implementing IGH_InstanceDescription from scratch.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_InstanceDescription  
[Grasshopper.KernelGH_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm)  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_InstanceDescription : IGH_InstanceDescription
    
    
    Public Class GH_InstanceDescription
    	Implements IGH_InstanceDescription

The GH_InstanceDescription type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Category](P_Grasshopper_Kernel_GH_InstanceDescription_Category.htm)|  Gets or
sets the Category in which this object belongs. If HasCategory() returns
false, this field has no meaning.  
![Public property](../icons/pubproperty.gif)|
[Description](P_Grasshopper_Kernel_GH_InstanceDescription_Description.htm)|
Gets or sets the description of the object. This field typically remains fixed
during the lifetime of an object.  
![Public property](../icons/pubproperty.gif)|
[HasCategory](P_Grasshopper_Kernel_GH_InstanceDescription_HasCategory.htm)|
Gets whether or not the Category field has been set.  
![Public property](../icons/pubproperty.gif)|
[HasSubCategory](P_Grasshopper_Kernel_GH_InstanceDescription_HasSubCategory.htm)|
Gets whether or not the SubCategory field has been set.  
![Public property](../icons/pubproperty.gif)|
[InstanceDescription](P_Grasshopper_Kernel_GH_InstanceDescription_InstanceDescription.htm)|
Gets a description of the current state of the object. This field is usually
the same as the Description() field, but it might be variable when overridden.  
![Public property](../icons/pubproperty.gif)|
[InstanceGuid](P_Grasshopper_Kernel_GH_InstanceDescription_InstanceGuid.htm)|
Gets the ID of this runtime instance.  
![Public property](../icons/pubproperty.gif)|
[Keywords](P_Grasshopper_Kernel_GH_InstanceDescription_Keywords.htm)|  Gets a
list of additional keywords that describe the object. Typically this list is
empty but you can override this property to aid in object searches.  
![Public property](../icons/pubproperty.gif)|
[Name](P_Grasshopper_Kernel_GH_InstanceDescription_Name.htm)|  Gets or sets
the name of the object. This field typically remains fixed during the lifetime
of an object.  
![Public property](../icons/pubproperty.gif)|
[NickName](P_Grasshopper_Kernel_GH_InstanceDescription_NickName.htm)|  Gets or
sets the nickname of the object. This field can be changed by the user.  
![Public property](../icons/pubproperty.gif)|
[SubCategory](P_Grasshopper_Kernel_GH_InstanceDescription_SubCategory.htm)|
Gets or sets the SubCategory in which this object belongs. If HasSubCategory()
returns false, this field has no meaning.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CopyFrom](M_Grasshopper_Kernel_GH_InstanceDescription_CopyFrom.htm)|  Copy
all fields (except the instance ID) from another instance description.  
![Public method](../icons/pubmethod.gif)|
[NewInstanceGuid](M_Grasshopper_Kernel_GH_InstanceDescription_NewInstanceGuid.htm)|
Generate a new random instance GUID  
![Public method](../icons/pubmethod.gif)|
[NewInstanceGuid(Guid)](M_Grasshopper_Kernel_GH_InstanceDescription_NewInstanceGuid_1.htm)|
Set the instance ID to be a specific GUID. This is very dangerous, only use
this function if you're 6"4' and your first name is David.  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_GH_InstanceDescription_Read.htm)|  Default
deserialization. Only retrieves Name, NickName, Description and InstanceGuid
fields. If you want to retrieve additional fields use ReadFull() instead.
However, ReadFull() will only work if the archive was written using
WriteFull().  
![Public method](../icons/pubmethod.gif)|
[ReadFull](M_Grasshopper_Kernel_GH_InstanceDescription_ReadFull.htm)|
GH_InstanceDescription does not by default serialize all fields. Use this
function to read _all_ fields from the archive. This method is compatible with
the default Write()/Read() operations.  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_GH_InstanceDescription_Write.htm)|  Default
serialization. Only stores Name, NickName, Description and InstanceGuid
fields. If you want to store additional fields use WriteFull() instead.  
![Public method](../icons/pubmethod.gif)|
[WriteFull](M_Grasshopper_Kernel_GH_InstanceDescription_WriteFull.htm)|
GH_InstanceDescription does not by default serialize all fields. Use this
function to write _all_ fields to the archive. This method is compatible with
the default Write()/Read() operations.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

