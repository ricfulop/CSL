---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_GH_SpinForce.htm
scraped_at: 2025-09-08T16:21:28.607802
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[GH_SpinForce Class](../html/T_Grasshopper_Kernel_Types_GH_SpinForce.htm
"GH_SpinForce Class")

[GH_SpinForce Constructor
](../html/M_Grasshopper_Kernel_Types_GH_SpinForce__ctor.htm "GH_SpinForce
Constructor ")

[GH_SpinForce
Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_SpinForce.htm
"GH_SpinForce Properties")

[GH_SpinForce
Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_SpinForce.htm
"GH_SpinForce Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_SpinForce Class  
  
---  
  
Rotational spin force for IGH_Fields.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.Kernel.TypesGH_FieldElement](T_Grasshopper_Kernel_Types_GH_FieldElement.htm)  
Grasshopper.Kernel.TypesGH_SpinForce  

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_SpinForce : GH_FieldElement
    
    
    Public Class GH_SpinForce
    	Inherits GH_FieldElement

The GH_SpinForce type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_SpinForce](M_Grasshopper_Kernel_Types_GH_SpinForce__ctor.htm)| Initializes
a new instance of the GH_SpinForce class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[BoundingBox](P_Grasshopper_Kernel_Types_GH_SpinForce_BoundingBox.htm)|
(Overrides
[GH_FieldElementBoundingBox](P_Grasshopper_Kernel_Types_GH_FieldElement_BoundingBox.htm).)  
![Public property](../icons/pubproperty.gif)|
[ClippingBox](P_Grasshopper_Kernel_Types_GH_FieldElement_ClippingBox.htm)|
(Inherited from
[GH_FieldElement](T_Grasshopper_Kernel_Types_GH_FieldElement.htm).)  
![Public property](../icons/pubproperty.gif)|
[Decay](P_Grasshopper_Kernel_Types_GH_SpinForce_Decay.htm)|  
![Public property](../icons/pubproperty.gif)|
[ElementGuid](P_Grasshopper_Kernel_Types_GH_SpinForce_ElementGuid.htm)|
(Overrides
[GH_FieldElementElementGuid](P_Grasshopper_Kernel_Types_GH_FieldElement_ElementGuid.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsLimited](P_Grasshopper_Kernel_Types_GH_FieldElement_IsLimited.htm)|
(Inherited from
[GH_FieldElement](T_Grasshopper_Kernel_Types_GH_FieldElement.htm).)  
![Public property](../icons/pubproperty.gif)|
[Limits](P_Grasshopper_Kernel_Types_GH_FieldElement_Limits.htm)|  (Inherited
from [GH_FieldElement](T_Grasshopper_Kernel_Types_GH_FieldElement.htm).)  
![Public property](../icons/pubproperty.gif)|
[Plane](P_Grasshopper_Kernel_Types_GH_SpinForce_Plane.htm)|  
![Public property](../icons/pubproperty.gif)|
[Radius](P_Grasshopper_Kernel_Types_GH_SpinForce_Radius.htm)|  
![Public property](../icons/pubproperty.gif)|
[Strength](P_Grasshopper_Kernel_Types_GH_SpinForce_Strength.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[DrawViewportMeshes](M_Grasshopper_Kernel_Types_GH_FieldElement_DrawViewportMeshes.htm)|
(Inherited from
[GH_FieldElement](T_Grasshopper_Kernel_Types_GH_FieldElement.htm).)  
![Public method](../icons/pubmethod.gif)|
[DrawViewportWires](M_Grasshopper_Kernel_Types_GH_SpinForce_DrawViewportWires.htm)|
(Overrides
[GH_FieldElementDrawViewportWires(GH_PreviewWireArgs)](M_Grasshopper_Kernel_Types_GH_FieldElement_DrawViewportWires.htm).)  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Kernel_Types_GH_SpinForce_Duplicate.htm)|
(Overrides
[GH_FieldElementDuplicate](M_Grasshopper_Kernel_Types_GH_FieldElement_Duplicate.htm).)  
![Public method](../icons/pubmethod.gif)|
[Force](M_Grasshopper_Kernel_Types_GH_SpinForce_Force.htm)|  (Overrides
[GH_FieldElementForce(Point3d)](M_Grasshopper_Kernel_Types_GH_FieldElement_Force.htm).)  
![Public method](../icons/pubmethod.gif)|
[IsCoincident](M_Grasshopper_Kernel_Types_GH_FieldElement_IsCoincident.htm)|
(Inherited from
[GH_FieldElement](T_Grasshopper_Kernel_Types_GH_FieldElement.htm).)  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_Types_GH_SpinForce_Read.htm)|  (Overrides
[GH_FieldElementRead(GH_IReader)](M_Grasshopper_Kernel_Types_GH_FieldElement_Read.htm).)  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_Types_GH_SpinForce_Write.htm)|  (Overrides
[GH_FieldElementWrite(GH_IWriter)](M_Grasshopper_Kernel_Types_GH_FieldElement_Write.htm).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

