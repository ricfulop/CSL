---
url: https://developer.rhino3d.com/samples/rhinoscript/trim-curve-with-circle/
scraped_at: 2025-09-08T15:49:28.030885
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

Trim Curve with Circle

__

Windows only

Demonstrates how to trim a closed curve with a circle using RhinoScript.

VBScript

    
    
    Option Explicit
    
    Sub CircleTrimmer
    
      ' Local variable declarations
      Dim curve, circle, ccx, ccx_t(1), interval
    
      ' Select closed curve to split
      curve = Rhino.GetObject("Select closed curve to split", 4)
      If IsNull(curve) Then Exit Sub
      If Not Rhino.IsCurveClosed(curve) Then Exit Sub
    
      ' Select circle to split with    
      circle = Rhino.GetObject("Select circle to split with", 4)
      If IsNull(circle) Then Exit Sub
      If Not Rhino.IsCircle(circle) Then Exit Sub
    
      ' Intersect the two curves
      ccx = Rhino.CurveCurveIntersection(curve, circle)
      If IsNull(ccx) Then
        Rhino.Print "Curve and circle do not intersect"
        Exit Sub
      End If
    
      ' Make sure there are only two intersection events
      If UBound(ccx) <> 1 Then
        Rhino.Print "Unable to split curve"
        Exit Sub
      End If
    
      ' Get two intersection parameters on the curve
      ccx_t(0) = ccx(0,5)
      ccx_t(1) = ccx(1,5)
    
      ' If the input curve is closed and the interval is decreasing,
      ' then the portion of the curve across the start and end of the
      ' curve is returned.
      If ccx_t(0) < ccx_t(1) Then
        interval = Array(ccx_t(1), ccx_t(0))
      Else
        interval = Array(ccx_t(0), ccx_t(1))
      End If
    
      ' Trim the curve
      Rhino.TrimCurve curve, interval
    
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

