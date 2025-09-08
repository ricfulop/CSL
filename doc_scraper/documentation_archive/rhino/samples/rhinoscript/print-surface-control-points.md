---
url: https://developer.rhino3d.com/samples/rhinoscript/print-surface-control-points/
scraped_at: 2025-09-08T15:49:44.098796
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

Print Surface Control Points

__

Windows only

Demonstrates how to print the location of a surface's control points using
RhinoScript.

VBScript

    
    
    Option Explicit
    
    Sub PrintSurfacePoints
    
    Dim strSurface
    strSurface = Rhino.GetObject("Select surface", 8)
    If IsNull(strSurface) Then Exit Sub  
    
    Dim arrPoints
    arrPoints = Rhino.SurfacePoints(strSurface)
    If Not IsArray(arrPoints) Then Exit Sub
    
    Dim arrCount
    arrCount = Rhino.SurfacePointCount(strSurface)
    
    Dim u, v
    Dim ulast : ulast = arrCount(0)
    Dim vlast : vlast = arrCount(1)
    Dim i : i = 0
    
    For u = 0 To ulast - 1
      For v = 0 To vlast - 1
        Rhino.Print "CV[" & CStr(u) & "," & CStr(v) & "] = " _
              & Rhino.Pt2Str(arrPoints(i), 3)
        i = i + 1
      Next
    Next
    
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

