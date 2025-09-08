---
url: https://developer.rhino3d.com/guides/rhinoscript/closest-axis-point/
scraped_at: 2025-09-08T15:42:36.354888
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

[Closest Axis Point](https://developer.rhino3d.com/guides/rhinoscript/closest-
axis-point/)

  * Problem
  * Solution

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Closest Axis Point

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You have a bunch of 2-D curves that are planar to the world x-y plane, and you
need to find a point in each curve that is closest to the world y-axis. For
example:

![Closest Axis Point](https://developer.rhino3d.com/images/closest-axis-
point-01.png)

What can you do to calculate this point?

## Solution

After selecting the curves and verifying that they are both planar and line in
the world x-y plane, calculate the world axis-aligned bounding box for each
curve. Using the results of the bounding box calculation, create a line, using
the first two points from the results, that is parallel to the world y-axis.
Intersect this line with the curve. The results of the intersection will be at
the point that is closest to the world y-axis.

The following example demonstrates the above algorithm…

    
    
    Option Explicit
    
     Sub ClosestAxisPoint
    
       Dim arrCurves
       arrCurves = Rhino.GetObjects("Select planar curves", 4, True, True)
       If Not IsArray(arrCurves) Then Exit Sub
    
       Dim strCurve, arrPlane(3), arrBox, strLine, arrCCX
       arrPlane(0) = Array(0,0,0)
       arrPlane(1) = Array(1,0,0)
       arrPlane(2) = Array(0,1,0)
       arrPlane(3) = Array(0,0,1)
    
       Rhino.EnableRedraw False
    
       For Each strCurve In arrCurves
         If Rhino.IsCurvePlanar(strCurve) Then
           If Rhino.IsCurveInPlane(strCurve, arrPlane) Then
             arrBox = Rhino.BoundingBox(strCurve)
             strLine = Rhino.AddLine(arrBox(0), arrBox(1))
             arrCCX = Rhino.CurveCurveIntersection(strCurve, strLine)
             If IsArray(arrCCX) Then
               Rhino.AddPoint arrCCX(0,1)
             End If
             Rhino.DeleteObject strLine
           End If
         End If
       Next
    
       Rhino.EnableRedraw True      
    
     End Sub
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/closest-
axis-point/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/closest-
axis-point/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

