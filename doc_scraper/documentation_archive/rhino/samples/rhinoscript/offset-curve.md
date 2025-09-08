---
url: https://developer.rhino3d.com/samples/rhinoscript/offset-curve/
scraped_at: 2025-09-08T15:49:23.021414
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

Offset Curve

__

Windows only

Demonstrates how to offset a curve inside or outside using RhinoScript.

VBScript

    
    
    ' Description:
    '   Offsets a closed planar curve inside or outside.
    ' Parameters:
    '   strSurface  - String, The identifier of the closed planar curve to offset.
    '   dblDistance - Number, The distance to offset.
    '   blnOutside  - Boolean, Offset outside (true) or inside (false).
    ' Returns:
    '   Array, An array containing the identifiers of the new objects if successful.
    '   Null on error
    
    Option Explicit
    
    Function RhinoOffsetClosedPlanarCurve(ByVal strCurve, ByVal dblDistance, ByVal blnOutside)
    
      ' Local variables
      Dim arrPlane, arrOldPlane, strView, arrBox, arrPoint
    
      ' Default return value
      RhinoOffsetClosedPlanarCurve = Null
    
      ' Quick parameter validation
      If (VarType(strCurve) <> vbString) Then Exit Function
      If Not IsNumeric(dblDistance) Then Exit Function
      If (VarType(blnOutside) <> vbBoolean) Then Exit Function
    
      ' Curve validation
      If (Rhino.IsCurve(strCurve) = False) Then Exit Function
      If (Rhino.IsCurveClosed(strCurve) = False) Then Exit Function
      arrPlane = Rhino.CurvePlane(strCurve)
      If Not IsArray(arrPlane) Then Exit Function
    
      ' Calculate plane-based bounding box
      strView = Rhino.CurrentView()
      arrOldPlane = Rhino.ViewCPlane(strView, arrPlane)
      arrBox = Rhino.BoundingBox(strCurve, strView)
      Call Rhino.ViewCPlane(strView, arrOldPlane)
    
      ' Offset point so its outside of bounding box
      arrPoint = Rhino.PointAdd(arrBox(0), Rhino.VectorCreate(arrBox(0), arrBox(2)))
    
      ' Offset the curve
      If (blnOutside = False) Then dblDistance = -dblDistance
      RhinoOffsetClosedPlanarCurve = Rhino.OffsetCurve(strCurve, arrPoint, dblDistance, arrPlane(3))
    
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

