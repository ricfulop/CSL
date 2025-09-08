---
url: https://developer.rhino3d.com/guides/rhinoscript/curve-osculating-planes/
scraped_at: 2025-09-08T15:42:40.246890
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

[Curve Osculating
Planes](https://developer.rhino3d.com/guides/rhinoscript/curve-osculating-
planes/)

  * Problem
  * Solution

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Curve Osculating Planes

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

Is it possible to calculate the osculating plane at point $$P$$ on a given
curve with the methods provided by RhinoScript?

## Solution

Yes. There are a number of methods included in RhinoScript that can be used to
calculate a curve’s osculating plane, such as `CurveClosestPoint`,
`CurveTangent`, `CurveCurvature`, and `CurveEvaluate`. In this example, we
will use the `CurveEvaluate` function to calculate the 2nd derivative of a
curve at a parameter…

    
    
    Function CurveOsculatingPlane(crv, t)
      CurveOsculatingPlane = Null ' default return value
      If Not Rhino.IsCurveLinear(crv) Then
        Dim rc : rc = Rhino.CurveEvaluate(crv, t, 2)
        If IsArray(rc) Then
          CurveOsculatingPlane = Rhino.PlaneFromFrame(rc(0), rc(1), rc(2))
        End If
      End If
    End Function
    

The following is an example of how you might use this function…

    
    
    Sub TestCurveOsculatingPlane
      Dim segs : segs = 10
      Dim crv : crv = Rhino.GetObject("Select non-linear curve", 4)
      If Not IsNull(crv) Then
        Dim pts : pts = Rhino.DivideCurve(crv, segs)
        If IsArray(pts) Then
          Dim i, t, p
          For i = 0 To UBound(pts)
            t = Rhino.CurveClosestPoint(crv, pts(i))
            p = CurveOsculatingPlane(crv, t)
            Rhino.AddPlaneSurface p, 1.0, 1.0
          Next
        End If
      End If
    End Sub
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/curve-
osculating-planes/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/curve-
osculating-planes/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

