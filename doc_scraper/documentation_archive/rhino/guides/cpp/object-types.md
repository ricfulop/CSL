---
url: https://developer.rhino3d.com/guides/cpp/object-types/
scraped_at: 2025-09-08T15:39:28.565561
title: Untitled
---

[RhinoDeveloper®](/)

[design, model, present, analyze, realize...](/)

[![Rhino Logo](https://developer.rhino3d.com/images/rhinodevlogo.png)](/)

__

[Guides](https://developer.rhino3d.com/guides)
[Samples](https://developer.rhino3d.com/samples)
[API](https://developer.rhino3d.com/api)
[Videos](https://developer.rhino3d.com/videos)
[Community](https://discourse.mcneel.com/c/rhino-developer) [my account
](https://www.rhino3d.com/my-account/ "Manage your account, licenses, and
teams")

[Object Types](https://developer.rhino3d.com/guides/cpp/object-types/)

  * Overview

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Object Types

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

`CRhinoObject` is the base class for all runtime Rhino geometric objects.
`ON_Geometry` is the base class for all geometry class. All `CRhinoObject`
derived object maintain a `ON_Geometry` derived class as a data member.

The following is an inventory of the geometric objects you are most likely to
encounter in Rhino:

  * `CRhinoAnnotationObject` \- Virtual base class for annotation objects. 
    * `ON_Annotation2`
  * `CRhinoAngularDimension` \- Angular dimension. 
    * `ON_AngularDimension2`
  * `CRhinoAnnotationLeader` \- Annotation leader. 
    * `ON_Leader2`
  * `CRhinoLinearDimension` \- Linear dimension. 
    * `ON_LinearDimension2`
  * `CRhinoOrdinateDimension` \- Ordinate dimension. 
    * `ON_OrdinateDimension2`
  * `CRhinoRadialDimension` \- Radial dimension. 
    * `ON_RadialDimension2`
  * `CRhinoAnnotationText` \- Annotation text. 
    * `ON_TextEntity2`
  * `CRhinoBrepObject` \- Surface or polysurface. 
    * `ON_Brep`
  * `CRhinoClippingPlaneObject` \- Clipping plane. 
    * `ON_ClippingPlane`
  * `CRhinoCurveObject` \- Curve.
  * `ON_Curve` \- Virtual base class for curve objects. 
    * `ON_ArcCurve`
    * `ON_CurveOnSurface`
    * `ON_CurveProxy`
    * `ON_LineCurve`
    * `ON_NurbsCurve`
    * `ON_PolyCurve`
    * `ON_PolylineCurve`
  * `CRhinoDetailViewObject` \- Detail view. 
    * `ON_DetailView`
  * `CRhinoExtrusionObject` \- Lightweight extrusion 
    * `ON_Extrusion`
  * `CRhinoGripObject` \- Grip object. Note grip objects are not stored in the document. 
    * `ON_Point`
  * `CRhinoHatch` \- Area hatching. 
    * `ON_Hatch`
  * `CRhinoInstanceObject` \- Block instance. 
    * `ON_InstanceRef`
  * `CRhinoLight` \- Rendering light. 
    * `ON_Light`
  * `CRhinoMeshObject` \- Polygon mesh. 
    * `ON_Mesh`
  * `CRhinoPointCloudObject` \- Point cloud. 
    * `ON_PointCloud`
  * `CRhinoPointObject` \- Point. 
    * `ON_Point`
  * `CRhinoSurfaceObject` \- Untrimmed surface. 
    * `ON_Surface`
    * `ON_NurbsSurface`
    * `ON_PlaneSurface`
    * `ON_RevSurface`
    * `ON_SumSurface`
  * `CRhinoTextDot` \- Text dot. 
    * `ON_TextDot`

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/object-
types/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/object-
types/index.md) [ Admin](https://developer.rhino3d.com/admin)

[Find a Reseller](https://www.rhino3d.com/sales)

[Shop online](https://www.rhino3d.com/store) or find a
[Reseller](https://www.rhino3d.com/sales)

[Find a Reseller](https://www.rhino3d.com/sales)

[Privacy Policy](https://www.rhino3d.com/privacy) •
[About](https://www.rhino3d.com/mcneel/about) • [Contact
Us](https://www.rhino3d.com/mcneel/contact) • [
Language](https://www.rhino3d.com/language "Change to a different region or
language")

[Copyright © 1993-2025 Robert McNeel & Associates. All Rights
Reserved.](https://www.rhino3d.com/mcneel/about)

[](https://www.facebook.com/McNeelRhinoceros/)
[](https://twitter.com/bobmcneel) [](https://www.linkedin.com/groups/75313/)
[](https://www.youtube.com/user/RhinoGuide/videos) [](https://vimeo.com/rhino)
[![Blogger
icon](https://developer.rhino3d.com/images/blogger.svg)](http://blog.rhino3d.com/)
[![Food4Rhino](https://developer.rhino3d.com/images/f4r_icon_01.svg)](https://www.food4rhino.com)

