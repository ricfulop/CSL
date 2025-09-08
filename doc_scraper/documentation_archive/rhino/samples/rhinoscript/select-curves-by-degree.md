---
url: https://developer.rhino3d.com/samples/rhinoscript/select-curves-by-degree/
scraped_at: 2025-09-08T15:49:24.015659
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

Select Curves by Degree

__

Windows only

Demonstrates how to use RhinoScript to select all curves that are of a
specified degree.

VBScript

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' SelCrvDegree.rvb -- September 2011
    ' If this code works, it was written by Dale Fugier.
    ' If not, I don't know who wrote it.
    ' Works with Rhino 4.0.
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    Option Explicit
    
    ' Declare global variable
    Public g__nDegree
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Selects curves of a user-specified degree
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub SelCrvDegree
    
      ' Declare local constants
      Const RH_CURVE = 4
      Const RH_MAX_DEGREE = 11
      Const RH_DEF_DEGREE = 3
    
      ' Declare local variables
      Dim nDegree, arrCurves, strCurve, nCount
    
      ' Make sure global variable is initialized
      If IsEmpty(g__nDegree) Or IsNull(g__nDegree) Then g__nDegree = RH_DEF_DEGREE
      nDegree = g__nDegree
    
      ' Get all curve objects
      Call Rhino.EnableRedraw(False)    
      arrCurves = Rhino.ObjectsByType(RH_CURVE)
      If IsNull(arrCurves) Then
        Call Rhino.Print("No curves to select.")
        Exit Sub
      End If
    
      ' Prompt for curve degree
      nDegree = Rhino.GetInteger("Degree of curves to select", nDegree, 1, RH_MAX_DEGREE)
      If IsNull(nDegree) Then Exit Sub
    
      ' Select curves of specified degree
      Call Rhino.EnableRedraw(False)
      nCount = 0
      For Each strCurve In arrCurves
        If nDegree = Rhino.CurveDegree(strCurve) Then
          If Not Rhino.IsObjectSelected(strCurve) Then
            Call Rhino.SelectObject(strCurve)
            nCount = nCount + 1
          End If        
        End If
      Next
      Call Rhino.EnableRedraw(True)
    
      ' Print results
      If 0 = nCount Then
        Call Rhino.Print("No degree=" & CStr(nDegree) & " curves added to selection.")
      ElseIf 1 = nCount Then
        Call Rhino.Print("1 degree=" & CStr(nDegree) & " curve added to selection.")
      Else
        Call Rhino.Print(CStr(nCount) & " degree=" & CStr(nDegree) & " curves added to selection.")
      End If  
    
      ' Remember curve degree
      g__nDegree = nDegree
    
    End Sub
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Drag & drop support
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Rhino.AddStartUpScript Rhino.LastLoadedScriptFile
    Rhino.AddAlias "SelCrvDegree", "_-RunScript (SelCrvDegree)"
    

  

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

