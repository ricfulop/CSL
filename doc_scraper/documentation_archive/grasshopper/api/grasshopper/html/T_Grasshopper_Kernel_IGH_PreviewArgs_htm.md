---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_IGH_PreviewArgs.htm
scraped_at: 2025-09-08T16:18:37.862506
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH_PreviewArgs Interface](../html/T_Grasshopper_Kernel_IGH_PreviewArgs.htm
"IGH_PreviewArgs Interface")

[IGH_PreviewArgs
Properties](../html/Properties_T_Grasshopper_Kernel_IGH_PreviewArgs.htm
"IGH_PreviewArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_PreviewArgs Interface  
  
---  
  
Preview display arguments for IGH_PreviewObjects.

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_PreviewArgs
    
    
    Public Interface IGH_PreviewArgs

The IGH_PreviewArgs type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[DefaultCurveThickness](P_Grasshopper_Kernel_IGH_PreviewArgs_DefaultCurveThickness.htm)|
Gets the curve thickness as defined by the viewport display scheme.  
![Public property](../icons/pubproperty.gif)|
[Display](P_Grasshopper_Kernel_IGH_PreviewArgs_Display.htm)|  Gets the
Pipeline that is being used to draw the current preview.  
![Public property](../icons/pubproperty.gif)|
[Document](P_Grasshopper_Kernel_IGH_PreviewArgs_Document.htm)|  Gets the
Grasshopper document that is currently drawing the preview.  
![Public property](../icons/pubproperty.gif)|
[MeshingParameters](P_Grasshopper_Kernel_IGH_PreviewArgs_MeshingParameters.htm)|
Gets the meshing parameters to be used during meshing breps.  
![Public property](../icons/pubproperty.gif)|
[ShadeMaterial](P_Grasshopper_Kernel_IGH_PreviewArgs_ShadeMaterial.htm)|  Gets
the document default material for unselected Faces.  
![Public property](../icons/pubproperty.gif)|
[ShadeMaterial_Selected](P_Grasshopper_Kernel_IGH_PreviewArgs_ShadeMaterial_Selected.htm)|
Gets the document default material for selected Faces.  
![Public property](../icons/pubproperty.gif)|
[Viewport](P_Grasshopper_Kernel_IGH_PreviewArgs_Viewport.htm)|  Gets the
Viewport in which the current preview is drawn.  
![Public property](../icons/pubproperty.gif)|
[WireColour](P_Grasshopper_Kernel_IGH_PreviewArgs_WireColour.htm)|  Gets the
document default colour for unselected Wires.  
![Public property](../icons/pubproperty.gif)|
[WireColour_Selected](P_Grasshopper_Kernel_IGH_PreviewArgs_WireColour_Selected.htm)|
Gets the document default colour for selected Wires.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

