---
url: https://developer.rhino3d.com/samples/rhinoscript/set-camera-angle/
scraped_at: 2025-09-08T15:49:49.131859
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

Set Camera Angle

__

Windows only

Demonstrates how to set the camera angle using RhinoScript.

VBScript

    
    
    Sub TestSetCameraAngle()
    
      ' Local constants (could easily prompt for these...)
      Const horz_angle = 7.3
      Const vert_angle = 5.5
      Const horz_res = 1200
    
      ' Local variables
      Dim view, vert_res
    
      ' Current view must be a perspective view
      view = Rhino.CurrentView()
      If Not Rhino.IsViewPerspective(view) Then
        Call Rhino.Print("Select a perspective view and rerun the script.")
        Exit Sub
      End If
    
      ' Calculate vertical resolution based on existing parameters    
      vert_res = CInt(Round((vert_angle * 2) / (horz_angle * 2) * horz_res))
    
      ' Set the viewport size
      Call Rhino.Command("_-ViewportProperties _Size " & CStr(horz_res) & " " & CStr(vert_res) & " _Enter _Enter", 0)
    
      ' Set the viewing angle
      If (horz_res < vert_res) Then
        Call Rhino.Command("_-PerspectiveAngle " & CStr(horz_angle), 0)
      Else
        Call Rhino.Command("_-PerspectiveAngle " & CStr(vert_angle), 0)
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

