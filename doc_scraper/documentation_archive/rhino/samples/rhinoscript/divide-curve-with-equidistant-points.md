---
url: https://developer.rhino3d.com/samples/rhinoscript/divide-curve-with-equidistant-points/
scraped_at: 2025-09-08T15:49:13.000303
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

Divide Curve With Equidistant Points

__

Windows only

Demonstrates equidistance curve division using RhinoScript.

VBScript

    
    
    Option Explicit
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' ''''''''''  
    ' Description
    '   Divides a curve based on the linear distance between points.
    '
    Sub DivideCurveEquiDistant
    
      Dim crv
      crv = Rhino.GetObject("Select curve to divide", 4, True)
      If IsNull(crv) Then Exit Sub
    
      Dim crv_length
      crv_length = Rhino.CurveLength(crv)
    
      Dim length
      length = Rhino.GetReal("Curve length is " & CStr(crv_length) & ". Division length", 1.0)
      If Not IsNumeric(length) Then Exit Sub
    
      If (crv_length < length) Then
        Rhino.Print "Specified divison length exceeds curve length."
        Exit Sub
      End If    
    
      Rhino.EnableRedraw False  
    
      Dim dom, t, pt
      dom = Rhino.CurveDomain(crv)
      t = dom(0)
      pt = Rhino.EvaluateCurve(crv, t)
      Rhino.AddPoint pt
    
      Dim bDone: bDone = False
      While (bDone = False)
        t = EquiDistantParameter(crv, t, length)
        If IsNull(t) Then
          bDone = True
        Else
          pt = Rhino.EvaluateCurve(crv, t)
          Rhino.AddPoint pt
        End If
      Wend
    
      Rhino.EnableRedraw True
    
    End Sub
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Description
    '   Finds the parameter on a curve that is a specified
    '   linear distance from a known parameter.
    '
    Function EquiDistantParameter(crv, t, length)
    
      EquiDistantParameter = Null
    
      Dim pt
      pt = Rhino.EvaluateCurve(crv, t)
    
      Dim sphere
      sphere = Rhino.AddSphere(pt, length)
    
      Dim csx
      csx = Rhino.CurveSurfaceIntersection(crv, sphere)
    
      Rhino.DeleteObject sphere
      If Not IsArray(csx) Then Exit Function
    
      Dim i
      For i = 0 To UBound(csx)
        If csx(i,0) = 1 Then
          If (csx(i,5) > t) Then
            EquiDistantParameter = csx(i,5)
            Exit Function
          End If
        End If
      Next
    
    End Function
    

  

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

