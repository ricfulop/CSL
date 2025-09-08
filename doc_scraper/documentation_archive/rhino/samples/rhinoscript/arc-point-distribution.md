---
url: https://developer.rhino3d.com/samples/rhinoscript/arc-point-distribution/
scraped_at: 2025-09-08T15:50:04.181077
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

Arc Point Distribution

__

Windows only

Demonstrates arc point distribution.

VBScript

    
    
    Option Explicit
    
    Sub ArcPointDistribution
       ' Local variables
       Dim arc, cnt, rads
       Dim n_t(), n, i, a0, a1
       Dim line, dom, t
    
       ' Select arc curve  
       arc = Rhino.GetObject("Select arc", 4)
       If IsNull(arc) Then Exit Sub
       If Not Rhino.IsArc(arc) Then Exit Sub
    
       ' Get number of points to calculate
       cnt = Rhino.GetInteger("Number of points", 2)
       If IsNull(cnt) Then Exit Sub   
    
       rads = Rhino.ToRadians(Rhino.ArcAngle(arc))
       n = cnt - 1
       ReDim n_t(n)
    
       ' Calculate normalized parameters
       For i = 0 To n
         a0 = Sin(rads/2)
         a1 = Sin(i*rads/n - rads/2)
         n_t(i) = (a0+a1)/(2*a0)
       Next
    
       Rhino.EnableRedraw False
    
       line = Rhino.AddLine(Rhino.CurveStartPoint(arc), Rhino.CurveEndPoint(arc))
       dom = Rhino.CurveDomain(line)
    
       For i = 0 To n
         ' Convert normalized parameter to domain value
         t = (1.0 - n_t(i)) * dom(0) + n_t(i) * dom(1)
         Rhino.AddPoint Rhino.EvaluateCurve(line, t)
       Next
    
       Rhino.EnableRedraw True
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

