---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_GH_Field.htm
scraped_at: 2025-09-08T16:20:37.374525
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[GH_Field Class](../html/T_Grasshopper_Kernel_Types_GH_Field.htm "GH_Field
Class")

[GH_Field Constructor
](../html/Overload_Grasshopper_Kernel_Types_GH_Field__ctor.htm "GH_Field
Constructor ")

[GH_Field
Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Field.htm
"GH_Field Properties")

[GH_Field Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Field.htm
"GH_Field Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Field Class  
  
---  
  
Represents a field of forces.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Kernel.TypesGH_Field  

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Field : IGH_Goo, IGH_PreviewData
    
    
    Public Class GH_Field
    	Implements IGH_Goo, IGH_PreviewData

The GH_Field type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_Field](M_Grasshopper_Kernel_Types_GH_Field__ctor.htm)|  Blank constructor.  
![Public method](../icons/pubmethod.gif)|
[GH_Field(GH_Field)](M_Grasshopper_Kernel_Types_GH_Field__ctor_1.htm)|  Copy
constructor.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[ClippingBox](P_Grasshopper_Kernel_Types_GH_Field_ClippingBox.htm)|  
![Public property](../icons/pubproperty.gif)|
[Elements](P_Grasshopper_Kernel_Types_GH_Field_Elements.htm)|  Gets the list
of elements of this field.  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Kernel_Types_GH_Field_IsValid.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Field_IsValidWhyNot.htm)|  
![Public property](../icons/pubproperty.gif)|
[TypeDescription](P_Grasshopper_Kernel_Types_GH_Field_TypeDescription.htm)|  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_Types_GH_Field_TypeName.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CastFrom](M_Grasshopper_Kernel_Types_GH_Field_CastFrom.htm)|  
![Public method](../icons/pubmethod.gif)|
[CastToT](M_Grasshopper_Kernel_Types_GH_Field_CastTo__1.htm)|  
![Public method](../icons/pubmethod.gif)|
[CurvatureAt](M_Grasshopper_Kernel_Types_GH_Field_CurvatureAt.htm)|  
![Public method](../icons/pubmethod.gif)|
[DrawViewportMeshes](M_Grasshopper_Kernel_Types_GH_Field_DrawViewportMeshes.htm)|  
![Public method](../icons/pubmethod.gif)|
[DrawViewportWires](M_Grasshopper_Kernel_Types_GH_Field_DrawViewportWires.htm)|  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Kernel_Types_GH_Field_Duplicate.htm)|  
![Public method](../icons/pubmethod.gif)|
[EmitProxy](M_Grasshopper_Kernel_Types_GH_Field_EmitProxy.htm)|  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_Types_GH_Field_Read.htm)|  
![Public method](../icons/pubmethod.gif)|
[ScriptVariable](M_Grasshopper_Kernel_Types_GH_Field_ScriptVariable.htm)|  
![Public method](../icons/pubmethod.gif)|
[SolveStep](M_Grasshopper_Kernel_Types_GH_Field_SolveStep.htm)|  Move a point
through the field.  
![Public method](../icons/pubmethod.gif)|
[SolveSteps](M_Grasshopper_Kernel_Types_GH_Field_SolveSteps.htm)|  Move a
point through a succession of steps.  
![Public method](../icons/pubmethod.gif)|
[TensorAt](M_Grasshopper_Kernel_Types_GH_Field_TensorAt.htm)|  Compute the
field tensor at the given location as contributed by all the field elements.  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Types_GH_Field_ToString.htm)|  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_Types_GH_Field_Write.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

