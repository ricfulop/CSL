---
url: https://developer.rhino3d.com/samples/rhinoscript/random-surface-points/
scraped_at: 2025-09-08T15:49:03.941509
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

Random Surface Points

__

Windows only

Generate random points on a surface using RhinoScript.

VBScript

    
    
    Sub RandomSurfacePoints()
    
      Dim srf, num, cnt
      Dim dom_u, dom_v, uv(1), pt
    
      srf = Rhino.GetObject("Select surface", 8, True, True)
      If IsNull(srf) Then Exit Sub
    
      num = Rhino.GetInteger("Number of points", 10, 1)
      If IsNull(num) Then Exit Sub
    
      Call Rhino.EnableRedraw(False)
    
      Randomize
      dom_u = Rhino.SurfaceDomain(srf, 0)
      dom_v = Rhino.SurfaceDomain(srf, 1)
      cnt = 0
    
      While (cnt < num)
        uv(0) = Rnd() * (dom_u(1) - dom_u(0)) + dom_u(0)
        uv(1) = Rnd() * (dom_v(1) - dom_v(0)) + dom_v(0)
        pt = Rhino.EvaluateSurface(srf, uv)
        If (Rhino.IsPointOnSurface(srf, pt) = True) Then
          Call Rhino.AddPoint(pt)
          cnt = cnt + 1
        End If
      Wend
    
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

