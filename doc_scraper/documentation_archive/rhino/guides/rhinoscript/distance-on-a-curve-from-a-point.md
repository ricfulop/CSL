---
url: https://developer.rhino3d.com/guides/rhinoscript/distance-on-a-curve-from-a-point/
scraped_at: 2025-09-08T15:42:42.251259
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

[Distance on a Curve from a
Point](https://developer.rhino3d.com/guides/rhinoscript/distance-on-a-curve-
from-a-point/)

  * Problem
  * Solution

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Distance on a Curve from a Point

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

How do you create a point that is a given distance from another point, where
the distance is to be measured along the curve?

## Solution

The problem can be easily solved by using RhinoScript’s `CurveArcLengthPoint`
function. The `CurveArcLengthPoint` function returns the point on the curve
that is a specified arc length from the start of the curve. By first
determining the distance of the known point from the start of the curve, you
can then determine how far to offset another point.

For example:

    
    
    Option Explicit
    
    Sub OffsetPointOnCurve
    
      ' Select the curve
      Dim crv : crv = Rhino.GetObject("Select curve", 4)
      If IsNull(crv) Then Exit Sub
    
      ' Select a point on the curve to offset from      
      Dim pt : pt = Rhino.GetPointOnCurve(crv, "Select point on curve")
      If IsNull( pt) Then Exit Sub
    
      ' Specify the offset distance    
      Dim dist : dist = Rhino.GetReal("Distance to offset point")
      If IsNull(dist) Then Exit Sub
    
      ' Get the closest point on the curve from the test point      
      Dim t : t = Rhino.CurveClosestPoint(crv, pt)
    
      ' Get the curve's domain
      Dim d : dom = Rhino.CurveDomain(crv)
    
      ' Get the total length of the curve
      Dim l : l = Rhino.CurveLength(crv)
    
      ' Determine the length from the start of the curve to the test point
      Dim ls : ls = Rhino.CurveLength(crv,,Array(Dom(0),t))
    
      ' Offset a point in each direction    
      Rhino.AddPoint Rhino.CurveArcLengthPoint(crv, ls + dist, True)
      Rhino.AddPoint Rhino.CurveArcLengthPoint(crv, l - ls + dist, False)
    
      ' Add the test point for reference
      Rhino.AddPoint pt
    
    End Sub
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/distance-
on-a-curve-from-a-point/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/distance-
on-a-curve-from-a-point/index.md) [
Admin](https://developer.rhino3d.com/admin)

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

