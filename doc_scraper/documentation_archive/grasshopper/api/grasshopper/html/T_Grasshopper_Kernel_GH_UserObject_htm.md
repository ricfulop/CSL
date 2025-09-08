---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_UserObject.htm
scraped_at: 2025-09-08T16:18:09.740501
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_UserObject Class](../html/T_Grasshopper_Kernel_GH_UserObject.htm
"GH_UserObject Class")

[GH_UserObject Constructor
](../html/Overload_Grasshopper_Kernel_GH_UserObject__ctor.htm "GH_UserObject
Constructor ")

[GH_UserObject
Properties](../html/Properties_T_Grasshopper_Kernel_GH_UserObject.htm
"GH_UserObject Properties")

[GH_UserObject Methods](../html/Methods_T_Grasshopper_Kernel_GH_UserObject.htm
"GH_UserObject Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_UserObject Class  
  
---  
  
Represents a custom user object. A User Object is an existing
IGH_DocumentObject with overridden icon, instance description and exposure.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_UserObject  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_UserObject
    
    
    Public Class GH_UserObject

The GH_UserObject type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_UserObject](M_Grasshopper_Kernel_GH_UserObject__ctor.htm)|  Empty
constructor  
![Public method](../icons/pubmethod.gif)|
[GH_UserObject(String)](M_Grasshopper_Kernel_GH_UserObject__ctor_1.htm)|
Create a new user object from an existing *.ghuser file.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[BaseGuid](P_Grasshopper_Kernel_GH_UserObject_BaseGuid.htm)|  Gets or sets the
ComponentID of the IGH_DocumentObject that functions as the base class for
this User Object.  
![Public property](../icons/pubproperty.gif)|
[Data](P_Grasshopper_Kernel_GH_UserObject_Data.htm)|  Gets or sets the
serialized data. This data is used to deserialize a new instance of the base
class.  
![Public property](../icons/pubproperty.gif)|
[Description](P_Grasshopper_Kernel_GH_UserObject_Description.htm)|  Gets or
sets the Instance Description override for this User Object.  
![Public property](../icons/pubproperty.gif)|
[Exposure](P_Grasshopper_Kernel_GH_UserObject_Exposure.htm)|  Gets or sets the
Exposure of this User Object.  
![Public property](../icons/pubproperty.gif)|
[Guid](P_Grasshopper_Kernel_GH_UserObject_Guid.htm)|  Gets or sets the Guid of
this User Object. The Guid is created anew during construction and is not
stored in the User Object File. You should never have to set this field.  
![Public property](../icons/pubproperty.gif)|
[Icon](P_Grasshopper_Kernel_GH_UserObject_Icon.htm)|  Gets or sets the icon
associated with this User Object. If the icon hasn't been overridden, then a
Default icon is returned.  
![Public property](../icons/pubproperty.gif)|
[Path](P_Grasshopper_Kernel_GH_UserObject_Path.htm)|  Gets or sets the file
path this User Object is loaded from or saved to.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Clear](M_Grasshopper_Kernel_GH_UserObject_Clear.htm)|  Destroy all data
except the file path and the ID.  
![Public method](../icons/pubmethod.gif)|
[CreateDefaultPath](M_Grasshopper_Kernel_GH_UserObject_CreateDefaultPath.htm)|
Set the Path field for this user object to the default. The default file name
is derived from the Description.Name field. This method also ensures the
UserObject directory exists.  
![Public method](../icons/pubmethod.gif)|
[InstantiateObject](M_Grasshopper_Kernel_GH_UserObject_InstantiateObject.htm)|
Instantiate a new IGH_DocumentObject from this User Object.  
![Public method](../icons/pubmethod.gif)|
[ReadFromFile](M_Grasshopper_Kernel_GH_UserObject_ReadFromFile.htm)|  Force an
update of the local data from the file. The Path field must be set for this to
work.  
![Public method](../icons/pubmethod.gif)|
[SaveToFile](M_Grasshopper_Kernel_GH_UserObject_SaveToFile.htm)|  Save the
current User Object state to a file. Any existing file will be overwritten.  
![Public method](../icons/pubmethod.gif)|
[SetDataFromObject](M_Grasshopper_Kernel_GH_UserObject_SetDataFromObject.htm)|
Set the Data field content of ths UserObject from a Document object instance.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

