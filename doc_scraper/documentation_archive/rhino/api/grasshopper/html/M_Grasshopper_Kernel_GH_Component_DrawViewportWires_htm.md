---
url: https://developer.rhino3d.com/api/grasshopper/html/M_Grasshopper_Kernel_GH_Component_DrawViewportWires.htm
scraped_at: 2025-09-08T16:03:13.713332
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_Component Class](../html/T_Grasshopper_Kernel_GH_Component.htm
"GH_Component Class")

[GH_Component Methods](../html/Methods_T_Grasshopper_Kernel_GH_Component.htm
"GH_Component Methods")

[AddedToDocument Method
](../html/M_Grasshopper_Kernel_GH_Component_AddedToDocument.htm
"AddedToDocument Method ")

[AfterSolveInstance Method
](../html/M_Grasshopper_Kernel_GH_Component_AfterSolveInstance.htm
"AfterSolveInstance Method ")

[AppendAdditionalComponentMenuItems Method
](../html/M_Grasshopper_Kernel_GH_Component_AppendAdditionalComponentMenuItems.htm
"AppendAdditionalComponentMenuItems Method ")

[AppendAdditionalMenuItems Method
](../html/M_Grasshopper_Kernel_GH_Component_AppendAdditionalMenuItems.htm
"AppendAdditionalMenuItems Method ")

[AssignInitCodeToInputParameter Method
](../html/M_Grasshopper_Kernel_GH_Component_AssignInitCodeToInputParameter.htm
"AssignInitCodeToInputParameter Method ")

[BakeGeometry Method
](../html/Overload_Grasshopper_Kernel_GH_Component_BakeGeometry.htm
"BakeGeometry Method ")

[BeforeSolveInstance Method
](../html/M_Grasshopper_Kernel_GH_Component_BeforeSolveInstance.htm
"BeforeSolveInstance Method ")

[ClearData Method ](../html/M_Grasshopper_Kernel_GH_Component_ClearData.htm
"ClearData Method ")

[ClearRuntimeMessages Method
](../html/M_Grasshopper_Kernel_GH_Component_ClearRuntimeMessages.htm
"ClearRuntimeMessages Method ")

[CollectData Method
](../html/M_Grasshopper_Kernel_GH_Component_CollectData.htm "CollectData
Method ")

[ComputeData Method
](../html/M_Grasshopper_Kernel_GH_Component_ComputeData.htm "ComputeData
Method ")

[CreateAttributes Method
](../html/M_Grasshopper_Kernel_GH_Component_CreateAttributes.htm
"CreateAttributes Method ")

[DependsOn Method ](../html/M_Grasshopper_Kernel_GH_Component_DependsOn.htm
"DependsOn Method ")

[DocumentAngleTolerance Method
](../html/M_Grasshopper_Kernel_GH_Component_DocumentAngleTolerance.htm
"DocumentAngleTolerance Method ")

[DocumentContextChanged Method
](../html/M_Grasshopper_Kernel_GH_Component_DocumentContextChanged.htm
"DocumentContextChanged Method ")

[DocumentTolerance Method
](../html/M_Grasshopper_Kernel_GH_Component_DocumentTolerance.htm
"DocumentTolerance Method ")

[DrawViewportMeshes Method
](../html/M_Grasshopper_Kernel_GH_Component_DrawViewportMeshes.htm
"DrawViewportMeshes Method ")

[DrawViewportWires Method
](../html/M_Grasshopper_Kernel_GH_Component_DrawViewportWires.htm
"DrawViewportWires Method ")

[ExpireDownStreamObjects Method
](../html/M_Grasshopper_Kernel_GH_Component_ExpireDownStreamObjects.htm
"ExpireDownStreamObjects Method ")

[GenerateDefaultHTML Method
](../html/M_Grasshopper_Kernel_GH_Component_GenerateDefaultHTML.htm
"GenerateDefaultHTML Method ")

[GenerateParameterHelp Method
](../html/Overload_Grasshopper_Kernel_GH_Component_GenerateParameterHelp.htm
"GenerateParameterHelp Method ")

[HtmlHelp_Source Method
](../html/M_Grasshopper_Kernel_GH_Component_HtmlHelp_Source.htm
"HtmlHelp_Source Method ")

[IsolateObject Method
](../html/M_Grasshopper_Kernel_GH_Component_IsolateObject.htm "IsolateObject
Method ")

[MovedBetweenDocuments Method
](../html/M_Grasshopper_Kernel_GH_Component_MovedBetweenDocuments.htm
"MovedBetweenDocuments Method ")

[PostConstructor Method
](../html/M_Grasshopper_Kernel_GH_Component_PostConstructor.htm
"PostConstructor Method ")

[Read Method ](../html/M_Grasshopper_Kernel_GH_Component_Read.htm "Read Method
")

[RegisterInputParams Method
](../html/M_Grasshopper_Kernel_GH_Component_RegisterInputParams.htm
"RegisterInputParams Method ")

[RegisterOutputParams Method
](../html/M_Grasshopper_Kernel_GH_Component_RegisterOutputParams.htm
"RegisterOutputParams Method ")

[RegisterRemoteIDs Method
](../html/M_Grasshopper_Kernel_GH_Component_RegisterRemoteIDs.htm
"RegisterRemoteIDs Method ")

[RemovedFromDocument Method
](../html/M_Grasshopper_Kernel_GH_Component_RemovedFromDocument.htm
"RemovedFromDocument Method ")

[RuntimeMessages Method
](../html/M_Grasshopper_Kernel_GH_Component_RuntimeMessages.htm
"RuntimeMessages Method ")

[SolveInstance Method
](../html/M_Grasshopper_Kernel_GH_Component_SolveInstance.htm "SolveInstance
Method ")

[Write Method ](../html/M_Grasshopper_Kernel_GH_Component_Write.htm "Write
Method ")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_ComponentDrawViewportWires Method  
  
---  
  
Draw preview wires for this component and all associated parameters.

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public virtual void DrawViewportWires(
    	IGH_PreviewArgs args
    )
    
    
    Public Overridable Sub DrawViewportWires ( 
    	args As IGH_PreviewArgs
    )

#### Parameters

args

    Type: [Grasshopper.KernelIGH_PreviewArgs](T_Grasshopper_Kernel_IGH_PreviewArgs.htm)  
Display data used during preview drawing.

#### Implements

[IGH_PreviewObjectDrawViewportWires(IGH_PreviewArgs)](M_Grasshopper_Kernel_IGH_PreviewObject_DrawViewportWires.htm)  

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH_Component Class](T_Grasshopper_Kernel_GH_Component.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

