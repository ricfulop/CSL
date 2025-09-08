---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_UpgradeUtil.htm
scraped_at: 2025-09-08T16:18:08.731913
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_UpgradeUtil Class](../html/T_Grasshopper_Kernel_GH_UpgradeUtil.htm
"GH_UpgradeUtil Class")

[GH_UpgradeUtil Constructor
](../html/M_Grasshopper_Kernel_GH_UpgradeUtil__ctor.htm "GH_UpgradeUtil
Constructor ")

[GH_UpgradeUtil
Methods](../html/Methods_T_Grasshopper_Kernel_GH_UpgradeUtil.htm
"GH_UpgradeUtil Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_UpgradeUtil Class  
  
---  
  
Exposes several utility functions for migrating parameters and wires between
components useful while upgrading components.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_UpgradeUtil  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_UpgradeUtil
    
    
    Public Class GH_UpgradeUtil

The GH_UpgradeUtil type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_UpgradeUtil](M_Grasshopper_Kernel_GH_UpgradeUtil__ctor.htm)| Initializes a
new instance of the GH_UpgradeUtil class  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[MigrateInputParameters(IGH_Component,
IGH_Component)](M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateInputParameters.htm)|
Migrate all input parameters.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[MigrateInputParameters(IGH_Component, IGH_Component, Int32,
Int32)](M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateInputParameters_1.htm)|
Migrate a bunch of input parameters.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[MigrateOutputParameters(IGH_Component,
IGH_Component)](M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateOutputParameters.htm)|
Migrate all output parameters.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[MigrateOutputParameters(IGH_Component, IGH_Component, Int32,
Int32)](M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateOutputParameters_1.htm)|
Migrate a bunch of output parameters.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[MigrateRecipients(IEnumerableIGH_Param,
IGH_Param)](M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateRecipients_1.htm)|
Utility method for bulk assigning a bunch of sources.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[MigrateRecipients(IGH_Param,
IGH_Param)](M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateRecipients.htm)|
Migrate all recipients from A to B, while maintaining order.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[MigrateSources(IEnumerableIGH_Param,
IGH_Param)](M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateSources_1.htm)|
Utility method for bulk assigning a bunch of sources.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[MigrateSources(IGH_Param,
IGH_Param)](M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateSources.htm)|  Migrate
all sources from A to B, while maintaining order.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ReplaceInputParameters](M_Grasshopper_Kernel_GH_UpgradeUtil_ReplaceInputParameters.htm)|
Move all input parameters from one component to another. Only use this
function if the target component can handle the input layout of the source
component.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ReplaceOutputParameters](M_Grasshopper_Kernel_GH_UpgradeUtil_ReplaceOutputParameters.htm)|
Move all output parameters from one component to another. Only use this
function if the target component can handle the output layout of the source
component.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[SwapComponents(IGH_Component,
IGH_Component)](M_Grasshopper_Kernel_GH_UpgradeUtil_SwapComponents.htm)|
Replace an existing component with a different one. All parameters (input and
output) will be migrated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[SwapComponents(IGH_Component,
Guid)](M_Grasshopper_Kernel_GH_UpgradeUtil_SwapComponents_2.htm)|  Replace an
existing component with a different one. All parameters (input and output)
will be migrated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[SwapComponents(IGH_Component, IGH_Component,
Boolean)](M_Grasshopper_Kernel_GH_UpgradeUtil_SwapComponents_1.htm)|  Replace
an existing component with a different one. All parameters (input and output)
will be migrated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[SwapComponents(IGH_Component, Guid,
Boolean)](M_Grasshopper_Kernel_GH_UpgradeUtil_SwapComponents_3.htm)|  Replace
an existing component with a different one. All parameters (input and output)
will be migrated.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

