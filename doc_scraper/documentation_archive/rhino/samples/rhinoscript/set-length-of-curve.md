---
url: https://developer.rhino3d.com/samples/rhinoscript/set-length-of-curve/
scraped_at: 2025-09-08T15:49:25.023177
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

Set Length of Curve

__

Windows only

Demonstrates how to set the length of a curve object using RhinoScript.

VBScript

    
    
    Option Explicit
    
    Sub SetCrvLength
    
      Dim crv, lold, lnew, dom, pts, t
    
      crv = Rhino.GetCurveObject("Select curve to set length", 4, True)
      If Not IsArray(crv) Then Exit Sub
    
      If Rhino.IsCurveClosed(crv(0)) Then
        Rhino.Print "Cannot set the length of closed curves."
        Exit Sub
      End If
    
      lold = Rhino.CurveLength(crv(0))
      lnew = Rhino.GetReal("New curve length", lold, 0.0, lold)
      If Not IsNumeric(lnew) Then Exit Sub
      If (lnew <= 0) Or (lnew >= lold) Then Exit Sub
    
      dom = Rhino.CurveDomain(crv(0))
      If (dom(1)-crv(4)) < (crv(4)-dom(0)) Then
        Rhino.ReverseCurve crv(0)
        dom = Rhino.CurveDomain(crv(0))
      End If
    
      pts = Rhino.DivideCurveLength(crv(0), lnew)
      t = Rhino.CurveClosestPoint(crv(0), pts(1))
      Rhino.TrimCurve crv(0), Array(dom(0), t), True
    
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

