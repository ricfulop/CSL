---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_Convert.htm
scraped_at: 2025-09-08T16:15:57.234037
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_Convert Class](../html/T_Grasshopper_Kernel_GH_Convert.htm "GH_Convert
Class")

[GH_Convert Properties](../html/Properties_T_Grasshopper_Kernel_GH_Convert.htm
"GH_Convert Properties")

[GH_Convert Methods](../html/Methods_T_Grasshopper_Kernel_GH_Convert.htm
"GH_Convert Methods")

[GH_Convert Fields](../html/Fields_T_Grasshopper_Kernel_GH_Convert.htm
"GH_Convert Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Convert Class  
  
---  
  
Provides static converters for different data types inside Grasshopper. This
class both has specific and generic converters.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_Convert  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class GH_Convert
    
    
    Public NotInheritable Class GH_Convert

The GH_Convert type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[CultureTable](P_Grasshopper_Kernel_GH_Convert_CultureTable.htm)|  Gets the
cached culture table. Do not modify this dictionary unless you know what you
are doing.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[BackSolveExpression](M_Grasshopper_Kernel_GH_Convert_BackSolveExpression.htm)|
Try and backsolve an expression  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ByteArrayToCommonObjectT](M_Grasshopper_Kernel_GH_Convert_ByteArrayToCommonObject__1.htm)|
Convert an OpenNurbs compliant compressed byte array into a RhinoCommon
object.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CombineDateAndTime](M_Grasshopper_Kernel_GH_Convert_CombineDateAndTime.htm)|
Combine a pure date and a pure time.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CommonObjectToByteArray](M_Grasshopper_Kernel_GH_Convert_CommonObjectToByteArray.htm)|
Convert a RhinoCommon object into a compressed byte-array using OpenNurbs
serialization.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateDateAndTime](M_Grasshopper_Kernel_GH_Convert_CreateDateAndTime.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreatePureDate](M_Grasshopper_Kernel_GH_Convert_CreatePureDate.htm)|  Convert
a datetime structure into a pure date, i.e. remove the time portion. As per
convention, this leaves 1 tick into the day in question intact.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreatePureTime(DateTime)](M_Grasshopper_Kernel_GH_Convert_CreatePureTime.htm)|
Convert a datetime structure into a pure time, i.e. remove the date portion.
As per convention, this means setting the year, month and day to 1.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreatePureTime(Int32, Int32,
Int32)](M_Grasshopper_Kernel_GH_Convert_CreatePureTime_1.htm)|  Create a pure
time instance. If the total number of hours, minutes and seconds exceeds a
full year then it is not possible to create a pure time and the largest
possible pure time will be returned instead.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FileToHash](M_Grasshopper_Kernel_GH_Convert_FileToHash.htm)|  Create a hash
of a file.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FindRhinoObjectByNameAndType](M_Grasshopper_Kernel_GH_Convert_FindRhinoObjectByNameAndType.htm)|
Search the current Rhino document for an object with a given name of a given
type.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[GeometryToObjRef](M_Grasshopper_Kernel_GH_Convert_GeometryToObjRef.htm)|
Create an ObjRef for a referenced IGH_GeometricGoo. Unreferenced
IGH_GeometryGoo will return null.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[GetBrepFromDocument](M_Grasshopper_Kernel_GH_Convert_GetBrepFromDocument.htm)|
Harvest a brep object from a Rhino document.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[GetClippingPlaneFromDocument](M_Grasshopper_Kernel_GH_Convert_GetClippingPlaneFromDocument.htm)|
Harvest a clipping plane surface from a Rhino document.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[GetCurveFromDocument](M_Grasshopper_Kernel_GH_Convert_GetCurveFromDocument.htm)|
Harvest a curve object from a Rhino document.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[GetExtrusionFromDocument](M_Grasshopper_Kernel_GH_Convert_GetExtrusionFromDocument.htm)|
Harvest an extrusion object from a Rhino document.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[GetMeshFromDocument](M_Grasshopper_Kernel_GH_Convert_GetMeshFromDocument.htm)|
Harvest a mesh object from a Rhino document.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[GetPlaneFromDocument](M_Grasshopper_Kernel_GH_Convert_GetPlaneFromDocument.htm)|
Harvest the object frame plane from a Rhino document.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[GetPointFromDocument](M_Grasshopper_Kernel_GH_Convert_GetPointFromDocument.htm)|
Harvest a point object from a Rhino document.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[GetSubDFromDocument](M_Grasshopper_Kernel_GH_Convert_GetSubDFromDocument.htm)|
Harvest a sub-d object from a Rhino document.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[GetSurfaceFromDocument](M_Grasshopper_Kernel_GH_Convert_GetSurfaceFromDocument.htm)|
Harvest a surface object from a Rhino document.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[GetTimeKind(DateTime)](M_Grasshopper_Kernel_GH_Convert_GetTimeKind.htm)|
Gets the kind of time implied by a System.DateTime value.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[GetTimeKind(DateTime,
DateTime)](M_Grasshopper_Kernel_GH_Convert_GetTimeKind_1.htm)|  Gets the kind
of time implied by two System.DateTime values.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[IsPureDate](M_Grasshopper_Kernel_GH_Convert_IsPureDate.htm)|  Tests whether a
DateTime instance represents a pure date (i.e. that the time portion is
undefined). Pure dates are a Grasshopper convention, basically a pure date is
1 tick past midnight.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[IsPureTime](M_Grasshopper_Kernel_GH_Convert_IsPureTime.htm)|  Tests whether a
DateTime instance represents a pure time (i.e. that the date portion is
undefined). Pure times are a Grasshopper convention, basically a pure time is
2 ticks past any second.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ObjRefToGeometry](M_Grasshopper_Kernel_GH_Convert_ObjRefToGeometry.htm)|
Convert a Rhino Object Reference into Grasshopper IGH_GeometricGoo.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ParseExpression](M_Grasshopper_Kernel_GH_Convert_ParseExpression.htm)|
Attempts to parse an expression.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[StringToDate](M_Grasshopper_Kernel_GH_Convert_StringToDate.htm)|  Convert a
string representing a date into an actual date. If a pure date is possible it
will be returned. If the input is a pure time this method will fail, you need
to use StringToTime instead.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[StringToGuid](M_Grasshopper_Kernel_GH_Convert_StringToGuid.htm)|  Create a
Guid based on SHA256 hashing of a string.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[StringToTime](M_Grasshopper_Kernel_GH_Convert_StringToTime.htm)|  Convert a
string representing a time into an pure time. Allowed separators of hour,
minute and second portions are colons, semi-colons, points and commas.
Grasshopper itself uses colons when formatting times. A PM or AM symbol is
allowed provided it does not border on any alphabetical characters. A time can
be prefixed by a "X day[s] + " string which defines the total number of
24-hour periods to include.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToAnnotationBase](M_Grasshopper_Kernel_GH_Convert_ToAnnotationBase.htm)|
Convert data into Rhino.Geometry.AnnotationBase.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToAnnotationBase_Primary](M_Grasshopper_Kernel_GH_Convert_ToAnnotationBase_Primary.htm)|
Performs a direct cast from Rhino.Geometry.AnnotationBase or
GH_AnnotationBase. Data is not guaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToAnnotationBase_Secondary](M_Grasshopper_Kernel_GH_Convert_ToAnnotationBase_Secondary.htm)|
Attempts to convert other data types into an Rhino.Geometry.AnnotationBase.
Data is not quaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToArc](M_Grasshopper_Kernel_GH_Convert_ToArc.htm)|  Convert data into
Rhino.Geometry.Arc.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToArc_Primary](M_Grasshopper_Kernel_GH_Convert_ToArc_Primary.htm)|  Performs
a direct cast from OnArc or GH_Arc. Data is not quaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToArc_Secondary](M_Grasshopper_Kernel_GH_Convert_ToArc_Secondary.htm)|
Attempts to convert other data types into an OnArc. Data is not quaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToBoolean](M_Grasshopper_Kernel_GH_Convert_ToBoolean.htm)|  Convert data into
Booleans.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToBoolean_Primary](M_Grasshopper_Kernel_GH_Convert_ToBoolean_Primary.htm)|
Performs a direct cast from boolean or GH_Boolean.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToBoolean_Secondary](M_Grasshopper_Kernel_GH_Convert_ToBoolean_Secondary.htm)|
Performs indirect casts from other data types into booleans.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToBoundingBox_Primary](M_Grasshopper_Kernel_GH_Convert_ToBoundingBox_Primary.htm)|
Performs a direct cast from OnBoundingBox. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToBox_Primary](M_Grasshopper_Kernel_GH_Convert_ToBox_Primary.htm)|  Performs
a direct cast from Box. Data is not quaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToBrep](M_Grasshopper_Kernel_GH_Convert_ToBrep.htm)|  Convert data into
Rhino.Geometry.Brep.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToBrep_Primary](M_Grasshopper_Kernel_GH_Convert_ToBrep_Primary.htm)|
Performs a direct cast from OnBrep or GH_Brep. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToBrep_Secondary](M_Grasshopper_Kernel_GH_Convert_ToBrep_Secondary.htm)|
Attempts to convert other data types into an OnBrep. Data is not quaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToCircle](M_Grasshopper_Kernel_GH_Convert_ToCircle.htm)|  Convert data into
Rhino.Geometry.Circle.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToCircle_Primary](M_Grasshopper_Kernel_GH_Convert_ToCircle_Primary.htm)|
Performs a direct cast from OnCircle or GH_Circle. Data is not quaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToCircle_Secondary](M_Grasshopper_Kernel_GH_Convert_ToCircle_Secondary.htm)|
Attempts to convert other data types into an OnCircle. Data is not quaranteed
to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToColor](M_Grasshopper_Kernel_GH_Convert_ToColor.htm)|  Convert data into
Colors.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToColor_Primary](M_Grasshopper_Kernel_GH_Convert_ToColor_Primary.htm)|
Performs a direct cast from Drawing.Color, GH_Color and OnColor.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToColor_Secondary](M_Grasshopper_Kernel_GH_Convert_ToColor_Secondary.htm)|
Performs indirect casts from other data types into Colors.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToComplex](M_Grasshopper_Kernel_GH_Convert_ToComplex.htm)|  Convert data into
Complex.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToComplex_Primary](M_Grasshopper_Kernel_GH_Convert_ToComplex_Primary.htm)|
Performs a direct cast from Complex or GH_ComplexNumber  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToComplex_Secondary](M_Grasshopper_Kernel_GH_Convert_ToComplex_Secondary.htm)|
Performs indirect casts from other data types into Complex.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToCoordinates](M_Grasshopper_Kernel_GH_Convert_ToCoordinates.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToCulture](M_Grasshopper_Kernel_GH_Convert_ToCulture.htm)|  Convert data into
Colors.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToCulture_Primary](M_Grasshopper_Kernel_GH_Convert_ToCulture_Primary.htm)|
Performs a direct cast from System.Globalization.CultureInfo and GH_Culture.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToCulture_Secondary](M_Grasshopper_Kernel_GH_Convert_ToCulture_Secondary.htm)|
Performs indirect casts from other data types into CultureInfo.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToCurve](M_Grasshopper_Kernel_GH_Convert_ToCurve.htm)|  Convert data into
Rhino.Geometry.Curve.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToCurve_Primary](M_Grasshopper_Kernel_GH_Convert_ToCurve_Primary.htm)|
Performs a direct cast from OnCurve or GH_Curve. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToCurve_Secondary](M_Grasshopper_Kernel_GH_Convert_ToCurve_Secondary.htm)|
Attempts to convert other data types into an IOnCurve. Data is not quaranteed
to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToDate](M_Grasshopper_Kernel_GH_Convert_ToDate.htm)|  Convert data into
Dates.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToDate_Primary](M_Grasshopper_Kernel_GH_Convert_ToDate_Primary.htm)|
Performs a direct cast from DateTime or GH_DateTime.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToDate_Secondary](M_Grasshopper_Kernel_GH_Convert_ToDate_Secondary.htm)|
Performs indirect casts from other data types into DateTime constructs.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToDimension](M_Grasshopper_Kernel_GH_Convert_ToDimension.htm)|  Convert data
into Rhino.Geometry.Dimension.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToDimension_Primary](M_Grasshopper_Kernel_GH_Convert_ToDimension_Primary.htm)|
Performs a direct cast from Rhino.Geometry.Dimension or GH_Dimension. Data is
not guaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToDimension_Secondary](M_Grasshopper_Kernel_GH_Convert_ToDimension_Secondary.htm)|
Attempts to convert other data types into an Rhino.Geometry.Dimension. Data is
not quaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToDouble](M_Grasshopper_Kernel_GH_Convert_ToDouble.htm)|  Convert data into
Doubles.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToDouble_Primary](M_Grasshopper_Kernel_GH_Convert_ToDouble_Primary.htm)|
Performs a direct cast from Double or GH_Number.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToDouble_Secondary](M_Grasshopper_Kernel_GH_Convert_ToDouble_Secondary.htm)|
Performs indirect casts from other data types into Doubles.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToExtrusion](M_Grasshopper_Kernel_GH_Convert_ToExtrusion.htm)|  Convert data
into Rhino.Geometry.Brep.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToExtrusion_Primary](M_Grasshopper_Kernel_GH_Convert_ToExtrusion_Primary.htm)|
Performs a direct cast from Rhino.Geometry.Extrusion or GH_Extrusion. Data is
not quaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToExtrusion_Secondary](M_Grasshopper_Kernel_GH_Convert_ToExtrusion_Secondary.htm)|
Attempts to convert other data types into a Extrusion. Data is not quaranteed
to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGeometricGoo](M_Grasshopper_Kernel_GH_Convert_ToGeometricGoo.htm)|
Converts an object into GeometricGoo. Does not duplicate the data if a
lossless conversion is possible.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGeometryBase](M_Grasshopper_Kernel_GH_Convert_ToGeometryBase.htm)|  Attempt
to convert an object into a Rhino.Geometry.GeometryBase instance.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHAngularDimension](M_Grasshopper_Kernel_GH_Convert_ToGHAngularDimension.htm)|
Convert data into GH_AngularDimension.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHAngularDimension_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHAngularDimension_Primary.htm)|
Converts similar data into a GH_AngularDimension instance. Data is not
guaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHAngularDimension_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHAngularDimension_Secondary.htm)|
Converts similar data into a GH_AngularDimension instance. Data is not
guaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHAnnotationBase](M_Grasshopper_Kernel_GH_Convert_ToGHAnnotationBase.htm)|
Convert data into GH_AnnotationBase.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHArc](M_Grasshopper_Kernel_GH_Convert_ToGHArc.htm)|  Convert data into
GH_Arcs.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHArc_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHArc_Primary.htm)|
Converts similar data into a GH_Arc instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHArc_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHArc_Secondary.htm)|
Converts similar data into a GH_Arc instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHBoolean](M_Grasshopper_Kernel_GH_Convert_ToGHBoolean.htm)|  Convert data
into GH_Boolean.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHBoolean_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHBoolean_Primary.htm)|
Converts similar data into a GH_Boolean instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHBoolean_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHBoolean_Secondary.htm)|
Converts similar data into a GH_Boolean instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHBox](M_Grasshopper_Kernel_GH_Convert_ToGHBox.htm)|  Convert data into
GH_Boxes.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHBox_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHBox_Primary.htm)|
Converts similar data into a GH_Box instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHBox_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHBox_Secondary.htm)|
Converts similar data into a GH_Box instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHBrep](M_Grasshopper_Kernel_GH_Convert_ToGHBrep.htm)|  Convert data into
GH_Breps.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHBrep_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHBrep_Primary.htm)|
Converts similar data into a GH_Brep instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHBrep_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHBrep_Secondary.htm)|
Converts similar data into a GH_Brep instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHCentermark](M_Grasshopper_Kernel_GH_Convert_ToGHCentermark.htm)|  Convert
data into GH_Centermark.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHCentermark_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHCentermark_Primary.htm)|
Converts similar data into a GH_Centermark instance. Data is not guaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHCentermark_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHCentermark_Secondary.htm)|
Converts similar data into a GH_Centermark instance. Data is not guaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHCircle](M_Grasshopper_Kernel_GH_Convert_ToGHCircle.htm)|  Convert data
into GH_Circles.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHCircle_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHCircle_Primary.htm)|
Converts similar data into a GH_Circle instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHCircle_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHCircle_Secondary.htm)|
Converts similar data into a GH_Circle instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHColour](M_Grasshopper_Kernel_GH_Convert_ToGHColour.htm)|  Convert data
into GH_Colour.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHColour_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHColour_Primary.htm)|
Converts similar data into a GH_Colour instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHColour_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHColour_Secondary.htm)|
Converts similar data into a GH_Colour instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHComplexNumber](M_Grasshopper_Kernel_GH_Convert_ToGHComplexNumber.htm)|
Convert data into GH_ComplexNumber.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHComplexNumber_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHComplexNumber_Primary.htm)|
Converts similar data into a GH_ComplexNumber instance. Data is not quaranteed
to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHComplexNumber_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHComplexNumber_Secondary.htm)|
Converts similar data into a GH_ComplexNumber instance. Data is not quaranteed
to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHCurve](M_Grasshopper_Kernel_GH_Convert_ToGHCurve.htm)|  Convert data into
GH_Curves.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHCurve_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHCurve_Primary.htm)|
Converts similar data into a GH_Curve instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHCurve_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHCurve_Secondary.htm)|
Converts similar data into a GH_Curve instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHDimension](M_Grasshopper_Kernel_GH_Convert_ToGHDimension.htm)|  Convert
data into GH_Dimension.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHExtrusion](M_Grasshopper_Kernel_GH_Convert_ToGHExtrusion.htm)|  Convert
data into GH_Extrusion.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHExtrusion_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHExtrusion_Primary.htm)|
Converts similar data into a GH_Extrusion instance. Data is not quaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHExtrusion_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHExtrusion_Secondary.htm)|
Converts similar data into a GH_Brep instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHGuid](M_Grasshopper_Kernel_GH_Convert_ToGHGuid.htm)|  Convert data into
GH_Guid.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHGuid_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHGuid_Primary.htm)|
Converts similar data into a GH_Guid instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHGuid_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHGuid_Secondary.htm)|
Converts similar data into a GH_Guid instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHHatch](M_Grasshopper_Kernel_GH_Convert_ToGHHatch.htm)|  Convert data into
GH_Hatch.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHHatch_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHHatch_Primary.htm)|
Converts similar data into a GH_Hatch instance. Data is not guaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHHatch_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHHatch_Secondary.htm)|
Converts similar data into a GH_Hatch instance. Data is not guaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHInstanceReference](M_Grasshopper_Kernel_GH_Convert_ToGHInstanceReference.htm)|
Convert data into GH_InstanceReference.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHInstanceReference_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHInstanceReference_Primary.htm)|
Converts similar data into a GH_InstanceReference instance. Data is not
guaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHInstanceReference_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHInstanceReference_Secondary.htm)|
Converts similar data into a GH_InstanceReference instance. Data is not
guaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHInteger](M_Grasshopper_Kernel_GH_Convert_ToGHInteger.htm)|  Convert data
into GH_Integer.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHInteger_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHInteger_Primary.htm)|
Converts similar data into a GH_Integer instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHInteger_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHInteger_Secondary.htm)|
Converts similar data into a GH_Integer instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHInterval](M_Grasshopper_Kernel_GH_Convert_ToGHInterval.htm)|  Convert
data into GH_Intervals.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHInterval_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHInterval_Primary.htm)|
Converts similar data into a GH_Interval instance. Data is not quaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHInterval_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHInterval_Secondary.htm)|
Converts similar data into a GH_Interval instance. Data is not quaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHInterval2D](M_Grasshopper_Kernel_GH_Convert_ToGHInterval2D.htm)|  Convert
data into GH_Interval2Ds.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHInterval2D_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHInterval2D_Primary.htm)|
Converts similar data into a GH_Interval2D instance. Data is not quaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHInterval2D_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHInterval2D_Secondary.htm)|
Converts similar data into a GH_Interval2D instance. Data is not quaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHLeader](M_Grasshopper_Kernel_GH_Convert_ToGHLeader.htm)|  Convert data
into GH_Leader.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHLeader_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHLeader_Primary.htm)|
Converts similar data into a GH_Leader instance. Data is not guaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHLeader_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHLeader_Secondary.htm)|
Converts similar data into a GH_Leader instance. Data is not guaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHLight](M_Grasshopper_Kernel_GH_Convert_ToGHLight.htm)|  Convert data into
GH_Light.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHLight_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHLight_Primary.htm)|
Converts similar data into a GH_Light instance. Data is not guaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHLight_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHLight_Secondary.htm)|
Converts similar data into a GH_Light instance. Data is not guaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHLine](M_Grasshopper_Kernel_GH_Convert_ToGHLine.htm)|  Convert data into
GH_Lines.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHLine_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHLine_Primary.htm)|
Converts similar data into a GH_Line instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHLine_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHLine_Secondary.htm)|
Converts similar data into a GH_Line instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHLinearDimension](M_Grasshopper_Kernel_GH_Convert_ToGHLinearDimension.htm)|
Convert data into GH_LinearDimension.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHLinearDimension_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHLinearDimension_Primary.htm)|
Converts similar data into a GH_LinearDimension instance. Data is not
guaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHLinearDimension_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHLinearDimension_Secondary.htm)|
Converts similar data into a GH_LinearDimension instance. Data is not
guaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHMatrix](M_Grasshopper_Kernel_GH_Convert_ToGHMatrix.htm)|  Convert data
into ToGHMatrix.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHMatrix_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHMatrix_Primary.htm)|
Converts similar data into a GH_Matrix instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHMatrix_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHMatrix_Secondary.htm)|
Converts similar data into a GH_Matrix instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHMesh](M_Grasshopper_Kernel_GH_Convert_ToGHMesh.htm)|  Convert data into
GH_Meshs.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHMesh_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHMesh_Primary.htm)|
Converts similar data into a GH_Mesh instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHMesh_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHMesh_Secondary.htm)|
Converts similar data into a GH_Mesh instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHMeshFace](M_Grasshopper_Kernel_GH_Convert_ToGHMeshFace.htm)|  Convert
data into GH_MeshFaces.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHMeshFace_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHMeshFace_Primary.htm)|
Converts similar data into a GH_MeshFace instance. Data is not quaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHMeshFace_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHMeshFace_Secondary.htm)|
Converts similar data into a GH_MeshFace instance. Data is not quaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHNumber](M_Grasshopper_Kernel_GH_Convert_ToGHNumber.htm)|  Convert data
into GH_Number.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHNumber_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHNumber_Primary.htm)|
Converts similar data into a GH_Number instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHNumber_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHNumber_Secondary.htm)|
Converts similar data into a GH_Number instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHOrdinateDimension](M_Grasshopper_Kernel_GH_Convert_ToGHOrdinateDimension.htm)|
Convert data into GH_OrdinateDimension.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHOrdinateDimension_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHOrdinateDimension_Primary.htm)|
Converts similar data into a GH_OrdinateDimension instance. Data is not
guaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHOrdinateDimension_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHOrdinateDimension_Secondary.htm)|
Converts similar data into a GH_OrdinateDimension instance. Data is not
guaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHPlane](M_Grasshopper_Kernel_GH_Convert_ToGHPlane.htm)|  Convert data into
GH_Planes.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHPlane_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHPlane_Primary.htm)|
Converts similar data into a GH_Plane instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHPlane_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHPlane_Secondary.htm)|
Converts similar data into a GH_Plane instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHPoint](M_Grasshopper_Kernel_GH_Convert_ToGHPoint.htm)|  Convert data into
GH_Points.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHPoint_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHPoint_Primary.htm)|
Converts similar data into a GH_Point instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHPoint_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHPoint_Secondary.htm)|
Converts similar data into a GH_Point instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHPointCloud](M_Grasshopper_Kernel_GH_Convert_ToGHPointCloud.htm)|  Convert
data into GH_PointCloud.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHPointCloud_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHPointCloud_Primary.htm)|
Converts similar data into a GH_PointCloud instance. Data is not quaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHPointCloud_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHPointCloud_Secondary.htm)|
Converts similar data into a GH_PointCloud instance. Data is not quaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHRadialDimension](M_Grasshopper_Kernel_GH_Convert_ToGHRadialDimension.htm)|
Convert data into GH_RadialDimension.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHRadialDimension_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHRadialDimension_Primary.htm)|
Converts similar data into a GH_RadialDimension instance. Data is not
guaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHRadialDimension_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHRadialDimension_Secondary.htm)|
Converts similar data into a GH_RadialDimension instance. Data is not
guaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHRectangle](M_Grasshopper_Kernel_GH_Convert_ToGHRectangle.htm)|  Convert
data into GH_Rectangles.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHRectangle_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHRectangle_Primary.htm)|
Converts similar data into a GH_Rectangle instance. Data is not quaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHRectangle_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHRectangle_Secondary.htm)|
Converts similar data into a GH_Rectangle instance. Data is not quaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHString](M_Grasshopper_Kernel_GH_Convert_ToGHString.htm)|  Convert data
into GH_String.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHString_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHString_Primary.htm)|
Converts similar data into a GH_String instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHString_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHString_Secondary.htm)|
Converts similar data into a GH_String instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHSubD](M_Grasshopper_Kernel_GH_Convert_ToGHSubD.htm)|  Convert data into
GH_SubDs.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHSubD_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHSubD_Primary.htm)|
Converts similar data into a GH_SubD instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHSubD_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHSubD_Secondary.htm)|
Converts similar data into a GH_SubD instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHSurface](M_Grasshopper_Kernel_GH_Convert_ToGHSurface.htm)|  Convert data
into GH_Surfaces.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHSurface_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHSurface_Primary.htm)|
Converts similar data into a GH_Surface instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHSurface_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHSurface_Secondary.htm)|
Converts similar data into a GH_Surface instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHTextDot](M_Grasshopper_Kernel_GH_Convert_ToGHTextDot.htm)|  Convert data
into GH_TextDot.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHTextDot_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHTextDot_Primary.htm)|
Converts similar data into a GH_TextDot instance. Data is not guaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHTextDot_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHTextDot_Secondary.htm)|
Converts similar data into a GH_TextDot instance. Data is not guaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHTextEntity](M_Grasshopper_Kernel_GH_Convert_ToGHTextEntity.htm)|  Convert
data into GH_TextEntity.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHTextEntity_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHTextEntity_Primary.htm)|
Converts similar data into a GH_TextEntity instance. Data is not guaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHTextEntity_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHTextEntity_Secondary.htm)|
Converts similar data into a GH_TextEntity instance. Data is not guaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHTime](M_Grasshopper_Kernel_GH_Convert_ToGHTime.htm)|  Convert data into
GH_Time.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHTime_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHTime_Primary.htm)|
Converts similar data into a GH_Time instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHTime_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHTime_Secondary.htm)|
Converts similar data into a GH_Time instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHVector](M_Grasshopper_Kernel_GH_Convert_ToGHVector.htm)|  Convert data
into GH_Vectors.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHVector_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHVector_Primary.htm)|
Converts similar data into a GH_Vector instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGHVector_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHVector_Secondary.htm)|
Converts similar data into a GH_Vector instance. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGoo](M_Grasshopper_Kernel_GH_Convert_ToGoo.htm)|  Converts an object into
Goo. Does not duplicate the data if a lossless conversion is possible.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGUID](M_Grasshopper_Kernel_GH_Convert_ToGUID.htm)|  Convert data into
Guids.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGUID_Primary](M_Grasshopper_Kernel_GH_Convert_ToGUID_Primary.htm)|
Performs a direct cast from Guid, GH_Guid, String and GH_String.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToGUID_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGUID_Secondary.htm)|
Performs indirect casts from other data types into Guids.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToHatch](M_Grasshopper_Kernel_GH_Convert_ToHatch.htm)|  Convert data into
Rhino.Geometry.Hatch.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToHatch_Primary](M_Grasshopper_Kernel_GH_Convert_ToHatch_Primary.htm)|
Performs a direct cast from Rhino.Geometry.Hatch or GH_Hatch. Data is not
guaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToHatch_Secondary](M_Grasshopper_Kernel_GH_Convert_ToHatch_Secondary.htm)|
Attempts to convert other data types into an Rhino.Geometry.Hatch. Data is not
quaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToInt32](M_Grasshopper_Kernel_GH_Convert_ToInt32.htm)|  Convert data into
Int32s.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToInt32_Primary](M_Grasshopper_Kernel_GH_Convert_ToInt32_Primary.htm)|
Performs a direct cast from Int32 or GH_Integer.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToInt32_Secondary](M_Grasshopper_Kernel_GH_Convert_ToInt32_Secondary.htm)|
Performs indirect casts from other data types into Integers.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToInterval](M_Grasshopper_Kernel_GH_Convert_ToInterval.htm)|  Convert data
into Rhino.Geometry.Interval.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToInterval_Primary](M_Grasshopper_Kernel_GH_Convert_ToInterval_Primary.htm)|
Performs a direct cast from OnInterval or GH_Interval.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToInterval_Secondary](M_Grasshopper_Kernel_GH_Convert_ToInterval_Secondary.htm)|
Attempts to convert other data types into an Interval. Data is not quaranteed
to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToLeader](M_Grasshopper_Kernel_GH_Convert_ToLeader.htm)|  Convert data into
Rhino.Geometry.Leader.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToLeader_Primary](M_Grasshopper_Kernel_GH_Convert_ToLeader_Primary.htm)|
Performs a direct cast from Rhino.Geometry.Leader or GH_Leader. Data is not
guaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToLeader_Secondary](M_Grasshopper_Kernel_GH_Convert_ToLeader_Secondary.htm)|
Attempts to convert other data types into an Rhino.Geometry.Leader. Data is
not quaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToLight_Secondary](M_Grasshopper_Kernel_GH_Convert_ToLight_Secondary.htm)|
Attempts to convert other data types into an Rhino.Geometry.Light. Data is not
quaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToLine](M_Grasshopper_Kernel_GH_Convert_ToLine.htm)|  Convert data into
Rhino.Geometry.Line.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToLine_Primary](M_Grasshopper_Kernel_GH_Convert_ToLine_Primary.htm)|
Performs a direct cast from OnLine or GH_Line. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToLine_Secondary](M_Grasshopper_Kernel_GH_Convert_ToLine_Secondary.htm)|
Attempts to convert other data types into an OnLine. Data is not quaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToMatrix](M_Grasshopper_Kernel_GH_Convert_ToMatrix.htm)|  Convert data into
Rhino.Geometry.Matrix.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToMatrix_Primary](M_Grasshopper_Kernel_GH_Convert_ToMatrix_Primary.htm)|
Performs a direct cast from Matrix or GH_Matrix.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToMatrix_Secondary](M_Grasshopper_Kernel_GH_Convert_ToMatrix_Secondary.htm)|
Attempts to convert other data types into a Matrix. Data is not quaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToMesh](M_Grasshopper_Kernel_GH_Convert_ToMesh.htm)|  Convert data into
Rhino.Geometry.Mesh.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToMesh_Primary](M_Grasshopper_Kernel_GH_Convert_ToMesh_Primary.htm)|
Performs a direct cast from Rhino.Geometry.Mesh or GH_Mesh. Data is not
guaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToMesh_Secondary](M_Grasshopper_Kernel_GH_Convert_ToMesh_Secondary.htm)|
Attempts to convert other data types into an OnMesh. Data is not quaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToNextPowerOfTen](M_Grasshopper_Kernel_GH_Convert_ToNextPowerOfTen.htm)|
Round a number upwards to the nearest power of ten.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToPlane](M_Grasshopper_Kernel_GH_Convert_ToPlane.htm)|  Convert data into
Rhino.Geometry.Plane.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToPlane_Primary](M_Grasshopper_Kernel_GH_Convert_ToPlane_Primary.htm)|
Performs a direct cast from OnPlane or GH_Plane. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToPlane_Secondary](M_Grasshopper_Kernel_GH_Convert_ToPlane_Secondary.htm)|
Attempts to convert other data types into an OnPlane. Data is not quaranteed
to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToPlural](M_Grasshopper_Kernel_GH_Convert_ToPlural.htm)|  Apply english rules
to convert a noun into its plural form. This algorithm is not water-tight as
it will not handle any irregular cases.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToPoint](M_Grasshopper_Kernel_GH_Convert_ToPoint.htm)|  Convert a floating
point GDI point structure to an integer rounded point.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToPoint3d](M_Grasshopper_Kernel_GH_Convert_ToPoint3d.htm)|  Convert data into
Rhino.Geometry.Point3d.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToPoint3d_Primary](M_Grasshopper_Kernel_GH_Convert_ToPoint3d_Primary.htm)|
Performs a direct cast from On3dPoint or GH_Point. Data is not quaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToPoint3d_Secondary](M_Grasshopper_Kernel_GH_Convert_ToPoint3d_Secondary.htm)|
Attempts to convert other data types into an Point. Data is not quaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToPointCloud](M_Grasshopper_Kernel_GH_Convert_ToPointCloud.htm)|  Convert
data into Rhino.Geometry.PointCloud.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToPointCloud_Primary](M_Grasshopper_Kernel_GH_Convert_ToPointCloud_Primary.htm)|
Performs a direct cast from Rhino.Geometry.PointCloud or GH_PointCloud. Data
is not guaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToPointCloud_Secondary](M_Grasshopper_Kernel_GH_Convert_ToPointCloud_Secondary.htm)|
Attempts to convert other data types into an Rhino.Geometry.PointCloud. Data
is not quaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToPointF](M_Grasshopper_Kernel_GH_Convert_ToPointF.htm)|  Convert a Rhino SDK
point structure to a GDI point structure.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToPrevPowerOfTen](M_Grasshopper_Kernel_GH_Convert_ToPrevPowerOfTen.htm)|
Round a number downwards to the nearest power of ten.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToRectangle](M_Grasshopper_Kernel_GH_Convert_ToRectangle.htm)|  Convert a
floating point GDI rectangle structure to an integer rounded rectangle. Use
this method for any and all GUI conversions as the specific rounding scheme
used here avoids pixel jitter.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToRectangle3d](M_Grasshopper_Kernel_GH_Convert_ToRectangle3d.htm)|  Convert
data into Rhino.Geometry.Line.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToRectangle3d_Primary](M_Grasshopper_Kernel_GH_Convert_ToRectangle3d_Primary.htm)|
Performs a direct cast from Rectangle3d or GH_Rectangle. Data is not
quaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToRectangle3d_Secondary](M_Grasshopper_Kernel_GH_Convert_ToRectangle3d_Secondary.htm)|
Attempts to convert other data types into a Rectangle3d. Data is not
quaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToRelativePath](M_Grasshopper_Kernel_GH_Convert_ToRelativePath.htm)|
**Obsolete.** Create a relative path from two absolute paths.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToSafeRhinoCommonObject](M_Grasshopper_Kernel_GH_Convert_ToSafeRhinoCommonObject.htm)|
Convert RhinoCommon types that are dangerous to use out of context (BrepFace,
BrepEdge, etc.) into safe types (Brep, Curve, etc.).  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToSHA_Hash(Byte)](M_Grasshopper_Kernel_GH_Convert_ToSHA_Hash.htm)|  Create a
SHA hash. The hash algorithm is only guaranteed to yield the same results from
within a unique application domain.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToSHA_Hash(Stream)](M_Grasshopper_Kernel_GH_Convert_ToSHA_Hash_1.htm)|
Create a SHA hash. The hash algorithm is only guaranteed to yield the same
results from within a unique application domain.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToSize](M_Grasshopper_Kernel_GH_Convert_ToSize.htm)|  Convert a floating
point GDI size structure to an integer rounded size.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToString](M_Grasshopper_Kernel_GH_Convert_ToString.htm)|  Convert data into
Colors.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToString_Primary](M_Grasshopper_Kernel_GH_Convert_ToString_Primary.htm)|
Performs a direct cast from String and GH_String.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToString_Secondary](M_Grasshopper_Kernel_GH_Convert_ToString_Secondary.htm)|
Creates a String representation of an object by calling the ToString()
function.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToSubD](M_Grasshopper_Kernel_GH_Convert_ToSubD.htm)|  Convert data into
Rhino.Geometry.SubD.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToSubD_Primary](M_Grasshopper_Kernel_GH_Convert_ToSubD_Primary.htm)|
Performs a direct cast from OnSubD or GH_SubD. Data is not quaranteed to be
duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToSubD_Secondary](M_Grasshopper_Kernel_GH_Convert_ToSubD_Secondary.htm)|
Attempts to convert other data types into a Sub-D. Data is not quaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToSurface](M_Grasshopper_Kernel_GH_Convert_ToSurface.htm)|  Convert data into
Rhino.Geometry.Surface.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToSurface_Primary](M_Grasshopper_Kernel_GH_Convert_ToSurface_Primary.htm)|
Performs a direct cast from OnSurface or GH_Surface. Data is not quaranteed to
be duplicated. If data is of type GH_Surface, then trim curves are ignored.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToSurface_Secondary](M_Grasshopper_Kernel_GH_Convert_ToSurface_Secondary.htm)|
Attempts to convert other data types into an IOnSurface. Data is not
quaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToTextDot](M_Grasshopper_Kernel_GH_Convert_ToTextDot.htm)|  Convert data into
Rhino.Geometry.TextDot.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToTextDot_Primary](M_Grasshopper_Kernel_GH_Convert_ToTextDot_Primary.htm)|
Performs a direct cast from Rhino.Geometry.TextDot or GH_TextDot. Data is not
guaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToTextDot_Secondary](M_Grasshopper_Kernel_GH_Convert_ToTextDot_Secondary.htm)|
Attempts to convert other data types into an Rhino.Geometry.TextDot. Data is
not quaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToTextEntity](M_Grasshopper_Kernel_GH_Convert_ToTextEntity.htm)|  Convert
data into Rhino.Geometry.TextEntity.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToTextEntity_Primary](M_Grasshopper_Kernel_GH_Convert_ToTextEntity_Primary.htm)|
Performs a direct cast from Rhino.Geometry.TextEntity or GH_TextEntity. Data
is not guaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToTextEntity_Secondary](M_Grasshopper_Kernel_GH_Convert_ToTextEntity_Secondary.htm)|
Attempts to convert other data types into an Rhino.Geometry.TextEntity. Data
is not quaranteed to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToUVInterval](M_Grasshopper_Kernel_GH_Convert_ToUVInterval.htm)|  Convert
data into Grasshopper.Kernel.Types.UVInterval.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToUVInterval_Primary](M_Grasshopper_Kernel_GH_Convert_ToUVInterval_Primary.htm)|
Performs a direct cast from UVInterval or GH_Interval2D.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToUVInterval_Secondary](M_Grasshopper_Kernel_GH_Convert_ToUVInterval_Secondary.htm)|
Attempts to convert other data types into a UVInterval. Data is not quaranteed
to be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToVariableName](M_Grasshopper_Kernel_GH_Convert_ToVariableName.htm)|  Extract
the implied variable name from a compound string. A string is considered
compound if it contains a parenthesis pair with at least one character within
the brackets.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToVariant](M_Grasshopper_Kernel_GH_Convert_ToVariant.htm)|  Convert an object
to a Grasshopper Expression Variant if possible.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToVector3d](M_Grasshopper_Kernel_GH_Convert_ToVector3d.htm)|  Convert data
into Rhino.Geometry.Vector3d.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToVector3d_Primary](M_Grasshopper_Kernel_GH_Convert_ToVector3d_Primary.htm)|
Performs a direct cast from On3dVector or GH_Vector. Data is not quaranteed to
be duplicated.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ToVector3d_Secondary](M_Grasshopper_Kernel_GH_Convert_ToVector3d_Secondary.htm)|
Attempts to convert other data types into a Vector. Data is not quaranteed to
be duplicated.  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[PureDateTicks](F_Grasshopper_Kernel_GH_Convert_PureDateTicks.htm)|
Represents the total number of ticks past midnight that (by Grasshopper
convention) identifies a pure date.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[PureTimeTicks](F_Grasshopper_Kernel_GH_Convert_PureTimeTicks.htm)|
Represents the total number of ticks past a whole second that (by Grasshopper
convention) identifies a pure time.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

