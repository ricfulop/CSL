---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_GH_GooProxy_1.htm
scraped_at: 2025-09-08T16:20:44.428731
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[GH_GooProxy(T) Class](../html/T_Grasshopper_Kernel_Types_GH_GooProxy_1.htm
"GH_GooProxy\(T\) Class")

[GH_GooProxy(T) Constructor
](../html/M_Grasshopper_Kernel_Types_GH_GooProxy_1__ctor.htm "GH_GooProxy\(T\)
Constructor ")

[GH_GooProxy(T)
Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_GooProxy_1.htm
"GH_GooProxy\(T\) Properties")

[GH_GooProxy(T)
Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_GooProxy_1.htm
"GH_GooProxy\(T\) Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_GooProxyT Class  
  
---  
  
Abstract base implementation of IGH_GooProxy

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Kernel.TypesGH_GooProxyT  
More...

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public abstract class GH_GooProxy<T> : IGH_GooProxy
    where T : IGH_Goo
    
    
    
    Public MustInherit Class GH_GooProxy(Of T As IGH_Goo)
    	Implements IGH_GooProxy

#### Type Parameters

T

    

The GH_GooProxyT type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[GH_GooProxyT](M_Grasshopper_Kernel_Types_GH_GooProxy_1__ctor.htm)|
Initializes a new instance of the GH_GooProxyT class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[TypeDescription](P_Grasshopper_Kernel_Types_GH_GooProxy_1_TypeDescription.htm)|  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_Types_GH_GooProxy_1_TypeName.htm)|  
![Public property](../icons/pubproperty.gif)|
[Valid](P_Grasshopper_Kernel_Types_GH_GooProxy_1_Valid.htm)|  Gets a value
indicating whether this proxy represents valid data.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Construct](M_Grasshopper_Kernel_Types_GH_GooProxy_1_Construct.htm)|  Override
this method to supply a custom UI during proxy construction.  
![Public method](../icons/pubmethod.gif)|
[FormatInstance](M_Grasshopper_Kernel_Types_GH_GooProxy_1_FormatInstance.htm)|
Returns a String description of the current value.  
![Public method](../icons/pubmethod.gif)|
[FromString](M_Grasshopper_Kernel_Types_GH_GooProxy_1_FromString.htm)|  If
IsParsable(), then attempts to convert the string to a generic type value  
![Public method](../icons/pubmethod.gif)|
[MutateString](M_Grasshopper_Kernel_Types_GH_GooProxy_1_MutateString.htm)|
Munge a string to remove obvious errors on account of the user.  
![Protected method](../icons/protmethod.gif)|
[NumberToString](M_Grasshopper_Kernel_Types_GH_GooProxy_1_NumberToString.htm)|  
![Protected method](../icons/protmethod.gif)|
[StringToNumber](M_Grasshopper_Kernel_Types_GH_GooProxy_1_StringToNumber.htm)|  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Types_GH_GooProxy_1_ToString.htm)|  (Overrides
[ObjectToString](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Kernel.TypesGH_GooProxyT  
[Grasshopper.Kernel.TypesGH_AnnotationBaseGH_AnnotationBaseProxyT](T_Grasshopper_Kernel_Types_GH_AnnotationBase_GH_AnnotationBaseProxy_1.htm)  
[Grasshopper.Kernel.TypesGH_BoxGH_BoxProxy](T_Grasshopper_Kernel_Types_GH_Box_GH_BoxProxy.htm)  
[Grasshopper.Kernel.TypesGH_BrepGH_BrepProxy](T_Grasshopper_Kernel_Types_GH_Brep_GH_BrepProxy.htm)  
[Grasshopper.Kernel.TypesGH_CircleGH_CircleProxy](T_Grasshopper_Kernel_Types_GH_Circle_GH_CircleProxy.htm)  
[Grasshopper.Kernel.TypesGH_CurveGH_CurveProxy](T_Grasshopper_Kernel_Types_GH_Curve_GH_CurveProxy.htm)  
[Grasshopper.Kernel.TypesGH_ExtrusionGH_ExtrusionProxy](T_Grasshopper_Kernel_Types_GH_Extrusion_GH_ExtrusionProxy.htm)  
[Grasshopper.Kernel.TypesGH_GeometryGroupGH_GeometryGroupProxy](T_Grasshopper_Kernel_Types_GH_GeometryGroup_GH_GeometryGroupProxy.htm)  
[Grasshopper.Kernel.TypesGH_HatchGH_HatchProxy](T_Grasshopper_Kernel_Types_GH_Hatch_GH_HatchProxy.htm)  
[Grasshopper.Kernel.TypesGH_InstanceReferenceGH_InstanceReferenceProxy](T_Grasshopper_Kernel_Types_GH_InstanceReference_GH_InstanceReferenceProxy.htm)  
[Grasshopper.Kernel.TypesGH_Interval2DGH_Interval2DProxy](T_Grasshopper_Kernel_Types_GH_Interval2D_GH_Interval2DProxy.htm)  
[Grasshopper.Kernel.TypesGH_LineGH_LineProxy](T_Grasshopper_Kernel_Types_GH_Line_GH_LineProxy.htm)  
[Grasshopper.Kernel.TypesGH_MaterialGH_Material_Proxy](T_Grasshopper_Kernel_Types_GH_Material_GH_Material_Proxy.htm)  
[Grasshopper.Kernel.TypesGH_MeshGH_MeshProxy](T_Grasshopper_Kernel_Types_GH_Mesh_GH_MeshProxy.htm)  
[Grasshopper.Kernel.TypesGH_MeshFaceGH_MeshFaceProxy](T_Grasshopper_Kernel_Types_GH_MeshFace_GH_MeshFaceProxy.htm)  
[Grasshopper.Kernel.TypesGH_MeshingParametersRhMesherSettings_Proxy](T_Grasshopper_Kernel_Types_GH_MeshingParameters_RhMesherSettings_Proxy.htm)  
[Grasshopper.Kernel.TypesGH_PlaneGH_PlaneProxy](T_Grasshopper_Kernel_Types_GH_Plane_GH_PlaneProxy.htm)  
[Grasshopper.Kernel.TypesGH_PointGH_PointProxy](T_Grasshopper_Kernel_Types_GH_Point_GH_PointProxy.htm)  
[Grasshopper.Kernel.TypesGH_PointCloudPointCloudProxy](T_Grasshopper_Kernel_Types_GH_PointCloud_PointCloudProxy.htm)  
[Grasshopper.Kernel.TypesGH_RectangleGH_RectangleProxy](T_Grasshopper_Kernel_Types_GH_Rectangle_GH_RectangleProxy.htm)  
[Grasshopper.Kernel.TypesGH_SubDGH_SubDProxy](T_Grasshopper_Kernel_Types_GH_SubD_GH_SubDProxy.htm)  
[Grasshopper.Kernel.TypesGH_SurfaceGH_SurfaceProxy](T_Grasshopper_Kernel_Types_GH_Surface_GH_SurfaceProxy.htm)  
[Grasshopper.Kernel.TypesGH_TextDotGH_TextDotProxy](T_Grasshopper_Kernel_Types_GH_TextDot_GH_TextDotProxy.htm)  
[Grasshopper.Kernel.TypesGH_VectorGH_VectorProxy](T_Grasshopper_Kernel_Types_GH_Vector_GH_VectorProxy.htm)  

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

