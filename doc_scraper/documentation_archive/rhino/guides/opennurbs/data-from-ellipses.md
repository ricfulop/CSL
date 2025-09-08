---
url: https://developer.rhino3d.com/guides/opennurbs/data-from-ellipses/
scraped_at: 2025-09-08T15:38:20.279570
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

[Data from Ellipses](https://developer.rhino3d.com/guides/opennurbs/data-from-
ellipses/)

  * Problem
  * Solution
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [openNURBS and rhino3dm
Guides](https://developer.rhino3d.com/en/guides/opennurbs/) /

Data from Ellipses

by [Dale Lear](https://discourse.mcneel.com/u/dalelear/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You have drawn an ellipse in Rhino, using the _Ellipse_ command. While reading
the _.3dm_ file, using openNURBS, the ellipse is classified as as
`ON::curve_object`. How does one get the ellipse’s construction data, such as
center point, major and minor axes, etc?

## Solution

Unlike some curve types (e.g. Lines, Arcs, Polylines, etc.) which have their
own `ON_Curve`-derived classes, there is no special class that is used to
represent elliptical curves. Ellipses and elliptical arcs are simply NURBS, or
`ON_NurbsCurve`, curves.

To test to see if a curve is an ellipse or an elliptical arc, first try to
cast the `ON_Curve` object as an `ON_NurbsCurve` object. If successful, then
use `ON_NurbsCurve::IsEllipse()` to verify the NURBS curve is an ellipse and
to obtain its construction data.

## Sample

    
    
    ONX_Model model = ...
    
    ONX_ModelComponentIterator it(model, ON_ModelComponent::Type::ModelGeometry);
    const ON_ModelComponent* model_component = nullptr;
    for (model_component = it.FirstComponent(); nullptr != model_component; model_component = it.NextComponent())
    {
      const ON_ModelGeometryComponent* model_geometry = ON_ModelGeometryComponent::Cast(model_component);
      if (nullptr != model_geometry)
      {
        // Test for NURBS curve object
        const ON_NurbsCurve* nurb = ON_NurbsCurve::Cast(model_geometry->Geometry(nullptr));
        if (nullptr != nurb)
        {
          ON_Ellipse ellipse;
          double tolerance = model.m_settings.m_ModelUnitsAndTolerances.m_absolute_tolerance;
          bool rc = nurb->IsEllipse(nullptr, &ellipse, tolerance);
          if (rc)
          {
            // Center
            ON_3dPoint origin = ellipse.plane.origin;
    
            // Major and minor axes
            ON_3dVector xaxis = ellipse.radius[0] * ellipse.plane.xaxis;
            ON_3dVector yaxis = ellipse.radius[1] * ellipse.plane.yaxis;
    
            // Quad points
            ON_3dPoint p0(origin - xaxis);
            ON_3dPoint p1(origin + xaxis);
            ON_3dPoint p2(origin - yaxis);
            ON_3dPoint p3(origin + yaxis);
    
            // Foci
            ON_3dPoint f1, f2;
            ellipse.GetFoci(f1, f2);
    
            // TODO: do something with ellipse
          }
        }
      }
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/opennurbs/data-
from-ellipses/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/opennurbs/data-
from-ellipses/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

