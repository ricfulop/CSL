---
url: https://developer.rhino3d.com/samples/rhinoscript/array-points-on-surface/
scraped_at: 2025-09-08T15:48:49.871540
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

Array Points on Surface

__

Windows only

Demonstrates how to array points on a surface with a RhinoScript.

VBScript

    
    
    Option Explicit
    
    Sub ArrayPointsOnSurface()
       ' Get the surface object
       Dim srf : srf = Rhino.GetObject("Select surface", 8, vbTrue)
       If IsNull(srf) Then Exit Sub
    
       ' Get the number of rows
       Dim rows : rows = Rhino.GetInteger("Number of rows", 2, 2)
       If IsNull(rows) Then Exit Sub
       rows = rows - 1
    
       ' Get the number of columns
       Dim cols : cols = Rhino.GetInteger("Number of columns", 2, 2)
       If IsNull(cols) Then Exit Sub
       cols = cols - 1
    
       ' Get the domain of the surface
       Dim U : U = Rhino.SurfaceDomain(srf, 0)
       Dim V : V = Rhino.SurfaceDomain(srf, 1)
       If Not IsArray(U) Or Not IsArray(V) Then Exit Sub
    
       ' Turn off redrawing (faster)
       Rhino.EnableRedraw vbFalse
    
       ' Add the points
       Dim i, j, t(1), pt, obj
       For i = 0 To rows
         t(0) = U(0) + (((U(1) - U(0)) / rows) * i)
         For j = 0 To cols
           t(1) = V(0) + (((V(1) - V(0)) / cols) * j)
           pt = Rhino.EvaluateSurface(srf, t)
           If IsArray(pt) Then
             obj = Rhino.AddPoint(pt) ' add the point
             Rhino.SelectObject obj   ' select the point
           End If
         Next
       Next
    
       ' Turn on redrawing
       Rhino.EnableRedraw vbTrue
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

