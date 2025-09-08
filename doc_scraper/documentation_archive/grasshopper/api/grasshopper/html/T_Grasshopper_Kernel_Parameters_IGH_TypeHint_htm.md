---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Parameters_IGH_TypeHint.htm
scraped_at: 2025-09-08T16:19:58.216985
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Parameters](../html/N_Grasshopper_Kernel_Parameters.htm
"Grasshopper.Kernel.Parameters")

[IGH_TypeHint
Interface](../html/T_Grasshopper_Kernel_Parameters_IGH_TypeHint.htm
"IGH_TypeHint Interface")

[IGH_TypeHint
Properties](../html/Properties_T_Grasshopper_Kernel_Parameters_IGH_TypeHint.htm
"IGH_TypeHint Properties")

[IGH_TypeHint
Methods](../html/Methods_T_Grasshopper_Kernel_Parameters_IGH_TypeHint.htm
"IGH_TypeHint Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_TypeHint Interface  
  
---  
  
Represents conversion logic for a certain data type.

**Namespace:**
[Grasshopper.Kernel.Parameters](N_Grasshopper_Kernel_Parameters.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_TypeHint
    
    
    Public Interface IGH_TypeHint

The IGH_TypeHint type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[HintID](P_Grasshopper_Kernel_Parameters_IGH_TypeHint_HintID.htm)|  Unique ID
for every type of Hint.  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_Parameters_IGH_TypeHint_TypeName.htm)|  Name
of target Type  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Cast](M_Grasshopper_Kernel_Parameters_IGH_TypeHint_Cast.htm)|  Apply
conversion logic to a specific object. This function should not throw
exceptions.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Parameters Namespace](N_Grasshopper_Kernel_Parameters.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

