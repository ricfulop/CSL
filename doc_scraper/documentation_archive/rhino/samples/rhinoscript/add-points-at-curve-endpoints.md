---
url: https://developer.rhino3d.com/samples/rhinoscript/add-points-at-curve-endpoints/
scraped_at: 2025-09-08T15:48:48.746079
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

Add Points at Curve Endpoints

__

Windows only

Demonstrates how to add point at the starting and ending locations of curves.

VBScript

    
    
    Option Explicit
    
    Sub AddCurveEndPoints()
      Const rhCurve = 4
    
      ' Get all the curve objects in the document
      Dim arrCurves
      arrCurves = Rhino.ObjectsByType(rhCurve)
      If IsNull(arrCurves) Then Exit Sub
    
      ' For better performance, turn off screen redrawing  
      Call Rhino.EnableRedraw(False)
    
      ' Process each curve       
      Dim strCurve
      For Each strCurve In arrCurves
        ' Add a point at the start of the curve
        Call Rhino.AddPoint(Rhino.CurveStartPoint(strCurve))
        ' If not closed, add a point at the end of the curve
        If Not Rhino.IsCurveClosed(strCurve) Then
          Call Rhino.AddPoint(Rhino.CurveEndPoint(strCurve))
        End If
      Next
    
      ' Turn screen redrawing back on  
      Call Rhino.EnableRedraw(True)
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

