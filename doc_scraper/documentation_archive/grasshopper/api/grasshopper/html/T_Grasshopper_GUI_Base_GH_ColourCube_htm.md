---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Base_GH_ColourCube.htm
scraped_at: 2025-09-08T16:13:31.556499
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Base](../html/N_Grasshopper_GUI_Base.htm
"Grasshopper.GUI.Base")

[GH_ColourCube Class](../html/T_Grasshopper_GUI_Base_GH_ColourCube.htm
"GH_ColourCube Class")

[GH_ColourCube Constructor
](../html/M_Grasshopper_GUI_Base_GH_ColourCube__ctor.htm "GH_ColourCube
Constructor ")

[GH_ColourCube
Properties](../html/Properties_T_Grasshopper_GUI_Base_GH_ColourCube.htm
"GH_ColourCube Properties")

[GH_ColourCube
Methods](../html/Methods_T_Grasshopper_GUI_Base_GH_ColourCube.htm
"GH_ColourCube Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_ColourCube Class  
  
---  
  
Maintains a collection of graphical shapes and coordinates that specify
important features of the Colour Space Cube graphics.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.GUI.BaseGH_ColourCube  

**Namespace:** [Grasshopper.GUI.Base](N_Grasshopper_GUI_Base.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_ColourCube
    
    
    Public Class GH_ColourCube

The GH_ColourCube type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_ColourCube](M_Grasshopper_GUI_Base_GH_ColourCube__ctor.htm)|  Create a new
instance of this class.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[BackFace](P_Grasshopper_GUI_Base_GH_ColourCube_BackFace.htm)|  Gets a
graphics path describing the back face of the cube. Caller is responsible for
disposing of this path instance.  
![Public property](../icons/pubproperty.gif)|
[BottomFace](P_Grasshopper_GUI_Base_GH_ColourCube_BottomFace.htm)|  Gets a
graphics path describing the bottom face of the cube. Caller is responsible
for disposing of this path instance.  
![Public property](../icons/pubproperty.gif)|
[C0](P_Grasshopper_GUI_Base_GH_ColourCube_C0.htm)|  Gets the first point in
the corner point list.  
![Public property](../icons/pubproperty.gif)|
[C1](P_Grasshopper_GUI_Base_GH_ColourCube_C1.htm)|  Gets the second point in
the corner point list.  
![Public property](../icons/pubproperty.gif)|
[C2](P_Grasshopper_GUI_Base_GH_ColourCube_C2.htm)|  Gets the third point in
the corner point list.  
![Public property](../icons/pubproperty.gif)|
[C3](P_Grasshopper_GUI_Base_GH_ColourCube_C3.htm)|  Gets the fourth point in
the corner point list.  
![Public property](../icons/pubproperty.gif)|
[C4](P_Grasshopper_GUI_Base_GH_ColourCube_C4.htm)|  Gets the fifth point in
the corner point list.  
![Public property](../icons/pubproperty.gif)|
[C5](P_Grasshopper_GUI_Base_GH_ColourCube_C5.htm)|  Gets the sixth point in
the corner point list.  
![Public property](../icons/pubproperty.gif)|
[C6](P_Grasshopper_GUI_Base_GH_ColourCube_C6.htm)|  Gets the seventh point in
the corner point list.  
![Public property](../icons/pubproperty.gif)|
[C7](P_Grasshopper_GUI_Base_GH_ColourCube_C7.htm)|  Gets the eighth point in
the corner point list.  
![Public property](../icons/pubproperty.gif)|
[Grip](P_Grasshopper_GUI_Base_GH_ColourCube_Grip.htm)|  Gets the rectangle
that describes the slice grip.  
![Public property](../icons/pubproperty.gif)|
[LeftFace](P_Grasshopper_GUI_Base_GH_ColourCube_LeftFace.htm)|  Gets a
graphics path describing the left face of the cube. Caller is responsible for
disposing of this path instance.  
![Public property](../icons/pubproperty.gif)|
[Pivot](P_Grasshopper_GUI_Base_GH_ColourCube_Pivot.htm)|  Gets the point that
describes the center of the pivot on the slice.  
![Public property](../icons/pubproperty.gif)|
[S0](P_Grasshopper_GUI_Base_GH_ColourCube_S0.htm)|  Gets the first point in
the shadow point list. This point is coincident with C0.  
![Public property](../icons/pubproperty.gif)|
[S1](P_Grasshopper_GUI_Base_GH_ColourCube_S1.htm)|  Gets the second point in
the shadow point list. This is the corner of the drop-shadow on the bottom
face.  
![Public property](../icons/pubproperty.gif)|
[S2](P_Grasshopper_GUI_Base_GH_ColourCube_S2.htm)|  Gets the third point in
the shadow point list. This point is the kink of the drop-shadow on the edge
connecting C2 and C3.  
![Public property](../icons/pubproperty.gif)|
[S3](P_Grasshopper_GUI_Base_GH_ColourCube_S3.htm)|  Gets the fourth point in
the shadow point list. This point is coincident with C7.  
![Public property](../icons/pubproperty.gif)|
[S4](P_Grasshopper_GUI_Base_GH_ColourCube_S4.htm)|  Gets the fifth point in
the shadow point list. This point is coincident with C4.  
![Public property](../icons/pubproperty.gif)|
[Shadow](P_Grasshopper_GUI_Base_GH_ColourCube_Shadow.htm)|  Gets a graphics
path describing the outline of the drop shadow. Caller is responsible for
disposing of this path instance.  
![Public property](../icons/pubproperty.gif)|
[Silhouette](P_Grasshopper_GUI_Base_GH_ColourCube_Silhouette.htm)|  Gets a
graphics path describing the silhouette of the cube. Caller is responsible for
disposing of this path instance.  
![Public property](../icons/pubproperty.gif)|
[Slice](P_Grasshopper_GUI_Base_GH_ColourCube_Slice.htm)|  Gets the rectangle
that describes the cutting slide through the current colour space.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)| [Average(Color,
Color)](M_Grasshopper_GUI_Base_GH_ColourCube_Average.htm)|  Compute the
average of two colours.  
![Public method](../icons/pubmethod.gif)| [Average(Color, Color, Color,
Color)](M_Grasshopper_GUI_Base_GH_ColourCube_Average_1.htm)|  Compute the
average of four colours.  
![Public method](../icons/pubmethod.gif)|
[Blend](M_Grasshopper_GUI_Base_GH_ColourCube_Blend.htm)|  Inteprolate between
two colours.  
![Public method](../icons/pubmethod.gif)|
[ColorAtRail](M_Grasshopper_GUI_Base_GH_ColourCube_ColorAtRail.htm)|  Get the
color at a position along the depth rail.  
![Public method](../icons/pubmethod.gif)|
[ColorAtSlice](M_Grasshopper_GUI_Base_GH_ColourCube_ColorAtSlice.htm)|  Get
the color at a position on the slice.  
![Public method](../icons/pubmethod.gif)|
[RenderAll](M_Grasshopper_GUI_Base_GH_ColourCube_RenderAll.htm)|  Call all
render methods in the correct order.  
![Public method](../icons/pubmethod.gif)|
[RenderBackEdges](M_Grasshopper_GUI_Base_GH_ColourCube_RenderBackEdges.htm)|
Render the edges of the back face creases.  
![Public method](../icons/pubmethod.gif)|
[RenderBackFaces](M_Grasshopper_GUI_Base_GH_ColourCube_RenderBackFaces.htm)|
Render the fills of the backfaces.  
![Public method](../icons/pubmethod.gif)|
[RenderDropShadow](M_Grasshopper_GUI_Base_GH_ColourCube_RenderDropShadow.htm)|
Render the drop shadow of the cube.  
![Public method](../icons/pubmethod.gif)|
[RenderEdgeShadows](M_Grasshopper_GUI_Base_GH_ColourCube_RenderEdgeShadows.htm)|
Render the edge shadows of the cube due to GI.  
![Public method](../icons/pubmethod.gif)|
[RenderForeEdges](M_Grasshopper_GUI_Base_GH_ColourCube_RenderForeEdges.htm)|
Render the edges of the fore face creases.  
![Public method](../icons/pubmethod.gif)|
[RenderGrip](M_Grasshopper_GUI_Base_GH_ColourCube_RenderGrip.htm)|  Render the
slice grip.  
![Public method](../icons/pubmethod.gif)|
[RenderPivot](M_Grasshopper_GUI_Base_GH_ColourCube_RenderPivot.htm)|  Render
the colour pivot on the current slice.  
![Public method](../icons/pubmethod.gif)|
[RenderSilhouetteEdges](M_Grasshopper_GUI_Base_GH_ColourCube_RenderSilhouetteEdges.htm)|
Render the edges of the cube silhouettes.  
![Public method](../icons/pubmethod.gif)|
[RenderSlice](M_Grasshopper_GUI_Base_GH_ColourCube_RenderSlice.htm)|  Render
the square slice with colour gradients.  
![Public method](../icons/pubmethod.gif)|
[RenderSliceDropShadow](M_Grasshopper_GUI_Base_GH_ColourCube_RenderSliceDropShadow.htm)|
Render the drop shadow onto the slice.  
![Public method](../icons/pubmethod.gif)|
[RenderSliceEdgeShadows](M_Grasshopper_GUI_Base_GH_ColourCube_RenderSliceEdgeShadows.htm)|
Render the edge shadows of the slice due to GI.  
![Public method](../icons/pubmethod.gif)|
[RenderSliceSilhouetteEdges](M_Grasshopper_GUI_Base_GH_ColourCube_RenderSliceSilhouetteEdges.htm)|
Render the silhouette edges of the slice.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Base Namespace](N_Grasshopper_GUI_Base.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

