---
url: https://developer.rhino3d.com/samples/rhinoscript/list-knot-vector-of-nurbs-curve/
scraped_at: 2025-09-08T15:49:21.020685
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

List Knot Vector of NURBS Curve

__

Windows only

Demonstrates how to print the knot vector of NURBS curve using RhinoScript.

VBScript

    
    
    Option Explicit
    
    Sub ListKnotVector
    
      Dim curve : curve = Rhino.GetObject("Select curve", 4)
      If IsNull(curve) Then Exit Sub
    
      Dim knot : knot = Rhino.CurveKnots(curve)
      If Not IsArray(knot) Then
        Rhino.Print "NULL knot vector"
      End If
    
      ' order = degree + 1
      Dim order : order = Rhino.CurveDegree(curve) + 1
      If (order < 2) Then
        Rhino.Print "knot vector order < 2"
      End If
    
      Dim cv_count : cv_count = Rhino.CurvePointCount(curve)
      If (cv_count < order) Then
        Rhino.Print "knot vector cv_count < order"
      End If
    
      Dim knot_count, i, i0, mult
      If (order >= 2) And (cv_count >= order) And IsArray(knot) Then
        knot_count = order + cv_count - 2
        i = 0
        i0 = 0
        Rhino.Print "index, value, mult, delta"
        While (i < knot_count)
          mult = 1
          Do While (i + mult < knot_count)
            If (i + mult < knot_count) Then
              If (knot(i) = knot(i+mult)) Then
                mult = mult + 1
              Else
                Exit Do
              End If
            Else
              Exit Do
            End If
          Loop
          If (i = 0) Then
            Rhino.Print CStr(i) & ", " & CStr(knot(i)) & ", " & CStr(mult)
          Else
            Rhino.Print CStr(i) & ", " & CStr(knot(i)) & ", " & CStr(mult) & ", " & CStr(knot(i)-knot(i0))
          End If
          i0 = i
          i = i + mult
        Wend
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

