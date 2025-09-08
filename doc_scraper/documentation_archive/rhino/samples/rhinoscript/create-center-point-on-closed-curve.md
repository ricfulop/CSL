---
url: https://developer.rhino3d.com/samples/rhinoscript/create-center-point-on-closed-curve/
scraped_at: 2025-09-08T15:48:55.895519
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

Create Center Point on Closed Curve

__

Windows only

Demonstrates how to mark the center points of closed planar curves with a
point object using RhinoScript.

VBScript

    
    
    Sub MarkCenterPoints()
      Dim curves, crv, pt, arr
      curves = Rhino.GetObjects("Select closed planar curves", 4, ,True)
      If IsArray(curves) Then
        Rhino.EnableRedraw False
        For Each crv In curves
          pt = vbNull
          If Rhino.IsCircle(crv) Then
            pt = Rhino.CircleCenterPoint(crv)
          Else
            arr = Rhino.CurveAreaCentroid(crv)
            If IsArray(arr) Then pt = arr(0)
          End If
          If IsArray(pt) Then
            Rhino.SelectObject Rhino.AddPoint(pt)
          End If
        Next        
        Rhino.EnableRedraw True
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

