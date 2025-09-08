---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_RenderArgs.htm
scraped_at: 2025-09-08T16:17:46.643542
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_RenderArgs Class](../html/T_Grasshopper_Kernel_GH_RenderArgs.htm
"GH_RenderArgs Class")

[GH_RenderArgs Constructor
](../html/Overload_Grasshopper_Kernel_GH_RenderArgs__ctor.htm "GH_RenderArgs
Constructor ")

[GH_RenderArgs
Properties](../html/Properties_T_Grasshopper_Kernel_GH_RenderArgs.htm
"GH_RenderArgs Properties")

[GH_RenderArgs Methods](../html/Methods_T_Grasshopper_Kernel_GH_RenderArgs.htm
"GH_RenderArgs Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_RenderArgs Class  
  
---  
  
This class is passed to objects that implement IGH_RenderAwareData or
IGH_RenderAwareObject during render queue operations.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_RenderArgs  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_RenderArgs
    
    
    Public Class GH_RenderArgs

The GH_RenderArgs type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)| [GH_RenderArgs(RhinoDoc,
ViewportInfo, RenderPrimitiveList, Guid, DictionaryInt32,
RenderMaterial)](M_Grasshopper_Kernel_GH_RenderArgs__ctor_1.htm)|
**Obsolete.** Create new render arguments.  
![Public method](../icons/pubmethod.gif)| [GH_RenderArgs(RhinoDoc,
ViewportInfo, RenderPrimitiveList, Guid, RenderMaterial,
RenderMaterial)](M_Grasshopper_Kernel_GH_RenderArgs__ctor.htm)|  **Obsolete.**
Create new render arguments.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Document](P_Grasshopper_Kernel_GH_RenderArgs_Document.htm)|  Gets the rhino
document from whence the render originated.  
![Public property](../icons/pubproperty.gif)|
[MaterialNormal](P_Grasshopper_Kernel_GH_RenderArgs_MaterialNormal.htm)|
**Obsolete.** Gets the material hint to use for unselected objects.  
![Public property](../icons/pubproperty.gif)|
[MaterialSelected](P_Grasshopper_Kernel_GH_RenderArgs_MaterialSelected.htm)|
**Obsolete.** Gets the material hint to use for selected objects.  
![Public property](../icons/pubproperty.gif)|
[ModelTransform](P_Grasshopper_Kernel_GH_RenderArgs_ModelTransform.htm)|  Gets
the current model transform.  
![Public property](../icons/pubproperty.gif)|
[PluginId](P_Grasshopper_Kernel_GH_RenderArgs_PluginId.htm)|  Gets the render
plugin id that is about to render this geometry.  
![Public property](../icons/pubproperty.gif)|
[Viewport](P_Grasshopper_Kernel_GH_RenderArgs_Viewport.htm)|  Gets the
viewport details involved in this rendering.  
![Public property](../icons/pubproperty.gif)|
[ViewportName](P_Grasshopper_Kernel_GH_RenderArgs_ViewportName.htm)|  Gets the
viewport name involved in this rendering.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[PopModelTransform](M_Grasshopper_Kernel_GH_RenderArgs_PopModelTransform.htm)|  
![Public method](../icons/pubmethod.gif)|
[PushModelTransform](M_Grasshopper_Kernel_GH_RenderArgs_PushModelTransform.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

