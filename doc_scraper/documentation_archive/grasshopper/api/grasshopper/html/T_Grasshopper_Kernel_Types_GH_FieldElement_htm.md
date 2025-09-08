---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_GH_FieldElement.htm
scraped_at: 2025-09-08T16:20:38.365727
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[GH_FieldElement Class](../html/T_Grasshopper_Kernel_Types_GH_FieldElement.htm
"GH_FieldElement Class")

[GH_FieldElement Constructor
](../html/M_Grasshopper_Kernel_Types_GH_FieldElement__ctor.htm
"GH_FieldElement Constructor ")

[GH_FieldElement
Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_FieldElement.htm
"GH_FieldElement Properties")

[GH_FieldElement
Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_FieldElement.htm
"GH_FieldElement Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_FieldElement Class  
  
---  
  
Abstract implementation of IGH_FieldElement, derive from this class rather
than implementing IGH_FieldElement to save yourself time and effort.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Kernel.TypesGH_FieldElement  
[Grasshopper.Kernel.TypesGH_LineCharge](T_Grasshopper_Kernel_Types_GH_LineCharge.htm)  
[Grasshopper.Kernel.TypesGH_PointCharge](T_Grasshopper_Kernel_Types_GH_PointCharge.htm)  
[Grasshopper.Kernel.TypesGH_SpinForce](T_Grasshopper_Kernel_Types_GH_SpinForce.htm)  
[Grasshopper.Kernel.TypesGH_VectorForce](T_Grasshopper_Kernel_Types_GH_VectorForce.htm)  

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public abstract class GH_FieldElement : IGH_FieldElement
    
    
    Public MustInherit Class GH_FieldElement
    	Implements IGH_FieldElement

The GH_FieldElement type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[GH_FieldElement](M_Grasshopper_Kernel_Types_GH_FieldElement__ctor.htm)|
Initializes a new instance of the GH_FieldElement class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[BoundingBox](P_Grasshopper_Kernel_Types_GH_FieldElement_BoundingBox.htm)|  
![Public property](../icons/pubproperty.gif)|
[ClippingBox](P_Grasshopper_Kernel_Types_GH_FieldElement_ClippingBox.htm)|  
![Public property](../icons/pubproperty.gif)|
[ElementGuid](P_Grasshopper_Kernel_Types_GH_FieldElement_ElementGuid.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsLimited](P_Grasshopper_Kernel_Types_GH_FieldElement_IsLimited.htm)|  
![Public property](../icons/pubproperty.gif)|
[Limits](P_Grasshopper_Kernel_Types_GH_FieldElement_Limits.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[DrawViewportMeshes](M_Grasshopper_Kernel_Types_GH_FieldElement_DrawViewportMeshes.htm)|  
![Public method](../icons/pubmethod.gif)|
[DrawViewportWires](M_Grasshopper_Kernel_Types_GH_FieldElement_DrawViewportWires.htm)|  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Kernel_Types_GH_FieldElement_Duplicate.htm)|  
![Public method](../icons/pubmethod.gif)|
[Force](M_Grasshopper_Kernel_Types_GH_FieldElement_Force.htm)|  
![Public method](../icons/pubmethod.gif)|
[IsCoincident](M_Grasshopper_Kernel_Types_GH_FieldElement_IsCoincident.htm)|  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_Types_GH_FieldElement_Read.htm)|  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_Types_GH_FieldElement_Write.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

