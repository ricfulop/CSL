---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_PreviewUtil.htm
scraped_at: 2025-09-08T16:17:39.609904
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_PreviewUtil Class](../html/T_Grasshopper_Kernel_GH_PreviewUtil.htm
"GH_PreviewUtil Class")

[GH_PreviewUtil Constructor
](../html/Overload_Grasshopper_Kernel_GH_PreviewUtil__ctor.htm "GH_PreviewUtil
Constructor ")

[GH_PreviewUtil
Properties](../html/Properties_T_Grasshopper_Kernel_GH_PreviewUtil.htm
"GH_PreviewUtil Properties")

[GH_PreviewUtil
Methods](../html/Methods_T_Grasshopper_Kernel_GH_PreviewUtil.htm
"GH_PreviewUtil Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_PreviewUtil Class  
  
---  
  
This class exposes functionality that makes it easy to draw temporary geometry
in Rhino viewports.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_PreviewUtil  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class GH_PreviewUtil : IDisposable
    
    
    Public NotInheritable Class GH_PreviewUtil
    	Implements IDisposable

The GH_PreviewUtil type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_PreviewUtil](M_Grasshopper_Kernel_GH_PreviewUtil__ctor.htm)| Initializes a
new instance of the GH_PreviewUtil class  
![Public method](../icons/pubmethod.gif)|
[GH_PreviewUtil(Boolean)](M_Grasshopper_Kernel_GH_PreviewUtil__ctor_1.htm)|
Initializes a new instance of the GH_PreviewUtil class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Enabled](P_Grasshopper_Kernel_GH_PreviewUtil_Enabled.htm)|  Gets or sets the
enabled state of this Preview util.  
![Public property](../icons/pubproperty.gif)|
[WireColour](P_Grasshopper_Kernel_GH_PreviewUtil_WireColour.htm)|  Gets or
sets the colour to use for Preview geometry.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AddBox](M_Grasshopper_Kernel_GH_PreviewUtil_AddBox.htm)|  Add a box to the
temporary Preview lists.  
![Public method](../icons/pubmethod.gif)|
[AddBrep](M_Grasshopper_Kernel_GH_PreviewUtil_AddBrep.htm)|  Add a brep to the
temporary Preview lists.  
![Public method](../icons/pubmethod.gif)|
[AddCurve](M_Grasshopper_Kernel_GH_PreviewUtil_AddCurve.htm)|  Add a curve to
the temporary Preview lists.  
![Public method](../icons/pubmethod.gif)|
[AddLine](M_Grasshopper_Kernel_GH_PreviewUtil_AddLine.htm)|  Add a line to the
temporary Preview lists.  
![Public method](../icons/pubmethod.gif)|
[AddMesh](M_Grasshopper_Kernel_GH_PreviewUtil_AddMesh.htm)|  Add a mesh to the
temporary Preview lists.  
![Public method](../icons/pubmethod.gif)|
[AddPlane](M_Grasshopper_Kernel_GH_PreviewUtil_AddPlane.htm)|  Add a plane to
the temporary Preview lists.  
![Public method](../icons/pubmethod.gif)|
[AddPoint](M_Grasshopper_Kernel_GH_PreviewUtil_AddPoint.htm)|  Add a point to
the temporary Preview lists.  
![Public method](../icons/pubmethod.gif)|
[AddVector](M_Grasshopper_Kernel_GH_PreviewUtil_AddVector.htm)|  Add a vector
to the temporary Preview lists.  
![Public method](../icons/pubmethod.gif)|
[Clear](M_Grasshopper_Kernel_GH_PreviewUtil_Clear.htm)|  Clear all temporary
geometry.  
![Public method](../icons/pubmethod.gif)|
[Dispose](M_Grasshopper_Kernel_GH_PreviewUtil_Dispose.htm)| Releases all
resources used by the GH_PreviewUtil  
![Public method](../icons/pubmethod.gif)|
[Redraw](M_Grasshopper_Kernel_GH_PreviewUtil_Redraw.htm)|  Forces a redraw the
the viewports.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

