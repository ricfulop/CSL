---
url: https://developer.rhino3d.com/guides/cpp/adding-curve-objects/
scraped_at: 2025-09-08T15:38:39.338264
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

[Adding Curve Objects](https://developer.rhino3d.com/guides/cpp/adding-curve-
objects/)

  * Overview
  * Examples
    * Example 1
    * Example 2
    * Example 3
  * Discussion

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Adding Curve Objects

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

Curve objects can be added to Rhino by using the following functions found on
`CRhinoDoc`:

  1. `CRhinoDoc::AddCurveObject`
  2. `CRhinoDoc::AddObject`

For `CRhinoDoc::AddCurveObject`, there are six overridden versions that will
make curve objects from a variety of inputs, including:

  1. `ON_Line`: line definition objects
  2. `ON_Polyline`: polyline definition objects
  3. `ON_Arc`: arc definition objects
  4. `ON_Circle`: circle definition objects
  5. `ON_BezierCurve`: bezier curve objects
  6. `ON_Curve`: `ON_Curve`-derived curve objects

## Examples

The following code samples will demonstrate three different ways of adding
curves to Rhino. In these examples, we will create circle curves; but, there
is no reason that we could create lines, polylines, arcs or any other type of
curve.

### Example 1

In this example, we define a circle, using `ON_Circle`, and pass the
definition off to `CRhinoDoc::AddCurveObject`.

    
    
    ON_3dPoint center(0.0, 0.0, 0.0);
    double radius = 10.0;
    
    ON_Circle circle( center, radius );
    
    CRhinoCurveObject* curve_object = context.m_doc.AddCurveObject( circle );
    context.m_doc.Redraw();
    

### Example 2

In this example, we first define a circle. Then we create an `ON_ArcCurve`
object from the circle definition. `ON_ArcCurve` is one of the many curve
classes this is derived from `ON_Curve`. We then pass the `ON_ArcCurve` object
off to `CRhinoDoc::AddCurveObject`.

    
    
    ON_3dPoint center(0, 0, 0);
    double radius = 10.0;
    
    ON_Circle circle( center, radius );
    
    ON_ArcCurve arc_curve( circle );
    
    CRhinoCurveObject* curve_object = context.m_doc.AddCurveObject( arc_curve );
    context.m_doc.Redraw();
    

### Example 3

In this example, we will add a circle curve the brute force way. We first
define a circle. Then we allocate a new `ON_ArcCurve` and pass the circle
definition to its constructor. We then allocate a new `CRhinoCurveObject` and
assign our `ON_ArcCurve` object pointer to it. Finally, we pass the pointer to
the `CRhinoCurveObject` to `CRhinoDoc::AddObject`.

    
    
    ON_3dPoint center(0.0, 0.0, 0.0);
    double radius = 10.0;
    
    ON_Circle circle( center, radius );
    
    ON_ArcCurve* arc_curve = new ON_ArcCurve( circle );
    if( arc_curve )
    {
      CRhinoCurveObject* curve_object = new CRhinoCurveObject();
      if( curve_object )
      {
        // Set the curve to the curve object. Note,
        // curve_object will delete arc_curve.
        curve_object->SetCurve( arc_curve );
        if( context.m_doc.AddObject(curve_object) )
          context.m_doc.Redraw();
        else
          delete curve_object;
      }
    }
    

## Discussion

What is interesting to note is that the code found in [Example
3](https://developer.rhino3d.com/guides/cpp/adding-curve-objects/#example-3)
is essentially what Rhino does inside of `CRhinoDoc::AddCurveObject`. All of
the `CRhinoDoc::AddCurveObject` overrides are simply provided to make it
easier for SDK developers to add curves to Rhino.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/adding-
curve-objects/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/adding-
curve-objects/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

