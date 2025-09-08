---
url: https://developer.rhino3d.com/samples/rhinoscript/find-closest-curve-to-point/
scraped_at: 2025-09-08T15:49:18.021145
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

Find Closest Curve to Point

__

Windows only

Demonstrates how to find the closest curve to test point using RhinoScript.

VBScript

    
    
    Sub FindClosestCurve
    
      Const rhPoint = 1
      Const rhCurve = 4
    
      'Dim arrCurves : arrCurves = Rhino.ObjectsByType(rhCurve)
      Dim arrCurves: arrCurves = Rhino.GetObjects("Select curves to test", rhCurve)
      If Not IsArray(arrCurves) Then Exit Sub
    
      Dim strPoint : strPoint = Rhino.GetObject("Select test point", rhPoint)
      If IsNull(strPoint) Then Exit Sub
    
      Dim arrPoint : arrPoint = Rhino.PointCoordinates(strPoint)
    
      Dim dblDistance : dblDistance = Null
      Dim strCurve : strCurve = Null
      Dim dblParameter : dblParameter = Null
      Dim arrPt : arrPt = Null
    
      Dim i, b, t, pt, d
      For i = 0 To UBound(arrCurves)
        b = vbFalse
        t = Rhino.CurveClosestPoint( arrCurves(i), arrPoint )
        If Not IsNull(t) Then
          pt = Rhino.EvaluateCurve( arrCurves(i), t )
          If IsArray(pt) Then
            d = Rhino.Distance(pt, arrPoint)
            If IsNull(dblDistance) Then
              b = vbTrue
            ElseIf (d < dblDistance) Then
              b = vbTrue
            End If
    
            If (b = vbTrue) Then
              dblDistance = d
              strCurve = arrCurves(i)
              dblParameter = t
              arrPt = pt
            End If
          End If
        End If
      Next
    
      If Not IsNull(dblDistance) Then
        Rhino.Print "Closest curve = " & CStr(strCurve)
        Rhino.Print "Curve parameter = " & CStr(dblParameter)
        Rhino.Print "Point = " & Rhino.Pt2Str(arrPt)
        Rhino.Print "Distance = " & CStr(dblDistance)
    
        Rhino.SelectObject strCurve
        Rhino.SelectObject Rhino.AddPoint(arrPt)
      End If
    
    End Sub
    

  

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

