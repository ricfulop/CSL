---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm
scraped_at: 2025-09-08T16:15:42.109348
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_Component.GH_InputParamManager
Class](../html/T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm
"GH_Component.GH_InputParamManager Class")

[GH_InputParamManager
Properties](../html/Properties_T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm
"GH_InputParamManager Properties")

[GH_InputParamManager
Methods](../html/Methods_T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm
"GH_InputParamManager Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_ComponentGH_InputParamManager Class  
  
---  
  
This class is used during Component construction to add input parameters.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
GH_ParamManager  
Grasshopper.KernelGH_ComponentGH_InputParamManager  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    protected class GH_InputParamManager : GH_ParamManager
    
    
    Protected Class GH_InputParamManager
    	Inherits GH_ParamManager

The GH_ComponentGH_InputParamManager type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Param](P_Grasshopper_Kernel_GH_Component_GH_InputParamManager_Param.htm)|
Gets the input parameter at the given index.  (Overrides
GH_ParamManager.Param.)  
![Public property](../icons/pubproperty.gif)|
[ParamCount](P_Grasshopper_Kernel_GH_Component_GH_InputParamManager_ParamCount.htm)|
Returns the number of input parameters already part of this component.
(Overrides GH_ParamManager.ParamCount.)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)| [AddAngleParameter(String, String,
String,
GH_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddAngleParameter.htm)|
Add a floating point Number parameter to the input list of this component. The
parameter will be aware that it is representing angles.  
![Public method](../icons/pubmethod.gif)| [AddAngleParameter(String, String,
String, GH_ParamAccess,
IEnumerableDouble)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddAngleParameter_1.htm)|
Add a floating point Number parameter to the input list of this component. The
parameter will be aware that it is representing angles.  
![Public method](../icons/pubmethod.gif)| [AddAngleParameter(String, String,
String, GH_ParamAccess,
Double)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddAngleParameter_2.htm)|
Add a floating point Number parameter to the input list of this component. The
parameter will be aware that it is representing angles.  
![Public method](../icons/pubmethod.gif)| [AddArcParameter(String, String,
String,
GH_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddArcParameter.htm)|
Add a 3D Arc parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddArcParameter(String, String,
String, GH_ParamAccess,
Arc)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddArcParameter_1.htm)|
Add a 3D Arc parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddBooleanParameter(String, String,
String,
GH_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddBooleanParameter.htm)|
Add a Boolean parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddBooleanParameter(String, String,
String, GH_ParamAccess,
Boolean)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddBooleanParameter_1.htm)|
Add a Boolean parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddBooleanParameter(String, String,
String, GH_ParamAccess,
IEnumerableBoolean)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddBooleanParameter_2.htm)|
Add a Boolean parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddBoxParameter(String, String,
String,
GH_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddBoxParameter.htm)|
Add a 3D Box parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddBoxParameter(String, String,
String, GH_ParamAccess,
Box)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddBoxParameter_1.htm)|
Add a 3D Box parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)|
[AddBrepParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddBrepParameter.htm)|
Add a 3D Brep parameter to the input list of this component. Brep parameters
can handle both trimmed and untrimmed single or multi-faced Breps.  
![Public method](../icons/pubmethod.gif)| [AddCircleParameter(String, String,
String,
GH_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddCircleParameter.htm)|
Add a 3D Circle parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddCircleParameter(String, String,
String, GH_ParamAccess,
Circle)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddCircleParameter_1.htm)|
Add a 3D Circle parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddColourParameter(String, String,
String,
GH_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddColourParameter.htm)|
Add an ARGB Colour parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddColourParameter(String, String,
String, GH_ParamAccess,
IEnumerableColor)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddColourParameter_1.htm)|
Add an ARGB Colour parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddColourParameter(String, String,
String, GH_ParamAccess,
Color)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddColourParameter_2.htm)|
Add an ARGB Colour parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddComplexNumberParameter(String,
String, String,
GH_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddComplexNumberParameter.htm)|
Add a Complex Number parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddComplexNumberParameter(String,
String, String, GH_ParamAccess,
GH_ComplexNumber)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddComplexNumberParameter_1.htm)|
Add a Complex Number parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddCultureParameter(String, String,
String,
GH_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddCultureParameter.htm)|
Add a Cultue parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddCultureParameter(String, String,
String, GH_ParamAccess,
CultureInfo)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddCultureParameter_1.htm)|
Add a Culture parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)|
[AddCurveParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddCurveParameter.htm)|
Add a 3D Curve parameter to the input list of this component. Curve parameters
can handle all curve types (Lines, Polylines, Circles, Arcs, NurbsCurves etc.)  
![Public method](../icons/pubmethod.gif)|
[AddFieldParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddFieldParameter.htm)|
Add a Field parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)|
[AddGenericParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddGenericParameter.htm)|
Add a Generic parameter to the input list of this component. Generic
parameters can handle all types of data.  
![Public method](../icons/pubmethod.gif)|
[AddGeometryParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddGeometryParameter.htm)|
Add a generic 3D Geometry parameter to the input list of this component.
Geometry parameters can handle all types that represent actual shapes.  
![Public method](../icons/pubmethod.gif)|
[AddGroupParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddGroupParameter.htm)|
Add a Transform Group parameter to the input list of this component. Groups
are collections of geometry that are transformed as one, they are not the same
as Rhino groups.  
![Public method](../icons/pubmethod.gif)| [AddIntegerParameter(String, String,
String,
GH_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddIntegerParameter.htm)|
Add a Integer parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddIntegerParameter(String, String,
String, GH_ParamAccess,
IEnumerableInt32)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddIntegerParameter_1.htm)|
Add a Integer parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddIntegerParameter(String, String,
String, GH_ParamAccess,
Int32)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddIntegerParameter_2.htm)|
Add a Integer parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)|
[AddInterval2DParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddInterval2DParameter.htm)|
Add an Interval2D (i.e. uv domain) parameter to the input list of this
component.  
![Public method](../icons/pubmethod.gif)| [AddIntervalParameter(String,
String, String,
GH_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddIntervalParameter.htm)|
Add an Interval (i.e. numeric domain) parameter to the input list of this
component.  
![Public method](../icons/pubmethod.gif)| [AddIntervalParameter(String,
String, String, GH_ParamAccess,
Interval)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddIntervalParameter_1.htm)|
Add an Interval (i.e. numeric domain) parameter to the input list of this
component.  
![Public method](../icons/pubmethod.gif)| [AddIntervalParameter(String,
String, String, GH_ParamAccess,
IEnumerableInterval)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddIntervalParameter_2.htm)|
Add an Interval (i.e. numeric domain) parameter to the input list of this
component.  
![Public method](../icons/pubmethod.gif)| [AddLineParameter(String, String,
String,
GH_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddLineParameter.htm)|
Add a 3D Line parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddLineParameter(String, String,
String, GH_ParamAccess,
Line)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddLineParameter_1.htm)|
Add a 3D Line parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)|
[AddMatrixParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddMatrixParameter.htm)|
Add a Matrix parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)|
[AddMeshFaceParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddMeshFaceParameter.htm)|
Add a topological MeshFace parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)|
[AddMeshParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddMeshParameter.htm)|
Add a 3D Mesh parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddNumberParameter(String, String,
String,
GH_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddNumberParameter.htm)|
Add a floating point Number parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddNumberParameter(String, String,
String, GH_ParamAccess,
IEnumerableDouble)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddNumberParameter_1.htm)|
Add a floating point Number parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddNumberParameter(String, String,
String, GH_ParamAccess,
Double)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddNumberParameter_2.htm)|
Add a floating point Number parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)|
[AddParameter(IGH_Param)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddParameter.htm)|
Generic parameter addition. If you cannot use one of the utility methods
provided by this class, you can register a customized parameter using this
method.  
![Public method](../icons/pubmethod.gif)| [AddParameter(IGH_Param, String,
String, String,
GH_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddParameter_1.htm)|
Generic parameter addition. If you cannot use one of the utility methods
provided by this class, you can register a customized parameter using this
method.  
![Public method](../icons/pubmethod.gif)|
[AddPathParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddPathParameter.htm)|
Add a Data Path parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddPlaneParameter(String, String,
String,
GH_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddPlaneParameter.htm)|
Add a 3D Plane parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddPlaneParameter(String, String,
String, GH_ParamAccess,
Plane)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddPlaneParameter_1.htm)|
Add a 3D Plane parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddPointParameter(String, String,
String,
GH_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddPointParameter.htm)|
Add a 3D Point parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddPointParameter(String, String,
String, GH_ParamAccess,
Point3d)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddPointParameter_1.htm)|
Register a new 3D point param with a single default coordinate.  
![Public method](../icons/pubmethod.gif)| [AddPointParameter(String, String,
String, GH_ParamAccess,
IEnumerablePoint3d)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddPointParameter_2.htm)|
Register a new 3D point param with multiple default coordinates.  
![Public method](../icons/pubmethod.gif)| [AddRectangleParameter(String,
String, String,
GH_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddRectangleParameter.htm)|
Add a 3D Rectangle parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddRectangleParameter(String,
String, String, GH_ParamAccess,
Rectangle3d)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddRectangleParameter_1.htm)|
Add a 3D Rectangle parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)|
[AddScriptVariableParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddScriptVariableParameter.htm)|
Add a Script Variable parameter to the input list of this component. Script
variable parameters are used almost exclusively in VB/C#/Python components so
you probably don't want this one.  
![Public method](../icons/pubmethod.gif)|
[AddSubDParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddSubDParameter.htm)|
Add a 3D Sub-D parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)|
[AddSurfaceParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddSurfaceParameter.htm)|
Add a 3D Surface parameter to the input list of this component. Surface
parameters can handle both trimmed and untrimmed single-faced Breps.  
![Public method](../icons/pubmethod.gif)| [AddTextParameter(String, String,
String,
GH_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddTextParameter.htm)|
Add a Text parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddTextParameter(String, String,
String, GH_ParamAccess,
IEnumerableString)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddTextParameter_1.htm)|
Add a Text parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddTextParameter(String, String,
String, GH_ParamAccess,
String)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddTextParameter_2.htm)|
Add a Text parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddTimeParameter(String, String,
String,
GH_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddTimeParameter.htm)|
Add a Time parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddTimeParameter(String, String,
String, GH_ParamAccess,
DateTime)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddTimeParameter_1.htm)|
Add a Time parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)|
[AddTransformParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddTransformParameter.htm)|
Add a Transformation parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddVectorParameter(String, String,
String,
GH_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddVectorParameter.htm)|
Add a 3D Vector parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)| [AddVectorParameter(String, String,
String, GH_ParamAccess,
Vector3d)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddVectorParameter_1.htm)|
Add a 3D Vector parameter to the input list of this component.  
![Public method](../icons/pubmethod.gif)|
[HideParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_HideParameter.htm)|
Hide a specific input parameter. If the parameter at the given index
implements IGH_PreviewObject then the Hidden flag will be set to True.
Otherwise, nothing will happen.  (Overrides
GH_ParamManager.HideParameter(Int32).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

