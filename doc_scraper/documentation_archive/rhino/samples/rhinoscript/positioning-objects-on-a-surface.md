---
url: https://developer.rhino3d.com/samples/rhinoscript/positioning-objects-on-a-surface/
scraped_at: 2025-09-08T15:49:43.130196
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

Positioning Objects on a Surface

__

Windows only

Demonstrates how to positioning objects on a surface using RhinoScript.

VBScript

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' PositionOnSrf.rvb -- February 2009
    ' If this code works, it was written by Dale Fugier.
    ' If not, I don't know who wrote it.
    ' Works with Rhino 4.0.
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Option Explicit
    
    Sub PositionOnSrf
    
      Dim objs, srf, box, p0, p1, pt, arr, i
    
      objs = Rhino.GetObjects("Select objects to position on surface")
      If IsNull(objs) Then Exit Sub
    
      srf = Rhino.GetObject("Select surface", 8)
      If IsNull(srf) Then Exit Sub
    
      Rhino.EnableRedraw False
    
      For i = 0 To UBound(objs)
        box = Rhino.BoundingBox(objs(i))
        If IsArray(box) Then
          p0 = box(0)
          p1 = box(2)
          pt = Array((p1(0)+p0(0))/2,(p1(1)+p0(1))/2,(p1(2)+p0(2))/2)
          arr = Rhino.ProjectPointToSurface(pt, srf, Array(0,0,1))
          If IsArray(arr) Then
            Rhino.MoveObject objs(i), pt, arr(0)
          End If
        End If
      Next
    
      Rhino.EnableRedraw True
    
    End Sub
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    Rhino.AddStartupScript Rhino.LastLoadedScriptFile
    Rhino.AddAlias "PositionOnSrf", "_NoEcho _-RunScript (PositionOnSrf)"
    

  

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

