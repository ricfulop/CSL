---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_IGH_UpgradeObject.htm
scraped_at: 2025-09-08T16:18:45.893875
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH_UpgradeObject
Interface](../html/T_Grasshopper_Kernel_IGH_UpgradeObject.htm
"IGH_UpgradeObject Interface")

[IGH_UpgradeObject
Properties](../html/Properties_T_Grasshopper_Kernel_IGH_UpgradeObject.htm
"IGH_UpgradeObject Properties")

[IGH_UpgradeObject
Methods](../html/Methods_T_Grasshopper_Kernel_IGH_UpgradeObject.htm
"IGH_UpgradeObject Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_UpgradeObject Interface  
  
---  
  
Create a class with an empty constructor that implements this interface if you
want to provide an upgrade mechanism.

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_UpgradeObject
    
    
    Public Interface IGH_UpgradeObject

The IGH_UpgradeObject type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[UpgradeFrom](P_Grasshopper_Kernel_IGH_UpgradeObject_UpgradeFrom.htm)|  Gets
the ComponentGuid of the old object (the object to be updated).  
![Public property](../icons/pubproperty.gif)|
[UpgradeTo](P_Grasshopper_Kernel_IGH_UpgradeObject_UpgradeTo.htm)|  Gets the
ComponentGuid of the new object (the object that will be inserted).  
![Public property](../icons/pubproperty.gif)|
[Version](P_Grasshopper_Kernel_IGH_UpgradeObject_Version.htm)|  Return a
DateTime object that indicates when this upgrade mechanism was written, so
that it becomes possible to distinguish competing upgrade mechanisms.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Upgrade](M_Grasshopper_Kernel_IGH_UpgradeObject_Upgrade.htm)|  Upgrade an
existing object.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

