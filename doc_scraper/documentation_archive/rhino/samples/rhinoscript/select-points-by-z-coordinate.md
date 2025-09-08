---
url: https://developer.rhino3d.com/samples/rhinoscript/select-points-by-z-coordinate/
scraped_at: 2025-09-08T15:49:38.081879
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

Select Points by Z Coordinate

__

Windows only

Demonstrates how to select point objects with a user-specified z coordinate
using RhinoScript.

VBScript

    
    
    Option Explicit
    
    Sub SelZ()
    
      Dim arr
      arr = Rhino.ObjectsByType(1)
      If Not IsArray(arr) Then
        Rhino.Print "No point objects to select"
        Exit Sub
      End If
    
      Const zero_tol = 1.0e-12
    
      Dim z, obj, pt
      z = Rhino.GetReal("Z coordinate", 0.0)
      If IsNumeric(z) Then
        For Each obj In arr
          pt = Rhino.PointCoordinates(obj)
          If IsArray(pt) Then
            If Abs(pt(2)-z) <= zero_tol Then
              Rhino.SelectObject obj
            End If
          End If
        Next
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

