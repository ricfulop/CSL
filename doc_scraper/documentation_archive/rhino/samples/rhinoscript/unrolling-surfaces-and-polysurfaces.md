---
url: https://developer.rhino3d.com/samples/rhinoscript/unrolling-surfaces-and-polysurfaces/
scraped_at: 2025-09-08T15:49:47.218922
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

Unrolling Surfaces and Polysurfaces

__

Windows only

Demonstrates how to unroll surfaces and polysurfaces using RhinoScript.

VBScript

    
    
    ' Description:
    '   Unroll a surface or polysurface.
    ' Parameters:
    '   strSurface - String, The identifier of the surface or polysurface to unroll.
    '   arrCurves  - Array, The identifiers of one or more curves to unroll.
    '   blnExplode - Boolean, Explode the resulting objects.
    '   blnLabels  - Boolean, Label the resulting objects with numbered dots.
    ' Returns:
    '   Array, The identifiers of the unrolled objects if successful.
    '   Null on error
    
    Option Explicit
    
    Function RhinoUnrollSurface(strSurface, arrCurves, blnExplode, blnLabels)
    
      ' Default return value  
      RhinoUnrollSurface = Null
    
      ' For speed, turn of screen redrawing
      Call Rhino.EnableRedraw(False)
    
      ' Save any selected objects
      Dim arrSaved : arrSaved = Rhino.SelectedObjects
    
      ' Unselect all objects
      Rhino.UnSelectAllObjects
    
      ' Select the surface to unroll
      Rhino.SelectObject strSurface
    
      ' Format curve string
      Dim i : i = 0
      Dim strCurves
      If IsArray(arrCurves) Then
        For i = 0 To UBound(arrCurves)
          strCurves = strCurves & " _SelId " & arrCurves(i)
        Next
        strCurves = strCurves & " _Enter"
      End If
    
      ' Format explode string
      Dim strExplode : strExplode = " _Explode=_Yes"
      If (blnExplode = False) Then strExplode = " _Explode=_No"
    
      ' Format labels string
      Dim strLabels : strLabels = " _Labels=_No"
      If (blnLabels = True) Then strLabels = " _Labels=_Yes"
    
     ' Script the command
      Dim strCommand : strCommand = "_-UnrollSrf" & strExplode & strLabels & strCurves
      Call Rhino.Command(strCommand, 0)
    
      ' Return the results
      RhinoUnrollSurface = Rhino.LastCreatedObjects
    
      ' Unselect all objects
      Rhino.UnSelectAllObjects
    
      ' If any objects were selected before calling
      ' this function, re-select them
      If IsArray(arrSaved) Then Rhino.SelectObjects(arrSaved)
    
      ' Don't forget to turn redrawing back on
      Call Rhino.EnableRedraw(True)
    
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

