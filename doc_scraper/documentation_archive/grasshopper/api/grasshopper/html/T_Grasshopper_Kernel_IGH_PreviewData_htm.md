---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_IGH_PreviewData.htm
scraped_at: 2025-09-08T16:18:38.862434
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH_PreviewData Interface](../html/T_Grasshopper_Kernel_IGH_PreviewData.htm
"IGH_PreviewData Interface")

[IGH_PreviewData
Properties](../html/Properties_T_Grasshopper_Kernel_IGH_PreviewData.htm
"IGH_PreviewData Properties")

[IGH_PreviewData
Methods](../html/Methods_T_Grasshopper_Kernel_IGH_PreviewData.htm
"IGH_PreviewData Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_PreviewData Interface  
  
---  
  
All IGH_Goo types that wish to participate in Viewport redraws must implement
this interface.

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_PreviewData
    
    
    Public Interface IGH_PreviewData

The IGH_PreviewData type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[ClippingBox](P_Grasshopper_Kernel_IGH_PreviewData_ClippingBox.htm)|  Gets the
clipping box for this data. The clipping box is typically the same as the
boundingbox.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[DrawViewportMeshes](M_Grasshopper_Kernel_IGH_PreviewData_DrawViewportMeshes.htm)|
Implement this function to draw all shaded meshes. If the viewport does not
support shading, this function will not be called.  
![Public method](../icons/pubmethod.gif)|
[DrawViewportWires](M_Grasshopper_Kernel_IGH_PreviewData_DrawViewportWires.htm)|
Implement this function to draw all wire and point previews.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

